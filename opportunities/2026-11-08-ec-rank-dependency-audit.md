# EC Rank: exact negative dependency audit — 2026-11-08

## Decision and source

**PURSUE (bounded), no entry and no certified leaderboard gain.** Official [Elliptic Rank Challenge](https://github.com/Layr-Labs/elliptic-rank-challenge-public/blob/main/README.md) scores **independent rational points** in a novel curve's torsion/rank cell, not raw count of integral points. Its original-work [RULES.md](https://github.com/Layr-Labs/elliptic-rank-challenge-public/blob/main/RULES.md) forbids copied published or competitor curves and disguised twists/isogenies. The organizer's verifier requires minimality, known-curve novelty, exact point membership, torsion removal and a positive-definite canonical height pairing at two precisions. User-reported cutoff: November 14, 2026, not independently confirmed in the GitHub manifest. No confirmed individual cash award; score is not dollars.

## Concrete technical advance: falsify a misleading ranking heuristic

Previous [original exhaustive search](../artifacts/ec-rank-2026/ec_rank_probe.py) ranked curves by count of integer-x point representatives. New [exact group-law dependency audit](../artifacts/ec-rank-2026/ec_rank_relation_audit.py) uses `fractions.Fraction` and checks all P_i + P_j = ±P_k, including doubling, to detect explicit short dependencies. It does not approximate coordinates or compute height matrices.

**Local execution:** 8/8 regression tests passed in Python 3. The original search bounds (|a|≤30, |b|≤60, |x|≤20, at least six points, top five candidates) were replayed using a locally reconstructed equivalent search implementation because the container could not resolve raw.githubusercontent.com. This is a local independent negative check, not an official scorer run or a byte-for-byte rerun of the repository generator.

| Curve [a1,a2,a3,a4,a6] | Integral-x representatives | Explicit short relations detected |
|---|---:|---:|
| [0,0,0,-28,52] | 10 | **27** |
| [0,0,0,-4,1] | 9 | **22** |
| [0,0,0,-7,10] | 9 | **23** |
| [0,0,0,-16,1] | 9 | **18** |
| [0,0,0,-19,34] | 9 | **25** |

The top candidate includes exact points P=(-6,2), Q=(-2,10), R=(12,38) satisfying **P+Q=-R**, hence P+Q+R=O. This is a rigorous witness that the *full set of ten points is dependent* and cannot be claimed to certify rank 10. It does not establish the actual rank, and short-relation count is not the dimension of the span. The other four candidate lists likewise contain explicit dependencies. Absence of short relations would also **not** prove independence.

## Economics, gating and next experiment

No individual prize amount or guaranteed point-to-dollar conversion verified. Direct monetary expected value **unquantifiable**. With a hypothetical $35/h labor rate and 0.5h incremental test/audit, opportunity cost is ~$17.50; no measured probability uplift is claimed. The practical gain is avoiding invalid submission effort. A genuinely new ranked result still requires pinned PARI/GP 2.17.4, minimal-model conversion, original-search provenance, known/twist/isogeny exclusion, torsion stripping, canonical-height independence, board nonregression and official benchmark score. No paid compute, contest submission, account login, rights transfer or external contact occurred. Stop counting integral points as rank and focus future searches on independently certified generator sets.

All five Svyable frontier benchmark families remain active; this run selected the time-sensitive EC Rank lane. No new opportunity ID or changed status.
