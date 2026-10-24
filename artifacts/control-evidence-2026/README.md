# Control Evidence — executable synthetic contract smoke test
**Prepared:** 2026-10-24 | **Funding target:** EA Funds Transformative AI Fund (rolling) | **Requested pilot:** $25,000 / 10 weeks | **Status:** public technical appendix, NOT an application or empirical result.

**Run locally (Python 3.10+, standard library only):**

```bash
python artifacts/control-evidence-2026/contract_smoke.py -v
python artifacts/control-evidence-2026/contract_smoke.py --fixtures
```

## Reproducibility check — 2026-10-24

The exact committed Python file was reproduced locally and its Git blob SHA-1 matched GitHub's file blob (`c95be1d7a8d9d161be5b46c8cd51d0f5459f032f`). Command: `python contract_smoke.py -v`. **10/10 unit-test methods passed**, including all 19 visible fixture verdicts. This verifies deterministic contract behavior under its declared synthetic assumptions, **not** correctness on real agent telemetry or independent evaluation. GitHub Actions workflow `.github/workflows/control-evidence-contract.yml` was committed; no successful remote workflow status has been independently confirmed.

## What is now real

The committed `contract_smoke.py` defines an executable **three-verdict claim-to-record decision contract** for exactly three narrow claim types: `action_completed`, `approval_before_action`, and `alert_delivered`. It includes **19 transparent, deterministic synthetic fixtures** (six expected support, six expected refutation, seven expected abstention) and **10 unit-test methods**. The fixtures are visible and hand-constructed. They are *not* a blind test, not agent traces, not a sample of deployed systems, and not evidence of model accuracy. The test program does not call external services or access secrets.

The rules explicitly refuse to promote agent-authored logs, wrong-scope or wrong-argument records, partial coverage, mere provider acceptance, or conflicting records to proof of a claim. For the approval-before-action claim, the contract requires an independent, argument-bound approval timestamp earlier than an independently recorded execution timestamp. An explicit trustworthy failure may refute even when coverage is partial; silence never refutes. The result `insufficient_evidence` is an intended and reportable outcome.

**Critical security limitation:** the synthetic `writer: independent` and `coverage_writer: independent` fields are *labels*, not authenticated attestations. In a real system, the evaluation must independently verify recorder identity, integrity, time order, and completeness. This script is a contract and regression smoke test only. It must not be used to certify real agent actions.

## 24 October adversarial clock-boundary hardening

The synthetic contract previously accepted Python/JSON-adjacent nonfinite event timestamps (NaN, positive infinity, negative infinity) in `approval_before_action`. Python's floating-point comparisons can silently turn such inputs into a false `refuted` verdict or an untrustworthy order comparison. The code now **abstains** when any relevant approval or execution timestamp is nonfinite, with two additional regression methods covering both event classes (12 test methods in source, versus 10 originally). The 19 original visible fixtures are unchanged.

This closes a *specific implementation failure mode*, not the broader problem of trusted clocks. Real event ordering still requires authenticated source identity, clock-skew bounds, monotonic event sequencing, and completeness witnesses. Do not treat this patch as real-world validation. The earlier 10/10 local result predates this patch; the updated 12-method suite requires a fresh CI or local run before claiming all tests pass.

## Why a grant is still needed

The proposed research is **not** to invent agent auditability. [Auditable Claims about AI Agents](https://arxiv.org/abs/2610.07459) (5 Oct 2026) already formalizes the policy, scope, record authorship, completeness and decision-rule requirements. [Auditable Agents](https://arxiv.org/abs/2604.05485) also predates this pilot. The genuinely unresolved question is **how independently blinded reviewers and methods behave on claim-to-record adjudication when real telemetry is delayed, missing, contradictory or misleading**.

This artifact reduces a specific feasibility risk: it makes the proposed verdict grammar executable before funding. It does **not** reduce uncertainty about real-world measurement quality, evaluator agreement, data access or the sponsor's selection probability.

## Proposed prospective evaluation — not yet run

1. Freeze a claim schema, record-authorship verification protocol, completeness witness, privacy/sandbox rules, analysis script, exclusion policy, and at least 60 task scenarios **before** collecting final traces. The 19 visible fixtures remain training/smoke material, never the held-out score.
2. Obtain genuinely independent review of a held-out set. Blind reviewers to case construction and method verdict where feasible; track disagreement, resolution, and review time. No reviewer has been recruited or consented.
3. Compare a narrative-only baseline, a trace-search baseline, and a structured claim-to-trace adjudicator. Count all attempts, missing records and abstentions in denominators.
4. Report **false support rate** as the primary safety failure: proportion of objectively unsupported/refuted claims that the system incorrectly marks `supported`, with raw denominators and uncertainty intervals. Also report correct refutations, abstention calibration, reviewer agreement and time.
5. Require independent recorder identity, integrity, argument binding and completeness; treat missing witnesses as abstentions. No synthetic fixture label may be mistaken for authenticated telemetry.
6. Publish negative results, including cases where the structured method adds no value or where reviewers cannot reach agreement. Avoid claims of catastrophic-risk reduction from synthetic experiments.

**Stop / revise rule:** If the pilot cannot obtain credible independent ground truth or record-authorship evidence, do not score claims as supported. Publish a feasibility failure and scope down. If the evaluation relies only on synthetic fixtures, label its external validity unknown.

## Commercial and delivery boundaries

- **Fund:** [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) — accepts early-stage individuals and organizations, typical $10k–$150k, rolling.
- **Proposed $25,000 / 10-week project:** founder 120h (12/week) and $12,000 allocation, with remaining $13,000 for independent evaluation, engineering, compute and dissemination per the applicant packet. All allocations and capacity remain unverified; no grant is awarded.
- **Existing assets:** [Human Kind](https://github.com/Svyable/human-kind) agent-authority boundaries; [ScrolIQ](https://github.com/Svyable/scrollq) evidence provenance and fail-closed validation.
- **No double funding:** TAIF covers retrospective claim-to-record reconciliation. The separate Foresight proposal covers prospective *causal effect of enforced human veto*. Shared code may be reused openly; grant-paid hours and deliverables must not be charged twice.
- **Applicant-controlled gates:** legal payee, 12h/week, IP/third-party licenses, external reviewers, privacy/data permission, exact application fields and personal final approval.
- **No external outreach, grant submission, expenses or commitments have occurred.**

**Interpretation:** A runnable smoke-test contract is a useful application attachment. It is not evidence that a $25,000 pilot has already succeeded.
