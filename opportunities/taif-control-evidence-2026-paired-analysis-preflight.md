# Control Evidence — paired primary-endpoint analysis release preflight

**Prepared:** 2026-10-28 US Central. **Sponsor:** [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai). **Request:** $25,000 / 10 weeks, rolling. **Status:** PURSUE, NOT SUBMITTED. No human judgments, authenticated traces or efficacy results exist.

## The concrete methodological gap closed

The [two-arm allocation](../artifacts/control-evidence-2026/two_arm_design.py) assigns each case to one narrative-only reviewer and a different receipts reviewer, balancing receipt exposure within claim type. The prior `summarize` method only reported marginal counts by arm. Those counts are insufficient for the **case-paired** primary comparison promised in the proposal: they do not distinguish cases helped by receipts from cases harmed by receipts.

The new [paired analysis module](../artifacts/control-evidence-2026/paired_analysis.py) and [10 regression tests](../artifacts/control-evidence-2026/test_paired_analysis.py) preserve the case pairing and report four mutually exclusive categories for reference-non-support cases:

| Category | Narrative-only | With receipts | Meaning |
|---|---|---|---|
| Both false-support | supported | supported | Both reviewers incorrectly endorse a non-support claim |
| Beneficial discordance | supported | not supported | Receipts prevent false support |
| Harmful discordance | not supported | supported | Receipts introduce false support |
| Neither false-support | not supported | not supported | Neither endorses the claim |

The **prospective primary estimand** is (beneficial discordances minus harmful discordances) divided by the number of reference-non-support cases. `no_decision` and `insufficient_evidence` count as *not supported* for this specific error metric; their rates are separately reported by the earlier descriptive scorer. Cases with a `supported` reference are excluded from this primary denominator and must be reported as secondary false-rejection/appropriate-support outcomes.

The module also calculates the conventional **two-sided exact McNemar binomial p-value**, conditional on discordant pairs. The algorithm matches the standard exact-binomial formulation described in [statsmodels documentation](https://www.statsmodels.org/stable/generated/statsmodels.stats.contingency_tables.mcnemar.html). A p-value is not evidence until real judgments, independent reference labels, frozen assignments and a prospectively finalized analysis plan exist. No multiplicity-adjusted, powered causal claim is made. Two reviewers, case clusters, possible reviewer effects and the small non-support denominator can limit inference; consider a randomization-based sensitivity analysis before the study begins.

## Input integrity and privacy

The module requires matching dataset hashes, exactly two complementary arms per case, distinct reviewers per case, complete responses, nonduplicated pseudonymous case IDs, and valid verdict categories. Missing data trigger an error rather than being silently scored as correct. It does **not** authenticate receipts, source telemetry, reviewer independence or reference labels. Never commit real reviewer packets, assignments, response records, narratives, secret keys, source case IDs or reference keys. Use restricted local storage and freeze digests before review.

## Reproducibility and boundaries

Local test command:

```bash
python artifacts/control-evidence-2026/test_paired_analysis.py -v
```

**Verified:** 10/10 new tests passed locally and in [GitHub Actions run 40797112938](https://github.com/Svyable/Opps/actions/runs/40797112938), commit `910fdd7394087bb4f2db37b34c42c10a203cadb7`, job `123196147345`, with **55/55 tests total** across five suites (14 + 9 + 11 + 11 + 10). All test responses are synthetic; remote CI verifies code behavior, not research outcomes.

## Commercial effect, not a claimed award uplift

EA Funds [accepts rolling applications](https://funds.effectivealtruism.org/funds/transformative-ai), typically funds $10k–$150k early-stage projects and prioritizes advanced-AI catastrophic-risk reduction. The $25k request is a proposal, not cash won. This change fixes an important analysis-specification weakness without requiring new data or changing the proposed 30-hour reviewer envelope.

Keep the previous **illustrative +$144.50 marginal founder-surplus EV** unchanged: $7,800 conditional lead surplus × 55% subjective delivery feasibility × 5% subjective selection − $70 estimated application work. There is no calibrated basis for raising selection odds. Additional engineering time is a real pursuit cost, not automatically reimbursable.

**Release blockers:** verified legal payee, actual 12 lead hours/week, independent reviewers and engineering, source/IP rights, data and consent permissions, live Paperform terms, and explicit authorization to apply. No external contact, spending, form submission or terms acceptance is authorized.
