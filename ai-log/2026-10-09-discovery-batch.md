# AI-assisted candidate discovery expansion — 2026-10-09

**Tool:** OpenAI ChatGPT, not Claude Code. **Type:** work summary, not a verbatim exported transcript.

## User's actual request

> «давай»

This followed the explicit plan to enlarge the pilot to 20–30 organizations automatically, then audit a subset.

## Instructions and decisions

- The assistant searched a 2025 publicly available Czech government industrial-transformation report (Figure 17, based on Dealroom) and CzechStartups's public investor directory.
- Selected 20 previously unlisted names, and intentionally included five repeated sightings of already known candidates to verify alias handling.
- **Kept every newly discovered entity at `status=discovered_unreviewed`, `category_proposed=unknown`.** No fictitious investment activity, tickets, AUM, AI decision or human audit row was generated for the new names.
- Implemented repeatable Python name normalization/deduplication and optional live heading scraping into an isolated staging CSV.
- Reworked structural validation so discovery-only candidates may legitimately lack a frozen AI decision while already screened old records still require one.
- Added test cases for alias collisions, duplicate re-import, discovery coverage, structural safety and HTML heading parsing.
- Updated GitHub Actions to run discovery coverage first.

## Data-quality traps intentionally retained for screening

- The 2025 report includes accelerators (StartupYard and Starcube), angel group Garage Angels, corporate VCs and investment groups, rather than only VC funds.
- Presence in a source is a **candidate lead**, not direct investment proof.
- The duplicate N1 source mention must match the approved alias of Czech Nation1; unrelated N1 companies are not silently merged.
- Reported amounts such as total financing rounds, fund size, AUM and available capital are separate concepts.

## Verification and results

After committing, refer to the actual GitHub Actions output for syntax tests and data validation. The intended result is 27 candidate records (7 old + 20 discovered), 25 input sightings, and no new human audit labels. Only actual CI results can establish passing tests.

## Follow-up: 20-candidate AI classification

User's literal continuation prompt:

> «давай»

AI examined primary portfolio and investor terms and CzechStartups/government links, screened all 20 originally unreviewed candidates and froze 13 `include`, 5 `review`, 2 `exclude` decisions, with per-claim source URLs. No new human labels were added.

**Real model risk caught during research:** originally we described StartupYard only as an accelerator that might not invest. Its [FAQ](https://startupyard.com/faq/) explicitly discloses optional cash convertible-note funding and a follow-on investment fund. This falsifies any automatic rule 'accelerator means no equity investing'; decision set to `review` for mixed financing/legal structure.

**Scope risk caught:** Garage Angels really invests the members' own money; its `exclude` is only a statement about the **VC-only pilot category**, not a 'not an investor' claim. A worldwide investor dataset must include its verified individual angels or an appropriately labeled group record if deduplicated. Miton, Rockaway, Pale Fire and former Czech Founders VC require parent/vehicle or current brand resolution, not hallucinated VC-only labels.

**Validation plan:** a new GitHub Actions run must establish schema checks and unit tests on the atomic screening commit. Do not say tests passed until the run is complete. User manual audits are still seven; precision numerator and denominator have not changed.
