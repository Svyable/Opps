# BlueDot Rapid — reviewer-ready $4,500 self-contained alternative (NO SUBMISSION)

**Prepared 2026-10-31; Sven Hardy Benson / Svyable.** This is an *alternative scope and budget* to the existing $6,000 / four-week draft, **not** an authorized change to an application, an award, or evidence of applicant availability. The principal must choose one version before any application.

## Specific weakness resolved in the application package

The earlier [$6,000 draft](bluedot-rapid-2026-recorder-integrity-four-week-preflight.md) assumes a **10-hour/$1,000 independent reviewer who has not been identified or engaged**, plus $500 of unquoted testing and packaging expenses. An application whose outcome depends on that reviewer is not yet deliverable on its own. The revised alternative **removes that dependency and those speculative costs**, preserves a narrow falsifiable outcome, and makes any independent reproduction an explicitly unfunded optional follow-up. It also avoids charging already-completed characterization tests to a future grant.

The [current BlueDot Rapid rules](https://bluedot.org/grants/rapid) (checked October 31, 2026) allow up to **$20,000**, including **research time/living costs**, and projects already underway; applications are rolling and approximately 15 minutes. BlueDot asks for a worthwhile direction, credible progress, and a clear role for funding. Funds are restricted to the approved purpose, paid as **one lump sum after a claim and checks**, and a completion report is due within **60 days** of finishing. The official [grants overview](https://bluedot.org/grants) says BlueDot course membership is not required. The April 14 [funder progress report](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants) says applications over $5,000 **might** involve a call; this is historical process commentary, **not** a current promise that $4,500 avoids a call or improves selection.

**Important separate-program warning:** the [March 2026 Technical AI Safety Project Sprint-specific small grant](https://blog.bluedot.org/p/rapid-small-grants-for-the-bluedot) prohibited payment for the applicant's time and required Sprint participation. It is **not** the current general Rapid program. The latter's live terms, not the older cohort reimbursement rules, govern this proposal.

## Proposed application material — conditional and applicant-editable

**Question.** When a tool-use report says a consequential local action succeeded, can a verifier distinguish an actual supervisor-observed event from a forged or replayed record without trusting an event's self-declared `independent` label?

**Evidence already completed, not to be funded again.** The [Apache-2.0 local subprocess pilot](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py) checks a real local subprocess/file result. Five [negative-control tests](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py) demonstrate that the *synthetic* contract accepts constructed self-declared independent records and repeats them without freshness checks. The [GitHub Actions run 41170302920](https://github.com/Svyable/Opps/actions/runs/41170302920), completed successfully on October 31 at commit `c7e3acf0c46dffa1710f95e435f0d0cd551f9efd`, is historical **82-test engineering CI**, not authenticated recorder safety or independent validation. No real agent deployment, field study or external user is claimed.

**Proposed new four-week work (60 founder hours, subject to actual availability):**

| Week | Prospective work | Precommitted acceptance evidence |
|---|---|---|
| 1 | Freeze adversary powers, trust boundary, test inputs and run-ID policy | Versioned threat model; attack matrix with denominators and expected abstentions |
| 2 | Build supervisor-owned run binding and a verifier that does not trust event-supplied origin labels | Source, deterministic run instructions, unit tests for forged origin and replay |
| 3 | Execute the frozen attack matrix, including mutation, missing observation, scope mismatch and replay | Raw pass/fail/abstain counts; false-support rate on **constructed** cases, including failures |
| 4 | Release reproducibility package and a limitations/stop-go decision | Pinned commands and versions, negative results, comparison with frozen pre-grant baseline |

**Success condition:** zero false `supported` verdicts on the specified constructed forged/replayed cases, with exact numerator and denominator, while preserving at least one legitimate local subprocess success. If the verifier cannot establish origin/freshness, it must abstain or reject. This is an **experimental target, not an achieved result**. The study will not claim robustness to compromised supervisor hosts, side channels, production agents or third-party telemetry. Independent reproduction may be sought **only after separate approval** and is not a required deliverable in this self-contained version.

## Alternative request and non-overlap

| Item | Basis | Conditional request |
|---|---|---:|
| Founder time / living support | 60 hours × **$75/hour planning rate**, 15 hours/week × 4 weeks, unverified | **$4,500** |
| Independent reviewer | **Not funded or promised** | $0 |
| Compute, API, equipment, packaging | Use existing/free local resources; no prospective expense authorization | $0 |
| **Total** | No invoices, no approval, no reimbursement guaranteed | **$4,500** |

The $75/hour rate is **not a sponsor-approved rate or a market-rate finding**. Applicant must affirm the opportunity cost and whether $4,500 actually enables the proposed time. If the applicant cannot perform 60 hours, do not use this budget. The $6,000 original remains a separate, unapproved alternative; **never submit both as overlapping requests**.

**Rights and overlap:** Existing tests, local subprocess pilot, Foresight sequence-control mock, EA blinded review research, Human Kind and ScrolIQ remain **pre-grant assets**, not billable future milestones. Do not copy unlicensed `Svyable/agents` source. Public Apache-2.0 declaration does not itself verify every contributor's rights. If EA, Foresight, Seed or another sponsor actually funds any of these prospective hours, disclose and remove the overlap before applying or claiming.

## Risk-adjusted economic decision (no claimed probability uplift)

The official ceiling is $20,000; this draft requests **$4,500 restricted support**, not a $4,500 profit. Conditional economic surplus depends on the applicant's actual displaced earnings, taxes and whether time is genuinely additional. A simple upper-bound arithmetic illustration is $4,500 less 60 × $35 assumed alternative labor value = **$2,400 before taxes and other costs**; this is **not** an established profit or personal earnings fact.

Assume **one hour/$35** of *additional* applicant review of this alternative and use hypothetical conditional economic benefit after delivery of $1,200 cautious, $1,800 central, or $2,400 favorable:

| Scenario | Capacity/legal qualification | Conditional selection | Benefit if awarded/delivered | Incremental EV |
|---|---:|---:|---:|---:|
| Cautious | 40% | 5% | $1,200 | **−$11.00** |
| Central | 60% | 8% | $1,800 | **+$51.40** |
| Favorable | 70% | 10% | $2,400 | **+$133.00** |

`EV = qualification × selection × conditional benefit − $35`. All probabilities are **uncalibrated subjective scenarios**, not observed BlueDot award rates. The earlier research/CI/application labor is sunk and **excluded** here; do not add these marginal EVs to the old $6,000 cumulative EV. At central assumptions, a **3.24%** conditional selection probability would break even on $35. We assume **zero improvement** in award odds from this revised budget. The verified improvement is *scope feasibility*: one uncommitted third-party reviewer and $1,500 of unverified line items are no longer necessary to complete the proposed milestones.

## Applicant release gates / stop decision

1. Confirm real 15 hours/week availability, payee identity, lawful grant receipt/jurisdiction, sanctions, tax and whether $75/hour support is justified. No personal details are inferred from public GitHub.
2. Verify rights in the exact source and all actual funding/award overlap; do not count other applications as awards.
3. Read the exact live application and acceptance terms; they were **not accessed as an authenticated applicant** in this audit. BlueDot can alter grant terms or reject the proposed rate.
4. Choose **either** $4,500 self-contained or the earlier $6,000 reviewer-inclusive version, amend the narrative in the applicant's own judgment, and explicitly approve any submission. No submission, spending, hiring, outreach, acceptance or legal commitment has occurred.

**Decision:** Keep BlueDot Rapid at **PURSUE / applicant decision required**. This packet is a substantive de-risked alternative, not a reason to continue autonomous grant polishing. If the applicant cannot confirm the four gates, further application effort has no demonstrated positive EV.

**Sources checked October 31, 2026:** https://bluedot.org/grants/rapid ; https://bluedot.org/grants ; https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants ; https://github.com/Svyable/Opps/actions/runs/41170302920 .
