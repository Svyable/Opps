# NIH/NLM SPARK PubMed/PMC Challenge

**Status:** PURSUE
**Official prize pool:** $250,000
**Code/container deadline:** January 15, 2027
**Result submissions:** January 18–31, 2027
**Awards:** $100,000 first and $25,000 second for each of two tasks.
**Official source:** https://www.nih.gov/challenges/semantic-precision-ai-retrieval-knowledge-spark-pubmedpmc-challenge

## Fit

This is a direct reuse opportunity for Svyable's existing research, retrieval, agent, reproducibility and provenance capabilities:

- Desk: source-heavy research and synthesis.
- ScrollQ: provenance, falsification, hashes, reproducibility and evaluator-facing evidence.
- Agents: agent architecture and routing.
- Frontier Lab: measured ML experimentation and ablations.

The challenge requires grounded retrieval, citation-backed synthesis and reproducible containerized execution. Evaluation-time systems may use public open-weight models and open-source/public resources, but not proprietary hosted frontier-model APIs.

## Proposed system

Build an evidence-first retrieval stack:

1. Freeze the official PubMed/PMC challenge corpus and hash every input.
2. Hybrid lexical + dense candidate retrieval.
3. Open-weight reranking using question-component coverage and provenance.
4. Passage extraction bound to PMID/PMCID.
5. Task 1: calibrated known-item/provenance retrieval.
6. Task 2: local open-weight synthesis over retrieved evidence only.
7. Reproducibility passport with image, corpus, index and model hashes plus one-command evaluation.

## Cheap stop/go experiment

Before building the full system, create a public-data proxy benchmark with known PMID/PMCID targets and compare:

- BM25;
- dense retrieval;
- hybrid retrieval;
- hybrid + reranker;
- hybrid + reranker + query decomposition.

Record Recall@10, MRR, latency, peak memory and index size. Continue only if the more capable stack produces a repeatable material retrieval gain over BM25 within challenge resource and licensing constraints.

## Eligibility gates

Verify the actual entrant before registration. Official rules allow qualifying U.S. individuals/teams and U.S.-incorporated entities with a primary U.S. place of business. UEI is encouraged, not required. Entrants retain applicable IP rights subject to the challenge's nonexclusive federal licenses. Up to three submissions per task are allowed.

## Internal EV model

These are Svyable pursuit assumptions, not NIH estimates.

| Case | Prize target | Win probability | Pursuit cost | EV |
|---|---:|---:|---:|---:|
| Weak proxy; stop | $0 | — | ~$1,000 | -$1,000 |
| Credible Task 1 | $100,000 | 8% | ~$5,000 | +$3,000 |
| Strong two-task entry | up to $200,000 | 6% blended | ~$9,000 | +$3,000 |

## Next action

Implement the Task-1 proxy benchmark as a bounded Frontier Lab experiment or dedicated repo. Do not build a large synthesis stack until retrieval evidence clears the gate.
