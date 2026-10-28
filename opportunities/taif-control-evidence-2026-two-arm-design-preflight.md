# Control Evidence — prospective two-arm allocation and reviewer-contamination preflight

**Prepared:** 2026-10-28. **Funder:** [EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai). **Proposed request:** $25,000 / 10 weeks, rolling. **Status:** PURSUE, NOT SUBMITTED. This is a study-design and executable-protocol deliverable, **not a completed experiment**.

## Material problem found

The existing [blind-packet builder](../artifacts/control-evidence-2026/blind_packet.py) can conceal reference labels, and [score_reviews.py](../artifacts/control-evidence-2026/score_reviews.py) can score one full packet per reviewer. But the **application promises a comparison of narrative-only versus receipt-supported judgments**. The existing scorer requires each reviewer to judge every case and does not assign an arm. If the same reviewer sees the same case with and without receipts, recall and learning can contaminate the comparison; if different reviewers are assigned only one arm, reviewer skill can be confounded with treatment. Neither design was adequately specified in the application.

## Implemented prospective design

The new [two_arm_design.py](../artifacts/control-evidence-2026/two_arm_design.py) accepts an existing blinded reviewer packet, a separately prepared narrative for every pseudonymous review ID, and a local secret of at least 32 bytes. It uses keyed deterministic ordering to balance receipt exposure **within each claim type**. Two distinct reviewers each see every case **exactly once**, with complementary assignments: one narrative-only judgment and one narrative-plus-receipts judgment per case, by different reviewers. Every reviewer sees both conditions. This is a **reviewer-balanced, case-paired allocation**, not two independent samples.

The narrative-only packet contains only a pseudonymous review ID, claim type, narrative and arm. It does **not** contain scope IDs, evidence coverage, timestamps, tool receipts or reference labels. The receipts arm includes those fields. The private assignment table is separate. The source packet is bound to its dataset ID and source hash. Missing narratives, duplicate case IDs, weak secrets, unexpected case fields, invalid/missing judgments and inconsistent label bindings are rejected. The prospective summary counts reference-label agreement, false support against a non-support reference, abstentions and explicit no-decisions **by arm**. It deliberately does not report statistical significance or call reference labels authenticated truth.

**Testing:** [11 new synthetic regression tests](../artifacts/control-evidence-2026/test_two_arm_design.py) passed in a local Python 3.13.5 standard-library execution on 2026-10-28; the GitHub Actions workflow has been updated to include them. **Remote CI result must be independently checked before claiming 45/45.** No reviewer has been recruited, no actual data collected, no random allocation used in a human trial and no empirical improvement measured.

## Workload / cost feasibility

At the **planned maximum of 60 cases**, two reviewers each assess 60 cases, for **120 total case judgments** (60 per arm). At an illustrative 12 minutes per judgment, that is **24 reviewer hours**, leaving **6 hours** of the existing 30-hour / $3,000 aggregate reviewer envelope for calibration, conflict screening and disagreement notes. This is a planning estimate, **not a rate quotation, availability confirmation or evidence that 60 cases are feasible**. Reviewers must be independent of holdout labeling and instrumentation. If actual decision time exceeds 12 minutes or independent reviewers are unavailable, reduce the case target, seek a revised budget or publish a feasibility shortfall.

## Prespecified analysis and limits

- **Unit of pairing is the case**, not 120 independent trials. Preserve the two judgments for each case. Report per-arm raw counts, reference categories, missingness, reviewer identifiers and uncertainty. A case-clustered or randomization-based analysis plan must be frozen before viewing outcomes; the new summary intentionally does not compute p-values.
- **Primary failure:** proportion of independently established non-support cases incorrectly marked `supported`, separately by arm. Reference labels require independent, authenticated adjudication; the current `expected_verdict` is merely a synthetic label.
- **Secondary:** appropriate abstention on incomplete evidence, justified support on complete evidence, time per judgment, and disagreements. Do not reclassify a missing response as correct; explicitly record `no_decision`.
- **Blinding is incomplete by design:** reviewers can tell whether receipts are present. They must not see reference labels, earlier judgments, private source IDs, model verdicts, or each other's responses.
- **Narrative leakage is a human quality-control gate:** the generator cannot prove that author-supplied narrative text omits hints from hidden evidence. An independent preflight reviewer must check the frozen narratives without seeing reference labels.
- **Reliability caveat:** one judgment per case-condition does not estimate within-arm inter-rater agreement. A separate consented calibration set or funded duplicate review is required to estimate it; do not claim independent replication.
- **Causal caveat:** balancing claim type and crossing reviewers reduces two obvious confounds but does not authenticate source records, prove reviewer independence, guarantee adequate statistical power or establish transfer to deployed agents.
- **Security:** never commit secret keys, reviewer packets, case narratives, reference labels, private assignments or judgments. The Python module is a library API, not a secure clinical-grade or production data system. Keep generated artifacts in restricted local storage and freeze hashes before review.

## Funding relevance

EA Funds says it funds early-stage transformative-AI work, typically **$10,000–$150,000**, with a primary focus on reducing catastrophic risks from advanced AI. The proposal is strongest when framed as a *testable oversight failure mechanism*: when a consequential agent claims to have completed an action, what independent evidence justifies a human accepting that claim? The two-arm design now makes the planned comparison falsifiable without asserting any safety gain. [Official fund](https://funds.effectivealtruism.org/funds/transformative-ai).

**Incremental economic screening (unchanged):** conditional lead surplus $7,800 × subjective 55% feasibility × 5% selection − $70 incremental preparation = **+$144.50**. This is not a calibrated award forecast. Additional design work reduces an identifiable research-method risk but **does not warrant increasing the assumed selection probability**. The $25,000 grant is restricted research funding, not unrestricted profit.

**Applicant-controlled blockers remain:** legal payee, 12h/week founder capacity, source/IP rights, actual independent engineer and reviewers, data/consent permissions, live Paperform questions and terms, and explicit approval before any application, external contact, spending or legal commitment.
