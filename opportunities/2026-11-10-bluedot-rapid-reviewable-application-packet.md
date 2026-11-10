# BlueDot Rapid — Control Evidence: conditional application packet (2026-11-10)

**Internal draft only. NOT authorized for submission.** Status PURSUE / release-blocked. This packet converts the existing 60-hour proposal into a reviewable application narrative and explicit factual gates; it does not assert credentials, independent benchmark success, applicant identity, or approval.

Official rules checked 2026-11-10: https://bluedot.org/grants/rapid — up to $20,000; research time, compute and experiments permitted; asks for plan and budget; selection looks for a worthwhile direction, evidence of ability to make progress, and a clear role for funding. Approximately 15-minute application; lump sum after claim/checks; approved-purpose restriction, material changes require written approval, completion report within 60 days of finishing. No fixed deadline or selection rate published. Payment restrictions and sanctions apply; see prior audit at `2026-11-10-bluedot-rapid-release-decision-source-audit.md`.

## Proposed narrative — fact-checked versus proposed

**Project:** Control Evidence — independently reproducible evidence for agent-control failures.

**Problem and purpose (hypothesis, not demonstrated impact):** Advanced AI agents can act through tools, permissions, and external state. A safety-relevant question is whether a claimed control or containment boundary actually prevents an agent from performing an unauthorized action, and whether an outside reviewer can reproduce the evidence. The proposed research would develop a minimal reproducible recorder/fixture workflow to test this question. A connection to catastrophic-risk reduction is **hypothesized**, not yet empirically established.

**What already exists (repository evidence, not independent validation):** Svyable/Opps contains a Python funding-release gate and ten synthetic unit-test cases; `artifacts/control-evidence-2026/funding_release_gate.py` and `test_funding_release_gate.py`. These demonstrate budget-scope duplicate detection, **not** agent-control safety effectiveness. Prior ledger records also describe Control Evidence receipt-verification work; exact executable evidence and independently administered test results remain to be supplied.

**What funding would enable (future, conditional):** 60 prospective research hours devoted to designing a small, explicit agent/tool control boundary; building deterministic failure/success fixtures; capturing raw recorder traces and hashes; rerunning the cases in an independently reproducible environment; and publishing a limitations-first technical report with a reviewer replay procedure. The exact four stable deliverable IDs and cross-funder exclusions must be reconciled with `2026-11-09-bluedot-rapid-60h-funder-exclusion-schedule.md` before any submission.

**Budget:** Request $4,500 = 60 prospective hours × $75/hour. This is a *proposed rate*, not a validated market rate or approved salary. Require applicant-provided rate basis, actual capacity and taxes/fees estimate. Do not charge BlueDot for work already charged or proposed to EA Funds; same actual deliverable is excluded even if its ID differs.

**Milestones (proposed; no completion claims):**
1. Define the tested control boundary, threat model, expected outcomes, and precommitted fixtures.
2. Produce runnable fixtures and raw traces for both permitted and denied tool actions, with machine-checkable evidence hashes.
3. Reproduce the results on a separately provisioned environment, record failures and limitations, and supply replay instructions.
4. Deliver an auditable research report explaining what was and was not established, and a completion report on the funder's schedule.

**Why this applicant?** [BLOCKED: first-party CV, contribution history, AI safety involvement, and applicant authority must be supplied. Do not claim them from a GitHub organization name.]

**Why now / why this amount?** A bounded 60-hour experiment could turn existing exploratory artifacts into independently checkable evidence; $4,500 is the proposed cost of the new work, not an award or verified marginal benefit. [BLOCKED: availability and alternative funding must be confirmed.]

## Mandatory release evidence (all must be resolved)
- [ ] Named lawful applicant/payee and actual payment country; sanctions and transfer eligibility verified.
- [ ] Applicant-authored qualifications/contribution evidence and any BlueDot/community involvement, with links.
- [ ] Signed or otherwise first-party-confirmed 60 future hours, $75/h rate basis, and actual research ownership.
- [ ] Independent raw agent-control recorder output, replay commands, source revision, environment and pass/fail log; distinguish synthetic finance-validator tests from safety tests.
- [ ] Human-reviewed non-overlap schedule with EA $25k plan and other funding; reconcile semantically equivalent deliverables, not just IDs.
- [ ] Check relevant code/dataset licensing, confidential material, public disclosure constraints and any funder terms.
- [ ] Applicant reviews final narrative and grants explicit authorization **before** any submission.

## Commercial decision

Official maximum $20,000; requested $4,500; no published deadline or selection odds. Illustrative delivery opportunity cost 60 × $35 = $2,100; conditional surplus $2,400 before taxes, fees, overhead and restrictions. If final applicant review costs 1 hour/$35, break-even joint probability of qualification, award and payment is 35/2400 = **1.46%**. This is only a threshold, **not** a probability estimate. Actual EV is **unknown**. Packet drafting has no measured incremental award-probability uplift; do not call it positive-EV proof.

**Decision:** Hold conditional PURSUE, not submit. The next valuable work is a real independently reproducible control-boundary trace or first-party eligibility confirmation, not more cosmetic rewriting. No contact, payment, registration, acceptance, or rights grant authorized.
