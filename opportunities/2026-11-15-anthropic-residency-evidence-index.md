# Anthropic Residency — source-verified technical evidence index (2026-11-15)

**Decision:** WATCH / urgent, applicant-only release. **Application deadline: 2026-11-22**, exact closing hour/timezone not stated in the [official announcement](https://alignment.anthropic.com/2026/anthropic-residency/). This index is an internal factual appendix, not a cover letter or authorization to apply.

## Verified code artifacts (GitHub source inspection, not execution)

| Artifact | Verified repository blob SHA | What can truthfully be claimed | What cannot be claimed |
|---|---|---|---|
| [Synthetic claim-to-record contract](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/contract_smoke.py) | `725cde08e15baa6c2df1530a68fd0380e1840afb` | Public Python implementation with synthetic test fixtures and three claim types | Independently validated agent performance, deployed audit product or real-world accuracy |
| [Mock authorization gateway](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/mock_gateway.py) | `d9eaf15d622bc9e383611fee5bf5d83691960c7f` | Deterministic policy-driven event generator; explicitly mock-only | Authenticated external tool calls, independent telemetry, security certification |
| [Gateway regression suite](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_mock_gateway.py) | `478bcad1f0bf5ca6ad557756b4ce0a2275de5169` | Committed unit-test source exists | Successful current full-suite run or passing CI (not verified this run) |
| [Research protocol and limitations](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/README.md) | See live file | Proposed prospective blinded-review study and explicit synthetic limitations | Completed study, measured safety benefit, independent reviewers or funded pilot |

The exact three source blob hashes above were returned by GitHub file inspection on 2026-11-15. **No tests were executed during this audit.** Prior local reconstructed smoke tests do not establish full current repository CI.

## Match to the official research criteria

The [Residency announcement](https://alignment.anthropic.com/2026/anthropic-residency/) explicitly names **Adversarial Robustness and AI Control**, **Scalable Oversight**, and **Safeguards Research**. Control Evidence's separation of policy, execution events and independent claim adjudication is relevant to those areas. This is *topic fit*, not evidence of an accepted research result, seniority or individual ownership.

**Applicant-only critical evidence, currently absent:**
1. Two dated, attributable examples of personally leading ambitious technical work, with role and collaborators clearly identified. A repository owned by an organization does not prove who authored or led it.
2. A truthful CV and permission to present the specific work above; disclose synthetic/mock scope.
3. Confirmation of full-time availability for 6 weeks, 3 months or 6 months, and relevant US/UK work authorization/location.
4. Personal assessment of whether a full-time Anthropic role conflicts with Svyable ownership, current obligations or proposed grant-funded work; review invention assignment, confidentiality, outside activities and publication terms before any commitment.
5. Applicant approval of the final application and its terms. **No automated submission.**

## Economics and decision gate

Official annual-equivalent compensation: **$350,000–$500,000**; six-week prorated gross illustration **$40,385–$57,692**, before taxes and opportunity costs. Anthropic is the identified payer, but no offer or selection probability is known. The six-week figure is not a verified take-home amount.

Use **net incremental compensation** (gross less displaced work, relocation, taxes, benefits differences and rights/opportunity costs), not headline salary, as the economic payoff. If the applicant cannot document leadership or full-time availability, the qualification probability is effectively zero. If an illustrative $15,000 net benefit were real, 1 hour of further labor at an illustrative $35/hour would require >0.233% joint success probability to break even. **Neither the $15,000 net benefit nor probability is verified; monetary EV is unknown.** Limit further work to first-party evidence gathering; do not write a speculative personalized application.

**Official terms verified:** applications close Nov 22, 2026; full-time paid fixed-term placements; SF preferred, shorter remote possible; senior technical leadership sought; PhD/ML background not mandatory. Individual posting-specific legal, IP and compensation terms were not independently audited here.

**Sources:** https://alignment.anthropic.com/2026/anthropic-residency/ ; https://funds.effectivealtruism.org/funds/transformative-ai ; https://bluedot.org/grants/rapid .

No application, registration, outreach, spending, contract, rights transfer or employment claim was made. Existing five frontier benchmark lanes remain untouched and unpriced.
