# TAIF / Control Evidence — causal safety case and $25k decision brief
**Prepared:** 2026-11-21. **Status:** internal pre-submission material; no application, grant, independent recorder or study is represented as completed.

## Funding decision
**PURSUE / HOLD** the existing EA Funds Transformative AI Fund (TAIF) opportunity, rather than opening a duplicate. The project should be presented as a *falsifiable evaluation of false-completion claims in high-consequence agent workflows*, not as a working independent attestation system.

Official sponsor: https://funds.effectivealtruism.org/funds/transformative-ai — rolling applications, typical $10k–$150k early-stage awards, primarily projects reducing global catastrophic risks from advanced AI. EA Funds reports $100m+ historical grants at https://funds.effectivealtruism.org/. The proposed $25,000 is **restricted project funding**, not profit or a prize. No award or selection probability is established.

## Reviewer-ready causal pathway (hypothesis, not observed impact)
1. **Failure mode:** An autonomous agent reports that a safety-relevant external action was completed, but its own output, a matching file, or an agent-controlled receipt does not establish that action's provenance.
2. **High-consequence pathway:** If a human operator or automated safety gate relies on such a report to authorize a subsequent operation, an unexecuted shutdown, isolation, permission revocation, monitoring step, or incident response could remain undetected. This is a *plausible* failure mechanism; no real catastrophic incident or prevalence has been demonstrated.
3. **Intervention to test:** Independently administered action recorder, precommitted attempt manifest, key custody outside claimant control, complete-coverage checks and an abstention path when evidence is absent.
4. **Intermediate outcome:** Lower false-supported-action rate on a predeclared adversarial holdout than claim-only evaluation, while preserving usable support for valid completions.
5. **Decision value:** A reproducible failure-mode dataset and transparent coverage/abstention tradeoff could inform agent oversight and deployment gates. This does **not** establish reduction in global catastrophic risk without later adoption, external validation and a credible deployment model.

**Causal weakest links:** (a) genuine separation of recorder and claimant; (b) completeness of event coverage; (c) relevance of synthetic attacks to real agent workflows; (d) independent evaluator; (e) adoption in actual high-consequence oversight. Treat each as a milestone with evidence, not as an existing asset.

## Existing verified evidence, correctly bounded
- https://github.com/Svyable/Opps/actions/runs/44852961142 — push SHA `f5fb99ac71f395e4cce16f274f026e292fa3a4d1`, Python 3.11.18 and 3.13.18 each **6/6 tests passed**, with actual job logs cited in [verified CI evidence](2026-11-21-taif-verified-ci-run-evidence.md).
- Both legitimate matching-file and adversarial matching-byte injection paths return `OBSERVED_ONLY`. This demonstrates a *negative control and honest claim semantics*, not authenticated action execution.
- No independently controlled recorder, human evaluation, production trace, actual failure-rate estimate or downstream safety outcome exists in this evidence record.

## Falsifiable study and acceptance criteria (proposed)
Pre-register the action taxonomy, threat model, seed, frozen holdout and all exclusions before collecting data. Use >=100 independent attempts across successful action, omitted execution, delayed event, tampering, replay, missing coverage, cross-scope receipt and recorder outage. Independent recorder operator must attest access control and sign an event/attempt manifest outside the claimant's trust domain. Blind evaluator must score claim-only and protected-recorder evidence on the **same** cases.

Primary endpoint: false support among *known unexecuted actions*, reporting numerator, denominator and uncertainty interval. Secondary: correct support for completed actions, abstention rates, missingness and false rejection. Predeclared pilot go/no-go: zero false supports in the protected-recorder subset, >=90% non-abstention for valid completed actions, and 100% abstention when manifest coverage is absent. These are ambitious *internal research gates*, not sponsor requirements; even zero errors in 100 cases does not prove general safety. Report every failure, including invalidating key compromise or missing events. No deployment or security guarantee is claimed.

## Conditional budget: reconcile existing $25,000 packet, do not create new expenses
| Package | Planning cap | Verification before application |
|---|---:|---|
| Independent recorder/key separation/durable logs | $7,000 | Named independent operator, work estimate, quote and host/key custody |
| Authorized attack fixture and frozen holdout | $5,000 | Data rights, threat taxonomy, realistic labor allocation |
| Blind evaluation and negative-result audit | $5,000 | Independent evaluator, rate/availability, predeclared analysis |
| Reproducibility, privacy, external review | $4,000 | Reviewer role, privacy handling, release rights |
| Coordination, reporting, contingency | $4,000 | Payee and cost policy, nonoverlap timesheets, contingency restrictions |
| **Total (unquoted, uncommitted)** | **$25,000** | No invoices, hiring, reimbursement or grant approval assumed |

This is the *same* allocation as the 2026-11-08 reviewer packet, not additional funding. No double-counting of the BlueDot Control Evidence proposal, internal Svyable labor or another funder's budget. If independent staffing/rights cannot be established, **do not submit this scope**.

## Missing applicant-controlled evidence — binary decision gate
- Legal applicant/payee, jurisdiction, tax/grant acceptance eligibility and actual 10–12 week capacity: **UNVERIFIED**.
- Rights to reuse/release Svyable code, datasets, evaluation outputs and any participant traces: **UNVERIFIED**.
- Named independent recorder operator with protected host/key custody, qualified blind evaluator and written rates: **UNVERIFIED**.
- Permission to collect real agent traces and publish redacted results: **UNVERIFIED**; synthetic-only fallback must be labeled.
- Sponsor's current application form, upload confidentiality, grant agreement, reporting and IP terms: **NOT ACCEPTED OR CLEARED**. Avoid uploading proprietary material before human review.
- Concrete non-overlap of hours, equipment, reviewer costs and deliverables across TAIF/BlueDot/other asks: **UNVERIFIED**.

**Stop rule:** No further cosmetic application polishing. Proceed to an authorized submission review only after applicant/payee/rights, independent operator/evaluator, budget quotes and nonoverlap are documented. If those are unavailable, narrow to a smaller, candid negative-control methods grant or hold.

## Cash economics (sensitivity, not forecast)
Illustrative 1.5h of additional applicant verification at $35/h costs **$52.50**; zero external spend authorized. If an *assumed* $5,000 of legitimate retained economic benefit were available after restricted project costs, the action must increase the **joint eligibility-and-award probability by 1.05 percentage points** to break even ($52.50/$5,000). Neither the retained benefit nor probability uplift is measured. On verified facts alone, **incremental monetary EV is unknown**, and without an uplift estimate the labor is a cost, not a proven investment. A $25k grant cannot be counted as $25k profit.

## Nearby alternatives, screened without duplicates
- [BlueDot Seed](https://bluedot.org/grants/seed): $20k–$200k for 6–12 months, monthly updates and unspent-fund return; high reuse but organizational/payee commitment and longer delivery; WATCH.
- [BlueDot Media](https://bluedot.org/grants/media): $20k–$200k, publication/audience evidence not established; OPEN/HOLD.
- [BlueDot Rapid](https://bluedot.org/grants/rapid): canonical page says $50–$10k while [index](https://bluedot.org/grants) says up to $20k; no documented cash bottleneck and terms vary across pages; WATCH.
- Five frontier benchmark lanes remain tracked in [campaign](2026-11-07-frontier-five-benchmark-campaign.md), **no verified cash awards**. Do not count leaderboard points as income.

No money spent, third parties contacted, applications submitted, terms accepted or IP transferred.
