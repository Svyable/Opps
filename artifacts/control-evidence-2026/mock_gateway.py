"""Deterministic mock gateway: produces execution events from a policy, not scorer assertions.

This is a synthetic harness, NOT an agent experiment or independently attested trace.
"""
import json
import sys

ARMS = ("instructions_only", "external_gate")

def run_gateway(rows):
    if not isinstance(rows, list):
        raise ValueError("rows must be a list")
    events = []
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"scenario_id", "arm", "task_authorized", "policy", "call_id", "proposed_action"}:
            raise ValueError("invalid row")
        arm, call_id, action = row["arm"], row["call_id"], row["proposed_action"]
        if arm not in ARMS:
            raise ValueError("invalid arm")
        key = (arm, call_id)
        if key in seen:
            raise ValueError("duplicate call")
        seen.add(key)
        policy = row["policy"]
        if not isinstance(policy, dict) or set(policy) != {"principal", "resource", "allowed_actions"}:
            raise ValueError("invalid policy")
        allowed = policy["allowed_actions"]
        if not isinstance(allowed, list) or any(not isinstance(x, str) or not x for x in allowed) or len(set(allowed)) != len(allowed):
            raise ValueError("invalid allowed_actions")
        if action is None and call_id is None:
            continue
        if not isinstance(action, str) or not action or not isinstance(call_id, str) or not call_id:
            raise ValueError("invalid proposed call")
        # Baseline is intentionally permissive; gate checks exact membership.
        executed = arm == "instructions_only" or action in allowed
        events.append({"arm": arm, "call_id": call_id, "executed": executed})
    return events

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: mock_gateway.py proposals.jsonl")
    with open(sys.argv[1], encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    for event in run_gateway(rows):
        print(json.dumps(event, sort_keys=True))
