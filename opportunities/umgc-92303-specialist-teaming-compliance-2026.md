# UMGC RFP 92303 — specialist teaming / compliance decision package

**Prepared 2026-10-27. Internal, nonbinding. Status: WATCH (no prime bid).** No inquiry, proposal, subcontract offer, registration, or acceptance has been sent. This is not a representation that Svyable has government contracting credentials, two comparable client case studies, an LMS integration, accessibility certification, or operational capacity.

## Source of record and commercial shape

- **Buyer:** University of Maryland Global Campus (UMGC), public university. **Official [Bid Locker listing](https://bidlocker.us/a/umgc/details/6564_Umgc_Solicitation_92303_Custom_Ai_Enabled_Content_Development)** and [35-page primary RFP](https://bidlocker.us/uploads/documents-guid/5980c4f0-a6a2-492a-ab52-e946b89347b2/UMGC%20RFP%2092303.pdf).
- **Questions:** October 29, 2026 **10:00 a.m. Eastern**. **Technical and price proposals:** November 20, 2026 **10:00 a.m. Eastern**, separate uploads through Bid Locker. The RFP requires registration before upload; technical response **must not contain pricing** (pp. 1, 5–6).
- **Award:** one single-award, indefinite-delivery/indefinite-quantity (IDIQ) contract, initial three years plus two discretionary one-year renewals. **$1,000,000 aggregate task-order ceiling, no guaranteed work or revenue** (p. 7). A typical task order is approximately **$100,000 including development and twelve months' recurring services** (p. 12). These are buyer figures, not Svyable receipts.
- **Expected scope:** short-form modular workforce learning, skills mapping, assessment, AI content operations, D2L Brightspace access, analytics, maintenance and learner support (pp. 8–12).
- **Procurement status:** Bid Locker displayed the opportunity as Open on October 27. Its public [vendor Q&A](https://bidlocker.us/a/umgc/details/6564_Umgc_Solicitation_92303_Custom_Ai_Enabled_Content_Development) already contains **pending questions** on whether subcontractor case studies count, consortium responses, prime/subcontractor security evidence, Brightspace-only delivery, and ownership of pre-existing tools. Do **not** send duplicate questions; monitor the published answers/addenda.

## Mandatory / preferred compliance crosswalk (primary RFP)

| Source | Buyer requirement | Svyable evidence / gap | Decision |
|---|---|---|---|
| §III.1, pp. 24–25 | Complete signed forms, affidavits, addenda acknowledgments, proper technical format | Legal entity, authorized signatory and forms not verified | **Hard gate** |
| §III.2.1.1, p. 25 | **Two comparable client case studies** with named client, annual learners, outcome metrics, completion methodology and duration | Public books and code are **not** verified client deployments; cannot fabricate case studies | **Prime no-go pending evidence** |
| §III.2.1.2, pp. 25–26 | Preferred ≥1,000 learners/year, two higher-ed clients, ≥70% completion at 150% expected time, military learner experience | No verified metrics; preferred, not stated mandatory | Scoring disadvantage |
| §III.2.2–2.3, pp. 26–27 | Instructional design, QA, AI governance, adaptive learning, current vs planned features, update controls | Source/provenance/review patterns exist; deployed educational service and results unverified | Narrow specialist fit |
| §II.4.2 and Attachment A, pp. 9, 13 | Brightspace integration; LTI 1.3, xAPI, SSO described as desirable standards | No verified production Brightspace/LTI/xAPI integration | Prime technical gap |
| Attachment A §8, pp. 14–15 | WCAG 2.1 AA or applicable successor across all digital deliverables | No verified independent ACR, accessibility audit or remediation team | **Hard delivery gate** |
| §III.2.6, pp. 27–28 | Current **VPAT 2.4+ ACR**, disclose SOC 2 Type II or alternatives, HECVAT if available, AI governance and SLA documentation | No compliant Svyable product-specific ACR or SOC 2 attestation verified | **Hard proposal gate** |
| Attachment A §10, pp. 15–16 | Data protection, audits, SOC 2 Type II or equivalent if applicable | No validated enterprise controls or data-handling agreements | No learner data/hosting commitment |
| Attachment B, p. 17 | 99.5% desired uptime; critical response target 30 minutes and workaround within 4 hours | No 24/7 enterprise support capacity verified | Prime operational gap |
| §II.5, pp. 10–12 | Milestone acceptance, ~3-month build, 12-month recurring support, 10-day task-order quote response | Existing repository workflows are not a staffed services operation | Teaming only |
| §III.3, pp. 31–33 | Four price-workbook tabs: rate card, hypothetical program, recurring fees, assumptions; technical price separation | No authorized rate card, wage-cost or delivery budget | No bid |
| §I.7–8, pp. 7–8; Appendix C-1 | Submission accepts solicitation terms; contract IP and exit terms require review | Appendix C-1 not fully reviewed; public Q&A on pre-existing IP remains pending | **No legal commitment** |

**Additional unknowns:** Maryland registration and living wage application, insurance, references and subcontracting permission, accessibility responsibilities across prime and specialist, IP chain of title, data processing geography, and subcontractor flow-down obligations. The RFP and its contract appendices govern; this is a triage matrix, not legal advice.

## One narrow Svyable service that could fit under an eligible prime

**Candidate work package:** *AI Learning Content Evidence & Change-Control Layer*. This is a proposed **specialist subcontract**, not an attempt to supply the whole LMS, instructional-design operation or learner support service.

**Existing reusable evidence:** [Desk](https://github.com/Svyable/desk) maintains versioned manuscript and research sources; [Human Kind](https://github.com/Svyable/human-kind) maintains source-backed idea dossiers and human verification boundaries; [ScrolIQ](https://github.com/Svyable/scrollq) contains fail-closed provenance/evaluation patterns. These show technical approaches, **not** a deployed education QA product or past-performance claim.

**Proposed deliverables, contingent on a prime's scope and a signed agreement:**

1. **Competency-to-evidence matrix** for one pilot module: each objective linked to approved source, claim, lesson, exercise and assessment, with reviewer and revision state.
2. **AI-assisted draft change ledger**: source/version hashes, change trigger, proposed revision, human decision, regression check and rollback artifact; no autonomous publication.
3. **Deterministic QA fixtures** using public/synthetic content: missing source, stale source, conflicting claims, missing human approval, broken assessment alignment. Report pass/fail and unresolved cases.
4. **Handoff schema and documentation**: CSV/JSON export and an integration contract for the prime's Brightspace/SCORM/LTI workflow; **do not claim an existing LTI connector**.
5. **Review evidence**: a fixed sample audit showing trace completeness, error counts, time spent and any exceptions. Any accessibility conformance requires a qualified independent audit and the prime's agreed remediation path.

**Proposed acceptance tests (not achieved results):** 100% of pilot objectives have a trace to a reviewer-approved source and assessment; zero missing source IDs in the fixed acceptance set; 100% of published changes carry explicit human signoff and version/rollback reference; all deliberately planted invalid cases fail closed; exception report includes denominators and manual review notes. These are **contract targets**, not measured performance.

**Scope exclusions:** no hosting of UMGC learner records, no live tutoring, no SSO/LTI claims, no 99.5% SLA, no university-issued credential, no claim of WCAG compliance without assessment. Prime owns overall solution, integration, legal compliance and learner support unless separately contracted.

### Internal nonbinding price and EV sensitivity

A single typical **$100,000 task order** is not guaranteed. Assume the prime could allocate **$20,000–$30,000** to this specialist work (entirely hypothetical), at **35% contribution margin after delivery costs**. Conditional contribution is **$7,000–$10,500**, not $20k–$30k profit.

| Scenario | Team acceptance × prime win × actual task-order issue | Contribution if awarded | Initial 2h screening cost @ $35/h | Incremental EV |
|---|---:|---:|---:|---:|
| Cautious | 10% × 8% × 50% | $7,000 | $70 | **−$42** |
| Conditional favorable | 30% × 15% × 75% | $10,500 | $70 | **+$284.38** |

Formula: **EV = specialist contribution × P(team) × P(prime award) × P(task order) − pre-award pursuit cost.** Subjective probabilities, not buyer data; no actual teaming candidate, pricing, contract, margin, or task order exists. The earlier *prime* scenario in the structured registry remains **−$1,800** after $6k bid cost. These scenarios are alternatives, **not additive**.

## Decision and next action

**WATCH / no prime bid.** The two comparable case studies and enterprise service requirements are not evidenced by Svyable's public repositories. The only potentially rational route is a **bounded specialist role with a qualified prime**, contingent on (a) UMGC's pending clarification that such teaming is acceptable and how case studies are attributed; (b) a real prime with references, accessibility/security infrastructure and LMS delivery; (c) written scope, rate, IP carve-outs and delivery resources; and (d) explicit user approval before any external contact or commitment.

**Review the public Q&A after October 29**, update the model, and only then consider preparing a nonbinding introduction for an identified eligible prime. Do not send the text below without explicit approval:

> Svyable has public, inspectable work in source-linked research, AI-output verification and human review boundaries. For UMGC RFP 92303, we would be interested in discussing a bounded specialist role in evidence traceability and change-control QA under a qualified learning-platform prime. We would not represent ourselves as the LMS host or claim institutional learner outcomes. If your proposal includes such a role, we can exchange a specific scope and acceptance criteria after confirming compliance and IP terms.

**No outreach or bid submitted. No terms accepted.**


## October 27 — potential prime evidence scan

[Three evidence-backed prospective primes and tailored unsent nonbinding inquiries](umgc-92303-verified-prime-targets-2026.md) were prepared: Magic EdTech (D2L course build and accessibility), KnowledgeNow (named Centennial College and Western Continuing Studies Brightspace engagements), and OES Learning Solutions (institutional learning and support). **None is known to be bidding, qualified for every term, willing to subcontract, or contacted.** Buyer Q&A on teaming and IP remains pending; do not update award probabilities merely because a prospect list exists. No change to WATCH/no prime bid.
