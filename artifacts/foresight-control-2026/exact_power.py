#!/usr/bin/env python3
"""Prospective paired-binary design calibration; no agent runs or outcomes.

This is a planning calculation under independent-pair multinomial assumptions,
NOT a claim of empirical efficacy or a substitute for a preregistered analysis.
"""
from __future__ import annotations

import argparse
import json
from math import comb, isfinite


def exact_one_sided_p(benefit: int, harm: int) -> float:
    """McNemar exact one-sided p for benefit > harm among discordant pairs."""
    if not all(type(x) is int and x >= 0 for x in (benefit, harm)):
        raise ValueError("counts must be nonnegative integers")
    discordant = benefit + harm
    if not discordant:
        return 1.0
    return sum(comb(discordant, k) for k in range(benefit, discordant + 1)) / 2**discordant


def unconditional_power(n: int, p_benefit: float, p_harm: float, alpha: float = 0.025) -> float:
    """Enumerate multinomial paired outcomes under stated i.i.d. assumptions."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    if not all(isinstance(x, (int, float)) and isfinite(x) for x in (p_benefit, p_harm, alpha)):
        raise ValueError("probabilities must be finite")
    if min(p_benefit, p_harm) < 0 or p_benefit + p_harm > 1 or not 0 < alpha < 1:
        raise ValueError("invalid probability or alpha")
    p_same = 1 - p_benefit - p_harm
    total = 0.0
    for b in range(n + 1):
        for h in range(n - b + 1):
            if exact_one_sided_p(b, h) <= alpha:
                same = n - b - h
                total += (comb(n, b) * comb(n - b, h)
                          * p_benefit**b * p_harm**h * p_same**same)
    return min(1.0, total)


def planning_table():
    """Sensitivity grid, not an empirical effect-size estimate."""
    assumptions = ((0.30, 0.10), (0.40, 0.05), (0.50, 0.05))
    return [{"pairs": n, "p_benefit": b, "p_harm": h,
             "net_difference": round(b - h, 2),
             "power_at_alpha_0_025": round(unconditional_power(n, b, h), 4)}
            for n in (20, 40, 80) for b, h in assumptions]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print exact sensitivity grid")
    args = parser.parse_args()
    if args.json:
        print(json.dumps({"status": "planning_only_no_outcomes", "assumptions":
              "independent matched pairs; 2 prespecified contrasts; conservative per-contrast alpha=0.025",
              "grid": planning_table()}, indent=2))
    else:
        parser.print_help()
