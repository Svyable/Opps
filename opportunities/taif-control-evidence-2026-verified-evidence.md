# Control Evidence — independently checkable technical-readiness receipt

**Evidence captured:** 2026-10-26 UTC (2026-10-25 US Central)  
**Opportunity:** EA Funds Transformative AI Fund — proposed **$25,000 / 10-week** pilot  
**Status:** PURSUE · **NOT SUBMITTED** · no independent experiment completed

## Sponsor fit and funding boundary

The [Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) states that it is always open, typically makes $10,000–$150,000 grants, and accepts individuals, new organizations, and new projects at existing organizations. It primarily prioritizes work reducing catastrophic risks from advanced AI. This proposal's narrower claim-verification pilot must still persuade reviewers that the research is relevant to those risks; an operational audit tool alone does not prove such relevance. The proposed $25,000 is an **ask, not an award**.

## Verified repository evidence (not experimental results)

| Item | Checkable receipt | What it proves |
|---|---|---|
| CI workflow | [GitHub Actions run 40251427716](https://github.com/Svyable/Opps/actions/runs/40251427716) | **Success** on `main`, head commit `c98d79cc8761b9fe9cc134e190e3394438efb8fc`; started 2026-10-26 00:52:21 UTC |
| Contract verifier | [source](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/contract_smoke.py), Git blob `725cde08e15baa6c2df1530a68fd0380e1840afb` | **14/14** synthetic regression tests passed in the CI job log |
| Blind reviewer packets | [source](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/blind_packet.py), Git blob `ca1087754d2b85652df2cdfb76401c12edb1c7bb` | **9/9** regression tests passed |
| Reference-label scorer | [source](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/score_reviews.py), Git blob `339e00ca7e2f8f0dc94a5b5a9a03763bdd60ec51` | **11/11** regression tests passed |
| CI job | [job 121343985477](https://github.com/Svyable/Opps/actions/runs/40251427716/job/121343985477) | Three named test steps each concluded success; job log reports `Ran 14 tests ... OK`, `Ran 9 tests ... OK`, and `Ran 11 tests ... OK` |

**Total: 34/34 automated synthetic/unit tests passed in one remote GitHub Actions run.** This corrects earlier application language that remote CI had not been confirmed. The job tested the repository snapshot at the cited commit; later documentation-only commits do not imply another test run. A passing test suite verifies software behavior against designed cases, **not** truth of real agent claims.

## Open-source reuse audit — scoped, not legal clearance

- [Svyable/Opps LICENSE](https://github.com/Svyable/Opps/blob/main/LICENSE) is Apache-2.0. The Control Evidence prototype and workflow are in this repository. Public license is not proof that every input, trace or collaborator contribution is free of third-party restrictions.
- [Svyable/human-kind LICENSE](https://github.com/Svyable/human-kind/blob/main/LICENSE) applies Apache-2.0 to code and CC-BY-4.0 to non-code material by default, unless a file says otherwise. Reuse of *concepts* is different from copying code or protected research content.
- [Svyable/scrollq LICENSE](https://github.com/Svyable/scrollq/blob/main/LICENSE) is MIT; its [third-party notices](https://github.com/Svyable/scrollq/blob/main/THIRD_PARTY_NOTICES.md) explicitly preserve upstream data/model terms. Reuse provenance *methods*, not third-party datasets or undisclosed contest material. Its [embargo policy](https://github.com/Svyable/scrollq/blob/main/EMBARGO.md) must be honored.

**No blanket IP or employer clearance has been established.** Before accepting funding, applicant must check contribution ownership, any outside-employment restrictions, trace/data licenses, consent, and whether prior grant/customer obligations overlap.

## What is deliberately *not* established

1. **No authenticated execution-side telemetry** has been collected for a prospective blinded study; synthetic fixtures are not independent ground truth.
2. **No independent reviewers or engineers** have been recruited, consented, or contracted. Budget rates are estimates, not quotes.
3. **No frozen holdout, preregistered analysis, human agreement estimate, or transfer to deployed frontier agents** has been demonstrated.
4. **No applicant legal identity, payment jurisdiction, tax arrangements, weekly capacity, or form consents** have been verified.
5. The public [Paperform entry](https://av20jp3z.paperform.co/?fund=Transformative+AI+Fund) was not inspectable via available public-source access. Do not claim exact form fields or word limits.

## Applicant-use paragraph (verified, safe to adapt)

> We have implemented an open-source prototype for three narrowly scoped claim-to-record decisions, plus blinded reviewer-packet and reference-label scoring utilities. A public GitHub Actions run passed all 34 synthetic/unit regression tests across these components. This establishes that the proposed evaluation infrastructure is executable, not that it has been validated on independent agent traces. The funded pilot would collect authenticated sandbox receipts, freeze a held-out evaluation protocol, obtain independent adjudication, and publish both successful and failed cases.

## Remaining go/no-go gates

- **Recipient and capacity:** Confirm legal payee, taxes and actual 12 research-lead hours/week for 10 weeks.
- **Rights and independence:** Verify ownership, third-party licenses, potential employer restrictions, consent, engineer and reviewer availability and conflicts.
- **Application reality:** Inspect live form fields/terms, check budget eligibility, and personally review final text.
- **Authority:** Submission, outreach, spending and commitments require separate explicit authorization.

## Economic decision

Keep **PURSUE**. Previous illustrative *incremental founder economic-surplus* estimate remains `($12,000 lead allocation − 120 × $35 opportunity cost) × 0.55 feasibility × 0.05 selection − $70 pursuit = +$144.50`. Probabilities are uncalibrated; no evidence supports raising selection odds simply because CI passed. Do not confuse the full $25,000 restricted research grant with personal profit.

**Next cash-conversion step:** clear the four applicant-controlled gates and adapt the prepared [application draft](taif-control-evidence-2026-application-draft.md) to the live form. Do not expand the synthetic fixture count as a substitute for real evidence.
