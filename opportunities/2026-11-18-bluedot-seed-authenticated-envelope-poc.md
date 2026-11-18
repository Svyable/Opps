# BlueDot Seed — authenticated envelope proof-of-concept (2026-11-18)

**Status: WATCH. Not a deployed independent recorder.**

## What actually ran
The isolated Python HMAC-SHA256 observation-envelope prototype is at [recorder.py](../artifacts/control-evidence-2026/seed-recorder-envelope/recorder.py) with [nine tests](../artifacts/control-evidence-2026/seed-recorder-envelope/test_recorder.py). Run from that directory: `python -m unittest discover -v`. Local Python execution: **9 run, 9 pass, 0 fail**, exit 0. Exact Git blob SHA-1 values of locally tested bytes and GitHub file contents match: recorder `7b44536c11fe313dda042bdd6a939d4151e342f2`; tests `4c259972b120f20277078b217e4f7e1954da8414`. Tests cover valid envelope, forged tag, unsigned substitution, *signed* substitution, run replay, digest mismatch, missing event, explicitly unobserved event, and schema extra field.

## What this does NOT prove
The HMAC key is hardcoded **only in tests** and is not isolated from an agent. The `sign` function is callable by any holder of the key; therefore the signed-substitution test checks approved-path binding, **not attacker-resistant origin**. No separate process, key custody, executor isolation, file-write side effect, independent final-state observation, crash/recovery test, recorder-compromise test, or 100-trial campaign has been implemented. An authenticated statement is not proof that an action occurred. Do not claim safety efficacy or independent observation.

## Official payer and conditions
[BlueDot Seed](https://bluedot.org/grants/seed), checked 2026-11-18, publishes $20k–$200k for a new 6–12 month project, about four-week decisions and no fixed deadline; review emphasizes problem selection, hypothesis, execution evidence and concrete plan. Normally pays individual founders; for-profit exceptions take longer. Monthly updates, final report, unspent-fund return, tax and geographic restrictions apply. This proof-of-concept strengthens *execution evidence*, not applicant eligibility.

## Economic stop/go
Reuse of Control Evidence receipt-auditor work is high. Incremental work was local code/test and repository commits; no purchased services. At an illustrative 1.5h × $35/h = **$52.50 internal labor**, and hypothetical **$10,000 retained economic benefit** after delivery, marginal break-even joint success probability is **0.525%**, ignoring all future work. This is not an estimated probability; actual qualification, selection, payment and incremental win-probability uplift are **unknown**, so monetary EV cannot be honestly signed positive. $20k–$200k grant face value is restricted project funding, not profit.

**Next gate:** move the key into a separately controlled recorder process and verify a harmless file write from an independently read final-state digest. Keep BlueDot Seed WATCH until demonstrated, and require founder/payee/IP/budget verification before submission. Do not submit or accept terms autonomously.
