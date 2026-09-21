# Phase 0 — Intake

**Ticker:** MARA
**As-of date:** 2026-06-18
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MARA/2026-06-18
**Version:** v1 (no prior run in this dir)
**Generated:** 2026-06-19

## Summary

Ticker MARA (MARA Holdings — bitcoin miner / treasury) validated. Output directory
created fresh (v1). UW CLI reachable and all datasets (options, darkpool, oi,
hotchains, screener) carry data through the as-of date 2026-06-18, so this is a
clean as-of reproducible run — no trailing-date drift. `fz` healthy; float and a
notably high 26.49% short float snapshotted for the positioning gate. Proceeding to
phase 0.5 (context).

## UW availability

- `uw historical available-dates`: **ok** (valid JSON; top-level keys: darkpool,
  hotchains, oi, options, screener)
- Latest available options date: **2026-06-18** (= as-of ✓)
- Latest available darkpool date: **2026-06-18** (= as-of ✓)
- Latest available oi date: 2026-06-18 · hotchains: 2026-06-18 · screener: 2026-06-18

## Ticker sanity

- Options activity (unusual_volume top 1): **MARA 2026-07-24 P10.5** —
  total_volume 5008, open_interest 32, vol_oi_ratio 156.5, total_premium $110,200,
  avg_iv 0.848 `[← .results[0]]`. Confirms live, liquid options tape (not thin).
- Source parquet: `All Options/bot-eod-report-2026-06-18.parquet`

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates: 2026-03-13 → 2026-03-27, **[gap]**, 2026-04-27 → 2026-06-18
  (contiguous trading days within each block).
  - **Gap flagged: yes** — known non-contiguous gap between 2026-03-27 and
    2026-04-27 (no local screener parquet for that ~1-month window). Phase-5
    self-history percentiles must treat the usable window as the ~36 trading days
    from 2026-04-27 onward (plus the March block), not a continuous 3-month run.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **372.36M** (Shs Outstand 380.87M; ~97.8% of shares are float)
- `Short Float`: **26.49%** (carried to phase-7c positioning gate — high; a crowded
  short is itself a squeeze-risk / two-sided signal worth flagging early)
- Carried to phase-2/3 for % -of-float order-size normalization.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); healthy
  here so phases 7b/7c use it directly rather than the WebSearch/Finnhub fallbacks.

## Prior versions

(none — v1)

## Tool errors

(none — all probes returned valid JSON; `uw --version` is simply not a supported
flag, irrelevant to the run)
