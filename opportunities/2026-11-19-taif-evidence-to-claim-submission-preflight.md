# TAIF submission preflight: evidence-to-claim crosswalk (2026-11-19)

**Status:** internal, unsubmitted; existing Transformative AI Fund opportunity **PURSUE / HOLD**. This is a reviewer-facing evidence index for the existing conditional $25,000 pilot, not a claim of grant eligibility or safety impact.

## Official criteria and funding route (checked 2026-11-19)

- [Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai): accepts applications continuously, typically $10k–$150k, rarely over $300k. Supports individuals and new projects, with primary focus on reducing catastrophic risk from advanced AI. Demonstrations and technical research can qualify, but generic audit tooling alone does not establish impact.
- [Apply for funding](https://funds.effectivealtruism.org/apply-for-funding): official application entry; review live form before submission. No fixed closing date claimed.
- [EA Funds](https://funds.effectivealtruism.org/): reports $100M+ historical grants, supporting payer credibility, not probability of selection.

## Claims that can and cannot be made

| Application claim | Existing evidence | Allowed wording | Prohibited inference |
|---|---|---|---|
| Signed envelopes can reject invalid or mismatched records | [recorder.py](../artifacts/control-evidence-2026/seed-recorder-envelope/recorder.py), [test_recorder.py](../artifacts/control-evidence-2026/seed-recorder-envelope/test_recorder.py) | Isolated synthetic authentication tests have been recorded | An HMAC proves an action occurred |
| Single-use receipt replay can be rejected under a protected state-store assumption | [replay_guard.py](../artifacts/control-evidence-2026/seed-recorder-envelope/replay_guard.py), [test_replay_guard.py](../artifacts/control-evidence-2026/seed-recorder-envelope/test_replay_guard.py) | Stateful verifier prototype and six previously reported isolated tests | Stateless callers are replay-safe; database cannot be tampered with |
| Distinct executor and observer processes can be demonstrated | [observer_boundary.py](../artifacts/control-evidence-2026/seed-recorder-envelope/observer_boundary.py) | Two-process proof of concept, shared host and parent-controlled key | Independent attestation or adversarial isolation |
| Existing file can be falsely attributed to an absent execution | [negative control](../artifacts/control-evidence-2026/seed-recorder-envelope/test_preexisting_file_negative_control.py) | One previously reported negative control exposes preexisting-state attribution failure | The defect is fully fixed |
| Fresh-target prestate gate can reject preexisting matching contents | [fresh_action_gate.py](../artifacts/control-evidence-2026/seed-recorder-envelope/fresh_action_gate.py), [five tests](../artifacts/control-evidence-2026/seed-recorder-envelope/test_fresh_action_gate.py) | Five previously reported isolated tests; NOT integrated into two-process observer | Trusted independent observation or race resistance |

**Evidence quality:** links point to repository files; test counts are historical ledger assertions, not tests rerun in this preparation. Before sending any proposal, fetch exact revision, run all relevant tests together, record Python version/commands/exit codes, and attach immutable commit links.

## Six-week pilot: falsifiable milestones

1. **Week 1:** document threat model and exact trust boundary, including malicious executor, key holder, state store, and shared-host attacker. Freeze test harness revision.
2. **Weeks 2–3:** integrate observer-controlled nonce/path and prestate check with a distinct observer process and protected evidence store. Explicitly state residual privileges.
3. **Week 4:** run pre-registered negative controls: preexisting target, absent executor, forged record, replay, substituted contents, observer crash, race between precheck and execution, and compromised signing key.
4. **Week 5:** reproduce on clean environment with pinned dependencies; publish raw outcomes, including failures, if rights permit.
5. **Week 6:** solicit **only after approval** an independent evaluator's assessment of whether this changes a real control/audit decision; publish limits and a go/no-go recommendation.

**Success criterion:** authenticated records must be distinguishable from observed execution under the declared threat model; false attribution and UNKNOWN cases must be measured rather than hidden. A failed experiment is a legitimate result. **Impact criterion:** show a concrete advanced-agent evaluation decision that would differ using the independent evidence; without that, do not claim reduced catastrophic risk.

## Submission blockers (not assumptions)

- Applicant identity, location/sanctions eligibility, tax/payee status and six-week availability not verified.
- Rights to use and publicly release relevant Svyable code, datasets, and dependencies not verified.
- $25k exclusive cost allocation not validated; [conditional budget](2026-11-18-taif-conditional-independent-observation-pilot.md) is not a quote, salary agreement or authorization. BlueDot funding cannot double-pay the same work.
- Current process/key separation is not sufficient to claim independent action provenance. Need integrated demonstration and exact-commit rerun.
- External evaluator demand and causal link to advanced-AI catastrophic-risk reduction unproven.
- Grant agreement, disclosure, reporting, tax and IP terms must be read before acceptance; no grant revenue assumed as personal profit.

## Economics and decision

Existing Control Evidence reuse: **high**; incremental technical build estimated 8–24 hours (planning estimate), application preflight 2 hours. At illustrative $35/hour, 2-hour preflight costs $70 and full build $280–$840 in internal labor, excluding legal, opportunity and infrastructure costs. Request: **$25,000 conditional restricted project support**, not expected profit. If net retained economic benefit after all delivery costs were hypothetically $5,000, the 2-hour preflight needs **1.4%** incremental joint success probability to break even; this is a threshold, **not** an estimated uplift. Neither qualification probability nor selection probability is measured, so monetary EV is **unknown**. Do not claim positive EV based on grant face value.

**Decision:** retain PURSUE / HOLD and cap next action at an exact-commit integrated falsification run or applicant-rights verification; stop proposal polishing until a material gate clears. Anthropic Residency remains WATCH pending independently evidenced applicant leadership before its November 22, 2026 cutoff. Five frontier benchmark lanes remain active but unpriced; no cash claim.

No submission, third-party contact, spend, contract, registration, or IP transfer authorized or performed.
