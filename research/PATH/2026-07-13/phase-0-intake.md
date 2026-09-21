# Phase 0 — Intake

**Ticker:** PATH
**As-of date:** 2026-07-13
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-07-13
**Version:** v1
**Generated:** 2026-07-13T20:12:59-04:00

## Summary

Ticker PATH (UiPath Inc., NYSE) validated — 1–5 alphanumeric US-listed equity.
Output directory created (empty → v1). UW CLI reachable; as-of date 2026-07-13
is the latest available local date for both options and darkpool datasets, so
the run is fully reproducible as-of. Options activity confirmed. `fz` healthy
but carries no float/short-interest fields for PATH (null → WebSearch fallback
in phases 7c/2/3). **Operator note carried forward:** a darkpool print on
2026-07-09 afterhours is flagged as the #4-largest-ever for PATH — phase 2 must
locate and characterize it explicitly. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date (hotchains): **2026-07-13**
- Latest available darkpool date: **2026-07-13**
- As-of 2026-07-13 == latest local date → no as-of staleness; all downstream
  UW reads pass `--date 2026-07-13` where the flag exists.

## Ticker sanity

- Options activity (unusual_volume top 1): **PATH 2026-07-17 C7.5** — total_volume=122,
  vol_oi_ratio=40.67, total_premium=$54,897, avg_iv=2.98. Options tape is thin
  in absolute premium terms (small-cap software name) but active — proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-07-13, contiguous **except one known
  non-contiguous gap 2026-03-27 → 2026-04-27** (~1 month missing). Gap flagged: **yes**.
  Recent window (May–Jul) is dense and complete, so phase-5 historical and
  phase-0.5 self-history are usable on the trailing ~3 months.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **n/a** (fz quote for PATH returns no Float/Short/Outstand fields;
  fundamentals block is a reduced set — Market Cap/Sales/EV only). Phase-2/3
  %-of-float normalization and phase-7c short-interest will use WebSearch fallback.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  missing fields, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

<none — v1>

## Tool errors

<none — all green>
