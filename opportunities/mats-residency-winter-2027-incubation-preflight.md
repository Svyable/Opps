# MATS Residency Winter 2027 — Svyable applicant-review package

**Prepared 2026-10-25 · Status WATCH / conditional applicant-review draft · NOT SUBMITTED.** This is a **personal, full-time paid research residency**, not a grant to Svyable or a guaranteed licensing/contract payment. No applicant consent, referee permission, job acceptance, disclosure, or legal commitment is implied.

**Official sources:** [program and compensation](https://www.matsprogram.org/residency), [current application and required fields](https://www.matsprogram.org/residency/apply), [track requirements](https://www.matsprogram.org/residency/tracks).

**Deadline:** **31 October 2026, Anywhere on Earth (AoE)**. Sponsor says applications open Aug 25–Oct 31; shortlisted applicants may interview or do a **paid** work test in early December; selected residents begin early 2027. The next application window is March 2027.

## Why screen this ahead of a fifth grant appendix?

MATS pays **$155,000–$285,000 gross per year**, prorated to the actual 6–24-month engagement, plus benefits and research compute. A six-month minimum corresponds arithmetically to **$77,500–$142,500 gross** before taxes, not an incremental $155k–$285k cash grant. MATS requires full-time work (part-time only case-by-case for academics on sabbatical) and at least one-third in-person at a Berkeley, London, or Washington, DC office. Relocation assistance may be available up to $25,000, subject to eligibility; it is not income. The applicant's full-time availability, work authorization, location preference, existing contracts, and ownership of Svyable IP are **not verified**.

**Qualification:** no PhD, formal academic title, or publication record required. Sponsor asks for substantive research work, a credible research agenda, two references, a representative work sample, and applicant-authored responses. The presence of public repositories makes initial work-sample fit plausible, but does **not** establish research quality or eligibility. Applicant must confirm two consenting references, ability to attend in person, full-time availability, and conflict/IP permissions.

## Proposed track: Incubation (conditional; applicant chooses)

**Candidate 2–3-sentence track note:**
> I want to develop a falsifiable research agenda for determining when autonomous-agent claims and control mechanisms deserve trust. Svyable already has bounded agent-authority patterns, an executable synthetic claim-verification contract, and real-data provenance work from scientific imaging, but these are not yet a validated agent-safety methodology. Incubation would let me test whether an independent, evidence-first research program can bridge that gap and deserve its own institutional home.

**Why Incubation, not automatic Anchor:** the central hypothesis and prospective independent validation remain open. Incubation explicitly supports greenfield research agendas and possible future organizations; it does not require founding a new company. If the applicant instead has a mature long-horizon program and can evidence sustained independent AI-safety research, Anchor may be more appropriate. The applicant must select the track personally.

## Candidate research plan — Evidence Boundaries for Autonomous Agents

**Research question.** When can a human or an automated reviewer justifiably rely on a statement that an AI agent performed, refrained from, or was authorized for a consequential action? A system may produce fluent summaries while the available execution evidence supports a narrower claim. Conversely, maximal abstention can make oversight useless. The aim is to measure the boundary between justified reliance and fabricated assurance.

**Hypothesis to falsify.** For bounded action types and authenticated execution-side records, explicit claim-to-evidence adjudication can lower false support relative to narrative-only reports, without making abstention so frequent that review loses practical value. This hypothesis may fail because record completeness cannot be independently established, reviewer disagreement is high, or the additional verification burden is too costly.

**Existing starting points, with limitations.**
- [Human Kind](https://github.com/Svyable/human-kind) encodes bounded agent authority, provenance, review and human decision ownership. This is a governance design, not proof of safety.
- [Control Evidence synthetic contract](https://github.com/Svyable/Opps/tree/main/artifacts/control-evidence-2026) has 19 transparent fixtures and a three-verdict claim-to-record contract. The source has 14 test methods; the post-patch suite and remote CI are not independently confirmed. The synthetic `independent` field is not an authenticated witness. A prospective blind-packet generator exists, but **no independent review or real trace study has occurred**.
- [ScrolIQ real-data evidence map](https://github.com/Svyable/scrollq/blob/main/docs/SUBMISSION.md) demonstrates provenance-bound evaluations on public scroll-imaging data, including negative controls and refusal to promote uncertain results. This is a transfer of **methods**, not an AI-agent safety result.
- [Foresight authorization-gate experimental design](https://github.com/Svyable/Opps/blob/main/opportunities/foresight-2026-application-narrative.md) is a separate **unrun** three-arm study. Do not treat it as evidence of effect or double fund its proposed work.

**Proposed methods.** First define a limited ontology of claims: action completed, authorization before action, alert delivered, and explicit non-action. Require verifiable recorder identity, event scope, integrity, bounded clock uncertainty, and coverage evidence. Treat unverifiable provenance and incomplete coverage as first-class outcomes. Run isolated mock-tool tasks with no real credentials, sensitive customer data, external messages, or irreversible side effects. Freeze evaluation questions and holdouts before agent executions; separate synthetic development cases from prospective evidence. Compare narrative-only, trace-search, and structured-receipt conditions. Use blinded reviewers and independently authored reference records. Report denominators, false support, justified abstention, reviewer agreement, time cost, failure modes, and uncertainty. Publish negative results.

**Theory of change.** Advanced systems will increasingly act through tools faster than direct human observation. Oversight depends on the validity of action evidence, not on an agent's confidence or a dashboard's appearance. An independently validated, bounded evidence contract could help evaluators reject unjustified assurances and specify what telemetry is necessary before delegating higher-stakes tasks. **No claim is made that the proposed work alone reduces catastrophic AI risk or generalizes to frontier deployments.**

**Prior art to distinguish, not erase:** [Auditable Claims about AI Agents](https://arxiv.org/abs/2610.07459), [Auditable Agents](https://arxiv.org/abs/2604.05485), and trace observability frameworks already exist. The intended novelty is independent adjudication under explicitly missing, delayed, conflicting, or compromised evidence, coupled to abstention calibration and operational cost. A serious novelty review may conclude the agenda is redundant; that is a valid stop outcome.

## First 90 days — evidence gates, not promised outcomes

| Period | Deliverable to attempt | Kill / pivot trigger |
|---|---|---|
| Days 1–30 | Threat model, prior-art map, verified trace-authorship design, legal/IP/data review, frozen hypotheses, registered holdout policy. | Cannot authenticate recorder identity or define defensible independent ground truth. |
| Days 31–60 | Isolated instrumented sandbox; independent tool-side receipts; adversarial missingness and clock-skew cases; provenance tests; blinded evaluation protocol. | Apparent results rely on self-attestation, leaked labels, or synthetic labels passed off as independent evidence. |
| Days 61–90 | First consented blinded adjudication, baseline comparison, confidence/abstention analysis, preregistered negative-results report and next-stage decision. | Reviewer agreement is insufficient, costs swamp utility, or claimed improvement vanishes under held-out evaluation. |

The 90-day schedule is **prospective**, not evidence that staff, data, reviewers, or infrastructure are secured. A 6–24 month program should scale only after the first phase supports continuation.

## Governance and publication plan (candidate, applicant must approve)

Research outputs would default to reproducible open publication when rights permit. Separate synthetic data from permissioned private telemetry; publish only de-identified or fully synthetic traces with provenance, consent and license checks. Preserve exact versions and hashes; do not disclose private credentials, vulnerabilities that materially enable misuse, or unapproved partner data. Disclose negative results, model limitations, reviewer disagreement, dual-use risks, and funding overlap. Human oversight governs external deployment and any escalation from mock tools to real systems. No institution, external reviewer or partner is claimed.

**Institutional/IP conflict:** Svyable already has public code and possible commercial interests. Before acceptance, determine whether MATS employment terms assign future IP, constrain consulting, require exclusive full-time service, or affect ongoing Svyable projects. No transfer of Svyable IP is authorized by this document. If the proposed work overlaps with EA Funds or Foresight grants, maintain distinct scope, time accounting, and outputs; do not double bill or promise simultaneous full-time residency plus 12–20 weekly founder hours.

## Suggested representative work sample — ONE primary

**Primary candidate:** [ScrolIQ's reproducible scientific-evaluation evidence map](https://github.com/Svyable/scrollq/blob/main/docs/SUBMISSION.md), anchored to its real-data [PHercParis4 winding experiment](https://github.com/Svyable/scrollq/tree/main/artifacts/2026-10-03-paris4-winding-attachment). This demonstrates a concrete research process with controls, uncertainty, exact artifact identities and falsifiable negative findings. It is **adjacent scientific methodology**, not a completed AI-safety experiment.

**Supporting context only if the form permits:** [Control Evidence executable synthetic contract](https://github.com/Svyable/Opps/tree/main/artifacts/control-evidence-2026) and [Human Kind](https://github.com/Svyable/human-kind). Do not represent repositories as peer-reviewed publications, independently validated results, or work solely authored by Sven without checking commit history and actual contributions.

## Applicant-controlled form completion matrix

| Required by MATS | Current status / needed evidence |
|---|---|
| Contact, affiliation, 2-page CV, work authorization, degree, prior MATS participation | **Unknown; applicant supplies truthful current details** |
| Track and 2–3 sentence rationale | Candidate Incubation wording above; applicant selects |
| Two consenting references | **Missing; no names invented or contacted** |
| One representative work sample | Public ScrolIQ sample selected for applicant review; authorship and rights to confirm |
| Two short written responses and counterfactual if not selected | **Applicant-authored responses needed**; no unsupported biographical claims |
| Incubation plan, 90-day plan, governance/publication, team/resources | Candidate sections above; staffing and ownership must be verified |
| Location, 1/3 in-person, full-time, start availability | **Unverified**; do not assume Berkeley commute or capacity |
| AI-use disclosure and consent to policy | Draft prepared with AI assistance; applicant must disclose accurately and personally accept terms |
| Explicit submission authorization | **NOT GIVEN**; no form submission, external outreach, reference contact or agreement |

## Economic screen: personal earnings, not Svyable grant revenue

Illustrative **six-month gross pay** at the advertised annual range: $77,500–$142,500. Incremental earnings must deduct actual foregone work and taxes/benefits differences; neither is known. To avoid equating salary with profit, use an **explicitly hypothetical** $60,000 six-month alternative earnings baseline and $105 preparation cost (3h × $35/h). At the $155k annual lower end, conditional incremental gross before taxes is $17,500.

- Cautious scenario: 30% availability/eligibility feasibility × 3% conditional selection × $17,500 − $105 = **+$52.50** incremental EV.
- If full-time availability is zero, **−$105**.
- If availability is 60% and selection 3%, **+$210** under the same baseline.
- At the upper salary end and 30% × 3%, with the same hypothetical alternative earnings, EV is **+$637.50**.
- The sponsor does not publish an applicant acceptance probability here; **3% is an uncalibrated screening assumption**, not an estimate of the actual rate.

**Decision: WATCH with high-priority eligibility gate.** The unusually large conditional personal compensation and strong methodological reuse warrant an applicant review; full-time availability, references, Svyable IP ownership and opportunity cost could make this economically unattractive. No further work should be treated as authorized submission.

**Next concrete gate:** verify full-time/in-person capacity, two consenting references, legal/IP compatibility, and the actual alternative earnings baseline before promoting to PURSUE. Application closes October 31 AoE; do not claim eligibility is confirmed.
