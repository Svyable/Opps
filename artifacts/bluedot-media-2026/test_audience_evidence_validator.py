import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from audience_evidence_validator import parse_rows

FIELDS = ["channel","period_start","period_end","views","watch_hours",
          "subscribers_gained","source_export","owner_attested"]
ROW = ["Vintage Era Radio","2026-10-01","2026-10-31","120","5.5","3",
       "owner-export-2026-11-01.csv","yes"]

class AudienceEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path=Path(self.tmp.name)/"analytics.csv"
    def write(self, rows, fields=FIELDS):
        with self.path.open("w", newline="", encoding="utf-8") as f:
            w=csv.writer(f)
            w.writerow(fields)
            w.writerows(rows)
    def test_valid_synthetic_fixture(self):
        self.write([ROW])
        d=parse_rows(self.path)
        self.assertEqual(d["channels"]["Vintage Era Radio"]["views"],120)
        self.assertEqual(len(d["source_sha256"]),64)
        self.assertIn("NOT independently verified",d["status"])
    def test_missing_columns(self):
        self.write([ROW[:-1]],FIELDS[:-1])
        with self.assertRaisesRegex(ValueError,"missing required"):parse_rows(self.path)
    def test_no_rows(self):
        self.write([])
        with self.assertRaisesRegex(ValueError,"no analytics"):parse_rows(self.path)
    def test_negative_views(self):
        self.write([ROW[:3]+["-1"]+ROW[4:]])
        with self.assertRaisesRegex(ValueError,"negative"):parse_rows(self.path)
    def test_no_attestation(self):
        self.write([ROW[:-1]+["no"]])
        with self.assertRaisesRegex(ValueError,"attestation"):parse_rows(self.path)
    def test_overlapping_periods(self):
        other=ROW.copy();other[1]="2026-10-15";other[2]="2026-11-01"
        self.write([ROW,other])
        with self.assertRaisesRegex(ValueError,"overlapping"):parse_rows(self.path)
    def test_adjacent_periods(self):
        other=ROW.copy();other[1]="2026-11-01";other[2]="2026-11-06"
        self.write([ROW,other])
        self.assertEqual(parse_rows(self.path)["channels"]["Vintage Era Radio"]["views"],240)
    def test_future_period(self):
        self.write([ROW[:2]+["2099-01-01"]+ROW[3:]])
        with self.assertRaisesRegex(ValueError,"future"):parse_rows(self.path)
    def test_noninteger_views(self):
        self.write([ROW[:3]+["many"]+ROW[4:]])
        with self.assertRaisesRegex(ValueError,"invalid row"):parse_rows(self.path)
    def test_two_channels(self):
        other=ROW.copy();other[0]="Plein Air Radio"
        self.write([ROW,other])
        self.assertEqual(len(parse_rows(self.path)["channels"]),2)

if __name__=="__main__":
    unittest.main(verbosity=2)
