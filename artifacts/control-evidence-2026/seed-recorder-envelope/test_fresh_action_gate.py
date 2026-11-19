"""Regression cases for the preexisting-state false-attribution finding."""
import unittest
from fresh_action_gate import run_fresh_trial


class FreshActionGateTests(unittest.TestCase):
    def test_authorized_fresh_write(self):
        self.assertEqual(run_fresh_trial(), 'VERIFIED')

    def test_preexisting_matching_file_rejected(self):
        self.assertEqual(run_fresh_trial(prepopulate=True), 'REJECT')

    def test_no_executor_is_unknown(self):
        self.assertEqual(run_fresh_trial(omit_executor=True), 'UNKNOWN')

    def test_tampered_bytes_rejected(self):
        self.assertEqual(run_fresh_trial(tamper=True), 'REJECT')

    def test_preexisting_and_omitted_executor_rejected(self):
        self.assertEqual(run_fresh_trial(prepopulate=True, omit_executor=True), 'REJECT')


if __name__ == '__main__':
    unittest.main()
