# Transformative AI Fund — Control Evidence (research pilot)

**Checked:** 2026-10-23 · **Status:** PURSUE (application not submitted) · **Sponsor:** EA Funds / Centre for Effective Altruism · **Deadline:** rolling.

**Funding:** official typical grants $10,000–$150,000, rarely above $300,000. **Current applicant-review choice: $25,000 over 10 weeks** (120 proposed lead hours, 12/week, not verified). The $50,000/12-week expansion is deferred unless 25 hours/week can be evidenced. Neither amount is an offer.

## Evidence and novelty gate

The proposed study asks whether an independent evaluator can distinguish an AI agent's *natural-language claims about completed actions and monitoring safeguards* from what incomplete or delayed execution/configuration records actually establish. Missing telemetry must produce abstention rather than an invented verdict. Provider acceptance is not the same as downstream delivery.

**Prior art to credit rather than rebrand:** [Auditable Claims about AI Agents](https://arxiv.org/abs/2610.07459) (5 Oct 2026) already defines claim auditability in terms of policy, scope, record authorship, completeness and a decision rule. [No Certificate, No Execution](https://arxiv.org/abs/2605.24462) studies pre-execution trace certification. [Langfuse](https://langfuse.com/docs/observability/features/agent-graphs) provides trace observability. [Tara Research](https://tararesearch.org/) studies agent dishonesty. The defensible increment is a **prospective independently labeled benchmark for claim-to-record adjudication under missing evidence**, not invention of auditability.

[OpenAI's 20 October 2026 incident report](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring/) motivates monitoring/alerting distinction, but does not establish that the proposed method would have prevented the incidents.

**Public asset reuse:** [Human Kind](https://github.com/Svyable/human-kind) bounded agent-authority protocols and [ScrolIQ](https://github.com/Svyable/scrollq) provenance and held-out evaluation methods. Transfer effectiveness is unproven. Prior locally reported test counts are not independently verified here.

## Economic and authorization gate

**Capacity-adjusted choice (23 Oct):** Lean $25,000 project / 120 lead hours: $12,000 proposed lead allocation − 120h × $35/h alternative labor = $7,800 conditional economic surplus; subjective 55% feasibility × 5% conditional selection − $70 preparation = **+$144.50 EV**. Expanded $50,000 project / 300 lead hours: $25,000 proposed lead allocation − 300h × $35/h = $14,500 conditional surplus; at conservative 20% feasibility × 5% selection − $70 = **+$75 EV**. These are sensitivity scenarios, not funder probabilities; expansion would overtake lean at ~29.6% feasibility with other assumptions unchanged. Restricted project funding is not personal income; neither selection probability is a sponsor statistic.

Applicant must verify 12h/week or 25h/week availability, identity/payee, outside-work/IP rights, other overlapping funding, independent reviewers, and personally review final answers. [EA Funds site terms](https://funds.effectivealtruism.org/terms-and-conditions) (updated 1 Oct 2026) treat user content as nonconfidential and grant broad noncommercial reuse rights; these are site terms, not a grant agreement. Do not upload unpublished manuscripts, private traces or restricted third-party code.

**Official fund:** https://funds.effectivealtruism.org/funds/transformative-ai

**Status:** No application submitted, no award, no contract or legal commitment.

## 23 October applicant package advancement

A single-scope $25,000 application-review packet has been prepared with a reconciled 10-week budget, preregistered false-support/abstention gates, prospective independent holdout plan, explicit prior-art credit and no claim of verified test performance. It is **not submitted**; applicant capacity, rights, payee and personally revised answers are mandatory. This public brief contains no private prototypes or applicant information.

## 24 October technical risk retired — nonfinite clock input

[Public contract implementation](../artifacts/control-evidence-2026/contract_smoke.py) now rejects NaN and ±infinity in approval/execution event times by returning `insufficient_evidence`, rather than permitting misleading ordering/refutation. Two adversarial regression methods were added; the full updated 12-method suite has **not** been independently confirmed to pass after this change. The 19 transparent smoke fixtures are not a held-out benchmark. The next funded milestone is authenticated telemetry with explicit clock uncertainty and blinded adjudication, not more self-scored synthetic fixtures.


## 24 October second-order execution-clock defect

The earlier NaN/infinity hardening checked only the `min()` of independent execution timestamps. With multiple execution records, `min([2.0, NaN])` or `min([2.0, +infinity])` yields `2.0`, allowing the invalid later record to be ignored and a false `supported` verdict. The [contract](../artifacts/control-evidence-2026/contract_smoke.py) now checks **every** execution and approval timestamp for finiteness before ordering; two additional regression methods bring the source to **14 test methods** (19 original visible fixtures unchanged). The fix is committed, but no post-fix Python run or successful remote CI is verified. See [technical appendix](../artifacts/control-evidence-2026/README.md). This is synthetic contract hardening, not independent agent telemetry validation.
