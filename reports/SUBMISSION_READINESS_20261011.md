# Submission readiness review — Assignment A (2026-10-11)

## Executive check

Status: **research pilot completed; final submission preparation in progress**. Deadline from Clientelo assignment: **16 October 2026**. The public GitHub repository is [Raknogun/InvestorVerify](https://github.com/Raknogun/InvestorVerify).

| Required deliverable | Status | Grounded location / remaining condition |
|---|---|---|
| Publicly sourced inclusion/exclusion rules | Done | [docs/PLAN.md](../docs/PLAN.md) — narrow VC/CVC pilot versus worldwide PE, angels and family offices |
| Discovery plan with realistic public-data reach | Done as **explicit scenario assumptions**, not a global census | [worldwide report](GLOBAL_SCALE_ESTIMATE_20261011.md) |
| Pilot investors and field-specific source URLs and dates | Done for available claims, often incomplete financial fields | [candidates](../data/candidates.csv), [evidence](../data/evidence.csv) |
| Human audit with AI predictions frozen | 20 / 27 candidates reviewed | [audit](../data/manual_audit.csv), [predictions](../data/ai_predictions.csv) |
| Precision of selected reviewed sample | Measured **13 TP, 4 TN, 0 observed FP/FN, 3 abstentions** | [quality code](../src/investorverify/quality.py), nonrandom selection means cannot generalize |
| Attribute-level public-data completeness | Measured on the *research already performed* | [coverage code](../src/investorverify/coverage.py) |
| Worldwide expansion cost | Low/base/high reproducible *hypothetical* budget | [report](GLOBAL_SCALE_ESTIMATE_20261011.md) and [calculator](../src/investorverify/global_estimate.py) |
| Code plus incremental Git commit history | Implemented | Git repository commit log |
| `ai-log` transcript transparency | **Partial format mismatch** | Actual ChatGPT-assisted research notes in `ai-log/`; they are NOT genuine Claude Code `/export` files |
| Submission email | Not yet sent | Prepare a short Slovak note linking repository and honestly describing the AI-tool format |

## What has been independently checked versus only tested in code

- CSV schema validation verifies URLs, fields, types, and cross-file references. It **does not fetch and independently authenticate every claim**.
- The human audit records evidence personally inspected during source review. Other rows explicitly remain `ai_source_checked_pending_human`; do not call them author verified.
- Technical CI passing is a test suite result, **not investor database production accuracy**.
- Included investor types have differing entity structure: self-funded venture builders and corporate VC firms should not be mislabeled as LP-backed standalone VC partnerships.
- `candidates.csv` deliberately keeps the original frozen intake marker for 20 newly screened records. The up-to-date labels are in `ai_predictions.csv` and `manual_audit.csv`.

## Audit findings corrected

1. README's clean-run expectation was stuck at `preliminary_small_sample` although after 20 reviews `quality.py` returns `measured`. Corrected.
2. README said worldwide estimates and costs did not exist. Replaced with an explicit statement that the published report is assumption-driven, not empirical.
3. Clarified that `minutes_spent` was not recorded and therefore **8/10/15 minutes per reviewer is only a scenario**.
4. Clarified the frozen intake marker is not an assertion that all 20 are *currently* awaiting review.

## Remaining limitations and decisions before sending

**High priority:**
- The task explicitly asks for a Claude Code conversation `/export` in `ai-log`, while the work was performed in ChatGPT. Do **not** fabricate Claude exports. Ask Clientelo whether plain-text ChatGPT-assisted research logs are acceptable as the permitted “similar tool,” or include a candid explanation in the submission.
- Capital/AUM/current deployable money is **not publicly disclosed for most sampled investors**. Among 16 included entities, only 2 have manually confirmed *some* published total capital/AUM/fund-size statement; none has independently established free deployable capital. Preserve `unknown` rather than inventing values. Employer should see this as a quantified data limitation.
- Audit sample is deliberately selected, **not random**. 13/13 observed positive-class precision applies only to 13 definite AI-positive audited rows. Three AI abstentions were manually verified and are not false negatives.

**Recommended polish:**
- Add one clear final report section mapping the user-facing take-home assignment to repository artifacts (this file already does this).
- If time permits, check a stratified random sample from *both* originally included and rejected pool; the small Czech pilot cannot estimate general recall.
- Review public source status and the dated/undated distinction in evidence; a 2019 investment establishes historical authenticity, not 2026 active investment.
- Use the last days before 16 October for README clarity, checking that CI is green, and drafting the actual submission email.

## Evidence-backed source benchmark sanity checks

- [NVCA 2026 Yearbook](https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf) reports 2,984 venture firms in existence in 2025 in the U.S., defined from recent fundraising history; this is **not every possible investor**.
- [Invest Europe 2024 capital under management report](https://www.investeurope.eu/publications-policy/publications/2025/positioned-for-the-challenge-capital-under-management-dry-powder-2024/) gives 3,095 European PE/VC firms active in 2024; not a worldwide unique population.
- [Deloitte 2024 family-office research](https://www.deloitte.com/global/en/services/deloitte-private/research/defining-the-family-office-landscape.html) estimates 8,030 single-family offices; many do not disclose their individual external investments.
- [Angel Capital Association](https://angelcapitalassociation.org/mission-and-leadership/) says its membership includes 15,000+ angels affiliated through 250+ groups/platforms; not an exhaustive worldwide list.

These benchmarks are individually compatible with their original source wording, but the low/base/high worldwide candidate volumes and costs remain **researcher assumptions**, with no statistical worldwide accuracy guarantee.
