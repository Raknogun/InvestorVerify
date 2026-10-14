# Global public-investor scaling analysis — AI work log (2026-10-11)

## Context and scope

After the project author independently confirmed INVEN Capital's 2019 direct Driivz investment, 20 candidate eligibility labels were available. The user supplied a screenshot and wrote verbatim "вот". The screenshot names INVEN Capital as an investing entity and says the entire USD 12m round was led by Centrica, with Ombu Group involved. Model deliberately preserved the difference between the total round and INVEN's undisclosed individual commitment.

The original take-home Assignment A also requests an estimated worldwide investor population and scaling costs using only public information. The researcher therefore prepared a transparent **hypothetical** scenario model, as opposed to claiming a measured global census.

## Sources researched and interpretation

- [NVCA 2026 Yearbook](https://nvca.org/wp-content/uploads/2026/04/NVCA-2026-Yearbook-4.9.26.pdf): 2,984 US venture firms in existence for 2025; **US VC only**.
- [Invest Europe 2024 assets study](https://www.investeurope.eu/publications-policy/publications/2025/positioned-for-the-challenge-capital-under-management-dry-powder-2024/): 3,095 active PE/VC firms in Europe in 2024; includes both categories, not solely VC.
- [Deloitte Family Office landscape 2024](https://www.deloitte.com/global/en/services/deloitte-private/research/defining-the-family-office-landscape.html): estimated 8,030 single family offices worldwide in 2024, not necessarily public investors in external businesses.
- [Angel Capital Association](https://angelcapitalassociation.org/mission-and-leadership/): association of 15,000+ member accredited angels and 250+ angel organizations; these numbers are not published names of all individual angels worldwide.

Source populations differ, overlap and are not directly additive. All category-specific counts, deduplication rates, public eligibility fractions, human-review times and hourly rates in the model are **explicit researcher assumptions**. The pilot did not record reviewer time, so no such cost is represented as measured. A user who downloads the code can change assumptions and recompute scenario budgets.

## Actual 20-candidate audit and field coverage

The narrow, purposively assembled Czech-connected VC sample has 20 author labels: 16 venture-capital investing organizations and four VC-scope negatives, including a real angel group and an accelerator. Of the 17 definite frozen AI classifications evaluated there were TP=13, TN=4, FP=0, FN=0, with three original AI `review` abstentions. It is **not representative global precision**.

For the **16 included** investors, the code `python -m investorverify.coverage` finds these `human_verified` evidence field counts: sector investment strategy 2; stage preference 4; both bounds of usual personal ticket size 4; any reported AUM/fund/managed capital 2. Sector of an investee is **not** silently classified as fund sector strategy; round total is not converted into a specific investor ticket. Unknown capital is `not_publicly_disclosed`/unverified rather than zero. No current deployable cash was established.

## Outputs

- `reports/GLOBAL_SCALE_ESTIMATE_20261011.md`: sources, global public-candidate scenario size, explicit uncertainty, reproducible budget and review protocol.
- `src/investorverify/global_estimate.py`: three cost/volume scenarios and formulas.
- `src/investorverify/coverage.py`: coverage among human-confirmed VC-scope investors.
- `tests/test_global_estimate.py`: repeatable scenario and coverage assertions.
- Updated README links. This is an **AI-authored retrospective collaboration summary** based on the actual project work, **not** a verbatim ChatGPT export or a fabricated Claude Code `/export` transcript.

## Remaining risks before submitting

Worldwide category counts were not obtained by running a worldwide discovery process; their values are planning assumptions only. Field-availability ratios from Czech research are not estimates of global disclosure. Individual capital for angels and family offices is often not public. Actual manual review time needs fresh measurement on a diverse, randomly sampled follow-on pilot. The task's demand for capital at each investor cannot be guaranteed from exclusively public data, even if organization existence can be reliably verified.
