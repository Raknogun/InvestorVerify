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

## Corrections to the AI-generated initial draft

These are actual changes to the earlier repository state, **not invented examples**.

- The initial seed contained `Startupstart.cz` without sufficiently checked identity or a source establishing whether it invests. That row was removed rather than asserted to be an investor or negative control; it was replaced with the clearly identified CzechStartups information portal, sourced to its own About page.
- The initial evidence relied too much on generic discovery-directory URLs, which did not uniquely substantiate each claimed ticket and capital figure. It was replaced with claim-specific source URLs, including direct investor websites and specific CVCA member profiles.
- The earlier dataset used `country=CZ` ambiguously. This was renamed `country_focus=CZ` because Tensor's disclosed fund entities are Luxembourg-based despite a Prague contact presence.
- Legacy CVCA reported fund sizes/checks were not clearly separated from current figures. They are now named `*_historical` and marked as unsuitable for 2026 current-capital inference.
- The original validator only checked simple CSV links and names, not prediction-to-evidence ownership or audit status. Additional checks and tests were added. This remains **structural QA**, not a factual audit.

**Human verification state at end of session:** no human labels or verified accuracy percentage.

## Follow-up: Credo Ventures evidence (same day)

- User supplied a screenshot of Credo's portfolio listing for ElevenLabs and asked how to interpret it; the screenshot itself was **not** published to the repository.
- AI checked the portfolio source and the [ElevenLabs funding announcement](https://elevenlabs.io/blog/elevenlabs-raises-2m-pre-seed-and-announces-ai-speech-platform-promising-to-revolutionize-audio-storytelling), published 2023-01-23. ElevenLabs names Credo as lead investor in a **USD 2 million total** pre-seed round.
- Changed E006 to cite the specific Credo portfolio URL and added E030 for investee-side confirmation of the investment role.
- Important control: the USD 2 million **total round** is not Credo's individual investment amount.
- The user has **not** yet independently confirmed the ElevenLabs article. Therefore E006/E030 remain `ai_source_checked_pending_human` and `manual_audit.csv` stays empty.

## Follow-up: human confirmation from project author

Actual user reply after viewing the ElevenLabs investment announcement:

> «Открой официальную статью ElevenLabs от 23 января 2023 года и найди фразу `led by Credo Ventures`. - да такое есть»

The user had earlier submitted a screenshot of the Credo portfolio page showing ElevenLabs, stage Pre-seed, 2022, current. The user now confirmed the investee-side phrase independently.

**Decision:** `czvc001` marked `include` in `data/manual_audit.csv`, reviewed by `project_author`. Evidence entries E006 and E030 marked `human_verified` for the specific portfolio and lead-investor assertions; other Credo attributes (including fund capital and quoted ticket size) remain AI-screened and not independently audited.

**Missing measurement:** minutes spent on the review were not recorded, so `minutes_spent` is empty. The validator permits an unknown duration rather than making up a number. Any precision calculated from a single audited company is flagged as a very small preliminary sample, not claimed as reliable general accuracy.

## Follow-up: Tilia portfolio screenshot and investee source

User submitted a screenshot of Tilia's "Portfolio Impact" area, with "21 companies in portfolio" and "37m+ EUR unlocked for impact from investors", and explicitly stated: "Не уверен." The screenshot **does not** independently establish a transaction. The latter amount is not fund AUM.

AI found a public [Delta Green company press release dated 2024-05-28](https://www.deltagreen.cz/press-releases/cesti-energeticti-inovatori-v-centru-zajmu-delta-green-ziskava-2-2-milionu-eur-od-tilia-impact-ventures-credo-ventures-a-purple-ventures) naming Tilia as lead among three VC investors in a total EUR 2.2m round. Added claim E031 as `ai_source_checked_pending_human`. No individual contribution was disclosed; no claim of Tilia contributing EUR 2.2m has been made.

**Pending author action:** open the Delta Green article and confirm the relationship independently. The Tilia investor-level human audit remains unentered.
