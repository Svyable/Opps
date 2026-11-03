# BlueDot Rapid — official-page conflict and $4,500 submission hold (2026-11-03)

## Decision
**PURSUE — HOLD (no application, expense, or claim).** A fresh public search of the canonical [Rapid Grants page](https://bluedot.org/grants/rapid) on November 3 returned **$50–$10,000**, **stipends/living expenses outside usual scope (exceptional case possible)**, and **upfront payment by default, sometimes reimbursement**. This materially contradicts the earlier November 3 ledger assertion of a **$20,000 ceiling, explicitly routine time/living eligibility, and payment after approved claim**. The discrepancy could reflect a changed live page or inconsistent site snapshots; neither version should be treated as unconditionally authoritative without reviewing the actual application terms immediately before submitting. The $4,500 request is below either ceiling, but its **entire budget is founder time**, making the cost-category ambiguity decisive.

Sources: [canonical Rapid page](https://bluedot.org/grants/rapid) (fresh search result, Nov 3, 2026); [BlueDot's Apr 14, 2026 retrospective](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants) (77 grants, over $50k, exceptional examples including $8k transition support); [March 17 participant-specific sprint rules](https://blog.bluedot.org/p/rapid-small-grants-for-the-bluedot) (different restricted program; **do not** apply its participation requirement to general Rapid).

## Reuse and qualification
Existing Control Evidence code, local subprocess evaluation, and historical CI may support project readiness. No new test or security assurance is claimed. Applicant must attest 60 **future** hours at $75/hour, lawful payee, contributor permissions, absence of overlapping EA Funds / other funded work, and a demonstrable AI-safety bottleneck. Historic grant precedent is not approval of ordinary founder labor. Payer credibility is supported by BlueDot's published grant history, not independent verification of each payment.

## Risk-adjusted go/no-go
The proposed **$4,500** is a request, not a prize or contract fee. Assume conditional *net* applicant economic benefit of **$1,800** (after delivery opportunity cost), 60% delivery feasibility, 8% conditional selection, and $35 remaining applicant labor. These probabilities are subjective, not empirical.

- At 10% cost-category eligibility feasibility (exceptional-stipend case): **$1,800 × .10 × .60 × .08 − $35 = −$26.36**.
- At 50% category feasibility (if applicant verifies an explicitly eligible cost basis): **+$8.20**.
- Break-even category feasibility: **40.51%** at these assumptions.
- A 30-minute applicant check costing $17.50 is worth pursuing only if it resolves the uncertainty enough to avoid a futile $35 application or establishes a stronger qualifying budget. No measurable award-probability uplift from this document.

## Release gates
1. Read the live form and linked grant conditions at time of intended submission; preserve dated text or screenshots and resolve the **$10k vs $20k, stipend, and payout** discrepancies.
2. If founder compensation remains exceptional, supply truthful evidence why money is the actual bottleneck; otherwise **do not invent compute, travel, reviewers, invoices, or alternate costs**.
3. Use actual prospective allocations with the existing `tools/funding_overlap_guard.py`; a passing synthetic test does not establish no duplicate billing.
4. Verify legal receipt, contributor rights, time commitment and tax/transfer implications.
5. Applicant approves final content and any required terms; no autonomous submission.

**Next decision:** hold BlueDot Rapid pending applicant-controlled facts, while favoring rolling EA Funds research funding if independent review, authenticated evidence and non-overlap can be substantiated. Do not continue polishing speculative applications.
