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

## StartupYard FAQ — author verified actual terms

Project author posted two screenshots of StartupYard's [official FAQ](https://startupyard.com/faq/) and wrote verbatim:

> «Вот это»

The screenshots clearly state:
- EUR 45,000 **in-kind acceleration programme** via convertible note — services, **not cash**.
- Up to EUR 25,000 **optional cash** funding, bringing the conditional combined note to EUR 70,000.
- Programme typically targets approximately **5% equity**, not a guaranteed fixed ownership stake.
- Follow-on investments up to EUR 100,000 are **in partnership with DEPO Ventures, which has full authority to choose eligible teams**.

**Actual model attribution correction:** initial E065 (`follow_on_investment_ceiling`) lacked explicit attribution and could mislead a reader into treating the EUR 100k as StartupYard's own investing power. Replaced the field with `partner_follow_on_investment_ceiling`, added DEPO discretion details, and marked only the directly inspected FAQ assertions `human_verified`. Added separately typed in-kind value, equity target and conditional total note statements. E044 and E064 updated to distinguish in-kind services from cash. Added regression test for this misattribution.

**Unresolved:** who holds/invests the optional EUR 25k note legally, and whether the accelerator counts as a VC manager under the narrow pilot. The model's frozen `review` prediction is left unchanged, and `human_review_status` remains `not_reviewed`. No invented manual audit, review duration, or investor classification result.

## Purple Ventures — author-confirmed investing terms, investor audit pending

The user supplied a screenshot of the Purple Ventures **official investment strategy** and asked verbatim:

> «Это?»

It shows direct **minority equity stakes**, **pre-seed and seed** stages, **EUR 250k–400k initial ticket**, **4–7 years investment horizon**, and co-investing with other VC funds/angels, sometimes leading **up to 50% of rounds**. The last figure is not a 50% equity ownership assertion. The screenshot doesn't state total fund capital.

Updated E053, E077, E078 as `human_verified`; added E092–E095 as author-verified statements with links to the primary site. Independently consulted the [Delta Green 2024 investee announcement](https://www.deltagreen.cz/press-releases/cesti-energeticti-inovatori-v-centru-zajmu-delta-green-ziskava-2-2-milionu-eur-od-tilia-impact-ventures-credo-ventures-a-purple-ventures), which explicitly names Purple Ventures as a member of the **three-investor EUR 2.2m total round**; stored as E096, pending **specific user confirmation** of Purple's participation. None of EUR 2.2m should be attributed to Purple individually.

No human investor-level label has been recorded for Purple, and its frozen AI decision remains `include` but `human_review_status=not_reviewed`. The seven previous independent investor classifications remain unchanged.

## Purple Ventures: completed independent investor classification audit

User independently opened [Delta Green's public announcement of the 2024 financing round](https://www.deltagreen.cz/press-releases/cesti-energeticti-inovatori-v-centru-zajmu-delta-green-ziskava-2-2-milionu-eur-od-tilia-impact-ventures-credo-ventures-a-purple-ventures), uploaded a screenshot highlighting **Purple Ventures** in the article title and lead, and wrote verbatim:

> «есть»

The screenshot states Delta Green received a total EUR 2.2 million from **Tilia Impact Ventures, Credo Ventures and Purple Ventures**; it does not say Purple contributed EUR 2.2m individually. The author earlier checked Purple's own website: pre-seed/seed, minority equity, initial ticket EUR 250k–400k and investment strategy.

**Audit recorded:** `cznew010` = `include`, reviewer `project_author`, access/review date 2026-10-09, duration unknown (left empty, not invented), two source URLs, decision rationale. E096 marked `human_verified`. Frozen model prediction `include` is unchanged; only `human_review_status` switched to `reviewed`.

After this manual check, there are 8 human-audited candidates (6 investors and 2 excluded entities). The original model's Nation1 `review` is still an abstention. Thus, among the 7 binary predictions evaluated: TP=5, TN=2, FP=0, FN=0. Precision on these **selected cases** is 5/(5+0) = 100%, but this does **not** estimate production accuracy or generalizability, and most required per-field capital figures remain unavailable.

## Presto Ventures — strategy screenshot; specific deal pending author check

User submitted screenshot of [official Presto Ventures page](https://www.prestoventures.com/) highlighting the €500k–5M investment ticket and asked verbatim:

> «Это?»

Author-observed strategy: **seed to Series A**, mostly post-revenue startups, **NATO and allied markets / Israel**, security, defense, aerospace and dual-use technologies. Crucially, the site distinguishes ***Presto's own planned €500k–5M investment ticket*** (E068/E069) from ***€800k–8M target total financing rounds*** (new E100/E101). These are different investment metrics and must not be substituted.

Verified screenshot claims are E068, E069, E097–E101, marked `human_verified` for the precise statements present; the current managed-capital/fund-vehicle claim E070 is still AI-screened, not author-audited.

Model researched a [Silicon Canals January 22 2024 funding report](https://siliconcanals.com/outkept-secures-500k/) naming **Presto Ventures** among investors in Belgian startup **OutKept's total €500k seed round**, with BAN Flanders business angels. This is an **independent media source**, *not* investee's own announcement. Individual Presto contribution not known. Staged as E102, `ai_source_checked_pending_human`, pending the author's independent source review. No investor-level manual audit row was added. The model's frozen `include` prediction remains unchanged.
