# TAIF funding-release decision — 2026-11-14 (official-source check)

**Status:** PURSUE / HOLD. **No application submitted.** This is a decision aid, not evidence of eligibility or award.

## Payer and current route

The Effective Altruism Funds **Transformative AI Fund** (TAIF) is the active fund; the Long-Term Future Fund is **closed** and must not be selected on an application. TAIF's official page explicitly says applications are always open, typical awards are **$10,000–$150,000**, rarely over $300,000, and applicants may be individuals, new organizations or existing organizations beginning new projects. The fund primarily prioritizes work reducing catastrophic risk from advanced AI. EA Funds publishes a historical grant database. This is evidence of payer activity, not assurance of funding.

Official sources checked 2026-11-14:
- https://funds.effectivealtruism.org/funds/transformative-ai
- https://funds.effectivealtruism.org/funds/far-future
- https://funds.effectivealtruism.org/grants
- https://funds.effectivealtruism.org/apply-for-funding

## Specific submission weakness and corrective scope

The repository has multiple Control Evidence grant narratives, including BlueDot Rapid, with potentially overlapping future instrumentation, paired agent evaluation, and reporting. **The TAIF application must contain an exclusive expense schedule**, not merely a narrative assertion of non-overlap. Existing mock-gateway and scorer fixtures are reusable *prior work*, not independently recorded real-agent outcome evidence. A passing unit/fixture CI suite is not a field efficacy result.

Before release, create one immutable project budget with line IDs, each containing: deliverable, named payee, quantity, hourly or invoice rate with basis, amount, dates, whether already incurred, alternative funding source, and a yes/no exclusivity attestation. Sum by line and reconcile against any BlueDot request; reject duplicated line IDs or overlapping deliverables/time. No retroactive compensation assumption. Link a real agent/gateway execution receipt and explicit method/limitations for any empirical claim.

## Conservative commercial model

TAIF award face value is restricted project financing, **not automatically net personal income**. For a purely illustrative $25,000 request with $20,000 legitimate incremental project costs, the conditional residual is $5,000 *only if unrestricted and lawfully retainable*; absent agreement review, treat residual as **$0 verified cash benefit**. If preparation takes 2 hours at a hypothetical $35/hour, pursuit labor is $70. With a genuine $5,000 conditional net benefit, break-even joint qualification/award/payment probability is 70/5000 = **1.4%**. With verified personal residual $0, the direct founder-cash EV is **negative $70** regardless of award likelihood. Neither 1.4% nor any award probability is a prediction. Technical/IP reuse is high; independent instrumentation and budget evidence remain substantial.

## Release checklist (do not infer facts)

1. Applicant legal identity, jurisdiction, receiving account and capacity: **UNVERIFIED**.
2. IP ownership and permission to reuse relevant Svyable code/datasets: **UNVERIFIED**.
3. New project work, deliverables and causal connection to catastrophic AI risk: **PARTIALLY DRAFTED; not externally validated**.
4. Independently recorded agent/tool execution traces and scorer provenance: **NOT VERIFIED FOR THE PROPOSED REAL-AGENT STUDY**.
5. Exclusive TAIF budget reconciled line-by-line with BlueDot alternatives: **NOT COMPLETE**.
6. Grant agreement, allowable compensation, publication and IP obligations: **NOT REVIEWED**.
7. Human approval to submit: **NOT GRANTED**.

**Decision:** Preserve TAIF as PURSUE, BlueDot Rapid as PURSUE/HOLD, and all five frontier benchmark lanes unchanged. No speculative claim of positive monetary EV. Next scarce-hour investment should go to an exclusive eligible-cost budget and one externally reproducible tool-execution receipt, not another cosmetic narrative edit. No registration, submission, contact, purchase, terms acceptance or IP transfer authorized.
