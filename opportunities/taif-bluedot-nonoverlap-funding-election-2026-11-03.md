# Control Evidence — mutually exclusive grant funding and release gate (2026-11-03)

**Decision artifact; not a grant application, agreement, award or evidence of applicant eligibility.** Selected active opportunity: EA Funds Transformative AI Fund (TAIF), proposed **$25,000 / ten weeks**, status **PURSUE — blocked pending applicant attestations**. Current official fund: https://funds.effectivealtruism.org/funds/transformative-ai (checked 2026-11-03; rolling, typically $10k–$150k). Alternative existing opportunity: BlueDot Rapid, proposed **$4,500 / 60 future founder hours**, https://bluedot.org/grants/rapid (checked 2026-11-03; up to $20k, time and living costs listed). These are *alternative* financing paths for related Control Evidence work, **not $29,500 stackable income**.

## Specific submission weakness and decision

The existing TAIF budget assumes 120 lead hours ($12,000), 100 engineering hours ($7,500), 40 independent review hours ($4,000), $1,000 compute and $500 documentation. The BlueDot budget proposes 60 founder hours ($4,500). Both concern Control Evidence receipts, mutation/replay checks, evidence-quality protocol and reproducible release. Without an auditable separation of tasks and dates, simultaneous applications could imply duplicate compensation for the same work. **No contemporaneous timesheet, funding contract, payee, approved reviewer, engineer quote or deliverable-level allocation has been verified.** Do not claim this conflict is cleared.

## Conservative funding election — before any submission

**Default election: TAIF primary; BlueDot held, not concurrently budgeted.** Do not submit both overlapping budgets without applicant-approved, documented nonoverlapping scopes and disclosures to each funder consistent with their actual terms. The choice does not withdraw an existing application; no submission is known in the ledger.

| Work package | Existing baseline (unfunded here) | TAIF proposed *future* activity | BlueDot proposed activity | Gate |
|---|---|---|---|---|
| Receipt and replay checks | Historical synthetic receipt demo and 96/96 historical CI tests | New consented isolated tool-side telemetry with provenance and missingness | Mutation/replay improvements could overlap | **HOLD BlueDot** unless distinct future tests and hours are documented |
| Evidence-quality protocol | Existing local independent-reference gate | Preregistered labels, reference adjudication, blinded comparative evaluation | Evidence-quality scoring could overlap | **HOLD BlueDot** until mutually exclusive case IDs, deliverables and labor are specified |
| Public release | Existing code and test artifacts | Permissioned dataset, denominator-level results and replication guide | Sanitized reproducibility package could overlap | **HOLD BlueDot** unless separate release scope is documented |
| Founder time | Existing development already completed | 120 *future* lead hours, $100/h planning assumption | 60 *future* hours, $75/h planning assumption | Never charge identical hours to both; do not reclassify past work as future |

**Evidence to obtain before any applicant-controlled submission:** (1) applicant's legal grant-receipt jurisdiction and identity; (2) signed-off prospective 10-week availability and nonoverlapping hour ledger with start/end dates and task IDs; (3) ownership/license authority for public code, private telemetry and research results; (4) actual engineer/reviewer commitments and cost quotes or explicitly revised conditional budget; (5) permissioned trace acquisition and independent reference labels; (6) any existing grant applications, awards or contractual restrictions, including BlueDot; (7) review of form/site terms before upload. All are **UNVERIFIED**. No outreach or spending authorized.

## Proposed audit record (blank; do not fabricate)

For each future cost: `task_id | scope | funding_source | person/payee | date | hours | rate | evidence_link | other_funding_check | approval`. Enforce unique `(person, date, hour interval)` across sponsors and a unique deliverable/case ID where costs are shared. Record zero/unknown rather than infer. If an existing award covers a task, subtract it from the proposed budget before submission and disclose as required. No personal information should be added to the public repository.

## Decision economics (illustrative, not measured)

TAIF: conditional founder economic benefit **$12,000 − (120×$35) = $7,800** before taxes; assumed 55% feasibility × 5% conditional selection yields $214.50 gross expected benefit; less $70 prospective applicant labor = **+$144.50 prospective EV**, excluding prior sunk audits and any additional verification labor. BlueDot: conditional net benefit $1,800 × 50% category feasibility × 60% delivery × 8% selection − $35 applicant labor = **+$8.20 prospective EV**. These outcomes are **correlated and mutually exclusive in overlapping scope**; adding EVs is not warranted. Neither selection probability nor incremental uplift is observed. A further 2 hours of unfunded verification at $35/h would reduce TAIF prospective EV to **+$74.50** if it does not change odds, and to negative if actual applicant feasibility is zero. At 55% feasibility and $7,800 conditional surplus, a $35 new work item needs a **0.816 percentage-point increase in conditional award probability** to break even from award value alone. No such uplift is demonstrated.

**Next decision:** applicant must choose a funding lane and provide genuine staffing/rights/time/payee evidence. If unavailable, pause grant preparation rather than manufacture qualifications. The technical baseline is reusable, but no independent human evaluation or safety benefit has been demonstrated.

**Source and provenance:** https://funds.effectivealtruism.org/funds/transformative-ai ; https://bluedot.org/grants/rapid ; https://github.com/Svyable/Opps/blob/main/opportunities/taif-control-evidence-2026-causal-impact-and-stop-gates-2026-11-02.md ; https://github.com/Svyable/Opps/blob/main/opportunities/bluedot-rapid-2026-live-rule-change-2026-11-03.md . No new runtime tests performed; this is a funding-controls artifact.
