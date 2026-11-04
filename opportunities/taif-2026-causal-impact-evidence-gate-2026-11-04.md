# TAIF Control Evidence — funder-fit and evidence-release gate (2026-11-04)

**Internal reviewer-facing due-diligence worksheet; NOT an application or verified benchmark.** Opportunity ID: `ea-funds-transformative-ai-fund-2026`. Decision: **PURSUE, application held pending evidence**.

## Verified current fund terms
- Official fund: https://funds.effectivealtruism.org/funds/transformative-ai (checked 2026-11-04). Applications **always open**; typical awards **$10,000–$150,000**; early-stage individuals/new organizations eligible in principle. Primary focus: reducing **global catastrophic risks** from advanced AI. It also permits demonstrations and technical research.
- Official application page: https://funds.effectivealtruism.org/apply-for-funding (checked 2026-11-04). Applications use an external Paperform; advertised application time under one hour. Public page identifies the Centre for Effective Altruism Inc. as a US 501(c)(3), EIN 33-3737390. Actual form-specific questions, privacy/rights and grant agreement have **not** been accepted or verified.
- Official public grants database: https://funds.effectivealtruism.org/grants; historical payouts substantiate payer activity, not selection probability.
- **Do not confuse fund fit with award likelihood.** A claim-to-record auditability tool may be useful to ordinary agent reliability without reducing catastrophic risk. The application must state a credible, testable causal pathway or avoid implying established catastrophic-risk impact.

## One funder-critical weakness: missing causal evidence
The existing proposal's narrow scientific claim is defensible: adjudicate whether an agent's self-reported completion/safety statements are supported by independent, potentially missing records, and abstain when evidence is insufficient. But **there is no demonstrated chain from this benchmark to reduced catastrophic risk**. Synthetic fixtures and local contract tests are engineering checks, not evidence of real-world agent oversight effectiveness.

**Proposed falsifiable causal pathway, not a finding:**
1. Claim-to-record audit detects unsupported self-reports or correctly abstains on absent telemetry.
2. A human oversight operator receives calibrated evidence labels rather than a confident narrative.
3. In a prospective blinded task, the operator makes fewer unsafe approvals **without unacceptable false blocks or delays** than with baseline monitoring.
4. If repeated across realistic high-stakes agent workflows and adopted by developers, this could improve oversight reliability. Whether this meaningfully reduces catastrophic risk remains an open question.

**Primary study endpoint (to preregister before collecting data):** difference in *unsafe approval rate* between baseline record display and evidence-labeled display, measured on independent, pre-labeled scenarios. Report confidence intervals and number of cases; no invented effect size. **Safety countermetric:** false-block/abstention rate on legitimately completed tasks; **operational countermetric:** reviewer decision time. Missing traces and ambiguous clocks must remain explicit, never coerced to success.

## Existing evidence vs missing evidence
| Claim or input | Currently supportable | Missing before application/release |
|---|---|---|
| Public Control Evidence contract code | Source and transparent fixtures in `artifacts/control-evidence-2026/`; known limitations in project brief | Authenticated third-party execution records, verified deployment |
| Blind packet infrastructure | Generator and tests in same directory; test outcomes in prior ledger are historical claims | Independent blind adjudicators, consent, real labels, leakage audit |
| Novelty | Prior-art citations in `opportunities/taif-control-evidence-2026.md` | Independent literature novelty review |
| Staff/capacity | 120 lead hours proposed, not verified | Applicant-confirmed 12h/week for 10 weeks, engineer commitment, 3 human reviewers |
| Legal/funding | Proposed $25k, no grant awarded | Recipient/payment eligibility, rights to traces/code, actual cost invoices, no BlueDot hour/deliverable duplication |
| Impact | Plausible oversight mechanism | Real operator study, measured unsafe-approval reduction, adoption pathway |

## Reviewer decision gates
**Release only when all are true:** (A) applicant confirms identity, lawful recipient and 120h availability; (B) contributor/IP permissions documented; (C) independently labeled study is feasible and ethical; (D) all overlapping funding tasks/hours reconciled with the existing guard; (E) proposed budget reconciled to actual future costs; (F) final applicant reviews exact current form, grant terms and causal claims. **If no independent operator evaluation can be arranged, narrow the request to exploratory tooling and remove claims of measured risk reduction; reconsider whether the fund is the correct payer.**

## Risk-adjusted economics (not sponsor statistics)
Existing subjective model: conditional lead economic surplus = $12,000 lead allocation − 120h×$35/h = **$7,800**. Feasibility 55% × conditional award probability 5% × $7,800 − $70 future application work = **+$144.50 prospective EV** before newly incurred research time. This worksheet estimated 0.5h × $35 = **$17.50**. No measured probability improvement: **standalone incremental EV −$17.50** unless it prevents a genuine eligibility error or leads to stronger independently verified evidence. At 55% feasibility and $7,800 surplus, break-even uplift in conditional selection probability is $17.50/(0.55×7,800) = **0.408 percentage points**, unmeasured.

**Status:** PURSUE (conditional), not submitted. No contact, spend, contract, rights transfer, or new benchmark result. Other active comparison: Bellingcat official $80k–$93k full-time 12-month contractor, November 8 deadline and AI-authored applications prohibited (https://www.bellingcat.com/contractor-ai-engineer-open-source-agentic-systems/); BlueDot $4,500 founder-time budget remains WATCH because cost-category eligibility and funding nonoverlap are unresolved (https://bluedot.org/grants/rapid). Their earlier EV scenarios are not comparable to a grant's restricted budget as gross income.
