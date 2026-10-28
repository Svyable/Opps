#!/usr/bin/env python3
"""Side-effect-free protocol-to-boundary smoke test; NOT an agent experiment.

Only three of five preregistered categories have an honest, explicit mapping
to the existing mock ToolCall API. Do not treat labels as observed outcomes.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from gate_runner import Grant, ToolCall, evaluate
from preregister import ARMS, make_manifest

MAPPING_VERSION = "cwic-mock-mapping-v0.1"
SUPPORTED = frozenset(("file_write", "external_message", "tool_alias_and_timing"))


def map_case(case: dict) -> tuple[ToolCall, tuple[Grant, ...]]:
    """Map a synthetic fixture to a deterministic mock, never a real tool."""
    category, label = case["category"], case["policy_label"]
    if category not in SUPPORTED or label not in ("authorized", "unauthorized", "ambiguous"):
        raise ValueError("category or label not mapped")
    index = int(case["case_id"].rsplit("-", 1)[-1])
    if not 1 <= index <= 4:
        raise ValueError("unexpected fixture index")

    if category == "file_write":
        tool = "mock.file.write"
        directory = {"authorized": "notes", "unauthorized": "locked", "ambiguous": "shared"}[label]
        target = f"sandbox:/workspace/{directory}/{index}.txt"
    elif category == "external_message":
        tool = "mock.message.send"
        directory = {"authorized": "inbox/approved", "unauthorized": "outbox/public",
                     "ambiguous": "inbox/unresolved"}[label]
        target = f"mock://{directory}/{index}"
    else:
        tool = "mock.file.write_alias"
        directory = "approved" if label == "authorized" else "alias"
        target = f"mock://tool/{directory}/{index}"

    call = ToolCall("mock-agent", tool, target, 10, 20,
                    classification="ambiguous" if label == "ambiguous" else "clear")
    canonical = "mock.file.write" if tool == "mock.file.write_alias" else tool
    if label == "authorized" or label == "ambiguous":
        grants = (Grant("mock-agent", canonical, target, 10, 30, "human:synthetic-marker"),)
    elif category == "tool_alias_and_timing":
        grants = (Grant("mock-agent", canonical, target, 10, 20, "human:synthetic-marker"),)
    else:
        grants = ()
    return call, grants


def make_pilot() -> dict:
    manifest = make_manifest()
    cases = {case["case_id"]: case for case in manifest["spec"]["scenarios"]}
    included = [case for case in cases.values() if case["category"] in SUPPORTED]
    excluded = sorted(case["case_id"] for case in cases.values()
                      if case["category"] not in SUPPORTED)
    receipts = []
    for assignment in manifest["spec"]["assignments"]:
        case = cases[assignment["case_id"]]
        if case["category"] not in SUPPORTED:
            continue
        call, grants = map_case(case)
        result = evaluate(call, assignment["arm"], grants)
        receipts.append({
            "case_id": case["case_id"],
            "policy_label_from_fixture": case["policy_label"],
            "arm": assignment["arm"],
            "source_assignment_status": assignment["status"],
            "mock_receipt": result,
        })
    counts = Counter((r["arm"], r["mock_receipt"]["decision"]) for r in receipts)
    return {
        "status": "synthetic_contract_smoke_test_not_agent_research",
        "mapping_version": MAPPING_VERSION,
        "source_manifest_sha256_spec": manifest["sha256_spec"],
        "covered_scenarios": len(included),
        "excluded_scenarios": len(excluded),
        "covered_assignments": len(receipts),
        "excluded_assignments": len(manifest["spec"]["assignments"]) - len(receipts),
        "excluded_case_ids": excluded,
        "mock_decision_counts": {
            arm: {"mock_executed": counts[(arm, "mock_executed")],
                  "blocked": counts[(arm, "blocked")]} for arm in ARMS
        },
        "all_real_side_effects_false": all(
            not r["mock_receipt"]["real_side_effects"] for r in receipts
        ),
        "receipts": receipts,
        "limitations": (
            "Fixture policy labels determine mock grants and are not independent ground truth. "
            "No AI agents, authenticated approvals, CT data, real tools, blinded reviewers or "
            "outcome measurements. Secret handling and delegation remain unmapped. "
            "All 180 prospective experimental assignments remain unrun."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", metavar="PATH", help="write full deterministic mock receipts")
    parser.add_argument("--summary", action="store_true", help="print counts, not all receipts")
    args = parser.parse_args()
    pilot = make_pilot()
    if args.write:
        Path(args.write).write_text(json.dumps(pilot, indent=2, sort_keys=True) + "\n")
        print("WROTE", args.write)
    if args.summary or not args.write:
        print(json.dumps({k: v for k, v in pilot.items() if k not in ("receipts", "excluded_case_ids")},
                         indent=2, sort_keys=True))
