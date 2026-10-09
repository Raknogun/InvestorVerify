# AI screening of 20 Czech-connected VC candidates — 2026-10-09

**Status: original AI predictions frozen; five completed VC-scope reviews among these 20 (Purple, Presto, JIC Ventures `include`; Garage Angels as an angel group and JIC Starcube as an accelerator `exclude` from VC fund managers only).** The project author also checked individual StartupYard FAQ statements, but the StartupYard organization-level status remains unresolved.

| AI decision | Count |
|---|---:|
| Include — apparent direct VC or corporate VC | 13 |
| Review — genuine uncertainty about type or identity | 5 |
| Exclude — outside the VC-only pilot (not necessarily non-investors) | 2 |
| Total | **20** |

## All provisional decisions and source links

| Name | AI | Preliminary type | Main publicly available basis |
|---|---|---|---|
| StartupYard | **review** | hybrid_accelerator | [Source](https://startupyard.com/faq/) — Company combines accelerator and investments; determine fund/legal owner before VC-only inclusion |
| Reflex Capital | **include** | VC | [Source](https://www.reflexcapital.com/portfolio/) — Official portfolio provides investor-level evidence |
| Lighthouse Ventures | **include** | VC | [Source](https://lhv.vc/about-us/) — Official VC strategy and portfolio |
| Presto Ventures | **include** | VC | [Source](https://www.prestoventures.com/) — Official site lists prior investing and tickets |
| Miton | **review** | venture_builder_investor | [Source](https://www.miton.cz/en/about) — Direct investing real but venture studio/VC fund unit ambiguous |
| J&T Ventures | **include** | VC | [Source](https://www.jtventures.cz/en/portfolio) — Primary portfolio site |
| Rockaway | **review** | mixed_investment_group | [Source](https://www.rockawaycapital.com/en/funds) — Parent group vs VC subfund not one VC record; avoid double counting |
| Kaya VC | **include** | VC | [Source](https://www.kaya.vc/) — Official VC fund site and terms |
| Czech Founders VC | **review** | VC_brand_transition | [Source](https://czechfounders.vc/) — Must reconcile current manager and new brand before duplicate merging |
| Purple Ventures | **include** | VC | [Source](https://www.purple-ventures.com/) — Issuer explicitly states early-stage minority equity stakes |
| Starcube | **exclude** | accelerator_unproven_vc | [Source](https://www.jic.cz/en/o-nas/pro-media/jic-starcube-with-a-new-manager-and-new-topics-for-this-years-round) — No independent proof of Starcube own VC investment vehicle; exclude VC-only sample pending contrary evidence |
| Pale Fire Capital | **review** | private_growth_investment_group | [Source](https://palefirecapital.com/en/) — Confirmed investor, growth and private-equity mix not strict VC fund classification |
| Y Soft Ventures | **include** | corporate_vc | [Source](https://www.ysoft.com/ventures) — Corporate venture investments supported by direct testimonial |
| Garage Angels | **exclude** | angel_group | [Source](https://g-angels.cz/) — Genuine angel investors; exclude VC-fund-only PILOT, not from future global angel population |
| JIC Ventures | **include** | VC | [Source](https://www.jic.cz/cz/o-nas/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do) — JIC official May 2026 transaction news |
| Novira Capital | **include** | VC | [Source](https://www.businessinfo.cz/clanky/milionova-investice-pro-jihomoravsky-startup-ofisly-fond-novira-capital-podporil-aplikaci-pro-chytrou-spravu-kancelari/) — Government business portal republishes JIC investee news |
| Heartcore Capital | **include** | VC | [Source](https://heartcore.capital/about) — CzechStartups interview confirms active representative prospecting in Czechia |
| Tachles VC | **include** | VC | [Source](https://tachlesvc.com/) — Official sector-specific VC site; Prague office by secondary/issuer |
| INVEN Capital | **include** | corporate_vc | [Source](https://www.cez.cz/en/cez-group/cez-group/selected-companies/inven-capital-sicav) — Parent confirms direct minority holdings in startups |
| Springtide Ventures | **include** | corporate_vc | [Source](https://www.springtide.cz/about/) — Primary fund statement, investee portfolio and normal ticket published |

## Important distinctions

- **StartupYard (author-confirmed FAQ):** [official FAQ](https://startupyard.com/faq/) states **€45,000 in-kind** acceleration (not cash) via convertible note, **optional €25,000 cash** (conditional total note €70,000), and a typical **~5% equity** target. The *up to €100,000* follow-on fund is **in partnership with DEPO Ventures, which has full discretion over investments**. Earlier model wording could imply StartupYard controls the whole €100k fund; E065 was corrected to `partner_follow_on_investment_ceiling`. This does not establish the legal investor of the optional €25k cash. The frozen model label stays `review`, and no human classification has been recorded.
- **Starcube (author-checked 2016 programme description):** JIC explicitly attributes nearly USD 5m alumni funding to external private-sector investors. Cohorts were charged 2% equity for participation and received prototyping and service support; this does not establish direct cash investments by a Starcube VC fund. `exclude` under VC manager pilot, not proof that no in-kind investment occurred.
- **Garage Angels (author-confirmed type):** informal group of private angels investing only their own money (official screenshots). Angel-investor activity is claimed, but individual capital totals, named deals and member identities remain unverified. Correct `exclude` for VC-fund scope must not become `exclude` from the broader investor database.
- **Rockaway**, **Miton**, **Pale Fire Capital:** documented investors, but mixed parent/group, venture builder or growth/private-equity-oriented operations. `review` avoids double-counting with dedicated VC arms or overclaiming strict VC status.
- **Czech Founders VC:** the [old site](https://czechfounders.vc/) explicitly announces United Founders; verify exact legal successor/current investing vehicle before merging brands or counting two investors.
- **Heartcore Capital:** Copenhagen-based investor with European VC track record; a [2026 CzechStartups interview](https://czechstartups.gov.cz/en/novinky/interview-heartcore-capital-is-heading-to-czechia-and-looking-for-startups-that-will-change-the-world/) supports Czech market presence. Czech market connection does **not** mean Czech domicile.
- **Amounts:** AUM, fund targets, a funding round, fund size and ticket ranges have separate `field` keys; unknown totals stay unknown.

## Limits of the source checking

The model consulted public investor sites, a government-backed directory, and a small number of independently reported investment announcements. These are **screening-stage source observations**, not manually verified facts. Most newly sourced claims remain `ai_source_checked_pending_human`; fields checked by the author are marked `human_verified`, and the Purple Ventures investor-level label is now recorded separately. Original AI predictions have not been retrospectively changed.

This deliberately mixed sample and the earlier seven were selected purposively, so even a successful later sample accuracy score **cannot be presented as the worldwide precision**. Report TP/FP/FN/TN with denominators and the number of abstentions; measure per-field accuracy and missingness independently.

## Prioritised manual audit

1. [StartupYard FAQ](https://startupyard.com/faq/): **terms checked by author**; still determine who legally invests the optional €25k and whether StartupYard is eligible as a VC manager. Partner-controlled follow-on financing must not be assigned to StartupYard.
2. [Purple Ventures](https://www.purple-ventures.com/): **investor-level audit completed (include)**. Author independently checked initial €250k–€400k, minority equity and pre-seed/seed on primary website and verified its participation in [Delta Green's 2024 announcement](https://www.deltagreen.cz/press-releases/cesti-energeticti-inovatori-v-centru-zajmu-delta-green-ziskava-2-2-milionu-eur-od-tilia-impact-ventures-credo-ventures-a-purple-ventures). The round total (€2.2m) is not Purple's individual investment.
3. [Presto Ventures](https://www.prestoventures.com/): **investor-level audit completed (include)**. Author confirmed seed–Series A strategy, €500k–5m own tickets versus €800k–8m target rounds, security/defense/dual-use, and a [Silicon Canals article from 22 January 2024](https://siliconcanals.com/outkept-secures-500k/) naming Presto and BAN Flanders in OutKept's €500k total seed round. The article quotes Eduard Kucera, partner at Presto. This is independent press evidence, not an issuer statement by OutKept, and no individual Presto amount was disclosed. Separate vehicle Presto Tech Horizons and a €150m fund **target** must not be mistaken for current AUM.
4. [JIC Ventures](https://www.jic.cz/cz/o-nas/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do): **investor-level audit completed (include)**. Author viewed JIC press release confirming direct participation in FaceUp Series A, led by Fil Rouge Capital, with overall financing **exceeding CZK 110m**. The amount does **not** represent JIC Ventures' own investment and reported fund size requires a separate check.
5. [Garage Angels](https://g-angels.cz/): **review complete for VC eligibility**. Author screenshots confirm a group of angels investing their own money in early-stage companies with no set sector. `exclude` applies only to VC fund-manager scope; a worldwide angel database must retain this lead. No named transaction or individual member verified.
6. [Starcube](https://www.jic.cz/en/o-nas/pro-media/jic-starcube-with-a-new-manager-and-new-topics-for-this-years-round): **human VC-scope review completed (`exclude`)**. Historic 2016 JIC disclosure shows 72 programme participants collectively attracted almost USD 5m **from outside private investors** and the programme required 2% equity from cohort seven. The equity may compensate accelerator benefits rather than a direct cash VC investment; no independent pooled Starcube fund was evidenced. [JIC's 2015 explanation](https://www.jic.cz/en/o-nas/pro-media/join-czech-accelerator-jic-starcube-and-enjoy-up-to-4100-worth-of-benefits) values programme support at up to EUR 4100; AI-found, not checked by author. Distinct from current JIC Ventures manager.
7. Review at least 20 records in total, including other straightforward and edge-case predictions.

**Next:** author independently reviews original sources and records decisions and actual review minutes. Report global volume and cost scenarios once review timings are measured.
