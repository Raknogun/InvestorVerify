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

## Presto Ventures: completed independent investor-level audit

The project author supplied a screenshot from [Silicon Canals' public January 2024 article](https://siliconcanals.com/outkept-secures-500k/) with Presto Ventures highlighted and asked verbatim:

> «это?»

The article states that Belgian cybersecurity startup OutKept received **EUR 500,000 in a Seed funding round led by Presto Ventures and BAN Flanders business angels**. It also prints a comment from **Eduard Kucera, Partner at Presto Ventures**. This constitutes independent media evidence of participation, supplementing the earlier manually reviewed official investment strategy.

**Audit result:** `cznew004` = `include`, reviewer `project_author`, date 2026-10-09, review duration not measured (empty), supporting URLs the official Presto site and Silicon Canals. E102 became `human_verified` for the source's exact assertion. The **EUR 500,000 is the total OutKept financing round**, not a proved personal Presto commitment, and Silicon Canals is secondary rather than OutKept's own primary announcement. Original frozen model decision `include` was left unchanged; only its human-review status was updated.

Now 9 investor candidates have human classification decisions (7 positive, 2 excluded), with 1 AI abstention on Nation1. On the 8 determinate predictions that were audited: TP=6, TN=2, FP=0, FN=0. The observed precision on this purposive small sample is 6/6 (not a representative population estimate). Capital/fund size attributes remain insufficient for an aggregate global estimate.

## JIC Ventures: FaceUp investment author-verified

The user provided a screenshot of JIC's [official 2026 press announcement](https://www.jic.cz/cz/o-nas/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do) showing the headline 'První investice nového fondu JIC Ventures míří do technologického startupu FaceUp' and article stating that JIC Ventures joined FaceUp's Series A capital investment. The user wrote verbatim:

> «вот»

The visible Czech text says the **overall** Series A financing **exceeded CZK 110 million** and was **led by Fil Rouge Capital**, a Croatian fund. This must not be attributed in full to JIC Ventures. The article confirms JIC Ventures supplied capital and knowledge, not merely accelerator mentoring.

Added human classification `cznew015=include` (review date 2026-10-09, duration unknown/blank). Changed E058 to `human_verified`, and added E103 as an exclusive numerical lower bound on the total round and E104 for lead investor Fil Rouge Capital. The pre-existing separately reported CZK 400m JIC Ventures fund figure E079 remains `ai_source_checked_pending_human`: the user's screenshot did **not** independently verify it. The originally frozen AI prediction `include` is unchanged, only status updated to `reviewed`.

Now ten candidates have independent project-author screening labels (8 included, 2 excluded); one of ten was an original AI abstention `review`, so eight? **Precisely nine** determinate model classifications are evaluated (TP=7, TN=2). This is a small purposive sample, not an externally valid worldwide precision estimate. No review duration was fabricated.

## Garage Angels: firsthand screenshots and negative-class scope

User posted two screenshots of the official [Garage Angels website](https://g-angels.cz/) and asked verbatim:

> «это?»

The first identifies an *informal group of individual investors* investing **exclusively their own money**. The second explicitly focuses on early-stage angel financing, with no specified industries.

**Model classification nuance:** this is evidence of legitimate angel-type investment activity as described by the group, not evidence of a pooled VC fund. Its original `exclude` decision remains unchanged as a VC-only exclusion, and `human_review_status` is now `reviewed`. This must NOT be marketed as an AI victory at detecting "fake investors" worldwide: angels are expressly included in the employer's original assignment. No named completed transaction, individual member funding or investable capital was established.

Author's audit: `cznew014=exclude` for **VC pilot only**, dated 2026-10-09; review minutes unrecorded. E057 and E105–E107 checked against user's screenshots. The sample is now 11 reviewed for VC scope (8 included VC funds, 2 excluded non-investor entities, 1 excluded genuine angel group). Original Nation1 `review` prediction remains an abstention: among 10 determinate VC eligibility predictions TP=7 and TN=3, no observed FP or FN. Not representative of the global investor population.

## JIC STARCUBE — author screenshot and historic programme equity check

User supplied a screenshot of the footnotes of JIC's [2016 official accelerator article](https://www.jic.cz/en/o-nas/pro-media/jic-starcube-with-a-new-manager-and-new-topics-for-this-years-round) and asked verbatim:

> «это?»

Author-visible source: since 2010 the accelerator had supported 72 projects which collectively raised **almost USD 5m from private-sector investors**; it provided 3-month workshops and mentoring, service and prototype assistance, some financial reimbursements, and starting from the 7th accelerator cohort required **transfer of a 2% interest** for programme participation.

**Model risk corrected:** the 2% ownership transfer is not to be ignored or described as proof of cash investment. Conversely, the USD 5m figure belongs to alumni funded by **third-party** private investors and is not a Starcube fund AUM or its direct check. Distinguish equity-for-services from a pooled VC-manager with investments.

AI independently opened JIC's older [2 Jun 2015 benefits article](https://www.jic.cz/en/o-nas/pro-media/join-czech-accelerator-jic-starcube-and-enjoy-up-to-4100-worth-of-benefits), which explains assistance packages worth up to EUR 4,100 for the 2% programme share. Model also checked [JIC's current page](https://www.jic.cz/en/needs/looking-for-funding), which identifies JIC Ventures as a **different investment fund**. Those two follow-up sources were not independently checked by the author and are marked `ai_source_checked_pending_human`.

**Audit:** `cznew011` = `exclude` for **VC-only fund-manager eligibility**, not proven incapable of taking equity. One project-author review dated 2026-10-09; minutes not measured and left blank. Original frozen AI `exclude` unchanged; human-review status updated. E054 and E108–E110 author verified; E111 and E112 remain AI-screened.

Now 12 VC-scope reviews (8 included VC funds, 4 excluded: two non-investor portals/association, one angel group, one accelerator). Among 11 determinate frozen AI decisions: TP=7, TN=4, FP=0, FN=0, with one Nation1 abstention. This purposively assembled pilot cannot estimate true general investor authenticity accuracy.

## J&T Ventures author verification of Grid.online financing

User uploaded a screenshot of Forbes Cesko's 2025-02-12 report and wrote: "вот". Source: https://forbes.cz/miliony-na-revoluci-cesky-logisticky-startup-grid-online-ziskal-investici-15-milionu-eur/

The article names Reflex Capital, J&T Ventures and Grid Invest as providers of EUR 1.5m overall funding to Grid.online. EUR 1m is explicitly attributed to Reflex Capital. The remaining EUR 0.5m is not assignable entirely to J&T because Grid Invest also invested and their split is unpublished.

Decision: author verified J&T as include for VC-only pilot, saved as cznew006 in manual_audit.csv. Review duration was not measured. E113-E115 record participation, total round and another investor's known amount, all checked by the author. Original AI prediction include remains frozen. The primary portfolio listings E049 and E086 remain only AI-screened.

Current author audits: 13 candidates: 9 VC includes and 4 VC exclusions. One AI abstention, 12 evaluated determinate decisions: TP=8, TN=4, FP=0, FN=0. Purpose-selected evidence sample cannot establish overall accuracy.

## Kaya VC staged independent source and conflicting ticket disclosures

Before any author source check, AI located Portfolion Capital Partners' 2025-04-23 investment story: https://www.portfolion.com/investment-story/riptides-seed/. Portfolion names Kaya VC as a **co-lead** in Riptides' overall **USD 3.3m** pre-seed financing; this is a report by another participating investor, not a company-issued Riptides press release. Kaya-specific contribution not disclosed. New E119-E120 are therefore `ai_source_checked_pending_human`, not human verified.

AI also detected inconsistent public ticket ranges across Kaya pages: https://www.kaya.vc/ homepage **USD 1-3m**, https://www.kaya.vc/facts descriptive introduction **USD 0.5-2m**, and a later section of that same facts page says **EUR 0.1-3m**. The site does not make clear whether these refer to different products/periods. E121 records the conflict for human review. Existing E071-E072 came from the homepage and remain *claims attributable to that page*, not a conclusive global typical ticket range. USD 500m of total AUM and USD 85m current fund on homepage are distinct metrics.

Original frozen Kaya `include` AI prediction stays unchanged; no manual label or fictitious review minutes added.

## Kaya VC — project author checked official homepage screenshot
User supplied a screenshot of official homepage showing **60+ Companies**, **2011 Founded**, **$500M AUM Total**, **$1–3M Ticket**, **Pre+Seed Round**, **$85M Current Fund** and CEE-founder investment strategy; wrote verbatim "вот". Existing E051 E071 E072 E073 E074 are now human-verified as precise **self-reported site claims**, and E122–E125 record an inclusive company count floor of 60 and basic site metadata.

The observed USD 500m total AUM is **not** the cash still available to invest. USD 85m refers to current fund size rather than that fund's free cash. USD 1m–3m is the homepage ticket claim; other ranges on Kaya Facts remain unresolved and E121 stays model-checked only. The external co-investor report on Riptides E119 and E120 still awaits project-author reading. No human investor-level label or fictional review duration added; frozen model include unchanged.

## Czech Founders VC banner — user-supplied author review
The user supplied screenshot of Czech Founders VC website banner which states **We've launched United Founders!** and wrote verbatim "вот". AI initially flagged ambiguous VC brand transition. We marked E052 human-verified for **launch of related initiative only**, not an established rename or legal identity consolidation. Subsequent AI research found an [official Czech Founders VC public post](https://www.linkedin.com/posts/czech-founders-vc_unitedfounders-czechfoundersvc-slovakfounders-activity-7392529692890906624-L546) saying the existing fund continues operating while United Founders broadens the reach, and [Schalast's 2025 transaction statement](https://www.schalast.com/schalast-advises-czech-founders-vc.php) saying Czech Founders VC led the **EUR 1.1m total** Every Health seed round with other investors. These two sources were **not independently opened by the project author**, hence E127–E129 stay `ai_source_checked_pending_human`. Czech Founders VC's individual investment amount and legal fund structure are unknown. Original model `review` remains frozen and investor-level manual label **not yet recorded**. Review minutes unknown. No artificial performance increase.
