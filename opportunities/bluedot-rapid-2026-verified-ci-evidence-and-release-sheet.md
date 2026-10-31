# BlueDot Rapid — verified CI evidence and applicant release sheet (NOT SUBMITTED)

**Prepared 2026-10-31 UTC.** Svyable / Sven Hardy Benson. This is a *reviewer-facing evidence index* for the existing conditional **$6,000 / four-week** Rapid Grants proposal, not a grant award, new experiment with real agents, or permission to apply.

## Funder: verified current terms and payer credibility

- Official live Rapid Grants page: https://bluedot.org/grants/rapid (checked 2026-10-31). **Up to $20,000**, **rolling/no published fixed cutoff**, ~15-minute application. Supports research time, living costs, tests, tools and projects already underway. The stated screen is: worthwhile AI-safety direction, evidence the applicant can make progress, and a clear role for funding.
- BlueDot Impact has publicly reported **77 grants totaling over $50,000** by April 14, 2026, with examples including $4,800, $5,000 and $8,000 awards. Source: https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants . These are BlueDot's own claims, not independently audited payouts. Its April blog described a $10,000 maximum at that time; the **current official Rapid page supersedes it with $20,000**.
- Official restrictions: no payments to listed restricted jurisdictions or sanctioned recipients; charitable/educational purpose; no party-political campaigning; written approval before material project changes; grant paid as a lump sum **after an approved claim and required checks**, with possible transfer costs; completion report within 60 days. BlueDot community participation can improve likelihood but is not required. No membership or jurisdiction is claimed for this applicant.
- This is restricted project funding, **not a $6,000 profit or guaranteed salary**. No cash-flow promise before the approved claim.

## Evidence: reproducible, correctly bounded

**Remote CI:** https://github.com/Svyable/Opps/actions/runs/41170302920

- Commit https://github.com/Svyable/Opps/commit/c7e3acf0c46dffa1710f95e435f0d0cd551f9efd adds the five pre-existing negative-control tests to the existing GitHub Actions workflow.
- **82/82 tests passed in eight sequential suites** on GitHub-hosted Ubuntu / Python 3.11 (14 + 9 + 11 + 11 + 10 + 12 + 10 + 5). All eight suite steps show success in the job logs; no new safety-efficacy inference follows.
- The new five tests: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_receipt_authenticity_gap.py . They establish that the *synthetic* claim contract trusts a self-declared `independent` writer label, accepts replayed records without a freshness check, and does not distinguish a real local supervisor observation from a fabricated event **when both are passed as synthetic cases**.
- The existing local subprocess pilot actually executes a separate local process and compares observed file hashes: https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/local_tool_receipt_pilot.py . It is **not** an authenticated recorder, real AI-agent integration, third-party validation or an externally deployed safety control.
- The five characterization tests intentionally **pass while demonstrating a known weakness**. They are not five successful security mitigations. The remote CI run confirms reproducibility of that characterization only.

## Application-ready short evidence paragraph (applicant must approve)

> We have an Apache-2.0 local subprocess demonstration that independently observes a file operation and checks its result against an action claim. A public GitHub Actions run passes 82 tests across eight suites. Five of those tests characterize an unresolved trust-boundary gap: a constructed event can spoof an independent recorder label, and the synthetic contract lacks replay freshness. We are seeking four weeks of funding to test run-bound recorder authentication, replay rejection and conservative abstention in a reproducible local harness, then publish negative results and seek independent reproduction if a qualified reviewer is available. We do not claim that the existing tests establish deployed-agent safety or independent attestation.

## Specific work that funding, not this preflight, would buy

- **60 founder hours / four weeks**: frozen threat model; isolated run-bound receipt prototype; tamper, role-spoof and replay negative controls; reproducibility release; raw case counts and stop/go report.
- **10 independent-review hours** at planning rate only, conditional on a consenting reviewer and separate outreach authorization. If no reviewer is available, disclose that fact and do not claim independent reproduction.
- **$6,000 conditional budget**: $4,500 founder time, $1,000 reviewer, $300 isolated testing, $200 accessible packaging. These are planning assumptions, not invoices, quotes or approved rates.
- Do not charge pre-existing Control Evidence, Foresight or EA tests, this new CI wiring, or this application packet to the future grant. Keep any Seed, EA and Foresight scopes and hours separate.

## Release gate: unresolved facts requiring the applicant

1. **Time:** actual 15 hours/week for four weeks and ability to deliver the stated milestones.
2. **Payee:** applicant name, entity/individual status, jurisdiction, lawful receipt and tax considerations; sanctions eligibility cannot be inferred from GitHub.
3. **Rights:** contributor and third-party permissions for the precise code, data and outputs, beyond public Apache-2.0 repository declaration.
4. **Non-overlap:** truthful current funding/applications, no double billing and sponsor-specific disclosures.
5. **Consent:** exact live form and agreement, any confidentiality/publication implications, approval of budget/narrative, and separate explicit authorization **before submission, contact, hiring, spending or accepting terms**.

**Current status: PURSUE — applicant review only. No submission, inquiry, award, third-party reviewer or spending.**

## Incremental economics and stop rule

Prior BlueDot Rapid model: $1,500–$3,000 hypothetical *economic benefit after delivery*, 40–70% feasibility/capacity, 5–10% conditional selection, $70 initial application preparation plus $17.50–$35 earlier characterization labor. These are subjective assumptions, not observed BlueDot award rates.

Budget an additional **0.5 hour × $35 = $17.50** for CI inclusion, verification and this evidence index. With **zero assumed selection uplift**, updated cumulative modeled EV is:

- Cautious: **−$92.50 to −$75.00** (prior −$75 to −$57.50 less $17.50).
- Central: **−$26.50 to −$9.00** (prior −$9 to +$8.50 less $17.50).
- Favorable: **+$87.50 to +$105.00** (prior +$105 to +$122.50 less $17.50).

At $2,000 conditional surplus and 60% qualification, this step needs **at least +1.46 percentage points** of *conditional selection probability* to recoup $17.50; no such improvement is evidenced. **Do not perform more synthetic engineering or grant-polishing unless a specific applicant gate clears or a sponsor requirement makes it economically justified.** The next decision is applicant capacity/eligibility/approval, not another pre-grant feature.
