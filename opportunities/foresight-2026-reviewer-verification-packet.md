# Control Where It Counts — reproducibility and evidence packet for grant review

**Prepared 2026-10-28 UTC | Foresight Institute, Human Empowerment | proposed $35,000 / 12 weeks | DRAFT, NOT SUBMITTED**

This is a concise, independently checkable evidence attachment for the [Foresight application narrative](foresight-2026-application-narrative.md). It separates **verified preparatory software** from **future research**. It does not establish applicant eligibility, grant approval, contractor commitments or intervention efficacy.

## One-minute reviewer verification

| Claim | Evidence | What it does **not** establish |
|---|---|---|
| **44/44 automated tests passed remotely** on October 28, 2026 UTC | [GitHub Actions run 40635208184](https://github.com/Svyable/Opps/actions/runs/40635208184), job `synthetic-protocol-contract`; logs report `Ran 44 tests` and `OK` | No real-agent experiment, human approval authentication, or causal safety effect |
| 8 study-design contract tests | [preregistration tests](../artifacts/foresight-control-2026/test_preregister.py) | Not preregistration of observed outcomes |
| 20 deterministic mock-boundary tests | [authorization-boundary tests](../artifacts/foresight-control-2026/test_gate_runner.py) | Not live tool-boundary security assurance |
| 8 synthetic protocol-to-mock-pilot tests | [pilot tests](../artifacts/foresight-control-2026/test_pilot_receipts.py) | Does not show real-agent behavior or intervention efficacy |
| 36 of 60 synthetic cases mapped to 108 mock receipts; 24 cases/72 assignments explicitly excluded | [pilot runner](../artifacts/foresight-control-2026/pilot_receipts.py), [CI execution](https://github.com/Svyable/Opps/actions/runs/40635208184) | Fixture labels supply grants; all 180 real experiment assignments remain unrun |
| 8 exact-power-calculator tests | [exact-power tests](../artifacts/foresight-control-2026/test_exact_power.py) | Not measured treatment effect or calibrated population power |
| 60 synthetic case specifications and 180 three-arm assignments | [study fixture](../artifacts/foresight-control-2026/README.md) and [generator](../artifacts/foresight-control-2026/preregister.py) | All assignments are **unrun**; no agent outcomes or blinded labels exist |
| Public code licensing checked | [license-rights audit](foresight-2026-public-license-rights-audit.md) | No proof of contractor chain of title, third-party data permission, or future-output rights |

**Reproduce with Python 3.11 (standard library only):**

```bash
python -m unittest discover -s artifacts/foresight-control-2026 -p 'test_*.py' -v
python artifacts/foresight-control-2026/preregister.py --write /tmp/cwic-manifest.json
python artifacts/foresight-control-2026/preregister.py --check /tmp/cwic-manifest.json
python artifacts/foresight-control-2026/gate_runner.py --demo
python artifacts/foresight-control-2026/exact_power.py --json
python artifacts/foresight-control-2026/pilot_receipts.py --summary
```

The CI job runs the test suite, manifest checks, mock demo, and a separate pilot CLI that writes 108 deterministic receipts and verifies all side-effect flags are false. The exact-power CLI is an optional local sensitivity report. The mock receipts are generated from fixture policy labels, not from AI-agent observations.

## Scientific claim boundary

**Proposed experiment, not a completed one:** randomized sandbox comparison of no gate, cosmetic approval, and enforced scoped authorization, measuring unauthorized completion, legitimate-task success, false blocks, latency, trace completeness and review burden. Genuine agent runs, independently authenticated approvals, frozen held-out labels, blinded reviewers and tool-side receipts are **future deliverables**.

**Sample-size caveat:** 60 cases comprise 20 clearly unauthorized, 20 authorized and 20 ambiguous cases per arm. Only **20 matched unauthorized cases per arm** inform the primary unauthorized-completion contrast. Under the illustrative independent-pair assumptions p(benefit)=0.30, p(harm)=0.10 and one-sided alpha=0.025, the exact-power calculation gives **17.36%**, not 80% power. The 12-week proposal must therefore be described as **exploratory**, not confirmatory. [Power annex](foresight-2026-paired-power-preflight.md).

**Decision rule:** If independent ground truth is missing, approvals are unauthenticated, tool-side traces disagree, or the boundary is bypassable, report uncertainty and abstain from any deployment recommendation. A negative finding is an intended publishable result.

## Grant deliverability and restrictions

The [official call](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/) closes **October 31, 2026 at 23:59 PDT**. It accepts individual and for-profit applicants, strongly prioritizes in-person work at its Nodes, requires open-source code/data/outputs, permits overhead up to 10% of direct research costs, and subjects successful applicants to due diligence and reporting.

The proposed **$35,000** budget is **$33,000 direct + $2,000 overhead** (6.06%). Two mutually exclusive staffing models exist: 240 founder hours / 120 independent engineering hours / 24 reviewer hours, or 144 / 200 / 40 respectively. They are planning estimates, not accepted quotations or actual available capacity. [Budget](foresight-2026-itemized-budget-capacity.md). The separate EA Funds Control Evidence proposal has [explicit cost and study separation controls](foresight-2026-dual-grant-overlap-controls.md); neither proposal has been submitted.

**Hard application gates:** applicant/payee identity and legal status; real weekly founder availability; consenting professional reference; actual engineer/reviewer capacity; rights to all funded outputs; credible Node participation or truthful remote-only disclosure; review of live Airtable form and sharing terms; explicit submission authorization. **Do not submit, contact anyone, spend, or accept any terms without approval.**

## Reviewer's bottom line

There is an independently reproducible **research starting point**, including a mock policy gate and a tested planning calculator. There is **no demonstrated efficacy, deployed system, independently validated annotation or recruited research team**. The proposed grant would fund the missing real-agent intervention experiment and independent evaluation, not retroactively reimburse these pre-award preparatory artifacts unless explicitly allowed.
