# UMGC 92303 — Official RFP compliance and bid/no-bid gate

**Audit date:** 2026-10-08  
**Source of truth:** [UMGC Bid Locker solicitation #92303](https://bidlocker.us/a/umgc/details/6564_Umgc_Solicitation_92303_Custom_Ai_Enabled_Content_Development) · [35-page official RFP PDF](https://bidlocker.us/uploads/documents-guid/5980c4f0-a6a2-492a-ab52-e946b89347b2/UMGC%20RFP%2092303.pdf)  
**Purpose:** Determine whether Svyable can submit a **responsive and credible** prime proposal without inventing prior performance or building an enterprise LMS product. This is an internal pursuit artifact, **not** a proposal or representation to UMGC.

## Decision — prime bid is compliance-gated

**WATCH as prime until evidence gates are resolved.** The prior pursuit brief treated the opportunity as an open-ended, multi-year content contract. The actual RFP materially narrows the economics and raises the qualification bar:

- **$1,000,000 aggregate IDIQ ceiling**, **one intended award**, **no guaranteed work** (Section I.8, p.7).
- **Three-year base + two one-year options** (Section I.8, p.7).
- **Typical task order ≈ $100,000**, inclusive of program development and 12 months of recurring services (Section II.5.13, p.12).
- **At least two comparable client case studies** with annual learner counts, outcomes, completion methodology and duration (Section III.1.2.1.1, pp.24–25).
- **Current certificates of insurance** for general liability, workers' compensation, auto liability and professional liability (Section III.1.1.3, p.24).
- **Current product-specific ACR/VPAT WCAG edition v2.4+** (Section III.1.2.6.3, p.28).
- Brightspace/LTI integration, learner analytics, support and accessibility are meaningful delivery requirements, not merely nice narrative extras.

These are not demonstrated by public Svyable research repos. **Do not claim they exist.** A specialist content/evaluation subcontract to a qualified prime may have better expected value than a standalone bid, subject to the actual subcontracting rules and partner economics.

## Dates and submission mechanics

| Item | Official fact | Source |
|---|---|---|
| Questions deadline | **2026-10-29 10:00 AM ET** | RFP cover / p.2 |
| Technical and price proposals | **2026-11-20 10:00 AM ET** | RFP cover / p.2 |
| Oral discussion, if shortlisted | Week of **2026-12-07**, anticipated | RFP p.2 |
| Award selection | **2027-01-21**, anticipated | RFP p.2 |
| Execution | **2027-02-17**, anticipated | RFP p.2 |
| Submission | **Separate technical and price uploads through UMGC Bid Locker**; register before uploading | RFP §I.5, pp.5–6 |
| Pricing firewall | **No pricing in technical proposal**; may be deemed non-responsive | RFP §I.5.1, pp.5–6 |
| Questions channel | Email procurement officers using subject `Questions RFP 92303` and RFP section/page reference | RFP §I.3, pp.4–5 |
| Official document set | 11 attachments on Bid Locker; monitor for addenda | Bid Locker notice |

**Important correction:** a third-party listing suggests email proposal submission. **That is wrong for this RFP:** UMGC's own procurement instructions and RFP require Bid Locker uploads. No external communication or account registration has been performed.

## Compliance matrix

Status key: **UNKNOWN** = not established by reviewed public Svyable assets; **PARTIAL** = public technical evidence exists but not delivery qualification; **REQUIRES REVIEW** = legal/operational decision; **PROVEN PUBLIC** = repo evidence for a narrow technical claim only.

| ID / source | Requirement | Evidence / reuse | Gap / next evidence | State |
|---|---|---|---|---|
| G01 §III.1.2.1.1 pp.24–25 | Minimum **2 comparable case studies** with actual client, annual learners, scope, outcome metrics, completion method, duration | Desk/ScrollQ/Agents are technical work samples, **not** client deployments | Locate two real engagements with permission to name clients and verifiable learner outcomes | **UNKNOWN — PRIME GATE** |
| G02 §III.1.1.3 p.24 | Current COI: general, workers' comp, auto, professional liability | None established | Verify policies, limits, applicability and cost; do not purchase without approval | **UNKNOWN — PRIME GATE** |
| G03 §III.1.2.6.3 p.28 | Current product/service-specific ACR using VPAT WCAG edition 2.4+ | Public HTML repos are not ACRs | Define offered product; obtain accurate assessment/report from qualified reviewer | **UNKNOWN — PRIME GATE** |
| G04 §III.1.2.4 pp.27–28 | D2L Brightspace integration through LTI, analytics/xAPI/LRS, enrollment, progress | Agents/ScrollQ prove general technical implementation discipline only | Document real LTI 1.3, OAuth/OIDC, xAPI and Brightspace integration capability or qualified delivery partner | **PARTIAL — DELIVERY GATE** |
| G05 §II Attachment A pp.13–15 | WCAG 2.1 AA, ADA Title II, §504/508, accessible multimedia and ongoing remediation | Accessible-content design is feasible, not certified | Document testing workflow: automated + screen-reader + keyboard + captions + human review | **UNKNOWN — DELIVERY GATE** |
| G06 §II Attachment B p.17 | 99.5% desired uptime; critical incident response within 30 minutes; learner support coverage and SLAs | No hosted learning platform/SLA proven | Verify support staffing, escalation, monitoring, partner capability, economics | **UNKNOWN — DELIVERY GATE** |
| G07 §III.1.2.6.2 p.28 | Disclose SOC 2 Type II, or alternative controls/assessments | No certification established | Accurate statement of security posture; review whether a partner is needed | **UNKNOWN** |
| G08 §III.1.2.6.4 p.28 | HECVAT if available | Not established | Disclose availability accurately | **UNKNOWN (conditional)** |
| G09 §III.1.2.6.5 p.28 | Current AI governance documentation | Svyable repos show evaluation and bounded-agent discipline | Package actual policy, prompt/model update process, risk register, human QA; do not assert corporate certification | **PARTIAL** |
| G10 §III.1.2.2–2.3 pp.25–27 | Skills-aligned modular content, continuous updates, human QA, AI governance, learner support | Desk + ScrollQ + ARC + Agents offer concrete methodology | Build one 5-module sample with outcomes, assessments, traceability, review and change controls | **PARTIAL** |
| G11 §II.4.2 p.9 | Asynchronous/self-paced, distributed learners | Content can be authored; no production LMS demonstrated | Define platform integration and data residency model | **PARTIAL** |
| G12 §II.4.4 p.10 | Learner-level analytics including demographic data, engagement, completion | No compliant learner analytics deployment established | Privacy design, minimum-data collection, consent, retention and access controls | **UNKNOWN** |
| G13 §III.1.2.5 p.28 | Account manager, hosting, learner support, exit/migration plan | Named responsible operator not verified | Actual staffing and transition design | **UNKNOWN** |
| G14 §III.1.1.2 pp.24–25 | A-1 addenda, A-2 bid affidavit, A-3 references | Forms available on Bid Locker | Complete only with verified signatory/company/reference facts | **UNKNOWN** |
| G15 §III.1.1.4 pp.24–25 | Review Appendix C terms; identify exceptions in technical proposal | Public brief not a contract review | Legal review of IP, warranties, indemnity, liability, data rights and subcontracting | **REQUIRES REVIEW** |
| G16 §III.3 pp.31–33 | Price proposal B-1, B-2 **all four tabs**: rate card, hypothetical, recurring, assumptions | No pricing model approved | Model 5 modules, ~50 learning hours, ~500 learners/year, 3-month launch and 12-month support | **UNKNOWN** |
| G17 §II.5.5 p.11 | Response to future task-order request within **10 calendar days** | Potentially achievable with templates | Verify staffing and reusable estimates | **UNKNOWN** |
| G18 §II Attachment A p.14 | Work in UMGC Smartsheet environment | No client experience established | State capability truthfully; demonstrate process, not invented prior client use | **UNKNOWN** |

### Preferred but not strict eligibility conditions

Section III.2.1.2 (pp.25–26) prefers 1,000+ learners annually, two similar higher-education clients, ≥70% completion by 150% of expected duration, military-affiliated learner experience and quantified learner outcomes. These are **preferred**, whereas the two case studies and specified proposal materials are required. Absence of preferred experience still harms ranking because experience is the **top technical criterion** (§III Article 2, p.29).

## Concrete reusable technical exhibit — evidence-backed learning-object schema

This is a **proposal concept**, not a claim that a production learning platform already exists.

```yaml
learning_object_id: ai-eval-01
version: 0.1-draft
program: Applied AI Evaluation and Agent Reliability
workforce_skill: "Construct a reproducible test for an AI-assisted workflow"
learning_object_type: "scenario + applied assessment"
delivery: "asynchronous / platform-neutral source; LTI packaging not yet implemented"
objectives:
  - "Identify an ungrounded output and its downstream risk"
  - "Design a five-case evaluation set with pass/fail criteria"
  - "Record a source-to-claim trace and a human-review decision"
assessment:
  artifact: "evaluation case sheet and failure analysis"
  rubric:
    reproducibility: 30
    evidence_traceability: 30
    failure_analysis: 25
    accessibility_and_clarity: 15
source_packet:
  - "https://github.com/Svyable/scrollq"
  - "https://github.com/Svyable/ARCPrize2026"
human_review:
  factual: pending
  instructional_design: pending
  accessibility: pending
  security_privacy: pending
change_control:
  triggers: ["source revision", "model/tool behavior change", "rubric drift"]
  regression_evaluation: pending
  learner_analytics: "not implemented; privacy design required"
```

### Five-module / 50-hour illustrative program map

| Module | Skill outcome | Applied assessment | Approx. learner hours |
|---|---|---|---:|
| 1. Model evidence vs claims | Distinguish demo from validated capability | Evidence classification audit | 10 |
| 2. Prompt and tool boundaries | Identify prompt injection and permission failures | Threat-model exercise | 10 |
| 3. Reproducible evaluation | Build versioned test cases and scorecards | Test harness + rubric | 10 |
| 4. Provenance and human QA | Trace claims to sources and reviewer decisions | Evidence passport | 10 |
| 5. Deployment, drift and maintenance | Define update triggers, regressions and escalation | Capstone maintenance plan | 10 |

This mirrors the RFP's **hypothetical pricing scenario** (five modules, ~50 hours, 500 learners/year, three-month launch, Brightspace integration). It is **not** a priced commitment and does not demonstrate LTI, accessibility certification or learner-support staffing.

## Bid economics after official-document review

The earlier `$300k × 8% − $6k = $18k` base case is **not supportable as a current prime-bid EV** without case studies, VPAT, insurance and LMS delivery evidence.

Use **contribution margin** rather than gross contract revenue where delivery costs are material:

`EV = P(responsive) × P(win | responsive) × expected contract contribution margin − pursuit cost`

**Illustrative gate model, not a forecast:**

- If responsive probability = 20%, conditional win = 5%, realized task orders = $200k, contribution margin = 30%, bid cost = $5k, then EV = `0.20 × 0.05 × $60k − $5k = −$4,400`.
- If credible prime + partner raises responsiveness to 80%, conditional win = 10%, realized task orders = $300k, contribution margin = 30%, bid cost = $6k, then EV = `0.80 × 0.10 × $90k − $6k = +$1,200`.

The full $1M ceiling is **not expected revenue**; the ~$100k typical task order is an **official planning figure**, not a guaranteed minimum. A specialist subcontract may offer lower gross revenue but much lower compliance/pursuit cost.

## Go / no-go gate

**Before October 29:**
1. Identify two genuine comparable client case studies with completion methodology and outcomes. If none, **do not draft a prime submission**.
2. Verify COI, ACR/VPAT and a credible Brightspace/LTI delivery route. If missing, **seek a qualified prime partner rather than misrepresent readiness**.
3. Review Appendix C-1 and Appendix S for ownership of background IP, deliverable IP, data, indemnity, warranties, subcontract approval and termination. No legal commitments.
4. If a responsive path exists, use the official RFP sections to create the final technical response and pricing workbook; keep price out of technical proposal.
5. If no credible path, move **REJECT as prime / WATCH for specialist teaming** and focus engineering on SPARK, GEMS or ScrollQ instead.

**No application, question email, vendor registration, spending, or legal commitment was made in this audit.**
