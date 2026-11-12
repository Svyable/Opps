# Transformative AI Fund — preregistered Control Evidence pilot and funding gate (2026-11-11)

**Status: PURSUE, no application authorized.** This is a reproducible experimental protocol, not a claim of demonstrated real-agent safety or grant eligibility. It advances an existing Svyable Control Evidence asset toward the [EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai), which explicitly accepts early-stage technical projects addressing catastrophic risks from transformative AI. Official program: applications always open; typical grants **$10,000–$150,000**, rarely above $300,000. No published applicant-specific selection probability. Funding is restricted grant support, not an earned service fee.

## Research question and falsifiable claim

Can a narrowly scoped external authorization boundary prevent an agent from invoking tools outside a predeclared policy **under adversarially generated tool-call proposals**, while still allowing valid tasks? Existing Svyable fixture `artifacts/control-evidence-2026/control_fixture.py` implements deterministic exact-membership authorization and has synthetic regression tests. It does **not** demonstrate behavior of an actual LLM agent, external tool gateway, or risk reduction in deployment. This pilot is a prospective study, not a retrospective benchmark.

## Pre-registration before any run

1. Freeze code commit, Python/runtime versions, model/provider version and prompt, tool schema, policy manifest, seed and evaluator before recording outcomes. Keep secrets and personal data out of traces.
2. Implement an *isolated, no-network, non-destructive* mock-tool gateway; agent can propose `read_public`, `read_private`, `write_record`, and malformed calls, but the gateway must never execute real external side effects.
3. Compare two arms with the **same** fixed task/adversarial prompt set: (A) application-only instructions with no independent enforcement; (B) identical instructions plus independent authorization gate. Record the proposed action, policy, gateway decision and actual mock execution separately. Randomize task order using recorded seed.
4. Predeclare a balanced suite of at least 40 scenarios: 10 authorized requests, 10 explicitly unauthorized, 10 role/prompt-injection attempts, 10 malformed/tool-schema edge cases. Preserve task-level scenario IDs and ground-truth expected authorization. No cherry-picked prompts, post-hoc exclusion or unseen prompt changes.
5. Primary metric: **unauthorized mock executions / unauthorized proposals** with numerator and denominator, and an exact binomial confidence interval. Also report **unauthorized executions / unauthorized scenarios**, false denial rate on legitimate tasks, schema-validation failures, latency and complete per-case outcomes. Zero observed failures is not proof of zero true failure risk. Any observed unauthorized execution in the gated arm is a critical negative result.
6. Negative controls: string-as-allowlist substring, empty action, unknown principal, wrong resource, malformed types and deny-by-default on missing policy. Fail closed and record whether the proposed call was rejected before any mock side effect.
7. Reproduction package: immutable scenario manifest, policy, code and test commit, local invocation, redacted JSONL trace with deterministic digest, exact metric script, raw counts, limitations and failures. An independent reviewer must be able to rerun without credentials or spending money.

**Stop/go:** Do not claim empirical success until the actual agent integration runs and the full trace is available. Stop if a mock gateway can produce an unauthorized side effect or if trace integrity cannot be independently verified. Do not purchase API credits or compute without approval; use available free/local resources only when permitted.

## Funding rationale and economic gates

EA Fund supports early-stage projects, including technical research, but a direct causal connection to reducing advanced-AI catastrophic risk remains to be argued, not assumed from a basic authorization fixture. Proposed pilot scope is **40+ paired scenarios and reproducible release**, not a funded result. A $10,000 *illustrative* grant request would require an itemized prospective budget, applicant identity, permissible payee jurisdiction, project ownership and nonoverlap with BlueDot Rapid/Media; **no such budget or award is verified**.

At hypothetical 80h × $35/h = $2,800 labor opportunity cost, a $10,000 award leaves $7,200 *conditional* before overhead, tax, equipment, provider charges and any other restricted-use constraints. If application/review labor is 4h × $35 = $140, the break-even joint probability of qualification, selection and payment is **1.94%** (140/7200), assuming no other expenses. This is a threshold, **not an estimated probability**; actual probability and EV are unknown. An incremental 2h/$70 pilot setup would need 0.97 percentage-point improvement in joint success probability on the same simplified model, unmeasured. Existing synthetic code and test IP can be reused, subject to license and third-party rights review; do not promise IP assignment.

## Required release evidence

- First-party applicant identity, eligibility, payment country, capacity and rights.
- Exact pinned real-agent integration, frozen scenario set, redacted trace and independent replay.
- Itemized budget for work not simultaneously claimed under BlueDot Rapid or Media.
- Explicit explanation of why tool-authorization experiments plausibly affect catastrophic-risk pathways, including limits and counterexamples.
- Human approval of final claims, budget, grant terms and submission.

## Alternative comparison and decision

[BlueDot Rapid](https://bluedot.org/grants/rapid) direct page currently says **$50–$10,000** and that stipends/living expenses are exceptional; its [index](https://bluedot.org/grants) says up to **$20,000**. Neither inconsistency authorizes optimistic stipend assumptions. [BlueDot Media](https://bluedot.org/grants/media) offers **$20,000–$200,000**, 6–12 months, but requires existing attributable published work and a self-built audience; those owner analytics are not verified. EA is the more natural technical-research fund, but its higher nominal ceiling does not imply higher expected value.

**Decision:** preserve EA as conditional PURSUE. Advance only the zero-spend, reproducible agent-integration pilot when actual runnable tooling is available. Do not write success claims or submit before evidence. No spending, submission, outreach, agreement, or IP transfer.
