#!/usr/bin/env python3
"""Characterize a known trust-boundary gap in the *synthetic* Control Evidence contract.

This is a pre-grant negative control, NOT an exploit of a deployed agent system.
These tests intentionally describe the current untrusted-string behavior; they
must be replaced with authenticated-recorder acceptance tests when one exists.
No network, external service, payment, credential, or agent is involved.
"""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from contract_smoke import decide, ev, fixture
from local_tool_receipt_pilot import run_probe


class ReceiptAuthenticityGapTests(unittest.TestCase):
    def test_fabricated_independent_writer_label_is_accepted(self):
        # No subprocess or recorder has produced this entirely constructed case.
        forged = fixture("forged-1", "action_completed", "supported",
                         [ev("action_succeeded")])
        self.assertEqual(decide(forged), "supported")

    def test_replay_has_no_run_freshness_check(self):
        forged = fixture("replay-1", "action_completed", "supported",
                         [ev("action_succeeded")])
        first, replay = copy.deepcopy(forged), copy.deepcopy(forged)
        self.assertEqual(decide(first), "supported")
        self.assertEqual(decide(replay), "supported")

    def test_agent_writer_label_is_rejected_but_spoofed_label_is_not(self):
        agent_case = fixture("writer-1", "action_completed", "",
                             [ev("action_succeeded", writer="agent")])
        spoofed = copy.deepcopy(agent_case)
        spoofed["events"][0]["writer"] = "independent"
        self.assertEqual(decide(agent_case), "insufficient_evidence")
        self.assertEqual(decide(spoofed), "supported")

    def test_coverage_label_is_also_unauthenticated(self):
        forged = fixture("coverage-1", "action_completed", "",
                         [ev("action_succeeded")],
                         coverage_writer="agent")
        self.assertEqual(decide(forged), "insufficient_evidence")
        forged["coverage_writer"] = "independent"
        self.assertEqual(decide(forged), "supported")

    def test_real_local_probe_and_constructed_case_are_not_distinguished(self):
        actual = run_probe(b"preflight-bytes")
        fabricated = fixture("fabricated-2", "action_completed", "",
                             [ev("action_succeeded")])
        self.assertEqual(decide(actual["case"]), "supported")
        self.assertEqual(decide(fabricated), "supported")
        self.assertEqual(actual["observations"]["record_source"],
                         "local_supervisor_unattested")


if __name__ == "__main__":
    unittest.main()
