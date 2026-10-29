# BlueDot Seed Grants — evidence-bound agent actions: conditional founder application packet

**Prepared 2026-10-29 · Svyable / Sven Hardy Benson · WATCH / not submitted.** This is a sponsor-specific, evidence-grounded draft for applicant review, **not** a claim of eligibility, a completed form, an approved project, a new legal entity, or a commitment to work full time.

## Funding opportunity and source integrity

- BlueDot Impact's [Seed Grants detail page](https://website-production.k8s.bluedot.org/grants/seed) describes **$20,000–$200,000 for 6–12 months**, a decision target of about four weeks, support for solo founders, and a project or organization intended to grow beyond its founder. The page was accessible on BlueDot's own production-preview host on 2026-10-29; **the canonical `bluedot.org/grants/seed` page could not be independently opened and the umbrella grants page does not currently expose a Seed listing in the retrieved text. Confirm the actual live application route and terms before any application.**
- The detail page says the default recipient is the **individual founder**; payment to an organization is negotiable, and for-profit funding is case-by-case and slower. The grant is **not salary, an investment, a contract for services, or automatically tax-free**. The applicant signs an agreement if approved; unused funds must be returned if the project stops. One Seed Grant per project. No verified application deadline is shown; treat as **rolling / live-intake unverified**.
- [BlueDot's current grant overview](https://bluedot.org/grants) lists Rapid Grants and Career Transition Grants. These are **alternative routes**, not additive awards for the same activities. [BlueDot's Incubator Week page](https://website-production.k8s.bluedot.org/programs/incubator-week) describes a potential pitch route to Seed funding, not a second $200k award.
- No sanctions or residence eligibility conclusion is inferred from Svyable's public GitHub. The applicant must confirm payment jurisdiction, legal/tax arrangements and actual founder availability.

## One-sentence proposal hypothesis — applicant must approve or rewrite

**Build an open-source, independently checkable receipt layer for consequential AI-agent tool actions so a user can distinguish an executed action, a claimed action, a blocked action, and a missing observation without trusting the agent's own narration.**

This is a **new six-month engineering and external-adoption project**, not a claim that a new company already exists or that Svyable has deployed customers. It must not relabel the existing research pilots as new funded work.

## Sponsor-aligned applicant-answer material (not exact form fields)

**Problem selection.** Autonomous agents increasingly operate tools, files and connected systems. Their natural-language self-reports do not establish whether an action occurred, whether a human authorized it, or whether evidence is complete. The product hypothesis is a small, framework-agnostic, fail-closed evidence interface that independent operators can run without accepting agent-authored logs as truth. This is a narrower, testable safety intervention, not a claim to solve frontier-model control.

**Evidence of ability.** Existing [Human Kind](https://github.com/Svyable/human-kind) provides a bounded agent-authority protocol with explicit no-decision-authority rules. [Control Evidence](https://github.com/Svyable/Opps/tree/main/artifacts/control-evidence-2026) contains synthetic claim-to-record contracts, reviewer allocation and adjudication scaffolding, and a real **local subprocess** file-action receipt probe. [77 passing GitHub Actions tests on 2026-10-29](https://github.com/Svyable/Opps/actions/runs/40916333085) establish software behavior under tests, **not** authenticated AI-agent traces, independent user validation, safety effectiveness, or real customers. [ScrolIQ](https://github.com/Svyable/scrollq) has evidence provenance and falsification patterns from a separate domain; its CT/scroll methods are not themselves agent safety evidence.

**First six months / measurable milestones.** M1 (weeks 1–4): freeze threat model and API for an independent recorder; demonstrate trusted-source binding, replay/tamper rejection, missing-evidence abstention and negative controls on a local isolated tool runner. M2 (weeks 5–8): integrate with **one** permitted open agent/tool framework; run reproducible benign action and attempted unauthorized-action scenarios, publishing both failures and limits. M3 (weeks 9–14): seek **permissioned** independent review of source, installation and recorder threat model; no reviewer is committed. M4 (weeks 15–20): seek **one** voluntary, consented external adopter for a non-sensitive sandbox pilot; no adopter exists today. M5 (weeks 21–26): publish Apache-compatible SDK/docs, a reproducible test matrix, counterexamples and a transparent continuation/stop decision. No third-party outreach, deployment, user testing or data transfer before explicit authorization.

**Success/failure measures.** Report test coverage for receipt integrity, source binding, replay, ordering, evidence completeness and unauthorized-action handling; number of independent reproducible installs; genuine adopter feedback if obtained; observed false-support, false-refutation and abstention counts on permissioned trials. If independent recorder authenticity cannot be established, do not claim the kit certifies agent actions. If no external adopter or reviewer is secured, publish that absence and do not invent traction.

**Why Seed rather than the existing grant drafts.** This proposed Seed work funds a reusable **open-source integration/installation layer and early external adoption**, not the EA Funds proposal's **blinded human claim-to-record adjudication experiment**, nor Foresight's **prospective comparison of no/cosmetic/enforced authorization gates**. Pre-existing code may be reused with its existing licenses; charge no previously completed work to any grant. If any sponsor considers the scopes overlapping, obtain written cost-allocation approval or pursue **only one** funding route. Maintain separate work-package IDs, time sheets, invoices, deliverable hashes and funding disclosures.

## Conditional six-month budget — $60,000 proposed, no quotes or commitments

| Cost | Internal planning basis | Amount |
|---|---|---:|
| Founder living/runway support | Six months; assumes actual **35 hours/week** focused on this project; not a salary offer or confirmed availability | $45,000 |
| Independent implementation support | 120 hours × $75/hour, hypothetical contractor | $9,000 |
| Independent security/evidence review | 30 hours × $100/hour, hypothetical reviewer | $3,000 |
| Isolated testing/compute/hosting | Estimated capped spend | $2,000 |
| Documentation, accessibility and reproducibility release | Estimated capped spend | $1,000 |
| **Total requested** | **Restricted project funding, not Svyable profit** | **$60,000** |

If founder availability is below 35 hours/week, if outside work conflicts, or if the recipient/tax treatment is unacceptable, **do not use this budget**. Re-scope and obtain applicant approval. No contractor or reviewer has been recruited, priced or authorized. No expenditure is authorized.

## Applicant-only decision gates — no public identity data

1. **Live route:** confirm current Seed intake, exact form, funder terms, confidentiality, and whether an existing Svyable initiative can qualify as a **new project** rather than a new organization.
2. **Founder commitment:** personally verify six months of ~35h/week, competing work, family/travel obligations and whether this is realistically the main project.
3. **Recipient/tax:** identify real individual recipient or obtain BlueDot's agreement to an organization payee; confirm sanctions, jurisdiction, tax treatment and grant-agreement acceptability.
4. **Rights:** verify ownership/permissions for all source, future contractor contributions, third-party framework licenses, and whether public release is feasible.
5. **Non-overlap:** disclose EA Funds, Foresight, Mercor and any actual awards accurately; use distinct cost codes, deliverables and time records. No duplicate-funded hours.
6. **External validation:** no representation that independent reviewers, users, partner organizations, vendors or security testers have consented.
7. **Approval:** review and rewrite application answers in applicant's own voice; explicitly approve any outreach or submission. No automatic submission, expense, contract, grant acceptance or personal-data disclosure.

## Economic decision, not an award forecast

Assume **3h additional application/readiness work × $35/h = $105** marginal pursuit cost. Since the $60k is restricted and includes actual delivery obligations, model only **conditional founder economic surplus**, not face value. Cautious: $10k surplus × 20% genuine eligibility/capacity × 3% selection − $105 = **−$45**. Favorable: $20k surplus × 50% capacity × 7% selection − $105 = **+$595**. Every probability and surplus is a **subjective assumption**; no historical grant success rate is available. No probability uplift is credited for this document.

**Decision: WATCH, prepared for applicant gate review.** If live intake, full-time capacity, new-project qualification, rights and non-overlap are all verified, move to PURSUE and adapt the final form. If they fail, do not manufacture a new company or promise unavailable work; prioritize the existing rolling EA Funds draft. The nearer Foresight October 31 deadline remains separate and applicant-blocked.

**Sources checked 2026-10-29:** [BlueDot Seed detail](https://website-production.k8s.bluedot.org/grants/seed); [BlueDot overview](https://bluedot.org/grants); [BlueDot Rapid Grants](https://bluedot.org/grants/rapid); [Foresight official RFP](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/); [EA Funds](https://funds.effectivealtruism.org/funds/transformative-ai).
