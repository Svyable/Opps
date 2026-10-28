"""Contract checks for the synthetic manifest-to-boundary smoke test.

No agent trial, live authorization, tool side effect, or safety outcome.
"""
import unittest
from collections import Counter

from pilot_receipts import SUPPORTED, make_pilot, map_case
from preregister import ARMS, make_manifest


class PilotReceiptTests(unittest.TestCase):
    def test_coverage_and_explicit_exclusions(self):
        pilot = make_pilot()
        self.assertEqual((36, 24, 108, 72),
                         (pilot["covered_scenarios"], pilot["excluded_scenarios"],
                          pilot["covered_assignments"], pilot["excluded_assignments"]))
        self.assertEqual(24, len(pilot["excluded_case_ids"]))
        self.assertEqual({"secret_handling", "delegation"},
                         {case_id.rsplit("-", 2)[0] for case_id in pilot["excluded_case_ids"]})

    def test_all_arms_and_cases_covered_once(self):
        pilot = make_pilot()
        pairs = [(r["case_id"], r["arm"]) for r in pilot["receipts"]]
        self.assertEqual(108, len(set(pairs)))
        self.assertEqual(set(ARMS), {r["arm"] for r in pilot["receipts"]})
        self.assertEqual(36, len({r["case_id"] for r in pilot["receipts"]}))

    def test_expected_mock_counts_are_not_measured_effects(self):
        self.assertEqual({
            "no_gate": {"mock_executed": 36, "blocked": 0},
            "cosmetic_approval": {"mock_executed": 36, "blocked": 0},
            "enforced_boundary": {"mock_executed": 12, "blocked": 24},
        }, make_pilot()["mock_decision_counts"])

    def test_source_manifest_remains_unrun(self):
        pilot = make_pilot()
        manifest = make_manifest()
        self.assertEqual(manifest["sha256_spec"], pilot["source_manifest_sha256_spec"])
        self.assertEqual("not_collected", manifest["spec"]["outcomes"])
        self.assertTrue(all(a["status"] == "not_run" for a in manifest["spec"]["assignments"]))
        self.assertTrue(all(r["source_assignment_status"] == "not_run" for r in pilot["receipts"]))

    def test_no_real_effects_or_approval_authentication(self):
        pilot = make_pilot()
        self.assertTrue(pilot["all_real_side_effects_false"])
        self.assertTrue(all(r["mock_receipt"]["real_side_effects"] is False
                            for r in pilot["receipts"]))
        self.assertTrue(all(r["mock_receipt"]["request_sha256"]
                            for r in pilot["receipts"]))

    def test_mapping_rejects_unmodeled_and_malformed_cases(self):
        with self.assertRaises(ValueError):
            map_case({"category": "secret_handling", "policy_label": "authorized",
                      "case_id": "secret_handling-authorized-01"})
        with self.assertRaises(ValueError):
            map_case({"category": "file_write", "policy_label": "authorized",
                      "case_id": "file_write-authorized-99"})

    def test_reproducible(self):
        self.assertEqual(make_pilot(), make_pilot())

    def test_policy_label_is_not_observed_outcome(self):
        pilot = make_pilot()
        self.assertTrue(all("policy_label_from_fixture" in r and
                            "observed_outcome" not in r for r in pilot["receipts"]))
        self.assertIn("not independent ground truth", pilot["limitations"])


if __name__ == "__main__":
    unittest.main()
