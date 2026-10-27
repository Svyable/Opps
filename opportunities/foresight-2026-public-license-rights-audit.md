# Foresight Human Empowerment — public-code license and publication-rights preflight

**Checked:** 2026-10-27 UTC · **Status:** evidence audit only, **not a rights clearance or grant submission**.
**Sponsor:** https://foresight.org/grants/ai-science-safety-nodes-rfp-coordination-and-accountability/ (October 31, 2026, 23:59 PDT).
**Proposal:** Control Where It Counts — $35,000 proposed, 12 weeks, Human Empowerment.

## Decision this audit supports

The funder requires grant-funded **code, data and outputs to be open-sourced**. The public repositories presently referenced in the proposal have published licenses compatible with *ordinary reuse and open publication*, subject to their conditions. This removes the need to guess the public license on the cited starting artifacts. **It does not prove Sven/Svyable has authority to promise future work, relicense a third party's material, or accept an award.** The applicant must still check authorship, employer/contractor assignments, third-party input rights, and sponsor-specific terms.

## Verifiable source inventory

| Source / role | Public evidence | Observed terms | What this establishes / does not establish |
|---|---|---|---|
| Svyable/Opps — prospective Foresight sandbox, manifest, mock gate and tests | [LICENSE](https://github.com/Svyable/Opps/blob/main/LICENSE), Git blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | Apache-2.0 | Published permissive license for repository software; not proof of contributor authority or all embedded material. |
| Svyable/human-kind — authority/boundary concepts | [LICENSE](https://github.com/Svyable/human-kind/blob/main/LICENSE), blob `26cf250e7295d50c3b8e591669afb5ea719b63bd` | Apache-2.0 for code/config; CC-BY-4.0 for documentation/research, unless file overrides | Code can be reused with Apache notices; documentation reuse requires CC attribution and any exceptions must be checked. |
| Svyable/scrollq — provenance/reproducibility patterns | [LICENSE](https://github.com/Svyable/scrollq/blob/main/LICENSE), blob `e6d99fc9b241adba96cfa192bd0b0fc99d9ebf1a` | MIT, copyright (c) 2026 Sven Hardy Benson | Permissive code reuse with MIT notice; does not license third-party scroll scans or annotations for a new project. |
| Foresight `gate_runner.py` | [source](https://github.com/Svyable/Opps/blob/main/artifacts/foresight-control-2026/gate_runner.py), blob `848a592d15f3f1666c0964df3b68e462c7e16aa7` | Python standard-library imports `argparse`, `hashlib`, `json`, `dataclasses` | No direct external Python package imports observed in this source. Not a full transitive provenance audit. |
| Foresight `preregister.py` | [source](https://github.com/Svyable/Opps/blob/main/artifacts/foresight-control-2026/preregister.py), blob `ab88c116ffa8648ae1b68e9ca40e80d025f9f270` | Python standard-library imports `argparse`, `hashlib`, `json`, `random`, `collections`, `pathlib` | Synthetic scenario strings and unrun assignments; no real human/agent data represented. |

**Software status:** The existing mock gate and preregistration manifest are preparatory. The [28-test CI receipt](https://github.com/Svyable/Opps/actions/runs/40363475074) verifies deterministic behavior, **not** empirical AI-agent efficacy, independent reviewer work, human authentication or actual permission to publish future data.

## Reuse and publication policy to apply if funded

1. Keep Apache-2.0 and MIT copyright/license notices with reused code; mark modified files where Apache requires. Retain CC-BY-4.0 attribution for copied human-kind prose, and check file-level overrides.
2. Do not incorporate third-party CT data, customer data, private prompts, personal records, contractor code or model outputs into public deliverables without separately checking provenance and publication rights. The current proposed 60 synthetic scenarios do not need real scroll data.
3. Before commissioning engineers or reviewers, obtain actual permission/agreements covering ownership, attribution, open-source release and data/privacy handling. This audit does **not** create or accept such agreements.
4. Separate Foresight's prospective authorization intervention study from EA Funds' retrospective Control Evidence adjudication study: distinct funded hours, invoices, trials and results. Shared pre-existing permissive code may be reused with notices, but **never charge the same work twice**.
5. Do not make an unconditional open-source commitment until the applicant verifies the full dependency/data/contributor inventory and all award terms.

## Applicant-only clearance gates (remain OPEN)

- **Chain of title:** who authored each material component, whether an employer, client, coauthor or contractor owns any relevant rights; any contributor license exceptions.
- **New work:** proposed independent engineer/reviewer willingness and ability to license deliverables for public release.
- **Data/ethics:** whether real future agent traces can be published or require synthetic substitutes/redaction; personal data and private evaluation material.
- **Grant recipient:** legal payee, jurisdiction, tax/organizational documents, 12h/week or 20h/week founder availability, reference consent, and real Node/sprint participation.
- **Consent:** live Airtable text, advisor/Lightcone sharing, grant reporting and explicit applicant authorization.

## Sponsor-facing truthful sentence (only after applicant review)

“Preparatory code is published in repositories with Apache-2.0, MIT and, for some Human Kind documentation, CC-BY-4.0 terms. The proposed study will use synthetic sandbox inputs and will release eligible funded code, data and results under appropriate open licenses, subject to confirming contributor rights and privacy constraints before execution. No live agent evaluation or independent human adjudication has yet been conducted.”

**Decision:** technical public-license compatibility: **supported**. Full IP/contractor/data rights clearance: **unverified**. This audit must not be presented as legal advice, sponsor approval, a signed open-source commitment, or proof of research outcomes.
