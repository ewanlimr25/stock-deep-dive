# Phase 0 — Intake

**Ticker:** BABA
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BABA/2026-05-27
**Version:** v1 (no prior runs in this dir)
**Generated:** 2026-05-28T02:50:53Z

## Summary

Ticker BABA (Alibaba Group Holding Ltd, US-listed ADR) validated. Output directory
created fresh (v1). UW CLI reachable and all four datasets (options, darkpool, oi,
hotchains) carry the as-of date 2026-05-27. BABA has live options activity. `fz`
(Finviz) is available; float snapshotted. All `uw` commands downstream will receive
`--date 2026-05-27`. Proceeding to phase 0.5 (context).

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-05-27 (as-of present ✓)
- Latest available darkpool date: 2026-05-27 (as-of present ✓)
- Latest available oi date: 2026-05-27 (as-of present ✓)
- Latest available hotchains date: 2026-05-27 (as-of present ✓)

## Ticker sanity

- Options activity (unusual_volume top 1): BABA 2026-06-05 C115 — total_premium
  $304,232, total_volume 232, vol/OI 232, avg_iv 0.530. BABA is an actively-traded
  optionable name; not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (33): 2026-03-13, 2026-03-16, 2026-03-17, 2026-03-18,
  2026-03-19, 2026-03-20, 2026-03-23, 2026-03-24, 2026-03-25, 2026-03-26,
  2026-03-27, **[gap]** 2026-04-27, 2026-04-28, 2026-04-29, 2026-04-30, 2026-05-01,
  2026-05-04, 2026-05-05, 2026-05-06, 2026-05-07, 2026-05-08, 2026-05-11,
  2026-05-12, 2026-05-13, 2026-05-14, 2026-05-15, 2026-05-18, 2026-05-19,
  2026-05-20, 2026-05-21, 2026-05-22, 2026-05-26, 2026-05-27.
  **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27 (~1
  month missing). Phase-5 self-history / phase-0.5 percentiles must treat the
  history as two contiguous blocks, not one continuous series.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 2.40B (Shs Outstand 2.40B; Short Float 1.63%) — carried to
  phase-2/3 for %-of-float normalization and to phase-7c for the SI gate.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on `no`,
  phase-7c would fall back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

(none — v1)

## Tool errors

(none — all green)
