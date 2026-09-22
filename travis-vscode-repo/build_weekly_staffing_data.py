# NRXX Peak Staffing Data Pipeline & Dashboard Builder
# FINAL PRODUCTION VERSION - Securely handles corporate SSL certificates.

import os
import re
import pandas as pd
import datetime
import webbrowser
from pathlib import Path
import http.server
import socketserver
import threading
import requests
from ssl import SSLError

# --- CONFIGURATION ---
DATA_SUBFOLDER = "data"
OUTPUT_DIRECTORY_NAME = "output"
TEMPLATE_HTML_NAME = "NRXX Staffing Dashboard.html"
SERVER_PORT = 8000
# The name of the corporate certificate bundle file your users will get from IT
CORPORATE_CERT_FILE = "corporate_certs.pem"

STATION_MAP = {
    "P895": "RENO/895", "P942": "SACL/942", "P945": "FAIR/945", "P948": "RCHM/948",
    "P949": "UKIA/949", "P954": "SROS/954", "P955": "EURK/955", "P956": "ROSV/956",
    "P957": "ESAC/957", "P950": "ESAX/950", "P958": "SACR/958", "P959": "CHCO/959",
    "P960": "REDD/960"
}
STATIONS_ORDER = [
    "NRXX Overall", "RENO/895", "SACL/942", "FAIR/945", "RCHM/948", "UKIA/949",
    "SROS/954", "EURK/955", "ROSV/956", "ESAC/957", "ESAX/950", "SACR/958",
    "CHCO/959", "REDD/960"
]

# --- Core Functions (Data processing functions are unchanged) ---
def format_hires_terms_matrix(df: pd.DataFrame) -> str:
    df['EOW'] = pd.to_datetime(df['EOW']).dt.strftime('%Y-%m-%d')
    all_dates = sorted(df['EOW'].unique())
    header_row_0 = ",".join([f'{node},,,' for node in STATIONS_ORDER]).rstrip(',')
    header_row_1 = ",".join(['EOW,Hires Count,Terms,' for _ in STATIONS_ORDER]).rstrip(',')
    data_lookup = {(str(r['Node']).strip(), str(r['EOW']).strip()): (r.get('Hires', ''), r.get('Terms', '')) for _, r in df.iterrows()}
    data_rows = []
    for dt in all_dates:
        row_cells = []
        for node in STATIONS_ORDER:
            h, t = data_lookup.get((node, dt), ('', ''))
            h_str = str(int(h)) if pd.notna(h) and h != '' else ''
            t_str = str(int(t)) if pd.notna(t) and t != '' else ''
            row_cells.extend([dt, h_str, t_str, ''])
        data_rows.append(','.join(row_cells).rstrip(','))
    return "\n".join([header_row_0, header_row_1] + data_rows)

def format_roster_actuals_matrix(df: pd.DataFrame, pht_dict: dict) -> str:
    df['EOW'] = pd.to_datetime(df['EOW']).dt.strftime('%Y-%m-%d')
    all_dates = sorted(df['EOW'].unique())
    header_row_0 = ",".join([f'{node},,,' for node in STATIONS_ORDER]).rstrip(',')
    header_row_1 = ",".join([f'PHT Count,,{pht_dict.get(node, 0)},' for node in STATIONS_ORDER]).rstrip(',')
    header_row_2 = ",".join(['EOW,Roster Need,Actual Headcount,' for _ in STATIONS_ORDER]).rstrip(',')
    data_lookup = {(str(r['Node']).strip(), str(r['EOW']).strip()): (r.get('Roster Need', ''), r.get('Actual Headcount', '')) for _, r in df.iterrows()}
    data_rows = []
    for dt in all_dates:
        row_cells = []
        for node in STATIONS_ORDER:
            need, act = data_lookup.get((node, dt), ('', ''))
            need_str = str(int(need)) if pd.notna(need) and need != '' else ''
            act_str = str(int(act)) if pd.notna(act) and act != '' else ''
            row_cells.extend([dt, need_str, act_str, ''])
        data_rows.append(','.join(row_cells).rstrip(','))
    return "\n".join([header_row_0, header_row_1, header_row_2] + data_rows)

def consolidate_from_filenames(folder_path, station_map):
    all_data = []
    if not os.path.exists(folder_path): raise FileNotFoundError(f"Data folder not found: {folder_path}")
    for filename in os.listdir(folder_path):
        if "pht_roster" in filename or "Overall" in filename: continue
        match = re.match(r"([A-Za-z0-9\s]+)_(hires|roster)\.xlsx", filename)
        if not match: continue
        station_key = match.group(1).strip()
        file_type = match.group(2)
        node_name = station_map.get(station_key)
        if not node_name: continue
        file_path = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(file_path, header=2)
            if df.empty: continue
            df['Node'] = node_name
            df['FileType'] = file_type
            all_data.append(df)
        except Exception as e: print(f"⚠️ WARNING: Could not process {filename}. Error: {e}")
    if not all_data: raise ValueError("No valid station data files were processed.")
    hires_dfs = [df for df in all_data if 'hires' in df['FileType'].unique()]
    roster_dfs = [df for df in all_data if 'roster' in df['FileType'].unique()]
    if not hires_dfs or not roster_dfs: raise ValueError("Both hires and roster files are required.")
    flat_ht_df = pd.concat(hires_dfs, ignore_index=True).rename(columns={'Hires Count': 'Hires'})
    flat_rn_df = pd.concat(roster_dfs, ignore_index=True)
    return pd.merge(flat_ht_df, flat_rn_df, on=['EOW', 'Node'], how='outer')

def create_bundled_html(hires_data, roster_data, template_path, output_path, cert_path):
    try:
        print("\nCreating bundled HTML file...")
        with open(template_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        html_content = re.sub(r"(const rawHiresTermsCSV = `)[\s\S]*?(`;)", f"\\1{hires_data}\\2", html_content, count=1, flags=re.DOTALL)
        html_content = re.sub(r"(const rawRosterNeedActualCSV = `)[\s\S]*?(`;)", f"\\1{roster_data}\\2", html_content, count=1, flags=re.DOTALL)
        print("✅ Data injected.")

        cdn_script_tags = re.findall(r'<script src="(https://cdn\..*?)"></script>', html_content)
        for url in cdn_script_tags:
            print(f"    > Downloading: {url}")
            try:
                # Try with verification first, then with corporate certs if available
                response = requests.get(url, verify=cert_path)
                response.raise_for_status()
                
                original_tag = f'<script src="{url}"></script>'
                embedded_tag = f'<script>\n// Embedded from {url}\n{response.text}\n</script>'
                html_content = html_content.replace(original_tag, embedded_tag)
                print(f"    ✅ Embedded: {os.path.basename(url)}")
            except SSLError:
                print(f"\n❌ SSL VERIFICATION FAILED. This is common on corporate networks.")
                print(f"   To fix this, ask your IT department for the 'corporate root CA certificate bundle' file.")
                print(f"   Save that file as '{CORPORATE_CERT_FILE}' in the same folder as this script and run it again.")
                print(f"   A non-bundled file will be created as a fallback.")
                break # Exit the loop and create a non-bundled file
            except requests.RequestException as e:
                print(f"    ⚠️ WARNING: Could not download {url}. The file will link to it instead. Error: {e}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"\n✅ Bundled HTML Dashboard successfully created at: {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ An error occurred during the bundling process: {e}")
        return None

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(project_dir, OUTPUT_DIRECTORY_NAME)
    data_dir = os.path.join(project_dir, DATA_SUBFOLDER)
    os.makedirs(output_dir, exist_ok=True)
    
    # Check for the corporate certificate file
    cert_file_path = os.path.join(project_dir, CORPORATE_CERT_FILE)
    if not os.path.exists(cert_file_path):
        print(f"NOTE: Corporate certificate file '{CORPORATE_CERT_FILE}' not found. Downloads will use standard SSL verification.")
        cert_file_path = True # Default to standard verification

    try:
        print("--- Running NRXX Data Pipeline (Bundler Edition) ---")
        
        pht_file_path = os.path.join(data_dir, "pht_roster.xlsx")
        pht_df = pd.read_excel(pht_file_path, header=2)
        pht_df['Station_ID'] = pht_df['WORK_LOCATION_CD'].str.extract(r'(P\d{3,4})')
        pht_counts = {STATION_MAP.get(p_id): count for p_id, count in pht_df.groupby('Station_ID').size().items() if STATION_MAP.get(p_id)}
        pht_counts["NRXX Overall"] = len(pht_df)
        print("✅ PHT counts loaded.")

        station_df = consolidate_from_filenames(data_dir, STATION_MAP)
        print(f"✅ Station data consolidation complete. Total records: {len(station_df)}")

        numeric_cols = ['Hires', 'Terms', 'Roster Need', 'Actual Headcount']
        for col in numeric_cols:
            station_df[col] = pd.to_numeric(station_df[col], errors='coerce')
        
        overall_df = station_df.groupby('EOW')[numeric_cols].sum().reset_index()
        overall_df['Node'] = 'NRXX Overall'
        
        combined_df = pd.concat([station_df, overall_df], ignore_index=True)
        print("✅ 'NRXX Overall' data calculated by summing station data.")

        hires_csv_string = format_hires_terms_matrix(combined_df)
        roster_csv_string = format_roster_actuals_matrix(combined_df, pht_counts)
        print("✅ Data transformed.")

        template_path = os.path.join(project_dir, TEMPLATE_HTML_NAME)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"NRXX_Dashboard_LATEST_{timestamp}_Bundled.html"
        output_path = os.path.join(output_dir, output_filename)
        
        final_file = create_bundled_html(hires_csv_string, roster_csv_string, template_path, output_path, cert_file_path)

        if final_file:
            print("\nOpening the self-contained dashboard file...")
            uri = Path(final_file).as_uri()
            webbrowser.open(uri)
            
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
    
    print("\n--- Script Finished ---")
