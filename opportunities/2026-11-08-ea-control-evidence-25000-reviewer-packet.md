# Transformative AI Fund — Control Evidence $25,000 conditional pilot packet
**Prepared:** 2026-11-08. **Status:** internal, NOT submitted or approved for submission. No award, applicant eligibility, signed commitments, or validated real-world results are asserted.

## Sponsor fit and payment reality
[EA Funds Transformative AI Fund](https://funds.effectivealtruismfunds.org/funds/transformative-ai) **corrected canonical source:** https://funds.effectivealtruism.org/funds/transformative-ai. Official page checked 2026-11-08: always open, typical $10,000–$150,000, early-stage technical research and demonstrations reducing catastrophic AI risk, including individuals and new projects. The sponsor explicitly describes a first $25,000 grant as potentially sufficient to launch a pilot. Funding is restricted project support, **not a contract, a cash prize, or $25,000 of founder profit**. Grant terms and eligibility remain unreviewed by the applicant.

## Reviewer-facing problem statement (proposed, not a finding)
Agent systems may report that an external action was completed without independently verifiable evidence of execution. A plausible signed receipt is insufficient if the agent can control the signing key, recording scope, event coverage, or the evaluation input. The project tests whether a *protected recorder* and precommitted holdout can distinguish genuinely completed actions from plausible but unsupported claims. It is not a claim to solve general AI alignment or prove model reliability.

## Scope: single independent R3 pilot only
The smallest fundable design is **one genuinely independent recording boundary**, not two adjudicators or a production SaaS platform. A human-controlled recorder must be operationally and cryptographically separate from the claimant, with key material and write access outside claimant control. Reuse Svyable's synthetic receipt boundary, durable SQLite nonce registry, claim evaluator and CI as **fixtures** only. They are not evidence that independent deployment exists.

**Hypotheses:** (H1) claim-only evaluation will accept at least some false-completion assertions on a controlled holdout; (H2) a protected recorder with predeclared complete coverage and nonces can reduce false supported decisions at an explicit abstention cost. These are hypotheses, not measured results.

### Pre-registered evaluation design
1. Publish a protocol version, threat model, action taxonomy, sampling seed and pass/fail thresholds **before** holdout collection. Include positive completions, failed actions, omitted events, malformed signatures, replay, cross-scope claims, conflicting receipts, recorder outages and key compromise simulations.
2. Separate three roles: claimant/agent; independently administered event recorder; blind scorer. Identify who controls each role and how their access is enforced. If roles cannot be separated, stop rather than labeling evidence independent.
3. Record a manifest of every attempted action, including failures and timeouts, not merely successful actions. Coverage attestations must be independently authenticated, with gaps causing abstention rather than success.
4. Compare baseline claim-only judgments against protected-receipt judgments on the *same* frozen holdout. Report confusion matrices, supported/refuted/abstained counts, denominators, missingness, false-support rate, false-refute rate and 95% uncertainty intervals. Do not remove failed or ambiguous runs.
5. Release hashes of manifests, code versions, evaluator output, test logs, negative examples and a limitations report; protect secrets and personal data. No access to real third-party systems without authorization.

**Proposed go/no-go success gate (not an official sponsor criterion):** at least 100 independent test cases spanning all declared attack classes; zero unsupported claims incorrectly classified as supported in the protected-recorder subset; at least 90% non-abstention on valid completed-action cases; every missing-coverage case abstains. If any gate fails, report the negative result rather than tuning the holdout.

### Work packages and conditional $25,000 budget
These are **planning allocations, not vendor quotes, salaries promised, costs incurred or a verified market-rate budget**.

| Work package | Proposed cap | Deliverable / acceptance evidence |
|---|---:|---|
| Independent recorder engineering, key separation, durable logs | $7,000 | Source, signed access-control/host-separation attestation, independent reproducible verification |
| Controlled action/attack fixture and frozen holdout | $5,000 | Timestamped protocol, seeds, input/output manifest, rights-cleared data |
| Independent evaluator and negative-result audit | $5,000 | Reproducible confusion matrices, uncertainty, blinded adjudication log |
| Reproducibility, privacy and external technical review | $4,000 | CI artifact hashes, redacted reproducibility bundle, external reviewer note |
| Project coordination, reporting and contingency | $4,000 | Milestone reports, budget ledger, documented underspend and disposition |
| **Total proposed restricted grant** | **$25,000** | **No line committed until recipient, staffing and sponsor terms verified** |

**Milestones (relative to funding, not promises):** month 1 recorder/roles/protocol, month 2 holdout execution, month 3 independent analysis and publication. Schedule is provisional and conditional on an authorized recorder, qualified personnel and data rights. Do not claim a three-month result is already feasible.

## Exact pre-submission eligibility and integrity gate
- [ ] Identify legal payee, jurisdiction, grant eligibility, tax treatment and person accountable for funds.
- [ ] Obtain written consent/commitment and independent control evidence for recorder operator; establish realistic hours and budget quotes.
- [ ] Verify the CI workflow's actual job result and **raw logs** for the committed nonce and claim tests; do not treat source code or test definitions as passing evidence.
- [ ] Verify durable database path, atomicity, backup/recovery, cross-host scope, and that nonce consumption and action adjudication cannot be replayed or partially committed.
- [ ] Prove data collection authorization, privacy, export permissions and IP/licensing for code, logs and research outputs.
- [ ] Reconcile budgets against every BlueDot, Mercor or other request; no double-funding or overlapping reimbursable labor.
- [ ] Inspect official application fields, grant agreement, reporting, publicity and IP conditions with applicant; obtain explicit approval before submission.
- [ ] Document qualified independent evaluator and why the work matters for catastrophic AI risk rather than only ordinary software audit hygiene.

## Commercial screen / stop-loss
EA Funds is an established charitable grantmaker; public eligibility is plausible for a new project, but Svyable-specific qualification is **unverified**. The official page has no fixed deadline. New proposal preparation is estimated at **1 hour × illustrative $35/hour = $35**. Incremental award probability uplift is **not measured**. Therefore this step has **−$35 incremental cash EV absent demonstrable improvement or reusable IP value**; break-even on the full *restricted* $25,000 face value is a +0.14 percentage-point increase in joint award probability, but actual founder surplus is less than face value and the threshold would be higher. Avoid adding new synthetic code or a second adjudicator without real recorder and independent test evidence. The next funded-likelihood milestone is evidence of an independent recorder and a verified CI log.

## Other opportunities screened on 2026-11-08
- [BlueDot Media Grants](https://bluedot.org/grants/media): $20k–$200k, 6–12 months, rolling/no published cutoff, established media grantmaker. Existing Sven Hardy Benson books/YouTube are reusable. Existing *self-built* audience and first-party analytics remain unverified; expected eligibility cannot be responsibly quantified, no new validator work without real export. WATCH.
- [SOA AI model selection RFP](https://www.soa.org/research/opportunities/2026/how-act-choose-between-models-plat/): user-tracked November 13 deadline, actuarial specialization and human-written proposal restriction, no specific contract price; low fit without human subject expert. REJECT for autonomous application.
- [Mercor AI Safety Fund](https://www.mercor.com/): previously tracked pooled $5m, not individual award; contractual competitor/IP restrictions and exact live program terms require separate verification. WATCH, no EOI submission.

**No third-party contact, application, paid compute, rights transfer or contractual commitment was made.**
