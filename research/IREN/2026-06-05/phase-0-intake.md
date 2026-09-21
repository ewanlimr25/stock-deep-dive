# Phase 0 — Intake

**Ticker:** IREN
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/IREN/2026-06-05
**Version:** v1
**Generated:** 2026-06-07T00:46:08Z

## Summary

Ticker validated (IREN — IREN Limited, US-listed equity). Output directory
created, empty → v1 run. UW CLI reachable; latest available options AND
darkpool snapshot is exactly the as-of date (2026-06-05), so no
trailing-anchor drift risk. Options activity confirmed (non-thin). Local
parquet + DuckDB available for the escape hatch. `fz` healthy — float
snapshotted; short float 15.71% is elevated and flagged for the phase-7c
positioning gate. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets: darkpool, hotchains, oi, options, screener
- Latest available options date: 2026-06-05 (`.options | sort | last`; 40 dates present)
- Latest available darkpool date: 2026-06-05 (`.darkpool | sort | last`)

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`):
  `IREN 2026-06-12 $20 put` — total_volume 124, OI 1, vol/OI 124.0,
  total_premium $352, trade_count 7, avg_iv 2.78
  (jq: `.results[0]`; source parquet `All Options/bot-eod-report-2026-06-05.parquet`)
- Verdict: options listed and active → proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (40): 2026-03-13 … 2026-03-27, then 2026-04-27 … 2026-06-05
  (contiguous trading days within each block; 2026-05-25 absent = Memorial Day)
- Gap flagged: **yes** — known non-contiguous gap 2026-03-28 → 2026-04-26
  (phase-0.5 self-history and phase-5 must not assume continuity across it)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: **324.15M** · `Shs Outstand`: 340.98M · `Short Float`: **15.71%**
  (jq: `.fundamentals."Shs Float" / ."Shs Outstand" / ."Short Float"`)
- Carried to phase-2/3 for %-of-float normalization; short float 15.71% is
  pre-flagged for the phase-7c squeeze/positioning gate.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Tool calls

| Command | jq path | Result |
|---|---|---|
| `uw historical available-dates --json` | `.options/.darkpool \| sort \| last` | 2026-06-05 / 2026-06-05 |
| `uw options-flow unusual-volume --symbol IREN --top-n 1 --date 2026-06-05 --json` | `.results[0]` | $20P 06/12, vol 124, vol/OI 124 |
| local snapshot probe (`ls Stock Screener/`) | n/a (shell) | 40 dates, gap 03-28→04-26 |
| `fz quote IREN --agent` | `.fundamentals."Shs Float"` etc. | 324.15M / 340.98M / 15.71% |

## Prior versions

(empty — v1)

## Tool errors

(none — all green)
