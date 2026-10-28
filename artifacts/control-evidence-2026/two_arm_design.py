#!/usr/bin/env python3
"""Prospective two-arm reviewer allocation for Control Evidence (not a study result).

Uses blinded packets from blind_packet.py. Never commit reviewer narratives, packets,
secrets, responses, reference keys, or generated allocation files.
"""
import hashlib
import hmac
from collections import defaultdict

VERDICTS = {"supported", "refuted", "insufficient_evidence", "no_decision"}
BINDING = ("schema_version", "dataset_id", "source_sha256", "case_count")
ARMS = ("narrative_only", "narrative_plus_receipts")
EVIDENCE_FIELDS = ("scope_id", "action_id", "args_digest", "coverage", "coverage_writer", "events")


def _binding(data):
    if not isinstance(data, dict) or any(k not in data for k in BINDING):
        raise ValueError("missing binding")
    b = {k: data[k] for k in BINDING}
    if (b["schema_version"] != 1 or not isinstance(b["dataset_id"], str)
            or not b["dataset_id"] or not isinstance(b["source_sha256"], str)
            or len(b["source_sha256"]) != 64 or not isinstance(b["case_count"], int)
            or isinstance(b["case_count"], bool) or b["case_count"] <= 0):
        raise ValueError("invalid binding")
    try:
        int(b["source_sha256"], 16)
    except ValueError as exc:
        raise ValueError("invalid source digest") from exc
    return b


def allocate(packet, narratives, secret, reviewers=("R1", "R2")):
    """Balance receipt exposure by claim type without reading reference labels.

    Every reviewer sees each case once, and each case is evaluated once per arm
    by different reviewers. Two-reviewer minimum is deliberate; further blinded
    reliability replication requires separately consented additional reviewers.
    """
    binding = _binding(packet)
    if packet.get("packet_type") != "reviewer_blinded" or set(packet) != set(BINDING) | {"packet_type", "cases"}:
        raise ValueError("expected exact blinded packet schema")
    if not isinstance(secret, bytes) or len(secret) < 32:
        raise ValueError("secret must be at least 32 bytes")
    if (not isinstance(reviewers, (tuple, list)) or len(reviewers) != 2
            or any(not isinstance(r, str) or not r.strip() for r in reviewers)
            or reviewers[0] == reviewers[1]):
        raise ValueError("two distinct reviewer identifiers required")
    cases = packet["cases"]
    if not isinstance(cases, list) or len(cases) != binding["case_count"]:
        raise ValueError("case count mismatch")
    if not isinstance(narratives, dict):
        raise ValueError("narratives must be mapping from blinded review ID to text")
    by_claim = defaultdict(list)
    seen = set()
    for c in cases:
        if not isinstance(c, dict) or set(c) != {"review_id", "claim_type", *EVIDENCE_FIELDS}:
            raise ValueError("unexpected case fields; possible label leakage")
        rid = c["review_id"]
        if not isinstance(rid, str) or not rid or rid in seen:
            raise ValueError("missing or duplicate review ID")
        seen.add(rid)
        if not isinstance(c["claim_type"], str) or not c["claim_type"]:
            raise ValueError("invalid claim type")
        by_claim[c["claim_type"]].append(c)
    if set(narratives) != seen or any(not isinstance(v, str) or not v.strip() for v in narratives.values()):
        raise ValueError("narratives must cover every case with nonempty text")
    allocations = {r: [] for r in reviewers}
    private = []
    for claim_type in sorted(by_claim):
        group = sorted(by_claim[claim_type], key=lambda c: hmac.new(secret, c["review_id"].encode(), hashlib.sha256).digest())
        offset = hmac.new(secret, ("offset:" + claim_type).encode(), hashlib.sha256).digest()[0] % 2
        for idx, c in enumerate(group):
            receipt_reviewer = reviewers[(idx + offset) % 2]
            for reviewer in reviewers:
                arm = ARMS[1] if reviewer == receipt_reviewer else ARMS[0]
                row = {"review_id": c["review_id"], "claim_type": c["claim_type"],
                       "narrative": narratives[c["review_id"]], "arm": arm}
                if arm == ARMS[1]:
                    row.update({k: c[k] for k in EVIDENCE_FIELDS})
                allocations[reviewer].append(row)
                private.append({"review_id": c["review_id"], "reviewer_id": reviewer, "arm": arm})
    packets = {r: {**binding, "packet_type": "two_arm_reviewer", "reviewer_id": r,
                   "cases": sorted(allocations[r], key=lambda c: c["review_id"])} for r in reviewers}
    assignment = {**binding, "packet_type": "PRIVATE_TWO_ARM_ASSIGNMENT",
                  "assignments": sorted(private, key=lambda x: (x["review_id"], x["reviewer_id"]))}
    return packets, assignment


def summarize(assignment, key, responses):
    """Count reference-label comparisons after responses are frozen.

    Responses format: {reviewer_id: {review_id: verdict}}. Does not claim labels
    are authenticated ground truth or calculate causal significance.
    """
    binding = _binding(assignment)
    if binding != _binding(key) or assignment.get("packet_type") != "PRIVATE_TWO_ARM_ASSIGNMENT" or key.get("packet_type") != "PRIVATE_LABEL_KEY":
        raise ValueError("mismatched bindings or packet types")
    labels = key.get("labels")
    rows = assignment.get("assignments")
    if not isinstance(labels, list) or not isinstance(rows, list) or len(labels) != binding["case_count"] or len(rows) != 2 * binding["case_count"]:
        raise ValueError("invalid label/assignment counts")
    ref = {}
    for x in labels:
        if not isinstance(x, dict) or set(x) != {"review_id", "case_id", "expected_verdict"} or x.get("expected_verdict") not in VERDICTS - {"no_decision"} or x.get("review_id") in ref:
            raise ValueError("invalid or duplicate reference label")
        ref[x["review_id"]] = x["expected_verdict"]
    if not isinstance(responses, dict):
        raise ValueError("responses must be a reviewer mapping")
    expected = defaultdict(set)
    case_arms = defaultdict(set)
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"review_id", "reviewer_id", "arm"} or row["review_id"] not in ref or row["arm"] not in ARMS:
            raise ValueError("invalid assignment row")
        pair = (row["review_id"], row["arm"])
        if pair in case_arms[row["review_id"]]:
            raise ValueError("duplicate assignment")
        case_arms[row["review_id"]].add(pair)
        if row["review_id"] in expected[row["reviewer_id"]]:
            raise ValueError("same reviewer sees case twice")
        expected[row["reviewer_id"]].add(row["review_id"])
    if set(case_arms) != set(ref) or any(len(v) != 2 for v in case_arms.values()) or set(responses) != set(expected):
        raise ValueError("missing case, arm or reviewer")
    for reviewer, cases in expected.items():
        if not isinstance(responses[reviewer], dict) or set(responses[reviewer]) != cases or any(v not in VERDICTS for v in responses[reviewer].values()):
            raise ValueError("incomplete, unknown or invalid reviewer decisions")
    by_arm = {arm: {"decisions": 0, "reference_agreement": 0, "support_on_non_support_reference": 0,
                    "non_support_reference": 0, "insufficient_evidence": 0, "no_decision": 0} for arm in ARMS}
    for row in rows:
        verdict = responses[row["reviewer_id"]][row["review_id"]]
        truth = ref[row["review_id"]]
        out = by_arm[row["arm"]]
        out["decisions"] += 1
        out["reference_agreement"] += verdict == truth
        out["non_support_reference"] += truth != "supported"
        out["support_on_non_support_reference"] += truth != "supported" and verdict == "supported"
        out["insufficient_evidence"] += verdict == "insufficient_evidence"
        out["no_decision"] += verdict == "no_decision"
    return {"dataset_id": binding["dataset_id"], "case_count": binding["case_count"], "by_arm": by_arm,
            "reference_is_ground_truth": False,
            "warning": "Prospective reference-label counts only; independent ground truth, reviewer blinding, case clustering and external validity unverified. No causal or safety-effect claim."}
