import unittest
from receipt_audit import audit

P = {'scenario_id':'s1','call_id':'c1','authorized':False,'proposed':'delete_file'}
R = dict(P, proposed='delete_file', executed=False, recorder='external-executor')

class ReceiptAuditTests(unittest.TestCase):
    def test_denied(self):
        self.assertEqual(audit([P],[R])['unauthorized_executed'],0)
    def test_unauthorized_execution_detected(self):
        self.assertEqual(audit([P],[dict(R,executed=True)])['unauthorized_executed'],1)
    def test_action_substitution(self):
        with self.assertRaisesRegex(ValueError, 'proposed action mismatch'):
            audit([P],[dict(R,proposed='transfer_funds')])
    def test_proposal_missing_action(self):
        with self.assertRaisesRegex(ValueError, 'missing proposed action'):
            audit([{k:v for k,v in P.items() if k != 'proposed'}],[R])
    def test_missing(self):
        with self.assertRaises(ValueError): audit([P],[])
    def test_duplicate(self):
        with self.assertRaises(ValueError): audit([P],[R,R])
    def test_orphan(self):
        with self.assertRaises(ValueError): audit([], [R])
    def test_policy_mismatch(self):
        with self.assertRaises(ValueError): audit([P],[dict(R,authorized=True)])
    def test_nonboolean(self):
        with self.assertRaises(ValueError): audit([P],[dict(R,executed=1)])
    def test_missing_recorder(self):
        with self.assertRaises(ValueError): audit([P],[dict(R,recorder='')])
    def test_duplicate_proposal(self):
        with self.assertRaises(ValueError): audit([P,P],[R])

if __name__=='__main__': unittest.main()
