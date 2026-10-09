# Research plan — InvestorVerify (draft 0.1)

## Objective and scope
Build a reproducible, evidence-backed directory of actual investors. Pilot: Czech-connected VC managers, ~30 candidates, manually verify at least 20 where practical. Targets are not measured achievements.

## Eligibility
Unit: investing organization or manager; fund vehicles separately where appropriate, never double count. INCLUDE if it invests directly in external businesses, identity is clear, and investment activity is evidenced by one primary or two independent reliable secondary sources. Classify active, historical, or uncertain separately.

EXCLUDE advisory companies, investor-matching platforms, trade associations, grant-only accelerators, investee startups, directories, duplicate brands, public-equity-only funds, and firms with no credible proof of investing. Retain excluded candidates for evaluation.

Pilot includes VC and corporate VC only. Global expansion adds private equity, family offices and angels with separate criteria.

## Evidence requirements
Record one evidence row per claim: entity, field, value, unit, source URL, source publication date (if known), access date, reviewer, verification status. Prefer primary investor disclosures and regulator filings; use associations and independently reported transactions as supporting evidence. Directories only discover candidates.

Fields: canonical name, aliases, jurisdiction, legal entity, type, status, sectors, stages, investment strategy, usual ticket size with currency, fund capital/AUM/committed capital (metric and as-of date). These amounts are NOT interchangeable. Unpublished figures remain unknown, never zero or guessed.

## Workflow
1. Discover candidates in public Czech directories and disclosed investment deals.
2. Resolve names and duplicate manager/fund entities; retain negative cases.
3. Extract typed claims; AI must return evidence URL or null.
4. Check attribution, publication dates and sources; manually review ambiguity.
5. Freeze predictions before independent manual labels.
6. Publish decision register, audited evidence and measurement.

## Metrics
TP/FP/FN/TN from reviewed candidates; precision = TP/(TP+FP). If there are no predicted positives, return N/A. Recall refers only to reviewed candidate universe, NOT worldwide recall. Separately publish non-null verified field accuracy, per-field coverage and sample sizes. No score can be claimed prior to audit.

## Global scope estimate
Build bottom-up counts from unique eligible Czech directory entries; estimate by geography/investor type with duplicates, inactive rates, and public capital/ticket availability considered. Disclose coverage uncertainty, especially for angels and family offices.

## Scaling cost
Cost = candidate acquisition + pages parsed and tokens + manual review minutes × loaded hourly rate + hosting/maintenance + refresh. Low/base/high scenarios should use measured pilot time and public-data visibility. Respect site terms, rate limits, and personal privacy.

## Limits
The pilot is not a census. Old directory profiles may be stale. AUM and fund size are not cash available. No paywalled or non-public data.

## Pilot screening stage and type handling (2026-10-09 update)

This pilot is **VC/corporate-VC-manager only**, whereas the eventual world dataset must include angels, family offices and PE as separate types. Under a narrow VC pilot, an authentic **angel network** is excluded from this VC sample but is **not a fake investor**. Accelerator programs with direct equity notes and follow-on funds are **review**, not automatic non-investors. Broad investment groups and rebranded managers are reviewed at the proper manager/fund unit to prevent double counting.

The original seven predictions and seven author labels are frozen. Twenty new names have received **provisional AI-only** decisions supported by sources in `data/evidence.csv`: include (13), exclude (2), review (5). No extra human results or precision improvements are claimed. Source publication dates are left empty if undated; access date is not a statement's as-of date.

The methodology uses three buckets: `include` only for apparent direct VC/CVC managers, `exclude` for out-of-scope VC-only entities, `review` for type/identity/activity ambiguity. Manual labels must be decided **after** seeing these saved predictions. For the worldwide estimate, re-evaluate angel and PE exclusions under their proper dataset types.

## Investor type versus investor validity: Garage Angels check

The user reviewed [Garage Angels](https://g-angels.cz/) and confirmed that it describes itself as an informal group of individual investors funding early-stage companies with their **own money** and without a set industry focus. For a **VC/CVC manager-only pilot**, classify `exclude` because the organization is not presented as a pooled VC fund manager. For the **full Assignment A**, business angels must be in scope: keep Garage Angels as an angel-group lead, but verify a specific investment or individual angel before reporting fully validated global investor data.

Important measurement limitation: `quality.py` labels this case a TN only under **VC eligibility**, never under "real investor versus fake". World-scale evaluation needs separate `investor_type`, `is_real_investor` and `vc_pilot_eligible` decisions. The existing pilot confusion matrix cannot establish precision across all investor types.
