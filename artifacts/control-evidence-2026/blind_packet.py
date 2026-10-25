#!/usr/bin/env python3
"""Create prospective reviewer packets without exposing adjudication labels.

Not an independent evaluation. Never commit source truth, secret, or generated packets.
"""
import argparse
import hashlib
import hmac
import json
import os
from pathlib import Path

VERDICTS = {"supported", "refuted", "insufficient_evidence"}
CLAIMS = {"action_completed", "approval_before_action", "alert_delivered"}
PUBLIC_FIELDS = ("claim_type", "scope_id", "action_id", "args_digest", "coverage", "coverage_writer", "events")


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def prepare(source_bytes, secret):
    if len(secret) < 32:
        raise ValueError("secret file must contain at least 32 bytes")
    source = json.loads(source_bytes)
    if not isinstance(source, dict) or not isinstance(source.get("dataset_id"), str) or not source["dataset_id"]:
        raise ValueError("dataset_id required")
    cases = source.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("nonempty cases array required")
    seen = set()
    rows = []
    private = []
    for c in cases:
        if not isinstance(c, dict):
            raise ValueError("each case must be an object")
        if set(c) != set(PUBLIC_FIELDS) | {"case_id", "expected_verdict"}:
            raise ValueError("unexpected/missing case fields; fail closed on possible label leakage")
        cid = c["case_id"]
        if not isinstance(cid, str) or not cid or cid in seen:
            raise ValueError("missing or duplicate case_id")
        seen.add(cid)
        if c["claim_type"] not in CLAIMS or c["expected_verdict"] not in VERDICTS:
            raise ValueError("invalid claim or label")
        if any(not isinstance(c[k], str) or not c[k] for k in ("scope_id", "action_id", "args_digest")):
            raise ValueError("invalid identity fields")
        if c["coverage"] not in {"complete", "partial", "unknown"} or c["coverage_writer"] not in {"independent", "agent", "unknown"}:
            raise ValueError("invalid coverage metadata")
        if not isinstance(c["events"], list) or any(not isinstance(e, dict) for e in c["events"]):
            raise ValueError("events must be a list of objects")
        event_fields = {"kind", "at", "writer", "scope_id", "action_id", "args_digest"}
        if any(not set(e).issubset(event_fields) for e in c["events"]):
            raise ValueError("unexpected event fields; possible label leakage")
        rid = hmac.new(secret, cid.encode("utf-8"), hashlib.sha256).hexdigest()[:24]
        rows.append({"review_id": rid, **{k: c[k] for k in PUBLIC_FIELDS}})
        private.append({"review_id": rid, "case_id": cid, "expected_verdict": c["expected_verdict"]})
    rows.sort(key=lambda r: r["review_id"])
    private.sort(key=lambda r: r["review_id"])
    binding = {"schema_version": 1, "dataset_id": source["dataset_id"],
               "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
               "case_count": len(rows)}
    reviewer = {**binding, "packet_type": "reviewer_blinded", "cases": rows}
    key = {**binding, "packet_type": "PRIVATE_LABEL_KEY", "labels": private}
    return reviewer, key


def exclusive_write(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(canonical(data) + b"\n")
    except BaseException:
        Path(path).unlink(missing_ok=True)
        raise


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True)
    p.add_argument("--secret-file", required=True)
    p.add_argument("--reviewer-out", required=True)
    p.add_argument("--private-key-out", required=True)
    a = p.parse_args()
    paths = [Path(x).resolve() for x in (a.source, a.secret_file, a.reviewer_out, a.private_key_out)]
    if len(set(paths)) != 4 or any(x.exists() for x in paths[2:]):
        p.error("all paths must be distinct and output files must not exist")
    reviewer, key = prepare(Path(a.source).read_bytes(), Path(a.secret_file).read_bytes())
    exclusive_write(a.private_key_out, key)
    try:
        exclusive_write(a.reviewer_out, reviewer)
    except BaseException:
        Path(a.private_key_out).unlink(missing_ok=True)
        raise
    print("Prepared", reviewer["case_count"], "reviewer cases; no adjudications performed")
    print("source_sha256:", reviewer["source_sha256"])


if __name__ == "__main__":
    main()
