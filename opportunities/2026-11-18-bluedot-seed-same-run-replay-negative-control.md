# BlueDot Seed — same-run replay negative control (2026-11-18)

## Finding
The existing HMAC-SHA256 envelope verifier authenticates a record but does not consume an event or track previously accepted action IDs. A previously accepted, correctly signed event is accepted again **within the same run**, without needing the signing key. This is distinct from the cross-run replay already rejected by run-ID binding. It can inflate event counts or make an old observation appear to be a fresh one if a downstream consumer treats each VERIFIED return as a unique action.

## Exact reproducible evidence
Source: [recorder.py](../artifacts/control-evidence-2026/seed-recorder-envelope/recorder.py) (Git blob `7b44536c11fe313dda042bdd6a939d4151e342f2` at inspection).
Regression: [test_same_run_replay.py](../artifacts/control-evidence-2026/seed-recorder-envelope/test_same_run_replay.py).

Command: `cd artifacts/control-evidence-2026/seed-recorder-envelope && python -m unittest -v test_same_run_replay.py`.

Local reconstructed exact verifier text plus new test: **1 test passed, 0 failures**, Python unittest, exit 0. This passing *negative control* confirms two VERIFIED responses for one signed record. It does **not** demonstrate correct replay defense. The new test was subsequently committed; a full checkout/CI run has not been executed. The original nine tests were not rerun here.

## Release gate
For a reviewer-credible independent-recorder pilot, require an append-only event store with a unique, durable (run_id, action_id, event_id) key and monotonic recorder sequence, an authenticated trusted clock or ordering source where needed, atomic consume/insert semantics, and a negative test that the second presentation is REJECT rather than VERIFIED. A stateful consuming verifier should be separate from the existing pure signature validator; never equate a valid signature with a unique observed execution. Then add recorder process/key isolation and independently measured harmless file side effects.

## Commercial relevance
[BlueDot Seed](https://bluedot.org/grants/seed) officially offers **$20k–$200k** for 6–12 months, aims for decisions in about four weeks, and does not display a fixed deadline. It asks for a reasoned hypothesis, concrete first-month plan, and evidence of execution. This negative control improves honesty and reviewer falsifiability, but **does not establish an award probability uplift**. Existing Control Evidence reuse is high. Individual-founder payee, for-profit public benefit, tax/sanctions, monthly/final reporting and unspent-fund return are material restrictions. Eligibility, IP rights and award odds remain unknown.

Illustrative incremental labor: 1h at $35/h = $35, zero external spend. Under a **hypothetical** $10,000 retained net economic benefit, break-even joint success probability for this marginal labor alone is 0.35%; this is not an estimated success probability. Actual monetary EV is unknown. Stop further work unless the stateful uniqueness gate can be demonstrated with a bounded implementation and founder eligibility is confirmed.

No application, spending, third-party contact, contract or IP transfer.
