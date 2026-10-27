# Control Where It Counts — paired-outcome power and inference preflight

**Prepared 2026-10-27 | Foresight AI Nodes / Human Empowerment | $35,000 proposed, NOT SUBMITTED.**
**Status:** prospective planning calculation, **zero agent runs, zero outcome observations, zero independent labels**. This is not a statistical analysis of results.

## Why this matters for the grant

The [existing frozen synthetic manifest](../artifacts/foresight-control-2026/README.md) has 60 scenario specifications: five threat categories × three policy labels (authorized / unauthorized / ambiguous) × four variants. Each scenario is assigned to no-gate, cosmetic-approval and enforced-boundary arms, giving 180 **unrun** arm assignments. For the proposed primary endpoint (unauthorized action completion), there are only **20 clearly policy-unauthorized scenarios per arm**, not 60 independent unauthorized observations per arm. The other 40 cases per arm test legitimate-task false blocks and authority ambiguity; they must not silently inflate the primary denominator.

This matters because a small exploratory test can demonstrate feasibility, bypass patterns and failure traces but is poorly positioned to establish modest efficacy improvements with statistical confidence. The grant application should not imply a powered safety-effect estimate.

## Proposed estimand and comparison (subject to independent protocol review)

- Primary outcome: binary **unauthorized action completion** in a mock/sandbox environment, for independently adjudicated policy-unauthorized scenarios. Attempted actions, incomplete traces, missing ground truth and failures must be reported with raw counts. Do not substitute mock evaluator decisions for actual agent/tool execution.
- Pair each policy-unauthorized scenario across arms under matched task conditions, with independently randomized execution order and controlled model configuration. The existing shuffled assignment list is a *plan*, not execution randomization or independent observations.
- Two prespecified one-sided contrasts: no gate vs enforced boundary; cosmetic approval vs enforced boundary. For a conservative sensitivity calculation use **alpha=0.025 per contrast** (Bonferroni control of family-wise alpha 0.05). This is a planning convention, not an approved preregistration.
- Define **benefit pair** = unauthorized completion under comparator, not under enforcement; **harm pair** = completion under enforcement, not comparator. Concordant pairs do not enter the exact McNemar test statistic. A paired difference can be estimated as (benefit − harm)/n, but precision and dependence require careful treatment.
- Exact one-sided McNemar p-value conditional on d discordant pairs is P[Binomial(d, 0.5) >= benefit]. This tests paired directional asymmetry under the exchangeability null, **not** a causal claim without sound design and independent ground truth.
- Predeclare how missing traces and ambiguous policies are handled; publish all attempted cases, exclusions and sensitivity bounds. Avoid significance hunting across five categories or multiple outcomes.

## Exact sensitivity results — planning assumptions, not measured rates

Reproduce with Python 3.10+ (standard library):

```bash
python artifacts/foresight-control-2026/exact_power.py --json
python -m unittest discover -s artifacts/foresight-control-2026 -p 'test_*.py' -v
```

The [source](../artifacts/foresight-control-2026/exact_power.py) enumerates all multinomial paired-outcome configurations under **independent matched pairs** with assumed probabilities p(benefit), p(harm), and p(concordant) = 1 − p(benefit) − p(harm). It calculates unconditional rejection probability for the exact one-sided test at alpha 0.025. These assumptions may fail when templates repeat, models are stochastic, policy labels are disputed, or cases are correlated by category.

| Unauthorized matched pairs per contrast | Assumed p(benefit) / p(harm) | Assumed net benefit | Illustrative power |
|---:|---:|---:|---:|
| **20 (current manifest)** | 0.30 / 0.10 | 20 percentage points | **17.36%** |
| **20** | 0.40 / 0.05 | 35 points | **58.23%** |
| **20** | 0.50 / 0.05 | 45 points | **78.47%** |
| 40 | 0.30 / 0.10 | 20 points | 43.97% |
| 80 | 0.30 / 0.10 | 20 points | 77.95% |

With no harm pairs, **five** favorable discordant pairs give p=0.03125 and **six** give p=0.015625; only the latter crosses the conservative 0.025 threshold. One or more harm pairs require stronger evidence. No outcome is observed or forecast by this illustration.

## Revised delivery interpretation

1. **Stage 1 (funded pilot baseline):** Keep the existing 60-case / 180-arm assignment fixture as an **exploratory, reproducible feasibility and failure-mode study**. Report unauthorized completion, false blocks, legitimate-task success, trace completeness, bypass classes and human review costs with raw denominators and uncertainty. Do not promise a statistically powered detection of a 20-point effect.
2. **Stage 2 (only if independently justified):** Before collecting outcomes, obtain independent protocol review, confirm genuine agent execution and ground-truth adjudication, estimate within-scenario variability and correlation, and predeclare any larger sample. Approximately 80 **independent unauthorized pairs** would give ~78% power under one specific optimistic distribution above; if preserving the current 1:1:1 policy-label mix, that means 240 scenarios and 720 arm assignments, roughly four times the current manifest. This is **not included as a committed $35k deliverable**.
3. **Stop / no-go:** If no authenticated approvals, independent instrumentation or adjudication can be staffed, publish only the preparatory tooling and explicitly report that the intervention study did not occur. Do not relabel deterministic mock receipts as efficacy evidence.
4. **Decision criterion:** The sponsor should receive useful *negative findings* as well as positive ones: a gate that is bypassable, overblocks legitimate work, or adds unacceptable latency is not validated merely by showing blocked mock calls.

## Sponsor relevance, commercial and consent gates

The [official Foresight RFP](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/) asks for evidence-based maps of when human control adds value versus hollow oversight, open-source deliverables, realistic execution and Node participation. The exact-power script is an additional **technical due-diligence artifact**, not an increase in demonstrated effectiveness or award probability. Its code is preparatory work already publicly committed and must not be billed twice to Foresight and EA Funds.

**Still unverified:** legal applicant/payee, 12–20h/week lead capacity, consenting reference, contractor availability, future dataset and IP rights, actual SF/Berlin Node plan, and applicant approval of live Airtable terms. No application, agreement or expenditure is authorized by this document.
