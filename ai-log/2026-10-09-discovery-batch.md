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
