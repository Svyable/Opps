# Epistemics Fund — reviewer-facing falsification fixture (draft, 2026-11-23)

**Status:** PURSUE / unsubmitted. This is a synthetic *evaluation design*, not empirical evidence. Do not imply any reviewer study has occurred.

## Why this exists
A provenance tool can look convincing while adding no information. The funder should be able to test whether Svyable's evidence-to-decision interface helps users distinguish supported, unsupported and indeterminate claims, rather than merely increasing trust in a polished interface.

## Minimal public demo fixture
Each row is a deliberately synthetic claim/evidence pattern; replace with independently sourced, rights-cleared cases before external testing. Do not score the example labels as observed results.

| ID | Evidence shown to reviewer | Correct disposition | Failure mode to test |
|---|---|---|---|
| E01 | A claim supported by a directly accessible primary record | Supported | Tool rejects genuine support |
| E02 | Claim linked to a source that does not contain the assertion | Unsupported | Citation laundering |
| E03 | Source asserts the opposite of the claim | Unsupported | Contradictory evidence overlooked |
| E04 | Multiple pages repeat one unsourced statement | Indeterminate | Repetition mistaken for corroboration |
| E05 | Authentic document with an altered or misleading headline | Unsupported | Provenance mistaken for truth |
| E06 | Original source exists but the cited passage is out of context | Unsupported | Context stripping |
| E07 | A claim has no accessible source | Indeterminate | Confident unsupported answer |
| E08 | A later correction supersedes an earlier report | Indeterminate until chronology resolved | Stale evidence |
| E09 | Two independent primary records agree | Supported | Unnecessary skepticism |
| E10 | An AI-generated summary cites a genuine paper but invents a number | Unsupported | Numeric hallucination |
| E11 | A source is credible but describes a different population | Indeterminate | Scope mismatch |
| E12 | Document identity is verifiable but its factual assertions are disputed | Indeterminate | Authenticity conflated with accuracy |

## Paired test design
- Two randomized arms: conventional citation UI vs. Svyable provenance UI, using the *same* underlying claims and source material.
- Independent blinded adjudicators determine reference dispositions before any interface is shown.
- Primary endpoint: proportion of unsupported claims incorrectly accepted as supported; compare arms with uncertainty intervals.
- Secondary endpoints: correctly supported claims accepted, indeterminate claims marked uncertain, reviewer time, confidence calibration, and perceived usability.
- Prevent learning leakage by balancing case order and assigning disjoint case subsets when possible.
- Pre-register a sample-size calculation based on an explicit minimum detectable effect and cluster by reviewer where appropriate.
- Report attrition, disagreements, failed cases, null results and any conflicts of interest.
- Do not treat the software gate's 100-case threshold as a powered human experiment.

## Submission-ready project claim (conditional)
“We will compare an inspectable evidence-to-decision interface with a conventional citation interface in a preregistered, independently adjudicated reviewer study. Our primary outcome is whether reviewers are less likely to accept unsupported claims, without losing sensitivity to genuine support. Existing Svyable scoring and provenance work supplies the prototype starting point; results are not yet known.”

## Fund and commercial controls
- Ought-sponsored Epistemics Fund; organizer says applications close **no earlier than 2026-11-26**. Exact closing time not confirmed from official portal. Aim for 2026-11-25 internally.
- $500k–$5m is the **total pool**, not a guaranteed award. $50k is a proposed request only.
- Funding source: https://epistemic.fund/ ; application: https://www.lightconecommons.com/epistemics/apply
- Organizer announcement: https://x.noodl3.net/NathanpmYoung/status/2120200145900056579
- Missing before any submission: verified applicant/payee, three consenting references, source-code and dataset rights, evaluator consent/independence, evidence-backed budget, live portal terms, explicit owner approval.
- Distinguish Epistemics' provenance and reviewer-calibration deliverables from TAIF's protected agent-action / isolation experiments. No double charging.
- Do not spend, contact references, or submit without owner approval.

## EV discipline
The previous 65% eligibility × 4–12% conditional award assumptions imply a **2.6–7.8% joint probability**. At a hypothetical $50,000 award this is $1,300–$3,900 of expected *gross grant funding*, not profit. A realistic retained-margin estimate is unavailable until allowable compensation, tax, and delivery obligations are known. Stop further development if applicant evidence cannot be verified by the internal target.
