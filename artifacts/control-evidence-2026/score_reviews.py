#!/usr/bin/env python3
"""Score prospective blinded judgments against a private *reference* key.

Reference labels are NOT automatically ground truth. Synthetic fixtures are not
independent evaluation. Run only after reviewers have frozen their responses.
"""
import argparse
import json
import math
import os
from collections import Counter, defaultdict
from pathlib import Path

VERDICTS = {"supported", "refuted", "insufficient_evidence", "no_decision"}
LABELS = VERDICTS - {"no_decision"}
BINDING = ("schema_version", "dataset_id", "source_sha256", "case_count")


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return None
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [round(max(0.0, mid - half), 6), round(min(1.0, mid + half), 6)]


def _binding(d):
    if not isinstance(d, dict) or any(k not in d for k in BINDING):
        raise ValueError("missing dataset binding")
    b = tuple(d[k] for k in BINDING)
    if b[0] != 1 or not isinstance(b[1], str) or not b[1] or not isinstance(b[2], str) or len(b[2]) != 64 or not isinstance(b[3], int) or isinstance(b[3], bool) or b[3] <= 0:
        raise ValueError("invalid dataset binding")
    try:
        int(b[2], 16)
    except ValueError as e:
        raise ValueError("invalid source hash") from e
    return b


def score(packet, key, responses):
    """No ground-truth claims; all rates are conditional on the private labels."""
    b = _binding(packet)
    if b != _binding(key) or b != _binding(responses):
        raise ValueError("source/dataset binding mismatch")
    if packet.get("packet_type") != "reviewer_blinded" or key.get("packet_type") != "PRIVATE_LABEL_KEY" or responses.get("packet_type") != "reviewer_responses":
        raise ValueError("incorrect packet type")
    if set(packet) != set(BINDING) | {"packet_type", "cases"} or set(key) != set(BINDING) | {"packet_type", "labels"} or set(responses) != set(BINDING) | {"packet_type", "judgments"}:
        raise ValueError("unexpected top-level fields")
    cases, labels, judgments = packet["cases"], key["labels"], responses["judgments"]
    if not isinstance(cases, list) or not isinstance(labels, list) or not isinstance(judgments, list):
        raise ValueError("invalid case, label or judgment list")
    if len(cases) != b[3] or len(labels) != b[3]:
        raise ValueError("case count mismatch")
    case_ids = []
    for c in cases:
        if not isinstance(c, dict) or not isinstance(c.get("review_id"), str) or not c["review_id"]:
            raise ValueError("invalid reviewer packet case")
        case_ids.append(c["review_id"])
    if len(set(case_ids)) != len(case_ids):
        raise ValueError("duplicate case IDs")
    ref = {}
    for l in labels:
        if not isinstance(l, dict) or set(l) != {"review_id", "case_id", "expected_verdict"} or not isinstance(l["case_id"], str) or not l["case_id"] or l["expected_verdict"] not in LABELS:
            raise ValueError("invalid reference label")
        rid = l["review_id"]
        if rid in ref:
            raise ValueError("duplicate reference label")
        ref[rid] = l["expected_verdict"]
    if set(ref) != set(case_ids):
        raise ValueError("reference labels do not match blinded cases")
    if not judgments:
        raise ValueError("no reviewer responses")
    by_reviewer = defaultdict(dict)
    for j in judgments:
        if not isinstance(j, dict) or set(j) != {"reviewer_id", "review_id", "verdict"}:
            raise ValueError("invalid judgment fields")
        reviewer, rid, verdict = j["reviewer_id"], j["review_id"], j["verdict"]
        if not isinstance(reviewer, str) or not reviewer.strip() or rid not in ref or verdict not in VERDICTS:
            raise ValueError("invalid reviewer, case or verdict")
        if rid in by_reviewer[reviewer]:
            raise ValueError("duplicate reviewer-case judgment")
        by_reviewer[reviewer][rid] = verdict
    # Each reviewer must explicitly mark every case, including no_decision.
    for reviewer, answers in by_reviewer.items():
        if set(answers) != set(ref):
            raise ValueError(f"incomplete reviewer {reviewer}: missing decisions must be explicit no_decision")
    reports = []
    for reviewer in sorted(by_reviewer):
        answers = by_reviewer[reviewer]
        matrix = {label: dict(sorted(Counter(answers[rid] for rid in ref if ref[rid] == label).items())) for label in sorted(LABELS)}
        unsupported = [rid for rid, label in ref.items() if label != "supported"]
        false_support = sum(answers[rid] == "supported" for rid in unsupported)
        abstain = sum(v == "insufficient_evidence" for v in answers.values())
        no_decision = sum(v == "no_decision" for v in answers.values())
        correct = sum(answers[rid] == label for rid, label in ref.items())
        reports.append({
            "reviewer_id": reviewer,
            "case_count": len(ref),
            "reference_label_agreement": {"count": correct, "denominator": len(ref), "rate": round(correct / len(ref), 6), "wilson_95": wilson(correct, len(ref))},
            "support_on_non_support_reference": {"count": false_support, "denominator": len(unsupported), "rate": round(false_support / len(unsupported), 6) if unsupported else None, "wilson_95": wilson(false_support, len(unsupported))},
            "insufficient_evidence_verdicts": abstain,
            "explicit_no_decision": no_decision,
            "confusion_by_reference": matrix,
        })
    return {"schema_version": 1, "dataset_id": b[1], "source_sha256": b[2], "case_count": b[3],
            "reference_is_ground_truth": False,
            "warning": "Reference-label agreement only. Independent ground truth, recorder integrity, and reviewer blinding require external verification; synthetic data must never be described as empirical validation.",
            "reviewers": reports}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--packet", required=True)
    p.add_argument("--private-key", required=True)
    p.add_argument("--responses", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    paths = [Path(x).resolve() for x in (a.packet, a.private_key, a.responses, a.output)]
    if len(set(paths)) != 4 or paths[3].exists():
        p.error("paths must be distinct and output must not exist")
    result = score(*(json.loads(path.read_text(encoding="utf-8")) for path in paths[:3]))
    # Fail closed: exclusive create with restrictive permissions.
    fd = os.open(paths[3], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(result, f, sort_keys=True, separators=(",", ":"))
            f.write("\n")
    except BaseException:
        paths[3].unlink(missing_ok=True)
        raise
    print(f"Scored {len(result['reviewers'])} reviewer(s) on {result['case_count']} cases; reference labels are NOT verified ground truth")


if __name__ == "__main__":
    main()
