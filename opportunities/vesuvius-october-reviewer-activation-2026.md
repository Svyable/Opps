# October 2026 Vesuvius — independent review activation (PURSUE)

**Prepared, not sent.** Official October best-progress prize: $20,000, deadline 2026-10-31 23:59 Pacific: https://scrollprize.org/prizes

## Existing real-data evidence
ScrolIQ's PHercParis4 run attached 2,111/2,232 points, flagged 6/16,074 constraints, and detected 194/200 deliberately injected +2 errors. The six flags reduce to **five** distinct native VC3D review markers. These are **review cues, not proven errors**. Source and hashes: https://github.com/Svyable/scrollq/tree/main/artifacts/2026-10-03-paris4-winding-attachment

Native marker file: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/vc3d-review-points.json
Review protocol: https://github.com/Svyable/scrollq/blob/main/docs/vc3d-review-bundles.md

## Reviewer request — draft, not sent
Please load the five PHercParis4 markers in VC3D against the matching CT and patch geometry. For every marker, record `scroliq_review_status` as `annotation_corrected`, `patch_issue`, `no_issue`, or `uncertain`, and a nonempty `scroliq_review_note`. If a winding annotation is demonstrably incorrect, change only its winding value; do not move the marker or alter provenance tags. Save the native reviewed PointCollections JSON and record reviewer identity, timezone-aware completion timestamp, and actual review minutes. A negative or uncertain result is useful.

## Acceptance gate
1. Load the committed marker file using VC3D `vc3d_load_points_json` with the matching scroll.
2. Ingest actual reviewer decisions with `scroliq-vc3d-review-ingest`, binding to the original diagnostic.
3. **Only if** a relative-winding correction is confirmed, apply with `scroliq-winding-apply-review` to a *new* file; rerun the same diagnostic with all other inputs unchanged; compare with `scroliq-winding-review-compare`.
4. Require measured improvement, unchanged-input proof, valid injection controls and reproducible standard-format artifact before prize nomination. Do not claim a fit improvement, corrected annotation, ink discovery or community uptake without evidence.

**Budget and stop:** up to 8h × $35/h = $280. Illustrative EV = $20,000 × .90 assumed eligibility × .03 assumed conditional win − $280 = **+$260**. This is not a calibrated forecast. **Submission gate: NO** until independent review and, where applicable, controlled comparison exist. No registration, submission or contract authorized.
