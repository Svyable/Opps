# Epistemics Fund — preregistered pilot evaluation protocol (UNSUBMITTED; draft v0.1)

Prepared 2026-11-23 for the existing $50,000 illustrative Ought / Lightcone Commons application. This is a **technical attachment proposal**, not a completed study, independent audit, grant requirement, or evidence of measured benefit. No participants recruited, data collected, evaluator appointed, or costs incurred.

## Research question and falsifiable claim
Does an inspectable claim–source–action evidence interface reduce reviewers' *false acceptance of unsupported claims* compared with a baseline source display, without materially reducing acceptance of genuinely supported claims? This is about reviewer calibration, **not** proof that an agent executed a protected action or a generalized AI safety improvement.

## Unit, conditions, and labels
- Unit: a reviewer judgment of a pre-labeled claim/evidence case. Recruit consenting reviewers, avoid collecting unnecessary personal information, and obtain any required ethics/privacy review before recruitment.
- Baseline: claim plus conventional source citation/context; treatment: same claim and underlying evidence plus explicit provenance links, custody/identity uncertainty, and OBSERVED_ONLY versus VERIFIED labels where justified.
- Cases: supported, unsupported, and ambiguous; separate "missing action" from "action occurred but evidence insufficient". Independently establish gold labels *before* exposure; labeler blinded to UI assignment where feasible. No synthetic example may be presented as a real-world observation.
- Primary outcome: false-support rate among truly unsupported cases. Secondary: true-support rate among supported cases, calibration (confidence versus correctness), response time, and usability.

## Design and analysis plan
1. Freeze a versioned case set, labeling rubric, UI snapshots, exclusion criteria, and analysis script before the first real participant. Document source licenses and consent.
2. Randomize case presentation and condition within reviewer, counterbalance order, and prevent a reviewer seeing the same case in both conditions where recall could contaminate judgments. Use matched case strata and reviewer-clustered inference.
3. Pre-specify a practically meaningful minimum improvement and acceptable noninferiority margin for true-support rate **with an independent evaluator**. Do not select these margins after seeing results.
4. Estimate condition-specific false-support rates and treatment-minus-baseline difference with uncertainty intervals accounting for clustering by reviewer/case. Report raw denominators and abstentions. Include an intention-to-treat analysis and a sensitivity analysis treating abstention as non-acceptance.
5. Use a preregistered noninferiority check on true-support rate; a point estimate alone is insufficient. Report multiplicity and exploratory analyses separately.
6. Publish anonymized, rights-cleared case manifests, exact code revision, scripts, protocol deviations, failures, and limitations. If custody or identity cannot be independently established, use OBSERVED_ONLY rather than VERIFIED.

## Feasibility gate, not a power claim
Existing internal gate of >=100 omitted-action and >=100 executed-action trials is a **software smoke threshold**, not a statistically justified sample size for human reviewers. Power/sample size must be calculated from plausible baseline rates, target effect, reviewer/case clustering, and attrition **before recruitment**. If resources cannot support adequate precision, label the project a feasibility pilot and do not claim a definitive effect. Do not substitute simulated trials for human data.

## Failure criteria and honest reporting
- No claim of efficacy if treatment fails the prespecified primary improvement criterion, harms true-support beyond the agreed margin, or data quality is insufficient.
- No claim of independent verification absent external custody/identity evidence.
- Report negative/null results and all preregistered deviations; no cherry-picking of successful cases.

## Funding separation and release requirements
Epistemics work covers public claim/source provenance and human decision calibration. TAIF work covers protected agent-action recording, isolation/shutdown evidence, and related safety experiments. Shared pre-existing code is not billed twice. Before submission, obtain: legal payee eligibility; code/data rights; three consenting references if required; independent evaluator; itemized supported costs; official portal terms; and explicit owner approval. Illustrative $50k ask is not an award or approved budget.

## Source verification (2026-11-23)
- Organizer announcement and fund description: https://epistemic.fund/ (automated fetch failed); https://www.lightconecommons.com/epistemics/apply (automated fetch failed).
- Secondary listing: https://www.leadersoftoday.com/opportunities/epistemics-fund-2026 (November 26, 2026; claims 23:59 UTC, but simultaneously notes official closing hour unspecified). Treat November 25 as internal safety target, **not** official closing time.
- Existing application draft: https://github.com/Svyable/Opps/blob/main/opportunities/2026-11-22-epistemics-fund-application-draft.md

**Status: PURSUE / HOLD.** No submission, spending, outreach, or commitments authorized by this document.
