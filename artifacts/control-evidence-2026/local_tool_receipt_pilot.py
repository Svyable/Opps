#!/usr/bin/env python3
"""Real local subprocess evidence probe for Control Evidence (not an AI-agent study).

A separate Python worker performs a file action. The supervisor independently
observes exit status and file bytes rather than trusting a supplied narrative.
The resulting 'independent' fields are LOCAL ROLE LABELS, not authenticated
recorder attestations, trusted clocks, or evidence of deployed-agent behavior.
No network, external messages, credentials, or irreversible actions are used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _worker(target: Path, payload_hex: str, mode: str) -> int:
    if mode == "fail":
        return 7
    target.write_bytes(bytes.fromhex(payload_hex))
    return 0


def run_probe(payload: bytes, mode: str = "success", narrative: str = "completed") -> dict:
    """Capture a *real local tool process*, with deliberate failure modes.

    mode: success, fail, tamper (post-execution mutation), missing (lost receipt).
    The agent-like narrative is an untrusted input and never affects the verdict.
    """
    if mode not in {"success", "fail", "tamper", "missing"}:
        raise ValueError("unsupported probe mode")
    if not isinstance(payload, bytes) or len(payload) > 4096:
        raise ValueError("payload must be bytes no longer than 4096")
    expected_digest = sha256(payload)
    with tempfile.TemporaryDirectory(prefix="control-evidence-probe-") as directory:
        target = Path(directory) / "tool-output.bin"
        # Argument vector; no shell and no external service.
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--worker",
             str(target), payload.hex(), "fail" if mode == "fail" else "write"],
            capture_output=True, timeout=5, check=False,
        )
        if mode == "tamper" and target.exists():
            target.write_bytes(b"post-execution mutation")
        observed = target.read_bytes() if target.exists() else None
        observed_digest = sha256(observed) if observed is not None else None
        events = []
        coverage = "unknown"
        if mode != "missing":
            if result.returncode == 7 and observed is None:
                events.append("action_failed")
                coverage = "complete"
            elif result.returncode == 0 and observed_digest == expected_digest:
                events.append("action_succeeded")
                coverage = "complete"
            # A mutated or inconsistent result is *not* positive or negative proof.
        scope_id, action_id = "isolated-local-sandbox", "local-write-1"
        case = {
            "case_id": "local-probe-" + mode,
            "claim_type": "action_completed",
            "scope_id": scope_id,
            "action_id": action_id,
            "args_digest": expected_digest,
            "coverage": coverage,
            "coverage_writer": "independent" if coverage == "complete" else "unknown",
            "events": [{"kind": kind, "writer": "independent", "scope_id": scope_id,
                        "action_id": action_id, "args_digest": expected_digest}
                       for kind in events],
        }
        return {
            "case": case,
            "observations": {
                "worker_returncode": result.returncode,
                "expected_sha256": expected_digest,
                "observed_sha256": None if mode == "missing" else observed_digest,
                "coverage": coverage,
                "record_source": "local_supervisor_unattested",
                "worker_process": "separate_local_subprocess",
            },
            "untrusted_narrative": narrative,
            "limitations": "No agent, trusted recorder, independent human, or signed telemetry",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("worker_args", nargs="*")
    parser.add_argument("--mode", choices=["success", "fail", "tamper", "missing"],
                        default="success")
    args = parser.parse_args()
    if args.worker:
        if len(args.worker_args) != 3:
            parser.error("worker requires target, hex payload, and mode")
        sys.exit(_worker(Path(args.worker_args[0]), args.worker_args[1], args.worker_args[2]))
    if args.worker_args:
        parser.error("unexpected arguments")
    result = run_probe(b"public-demo-payload", mode=args.mode)
    # The verdict grammar is in contract_smoke; do not duplicate it here.
    from contract_smoke import decide
    result["contract_verdict"] = decide(result["case"])
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
