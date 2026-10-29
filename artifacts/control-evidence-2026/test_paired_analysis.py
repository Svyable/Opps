#!/usr/bin/env python3
import unittest
from paired_analysis import paired_false_support, exact_mcnemar_p


def fixture():
    b = {"schema_version": 1, "dataset_id": "synthetic", "source_sha256": "a" * 64, "case_count": 4}
    key = {**b, "packet_type": "PRIVATE_LABEL_KEY", "labels": [
        {"review_id": f"id-{i}", "case_id": f"private-{i}",
         "expected_verdict": "supported" if i == 3 else "refuted"} for i in range(4)]}
    rows = []
    for i in range(4):
        rows += [{"review_id": f"id-{i}", "reviewer_id": "R1" if i % 2 == 0 else "R2", "arm": "narrative_only"},
                 {"review_id": f"id-{i}", "reviewer_id": "R2" if i % 2 == 0 else "R1", "arm": "narrative_plus_receipts"}]
    a = {**b, "packet_type": "PRIVATE_TWO_ARM_ASSIGNMENT", "assignments": rows}
    responses = {"R1": {}, "R2": {}}
    for row in rows:
        responses[row["reviewer_id"]][row["review_id"]] = "refuted"
    return a, key, responses


class PairedTests(unittest.TestCase):
    def test_no_false_support(self):
        a, k, r = fixture()
        s = paired_false_support(a, k, r)
        self.assertEqual(s["non_support_cases"], 3)
        self.assertEqual(s["supported_reference_cases_excluded"], 1)
        self.assertEqual(s["paired_absolute_reduction"], 0)
        self.assertEqual(s["exact_two_sided_mcnemar_p"], 1)
        self.assertFalse(s["reference_is_ground_truth"])

    def test_beneficial_discordance(self):
        a, k, r = fixture()
        for row in a["assignments"]:
            if row["arm"] == "narrative_only" and row["review_id"] in ("id-0", "id-1"):
                r[row["reviewer_id"]][row["review_id"]] = "supported"
        s = paired_false_support(a, k, r)
        self.assertEqual(s["narrative_only_false_support_receipts_not"], 2)
        self.assertEqual(s["paired_absolute_reduction"], 2/3)
        self.assertEqual(s["exact_two_sided_mcnemar_p"], 0.5)

    def test_harmful_discordance(self):
        a, k, r = fixture()
        row = next(x for x in a["assignments"] if x["arm"] == "narrative_plus_receipts" and x["review_id"] == "id-2")
        r[row["reviewer_id"]][row["review_id"]] = "supported"
        s = paired_false_support(a, k, r)
        self.assertEqual(s["receipts_false_support_narrative_only_not"], 1)
        self.assertEqual(s["paired_absolute_reduction"], -1/3)

    def test_exact_tail(self):
        self.assertAlmostEqual(exact_mcnemar_p(10, 0), 0.001953125)
        self.assertEqual(exact_mcnemar_p(3, 3), 1.0)
        with self.assertRaises(ValueError): exact_mcnemar_p(True, 2)

    def test_reject_duplicate_assignment(self):
        a, k, r = fixture()
        a["assignments"][1]["arm"] = a["assignments"][0]["arm"]
        with self.assertRaises(ValueError): paired_false_support(a, k, r)

    def test_reject_missing_response(self):
        a, k, r = fixture()
        r["R1"].pop("id-0")
        with self.assertRaises(ValueError): paired_false_support(a, k, r)

    def test_reject_wrong_binding(self):
        a, k, r = fixture()
        k["source_sha256"] = "b" * 64
        with self.assertRaises(ValueError): paired_false_support(a, k, r)

    def test_reject_duplicate_case_id(self):
        a, k, r = fixture()
        k["labels"][1]["case_id"] = k["labels"][0]["case_id"]
        with self.assertRaises(ValueError): paired_false_support(a, k, r)

    def test_reject_same_reviewer_both_arms(self):
        a, k, r = fixture()
        a["assignments"][1]["reviewer_id"] = a["assignments"][0]["reviewer_id"]
        with self.assertRaises(ValueError): paired_false_support(a, k, r)

    def test_all_supported_reference_has_no_primary_denominator(self):
        a, k, r = fixture()
        for label in k["labels"]:
            label["expected_verdict"] = "supported"
        s = paired_false_support(a, k, r)
        self.assertIsNone(s["paired_absolute_reduction"])
        self.assertIsNone(s["exact_two_sided_mcnemar_p"])


if __name__ == "__main__":
    unittest.main()
