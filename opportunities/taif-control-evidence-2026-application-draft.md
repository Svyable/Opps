# Transformative AI Fund — Control Evidence: applicant-review submission draft

**Prepared 2026-10-25 · $25,000 proposed / 10 weeks · PURSUE · NOT SUBMITTED.**
Official fund: https://funds.effectivealtruism.org/funds/transformative-ai
Official application entry: https://av20jp3z.paperform.co/?fund=Transformative+AI+Fund
The public Paperform could not be inspected reliably on 2026-10-25. **These are candidate answers, not verified form fields or character limits.** Applicant must adapt and personally approve them. No legal recipient, collaborator, staffing, or institutional affiliation is asserted.

## Candidate project title
**Control Evidence: Can We Prove What an AI Agent Actually Did?**

## Short project summary (candidate; adapt to live field)
An agent can say it sent an alert, obtained approval, or completed an action. The trace may establish something narrower—or nothing at all. Control Evidence proposes a ten-week, $25,000 pilot testing whether independent reviewers can distinguish supported, contradicted, and unprovable agent claims from execution-side records. We will build a consented sandbox trace set, preregister adjudication rules, blind reviewers to reference labels, and publish failure cases and a reproducible evaluation protocol. The result may be negative.

## What problem does the project solve?
As autonomous systems gain authority to use tools, a natural-language report of what happened is not reliable evidence that it happened. A provider accepting an alert is not the same as the alert reaching its recipient. A UI displaying approval is not proof that authorization preceded execution. An agent-authored log is not an independent witness.

This is not a proposal to certify agents as safe. It asks a smaller, falsifiable question: **given imperfect records, when is an external reviewer justified in believing a claim about an agent action?** A system that reports certainty from partial traces can hide exactly the failure a human overseer needs to notice. Conversely, a system that always abstains is not useful. The pilot measures that tradeoff.

## What will be done, and what would count as success?
**Weeks 1–2:** Review prior art, confirm data rights, freeze claim types, trace schema, ground-truth and missingness rules, sampling protocol and the analysis plan. No outcome labels will be changed after blinded review begins.

**Weeks 3–4:** Build isolated mock-tool adapters and capture independently authored receipts for three scoped claim types: action completion, approval before action, and alert delivery. Use no real credentials, external messages, or private user records. Intentionally inject missing, delayed, conflicting and misleading records.

**Weeks 5–6:** Assemble a prospective evaluation set targeting up to 60 adjudicable and explicitly non-adjudicable cases. Separate development examples from the final holdout; report actual counts and shortfalls. Produce a blinded reviewer packet and keep reference labels inaccessible to reviewers.

**Weeks 7–8:** Recruit and compensate independent adjudicators if availability and consent are verified. Compare judgments from narrative-only descriptions against judgments with structured evidence receipts. Record disagreements, review time, and cases where no responsible conclusion is possible.

**Weeks 9–10:** Publish permissible synthetic data, schema, scripts, denominator-level results, uncertainty, disagreements, negative findings and a replication guide. If independent telemetry or reviewer capacity cannot be secured, publish the limitation and a smaller feasibility result rather than imply validation.

**Primary readouts:** false-support rate among claims with independently established contradictory or insufficient evidence; justified abstention on incomplete records; and unjustified rejection of claims with sufficient independent support. Report the exact denominators and uncertainty intervals for each category. Secondary readouts: adjudicator agreement and time-to-verdict. Sixty cases is a planning target, **not** a power calculation. No precommitted effect size or risk-reduction claim is justified yet.

## Why this could matter for transformative-AI risk
Advanced agents may take consequential actions faster than humans can directly observe. If organizations rely on unsupported self-reports, oversight becomes a story told after the fact. The near-term contribution is a reusable method for exposing that evidentiary gap, especially when telemetry is missing or internally inconsistent. Whether it transfers to frontier-agent deployments is an empirical question; this pilot will not claim to have solved it.

## Why this is new enough to fund
Existing work already covers claim auditability, trace observability and pre-execution certification. Credit, rather than rename, that work:
- Auditable Claims about AI Agents: https://arxiv.org/abs/2610.07459
- No Certificate, No Execution: https://arxiv.org/abs/2605.24462
- Langfuse trace observability: https://langfuse.com/docs/observability/features/agent-graphs

The incremental deliverable is a **prospective, independently adjudicated comparison** of narrative-only versus receipt-supported claim verification under explicit missing-evidence conditions. It is not a claim to have invented auditing or to have validated the current synthetic contract.

## Existing work that reduces execution risk
- Svyable Human Kind authorization concepts: https://github.com/Svyable/human-kind
- ScrolIQ provenance and evidence-integrity practices: https://github.com/Svyable/scrollq
- Visible 19-case synthetic contract and 14 test methods: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/contract_smoke.py
- Prospective blinded packet builder and nine test methods: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/blind_packet.py
- Prospective reviewer reference-label scorer: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/score_reviews.py
- **Independently checkable CI receipt:** https://github.com/Svyable/Opps/actions/runs/40251427716 — 34/34 synthetic/unit tests passed on commit `c98d79cc8761b9fe9cc134e190e3394438efb8fc` (14 contract + 9 blind-packet + 11 scoring). Source blobs, licenses, limitations and applicant gates: https://github.com/Svyable/Opps/blob/main/opportunities/taif-control-evidence-2026-verified-evidence.md

These are **preparatory artifacts**. Remote CI passed the synthetic/unit suites, but that does **not** demonstrate accuracy on independently authenticated traces, a frozen held-out benchmark, completed human review, or transfer to deployed agents. The applicant's IP, staffing, legal-payee and availability gates remain unresolved.

## Proposed budget — $25,000 total, all figures unquoted estimates
| Cost | Calculation | Amount |
|---|---|---:|
| Research lead: protocol, data generation, analysis, release | 120 hours × $100 | $12,000 |
| Independent engineering and instrumented sandbox | 100 hours × $75 | $7,500 |
| Independent adjudication and disagreement review | 30 hours × $100 | $3,000 |
| Isolated compute, storage and reproducibility | estimate | $1,000 |
| Documentation, accessibility and dissemination | estimate | $1,500 |
| **Total** | | **$25,000** |

This assumes **12 lead hours/week for ten weeks**, not yet verified. The engineering and reviewer allocations are **not quotations, hires or promises**. There is no contingency; if vendor costs differ, rescope or revise the request before submitting. No expense may be incurred on the assumption of funding.

## Why grant funding rather than a commercial sale?
The value of this work depends on publishing failure cases, an inspectable protocol and negative results, not just building a proprietary compliance dashboard for a customer. A small early-stage grant could pay for independent evidence that existing public code alone cannot provide. The applicant must verify there is no customer or grant agreement that already pays for this work.

## Separation from the Foresight proposal
This application would fund **retrospective claim-to-record adjudication**. The separate Foresight Human Empowerment application proposes **prospective causal testing of enforced human authorization gates**. Shared pre-existing code may be reused subject to licenses, but the same personnel hours, cases, data collection, deliverables and invoices must not be charged to both. Maintain separate time sheets and outputs if either is funded.

## Critical applicant-controlled gates — STOP until established
1. Confirm actual legal recipient, jurisdiction, tax status and payment arrangements.
2. Confirm 12 hours/week of lead availability for ten weeks; if false, rescope.
3. Verify code ownership, employment/outside-work restrictions, third-party licenses and release rights.
4. Confirm engineering and independent reviewer availability, rates, conflicts, consent and privacy/data handling.
5. Review current application questions and all site terms. Do not upload private traces, unpublished manuscripts, or confidential IP to a public/nonconfidential form.
6. Replace any generic phrasing with applicant's own research judgment and confirm the exact empirical promises.
7. Explicitly authorize submission separately. **This draft does not authorize an application, spending, outreach or acceptance of terms.**

## Economic screening (not an award forecast)
Assuming $12,000 lead allocation, 120h × $35/h alternative labor cost, 55% project feasibility, 5% conditional selection and $70 further preparation: ($12,000 − $4,200) × 0.55 × 0.05 − $70 = **+$144.50 illustrative net economic surplus EV**. These are subjective probabilities, not EA Funds statistics. Restricted grant funding is not unrestricted personal revenue.

**Decision: PURSUE the applicant-controlled submission gate; no form submitted.**
