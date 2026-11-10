# 2026-11-10 — BlueDot Rapid $4,500 release decision: evidence-backed, no submission

**Status: PURSUE (blocked pending first-party verification).** This is an internal underwriting/eligibility decision instrument, not application text or an award claim. Source checked 2026-11-10: https://bluedot.org/grants/rapid

## What is actually verified
- Current BlueDot program permits research time/living costs, up to **$20,000**; ~15-minute application; lump-sum payment after claims and checks; no published fixed deadline or award rate.
- BlueDot course participation is **not mandatory** but course participation/alumni/facilitation or active AI safety/biosecurity community participation is a selection advantage.
- Official excluded payment jurisdictions: Afghanistan, Belarus, Burundi, Central African Republic, Chad, China, Congo Republic, Cuba, Democratic Republic of the Congo, Eritrea, India, Iraq, Iran, Libya, Myanmar, North Korea, Somalia, South Sudan, Sudan, Syria, Russia, Venezuela, Yemen; sanctions rules additionally apply. **No applicant jurisdiction has been verified**. Do not infer eligibility from repository location.
- Allowed spending is restricted to approved purpose; material changes require prior written approval; completion report due within 60 days of project/grant period ending; fees and FX can reduce payout.
- Existing repository code at `artifacts/control-evidence-2026/funding_release_gate.py` (Git blob e51a389a5fac4de072eaf00c1138b3b0ba83438a) rejects repeated stable scope IDs, including cross-funder duplicates. Tests at `test_funding_release_gate.py` (blob 0525c9e91bbd9bb5664be32f6091ed65149fd0c3) cover ten cases. **Code inspection only in this run**: neither tests nor CI were executed, and neither code nor tests establishes independently recorded research results or actual nonoverlap.

## Reviewer release gates — evidence, not assumptions
| Gate | Required first-party evidence | Current result |
|---|---|---|
| Eligible payee | Applicant name, actual payment country, sanctions/transfer eligibility | **UNKNOWN** |
| Researcher credibility | Applicant-specific CV/contribution evidence; AI-safety community work if any | **UNKNOWN** |
| 60 future hours | Dated capacity and project ownership affirmation | **UNKNOWN** |
| Research novelty/importance | Independent, reproducible recorder evidence and clear advanced-AI failure hypothesis | **UNVERIFIED** |
| Budget reasonableness | Defensible rate, taxes/fees, real milestones, explicit prospective hours | **UNVERIFIED** |
| Cross-funder exclusion | Human-signed mapping of BlueDot vs EA scopes, including differently named equivalents | **UNVERIFIED** |
| IP and obligations | Review payment, reporting, purpose restriction, pre-existing code licensing | **PENDING** |

**Release rule:** No application should be submitted unless applicant/payee, capacity, authentic evidence, exclusive budget, and terms are verified. No application submission or third-party contact authorized by this memo.

## Commercial economics (scenario, not forecast)
Requested $4,500 / 60 future hours at proposed $75/h. If 60h opportunity cost is $35/h, conditional margin = $4,500 − $2,100 = **$2,400**, before taxes/fees/overhead. A further 1h review at $35 gives break-even joint qualification×selection×payment probability = **1.46%**. This is *not* an empirical award estimate; actual probability and monetary EV remain unknown. The $4,500 is restricted funding, not automatic business profit. Marginal value of this memo is not measurable; do not claim odds uplift.

## Why this remains the highest-leverage small grant route
- **EA Transformative AI Fund:** https://funds.effectivealtruism.org/funds/transformative-ai; rolling, typically $10k–$150k, early-stage advanced-AI catastrophic risk focus. Larger possible check, but the existing $25k Control Evidence plan requires stronger independent technical evidence and nonoverlapping scope; no measured higher selection chance.
- **SOA Policyholder Behavior AI RFP:** https://www.soa.org/research/opportunities/2026/policyholder-behavior-ai-era/; due **2026-11-13**; historical project cost $25k–$50k is not an offer; researcher must author proposal in own words, disclose AI assistance, and accept substantial copyright/publicity obligations if awarded. Without a qualified actuarial lead, pursuing an AI-authored bid is inappropriate.
- **Frontier five benchmarks:** recorded at `opportunities/2026-11-07-frontier-five-benchmark-campaign.md`; no verified cash payout for the benchmark scores. Preserve technical research lanes but do not treat points as revenue.

**Decision:** Hold BlueDot at conditional PURSUE; do not invent credentials or additional synthetic evidence. The next money-relevant step is first-party evidence capture and an actual independent recorder/CI artifact, not another funding-validator refactor. Time-box future unfunded work; no spend, grant acceptance, IP transfer or submission.
