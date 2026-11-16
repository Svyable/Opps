# Transformative AI Fund — exclusive budget and independent-evidence submission gate
Date: 2026-11-16 | Status: PURSUE / HOLD | No application authorized

## Funding decision
Official fund: https://funds.effectivealtruism.org/funds/transformative-ai
The Transformative AI Fund is continuously open, normally awards $10,000–$150,000 and rarely exceeds $300,000. It supports individuals and existing organizations starting new work on reducing catastrophic AI risks. This is restricted research funding, **not unrestricted company revenue**. The payer is EA Funds, an established grantmaker with a public grants database (https://funds.effectivealtruism.org/). No selection rate or Svyable eligibility confirmation is published for this proposal.

**Specific submission weakness:** The existing Control Evidence project has synthetic gateway and receipt-integrity tests, but lacks independently observed real-agent outcomes and an auditable nonoverlapping eligible-cost budget. Prior BlueDot Rapid proposals ($4,500/60h and $2,800/80h) overlap TAIF scope. Do not submit both claims for the same work.

## Minimum reviewer-ready evidence manifest (not completed)
| Evidence | Existing source | Required independent verification | Gate |
|---|---|---|---|
| Policy/authorization contract | Control Evidence mock gateway and synthetic contract in Opps | pinned source revision and documented scope | Existing artifact, not real-agent proof |
| Executor receipt integrity | `artifacts/control-evidence-2026/receipt_audit.py` | full regression suite on pinned commit; archive command, interpreter, stdout, exit status and source hash | NOT VERIFIED in this run |
| Action-substitution rejection | `artifacts/control-evidence-2026/test_receipt_audit.py` | run new cases and negative controls | NOT VERIFIED in this run |
| Real-agent evaluation | no independent recorder evidenced | third-party/executor-side timestamped traces, matched baseline and treatment trials, blinded labels, reproducible scorer | ABSENT |
| Originality/IP | repository files | confirm contributor ownership, dependencies and licensing | UNVERIFIED |
| Applicant eligibility | none in repository | legal payee, jurisdiction, capacity and conflict declarations | UNVERIFIED |

**Minimum experimental design:** Freeze policy and scoring before trials; log proposed tool action and executor-side receipt independently; include both authorized and unauthorized actions, missing/duplicate/orphaned receipts, substituted actions, blinded human classification, and paired baseline/treatment cases. Preserve all failed trials. Do not infer deployment safety from unit-test success.

## Exclusive expense register — completion required before application
No costs below are claimed or authorized. Fill in actual hours/rates and documentary evidence. A line item can appear in only one funder's request.

| ID | Deliverable | Hours | Rate | Requested amount | Assigned funder | Evidence of cost | Status |
|---|---|---:|---:|---:|---|---|---|
| T1 | independent execution instrumentation | TBD | TBD | TBD | TAIF only if approved | quote / time plan | UNVERIFIED |
| T2 | controlled real-agent evaluation | TBD | TBD | TBD | TAIF only if approved | protocol / receipts | UNVERIFIED |
| T3 | independent blind review and reproduction | TBD | TBD | TBD | TAIF only if approved | reviewer plan | UNVERIFIED |
| B1 | earlier BlueDot $4,500/60h draft | — | — | $0 in TAIF until reconciled | QUARANTINE | overlap unresolved | EXCLUDED |
| B2 | earlier BlueDot $2,800/80h draft | — | — | $0 in TAIF until reconciled | QUARANTINE | overlap unresolved | EXCLUDED |

**Application budget = sum of verified, nonoverlapping TAIF-only costs, not the published grant range.** No legitimate positive amount is established today. Confirm whether founder time, contractors, compute, taxes, overhead and existing sunk work are eligible in the actual agreement before inclusion. Do not assume IP retention or payment schedule.

## Decision thresholds and EV
- Advance to a draft application only if applicant/legal payee, exclusive cost basis and independent execution evidence are documented.
- Cap the next verification at 2 hours and zero external spend. Illustrative labor opportunity cost at $35/hour = $70; not an actual invoice.
- Monetary EV = retainable incremental economic benefit × P(eligible) × P(award|eligible) × P(payment|award) − all incremental labor and rights costs. Every probability and retainable benefit is presently unknown. Gross restricted award is **not** the benefit.
- A hypothetical $5,000 incremental retainable benefit would require >1.4% joint success probability to offset $70, before delivery costs. This is a break-even sensitivity, **not** an award estimate.

## Current alternative screening (2026-11-16)
- Anthropic Residency: official https://alignment.anthropic.com/2026/anthropic-residency/ ; November 22 deadline; $350k–$500k annual-equivalent; personal full-time senior leadership and work authorization unverified. WATCH urgent, no speculative personal assertions.
- BlueDot Media: official https://bluedot.org/grants/media ; $20k–$200k over 6–12 months, applications any time; existing Desk IP strong but verified audience/distribution and original reporting samples missing. WATCH.
- BlueDot Rapid: https://bluedot.org/grants/rapid states $50–$10k, while https://bluedot.org/grants says up to $20k; payment terms differ by version. PURSUE/HOLD, $0 exclusive verified expense.
- Five frontier benchmarks: keep existing lanes in registry; no independently confirmed cash award. Do not equate points or leaderboard rank with cash.

## Next authorized step
Run pinned complete Control Evidence tests and record a real executor-side trace; separately obtain applicant-authorized nonoverlapping costs and rights information. No external submission, spend, registration, outreach, or IP transfer.
