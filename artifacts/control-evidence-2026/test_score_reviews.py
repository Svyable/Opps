"""Contract tests for prospective, not-yet-independent reviewer scoring."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from score_reviews import score, wilson


def fixture():
    b = dict(schema_version=1, dataset_id="synthetic-only", source_sha256="a"*64, case_count=3)
    packet = {**b, "packet_type": "reviewer_blinded", "cases": [{"review_id": str(i)} for i in range(3)]}
    key = {**b, "packet_type": "PRIVATE_LABEL_KEY", "labels": [
        {"review_id": "0", "case_id": "A", "expected_verdict": "supported"},
        {"review_id": "1", "case_id": "B", "expected_verdict": "refuted"},
        {"review_id": "2", "case_id": "C", "expected_verdict": "insufficient_evidence"}]}
    responses = {**b, "packet_type": "reviewer_responses", "judgments": [
        {"reviewer_id": "R1", "review_id": "0", "verdict": "supported"},
        {"reviewer_id": "R1", "review_id": "1", "verdict": "supported"},
        {"reviewer_id": "R1", "review_id": "2", "verdict": "no_decision"}]}
    return packet, key, responses


class ScoreTests(unittest.TestCase):
    def test_denominators_and_false_support(self):
        x = score(*fixture())
        r = x["reviewers"][0]
        self.assertEqual(r["support_on_non_support_reference"]["count"], 1)
        self.assertEqual(r["support_on_non_support_reference"]["denominator"], 2)
        self.assertEqual(r["reference_label_agreement"]["count"], 1)
        self.assertEqual(r["explicit_no_decision"], 1)
        self.assertFalse(x["reference_is_ground_truth"])

    def test_hash_mismatch_rejected(self):
        p, k, r = fixture(); r["source_sha256"] = "b"*64
        with self.assertRaises(ValueError): score(p, k, r)

    def test_case_count_mismatch_rejected(self):
        p, k, r = fixture(); p["cases"].pop()
        with self.assertRaises(ValueError): score(p, k, r)

    def test_duplicate_judgment_rejected(self):
        p, k, r = fixture(); r["judgments"].append(r["judgments"][0])
        with self.assertRaises(ValueError): score(p, k, r)

    def test_unknown_case_rejected(self):
        p, k, r = fixture(); r["judgments"][0]["review_id"] = "bogus"
        with self.assertRaises(ValueError): score(p, k, r)

    def test_missing_decision_rejected(self):
        p, k, r = fixture(); r["judgments"].pop()
        with self.assertRaises(ValueError): score(p, k, r)

    def test_extra_field_rejected(self):
        p, k, r = fixture(); r["judgments"][0]["expected_verdict"] = "supported"
        with self.assertRaises(ValueError): score(p, k, r)

    def test_no_non_support_denominator(self):
        p, k, r = fixture()
        for l in k["labels"]: l["expected_verdict"] = "supported"
        x = score(p, k, r)
        self.assertIsNone(x["reviewers"][0]["support_on_non_support_reference"]["rate"])

    def test_multi_reviewer(self):
        p, k, r = fixture()
        r["judgments"] += [{**j, "reviewer_id": "R2"} for j in list(r["judgments"])]
        self.assertEqual(len(score(p, k, r)["reviewers"]), 2)

    def test_wilson_bounds(self):
        self.assertIsNone(wilson(0, 0))
        self.assertEqual(wilson(0, 10)[0], 0)
        self.assertEqual(wilson(10, 10)[1], 1)

    def test_cli_exclusive_private_output(self):
        p, k, r = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            for name, obj in [("packet.json",p),("key.json",k),("answers.json",r)]:
                (t/name).write_text(json.dumps(obj))
            cmd = [sys.executable, str(Path(__file__).with_name("score_reviews.py")),
                   "--packet",str(t/"packet.json"),"--private-key",str(t/"key.json"),
                   "--responses",str(t/"answers.json"),"--output",str(t/"results.json")]
            a = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(a.returncode, 0, a.stderr)
            self.assertEqual((t/"results.json").stat().st_mode & 0o777, 0o600)
            self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)


if __name__ == "__main__": unittest.main()
