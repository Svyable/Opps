#!/usr/bin/env python3
"""Pre-registered paired false-support analysis for the Control Evidence pilot.

No human data or authenticated ground truth is supplied here. Reference labels
are inputs, not facts independently verified by this software.
"""
from collections import defaultdict
from math import comb

ARMS = ("narrative_only", "narrative_plus_receipts")
VERDICTS = {"supported", "refuted", "insufficient_evidence", "no_decision"}
REFERENCE_VERDICTS = VERDICTS - {"no_decision"}
BINDING = ("schema_version", "dataset_id", "source_sha256", "case_count")


def _binding(data):
    if not isinstance(data, dict) or any(k not in data for k in BINDING):
        raise ValueError("missing dataset binding")
    b = {k: data[k] for k in BINDING}
    if (b["schema_version"] != 1 or not isinstance(b["dataset_id"], str)
            or not b["dataset_id"] or not isinstance(b["source_sha256"], str)
            or len(b["source_sha256"]) != 64 or not isinstance(b["case_count"], int)
            or isinstance(b["case_count"], bool) or b["case_count"] <= 0):
        raise ValueError("invalid dataset binding")
    try:
        int(b["source_sha256"], 16)
    except ValueError as exc:
        raise ValueError("invalid source hash") from exc
    return b


def exact_mcnemar_p(beneficial, harmful):
    """Two-sided exact conditional McNemar p, based only on discordant pairs."""
    if (not isinstance(beneficial, int) or isinstance(beneficial, bool)
            or not isinstance(harmful, int) or isinstance(harmful, bool)
            or min(beneficial, harmful) < 0):
        raise ValueError("discordance counts must be nonnegative integers")
    n = beneficial + harmful
    if not n:
        return 1.0
    k = min(beneficial, harmful)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / (2 ** n))


def paired_false_support(assignment, key, responses):
    """Summarize per-case paired errors for reference-non-support cases.

    The primary estimand is (narrative-only false-support count minus
    receipt-supported false-support count) / non-support case count.
    Missing judgments are rejected, not treated as correct. All results are
    conditional on supplied reference labels, not authenticated ground truth.
    """
    binding = _binding(assignment)
    if (_binding(key) != binding or assignment.get("packet_type") != "PRIVATE_TWO_ARM_ASSIGNMENT"
            or key.get("packet_type") != "PRIVATE_LABEL_KEY"):
        raise ValueError("packet types or dataset bindings disagree")
    labels, rows = key.get("labels"), assignment.get("assignments")
    if (not isinstance(labels, list) or len(labels) != binding["case_count"]
            or not isinstance(rows, list) or len(rows) != 2 * binding["case_count"]
            or not isinstance(responses, dict)):
        raise ValueError("invalid label, assignment or response counts")
    ref, case_ids = {}, set()
    for label in labels:
        if (not isinstance(label, dict) or set(label) != {"review_id", "case_id", "expected_verdict"}
                or not isinstance(label["review_id"], str) or not label["review_id"]
                or not isinstance(label["case_id"], str) or not label["case_id"]
                or label["review_id"] in ref or label["case_id"] in case_ids
                or label["expected_verdict"] not in REFERENCE_VERDICTS):
            raise ValueError("invalid or duplicate reference label")
        ref[label["review_id"]] = label["expected_verdict"]
        case_ids.add(label["case_id"])
    paired = defaultdict(dict)
    expected = defaultdict(set)
    for row in rows:
        if (not isinstance(row, dict) or set(row) != {"review_id", "reviewer_id", "arm"}
                or row["review_id"] not in ref or row["arm"] not in ARMS
                or not isinstance(row["reviewer_id"], str) or not row["reviewer_id"]):
            raise ValueError("invalid assignment row")
        rid, reviewer, arm = row["review_id"], row["reviewer_id"], row["arm"]
        if arm in paired[rid] or rid in expected[reviewer]:
            raise ValueError("duplicate case/arm or reviewer exposure")
        paired[rid][arm] = reviewer
        expected[reviewer].add(rid)
    if (set(paired) != set(ref) or any(set(v) != set(ARMS) or len(set(v.values())) != 2 for v in paired.values())
            or set(responses) != set(expected)):
        raise ValueError("incomplete or invalid paired allocation")
    for reviewer, ids in expected.items():
        if (not isinstance(responses[reviewer], dict) or set(responses[reviewer]) != ids
                or any(verdict not in VERDICTS for verdict in responses[reviewer].values())):
            raise ValueError("incomplete or invalid reviewer responses")
    both, benefit, harm, neither, excluded = 0, 0, 0, 0, 0
    for rid, truth in ref.items():
        if truth == "supported":
            excluded += 1
            continue
        no_receipt = responses[paired[rid][ARMS[0]]][rid] == "supported"
        with_receipt = responses[paired[rid][ARMS[1]]][rid] == "supported"
        if no_receipt and with_receipt:
            both += 1
        elif no_receipt:
            benefit += 1
        elif with_receipt:
            harm += 1
        else:
            neither += 1
    n = both + benefit + harm + neither
    return {
        "dataset_id": binding["dataset_id"], "non_support_cases": n,
        "supported_reference_cases_excluded": excluded,
        "both_false_support": both,
        "narrative_only_false_support_receipts_not": benefit,
        "receipts_false_support_narrative_only_not": harm,
        "neither_false_support": neither,
        "narrative_only_false_support_rate": (both + benefit) / n if n else None,
        "receipts_false_support_rate": (both + harm) / n if n else None,
        "paired_absolute_reduction": (benefit - harm) / n if n else None,
        "discordant_pairs": benefit + harm,
        "exact_two_sided_mcnemar_p": exact_mcnemar_p(benefit, harm) if n else None,
        "reference_is_ground_truth": False,
        "warning": "Conditional on supplied reference labels; no independent authentication, randomization audit, power guarantee or real-world safety claim. The exact p-value is exploratory unless analysis and labels were frozen prospectively. Reviewer effects and clustering may remain."
    }
