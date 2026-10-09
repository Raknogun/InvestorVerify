# AI screening of 20 Czech-connected VC candidates — 2026-10-09

**Status: frozen provisional AI predictions; no independent investor-level inclusion/exclusion audit of the 20 yet.** The project author has checked individual StartupYard FAQ statements and the Purple Ventures investment-strategy screenshot, but this is a field-level source check only, **not** a completed organization-classification audit.

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
- **Starcube:** historical JIC program profile reports financing obtained by **participating startups from external private investors**, not conclusive proof that Starcube runs its own VC fund. `exclude` within this VC-only pilot, explicitly contestable on human audit.
- **Garage Angels:** [they invest their own money](https://g-angels.cz/), so **they are genuine angel investors**. `exclude` only means not a pooled VC/CVC organization in this first sample. This case must be eligible for global angel coverage.
- **Rockaway**, **Miton**, **Pale Fire Capital:** documented investors, but mixed parent/group, venture builder or growth/private-equity-oriented operations. `review` avoids double-counting with dedicated VC arms or overclaiming strict VC status.
- **Czech Founders VC:** the [old site](https://czechfounders.vc/) explicitly announces United Founders; verify exact legal successor/current investing vehicle before merging brands or counting two investors.
- **Heartcore Capital:** Copenhagen-based investor with European VC track record; a [2026 CzechStartups interview](https://czechstartups.gov.cz/en/novinky/interview-heartcore-capital-is-heading-to-czechia-and-looking-for-startups-that-will-change-the-world/) supports Czech market presence. Czech market connection does **not** mean Czech domicile.
- **Amounts:** AUM, fund targets, a funding round, fund size and ticket ranges have separate `field` keys; unknown totals stay unknown.

## Limits of the source checking

The model consulted public investor sites, a government-backed directory, and a small number of independently reported investment announcements. These are **screening-stage source observations**, not manually verified facts. Every new evidence row uses `ai_source_checked_pending_human`; no entity-level judgement has been retrospectively changed after an author's audit.

This deliberately mixed sample and the earlier seven were selected purposively, so even a successful later sample accuracy score **cannot be presented as the worldwide precision**. Report TP/FP/FN/TN with denominators and the number of abstentions; measure per-field accuracy and missingness independently.

## Prioritised manual audit

1. [StartupYard FAQ](https://startupyard.com/faq/): **terms checked by author**; still determine who legally invests the optional €25k and whether StartupYard is eligible as a VC manager. Partner-controlled follow-on financing must not be assigned to StartupYard.
2. [Purple Ventures](https://www.purple-ventures.com/): author confirmed initial €250k–€400k, minority equity and pre-seed/seed via screenshot; independently verify [Delta Green investee funding announcement](https://www.deltagreen.cz/press-releases/cesti-energeticti-inovatori-v-centru-zajmu-delta-green-ziskava-2-2-milionu-eur-od-tilia-impact-ventures-credo-ventures-a-purple-ventures) to complete investor-level classification audit.
3. [Presto Ventures](https://www.prestoventures.com/): direct investment activity, €500k–5m tickets and the *target* of a separate new fund.
4. [JIC Ventures](https://www.jic.cz/cz/o-nas/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do): verify FaceUp transaction and fund manager identity.
5. [Garage Angels](https://g-angels.cz/): distinguish genuine angel group from VC funds.
6. [Starcube](https://www.jic.cz/en/o-nas/pro-media/jic-starcube-with-a-new-manager-and-new-topics-for-this-years-round): check if it itself invested rather than facilitating investment.
7. Review at least 20 records in total, including other straightforward and edge-case predictions.

**Next:** author independently reviews original sources and records decisions and actual review minutes. Report global volume and cost scenarios once review timings are measured.
