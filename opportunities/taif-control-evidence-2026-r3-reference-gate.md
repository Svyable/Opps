# EA Funds Control Evidence — independent reference gate and reviewer-integrity release

**2026-10-29 · $25,000 / 10-week proposed Transformative AI Fund pilot · PURSUE, not submitted.**

**Official sponsor:** https://funds.effectivealtruism.org/funds/transformative-ai — rolling applications; typical grants $10,000–$150,000. This is a proposed restricted research budget, not revenue awarded to Svyable.

## Material defect addressed

The prior two-arm analysis accepted a `PRIVATE_LABEL_KEY` with `expected_verdict` values derived from the *case-author manifest*. The proposed study, however, promises that a **third independent reference adjudicator (R3)** checks the evidence *before* the two experimental reviewers (R1/R2) are unblinded. Without a separate gate, the code could silently score R1/R2 against the author's expectations, even when no independent adjudication occurred. Passing unit tests would not expose that provenance error.

This patch adds a **fail-closed, declared-R3-only scoring path**:
- [independent_reference.py](../artifacts/control-evidence-2026/independent_reference.py) requires a private `PRIVATE_R3_ADJUDICATION` register with exactly one decision for each assigned case, matching frozen dataset binding, a distinct R3 identifier, a substantive rationale, a source-evidence digest for positive support/refutation, and declared coverage. It rejects author-label fields, missing/duplicate cases, mismatched bindings, same-reviewer duplicate arm assignments, unsupported positive labels, and partial-coverage support.
- `freeze_reference` produces a private `PRIVATE_LABEL_KEY` *from R3 decisions only*, with a SHA-256 commitment to the exact adjudication register. It uses blinded review IDs as internal pseudonymous case identifiers; it does **not** reconstruct source case IDs.
- `score_after_r3` calls the existing [paired analysis](../artifacts/control-evidence-2026/paired_analysis.py) and attaches the R3-register digest and an explicit provenance limitation. The CLI writes a **non-overwriting, mode-0600 private output**, not a public result.
- [test_independent_reference.py](../artifacts/control-evidence-2026/test_independent_reference.py) adds 12 synthetic regression tests; [CI workflow](../.github/workflows/control-evidence-contract.yml) invokes them. **Verified remote CI:** [GitHub Actions run 40888335435](https://github.com/Svyable/Opps/actions/runs/40888335435), commit `cabab2fa6890dbe4d58d2bf08dbb4c89b4c40273`, completed successfully on 2026-10-29. Job logs show **67/67 synthetic/unit tests passed** across six suites (14 + 9 + 11 + 11 + 10 + 12). This confirms software regression behavior only.

## Critical limit: this is an integrity gate, not authentication

`source_verified: true`, `coverage: complete`, `adjudicator_id: R3`, and `evidence_sha256` are **operator-provided declarations**. The module cannot prove that R3 is an independent human, that evidence bytes match a trusted recorder, that source timestamps are valid, that evidence coverage is complete, or that the reviewer was blinded. A SHA-256 digest only commits to bytes supplied to the tool; it is not a signature or chain of custody. No real human adjudication or agent telemetry has occurred.

The independent engineering work proposed for weeks 3–6 must still establish source authentication, tamper-evident capture, clock domains, a completeness witness, privacy permissions, and a frozen reference decision process. If any required R3 case is indeterminate, do not silently drop it: prospectively revise the dataset and binding, disclose the attrition, and rerun allocation. Never substitute the case author's `expected_verdict` for independent reference adjudication.

## Reproducible invocation (private local data only)

```bash
python artifacts/control-evidence-2026/test_independent_reference.py -v
python artifacts/control-evidence-2026/independent_reference.py \
  --assignment /secure/private-two-arm-assignment.json \
  --adjudication /secure/private-r3-adjudication.json \
  --responses /secure/private-r1-r2-responses.json \
  --output /secure/private-paired-result.json
```

The R3 register shares `schema_version`, `dataset_id`, `source_sha256` and `case_count` with the private assignment, sets `packet_type` to `PRIVATE_R3_ADJUDICATION`, includes `adjudicator_id`, and has `decisions` of exactly `review_id`, `verdict`, `evidence_sha256` (64 hex or null), `source_verified` (Boolean), `coverage` (complete/partial/unknown), and `rationale`. No real data, keys, identity or adjudications should be committed to GitHub.

## Funding and decision economics

This is a **reuse-heavy** improvement to the existing Control Evidence proposal; no new funded work package or budget line is asserted. The [40h / $4,000 three-role review plan](taif-control-evidence-2026-independent-reference-budget-repair.md) remains hypothetical. An incremental 1.5–2.5h engineering-and-audit effort at $35/h implies **$52.50–$87.50 pursuit cost** (assumption). No selection-probability uplift is evidenced; the prior illustrative **+$144.50** net-EV scenario is **not recalculated upward**. If one counted this new work as additional unsunk cost with no increase in selection odds, that scenario falls to **+$57.00 to +$92.00**. This does not establish a calibrated positive return, because applicant feasibility, true labor cost and reviewer availability remain unknown.

**Applicant-controlled stop gates:** legal recipient and tax/payee arrangements; 12h/week lead capacity; separate independent engineer and three review roles (R1, R2, R3); 40h reviewer budget; authentic permissioned telemetry; rights and privacy; live form terms; and explicit approval to submit. No outreach, hiring, expense, submission or contractual acceptance authorized.

**Decision:** Continue **PURSUE** only as a prepared rolling proposal. Do not claim independent validation or apply without truthful applicant facts. The next high-value action is real independent staffing/evidence access verification, not additional synthetic polishing.
