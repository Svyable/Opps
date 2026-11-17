# BlueDot Media — claim-to-source verification dossier (2026-11-17)

**Opportunity:** existing BlueDot Media WATCH entry. **Purpose:** make the November 17 editorial sample defensible to a technical editor without upgrading synthetic evidence into field reporting. This is a source inspection, not an executed regression or published reporting sample.

## Exact source audit

Read repository source via GitHub connector on 2026-11-17:

| Source | Git blob SHA | Observed behavior | Permissible editorial claim |
|---|---|---|---|
| `artifacts/control-evidence-2026/receipt_audit.py` | `e29471f5cfabd149115e0e220714dcefb91838a5` | `audit` requires proposal/receipt call and scenario IDs, Boolean authorization/execution, exact proposed-action equality, nonempty recorder string, and one receipt per proposal. It counts `executed and not authorized`. | A local auditor checks internal consistency and detects unauthorized actions **as represented by supplied receipts**. |
| `artifacts/control-evidence-2026/test_receipt_provenance_gap.py` | `9a938d00cff78064588227fdaa0f1bb68121cd0b` | Test constructs a denied `delete_file` proposal and a synthetic receipt with `executed=False` and `recorder='independent-executor'`, then expects a zero-unauthorized result. | The test encodes a forged-recorder-label negative control. **Source inspection alone does not prove the test passed in this run.** |

The auditor contains **no signature check, independent key validation, authenticated transport attestation, external executor observation or binding to actual filesystem side effects**. Therefore its `unauthorized_executed=0` output cannot establish that a tool did not run. This is a precise source-level limitation, not evidence that any production deployment was compromised.

## Editorial claim disposition

- **Keep:** A receipt with an arbitrary nonempty `recorder` string is accepted when the other schema fields agree. Source: auditor condition on `r['recorder']`.
- **Keep, qualify:** The auditor enforces proposed-action equality. Source: `r['proposed'] != expected[key]['proposed']` branch; does not independently attest what the executor performed.
- **Rewrite if necessary:** “Perfect audit log” is rhetorical; describe it as a *self-consistent supplied log* rather than an authenticated audit trail.
- **Do not claim:** Real-agent exploit, measured failure frequency, external replication, production safety efficacy, cryptographic forgery, or independent validation.
- **Do not call this published journalism:** No independent interview, external fact-check, public audience evidence or published URL was established.

## Reviewer preflight: bounded next experiment

1. In a clean checkout, record `git rev-parse HEAD`, Python version and exact command `python3 -m unittest discover -s artifacts/control-evidence-2026 -p 'test_receipt*.py' -v`, preserving full stdout/stderr and exit status.
2. Introduce a **trusted recorder boundary** outside the agent-controlled receipt JSON (e.g., executor-held signing key with pinned public key and key-rotation/replay policy). A new `recorder_verified` string field is **not** authentication.
3. Repeat forged-recorder tests and capture an independently observable, harmless side effect. State explicitly whether the trusted observer can itself be compromised.
4. Have an external technical editor check the source-to-claim map and disclose Svyable authorship. No third party has been contacted.

## Official payer rules and commercial gate

[BlueDot Media](https://bluedot.org/grants/media) advertises **$20,000–$200,000**, **6–12 months**, roughly **four-week** decisions, and applications at any time per [grant index](https://bluedot.org/grants). It explicitly permits living costs and part-time work, but expects demonstrated craft, accuracy, existing self-built audience, monthly updates and a final report. It requires return of unspent funds if work stops; grants may be taxable; listed jurisdictions and sanctions are excluded. Editorial independence is retained. Applicant-specific country, rights, actual audience and terms remain unverified.

**Risk-adjusted decision: WATCH, not submission-ready.** Existing Control Evidence code and Desk/Shelf research give high reuse. Source verification costs roughly 1 hour ($35 at an illustrative internal rate); the next clean-checkout + editorial preflight is capped at 2 hours ($70), no external spend. Incremental award probability cannot be measured. At a hypothetical $5,000 **net** incremental retained benefit, a 1.4% joint success probability would break even on the *next* $70 alone, before any further pursuit or delivery cost. No defensible success probability or net benefit is established: **monetary EV unknown**, not presumed positive. Anthropic Residency (Nov 22, $350k–$500k annualized prorated) is WATCH pending applicant/legal gates; EA Transformative AI Fund ($10k–$150k typical, rolling) is PURSUE/HOLD pending authenticated execution and exclusive budget.

**No application, contact, contract, spending or IP transfer.** This dossier does not alter the 94-entry deduplicated registry (8 PURSUE / 34 WATCH / 52 REJECT; zero OPEN/WON/LOST); five unpriced frontier benchmark lanes remain retained.
