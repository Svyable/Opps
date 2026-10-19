# TAIF application preflight — 2026-10-19

**Internal research note; not submitted. No funding or applicant eligibility verified.**

**Opportunity:** [EA Funds — Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai). Official page says applications are always open, generally $10k–$150k and rarely above $300k. Individual/new-organization applicants accepted.

**Proposed ask:** $50,000 for 12 weeks to evaluate whether oversight systems can reliably reconcile long-horizon AI agents' claims about completed tool actions with independent execution evidence. The project would publish a Python evaluation harness, frozen synthetic/adversarial fixtures, uncertainty-aware reports, an independently reviewed replication protocol and negative findings if validity fails.

**Evidence reuse (not proof of a deployed control system):**
- [Human Kind agent protocol](https://github.com/Svyable/human-kind/blob/main/docs/agent-protocol.md) defines bounded repository authority and verification states; verified blob SHA `492ac962556db719cc6db4e40c0f37145cc7df5a`.
- [ScrolIQ model-evaluation methods](https://github.com/Svyable/scrollq/blob/main/docs/model-evaluation.md) define reproducible provenance, failure accounting and blind evaluation in the Vesuvius domain; verified blob SHA `f216b496b058d7d92b0e94620bba5346f5121335`.
- These public documents do not establish personal contribution to every line, independent agent-oversight efficacy or access to production traces.

**Provisional budget:** founder 300h $25,000; independent review $8,000; OTel adapter/integration $7,000; compute $4,000; fixture preparation $3,000; publication/admin $3,000. Total $50,000. Founder availability (25h/week) and subcontractors are unverified.

**Falsifiable targets:** on a frozen controlled holdout, >=80% detection of injected fabricated-success claims with complete traces, <=5% false contradiction flags on clean traces, and >=95% abstention for cases with missing decisive spans. These are proposed criteria, **not achieved results**. If data are insufficient or replication fails, publish the failure.

**Funding overlap:** TAIF and BlueDot are alternatives for shared agent-control deliverables. Allodial Track 03 would overlap passive trace-integrity methods. No hours, data, or code delivery should be charged twice. Disclose other applications and re-scope or withdraw if funded elsewhere.

**Site terms caution:** [CEA terms, updated 2026-10-01](https://funds.effectivealtruism.org/terms-and-conditions) describe user-submitted content as nonconfidential and include a perpetual noncommercial license and moral-rights waiver. These are site terms, not a grant contract. Avoid uploading confidential IP, manuscripts, employer documents or restricted datasets.

**Blockers before any application:** applicant/payee jurisdiction, actual 25h/week capacity, outside-work and IP permissions, truthful CV, exact [Paperform](https://av20jp3z.paperform.co/?fund=Transformative+AI+Fund) prompts (not readable in text fetch), overlap choice and explicit approval to submit.

**Economic model (screening assumptions only):** $25k founder allocation less 300h x $35 alternative labor = $14,500 conditional economic surplus. At 65% eligibility, 5% selection and $105 prep cost, forward EV = **+$366.25**, not a $50k profit claim. Selection probabilities are subjective, not observed grantmaker rates.

**Decision:** PURSUE preparation; do not submit or enter terms without applicant approval.
