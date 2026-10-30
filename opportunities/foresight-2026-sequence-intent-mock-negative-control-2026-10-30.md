# Foresight Human Empowerment — executable sequence-level authority negative control

**2026-10-30 UTC | $35,000 proposed | PURSUE preparation only | deadline 2026-10-31 23:59 PDT | NOT SUBMITTED**

## Specific weakness addressed in the mock, not a deployed system

The original [per-call mock boundary](../artifacts/foresight-control-2026/gate_runner.py) grants each individually scoped action but has no cumulative authorization accounting. The [October 30 external-prior-art audit](foresight-2026-external-sequence-veto-evidence-2026-10-30.md) established relevance: a third-party PinkWallet sandbox benchmark records two repetitions of one $1,600 split-under-cap tactic. These are **third-party sandbox observations, not Svyable agent results**.

This update adds a [bounded-intent negative-control harness](../artifacts/foresight-control-2026/sequence_intent.py) and [13 regression tests](../artifacts/foresight-control-2026/test_sequence_intent.py). It retains the existing three study arms and compares two **diagnostic implementations within the enforced arm**: stateless per-call approval versus an in-memory cumulative-intent guard. This is **not** a fourth experimental arm or an observed effectiveness result.

## Reproducible mock contrast

One synthetic human intent permits at most **$1,000** total to a fixed mock target, within a simulated time window. Four calls of **$400** each reuse the same individually valid mock grant. The fixture uses integer cents and has no real payment or message side effects.

| Diagnostic | Synthetic accepted calls | Mock cumulative total | Interpretation |
|---|---:|---:|---|
| No gate | 4/4 | $1,600 | No authorization boundary |
| Cosmetic UI | 4/4 | $1,600 | UI does not enforce authorization |
| Enforced per-call only | 4/4 | $1,600 | Existing stateless mock allows an over-cap sequence |
| Enforced with bounded intent | 2/4 | $800 | Third and fourth calls blocked as cumulative total would exceed $1,000 |

The guard also checks canonical tool, exact target/actor, intent identifier, mock approver binding, grant revocation, intent validity, positive integer amounts, maximum operations, accepted operation-ID replay and accepted-call ordering. Blocked actions do not consume mock budget. The receipt digest includes operation ID and amount, but **a SHA-256 digest alone is not authentication or tamper-proof provenance**.

**Local test evidence:** 13/13 new regression tests passed in the isolated working copy. **Remote test evidence:** [GitHub Actions run 41058692751](https://github.com/Svyable/Opps/actions/runs/41058692751) completed successfully on 2026-10-30, with **57/57 Foresight tests** (44 prior + 13 new), confirmed from job logs. Reproduce with the Python unittest discover command for the foresight-control-2026 directory or run sequence_intent.py directly.

**Hard limits:** the guard is single-process, in-memory, sequential and not durable, concurrency-safe, authenticated, connected to an AI agent, integrated with real tool calls, independently audited or externally adopted. The human: field is an unauthenticated string. The fixture is constructed to expose a known failure; it does not measure real-world prevalence or improvement. The 60-case/180-assignment prospective study manifest remains unchanged and all agent assignments remain unrun.

## Funder criteria and payout gate

The official [Foresight AI Nodes RFP](https://foresight.org/grants/ai-science-safety-nodes-rfp/) and [Human Empowerment/Coordination track](https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/) specify **2026-10-31 23:59 PDT**, typical **$30,000–$100,000** grants (often smaller in Human Empowerment), and evaluation for RFP fit, x-risk impact, feasibility, AI-first execution, team capability and high-risk/high-reward potential. The sponsor accepts individuals and organizations, prioritizes meaningful SF/Berlin Node participation and open-source funded outputs. The proposed **$35,000** is an internal ask, not an award.

This harness improves the **specific technical credibility** of a previously unimplemented negative control, not applicant identity, staffing, rights, reference consent or in-person participation. No grant selection probability uplift is claimed.

### Conservative incremental economics

Prior founder-led favorable model: **$12,000 hypothetical economic surplus after funded obligations × 45% feasibility × 3.5% conditional selection − $140 initial application labor = +$49**. The preceding external audit cost of **$17.50–$35** reduced that to **+$14–$31.50** if additional. This implementation's incremental engineering labor is *not time-tracked*; assume **1–2 hours × $35/hour = $35–$70** opportunity cost. Without demonstrated selection uplift, cumulative favorable EV becomes **−$56 to −$3.50**; at 25% feasibility it is more negative. A 0.65–1.30 percentage-point increase in *conditional selection probability* would be needed to offset just this $35–$70 increment at $12k surplus and 45% feasibility. No empirical basis supports assigning that increase.

These are subjective screening scenarios, **not calibrated award odds or $35,000 profit**. Completed engineering is sunk for the next decision. Do not spend more time polishing without resolving applicant-controlled gates.

### Submission release decision

**PURSUE preparation; no submission authorized.** Applicant must confirm legal recipient and tax suitability, actual 12–20h/week availability, independent engineer and reviewer, consenting reference, code/data rights, credible SF/Berlin Node participation, overlap with EA Funds/BlueDot, live form fields and sharing/consent choices, and explicit approval. If gates cannot be truthfully cleared before the deadline, **do not submit**. No outreach, application, spending, contract or terms acceptance occurred.
