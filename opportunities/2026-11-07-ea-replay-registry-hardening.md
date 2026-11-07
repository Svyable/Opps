# EA Transformative AI Fund — cross-call replay integrity gate (2026-11-07)

## Actual defect and repair

Existing `artifacts/control-evidence-2026/verified_claim.py` initialized `used = set()` **inside every `decide_verified` call**. Although one call rejected duplicate receipt nonces, an identical signed action and coverage receipt could be presented in a later call and scored again. This contradicts any claim of durable replay protection.

**Code change:** `decide_verified(..., used_nonces=None)` now requires a caller-owned set and returns `insufficient_evidence` if no set is provided. It consumes coverage and action nonces into the same provided registry. Added regression cases for repeated calls, absent registry and malformed receipt collection; total `test_verified_claim.py` test methods: **12** (previously nine). This is an API behavior change; the only known committed callsite is the test suite. All runtime consumers must supply the same registry across calls. A process-local set is still **not durable across restarts or concurrent workers**. A production implementation requires transactional uniqueness constraints, scoped authenticated run identifiers, and a protected recorder/key boundary.

**Evidence limitation:** Commits were accepted by GitHub but the updated combined source has **not** been independently executed or confirmed by CI in this run. The twelve test definitions are not twelve passing results. The prior 9/9 local suite was for an older version.

## Funding and stop-loss

Official fund: https://funds.effectivealtruism.org/funds/transformative-ai. Rolling; typical awards $10k–$150k; proposed Control Evidence pilot $25k **restricted research funding**, not personal profit. Existing technical asset reuse is high, but independent trusted recording, blind adjudication, participant/payee eligibility, IP rights and budget nonoverlap are unresolved. This patch fixes a specific internal logic flaw, not a demonstrated real-world security property.

At a hypothetical 0.5 hour × $35/hour, labor opportunity cost is **$17.50**. No measured uplift in grant award probability. Incremental cash EV is **−$17.50** absent any demonstrated probability improvement or reusable value. Break-even on the full $25k face value requires 0.07 percentage-point joint award-probability uplift; using conditional founder economic surplus requires more. No assertion of a positive EV or award probability increase.

## Immediate technical gate

Execute `cd artifacts/control-evidence-2026 && python3 -m unittest -v receipt_boundary test_verified_claim` against committed SHA; record run ID, raw stdout and source SHA. Then design and test a transactional replay store across process restarts, not a mere set, and independently attest recorder coverage. Stop engineering spend if no independently verified progress or applicant eligibility.

No application, paid compute, external contact or terms acceptance.
