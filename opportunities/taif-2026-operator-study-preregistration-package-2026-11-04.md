# Control Evidence: preregisterable operator-study package (2026-11-04)

**Internal research protocol, not an application, completed study, or claim of safety impact.** Opportunity: `ea-funds-transformative-ai-fund-2026`. Status: **PURSUE, evidence hold**. This package converts the previously identified causal-impact weakness into an auditable, executable-by-humans study specification; it does not fabricate participants, results, datasets or approvals.

## Official fund fit and payer
- https://funds.effectivealtruism.org/funds/transformative-ai — checked 2026-11-04. Always open, typical grants $10k–$150k; individuals/new organizations eligible in principle. Primarily catastrophic-risk reduction, with technical research and demonstration projects supported.
- https://funds.effectivealtruism.org/apply-for-funding — checked 2026-11-04. Application advertised under 1 hour; final form, rights, payment and grant terms require applicant review. The page identifies Centre for Effective Altruism Inc. as US 501(c)(3), EIN 33-3737390. A credible payer is not a guaranteed award.
- Existing request: **$25,000 proposed**, not an awarded amount. Research money is restricted project funding, not automatically personal income.

## Decision-critical causal hypothesis
**H1 (unproven):** In independently labeled agent-execution review tasks, showing a human reviewer a claim-to-evidence audit (including explicit missing-evidence/abstain) reduces approval of *unsafe or unsupported* completion claims compared with showing the same underlying agent narrative and records without the audit. **H0:** No reduction. The study cannot directly establish a reduction in catastrophic AI risk.

### Protocol fixed before recruiting/collecting
1. **Scenario source and rights.** Collect consented, non-sensitive real execution traces from an independent source; document provenance, redaction, permission and retention. Synthetic fixtures may be used to pilot UI only and **must be excluded from primary outcome claims**.
2. **Ground truth.** Two independent adjudicators label each case as safe-to-approve / unsafe-to-approve / indeterminate using evidence hidden from participants; a third adjudicator resolves disagreement. Publish agreement and disagreement counts; do not quietly exclude hard cases. Predefine what counts as unsafe approval.
3. **Randomization.** Randomize scenario order and intervention/control presentation at the reviewer–scenario level using a recorded seed; each reviewer sees a scenario only once. Balance condition assignment by scenario and reviewer, with a separate held-out set for final analysis. Keep labels and the expected condition outcome concealed from operators.
4. **Control.** Baseline interface shows the original claim, timeline and underlying records without Control Evidence verdicts. **Treatment** adds evidence-linked labels and explicit abstention for missing records. Preserve identical record access and time limits so the only intended difference is the audit interpretation.
5. **Primary outcome.** Unsafe approvals divided by independently unsafe-labeled reviewed cases, reported by condition with numerator, denominator, absolute difference and uncertainty interval. Include all randomized cases in intention-to-treat reporting; report missing decisions separately.
6. **Safety countermeasure.** False blocks on safe-labeled cases, abstentions on both labels, and median decision time by condition. Any reduction in unsafe approvals accompanied by excessive false blocks or delay is not a clean success.
7. **Leakage/quality checks.** Predefine leakage inspection of UI wording, source identifiers and case order; record reviewer prior experience, exposure to the project and case-level confidence. Do not treat adjudicators as independent if they authored the system or scenarios.
8. **Analysis.** Publish per-condition counts and reviewer/scenario clustering; use a confidence interval that respects clustering rather than treating repeated reviewer decisions as independent. Report exploratory subgroup results as exploratory. No post-hoc threshold shopping.
9. **Stop/go.** Do not claim efficacy until a real consented pilot establishes feasibility, independent labels, and a precommitted analysis. If access to reviewers/traces fails, narrow the funding claim to **exploratory audit tooling** and reconsider whether this fund's catastrophic-risk focus is appropriate.

## Machine-readable evidence fields for future collection
`scenario_id, provenance_ref, consent_ref, rights_ref, labeler_1, labeler_2, adjudicated_label, reviewer_pseudonym, assignment_seed, condition, decision, decision_time_seconds, abstain, record_missing, leakage_flag, exclusion_reason, timestamp`. Do not populate with fabricated measurements. Store identity/consent separately from public benchmark data.

## Budget and eligibility release checklist
- [ ] Actual applicant and lawful grant recipient confirmed, including payment/tax implications.
- [ ] 120 founder hours and engineer/reviewer availability confirmed by real people.
- [ ] Permission for traces, code, labels and publication documented; privacy plan reviewed.
- [ ] $25,000 itemized **future** costs supported, not retrospective invented invoices.
- [ ] BlueDot/other funder overlap guard run on **authentic** dated tasks and costs.
- [ ] Pilot ethics, consent, participant compensation and retention reviewed.
- [ ] Applicant checks actual Paperform questions and terms; authorizes any submission.

## Economics and honest limitations
Previously recorded subjective future EV: `$7,800 conditional founder surplus × 55% qualification feasibility × 5% conditional award − $70 future application labor = +$144.50`. This is **not** a measured probability or grant forecast. This protocol's drafting labor estimated 0.75h × $35 = **$26.25**; absent verified probability uplift or avoided rejection, standalone incremental EV is **−$26.25**. At 55% feasibility and $7,800 conditional surplus, a **0.612 percentage-point** increase in conditional selection probability would be required to offset this labor; none has been observed. No recruitment, tests, data collection, outreach, spending, application or acceptance of terms occurred.

**Next decisive action:** applicant supplies real permissioned traces and independently available reviewers, or marks the research component infeasible and reduces/stops pursuit. The protocol is designed to make that decision falsifiable rather than to cosmetically improve a grant narrative.
