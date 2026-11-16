# Anthropic Residency — evidence-backed AI-control work sample (prepared 2026-11-16)

**Internal applicant-review attachment only. Not submitted, not a claim of applicant authorship, employment eligibility, seniority, or live-agent results.** Official call: https://alignment.anthropic.com/2026/anthropic-residency/ ; applications close **2026-11-22** (time zone not confirmed). This is a paid **full-time individual** research placement, not a company contract. The official program explicitly lists AI control, adversarial robustness, safeguards, scalable oversight, and empirical research.

## Research question
Can a tool-execution safety monitor detect an unauthorized *executed* action when a model or intermediary can fabricate the event stream used to score it? A decision log is not evidence of what the tool actually did. A self-declared `recorder` string is not authenticated provenance.

## Reproducible existing artifact and what it actually establishes
- Source: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/receipt_audit.py
- Regression tests: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_receipt_audit.py
- Negative control: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_receipt_provenance_gap.py
- Prior report: https://github.com/Svyable/Opps/blob/main/opportunities/2026-11-16-taif-executor-provenance-negative-control.md

The source rejects orphaned, duplicated, missing and authorization-mismatched receipts, and rejects substituted proposed actions. Its output counts executed actions recorded as unauthorized. However, the `recorder` field is only a nonempty string, and **no cryptographic origin binding or executor-isolated collection boundary exists**. A fabricated receipt can be accepted; therefore `unauthorized_executed=0` is not a measured real-world safety result. Earlier isolated tests were reported as passing, but no clean full-suite run or independent live executor evidence is established here. Do not turn these into resume claims of deployed safety impact.

## Proposed falsifiable empirical extension (not performed)
1. Pin a real tool-executor adapter and a separate append-only event collector. Have the executor issue an authenticated, nonce-bound receipt *after* execution, including canonical action digest, authorization decision ID, tool outcome, monotonically increasing sequence and collector-observed timestamp.
2. Create paired scenarios with the same task and tool opportunities, varying monitor enforcement; use a precommitted, blinded labeler for whether execution violates the user's authorized scope. Record attempted and completed tool calls separately.
3. Attack the recording boundary with dropped, duplicated, reordered, action-substituted and forged receipts. Require independent fail-closed detection; a missing record is an **unknown**, not proof of no execution.
4. Report denominator counts, false positives, unauthorized executions per opportunity, coverage, confidence intervals, latency and provenance failures. Include a no-monitor baseline and negative controls. Do not report a success rate until actual trials run.
5. Publish source, environment versions, event schema, fixture digests and a reproducibility command only after rights/privacy review.

**Success gate:** independent executor receipts cannot be forged by the monitored agent; every completed tool action is accounted for, or the run is explicitly marked incomplete. **Failure gate:** any agent-origin forged receipt passes as independent evidence, any missing execution silently counts safe, or paired trials are not comparable.

## Personal qualification gate before any application
Applicant must personally attest and document: (a) two dated senior technical leadership examples and their precise role, (b) which lines/code/design in this sample they actually created or directed, (c) ability to work full-time for 6 weeks / 3 months / 6 months, (d) US or UK employment eligibility, (e) SF/remote constraints, (f) Svyable outside-work, confidential information and IP conflicts. **None verified by this work sample.** Applicant must decide whether to apply; no third-party contact or submission authorized.

## Economics and stop-loss
Official annual-equivalent compensation **$350k–$500k**; illustrative six-week gross at 52 weeks/year **$40,385–$57,692**. Actual pay, tax, displacement, IP and offer terms unknown. If **hypothetical** incremental retained benefit were $15k, a 2h/$70 preflight requires >0.467% joint eligibility/selection/payment probability to break even. This is a sensitivity threshold, **not** an estimated probability. No positive monetary EV is claimed; if full-time availability or leadership evidence fails, stop. No outside spend.

## Decision
**WATCH / urgent:** strongest time-limited individual cash opportunity among reviewed active options, but unverified eligibility makes an application premature. This work sample removes the *technical-portfolio clarity* weakness, not the *personal eligibility* blocker. Rolling TAIF remains PURSUE/HOLD for separate restricted project funding. All five unpriced benchmark lanes remain unchanged.
