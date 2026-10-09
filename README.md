# InvestorVerify — Evidence-first investor database

A small, reproducible Python research pilot for **Assignment A: Reliable Investor Database**.

**Pilot:** venture capital organizations with a Czech market or office connection (not necessarily Czech legal domicile). **Status:** first AI-assisted web screening, **eight candidate classifications independently audited (6 investors, 2 excluded non-investors); N1 brand/entity continuity pending**.

## Why this project exists

Investor directories frequently mix actual funds with advisers, associations and information portals. An AI-generated list can also confuse fund size, assets under management, typical investment amount and capital raised by investee companies. InvestorVerify keeps every material claim attached to a source, and separates machine predictions from independent human decisions.

## Current deliverables (2026-10-09)

- [Research design and inclusion/exclusion rules](docs/PLAN.md)
- [Candidate registry](data/candidates.csv): 27 candidates: 8 manually audited entries (including Purple Ventures) and 19 additional AI-screened organizations without investor-level manual audit (not a census)
- [Reproducible discovery source sightings](data/discovery_sightings.csv): 25 sourced sightings, including 5 deliberate name/alias duplicates
- [Discovery batch report](reports/DISCOVERY_BATCH_20261009.md) and [candidate intake script](src/investorverify/discover.py): source-driven expansion and deduplication; **not** automated proof of direct investing
- [Claim-level evidence](data/evidence.csv): 96 claims with URLs, accessed date and verification stage
- [Frozen preliminary AI predictions](data/ai_predictions.csv): 27 total (20 newly AI-screened: 13 include, 2 exclude from **VC-only scope**, 5 review; original 7 predictions unchanged)
- [Independent audit register](data/manual_audit.csv): 8 independently reviewed candidates: six direct VC investors (Credo, Tilia, DEPO, Tensor, Nation1, Purple Ventures) and two non-investors (CVCA, CzechStartups). Nation1 is an audited investor but the original AI prediction stays `review` due to brand ambiguity
- [Screening of 20 new candidates](reports/SCREENING_BATCH_20261009.md), [first seven candidates](reports/INITIAL_SCREENING.md)
- [AI collaboration log](ai-log/): source and code work, actual issues and corrections; uses ChatGPT **not Claude Code**
- [Python data validator](src/investorverify/validate.py), [precision measurement](src/investorverify/quality.py) and [unit tests](tests/test_validate.py)

**Six confirmed investor labels and two excluded organizations are not enough to estimate general accuracy.** The calculator currently returns `preliminary_small_sample` and displays sample size. Our target is about 30 candidates and at least 20 independently audited entries; these are targets, not achievements.

## Setup and checks

Python 3.10+ and pip required. No paid API key is needed to run the current code.

```bash
python -m pip install -e .
python -m investorverify.discover --check
python -m investorverify.validate
python -m unittest discover -s tests -v
python -m investorverify.quality
```

To refresh candidates from curated public-source sightings, run `python -m investorverify.discover --write` and review the Git diff before committing. To collect fresh public HTML headings into an **unverified staging CSV only**, run `python -m investorverify.discover --fetch-czechstartups` (requires internet and the website layout may change). Avoid excessive requests and respect site terms.

A clean run should show structural validation passing, tests passing and quality status `preliminary_small_sample` (8 reviewed candidates: TP=5, TN=2, 1 abstention). GitHub Actions runs the same checks on push. **Passing code tests does not verify real-world investor assertions.**

## Data definitions

- `candidates.csv`: sourced organizations and aliases; a screened row is not automatically a human-verified investor. The 20 new rows are marked `ai_screened_pending_human`.
- `evidence.csv`: each field has its own URL, source type, publication date if known, access date, and verification status.
- `ai_predictions.csv`: screening result, frozen before human review. `review` is intentionally unresolved.
- `manual_audit.csv`: source-based independent human classifications with reviewer, date and time spent.
- `*_historical`: historical association-directory figures. Do not treat as current AUM, available money, fund size or investment ticket.
- `country_focus=CZ`: Czech-connected pilot, not a claim that all legal entities are domiciled in Czechia.

The source status `ai_source_checked_pending_human` explicitly **does not** mean human verification. An inaccessible source or undated report remains a limitation, never a fabricated certainty.

## Method and measurement

1. Discover candidates through public directories and news.
2. Verify existence and investment activity using official sites, named investments and credible secondary sources.
3. Deduplicate and disambiguate managers, funds and rebranded organizations.
4. Save supporting URLs per claim; leave unknown amounts blank.
5. Freeze AI screening decisions; perform independent human review of a defined sample.
6. Calculate confusion-matrix counts TP / FP / FN / TN and precision = TP / (TP + FP), with sample size.
7. Report per-field coverage, accuracy of sampled claims, global data coverage assumptions and scaling costs.

Precision is meaningful only for the **audited candidate sample**, not all investors worldwide. The original Nation1 AI classification was `review` and remains an abstention even though a human verified its 2023 investment. If positive predictions were not independently reviewed, show no number. The test suite uses **synthetic fixture decisions** strictly to verify arithmetic; these are never imported into the research dataset.

## Known limitations and next work

- Audit sample has 8 independently reviewed candidates (6 includes; 2 excludes). Of the 20 newly AI-screened organizations, only Purple Ventures has a completed investor-level human audit; Nation1's original AI prediction stays `review`.
- No empirically supported worldwide investor count or costs yet.
- Some disclosed capital figures are historical; there is not enough public evidence to infer current available capital.
- Nation1 → N1 brand rename was author-confirmed from a 2023 Newstream article, and current partner Jaroslav Trojan and Prague address match the historical profile. N1's self-reported USD 60m managed across two funds (AI and healthcare focus) was verified on its website on 2026-10-09. This figure is neither available capital nor the historical EUR 35m reported by CVCA. Current legal-entity/fund-vehicle continuity remains unverified; original AI decision stays `review`.
- The pilot is not exhaustive and has not measured recall in a global universe.
- Purple Ventures initial €250k–€400k ticket, minority equity strategy and pre-seed/seed stages were author-checked on its official site. The author also confirmed Purple in Delta Green's 2024 investee-side announcement and completed the investor-level `include` audit. The €2.2m is the total three-investor round, not Purple's individual contribution.
- StartupYard FAQ's financing terms have been checked by the project author, but its investor eligibility label is still `review`. Its €45k in-kind note and optional €25k cash must not be confused with €100k follow-on investments controlled by partner DEPO Ventures.
- Next: independently audit the 20 new AI-screened candidates, preserving frozen predictions, then compute quality metrics and global cost model.

## AI use and transparency

Work was completed with OpenAI ChatGPT and public-web research. `ai-log/` documents prompts, actual source-screening choices and model mistakes. This is **not** a genuine Claude Code `/export`; we do not pretend otherwise. The take-home permits similar tooling but the alternate logging format may require employer confirmation.

**Public sources only**. No paywalled datasets, private investor contact databases or personal credentials are committed.

Submission deadline: **2026-10-16**.
