# Mozilla 2027–28 Independent Fellowship — verified remote CI evidence and decision gates

**Audit:** November 1, 2026 America/Chicago (remote run occurred November 2 UTC). **Status:** WATCH; no application, contact, account registration, funding request, license or contractual acceptance. This is an evidence index for an applicant-authored LOI, **not** an AI-written application answer.

## Official payer, fit and deadline

- [Mozilla Foundation official 2027–28 call](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/) and [October 25 updated FAQ](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/faqs/): Independent Fellows receive a **$100,000 personal stipend plus a $25,000 restricted project budget** for a June 2027–May 2028 fellowship. This is not $125,000 in unrestricted Svyable revenue.
- **Letter of Intent:** December 17, 2026, **11:59 p.m. Pacific (UTC−8)**. Late LOIs are not accepted. Mozilla Foundation is an established nonprofit with public fellow cohorts; selection probability is not published.
- The call explicitly prioritizes **shared security and audit infrastructure for small organizations**. The RFP discusses affordable tools for organizations using agents. The [official FAQ](https://www.mozillafoundation.org/en/what-we-do/grantmaking/fellowship/2027-call-for-applications/faqs/) clarifies that **working technology and users are welcome but NOT required for fellowship eligibility**. A user need and plausible community benefit still matter for evaluation; do not present missing pilot organizations as a hard eligibility exclusion.
- The FAQ also says **individual applicants only** and legal ability to receive funding from a US 501(c)(3) is required; Independent Fellows generally have senior experience and a developed prototype/project. The applicant's individual qualifications and legal receipt remain unverified.
- Existing [preflight](mozilla-fellowship-2027-independent-agent-audit-preflight.md) records open-license obligations and application AI-use boundaries. The applicant must write their own substantive answers; this document is not submission text.

## Material new evidence: GitHub Actions verified, not merely local

**Run:** [41375155596](https://github.com/Svyable/Opps/actions/runs/41375155596), **commit** [16b385d62eb96741e3418e010fc36f1d97e21218](https://github.com/Svyable/Opps/commit/16b385d62eb96741e3418e010fc36f1d97e21218), **job** [125053670853](https://github.com/Svyable/Opps/actions/runs/41375155596/job/125053670853).

- GitHub Actions run created **2026-11-02 01:57:43 UTC**, completed **success**. The single `smoke` job completed **success**; all nine test steps completed successfully.
- Workflow: [control-evidence-contract.yml](../.github/workflows/control-evidence-contract.yml), Ubuntu runner, Python **3.11** configured with `actions/setup-python@v5`. No credentials, paid services, real inbox or live agent are required by these synthetic regression suites.
- The decoded **remote job log** shows nine completed Python test suites with counts **14 + 9 + 11 + 11 + 10 + 12 + 10 + 5 + 14 = 96**, each followed by `OK`. This is **96 remote passing regression tests**, not 96 independent field observations or a measured security success rate.
- The new [run-bound receipt test file](../artifacts/control-evidence-2026/test_run_bound_receipt_demo.py) alone reports **14/14 remote tests passed in 0.299 seconds**. The older recorder-gap suite reports **5/5**; it intentionally demonstrates that a self-declared `writer: independent` label can be spoofed. Passing vulnerability-characterization tests does **not** mean the original design was secure.
- Verified from the GitHub Actions run metadata, jobs endpoint and decoded job logs, rather than relying on the earlier local 14/14 report.

### Reviewer-facing, bounded claims

| Claim | Evidence | Do NOT infer |
|---|---|---|
| Local subprocess observations can be bound to a run ID, expected payload digest and supervisor MAC | [Implementation](../artifacts/control-evidence-2026/run_bound_receipt_demo.py), 14 remote regression tests | Independent cryptographic attestation, trusted third-party observation or production security |
| Replayed, altered, wrong-key and wrong-run receipts abstain in tested scenarios | Remote test cases for replay, MAC, run/payload substitution, tampered return code | Durability across process restarts; replay cache is in-memory |
| A prior self-asserted recorder label is spoofable | [Five gap tests](../artifacts/control-evidence-2026/test_receipt_authenticity_gap.py) | Real-world exploitation or an external audit |
| Entire synthetic Control Evidence workflow is reproducible in GitHub Actions | 96/96 remote tests, nine suites, successful job | Nonprofit adoption, usability, user interviews, independent reviewers, a live inbox agent or grant qualification |

**Threat boundary:** HMAC proves shared-key possession; the supervisor, verifier and secret must remain trusted. The replay set is process-local, not durable. There is no cross-host attestation, trusted clock, deployment, externally permissioned agent trace, independent penetration test or human-review outcome.

## Economic decision: verify, do not inflate odds

- The **$25k project budget** is restricted. Model only an illustrative **$40k** personal economic surplus from the $100k stipend *after* displacement, not the gross package.
- Previous future-LOI central sensitivity: **40%** applicant feasibility × **0.5%** conditional selection × **$40k** net stipend surplus − **$105** applicant labor = **−$25**. These probabilities are subjective, not sponsor statistics.
- Estimated incremental effort to verify the remote run, decode job logs and prepare this reusable evidence record: **0.5h × $35/h = $17.50**. **Measured selection-probability uplift = none**. On a strict award-only basis the standalone incremental EV is **−$17.50** absent reviewer time saved or cross-funder reuse.
- Break-even uplift for this $17.50 step alone would be **0.1094 percentage points** of conditional award probability at 40% applicant feasibility and $40k conditional net benefit: $17.50 / (0.4 × $40,000). No such uplift is claimed.
- Positive value is factual risk reduction: replacing an unverified remote-CI assertion with a traceable run, exact test count and threat boundary, reusable in Mozilla, BlueDot and EA Funds without double-charging prior work.

## Applicant-controlled decision gates

1. Verify genuine personal senior-level builder/leadership experience and role in public code; Git commit attribution alone is not proof.
2. Verify lawful receipt of US charity funds, individual payee, 12-month availability and any actual overlapping awards.
3. Decide whether open licensing of funded code/nonconfidential outputs is acceptable and ensure all contributor rights permit it.
4. Document a concrete small-organization use case and credible community benefit. **Do not invent users or partners.** The FAQ says existing users are not mandatory, but applicant must explain public benefit.
5. Applicant independently authors the LOI, checks AI-use disclosure and live form terms, and explicitly authorizes submission. No application or external inquiry has been made.

## Opportunity comparison (screened, not advanced)

- [Atlassian Codegeist 2026 official rules](https://codegeist2026.devpost.com/rules): **$120k aggregate cash**, three $15k first prizes, three $8k second, three $5k third, and $1.5k bonuses; deadline **Dec 22, 2026, noon PST**. Requires a genuinely installed **Forge** app with Atlassian integration, installation link and YouTube demonstration; Svyable has conceptual agent/evidence reuse but no verified Forge app. Illustrative first-prize-only EV **$15,000 × 70% feasible × 0.5% win − 12h × $35 = −$367.50**. Established Atlassian/Devpost payer; personal/organizational eligibility, IP and developer terms unverified. **REJECT cash-first build** absent existing Forge integration.
- [Codex × TwitchCon official rules](https://twitchcon-codex.devpost.com/rules): **$25k aggregate cash**, $10k first, $6k second, $4k third, two $2.5k runners; deadline **Nov 2, 2026, 2 p.m. PST**. Requires **new** Twitch-connected interactive project built during contest period, Codex session ID, functioning Twitch footage and YouTube demo; Svyable's cinematic channels offer only modest reuse. Illustrative first-prize-only EV **$10,000 × 60% feasible × 0.3% win − 10h × $35 = −$332**. Amazon Advertising/Devpost credible, but personal eligibility, source rights, publicity and arbitration terms need review. **REJECT** for cash-only pursuit.
- [GEMS official competition](https://www.drivendata.org/competitions/306/): **$300k aggregate**, Dec 3. Significant existing [GEMS-CONTEST](https://github.com/Svyable/GEMS-CONTEST) reuse, but §1.3/§1.4 U.S. cash eligibility and genuine commercialization remain applicant-controlled and unverified. Existing known-fault CV scores are **not** hidden-fault prize probabilities. Remains **WATCH**.

**Decision:** Mozilla remains WATCH for the *personal applicant* gate, with a newly verified technical proof point. This run did not demonstrate higher selection odds, real-world security, adoption or grant eligibility. No entry, account registration, submission, contact, spend or IP grant.
