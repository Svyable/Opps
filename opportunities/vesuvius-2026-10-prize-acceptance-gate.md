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

- Problem and exact public dataset: **NOT YET VERIFIED**
- Baseline failure and reproduction: **NOT YET VERIFIED**
- ScrollQ improvement / quantified delta: **NOT YET VERIFIED**
- Reproducibility commands and artifact checksums: **NOT YET VERIFIED**
- Open-source license and public repository: **TO CONFIRM**
- Independent community use / feedback: **NOT YET VERIFIED**
- Final prize form: **NOT SUBMITTED**

## Marginal EV gate

Illustrative $20,000 first-prize scenario: 90% eligibility × 3% conditional win probability × $20,000 − 8 hours × $35 = **+$260**. The 3% win probability is a screening assumption, not a measured estimate. If work rises to 20 hours with the same odds, EV becomes **−$160**. Prize award is discretionary; taxes and potential computing costs not included.

**Authorization boundary:** No registration, prize submission, spending, or contractual acceptance without explicit approval. General progress contributions may be public, but milestone discoveries involving newly read text have additional non-disclosure conditions; check prize category before publication.
