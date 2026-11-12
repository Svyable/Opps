# EA Transformative AI Fund — application draft (NOT SUBMITTED)

Prepared 2026-11-12. **Conditional PURSUE; do not submit until release gates pass.** Official program: https://funds.effectivealtruism.org/funds/transformative-ai (always open; typical awards $10,000–$150,000; primarily catastrophic-risk reduction from advanced AI). Payer record: https://funds.effectivealtruism.org/grants .

## Proposed project title
Control Evidence: measuring whether an external authorization gateway prevents prohibited AI-agent tool actions without blocking legitimate ones.

## Project summary (draft for applicant verification)
AI agents can propose tool actions that conflict with an operator's explicit authorization policy. We propose a preregistered, paired, reproducible evaluation of an instructions-only baseline against an external authorization gate, using a no-network mock-tool gateway. We will report unauthorized executions per unauthorized proposed call and false denials per authorized proposed call, with denominators and raw event records published subject to privacy/security review. We will test legitimate requests, unauthorized requests, prompt injection and malformed calls. We will not claim that this small evaluation establishes protection against catastrophic AI risks; its possible contribution is a narrower measurement method for agent-control mechanisms.

## What already exists (do not inflate)
- Synthetic authorization fixture and adversarial unit tests: artifacts/control-evidence-2026/control_fixture.py and test_control_fixture.py.
- Corrected paired scorer and 14 regression tests: artifacts/control-evidence-2026/score_pilot.py and test_score_pilot.py.
- Preregistered prospective 40+ scenario protocol: opportunities/2026-11-11-ea-transformative-ai-control-evidence-preregistered-pilot.md.
- Existing tests were reported as 14/14 on equivalent local source; **clean-checkout parity, CI, independent gateway-event provenance, and real-agent outcome data have NOT been verified.**

## Proposed deliverables (not results)
1. Frozen scenario manifest and authorization policy per scenario, including negative controls and preregistered exclusions.
2. Independently generated mock-tool execution log, with explicit trust boundary and tamper-evident digest; scorer input must not be manually invented.
3. Paired evaluation and full counts/denominators; disclose undefined rates, missing calls, failed runs and uncertainty.
4. Reproduction instructions and an independent replay, plus limitations and threat-model analysis.
5. Public technical report, with redactions only for genuinely sensitive content.

## Budget — illustrative, not a funding request yet
80 hours of research/engineering at a **hypothetical** $35/hour = $2,800 opportunity cost. A $10,000 grant is an illustrative lower-range award, **not a justified request**: the remaining $7,200 needs an itemized, eligible, necessary budget or the ask must be reduced. No compute or API purchases are authorized. Avoid representing unrestricted surplus as project expense. Funding nonoverlap with BlueDot and other sources must be established.

## Theory of change and critical counterargument
If external policy enforcement reduces unauthorized executions under realistic adversarial conditions without excessive false denials, an open measurement protocol could help researchers compare agent-control designs. **Critical weakness:** mock-gateway performance may not transfer to deployed agents or meaningfully reduce global catastrophic risk; a funder may reasonably prefer more direct work. Application should specify downstream users, a credible adoption path and a falsifiable decision rule, or be withdrawn.

## Required evidence before submission
- [ ] Applicant legal identity, country/payment eligibility, and ability to accept grant terms verified by applicant.
- [ ] Applicant's actual qualifications, prior work, time availability, and ownership/rights verified; do not fabricate credentials.
- [ ] Execute exact committed tests from a clean checkout and preserve command, Python version, SHA and output.
- [ ] Produce real-agent paired traces from an independently instrumented gateway; document event provenance and limitations.
- [ ] Itemize eligible expenses and justify requested amount; confirm no duplicate funding.
- [ ] Review current application questions, grant agreement, tax treatment, publication and IP clauses before applicant approval.
- [ ] Establish credible catastrophic-risk pathway; otherwise retain WATCH or stop.

## Decision economics (illustrative, not a probability estimate)
For a hypothetical $10,000 award and $2,800 delivery labor, conditional net before other costs is $7,200. Four hours of preparation at $35/hour cost $140. A simplified break-even joint qualification/award/payment probability is $140/$7,200 = 1.94%, assuming no additional costs and that all grant funds are legitimately usable for this work. **Actual probability and monetary EV are unknown.** Incremental probability uplift from this draft is unmeasured. Stop further drafting until the real-agent evidence and budget gates are resolved.

No application, spending, outreach, terms acceptance, or IP transfer authorized by this document.
