# ARIA Scaling Trust — Track 2.2 Component: verifiable agent-action reporting (conditional application preflight)

**Screened 2026-10-29 · Svyable / Sven Hardy Benson · WATCH · no submission, contact, expenditure or terms accepted.**

## Sponsor, live opportunity and why this is not another generic grant
- **Payer:** UK's Advanced Research and Invention Agency (ARIA), a UK government-sponsored public R&D body. [Official funding page](https://aria.org.uk/opportunity-spaces/trust-everything-everywhere/scaling-trust/funding) and [32-page rolling call (4 September 2026, v2.0)](https://aria.org.uk/media/013loxe3/scaling-trust-solicitation_rolling-applications.pdf).
- **Programme:** Scaling Trust (£49.8m total programme), **Track 2.2 Components** for reusable open-source secure-agent coordination tooling. Track 2 projects are stated at **£200k–£2m**, 3–12 months; the combined rolling call gives £100k–£3m across Tracks 2/3. **Neither is an offer or Svyable award.** Track 2 expects 4–6 teams; a small number of rolling awards may be made and zero in a batch is possible.
- **Timing:** First rolling batch **31 October 2026** cutoff, review 1–30 November, notice targeted 30 November; after cutoff proposals roll into the next quarterly batch. The live portal's precise cutoff hour must be confirmed, because the PDF embeds a **superseded March 24, 2026 14:00 GMT** deadline in its original summary; do not rely on that stale line. The website describes the October cutoff, not a confirmed hour.
- **Scope:** Track 2.2 includes a `Report` component (execution trace → convincing statement) and security auditing, but ARIA explicitly says it expects to focus **mostly on Negotiation and Security Reasoner**. A stand-alone receipt logger may therefore be *outcompeted* by proposals more central to the programme. Track 2.3 Adoption is **not** open in this call.
- **Payer credibility:** High (UK public agency, official published call). **Award probability:** very low/unknown for this particular non-UK, unstaffed applicant; no historical rate available.

## Distinct, falsifiable technical hypothesis — for applicant review, not a claim of demonstrated performance
**A policy-bound, independently witnessed execution-trace verifier can give an agent-to-agent coordinator a machine-checkable answer to whether a negotiated obligation was actually performed, while abstaining when observation is incomplete.**

Proposed reusable **Track 2.2 Component**, not a full multi-agent system: an API accepting (a) an explicit signed/identified agreement or security policy, (b) a typed action trace from a recorder outside the agent's own narrative channel, (c) a source/sequence binding and evidence manifest, and returning one of `SUPPORTED`, `REFUTED`, or `INSUFFICIENT`, plus reasons and a minimal audit report. A hostile counterparty must not be able to convert self-asserted logs into trusted execution receipts.

**Novelty to establish, not assume:** independent provenance + abstention + policy-to-execution binding under *two-agent negotiated obligations*, compared with existing event-log, observability, cryptographic receipt, agent-audit and formal-verification tools. Svyable has **not** yet demonstrated cryptographic attestations, multi-agent negotiation, proof-carrying protocols or production-grade trust boundaries. Avoid claiming formal guarantees or solved agent control.

### Existing assets to reuse without misrepresenting them
1. [Human Kind](https://github.com/Svyable/human-kind): bounded agent authority and decision-gate concepts; inspect ownership and exact licensing before reuse.
2. [Control Evidence](https://github.com/Svyable/Opps/tree/main/artifacts/control-evidence-2026): synthetic claim-to-record contracts, independent-reference protocol, reviewer allocation and local OS subprocess receipt probe. [77/77 GitHub Actions tests](https://github.com/Svyable/Opps/actions/runs/40916333085) passed 2026-10-29; these are **unit/synthetic/local-process tests**, not multi-agent robustness evidence.
3. [ScrolIQ](https://github.com/Svyable/scrollq): provenance and falsification practices; domain transfer is a hypothesis, not agent security evidence.
4. [agents](https://github.com/Svyable/agents): possible orchestration adapter; integration maturity unverified.

### Proposed staged work (conditional 6 months, not promised capacity)
| Stage | Deliverable | Honest pass/fail gate |
|---|---|---|
| Weeks 1–3 | Threat model and policy/receipt schema; prior-art matrix | Explicit trust assumptions; no claims based solely on agent narration |
| Weeks 4–8 | Minimal two-agent sandbox and independently instrumented receipt collector | Show supported/refuted/insufficient outcomes with a counterparty that can lie |
| Weeks 9–13 | Replay, truncation, reorder, tampering, confused-deputy and collusion test suite | Published false-support and abstention rates with adversarial controls |
| Weeks 14–19 | Open API, reference integration and benchmark pack | Independent install and reproduction, if a consenting tester exists |
| Weeks 20–26 | Third-party audit if available, negative-results report and dual-license release | No false claim of third-party audit if no reviewer is secured |

The benchmark must distinguish **execution**, **policy compliance**, and **evidence sufficiency**. Passing a local file-write test is not proof of an agent's obedience to policy.

### Six-criterion reviewer crosswalk
1. **Worth shooting for:** agents making verifiable commitments is central to Scaling Trust; narrow trace verification may be a necessary component, but its incremental importance versus negotiation/security reasoners must be demonstrated.
2. **Differentiated:** no defensible comparative claim until existing receipt/attestation frameworks and ARIA-funded components are surveyed and tested.
3. **Well defined:** six-month milestones above, but team composition, cost quotes, customer adoption and a credible security researcher are missing.
4. **Responsible:** minimize personal/secret data in traces, use isolated benign tasks, consent for third-party tests, explicit no-authenticity verdict without trusted recorder, and document export-control/dual-use issues.
5. **Intrinsic motivation:** existing open source supports interest and some execution, not claimed cryptographic expertise or committed 50–80% lead time.
6. **Benefit to UK:** **material blocker**. ARIA primarily favors UK-led/majority-UK-cost projects; non-UK proposals require credible, proportionate UK benefit and commitments. No UK collaborator, UK expenditure, operations or community event attendance has been verified. Do not invent one.

## Conditional budget architecture — NOT a bid, quote, award or promise
The Track 2 floor is **£200k**. A six-month £200k *illustrative* budget might allocate £60k technical lead, £54k integration engineering, £42k security/formal methods, £15k sandbox/compute, £12k independent adversarial review, £12k UK collaboration/travel and £5k administration/release. **Every role, cost, UK spend share and availability is unverified**; these allocations are placeholders, not evidence of capacity. ARIA's official cost spreadsheet and eligible-cost rules must replace this before submission. The current package does **not** demonstrate a majority-UK project or even a feasible six-month team.

## IP, eligibility, conflict and administrative stop-gates
- ARIA welcomes **individuals and non-UK organisations** but makes UK benefit a scored criterion and asks non-UK applicants for specific UK commitments. Lead researchers usually expected to commit **at least 50%, ideally 80%** of their time. No personal availability is assumed.
- **Foreground IP:** mandatory dual **MIT and Apache 2.0** licensing of funded software. Background IP remains owned by its holder, but its ownership, third-party dependencies and relicensing permissions need an actual audit. Do not promise to dual-license a dependency that cannot be.
- Team identity, jurisdiction, payee, sanctions/national security and conflict-of-interest checks, background IP, eligible costs, commercialization hypothesis and official budget template all require real evidence.
- Disclose EA Funds Control Evidence, Foresight, BlueDot Seed and Mercor **applications/proposals accurately**; none is an award in this ledger. ARIA must fund **new, distinct multi-agent policy-to-receipt integration**; do not rebill existing code, same staff hours or overlapping deliverables.
- The official application is a **PDF ≤10 pages**, Arial ≥11pt, ≥0.5-inch margins, plus portal administrative answers and budget. It requires explicit organizational authorization and acceptance/understanding of funding terms. **No portal submission, UK collaborator outreach, team registration, financial commitment or contract acceptance is authorized.**

## Incremental commercial screening (restricted project grant ≠ unrestricted revenue)
**Plausible programme grant:** £200k minimum Track 2 project, *not a promised payout*. Model only **£25k hypothetical net economic benefit after real delivery costs**, not the £200k face value. Four additional preparation hours at **£30/hour = £120** assumed opportunity cost. Subjective conditional scenarios:
- Cautious: 10% real eligibility/capacity × 1% selection × £25k benefit − £120 = **−£95**.
- Favorable: 35% real eligibility/capacity × 3% selection × £25k benefit − £120 = **+£142.50**.
These are not calibrated award odds. Unverified UK benefits, scarce staff and opportunity costs could make the real EV **substantially negative**. If the programme requires a UK operating plan or 50–80% lead commitment that the applicant cannot make, treat selection probability as approximately zero and **REJECT**.

## One concrete next decision
**WATCH**, not PURSUE. Before spending a further 4+ hours on the portal: (1) verify a lawful applicant/payee and genuine lead availability; (2) produce a specific, truthful UK benefit or UK partner plan without contacting anyone yet; (3) identify a credible independent security/formal researcher and source licenses; (4) demonstrate an agent-to-agent policy-to-receipt test absent from existing synthetic/local single-agent demos. If these are established and the applicant authorizes a bid, develop the ≤10-page PDF, ARIA spreadsheet and commercial hypothesis for a *later rolling batch* if the Oct 31 window is missed. Do not rush a misleading Oct 31 submission.

**Primary evidence:** [ARIA live call](https://aria.org.uk/opportunity-spaces/trust-everything-everywhere/scaling-trust/funding); [official v2 rolling CFP](https://aria.org.uk/media/013loxe3/scaling-trust-solicitation_rolling-applications.pdf), esp. pp. 14–16 (Track 2), 22–24 (IP/eligibility), 26–31 (review criteria and application).