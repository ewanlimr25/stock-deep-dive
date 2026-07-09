# Phase A0 — Intake & Reuse Detection

## Goal

Validate the ticker, set up the output directory, and **find and load any
existing stock-deep-dive research to reuse** (goal: "utilize already analyzed
stock results if present"). Also load the reasoning ledger so prior lessons feed
this plan.

## Steps

1. **Parse inputs.** Uppercase the ticker (1–6 chars, `^[A-Z][A-Z0-9.]{0,5}$`).
   Resolve the as-of date (default = today, US/Eastern). All look-backs are
   look-ahead safe (`<= as_of`).

2. **Create the output dir** (immutable, never overwrite):
   ```bash
   mkdir -p trade-plans/<SYMBOL>/<YYYY-MM-DD>/
   ```
   If `trade-plan.md` already exists for this `<SYMBOL>/<DATE>`, append `-v2`
   (then `-v3`, …) and reference the prior version — same rule as the deep dive.

3. **Detect the most recent reusable deep dive.** List dated runs and pick the
   newest `<= as_of` that has a `decision.json`:
   ```bash
   ls -d research/<SYMBOL>/*/ 2>/dev/null | sort
   ls research/<SYMBOL>/<latest>/decision.json 2>/dev/null
   ```
   - If found: record the path and its **age in sessions/days** vs as_of. Read
     its `decision.json` (bias, conviction, sizing, gates, levels, thesis,
     citations) and skim the phase MDs it points to (`phase-1`…`phase-8b`). This
     is your flow/positioning/structure/macro/fundamentals substrate — do NOT
     re-pull what it already has.
   - **Staleness:** if the newest run is **> 10 trading days** old, flag it.
     Phase A3 cuts conviction one bin for stale flow; A1 lists "refresh flow" as
     an `important` gap.
   - If **no deep dive exists** (or all are stale and the user wants fresh): you
     have two options — (a) recommend the user run `/stock-deep-dive <SYMBOL>`
     first and proceed with a *chart-led* plan flagged `USABLE_WITH_GAPS`; or
     (b) pull a **compact live flow snapshot** yourself with a few `uw` calls
     (`uw insights deep-dive --symbol <T> --json`, `uw options-structure gex`,
     `uw options-flow sweeps`, `uw dark-pool largest`). Record `flow_source` =
     `deep_dive` | `live_uw` | `none`.

4. **Load the reasoning ledger** (the learning loop, goal #6):
   ```bash
   cat trade-plans/_eval/reasoning-ledger.md 2>/dev/null
   ```
   Note any lessons tagged for this ticker, sector, setup type, or pattern.
   Lessons marked `ACTIVE` are applied in A3/A4 and listed in
   `sources.ledger_lessons_applied`.

5. **Probe the chart source** (smoke test, don't analyze yet):
   ```bash
   python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker <SYMBOL> --date <as_of> | head -c 400
   ```
   Confirm `available: true` and note `source` (yfinance | screener_parquet).
   If `available: false`, B1 is a **critical** gap (A1 will mark INSUFFICIENT
   unless flow alone supports a non-chart plan).

## Write `trade-plans/<SYMBOL>/<DATE>/phaseA0-intake.md`

Record: ticker, as_of, version, reused deep-dive path + age (or "none"),
flow_source, chart source, ledger lessons loaded, and any tool errors verbatim.

## Verdict for downstream

- `deep_dive_reused`, `deep_dive_age_days`, `flow_source`, `chart_source`
- `ledger_lessons` (ids + one-liners) to thread into A3/A4
