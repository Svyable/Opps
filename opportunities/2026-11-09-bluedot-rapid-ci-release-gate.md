# BlueDot Rapid — CI evidence path for funding release gate (2026-11-09)

**Status:** conditional PURSUE; internal grant-compliance artifact, not sponsor approval, independent recorder evidence, or application.

## Concrete gap closed
The committed `funding_release_gate.py` and its 10 synthetic `unittest` cases were previously not included in the GitHub Actions receipt workflow. That made the funding-integrity check easy to miss in routine pushes. Commit [963f60e](https://github.com/Svyable/Opps/commit/963f60e062d5a69e590eafb59cb5c0a988ded3b2) adds both files to push path triggers and runs `test_funding_release_gate` alongside existing receipt tests. The existing artifact upload records raw test output for subsequent inspection.

**Evidence distinction:** GitHub workflow source was read and changed through the repository connector. The earlier 10/10 local test result is historical, **not** a new CI result. No new workflow run ID, pass/fail status, or artifact log has been inspected during this run. Do not present CI as green until a completed job and raw log are independently checked. The gate tests use synthetic allocations and do not validate real expenses, semantic equivalence, eligibility, or funder authorization.

## Official funding terms, checked November 9
[BlueDot Rapid Grants](https://bluedot.org/grants/rapid): up to $20,000, including research time and living costs; no published fixed deadline or average decision time; claims-portal lump-sum payment after checks; completion report within 60 days; funding restricted to approved purpose and material changes require written approval. Course participation is advantageous but not mandatory. The payer is identifiable and has [published real prior awards](https://blog.bluedot.org/p/weve-given-out-50000-in-rapid-grants). The proposed $4,500/60-hour Control Evidence scope remains unawarded.

[EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai): rolling, typical $10,000–$150,000; proposed $25,000 Control Evidence project remains distinct only if deliverables and costs are actually segregated. [BlueDot Media](https://bluedot.org/grants/media): $20,000–$200,000, 6–12 months, requires creator-controlled audience evidence, still absent. No measured selection odds for any.

## Economics and stop rule
Potential $4,500 BlueDot gross grant, with 60 future hours at illustrative $35/h cost = $2,400 conditional pretax surplus before taxes/overhead; $75/h proposed reimbursement rate requires substantiation. Incremental workflow edit estimated 0.25h × $35/h = $8.75. **No measurable award-probability improvement**: incremental standalone cash EV = −$8.75 before reuse and avoided compliance errors. Break-even improvement in *joint award probability* using $2,400 conditional surplus is $8.75/$2,400 = **0.365 percentage points**. This is a threshold, not an odds estimate. Actual EV unknown.

**Next evidence gate:** obtain a completed CI run URL and raw test artifact, first-party lawful payee/jurisdiction, 60 available future hours and defensible rate, independently controlled recorder evidence, and explicit nonoverlap election against EA. No more code polishing absent a specific failing test or reviewer need. No spending, applications, outreach, grant terms acceptance or IP transfer.
