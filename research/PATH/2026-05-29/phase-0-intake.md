# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-05-29
**Version:** v1
**Generated:** 2026-05-29

## Summary

Ticker validated (PATH = UiPath Inc., NYSE-listed equity). Output directory
created. UW CLI reachable; latest available date 2026-05-29 == as-of, so this is
a reproducible as-of run (not a live/trailing call). PATH carries options
activity. `fz` available. Proceeding to phase 0.5 (context).

**Headline intake signals (color only, no bias):**
- Price ≈ **$11.72** — low-priced, post-de-rate software name.
- **Short Float ≈ 31.15%** — extremely high; this is a heavily-shorted stock.
  Squeeze/cover dynamics and SI gate (phase 7c) will matter a lot.
- Float ≈ **412.34M** / Shs Outstand ≈ 520.44M.

## UW availability

- `uw historical available-dates`: ok (JSON returned)
- Latest available darkpool date: 2026-05-29
- Latest available hotchains date: 2026-05-29
- As-of 2026-05-29 == latest local date → reproducible as-of run.

## Ticker sanity

- Options activity (unusual_volume top 1): `PATH` Dec-2026 16P, vol 100 / OI 5,
  vol_oi 20, avg_iv ≈ 0.70. Confirms tradable options surface (though premium is
  modest — a small/mid-cap with moderate options depth).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (screener): 2026-03-13 → 2026-03-27, then
  **GAP**, then 2026-04-27 → 2026-05-29 (gap flagged: **yes**, ~1 month
  missing 2026-03-28 → 2026-04-26).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`). Phase-5 historical must treat the gap as a
  hole, not a continuous window.

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **412.34M** (carried to phase-2/3 for %-of-float normalization)
- Shs Outstand: 520.44M · Short Float: 31.15% · Price: $11.72
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

(none — v1)

## Tool errors

(none — all green)
