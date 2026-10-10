# Vesuvius October 2026 Progress Prize — acceptance gate

Status: **PURSUE**, with **8-hour incremental experiment cap**. This is a submission-readiness artifact, **not a submitted entry or a claim of measured improvement**.
Verified source (2026-10-09): https://scrollprize.org/prizes
Deadline: **2026-10-31 11:59 p.m. Pacific**.
Prize: **$20,000 best submission of the month**; other discretionary progress awards typically $250–$20,000. Organizer: Scroll Prize, Inc. Judging discretionary; permissive open-source license required to accept a prize.

## Narrow ScrollQ claim to test

ScrollQ/ScrolIQ's evidence-passport and failure-case diagnostics might make a **specific, reproducible failure mode** in Vesuvius surface prediction, virtual unwrapping, or ink detection easier to identify and repair. This hypothesis is unproven until demonstrated on actual public scroll data.

## Organizer-to-evidence acceptance matrix

| Official requirement / preference | Evidence needed before pursuing submission | Pass condition |
|---|---|---|
| Address a specific problem using Vesuvius scroll data | Public dataset URL, volume/segment ID, license, exact file SHA-256 and failure coordinates | Third party can locate identical data and observed failure |
| Demonstrate significant advantages | Baseline command and results; ScrollQ command and results; matched before/after visuals, metrics, logs | Nontrivial measured or visually unambiguous improvement on same data |
| Reveal actionable information | Failure classification, probable cause, remediation suggestion and evidence passport | Someone can use diagnosis to change a workflow or fix a bug |
| Standard formats / modular integration | Zarr/OME-Zarr or tifxyz/mesh inputs as appropriate; documented output schema | Existing community workflow can ingest artifact without bespoke manual steps |
| Comprehensive documentation | README, one-command example, expected outputs, dependency pinning, reproducibility notes | Fresh environment runs end to end |
| Early release and community usage | Public code link and timestamp; feedback/issue/reproduction links | Independent community engagement documented honestly (never invented) |

## Experiment plan: hard stop after eight hours

1. **Hour 0–1:** select one publicly available Vesuvius scroll data example and pin provenance. Do not download huge volumes without first estimating transfer/storage.
2. **Hour 1–3:** reproduce one concrete error/failure and record baseline outputs.
3. **Hour 3–5:** run ScrollQ diagnostic and export evidence passport + images/metrics.
4. **Hour 5–7:** compare against baseline, verify negative control and independent rerun instructions.
5. **Hour 7–8:** decide GO only if the real-data improvement is concrete, reproducible and relevant to reading scrolls; otherwise stop or reframe as a non-prize open-source contribution.

## Submission outline — fill only with verified evidence

- Problem and exact public dataset: **PARTIAL** — PHercParis4 source diagnostic and native VC3D markers are committed, but this packet does not pin a complete public CT download/volume identity for a new third-party rerun.
- Baseline failure and reproduction: **PARTIAL** — 2,111/2,232 attached points; 6/16,074 flagged constraints; 194/200 deliberately injected +2 errors detected. Flags are review cues, not independently proven annotation mistakes.
- ScrollQ improvement / quantified delta: **NOT DEMONSTRATED** — five native VC3D markers exist, but no confirmed correction and no controlled downstream benefit have been established.
- Reproducibility commands and artifact checksums: **PARTIAL** — marker Git blob `ca2d623afdb601bceaa215ebec622db47617120f`; diagnostic source SHA-256 `5ff4330182324c5cd7a9334f0a7eeb712c1e70a155c6dbca28e1e8d8cb6701fe`; `scroliq-vc3d-review` documented. Independent rerun not recorded.
- Open-source license and public repository: **VERIFIED** — ScrolIQ public repository has MIT `LICENSE`.
- Independent community use / feedback: **NOT VERIFIED** — no independent adjudication, reviewed VC3D bundle, or externally documented use has been established by this audit.
- Final prize form: **NOT SUBMITTED**

## Marginal EV gate

Illustrative $20,000 first-prize scenario: 90% eligibility × 3% conditional win probability × $20,000 − 8 hours × $35 = **+$260**. The 3% win probability is a screening assumption, not a measured estimate. If work rises to 20 hours with the same odds, EV becomes **−$160**. Prize award is discretionary; taxes and potential computing costs not included.

**Authorization boundary:** No registration, prize submission, spending, or contractual acceptance without explicit approval. General progress contributions may be public, but milestone discoveries involving newly read text have additional non-disclosure conditions; check prize category before publication.

## Source-bound October 10 readiness correction

The earlier checklist was stale: the public ScrolIQ repository already contains real-data winding diagnostics, a native review export, documentation, and an MIT license. This update separates **existing measured diagnostics** from the still-missing **prize-grade actionable advantage**.

- Frozen native markers: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/vc3d-review-points.json (Git blob `ca2d623afdb601bceaa215ebec622db47617120f`). Its five distinct collections encode six flagged constraints and carry source SHA-256 `5ff4330182324c5cd7a9334f0a7eeb712c1e70a155c6dbca28e1e8d8cb6701fe`.
- Existing reviewer instructions and fail-closed tools: https://github.com/Svyable/scrollq/blob/main/docs/vc3d-review-bundles.md . A reviewer must classify each marker; `scroliq-vc3d-review-ingest` rejects missing decisions, unbound provenance, and unsupported winding edits. `scroliq-winding-review-compare` rejects unmatched before/after input hashes.
- Existing prize reviewer map: https://github.com/Svyable/scrollq/blob/main/docs/SUBMISSION.md . The real-data evidence is already public, but this audit found no evidence that a third party confirmed a winding correction or that the change measurably improved unwrapping. Absence of a named reviewed artifact in the current repo tree is **not proof** no review happened elsewhere.
- Official progress-prize source, checked 2026-10-10: https://scrollprize.org/prizes . The organizer favors real-data improvements, community use, actionable information, standard formats and documentation. October 31 23:59 Pacific; $20k for one best monthly submission; permissive open-source licensing required to accept a prize. The published $20k guarantee is to **one winner**, not to this project.

**Highest-information next action (not performed):** independent CT-backed classification of the two prioritized markers `relative:198/2233` and `relative:280/2860`, with review time, identity, notes and saved native JSON. If neither produces an independently defensible correction, stop spending time on the winding-correction prize hypothesis. If one does, run the existing apply/compare tools with frozen non-winding inputs, preserve negative controls, and require a measured delta before nomination. No outreach or submission is authorized here.

**EV sensitivity, not a forecast:** at $20k × 90% assumed eligibility × 3% assumed conditional win − $280 incremental cost, EV = **+$260**; at 0.5% conditional win, EV = **−$190**. There is no calibrated winning probability yet. The next two-hour review is a bounded evidence gate, not proof of positive net value.
