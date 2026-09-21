# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc — NYSE)
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-07-17
**Version:** v1
**Generated:** 2026-07-18T00:00:00Z

## Summary

Ticker validated (PATH = UiPath Inc, US-listed equity, options-active). Output
directory created and empty → v1. UW CLI reachable; latest options + darkpool
snapshot both land on the as-of date 2026-07-17, so this run is fully
reproducible with `--date 2026-07-17` (or trailing anchors that land on the
latest date). Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-07-17**
- Latest available darkpool date: **2026-07-17**

## Ticker sanity

- Options activity (unusual_volume top 1): **PATH 2026-07-31 18C** (vol 150,
  OI 1, vol/OI 150, avg_iv ~0.97) — options ARE active; not thin at the tape
  level but strikes are low-priced (sub-$20 underlying) so premium is small.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, then **GAP**, resume
  2026-04-27 → 2026-07-17 (contiguous trading days). **Gap flagged: yes**
  (the known non-contiguous ~1-month hole 2026-03-27 → 2026-04-27). All of
  May/June/July is present, so phase-5 self-history and the DuckDB escape hatch
  are usable for the recent window; long-lookback percentiles that cross the
  gap must note the discontinuity.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (binary + doctor both green)
- `Shs Float`: **n/a this run** — `fz quote PATH` returned a truncated
  fundamentals payload (keys present: Book/sh, Cash/sh, Dividends, Employees,
  Enterprise Value, IPO, Income, Index, Market Cap, Payout, Sales; **no**
  Shs Float / Shs Outstand / Short Float / Price). Recorded n/a and carried
  forward; phase-7c (SI/float gate) and phase-2/3 (%-of-float normalization)
  will retry `fz` and degrade to WebSearch / Finnhub if still absent. Never
  abort per orchestration rule 4.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

<none — v1>

## Tool errors

<none — all probes green; fz float truncation handled as graceful n/a, not an error>
