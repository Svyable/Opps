# Pivotal Research Q1 2027 — mentor-specific evidence and research plan (NOT SUBMITTED)

**Prepared 2026-11-01 UTC for Sven Hardy Benson / Svyable.** This is an applicant-review technical packet, **not** a representation that the applicant is available, eligible to work in London, has completed human-subjects research, or has been selected. No application, referral, mentor contact, registration, or commitment was made.

## Official opportunity and decisive fit

- **Payer:** [Pivotal Research](https://www.pivotal-research.org/fellowships/ai-safety-fellowship), a UK non-profit company limited by guarantee (company number 16440066, as stated on its official site), with prior fellowship cohorts and publicly described projects. Financial statements and individual stipend payouts were not independently audited.
- **Deadline:** **November 1, 2026**, with no cutoff hour/timezone stated on the official page when checked November 1. Do not infer that an application remains open through local midnight.
- **Terms:** January 18–April 30, 2027, **15 weeks full-time in person in London**. **£15,000 fellow / £18,000 senior fellow** stipend, travel, compute and **£1,800 per month housing support for non-London fellows**; these are not a Svyable service contract or grant to a company. Rare remote exceptions and visa assistance are discretionary, not assured. Applicants must be **18+** and apply to **at least one mentor**. Shortlisted applicants face a video interview, 1–3h work task and personal interview. The fellow retains ownership of research outputs; precise grant/employment/tax terms have not been reviewed as an applicant.
- **Strongest named mentor fit:** [Preeti Ravindra](https://www.pivotal-research.org/mentors/profile/preeti-ravindra) (independent AI control researcher) and [Jess Bergs](https://www.pivotal-research.org/mentors/profile/jess-bergs) (UK AI Security Institute), who **jointly describe a specific empirical human-in-the-loop oversight project** for automated R&D tasks, emphasizing human attention, failure of existing oversight patterns and real experimental evidence. This is a documented research agenda, not mentor endorsement or a commitment to accept this proposal.
- **Lower-confidence alternative:** [Pascal Berrang](https://www.pivotal-research.org/mentors/profile/pascal-berrang) seeks zero-knowledge inference and multi-step agent proofs. Control Evidence has no demonstrated ZKP/GPU expertise, so do **not** claim direct qualification for that track.

## Verifiable existing Svyable work (with boundaries)

1. [Control Evidence contract and threat model](../artifacts/control-evidence-2026/README.md): public, deterministic claim-to-record decision grammar for `action_completed`, `approval_before_action`, and `alert_delivered`; includes synthetic support/refute/abstain fixtures. It is **not** an AI model evaluation or independent real-world attestation.
2. [Local subprocess evidence pilot](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py): launches a real local subprocess and compares an observed file digest. Its supervisor identity is **not cryptographically authenticated** and the pilot does not demonstrate deployed-agent security.
3. [Two-arm allocation and contamination preflight](../opportunities/taif-control-evidence-2026-two-arm-design-preflight.md) and [allocation code](../artifacts/control-evidence-2026/two_arm_design.py): two reviewers each see each case once, in complementary narrative-only / narrative-plus-receipt assignments; balanced by claim type. No human reviewers were recruited and no blinded study has been conducted.
4. [GitHub-hosted CI run](https://github.com/Svyable/Opps/actions/runs/41170302920): **82/82 passing tests across eight suites**, previously verified on Ubuntu/Python 3.11. Five tests deliberately characterize spoofed writer labels and missing replay freshness in the synthetic contract. These passing tests **expose unresolved vulnerabilities**, not five fixed security controls.
5. [Human Kind](https://github.com/Svyable/human-kind): adjacent authorization/review architecture. Public source existence does not prove adoption, participant rights, clinical/enterprise use or research impact.

**Prior art:** The existing Control Evidence README identifies *Auditable Claims about AI Agents* (arXiv:2610.07459) and *Auditable Agents* (arXiv:2604.05485). The proposed contribution is a bounded **human-oversight empirical comparison** and instrumented trust-boundary test, not invention of auditability.

## Proposed mentor-aligned research question (draft technical substance, not a personal attestation)

**Working title:** *When Does a Human Believe an Agent's Receipt?*

**Falsifiable question:** In controlled action-completion tasks, does providing a run-bound, independently recorded action receipt reduce **incorrect human acceptance of false agent claims**, relative to narrative-only reports, without creating excessive abstention or review-time cost? Under what missingness, spoofing, replay and contradiction conditions does a receipt **mislead** rather than help?

**Why it fits Preeti/Jess:** Their published project asks for empirical evidence about human attention and scalable oversight, not just a new monitoring architecture. This proposal treats the *human reviewer* as an experimental endpoint and deliberately includes misleading evidence.

### Prospective design — not executed

- Freeze 3 claim types, a recorder-authentication threat model, scenario construction and an independent reference-adjudication protocol **before** the evaluation. Start with local sandbox actions, not private third-party telemetry.
- Build distinct action-run IDs and recorder-bound freshness/coverage checks; retain intentionally forged-origin, replay, omitted-record and contradiction controls. **Do not claim these checks already exist.**
- Construct up to **60 held-out cases**, stratified by claim type and evidence condition, with independently verified non-support cases. Synthetic examples remain public development fixtures, not the held-out score.
- Two genuinely independent reviewers each judge every case **once** under complementary conditions (narrative only versus narrative plus receipt), yielding at most **120 judgments**. Reviewer balancing and case pairing are prospective; the current code does not recruit or authenticate people.
- **Primary endpoint:** false-support rate on independently adjudicated non-support cases, reported by arm with raw numerator/denominator and uncertainty. **Secondary:** justified support, abstention, decision time, disagreement, contamination and missing data. Pre-specify analyses; do not use synthetic expected labels as independent ground truth.
- Human-factors extension: test whether evidence completeness and risk tier can prioritize scarce reviewer attention while preserving the ability to abstain. A negative or null result is publishable if the study is reproducible.

### 15-week possible delivery sequence, subject to mentor approval

| Weeks | Proposed deliverable | Acceptance boundary |
|---|---|---|
| 1–3 | Threat model, ethics/privacy and source-rights check, frozen preregistration | No invented consent or real-world agent claims |
| 4–6 | Run-bound recorder prototype and adversarial local cases | Independent observer identity/freshness limitations explicit |
| 7–9 | Held-out case generation, independent reference review, pilot calibration | Stop if reviewer independence or permissions fail |
| 10–12 | Consented paired human evaluation | Preserve raw counts, exclusions and reviewer blinding |
| 13–15 | Analysis, negative-result checks, public research note and code | Publish only rights-cleared artifacts, avoid safety-certification claims |

**Critical resource risk:** The 60-case / 120-judgment design assumes two independent reviewers and reference adjudication. At 12 minutes/judgment, this alone is **24 reviewer-hours**, excluding reference work. No reviewer, stipend allocation or ethics approval is secured; the mentor and applicant must rescope if this cannot be funded and ethically conducted. Pivotal's advertised stipend is for the fellow, not a guaranteed third-party reviewer budget.

## Applicant-only eligibility and release gates

1. Confirm age 18+, actual January–April **full-time London availability**, right to enter/work in the UK or feasible visa sponsorship, housing logistics and impact on other Svyable commitments.
2. Verify personal research background, credentials and writing samples truthfully. Existing synthetic CI tests do **not** establish empirical research experience, peer-reviewed publications, or prior human study leadership.
3. Choose actual mentor(s) in the live form; use Preeti/Jess as strongest documented match. Read and accept no terms until personally reviewed.
4. Verify ownership/contributor licenses, potential overlapping BlueDot/EA-funded work, independent reviewers, privacy and any human-research approvals. Keep pre-existing Svyable IP outside any new deliverable license absent permission.
5. Applicant must author/approve personal answers, availability, career intent and compensation/visa statements. **Explicit submission authorization is required**; none exists.

## Marginal economic screening (GBP, not a selection forecast)

Assume **1.5h future applicant preparation × £25/h = £37.50**; additional interviews, taxes, foregone licensing and moving friction are *not* priced, so the figures may be optimistic. Stipend is personal compensation; housing/travel are treated as expense offsets, **not additional free cash**.

| Scenario | Conditional net personal surplus after 15-week foregone work | Feasible/eligible | Conditional selection | Net EV = surplus × both probabilities − £37.50 |
|---|---:|---:|---:|---:|
| Cautious | £0 (£15k stipend − £15k opportunity cost) | 25% | 1% | **−£37.50** |
| Central | £4,800 (£15k − £10.2k opportunity cost) | 50% | 3% | **+£34.50** |
| Favorable | £10,000 (£18k − £8k opportunity cost) | 70% | 5% | **+£312.50** |

All probabilities and opportunity costs are **subjective assumptions**, not observed selection rates. A 15-week founder absence could make the true surplus negative. This is not £18k in unrestricted Svyable revenue. No probability uplift is attributed to this dossier.

**Decision:** Time-sensitive **PURSUE for applicant decision only**, with a strong named mentor match and a concrete falsifiable research sketch. The next action is applicant-controlled confirmation of London availability and author-approved submission *before the official November 1 cutoff if still open*. If not authorized by the deadline, close this intake as REJECT (unsubmitted), not LOST. No contact or application was made.

**Official sources checked 2026-11-01:** https://www.pivotal-research.org/fellowships/ai-safety-fellowship ; https://www.pivotal-research.org/mentors/profile/preeti-ravindra ; https://www.pivotal-research.org/mentors/profile/jess-bergs ; https://www.pivotal-research.org/mentors/profile/pascal-berrang ; https://www.pivotal-research.org/people?areas=show&fellowship=ai-safety-fellowship&group=mentors .
