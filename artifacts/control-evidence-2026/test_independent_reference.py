#!/usr/bin/env python3
"""Synthetic regression checks only; no real independent R3 has participated."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from independent_reference import freeze_reference, score_after_r3


def fixture():
    b = {"schema_version": 1, "dataset_id": "synthetic-r3",
         "source_sha256": "a" * 64, "case_count": 4}
    assignments = []
    for i in range(4):
        rid = f"blind-{i}"
        assignments.extend([
            {"review_id": rid, "reviewer_id": "R1" if i % 2 == 0 else "R2",
             "arm": "narrative_only"},
            {"review_id": rid, "reviewer_id": "R2" if i % 2 == 0 else "R1",
             "arm": "narrative_plus_receipts"}])
    a = {**b, "packet_type": "PRIVATE_TWO_ARM_ASSIGNMENT",
         "assignments": assignments}
    decisions = []
    for i in range(4):
        decisions.append({
            "review_id": f"blind-{i}",
            "verdict": ["refuted", "supported", "insufficient_evidence", "refuted"][i],
            "evidence_sha256": "b" * 64 if i != 2 else None,
            "source_verified": i != 2,
            "coverage": "complete" if i != 2 else "unknown",
            "rationale": "Synthetic reference rationale for regression test"})
    r3 = {**b, "packet_type": "PRIVATE_R3_ADJUDICATION",
          "adjudicator_id": "R3", "decisions": decisions}
    responses = {"R1": {}, "R2": {}}
    for row in assignments:
        responses[row["reviewer_id"]][row["review_id"]] = "refuted"
    return a, r3, responses


class IndependentReferenceTests(unittest.TestCase):
    def test_valid_register_scored_with_warning(self):
        a, r, responses = fixture()
        key = freeze_reference(a, r)
        self.assertEqual(key["reference_origin"], "R3_declared_independent_not_authenticated")
        self.assertFalse(key["reference_is_ground_truth"])
        self.assertEqual(len(key["labels"]), 4)
        s = score_after_r3(a, r, responses)
        self.assertEqual(s["non_support_cases"], 3)
        self.assertFalse(s["reference_is_ground_truth"])
        self.assertIn("operator declarations", s["warning"])

    def test_r3_cannot_be_experimental_reviewer(self):
        a, r, _ = fixture()
        r["adjudicator_id"] = "R1"
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_missing_r3_decision(self):
        a, r, _ = fixture()
        r["decisions"].pop()
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_duplicate_r3_decision(self):
        a, r, _ = fixture()
        r["decisions"][1]["review_id"] = "blind-0"
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_author_label_leak_rejected(self):
        a, r, _ = fixture()
        r["decisions"][0]["expected_verdict"] = "refuted"
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_unverified_support_rejected(self):
        a, r, _ = fixture()
        r["decisions"][1]["source_verified"] = False
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_incomplete_coverage_support_rejected(self):
        a, r, _ = fixture()
        r["decisions"][1]["coverage"] = "partial"
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_refutation_without_evidence_digest_rejected(self):
        a, r, _ = fixture()
        r["decisions"][0]["evidence_sha256"] = None
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_unverified_insufficient_evidence_allowed(self):
        a, r, _ = fixture()
        r["decisions"][2]["source_verified"] = False
        key = freeze_reference(a, r)
        self.assertEqual(key["labels"][2]["expected_verdict"], "insufficient_evidence")

    def test_wrong_binding_rejected(self):
        a, r, _ = fixture()
        r["source_sha256"] = "f" * 64
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_duplicate_arm_rejected(self):
        a, r, _ = fixture()
        a["assignments"][1]["arm"] = "narrative_only"
        with self.assertRaises(ValueError):
            freeze_reference(a, r)

    def test_cli_private_file_and_no_overwrite(self):
        a, r, responses = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, data in [("assignment.json", a), ("r3.json", r),
                               ("responses.json", responses)]:
                (root / name).write_text(json.dumps(data), encoding="utf-8")
            cmd = [sys.executable, str(Path(__file__).with_name("independent_reference.py")),
                   "--assignment", str(root / "assignment.json"),
                   "--adjudication", str(root / "r3.json"),
                   "--responses", str(root / "responses.json"),
                   "--output", str(root / "out.json")]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            if os.name == "posix":
                self.assertEqual((root / "out.json").stat().st_mode & 0o777, 0o600)
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)


if __name__ == "__main__":
    unittest.main()
