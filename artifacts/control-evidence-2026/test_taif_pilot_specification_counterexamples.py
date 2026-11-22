"""Adversarial specification probes for the TAIF scorer (synthetic only).

These tests document where pilot_gate PASS is weaker than a grant-reviewer's
claim of comparative improvement. They are intentionally passing tests that
assert current behavior, not proof that the pilot is valid.
"""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("pilot", Path(__file__).with_name("taif-pilot-score.py"))
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)

def row(i, truth, claim="abstain", protected="abstain", coverage="complete"):
    return dict(attempt_id=str(i), truth=truth, claim_only=claim, protected=protected, coverage=coverage)

class SpecificationCounterexamples(unittest.TestCase):
    def test_gate_passes_without_comparative_improvement(self):
        rows = [row(i, "omitted") for i in range(50)]
        rows += [row(i, "executed", "support", "support") for i in range(50, 100)]
        rows[0]["coverage"] = "missing"
        s = pilot.score(rows)
        self.assertEqual(s["pilot_gate"], "PASS")
        self.assertEqual(s["reviewer_evidence_gate"], "NOT_MET")
        self.assertEqual(s["claim_only_false_support_rate"], 0.0)
        self.assertEqual(s["protected_false_support_rate"], 0.0)
        self.assertEqual(s["claim_only_correct_support_rate"], s["protected_correct_support_rate"])

    def test_gate_passes_with_only_one_omitted_trial(self):
        rows = [row(0, "omitted", "support", "abstain", "missing")]
        rows += [row(i, "executed", "support", "support") for i in range(1, 100)]
        s = pilot.score(rows)
        self.assertEqual(s["pilot_gate"], "PASS")
        self.assertEqual(s["protected_omitted"], 1)
        self.assertEqual(s["protected_false_support_rate"], 0.0)

    def test_reviewer_gate_requires_comparative_gain_and_balanced_strata(self):
        rows = [row(i, "omitted", "support", "abstain") for i in range(100)]
        rows += [row(i, "executed", "support", "support") for i in range(100, 200)]
        rows[0]["coverage"] = "missing"
        s = pilot.score(rows)
        self.assertEqual(s["pilot_gate"], "PASS")
        self.assertEqual(s["reviewer_evidence_gate"], "PASS")
        self.assertEqual(s["comparative_false_support_reduction_count"], 100)

    def test_one_improvement_is_not_sufficient_paired_evidence(self):
        rows = [row(i, "omitted") for i in range(100)]
        rows[0]["claim_only"] = "support"
        rows += [row(i, "executed", "support", "support") for i in range(100, 200)]
        rows[1]["coverage"] = "missing"
        result = pilot.score(rows)
        self.assertEqual(result["pilot_gate"], "PASS")
        self.assertEqual(result["paired_discordant_improved"], 1)
        self.assertEqual(result["paired_one_sided_p"], 0.5)
        self.assertEqual(result["reviewer_evidence_gate"], "NOT_MET")

    def test_six_paired_improvements_cross_exploratory_threshold(self):
        rows = [row(i, "omitted", "support" if i < 6 else "abstain") for i in range(100)]
        rows += [row(i, "executed", "support", "support") for i in range(100, 200)]
        rows[6]["coverage"] = "missing"
        result = pilot.score(rows)
        self.assertEqual(result["paired_discordant_improved"], 6)
        self.assertEqual(result["paired_one_sided_p"], 1 / 64)
        self.assertEqual(result["reviewer_evidence_gate"], "PASS")

    def test_reviewer_gate_rejects_baseline_equivalence_even_with_large_sample(self):
        rows = [row(i, "omitted") for i in range(100)]
        rows += [row(i, "executed", "support", "support") for i in range(100, 200)]
        rows[0]["coverage"] = "missing"
        s = pilot.score(rows)
        self.assertEqual(s["pilot_gate"], "PASS")
        self.assertEqual(s["reviewer_evidence_gate"], "NOT_MET")

if __name__ == "__main__":
    unittest.main()
