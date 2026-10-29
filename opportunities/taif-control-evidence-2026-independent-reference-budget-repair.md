# Control Evidence — independent reference adjudication and corrected review-hour budget

**Prepared 2026-10-29 UTC · EA Funds Transformative AI Fund · applicant-review proposal only · no human study, hiring, grant application or empirical result.**

**Sponsor:** https://funds.effectivealtruism.org/funds/transformative-ai (rolling; typical grants $10k–$150k).  
**Existing design:** [two-arm allocation](../artifacts/control-evidence-2026/two_arm_design.py), [paired endpoint](../artifacts/control-evidence-2026/paired_analysis.py), [application](taif-control-evidence-2026-application-draft.md).

## Material feasibility defect found

The earlier $3,000 / 30-hour reviewer budget was consumed by **120 experimental judgments × 12 minutes = 24 hours**, leaving **six hours** for calibration/disagreement. It **did not separately pay for 60 independent reference-label decisions**, despite the proposed primary outcome requiring reference-non-support labels established independently of the two treatment reviewers. Treating case-author labels or the existing `expected_verdict` field as verified ground truth would invalidate the proposed claim of independent evaluation.

The software tests check schema and calculations, not the provenance or correctness of the labels. Neither 55 passing CI tests nor HMAC pseudonymization solves this measurement problem.

## Proposed correction — same $25,000 request, no new grant scope

Use **three distinct human roles**: R1 and R2 make blinded experimental judgments (each sees a given case once, in different arms); R3 independently checks case-level reference claims against authenticated tool-side records and a frozen policy oracle **before** R1/R2 see outcomes. The case author is not R3. R3 must not see R1/R2 responses. If a genuinely independent R3 cannot be recruited, do not describe the labels as independently adjudicated.

| Work | Planning assumption | Hours |
|---|---:|---:|
| R1/R2 paired reviewer judgments | 60 cases × 2 arms × 12 min | 24 |
| R3 independent reference adjudication | 60 cases × 10 min | 10 |
| Calibration, conflicts, audit and rework reserve | explicit | 6 |
| **Total paid independent review** | **at $100/hour (unquoted)** | **40** |

**Revised illustrative budget (not a hiring commitment):**

| Expense | Prior | Proposed |
|---|---:|---:|
| Research lead, 120h × $100 | $12,000 | $12,000 |
| Independent engineering, 100h × $75 | $7,500 | $7,500 |
| Independent review/adjudication | $3,000 (30h) | **$4,000 (40h)** |
| Isolated compute/storage | $1,000 | $1,000 |
| Documentation/accessibility/release | $1,500 | **$500** |
| **Total** | **$25,000** | **$25,000** |

Documentation is reduced because much of the public protocol, tests, schemas and README already exists. $500 may still prove insufficient for a usable public release: if actual quotes or accessibility needs exceed it, reduce case count, seek a revised budget with explicit applicant approval, or do not claim a fully deliverable $25k scope. No outside labor is committed or priced by a provider.

**Fallback without changing the original $3,000 reviewer line:** at most 40 cases × 2 × 12min = 16h experimental review, 40 × 12min = 8h independent reference checks, and 6h reserve = 30h. This has a smaller primary denominator and lower precision; disclose it as an exploratory 40-case study, never a powered 60-case study.

## Protocol before any reviewer sees a case

1. **Source authenticity:** Instrument an authorized isolated sandbox. Preserve immutable source bytes, receipt digests, clock-domain/skew information, recorder ownership and completeness/missingness witnesses. A string such as `writer: independent` is NOT an attestation.
2. **Reference construction:** The case author freezes task/policy intent and an expected-verdict *candidate* separately from reviewer packets. R3, blind to the candidate label where practical, verifies the independently recorded events and assigns `supported`, `refuted` or `insufficient_evidence`, documenting evidence and confidence. A contradictory or incomplete witness can force `insufficient_evidence` even when the author expected `supported`.
3. **Disputes:** If R3 cannot verify record authorship, scope, temporal order or completeness, mark the reference `indeterminate` in a **private adjudication register** and exclude it from the confirmatory non-support denominator only under a prospectively frozen exclusion rule. Publish the count and reasons. Do not relabel after seeing R1/R2 responses. If an additional independent adjudicator is required, charge it against the 6h reserve or rescope.
4. **Allocation and masking:** Generate R1/R2 assignment using the existing HMAC allocator. Ensure reviewer packets contain no reference labels, case-construction hints or outcomes; store secret, source manifest, private key, reviewer identities and judgments outside public GitHub.
5. **Freeze:** Hash and timestamp the final dataset, reference decisions, inclusion/exclusion decisions, assignment seed commitment and primary analysis plan before judgments are unblinded. Record any later deviations, with dates and reasons.
6. **Analysis:** Primary endpoint is the paired difference in false support on **independently established non-support** cases, with raw beneficial/harmful discordances and exact two-sided McNemar p as exploratory sensitivity. Report support-reference cases separately, including false rejection and unjustified abstention. Reviewer effects, clustering, small n and selective missingness remain threats to inference.
7. **Stop rule:** If authentic source records, an independent R3, sufficient reviewer consent or adequate funding are unavailable, publish a transparent feasibility limitation instead of claiming independent validation.

## What this does and does not change

This is a **design-and-budget repair** that removes a specific underfunded dependency from the application. It is not an observed improvement in agent oversight, an independent human review, a grant award or a calibrated selection-probability uplift. It also does not establish that three real people, actual rates, rights, capacity or applicant identity are available. The $25k grant remains restricted project funding; prior illustrative founder-surplus EV **+$144.50** is left unchanged until applicant feasibility is verified.

**Applicant decision gate:** confirm three independent roles, 40h actual reviewer availability, rights to authenticated sandbox receipts, 12h/week lead capacity, and a credible $500 release plan. If not, adopt the smaller exploratory fallback or revise the budget before any applicant-approved submission. No outreach, payment, application or terms acceptance authorized.

**Source verification 2026-10-29:** [EA Funds official fund page](https://funds.effectivealtruism.org/funds/transformative-ai); existing [Svyable two-arm methodology](taif-control-evidence-2026-two-arm-design-preflight.md) and [paired-analysis preflight](taif-control-evidence-2026-paired-analysis-preflight.md).
