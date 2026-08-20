import csv
import win32com.client as win32
cert = "workday learning"

def draft_compliance_emails_local():
    print("🔗 Connecting to local Outlook Desktop app...")
    try:
        #Hooks directly into O365
        outlook = win32.Dispatch('outlook.application')
    except Exception as e:
        print("❌ Error connecting to Outlook. Make sure the Outlook Desktop app is open.")
        return

    print("📂 Reading extracted Workday data...")
    try:
        with open('expiring_compliance_data.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            draft_count = 0
            for row in reader:
                name = row['Employee_Name']
                cert = row['Certification']
                days = int(row['Days_Until_Expired'])
                supervisor_email = row['Supervisor_Email']
                
                #Determine urgency
                urgency = "🚨 CRITICAL ACTION REQUIRED" if days <= 3 else "⚠️ REMINDER"
                    
                #Create the email draft in the local Outlook app
                mail = outlook.CreateItem(0)  # 0 represents a new MailItem
                mail.To = supervisor_email
                mail.Subject = f"{urgency}: Compliance Expiration for {name} ({cert})"
                
                #points to the Workday Learning link
                mail.Body = f"""Hi there,

This is an automated operational alert from the FedEx Operations Agent.

Our records indicate that {name} has a training module for '{cert}' that expires in {days} days. 

If this lapses, they will be out of compliance for their scheduled area. Please ensure they complete their renewal module by the end of their next shift.

You can view the Workday Learning Center and their transcript here: 
https://www.myworkday.com/fedex/learning

Thank you,
FedEx Operations Agent
"""
                
                mail.Save()
                print(f"📥 Staged draft for {name}'s supervisor ({supervisor_email})")
                draft_count += 1
                
        print(f"🎉 Success! {draft_count} drafts have been staged in your Outlook.")
            
    except FileNotFoundError:
        print("❌ Error: Could not find 'expiring_compliance_data.csv'. Make sure you run the scraper script first!")

if __name__ == "__main__":
    draft_compliance_emails_local()
