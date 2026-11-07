import unittest
from receipt_boundary import sign
from verified_claim import decide_verified

KEY = b'fixture-only-key'
CLAIM = dict(claim_type='action_completed', scope_id='s', action_id='a', args_digest='d')

def receipt(kind, nonce, key=KEY, **changes):
    event = dict(scope_id='s', action_id='a', args_digest='d', kind=kind, nonce=nonce)
    event.update(changes)
    return dict(event=event, signature=sign(event, key))

class VerifiedClaimTests(unittest.TestCase):
    def decide(self, events, coverage=None, key=KEY):
        return decide_verified(CLAIM, events, coverage, key, set())
    def test_valid(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e')],receipt('coverage_complete','c')), 'supported')
    def test_negative(self):
        self.assertEqual(self.decide([receipt('action_failed','e')],receipt('coverage_complete','c')), 'refuted')
    def test_missing_coverage(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e')]), 'insufficient_evidence')
    def test_forged_coverage_label(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e')],{'coverage':'complete','coverage_writer':'independent'}), 'insufficient_evidence')
    def test_wrong_key(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e',b'other')],receipt('coverage_complete','c')), 'insufficient_evidence')
    def test_replay_nonce(self):
        self.assertEqual(self.decide([receipt('action_succeeded','same')],receipt('coverage_complete','same')), 'insufficient_evidence')
    def test_tampered_scope(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e',scope_id='other')],receipt('coverage_complete','c')), 'insufficient_evidence')
    def test_conflicting_receipts(self):
        self.assertEqual(self.decide([receipt('action_succeeded','e'),receipt('action_failed','f')],receipt('coverage_complete','c')), 'insufficient_evidence')
    def test_cross_call_replay_rejected(self):
        used = set()
        events = [receipt('action_succeeded', 'e')]
        coverage = receipt('coverage_complete', 'c')
        self.assertEqual(decide_verified(CLAIM, events, coverage, KEY, used), 'supported')
        self.assertEqual(decide_verified(CLAIM, events, coverage, KEY, used), 'insufficient_evidence')

    def test_no_registry_fails_closed(self):
        self.assertEqual(decide_verified(CLAIM, [receipt('action_succeeded', 'e')],
                                         receipt('coverage_complete', 'c'), KEY),
                         'insufficient_evidence')

    def test_invalid_receipts_abstain(self):
        self.assertEqual(decide_verified(CLAIM, None,
                                         receipt('coverage_complete', 'c'), KEY, set()),
                         'insufficient_evidence')

    def test_unsigned_agent_label(self):
        self.assertEqual(self.decide([{'event':dict(kind='action_succeeded',writer='independent')}],receipt('coverage_complete','c')), 'insufficient_evidence')

if __name__ == '__main__':
    unittest.main()
