# TAIF Control Evidence — clean-checkout verification gate (2026-11-15)

## Decision

**PURSUE / HOLD; Gate A not passed.** The latest hunter release specification requires the complete committed unit suite before any reviewer-facing empirical claim. This run attempted to fetch the actual repository and run the suite, but network DNS resolution prevented checkout. This is a **negative environment-access test**, not a failing code test or a passing code test. Do not claim improved agent safety.

## Exact attempted command and result

```sh
git clone -q --depth 1 https://github.com/Svyable/Opps.git /tmp/svyable-opps && cd /tmp/svyable-opps && python -m unittest discover -s artifacts/control-evidence-2026 -p 'test_*.py'
```

Exit code **128** at clone; stderr: `fatal: unable to access 'https://github.com/Svyable/Opps.git/': Could not resolve host: github.com`. The unittest command **never ran**. The test count is **not available** for this run. No local checkout, code patch, trace, or official benchmark result was produced.

## Minimal reproducible next action

1. In a network-enabled runner, pin the Git commit SHA and Python version, then execute `python -m unittest discover -s artifacts/control-evidence-2026 -p 'test_*.py' -v`; preserve workflow URL, exit code, stdout/stderr, commit SHA and artifact hash.
2. Confirm the tests cover malformed scenario IDs, nonboolean authorization flags, missing/orphan executor receipts, and duplicate call IDs. Any absent test is a specific engineering task; do not infer coverage from names alone.
3. Separately execute the external-recorder feasibility test from [independent execution specification](2026-11-15-taif-independent-execution-release-spec.md). Unit tests, even if green, do not establish independent tool-execution efficacy.
4. Only then revisit the eligible, exclusive project budget and applicant eligibility. No BlueDot/TAIF double billing.

## Funding economics and source check

[EA Transformative AI Fund](https://funds.effectivealtruism.org/funds/transformative-ai) is rolling, with typical **$10,000–$150,000** early-stage grants to individuals and organizations starting new transformative-AI projects. The official [EA Funds platform](https://funds.effectivealtruism.org/) publishes its grantmaking record; payer is credible. Existing Svyable gateway/scorer/tests have high reuse. Applicant jurisdiction, legal payee, rights, legitimate incremental costs and selection probability remain unverified. Grant face value is restricted project financing, not founder profit. **Cash EV unknown**, and no probability uplift is defensibly measurable from a failed clone. At illustrative $35/hour, 0.25h triage costs $8.75; further speculative work should be stopped until a real test environment is available.

BlueDot Rapid's [official grants index](https://bluedot.org/grants) shows **up to $20k**, but the [direct page](https://bluedot.org/grants/rapid) has served a **$10k** variant; do not treat either as approved reimbursement. The five frontier benchmark lanes remain unpriced and must not be represented as cash awards.

**No application, spending, external contact, contract, benchmark submission or IP transfer.**
