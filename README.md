# InvestorVerify — Evidence-first investor database

A small, reproducible Python research pilot for **Assignment A: Reliable Investor Database**.

**Pilot:** venture capital organizations with a Czech market or office connection (not necessarily Czech legal domicile). **Status:** first AI-assisted web screening, **not yet independently human-audited**.

## Why this project exists

Investor directories frequently mix actual funds with advisers, associations and information portals. An AI-generated list can also confuse fund size, assets under management, typical investment amount and capital raised by investee companies. InvestorVerify keeps every material claim attached to a source, and separates machine predictions from independent human decisions.

## Current deliverables (2026-10-09)

- [Research design and inclusion/exclusion rules](docs/PLAN.md)
- [Candidate registry](data/candidates.csv): 7 candidates, including negative controls (not a market census)
- [Claim-level evidence](data/evidence.csv): 29 claims with URLs, accessed date and verification stage
- [Frozen preliminary AI predictions](data/ai_predictions.csv): 4 include, 2 exclude, 1 review
- [Independent audit register](data/manual_audit.csv): **empty** until a human checks the sources
- [Initial screening report](reports/INITIAL_SCREENING.md)
- [AI collaboration log](ai-log/): source and code work, actual issues and corrections; uses ChatGPT **not Claude Code**
- [Python data validator](src/investorverify/validate.py), [precision measurement](src/investorverify/quality.py) and [unit tests](tests/test_validate.py)

**No accuracy percentage is claimed yet.** The current `status=not_measured` is deliberate. Our target is about 30 candidates and at least 20 independently audited entries; these are targets, not achievements.

## Setup and checks

Python 3.10+ and pip required. No paid API key is needed to run the current code.

```bash
python -m pip install -e .
python -m investorverify.validate
python -m unittest discover -s tests -v
python -m investorverify.quality
```

A clean initial run should show structural validation passing, tests passing and quality status `not_measured`. GitHub Actions runs the same checks on push. **Passing code tests does not verify real-world investor assertions.**

## Data definitions

- `candidates.csv`: discovered organizations and aliases, not final verified investors.
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

Precision is meaningful only for the **audited candidate sample**, not all investors worldwide. If positive predictions were not independently reviewed, show no number. The test suite uses **synthetic fixture decisions** strictly to verify arithmetic; these are never imported into the research dataset.

## Known limitations and next work

- Audit sample currently has zero independently reviewed records.
- No empirically supported worldwide investor count or costs yet.
- Some disclosed capital figures are historical; there is not enough public evidence to infer current available capital.
- Nation1/N1 naming and fund-manager continuity require identity checking.
- The pilot is not exhaustive and has not measured recall in a global universe.
- Next: manual review, scale sample, compute real metrics and global cost model.

## AI use and transparency

Work was completed with OpenAI ChatGPT and public-web research. `ai-log/` documents prompts, actual source-screening choices and model mistakes. This is **not** a genuine Claude Code `/export`; we do not pretend otherwise. The take-home permits similar tooling but the alternate logging format may require employer confirmation.

**Public sources only**. No paywalled datasets, private investor contact databases or personal credentials are committed.

Submission deadline: **2026-10-16**.
