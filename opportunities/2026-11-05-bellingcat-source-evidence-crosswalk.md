# Bellingcat AI Engineer — verified public work-sample boundary (2026-11-05)

**Internal evidence memo only. Not an application, motivation letter, portfolio attribution, or suggested submission text.** Bellingcat explicitly rejects AI-generated applications. The individual must independently decide what to cite and write their own submission.

## Verified public source and exact claims

- [Contract evaluator](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/contract_smoke.py): `decide(case)` validates scope/action/digest and filters records whose `writer` label is `independent`. It abstains on conflicting success/failure evidence and non-finite approval timestamps. The source contains 19 *visible synthetic fixtures* and unittest assertions. **Limitation:** `writer` is an unauthenticated input string, not recorder identity; public fixtures are not an external benchmark.
- [Local process observer](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/local_tool_receipt_pilot.py): `run_probe` starts a separate Python subprocess without shell execution, captures return code and local file bytes, and compares a SHA-256 digest. It models success/fail/tamper/missing outcomes. **Limitation:** supervisor is local and unattested; no deployed agent, independent third party, or signed telemetry.
- [Adversarial negative controls](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_receipt_authenticity_gap.py): five tests explicitly show that fabricated independent-writer labels and replayed synthetic events can be accepted by the current contract. **These are tests that expose a vulnerability, not five passing security guarantees.**
- [Prior CI run](https://github.com/Svyable/Opps/actions/runs/41170302920) was previously reported as 82 passing tests; this memo did not independently rerun or inspect the full CI log. Do not cite it as a fresh test result.

## Job-criterion crosswalk (code evidence vs missing human evidence)

| Official criterion | Public artifact support | Unverified gap |
|---|---|---|
| Agent workflow evaluation and guardrails | Claim/evidence evaluator, explicit abstention, negative controls | Production agent integration, genuine safety impact, external benchmarking |
| Human approval and feedback loops | Synthetic `approval_before_action` temporal logic | Actual human UI, consent/approval workflow, user testing |
| Full-stack engineering | No proof from these three Python files | React/frontend, backend operations, cloud deployments and maintenance |
| MCP / open-source harness integration | No proof from these files | Actual MCP adapters and maintained agent harness |
| Collaboration and mission-driven delivery | No proof from source alone | Specific personal collaboration, stakeholder and ownership examples |
| Authorship, availability, rights | No proof from source alone | Applicant's contributions, disclosure permission, European-hours overlap and 20/40h capacity |

## Opportunity, economics and release gate

Official [Bellingcat vacancy](https://www.bellingcat.com/contractor-ai-engineer-open-source-agentic-systems/) says **November 8, 2026** close (time unspecified), rolling review since October 21, 12-month contract, 20h or 40h per week, and **$80,000–$93,000 annual gross fee for 40h only**. The 20h rate is unpublished. Bellingcat is an established investigative nonprofit, but this does not establish personal eligibility.

This artifact reduces risk of *overclaiming* an existing code sample, not hiring uncertainty. No measured increase in qualification or hiring probability. Previously modeled +$101.25 prospective EV is subjective and **not incremental**. Estimated research/documentation cost: 0.5h × $35 = $17.50. Marginal EV = **−$17.50** unless the human independently uses this evidence to avoid a rejection or verify fit; no such gain is assumed. Because the payer forbids AI-generated applications, do not reuse any prose from this memo in the application.

**Human-only decision by November 8:** verify personal authorship/disclosure rights, independent full-stack/MCP and human-in-loop examples, European-hours overlap, availability and contractor economics; otherwise stop. No application, outreach, expenditure, contract or terms acceptance performed.
