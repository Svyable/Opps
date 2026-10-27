# Foresight AI Nodes 2026 — 37-field application crosswalk and submission gate

**Prepared 2026-10-26. Status: applicant-review packet only. NOT SUBMITTED; no form consents accepted.**  
**Program:** https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/  
**Official form:** https://airtable.com/appyVXc5SMPAvIKpP/pagp7takV26cG6JY1/form  
**Deadline:** **2026-10-31 23:59 PDT** (2026-11-01 06:59 UTC).  
**Secondary 37-field transcription:** https://viamu.app/opportunities/ai-science-safety-nodes  
**Source limitation:** The official Airtable form was not readable through the research browser on 2026-10-26. The question inventory below is paraphrased from a third-party transcription, **not independently verified against the live Airtable fields**. The sponsor's RFP, eligibility, funding and deadline were checked on its own website. The applicant must inspect the actual form, including conditional fields, before using this packet.

## Commercial go/no-go

**Opportunity:** Foresight Institute, Human Empowerment (Coordination and Accountability), **$35,000 requested** for 12 weeks. Foresight says grants typically range $30k–$100k, with Human Empowerment generally receiving smaller awards. Credible payer: Foresight Institute (nonprofit), subject to grant due diligence. Existing code and design: [three-arm prospective study and mock boundary](../artifacts/foresight-control-2026/README.md); 28/28 automated tests [passed remote CI](https://github.com/Svyable/Opps/actions/runs/40363475074). **No AI-agent intervention trial, human reviewer result, or safety-effect estimate exists.**

**Qualification:** Individuals, teams, nonprofit and for-profit applicants are permitted; for-profit funding need must be explained. Real eligibility remains **unverified** because applicant/payee identity, weekly capacity, reference, release rights and Node participation are unknown. Strong preference for actual in-person contribution to Bay Area/Berlin Nodes, not an absolute ban on remote-only applicants.

**NEW 2026-10-27 dual-grant disclosure gate:** [Foresight/EA Funds cost-separation and funder-disclosure annex](foresight-2026-dual-grant-overlap-controls.md). If both grants are pursued, use disjoint research cases, personnel hours, invoices and outputs; verify 24h/week (delegated Foresight B plus EA) or 32h/week (founder-led A plus EA) during fully concurrent execution, plus administration. These are unverified workloads, not commitments. Before submitting either form, truthfully disclose the other proposal's actual status; no dual award or funder approval exists.

**Economics:** Previously modeled subjective economic-surplus EV (not gross grant EV): founder-led 20h/week, 45% feasible × 3.5% selection, $12k conditional founder surplus, minus $140 prep = **+$49**; at 25% feasible **−$35**. Delegated 12h/week, 65% feasible × 3.5% selection, $7.2k conditional surplus, minus $140 prep = **+$23.80**; at 45% feasible **−$26.60**. These are sensitivity assumptions, not sponsor selection rates. No verified capacity means **no defensible positive-EV claim**. Budget A and B are mutually exclusive: [cost and capacity model](foresight-2026-itemized-budget-capacity.md). No hiring or spending.

**NEW 2026-10-27 statistical feasibility gate:** The 60 synthetic scenarios include only **20 policy-unauthorized matched cases per arm** for the primary outcome. The [exact paired-power preflight](foresight-2026-paired-power-preflight.md) shows just **17.36% illustrative power** for a 20-point net effect under one assumed discordance distribution and alpha 0.025; 80 independent unauthorized pairs would yield ~77.95% under those same assumptions. Treat the $35k/12-week study as **exploratory**, report effect sizes and uncertainty, and do not claim a powered efficacy finding. [Reproducible standard-library calculator](../artifacts/foresight-control-2026/exact_power.py) with eight local tests; no new agent outcomes.

**Decision:** PURSUE only the applicant-controlled eligibility/submission gate before the deadline. **Do not submit** until the required confirmations and explicit authorization exist. The $35k is restricted project funding, not $35k profit.

## Copy-ready project responses (subject to applicant judgment and live form)

**Title:** Control Where It Counts

**Plain-language project summary — 329 characters, under secondary-source 350-character cap:**

> Control Where It Counts tests whether human approval actually prevents unauthorized AI-agent actions or merely records oversight. We will compare no gate, cosmetic approval, and enforced authorization in a sandbox, publish failures and throughput costs, and release a decision rule for when humans should retain or defer control.

**RFP fit — 405 characters, under secondary-source 500-character cap:**

> Foresight asks when human oversight adds value versus becomes theatre. Our 12-week, $35,000 study will test three approval designs on 60 preregistered synthetic tasks, with independent review and explicit abstention. AI agents perform sandbox work; deterministic boundaries enforce policy. Human review remains mandatory for legitimacy-sensitive or irreversible actions even if slower. No trials have run.

**Limitations, novelty, success.** Many approval interfaces record that a person clicked a button but do not prove that the downstream tool action was gated by that authorization. We propose a matched three-arm comparison: no approval, cosmetic approval, and a scoped, enforced boundary. We will preregister policy labels and scoring, use isolated mock tools, and collect tool-side receipts rather than trust agent self-reports. Success is a reproducible comparison of unauthorized completion, legitimate task completion, false blocks, approval delay and review burden, with explicit uncertainty and failures. A negative result is publishable. This is not a claim to have invented approval gates or proven they reduce risk. The existing mock gate passes deterministic tests but has not been exercised by a real agent.

**Risks and differential safety.** The principal research risk is that a bypass demonstration could be mistaken for a safe deployment recipe, or that synthetic tasks create false confidence. Begin with no real credentials, no external messages, no irreversible effects and no operational targets. Publish abstract failure classes and safe reproduction fixtures, not exploitable live-target details. Freeze the held-out set before trials, separate agent-generated development cases from evaluation, and retain missing telemetry and reviewer disagreement in denominators. Do not generalize to frontier deployments without independent replication. Funded outputs will be open source only if the applicant verifies the relevant rights.

**Schedule and milestones.** Proposed start: within four weeks after a signed award and confirmed personnel availability; end: 12 weeks after actual start (do not invent calendar dates). Weeks 1–2: threat model, data rights, policy labels, preregistration. Weeks 3–5: real sandbox runner, three-arm tool adapters and enforcement tests. Weeks 6–8: randomized agent trials with receipts and negative controls. Weeks 9–10: blinded independent adjudication and effect/latency estimates. Weeks 11–12: public code, permissible synthetic data, limitations, decision rubric and replication instructions. If personnel cannot be secured, rescope before accepting funding rather than promise impossible milestones.

**Three-year path, conditional rather than promised.** Year 1: publish and invite independent replication of the sandbox benchmark, with failures and costs visible. Year 2: if evidence warrants, adapt the authorization interface to one real but reversible open-source agent workflow and test cross-tool bypasses with independent reviewers. Year 3: if external results generalize, publish interoperable boundary checks and a decision framework separating performance benefit, intrinsic legitimacy and irreversible delegation. Abandon or narrow the approach if legitimate work is blocked disproportionately or bypasses defeat the boundary.

**Track record — repository-grounded, not credential claims.** Svyable maintains [Human Kind](https://github.com/Svyable/human-kind), an evidence-oriented commons with explicit boundaries on agent authority, and [ScrolIQ](https://github.com/Svyable/scrollq), reproducible scientific diagnostics emphasizing provenance and falsification. The Foresight preparatory work contains 60 synthetic task specifications, 180 **unrun** planned assignments and a side-effect-free mock authorization evaluator; 28 unit tests passed GitHub Actions on October 26, 2026. These demonstrate software preparation, **not** scientific efficacy, institutional affiliation, prior grant performance, or independent research credentials. Applicant must add truthful personal experience and actual role history.

**For-profit funding rationale, ONLY if applicable and verified.** The public-good deliverable is an independent comparative test, including negative findings and open research artifacts. Existing public code does not establish whether human checkpoints reduce unauthorized actions. A customer-specific proprietary implementation would not finance a publishable blinded evaluation. This rationale requires confirmation that no existing customer, employer or grant already funds the same work.

**Additional evidence links:** https://github.com/Svyable/Opps/blob/main/opportunities/foresight-2026-application-narrative.md ; https://github.com/Svyable/Opps/blob/main/opportunities/foresight-2026-itemized-budget-capacity.md ; https://github.com/Svyable/Opps/blob/main/artifacts/foresight-control-2026/README.md ; https://github.com/Svyable/Opps/actions/runs/40363475074 .

## Field-by-field mapping (37 fields reported by third party)

The numbers are a preparation aid, **not** claims that the official form uses this ordering. Conditional Node/compute questions may appear only after relevant choices.

| # | Paraphrased field | Draft response or hard gate |
|---:|---|---|
| 1 | Applicant full name | **Applicant must enter and verify legal/usable application name.** Public author name is not legal identity evidence. |
| 2 | Applicant email | **Applicant only; do not infer from commits.** |
| 3 | Website, CV or profile | Candidate public project URL: https://github.com/Svyable ; applicant confirms acceptable profile and any CV. |
| 4 | Affiliated projects | Candidate: Svyable / Human Kind / ScrolIQ; do not assert legal affiliation beyond what applicant verifies. |
| 5 | Individual versus organization | **Applicant decision**, dependent on legal payee. |
| 6 | Track record | Use grounded paragraph above; applicant supplies own credentials and contribution attribution. |
| 7 | Participants and roles | Lead and outside engineer/reviewer are **proposed roles only**; no named personnel or consents secured. |
| 8 | Primary region | **Applicant verifies**; do not guess residence. |
| 9 | Primary country | **Applicant verifies.** |
| 10 | Primary professional reference name/email | **BLOCKER:** consenting reference and permission to disclose contact details required. |
| 11 | Organization category | **Applicant verifies** legal status; do not invent corporation/nonprofit. |
| 12 | Requested support types | Candidate: grant funding only; do not request physical space or compute without real plan. |
| 13 | RFP area | Candidate: **3. Human Empowerment**. |
| 14 | Project title | Control Where It Counts. |
| 15 | Short plain-language summary | Copy 329-character draft above; confirm live 350-character limit. |
| 16 | RFP alignment | Copy 405-character draft above; confirm live 500-character limit. |
| 17 | Existing limitation, novelty and success | Copy project response above. |
| 18 | Risks and safety-first sequencing | Copy risks response above. |
| 19 | Start/end dates and milestones | Copy 12-week schedule; applicant chooses feasible calendar dates after award. |
| 20 | Three-year scaling plan | Copy conditional three-year path. |
| 21 | Open-source commitment | [Public-code license evidence audit](foresight-2026-public-license-rights-audit.md) confirms published Apache-2.0 (Opps), MIT (ScrolIQ) and Apache-2.0/CC-BY-4.0 (Human Kind) terms; **applicant must still verify chain of title, contractor/data rights, privacy and the live commitment; do not pre-accept.** Sponsor requires open-source funded work. |
| 22 | Other links | Use evidence links above, no unverifiable performance claims. |
| 23 | Preferred Node | **Conditional; applicant decides** Bay Area/Berlin/both only with actual ability to attend. |
| 24 | Space dates/duration | **Conditional; no dates claimed.** |
| 25 | Node users | **Conditional; no named attendee or headcount asserted.** |
| 26 | Space type | **Conditional; applicant choice only.** |
| 27 | Node community plan | **Conditional; genuine sprint/contribution plan required, not an invented residency.** |
| 28 | Workshop availability | **Conditional; applicant confirms availability before selecting yes/no.** |
| 29 | Request funding | Candidate yes, subject to applicant approval. |
| 30 | Overhead | Proposed $2,000 directly supportive overhead on $33,000 direct costs = 6.06%; sponsor ceiling 10%. **Choose budget A or B**, not both. |
| 31 | Request compute | Candidate no, unless a justified eligible compute need is documented. |
| 32 | Optional Lightcone Commons sharing | **Privacy/rights decision reserved to applicant.** No default opt-in; sharing may extend beyond sponsor control. |
| 33 | Sharing with grant advisors | **Applicant consent required**; check exact scope and consequences. |
| 34 | Confidential material | Proposed N/A if accurate; do not place private data here on assumption of absolute secrecy (secondary transcription says AI processing may occur). |
| 35 | Discovery channel | Applicant confirms actual source; do not invent. |
| 36 | Optional seminar-group interest | Applicant choice; leave unselected absent genuine interest. |
| 37 | Submission authority/accuracy/AI processing/other-person data consent | **STOP: applicant-only acceptance.** No automation acceptance or submission. |

## Blocking items ranked by ability to prevent an honest application

1. **Legal applicant and payee** (individual vs actual organization, jurisdiction and tax status). This determines form choices and due diligence.
2. **Capacity and deliverability** (realistic 12 or 20 founder hours/week; qualified independent engineering and reviewer availability; budget A or B). Neither budget is an actual contractor quotation.
3. **Reference with consent** (name/email must not be fabricated or published without permission).
4. **Open-source and data rights** (pre-existing code, future outputs, third-party assets, employer restrictions).
5. **Realistic Node contribution** (sponsor strongly prioritizes in-person; a remote-only proposal must acknowledge selection disadvantage).
6. **Privacy/Lightcone and advisor-sharing choices**, plus applicant confirmation of all live form text.
7. **Explicit approval to submit**; no binding terms, applications or external inquiries executed.

## Separation from other grants

This Foresight application funds **prospective comparison of authorization mechanisms**. The EA Funds $25k Control Evidence application funds **retrospective independent verification of agent claims against execution records**. Reuse of pre-existing open code is permissible only within its licenses; do not bill the same hours, datasets, evaluations or deliverables to both. Keep distinct work packages and funding reports if either is awarded.

## Sources

- Primary: https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/ (deadline, focus, eligible applicants, open-source terms, Node preference, overhead, due diligence).
- Secondary: https://viamu.app/opportunities/ai-science-safety-nodes (37-field inventory and conditional sharing/consent descriptions; **not independently confirmed live form**).
- Source repositories and CI links above. No other applicant facts inferred.
