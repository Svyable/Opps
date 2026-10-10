# PHercParis4 — bounded VC3D independent review work order (2026-10-10)

**Prepared, not sent. No independent review or corrected geometry is claimed.**

## Frozen evidence and why this matters

- ScrolIQ source: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/vc3d-review-points.json
- Git blob SHA: `ca2d623afdb601bceaa215ebec622db47617120f`
- Embedded diagnostic source SHA-256: `5ff4330182324c5cd7a9334f0a7eeb712c1e70a155c6dbca28e1e8d8cb6701fe`
- Context: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/README.md
- Native VC3D PointCollections v1: five review markers for six flagged constraints, **not five proven errors**. XYZ below are level-0 voxel coordinates.

| Priority | Frame / source point | XYZ | Original winding | Flagged residual | Review question |
|---|---|---|---:|---|---|
| 1 | relative:198 / 2233 | 4845.294, 3449.741, 11372.407 | 3 | −2 | Nine attachments; none exactly agrees. Is the annotation wrong, or do patches cross windings? |
| 2 | relative:280 / 2860 | 5223.010, 3607.992, 11825.363 | 8 | −2 | Single attachment. Can CT evidence distinguish annotation from patch error? |
| 3 | relative:242 / 2549 | 5007.217, 3022.627, 11494.725 | 4 | +2 | Two near patches disagree; inspect both patch surfaces. |
| 4 | relative:227 / 2445 | 5255.700, 3610.183, 12125.700 | 1 | −5 | Four of five attachments agree; test patch-side conflict. |
| 5 | relative:166 / 2024 | 5401.597, 4463.881, 10728.110 | 10 | −2, −2 | Nine closer patches agree; inspect two farther patches before touching winding. |

Priority is a hypothesis based on the committed post-hoc context, **not a new result**.

## Reviewer handoff (draft only)

Open the matching PHercParis4 CT and patch geometry in VC3D, then load the exact native JSON with `vc3d_load_points_json`. For each inspected marker, set one `scroliq_review_status` from `annotation_corrected`, `patch_issue`, `no_issue`, `uncertain`, plus a nonempty `scroliq_review_note`. Change `wind_a` only when the annotation is independently demonstrated wrong; preserve coordinates and provenance tags. Save reviewed native JSON; provide reviewer identity, timezone-aware completion time, and actual review minutes. Negative and uncertain findings are useful.

**Time gate:** prioritize first two markers within 60 minutes; stop review after 120 minutes absent CT-supported corrections. Total prize pursuit remains capped at 8h/$280. Do not spend on a blind rerun.

**Proof gate:** use `scroliq-vc3d-review-ingest` for real reviewed decisions. Only confirmed `annotation_corrected` decisions may feed `scroliq-winding-apply-review` to a new file. Then rerun the frozen diagnostic and compare with `scroliq-winding-review-compare`, requiring unchanged non-winding input hashes, positive controls, and a measured improvement. Full instructions: https://github.com/Svyable/scrollq/blob/main/docs/vc3d-review-bundles.md .

**Prize submission gate: NO.** Official October 31, 2026, 23:59 Pacific deadline: https://scrollprize.org/prizes . A $20,000 monthly best award exists, but no payout is guaranteed to Svyable. Judges expect an actionable advantage on real scroll data, documentation, standard formats and evidence of utility. No outreach, registration, submission, spend, or contract acceptance authorized.
