# Win accelerator: payability and reproducibility stop-loss — 2026-11-17

## Decision (one opportunity): EA Transformative AI Fund — PURSUE / HOLD

Selected for its existing Control Evidence IP and rolling intake, **not** because award probability is known. The immediate decision is **do not spend another engineering sprint or submit** until a verifiable executor-origin trace and nonoverlapping eligible cost exist. This is a negative commercial gate, not a grant application or completed validation.

Official fund: https://funds.effectivealtruism.org/funds/transformative-ai . Prior ledger reports typical restricted $10k–$150k; confirm current award guidance before any application. Existing auditor: [receipt_audit.py](../artifacts/control-evidence-2026/receipt_audit.py), negative control: [test_receipt_provenance_gap.py](../artifacts/control-evidence-2026/test_receipt_provenance_gap.py).

## New verification attempted

Read current repository files using authenticated GitHub access (auditor blob e29471f5cfabd149115e0e220714dcefb91838a5, test blob 7a76843454962d8ddb41f186647f2da8332792fd, negative-control blob 9a938d00cff78064588227fdaa0f1bb68121cd0b). Attempted to fetch exact raw files into a clean runtime and run `python -m unittest discover -v`. Fetch failed with `curl: (6) Could not resolve host: raw.githubusercontent.com`; **zero tests executed**. This does not demonstrate a regression or a pass. Previous reconstructed-code results are not exact-source CI evidence.

The source inspection confirms that `recorder` is a nonempty user-supplied string, not a cryptographically authenticated executor-origin attestation. Existing negative control explicitly shows that forged `independent-executor` attribution is accepted. Thus a reported zero unauthorized-execution count is an internal consistency measure, not independent observation.

## Release criteria

1. Run exact-source `python -m unittest discover -v` in a network-enabled checkout and preserve commit SHA, Python version, command, exit code and unedited output.
2. Add an executor-origin boundary in which the executor, rather than the evaluated agent, controls receipt issuance and the verifier independently authenticates the origin. A signature or HMAC whose secret is available to the evaluated agent **does not qualify**.
3. Capture at least one actual allowed and one denied action with independent side-effect observation and negative controls for missing, forged, duplicated, action-swapped and replayed receipts.
4. Establish legal payee, IP permissions and a cost register excluding BlueDot overlap; do not treat gross restricted grant dollars as founder profit.

## Risk-adjusted economics

Payer: identifiable grantmaker; eligibility/payee/rights and award odds unverified. Reuse: high (existing auditor, protocols and Desk research). Deadline: rolling per prior source audit, reconfirm before submission. Costs: proposed next 2h × illustrative $35/h = $70, zero infrastructure spend. Grant face value $10k–$150k is **not** retainable net benefit. If net incremental benefit were hypothetically $5,000, the joint eligibility × award × payment probability would need to exceed 1.4% merely to cover $70; neither that benefit nor probability is evidenced. Incremental probability change: **not estimable**. Monetary EV: **unknown**, no positive assignment. No reason to commission an additional sprint before the evidence boundary is available.

## Other live options / deduplication

- Anthropic Residency WATCH, official https://alignment.anthropic.com/2026/anthropic-residency/ : applications close **2026-11-22**, US compensation $350k–$500k annualized and prorated, 6 weeks–6 months. Personal senior leadership, full-time availability, work eligibility, reference consent and application-stage legal acknowledgement remain applicant-controlled and unverified; no autonomous application.
- BlueDot Media WATCH, https://bluedot.org/grants/media : prior official review $20k–$200k, rolling, 6–12 months. Existing journalism draft is unpublished; self-built audience and independently verified reporting evidence absent.
- ECDSA.fail and the other four frontier lanes remain active as **unpriced research**, not presumed cash prizes. ECDSA official harness https://github.com/Layr-Labs/ecdsafail-challenge/blob/main/README.md requires 9,024-shot correctness, ancilla/phase/reverse checks and allows changes only in `src/point_add/`. The user-reported Dec 31 horizon is not independently confirmed. No paid-compute, CLI submission or benchmark score claimed.

**Ledger baseline unchanged**: 94 unique, 8 PURSUE / 34 WATCH / 52 REJECT, zero OPEN/WON/LOST; all five benchmark lanes preserved. No application, outreach, money, contract or IP transfer.
