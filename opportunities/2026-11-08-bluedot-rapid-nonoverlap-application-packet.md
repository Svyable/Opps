# BlueDot Rapid Grants — nonoverlapping $4,500 applicant-ready conditional packet
**Prepared 2026-11-08. Internal draft only. NOT submitted, approved, or a verified statement of applicant eligibility.**

## Sponsor and authoritative current terms

[BlueDot Rapid Grants](https://bluedot.org/grants/rapid), official page read 2026-11-08: up to **$20,000**; funds may support research time, living costs, tools and experiments. Applicants describe plan and budget in a ~15-minute form. No published fixed deadline or decision-time SLA. Payment is a lump sum via a claim after required checks; material project changes need written approval and a short report is due within 60 days after project completion or the end of the grant period. Participation in BlueDot programs helps but is **not a prerequisite**. Restricted jurisdictions and sanctions apply. These are grant funds for the approved purpose, **not an unrestricted $4,500 founder profit**. Verify the live page again immediately before any human-approved submission.

## Applicant-facing short-form proposal — DRAFT, conditional on gates

**Working title:** Independent action-receipt feasibility: falsifying unsupported AI-agent completion claims.

**Problem:** AI agents can report an external action as complete without an independent record of execution. Existing Svyable Control Evidence synthetic tests exercise receipt parsing, replay resistance, scope and adversarial cases, but do **not** prove that a real recorder is independent of the agent or covers every attempted action.

**Specific next step funded:** A bounded, 60-hour *feasibility phase* before any larger-scale evaluation: specify and exercise an independently administered recorder boundary on an authorized local fixture; establish a frozen manifest of attempts including omissions, failures and timeouts; run predeclared replay, scope and coverage negative controls; produce raw reproducibility logs and an explicit go/no-go report. This is research to find whether the protected boundary can be established at all, not a claim of demonstrated effectiveness or a promise of 100-case statistical validation.

**Existing work reused:** Svyable's synthetic claim evaluator, signed-receipt boundary, SQLite replay-nonce prototype and regression tests. No completed independent recorder, passing CI evidence, or authenticated third-party measurement is asserted.

**Proposed funding:** $4,500 = 60 **future** research hours × **provisional** $75/hour. This is a planning request, not a verified market rate or documented applicant capacity. No equipment, cloud, third-party labor or past work is charged. Grant funding is requested only if the applicant can substantiate the rate and availability and the sponsor permits this use.

**Delivery milestones, contingent on funding and authorized access:**
- Hours 1–12: written role/host/key threat model and independently testable access-control protocol; document who controls recorder and claimant
- Hours 13–32: controlled local fixture with complete attempt manifest, explicit missingness, failed actions and replay/scope tests; preserve raw logs
- Hours 33–48: reproducible verification of positive/negative controls; disclose any failure, leakage, shared control or lack of independence
- Hours 49–60: bounded go/no-go decision, redacted evidence bundle, code/version hashes and completion report

**Stop rule:** If no demonstrably separate recorder authority can be established, stop and report a negative feasibility result. Do not call a local subprocess or self-signed fixture independent. Do not represent proposed metrics as achieved.

**What success means:** A reproducible proof-of-feasibility with explicit recorder-control boundary, event coverage accounting and failure-mode logs, or a reproducible negative finding. This stage **does not** include a 100-case holdout, independent external evaluation, deployment or generalized safety claims.

## Mandatory nonoverlap with the separate $25,000 EA Funds concept

The [EA Funds proposal](2026-11-08-ea-control-evidence-25000-reviewer-packet.md) currently allocates $7,000 to independent recorder engineering, $5,000 to evaluation cases, $5,000 to independent evaluation, $4,000 to reproducibility and $4,000 to coordination. **As written, its recorder engineering and reproducibility packages overlap this Rapid feasibility phase.** Two parallel applications on the current budgets would be misleading if they claimed the same 60 hours or outputs. Choose one of these *mutually exclusive* paths before submission:

**Path A — Rapid first (preferred if actual 60-hour capacity and acceptable terms):** BlueDot pays *only* the preliminary feasibility hours above. If funded, EA's eventual application must be rebudgeted and explicitly exclude those 60 hours, already funded feasibility code and reports. Its later-phase scope would begin with an independent evaluator, a preregistered holdout and additional, separately logged work; do not imply EA funding is secured or that its $25,000 budget can remain unchanged. Any sponsor-required disclosure of related funding or proposals must be accurate.

**Path B — EA only:** Do not submit or accept the overlapping BlueDot request. Keep the $25,000 proposal intact subject to its own applicant and evidence gates.

**Path C — BlueDot rejected/unfunded:** Work that has not been funded or delivered may be reconsidered for a later EA proposal, with updated dates and a truthful cost ledger. Never charge both sponsors for identical hours.

**Hard reconciliation invariant:** Every funded hour and cost line must have one unique `(work-package, date, contributor, deliverable, funder)` record and exactly one payer; an unfunded proposal is not a paid expense. No retroactive charging of preexisting code. Record approvals and final funding terms before allocating costs.

## Applicant release checklist (all unresolved)

- [ ] Identify the lawful individual/entity payee, country of residence, sanctions and payout eligibility; verify the applicant controls and can perform the work
- [ ] Confirm 60 **future** hours are genuinely available and justify the $75/hour requested support
- [ ] Confirm official sponsor's current application, funding restrictions, claims and IP/publication terms
- [ ] Obtain a real CI run URL and raw log for existing test suites; distinguish unit fixtures from independent evidence
- [ ] Verify a recorder can be separately controlled or explicitly frame as an exploratory risk, with a stop condition
- [ ] Choose Path A, B or C and sign off on an itemized nonoverlap ledger before any application
- [ ] Review potential tax and opportunity costs; approve any grant application and eventual acceptance separately

## Conservative economics and decision

Credible first-party grantmaker with public award examples; payout is conditional, not guaranteed. Cash request **$4,500**; individual unrestricted economic benefit **unknown**. Illustrative *not measured* sensitivity: assume $1,800 conditional economic benefit after 60h work and restrictions, P(eligibility)=0.50, P(delivery)=0.60, P(award|eligible,deliverable)=0.08, and 0.5h applicant review at $35/h ($17.50). Then EV of this *incremental application decision* is `$1,800×0.5×0.6×0.08−$17.50 = +$25.70`. At P(eligibility)=0.20, EV = `−$0.22`. These probabilities are judgmental sensitivity inputs, not observed odds, and actual opportunity EV cannot be validated without eligibility, terms and net benefit. The 60h is **not free**: if $75/h represents compensation for those hours, its economic surplus depends on the applicant's true opportunity cost and tax treatment. No positive cash EV is established.

**Decision:** conditional PURSUE with **no additional technical build** until human applicant and nonoverlap gates clear. This packet advances a usable application narrative and prevents duplicate-grant claims; it is not an instruction to submit.
