"""Render review-only compliance drafts from a validated synthetic CSV."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

REQUIRED_FIELDS = {
    "employee_display_name",
    "compliance_item",
    "days_until_due",
    "reviewer_email",
    "source_as_of",
    "source_record_id",
}
SYNTHETIC_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.invalid$")


@dataclass(frozen=True)
class ComplianceRecord:
    employee_display_name: str
    compliance_item: str
    days_until_due: int
    reviewer_email: str
    source_as_of: str
    source_record_id: str


def load_records(input_path: Path) -> list[ComplianceRecord]:
    with input_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_FIELDS.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(sorted(missing))}")

        records: list[ComplianceRecord] = []
        for row_number, row in enumerate(reader, start=2):
            try:
                days_until_due = int(row["days_until_due"])
            except (TypeError, ValueError) as error:
                raise ValueError(f"Row {row_number}: days_until_due must be an integer") from error
            if not -365 <= days_until_due <= 3650:
                raise ValueError(f"Row {row_number}: days_until_due is outside the demo range")
            reviewer_email = row["reviewer_email"].strip()
            if not SYNTHETIC_EMAIL.fullmatch(reviewer_email):
                raise ValueError(
                    f"Row {row_number}: public demo addresses must use the .invalid domain"
                )
            records.append(
                ComplianceRecord(
                    employee_display_name=row["employee_display_name"].strip(),
                    compliance_item=row["compliance_item"].strip(),
                    days_until_due=days_until_due,
                    reviewer_email=reviewer_email,
                    source_as_of=row["source_as_of"].strip(),
                    source_record_id=row["source_record_id"].strip(),
                )
            )
    return records


def urgency(record: ComplianceRecord) -> str:
    if record.days_until_due < 0:
        return "OVERDUE - REVIEW REQUIRED"
    if record.days_until_due <= 3:
        return "DUE SOON - REVIEW REQUIRED"
    return "UPCOMING - REVIEW REQUIRED"


def render_draft(record: ComplianceRecord) -> tuple[str, str]:
    subject = (
        f"{urgency(record)}: {record.employee_display_name} - "
        f"{record.compliance_item}"
    )
    body = f"""DRAFT - HUMAN REVIEW REQUIRED

Hello,

The synthetic demonstration dataset dated {record.source_as_of} lists
{record.employee_display_name}'s "{record.compliance_item}" item as due in
{record.days_until_due} day(s).

Before taking action:
1. Verify the record in the approved source system.
2. Confirm the recipient and the current approved procedure.
3. Edit or reject this draft. Do not rely on this demonstration as policy.

Synthetic record: {record.source_record_id}
"""
    return subject, body


def safe_filename(record: ComplianceRecord) -> str:
    token = re.sub(r"[^A-Za-z0-9._-]+", "-", record.source_record_id).strip("-")
    return f"{token or 'synthetic-record'}.txt"


def write_text_drafts(records: list[ComplianceRecord], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        subject, body = render_draft(record)
        content = f"To: {record.reviewer_email}\nSubject: {subject}\n\n{body}"
        (output_dir / safe_filename(record)).write_text(content, encoding="utf-8")


def write_outlook_drafts(records: list[ComplianceRecord]) -> None:
    try:
        import win32com.client as win32  # type: ignore[import-not-found]
    except ImportError as error:
        raise RuntimeError("pywin32 is required for the optional Outlook handoff") from error

    outlook = win32.Dispatch("outlook.application")
    for record in records:
        subject, body = render_draft(record)
        mail = outlook.CreateItem(0)
        mail.To = record.reviewer_email
        mail.Subject = subject
        mail.Body = body
        mail.Save()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("generated_drafts"))
    parser.add_argument(
        "--write-outlook-drafts",
        action="store_true",
        help="Explicitly stage Drafts in local Outlook; never sends messages",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    compliance_records = load_records(arguments.input)
    write_text_drafts(compliance_records, arguments.output_dir)
    if arguments.write_outlook_drafts:
        write_outlook_drafts(compliance_records)
    print(f"Prepared {len(compliance_records)} review-only draft(s)")
