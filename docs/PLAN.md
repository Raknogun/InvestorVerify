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
