# BlueDot Rapid — falsifiable recorder-authenticity negative control

**Prepared 2026-10-30 · Svyable / Sven Hardy Benson · BlueDot Rapid PURSUE preparation only · NOT SUBMITTED.**

## Why this changes the funding evidence

The [current official Rapid Grants page](https://bluedot.org/grants/rapid) offers up to **$20,000**, including research time/living costs, for work already underway. It asks for evidence the applicant can make progress and a clear role for funding. The existing [four-week $6,000 proposal](bluedot-rapid-2026-recorder-integrity-four-week-preflight.md) previously described an unauthenticated local supervisor but did not isolate the *exact current failure* in an executable adversarial control.

This preflight supplies that missing falsifiable boundary: [five deterministic tests](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py) exercise the existing [synthetic contract](../artifacts/control-evidence-2026/contract_smoke.py) and [local subprocess probe](../artifacts/control-evidence-2026/local_tool_receipt_pilot.py). They are **characterization tests of a known gap**, not security success tests.

| Constructed input | Current contract behavior (test expectation) | What it means |
|---|---|---|
| No process run; event and coverage strings both say `independent` | `supported` | A self-declared role is not proof of recorder origin |
| Replay the same fabricated case unchanged | `supported` again | No nonce, freshness or replay state |
| Change event writer from `agent` to `independent` | `insufficient_evidence` becomes `supported` | Role string is spoofable in an untrusted input |
| Change coverage writer from `agent` to `independent` | `insufficient_evidence` becomes `supported` | Completeness witness also lacks origin authentication |
| Actual local subprocess success versus constructed success | Both `supported` | Current verdict grammar cannot distinguish provenance |

These tests **do not demonstrate an exploit against a production recorder**; the contract is intentionally synthetic and has no claimed adversarial trust boundary. They document why a grant-funded recorder-authentication experiment is necessary. They must be revised when a real verifier is implemented so that forged and replayed inputs are rejected or lead to abstention.

## Fundable next work (not completed or billed)

1. Define recorder/worker threat model, run identity, independent observation authority, and allowed failure modes; freeze an adversarial matrix before implementation.
2. Implement a supervisor-owned run binding (nonce or equivalent), a verifier that does **not** trust event-supplied role labels, and a replay policy with explicit persistence/concurrency limitations.
3. Re-run these five controls plus tampering, missing observation and scope-binding cases; target **zero false support on constructed forged/replayed inputs**, with denominators and failures published.
4. Obtain independently permissioned local reproduction if a reviewer is actually available; do not claim one exists. Report limitations and stop/go decision before any real-agent integration.

**Non-overlap:** The five characterization tests and this preflight are **pre-existing unfunded application evidence**, not new grant-billable work. The proposed $6,000 / four-week budget remains prospective: 60 unverified founder hours, 10 uncontracted reviewer hours, $500 capped resources/packaging. It is distinct from EA's blinded human adjudication, Foresight's human-veto arms and Seed's six-month SDK adoption. No costs are authorized.

## Economic decision and gates

For the Rapid grant, keep the previous **illustrative** founder-surplus model: cautious $1,500 × 40% qualification/capacity × 5% selection − $70 preparation = **−$40**; central $2,000 × 60% × 8% − $70 = **+$26**; favorable $3,000 × 70% × 10% − $70 = **+$140**. This preflight adds an estimated **0.5–1.0 hour × $35/hour = $17.50–$35** of research labor. If all costs are treated as still-to-be-recouped, revised cumulative sensitivity is **−$75 to −$57.50 cautious; −$9 to +$8.50 central; +$105 to +$122.50 favorable**. No award-probability uplift is assumed: it would need to be empirically supported, and all probabilities are subjective.

**Still blocked:** applicant's 15 hours/week, lawful payee/jurisdiction, actual source/contributor rights, funder overlap, exact application fields and explicit authorization to submit. The official page states a lump-sum payment follows an approved claim and checks; the grant is restricted to agreed work, with a completion report due within 60 days. Do not submit, spend, hire or contact anyone on this preflight.

**Sources rechecked 2026-10-30:** https://bluedot.org/grants/rapid ; https://funds.effectivealtruism.org/funds/transformative-ai ; https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/ .
