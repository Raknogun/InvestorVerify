# Preliminary Czech VC screening — 2026-10-09

**Mostly AI-screened data.** Four investor classifications (Credo, Tilia, DEPO and Tensor) are now manually checked by the project author; this is not a representative accuracy sample. The first pilot contains 7 candidates (5 fund candidates and 2 non-investor negative controls), 34 extracted assertions, 7 preliminary AI decisions. Four positive cases were independently confirmed; 4/4 alone is too small for a credible precision estimate.

## Candidate screening

| Candidate | AI decision | Source rationale | Data caveat |
|---|---|---|---|
| Credo Ventures | Include | [Official website](https://www.credoventures.com/) describes direct VC investing, pre-seed rounds, USD 1–5m initial checks and named investments | Total fund capital not established |
| DEPO Ventures | Include | [Tatum issuer release](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html) names DEPO among investors; [CVCA profile](https://cvca.cz/en/depo-ventures-2/) gives portfolio and historical fund facts; an [April 2026 interview](https://www.e15.cz/clanek/rozhovory/kvalitnich-startupu-je-dost-musite-je-ale-najit-s-novym-fondem-cilime-na-vesmir-rika-sima-z-depo-ventures-1431871) discusses continued investments and a new fund | CVCA investment ranges and funds managed may be stale |
| Tensor Ventures | Include | [Official portfolio](https://tensor.ventures/) shows a 2021 Neuronix AI Labs investment; [Tatum issuer announcement](https://www.prnewswire.com/news-releases/tatum-receives-41-5-million-funding-to-accelerate-growth-of-unique-blockchain-development-platform-speeding-time-to-market-for-digital-finance-and-web-3-0-applications-301646685.html) names Tensor as an investor. Official website also describes Seed/Series A focus and deeptech portfolio | Fund legal entities are in Luxembourg, with Czech contact office; include because scope is Czech-connected, not Czech incorporation |
| Nation1 | Needs review | [Old CVCA profile](https://cvca.cz/en/nation1-2/) confirms historical investment activity; [2023 report](https://zpravy.kurzy.cz/743732-fond-nation-1-meni-jmeno-do-cela-jmenoval-dva-nove-partnery--ondreje-homolu-a-klaru-kocarovou/) discusses rebrand to N1 | Do NOT conflate Nation1 / N1 Ventures with any similarly named firm without identity proof; current manager/fund relationship unresolved |
| Tilia Impact Ventures | Include | [Official website](https://tilia.vc/) identifies direct early-stage impact investment, a 0.3–1.2m EUR initial ticket and portfolio | Older pages have other ticket ranges. EUR 37m unlocked from other investors does **not** equal Tilia fund size |
| CVCA | Exclude | [Association description](https://cvca.cz/en/about-us/) identifies it as an industry association rather than direct VC investor | Useful negative control |
| CzechStartups | Exclude | [Portal description](https://czechstartups.gov.cz/en/about/) identifies it as an information website rather than investor | Useful negative control |

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

The pilot has only four independently reviewed positive labels; general investor-level precision cannot be claimed. Candidate discovery is not exhaustive. Some sources provide historical, not current, capital estimates. DEPO's official website was inaccessible to the web reader, so its profile also relies on association and press sources. Nation1 alias linkage is pending.
