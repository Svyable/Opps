# Anthropic AI Safety & Security Fellows — October 13 evidence preflight

**Status:** PURSUE (eligibility-gated); **January cohort application cutoff:** 2026-10-18.
**Official opportunity:** https://job-boards.greenhouse.io/anthropic/jobs/5183044008
**Official AI-use policy:** https://www.anthropic.com/candidate-ai-guidance

## Financial screening

The official posting lists USD $3,850/week for four months (40 hours/week), a $61,600 illustrative 16-week stipend. At an assumed $35/hour alternative labor value, the conditional economic surplus is $61,600 − (640 × $35) = $39,200. With *subjective*, unverified qualification 25% and conditional selection 2.5%, less four hours of preparation ($140), the modeled EV is **+$105**. This is **personal income**, not Svyable contract revenue. Actual eligibility or selection may be zero.

## Evidence and falsification

Existing Svyable/scrollq [model-evaluation protocol](https://github.com/Svyable/scrollq/blob/main/docs/model-evaluation.md) specifies model/data binding, held-out manifests, failure-inclusive aggregation and hashes. [Human Kind's agent protocol](https://github.com/Svyable/human-kind/blob/main/docs/agent-protocol.md) distinguishes repository authority from external operational authority.

The prior synthetic Human–Agent Boundary Ledger test accepted 24/24 constructed legitimate chains and rejected 24/24 constructed corrupted chains. This is **not** a real-world safety result. A new *post-hoc, non-blind* stress suite tested six **authorization-ready policy violations** outside the original test taxonomy. The narrow validator accepted all six. It also accepts the same event chain on repeated calls because it has no replay state. These are gaps **relative to a stronger external authorization policy**, not necessarily bugs in the documented synthetic contract. The next research step is to freeze a threat model and obtain independently authored cases, with real identity/authentication and cost-of-review controls, before claiming generalization.

The complete reproducible stress suite and tests are preserved in the October 13 downloadable preparation package. Eight standard-library unittest groups passed, including four new groups that assert the observed limitations. Passing tests do not certify authorization or model safety.

## Application gates — do not guess

- Verify candidate's full-time work authorization and location in US, UK or Canada. The Fellows program **does not sponsor visas**.
- Verify 40h/week availability for four months, Python fluency, actual personal contribution to cited repositories, CV and references.
- Submit via the **Constellation application**, not Greenhouse alone; the form is linked from the official posting.
- Candidate writes the **first draft of every application response** personally. AI may refine afterward. Do not use AI during assessments unless explicitly permitted.
- No application, outreach, registration, payment or commitment authorized by this document.

**Decision:** Finish applicant-owned evidence and eligibility verification before October 18. Do not spend more time on synthetic scoring absent independent challenge data.
