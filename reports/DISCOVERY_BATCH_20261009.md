# Czech VC-adjacent candidate discovery batch — 2026-10-09

**Stage:** sourcing, **not inclusion**, and **not an AI accuracy result**.

## Sources and reproducibility

1. [RIS3 / Ministry-supported public industrial transformation analysis (2025), p. 27, Figure 17](https://ris3.gov.cz/sites/default/files/2025-08/20280819_Anal%C3%BDza%20vybran%C3%BDch%20t%C3%A9mat%20pr%C5%AFmyslov%C3%A9%20transformace_web_144dpi_75%25_0.pdf). Based on Dealroom 2025, lists **VC funds and investors** funding Czech startups, including accelerators, business angels and funds. This is a *mixed-type discovery list*, not an independently verified VC-only registry.
2. [CzechStartups investor directory](https://czechstartups.gov.cz/en/startup-ecosystem/investors/). Also mixes investor funds, angel groups, investment networks and platforms.

The relevant public organization names and URLs are captured in `data/discovery_sightings.csv`. The 2025 report is licensed CC BY 4.0, and only factual organization names are transcribed here with attribution. Data source years and access dates are kept separately.

### Source intake statistics

| Item | Count |
|---|---:|
| Existing manually audited candidates | 7 |
| New, distinct discovery-only candidates | 20 |
| Source sightings in this batch | 25 |
| Explicit overlapping mentions matched to existing candidates | 5 |
| Total candidate rows now | **27** |
| New AI classifications | **0** |
| New independent manual audit labels | **0** |

This run uses source-derived, curated input names. **The names were selected from the public documents by an AI-assisted researcher; no claim of fully automated internet scraping is made.** Python automates exact-name / approved-alias normalization, stable ID assignment, safe append, reruns without duplicates and coverage checking.

```bash
python -m investorverify.discover --check
python -m investorverify.validate
python -m unittest discover -s tests -v
# Optional: fetch live headings into unverified staging (not added to candidates automatically):
python -m investorverify.discover --fetch-czechstartups
```

`--write` adds only newly seen candidates; it cannot retroactively change frozen AI predictions or manual labels. Source domains and robots/site terms must be respected; live collection is opt-in and limited to a single public page.

## Selection for next independent audit

**Likely VC profiles (still unverified):** Presto Ventures, Purple Ventures, J&T Ventures, Kaya VC, Reflex Capital, Lighthouse Ventures, Czech Founders VC and Miton.

**Deliberate edge cases:** StartupYard and Starcube (accelerators might invest but require evidence); Garage Angels (real own-money angel group, not necessarily a VC *fund*); Y Soft Ventures and INVEN Capital (corporate ventures); Pale Fire Capital and Rockaway (brand/legal structure and type need resolution). Keep them as discovery candidates until classification.

**Preliminary official website checks (AI only, do not count as human audit):**
- [Presto Ventures](https://www.prestoventures.com/): says it backs founders, invests across two funds, and lists portfolio companies. It publishes a *ticket range* (not fund AUM).
- [J&T Ventures](https://www.jtventures.cz/en/home): published a startup portfolio and €300k–3m investment criterion.
- [Purple Ventures](https://www.purple-ventures.com/): says it invests in pre-seed/seed CEE startups, with €250k–400k initial tickets.
- [Garage Angels](https://g-angels.cz/): explicitly describes an informal group of individuals investing their **own money**, likely excluded from this VC-only pilot if classified as a group, while eligible for a later Angel investor collection.

**Do not use source presence or a matching brand name as proof of investing.** Missing capital figures must stay missing until a clearly typed source statement is checked; self-reported figures and undated directories cannot establish current available funds.

## Remaining work

1. Run AI screening on new candidates and freeze `include` / `exclude` / `review` decisions before the next human audit.
2. Audit both positive and negative predictions, including edge cases and at least one non-obvious false positive candidate.
3. Count source-level field accuracy and coverage separately from investor classification.
4. Estimate global reach and cost from actual extraction/review time.

## Subsequent screening update
A separate follow-up step produced [frozen AI screening for the 20 new records](SCREENING_BATCH_20261009.md) and 44 new evidence rows. The original values in this discovery snapshot are historical stage metrics, **not current screening totals**.
