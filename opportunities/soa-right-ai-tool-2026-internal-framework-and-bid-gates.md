# SOA Research Institute — AI tool-selection RFP: internal feasibility and decision-matrix proof

**As of 2026-11-02 · WATCH · NOT AN APPLICATION · DO NOT SEND OR COPY INTO A PROPOSAL.** The [official RFP](https://www.soa.org/research/opportunities/2026/how-act-choose-between-models-plat) expressly requires a researcher-written proposal and disclosure of any AI use in preparing it. This internal analysis was AI-assisted. The applicant must independently do the research and author any proposal in their own words, disclose AI assistance as required, and approve any submission.

## The opportunity and the exact commercial constraint

- **Payer:** Society of Actuaries Research Institute (SOA), established professional research institution; it may elect not to award a contract.
- **Deadline:** proposal received by **2026-11-13**; no cutoff hour published. Expected status notice by end of February 2027.
- **Payoff:** **NO advertised contract price for this RFP.** SOA's historical cost guide says 33rd–66th percentile **$25,000–$50,000** for all contracted projects, **$15,000–$20,000** for literature reviews; neither is an offer or guaranteed payout. **$25,000** below is an *illustrative bid only*.
- **Required deliverables:** publishable report; practical model/platform/architecture selection matrix or checklist; illustrative actuarial use cases; presentation-ready summary. Market/literature scan and practitioner interviews encouraged.
- **Proposal requirements:** researcher CV(s), approach and limitations, deliverables, itemized cost/time, milestones, demonstrated competence; **maximum five pages excluding resumes**; human-authored, with all AI use disclosed.
- **Terms:** award only after executed Letter of Agreement; SOA plans to own copyright in resulting research; required publicity/webinar/meeting or article may be requested; conflicts must be disclosed; academic overhead generally not funded. **No license, payment schedule, liability cap or data-processing terms verified.**
- **No submission, email, contract, registration, paid expense or third-party inquiry authorized or performed.**

## Existing Svyable assets actually inspected

| Asset | Source / blob | Defensible use | Not established |
|---|---|---|---|
| Python strategy-selection service | [Svyable_Strategies/engine/svyable/strategy_selection_service.py](https://github.com/Svyable/Svyable_Strategies/blob/main/engine/svyable/strategy_selection_service.py), Git blob `ff90121399bdbfaa8837fb10c276e82683804c19` | Implemented registry, strategy details, selection-policy and reporting plumbing; relevant to comparative model-governance research | Actuarial validation, production insurance workflow, regulatory acceptance |
| Agent decision pre-activation guard | [Svyable_Strategies/engine/svyable/agent_decision_guard.py](https://github.com/Svyable/Svyable_Strategies/blob/main/engine/svyable/agent_decision_guard.py), blob `612d46b92c8432d148e773ab42080f25016547f7` | Implemented PASS/BLOCK logic and context/decision integrity checks; example of a human-authority gate | Correctness of any actuarial model, SOC certification, field adoption |
| Desk research/publishing workspace | [Svyable/desk README](https://github.com/Svyable/desk/blob/main/README.md), blob `44de02796d0c00d491b99e27112a9363930aa332` | Public research/writing production infrastructure and extensive book-project catalog | Peer-reviewed actuarial research, professional credentials, commissioned reports |

**Major qualification gap:** no independently verified actuarial designation, insurance-domain project, practitioner interview commitments, paid client delivery history, personal authorship attribution or specialist co-researcher. A repository is not a résumé. The SOA RFP does not explicitly require an actuarial designation, but reviewers demand demonstrated capacity to perform the specific research.

## Prototype decision matrix — internal research instrument, not validated advice

This is a *falsifiable structure* to be tested with qualified actuaries, not a recommendation to deploy any specific model. Never treat the qualitative examples below as observed insurance outcomes.

### Hard gates before ranking alternatives

1. **Use-case classification:** is the output explanatory/advisory, or does it materially affect a price, reserve, eligibility, regulatory filing or customer?
2. **Data permissions:** is training/inference use lawful and permitted for personal/health/financial data? If not, stop; no score can override a prohibition.
3. **Auditability:** can the organization reconstruct inputs, model version, overrides, approvals, validation and outputs? If not, stop for consequential uses.
4. **Independent validation:** is there a fit-for-purpose holdout, drift plan, subgroup assessment and accountable sign-off? If not, do not deploy for consequential uses.
5. **Human override:** is there an accountable person able to block or reverse the result, with a logged reason? If not, stop for high-impact workflows.
6. **Vendor/contract constraints:** data residency, retraining, retention, exit/export, change notice and regulator access must be reviewed before selection.

### Comparative questions (no invented numerical scores)

| Candidate approach | Potential advantage | Distinctive failure or trade-off to test | Evidence needed |
|---|---|---|---|
| Rules / deterministic calculations | Reproducibility and transparent rules | Brittle coverage and maintenance of exceptions | Rule inventory, change control, exception analysis |
| GLM / classical statistical model | Interpretable coefficients and mature validation patterns | Specification error, nonlinear relationships, proxy effects | Calibration, stability, residuals, subgroup checks |
| GBM / other ML | Nonlinear predictive flexibility | Explanation fidelity, drift and model risk | Out-of-time validation, sensitivity, surrogate-vs-model gap |
| Generative AI copilot | Natural-language assistance with research/documentation | Unsupported statements, confidentiality and prompt injection | Source-grounding audit, abstention, access and trace tests |
| Hybrid human-reviewed pipeline | Separate calculations, retrieval, narrative and approvals | Integration failure, ambiguous ownership and audit gaps | End-to-end lineage, role separation, error injection, rollback |

### Three illustrative cases for practitioner review

| Case | Gate that decides the architecture | Hypothesis to test (NOT a result) |
|---|---|---|
| Drafting internal model documentation | Source-grounding and confidentiality | A retrieval-assisted copilot with mandatory citations may save writing time without allowing unsupported statements to pass review |
| Reserving or pricing assumption update | Reproducibility, independent validation, change approval | A validated statistical baseline plus explicit human approval may be easier to defend than unconstrained agentic generation |
| Underwriting triage | Privacy, fairness, adverse-action explanation, appeals | A black-box score may be unsuitable without reliable explanation, subgroup monitoring and appeal procedures |

**Test protocol if commissioned:** independent actuarial reviewers each score the same three cases against the gates, record disagreements, then apply the matrix to a fourth withheld case. Report inter-reviewer disagreement and rejected options; no claims of improved decision quality without a comparator. Obtain actual interview consent and data rights before collection.

## Budget and expected-value preflight — illustrative, not a quoted fee

For a hypothetical **$25,000 fixed-fee contract**, allow **160 founder research/writing hours × $35 = $5,600** opportunity cost, **40 actuarial specialist hours × $100 = $4,000** unquoted external labor, and **$1,000** interviews, publication and contingency. Conditional economic surplus = **$14,400** before taxes, legal review, insurance and unpriced promotional obligations. Future applicant-only proposal labor = **3h × $35 = $105**.

| Scenario | Qualification feasibility | Conditional award probability | Illustrative remaining pursuit EV = $14,400 × both − $105 |
|---|---:|---:|---:|
| No actuarial domain partner / current cautious | 10% | 3% | **−$61.80** |
| Domain partner and references verified (not current fact) | 35% | 5% | **+$147.00** |
| Strong specialist team and prior paid studies verified (not current fact) | 50% | 8% | **+$471.00** |

These are subjective sensitivity inputs, not empirical win rates. This internal preflight cost ~1.5h × $35 = **$52.50** if valued as labor. **No measured award-probability uplift**. The current cautious end-to-end case including preflight is **−$114.30**. A speculative application is not justified on present evidence.

## Release gate / next decision

**WATCH, not PURSUE:** before Nov 6, independently verify (a) at least one named actuarial subject-matter expert willing and qualified to deliver, (b) founder research authorship/experience and truthful CV, (c) a feasible 160h delivery slot, (d) an actual costed partner quote and lawful payee, (e) rights separation for pre-existing Svyable code and SOA-owned commissioned report, (f) acceptability of publicity and conflict disclosures. **If missing, move to REJECT before Nov 13**. If cleared, the human applicant may choose to write a proposal personally and disclose AI involvement. No automated submission.

Sources: [official RFP](https://www.soa.org/research/opportunities/2026/how-act-choose-between-models-plat); [SOA active RFP directory](https://www.soa.org/research/opportunities/research-proposal-list/). Source and code reviewed 2026-11-02. No new code tests or actuarial interviews were run.
