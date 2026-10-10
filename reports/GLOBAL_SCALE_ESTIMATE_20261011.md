# Global public-data coverage and scaling estimate — 11 October 2026

> **Scenario analysis, not a worldwide investor census.** All counts/rates/prices below are assumptions unless an explicit source is cited. The pilot was intentionally chosen rather than sampled randomly. All proposed collection uses public data only and respects source terms.

## 1. Units and source benchmarks

Target a *unique real investing person or organization*, not each fund/vehicle/brand as another manager. Store fund vehicles and linked angel groups as related records without double counting. Evidence of a completed direct investment outranks marketing, advisory services or a startup-directory listing. Distinguish active investor, historical investor and uncertain activity. The full Assignment A includes **VC/CVC, PE/growth, family offices and business angels**, unlike the narrow Czech VC-type pilot.

Independent public benchmarks:

| Observable benchmark | Value and period | Public source | Important limitation |
|---|---|---|---|
| U.S. venture firms | **2,984 firms existing in 2025** | [NVCA 2026 Yearbook, p. 6](https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf) | U.S. VC only; not unique global managers, corporate investors or angel people |
| European PE/VC firms | **3,095 active firms**, 2024 | [Invest Europe, Capital Under Management & Dry Powder 2024](https://www.investeurope.eu/publications-policy/publications/2025/positioned-for-the-challenge-capital-under-management-dry-powder-2024/) | PE and VC together; can overlap VC categories or international firms |
| Global single-family offices | **8,030 estimated in 2024**, not all investing in external companies | [Deloitte, Defining the Family Office Landscape 2024](https://www.deloitte.com/global/en/services/deloitte-private/research/defining-the-family-office-landscape.html) | Estimated population of family offices; many private and absent from public direct-deal evidence |
| Angel community benchmark | **15,000+ ACA individual members and 250+ groups/platforms** | [Angel Capital Association mission](https://angelcapitalassociation.org/mission-and-leadership/) | Members, not a census of publicly discoverable individuals globally; names often withheld |

The denominators differ. **Never add these four figures into a precise world count.** The following category estimates are deliberate, transparent planning assumptions, broadly informed by their scale.

## 2. Publicly discoverable *candidate* scenarios

Estimated possible **public profiles with at least some investment signal** (not necessarily complete records or currently active investors):

| Category | Low | Base | High |
|---|---:|---:|---:|
| VC & corporate VC organizations | 4,000 | 6,500 | 10,500 |
| Private equity & growth investors | 3,000 | 5,000 | 8,500 |
| Family offices *with some public investing signal* | 500 | 1,500 | 3,000 |
| Publicly evidenced individual angels / angel organizations | 3,000 | 9,000 | 20,000 |
| Gross, before cross-category duplicates | 10,500 | 22,000 | 42,000 |
| Assumed name / vehicle / cross-category duplicates | 5% | 10% | 17% |
| **Approximate unique candidates** | **9,975 (~10k)** | **19,800 (~20k)** | **34,860 (~35k)** |
| Assumed proportion ultimately accepted on direct-investor evidence | 55% | 65% | 75% |
| **Potential eligible investor records** | **5,486** | **12,870** | **26,145** |

Source anchors support the *order of magnitude*, not these invented rates. Candidate counts are not observed search yields. The eligibility fractions are illustrative, **not inferred from the selectively reviewed Czech sample**. Before deployment, measure actual capture and duplicates country-by-country for a random, stratified pilot (including source-poor geographies).

A true count of *all* global individual angels or family offices is neither publicly observable nor recoverable with good confidence. An estimated **10k–35k publicly discoverable candidates** is therefore a **project capacity-planning range only**, not a claim that the world contains this many or no more investors. For strictly source-complete fields, the usable count is much lower and currently not estimable with confidence.

## 3. Measured evidence completeness in the Czech pilot

**Actual current pilot:** 27 sourced candidate entities, 20 author-reviewed VC-scope classifications: 16 included direct venture investors; four excluded *from this scope* (two non-investors, one real angel group, one accelerator). Original AI predictions were frozen. Of 17 determinate labels, **TP=13, TN=4, FP=0, FN=0**; **three AI abstentions** (`review`) were subsequently checked manually. Positive-class observed precision is 13/13 among determinate predictions but **is not a statistical estimate of world-wide precision**.

Among **16 included investors**, count each field only if present as a **human_verified** claim. The code `python -m investorverify.coverage` computes these measures from the CSVs:

| Investor attribute | Records with human-reviewed public evidence | Sample coverage |
|---|---:|---:|
| Usual sector strategy (do not substitute investee's sector) | 2 / 16 | 12.5% |
| Stated stage preference | 4 / 16 | 25.0% |
| Typical ticket **both bounds** | 4 / 16 | 25.0% |
| Reported AUM / fund or managed capital (any metric; may be dated/self-reported) | 2 / 16 | 12.5% |
| **Free capital available to invest right now** | 0 proven | Not established |

These figures mainly reflect *how far we researched every field*, not necessarily the maximum available information. They **cannot be applied to the global population**. Even a sourced total AUM is not independently audited, identical to dry powder or interchangeable with fund size. A fund's round participation does not make the round total its own ticket. No values were imputed as zero when missing.

**Completeness limitation in employer requirement:** public sources frequently omit individual/family-office capital or investment size. If *every row must have a numeric total investable capital*, the fully compliant database will necessarily be a **smaller, biased subset**. Report `not_publicly_disclosed` or `not_verified` and field-level coverage rather than inventing amounts. A fund capital number should always be tagged as (fund size vs aggregate AUM vs commitments vs liquid unallocated capital) and have a date.

## 4. Estimated cost for first full worldwide acquisition + first-year upkeep

The planned method has one human review for **every unique candidate**, not only AI-selected likely positives. The observed Czech audit **did not record minutes**, so review times and hourly costs below are scenarios, *not measurements*.

| Parameter | Low | Base | High |
|---|---:|---:|---:|
| Unique candidates reviewed | 9,975 | 19,800 | 34,860 |
| Human minutes / candidate (assumed) | 8 | 10 | 15 |
| Fully loaded human review hourly USD (assumed) | $20 | $30 | $40 |
| Review hours | 1,330 | 3,300 | 8,715 |
| **Manual reviews** | **$26,600** | **$99,000** | **$348,600** |
| Automated research / crawl / AI verification per candidate | $0.15 | $0.30 | $0.60 |
| **Automated research cost** | $1,496 | $5,940 | $20,916 |
| Initial engineering / setup | $3,000 | $10,000 | $25,000 |
| First-year recheck / hosting / operations allowance | $2,000 | $8,000 | $20,000 |
| **Approx. first-year total** | **$33,096** | **$122,940** | **$414,516** |

Formula: `candidate_count = round(sum(category_profiles) × (1 - duplicate_rate))`; `manual_usd = count × assumed_minutes/60 × loaded_hourly_rate`; `total = manual + count × automated_cost + engineering + upkeep`. Reproduce with `python -m investorverify.global_estimate`. Currency is USD; no FX conversion applied.

Costs exclude commercially licensed private datasets, legal reviews, multi-reviewer arbitration, paid lead/contact verification, international taxation and unusually inaccessible jurisdictions. More stringent source-completeness (especially family office assets, single angel's deployable capital) may make some desired records **unobtainable from public data at any cost**. Operational review times should be timed in a new randomized 50–100-record trial to calibrate estimates.

## 5. Practical expansion process and evaluation

1. **Discovery** by geography and investor class: publicly accessible regulator lists (where applicable), published venture transactions, national VC associations, official portfolios and investor announcements. Use association directories only to seed candidates, not authenticate them.
2. **Entity resolution** with canonical manager, legal fund vehicle, parent company, old brand, founder/angel person, and source-linked relationships. E.g., do not treat Czech Founders VC / United Founders or an angel group and each member as automatically one entity.
3. **Typed extraction** with source URL, publisher, publication and access dates; record sector, stage, usual **personal check**, separate **round size**, capital metric, currency, fund vintage, status, and evidence freshness. Leave missing as unknown; do not hallucinate.
4. **Two-level verification**: one credible source establishing investing, preferably a deal confirmation from the investee/co-investor/official filing; stronger secondary confirmation for ambiguity or stale websites. Human audit of exclusions and low-confidence/identity collisions.
5. **Honest independent evaluation**: draw random, stratified samples by country and investor type from both accepted **and excluded** candidate groups; preserve original AI decisions, count abstentions, measure per-class precision, recall *within audited pool only*, per-field extraction accuracy and separate completeness ratios, with intervals and sample sizes.
6. **Updates**: periodic source rechecks and verified timestamps, retain historical snapshots, do not mark decade-old transactions as current activity. Respect robots.txt, site terms, rate limits and source copyright; no paywalls or purchased private contact lists.

## Limitations and next measurements

- The Czech selected sample is not a representative survey of Czech investors, nor a source-availability estimate for other continents.
- Angel and family-office identifiability, sector/ticket disclosure and current capital are highly uneven by geography, type and privacy.
- A public **claim** that an investment manager holds assets is not an independently verified balance sheet.
- Next: measure actual pages/person-hours per investor, crawl success rate, public-source completeness by category, and adjudicated ground-truth scores in at least one additional random geography/type sample.
