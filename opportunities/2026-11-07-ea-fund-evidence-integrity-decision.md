# EA Transformative AI Fund — evidence integrity and submission decision (2026-11-07)

**Decision: conditional PURSUE, no application authorized.** Official program: https://funds.effectivealtruism.org/funds/transformative-ai (checked 2026-11-07). Applications always open; typical grants $10,000–$150,000; focus on early-stage work reducing catastrophic risks from advanced AI. The existing $25,000 Control Evidence request is a proposed restricted project budget, not guaranteed revenue. EA Funds publicly reports $100M+ grants across all funds (https://funds.effectivealtruism.org/); this is payer credibility, not odds for this proposal.

## Verified source-level result (not a runtime benchmark)

Inspected `artifacts/control-evidence-2026/contract_smoke.py`, `local_tool_receipt_pilot.py`, and `rapid_grant_baseline.py` through GitHub source reads on 2026-11-07. In `decide(case)`, event eligibility depends on the input-controlled string `e["writer"] == "independent"`; complete coverage depends on input-controlled `coverage_writer == "independent"`. No signature, MAC, trust-root identity, nonce, or external receipt verification is performed in that evaluator. The existing baseline includes four attack-labelled cases expected to be falsely supported (fabricated, replay, writer spoof, coverage spoof). Those are **expected fixture outcomes**, not independently measured run counts, attack prevalence, or successful mitigation.

A local clone-and-run attempt on 2026-11-07 failed before execution: `Could not resolve host: github.com`. Therefore neither the 19-fixture contract test nor ten-case baseline was independently executed in this run. Do not cite CI or runtime success without a retrievable run ID and raw output.

## Reviewer-facing minimum evidence gate

1. Obtain a clean GitHub Actions run ID, commit SHA, test exit codes, and downloadable raw JSON artifact for the existing deterministic baseline. Label its attack cases as constructed, public, nonblind controls.
2. Implement a separately trusted receipt verifier with a protected secret or signature verification key, canonical binding of scope/action/arguments, replay prevention, and independently attested coverage. Test wrong-key, replay, tampered-arguments, missing-receipt, and agent-controlled-label attacks. A same-process secret or agent-controlled signing key does **not** establish independent provenance.
3. Run a predeclared, independently authored holdout; publish denominators and all abstentions. Avoid extrapolation to deployed-agent risk or catastrophic-risk reduction without further evidence.
4. Verify recipient/payee, IP and data rights, research hours, nonoverlapping budgets, and the causal link between evidence integrity and advanced-AI catastrophic-risk reduction before application.

## Economics and stop-loss

Official fund typical award range $10k–$150k; proposed request $25k. Existing subjective prospective **economic** EV +$144.50 (not grant face-value EV), unchanged; no measured selection probability improvement. Illustrative incremental action: a 2-hour engineering test/receipt preflight at $35/hour costs $70. To justify that step on a $25,000 face-value basis would require at least +0.28 percentage points in *joint* award probability; on the narrower conditional economic benefit, the required uplift is larger. This is a break-even sensitivity, **not** a forecast of uplift. New verified-source review here has no measured uplift. Reuse: high for existing Python evaluator, subprocess probe, constructed cases and CI; low for authenticated independent provenance, which does not yet exist. Payer is established; eligibility and grant agreement terms remain applicant-specific and unverified.

**Next decision:** do not spend more time on prose or submit. Prioritize an actual CI run plus authenticated-provenance negative controls only if a feasible trusted recording boundary can be established. If not, leave the fund conditional PURSUE and suspend application work. No contact, expenditure, submission, or agreement.
