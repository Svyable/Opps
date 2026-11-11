# BlueDot Rapid — authorization fixture adversarial regression (2026-11-11)

**Decision:** BlueDot Rapid $4,500 Control Evidence request remains **PURSUE / submission blocked**. One concrete technical flaw fixed; this is not independent real-agent evidence.

## Reproducible negative test and fix
Previous `run_fixture(requests, allowed_actions=...)` used `action in allowed_actions` without validating the type of `allowed_actions`. Supplying the string `'read_public'` rather than a collection would authorize the shorter action `'read'` by Python substring membership, violating exact-match authorization. This is a fixture API misuse/security weakness, **not** an observed live-agent exploit.

Changed `artifacts/control-evidence-2026/control_fixture.py` to reject noncollection or malformed allowlists and normalize valid list/tuple/set/frozenset collections into a frozenset. Added three tests to `test_control_fixture.py` covering string bypass, malformed entries, and exact membership. Local command: `cd artifacts/control-evidence-2026 && python -m unittest -v` (equivalent copied bytes executed in isolated local directory): **8 tests passed, 0 failures** on 2026-11-11. The repository's post-commit GitHub CI and clean-checkout execution were **not** verified. No real tools executed.

## Current official rules and economics
Official program: https://bluedot.org/grants/rapid checked 2026-11-11: **up to $20,000**, time/living costs and research experiments eligible, ~15-minute application, no published fixed deadline; single lump sum after claim/checks; 60-day completion report; restricted payment jurisdictions and sanctions, approved-purpose restrictions. BlueDot is the named program operator; selection probability unpublished.

Proposed grant **$4,500** for 60h; illustrative delivery labor cost **$2,100** at $35/h, conditional surplus **$2,400** before tax/fees/overhead. If this fix consumed 0.5h ($17.50), it would need to raise joint award/payment probability by **0.73 percentage points** to pay for itself using that conditional surplus. No such improvement is observed. Actual probability, increment and monetary EV **unknown**; this is a break-even calculation, not a claim of positive EV. No external compute cost incurred. The code and test corpus are reusable research IP; licensing/ownership terms require review before grant acceptance.

## Release gates
Applicant/payee jurisdiction and sanctions, actual 60h capacity, rate justification, independently reproducible real-agent control trace, grant-versus-EA scope separation and application authorization remain unverified. Do not cite synthetic unit tests as measured AI safety effectiveness. No application, registration, contact, spend, contract or rights transfer.
