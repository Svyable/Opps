# TAIF reviewer gate: causal pathway and falsification plan (2026-11-18)

**Status: PURSUE / HOLD. Unsubmitted, not an eligibility determination.** Supplements [conditional $25k proposal](2026-11-18-taif-conditional-independent-observation-pilot.md). No new empirical test is claimed.

## Why the existing application is not yet compelling
EA Funds' [Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) prioritizes early-stage work reducing global catastrophic risks from advanced AI, not generic audit tooling. The existing two-process observer demonstrates only a disposable file operation on one host; the parent controls key custody. This does not show that an untrusted agent cannot forge evidence or that downstream decision-makers act on it. The application must not equate receipt integrity with catastrophe prevention.

## Narrow, testable theory of change
**Target decision:** a safety evaluator considering whether to grant a tool-using AI agent additional authority should not accept an agent-produced receipt as independent evidence of action. **Intervention:** a public, reproducible falsification harness that labels evidence VERIFIED, REJECT or UNKNOWN based on a separately controlled observer, not on self-attested recorder identity. **Immediate measurable output:** detection of fabricated or missing execution evidence under an explicit adversary model. **Intermediate outcome (unproven):** at least one independent evaluator can reproduce the finding and incorporate the test into an agent evaluation or deployment gate. **Long-run relevance (speculative):** reducing false assurance may improve decisions about deploying highly capable agents; no numerical catastrophic-risk reduction is estimated.

## Pre-registered acceptance matrix (planned, not run)
| Scenario | Expected result | Required independent evidence |
|---|---|---|
| Authorized disposable-file write | VERIFIED once | Observer-owned digest and durable unique event ID |
| Same signed receipt presented twice | REJECT second time | Atomic replay ledger |
| Executor invents recorder identity | REJECT | Executor cannot access recorder authentication key |
| Modified action/path or content | REJECT | Observer-side allowlist and file digest |
| No action / recorder unavailable | UNKNOWN, never VERIFIED | Missing-event and crash logs |
| Recorder key stolen or shared-host root compromised | UNKNOWN / explicitly out of threat model | Document inability to guarantee provenance |

**Acceptance gate:** run exact committed bytes in a clean environment; record Python version, commit SHA, full command, stdout/stderr and exit code. Repeat a minimum of 10 independent trials per in-scope scenario, with no false VERIFIED in negative cases; report confidence limits rather than claim zero real-world failure probability. Use a separate recorder with secret not available to the executor, and independent disposable file-state inspection. The earlier 3/3 two-process local tests are historical and used a parent-owned key; they do not meet this gate.

## Commercial stop/go and applicant-controlled gates
Official TAIF: [fund page](https://funds.effectivealtruism.org/funds/transformative-ai), rolling applications, typical $10k–$150k, credible EA Funds team; [application](https://funds.effectivealtruism.org/apply-for-funding). Proposed $25k restricted grant is not $25k personal profit. Before applying verify (1) individual/legal payee and jurisdiction, (2) permission to use and publish each code artifact, (3) six-week availability, (4) exclusive eligible budget against BlueDot Seed, (5) actual alignment with fund's advanced-AI catastrophic-risk priorities, (6) grant terms and reporting, and (7) independent evaluation adoption or reviewer feedback. No third-party contact authorized.

**Risk-adjusted decision:** reuse of Control Evidence, observer and replay guard is high. A bounded next experiment is 4 hours at illustrative $35/hour = $140 labor and zero external spend. With a *hypothetical* $5,000 retained net benefit after delivery, marginal break-even joint eligibility-and-award probability is 2.8%; at 1% assumed success EV = -$90 and at 5% = +$110. Neither is an estimated probability; incremental win probability and actual cash EV remain unknown. Stop further application polish if independently controlled observation or plausible evaluator adoption cannot be demonstrated. Do not submit or accept terms without approval.

## Competing paths checked (2026-11-18)
- [BlueDot Seed](https://bluedot.org/grants/seed): $20k–$200k for first 6–12 months, ~4-week decisions, no fixed cutoff; individual payee by default, for-profit public-benefit scrutiny, monthly reporting and return of unspent funds. Existing six-week engineering plan alone does not satisfy a 6–12 month new-project case. WATCH; high reuse but additional program-design and eligibility work.
- [Anthropic Residency](https://alignment.anthropic.com/2026/anthropic-residency/): Nov 22, 2026 deadline, $350k–$500k annualized prorated for six weeks to six months; potentially high personal payoff but established technical-leadership, full-time availability, references, work rights and application-stage legal consent are unverified. WATCH / urgent applicant-controlled decision; no unsupported application claims.
- Five frontier benchmark lanes remain tracked in the [campaign](2026-11-07-frontier-five-benchmark-campaign.md). Monetary prizes are not verified; no positive cash EV assigned.

**No submission, third-party contact, money spent, agreement or IP transfer.**
