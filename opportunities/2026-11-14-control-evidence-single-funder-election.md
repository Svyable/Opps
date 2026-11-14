# Control Evidence — single-funder scope election and cash-realization gate
Prepared 2026-11-14 UTC. Internal decision artifact; no application submitted.

## Decision
**Advance EA Transformative AI Fund as the primary candidate; BlueDot Rapid remains PURSUE / HOLD, not a parallel funding claim.** The same scorer, gateway, recorder, scenarios, evaluation and publication cannot be billed to both funders. This document does not assert that the $25,000 EA request is eligible or justified. A smaller defensible budget is preferable to padding a grant request.

## Official source checks
- EA Transformative AI Fund: https://funds.effectivealtruism.org/funds/transformative-ai — always open; typical grants $10,000–$150,000, rarely above $300,000; early-stage transformative AI work primarily reducing catastrophic risk. Payer's published grants database: https://funds.effectivealtruism.org/grants .
- BlueDot Rapid: https://bluedot.org/grants/rapid and https://bluedot.org/grants — conflicting previously observed $10k direct-page versus $20k index ceiling and disputed stipend treatment. Treat both as **unresolved**, not automatic permission to fund founder hours. April 14 2026 history: https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants (77 grants exceeding $50k).
- BlueDot Media: https://bluedot.org/grants/media — $20k–$200k / 6–12 months; self-built following and actual audience proof required. This is a distinct media lane, not the Control Evidence research budget.
- No fixed deadline for these programs verified. No applicant-specific payee qualification, grant agreement, tax or IP terms verified.

## Work-package allocation: one claim only
| Work package | Existing asset | EA proposal | BlueDot Rapid alternative | Evidence before request |
|---|---|---|---|---|
| Scorer and synthetic gateway | score_pilot.py, mock_gateway.py, tests | Existing in-kind work, **not new reimbursable work** | Same; cannot rebill | Source SHA, authorship/right-to-use |
| Independent execution recorder | Not demonstrated | Candidate **future** EA task | **Excluded** while EA active | New work estimate, recorder event provenance, test results |
| Frozen paired real-agent scenarios | Preregistered protocol only | Candidate **future** EA task | **Excluded** while EA active | Manifest, costs, exact agent/tool setup |
| Reproducible analysis and write-up | Partial existing code | Candidate **future** EA task | **Excluded** while EA active | Milestone, independent replay, reviewer |
| Public media adaptation | Existing Shelf/Desk writing | Not included in technical pilot by default | Not included | Separate deliverables and audience/rights proof |

**Election rule:** Before any grant application, allocate each task, person, date, hours and expense to exactly one funding source. If BlueDot is chosen instead, remove the overlapping work from EA and withdraw/replace the EA budget. Disclose any other application where required. No duplicate claims for existing unpaid or funded labor.

## Reviewer-facing claim boundary
What exists: synthetic authorization scorer, mock gateway, regression test source, preregistered paired-study protocol. What does not yet exist as verified evidence: independently recorded real-agent execution traces, completed clean-checkout CI logs, measured safety effect, external adoption, independent evaluator, payee qualification, or agreed budget. Do not imply that gateway unit tests demonstrate reduced catastrophic risk.

## Budget and EV decision
The previous $25,000 EA request is **not an earned $25,000**, and the old illustrative $7,200 “surplus” is not an allowable grant budget. Rebuild an itemized budget from actual future hours, documented rates, external costs and allowable grant terms. For a $10,000 hypothetical award with $2,800 incremental labor and $140 application cost, a *cash-receipt less labor* expression is $10,000×p − $2,940, but only if all $10,000 are legitimately payable and economically retained; those assumptions are unverified. If grant funds must all be spent on eligible work, distributable founder surplus may be zero. No observed selection probability, and no defensible positive monetary EV yet. A one-hour additional preflight at $35 requires at least a 0.35-percentage-point improvement in joint paid-award probability **if** $10k is fully realizable; otherwise this threshold is inapplicable. This is a break-even threshold, not a probability estimate.

## Next release gate (one high-value action)
1. Retrieve a clean-checkout GitHub Actions success URL or run both committed scorer and gateway suites with exact SHA, Python version and log. GitHub Actions status is currently **unverified**, not passed.
2. Produce one independently instrumented agent-generated tool-call trace with immutable execution-event provenance; no fabricated or synthetic evidence.
3. Verify payee jurisdiction, actual 10-week time availability, independent review staffing, restricted budget and source/IP rights.
4. Obtain applicant approval of a single accurate request and inspect actual application/grant terms. **Do not submit or contact funders without approval.**

## Other active lanes
Keep EC Rank, ECDSA.fail, Proximity Prize, FLock/SNARK.fast and CircuitBreaker in the registry. EC Rank's Nov 14 and ECDSA.fail's Dec 31 dates are user-reported, not independently confirmed; no cash award is verified. Zero-spend technical experiments only, with explicit stop-loss.

No money spent, third-party contact, application, binding terms or IP transfer.
