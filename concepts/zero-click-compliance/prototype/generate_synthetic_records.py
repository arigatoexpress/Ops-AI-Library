"""Generate synthetic fixtures for the Zero-Click Compliance Agent demo."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

FIELDNAMES = [
    "employee_display_name",
    "compliance_item",
    "days_until_due",
    "reviewer_email",
    "source_as_of",
    "source_record_id",
]

SYNTHETIC_RECORDS = [
    {
        "employee_display_name": "Sample Employee A",
        "compliance_item": "Synthetic Safety Refresher",
        "days_until_due": 2,
        "reviewer_email": "reviewer.a@example.invalid",
        "source_as_of": "2026-08-27",
        "source_record_id": "SYN-001",
    },
    {
        "employee_display_name": "Sample Employee B",
        "compliance_item": "Synthetic Equipment Qualification",
        "days_until_due": 10,
        "reviewer_email": "reviewer.b@example.invalid",
        "source_as_of": "2026-08-27",
        "source_record_id": "SYN-002",
    },
]


def write_records(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(SYNTHETIC_RECORDS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("synthetic_compliance_data.csv"),
        help="Destination CSV (default: synthetic_compliance_data.csv)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    write_records(arguments.output)
    print(f"Wrote {len(SYNTHETIC_RECORDS)} synthetic records to {arguments.output}")
