#!/usr/bin/env python3
"""Synthetic attack/control regressions for a local-only supervisor demo."""
import copy
import secrets
import unittest

from run_bound_receipt_demo import observe_local_action, verify_local_receipt


class RunBoundReceiptDemoTests(unittest.TestCase):
    def setUp(self):
        self.key = secrets.token_bytes(32)
        self.payload = b"test bytes"
        self.used = set()

    def check(self, envelope, expected=None, payload=None, used=None):
        return verify_local_receipt(envelope, self.key,
                                    expected or envelope["receipt"]["run_id"],
                                    self.payload if payload is None else payload,
                                    self.used if used is None else used)

    def test_real_subprocess_success(self):
        self.assertEqual(self.check(observe_local_action(self.key, self.payload)), "supported")

    def test_worker_failure_refutes(self):
        self.assertEqual(self.check(observe_local_action(self.key, self.payload, "fail")), "refuted")

    def test_post_execution_mutation_abstains(self):
        self.assertEqual(self.check(observe_local_action(self.key, self.payload, "tamper")),
                         "insufficient_evidence")

    def test_missing_observation_abstains(self):
        self.assertEqual(self.check(observe_local_action(self.key, self.payload, "missing")),
                         "insufficient_evidence")

    def test_forged_source_label_and_mac_abstain(self):
        e = observe_local_action(self.key, self.payload)
        e["receipt"]["source"] = "unattested_local_supervisor"
        e["mac"] = "0" * 64
        self.assertEqual(self.check(e), "insufficient_evidence")
        self.assertFalse(self.used)

    def test_replay_abstains(self):
        e = observe_local_action(self.key, self.payload)
        self.assertEqual(self.check(e), "supported")
        self.assertEqual(self.check(e), "insufficient_evidence")

    def test_cross_run_receipt_abstains(self):
        e = observe_local_action(self.key, self.payload)
        self.assertEqual(self.check(e, expected="0" * 32), "insufficient_evidence")

    def test_payload_substitution_abstains(self):
        e = observe_local_action(self.key, self.payload)
        self.assertEqual(self.check(e, payload=b"different"), "insufficient_evidence")

    def test_action_substitution_abstains(self):
        e = observe_local_action(self.key, self.payload)
        e["receipt"]["action_id"] = "different"
        self.assertEqual(self.check(e), "insufficient_evidence")

    def test_tampered_returncode_abstains(self):
        e = observe_local_action(self.key, self.payload)
        e["receipt"]["returncode"] = 7
        self.assertEqual(self.check(e), "insufficient_evidence")

    def test_untrusted_narrative_has_no_effect(self):
        e = observe_local_action(self.key, self.payload, narrative="I failed")
        self.assertEqual(self.check(e), "supported")

    def test_wrong_key_abstains(self):
        e = observe_local_action(secrets.token_bytes(32), self.payload)
        self.assertEqual(self.check(e), "insufficient_evidence")

    def test_invalid_field_and_bool_returncode_abstain(self):
        e = observe_local_action(self.key, self.payload)
        a = copy.deepcopy(e)
        a["receipt"]["extra"] = "fake"
        self.assertEqual(self.check(a), "insufficient_evidence")
        b = copy.deepcopy(e)
        b["receipt"]["returncode"] = True
        self.assertEqual(self.check(b), "insufficient_evidence")

    def test_invalid_key_and_payload_rejected(self):
        with self.assertRaises(ValueError):
            observe_local_action(b"short", self.payload)
        with self.assertRaises(ValueError):
            observe_local_action(self.key, b"x" * 4097)


if __name__ == "__main__":
    unittest.main()
