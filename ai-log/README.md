# AI collaboration log (ChatGPT, not Claude Code)

**AI tool used:** OpenAI ChatGPT with connected GitHub tooling and public-web source research. Assignment A explicitly permits **"Claude Code alebo v podobnom nástroji"** (Claude Code or a comparable tool).

**Log format:** dated **AI-authored retrospective summaries of actual ChatGPT-assisted work**, containing **selected verbatim user excerpts** where recorded. The project author independently inspected specific public source pages during the sessions; those checks are described in the notes. These files are **not a full verbatim conversation export**, nor are they Claude Code `/export` transcripts. We do not claim that a coding agent ran unattended or that reconstructed work instructions were original verbatim prompts.

## Index

| File | Purpose |
|---|---|
| [2026-10-09-source-screening.md](2026-10-09-source-screening.md) | Original screening, initial errors and corrections, source verification decisions for core investors |
| [2026-10-09-discovery-batch.md](2026-10-09-discovery-batch.md) | Discovery of 20 additional candidates, source-by-source author checks, classification changes and corrections |
| [2026-10-09-reflex.md](2026-10-09-reflex.md) | Direct investment verification and attribution of individual versus whole-round amounts |
| [2026-10-09-kaya-final-audit.md](2026-10-09-kaya-final-audit.md) | Specific Riptides deal, fund-vs-AUM handling and conflicting ticket claims |
| [2026-10-11-global-scaling.md](2026-10-11-global-scaling.md) | Worldwide public-investor sources and explicitly hypothetical candidate and cost estimates |

## Instructions, verification and corrections — quick evidence map

The following are **retrospective paraphrases of the tasks given to ChatGPT**, **not** a recovered literal prompt sequence. ChatGPT was used conversationally with connected GitHub access; no persistent Claude Code agents were run.

| Task instructions to AI (paraphrased) | How the author controlled the result | Concrete errors/limitations found |
|---|---|---|
| Find Czech-connected VC investors using only public sources. Do **not** classify a directory entry as proof of investing. | Opened fund portfolio websites and investee/co-investor announcements; checked that named funds really financed a company. | The first dataset included a weakly supported entity (`Startupstart.cz`); removed and replaced it with a separately identified information portal, rather than claiming it was an investor. |
| Record the fund's sector, typical check, capital and a claim-specific URL; do not fill unavailable numbers. | Verified screenshots of Kaya's funding terms, Nation1/N1's stated managed capital and other fund disclosures. | AUM, whole financing round, fund size and an investor-specific cheque are **different fields**. E.g., Kaya's co-led $3.3m Riptides round was **not** Kaya's personal check. |
| Treat reorganizations, accelerators and angel groups carefully; retain ambiguous preliminary judgments. | Used the Czech Founders VC–United Founders announcements and the investment in Every Health; checked Garage Angels' self-funded angel investing, and StartupYard's conditional financing terms. | A launch of United Founders does **not** prove a legal name change; `exclude` from this narrow VC-manager pilot does not mean the angel group is fake. |
| Write validators, quality metrics and tests; keep original model predictions separate from the human audit. | Re-ran GitHub Actions, reviewed failures, inspected CSV references and kept `review` cases as abstentions. | Tests initially held outdated expected row counts/review statuses; corrected. Passing Python tests **cannot** certify public claims are economically accurate. |
| Estimate worldwide data coverage and operating costs transparently from published statistics. | Compared published source populations and exposed every scenario input in Python rather than treating a model projection as measured data. | No representative global census or reviewer-time measurements exist; $/record and 10k–35k candidate figures remain assumptions. |

Specific dated checks and source links are in the five logs below. The recorded **user excerpts are genuine snippets**, but the tasks in the table are **paraphrased**, not literal user or agent prompt exports.

## What the AI actually did

- Proposed entity eligibility rules, helped find public sources, created/modified CSV data, Python modules, tests, reports and repository documentation.
- Suggested verification tasks for the project author, who opened sites and independently confirmed specified phrases/deals.
- Detected and helped correct mistakes: unsupported initial entity, duplicates, fund-size versus round-size confusion, different legal entities/brands, stale financial values and incorrect CI expectations.
- Logged source-verification states in `data/evidence.csv`; `human_verified` means the author checked the scoped claim, not that all facts on that page or the investor's financial accounts were verified.

## What the AI did **not** do

- It did **not** run Claude Code or call a production LLM API inside `investorverify`.
- It did **not** independently inspect all 152 facts with a human; many entries remain `ai_source_checked_pending_human`.
- The Python validator confirms structure and relationships, **not** truthfulness or independent source availability.
- The 20 manually classified candidates were not a random sample. Reviewer durations were not measured; the worldwide cost model uses assumptions, not time-tracking results.

## Reproducibility

See GitHub commit history for actual incremental changes; the frozen original predictions remain in `data/ai_predictions.csv`, final reviewer decisions in `data/manual_audit.csv`, and per-claim verification status in `data/evidence.csv`.

For tasks where a complete raw transcript is a mandatory format requirement, this summary-based log is a **format limitation**, not a fabricated substitute claiming literal completeness.
