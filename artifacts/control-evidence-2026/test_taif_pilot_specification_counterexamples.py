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

if __name__ == "__main__":
    unittest.main()
