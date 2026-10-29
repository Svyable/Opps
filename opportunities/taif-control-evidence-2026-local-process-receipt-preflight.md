# Control Evidence — real local tool-process receipt probe and funding gate

**2026-10-29 · EA Funds Transformative AI Fund · $25,000 proposed / 10 weeks · PURSUE · not submitted.**

## Why this is material

The existing 19-case contract and 67 regression tests used hand-constructed synthetic records. They established the verdict grammar but did not exercise a real OS-level action. This annex adds a **separate Python subprocess performing an actual local file write**, while a supervisor process observes the return code and hashes the file bytes. The agent-like narrative is an untrusted field and cannot affect the decision. This is a small step from fabricated event dictionaries toward instrumented tool-side records, not a model evaluation.

[Executable probe](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py) · [10 new tests](../artifacts/control-evidence-2026/test_local_tool_receipt_pilot.py) · [existing three-verdict contract](../artifacts/control-evidence-2026/contract_smoke.py).

## Four public, reproducible modes

| Mode | Real worker action / observation | Contract outcome |
|---|---|---|
| success | Separate worker writes exact bytes; supervisor sees exit 0 and matching SHA-256 | supported |
| fail | Worker intentionally exits 7 without writing | refuted |
| tamper | Worker writes, then file bytes are changed before observation | insufficient_evidence |
| missing | Worker writes, but receipt is intentionally withheld | insufficient_evidence |

This is **four demonstration conditions, not four independently sampled agent cases**. The worker is a deterministic Python subprocess, not an AI agent. The supervisor is separate from the worker but is not a trusted independent recorder. The `writer: independent` and `coverage_writer: independent` strings satisfy the existing contract schema; they are **not authenticated attestations**. The digest binds local bytes but cannot establish source identity, nonrepudiation, clock integrity or completeness outside this controlled process.

Run locally using Python 3.10+ standard library:

```bash
python artifacts/control-evidence-2026/test_local_tool_receipt_pilot.py -v
python artifacts/control-evidence-2026/local_tool_receipt_pilot.py --mode success
python artifacts/control-evidence-2026/local_tool_receipt_pilot.py --mode fail
python artifacts/control-evidence-2026/local_tool_receipt_pilot.py --mode tamper
python artifacts/control-evidence-2026/local_tool_receipt_pilot.py --mode missing
```

**Verification:** equivalent local code passed **10/10 tests** on 2026-10-29 using a test-only local copy of the action-completion decision rule. GitHub Actions is now configured to run the committed probe tests against the repository's **actual** `contract_smoke.py`. Do not claim the new 77-test remote suite passed until the workflow run is checked. Prior 67/67 remote pass: [run 40888335435](https://github.com/Svyable/Opps/actions/runs/40888335435). New workflow: [run 40916333085](https://github.com/Svyable/Opps/actions/runs/40916333085), initially in progress.

## How this changes the application claim

Permissible claim: **“We have a runnable, side-effect-contained local process demonstration showing that a claim's verdict follows independently observed subprocess outcomes rather than the narrative; tampering and missing observations lead to abstention.”**

Impermissible claims: a real agent has been tested; a third party authenticated the source; an R3 reviewer has adjudicated anything; the system is safe; these tests establish false-support rates or a grant-selection advantage. The actual funded research still needs permissioned AI-agent traces, trusted recorder identity, a frozen holdout, independent R1/R2/R3, privacy/rights clearance, and a prespecified analysis.

## Expected-value discipline

Official [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai): always open; typical awards $10,000–$150,000; individuals, new organizations and new projects at existing organizations may apply. Credible charitable grantmaker. The **$25,000 is an applicant-proposed restricted budget**, not an award or commercial revenue.

The ledger's earlier illustrative conditional founder surplus was $7,800, with subjective 55% delivery feasibility and 5% conditional selection. Expected surplus before pursuit cost is **$214.50**. Deducting $70 remaining application preparation gives **$144.50**. The prior R3 work was estimated at $52.50–$87.50; this new probe at another **1–2 hours × $35/hour = $35–$70**. If all those costs are incremental and no probability improvement is credited, the sensitivity is **−$13 to +$57**. The 5% selection assumption is not calibrated and **is not raised** by this work. Historical sunk effort is not included in a fresh go/no-go decision. The next hour of additional synthetic engineering is unlikely to be the best use of resources.

**Next decision, applicant-only:** verify a legal payee, 12 hours/week lead capacity, a separate engineer and three distinct review roles, actual authenticated trace access, rights/privacy, and the live Paperform terms; approve a truthful application before submission. Do not hire, contact, spend, submit, or accept terms automatically. Keep Foresight's separate prospective authorization-gate research and EA's retrospective receipt-adjudication hours, cases and deliverables distinct.

**Source check 2026-10-29:** [EA Funds official](https://funds.effectivealtruism.org/funds/transformative-ai); [Foresight official](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/) (separate October 31, 23:59 PDT deadline).
