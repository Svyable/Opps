# TAIF — exact-byte receipt auditor regression verification (2026-11-17)

**Opportunity:** existing EA Transformative AI Fund (PURSUE / HOLD). **Purpose:** remove the previous DNS-blocked test-execution uncertainty without overstating independent agent evidence.

## Source provenance and reproducibility

Fetched these three files from Svyable/Opps default branch through authenticated GitHub connector, copied their UTF-8 contents into a fresh local directory, and **verified their computed Git blob SHA-1 hashes matched the GitHub-returned blob identifiers** before running tests:

| File | Git blob SHA-1 (local equals remote) |
|---|---|
| `artifacts/control-evidence-2026/receipt_audit.py` | `e29471f5cfabd149115e0e220714dcefb91838a5` |
| `artifacts/control-evidence-2026/test_receipt_audit.py` | `7a76843454962d8ddb41f186647f2da8332792fd` |
| `artifacts/control-evidence-2026/test_receipt_provenance_gap.py` | `9a938d00cff78064588227fdaa0f1bb68121cd0b` |

Command from the local directory containing these exact three files: `python -m unittest discover -p 'test_receipt*.py' -v`.

**Result: 12 tests run, 12 passed, exit 0, 0.001s**. Eleven receipt-auditor cases passed (including action substitution, missing/duplicate/orphan receipts, Boolean and policy checks); the twelfth passed because the auditor **accepted a self-asserted forged recorder label**. Thus the passing negative control documents a live provenance weakness, not proof of a safe executor. The tests are a byte-matched **three-file isolated run**, not the complete repository suite, CI, a trusted executor integration test, or independent field evidence. No Git clone was required.

## Official funding criteria, costs and decision

[EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) confirms continuous intake, typical $10k–$150k grants (rarely above $300k), early-stage transformative AI risk work, and support for individuals/new projects. [EA Funds](https://funds.effectivealtruism.org/) reports over $100M in historical grants; this establishes institutional payer activity, not probability of this proposal winning. No fixed deadline.

Existing Control Evidence code and this reproducible regression evidence are reusable at low marginal cash cost. However, **verified independent executor evidence = absent; nonoverlapping allowable project budget = unverified; applicant/payee rights and jurisdiction = unverified**. Do not represent the 12 passing tests as demonstrating risk reduction in real agents. The next technical step is an executor-controlled authenticated receipt boundary plus harmless side-effect observation, not another editorial rewrite.

Illustrative 1-hour verification labor at $35/hour = $35, no paid compute. Illustrative net retained benefit $5,000 would require >0.7% joint qualification/selection/payment probability to cover that $35 alone, ignoring delivery and later pursuit costs. Actual success probability, marginal probability improvement and monetary EV are **unknown**. A restricted grant is not unrestricted earnings. **Decision: PURSUE / HOLD** pending authentic provenance and exclusive cost documentation.

Comparison: [BlueDot Media](https://bluedot.org/grants/media) $20k–$200k, rolling, 6–12 months, high reuse of Desk/Shelf and Control Evidence reporting, but self-built audience evidence absent and grant reporting/return of unspent funds required (WATCH). Anthropic Residency November 22 $350k–$500k annualized prorated, but personal eligibility, full-time availability and arbitration acceptance remain unverified (WATCH urgent). Both are credible identifiable payers; no positive EV asserted.

No application, registration, outreach, spend, contract, arbitration acknowledgement or IP transfer.
