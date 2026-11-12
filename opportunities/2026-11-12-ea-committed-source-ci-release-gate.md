# EA Transformative AI — committed-source regression CI gate (2026-11-12)

**Status: PURSUE / NOT SUBMITTED.** Official grant: https://funds.effectivealtruism.org/funds/transformative-ai (rolling, typical $10,000–$150,000; early-stage projects focused primarily on catastrophic risk from advanced AI). Official institutional record: https://funds.effectivealtruism.org/ . No verified grant probability or applicant/payee eligibility.

## One material advance
Added a narrowly scoped GitHub Actions workflow at [control-evidence-scorer.yml](../.github/workflows/control-evidence-scorer.yml), commit [93b797f](https://github.com/Svyable/Opps/commit/93b797fa8e7f6e17f8e24805ebfb1ecc4a38bf93). It checks out the committed repository, pins Python 3.12, and executes `python -m unittest -v test_score_pilot.py` from the scorer directory. It triggers for changes to scorer, tests or workflow, and can be manually dispatched. Read-only contents permission and five-minute timeout; no paid compute or API keys requested.

This directly addresses the repeated release gate: previous 14/14 tests were reported against an equivalent local implementation, **not the committed checkout**. A CI run, if it completes successfully, will test committed source rather than a local copy. **No successful GitHub Actions run has been observed or asserted here.** The container could not fetch raw GitHub files (DNS resolution failure); connector file reads did confirm current committed source and test contents. Workflow creation succeeded, but its execution and result remain unverified. Workflow is not independent gateway attestation or real-agent safety evidence.

## Reviewer-facing validity limits
The scorer still accepts caller-supplied boolean gateway events and cannot authenticate their origin. No real-agent paired trial, preregistered 40-scenario results, event provenance, external replication, or demonstrated reduction in catastrophic risk exists. Do not submit claims of empirical effectiveness on the strength of unit tests or CI alone.

## Decision economics and alternatives
A hypothetical $10,000 EA award is not a justified request absent an eligible budget. At 80h × $35/h, illustrative delivery labor is $2,800; the $7,200 difference is **not free income** and must be itemized or excluded. A 0.5h/$17.50 verification step would require >0.243 percentage-point improvement in the joint chance of eligible funding **if** $7,200 were legitimately net value; this is only a break-even sensitivity, not a measured uplift. Actual monetary EV is unknown. Reuse: existing scorer, 14 tests, mock authorization fixture, preregistered protocol.

BlueDot Media https://bluedot.org/grants/media: $20k–$200k, 6–12 months, audience and attributable published work unverified; WATCH. BlueDot Rapid https://bluedot.org/grants/rapid: existing $4,500 concept, published-term conflict and expense justification unresolved; PURSUE but blocked. Both have established institutional payers, no verified fixed cutoff, unknown award odds. Frontier five lanes remain separately tracked; benchmark points are not money.

## Next release gate
Inspect the GitHub Actions run for commit 93b797f and record exact URL, conclusion and logs; if it did not run, inspect repository Actions permissions. Then instrument the gateway independently and run the frozen paired experiment. Verify applicant identity/jurisdiction, rights, grant agreement, no funding overlap and eligible budget before submission.

No application, entry, contact, spend, agreement or IP transfer.
