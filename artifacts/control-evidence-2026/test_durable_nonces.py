import os
import tempfile
import unittest
from durable_nonces import SQLiteNonceRegistry
from receipt_boundary import sign, verify
from verified_claim import decide_verified

KEY = b'fixture-only-key'
CLAIM = dict(claim_type='action_completed', scope_id='s', action_id='a', args_digest='d')


def receipt(kind, nonce):
    event = dict(scope_id='s', action_id='a', args_digest='d', kind=kind, nonce=nonce)
    return dict(event=event, signature=sign(event, KEY))


class DurableNonceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.temp.name, 'nonces.sqlite')

    def tearDown(self):
        self.temp.cleanup()

    def test_restart_replay_rejected(self):
        coverage = receipt('coverage_complete', 'c')
        action = receipt('action_succeeded', 'e')
        with SQLiteNonceRegistry(self.path) as registry:
            self.assertEqual(decide_verified(CLAIM, [action], coverage, KEY, registry), 'supported')
        with SQLiteNonceRegistry(self.path) as registry:
            self.assertEqual(decide_verified(CLAIM, [action], coverage, KEY, registry), 'insufficient_evidence')

    def test_concurrent_connections_one_wins(self):
        with SQLiteNonceRegistry(self.path) as first, SQLiteNonceRegistry(self.path) as second:
            self.assertTrue(first.consume('same'))
            self.assertFalse(second.consume('same'))

    def test_invalid_signature_does_not_consume(self):
        action = receipt('action_succeeded', 'e')
        expected = {k: CLAIM[k] for k in ('scope_id', 'action_id', 'args_digest')}
        with SQLiteNonceRegistry(self.path) as registry:
            self.assertFalse(verify(action['event'], '0'*64, KEY, expected, registry))
            self.assertTrue(verify(action['event'], action['signature'], KEY, expected, registry))

    def test_no_memory_only_registry(self):
        with self.assertRaises(ValueError):
            SQLiteNonceRegistry(':memory:')

    def test_malformed_nonce_fails(self):
        with SQLiteNonceRegistry(self.path) as registry:
            self.assertFalse(registry.consume(''))
            self.assertFalse(registry.consume(None))

    def test_duplicate_coverage_fails_closed(self):
        with SQLiteNonceRegistry(self.path) as registry:
            self.assertEqual(decide_verified(CLAIM, [receipt('action_succeeded','e')],
                             receipt('coverage_complete','c'), KEY, registry), 'supported')
            self.assertEqual(decide_verified(CLAIM, [receipt('action_succeeded','new')],
                             receipt('coverage_complete','c'), KEY, registry), 'insufficient_evidence')


if __name__ == '__main__':
    unittest.main()
