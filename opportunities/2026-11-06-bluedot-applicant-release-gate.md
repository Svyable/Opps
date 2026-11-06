# BlueDot Rapid Grants — applicant release gate (2026-11-06)

**Decision:** conditional PURSUE, **do not submit** until first-party applicant checks clear. This is a release-control record, not a claim that eligibility has been verified.

## Official rule checked
[BlueDot Rapid Grants](https://bluedot.org/grants/rapid) (checked 2026-11-06): up to **$20,000**, expressly including time, living costs, and research access. Application estimated at 15 minutes; no fixed closing date displayed. A successful applicant claims a single lump-sum payment after required checks; transfer and exchange fees may reduce net proceeds. Funds are restricted to the agreed charitable/educational purpose; material changes need written approval; a short report is due within 60 days of project or grant-period completion. Course affiliation is favorable, **not stated as mandatory**.

**Critical jurisdiction gate:** the official FAQ excludes transfers to Afghanistan, Belarus, Burundi, Central African Republic, Chad, China, Congo Republic, Cuba, Democratic Republic of the Congo, Eritrea, India, Iraq, Iran, Libya, Myanmar, North Korea, Somalia, South Sudan, Sudan, Syria, Russia, Venezuela and Yemen; sanctions restrictions also apply. **Do not infer payee jurisdiction from GitHub identity, brand, or writing.**

## Existing Svyable material
- [Short-form $4,500 / 60-hour application packet](2026-11-05-bluedot-rapid-short-form-submission-packet.md)
- [Deterministic constructed baseline](../artifacts/control-evidence-2026/rapid_grant_baseline.py)
- [Baseline CI workflow](../.github/workflows/control-evidence-rapid-baseline.yml)

The code is a *constructed vulnerability baseline*, not a validated AI safety improvement. The workflow has not yielded an independently verified passing run or downloadable JSON result in this review.

## Release gates — evidence, not prose
1. **Payee identity and location:** confirm actual legal recipient, payment jurisdiction, sanctions screening, and ability to receive funds. Unknown.
2. **Work capacity and rate:** confirm 60 research hours in the proposed period and a defensible $75/hour budget basis. Unknown.
3. **Rights:** identify who owns the relevant Svyable code and whether its use/publication is permitted. Unknown.
4. **Nonoverlap:** itemize the 60 hours and outputs; ensure no same costs or deliverables are claimed under EA Funds or another source. Unknown.
5. **Reproducibility:** obtain real CI or local test output with commit SHA, exact command, pass/fail and raw JSON; do not cite a successful test until executed. Unknown.
6. **Authority:** applicant personally reviews and expressly approves any submission and agreement. Not granted.

**Stop-loss:** no further cosmetic proposal rewriting. If gates 1–4 cannot be verified, hold at WATCH rather than spending application labor. Once verified, a 15-minute application is a reasonable next decision; this document is not authorization to submit.

## Economics (subjective, not measured)
Proposed restricted award $4,500; earlier conditional economic surplus $1,800. Prior assumptions 50% eligibility/fit × 60% delivery × 8% award = 2.4% combined probability; $1,800 × 0.024 − $35 future labor = **+$8.20**. This estimate is not an observed success rate. With an ineligible payee the true EV is negative application cost. No incremental probability uplift is claimed for this document.

**Sources:** [official rules](https://bluedot.org/grants/rapid); [historical grantmaking report, April 14 2026](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants).