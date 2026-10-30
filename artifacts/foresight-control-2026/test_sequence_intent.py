"""Synthetic sequence-authorization negative controls; no real transactions."""
import unittest
from dataclasses import replace

from gate_runner import Grant, ToolCall
from sequence_intent import MockAction, MockIntent, MockSequenceHarness, negative_control


class SequenceIntentTests(unittest.TestCase):
    def setUp(self):
        self.intent = MockIntent("i", "agent", "mock.message.send", "mock://payee/test",
                                 1000, 3, 10, 100, "human:reviewer")
        self.grant = Grant("agent", "mock.message.send", self.intent.target, 10, 100, "human:reviewer")

    def harness(self, arm="enforced_boundary", guard=True):
        return MockSequenceHarness(self.intent, arm, (self.grant,), enforce_intent=guard)

    def action(self, op="a", amount=400, time=20, **kwargs):
        c = ToolCall("agent", "mock.message.send", self.intent.target, 10, time)
        return MockAction(c, "i", op, amount) if not kwargs else replace(MockAction(c, "i", op, amount), **kwargs)

    def test_negative_control_detects_stateless_overspend(self):
        results = negative_control()["results"]
        self.assertEqual(160000, results["enforced_per_call_only"][-1]["mock_cumulative_cents"])
        self.assertTrue(results["enforced_per_call_only"][-1]["over_cap"])
        guarded = results["enforced_with_intent_guard"]
        self.assertEqual(["mock_executed", "mock_executed", "blocked", "blocked"], [r["decision"] for r in guarded])
        self.assertEqual(80000, guarded[-1]["mock_cumulative_cents"])
        self.assertFalse(guarded[-1]["over_cap"])
        self.assertTrue(all(not r["real_side_effects"] for v in results.values() for r in v))

    def test_exact_cap_is_allowed_but_next_is_not(self):
        h = self.harness()
        self.assertEqual("mock_executed", h.apply(self.action("a", 600))["decision"])
        self.assertEqual("mock_executed", h.apply(self.action("b", 400, 21))["decision"])
        self.assertEqual("intent_total_limit", h.apply(self.action("c", 1, 22))["reason"])
        self.assertEqual(1000, h.mock_executed_cents)

    def test_replayed_operation_id_does_not_double_count(self):
        h = self.harness()
        h.apply(self.action())
        r = h.apply(self.action("a", 100, 21))
        self.assertEqual("replayed_operation_id", r["reason"])
        self.assertEqual(400, h.mock_executed_cents)

    def test_operation_limit_is_independent_of_amount(self):
        h = self.harness()
        for j in range(3):
            self.assertEqual("mock_executed", h.apply(self.action(str(j), 1, 20+j))["decision"])
        self.assertEqual("intent_operation_limit", h.apply(self.action("extra", 1, 23))["reason"])

    def test_intent_scope_mismatch_fails_closed(self):
        h = self.harness()
        for action in (self.action(intent_id="other"),
                       replace(self.action(), call=ToolCall("other", "mock.message.send", self.intent.target, 10, 20)),
                       replace(self.action(), call=ToolCall("agent", "mock.message.send", "mock://payee/other", 10, 20))):
            self.assertEqual("blocked", h.apply(action)["decision"])
        self.assertEqual(0, h.mock_executed_cents)

    def test_expired_intent_blocks_even_with_live_per_call_grant(self):
        h = MockSequenceHarness(replace(self.intent, valid_until=90), "enforced_boundary", (self.grant,))
        self.assertEqual("intent_expired_or_not_yet_valid", h.apply(self.action(time=95))["reason"])

    def test_out_of_order_calls_are_blocked(self):
        h = self.harness()
        h.apply(self.action(time=40))
        self.assertEqual("out_of_order_operation", h.apply(self.action("b", 10, 30))["reason"])

    def test_intent_approver_must_match_scoped_grant(self):
        h = MockSequenceHarness(replace(self.intent, approver="human:other"),
                                "enforced_boundary", (self.grant,))
        self.assertEqual("intent_approval_not_bound", h.apply(self.action())["reason"])

    def test_revoked_grant_still_blocks(self):
        h = MockSequenceHarness(self.intent, "enforced_boundary", (self.grant,), frozenset((self.grant,)))
        self.assertEqual("no_current_scoped_grant", h.apply(self.action())["reason"])
        self.assertEqual(0, h.mock_executed_cents)

    def test_no_gate_and_cosmetic_are_intentionally_unbounded(self):
        for arm in ("no_gate", "cosmetic_approval"):
            h = self.harness(arm)
            for j in range(4):
                h.apply(self.action(str(j), 400, 20+j))
            self.assertEqual(1600, h.mock_executed_cents)

    def test_invalid_amounts_and_intents_are_rejected(self):
        h = self.harness()
        for amount in (0, -1, True, 1.5):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                h.apply(self.action(amount=amount))
        with self.assertRaises(ValueError):
            MockSequenceHarness(replace(self.intent, approver="agent"), "enforced_boundary")
        with self.assertRaises(ValueError):
            MockSequenceHarness(replace(self.intent, max_total_cents=True), "enforced_boundary")
        self.assertEqual(0, h.mock_executed_cents)

    def test_receipt_binds_amount_and_operation_id(self):
        a = self.harness().apply(self.action("one", 100))
        b = self.harness().apply(self.action("one", 101))
        c = self.harness().apply(self.action("two", 100))
        self.assertEqual(64, len(a["action_sha256"]))
        self.assertNotEqual(a["action_sha256"], b["action_sha256"])
        self.assertNotEqual(a["action_sha256"], c["action_sha256"])

    def test_blocked_action_does_not_consume_budget(self):
        h = self.harness()
        self.assertEqual("intent_total_limit", h.apply(self.action(amount=1100))["reason"])
        self.assertEqual("mock_executed", h.apply(self.action("next", 100))["decision"])
        self.assertEqual(100, h.mock_executed_cents)


if __name__ == "__main__":
    unittest.main()
