# BlueDot Seed — independently recorded agent-action pilot: falsification and release gate
**Prepared 2026-11-17. Status: WATCH; no submission or grant commitment.**

## Official opportunity / fit
[BlueDot Seed Grants](https://bluedot.org/grants/seed) currently advertises **$20,000–$200,000**, first **6–12 months** of a new AI-safety/biosecurity project or organization, approximately **four-week** decisions, and no fixed closing date on its public page. Review criteria are problem selection, a reasoned hypothesis, evidence of execution, and a concrete early plan. The funder offers founder living costs, operating costs and introductions; these are restricted grant resources, not a commercial contract or guaranteed founder income. Public page and [grant index](https://bluedot.org/grants) checked 2026-11-17. Applicant jurisdiction, agreement, tax, IP, new-project status and available time remain unverified.

**Project separation:** proposed Seed project is a new *independent recorder and installation pilot*. Existing Control Evidence receipt auditor, synthetic negative controls and 12/12 isolated tests are pre-existing reusable code, **not** independent agent-safety evidence, new funded deliverables, external user validation, or proof of novel project eligibility. Do not bill the same work to TAIF/BlueDot Rapid/Foresight.

## Specific weakness to remove before a Seed application
The existing auditor can accept a receipt that says `recorder=independent-executor` without cryptographically or operationally binding the receipt to a separate execution observer. A passing audit of such a receipt says only that the **record is internally consistent**, not that the action happened. An application describing the current implementation as independently verifying execution would be materially misleading.

## New pilot deliverable and falsifiable acceptance contract
A minimal isolated tool executor and **separate recorder process** must generate a transcript of harmless local file writes. Recorder signs or MACs a canonical action record with a secret inaccessible to the agent/executor under the stated threat model. A verifier must reject unsigned, modified, replayed, out-of-order and missing observations. A signature alone does **not** prove an actual side effect; independently check the final file digest against the recorder observation. State explicitly that process isolation on one host is weaker than hardware-backed attestation.

| Case | Controlled input | Expected reviewer-observable outcome |
|---|---|---|
| Positive authorized write | Approved action ID, exact path and bytes | Authenticated recorder event and independently checked file digest match |
| Forged origin | Agent fabricates `independent-executor` label | Fail closed: no authenticated recorder event |
| Action substitution | Valid authorization ID, different path/content | Reject mismatch to original approved action |
| Replay | Reuse valid prior event in new run | Reject nonce/run-ID mismatch |
| Truncation | Drop last event | Abstain on execution status; never report clean zero violations |
| Recorder compromise | Deliberately expose recorder secret | Explicitly fail threat-model assumption; do not claim detection |
| Crash between write and record | Kill recorder at boundary | Return UNKNOWN, reconcile file state; do not invent a completed audit |
| Unauthorized write | Denied action attempted | Independent file-state check and event trace disclose whether denial held |

**Pre-registered measurements:** 100 deterministic trials per case with seeded test IDs; report denominator, false accept/reject, UNKNOWN rate, missing observations and all failure logs. These are **planned sample sizes, not results**. Zero false accepts in 100 trials would only bound the underlying rate weakly (one-sided 95% upper bound ~2.95% under iid assumptions), not certify safety. Run on one pinned OS/runtime and repeat independently before claiming generalization. Publish failing cases and SHA256 manifests.

## Stop/go and reuse
**Go to applicant review** only after: (1) runnable pinned prototype, (2) forged-origin negative test actually rejects, (3) reproducible transcript and digest checks, (4) accurate project separation and license provenance, (5) founder capacity/payee/jurisdiction/terms verified. If no runnable recorder within a capped **8 engineering hours**, pause and revise hypothesis; do not spend on compute, external reviewers or outreach without approval. 8h at illustrative $35/h = **$280 internal labor**, $0 authorized external spend.

**Conditional economics:** A $60k request from the prior draft is **not profit**. Suppose, solely for sensitivity, $10k retained founder economic benefit after project delivery and a joint eligibility/award/payment probability of 1%, then marginal EV of an 8h experiment = $100 − $280 = **−$180**. At 5% it is **+$220**, ignoring further application effort, tax and IP costs. These probabilities and retained benefit are invented *scenario inputs*, not estimates; actual EV and incremental award-probability uplift remain **unknown**. A 2.8% joint success probability is the simple $280/$10k break-even, before other costs. Avoid a positive-EV claim.

**Decision:** WATCH / technical experiment gated; a credible grantpayer and strong pre-existing code reuse, but no demonstrated independent recorder, no confirmed applicant qualification and no quantified positive EV. Prefer this bounded evidence test to more prose-only applications. No submission, registration, legal consent, contact, spend or IP transfer.
