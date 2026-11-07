# Svyable Frontier Benchmark Campaign — 2026-11-07

## Decision

Target **all five named benchmark families** while concentrating the next technical experiment on **EC Rank**, whose user-reported closing date is 2026-11-14. Use **ECDSA.fail** as the longer-running Rust optimization lane. This is a technical-research mandate, not authorization to submit, accept terms, pay for infrastructure, or promise a cash reward.

**Economics:** No verified dollar prize or guaranteed conversion of Yukon Points into cash was established for these five contests as of this audit. Therefore direct cash payoff is **UNPRICED**, qualification is conditional on platform terms and original work, and prize-based EV cannot responsibly be positive-assigned. Each sprint gets a zero-spend labor stop-loss; reassess when actual compensation is documented. Do not treat leaderboard score as cash.

## Opportunity lanes and rules

| Priority | Challenge / actual upstream | User-reported deadline | Current public target (2026-11-07 source snapshot) | Contract and first step |
|---|---|---|---|---|
| 1 — urgent | **EC Rank** (Yukon `ec-rank`, [Layr-Labs/elliptic-rank-challenge-public](https://github.com/Layr-Labs/elliptic-rank-challenge-public)) | 2026-11-14, **not independently confirmed in upstream repo** | Leader 407.542488; *higher is better* | Find ORIGINAL integral/rational curves over Q, certify genuinely independent points with PARI/GP 2.17.4, check novelty against known/isogeny/twist gate, keep existing board cells and run official score. **Not Ethereum consensus ranking.** |
| 2 — sustained | **ECDSA.fail** ([Layr-Labs/ecdsafail-challenge](https://github.com/Layr-Labs/ecdsafail-challenge), Yukon ECDSA.fail CLI) | 2026-12-31, user-reported | Live independent dashboard 890,237,211; *lower is better*. 896,396,908 was an earlier score | Modify only `src/point_add/`; run 9,024-shot reversible correctness, ancilla cleanup, phase and forward/reverse checks; optimize Toffoli × live qubits. CLI authentication required for platform submission. |
| 3 — engineering | **FLock / SNARK.fast** ([Layr-Labs/flock-challenge-multi](https://github.com/Layr-Labs/flock-challenge-multi) x86; [Layr-Labs/flock-challenge](https://github.com/Layr-Labs/flock-challenge) Apple Silicon) | No cutoff independently established | x86 Yukon leader 2,078,747 verified BLAKE3 compressions/s; *higher is better*. Earlier 1,988,521 snapshot is stale | 262,144 BLAKE3 compressions per proof, 100 ranked trials, trusted verifier; edit `flock-core/src` or `flock-prover/src`. Establish baseline on comparable hardware; changes below ~1% x86 can be noise. Never compare x86 and Mac absolute scores. |
| 4 — long horizon | **Proximity Prize**, [proximity-prize/proximity-prize](https://github.com/proximity-prize/proximity-prize) | 2027-09-19, user-reported | Four Lean certificate tracks. Original lower 53.00 and upper 128.00 are *seed baselines*, not leaderboards | Two original Koala tracks plus two binary tracks. Lower **maximize B**, upper **minimize B**. Learn Lean 4.34 protocol and replay kernel; only touch each track's `Submission*` folder; no `sorry`. First establish a trusted baseline build and theorem replay; avoid mixing profile versions. |
| 5 — frontier theorem | **CircuitBreaker** ([Layr-Labs/circuitbreaker-llm-verifier](https://github.com/Layr-Labs/circuitbreaker-llm-verifier)) | None verified | Current public reviewed/evaluated frontier is roughly **4n − lower-order terms**, coefficient 4, exponent 1; not 'no best yet' | Prove unconditional gate lower bound for one eligible uniform NP Boolean family. Multi-objective Pareto, manual promotion and independent probabilistic reviewer. First audit scope and a complete original proof plan; do not claim P≠NP or confuse LLM review with theorem verification. |

Upstream GitHub repository names differ from the user-supplied benchmark slugs; map by official README and `benchmark.json`, do not assume a slug is a GitHub owner/repo.

## Today's material EC Rank experiment

Created an original, deterministic, stdlib-only integer candidate search:
- [ec_rank_probe.py](../artifacts/ec-rank-2026/ec_rank_probe.py)
- [test_ec_rank_probe.py](../artifacts/ec-rank-2026/test_ec_rank_probe.py)

Local Python execution: **9 of 9 unittest checks passed** (algebraic substitution, non-singularity, one positive y per x, sorting, deterministic report hash, bad input rejection). Source Git blob hashes cross-checked with the locally tested exact bytes: script `d4126114d8edc8d48cd1d179ba7c84e289c2697b`; tests `c79a83d11109c8d7106990c0de6b782b5d97d055`.

Unranked sweep: `python3 ec_rank_probe.py --amax 30 --bmax 60 --xmax 20 --min-points 6 --limit 5` found five top candidates with 10, 9, 9, 9, 9 distinct integer-x positive-y witnesses. Reproducibility digest `098430756d606a35dea93ffa2112dfe9e63527a2a8f1faee7f0742afc9c4ecb6`. First generator output: integral model `[0,0,0,-28,52]`, 10 algebraically checked integer point representatives. **This is NOT evidence of rank 10**, no point independence/novelty/minimality/PARI certification was run, and it has **no official score**. Source algorithm uses original exhaustive enumeration, not copied leaderboard curves. Do not submit these as rank claims.

PARI/GP 2.17.4 and official scorer were not available in the local runtime; GitHub connector inspection does not run the organizer's benchmarks.

## Next experiments and non-negotiable gates

1. **EC Rank first (deadline):** obtain pinned PARI/GP environment, run upstream novelty/minimality/height-pairing tests on original candidates, and retain dated generator logs. Abort this attempt if no independently certified positive leaderboard improvement emerges within the time budget.
2. **ECDSA.fail:** pin exact `point_add` source, reproduce a valid reference score, profile non-output qubit lifetimes and Toffoli-heavy arithmetic; test a single reversible optimization with all 9,024 official cases before considering CLI authorization.
3. **FLock:** use x86 benchmark if no Apple Silicon; benchmark controlled proof throughput locally, optimize one allowed prover-only phase and require verifier success plus gain > noise before pursuing official timing.
4. **Proximity:** set up all four separate Lean track baselines and record certificate/axiom checks; select the smallest tractable proof obligation rather than assuming lower/upper score directions are identical.
5. **CircuitBreaker:** inspect accepted full statements, identify exact theorem requiring an unconditional proof, do a reviewable first-principles proof audit; no conjectural claims presented as new bounds.

Time-box: 2h unpriced technical discovery for EC Rank; 2h ECDSA baseline; 2h FLock benchmark; 2h Proximity toolchain; 1h CircuitBreaker theorem-scoping. **Zero external expenditures**. Explicit approval is required for account registration/submission, binding terms, data/IP transfers and paid compute. If no verified remuneration and no demonstrable technical milestone, pause further labor pending a value decision.

## Monetary expected-value handling

If a verifiable individual cash award `A` is confirmed, model `EV = A × P(eligible) × P(win | eligible) − incremental labor − infrastructure − rights/opportunity costs`. At the moment `A` is **unknown** for every lane; assigning a numerical positive cash EV would be invented. With a hypothetical cost of $35/hour, the 2h proof-of-feasibility costs $70 and is not rationalized as guaranteed cash. Research and reusable IP may have noncash value, but must be reported separately.

## Source register

- EC Rank: https://www.yukon.org/ecrank ; https://github.com/Layr-Labs/elliptic-rank-challenge-public/blob/main/README.md ; RULES.md
- ECDSA.fail: https://www.ecdsafail.rocks/ ; https://github.com/Layr-Labs/ecdsafail-challenge/blob/main/README.md
- Proximity: https://github.com/proximity-prize/proximity-prize/blob/main/README.md ; benchmark.json
- FLock: https://www.yukon.org/flock ; https://github.com/Layr-Labs/flock-challenge-multi/blob/main/README.md ; https://github.com/Layr-Labs/flock-challenge/blob/main/README.md
- CircuitBreaker: https://www.yukon.org/circuitbreaker ; https://github.com/Layr-Labs/circuitbreaker-llm-verifier/blob/master/benchmark.json

No submissions, challenge registrations, prize claims or outside communications were made.
