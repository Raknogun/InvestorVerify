# AI collaboration log (ChatGPT, not Claude Code)

**AI tool used:** OpenAI ChatGPT with connected GitHub tooling and public-web source research. Assignment A explicitly permits **"Claude Code alebo v podobnom nástroji"** (Claude Code or a comparable tool).

**Log format:** dated **human-written/AI-assisted summaries of actual ChatGPT sessions**, containing selected **verbatim user excerpts** where captured. These documents are **not a full verbatim conversation export**, nor are they Claude Code `/export` transcripts. No Claude Code sessions, commands, or fictional prompts have been represented as real.

## Index

| File | Purpose |
|---|---|
| [2026-10-09-source-screening.md](2026-10-09-source-screening.md) | Original screening, initial errors and corrections, source verification decisions for core investors |
| [2026-10-09-discovery-batch.md](2026-10-09-discovery-batch.md) | Discovery of 20 additional candidates, source-by-source author checks, classification changes and corrections |
| [2026-10-09-reflex.md](2026-10-09-reflex.md) | Direct investment verification and attribution of individual versus whole-round amounts |
| [2026-10-09-kaya-final-audit.md](2026-10-09-kaya-final-audit.md) | Specific Riptides deal, fund-vs-AUM handling and conflicting ticket claims |
| [2026-10-11-global-scaling.md](2026-10-11-global-scaling.md) | Worldwide public-investor sources and explicitly hypothetical candidate and cost estimates |

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
