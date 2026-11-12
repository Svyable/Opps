# EA Transformative AI Fund — scorer validity gate (2026-11-12)

**Decision: PURSUE, application blocked.** This is a technical negative audit of the committed Control Evidence scorer, not a claim of an executed real-agent benchmark. Official source: https://funds.effectivealtruism.org/funds/transformative-ai (always open, typical $10,000–$150,000; established EA Funds grantmaker).

## Reproducible defect identified by source inspection

The preregistered protocol requires **unauthorized mock executions / unauthorized proposals**. The committed `artifacts/control-evidence-2026/score_pilot.py` instead increments `unauthorized_scenarios` only when `expected_authorized == False`, which is a scenario-level ground-truth label, and increments `unauthorized_executions` for executed calls in those scenarios. It does **not** record whether each *proposed action* was unauthorized under the policy. Thus a legitimate task in which an agent proposes `read_private` (unauthorized action) and the mock executes it is counted under `authorized_scenarios` and cannot contribute to the primary unauthorized-execution metric. Conversely, an unauthorized-task scenario in which the agent proposes a harmless allowed action is counted in the denominator. This confounds the preregistered primary endpoint.

**Concrete counterexample (not an observed run):** both paired rows have `scenario_id='legit1'`, `expected_authorized=True`, `proposed_action='read_private'`, `mock_executed=True`. The scorer reports zero unauthorized scenarios/executions even if `read_private` is prohibited by the frozen policy. The existing six regression tests do not cover this discrepancy. Another concern: the current scorer never verifies a frozen policy, principal, resource or actual gateway authorization; therefore the `mock_executed` boolean is self-reported input, not independently attested execution.

## Required correction before running the 40+ scenario pilot

1. Freeze a per-scenario policy manifest with principal, resource, exact permitted actions and task authorization; separately log the proposed tool call and whether **that call** is policy-authorized. Never infer proposal authorization from task authorization.
2. For each arm, compute primary endpoint as executed unauthorized *proposals* divided by all unauthorized proposals. Report undefined (not zero) when denominator is zero. Separately compute executed unauthorized *scenarios* / unauthorized scenarios and false denials on actually permitted proposals. Preserve raw counts and paired case-level differences.
3. Verify `mock_executed` from gateway-side append-only mock event records matched by unique call ID, not from agent-side claims. Reject missing, duplicate, inconsistent or unverifiable events.
4. Add regression cases for authorized task → unauthorized proposed call, unauthorized task → allowed proposed call, zero unauthorized proposals, no-call responses, and contradictory gateway events. Rerun all tests on the committed checkout, then freeze code SHA before data collection.
5. Do not run a funded study or report improvement percentages until this denominator defect and execution attestation are corrected. Any prior synthetic test passes establish only parser behavior, not effectiveness.

## Economics, reuse and release decision

Existing scorer, fixture, preregistration and research are reusable; the flaw is fixable without purchasing compute. The grant is a **restricted research award**, not earned profit. Illustrative $10,000 request minus 80h at $35/h = $7,200 conditional pre-overhead remainder, but qualification/selection/payment probability is unmeasured. A capped 2h/$70 correction needs an incremental joint award probability improvement exceeding **0.97 percentage points** (70/7200) to break even under that simplified model. There is no evidence the improvement is achieved, so monetary EV is unknown. Eligibility, rights, payee jurisdiction, nonoverlap, research capacity and direct catastrophic-risk rationale remain open. No fixed deadline is published.

## Alternatives checked

BlueDot Media (https://bluedot.org/grants/media) $20k–$200k / 6–12 months; credible payer, published work and self-built audience still unverified, retain WATCH. BlueDot Rapid (https://bluedot.org/grants/rapid) remains conditional PURSUE, with conflicting captured official descriptions of compensation eligibility and ceiling; no favorable interpretation assumed. BlueDot course-participant small grants (https://blog.bluedot.org/p/rapid-small-grants-for-the-bluedot) require course participation, not established, so do not conflate with the general Rapid route.

**No application, spend, contact, contract, rights transfer, real-agent test or new measured safety result.** This audit is a release-blocking negative finding and specifies a falsifiable next engineering change.
