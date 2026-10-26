# Vesuvius Challenge — October 2026 Progress Prize: exact-form submission preflight

**Prepared:** 2026-10-26 · **Status:** DRAFT FOR APPLICANT REVIEW — NOT SUBMITTED, NO RULES ACCEPTED.  
**Official prize rules:** https://scrollprize.org/prizes#progress-prizes  
**Official October form (fields inspected 2026-10-26):** https://docs.google.com/forms/d/e/1FAIpQLSc4flEfgK2nyjoczz2_U_XrIGMlgrnSknWatLqrFPnbtKfZwg/viewform  
**Deadline:** 2026-10-31 at 23:59 Pacific (PDT). **Prize:** $20,000 guaranteed for the single best monthly submission; additional awards at the organizers' discretion, historically as low as $250. The $2.14M open prize pool is **not** an individual payout.

## Exact live form field crosswalk (do not submit without explicit authorization)

| Live question | Draft answer / decision |
|---|---|
| Email (required) | **APPLICANT TO ENTER** the address they want associated with this entry. Do not infer from repository metadata. |
| Your full name (required) | **APPLICANT TO VERIFY** legal/entry name. Public author branding is not proof of the entrant's legal name. |
| Team description: individual or team; team leader (required) | **APPLICANT TO CONFIRM** whether individual or team and any contributor consent/prize-sharing terms. Proposed only if accurate: `Individual entrant, developing the open-source ScrolIQ project under Svyable.` |
| Discord display name (if member; optional) | **APPLICANT TO ENTER** if applicable; leave empty otherwise. |
| URL of publicly available contribution (required) | https://github.com/Svyable/scrollq ; https://github.com/Svyable/scrollq/blob/main/docs/SUBMISSION.md ; https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/README.md ; https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-25-paris4-review-triage/README.md |
| What is your contribution? Four required points (required) | **Candidate text below; applicant must review and edit before use.** |
| Terms and Conditions (required checkbox) | **STOP — APPLICANT ONLY.** The form requires “Yes, I agree.” The automation must not accept this or submit. |

## Candidate answer to the contribution question

**1. Scroll data.** ScrolIQ analyzed public PHercParis4 winding annotations and surface patches in the Vesuvius Challenge workflow. A frozen, source-hash-bound run attached 2,111 of 2,232 points to nearby patches and flagged 6 of 16,074 winding constraints, corresponding to five native VC3D review markers. In a planted +2-winding perturbation control, the detector flagged 194 of 200 injected errors. These are diagnostic measurements, not estimates of real annotation error rates.

**2. How it might help people read scrolls.** An incorrect winding attachment can make a spiral fit jump between physical sheets. The contribution links cross-collection inconsistencies to native VC3D points and specific candidate patches so a reviewer can inspect the local CT rather than chase aggregate scores. Two high-information questions are pre-ranked: `relative:227/2445` (nearest patch 0.886 voxels away, residual −5, while four other attachments have zero residual) and `relative:242/2549` (two nearly equidistant patches disagree by two windings). This narrows where a reviewer can look; it does **not** establish a corrected sheet, faster review, or improved unwrapping.

**3. What the contribution enables.** The existing open-source tooling packages a reproducible diagnostic-to-review handoff: frozen source identities, candidate patch provenance, native PointCollections markers, an adjudication worksheet, and a fail-closed correction/rerun protocol. This makes these particular discrepancies directly inspectable in VC3D without reconstructing the entire analysis manually. Winding-consistency checking itself is **not novel**: Vesuvius awarded a September 2026 $500 prize for a related checker. We do not claim superiority over that tool, community adoption, or downstream gains without independent evidence.

**4. Evidence and limitations.** Source run, controls and limitations: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/README.md ; five-marker handoff: https://github.com/Svyable/scrollq/blob/main/docs/october-2026-five-point-reviewer-handoff.md ; ranked two-marker evidence: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-25-paris4-review-triage/README.md ; native points: https://github.com/Svyable/scrollq/blob/main/artifacts/2026-10-03-paris4-winding-attachment/vc3d-review-points.json ; reviewer worksheet: https://github.com/Svyable/scrollq/blob/main/docs/october-2026-review-adjudication-sheet.csv . The 8-voxel attachment radius can match adjacent sheets; 48 relative frames were not tied to the absolute frame. **No independent CT adjudication, correction, downstream before/after comparison, or outside adoption is currently verified.**

## Judging criteria and evidence gate

The official rules prefer early open release, actual community use, improvements on real scroll data, actionable findings, documentation, standard formats and **significant advantages over existing solutions**. The repository demonstrates real-data diagnostics and standard native review output. **Significant advantage, actual use, and an independently confirmed downstream correction are not established.** This is the main award-risk, not a missing form paragraph.

**Strongest next receipt:** an independent VC3D reviewer checks `relative:227/2445` against the CT and records their identity, date, time spent, evidence and exact reviewed-file hash. If an error is confirmed, preserve an unchanged-input before/after comparison. If review says uncertain or no issue, publish that result without claiming a fix. Reviewer recruitment/outreach needs approval.

**Decision fork:** (A) applicant may explicitly authorize an honest, lower-confidence tool submission by October 31 using the existing public work and the disclosure above; or (B) defer until independent CT review produces a defensible outcome, potentially for a later monthly prize. Neither option is chosen or executed here.

## Economics and payer risk

Credible payer: Scroll Prize, Inc. publishes prior named winners and prize rules at https://scrollprize.org/winners . Awards are discretionary except the guaranteed $20,000 best-monthly-submission award, which still requires selection. A **sensitivity example**, not a calibrated forecast: $500 small-award payoff × 2% selection = $10 gross expected receipt; subtract 0.5 hour of final form preparation × $35/hour = **−$7.50 incremental EV** for the unreviewed entry. For a $20,000 best-award scenario at 0.1% assumed probability, gross expectation is $20; net after $17.50 prep is **+$2.50**. These cases cannot be added without a coherent mutually exclusive probability model. The prior portfolio **+$66** EV was based on different assumptions and is not evidence that this specific unreviewed entry has positive EV. Pursuing independent review has separate labor/availability costs.

**Restrictions:** entrant must agree to prize terms; if awarded, code must be public under a permissive open-source license; prize decisions are discretionary; winner must provide payment information within 30 days. Verify repository licenses and any third-party data restrictions. Do not disclose confidential data. No application, acceptance, outreach, spending or legal commitment is authorized by this document.
