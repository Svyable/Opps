"""Negative control: authenticated envelope does not provide single-use semantics.

A passing test demonstrates a vulnerability, not replay protection.
Run: python -m unittest -v test_same_run_replay.py
"""
import unittest
from recorder import sign, verify


class SameRunReplayNegativeControl(unittest.TestCase):
    def test_same_signed_event_is_accepted_twice(self):
        key = b'test-only-key-not-production'
        event = {
            'run_id': 'run-7',
            'action_id': 'write-1',
            'path': '/sandbox/out',
            'sha256': 'a' * 64,
            'observed': True,
        }
        tag = sign(event, key)
        results = [
            verify(event, tag, key, 'run-7', 'write-1', '/sandbox/out', 'a' * 64)
            for _ in range(2)
        ]
        # Current verifier is stateless: a valid signed event can be reused.
        self.assertEqual(results, ['VERIFIED', 'VERIFIED'])


if __name__ == '__main__':
    unittest.main()
