# Control Evidence — causal impact, falsification and release gates for EA Funds

**Prepared 2026-11-02 · INTERNAL applicant-review research annex · Transformative AI Fund · $25,000 proposed for ten weeks · PURSUE, NOT SUBMITTED.** No participant, contractor, payee, grant award, security certification or adoption claim is implied.

## The specific weakness this addresses

[EA Funds' Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) prioritizes early-stage projects that reduce *global catastrophic risk from transformative AI*; it is always open, and typical awards are **$10,000–$150,000**. The existing [application-review draft](taif-control-evidence-2026-application-draft.md) describes a technically coherent **claim-to-record adjudication** pilot, but does not yet establish why synthetic local-process receipts would change real frontier-agent oversight decisions. The missing step is **external operational usefulness**, not another synthetic test count. This annex makes the causal chain, potential falsifiers, and decision threshold explicit. It is not proof of that chain.

**Evidence already observed:** [run-bound receipt demonstration](../artifacts/control-evidence-2026/run_bound_receipt_demo.py), Git blob `1541995f0cd4064df2aefd8365781ddb92b70629`, uses a local supervisor's HMAC-protected observation and an *in-memory* replay register. [Independent reference gate](../artifacts/control-evidence-2026/independent_reference.py), blob `21c32ba94e4baa6d2bdcf6b4691acd867f687707`, validates declared R3 adjudications but cannot authenticate the adjudicator or source. [GitHub Actions run 41375155596](https://github.com/Svyable/Opps/actions/runs/41375155596) has a successful `smoke` job covering nine synthetic/unit suites; its previously decoded logs report **96/96 passing**. This run rechecked the job's successful conclusion, **not a fresh execution**. None of these facts establish a deployed agent, human-review effectiveness or catastrophic-risk reduction.

## Explicit causal theory, with evidence classification

| Link | Mechanism | Evidence today | What could disconfirm it |
|---|---|---|---|
| 1. Failure exists | Agents can make action/approval/alert claims not justified by observable tool-side records | General risk supported by cited outside monitoring incidents and local deliberately synthetic counterexamples; prevalence unknown | Realistic agents/records show almost no material claim-to-record discrepancies |
| 2. Independent observation is obtainable | A supervisor can collect run-bound, permissioned, tamper-evident records and record missingness | **Local-only demonstration**; key isolation, completeness, durable replay, clock domains and deployment not validated | Records remain agent-controlled, incomplete, privacy-prohibited or trivially replayable |
| 3. Humans use the evidence correctly | Reviewers with structured receipts falsely support fewer non-supported claims than narrative-only reviewers | **Prospective design only**, no independent labels or participants | No improvement, more false confidence, excess abstention or unacceptable review latency |
| 4. Tool transfers to real workflows | Public-interest or frontier safety operators can use the method without undue instrumentation cost | **No verified users, deployments, partner or procurement demand** | External reviewers cannot map the protocol to their telemetry or authority model |
| 5. Safer oversight follows | Better-supported human decisions may reduce an important class of agent-control failures | **Speculative downstream hypothesis**, not an observed safety outcome | Operators ignore the evidence or the relevant dangerous actions are not observable |

**Interpretation:** links 2–4 are empirical gates, not accomplishments. A successful small pilot would establish a narrow *measurement method*, not an AI safety certification. The catastrophic-risk contribution remains indirect and conditional on real-world adoption.

## Pre-award go/no-go decisions — require applicant verification

1. **Lawful and non-overlapping recipient.** Confirm jurisdiction, sanctions, identity, 12 lead hours/week, IP/release permissions, and that no BlueDot, Mercor or other funder pays the same 120 lead hours, 100 engineer hours, 40 reviewer hours, cases or invoices. This is a single study with *alternative* sponsors, not additive grant revenue.
2. **Genuine independent staffing.** Confirm an engineer who can instrument authorized sandbox tools and three distinct human roles: R1/R2 experimental reviewers and R3 reference adjudicator. Existing 40h/$4,000 reviewer and 100h/$7,500 engineer lines are **unquoted planning assumptions**; no collaborator has agreed.
3. **Trusted record acquisition.** Obtain permissioned sandbox instrumentation with recorder control separate from the tested agent, source bytes/digests, clock-domain and completeness evidence, and a durable replay strategy. Never label a self-declared `writer: independent` field an attestation.
4. **Preregistered evaluation.** Freeze case inclusion, R3 provenance and blinding before R1/R2 judgments. Target **up to 60 cases and 120 judgments**; 40 cases is an explicit lower-scope fallback, not a powered study. Report denominators, missingness, paired discordances, false-support and false-rejection rates, review time and uncertainty. Do not invent an effect size or claim statistical power.
5. **Adoption feasibility gate.** Before claiming practical safety impact, obtain independently verifiable feedback from at least one *actual* prospective oversight practitioner about telemetry compatibility and decision usefulness, with permission to quote. **No such person or endorsement is currently verified, and no outreach is authorized.** If none is available, describe the output only as an exploratory research artifact.
6. **Stop rule.** If authentic traces, independent R3, legal data rights, or credible staffing are unavailable, **rescope or withhold submission**. If the pilot shows no useful improvement, publish that negative result rather than claim safety efficacy.

## Deliverables the grant could actually buy

- Weeks 1–2: consent/rights and staffing gates, frozen protocol, source-authenticity threat model, preregistered scoring plan.
- Weeks 3–6: isolated supervisor-side instrumented traces; private R3 evidence register; preexisting code reused with attribution, not rebilled.
- Weeks 7–8: independently run, blinded paired reviewer evaluation *if human capacity is secured*; otherwise a documented feasibility shortfall.
- Weeks 9–10: permitted synthetic dataset, reproducible code, denominator-level results, limitations, privacy/redaction record and a one-page adoption-fit assessment.

**Existing proposed budget, unchanged and not committed:** lead 120h × $100 = $12,000; engineer 100h × $75 = $7,500; three-role review 40h × $100 = $4,000; isolated compute/storage $1,000; documentation/release $500; **total $25,000**. Actual quotes, available time, taxes, funder-allowed categories and deliverability are not verified. A grant is restricted research funding, not $25,000 in personal profit.

## IP, application terms and safety of disclosure

[CEA's site terms, updated October 1, 2026](https://funds.effectivealtruism.org/terms-and-conditions), treat uploaded user content as **non-confidential/non-proprietary** and require a perpetual, worldwide, nonexclusive noncommercial reuse license, with moral-rights waiver language. These are website terms, **not** a negotiated grant agreement. Never put private traces, participant identities, unpublished proprietary code or secrets into a public application. The [official application entry](https://funds.effectivealtruism.org/apply-for-funding) is live, but its current Paperform fields and grant-specific terms have not been authenticated by the applicant. No form was completed or terms accepted.

## Expected-value decision — no fabricated uplift

Prior **future application** illustration: ($12,000 lead allocation − 120h × $35/h displaced work) × 55% personal/project feasibility × 5% conditional selection − $70 applicant preparation = **+$144.50**. These are subjective sensitivities, not award rates. This annex is estimated at **1 hour × $35 = $35** incremental analysis cost; no measured selection-probability increase. **Including this new cost, illustrative remaining-pursuit EV = +$109.50**, before earlier sunk development, taxes and reviewer quote risk. The annex would need to increase *conditional* award probability by about **0.816 percentage points** (at 55% feasibility and $7,800 conditional founder surplus) to pay for itself on award odds alone. It has **not** demonstrated that uplift. At zero personal feasibility, further application labor has negative EV.

**Decision:** retain **PURSUE**, but the next economically useful move is *applicant-only* verification of recipient/availability/rights, actual independent collaborators, and evidence access; not more synthetic code or unapproved outreach. If those gates fail, mark this intake REJECT. No submission, contact, expenditure, contract or rights transfer was made.

**Primary sources checked November 2, 2026:** https://funds.effectivealtruism.org/funds/transformative-ai ; https://funds.effectivealtruism.org/apply-for-funding ; https://funds.effectivealtruism.org/terms-and-conditions ; https://github.com/Svyable/Opps/actions/runs/41375155596 .
