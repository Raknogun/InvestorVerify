# Source screening session — 2026-10-09

**AI tool:** ChatGPT. **Type:** session summary with short actual prompt excerpts; **not** a Claude Code `/export` or complete verbatim transcript.

## User instruction (actual relevant excerpt)

> «хорошо, давай делать»

This continued the explicit instruction to complete assignment A using ChatGPT and the connected GitHub repository.

## Tasks performed by AI

- Searched publicly available official VC websites, the CVCA industry association, CzechStartups and selected news coverage.
- Updated the seven-candidate register and claim-level evidence.
- Identified outdated fund claims and the Nation1/N1 identity issue.
- Separated AI screening predictions from **human labels** (the audit file is empty).
- Added schema checks, precision calculator and regression tests.

## Specific AI-observed data quality risks

1. **Nation1 identity**: old directory listing uses Nation1, while 2023 reports indicate rebranding; current legal continuity must be audited. The model did not silently merge identically named investors.
2. **Tilia financial field**: EUR 37m sourced from external investors into impact is not automatically a fund's managed capital.
3. **Tensor registration**: manager/fund address is Luxembourg; Czech-related sample must not be mistaken for Czech incorporation.
4. **Stale association records**: fund sizes and ticket ranges for DEPO, Nation1 and Tensor are explicitly historical, not current assertions.
5. **Data validation limitations**: tests verify structure/references and arithmetic; they cannot determine factual truth or link availability.

## Checks and next review

Web source examination performed by AI on 2026-10-09; **no human audit performed**. Genuine reviewer names, times and independent decisions must be entered by the user and never fabricated. The test fixture has synthetic human labels only in test code, not real pilot data.

## Files and commits

Consult GitHub commit history for actual changes; records in `data/ai_predictions.csv` are AI judgments, `data/manual_audit.csv` is reserved for independent reviewer labels.
