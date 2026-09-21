# Phase 0 — Intake

**Ticker:** RKT
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/RKT/2026-06-05
**Version:** v1
**Generated:** 2026-06-06T16:47:39-04:00

## Summary

Ticker validated (RKT — Rocket Companies, US-listed equity). Output directory
created and empty → v1. UW CLI reachable; latest options and dark-pool dataset
dates both equal the as-of date (2026-06-05), so no staleness offset. Options
activity confirmed. All downstream `uw` commands will carry `--date 2026-06-05`.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets: darkpool, hotchains, oi, options, screener
- Latest available options date: 2026-06-05 (via `sort | last`; arrays are unsorted)
- Latest available darkpool date: 2026-06-05 (via `sort | last`)

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`):
  `RKT 2026-07-10 14.5C` — total_premium $110,720, total_volume 3,460,
  open_interest 3, vol/OI 1,153.3, avg_iv 0.6146
  (jq path: `.results[0]`; source: bot-eod-report-2026-06-05.parquet)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (Stock Screener): 2026-03-13 → 2026-06-05, 40 dates:
  2026-03-13..2026-03-27 (11 contiguous trading days), then **gap**, then
  2026-04-27..2026-06-05 (29 contiguous trading days)
- Gap flagged: **yes** — non-contiguous between 2026-03-27 and 2026-04-27
  (~1 month missing). Phase-5 self-history and phase-0.5 percentiles must not
  assume continuity across that window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: 960.91M · `Shs Outstand`: 978.70M · `Short Float`: 7.48%
  (jq: `.fundamentals."Shs Float" / ."Shs Outstand" / ."Short Float"`)
  — float carried to phase-2/3 for %-of-float normalization; short-float
  seeds phase-7c.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

None in this directory (v1). Context only: a separate prior deep dive exists at
`research/RKT/2026-05-20/` (different as-of date — not a version of this run).

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw historical available-dates --json` | `to_entries` / dataset arrays, `sort \| last` | ok |
| `uw options-flow unusual-volume --symbol RKT --top-n 1 --date 2026-06-05 --json` | `.results[0]` | ok |
| local snapshot probe (`ls "$STOCKS_DIR/Stock Screener/"`) | n/a (shell) | ok |
| `fz doctor` + `fz quote RKT --agent` | `.fundamentals."Shs Float"` etc. | ok |

## Tool errors

None.
