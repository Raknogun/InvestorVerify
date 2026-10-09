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

## Follow-up: Tilia author confirmation

The project author submitted a screenshot of a Delta Green press release dated **2024-05-28**, highlighting the exact phrase:

> Tilia Impact Ventures jako lídr investice

User's actual response: **«да, это есть»**.

This confirms the **investee-side claim** that Tilia led the financing round with Credo Ventures and Purple Ventures. Earlier user-supplied Tilia portfolio screenshot showed **21 companies as of Q4 2025**. The model classified Tilia as `include`; author confirmed this investor-level decision.

Actions: created `czvc005` independent human audit record with author as reviewer; marked only E027 (portfolio count) and E031 (named lead-investor role) `human_verified`; other claims about ticket size, sector and capital remain AI-screened. Duration was not measured and remains blank. EUR 2.2m is the **total financing round**, not Tilia's personal contribution. Two reviewed investors are too few for representative precision.

## DEPO Ventures: directory screening and a concrete data-quality issue

The project author supplied a screenshot of the CVCA member profile and wrote (actual words):

> «Есть портфолио, но без ссылок»

This confirmed the CVCA listing of sector-agnostic VC, historical reported funds under management EUR 5.5m, preferred checks EUR 50k–300k, geographic focus CEE and multiple named portfolio firms. However, this association directory has no direct investee transaction links. The listed Czech portfolio mentions **Tatum twice**, an actual duplicate candidate token in the source list; therefore a raw count of names would be unreliable.

AI located an [issuer-side Tatum Technology LLC press announcement dated 2022-10-12](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html), naming Depo Ventures among the investors in a USD 41.5m *total* funding round. Added E032 with `ai_source_checked_pending_human`. Not claimed as DEPO's personal investment amount. **The project author has not yet independently verified this Tatum release**, so DEPO still has no manual label.

## DEPO human confirmation and newly noticed Tensor Ventures (same date)

The user shared a screenshot from Tatum's published 2022 funding announcement. Visible source passage explicitly names **Depo Ventures** among the investors, and **Tensor Ventures** also appears in the same passage. User asked, verbatim:

> «Я так понимаю это оно?»

The screenshot confirms DEPO as a participating investor in Tatum's **overall USD 41.5 million financing round**. Evolution Equity Partners led the round; individual contributions were not disclosed.

Actions: `czvc002` recorded `include` in author audit; `E032` marked `human_verified` for the specific participating-investor assertion; `E033` added for Tensor Ventures using the same investee press release, pending separate author audit. Original DEPO fund size, ticket range and other claims remain historical/AI-screened. No review duration was reported.

This makes 3 independently confirmed positive classifications in a deliberately selected sample of seven candidates — **not** a representative precision benchmark. We still need independently audited negative classifications and other candidates to measure credible performance.

## Tensor Ventures: screenshot and independent investment support

User opened the [official Tensor Ventures website](https://tensor.ventures/) at its Portfolio tab, shared a screenshot and asked:

> «Я так понимаю это то?»

The visible portfolio detail for **Neuronix AI Labs** said: founded 2020; **TV Invested 2021**; exit acquired by Microchip Technology in 2024. The displayed investment year is an explicit first-party portfolio statement. A previous user-provided screenshot of the [Tatum Technology LLC 2022 funding announcement](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html) independently named Tensor Ventures among investors alongside Depo Ventures.

Human audit result: Tensor classified `include` (`czvc003`), with the two source URLs; minutes not measured. `E033` marked `human_verified` for Tatum investment participation, `E034` added as `human_verified` for the official 2021 Neuronix investment claim. The acquisition/exiting 2024 was visible on the site but **not independently verified** and is not used as required proof. The EUR 41.5m represents the entire Tatum funding round, not Tensor's contribution.

State: four confirmed positives; no manually reviewed negative examples yet. Sample size is too small and selected for confirmed investors, so the resulting 4/4 is **not** representative accuracy.

## CVCA negative control — independently checked by project author

User was asked to locate the text "CVCA represents the interests" on the [CVCA About Us page](https://cvca.cz/en/about-us/) and responded verbatim:

> «Да, в слайдере есть эта надпись»

The author independently confirmed the association's self-description as representing PE and VC funds. Our pilot classifies **organizations making direct VC investments**, not associations representing members. Human label for `czneg001`: **exclude**. This is a classification under project eligibility rules, not absolute proof that CVCA has never made any investment.

Changes: record human-reviewed `exclude` in `manual_audit.csv` with blank duration (not measured); mark CVCA prediction reviewed; update E028 to a narrowly scoped description of the association and mark the confirmed text `human_verified`.

Confusion-matrix state at this point: 4 TP, 0 FP, 0 FN, 1 TN in the **five author-audited records**. The sample is deliberately selected and far below the target of 20 audited records; not suitable to estimate population precision or recall. The separate `CzechStartups` negative control remains unaudited.

## CzechStartups author screenshot: second independently reviewed negative control

User opened [CzechStartups About Us](https://czechstartups.gov.cz/en/about/), submitted a screenshot showing **"CzechStartups is the official website of the Czech startup scene"**, and asked:

> «Я так понимаю это вот?»

The webpage says it gathers information on programmes, investment support providers, investor news, events and start-up resources. This provides evidence of an **information portal**, not evidence that the site directly invests its own capital. Its partner entities (CzechInvest, IBM, Rockaway Capital, etc.) must not be treated as direct investment activity by the portal.

Human decision: `czneg002` = `exclude` under the direct VC investor inclusion rule. Only the observed portal purpose in E029 is marked `human_verified`; we do **not** claim proof the portal has never made investments. Review duration not measured and deliberately omitted.

Current manual decision tally: **6 candidates (4 include, 2 exclude)**, yielding TP=4, TN=2 in this purposively assembled pilot. No false positives/negatives have yet been observed; the sample is too small and selected to justify population accuracy claims. The unresolved candidate Nation1/N1 remains to be audited.

## Nation1 — author screenshot and AI source follow-up

User supplied screenshot of [Nation1 profile in CVCA](https://cvca.cz/en/nation1-2/) with three companies in the Czech portfolio: **VRgineers, Snuggs, Buildiro**. User said, verbatim:

> «3 компании в портфолио nation1»

Other historic CVCA values: reported funds managed EUR 35m, preferred check EUR 50k–1.5m, technology sector, 7 CZ deals. **3 portfolio companies != 7 reported transactions**; do not infer number of companies from number of deals. The page is historical; it cannot prove current 2026 amounts.

AI found an [issuer-side VRgineers announcement dated Nov 28 2023](https://www.prnewswire.com/news-releases/vrgineers-successfully-closes-6-million-usd-series-a-investment-301998176.html) explicitly reporting Nation 1 increased its stake by USD 0.5m in a USD 6m Series A round. Unlike many round-size announcements, **USD 0.5m is attributed to Nation 1 itself**. E036 added as `ai_source_checked_pending_human` while the project author verifies this second source.

[Newstream, Sep 19 2023](https://www.newstream.cz/zpravy-z-firem/nation-1-meni-jmeno-a-chysta-novy-fond-do-vedeni-jmenoval-dva-nove-partnery) states Nation 1 rebranded to N1. [n1.rocks](https://n1.rocks/) lists original partner names and Prague address; current brand/vehicle relationship should be checked further.

### Actual model disambiguation risk caught

An unrelated domain [n1invest.co](https://n1invest.co/) calls itself "N1 Investment Company"; it lists different management (Nykyta Izmaylov and Kyrylo Medvediev), a separate investment strategy and locations. This site **must NOT be used as evidence** for Czech Nation 1 / N1 Ventures. Same short brand does not establish common identity. This is an observed near-name collision, not a hypothetical example.

Author verified only the three portfolio names in CVCA (E035 `human_verified`); no independent `include` / `exclude` reviewer decision was recorded for Nation1 yet, and `data/manual_audit.csv` stays at six audited records. Do not use any of these claims to change the frozen AI `review` prediction retroactively.

## Nation1: independent confirmation of USD 0.5m follow-on investment

User shared a screenshot of VRgineers' own 2023-11-28 press release and wrote:

> «Вот, оно есть»

The screenshot highlights `Nation 1 increasing its share by 0.5 million USD`, so author independently verified the **Nation 1-specific USD 500,000** follow-on investment. The release also states the total Series A round was **USD 6 million**, led by Taiwania Capital; these are separate amounts.

Nation1's human audit label is now `include` for demonstrated **historical direct VC investing**, with no measured reviewer duration. Claim E036 changed to `human_verified`. The original AI prediction `review` is **unchanged** and now shows `human_review_status=reviewed`; the quality calculator counts this as an **abstention/deferred prediction**, not as a true positive. Current legal fund-manager continuity under the N1 brand remains unverified by the author. That is a separate entity-resolution question.

The author should next compare the Sep 2023 Nation 1 → N1 announcement with current N1 official website (n1.rocks). The unrelated site n1invest.co must not be merged into this identity.

## Nation1 → N1 brand rename verified by project author

The user supplied a screenshot of the [Newstream article dated September 19 2023](https://www.newstream.cz/zpravy-z-firem/nation-1-meni-jmeno-a-chysta-novy-fond-do-vedeni-jmenoval-dva-nove-partnery), highlighting the statement that Czech VC fund Nation 1 changed its name to N1, and confirmed:

> «да, есть»

The article also mentions VRgineers and Snuggs, consistent with the earlier historic Nation1 portfolio. Thus E037 was changed to `human_verified` for the **brand rename claim only**. N1's current [official site](https://n1.rocks/) (AI-read, not author-audited yet) lists Jaroslav Trojan, Marek Moravec and the Prague address Národní 135/14, consistent with the old CVCA profile. This is useful entity corroboration, **not proof that the legal fund vehicle stayed the same**.

The original AI prediction `review` is preserved to avoid hindsight changes. No new human investor classification row, precision change or invented audit duration was added. Do not conflate this fund with the unrelated n1invest.co.
