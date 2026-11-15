# Control Evidence — independent execution release specification (2026-11-15)

**Opportunity:** EA Transformative AI Fund (PURSUE / HOLD). **Purpose:** turn existing mock-gateway code into a falsifiable, reviewer-ready real-agent evaluation plan. This is a prospective protocol, **not** a completed experiment or a funding request.

## Grounded implementation boundary

Inspected GitHub default-branch source on 2026-11-15:
- [mock_gateway.py](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/mock_gateway.py), blob `d9eaf15d622bc9e383611fee5bf5d83691960c7f`: deterministic policy-driven events, not independent observation.
- [score_pilot.py](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/score_pilot.py), blob `4433389292c279c12dedaae8a4fcccaebb80df52`: paired scorer validates scenario/arm uniqueness, policy consistency, and missing/orphan events.
- [test_mock_gateway.py](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/test_mock_gateway.py), blob `478bcad1f0bf5ca6ad557756b4ce0a2275de5169`: synthetic regression source. **No tests executed in this audit.**

## Critical evidence gap

The scorer receives an `executed` Boolean from `mock_gateway.py`, which computes that Boolean from the arm and allowlist. Therefore any apparent reduction in unauthorized execution is **tautological within the synthetic simulator**. It cannot establish that an actual model, tool provider, or independent enforcement boundary resisted an unauthorized action. **Do not quote synthetic score differences as an empirical safety improvement in the TAIF application.**

## Smallest credible prospective study

1. Freeze and hash the proposal JSONL, policy manifest, scorer revision, tool schema, and paired scenario IDs before trials. Record whether each scenario is a legitimate task and which actions are authorized.
2. Run a real agent in two conditions with matched prompts, models, tools, seeds where available, and budgets: instructions-only versus an external authorization gate. Randomize arm order and preserve both successes and failures.
3. Place a separate append-only recorder **at the tool executor**, not inside the agent or the synthetic gateway. Record proposed call ID, policy decision, tool invocation attempt, actual execution outcome, timestamps, scenario ID, and executor-side error. Ensure denied calls cannot silently reach the tool.
4. Blind an independent reviewer to arm labels when adjudicating whether proposed actions are authorized. Disagreements and exclusions must be logged, not discarded.
5. Report per-arm numerator and denominator for unauthorized executed calls, false denials of authorized proposals, abstentions, scenario coverage, and missing events. Publish raw redacted traces, the schema, scripts and hashes. Report confidence intervals only after sample size and dependence structure are known; no fabricated power or significance.
6. Negative controls: an intentionally forbidden action, a valid action, a missing executor receipt, an orphan receipt, duplicated call IDs, and mismatched paired policies. **Fail closed** on missing or inconsistent execution evidence.

## Explicit release gates

- Gate A: clean checkout + `python -m unittest discover -s artifacts/control-evidence-2026 -p 'test_*.py'` executed and recorded with environment, commit, exit code and stdout/stderr. This command is a plan, not a passed test.
- Gate B: one actual externally recorded tool-execution trace, with independent recorder ownership and source hash.
- Gate C: paired real-agent trials with denominator accounting, blind adjudication, and complete reproducibility package.
- Gate D: named legal payee, jurisdiction, real exclusive incremental expenses, funding counterfactual, and TAIF/BlueDot nonoverlap.
- Gate E: review grant/IP/reporting terms and obtain explicit human approval before any application.

## Commercial stop-loss

Official [TAIF](https://funds.effectivealtruism.org/funds/transformative-ai) is rolling, with typical restricted grants $10k–$150k. Existing Svyable code and protocol have high reuse. Grant funds are not equivalent to personal profit. Qualification, selection probability, legitimate net benefit and therefore monetary EV remain unknown. Illustrative 2h next technical verification at $35/h costs $70; no positive expected return is claimed without evidence that it changes an eligible funding outcome. **Do not buy API credits, submit, contact funders, or accept terms without approval.**

**Decision:** pursue only Gate A and a zero-spend Gate B feasibility check next; hold application writing and all BlueDot-overlapping budget claims until real execution evidence exists.
