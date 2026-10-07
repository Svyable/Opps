# ARC Prize 2026 — ARC-AGI-3

**Status:** PURSUE  
**Entry deadline:** October 26, 2026  
**Final submission:** November 2, 2026  
**Track pool:** $850,000  
**Named final awards:** $40k / $15k / $10k / $5k / $5k

## Existing asset

`Svyable/ARCPrize2026` already contains an interactive agent, offline evaluator, framework adapter, tests, and measured public-game results.

## Current evidence

The existing public baseline has been documented around ~0.29–0.30 mean public-game score. The reported bottleneck is inefficient blind exploration.

## Highest-value technical direction

Prefer a bounded object-interaction / rule-inference layer that ranks objects by:
- persistent state change;
- repeated-click response;
- target-pattern similarity;
- non-HUD effects;

then falls back to the current explorer.

This directly attacks the observed failure mode instead of adding generic search.

## Eligibility / packaging gate

Verify the repository contains an appropriate prize-eligible open-source license and all Kaggle submission requirements.

## EV

Eligibility appears good, but cash-placement probability is low at the current baseline. Keep pursuit cost low until a valid competition run yields private-score/rank evidence.

## Next concrete step

Run a valid Kaggle competition notebook and use the measured private score as the stop/go gate for further engineering.
