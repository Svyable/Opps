# Transformative AI Fund — durable replay gate, 2026-11-08

## Commercial decision

**PURSUE, bounded; not submission-ready.** Official [EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) accepts applications continuously, typically awarding $10k–$150k; Svyable's existing Control Evidence request is **$25,000 restricted pilot funding**, not personal profit. Payer: established EA Funds grantmaker. Applicant eligibility, rights to source data, a protected independent recorder, causal evaluation and nonoverlap with other grants remain unverified. The grant is not awarded.

Other current options screened: [BlueDot Media Grants](https://bluedot.org/grants/media), $20k–$200k for 6–12 months, no fixed deadline, WATCH because genuine audience ownership/analytics unavailable; [SOA XAI regulatory RFP](https://www.soa.org/research/opportunities/2026/explainable-ai-reg-compliance/), closes 2026-11-13, REJECT current autonomous submission because it prohibits AI-written proposals and actuarial domain evidence is missing; [SOA AI policyholder behavior RFP](https://www.soa.org/research/opportunities/2026/policyholder-behavior-ai-era/), same deadline and barriers. SOA's historical $25k–$50k contracted-project range is not an advertised fee. [OpenAI Safety Fellowship](https://alignment.openai.com/safety-fellowship) closed May 3, 2026; [Foresight Nodes](https://viamu.app/opportunities/ai-science-safety-nodes) closed Oct 31, 2026. No new opportunity ID added.

## One opportunity materially advanced

A real replay-integrity gap remained after prior caller-owned in-memory set fix: restart and separate worker processes could replay the same signed receipt. Added **SQLiteNonceRegistry** using a durable SQLite file with a PRIMARY KEY unique nonce constraint and `INSERT OR IGNORE`, which atomically admits a nonce at most once across processes sharing that database. Integrated it into the signed-receipt verification path *after* HMAC and scope checks, and permitted it in the claim decision API. Added six test definitions: restart replay, two connections, bad signature must not consume, no in-memory-only store, invalid nonce, duplicate coverage. CI workflow updated to run old and new suites.

Code: [durable_nonces.py](../artifacts/control-evidence-2026/durable_nonces.py), [receipt_boundary.py](../artifacts/control-evidence-2026/receipt_boundary.py), [verified_claim.py](../artifacts/control-evidence-2026/verified_claim.py), [test_durable_nonces.py](../artifacts/control-evidence-2026/test_durable_nonces.py), [receipt CI](../.github/workflows/control-evidence-receipts.yml).

**Verification boundary:** All five changes were committed through GitHub connector. The local runtime could not resolve `raw.githubusercontent.com`; no successful test run or Actions job log was verified. The six tests are defined, **not reported as passing**. A SQLite UNIQUE constraint is atomic when all writers use the same trusted durable file, but it does not guarantee shared storage across distributed hosts, availability under disk failure, key separation, provenance, atomic coverage+action decision semantics, or authenticated recorder completeness. Existing set-based fallback remains for synthetic tests and is not production durable.

## Expected-value gate

Use `EV = $25,000 × P(qualified) × P(award|qualified) − labor − infrastructure − rights/opportunity cost` for *restricted project funds*, not net personal income. No credible award-probability improvement is measured. Estimated incremental 1h at illustrative $35/h = $35; standalone cash EV **−$35** without demonstrable probability uplift or reusable value. Break-even on the full grant face value is 0.14 percentage points joint probability, higher on actual founder surplus. No paid infrastructure authorized.

## Stop-loss / next action

Read GitHub Actions execution and raw logs for the new durable-nonce tests. Then independently verify recorder trust and signed coverage; no additional synthetic hardening until a failing test or third-party evidence proves it useful. No application, spend, contact, binding terms or IP transfer occurred.
