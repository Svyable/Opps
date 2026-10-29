# Mercor AI Safety Fund — Control Evidence EOI (alternative funding route)

**Prepared 2026-10-29 UTC · DRAFT ONLY · NOT SUBMITTED · WATCH pending eligibility and award-terms review.** This is the same Control Evidence study as the EA Funds draft; the [independent-reference budget repair](taif-control-evidence-2026-independent-reference-budget-repair.md) applies to either funder, not two separately funded projects.

**Official sponsor listing:** https://jobs.ashbyhq.com/mercor/1d59ce50-4207-4d95-b7fd-5a01e90b0897  
**Fund size:** Mercor announces **$5 million total**, **not** a $5 million individual grant. Individual grant size is discretionary. **Proposed request: $25,000**, not an offered award.  
**Deadline:** Official safety listing provides no fixed deadline in the publicly indexed text. A third-party funder bulletin describes rolling applications; verify the live portal before any action.  
**Relationship to existing applications:** This is a **potential alternative funding source for the same Control Evidence study**, not an additional $25,000 project to be funded concurrently with EA Funds. Do not send substantially overlapping applications without checking disclosure and agreement terms; never charge the same hours, cases, or deliverables twice.

## Draft expression of interest (1–2 page content; applicant must approve)

### Project: Control Evidence — When Should We Believe an AI Agent's Action Report?

**Research lead / institution:** [APPLICANT MUST PROVIDE ACTUAL NAME, CREDENTIALS, INSTITUTION AND LEGAL PAYEE]. Public code under Svyable is evidence of preparatory software, **not proof of an eligible U.S./U.K. research institution, applicant credentials, or staff commitments**.

### Research question and significance

AI agents can claim that a tool action completed, an approval preceded execution, or an alert was delivered. A persuasive narrative or agent-authored trace does not prove any of those claims. We propose a controlled study asking: **when does execution-side evidence improve an independent reviewer's ability to reject unsupported agent claims, and when do missing or conflicting receipts produce unwarranted confidence?**

This fits Mercor's stated interest in oversight and control, red-teaming methodology, and failures that evade apparent monitoring. The project does not propose another general-purpose dashboard or claim that receipt logging alone prevents dangerous actions. The unit of analysis is a specific agent-action claim, its independently captured records, and a blinded judgment of support, contradiction, or insufficiency.

### Method and falsifiable deliverables

**Weeks 1–2:** Freeze a preregistered taxonomy of three claims (completion, authorization timing, delivery), receipt provenance and missingness rules, attack/perturbation cases, holdout separation, scoring denominators, and adverse-result reporting. Audit existing literature and record overlap.

**Weeks 3–5:** Instrument an isolated mock-tool sandbox; collect independently authored tool-side receipts, with deliberately delayed, missing, conflicting and spoof-like records. No live secrets, unsolicited communications, real third-party account access, or uncontrolled offensive testing. Record source ownership and licensing.

**Weeks 6–8:** Target 60 cases and 120 blinded judgments. Use a case-paired, reviewer-balanced two-arm assignment: one reviewer sees narrative only, a different reviewer sees the same case plus structured receipts; each reviewer sees a given case once. A **third, independent adjudicator** must verify reference labels against authenticated tool-side evidence before experimental outcomes are revealed. Verify three distinct review roles, consent, conflicts and pay rates *before* promising the study. Keep reference labels inaccessible to experimental reviewers.

**Weeks 9–10:** Publish the allowed synthetic dataset, schema, code, exact denominators, uncertainty, failure examples, adjudication disagreements and replication instructions under a commercially reusable license if rights allow. If authentication or reviewers are unavailable, report a smaller feasibility study, not a fabricated effectiveness result.

**Primary outcomes:** paired false-support contrast on claims with independently established contradictory/insufficient evidence; beneficial and harmful reviewer discordances; justified abstention and unwarranted rejection. Secondary outcomes: review time and agreement. An exact McNemar analysis is available as a sensitivity check; 60 cases is an exploratory planning target, **not a powered claim of risk reduction**.

### Relevant existing assets (preparatory, not efficacy evidence)

- [Control Evidence application and research design](https://github.com/Svyable/Opps/blob/main/opportunities/taif-control-evidence-2026-application-draft.md)
- [Two-arm allocation](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/two_arm_design.py) and [case-paired endpoint analysis](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/paired_analysis.py)
- [Remote CI evidence: 55 passing synthetic/unit tests](https://github.com/Svyable/Opps/actions/runs/40797112938), **not** real-agent or human-study validation
- [Human Kind](https://github.com/Svyable/human-kind) authorization concepts; [ScrolIQ](https://github.com/Svyable/scrollq) provenance patterns.

No participant recruitment, independent labels, authenticated deployed-agent receipts or real-agent effect estimate has been completed.

### Outputs and requested resources

| Proposed expense (unquoted) | Calculation | Amount |
|---|---:|---:|
| Research lead / analysis / release | 120 h × $100 | $12,000 |
| Independent sandbox instrumentation | 100 h × $75 | $7,500 |
| Independent experimental review + reference adjudication | 40 h × $100 | $4,000 |
| Isolated compute / storage | estimate | $1,000 |
| Documentation / accessible public release (reuse existing artifacts) | estimate | $500 |
| **Total request** | | **$25,000** |

The 40h reviewer line covers 24h two-arm judgments, 10h independent reference checks and 6h reserve; the $500 release line needs feasibility confirmation. All people, rates and capacity are **hypothetical**. Request access to Mercor's expert network for *potential* independent grading only if consent, conflicts, privacy and funding terms are acceptable. Do not imply Mercor has agreed to provide experts or infrastructure.

**Potential impact:** a small reproducible evidence standard for deciding when an agent's claim about a consequential action is justified, contradicted or unprovable. Negative findings are valuable. Transfer to frontier deployment is not assumed.

## Mandatory commercial and eligibility gate — STOP before sending

1. **Recipient eligibility:** Mercor says grants go to the researcher's **institution**, limited to eligible U.S./U.K.-based universities, nonprofit research organizations, public-benefit corporations and small startups that **do not sell AI training data**. Svyable's legal form, headcount, business model, location and payment ability are **not verified**. Do not present an individual without an eligible recipient as qualified.
2. **Competition restrictions:** Sponsor's indexed award terms prohibit work with **specified Mercor competitors** on substantially similar benchmarks/evaluations during the award and **12 months after**. The list, breadth and impact on Svyable's future licensing, consulting and grant work are **unknown**. This may be a decisive no-go, even if selected. Obtain full agreement and evaluate opportunity cost before acceptance.
3. **IP and benchmark rights:** Grantee retains ownership but grants Mercor a nonexclusive **commercial-use license**; Mercor receives **early benchmark access** and the **exclusive right to build and host a private held-out test set** for benchmark/evaluation projects. Ensure existing Svyable, contributor and third-party rights allow this. Open-license release permits commercial use; do not promise restricted datasets.
4. **Privacy/publicity:** Mercor may name recipient and institution; publication subject to confidentiality review. Verify reference, data, security, brand and outside-work restrictions.
5. **Alternative grant:** EA Funds Control Evidence $25k and Foresight authorization-boundary $35k are *drafted, not submitted as last verified*. Reconcile work packages and funding disclosures; do not seek two awards for the same study or assign the same benchmark rights inconsistently.
6. **Applicant approval:** Confirm actual lead, capacity, staff, rights, live EOI fields, terms and explicit permission. No application, outreach, spending or agreement is authorized.

## Conservative commercial screen

The $5m program pool is **not a plausible individual payoff**. Use the **$12k budgeted lead compensation** as the conditional economic benefit, offset by 120 h × $35/h = $4,200 alternative labor cost. A 2-hour EOI review costs ~$70. Under purely subjective 40% delivery feasibility × 2% selection, marginal economic surplus EV = ($12,000 − $4,200) × 0.40 × 0.02 − $70 = **−$7.60**. Under favorable 60% feasibility × 5% selection, EV = **+$164**. Both **exclude** the potentially large 12-month competitor-restriction cost, which could make either negative. No sponsor-published acceptance probability or individual award amount exists. If the institution or exclusivity gate fails, do not apply.

**Decision: WATCH**, not PURSUE, until institutional eligibility and competitor/IP costs are established. This EOI is reusable as an alternate funder package, not permission to apply.

**Sources verified October 29 UTC:** [Mercor official AI Safety Fund listing](https://jobs.ashbyhq.com/mercor/1d59ce50-4207-4d95-b7fd-5a01e90b0897); [Manifund AI Safety Funder Bulletin (Oct 15)](https://manifund.org/ais-funder-bulletin); [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai).
