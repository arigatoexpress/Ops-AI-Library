from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path

PROTOTYPE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOTYPE_DIR))

from draft_agent import load_records, render_draft, urgency, write_text_drafts  # noqa: E402
from generate_synthetic_records import SYNTHETIC_RECORDS, write_records  # noqa: E402


class PrototypeTests(unittest.TestCase):
    def test_fixture_addresses_are_reserved_for_examples(self) -> None:
        self.assertTrue(SYNTHETIC_RECORDS)
        self.assertTrue(
            all(str(record["reviewer_email"]).endswith(".invalid") for record in SYNTHETIC_RECORDS)
        )

    def test_pipeline_generates_review_only_drafts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            csv_path = root / "synthetic.csv"
            output_dir = root / "drafts"
            write_records(csv_path)
            records = load_records(csv_path)
            write_text_drafts(records, output_dir)
            drafts = list(output_dir.glob("*.txt"))
            self.assertEqual(len(drafts), len(SYNTHETIC_RECORDS))
            self.assertTrue(all("HUMAN REVIEW REQUIRED" in item.read_text() for item in drafts))

    def test_non_demo_email_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "unsafe.csv"
            row = dict(SYNTHETIC_RECORDS[0])
            row["reviewer_email"] = "not-an-example-address"
            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=row.keys())
                writer.writeheader()
                writer.writerow(row)
            with self.assertRaisesRegex(ValueError, "must use the .invalid domain"):
                load_records(csv_path)

    def test_urgency_and_draft_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "synthetic.csv"
            write_records(csv_path)
            record = load_records(csv_path)[0]
            self.assertEqual(urgency(record), "DUE SOON - REVIEW REQUIRED")
            subject, body = render_draft(record)
            self.assertIn(record.employee_display_name, subject)
            self.assertIn(record.source_record_id, body)


if __name__ == "__main__":
    unittest.main()
