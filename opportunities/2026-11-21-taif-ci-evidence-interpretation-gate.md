# TAIF Control Evidence — exact-source CI verification and submission gate (2026-11-21 UTC)

## What was checked
Read the current default-branch GitHub blobs through the GitHub connector:
- `observer_boundary.py` blob `6e968f8c74028ccf68a53c6a3f716b1833089743`
- `test_observer_boundary.py` blob `1f20427f141929c44cd3e589386e435d501ec9a0`
- `.github/workflows/control-evidence-observer.yml` blob `ce8a7681299cb73a0c460573b8a508d250c48bf9`

The workflow declares path-filtered push and PR triggers, manual dispatch, Python 3.11 and 3.13, `py_compile`, and six `unittest` assertions against checked-out source. GitHub connector `fetch_commit_workflow_runs` for workflow commit `f5fb99ac71f395e4cce16f274f026e292fa3a4d1` returned an empty array; **this endpoint filters to PR-triggered runs, so it cannot establish that push-triggered CI did or did not run.** No passing CI run, job log, or exact-commit test execution was verified in this check.

## Evidence boundary
A legitimate executor writes expected bytes; a separate observer signs a file-content report with an HMAC key provided by the parent. The parent also selects the expected action ID and controls the key. The injected-file negative control deliberately writes matching bytes after the prestate check while omitting the executor. Both this negative control and a legitimate write return `OBSERVED_ONLY`. This is appropriate: it proves the current design cannot distinguish action provenance. HMAC authenticity for a parent-supplied key is not independent action attestation.

## Funding application claim, defensible today
“We built a reproducible negative-control prototype that distinguishes file-state observation from independently verified agent action. Its adversarial injection case demonstrates why matching output bytes alone cannot establish that an authorized executor ran. We propose to study independently protected event capture, correlation and adversarial false-attribution rates.” Do **not** claim deployed attestation, a measured false-positive rate across agents, a reduction in catastrophic risk, or passing exact-commit CI.

## Concrete next gate
1. Inspect the GitHub Actions tab for the workflow's push run and both matrix jobs, or dispatch it with explicit authorization if needed; save run URL, exact SHA, logs, and job conclusions.
2. Require both Python versions to pass six tests and syntax checks on the same commit; distinguish expected negative-control PASS from a security fix.
3. Before submission, verify applicant identity/jurisdiction, right to reuse Svyable code, an exclusive itemized $25,000 budget, and an evaluator-relevant causal path to advanced-AI-risk reduction.
4. If no independent execution principal and protected signing-key custody can be demonstrated, pitch a falsification/evaluation research pilot, not an attestation product.

## Commercial decision
Existing opportunity: [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai), rolling, typically $10k–$150k, conditional $25k request. Payer: established EA Funds program. Qualification/selection odds unknown; high reuse of Svyable Control Evidence code. Remaining CI review estimated 0.5–1h, illustrative $35/h = $17.50–$35, zero external spend. At hypothetical $5,000 *retained* value, incremental award probability must rise 0.35–0.70 percentage points to cover labor; no evidence establishes such a rise. Actual monetary EV unknown. Grants have conditions and may be taxable; no agreement accepted.

Alternatives checked: [BlueDot Seed](https://bluedot.org/grants/seed) $20k–$200k, rolling, 6–12 months, founder payee/for-profit scrutiny and return of unspent funds; [BlueDot Rapid](https://bluedot.org/grants/rapid) current canonical page up to $10k versus [grants index](https://bluedot.org/grants) up to $20k, rolling, specific cash bottleneck unverified; [BlueDot Media](https://website-production.k8s.bluedot.org/grants/media) $20k–$200k, rolling, published work and self-built audience unverified. All are already tracked: **no duplicate opportunity added**. Five frontier benchmark lanes retained, cash prize unverified.

No submission, outreach, spend, contract, acceptance of terms or IP transfer.
