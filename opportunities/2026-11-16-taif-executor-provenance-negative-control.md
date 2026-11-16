# TAIF executor-provenance negative control — 2026-11-16

Status: **PURSUE / HOLD**. Official grantmaker: https://funds.effectivealtruism.org/funds/transformative-ai (rolling, typically $10k–$150k). Existing Control Evidence IP reuse high. This is a specific reviewer-facing negative result, not evidence of deployed safety.

## Reproduced failure of evidence provenance

Source pinned from GitHub connector on 2026-11-16:
- `artifacts/control-evidence-2026/receipt_audit.py` blob `e29471f5cfabd149115e0e220714dcefb91838a5`
- Newly committed negative test: `artifacts/control-evidence-2026/test_receipt_provenance_gap.py` (commit `31802c1a47cfd87ce18c19b9f5803058d60b5283`)

The validator accepts any nonempty `recorder` string; it does not authenticate the source of receipts. A fabricated receipt bearing `recorder='independent-executor'` passes and produces zero unauthorized executions. **A zero count is therefore not independently trustworthy.** This is an intentionally passing *negative control*, not a fixed vulnerability or a real-agent trial.

A local Python 3 unittest run against a manually reconstructed copy of the pinned auditor logic and the negative test yielded **1/1 pass**; exact command: `cd /tmp/ce-run && python3 -m unittest -v test_receipt_provenance_gap`. This does **not** establish an exact-byte checkout test or full repository suite. A clean clone still failed before tests with DNS `Could not resolve host: github.com` (git exit 128). Preserve this distinction.

## Release gate

Before grant submission or any safety-efficacy claim: collect executor-origin receipts outside the agent-controlled logging path, use a verifiable authenticated transport/signature or a trusted collection boundary, bind receipt to proposal/action/policy version, archive provenance metadata and failed trials, and perform a blinded comparison. Do not treat arbitrary recorder strings as independent attestations. Full pinned tests and real execution remain outstanding.

## Economics and decision

EA Funds is a credible established funder; published typical **restricted project grants** are $10k–$150k and applications are continuously open. Applicant/payee, eligible exclusive budget, grant terms, IP rights, selection odds and incremental retainable economic benefit remain unverified. No numerical probability uplift is supported by this negative test. Illustrative 0.5h × $35/h = $17.50 labor; zero external spend. Cash EV unknown, not asserted positive. Maintain existing 94-entry deduplicated registry (8 PURSUE, 34 WATCH, 52 REJECT; none OPEN/WON/LOST), including all five frontier benchmark lanes with unverified cash awards. Next decision: secure independently authenticated executor evidence before more TAIF application prose.

No application, outreach, paid compute, agreement or IP transfer.
