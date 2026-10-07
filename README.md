# Svyable Opps

A working registry for opportunities that can turn existing Svyable / Sven Hardy Benson assets into cash, contracts, grants, prizes, bounties, licensing revenue, paid research, consulting work, fellowships, sponsorships, or commercially valuable partnerships.

## Opportunity Matrix

The human + agent dashboard lives under `docs/`:

- **Pages dashboard:** https://svyable.github.io/Opps/
- **Machine registry:** https://svyable.github.io/Opps/registry.json
- **Agent map:** https://svyable.github.io/Opps/llms.txt
- **Markdown ledger:** [LEDGER.md](LEDGER.md)

> GitHub Pages must be configured to publish from the `main` branch `/docs` directory for the public URLs above to resolve.

## Operating rule

Optimize for **expected dollars earned**, not opportunity count.

Every opportunity should be evaluated on:

- payoff or plausible contract value;
- deadline;
- probability of qualifying;
- new work required;
- reuse of existing Svyable code, research, books, datasets, expertise, or IP;
- payer credibility;
- restrictions or problematic terms;
- expected value: **payoff × realistic probability − pursuit cost**.

## Statuses

- **OPEN** — discovered, not yet triaged.
- **PURSUE** — worth active effort now.
- **WATCH** — potentially valuable, but timing/fit/evidence is not strong enough yet.
- **REJECT** — poor expected value or weak strategic fit.
- **WON** — converted to money or a signed award/contract.
- **LOST** — pursued but not won or no longer available.

## Repository structure

- [LEDGER.md](LEDGER.md) — canonical human-readable deduplicated ledger.
- [docs/registry.json](docs/registry.json) — canonical structured registry for the dashboard and agents.
- [docs/index.html](docs/index.html) — zero-dependency dashboard.
- [docs/llms.txt](docs/llms.txt) — machine operating contract.
- `opportunities/` — one working brief per procurement / prize / program.

Facts must stay distinguishable from estimates and assumptions. Do not submit binding applications, accept terms, spend money, or make legal commitments without explicit approval.
