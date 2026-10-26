"""Microprototype contract tests; no live agent, credentials, external calls or effects."""
import unittest
from gate_runner import ARMS, Grant, ToolCall, demo, evaluate


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.call = ToolCall("agent", "mock.file.write", "sandbox:/workspace/draft.txt", 10, 20)
        self.grant = Grant("agent", "mock.file.write", self.call.target, 10, 25, "human:reviewer")

    def decision(self, call=None, arm="enforced_boundary", grants=(), revoked=frozenset()):
        return evaluate(call or self.call, arm, grants, revoked)

    def test_three_arm_baseline(self):
        self.assertEqual(["mock_executed", "mock_executed", "blocked"], [r["decision"] for r in demo()])

    def test_approval_ui_is_cosmetic(self):
        result = self.decision(arm="cosmetic_approval")
        self.assertTrue(result["approval_ui_visible"])
        self.assertEqual("ui_only_not_enforced", result["reason"])

    def test_no_gate_executes_without_grant(self):
        self.assertEqual("mock_executed", self.decision(arm="no_gate")["decision"])

    def test_enforced_blocks_without_grant(self):
        self.assertEqual("no_current_scoped_grant", self.decision()["reason"])

    def test_enforced_allows_matching_grant(self):
        self.assertEqual("mock_executed", self.decision(grants=(self.grant,))["decision"])

    def test_expired_at_execution_time(self):
        g = Grant("agent", "mock.file.write", self.call.target, 10, 20, "human:reviewer")
        self.assertEqual("blocked", self.decision(grants=(g,))["decision"])

    def test_grant_not_yet_valid(self):
        g = Grant("agent", "mock.file.write", self.call.target, 21, 30, "human:reviewer")
        self.assertEqual("blocked", self.decision(grants=(g,))["decision"])

    def test_wrong_target_not_prefix_granted(self):
        g = Grant("agent", "mock.file.write", "sandbox:/workspace", 10, 30, "human:reviewer")
        self.assertEqual("blocked", self.decision(grants=(g,))["decision"])

    def test_wrong_tool(self):
        g = Grant("agent", "mock.message.send", self.call.target, 10, 30, "human:reviewer")
        self.assertEqual("blocked", self.decision(grants=(g,))["decision"])

    def test_alias_cannot_bypass_canonical_scope(self):
        call = ToolCall("agent", "mock.file.write_alias", self.call.target, 10, 20)
        self.assertEqual("mock_executed", self.decision(call, grants=(self.grant,))["decision"])
        self.assertEqual("blocked", self.decision(call)["decision"])

    def test_unknown_alias_fails_closed(self):
        call = ToolCall("agent", "mock.file.mystery", self.call.target, 10, 20)
        self.assertEqual("unknown_tool", self.decision(call, grants=(self.grant,))["reason"])

    def test_delegation_requires_parent_grant(self):
        call = ToolCall("child", "mock.file.write", self.call.target, 10, 20, delegated_from="parent")
        child = Grant("child", "mock.file.write", self.call.target, 10, 30, "human:reviewer")
        self.assertEqual("delegation_not_authorized", self.decision(call, grants=(child,))["reason"])
        parent = Grant("parent", "mock.file.write", self.call.target, 10, 30, "human:reviewer", True)
        self.assertEqual("mock_executed", self.decision(call, grants=(child, parent))["decision"])

    def test_parent_without_delegation_rights_blocked(self):
        call = ToolCall("child", "mock.file.write", self.call.target, 10, 20, delegated_from="parent")
        child = Grant("child", "mock.file.write", self.call.target, 10, 30, "human:reviewer")
        parent = Grant("parent", "mock.file.write", self.call.target, 10, 30, "human:reviewer")
        self.assertEqual("blocked", self.decision(call, grants=(child, parent))["decision"])

    def test_revoked_grant_fails_closed(self):
        self.assertEqual("blocked", self.decision(grants=(self.grant,), revoked=frozenset((self.grant,)))["decision"])

    def test_ambiguous_authority_fails_closed(self):
        call = ToolCall("agent", "mock.file.write", self.call.target, 10, 20, "ambiguous")
        self.assertEqual("ambiguous_authority", self.decision(call, grants=(self.grant,))["reason"])

    def test_mock_approver_marker_required(self):
        g = Grant("agent", "mock.file.write", self.call.target, 10, 30, "agent")
        self.assertEqual("blocked", self.decision(grants=(g,))["decision"])

    def test_invalid_targets_never_run(self):
        for target in ("https://real.example/", "sandbox:/a/../b", "file:///etc/passwd", "mock://a/../../b"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                self.decision(ToolCall("agent", "mock.file.write", target, 10, 20), arm="no_gate")

    def test_invalid_times_never_run(self):
        for start, end in ((21, 20), (10, float("nan")), (True, 20), (-1, 20)):
            with self.subTest(start=start, end=end), self.assertRaises(ValueError):
                self.decision(ToolCall("agent", "mock.file.write", self.call.target, start, end))

    def test_receipt_has_no_real_effects(self):
        for arm in ARMS:
            r = self.decision(arm=arm)
            self.assertFalse(r["real_side_effects"])
            self.assertEqual(64, len(r["request_sha256"]))

    def test_deterministic_receipts(self):
        self.assertEqual(demo(), demo())


if __name__ == "__main__":
    unittest.main()
