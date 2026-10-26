#!/usr/bin/env python3
"""Deterministic, side-effect-free authorization boundary microprototype.

Not an AI-agent evaluation. It does not authenticate approvers or use real tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass

ARMS = ("no_gate", "cosmetic_approval", "enforced_boundary")
TOOL_ALIASES = {
    "mock.file.write": "mock.file.write",
    "mock.file.write_alias": "mock.file.write",
    "mock.message.send": "mock.message.send",
    "mock.secret.read": "mock.secret.read",
    "mock.delegate": "mock.delegate",
}


def _safe_target(target: str) -> bool:
    if not isinstance(target, str) or not target or "\\" in target or "\x00" in target:
        return False
    if not (target.startswith("sandbox:/") or target.startswith("mock://")):
        return False
    return not any(part in (".", "..") for part in target.split("/"))


def _time_ok(value: object) -> bool:
    return type(value) is int and value >= 0


@dataclass(frozen=True)
class ToolCall:
    actor: str
    tool: str
    target: str
    requested_at: int
    executed_at: int
    classification: str = "clear"  # ambiguous is fail-closed
    delegated_from: str | None = None


@dataclass(frozen=True)
class Grant:
    subject: str
    tool: str
    target: str
    valid_from: int
    valid_until: int
    approver: str
    may_delegate: bool = False


def _valid_grant(grant: Grant, subject: str, tool: str, target: str, now: int,
                 require_delegation: bool = False) -> bool:
    return (grant.subject == subject and grant.tool == tool and grant.target == target
            and grant.approver.startswith("human:") and len(grant.approver) > len("human:")
            and _time_ok(grant.valid_from) and _time_ok(grant.valid_until)
            and grant.valid_from <= now < grant.valid_until
            and (not require_delegation or grant.may_delegate))


def evaluate(call: ToolCall, arm: str, grants: tuple[Grant, ...] = (),
             revoked: frozenset[Grant] = frozenset()) -> dict:
    """Evaluate a mock call; no filesystem, network or message effects ever occur.

    The mock 'human:' approver marker is not a real signature or identity check.
    """
    if arm not in ARMS:
        raise ValueError("unknown arm")
    if not isinstance(call.actor, str) or not call.actor.strip():
        raise ValueError("missing actor")
    if not _time_ok(call.requested_at) or not _time_ok(call.executed_at) or call.executed_at < call.requested_at:
        raise ValueError("invalid time ordering")
    if not _safe_target(call.target):
        raise ValueError("only mock/sandbox targets permitted")
    if call.classification not in ("clear", "ambiguous"):
        raise ValueError("invalid classification")
    if call.delegated_from is not None and (not isinstance(call.delegated_from, str) or not call.delegated_from.strip() or call.delegated_from == call.actor):
        raise ValueError("invalid delegation")
    canonical_tool = TOOL_ALIASES.get(call.tool)
    if not isinstance(call.tool, str):
        raise ValueError("invalid tool")

    if arm != "enforced_boundary":
        allowed, reason = True, "no_boundary" if arm == "no_gate" else "ui_only_not_enforced"
    elif canonical_tool is None:
        allowed, reason = False, "unknown_tool"
    elif call.classification == "ambiguous":
        allowed, reason = False, "ambiguous_authority"
    else:
        live_grants = tuple(g for g in grants if isinstance(g, Grant) and g not in revoked)
        has_direct = any(_valid_grant(g, call.actor, canonical_tool, call.target, call.executed_at) for g in live_grants)
        if not has_direct:
            allowed, reason = False, "no_current_scoped_grant"
        elif call.delegated_from is not None and not any(
            _valid_grant(g, call.delegated_from, canonical_tool, call.target, call.executed_at, True)
            for g in live_grants
        ):
            allowed, reason = False, "delegation_not_authorized"
        else:
            allowed, reason = True, "current_scoped_grant"

    request = {"actor": call.actor, "tool": call.tool, "canonical_tool": canonical_tool,
               "target": call.target, "requested_at": call.requested_at,
               "executed_at": call.executed_at, "classification": call.classification,
               "delegated_from": call.delegated_from}
    return {"arm": arm, "request_sha256": hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest(),
            "decision": "mock_executed" if allowed else "blocked", "reason": reason,
            "approval_ui_visible": arm == "cosmetic_approval",
            "real_side_effects": False}


def demo() -> list[dict]:
    """Three-arm demonstration on one deliberately unapproved synthetic action."""
    call = ToolCall("mock-agent", "mock.file.write", "sandbox:/workspace/locked/example.txt", 10, 12)
    return [evaluate(call, arm) for arm in ARMS]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="print deterministic mock decisions; no real actions")
    args = parser.parse_args()
    if args.demo:
        print(json.dumps({"status": "mock_demonstration_not_research", "receipts": demo()}, indent=2))
    else:
        parser.print_help()
