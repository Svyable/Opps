#!/usr/bin/env python3
"""Local-only, run-bound supervisor receipt demonstration (not security certification).

Threat model: a separate worker can lie in its narrative and alter its own output,
but cannot read the supervisor/verifier's HMAC key or compromise those processes.
The verifier must maintain a durable used-run registry in a real integration.
This demo uses an in-memory registry and an ephemeral temp directory. No agent,
network, external system, independent attestor, or trusted clock is involved.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import re
import secrets
import subprocess
import sys
import tempfile
from pathlib import Path

FIELDS = {"version", "run_id", "action_id", "args_sha256", "returncode",
          "observed_sha256", "coverage", "source"}
WORKER = ("import pathlib,sys; "
          "pathlib.Path(sys.argv[1]).write_bytes(bytes.fromhex(sys.argv[2]))")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _mac(key: bytes, receipt: dict) -> str:
    canonical = json.dumps(receipt, sort_keys=True, separators=(",", ":"),
                           ensure_ascii=True, allow_nan=False).encode("ascii")
    return hmac.new(key, canonical, hashlib.sha256).hexdigest()


def observe_local_action(key: bytes, payload: bytes, mode: str = "success",
                         narrative: str = "done") -> dict:
    """Run a real, isolated subprocess and sign the supervisor's observations."""
    if not isinstance(key, bytes) or len(key) < 32:
        raise ValueError("supervisor key must be at least 32 bytes")
    if not isinstance(payload, bytes) or len(payload) > 4096:
        raise ValueError("payload must be bytes, at most 4096 bytes")
    if mode not in {"success", "fail", "tamper", "missing"}:
        raise ValueError("invalid mode")
    with tempfile.TemporaryDirectory(prefix="receipt-demo-") as temp:
        target = Path(temp) / "out.bin"
        cmd = [sys.executable, "-c", WORKER, str(target), payload.hex()]
        if mode == "fail":
            cmd = [sys.executable, "-c", "import sys;sys.exit(7)"]
        proc = subprocess.run(cmd, capture_output=True, timeout=5, check=False)
        if mode == "tamper" and target.exists():
            target.write_bytes(b"changed after execution")
        observed = target.read_bytes() if target.exists() else None
        receipt = {
            "version": 1,
            "run_id": secrets.token_hex(16),
            "action_id": "isolated-local-write",
            "args_sha256": digest(payload),
            "returncode": proc.returncode,
            "observed_sha256": digest(observed) if observed is not None and mode != "missing" else None,
            "coverage": "unknown" if mode == "missing" else "complete",
            "source": "unattested_local_supervisor",
        }
    return {"receipt": receipt, "mac": _mac(key, receipt),
            "untrusted_narrative": narrative}


def verify_local_receipt(envelope: dict, key: bytes, expected_run_id: str,
                         expected_payload: bytes, used_run_ids: set[str]) -> str:
    """Fail closed on forged, altered, cross-run or replayed receipts.

    Returns supported/refuted/insufficient_evidence. A valid MAC proves only
    possession of a shared key, NOT an independent hardware/software attestor.
    """
    abstain = "insufficient_evidence"
    if not isinstance(key, bytes) or len(key) < 32:
        raise ValueError("verifier key must be at least 32 bytes")
    if not isinstance(expected_payload, bytes) or not isinstance(used_run_ids, set):
        raise TypeError("invalid verifier context")
    if not isinstance(envelope, dict) or not isinstance(envelope.get("receipt"), dict):
        return abstain
    r = envelope["receipt"]
    if set(r) != FIELDS or r.get("version") != 1:
        return abstain
    if not isinstance(r["run_id"], str) or not re.fullmatch(r"[0-9a-f]{32}", r["run_id"]):
        return abstain
    if r["run_id"] != expected_run_id or r["run_id"] in used_run_ids:
        return abstain
    if r["action_id"] != "isolated-local-write" or r["args_sha256"] != digest(expected_payload):
        return abstain
    if r["source"] != "unattested_local_supervisor":
        return abstain
    if type(r["returncode"]) is not int or r["coverage"] not in {"complete", "unknown"}:
        return abstain
    observed = r["observed_sha256"]
    if observed is not None and (not isinstance(observed, str) or
                                 not re.fullmatch(r"[0-9a-f]{64}", observed)):
        return abstain
    supplied_mac = envelope.get("mac")
    if not isinstance(supplied_mac, str) or not re.fullmatch(r"[0-9a-f]{64}", supplied_mac):
        return abstain
    if not hmac.compare_digest(supplied_mac, _mac(key, r)):
        return abstain
    used_run_ids.add(r["run_id"])
    if r["coverage"] != "complete":
        return abstain
    if r["returncode"] == 0 and observed == digest(expected_payload):
        return "supported"
    if r["returncode"] == 7 and observed is None:
        return "refuted"
    return abstain


if __name__ == "__main__":
    key = secrets.token_bytes(32)
    payload = b"public-demo"
    for mode in ("success", "fail", "tamper", "missing"):
        e = observe_local_action(key, payload, mode)
        print(mode, verify_local_receipt(e, key, e["receipt"]["run_id"],
                                         payload, set()))
