# NLnet CodeSupply — November 2026 eligibility and submission-integrity audit

**Checked 2026-11-01. Status: REJECT for the 2026-11-03 intake under Svyable's current autonomous authoring/development workflow. This is an internal evidence-only screening memo, NOT an NLnet proposal, AI-authored application, or authorization to submit.**

## The real money and deadline

NLnet's [CodeSupply call](https://nlnet.nl/codesupply/) funds independent FOSS work on software-package metadata: origin, licenses, vulnerabilities, quality, federated catalogs, and open access. **First-grant requests: EUR 5,000–50,000**, against **EUR 400,000** reserved for auxiliary open calls, not an individual EUR 400k award. The current deadline is **2026-11-03 at 12:00 CET (11:00 UTC)**. NLnet is a long-standing Dutch public-benefit foundation and the programme is supported by the European Commission through Horizon Europe grant agreement 101298846. Neither the fund's budget nor historic awards establish any payment to Svyable.

Sources: [official CodeSupply call](https://nlnet.nl/codesupply/), [live application](https://nlnet.nl/propose/), [CodeSupply guide](https://nlnet.nl/codesupply/guideforapplicants/).

## The three actual knock-out gates

1. **No AI-written proposals.** NLnet's [GenAI policy v2.0, effective 2026-10-20](https://nlnet.nl/foundation/policies/generativeAI/2.0/) prohibits using GenAI to write, restructure, shorten or translate proposals or interactive evaluation answers, except disclosed accessibility needs. It also prohibits generative AI producing funded code, design or documentation; read-only analysis of human-written work is permitted. The [policy FAQ](https://nlnet.nl/foundation/policies/generativeAI/faq/) says prior LLM-generated code is not automatically disqualifying but must be disclosed. **This memo is AI-produced and must never be pasted or repackaged as a proposal.** The existing Svyable agent-oriented development practice is not evidence of a compliant human-only future delivery plan. No accessibility exception is asserted.
2. **Strong European dimension.** [NLnet's rule](https://nlnet.nl/OIS/european-dimension/) ordinarily requires **at least 60% of funds to people from Horizon Europe-eligible countries**. A project merely serving European users is insufficient. [CodeSupply eligibility](https://nlnet.nl/codesupply/eligibility/) leaves a narrow exception for exceptional technical expertise, not an automatic waiver. Applicant residency, nationality, actual contributors and payment allocation are not verified. No qualifying EU collaborator may be invented or recruited without approval.
3. **Software supply-chain metadata, not general AI assurance.** CodeSupply's three objectives are current/correct/comprehensive package metadata, democratic access to datasets, and a sustainable extensible data framework. Svyable's [Control Evidence local subprocess pilot](https://github.com/Svyable/Opps/blob/main/artifacts/control-evidence-2026/local_tool_receipt_pilot.py) measures local process/file evidence and has synthetic recorder-origin and replay gaps. It **does not currently publish an independently validated package-origin/license/vulnerability catalog**, an SBOM ecosystem integration, or downstream supply-chain users. Reframing agent-action receipts as package provenance without a concrete bridge would be misleading.

## Existing assets: verified and not verified

- [Svyable/Opps](https://github.com/Svyable/Opps) declares Apache-2.0 and contains local subprocess evidence, negative-control tests, and reproducibility notes. The [historical 82/82 CI run](https://github.com/Svyable/Opps/actions/runs/41170302920) verifies engineering tests, not external package metadata quality.
- [Human Kind](https://github.com/Svyable/human-kind) declares Apache-2.0 for code and CC BY 4.0 for non-code, and explicitly invites bounded agent contributions. Its repository does not establish a CodeSupply package-data service, European paid team, or human-only delivery.
- **Not verified:** proportion and provenance of LLM-generated source, any European paid contributor, eligible country, signed source rights, package registry partnerships, licensed SBOM feeds, grant overlap, committed human developer hours, independent user adoption, or applicant's lawful payee details.
- The October 20 policy does **not** automatically ban an existing AI-assisted codebase; it does ban AI authoring of new funded artifacts. Distinguish these conditions.

## Why not write a proposal now

The [live application](https://nlnet.nl/propose/) requests a human-written 1,000-character summary, task/budget breakdown, comparison to prior art, challenges, ecosystem, applicant background, funding overlap and AI-use disclosures. The [review guide](https://nlnet.nl/codesupply/guideforapplicants/) gives weights **30% technical excellence, 40% strategic impact, 30% value for money** and requires a first-stage weighted score **above 5/7**. Writing the actual responses using this autonomous agent would violate the current policy. No submission, resubmission, outreach, eligibility representation or future work promise is authorized.

## Economic screen — scenarios, not award probabilities

A **hypothetical** EUR 15,000 request (not a budget recommendation or sponsor quote) for 120 hours of future *human-only* work at an illustrative EUR 75/hour opportunity cost leaves EUR 6,000 conditional economic benefit before tax, admin and audit costs. Assume four human application hours at EUR 35/hour = **EUR 140**.

| Scenario | Qualification/capacity | Selection conditional on qualification | Economic benefit if awarded | Expected value |
| --- | ---: | ---: | ---: | ---: |
| Current AI-authored proposal/development | 0% compliant | n/a | EUR 6,000 hypothetical | **−EUR 140** if attempted; **EUR 0** by not attempting |
| Unverified human-only/EU pathway | 20% | 5% | EUR 6,000 | **−EUR 80** |
| Conditional, fully documented human/EU pathway | 80% | 10% | EUR 6,000 | **+EUR 340** |

These probabilities are subjective decision sensitivities, **not funder selection rates**. The last row requires facts that do not exist in the inspected repositories and ignores the cost of establishing an eligible team. The prudent current action is **no submission and no extra engineering**.

## Human-controlled reactivation gate

Only revisit a later CodeSupply call if **all** of these are documented by the applicant: (a) a genuine human-authored, human-revised proposal without generative drafting; (b) human-only future artifact production with AI confined to allowed read-only uses and full provenance disclosure; (c) named Horizon Europe-eligible contributor(s) allocated >=60% of actual funds, or an evidenced exception; (d) a concrete package-metadata output with independently reproducible baseline and a real user or upstream integration; (e) contributor rights, non-overlap, hours and payee evidence; (f) explicit approval of any application and terms. If any gate is absent, retain **REJECT** for this intake.

## Distinguish adjacent Restack programme

[Restack](https://nlnet.nl/restack/) is separately open for EUR 5,000–50,000 at the same November 3 deadline, but its official scope explicitly excludes AI-related projects **unless already used by more than one million active human users and directly relevant to the stack**. Svyable has no verified qualifying adoption. Do not double-submit the same agent-safety concept to Restack.

**Result:** One material eligibility weakness resolved before deadline: a tempting EUR 50k headline cannot be pursued by the present AI-authored pipeline. No application artifact was generated, no money spent, and no external party contacted.
