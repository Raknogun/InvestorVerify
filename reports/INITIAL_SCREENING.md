# Preliminary Czech VC screening — 2026-10-09

**Mostly AI-screened data.** Seven candidate classifications (Credo, Tilia, DEPO, Tensor, Nation1, CVCA and CzechStartups) are now manually checked by the project author; this is not a representative accuracy sample. The first pilot contains 7 candidates (5 fund candidates and 2 non-investor negative controls), 37 extracted assertions, 7 preliminary AI decisions. Five investor cases and two negative-control cases were independently confirmed; this convenience sample is too small for a credible precision estimate.

## Candidate screening

| Candidate | AI decision | Source rationale | Data caveat |
|---|---|---|---|
| Credo Ventures | Include | [Official website](https://www.credoventures.com/) describes direct VC investing, pre-seed rounds, USD 1–5m initial checks and named investments | Total fund capital not established |
| DEPO Ventures | Include | [Tatum issuer release](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html) names DEPO among investors; [CVCA profile](https://cvca.cz/en/depo-ventures-2/) gives portfolio and historical fund facts; an [April 2026 interview](https://www.e15.cz/clanek/rozhovory/kvalitnich-startupu-je-dost-musite-je-ale-najit-s-novym-fondem-cilime-na-vesmir-rika-sima-z-depo-ventures-1431871) discusses continued investments and a new fund | CVCA investment ranges and funds managed may be stale |
| Tensor Ventures | Include | [Official portfolio](https://tensor.ventures/) shows a 2021 Neuronix AI Labs investment; [Tatum issuer announcement](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html) names Tensor as an investor. Official website also describes Seed/Series A focus and deeptech portfolio | Fund legal entities are in Luxembourg, with Czech contact office; include because scope is Czech-connected, not Czech incorporation |
| Nation1 / N1 (historical brand change author-verified) | AI: Review; Author: Include for historical direct investment | [CVCA historical listing](https://cvca.cz/en/nation1-2/) names VRgineers, Snuggs and Buildiro; [VRgineers 2023 funding release](https://www.prnewswire.com/news-releases/vrgineers-successfully-closes-6-million-usd-series-a-investment-301998176.html) discloses an additional USD 0.5m invested by Nation 1; [2023 rebranding report](https://www.newstream.cz/zpravy-z-firem/nation-1-meni-jmeno-a-chysta-novy-fond-do-vedeni-jmenoval-dva-nove-partnery) says Nation 1 became N1 | Author verified Nation 1 → N1 brand rename in the 2023 Newstream article. Legal-entity and fund-vehicle continuity still needs checking. Do **not** merge with the unrelated [N1 Investment Company](https://n1invest.co/) based solely on a matching shorthand. EUR 35m fund volume and EUR 50k–1.5m checks are undated historical CVCA data |
| Tilia Impact Ventures | Include | [Official website](https://tilia.vc/) identifies direct early-stage impact investment, a 0.3–1.2m EUR initial ticket and portfolio | Older pages have other ticket ranges. EUR 37m unlocked from other investors does **not** equal Tilia fund size |
| CVCA | Exclude (author verified) | [Association's About Us](https://cvca.cz/en/about-us/) states it represents PE and VC fund interests; this describes an industry association, not a confirmed direct-investing entity | Verified negative control under pilot eligibility rules, not absolute proof of no investments |
| CzechStartups | Exclude (author verified) | [About Us](https://czechstartups.gov.cz/en/about/) describes an official information portal for the startup ecosystem, offering information on investors and support programmes, not claiming to invest directly | Verified negative control under the pilot's eligibility rules; not proof of no investments anywhere |

## Policy decisions

- `country_focus=CZ` means a substantial Czech market or office connection; **not legal domicile**.
- Capital categories (fund size, AUM, commitments, available capital and raised capital by portfolio firms) must never be merged.
- Numeric values found in old association directories are labeled `*_historical` and are *not* current capital claims.
- Evidence status `ai_source_checked_pending_human` means content was reviewed through public-web tools but has **not** passed independent human audit.
- An unknown current figure is left blank, not invented; sources might be undated.
- Each claim includes a source URL and access date in `data/evidence.csv`.

## Next manual audit

Continue independently checking additional candidates under `docs/PLAN.md`; capture actual audit minutes where possible. The first review duration was not measured and is deliberately blank. Enter the human labels in `data/manual_audit.csv`. Run `python -m investorverify.quality`; the current status remains `preliminary_small_sample`, not a representative estimate.

## Known weaknesses

The pilot has five independently reviewed investor labels and two manually reviewed negative controls; the AI prediction for Nation1 was an abstention; general investor-level precision cannot be claimed. Candidate discovery is not exhaustive. Some sources provide historical, not current, capital estimates. DEPO's official website was inaccessible to the web reader, so its profile also relies on association and press sources. Nation1 alias linkage is pending.
