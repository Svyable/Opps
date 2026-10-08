#!/usr/bin/env python3
"""Offline proxy evaluator for NIH SPARK PubMed/PMC Task 1.

This is a *development* harness, not NIH's official evaluation script.
Input: JSONL gold with qid/gold_ids; JSONL predictions with qid/ids.
No network, no external packages, no answer memorization.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from pathlib import Path


def load_jsonl(path):
    rows = {}
    with Path(path).open(encoding="utf-8") as stream:
        for lineno, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
            if not isinstance(row, dict) or not isinstance(row.get("qid"), str):
                raise ValueError(f"{path}:{lineno}: expected object with string qid")
            qid = row["qid"].strip()
            if not qid or qid in rows:
                raise ValueError(f"{path}:{lineno}: blank or duplicate qid {qid!r}")
            rows[qid] = row
    if not rows:
        raise ValueError(f"{path}: empty JSONL")
    return rows


def ids(row, key):
    values = row.get(key)
    if not isinstance(values, list) or not values or not all(
        isinstance(v, str) and v.strip() for v in values
    ):
        raise ValueError(f"qid={row['qid']!r}: {key} must be a nonempty list of IDs")
    # Do not infer PMID↔PMCID equivalence without an explicit mapping.
    normalized = [v.strip().upper() for v in values]
    if len(set(normalized)) != len(normalized):
        raise ValueError(f"qid={row['qid']!r}: duplicate {key}")
    return normalized


def evaluate(gold, predictions, k=10):
    unexpected = sorted(set(predictions) - set(gold))
    if unexpected:
        raise ValueError(f"prediction qids absent from gold: {unexpected[:8]}")
    reciprocal_ranks = []
    hit1 = 0
    recall = 0
    latencies = []
    missing = []
    for qid, truth in gold.items():
        relevant = set(ids(truth, "gold_ids"))
        prediction = predictions.get(qid)
        if prediction is None:
            missing.append(qid)
            reciprocal_ranks.append(0.0)
            continue
        candidates = prediction.get("ids")
        if not isinstance(candidates, list) or not all(
            isinstance(v, str) and v.strip() for v in candidates
        ):
            raise ValueError(f"qid={qid!r}: ids must be a list of strings")
        candidates = [v.strip().upper() for v in candidates]
        if len(set(candidates)) != len(candidates):
            raise ValueError(f"qid={qid!r}: duplicate predicted IDs")
        rank = next((i for i, item in enumerate(candidates[:k], 1) if item in relevant), None)
        reciprocal_ranks.append(1.0 / rank if rank else 0.0)
        hit1 += int(rank == 1)
        recall += int(rank is not None)
        latency = prediction.get("latency_ms")
        if latency is not None:
            if isinstance(latency, bool) or not isinstance(latency, (int, float)) or not math.isfinite(latency) or latency < 0:
                raise ValueError(f"qid={qid!r}: invalid latency_ms")
            latencies.append(float(latency))
    n = len(gold)
    result = {
        "n": n, "submitted": n - len(missing), "missing_qids": missing,
        "mrr_at_k": sum(reciprocal_ranks) / n,
        "hit_at_1": hit1 / n, "recall_at_k": recall / n,
        "k": k, "per_query_rr": reciprocal_ranks,
    }
    if latencies:
        ordered = sorted(latencies)
        result["latency_ms_p50"] = statistics.median(ordered)
        result["latency_ms_p95"] = ordered[max(0, math.ceil(.95 * len(ordered)) - 1)]
        result["latency_n"] = len(ordered)
    return result


def paired_bootstrap(a, b, draws=2000, seed=2026):
    """95% percentile CI of paired mean RR delta (a - b); descriptive, not a p-value."""
    x, y = a["per_query_rr"], b["per_query_rr"]
    if len(x) != len(y):
        raise ValueError("comparison query counts differ")
    rng = random.Random(seed)
    n = len(x)
    deltas = []
    for _ in range(draws):
        indices = [rng.randrange(n) for _ in range(n)]
        deltas.append(sum(x[i] - y[i] for i in indices) / n)
    deltas.sort()
    return {
        "mrr_delta": a["mrr_at_k"] - b["mrr_at_k"],
        "bootstrap_ci95": [deltas[int(.025 * draws)], deltas[min(draws - 1, int(.975 * draws))]],
        "draws": draws,
        "seed": seed,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", required=True, help="Local proxy gold JSONL; never hidden official labels")
    parser.add_argument("--pred", required=True, help="Ranked retrieval JSONL")
    parser.add_argument("--baseline", help="Optional baseline predictions for paired comparison")
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--output", help="Write machine-readable report to this file")
    args = parser.parse_args()
    if args.k < 1:
        parser.error("--k must be >= 1")
    gold = load_jsonl(args.gold)
    candidate = evaluate(gold, load_jsonl(args.pred), args.k)
    report = {"candidate": {k:v for k,v in candidate.items() if k != "per_query_rr"},
              "note": "Proxy-development metrics only; not an official NIH score."}
    if args.baseline:
        baseline = evaluate(gold, load_jsonl(args.baseline), args.k)
        report["baseline"] = {k:v for k,v in baseline.items() if k != "per_query_rr"}
        report["paired"] = paired_bootstrap(candidate, baseline)
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
