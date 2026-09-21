# Phase 0 — Intake

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NBIS/2026-06-05
**Version:** v1
**Generated:** 2026-06-06T19:35:11-0400

## Summary

Ticker validated (NBIS, US-listed equity — Nebius Group). Output directory
created, empty (v1 run). UW CLI reachable; as-of date 2026-06-05 is the latest
available date for both options and darkpool datasets, so the run is fully
as-of-consistent. Options activity confirmed — far from thin: top unusual-volume
contract alone carries $49.3M premium. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets: darkpool, hotchains, oi, options, screener
- Latest available options date: 2026-06-05
- Latest available darkpool date: 2026-06-05
- (per-dataset arrays are unsorted; latest extracted via `sort | last`)

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`):
  `NBIS 2026-06-26 285P` — total_premium $49,340,924, total_volume 7,006,
  open_interest 6, vol/OI 1167.7×, avg_iv 1.113, trade_count 119
  (`jq '.results[0]'` on validated JSON)
- Extreme vol/OI on a fresh put line — carried forward as a flag for phase 1.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (Stock Screener): 2026-03-13 … 2026-06-05, 40 dates.
  - **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27
    (the known gap). 2026-05-22 → 2026-05-26 is the Memorial Day weekend
    (not a gap).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: **201.04M** · Shs Outstanding: 220.41M · Short Float: **22.43%**
  (carried to phase-2/3 for %-of-float normalization; short float is high —
  carried to phase-7c as a positioning-gate input)
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Tool calls

| Command | jq path | Result |
|---|---|---|
| `uw historical available-dates --json` | `.options // [] \| sort \| last`, `.darkpool // [] \| sort \| last` | 2026-06-05 / 2026-06-05 |
| `uw options-flow unusual-volume --symbol NBIS --top-n 1 --date 2026-06-05 --json` | `.results[0]` | 285P 2026-06-26, $49.3M prem, vol/OI 1167.7× |
| local snapshot probe (`ls Stock Screener/`) | n/a (shell) | 40 dates, gap 03-27→04-27 |
| `fz quote NBIS --agent` | `.fundamentals."Shs Float"` etc. | 201.04M / 220.41M / 22.43% |

## Prior versions

(none — v1)

## Tool errors

(none — all green)
