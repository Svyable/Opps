# Control Evidence — independent delivery sourcing packet (DRAFT; no commitments)

**Prepared:** 2026-10-26. **Opportunity:** EA Funds Transformative AI Fund; proposed $25,000 / ten-week research pilot. **Status:** PURSUE, NOT SUBMITTED. **Purpose:** turn the $10,500 uncommitted external-labor budget into two verifiable sourcing scopes, without claiming anyone has agreed to participate.

**Fund:** https://funds.effectivealtruism.org/funds/transformative-ai (rolling; typical $10k–$150k).
**Proposal:** [application draft](taif-control-evidence-2026-application-draft.md).
**Verified existing software:** [evidence dossier](taif-control-evidence-2026-verified-evidence.md), including 34/34 passing synthetic/unit tests in remote CI. **No authenticated real-world trace evaluation or independent human adjudication has been completed.**

## The cash-critical gate

The application budgets **$7,500 for independent engineering (100 hours × an unquoted $75/hour)** and **$3,000 for independent adjudication (30 hours × an unquoted $100/hour)**. These are **budget assumptions, not offers, market quotations, available contractors, or approved expenditure**. If independent staffing cannot be obtained, reduce the study, change the budget and explain the reduced evidence quality *before* applying. No contractor may be promised payment contingent on a grant without an applicant-approved agreement.

The research lead allocation remains **120 hours × $100 = $12,000**. Compute $1,000 and documentation/dissemination $1,500 complete the proposed $25,000 budget. Lead availability (12h/week) and legal payee are unverified.

## Role A — independent instrumentation engineer

**Estimated envelope:** up to 100 hours / $7,500 in the grant plan, subject to actual quotes and written authorization. Work expected mainly in weeks 2–6, with a limited reproducibility handoff in weeks 9–10.

**Mission:** build and verify isolated tool-side evidence capture that is not based solely on an agent's narrative or agent-authored logs. Three scoped claim families: (1) tool action completion, (2) authorization *before* action, (3) alert delivery versus provider acceptance. Use mock tools, fake identities and test credentials only; do not access live customer accounts or send external alerts.

**Proposed milestones (not yet contracted):**
1. **Design review (15h):** threat model, provenance schema, exact event identity, monotonic/UTC timestamp handling, independence boundary, failure modes, source licensing and a signed-off test plan.
2. **Instrumentation (45h):** mock-tool adapters and independent execution/approval/delivery receipts, with intentional missing, delayed, conflicting, reordered and tampered evidence.
3. **Freeze and reproduce (25h):** capture immutable source hashes, versioned fixture manifest, data-rights statement, reproducible runs, and a development/holdout separation mechanism.
4. **Handoff (15h):** runnable instructions, failure examples, security/privacy checklist and review of outstanding limitations.

**Acceptance evidence:** reproducible sandbox run; exact hashes for the code, trace schema and fixture set; documented negative controls; demonstrable separation of tool receipts from agent narratives; no network side effects; at least one test showing that missing/conflicting evidence cannot silently become “supported.” Do not certify the system as secure or production-ready.

**Independence/conflict screen:** disclose any role in authoring expected labels or reviewing outcomes; do not let the same person silently establish reference truth *and* judge blinded cases. Engineer may build instrumentation but must not grade their own evidence as an independent reviewer.

## Role B — blinded adjudicators

**Estimated envelope:** 30 reviewer hours in total / $3,000 budget assumption. This is an aggregate, not 30 hours per person. Prefer **at least two independently recruited reviewers** and reserve time for disagreement resolution; exact split is to be agreed only after real availability and rates are confirmed.

**Mission:** independently decide whether each claim is **supported**, **contradicted**, or **insufficient evidence**, using an explicit rubric. Compare narrative-only against structured receipt-supported conditions. Reviewers must not see reference labels before their judgments are frozen.

**Proposed milestones:**
1. **Calibration and conflict review (4h total):** sign confidentiality/data-use expectations as applicable, disclose conflicts, inspect rubric and do a small *non-holdout* practice set.
2. **Blinded judgments (20h total):** record verdict, reason, uncertainty/abstention, case ID and time spent; do not inspect private labels or developer annotations.
3. **Disagreement review and signoff (6h total):** document unresolved disagreements and ambiguous evidence, preserve individual decisions, and release a transparent methods note.

**Acceptance evidence:** consented reviewer identity/role; conflict statement; timestamped individual decision records; no reference-label access before freeze; complete denominator accounting including missing decisions; exact case/decision hashes; review-time logs; no claim of statistical power from the target of up to 60 cases.

**Independence:** a reviewer cannot be the engineer who instrumented or labeled the same holdout cases, nor a member of the project team with access to hidden reference answers. An external affiliation by itself does not establish independence.

## Candidate-screening matrix (to fill with actual, consenting people)

| Gate | Engineer | Reviewer | Current evidence |
|---|---|---|---|
| Identified candidate, relevant prior work | Required | Required | **NONE VERIFIED** |
| Conflicts and reference-label access disclosed | Required | Required | **NONE VERIFIED** |
| Hours within ten-week schedule | 100h target | 30h aggregate | **NONE VERIFIED** |
| Actual rate and payment conditions | Quote required | Quote required | **NONE VERIFIED** |
| Source code/data release and pre-existing IP carve-outs | Required | Required for permissible decisions/methods | **NONE VERIFIED** |
| Safe handling of synthetic/consented records | Required | Required | **NONE VERIFIED** |
| Right to publish negative findings | Required | Required | **NONE VERIFIED** |
| Applicant approves contact and any agreement | Required | Required | **NOT AUTHORIZED** |

**Screen-out conditions:** contractor requires production credentials; cannot disclose conflicts; cannot work with a blinded design; claims synthetic tests prove real-world safety; demands exclusive ownership of existing Svyable code; refuses to preserve negative findings; quotes exceed the budget without a credible scope reduction.

## Outreach drafts — NOT SENT

**Engineering inquiry subject: Paid independent sandbox instrumentation — AI-agent evidence pilot**

We are evaluating an independent engineering role for a proposed ten-week, grant-funded AI-agent evidence study. The scope is mock-tool instrumentation and independently authored execution, approval and delivery receipts—not production integration. Our planning budget is 100 hours at an *estimated*, not yet quoted, $75/hour; no funding or engagement has been secured. Would you be open to a short scope/rate/availability discussion, including conflicts, data handling and open-source deliverable rights? We can share the public protocol and repository before any commitment.

**Reviewer inquiry subject: Prospective paid blinded adjudication — agent-action evidence**

We are preparing a research proposal comparing AI-agent narratives with tool-side receipts. We seek independent reviewers who can judge supported, contradicted and insufficient-evidence cases without access to hidden labels. The planning envelope is 30 paid reviewer hours **across the reviewer pool** at an unquoted $100/hour assumption, subject to funding and approval. If the topic fits your experience, could you indicate relevant expertise, potential conflicts, availability and expected rate? No participation or payment is promised at this stage.

**These drafts are internal preparation only.** No recipient is identified, contacted, consented, or hired. Do not send without explicit authorization.

## Application decision rule

- **GO to applicant review:** applicant confirms legal recipient, 12h/week, code/data/IP rights, a realistic sourcing plan, and a budget that honestly describes uncommitted external roles; current application form and terms checked.
- **GO to submission only with explicit applicant approval.** A grant application may describe planned recruitment if the fund allows it; never describe estimates as signed contracts.
- **RESCOPE:** if rates or availability do not support two independent reviewers and receipt instrumentation, reduce target cases or duration, revise the $25k budget, and disclose loss of independence/power.
- **NO-GO:** if the evidence boundary or open-source rights cannot be secured, or if a conflict forces reviewers to grade their own labels.

## Opportunity economics and next action

Existing subjective model: **$7,800 conditional lead economic surplus × 55% feasibility × 5% selection − $70 incremental preparation = +$144.50**. This is *not* expected grant cash or a sponsor selection rate. Preparing this packet does **not** increase the assumed award probability or establish contractor availability.

**Next controlled action:** applicant approves or declines *outreach only* to candidate engineers/reviewers; obtain actual quotes, conflict declarations and availability. Separately verify payee, lead capacity, rights and the live Paperform fields. Do not submit or enter an agreement without explicit approval.
