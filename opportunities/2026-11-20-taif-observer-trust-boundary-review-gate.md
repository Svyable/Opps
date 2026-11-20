# TAIF Control Evidence — reviewer-facing trust-boundary decision (2026-11-20)

**Opportunity:** existing Transformative AI Fund PURSUE/HOLD; conditional $25,000 request. **Disposition:** do not submit an independent-action-attestation claim.

## Exact source inspected
- [observer_boundary.py](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/seed-recorder-envelope/observer_boundary.py), Git blob `6e968f8c74028ccf68a53c6a3f716b1833089743`
- [test_observer_boundary.py](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/seed-recorder-envelope/test_observer_boundary.py), Git blob `1f20427f141929c44cd3e589386e435d501ec9a0`

## Verified by source inspection (not runtime execution)
1. The parent creates the HMAC key and passes it to the observer child; the parent also controls the expected payload, action identifier and target path. This is not independently protected key custody.
2. The parent checks target absence once; the optional injection branch writes expected bytes after that check and before observation, even with `omit=True`.
3. The observer signs a report of *file contents*, not executor process identity, execution trace, or causal ownership of the write.
4. Both authorized write and attacker-supplied matching bytes return `OBSERVED_ONLY`; the status deliberately avoids claiming an action was verified.
5. The six test functions encode these distinctions, but the exact GitHub revision was **not executed in this run**. The local runtime could not resolve github.com; no CI/test success is inferred.

## Falsifiable pilot gate before submission
- Run `python -m unittest discover -s artifacts/control-evidence-2026/seed-recorder-envelope -p 'test_observer_boundary.py' -v` on the exact pinned commit; preserve commit SHA, Python version, stdout/stderr and exit status.
- Separate executor and observer into distinct security principals; prove the executor cannot read the observer signing key, overwrite the observation channel, or mint a trusted action event.
- Record observer-issued unpredictable nonce, pre-action state, authorized executor identity and independently witnessed action event; test replay, preexisting target, post-precheck injection, substitution, observer crash and key exposure.
- **Success criterion:** authorized write produces a separately evidenced execution event; matching bytes injected without authorized execution never produce that event. Signed file-state observations may still be reported as `OBSERVED_ONLY`.
- **Stop condition:** if separation and event attribution cannot be demonstrated, pitch the project as a *measurement of false-attribution failure modes* and publish negative controls, not as an attestation product.

## Funding case and eligibility
Official [TAIF](https://funds.effectivealtruism.org/funds/transformative-ai): rolling; typical $10k–$150k; early-stage advanced-AI catastrophic-risk research/demonstrations. [EA Funds](https://funds.effectivealtruism.org/) reports $100M+ historical grants. Applicant legal identity, geography, IP permissions, exclusive budget, credible catastrophic-risk causal pathway, and independent evaluation partner remain **unverified**. No claim that the funder endorsed this project.

A conservative next gate is **two hours** of no-spend exact-commit test and threat-model work (illustrative labor $70 at $35/hour). With *hypothetical* $5,000 retained benefit, break-even incremental joint qualification/award probability is 1.4 percentage points. There is no empirical basis for assigning that uplift, so monetary EV remains **unknown**, not positive. $25,000 restricted grant face value is not profit.

## Alternative comparison
- [BlueDot Rapid](https://bluedot.org/grants/rapid): official program page $50–$10k, fast rolling decisions, but funding must address a specific monetary bottleneck; none established for a zero-spend local test. BlueDot grants index advertises up to $20k; use lower program-page cap until reconciled.
- [BlueDot Seed](https://bluedot.org/grants/seed): $20k–$200k for 6–12 months, high code reuse but more project-delivery work and similar risk-fit/eligibility uncertainty.
- [BlueDot Media](https://bluedot.org/grants/media): $20k–$200k, high research reuse but published bylines and owned audience remain unverified.
- Frontier-five benchmark lanes: cash prizes unverified; do not convert scores to dollar value.

No application, registration, third-party contact, spending, contract, terms acceptance or IP transfer occurred.
