# Phase 0 — Intake

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/CMPS/2026-06-18
**Version:** v1
**Generated:** 2026-06-20

## Summary

Ticker validated (CMPS — Compass Pathways plc, US-listed equity). Output directory
created fresh (no prior run). UW CLI reachable and serving data through the as-of
date 2026-06-18. CMPS carries live options activity. Local parquet snapshot present,
DuckDB available, `fz` healthy. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: 2026-06-18 (as-of resolvable; not trailing)
- Latest available darkpool date: 2026-06-18
- Latest available oi date: 2026-06-18
- Latest available screener date: 2026-06-18

## Ticker sanity

- Options activity (unusual_volume top 1): CMPS 2028-01-21 P10 — total_volume=2011,
  open_interest=144, total_premium=$706,934, vol_oi_ratio=13.97. Confirmed live,
  not thin. (Note: top single unusual-volume line is a far-dated Jan-2028 P10 with
  vol/OI ~14× — flagged for phase 1/3 follow-up.)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (Stock Screener): 2026-03-13 … 2026-06-18.
  **Known non-contiguous gap flagged: 2026-03-27 → 2026-04-27** (≈1 month missing).
  Recent run is contiguous trading days 2026-06-08 → 2026-06-18.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 128.74M (Shs Outstand 134.92M; Short Float 5.69%) — carried to
  phase-2/3 for %-of-float normalization and to phase-7c for the SI gate.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

<none — v1>

## Tool errors

<none — all green>
