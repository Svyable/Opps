# BlueDot Rapid Grants — four-week recorder-integrity feasibility sprint (applicant-review packet)

**Prepared 2026-10-30 UTC · Sven Hardy Benson / Svyable · PURSUE preparation only · NOT SUBMITTED.** This packet corrects the older Rapid ceiling and funding-purpose assumptions using the live canonical BlueDot rules. It is a **shorter alternative** to the six-month BlueDot Seed proposal, not a second claim on the same work.

## Sponsor-verified opportunity and why the correction matters

- [Current official Rapid Grants page](https://bluedot.org/grants/rapid), inspected October 30, 2026, advertises **up to $20,000**, explicitly includes **time, living costs and research access**, says the application takes **about 15 minutes**, and permits **work already underway**. It offers no published fixed deadline. The old Opps ledger's "$50–$10,000" ceiling, "living stipends not usual", and "usually upfront" description no longer matches this canonical page.
- BlueDot asks for a worthwhile AI safety/biosecurity direction, evidence the applicant can make progress, and a clear role for funding. BlueDot course membership is **not required** ([official overview](https://bluedot.org/grants)); current Rapid FAQ says course participants, alumni and active community members may be **more likely** to receive a grant. No Svyable membership or track record with BlueDot is claimed.
- Rapid grants pay **one lump sum after an approved claim and checks**; acceptance email determines timing, and transfer/exchange fees can reduce proceeds. Restricted charitable/educational purpose; material changes need prior written approval; short completion report due within **60 days** of completion or grant-period end. Funding restrictions include specified jurisdictions and sanctions. No eligibility determination is possible without applicant identity and recipient jurisdiction.
- The [older BlueDot Technical AI Safety Project Sprint-specific small-grant post](https://blog.bluedot.org/p/rapid-small-grants-for-the-bluedot) has participant-only rules and narrower reimbursement exclusions; **do not confuse that separate sprint offer with the current general Rapid Grants page**. Exact live application form fields/consents have not been inspected. Do not invent a form URL.

## Why this is the most executable incremental funding route

The six-month [BlueDot Seed proposal](bluedot-seed-grants-2026-evidence-bound-agent-actions-preflight.md) assumes an unverified **35 hours/week for six months**, a new-project characterization, and $60,000 of restricted funding. Rapid expressly permits **work already underway** and funds a smaller piece of time and testing. It can therefore support a **four-week stop/go feasibility sprint**, rather than a new organization or a full SDK/adoption promise. This reduces the applicant's capacity burden but does **not** prove 15 hours/week is available, remove jurisdiction restrictions, or guarantee award.

**Proposed conditional ask: $6,000 for four weeks.** No award, contractor quote, third-party agreement or grant eligibility is claimed. If the applicant cannot personally commit the hours or does not want grant-paid living support, rescope before using this draft.

## Application material — sponsor-specific, applicant must verify and edit

**Problem.** AI-agent text and tool-authored logs are weak evidence that a consequential action occurred. A local subprocess demonstration can already detect missing, tampered and failed actions, but it relies on an unauthenticated supervisor role label. A grant should buy the next falsifiable answer: *which recorder-authentication and replay controls can be demonstrated with a reproducible local-only harness, and which claims still cannot be justified?*

**Existing proof of execution.** The Apache-2.0 [Control Evidence local subprocess pilot](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py) actually executes a separate local process and compares observed file digests; [10 regression tests](../artifacts/control-evidence-2026/test_local_tool_receipt_pilot.py) cover success, failure, mutation, missing receipts and scope mismatch. [Previously verified GitHub Actions run](https://github.com/Svyable/Opps/actions/runs/40916333085) passed **77/77** across the Control Evidence suites on October 29. Those are **engineering tests**, not actual AI-agent deployment, third-party telemetry, independent safety validation, or evidence of users. [Human Kind](https://github.com/Svyable/human-kind) provides bounded authority principles; [ScrolIQ](https://github.com/Svyable/scrollq) provides general provenance design ideas, not agent-efficacy evidence.

**Four-week funded work, prospective and distinct from sunk work:**
1. **Week 1:** Freeze threat model, evidence trust boundaries and attack matrix; specify attacker control of process output, agent-authored logs, replay and missing observations. Define success/abstention before running tests.
2. **Week 2:** Implement an isolated, local-only, run-bound receipt verification experiment, including tamper/replay/role-spoof negative controls. Never treat a self-declared `independent` writer string as proof of authentication.
3. **Week 3:** Invite **only after separate approval** an independent reviewer to attempt a fresh local reproduction; record disagreements, failures and any absence of a reviewer. No reviewer is engaged.
4. **Week 4:** Release a versioned, standard-library reproducibility bundle, attack matrix, raw counts and limitations; publish a clear stop/go recommendation for any later full SDK integration.

**Measurable outputs:** one frozen threat-model document; a reproducible isolated test harness; explicit true-positive/false-support/abstention counts on *constructed cases* with denominators; independent reproduction **if permissioned and available**; a negative-results section; a decision about whether real-agent integration is technically and economically warranted. No claim of deployed agent safety or customer adoption. If source authenticity cannot be established, the supported verdict must abstain.

## Conditional $6,000 budget (planning rates, not invoices or commitments)

| Work package | Basis | Proposed |
|---|---|---:|
| Founder research/implementation time | 60 hours over four weeks × $75/hour; **availability not attested** | $4,500 |
| Independent technical reproduction | 10 hours × $100/hour, **reviewer not engaged** | $1,000 |
| Isolated local test resources | Capped, actual receipted expenses | $300 |
| Accessible reproducibility packaging | Capped, actual receipted expenses; no double-charge of founder time | $200 |
| **Total** | **Restricted project support, not profit or salary** | **$6,000** |

The founder-time rate is an internal valuation assumption, not a BlueDot-approved stipend or guaranteed taxable treatment. Do not incur any expenses, hire, or contact reviewers before approval.

## Strict non-overlap / IP guard

- **Pre-existing and not newly billable:** 77 prior tests, existing subprocess probe, EA blinded reviewer scoring, Foresight's sequence-level veto mock, Human Kind policy, ScrolIQ scientific tooling.
- **Rapid's incremental work:** bounded recorder-integrity feasibility and reproduction; **not** EA Funds' 10-week human claim-verification study, **not** Foresight's three-arm human-veto experiment, and **not** BlueDot Seed's six-month SDK framework integration/adoption.
- **One BlueDot route at a time:** treat Rapid as the **shorter alternative/precursor** to Seed, not two applications for the same deliverables. If Rapid is funded, disclose it and **remove its funded hours/results/costs from any later Seed, EA or Foresight budget**; seek sponsor approval before overlapping scope. Do not add both face values as revenue.
- Opps has a public Apache-2.0 declaration, but contributor ownership and third-party rights still need verification. Do not copy source from unlicensed Svyable/agents or infer rights to third-party systems. No confidential traces, external systems or credentials are necessary for this proposed local-only sprint.

## Applicant-only release gates

1. Confirm **15 hours/week for four weeks** is real and compatible with existing obligations; otherwise rescope.
2. Confirm real individual/entity payee, jurisdiction, tax treatment and BlueDot sanctions restrictions. Never infer identity from GitHub.
3. Confirm IP and contributor permissions for the exact files to publish; check BlueDot grant terms, exact form, confidentiality and reporting requirements.
4. Disclose all actual concurrent applications/awards and separate the funded work. If another funder already pays for this work, **do not apply** for it again.
5. Applicant approves the exact narrative and budget and separately authorizes any form submission, reviewer outreach, grant agreement or spending. None is authorized by this packet.

## Risk-adjusted economics (screening, not an award forecast)

**Published potential:** up to $20,000; **proposed request:** $6,000, restricted support. For EV, count only hypothetical **net economic benefit after completing four weeks of delivery**, not the $6,000 face value. Assume 2 hours of remaining form/legal-readiness work at $35/hour = **$70 marginal pursuit cost**. Cautious: $1,500 conditional benefit × 40% eligibility/capacity × 5% selection − $70 = **−$40**. Central: $2,000 × 60% × 8% − $70 = **+$26**. Favorable: $3,000 × 70% × 10% − $70 = **+$140**. All probabilities, rates and conditional benefits are **subjective and uncalibrated**, not BlueDot historical award rates. If applicant cannot commit, eligibility factor becomes zero and EV is **−$70** if prep is spent. This source correction earns **no assumed increase in selection probability**.

**Decision:** **PURSUE preparation only**, with a narrower time commitment and verified current terms. Do **not** submit while applicant capacity, recipient, rights and overlap remain unverified. Keep the larger Seed proposal on **WATCH** as an alternative until a genuine six-month commitment exists. No software changes or tests were run for this documentary/source correction.

**Official sources checked October 30, 2026:** https://bluedot.org/grants/rapid ; https://bluedot.org/grants ; https://bluedot.org/grants/seed .

## October 30 executable negative-control preflight (unfunded)

[Five synthetic characterization tests](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py) and a [source-linked falsifiable trust-boundary annex](bluedot-rapid-2026-recorder-authenticity-negative-control-2026-10-30.md) document the current unauthenticated `independent` writer/coverage labels and lack of run freshness. Constructed role-spoof and replay inputs can receive a `supported` verdict from the *synthetic contract*, which has never claimed recorder authentication. This is not a production-agent exploit or evidence of real-world safety. These pre-grant tests and this annex are already completed and **must not be charged to any grant**. The prospective $6,000 request would fund run-bound recorder verification and replay controls, independent reproduction if consented, and publication of negative results. New preflight labor $17.50–$35 reduces the previous central subjective EV from +$26 to −$9 through +$8.50 with no selection-probability uplift. Remote CI for these new tests has not yet been verified; the earlier 77-test run remains historical evidence.

## October 31 remote CI verification (supersedes the preceding pending-CI sentence)

The five characterization tests are now included in the standard GitHub Actions workflow and **all 82 tests across eight suites passed** in [run 41170302920](https://github.com/Svyable/Opps/actions/runs/41170302920) on commit [`c7e3acf`](https://github.com/Svyable/Opps/commit/c7e3acf0c46dffa1710f95e435f0d0cd551f9efd). This verifies reproduction of the known synthetic recorder-label/replay gap, **not** deployed-agent safety or authenticated attestation. See the [verified CI evidence and applicant release sheet](bluedot-rapid-2026-verified-ci-evidence-and-release-sheet.md) for the eight-suite counts, official sponsor terms, explicit no-double-billing boundary and updated conservative EV. No applicant-controlled eligibility gate is resolved; no application submitted.
