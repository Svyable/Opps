# Foresight 2026 — grant-overlap control and funder disclosure annex

**Prepared 2026-10-27 · Foresight status: PURSUE / draft, NOT SUBMITTED · Internal application support, not a grant agreement.**

**Primary sources:** [Foresight Coordination and Accountability RFP](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/) (deadline **October 31, 2026, 23:59 PDT**; open-source work products, due diligence, progress reporting, up to 10% overhead on direct research costs) and [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) (rolling, typical $10k–$150k). These sources **do not establish that either funder has approved concurrent support**. This document proposes controls for applicant review, not a representation of funding, staff, approval, or eligibility.

## Commercial decision: do not treat two proposed grants as $60,000 unrestricted revenue

Svyable has two related but distinct **unsubmitted** proposals:

- **Foresight, $35,000 / 12 weeks:** *Control Where It Counts* — prospective intervention study of **no gate vs cosmetic approval vs enforced authorization boundary**, measuring unauthorized completions, false blocks, throughput, latency, and the normative boundary between delegation and human control. Existing deterministic mock gate has **28 passing tests**; no actual agent intervention trials or human review yet. [Narrative](foresight-2026-application-narrative.md), [two alternative budgets](foresight-2026-itemized-budget-capacity.md), [CI receipt](https://github.com/Svyable/Opps/actions/runs/40363475074).
- **EA Funds, $25,000 / 10 weeks:** *Control Evidence* — retrospective **claim-to-independent-receipt adjudication**, comparing narrative-only vs structured evidence judgments, including missing and contradictory evidence. Existing synthetic components have **34 passing tests**; no authenticated trace study or independent adjudication yet. [Application draft](taif-control-evidence-2026-application-draft.md), [CI receipt](https://github.com/Svyable/Opps/actions/runs/40251427716).

The common theme of agent oversight and some pre-existing code are **not** two separately billable discoveries. Grant restrictions, actual deliverability and staff capacity must be checked before any application is submitted or award accepted.

## 1. Dollar-for-dollar proposed budget separation

These are *planning allocations only*, not incurred costs or supplier quotes.

| Expense category | Foresight A: founder-led | Foresight B: delegated | EA Funds Control Evidence | Separation control |
|---|---:|---:|---:|---|
| Research lead | 240h × $85 = **$20,400** | 144h × $85 = **$12,240** | 120h × $100 = **$12,000** | Unique dated time entries with project code and deliverable; no shared billed hour |
| Independent engineering | 120h × $75 = **$9,000** | 200h × $75 = **$15,000** | 100h × $75 = **$7,500** | Separate SOWs, work logs, acceptance receipts, and non-overlapping invoice lines |
| Independent review | 24h × $100 = **$2,400** | 40h × $100 = **$4,000** | 30h × $100 = **$3,000** | Different review protocols/case IDs; preserve blinding and conflict declarations |
| Compute / storage | **$1,200** | **$1,760** | **$1,000** | Project-tagged runs, storage and usage receipts; no duplicate reimbursement |
| Documentation / accessibility / dissemination | Included in lead work and overhead; **$0 separately** | Included in lead work and overhead; **$0 separately** | **$1,500** | EA-only independently identified deliverables; Foresight outputs not billed again |
| Direct costs | **$33,000** | **$33,000** | **$25,000** | Foresight alternatives A/B are mutually exclusive |
| Overhead | **$2,000** | **$2,000** | **$0 separately** | Foresight 6.06% of direct research costs; document actual basis |
| **Total** | **$35,000** | **$35,000** | **$25,000** | **$60,000 combined only if BOTH are separately approved and fully deliverable** |

**Do not add Foresight A and B together.** Their labor, hours and cost assumptions are mutually exclusive. A sponsor's grant award is restricted project support, not a contract guaranteeing personal income or profit.

## 2. Deliverable ownership and evidence firewall

| Work product | Foresight-only billable outcome | EA-only billable outcome | Shared pre-existing, nonbillable input |
|---|---|---|---|
| Research question | Causal effect of authorization enforcement vs cosmetic/no gate | Epistemic validity of agent claims vs independent receipts | General agent oversight ideas |
| Dataset | Prospectively frozen three-arm intervention tasks, unique F-prefixed case IDs | Separately frozen claims/evidence packet set, unique E-prefixed case IDs | Existing synthetic test fixtures, disclosed with source hash |
| Instrumentation | Authorization gate, policy decisions, blocked/executed mock actions | Tool-side completion, approval and alert-delivery receipts | Existing authorization/provenance libraries |
| Experiment | Randomized real-agent sandbox trials under three enforcement arms | Blinded narrative-only vs receipt-supported judgments | Existing mock/unit tests are **not** either experiment |
| Evaluation | Unauthorized completion, legitimate task success, false blocks, delay | False support, justified abstention, disagreement, review time | Statistical helper methods, with attribution |
| Release | Foresight-specific trial harness, dataset, results and decision rubric | EA-specific adjudication schema, cases, results and replication guide | Permissively licensed code reused with license notices |

**Hard controls before any funded work:** project-specific immutable study manifests; separate experiment IDs, budget codes and versioned outputs; provenance linking every billed hour and invoice to one project; explicit allocation for genuinely shared infrastructure approved by both funders in writing, otherwise **bill it to neither twice**; holdout sets and labels inaccessible to blinded reviewers; no retrospective charging of pre-award prototype development unless expressly permitted. If a case or work product materially serves both grants, document the overlap and get approval for an equitable allocation **before** spending.

## 3. Founder capacity: the real constraint if both are awarded

- **Foresight A + EA, fully concurrent:** 20h/week Foresight + 12h/week EA = **32h/week** of lead effort during the ten overlapping weeks; approximately **360 distinct lead hours** across the two studies, plus administration and possible Node travel.
- **Foresight B + EA, fully concurrent:** 12h/week Foresight + 12h/week EA = **24h/week** during overlap; **264 distinct lead hours** overall, plus administration and travel. B also assumes **300 engineer hours** and **70 independent-reviewer hours** across both grants; none are staffed.
- **Foresight A + EA external work:** 220 combined engineer hours and 54 reviewer hours, if separately procured.
- **Sequential scheduling:** May reduce weekly conflict, but requires real award dates, actual funder-approved start dates and confirmation that milestone timelines permit it. Do not assert either funder will allow delay.

**Current feasibility evidence: NONE** for the applicant's weekly hours, payee, professional reference, Node participation, engineers, reviewers, quotations, data/contractor rights or funder approval of overlapping support. If capacity cannot be established, prefer a single deliverable project or rescope/withdraw one proposal rather than double-commit.

## 4. Copy-ready disclosure language — subject to applicant verification

**For Foresight's application or later due diligence:**

> Svyable is also preparing, but has not submitted or received, a separate $25,000 application to EA Funds for a ten-week study of whether independent reviewers can verify claims about AI-agent actions from execution-side evidence. This Foresight request is for a different twelve-week prospective experiment comparing no authorization gate, cosmetic approval and enforced tool-boundary approval. We would reuse properly licensed pre-existing software, but would not charge the same personnel hours, cases, compute, contractor invoices, experiments or deliverables to both funders. If both projects were funded, we would seek funder agreement on separate scopes, dates, cost codes, staffing and any shared inputs before accepting or spending either award. Neither award, staff availability nor approval of concurrent support is presently secured.

**For EA Funds' application or later due diligence:**

> Svyable is separately preparing an unsubmitted $35,000 Foresight proposal testing the prospective effects of human authorization gates. The EA Funds request would instead support retrospective claim-to-receipt adjudication with independent blinded reviewers. The applications share pre-existing open-source foundations, not billable work products. We would disclose any change in funding status and agree distinct milestones, case sets, staffing, costs and outputs with each funder before undertaking concurrent funded work. We do not represent either award or personnel commitment as secured.

**Accuracy rule:** If one application is submitted, awarded, rejected, withdrawn or materially revised before the other is sent, update the language to the *actual* status. The statements above are true only while **both are drafts and neither has been submitted**.

## 5. Submission and award gate

1. Verify legal recipient and applicant identity; select **one** Foresight budget based on demonstrable capacity.
2. Verify Foresight's actual Airtable questions, privacy/share choices, professional reference and real Node participation plan. The public RFP explicitly prioritizes in-person Node contribution, requires open-sourcing funded code/data/outputs, up to 10% overhead, due diligence and reporting; do not invent a Node commitment.
3. Confirm independent engineering and reviewer availability and rights, or reduce experimental scope before promising milestones.
4. Use the disclosure above only after checking any existing external funding or customer agreements. Do not claim that Foresight or EA Funds has explicitly approved dual funding.
5. Before award acceptance, obtain actual grant agreements and confirm reporting, pre-existing IP treatment, publication duties, shared-cost allocation, permitted start dates and tax obligations. Stop if conditions conflict.
6. Obtain explicit applicant approval before any form submission, outreach, payment or contractual commitment.

**Priority:** Foresight's October 31 deadline expires first; the EA Funds call is rolling. The overlap controls improve submission integrity, but **do not increase estimated award odds** or cure the applicant-controlled eligibility gaps. No applications, contacts, expenses or commitments are authorized by this annex.
