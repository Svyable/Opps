#!/usr/bin/env python3
"""Side-effect-free sequence-level authority negative control for Foresight.

This is a deterministic *mock*, not a payment service, authenticated grant,
thread-safe authorization boundary, or AI-agent evaluation.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

from gate_runner import ARMS, TOOL_ALIASES, Grant, ToolCall, _safe_target, _time_ok, _valid_grant, evaluate


@dataclass(frozen=True)
class MockIntent:
    intent_id: str
    actor: str
    tool: str  # canonical mock tool
    target: str
    max_total_cents: int
    max_operations: int
    valid_from: int
    valid_until: int
    approver: str  # unauthenticated human: marker


@dataclass(frozen=True)
class MockAction:
    call: ToolCall
    intent_id: str
    operation_id: str
    amount_cents: int


class MockSequenceHarness:
    """Compare existing three arms with/without mock cumulative intent checks.

    enforce_intent=False deliberately reproduces the known stateless weakness
    in the enforced_boundary arm. No tool or payment is actually executed.
    State is in-memory, sequential and neither durable nor concurrency-safe.
    """

    def __init__(self, intent: MockIntent, arm: str, grants: tuple[Grant, ...] = (),
                 revoked: frozenset[Grant] = frozenset(), enforce_intent: bool = True):
        if arm not in ARMS:
            raise ValueError("unknown arm")
        if type(enforce_intent) is not bool:
            raise ValueError("enforce_intent must be bool")
        if (not isinstance(intent, MockIntent)
                or any(not isinstance(x, str) or not x.strip()
                       for x in (intent.intent_id, intent.actor, intent.tool,
                                 intent.target, intent.approver))
                or intent.tool not in TOOL_ALIASES.values()
                or not _safe_target(intent.target)
                or not intent.approver.startswith("human:")
                or len(intent.approver) <= len("human:")
                or type(intent.max_total_cents) is not int or intent.max_total_cents <= 0
                or type(intent.max_operations) is not int or intent.max_operations <= 0
                or not _time_ok(intent.valid_from) or not _time_ok(intent.valid_until)
                or intent.valid_from >= intent.valid_until):
            raise ValueError("invalid mock intent")
        self.intent = intent
        self.arm = arm
        self.grants = grants
        self.revoked = revoked
        self.enforce_intent = enforce_intent
        self.mock_executed_cents = 0
        self.accepted_operation_ids: set[str] = set()
        self.last_accepted_time: int | None = None

    def apply(self, action: MockAction) -> dict:
        if (not isinstance(action, MockAction)
                or not isinstance(action.intent_id, str) or not action.intent_id.strip()
                or not isinstance(action.operation_id, str) or not action.operation_id.strip()
                or type(action.amount_cents) is not int or action.amount_cents <= 0):
            raise ValueError("invalid mock action")
        base = evaluate(action.call, self.arm, self.grants, self.revoked)
        reason = base["reason"]
        allowed = base["decision"] == "mock_executed"
        if allowed and self.arm == "enforced_boundary" and self.enforce_intent:
            c = action.call
            i = self.intent
            canonical = TOOL_ALIASES.get(c.tool)
            if action.intent_id != i.intent_id or c.actor != i.actor or canonical != i.tool or c.target != i.target:
                reason, allowed = "intent_scope_mismatch", False
            elif not any(isinstance(g, Grant) and g not in self.revoked
                         and g.approver == i.approver
                         and _valid_grant(g, i.actor, i.tool, i.target, c.executed_at)
                         for g in self.grants):
                reason, allowed = "intent_approval_not_bound", False
            elif not i.valid_from <= c.executed_at < i.valid_until:
                reason, allowed = "intent_expired_or_not_yet_valid", False
            elif action.operation_id in self.accepted_operation_ids:
                reason, allowed = "replayed_operation_id", False
            elif self.last_accepted_time is not None and c.executed_at < self.last_accepted_time:
                reason, allowed = "out_of_order_operation", False
            elif len(self.accepted_operation_ids) >= i.max_operations:
                reason, allowed = "intent_operation_limit", False
            elif self.mock_executed_cents + action.amount_cents > i.max_total_cents:
                reason, allowed = "intent_total_limit", False
            else:
                reason = "scoped_grant_and_bounded_intent"
        elif allowed and self.arm == "enforced_boundary":
            reason = "per_call_only_no_cumulative_guard"

        if allowed:
            self.mock_executed_cents += action.amount_cents
            if self.arm == "enforced_boundary" and self.enforce_intent:
                self.accepted_operation_ids.add(action.operation_id)
                self.last_accepted_time = action.call.executed_at

        action_digest = hashlib.sha256(json.dumps({
            "request_sha256": base["request_sha256"],
            "intent_id": action.intent_id,
            "operation_id": action.operation_id,
            "amount_cents": action.amount_cents,
        }, sort_keys=True).encode()).hexdigest()
        return {
            "arm": self.arm,
            "enforce_intent": self.enforce_intent,
            "decision": "mock_executed" if allowed else "blocked",
            "reason": reason,
            "intent_id": action.intent_id,
            "operation_id": action.operation_id,
            "amount_cents": action.amount_cents,
            "mock_cumulative_cents": self.mock_executed_cents,
            "intent_cap_cents": self.intent.max_total_cents,
            "over_cap": self.mock_executed_cents > self.intent.max_total_cents,
            "action_sha256": action_digest,
            "real_side_effects": False,
        }


def negative_control() -> dict:
    """Four $400 mock calls under a $1,000 mock total cap, same per-call grant."""
    intent = MockIntent("intent-1", "agent", "mock.message.send", "mock://payee/test",
                        100_000, 4, 10, 100, "human:reviewer")
    grant = Grant("agent", "mock.message.send", intent.target, 10, 100, "human:reviewer")
    calls = [MockAction(ToolCall("agent", "mock.message.send", intent.target, 10, 20 + j),
                        intent.intent_id, f"op-{j}", 40_000) for j in range(4)]
    variants = {
        "no_gate": MockSequenceHarness(intent, "no_gate"),
        "cosmetic_approval": MockSequenceHarness(intent, "cosmetic_approval"),
        "enforced_per_call_only": MockSequenceHarness(intent, "enforced_boundary", (grant,), enforce_intent=False),
        "enforced_with_intent_guard": MockSequenceHarness(intent, "enforced_boundary", (grant,)),
    }
    return {"status": "synthetic_negative_control_not_ai_agent_evidence",
            "results": {name: [h.apply(c) for c in calls] for name, h in variants.items()}}


if __name__ == "__main__":
    print(json.dumps(negative_control(), indent=2))
