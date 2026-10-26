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

## 24 October follow-up: multi-execution timestamp bypass fixed

A second flaw remained after the first nonfinite-clock fix. The original approval rule computed `min(execution_timestamps)` and validated only that **one selected minimum**. Python's `min([2.0, float("nan")])` returns `2.0`, and `min([2.0, float("inf")])` also returns `2.0`. A later invalid execution record could therefore disappear from validation, allowing a false `supported` verdict. This was an implementation defect in the public synthetic contract, **not** evidence of a deployed-system exploit.

The rule now parses **every** independent execution and approval timestamp, requires all of them to be finite, and only then selects the first execution. Two regression methods cover a nonfinite **additional** execution and a nonfinite **additional** approval; the source now has **14 unit-test methods** and retains the same 19 visible synthetic fixtures. The code change and tests were committed, but an end-to-end Python run of this updated revision and successful remote CI status have **not** been verified in this run. Do not report a 14/14 pass until a test runner confirms it.

**Research implication:** real-world authorization ordering also requires clock-domain identification, bounded skew and independent recorder integrity. This patch strengthens a deterministic decision contract; it does not establish authenticated telemetry or real-world accuracy.

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

## 25 October — prospective blinded reviewer-packet builder (synthetic contract, NOT a review result)

[blind_packet.py](blind_packet.py) now converts an applicant-controlled case manifest into two **separate local files**: a reviewer packet with claim/evidence but **no adjudication labels or original case IDs**, and a private label-key file linking pseudonymous review IDs to case IDs and expected verdicts. Both are bound to the SHA-256 of the exact input bytes. Review IDs use a secret-keyed HMAC; a different key changes identifiers. The generator rejects duplicate IDs, unknown claim/label fields, unexpected event fields, weak secret files and existing output paths. Both outputs are created with mode 0600. [Nine regression tests](test_blind_packet.py) exercise separation, determinism, input refusal and CLI file permissions; the equivalent code passed all nine tests locally on 2026-10-25. The GitHub Actions workflow now requests those tests on pushes; **remote CI success has not been independently verified**.

Example with a **permissioned, local-only** manifest (do not commit the input, key or generated files):

```bash
umask 077
python -c 'import secrets; open("local-secret.bin","wb").write(secrets.token_bytes(32))'
python artifacts/control-evidence-2026/blind_packet.py \
  --source /secure/frozen-cases.json \
  --secret-file local-secret.bin \
  --reviewer-out /secure/reviewer-packet.json \
  --private-key-out /secure/private-label-key.json
python artifacts/control-evidence-2026/test_blind_packet.py -v
```

Required source structure: `{"dataset_id":"...", "cases":[{"case_id":"...", "claim_type":"action_completed", "scope_id":"...", "action_id":"...", "args_digest":"...", "coverage":"complete", "coverage_writer":"independent", "events":[], "expected_verdict":"insufficient_evidence"}]}`. This example is **synthetic**. A field saying `writer=independent` is not a cryptographic authentication of its author; real records still need trusted source identity, consent, clock integrity and independently determined labels. Blinding labels in a packet does not make publicly visible fixtures an independent holdout. Do not publish source truth, private keys, permissioned traces or private reviewer data.

**Remaining funding-dependent step:** acquire authorized independent traces and reviewers, freeze a genuinely unseen test set, obtain blinded decisions, and only then compute false-support and abstention rates. No such data or reviewer decisions exist here.

## 25 October — reference-label scoring contract (prospective; not an empirical result)

[`score_reviews.py`](score_reviews.py) accepts the frozen blinded reviewer packet, the **private** reference-label key produced by `blind_packet.py`, and a separate reviewer-response JSON. It verifies the shared dataset identifier, source SHA-256 metadata, case count, packet types and case IDs; rejects duplicate or unknown reviewer/case decisions; and requires an explicit verdict for every case, including `no_decision`. It creates a non-overwriting mode-0600 result file with per-reviewer reference-label agreement, support asserted against a non-support reference, abstentions, a confusion table and Wilson 95% intervals. Zero denominators are `null`, never silently zero.

**Reviewer-response schema** (private; do not commit): `{"schema_version":1,"dataset_id":"<same>","source_sha256":"<same 64-hex>","case_count":3,"packet_type":"reviewer_responses","judgments":[{"reviewer_id":"R1","review_id":"<blinded ID>","verdict":"no_decision"}]}`. Supply exactly one judgment per reviewer per blinded case; allowed verdicts are `supported`, `refuted`, `insufficient_evidence`, and `no_decision`. Missing decisions must be recorded explicitly rather than disappearing from the denominator.

Run locally with Python 3.10+ and no external dependencies:

```bash
python artifacts/control-evidence-2026/test_score_reviews.py -v
python artifacts/control-evidence-2026/score_reviews.py \
  --packet /secure/reviewer-packet.json \
  --private-key /secure/private-label-key.json \
  --responses /secure/reviewer-responses.json \
  --output /secure/reviewer-score.json
```

**Validation boundary:** 11 regression methods passed locally on the equivalent implementation on 2026-10-25; a remote GitHub Actions success has not yet been independently confirmed. The tests use **three deliberately synthetic cases** and do not measure reviewer performance. The binding fields are untrusted metadata until source provenance and packet integrity are independently verified; a claimed `independent` recorder or `expected_verdict` is **not** authenticated ground truth. The scorer deliberately outputs `reference_is_ground_truth: false` and avoids calling agreement an accuracy estimate. An actual funded study must secure authentic evidence, frozen held-out labels, consent, blinded independent reviewers, and a preregistered analysis before drawing substantive conclusions. The scorer does not estimate AI safety improvement or sponsor award probability.
