#!/usr/bin/env python3
"""Local subprocess probe regression tests; no agent outcome is measured."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from local_tool_receipt_pilot import run_probe, sha256
from contract_smoke import decide


class LocalToolReceiptPilotTests(unittest.TestCase):
    def test_real_subprocess_success_supports_claim(self):
        r = run_probe(b"known bytes")
        self.assertEqual(r["observations"]["worker_returncode"], 0)
        self.assertEqual(r["observations"]["observed_sha256"], sha256(b"known bytes"))
        self.assertEqual(decide(r["case"]), "supported")

    def test_real_subprocess_failure_refutes_claim(self):
        r = run_probe(b"known bytes", "fail")
        self.assertEqual(r["observations"]["worker_returncode"], 7)
        self.assertIsNone(r["observations"]["observed_sha256"])
        self.assertEqual(decide(r["case"]), "refuted")

    def test_post_execution_tamper_abstains(self):
        r = run_probe(b"known bytes", "tamper")
        self.assertNotEqual(r["observations"]["expected_sha256"],
                            r["observations"]["observed_sha256"])
        self.assertEqual(decide(r["case"]), "insufficient_evidence")

    def test_missing_observation_abstains(self):
        r = run_probe(b"known bytes", "missing")
        self.assertIsNone(r["observations"]["observed_sha256"])
        self.assertEqual(decide(r["case"]), "insufficient_evidence")

    def test_narrative_cannot_change_result(self):
        a = run_probe(b"known bytes", "fail", "I succeeded")
        b = run_probe(b"known bytes", "fail", "I failed")
        self.assertEqual(a["case"], b["case"])
        self.assertEqual(decide(a["case"]), "refuted")

    def test_argument_binding_changes_with_payload(self):
        a = run_probe(b"a")
        b = run_probe(b"b")
        self.assertNotEqual(a["case"]["args_digest"], b["case"]["args_digest"])

    def test_shell_metacharacters_are_plain_data(self):
        data = b"; $(touch /tmp/should-not-run) | & ' \""
        r = run_probe(data)
        self.assertEqual(decide(r["case"]), "supported")
        self.assertEqual(r["observations"]["expected_sha256"], sha256(data))

    def test_invalid_mode_rejected(self):
        with self.assertRaises(ValueError):
            run_probe(b"x", "unknown")

    def test_payload_length_bounded(self):
        with self.assertRaises(ValueError):
            run_probe(b"x" * 4097)

    def test_event_scope_mismatch_abstains(self):
        r = run_probe(b"known bytes")
        r["case"]["events"][0]["scope_id"] = "wrong"
        self.assertEqual(decide(r["case"]), "insufficient_evidence")


if __name__ == "__main__":
    unittest.main()
