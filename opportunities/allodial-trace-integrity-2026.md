# Allodial Foundation — Track 03: Trace integrity and fabricated action claims

**Status:** PURSUE — applicant approval required; no application sent  
**Official source:** https://allodial.org/rfp/  
**Last checked:** 2026-10-19  
**Deadline:** Rolling, may close early once up to three awards are allocated  
**Published value:** Up to $50,000 per 12-week fixed-price research engagement

## Why this is relevant to Svyable

Track 03 asks for methods to compare an AI assistant's claims about completed actions with tool/runtime traces. Existing public Svyable work provides reusable *methods* for bounded agent action authority and provenance-aware evaluation:

- Human Kind: https://github.com/Svyable/human-kind
- ScrolIQ: https://github.com/Svyable/scrollq

Neither repository, by itself, establishes a validated detector for the sponsor's telemetry or holdout cases. The proposed method should be reference-free at runtime and report uncertainty and missing evidence explicitly.

## Sponsor requirements

- Select exactly one failure-mode track; Track 03 is trace integrity.
- Runtime may not require a canonical answer, paired probe, counterfactual prompt or altered user interaction.
- Input is text-based OpenTelemetry-style interaction data with tool calls; output is a corpus-level report with uncertainty.
- Working Python reference implementation, validation package and engineering handoff; stable I/O schema by week 4.
- Any runtime learned component must be an openly available self-hostable model.
- Permissive open-source licensing; published schedule is 20% kickoff, 30% week 4, 30% week 10, 20% holdout acceptance.

## Pre-submission / pre-contract gates

1. Confirm whether any award remains uncommitted. The published rolling status does **not** establish available slots.
2. Confirm applicant's legal contracting entity, authority, employment/IP restrictions, named method owner and 12-week availability.
3. Establish permitted access, retention, and redaction requirements for the sponsor's OTel data.
4. Agree in advance how trace gaps, abstentions, holdout metrics, a cure window and final-payment acceptance will be judged.
5. Confirm independent evaluation capacity; avoid claiming committed contractors or existing performance results.
6. Separate this scope and cost ledger from adjacent funding proposals. Do not bill overlapping work twice.
7. Obtain applicant approval before external contact, application, contract negotiation or signature.

**Public status only:** The detailed commercial bid and unsent application draft are maintained separately; they are intentionally not published in this repository.
