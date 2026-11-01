# BlueDot Rapid — source provenance and applicant release-gate audit (NOT SUBMITTED)

**Checked 2026-11-01 UTC · Sven Hardy Benson / Svyable · Decision: PURSUE only after applicant clearance.** This is a documentary eligibility artifact, not a legal opinion, an applicant attestation, an application, a security certification, or evidence of an award.

## Why this was the highest-risk-adjusted active file to advance

BlueDot's [live general Rapid Grants rules](https://bluedot.org/grants/rapid) describe rolling funding **up to $20,000** for AI safety/biosecurity research, time/living costs, experiments and other concrete work, including work already underway. The [program overview](https://bluedot.org/grants) confirms that a BlueDot course is **not required**, though the Rapid page says active community participation may help. This is a restricted grant, not a consulting fee or business profit. Its decision criteria emphasize a worthwhile direction, evidence of progress, and a clear role for funding.

The existing [self-contained $4,500 alternative](bluedot-rapid-2026-self-contained-4500-alternative-2026-10-31.md) requests 60 prospective founder hours at an **unapproved $75/h planning rate**, with no unengaged reviewer and no unquoted tooling expenses. The older $6,000 alternative must not be submitted simultaneously. Unlike Pivotal's November 1 full-time London fellowship, BlueDot is rolling and can reuse existing Control Evidence work without assuming a 15-week relocation; unlike Eticas Lot C, it does not require unverified standards-sector references. None of these comparisons establish that Sven personally qualifies.

**Funder credibility:** BlueDot [reported on 2026-04-14](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants) that it had made 77 rapid grants totaling over $50,000. These are funder-reported grants, not independently audited receipts. The canonical live Rapid page says grant payments follow a claim and required checks, generally as a lump sum; material scope changes need written approval; a short completion report is due within 60 days. Funds cannot be used for unlawful, political-campaigning, or non-charitable/non-educational purposes. Sanctions and listed jurisdiction restrictions apply. The historical *Technical AI Safety Project Sprint small grant* is a **different** program and its prohibition on paying applicant time must not be imported into general Rapid rules.

## Exact source evidence and public-history check

All links below were read through the connected GitHub repository on 2026-11-01. Git blob hashes identify **specific public file versions**, not signatures or evidence of exclusive copyright ownership.

| Pre-grant asset | Git blob SHA-1 | Public commit-history observation | What it establishes |
|---|---|---|---|
| [Contract smoke / verdict grammar](../artifacts/control-evidence-2026/contract_smoke.py) | `725cde08e15baa6c2df1530a68fd0380e1840afb` | Three visible path commits on Oct 24–25, author displayed as Sven Benson, GitHub account Svyable | Reproducible synthetic rule grammar, not authenticated recorder |
| [Local subprocess receipt pilot](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py) | `da36e0eb25109071f18c861a150bab55954c9378` | One visible Oct 29 path commit, same displayed author/account | Local supervisor-observed exit and file digest, not independent trusted telemetry |
| [Local probe regression tests](../artifacts/control-evidence-2026/test_local_tool_receipt_pilot.py) | `388cbdd29d88908c62c426928ee09e2bc46dbcbb` | One visible Oct 29 path commit, same displayed author/account | Ten regression methods; not real agent trials |
| [Recorder authenticity negative controls](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py) | `3c3011c5d00ea7445d0a6a8770a191ea9cf8f052` | One visible Oct 30 path commit, same displayed author/account | Five deliberately passing tests exposing writer-label spoof and replay gaps |

The repository [LICENSE](https://github.com/Svyable/Opps/blob/main/LICENSE) contains Apache License 2.0 (Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`). The inspected four Python files use Python standard-library imports and local project imports; no third-party Python package dependency is needed for these particular tests. GitHub's displayed commit author is **not** proof of authorship, work-for-hire status, permission to license, absence of copied material, or exclusive contributor rights. The absence of a root `NOTICE` file at the inspected path is not proof that no attribution obligations exist elsewhere. The public Apache declaration establishes a license notice, not a legal clearance certificate.

**Previously observed execution:** [GitHub Actions run 41170302920](https://github.com/Svyable/Opps/actions/runs/41170302920) reported 82/82 passing tests on Ubuntu/Python 3.11 on Oct 31. That is **historical** evidence, not a new test run for this audit. Five tests intentionally confirm an unresolved synthetic vulnerability: an event can self-label its writer as `independent`, and replayed evidence lacks run freshness. Do not call these tests mitigations or claim any deployed-agent safety result.

## Funding/non-overlap and release decision

| Gate | Evidence found | Current decision |
|---|---|---|
| Public code availability and declared license | Public four-file path inventory, blob identities, Apache-2.0 repository license | **Partially evidenced**; exact contribution rights still need applicant affirmation |
| Pre-grant work separation | These four files and the 82-test CI predate any BlueDot award; the proposed four-week run-bound recorder work is prospective | **Documented scope boundary**; no pre-grant hours may be rebilled |
| Lawful payee, jurisdiction, sanctions, tax | Official funding restrictions checked; no private recipient facts available | **BLOCKED — applicant-only** |
| 60 genuinely available founder hours / $75/h support rationale | No verified calendar, alternative income or personal time commitment | **BLOCKED — applicant-only** |
| Rights in all code, inputs and outputs, including AI-assisted contributions | Public GitHub history and license do not establish complete ownership/permissions | **BLOCKED — applicant-only** |
| EA/Foresight/Seed/other award overlap | Ledger lists applications and drafts, not confirmed awards; private external funding cannot be excluded | **BLOCKED — applicant-only attestation** |
| Live application terms and consent | Public Rapid page reviewed, no authenticated applicant form/terms accepted | **BLOCKED — applicant-only** |
| External submission and legal commitment | No authorization | **BLOCKED — no submission** |

**Do not claim the source-rights gate is cleared.** The concrete gain is a version-pinned public source-history inventory that an applicant can use to check contributor/IP representations, with the difference between observed GitHub metadata and legal ownership explicitly exposed. The exact unresolved decision is whether the applicant can truthfully affirm rights, lawful receipt, 60 hours of capacity, non-overlap and the $4,500 budget, then separately authorize submission.

## Conservative expected-value accounting

**Payoff:** $4,500 restricted funding if approved and claimed, not $4,500 unrestricted profit. The previous central illustration used $1,800 conditional economic benefit *after 60 hours of delivery*, 60% feasibility, 8% conditional selection and $35 future applicant review, yielding **+$51.40** marginal EV before this audit. This is subjective, not an empirical acceptance rate. Assume **0.5 hours × $35 = $17.50** incremental audit labor. With **zero proven uplift in selection odds**, the same central *remaining pursuit* sensitivity becomes **+$33.90** ($1,800 × 0.60 × 0.08 − $35 − $17.50); cautious **−$28.50** ($1,200 × 0.40 × 0.05 − $52.50); favorable **+$115.50** ($2,400 × 0.70 × 0.10 − $52.50). Historical preparation costs and taxes are excluded; if personal feasibility is zero, any further pursuit costs are negative EV.

The **standalone** audit has no demonstrated positive probability uplift; its incremental EV is **−$17.50** if assigned zero value to reducing legal/eligibility misstatements or applicant verification time. Do not spend more autonomous engineering time or promise new performance evidence until an applicant-controlled gate clears. This dossier is a finite risk-screening step, not a reason to keep polishing.

## Next authorized decision

Applicant must privately verify and explicitly approve the legal payee, jurisdiction, 15 hours/week for four weeks, source/contributor permissions, grant overlap and the proposed support rate. Choose **one** grant budget and read the live form/acceptance conditions before any application. No application, inquiry, spend, contract, rights grant, new software test or external consent was made in this audit.

**Primary sources checked 2026-11-01:** https://bluedot.org/grants/rapid ; https://bluedot.org/grants ; https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants ; https://github.com/Svyable/Opps/actions/runs/41170302920 .
