# BlueDot Rapid Grants — Control Evidence pilot, conditional application package
Prepared 2026-11-13. **PURSUE / NOT SUBMITTED.** This is a funder-facing draft with verification gates, not an assertion of eligibility or a grant request.

## Official rule verification (2026-11-13)
Primary: https://bluedot.org/grants/rapid
- **Current direct-page maximum: $20,000**, explicitly shown in headline, funding summary, and FAQ. This resolves the prior ledger's stale $10,000-vs-$20,000 discrepancy in favor of the current primary source; the April 14, 2026 announcement at https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants stated $10,000 at that time.
- No fixed deadline shown; application is presented as open, with a short plan/budget (~15 minutes). Do not infer a guaranteed decision time.
- Supports research time/living costs, projects, compute, tools, testing; looks for a worthwhile direction, evidence of progress, and **a clear role for funding**.
- BlueDot course/alumni/facilitator/active community participation improves prospects but is **not established for this applicant**.
- Published exclusion list includes India, China, Russia, Iran and other jurisdictions; actual payee country and sanctions eligibility **not verified**.
- Payment is a single lump sum **after claim and checks**; funds restricted to agreed purpose; material changes require prior written approval; short completion report due within 60 days after completion/end of grant period. Transfer/FX costs may reduce receipt. **No IP ownership or publication-license terms were confirmed from this page; obtain actual agreement before acceptance.**
- Payer credibility: BlueDot's April 14 report documents 77 awards totaling over $50,000, but neither selection odds nor payment for this applicant are established.

## Proposed project (not completed)
**Control Evidence: a reproducible authorization-gateway evaluation for AI-agent tool actions.**

Agents can propose tool actions outside their explicit permission policies. We propose a paired, preregistered evaluation comparing an instructions-only baseline against an independent authorization gate, measuring unauthorized executed actions and false denials. We will freeze at least 40 adversarial and legitimate scenarios, run an isolated no-network mock-tool environment with **real agent-generated proposals and independently captured execution events**, publish counts and denominators, and release reproducibility instructions and limitations. We will not claim that synthetic gateway tests establish deployed-agent safety.

**Existing reusable work:** `artifacts/control-evidence-2026/score_pilot.py`, `mock_gateway.py`, regression tests, and `opportunities/2026-11-11-ea-transformative-ai-control-evidence-preregistered-pilot.md`. Existing mock gateway generates synthetic events; it is **not** independently instrumented real-agent evidence. CI status and exact clean-checkout tests are unverified. No result or affiliation is invented.

## Specific cash bottleneck and smallest defensible budget
Funding would purchase dedicated research/engineering time to instrument independent execution traces, run the paired pilot, and produce a public reproducibility report. **Provisional minimum request: $2,800 for 80 hours at an illustrative $35/hour**, allocated:
- 20h / $700: independent tool-event instrumentation and threat-model review
- 24h / $840: paired scenario generation, execution, and trace collection
- 20h / $700: independent replay, adversarial tests, analysis and uncertainty
- 16h / $560: reproducibility package, write-up and reporting
- Total: **80h / $2,800**. No compute/API, travel, overhead or unallocated surplus assumed.

**HOLD:** $35/hour is an internal modeling rate, not a verified compensation entitlement or approved BlueDot expense. Applicant must establish real available hours, payee eligibility, permissible personal time/living cost treatment, no double funding with EA, and whether this work would occur absent grant. If any fail, revise amount or do not apply.

## Proposed milestones and falsification
1. Verified clean-checkout test results and independent event provenance, with commit SHA and tool versions.
2. Frozen paired scenario manifest and preregistered exclusions.
3. Actual agent-generated calls through no-network gateway; immutable event records; blinded/independent replay.
4. Public report with unauthorized-execution and false-denial rates, denominators, confidence/uncertainty, null outcomes, and failures.
Stop if event provenance cannot be separated from scorer assertions or if paired replay is irreproducible. Do not turn synthetic test passes into effectiveness claims.

## Release gates before any application
- [ ] Verify applicant identity, residence/payee country, sanctions status, and BlueDot-community relationship (if any).
- [ ] Verify 80 hours available, actual compensation/budget basis, eligible expenses, no EA overlap, and concrete funding counterfactual.
- [ ] Run committed scorer/gateway suites from clean checkout; capture test log and CI URL.
- [ ] Produce at least one independently recorded agent/tool trace before promising results; do not misstate synthetic data.
- [ ] Inspect application questions and any grant terms for publication, IP, reporting, repayment, tax, and disclosure restrictions.
- [ ] Applicant approves final truthful application; **no submission or acceptance without explicit approval**.

## Risk-adjusted decision (not an estimated win probability)
Payer credibility: credible published small-grant history. Deadline: rolling/no fixed close date verified. Qualification: plausible topic fit, **personal eligibility unverified**. Reuse: high; incremental proposal work: ~1h at $35; delivery 80h at $35 = $2,800. A $2,800 grant spent entirely on 80h of labor has **zero modeled surplus** before taxes/other costs; if labor is an actual compensable cash bottleneck, it can fund work, but cannot be counted as $2,800 profit *and* subtract the same labor cost inconsistently. Under a simplified cash-receipt model with $2,800 payable and $35 preparation cost, break-even joint qualification/award/payment probability is 1.25% **only if delivery labor is otherwise a nonincremental committed cost**. With all 80h incremental, monetary EV = $2,800 × p − $2,800 − $35, negative for all p ≤ 1; do not pursue on cash-profit logic alone. Real counterfactual and probability uplift unknown. **Time-box further work pending verified payee eligibility and labor counterfactual.**

No spend, outreach, application, contract, or IP transfer.

## 2026-11-13 live primary-source contradiction — release-blocking correction

**DO NOT RELY ON THE $20,000 CEILING OR AUTOMATIC STIPEND ELIGIBILITY ASSERTED ABOVE.** A fresh read of the direct official page https://bluedot.org/grants/rapid returned **“Typical grants up to $10k”** and FAQ **“Rapid Grants run from $50 to $10,000”**, while the official index https://bluedot.org/grants advertises **“Up to $20k”**. The direct page also states that **stipends and living expenses are not its usual scope** and require an unusually strong case. This conflicts with the earlier November 13 snapshot described above; website variants, caching, or revisions cannot be resolved without authoritative confirmation. For prudent budgeting, use **$10,000 as the direct-page ceiling, not a guaranteed cap**, and treat personal research-time compensation as **unconfirmed discretionary eligibility**. Official direct page: https://bluedot.org/grants/rapid ; official index: https://bluedot.org/grants ; historical April 14 announcement: https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants . No fixed deadline observed. Published payer history is credible, but not a payment promise.

**Application decision: HOLD.** Neither the 60h/$4,500 nor 80h/$2,800 overlapping alternative may be submitted as-is. Require payee-jurisdiction confirmation, one defensible actual hourly basis, explicit nonoverlap with EA, a verifiable cash bottleneck, and a contemporaneous direct-page/application screenshot or written official rule confirmation *before* asserting funding eligibility. No external contact is authorized. Earlier claims of a resolved ceiling discrepancy and generally allowed living expenses are superseded by this correction. No application or terms accepted.
