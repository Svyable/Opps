# Transformative AI Fund — conditional $25,000 pilot application package
Prepared 2026-11-18. **Unsubmitted draft.** Existing TAIF opportunity: PURSUE / HOLD. This is a separate, narrower alternative to BlueDot Seed, **not an additional funding claim for the same work**.

## Verified official route
[EA Funds Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) accepts applications continuously from individuals, new organizations and existing organizations with new projects. Typical awards $10,000–$150,000; rarely above $300,000. Its primary focus is reducing global catastrophic risk from advanced AI. It also supports technical demonstrations and early-stage infrastructure. [Official application](https://funds.effectivealtruism.org/apply-for-funding). EA Funds reports an established grantmaking operation, but no award probability or decision deadline is promised here. The older Long-Term Future Fund is closed; do not apply to it.

## Proposed title
**Can an AI agent forge its own execution evidence? A reproducible independent-observation pilot.**

## Application summary — draft, fact-limited
As AI agents gain authority to operate software and files, an internally consistent action log may be mistaken for evidence that an independent observer saw an authorized side effect. Svyable's existing Control Evidence receipt auditor provides a concrete falsification target: a synthetic negative control shows that a claimed recorder identity need not be independently authenticated. The existing exact-byte isolated suite ran 12/12 tests; this is not real-world safety validation. A separate authenticated-envelope prototype ran nine isolated tests and a SQLite single-use guard ran six; these authenticate and consume records under trust assumptions but **do not establish independently observed execution**.

We propose a six-week, bounded open research pilot to separate authorization, agent execution and observation across process boundaries, reconcile actual harmless file writes against an observer-controlled state, and publish both successes and failures. This is a measurement/evaluation infrastructure project, not a claim that the pilot itself materially reduces catastrophic AI risk. Its relevance is to avoiding false assurance in agent control and audit systems; the causal path to reducing catastrophic risk needs further justification.

## Specific work products
1. **Threat model and trust boundary**: distinguish untrusted agent, executor, observer, key custody, and privileged same-host attacker. Pin action/run IDs, path allowlist, state digest and UNKNOWN outcomes.
2. **Executable isolated harness**: a harmless write to a disposable temporary directory, independently checked by a recorder process with protected key and separate evidence store; explicitly document any residual shared-host trust.
3. **Pre-registered falsification suite**: valid action, forged origin, substituted action, replay, missing/truncated record, recorder crash, unauthorized write and compromised-key case. Record counts, exact source revision, commands, environment, seeds and raw outputs. Do not label a test passed until executed.
4. **Public reproducibility report**: release code and negative findings only where Svyable owns the rights and dependency licenses permit. Distinguish authentic log from independently witnessed side effect; document failure modes and generalization limits.

## Conditional exclusive budget (six weeks; $25,000 request)
| Cost category | Proposed cap | Verification |
|---|---:|---|
| Founder research and implementation support | $18,000 | Payee, work availability, eligible support and tax treatment unverified |
| Independent replication / security review | $4,000 | No reviewer retained or quote obtained |
| Tools and reproducibility infrastructure | $1,500 | No spend or vendor quote |
| Documentation and publication | $1,500 | Rights and eligible costs unverified |
| **Total** | **$25,000** | **Illustrative, not approved** |

**Mutual exclusivity:** This budget is an alternative to the BlueDot Seed independent-recorder pilot budget, not cumulative. If both applications were ever pursued, disclose the overlap, allocate mutually exclusive work packages, and obtain funder approval before charging any cost. No retrospective reimbursement for already completed Svyable work is assumed. No third-party IP release is promised.

## Reviewer evidence and missing prerequisites
- Existing source: [auditor exact-byte verification](2026-11-17-taif-byte-matched-regression-verification.md), [authenticated-envelope prototype](2026-11-18-bluedot-seed-authenticated-envelope-poc.md), [replay guard](../artifacts/control-evidence-2026/seed-recorder-envelope/replay_guard.py). Earlier isolated test claims are historical repository evidence, **not rerun in this preparation**.
- Must verify applicant identity, jurisdiction, tax/legal payee, permission to use/publish Svyable IP, and available six-week capacity.
- Must establish whether the project genuinely addresses a fund priority beyond generic audit tooling; ask for a credible risk pathway and external reviewer before submission.
- Must obtain an exclusive, costed budget and complete a real independently observed harmless action test. No claims of such a test exist yet.
- Must review final application form, grant agreement, reporting, IP and disclosure obligations before any submission or acceptance.

## Commercial decision and stop-loss
Payer credibility: established EA Funds grantmaker with public fund managers and published grants. Deadline: rolling; no fixed cutoff verified. Qualification: plausible category fit but founder-specific eligibility and catastrophic-risk relevance unverified. Existing IP reuse: high. Remaining engineering: estimated 8–24 hours before a defensible demonstration, plus application and budget verification; **estimate, not measured effort**. Terms: grant-restricted funds, tax and possible disclosure/IP obligations to check, not a commercial purchase order. Grant face value is not retained profit.

Illustrative preflight: 3 hours at $35/hour = $105 internal cost; no external spending. If net retained economic benefit after delivery and restrictions were hypothetically $5,000, break-even joint success probability for this preflight alone is 2.1%. At illustrative probabilities 1% and 5%, marginal values would be -$55 and +$145 respectively. These are sensitivities, not estimated probabilities; actual monetary EV and incremental selection uplift are **unknown**. **Stop** if applicant/legal eligibility, exclusive budget, or genuine catastrophic-risk theory of change cannot be established; do not inflate a technical audit tool into a demonstrated existential-risk intervention.

No application submitted, funder contacted, money spent, agreement entered or IP transferred.
