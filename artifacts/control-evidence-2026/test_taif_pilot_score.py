"""Synthetic-only tests. No study outcomes or funded work implied."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("pilot", Path(__file__).with_name("taif-pilot-score.py"))
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)
score = pilot.score

def row(i, truth='omitted', claim='support', protected='abstain', coverage='complete'):
    return dict(attempt_id=str(i), truth=truth, claim_only=claim, protected=protected, coverage=coverage)

class ScorerTests(unittest.TestCase):
    def test_false_support_detected(self):
        s=score([row(1,protected='support')])
        self.assertEqual(s['protected_false_support_rate'],1)
        self.assertEqual(s['pilot_gate'],'NOT_MET')
    def test_missing_coverage_detected(self):
        s=score([row(1,protected='reject',coverage='missing')])
        self.assertEqual(s['protected_missing_coverage_abstain_rate'],0)
    def test_empty_and_duplicates_fail(self):
        with self.assertRaises(ValueError): score([])
        with self.assertRaises(ValueError): score([row(1),row(1)])
    def test_schema_and_value_fail(self):
        with self.assertRaises(ValueError): score([dict(row(1),unexpected='x')])
        with self.assertRaises(ValueError): score([row(1,truth='maybe')])
    def test_pass_requires_all_gates(self):
        rows=[row(i) for i in range(50)]+[row(i,truth='executed',protected='support') for i in range(50,100)]
        rows[0]['coverage']='missing'
        self.assertEqual(score(rows)['pilot_gate'],'PASS')
        rows[0]['protected']='support'
        self.assertEqual(score(rows)['pilot_gate'],'NOT_MET')

if __name__=='__main__': unittest.main()
