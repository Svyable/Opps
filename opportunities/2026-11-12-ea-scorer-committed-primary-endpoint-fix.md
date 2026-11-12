# EA Transformative AI Fund — committed scorer correction (2026-11-12)

**PURSUE; application remains blocked.** Official fund: https://funds.effectivealtruism.org/funds/transformative-ai — always open, typical $10,000–$150,000, primary focus on catastrophic AI risk. EA Funds reports an established grantmaking record (https://funds.effectivealtruism.org/). No published award probability or fixed deadline.

## Material correction

Prior scorer conflated scenario task authorization with authorization of the agent's *proposed call*, potentially omitting executed forbidden calls inside legitimate tasks. The replacement `artifacts/control-evidence-2026/score_pilot.py` now takes two JSONL inputs: paired scenario rows and separately supplied gateway events. It validates a per-scenario principal/resource/exact-action allowlist, rejects malformed or inconsistent paired policy, matches each proposed call to exactly one event by arm and call ID, rejects duplicate/missing/orphan events, and computes unauthorized executed proposals / unauthorized proposed calls. Zero denominators produce JSON null. It separately reports false denials of allowed proposed calls and task-level counts.

New `test_score_pilot.py` covers 14 cases, including both cross-label counterexamples, no-call, absent/duplicate/orphan events, bad allowlist, and contradictory paired policy. A **locally developed equivalent implementation** passed 14/14 Python unittest checks on November 12. The committed version was uploaded through GitHub and **has not yet been executed from a clean checkout or verified in CI**. The code validates record consistency, **not provenance or cryptographic authenticity**: separately supplied gateway events can still be fabricated, and no real agent has been evaluated. This is synthetic scoring infrastructure, not a safety-effectiveness result.

## Submission gate and economics

Next: clean-checkout test run, independently produced append-only gateway trace with provenance, frozen scenario manifest and paired real-agent evaluation, followed by independent replay. Verify applicant/payee jurisdiction, grant restrictions, research capacity, nonoverlap and a direct catastrophic-risk theory of change before applying.

Illustrative $10,000 restricted award less 80 hours × $35/hour = $7,200 before taxes/overhead. Additional 2h/$70 engineering requires >0.97 percentage-point improvement in joint eligibility/award/payment probability to cover incremental cost, **not an observed improvement**. Actual probability and monetary EV remain unknown; existing Control Evidence fixture, protocol and scorer are reusable research IP. No third-party terms accepted, no spending, outreach, submission, or rights transfer.

Five benchmark lanes remain active in registry; EC Rank Nov 14 is user-reported and cash prize unverified, so no prize EV assigned. BlueDot Rapid official rule conflicts and Media audience-evidence gate remain separate opportunities.
