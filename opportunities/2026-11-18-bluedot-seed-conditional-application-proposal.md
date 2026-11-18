# BlueDot Seed — independent executor evidence pilot: reviewer-ready conditional proposal
Prepared 2026-11-18 UTC. **Draft only; not submitted.** Existing opportunity, WATCH.

## Official basis and payer verification
[BlueDot Seed official rules](https://bluedot.org/grants/seed), checked 2026-11-18: $20,000–$200,000 for a **new** 6–12 month AI-safety/biosecurity project or organization; ~45-minute application; ~4-week decision target; solo founders welcome; no course prerequisite. Judging: problem selection, reasoned hypothesis, evidence of execution, concrete first-month plan. Funding generally paid to **individual founders**, not automatically a company. For-profit projects can sometimes qualify if public-good case is clear, **but approval takes longer**. Grant is **not salary, investment, or service contract**; often taxable. Monthly updates, final report, return of unspent funds if project stops. Geographic/sanctions restrictions apply. No fixed closing date shown. The funder publishes an operational grant process and terms; award not guaranteed.

## Proposed application narrative (subject to founder verification)
**Working title:** Independently Observed Agent Actions.

**Problem:** An agent can fabricate an internally consistent authorization-and-execution receipt. The current Svyable Control Evidence auditor checks consistency but does not authenticate recorder origin. Its forged-recorder negative control demonstrates this limitation. For consequential agents, audit logs without independent provenance can create false assurance.

**Hypothesis:** A narrow, independently controlled observation boundary, coupled with authenticated events and side-effect reconciliation, can reliably distinguish (a) authorized observed execution, (b) denied or substituted execution, and (c) unknown outcomes from missing evidence in a local sandbox. The pilot is designed to **falsify** this hypothesis, not assume it.

**Existing execution evidence:** Existing receipt auditor, provenance negative-control code and an isolated 12/12 regression run documented in [exact-byte verification](2026-11-17-taif-byte-matched-regression-verification.md). The negative control currently passes by accepting forged provenance. These are synthetic tests, **not** independent real-agent safety results. Existing code is a reuse asset; the proposed recorder is new work.

**Initial six-week plan:**
- Weeks 1–2: pin threat model, canonical event schema, run/nonce binding and recorder/executor isolation; implement minimal harmless file-action runner.
- Weeks 3–4: independent MAC/signature verification, path/byte authorization binding, final-state digest reconciliation, fail-closed and UNKNOWN semantics.
- Weeks 5–6: execute eight pre-registered cases (authorized, forged origin, substitution, replay, truncation, recorder compromise, crash gap, unauthorized action); archive exact command, seeds, logs and failure counts; prepare a reproducible public technical report.

**Success criteria:** forged-origin and substitution cases rejected; missing observation never silently counted as safe; authorized writes verified against independently observed final state. Report denominators and failures, not only pass/fail. Compromised recorder keys and same-host privileged adversaries remain outside security guarantee. Do not claim cryptographic authenticity proves physical execution.

**Project public-good case:** publish reusable verification protocol, negative controls and evidence-limited findings for independent evaluation of agent monitoring. Do not promise open-source release of third-party code or transfer of pre-existing Svyable IP until ownership/licenses are verified.

## Conditional budget and scope (illustration, not an approved cost)
Illustrative six-month **$30,000 request**: $24,000 founder research/living support, $3,000 independent technical review/reproducibility, $2,000 tooling/compute, $1,000 documentation and dissemination. No quoted vendors, spending authorization, founder availability or eligibility established. A lower ask is possible only after cost validation. Founder costs are grant support, not automatic commercial profit. Avoid charging any prior auditor work or overlapping TAIF/Media hours.

## Application evidence still required — stop/go
1. Named individual payee, jurisdiction/sanctions eligibility, tax review, and whether Svyable's for-profit structure is acceptable.
2. Founder availability and project **newness**; distinction from existing Control Evidence work and other grant scopes.
3. Rights to publish the new pilot and use/relicense relevant existing code; no implied assignment.
4. Runnable isolated recorder with a real negative test and reproducible logs. The eight cases and 100-trial plan in [falsification gate](2026-11-17-bluedot-seed-independent-recorder-falsification-gate.md) are **not yet run**.
5. Verified costs, nonoverlapping budget, and explicit applicant approval before any application or grant agreement.

## Risk-adjusted decision
Status WATCH (not new ledger entry). Reuse high; funder credible; application eligibility **unverified**; selection odds **unknown**; no deadline found. A bounded 8-hour engineering gate at assumed $35/hour costs $280 internal labor, no external spend. If retained economic benefit after grant obligations were hypothetically $10,000, the joint probability of eligibility, award and payment would need to exceed 2.8% to offset only that labor; this is a **threshold, not a probability estimate**. No defensible numerical incremental win-probability or actual monetary EV can be assigned. Stop proposal polishing until the runnable negative control or founder-specific eligibility is verified.

No application, outreach, purchase, contract, legal acceptance, or IP transfer.
