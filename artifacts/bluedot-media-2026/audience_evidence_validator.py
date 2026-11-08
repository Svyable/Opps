#!/usr/bin/env python3
"""Validate FIRST-PARTY creator audience evidence for BlueDot Media Grants.

No metrics are fetched or inferred. Input must be exported from a channel's
owner analytics; this program only checks and summarizes submitted rows.
No network calls, no secrets, no external submissions.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

REQUIRED = ("channel", "period_start", "period_end", "views", "watch_hours",
            "subscribers_gained", "source_export", "owner_attested")
DATE = "%Y-%m-%d"

def parse_rows(path):
    raw = Path(path).read_bytes()
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not set(REQUIRED).issubset(reader.fieldnames):
            raise ValueError("missing required CSV columns: " + ", ".join(REQUIRED))
        rows = list(reader)
    if not rows:
        raise ValueError("no analytics rows")
    channels = {}
    for i, row in enumerate(rows, 2):
        try:
            channel = row["channel"].strip()
            start = dt.datetime.strptime(row["period_start"], DATE).date()
            end = dt.datetime.strptime(row["period_end"], DATE).date()
            views = int(row["views"])
            hours = float(row["watch_hours"])
            gained = int(row["subscribers_gained"])
            source = row["source_export"].strip()
            attested = row["owner_attested"].strip().lower()
        except (TypeError, ValueError, KeyError) as e:
            raise ValueError(f"invalid row {i}: {e}") from e
        if not channel or not source or attested != "yes":
            raise ValueError(f"row {i}: channel, owner attestation and export reference required")
        if end < start or end > dt.date.today() or (end-start).days > 366:
            raise ValueError(f"row {i}: invalid or future period")
        if not math.isfinite(hours) or views < 0 or hours < 0 or gained < 0:
            raise ValueError(f"row {i}: negative count not allowed")
        item = channels.setdefault(channel, {"periods": [], "views": 0, "watch_hours": 0.0,
                                              "subscribers_gained": 0, "sources": []})
        for previous in item["periods"]:
            if start <= previous[1] and end >= previous[0]:
                raise ValueError(f"row {i}: overlapping periods for {channel}; cannot add safely")
        item["periods"].append((start, end))
        item["views"] += views
        item["watch_hours"] += hours
        item["subscribers_gained"] += gained
        item["sources"].append(source)
    output = {}
    for channel, item in sorted(channels.items()):
        output[channel] = {"views": item["views"], "watch_hours": round(item["watch_hours"], 3),
                           "subscribers_gained": item["subscribers_gained"],
                           "periods": sorted([{"start": a.isoformat(), "end": b.isoformat()}
                                               for a, b in item["periods"]], key=lambda p:p["start"]),
                           "export_references": item["sources"]}
    return {"status": "owner-attested CSV, NOT independently verified",
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "channels": output,
            "limitations": ["Owner attestation is not proof of platform authenticity",
                            "Subscriber gains are not current subscriber counts",
                            "Period sums do not establish unique viewers or audience demographics",
                            "Submit original first-party exports separately for review"]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", help="Owner-exported analytics CSV, never a fabricated sample")
    parser.add_argument("--out", help="JSON destination; stdout if omitted")
    args = parser.parse_args()
    payload = json.dumps(parse_rows(args.csv), indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

if __name__ == "__main__":
    main()
