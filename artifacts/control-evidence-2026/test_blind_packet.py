"""Regression tests for the prospective reviewer-packet builder (synthetic only)."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from blind_packet import prepare


def sample():
    return {"dataset_id": "synthetic-demo-only", "cases": [
        {"case_id": "A01", "claim_type": "action_completed", "scope_id": "s", "action_id": "a",
         "args_digest": "d", "coverage": "complete", "coverage_writer": "independent",
         "events": [{"kind": "action_succeeded", "at": 1, "writer": "independent", "scope_id": "s", "action_id": "a", "args_digest": "d"}],
         "expected_verdict": "supported"},
        {"case_id": "A02", "claim_type": "action_completed", "scope_id": "s", "action_id": "a",
         "args_digest": "d", "coverage": "partial", "coverage_writer": "agent", "events": [],
         "expected_verdict": "insufficient_evidence"}]}


class PacketTests(unittest.TestCase):
    def setUp(self):
        self.data = json.dumps(sample()).encode()
        self.secret = b"x" * 32

    def test_blind_packet_and_identity(self):
        r, k = prepare(self.data, self.secret)
        self.assertEqual(r["case_count"], 2)
        self.assertNotIn("expected_verdict", json.dumps(r))
        self.assertNotIn("case_id", json.dumps(r))
        self.assertEqual(set(x["review_id"] for x in r["cases"]), set(x["review_id"] for x in k["labels"]))
        self.assertEqual(len(set(x["review_id"] for x in r["cases"])), 2)
        self.assertEqual(r["source_sha256"], k["source_sha256"])

    def test_deterministic(self):
        self.assertEqual(prepare(self.data, self.secret), prepare(self.data, self.secret))

    def test_different_secret_changes_ids(self):
        a, _ = prepare(self.data, self.secret)
        b, _ = prepare(self.data, b"y" * 32)
        self.assertNotEqual(a["cases"][0]["review_id"], b["cases"][0]["review_id"])

    def test_duplicate_case_rejected(self):
        d = sample(); d["cases"].append(d["cases"][0])
        with self.assertRaises(ValueError): prepare(json.dumps(d).encode(), self.secret)

    def test_hidden_extra_field_rejected(self):
        d = sample(); d["cases"][0]["gold_label"] = "supported"
        with self.assertRaises(ValueError): prepare(json.dumps(d).encode(), self.secret)

    def test_event_label_leak_rejected(self):
        d = sample(); d["cases"][0]["events"][0]["expected_verdict"] = "supported"
        with self.assertRaises(ValueError): prepare(json.dumps(d).encode(), self.secret)

    def test_short_secret_rejected(self):
        with self.assertRaises(ValueError): prepare(self.data, b"short")

    def test_bad_coverage_rejected(self):
        d = sample(); d["cases"][0]["coverage"] = "perfect"
        with self.assertRaises(ValueError): prepare(json.dumps(d).encode(), self.secret)

    def test_cli_files_private_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d/"cases.json").write_bytes(self.data)
            (d/"secret").write_bytes(self.secret)
            cmd = [sys.executable, str(Path(__file__).with_name("blind_packet.py")),
                   "--source", str(d/"cases.json"), "--secret-file", str(d/"secret"),
                   "--reviewer-out", str(d/"reviewer.json"), "--private-key-out", str(d/"key.json")]
            subprocess.run(cmd, check=True, capture_output=True)
            self.assertEqual((d/"key.json").stat().st_mode & 0o777, 0o600)
            self.assertEqual((d/"reviewer.json").stat().st_mode & 0o777, 0o600)
            self.assertNotIn("expected_verdict", (d/"reviewer.json").read_text())
            self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)


if __name__ == "__main__":
    unittest.main()
