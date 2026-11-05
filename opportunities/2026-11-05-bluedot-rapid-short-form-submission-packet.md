# BlueDot Rapid — short-form application packet and submission gates (NOT SUBMITTED)

Prepared 2026-11-05. **Candidate:** Svyable Control Evidence, self-contained $4,500 version only. This is a concise applicant-review packet, not a completed application, verified personal qualification, authorization to apply, or grant acceptance. It consolidates existing evidence rather than claiming new tests.

## Current official decision criteria and terms

BlueDot's [live Rapid Grants page](https://bluedot.org/grants/rapid), checked 2026-11-05, states: up to **$20,000**; time/living costs and research/experiments permitted; roughly **15-minute** application; applicant should show a worthwhile direction, evidence of progress and why funding matters. No fixed deadline appears. BlueDot affiliation is a positive selection signal, **not a formal prerequisite**. Restricted recipient countries and sanctions apply; money is paid **after a claim and checks**, as one lump sum, with potential transfer fees; approved-purpose use and written approval for material changes are required; a report is due within 60 days after completion. The payer has [publicly described earlier grant awards](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants), not independently audited here.

## Applicant-editable proposed answers (do not send without authorization)

**What problem and why does it matter?** AI tool-use reports can describe consequential actions as successful even when the report's purported independent evidence is merely a self-asserted label or a replay. An auditor that treats these assertions as trusted can mistakenly endorse unsupported actions. This pilot tests a narrow, falsifiable local trust boundary, **not** catastrophic-risk reduction in deployed systems.

**What exists today?** Svyable has a public [local subprocess/file-observation pilot](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py) and [five synthetic negative-control tests](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py). The historical [GitHub Actions run](https://github.com/Svyable/Opps/actions/runs/41170302920) reported 82 passing tests. The five negative controls **pass while exposing a gap**: synthetic self-described independent recorder labels and replayed events can be accepted. These tests do **not** establish recorder authentication, third-party replication, real-agent deployment or a safety effect.

**What will the grant unlock?** Four weeks of prospective work, 60 founder hours subject to availability: (1) freeze adversary capabilities and test matrix, (2) implement supervisor-owned run binding and reject/abstain behavior for untrusted origin or freshness, (3) publish raw counts on forged/replayed/missing/legitimate constructed cases, (4) release pinned reproduction instructions, failures and a stop/go report. Success target: **0 falsely supported forged/replayed constructed cases**, with denominator disclosed and at least one legitimate local subprocess case preserved. This is a *target*, not an outcome. No independent reviewer is promised or budgeted.

**Budget and why now?** Request **$4,500** of restricted time/living support: 60 hours × $75/hour planning rate; $0 for reviewers, compute and equipment. The rate and actual ability to free 15 hours/week are **not yet verified**. The grant would fund new recorder-integrity work, not reimburse existing pilot/tests or proposal-writing. No other sponsor may pay for the same hours. This proposal is an alternative to, **not cumulative with**, the older $6,000 version.

**Evidence and reporting?** Public source, reproducible commands, frozen threat model, test inputs and numerator/denominator outcomes, including negative results. Submit the funder's required completion report within 60 days of finishing. Do not assert independent human validation or production security.

## Submission release matrix (all required; currently unverified)

| Gate | Required evidence before submitting | Current disposition |
|---|---|---|
| Lawful recipient | Real individual/entity payee, location, sanctions and tax review | **UNKNOWN** |
| Capacity | Applicant confirms 60 *future* hours in four weeks | **UNKNOWN** |
| Rate and economic benefit | Applicant validates $75/hour support and grant's counterfactual value | **UNKNOWN** |
| IP | Contributor and third-party rights for specific source/data to be published | **UNKNOWN** |
| Nonoverlap | Dated work-package ledger separating EA Funds, Seed, Foresight and any other awards | **UNKNOWN** |
| Form and approval | Applicant checks live authenticated form/acceptance terms and explicitly authorizes submission | **NOT APPROVED** |

**Decision:** Conditional PURSUE, **do not submit**. The remaining constraint is first-party evidence and approval, not additional synthetic tests or prose. No outreach, application, expenditure, hiring or contractual commitment.

## Marginal economics and stop-loss

Existing prospective scenario (not observed grant statistics): $1,800 conditional economic benefit × 50% eligibility/fit × 60% delivery × 8% award − $35 remaining applicant labor = **+$8.20**. The gross $4,500 is restricted project funding, not profit. If this packet requires 0.5 hours at $35/hour, its additional opportunity cost is **$17.50**; absent measurable odds improvement, net prospective EV *including this new cost* becomes **−$9.30**. To recover $17.50 at 50% fit, 60% delivery and $1,800 benefit requires **+3.24 percentage points** in conditional award probability; no such improvement is claimed. **Stop further autonomous drafting** unless one of the six gates clears or the funder requires specific missing evidence. This packet primarily prevents accidental overclaiming and reduces human editing time; neither benefit is monetized.
