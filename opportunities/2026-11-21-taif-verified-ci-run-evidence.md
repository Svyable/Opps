# TAIF Control Evidence — independently retrievable CI evidence (2026-11-21)

## Decision
**PURSUE / HOLD**, existing Transformative AI Fund opportunity; do not duplicate the ledger entry. A previous blocker — no verified exact-checkout CI — is now resolved. This is reproducible *negative-control evidence*, not independent action attestation or proof of advanced-AI-risk reduction.

## Verified run
- [GitHub Actions run 44852961142](https://github.com/Svyable/Opps/actions/runs/44852961142), push event, commit [f5fb99ac71f395e4cce16f274f026e292fa3a4d1](https://github.com/Svyable/Opps/commit/f5fb99ac71f395e4cce16f274f026e292fa3a4d1), 2026-11-21 01:55 UTC; GitHub API conclusion **success**.
- [Python 3.11 job 136688385246](https://github.com/Svyable/Opps/actions/runs/44852961142/job/136688385246): CPython 3.11.18; checked-out syntax compilation successful; six named unittest cases **PASS**, 0.202s.
- [Python 3.13 job 136688385448](https://github.com/Svyable/Opps/actions/runs/44852961142/job/136688385448): CPython 3.13.18; checked-out syntax compilation successful; six named unittest cases **PASS**, 0.125s.
- Direct job logs were fetched, not inferred from a PR-only workflow lookup. Both logs include the same six cases: authorized write, missing execution, post-precheck matching-byte injection with executor omitted, preexisting matching file, preexisting without execution, substituted file.
- Runner warnings: Node.js 20 deprecation / forced Node.js 24 for checkout@v4 and setup-python@v5; not observed test failures. Do not overinterpret the pass.

## Reviewer-safe claim
On the committed code, six deterministic observer tests passed on two Python versions, including a negative control in which matching file bytes appear without the authorized executor. The result is **OBSERVED_ONLY**, not an authenticated execution event. The suite documents why file-state matching cannot establish action provenance. This is a bounded falsification demonstration, not a general-purpose security guarantee.

## What remains unproven
No isolated signing-key custody; no independently trusted action identity or event correlation; no adversarial isolation across host/principal boundaries; no empirical measure of catastrophic-risk reduction; no independent replication beyond GitHub-hosted CI. The tests do not validate a solution to those problems. Submission should propose measurable follow-up research and disclose these limitations.

## Commercial assessment and stop/go
Official [Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai): continuously open; typical $10k–$150k early-stage grants, with priority for advanced-AI catastrophic-risk reduction. Conditional Svyable request $25,000 restricted research funding, not profit. [EA Funds](https://funds.effectivealtruism.org/) reports $100M+ historical grants. Reuse: existing Control Evidence source, six regression cases, CI infrastructure, research narrative. Eligibility, ownership/IP permissions, detailed budget and causal safety relevance remain to verify; funding selection odds unknown. Illustrative incremental verification labor 0.5h at $35/h = $17.50, no outside spend. At hypothetical $5,000 retained economic benefit, a **0.35 percentage-point** incremental success-probability improvement would cover that labor; no evidence quantifies such an improvement, so monetary EV remains unknown.

Compared with [BlueDot Seed](https://bluedot.org/grants/seed) ($20k–$200k, ~4-week decision, 6–12 month plan, monthly updates and return of unspent funds), [BlueDot Media](https://bluedot.org/grants/media) ($20k–$200k, published work/audience qualification unverified), and [BlueDot Rapid](https://bluedot.org/grants/rapid) ($50–$10k on program page, cash bottleneck not established; index says $20k), TAIF currently offers the clearest reuse of an existing technical project without requiring fabricated audience credentials or speculative equipment spending.

**Next decision:** prepare a falsifiable pilot budget, named applicant and rights evidence, and an explicit causal theory of change. Only submit after approval. Maintain all five frontier benchmark lanes as separately tracked, cash-unpriced research; do not claim prize dollars from scores.

No application submitted, outreach, purchases, contracts, terms acceptance, or IP transfer.
