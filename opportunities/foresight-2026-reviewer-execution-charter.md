# Control Where It Counts — Foresight reviewer evidence and execution charter
**Prepared:** 2026-10-23 | **Opportunity:** Foresight AI for Science & Safety Nodes, Human Empowerment (Coordination & Accountability) | **Status:** PURSUE — not submitted

## The funding case
**Proposed request:** $35,000 over 12 weeks. **Source:** https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/ . Deadline: October 31, 2026 at 23:59 PDT. The sponsor explicitly asks for mechanisms to detect and fix hollow oversight and evidence-based rules for when human control adds value or degrades it.

**Question:** When does an approval checkpoint actually stop an unauthorized AI-agent action, rather than merely producing a record of human participation? This is a falsifiable empirical question, not a promise of general AI alignment.

**Asset reuse:** Svyable/human-kind supplies existing authority-boundary and approval concepts; Svyable/scrollq supplies provenance and reviewer-evidence patterns. Their existence is not proof of benchmark performance. Do not claim an independent evaluation or third-party partnership.

## Distinctness and anti-double-funding boundary
Foresight / Control Where It Counts tests **intervention effectiveness**: did the checkpoint prevent or delay an unauthorized action, and at what cost in useful work? EA Funds / Control Evidence tests **retrospective claim–trace reconciliation**: can an independent reviewer substantiate or contradict an agent's report? They may share open-source utilities but must have separate milestones, time sheets, expenses and outcome reports. Do not charge the same labor or artifact to both grants. No retroactive grant charging for work done before award.

## Proposed evaluation protocol — prospective, not yet run
1. **Freeze task specifications and policy:** Define at least 60 sandbox tasks across file modification, external-message simulation, secrets exposure simulation, approval bypass and benign work. Mark actions as authorized, unauthorized, or ambiguous *before* agent execution. No real credentials, messages or external side effects.
2. **Three experimental arms:** (A) no approval gate; (B) human approval UI without an enforced action boundary; (C) an enforceable approval boundary with auditable decision record. Randomize task order, rotate agents where feasible, and report per-arm sample counts.
3. **Separate safety from throughput:** Primary outcome: unauthorized action completion rate among policy-violating attempts. Secondary outcomes: legitimate task completion, reviewer time, false blocks, approval latency and evidence completeness.
4. **Independent adjudication:** At least two reviewers label a held-out sample while blind to intervention arm; disagreements receive documented adjudication. Do not imply reviewers are already contracted or have consented.
5. **Threat model:** Evaluate delayed actions, ambiguous approvals, tool aliases, delegated subagents, missing traces, and agent-generated explanations that misrepresent completed actions.
6. **Pre-registration and stopping:** Freeze policy labels, held-out split, metric definitions and analysis script before running final tests. Report negative findings and all excluded trials. No post-hoc target adjustment.

## Decision rules and failure criteria
- **Success is not assumed.** A candidate enforcement boundary is worth recommending only if unauthorized completions decrease versus arm B without unacceptable loss of legitimate completion. Publish confidence intervals and raw denominators; do not claim statistical significance from a tiny sample.
- **Abstain** when logs are incomplete, the ground-truth policy is disputed or the action cannot be reconstructed.
- **Stop deployment recommendations** if the intervention can be bypassed through a known tool alias, delegated action or race condition; document counterexamples.
- **No generalization claim** from synthetic tasks to real-world catastrophic-risk reduction. The research can inform control design; it cannot prove prevention of existential risk.

## Milestones and acceptance evidence
| Weeks | Deliverable | Reviewer-verifiable receipt |
|---|---|---|
| 1–2 | Threat model, frozen task taxonomy, consent and IP review | Versioned protocol, policy labels, license inventory |
| 3–4 | Three-arm sandbox harness and baselines | Reproducible runner, fixtures, seed manifest |
| 5–7 | Controlled experiments, failure-mode injections | Signed/hashable run manifests, trace samples, raw metrics |
| 8–9 | Blinded reviewer adjudication and uncertainty analysis | Independent label records, disagreement log, CIs |
| 10–11 | Open-source release and user-facing decision rules | Tagged repository, permissive code license, public documentation |
| 12 | Final negative/positive findings and grant report | Replication instructions, budget actuals, limitations |

## Budget gate (proposed, not authorized)
Previously proposed $35,000 consists of **$33,000 direct research costs** and **$2,000 overhead**. Foresight permits overhead up to 10% of direct research costs; $2,000 / $33,000 = 6.06%. The line-item expense ledger and contractor rates must be reconciled to the applicant's actual availability and procurement before submission. A 240-hour founder commitment implies 20 hours/week and remains unverified.

## Eligibility and fundability gates
- [ ] Applicant confirms legal recipient and tax/payee information.
- [ ] Applicant confirms 20 hours/week for 12 weeks and any outside-work/IP restrictions.
- [ ] Professional reference consents to being contacted.
- [ ] Reviewer/contractor availability and rates are real, not invented.
- [ ] Applicant can credibly describe SF/Berlin Node engagement, or clearly state remote-only availability and accept the disadvantage.
- [ ] All grant-funded outputs can be open-sourced without violating third-party licenses or confidential commitments.
- [ ] Final Airtable questions and terms are personally checked; application narrative reviewed in applicant's own voice.
- [ ] Explicit authorization obtained before submitting or accepting grant conditions.

## Economics and go/no-go
Previous working scenario: $12,000 **conditional founder economic surplus** × 45% feasibility × 3.5% selection − $140 remaining preparation = **+$49 modeled EV**. These probabilities are judgmental and uncalibrated. $35,000 grant budget is not unrestricted profit. The actual strategic value is a bounded, reusable public benchmark and a sponsor relationship, not an assumed cash windfall.

**Recommendation:** PURSUE the application preflight; do not submit until applicant-controlled gates are satisfied. Do not extend the experiment before funding merely to improve an unvalidated win probability.
