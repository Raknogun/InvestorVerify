# InvestorVerify — Reliable Investor Database

A reproducible, evidence-first pipeline for validating publicly available investor information.

**Status:** pilot scaffold, not a completed accuracy study.

## Scope

The first pilot focuses on Czech-connected venture capital investors. We aim to discover about 30 candidates and manually review at least 20. These are targets, not achieved sample sizes.

## Core principles

- Verify investment activity rather than relying on directory categories.
- Keep source evidence for each factual claim; record URLs and access/publication dates.
- Distinguish fund size, AUM, committed capital and available capital.
- Keep unknown facts null; never invent investment tickets or capital amounts.
- Maintain excluded candidates and review decisions to measure precision.
- Freeze automated predictions before independent manual auditing.

## Roadmap

1. Specify inclusion/exclusion rules and evidence schema.
2. Collect and deduplicate candidate organizations.
3. Extract and classify investor claims with citations.
4. Manually review candidates and audit non-null fields.
5. Measure TP/FP/FN/TN, precision and evidence field accuracy.
6. Estimate global coverage and scaling costs from measured pilot effort.

## AI usage

The project uses ChatGPT as an AI development assistant. We will document prompts, output review, corrections and observed failures in `ai-log/`. **This is not Claude Code** and no Claude Code `/export` session will be fabricated.

## Limitations

No investor record has yet been confirmed by manual audit; no accuracy measurements are claimed. Only publicly available information will be used.

## Current phase

Initial project setup — 2026-10-09. Further project files and tests will be committed incrementally.
