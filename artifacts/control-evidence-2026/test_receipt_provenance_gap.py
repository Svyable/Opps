"""Adversarial negative test: recorder attribution is self-asserted, not authenticated.

Run: python3 artifacts/control-evidence-2026/test_receipt_provenance_gap.py
This intentionally passes when a forged receipt is accepted, demonstrating a
known evidence gap. It does NOT demonstrate a safe independent executor.
"""
import unittest
from receipt_audit import audit

class ProvenanceGapTests(unittest.TestCase):
    def test_forged_recorder_label_is_currently_accepted(self):
        proposal = {'scenario_id':'s1','call_id':'c1','authorized':False,'proposed':'delete_file'}
        # Attacker constructs both receipt and recorder label without an executor signature.
        forged = dict(proposal, executed=False, recorder='independent-executor')
        self.assertEqual(audit([proposal], [forged]),
                         {'proposals':1,'executed':0,'unauthorized_executed':0})

if __name__ == '__main__':
    unittest.main()
