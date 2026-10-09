# InvestorVerify — Evidence-first investor database

A small, reproducible Python research pilot for **Assignment A: Reliable Investor Database**.

**Pilot:** venture capital organizations with a Czech market or office connection (not necessarily Czech legal domicile). **Status:** first AI-assisted web screening, **fifteen candidates audited for VC scope (11 VC investors, 2 non-investors, 1 out-of-scope angel group, 1 accelerator); N1 brand/entity continuity pending**.

## Why this project exists

Investor directories frequently mix actual funds with advisers, associations and information portals. An AI-generated list can also confuse fund size, assets under management, typical investment amount and capital raised by investee companies. InvestorVerify keeps every material claim attached to a source, and separates machine predictions from independent human decisions.

## Current deliverables (2026-10-09)

- [Research design and inclusion/exclusion rules](docs/PLAN.md)
- [Candidate registry](data/candidates.csv): 27 candidates: 15 manually audited for VC scope and 12 AI-screened candidates without classification audit (not a census)
- [Reproducible discovery source sightings](data/discovery_sightings.csv): 25 sourced sightings, including 5 deliberate name/alias duplicates
- [Discovery batch report](reports/DISCOVERY_BATCH_20261009.md) and [candidate intake script](src/investorverify/discover.py): source-driven expansion and deduplication; **not** automated proof of direct investing
- [Claim-level evidence](data/evidence.csv): 126 claims with URLs, accessed date and verification stage
- [Frozen preliminary AI predictions](data/ai_predictions.csv): 27 total (20 newly AI-screened: 13 include, 2 exclude from **VC-only scope**, 5 review; original 7 predictions unchanged)
- [Independent audit register](data/manual_audit.csv): 15 VC-scope reviews: eleven included VC investors (Credo, Tilia, DEPO, Tensor, Nation1, Purple, Presto, JIC Ventures, J&T Ventures, Reflex Capital, Kaya VC), two non-investors (CVCA, CzechStartups), one real angel group (Garage Angels) and one accelerator (JIC STARCUBE) excluded only from the VC-fund-manager pilot. Nation1 original AI decision remains `review`
- [Screening of 20 new candidates](reports/SCREENING_BATCH_20261009.md), [first seven candidates](reports/INITIAL_SCREENING.md)
- [AI collaboration log](ai-log/): source and code work, actual issues and corrections; uses ChatGPT **not Claude Code**
- [Python data validator](src/investorverify/validate.py), [precision measurement](src/investorverify/quality.py) and [unit tests](tests/test_validate.py)

**Eleven VC includes and four VC excludes are too few to estimate production accuracy; Garage Angels is a real angel group, and Starcube is an accelerator with historical equity participation, not established as a pooled VC manager.** The calculator currently returns `preliminary_small_sample` and displays sample size. Our target is about 30 candidates and at least 20 independently audited entries; these are targets, not achievements.

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

A clean run should show structural validation passing, tests passing and quality status `preliminary_small_sample` (15 VC-scope reviews: TP=10, TN=4, 1 abstention). GitHub Actions runs the same checks on push. **Passing code tests does not verify real-world investor assertions.**

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

- Audit sample has 15 VC-scope reviews (11 VC includes; 4 VC excludes: two non-investors, one angel group, one accelerator). Eight of the 20 new records have human reviews. This is not accuracy for all global investor types.
- No empirically supported worldwide investor count or costs yet.
- Some disclosed capital figures are historical; there is not enough public evidence to infer current available capital.
- Nation1 → N1 brand rename was author-confirmed from a 2023 Newstream article, and current partner Jaroslav Trojan and Prague address match the historical profile. N1's self-reported USD 60m managed across two funds (AI and healthcare focus) was verified on its website on 2026-10-09. This figure is neither available capital nor the historical EUR 35m reported by CVCA. Current legal-entity/fund-vehicle continuity remains unverified; original AI decision stays `review`.
- The pilot is not exhaustive and has not measured recall in a global universe.
- J&T Ventures: Forbes Cesko names it among three investors in Grid.online's EUR 1.5m round. EUR 1m was attributed to Reflex Capital; individual J&T check remains undisclosed.
- Starcube's JIC 2016 publication was checked: historical three-month acceleration, alumni raising nearly USD 5m from external private investors and a 2% participation equity interest. No separate pooled VC-manager is established; the JIC Ventures fund is distinct. The 2015 programme benefit and present JIC Ventures identity were AI-sourced but await the author's independent review.
- Garage Angels says its individual members invest personal money in early-stage startups. Human review established an angel-group type outside VC-fund scope. It must remain a lead for the **global angel category**, pending a named transaction or investor-member confirmation; fund capital and tickets are unknown.
- JIC Ventures participation in FaceUp Series A was verified from JIC's official article. Total round **exceeded CZK 110m**, led by Fil Rouge Capital; no JIC-specific check or fund AUM was established. Its previously sourced CZK 400m fund figure awaits a separate author check.
- Presto Ventures strategy was author-checked on its official site: seed–Series A, security/defense/dual-use, €500k–5m own check versus €800k–8m target **total round**. Independent Silicon Canals reporting on its participation in OutKept's €500k seed round was author-confirmed, completing the `include` investor audit. The €500k round is not Presto's individual contribution.
- Purple Ventures initial €250k–€400k ticket, minority equity strategy and pre-seed/seed stages were author-checked on its official site. The author also confirmed Purple in Delta Green's 2024 investee-side announcement and completed the investor-level `include` audit. The €2.2m is the total three-investor round, not Purple's individual contribution.
- StartupYard FAQ's financing terms have been checked by the project author, but its investor eligibility label is still `review`. Its €45k in-kind note and optional €25k cash must not be confused with €100k follow-on investments controlled by partner DEPO Ventures.
- Kaya VC homepage checked by project author: USD 500m self-reported total AUM versus USD 85m current fund size (neither is known available capital); USD 1m–3m homepage tickets; 60+ backed companies; founded 2011; CEE pre-seed and seed focus. Contradictory ticket claims on another official page still require checking. Riptides investment was author-confirmed by co-investor Portfolion; Kaya's investor-level `include` audit is complete.
- Next: independently audit the 20 new AI-screened candidates, preserving frozen predictions, then compute quality metrics and global cost model.

## AI use and transparency

Work was completed with OpenAI ChatGPT and public-web research. `ai-log/` documents prompts, actual source-screening choices and model mistakes. This is **not** a genuine Claude Code `/export`; we do not pretend otherwise. The take-home permits similar tooling but the alternate logging format may require employer confirmation.

**Public sources only**. No paywalled datasets, private investor contact databases or personal credentials are committed.

Submission deadline: **2026-10-16**.
