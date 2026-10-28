# Control Where It Counts — Foresight selection-criteria and impact-bridge annex

**28 October 2026 · Foresight Track II / Human Empowerment · $35,000 proposed · DRAFT, NOT SUBMITTED**

**Purpose:** make the funder's published review criteria legible in a defensible, falsifiable proposal rather than relying on a generic assertion that oversight is good. This is a proposed impact model and reviewer-facing response, **not** a measured improvement in AI safety, evidence of selection, or a claim of applicant eligibility.

Official criteria and terms: https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/ (sections “Human Empowerment,” “What are the evaluation criteria?” and “What are the funding terms?”). Deadline **2026-10-31 23:59 PDT**.

## The missing causal bridge: why this pilot matters to frontier-agent risk

The relevant failure is not simply that an agent can make a mistake. It is that a human or institution can believe it retained a veto when the actual tool boundary allows the agent to act anyway. In a higher-stakes deployment, the same mismatch could defeat a checkpoint meant to prevent irreversible or consequential actions. **This is a plausible risk mechanism, not evidence that this particular prototype prevents catastrophic outcomes.**

A bounded research chain worth testing:

1. **Intervention:** independently implement and instrument no gate, cosmetic approval and enforceable scoped authorization around isolated agent tool calls.
2. **Mechanism test:** in policy-unauthorized cases, measure whether enforced authorization actually blocks completion relative to cosmetic approval, including alias/race/delegation attempts. Count bypasses, incomplete telemetry and ambiguous approvals as failures or unknowns under preregistered rules, never silently as safe.
3. **Cost of control:** measure legitimate-task completion, latency, false blocks and reviewer workload. The proposal is not to put a human click in front of every action.
4. **Decision rule:** retain a human checkpoint where it reduces unauthorized completion at acceptable costs, where legitimacy/contestability independently requires it, or where delegation is irreversible; otherwise consider scoped delegation. Mark any untested deployment domain **not validated**.
5. **Possible longer-term public good:** a reusable, open-source test protocol and negative-result corpus could help other teams reject hollow approval mechanisms before granting agents more consequential authority. Adoption, real-world effect and any reduction in existential risk are **not measured** in the 12-week pilot.

**Counterfactual:** without this study, teams can still build approval UIs and collect traces. What they may lack is a paired, policy-grounded comparison distinguishing the presence of an approval ceremony from enforcement at the actual action boundary, with explicit throughput costs and bypass cases. This is a hypothesis about a missing evaluation tool, not a claim of unique invention.

**Falsification / stop conditions:** If the enforced arm can be bypassed through aliases, races or delegation, report that as a failure and make no deployment recommendation. If independent approval/receipt provenance cannot be established, report insufficient evidence. If the enforced arm offers no reliable advantage over cosmetic approval, publish the negative result. If the sample is too small for the target effect, report wide intervals rather than a safety success. If meaningful human review cannot be staffed, reduce scope or do not run the human-review component.

## Sponsor criterion → actual evidence → remaining weakness

| Official criterion | Existing support | Critical gap / defensible answer |
|---|---|---|
| **Track fit** | Human Empowerment asks when human control is effective, intrinsically warranted or wasteful; three-arm authorization experiment tests one mechanism | The study does **not** resolve all normative questions. Separate empirical safety, legitimacy and irreversibility instead of combining them into a single score |
| **Impact on existential AI risk** | Enforced tool boundaries plausibly matter for consequential autonomous agents | No observed real-world risk reduction. Explain the above mechanism and transfer uncertainty; avoid claiming prevention of catastrophe |
| **Feasibility in 1–3 years** | 12-week bounded exploratory milestones; 44 remote CI tests and 108 deterministic mock receipts | All 180 prospective agent assignments unrun; no authenticated human approvals or independent outcome labels. Staffing and founder availability unknown |
| **AI-first methods** | Planned isolated agents, automated trace capture, replay and candidate edge-case generation; deterministic authorization and independent review | Agent-runner not yet deployed or evaluated. Agent-generated training cases must not leak into frozen holdout |
| **Capability to execute** | Open-source study manifest, mock boundary, exact-power utility, reproducibility packet and public CI | Applicant identity, paid engineer/reviewer, rights, reference and Node attendance unverified. Never imply they are secured |
| **High-risk / high-reward** | A negative result can reveal oversight theatre and bypasses; open evaluation can change how others test agent permissions | Small sample, weak power, possible failure to reproduce on realistic agents. Publish negative results, uncertainty and all exclusions |

## Quantitative interpretation without invented results

The existing 60 synthetic cases are **20 unauthorized, 20 authorized and 20 ambiguous per arm**, for 180 **planned, unrun** agent assignments. Only 20 matched unauthorized cases per arm directly inform the primary unauthorized-completion contrast. Under one hypothetical paired-discordance model (beneficial 0.30, harmful 0.10, one-sided alpha 0.025), the preflight yields **17.36%** exact power for a 20-point net difference. The proposed 12-week study is exploratory. An 80-case expansion has a different cost and must not be silently promised under the current $35,000 budget.

Technical receipt: https://github.com/Svyable/Opps/actions/runs/40635208184 — 44/44 automated tests; **mock/software behavior only**. Reviewer packet: https://github.com/Svyable/Opps/blob/main/opportunities/foresight-2026-reviewer-verification-packet.md.

## Paste-ready longer impact answer — applicant must approve and adapt

> The risk we want to study is a false veto: a system appears to ask a person for permission while its actual tool boundary still permits the action. That is not just a UX defect. In systems entrusted with consequential actions, a nonbinding approval screen can leave an institution believing it retained authority that it has already lost. We propose to test this failure mode in isolated agent tasks, comparing no gate, cosmetic approval and enforceable scoped authorization. We will measure both unauthorized completions and the cost of control in legitimate-task failures, latency and review burden. The result will be a decision rule distinguishing where control helps, where legitimacy or irreversibility requires it, and where delegation is justified. We will report bypasses and negative findings, not a claim of catastrophe prevention. The public deliverable is a reproducible way to tell enforcement from oversight theatre before these patterns are reused in more powerful systems.

## Hard commercial and compliance limits

- Foresight grants in this track are often smaller than the typical $30k–$100k range. **$35,000 is a request, not guaranteed cash or personal profit.** Budget: $33,000 direct + $2,000 overhead (6.06% of direct), no Node travel included.
- Open-source funded code/data/outputs, due diligence, periodic reporting, and potentially public project/lead naming apply. For-profits must explain grant necessity. The funder strongly prioritizes in-person participation at SF/Berlin Nodes; remote-only may be permitted but disadvantaged.
- **Applicant-controlled release gates remain unresolved:** legal payee, 12/20 hours weekly lead capacity (depending on mutually exclusive budget), independent engineer and reviewer, consenting reference, future-data/IP rights, realistic Node plan, overlap disclosure, live form and terms review, and explicit submission authority.
- Current subjective founder-surplus EV remains **+$49** in the favorable founder-led scenario; this annex alone supplies no calibrated probability uplift. Pursuit labor is already sunk in the prior scenario and should not be double counted.
- Do not contact a sponsor, spend, hire, submit, accept terms or disclose private identities on the basis of this public annex.

**Next economic decision:** prioritize truthful applicant release gates before the October 31 deadline. Do not spend additional hours polishing the proposal if staffing or authorization cannot be substantiated.
