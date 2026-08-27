# Synthetic Zero-Click Prototype

This public prototype demonstrates a safe local pipeline:

1. `generate_synthetic_records.py` writes clearly synthetic compliance records.
2. `draft_agent.py` validates the CSV and renders deterministic draft messages.
3. By default, drafts are written as local `.txt` files under an ignored directory.
4. On Windows, an explicit `--write-outlook-drafts` flag may stage Drafts through local Outlook if `pywin32` is already approved and installed.

It never sends email, logs into an enterprise portal, stores credentials, or reads real employee data.

```bash
python3 generate_synthetic_records.py
python3 draft_agent.py --input synthetic_compliance_data.csv --output-dir generated_drafts
python3 -m unittest discover -s tests -v
```

All names are placeholders and all addresses use the reserved `.invalid` top-level domain.
