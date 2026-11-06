# EA Transformative AI Fund — evidence integrity and release decision (2026-11-06)

**Opportunity:** [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai). **Decision:** conditional PURSUE; do not submit. Official fund accepts rolling applications, typically $10k–$150k, rarely over $300k; prioritizes early-stage work reducing catastrophic risks from advanced AI. Svyable's existing proposed $25,000 Control Evidence request is inside the normal range, but this is not evidence of acceptance or of a catastrophic-risk impact pathway.

## Material technical finding from source review

The existing `artifacts/control-evidence-2026/contract_smoke.py` accepts `writer == "independent"` and `coverage_writer == "independent"` as ordinary string fields supplied inside the case. Neither field is cryptographically bound to a recorder identity, trusted execution context, immutable receipt, or independently verified coverage. `decide()` therefore cannot establish provenance: a party that controls input JSON can change `writer` from `agent` to `independent` and `coverage_writer` likewise. The existing `rapid_grant_baseline.py` explicitly constructs four attacks (fabricated writer label, identical replay, spoofed writer label, spoofed coverage), with expected verdict `supported` for each. **This is a source-level finding and expected test behavior, not a newly executed benchmark.** The local subprocess probe independently observes file bytes relative to its child process but is not an authenticated recorder and cannot close this boundary.

**Consequences for grant reviewers:** Do not describe the evaluator as secure against evidence fabrication, do not call the ten-case constructed fixture set an independent evaluation, and do not claim a measured reduction in catastrophic AI risk. The fundable research hypothesis is narrower: whether independently authenticated, action-scoped receipts and explicit coverage semantics can reduce false support for specific agent-action claims in controlled evaluations.

## Proposed measurable research gate before application

1. **Recorder trust boundary:** specify who controls the action process, receipt issuer, verifier, signing key, and case JSON. Keep the verifier's trust anchor out of agent-writable inputs. Define threat model and key-rotation/revocation assumptions.
2. **Replay defense:** bind a receipt to unique run ID, action ID, argument digest, outcome and verifier-issued nonce; reject duplicates and cross-run replays.
3. **Coverage defense:** require a separately authenticated completeness witness or abstain. A plain string field is insufficient.
4. **Blind test protocol:** freeze evaluator before an independent party creates holdout cases. Report numerator and denominator for false support, abstentions, and verified successful actions, with uncertainty; publish failures as well as successes.
5. **Safety relevance:** demonstrate a real agent workflow where an unsupported claim would otherwise cause an unsafe downstream decision, with human oversight and no external side effects. Distinguish this from global catastrophic-risk reduction, which would require an additional causal argument.

**Release conditions:** obtain actual baseline JSON and test logs; independently confirm applicant/payee identity, IP and disclosure rights, research hours, budget and nonoverlap with BlueDot or other grants; secure explicit approval before submission. Do not purchase compute, contact reviewers, or submit automatically.

## Commercial economics (subjective planning, not payer statistics)

Face request **$25,000 restricted grant**; use the existing ledger's **+$144.50 prospective EV** only as a historical subjective model, not a verified current expectation. No evidence in this review supports a probability uplift. This document costs an estimated 0.75h × $35/h = **$26.25**, so standalone incremental EV is **−$26.25** absent a demonstrable reduction in application error or better decision quality. Additional research should be undertaken only if the evidence can be produced cheaply and reused for both EA and commercial Control Evidence licensing. An authenticated provenance design and measured holdout result are potentially reusable IP, but no such system or measurement is claimed here.

**Payer credibility:** EA Funds reports $100M+ grants across its programs on its [official homepage](https://funds.effectivealtruism.org/); self-reported institutional totals, not a guarantee. **Terms:** charitable impact remit, fund discretion, eligibility/payee and grant restrictions require review before accepting an award. **Deadline:** rolling, no fixed close published on official fund page.

**Stop-loss:** If authenticated independent receipts and a credible advanced-AI risk pathway cannot be evidenced, move to WATCH rather than manufacture a stronger claim. 
