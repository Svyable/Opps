# Vesuvius October 2026 Progress Prize — release decision and verified evidence audit

**Decision recorded 2026-10-31, before 23:59 Pacific cutoff. Status: WATCH (October NO-GO on current evidence; retain later monthly prize route).** No entry submitted, no prize terms accepted, no reviewer contacted, no code or data license granted.

## Current official prize, judging and payer

- Official current [Open Prizes](https://scrollprize.org/prizes#progress-prizes): October deadline **2026-10-31 23:59 Pacific (PDT)**; best submission of the month receives **$20,000**; other awards are discretionary and typically **$250, $500, $1,000, $2,500, $5,000, $10,000, $20,000**. The $2.14m open pool is not a Svyable payoff.
- Judging favors *actual community use*, improvement on **real scroll data**, documented before/after bug fixes or actionable information that improves unwrapping/ink detection, standard integration, and **significant advantages over existing solutions**. Early open release helps but is not enough on its own.
- [Official winners](https://scrollprize.org/winners) document past named payouts, including **September 2026 $500 winding-consistency checking** by Sergei Evland, direct prior art for this lane. The payer is **Scroll Prize, Inc.**, with named awards but discretionary selection.
- [Terms](https://scrollprize.org/prizes#terms-and-conditions): award contingent on review, permissive open-source method if winning, and payment details within 30 days of award announcement. ScrolIQ has a public MIT LICENSE, but code licensing alone does not establish rights to all upstream scroll data or contributions. The October [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSc4flEfgK2nyjoczz2_U_XrIGMlgrnSknWatLqrFPnbtKfZwg/viewform) requires personal identity, contribution and affirmative agreement; applicant authorization is absent. Form fields were inspected on 2026-10-26; **the form was not independently re-opened in this audit**, so do not claim current field validation.

## Evidence audit against committed ScrolIQ data (2026-10-31)

Source files read from default branch, without regenerating data or running CT/VC3D:

1. [Frozen result.json](https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/result.json): **16,074** constraints, **6** inconsistent, **194/200** planted +2-winding shifts detected. This is a synthetic perturbation control *on real scroll geometry*, not an independently verified true-positive rate.
2. [Native VC3D markers](https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/vc3d-review-points.json): **5** distinct marker collections, bundle verdict `INCONSISTENT`.
3. [Ranked review priority](https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-25-paris4-review-triage/priority.json): **5** candidates, all `pending`. First candidate `relative:227/2445` is post-hoc prioritized, **not** adjudicated truth.
4. [Reviewer worksheet](https://github.com/Svyable/scrollq/blob/main/docs/october-2026-review-adjudication-sheet.csv): **5** marker rows, all `pending`.

**Cross-file verification:** five marker IDs in the native bundle, ranked manifest and worksheet match exactly (set equality); all five remain pending. This checks packaging consistency only. **No independent CT adjudication, confirmed erroneous annotation, reviewer time savings, downstream spiral-fit delta, ink improvement or community adoption is verified.** No new software test run or hidden-data benchmark is claimed.

## One decisive gap and stop/go rule

The missing evidence is **independent, source-hash-bound CT adjudication** of the first ranked `relative:227/2445` marker, followed, only if a real correction is confirmed, by an unchanged-input before/after rerun. Existing [reviewer handoff](https://github.com/Svyable/scrollq/blob/main/docs/october-2026-five-point-reviewer-handoff.md) and [exact form preflight](https://github.com/Svyable/Opps/blob/main/opportunities/vesuvius-october-2026-progress-prize-form-preflight.md) already exist. Writing another submission narrative, changing thresholds post-hoc, or re-running synthetic controls would not close this gap.

**October release decision: NO-GO for autonomous submission.** An honest low-confidence tool entry is technically possible only if the applicant independently approves the exact form and terms before the deadline; without new evidence it is not a justified additional automation pursuit. If a qualified independent reviewer later produces an authenticated negative, uncertain or positive result, publish it accurately and reassess for a **later monthly progress-prize cycle**, not as a retroactive October result. Do not contact reviewers or organizers without approval.

## Marginal economics — decision, not award prediction

A single $500 small-award scenario with **2%** *subjective* selection probability yields $10 expected gross. An additional 0.5 hour at an illustrative $35/hour costs $17.50, hence **−$7.50** net. A mutually exclusive $20,000 best-monthly-prize scenario with **0.1%** subjective chance yields $20 gross, hence **+$2.50** net; that optimistic case is not evidence of eligibility or actual odds. Neither model prices license/IP opportunity costs, applicant consent, reviewer availability or delivery time.

For a new **2-hour independent review costing $70**, break-even would require **14 percentage points** of added probability of a $500 prize or **0.35 percentage points** of added probability of the $20,000 prize (ignoring all other costs). **No defensible probability uplift is established**, and no authorized reviewer is available. The marginal value of more autonomous October work is therefore not shown positive. Avoid sunk-cost escalation.

## Next money decision

Retain ScrolIQ as **WATCH** for future monthly progress prizes and the separate 2027 grand-prize program. Resume only upon an independent CT review receipt, a measured downstream improvement or credible external user report, and applicant approval of any submission. The next step is evidence/authorization, not additional mock engineering.

**Integrity:** This document records a no-go and cross-file read audit, not a submission, payout, safety claim or new experiment. All existing repo assets remain unchanged.
