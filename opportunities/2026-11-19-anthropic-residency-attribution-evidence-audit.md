# Anthropic Residency — evidence-backed application exhibit and attribution stop gate
Prepared 2026-11-19. **Unsubmitted. Existing WATCH opportunity; no duplicate.**

## Official deadline and criteria
[Anthropic's 2026 Residency announcement](https://alignment.anthropic.com/2026/anthropic-residency/) says applications close **November 22, 2026**. It seeks established technical leaders transitioning to full-time empirical AI safety research, with six-week, three-month or six-month placements. US compensation $350,000–$500,000 **annualized and prorated**, not a lump-sum prize. Remote may be possible especially for shorter placements; San Francisco preferred. Payer: identifiable operating company. This file does not authorize submission.

## Audited public GitHub evidence: what it actually establishes
GitHub commit API was inspected on 2026-11-19 for these exact revisions:

| Evidence | Verified repository fact | What it does **not** prove |
|---|---|---|
| [ada3e633 — observer boundary](https://github.com/Svyable/Opps/commit/ada3e633918278f3505223f186eaf323c6b6d85c) | Commit adds `artifacts/control-evidence-2026/seed-recorder-envelope/observer_boundary.py`; GitHub attributes the commit to account `Svyable` | That Sven personally authored, directed, or tested the code; hardened isolation |
| [3d18538 — replay guard](https://github.com/Svyable/Opps/commit/3d18538f0f559db24b215774624dbd06834371df) | Commit adds `artifacts/control-evidence-2026/seed-recorder-envelope/replay_guard.py`; GitHub account `Svyable` | Personal authorship, independent security validation, deployment |
| [87b3482 — Residency preflight](https://github.com/Svyable/Opps/commit/87b3482b3f3f0aa770c56475ba2b037a4250c60a) | Account `Svyable` committed an eligibility matrix | That applicant qualifies as established technical leader |

**Attribution result: NOT ESTABLISHED.** A shared organization/account commit identity is not sufficient to connect a named individual to leadership or original engineering. Do not turn a commit account into a résumé claim. No applicant-controlled identity, work authorization, references or availability verified in this audit.

## Applicant-ready technical exhibit (conditional on authorship confirmation)
**Problem:** An agent-generated execution receipt can appear consistent without proving an independent observer witnessed the side effect.

**Demonstrated repository progression:** a signed observation-envelope verifier, a replay counterexample, a SQLite-backed single-use receipt guard, and a separate-process disposable-file observer. Source links above; [historical test record](../opportunities/2026-11-17-taif-byte-matched-regression-verification.md) and [bounded two-process report](../LEDGER.md) contain prior isolated results. Those tests were **not rerun** for this exhibit.

**Research judgment illustrated:** distinguish signed claims from witnessed effects; reject replay; treat missing evidence as UNKNOWN rather than verified. **Known limitations:** parent-controlled signing key, shared host/filesystem, no adversarial isolation or external attestation, no evidence of deployment or reduction in catastrophic risk.

**Possible application narrative, only after the applicant verifies direct contribution:** “My technical interest is the failure mode in which agent execution logs are accepted as independent evidence. The Svyable research prototypes distinguish authentication, replay resistance and observation; they also show why a separate process is not equivalent to a trusted recorder. I would investigate evaluation designs that make these distinctions measurable under stronger adversarial boundaries.” Do not state “I built/led” until corroborated.

## Five documentary gates before November 22
1. Named applicant attests which exact commits, designs and tests they personally authored or directed, with dates and role; corroborate through signed commits, PR discussion, colleagues or independent artifacts.
2. One verifiable example of **senior technical leadership** beyond a collection of automated repository commits: team/project scope, decisions, measurable outcome, independent witness.
3. Full-time six-week-to-six-month availability, eligible work location/authorization, and conflict review with Svyable obligations.
4. Actual references who can attest to technical leadership; no fabricated names or contact.
5. Applicant reviews the official US/UK application and approves any submission; check current form, personal-data and employment terms.

**Decision:** If gates 1–3 cannot be evidenced before deadline, leave WATCH and do not submit. This is a **documented negative eligibility result**, not proof that the person is ineligible.

## Conservative economics and alternatives
Gross six-week compensation proxy = $350k–$500k × 6/52 = ~$40,385–$57,692. Incremental net benefit after displaced earnings, taxes and relocation is unknown. A further 1-hour evidence audit at illustrative $35/hour costs $35. Hypothetical retained benefit $10,000 gives break-even joint probability 0.35%; at hypothetical 1% and 5% probabilities EV would be +$65 and +$465 for **the whole success**, but these are not measured probabilities and cannot be credited as marginal probability uplift. **Actual marginal monetary EV unknown**; stop additional polishing without proof of qualification.

Other existing candidates: [TAIF](https://funds.effectivealtruism.org/funds/transformative-ai), typical $10k–$150k, rolling, high Control Evidence reuse, applicant/risk-pathway/IP/budget unresolved; [BlueDot Seed](https://bluedot.org/grants/seed), $20k–$200k, no fixed cutoff published, individual payee and special for-profit treatment, high reuse. Grant amounts are restricted project funding, not net profit.

No spend, submission, outreach, contract, IP assignment, or acceptance of terms.
