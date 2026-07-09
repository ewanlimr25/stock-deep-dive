# Phase A1 — Critical-Information Gap Audit (goal #1 / #2)

## Goal

Before writing any direction, decide whether we actually have enough to make a
**good** recommendation. Grade the available evidence against
`rubrics/gap-rubric.md`, and for every gap state its severity and exactly how to
source it. This is a first-class deliverable, not a preamble.

## Inputs

- `phaseA0-intake.md` (what was reused / what's live)
- The reused `decision.json` + phase MDs (if any)
- `rubrics/gap-rubric.md` (the required-input checklist A1–A5, B1–B6, C1–C6)

## Steps

1. **Walk the checklist.** For each item, mark `HAVE` / `PARTIAL` / `MISSING`
   and cite where it came from (a phase MD path, a `chart.json` key, or "not
   available"). Compute `completeness = HAVE_count / total * 100`.

2. **Classify each gap's severity** per the rubric (`critical` / `important` /
   `nice_to_have`) and write a concrete `how_to_source` for each — a specific
   command (`uw …`, `finnhub_enrich.py …`, `fz quote …`, `chart_engine.py …`),
   feed, or "run `/stock-deep-dive <T>`". Never leave `how_to_source` vague.

3. **Decide the verdict** (`SUFFICIENT` / `USABLE_WITH_GAPS` / `INSUFFICIENT`)
   using the rubric's verdict table. The verdict gates Phase A4:
   - `INSUFFICIENT` (a `critical` input missing) → the final plan is
     **watch-only, size 0%**, and its main content is the shortlist of what to
     source first.
   - `USABLE_WITH_GAPS` → plan proceeds with explicit caveats; A3 cuts one step.
   - `SUFFICIENT` → full plan.

4. **Sourcing plan (goal #2).** If anything `critical` or `important` is
   missing, write the exact, ordered commands that would close the gaps, so the
   user (or a follow-up run) can fill them and re-run.

## Write `trade-plans/<SYMBOL>/<DATE>/phaseA1-gap-audit.md`

Include the full checklist table (item · status · source/where), the `missing[]`
list with severity + how_to_source, `completeness`, and the `verdict` with one
sentence of justification. These map 1:1 to the `gap_audit` block in
`trade-plan.json`.

## Verdict for downstream

- `gap_audit` object: `{completeness, have[], missing[], verdict}`
- The size/scope ceiling A4 must respect.
