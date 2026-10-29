#!/usr/bin/env python3
"""Prospective R3 adjudication gate for the Control Evidence pilot.

This software validates a *declared* independent reference register before
paired scoring. It cannot authenticate humans, recorders, or evidence itself.
Do not commit actual adjudications, assignments, responses, or identifiers.
"""
import argparse
import hashlib
import json
import os
from collections import defaultdict
from pathlib import Path

from paired_analysis import ARMS, REFERENCE_VERDICTS, _binding, paired_false_support

DECISION_FIELDS = {"review_id", "verdict", "evidence_sha256",
                   "source_verified", "coverage", "rationale"}


def _digest(value):
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _valid_sha(value):
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def freeze_reference(assignment, register):
    """Fail closed unless every assigned case has one declared R3 decision.

    The resulting PRIVATE_LABEL_KEY is an adapter for paired_analysis, not
    authenticated ground truth. R3 must not be an experimental reviewer.
    """
    binding = _binding(assignment)
    if (_binding(register) != binding
            or assignment.get("packet_type") != "PRIVATE_TWO_ARM_ASSIGNMENT"
            or register.get("packet_type") != "PRIVATE_R3_ADJUDICATION"
            or set(register) != set(binding) | {"packet_type", "adjudicator_id", "decisions"}):
        raise ValueError("wrong packet type, binding, or adjudication schema")
    rows = assignment.get("assignments")
    if not isinstance(rows, list) or len(rows) != 2 * binding["case_count"]:
        raise ValueError("incomplete assignment")
    case_arms = defaultdict(dict)
    reviewers = set()
    for row in rows:
        if (not isinstance(row, dict)
                or set(row) != {"review_id", "reviewer_id", "arm"}
                or not isinstance(row["review_id"], str) or not row["review_id"]
                or not isinstance(row["reviewer_id"], str) or not row["reviewer_id"]
                or row["arm"] not in ARMS):
            raise ValueError("invalid assignment row")
        rid, arm, reviewer = row["review_id"], row["arm"], row["reviewer_id"]
        if arm in case_arms[rid] or reviewer in case_arms[rid].values():
            raise ValueError("duplicate arm or same reviewer on both arms")
        case_arms[rid][arm] = reviewer
        reviewers.add(reviewer)
    if (len(case_arms) != binding["case_count"]
            or any(set(arms) != set(ARMS) for arms in case_arms.values())):
        raise ValueError("missing case or arm")
    r3 = register["adjudicator_id"]
    if not isinstance(r3, str) or not r3.strip() or r3 in reviewers:
        raise ValueError("R3 must have a distinct nonempty identifier")
    decisions = register["decisions"]
    if not isinstance(decisions, list) or len(decisions) != binding["case_count"]:
        raise ValueError("one R3 decision required per case")
    labels = []
    seen = set()
    for d in decisions:
        if not isinstance(d, dict) or set(d) != DECISION_FIELDS:
            raise ValueError("unexpected decision fields or author-label leakage")
        rid = d["review_id"]
        if not isinstance(rid, str) or rid not in case_arms or rid in seen:
            raise ValueError("unknown or duplicate R3 case")
        seen.add(rid)
        if (d["verdict"] not in REFERENCE_VERDICTS
                or type(d["source_verified"]) is not bool
                or d["coverage"] not in {"complete", "partial", "unknown"}
                or not isinstance(d["rationale"], str)
                or len(d["rationale"].strip()) < 15
                or (d["evidence_sha256"] is not None and not _valid_sha(d["evidence_sha256"]))):
            raise ValueError("invalid R3 decision")
        if d["verdict"] in {"supported", "refuted"} and (
                not d["source_verified"] or not _valid_sha(d["evidence_sha256"])):
            raise ValueError("support/refutation requires declared verified source evidence")
        if d["verdict"] == "supported" and d["coverage"] != "complete":
            raise ValueError("support requires declared complete coverage")
        labels.append({"review_id": rid, "case_id": "r3:" + rid,
                       "expected_verdict": d["verdict"]})
    if seen != set(case_arms):
        raise ValueError("incomplete adjudication")
    return {**binding, "packet_type": "PRIVATE_LABEL_KEY",
            "labels": sorted(labels, key=lambda x: x["review_id"]),
            "reference_origin": "R3_declared_independent_not_authenticated",
            "r3_register_sha256": _digest(register),
            "reference_is_ground_truth": False}


def score_after_r3(assignment, register, responses):
    key = freeze_reference(assignment, register)
    result = paired_false_support(assignment, key, responses)
    result["r3_register_sha256"] = key["r3_register_sha256"]
    result["reference_origin"] = key["reference_origin"]
    result["warning"] += (" R3 identity, independence, source authenticity, "
                          "coverage and evidence hashes are operator declarations, "
                          "not independently verified by this tool.")
    return result


def _private_write(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, sort_keys=True, indent=2, allow_nan=False)
        f.write("\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--assignment", required=True)
    p.add_argument("--adjudication", required=True)
    p.add_argument("--responses", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    paths = [Path(x).resolve() for x in
             (a.assignment, a.adjudication, a.responses, a.output)]
    if len(set(paths)) != 4 or paths[3].exists():
        p.error("input/output paths must be distinct; output must not exist")
    assignment, register, responses = [
        json.loads(path.read_text(encoding="utf-8")) for path in paths[:3]]
    result = score_after_r3(assignment, register, responses)
    _private_write(paths[3], result)
    print("Private paired analysis written; R3 attestations NOT independently verified.")


if __name__ == "__main__":
    main()
