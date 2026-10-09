# Google DeepMind — Gemma 4 Developer Agent Paper Track (WATCH)

Screened: 2026-10-09. **No entry, submission, or rule acceptance authorized.**

## Official sources and commercial terms

- Paper-track overview and rubric: https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/overview/submission-requirements
- Official rules (read in full before joining): https://www.kaggle.com/competitions/gemma-4-developer-agent-paper/rules
- Sponsor: Google DeepMind; host: Kaggle. **Credible payer**, subject to rules, tax and winner verification.
- Total paper-track cash pool **$35,000**: best paper $15,000; best new resource $10,000; best new application $10,000. These are **separate award categories**, not an expected $35k payout.
- **Deadline: 2026-11-12 23:59 UTC**. The main model/agent leaderboard is a *different* competition with a later deadline and $65k prize pool; do not conflate.
- Paper track accepts novel, **unpublished** research in a Kaggle Writeup (maximum 3,000 words). Main leaderboard participation is **not required**. Judging: novelty, quality/generalization, relevance, verifiability, clarity. Public notebook/project link optional.
- Joining and submitting require accepting competition rules; not done. Confirm exact eligibility, winner license, IP/publicity terms, and any tax requirements in official rules before approval. A private Kaggle resource linked to a public writeup may become public after deadline.

## Existing Svyable asset match

- https://github.com/Svyable/frontier-lab — measured ML ablations, falsification discipline, Hugging Face artifact publishing.
- https://github.com/Svyable/agents — agent work routing, provenance and GitHub-centered reproducibility (an invitation hub, **not** itself a benchmark).
- https://github.com/Svyable/proofbot — formal/verification mindset; suitability and code availability unverified.
- Candidate submission: **Patch Provenance: a falsification benchmark for coding-agent patches under environment drift and intentionally broken controls.** Target *Best New Resource* ($10k), not leaderboard model tuning.

This is a **research hypothesis**, not a completed or novel benchmark. The project must introduce a demonstrably new resource and original unpublished findings, not merely repackage public code.

## Technical feasibility artifact: proposed minimum evaluation protocol

Create a small **new** public evaluation dataset of permissively licensed repositories/issues, with a reproducible harness. Every row would carry:
```json
{
  "case_id": "example-001",
  "source_repo": "OWNER/REPO",
  "base_commit": "FULL_SHA",
  "issue_or_task": "PUBLIC_ISSUE_URL",
  "source_license": "SPDX_ID",
  "environment_digest": "sha256:...",
  "baseline_test_command": "pytest -q tests/test_regression.py",
  "expected_baseline_failure": "assertion identifier",
  "agent_patch_digest": "sha256:...",
  "post_patch_result": "pass|fail",
  "negative_control": "mutated_patch|dependency_drift|wrong_base",
  "negative_control_result": "pass|fail",
  "evidence_artifact": "relative/path/to/log.json"
}
```
The above is a **schema sketch**, not a measured record. No case, model result, or score has yet been generated.

**Required experiments before a credible writeup:**
1. Choose three *licensable* real software issues with pinned commit and tests; ensure tasks are not from hidden competition evaluation material.
2. Establish the unchanged baseline failure; run the patch in a clean environment; record time, dependency lock, SHA and stdout/stderr.
3. Run negative controls: intentionally broken patch, wrong base commit, and dependency drift. A successful detector should reject controls rather than rubber-stamp patches.
4. Compare naive patch-pass reporting against provenance-aware reporting. Report denominators, failure cases and uncertainty; no synthetic scores.
5. Independent reproduction on a clean machine; publish code/data with compatible rights; literature/novelty search against SWE-bench, reproducible builds, coding-agent evaluation.
6. Draft <=3,000-word writeup with title, abstract, method, experiment, limitations, citations and link to public artifact.

## Economic gate

Target prize: **$10,000**, not $35,000. Screening assumptions: eligibility **90%** (unverified); conditional category win **2.5%** (speculative, no calibrated prediction); **12h** new work at **$35/h** = **$420**. EV = $10,000 × 0.90 × 0.025 − $420 = **−$195**. Alternative optimistic 5% win => +$30. Both exclude potential compute cost and opportunity cost. High reuse in method, but new experimental evidence is mandatory.

**Decision: WATCH, not a funded build.** Allocate at most a 2-hour evidence/novelty check if spare capacity exists. Promote to PURSUE only if a real reproducible case and differentiating method exist, rules/IP terms are acceptable, and the estimated win probability justifies incremental cost. Otherwise REJECT.

No registration, acceptance of terms, public submission, spending, or legal commitment has occurred.
