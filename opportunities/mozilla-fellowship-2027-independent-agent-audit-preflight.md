# Mozilla Foundation 2027–28 Independent Fellowship — evidence-first preflight

**Prepared:** 2026-10-29 UTC. **Opportunity:** Mozilla Foundation Fellowships, Track II / Independent Fellows. **Status:** WATCH, not submitted or authorized. **Purpose:** reviewer-ready *evidence and eligibility crosswalk*, not AI-written form responses.

## Primary-source facts

- [Official call](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/) and [16-page official RFP](https://assets.mofoprod.net/network/documents/PUBLIC_2027_2028_Fellowship_RFP-2.pdf).
- **LOI closes December 17, 2026, 11:59 p.m. Pacific Standard Time (UTC−8).** Full application by invitation only, due March 12, 2027. Fellowship June 1, 2027–May 2028.
- Ten total fellowships; RFP identifies **five Independent Fellowships**, one reserved for Creative Advocacy. This leaves approximately four general Independent slots, but it does not reveal application volume or selection rates.
- **Track II:** $100,000 stipend plus $25,000 project budget, **$125,000 total**, not $125,000 of personal income and not Svyable corporate revenue. Track I offers $75,000 stipend plus $25,000 project budget and requires a host-organization relationship.
- Independent Fellows are expected to have senior-level leadership and a proven record of shipping. Individuals only, not a Svyable company application. The year is remote with cohort commitments (~5–10 hours/month), funded travel, and substantive project delivery.
- Fellows retain copyright/patent ownership in materials created during the fellowship, but must open-license code and nonconfidential content in consultation with Mozilla, and regularly work in the open. These are sponsor terms, not a negotiated agreement.
- [Eligibility guidelines](https://www.mozillafoundation.org/documents/501/Mozilla_Foundation_Grant_Eligibility_Guidelines_tNhKrgM.pdf): individual must be legally able to receive US charity funding; project must produce charitable public benefit, not primarily private profit; sanctions/conflict exclusions apply.
- **Critical AI-use policy:** the sponsor allows AI for brainstorming/clarity/translation but *not* to generate full application answers or replace the applicant's original work and voice. This file is research, evidence indexing and question preparation only. Sven must personally author and approve the LOI and disclose tool use truthfully.

## Why this is an unusually exact Svyable fit

The RFP's **“Shared security and audit infrastructure for small organizations”** focus explicitly gives as an example **a test kit a nonprofit can run in an afternoon on an agent connected to its inbox** (official RFP, page 4). Svyable already has a *research prototype* for verifying agent-action claims from independent receipts and separating cosmetic approval from enforced authorization. This is a narrower, more sponsor-specific fit than a generic AI safety grant.

**Working project direction for applicant consideration, not an approved new product:** an open, locally runnable *agent-action evidence kit* that lets small organizations check whether an AI tool actually obtained authorization, completed an action and delivered an alert. The core is an inspectable evidence contract, fail-closed reporting and bounded test scenarios, **not** a security certification, real-world exploit tool or commercial consulting wrapper.

### Existing assets and what they actually prove

| Existing public asset | Reuse | Evidence boundary |
|---|---|---|
| [Control Evidence study design](https://github.com/Svyable/Opps/blob/main/opportunities/taif-control-evidence-2026-application-draft.md) | Narrative vs receipt-supported claims, blind reviewer allocation, paired analysis, 60-case target | **55 synthetic/unit tests passed** in [GitHub Actions](https://github.com/Svyable/Opps/actions/runs/40797112938); no real human reviewer experiment, authenticated production telemetry, user adoption or independent validation |
| [Foresight authorization prototype](https://github.com/Svyable/Opps/blob/main/artifacts/foresight-control-2026/README.md) | Mock authorization gate, receipt generator, test cases | **44 CI tests** and 108 mock receipts, not a validated security product or real agent safety effect |
| [Human Kind](https://github.com/Svyable/human-kind) | Open evidence dossiers, accountable human decision rights, source provenance | Public GitHub contribution protocol, not evidence of participating small organizations or deployed agent auditing |
| [ScrolIQ](https://github.com/Svyable/scrollq) | Provenance contracts, fail-closed evaluation, reproducibility | Different scientific-imaging domain; conceptual/code reuse only, not evidence of nonprofit security adoption |
| [Agent for Hire](https://github.com/Svyable/agent-for-hire) | Existing bounded service intake, pricing, acceptance criteria and human review | Commercial service pilot; no verified customers or nonprofit use, and **do not** route Mozilla funds into a private profit-generating service |

No user counts, external deployments, partner letters, customers, security efficacy or community endorsement are verified in the inspected public repositories. Do not turn stars, commits or CI passes into traction claims.

## Reviewer question crosswalk (RFP pp. 11–15)

The official LOI requests applicant details, public builder links, track and issue area, project title (10 words), summary (200 words), one-liner (30 words), target users (50), traction (50), impact (150), disruption (50), quarterly milestones (150), charitable public benefit (150), professional experience (150), technical expertise (100), field role (150), post-fellowship sustainability (150), motivation, other funding, AI disclosure and sharing/consent.

| Reviewer criterion | Verifiable material to show | Missing proof before LOI |
|---|---|---|
| Early, distinctive, not redundant | Compare independently verifiable tool-side receipts with vendor-authored claims; reference prior agent-audit and trace-observability work in TAIF draft | Named comparator implementations, measurable delta, why an ordinary small org can operate it |
| Specific user and public need | RFP itself names nonprofits and small organizations relying on connected agents | Real nonprofit/coop user conversations, permissioned problem statements, accessibility and deployment constraints |
| Can build within 12 months | Existing code, test harness, schemas and GitHub CI links above | A verified lead capacity plan, security reviewer, user-testing partners, threat model, narrow scope and deliverability |
| Power and community governance | Human Kind's explicit human-decision boundaries | Who can veto tests, how pilot organizations control their own data, non-extractive feedback and opt-out process |
| Fellow's leadership and cohort value | Public Svyable/agents portfolio and reproducible commits | Applicant's genuine personal role, employment history, collaborators, actual reach and cohort commitment |
| Durable field influence | Open-source evidence schema and reproducibility practices | Adoption/distribution path, maintenance stewardship, realistic sustainability, no unsupported media/policy claims |

## Narrow 12-month delivery hypothesis — subject to applicant and community confirmation

1. **Q1:** Define a nonprofit-safe threat model and data-handling boundary with actual pilot stakeholders; freeze three agent-action claim types (authorization before action, tool completion, alert delivery). Reuse the existing synthetic receipt and audit modules; publish a documented gap list.
2. **Q2:** Deliver a runnable local test harness with deterministic fake inbox/tools, no real credentials, a human-readable evidence report and safe failure cases. Measure setup time and false-confidence failure modes in controlled tests.
3. **Q3:** Only with consent and appropriate safeguards, run small-org pilots using synthetic or explicitly authorized traces. Measure independent reproducibility, time to verdict, justified abstention and user comprehension; publish failures and denominator counts.
4. **Q4:** Release open code, schema, reproducible fixtures, accessible documentation, evaluation results, governance guidance and a stewardship plan. No security certification claim unless independently supported.

This is **a feasibility direction**, not a commitment or proof of user demand. If no partners or privacy-safe pilots exist, the project must shrink to an openly documented feasibility kit rather than invent deployments.

## Eligibility, rights and application gates

- [ ] Applicant personally verifies legal ability to receive USD from a US 501(c)(3), grant terms, and no sanctions or Mozilla conflict.
- [ ] Applicant verifies Track II senior-level record and that the public work cited was genuinely led by them; do not equate agent-generated commits with personal technical experience.
- [ ] Applicant confirms ability to deliver a substantial 12-month project beginning June 2027, including cohort participation/travel; no implied full-time guarantee from the RFP.
- [ ] Identify real small-organization stakeholders and secure permission **before** using their names, quotes or private data; no contact authorized in this run.
- [ ] Verify source, contractor and third-party rights for open licensing. Mozilla Fellow owns work product, but open-license obligations affect commercial licensing optionality.
- [ ] Separate this from EA Funds and Foresight: different scope, periods, labor allocations and deliverables; disclose any actual applications/awards. Do not seek duplicate funding for the same labor.
- [ ] Applicant personally writes the substantive LOI in their own voice; AI may help organize evidence only. Disclose AI use in the mandatory field.
- [ ] Review live submission terms and optional sharing permission; **no submission, registration, contact, spending or agreement without explicit approval**.

## Decision economics — subjective sensitivity, not sponsor odds

A restricted **$25k project budget is not personal profit**. For modeling, value only the *incremental net benefit of the $100k stipend after the personal opportunity cost of a year of work*, assumed to be $40k–$50k. This is not verified and could be negative.

- **Cautious:** 30% personal feasibility/qualification × 0.5% conditional selection × $40,000 net stipend surplus − (3h × $35/h) = **−$45**.
- **Favorable:** 60% feasibility/qualification × 1.5% conditional selection × $50,000 net stipend surplus − $105 = **+$345**.
- **Ineligible/unavailable:** $0 payoff − $105 = **−$105** if the full three-hour preparation is undertaken.

The probabilities are *invented sensitivity assumptions*, not calibrated award odds. Only four general Independent slots are apparent; applicant pool size is unknown. Do not extrapolate the total $125k package into expected profit. Extra preparation, travel opportunity cost, lost commercial IP optionality and actual labor opportunity cost may materially reduce EV.

**Decision: WATCH / applicant evidence gate.** The public-source match is unusually strong, but a full AI-generated LOI would violate the sponsor's policy, and actual personal eligibility, community participation and capacity remain unknown. The next legitimate step is applicant-authored evidence and first-person answers, not another synthetic test. Do not displace the Oct 31 Foresight decision or rolling EA submission on an assumed fellowship win.

## Alternative screened but not advanced

[Mozilla Human-Scale AI Incubator](https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/) offers **$300k in year one** with possible **$200k follow-on**, deadline **Nov 20, 2026, 23:59 PST**, but explicitly requires a working *deployed* technology, actual early users/product-community fit, and small fit-for-purpose AI at its core. Public Svyable assets inspected here do **not** establish these. The $300k is restricted project support, not founder income. **REJECT on current evidence**, reconsider only if independently verified deployed-user and small-model evidence already exists; no speculative retrofit to chase funding.

**Sources checked 2026-10-29:** official Mozilla Fellowship [call](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/), [RFP](https://assets.mofoprod.net/network/documents/PUBLIC_2027_2028_Fellowship_RFP-2.pdf), [FAQ](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/faqs/), [eligibility guidelines](https://www.mozillafoundation.org/documents/501/Mozilla_Foundation_Grant_Eligibility_Guidelines_tNhKrgM.pdf); official [Incubator RFP](https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/) and [FAQ](https://www.mozillafoundation.org/en/what-we-do/grantmaking/incubator/human-scale-ai/call-for-proposals/faqs/).


## 2026-11-01 — bounded technical improvement (no application)

**New source:** [run_bound_receipt_demo.py](../artifacts/control-evidence-2026/run_bound_receipt_demo.py) and [14 regression tests](../artifacts/control-evidence-2026/test_run_bound_receipt_demo.py), committed with [CI workflow wiring](../.github/workflows/control-evidence-contract.yml). These are an independently runnable *local demonstration* of a narrow mitigation for the earlier unauthenticated `writer: independent` label and receipt replay gap, not a deployment or a new user study.

- A supervisor invokes a real isolated Python subprocess (no shell, network, credentials or external system), reads its exit status and output digest, creates a random 128-bit run ID, and MACs a canonical receipt with an in-process secret.
- The verifier requires the expected run ID and payload digest, verifies the MAC with a shared key, checks strict receipt fields and rejects reuse of the same run ID within its supplied in-memory set. Success, explicit worker failure, post-execution mutation and missing observation yield the four expected verdicts.
- **Local test evidence:** Python 3.13.5; `python -m unittest discover -s /mnt/data/mozilla_demo -p 'test_run_bound_receipt_demo.py' -q` — **14/14 passed**, rerun 2026-11-01 (8.883s). Demo output: `success supported`, `fail refuted`, `tamper insufficient_evidence`, `missing insufficient_evidence`. GitHub file blobs `1541995f0cd4064df2aefd8365781ddb92b70629` and `abe4262cb94105fa131aa84e70c0fa30316cf4e9` were read back and match the locally tested files' `git hash-object` identities. This is **local** test evidence; no new successful remote CI run is claimed.
- **Threat boundary:** HMAC demonstrates possession of a shared key, not independently trusted authorship. The supervisor/verifier and key are assumed uncompromised; replay tracking is **in memory only**, so a verifier restart without a durable ledger reopens replay. There is no trusted clock, cross-host attestation, real inbox, live agent, independent reviewer, user adoption or external benchmark. The adversarial fixtures are visible and deliberately synthetic.
- **Relevance to Mozilla's exact RFP:** the example of an afternoon agent-audit kit for a nonprofit requires run-bound receipts rather than self-asserted writer labels. This change makes the *local* acceptance boundary executable and testable, but does not clear Mozilla's community co-design, personal senior-leadership, legal receipt, 12-month availability or charitable-benefit gates.
- **IP/reuse:** code is committed to the existing Apache-2.0 Opps repository and is potentially reusable in BlueDot/EA Control Evidence experiments. Verify individual contribution rights and exclude any double-funded hours; do not imply that code reuse is an external adoption signal.

**Incremental economics, not measured grant odds:** assume ~1.5 hours of coding/testing/documentation at $35/h = **$52.50** labor cost. If the conditional net personal benefit of the $100,000 stipend is $40,000 and applicant qualification feasibility is 40%, this incremental work would need to increase the *conditional award probability* by **0.328 percentage points** to break even if it has no reuse value. No such increase has been measured. The $25,000 project budget is restricted, and no direct commercial profit or paid engagement has resulted. No further engineering should be undertaken solely for the Fellowship without applicant and small-organization demand evidence.

**Next decision:** keep **WATCH** until the applicant personally verifies senior-level leadership, legal USD receipt, a charitable public beneficiary, a genuine community pathway, 2027 availability and ability to open-license outputs. Mozilla prohibits AI-generated full LOI answers; this engineering appendix is *not* submission text. The applicant must independently write the LOI and explicitly authorize submission before December 17, 2026 at 23:59 PST.
