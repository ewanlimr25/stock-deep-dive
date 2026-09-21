# Phase 0 — Intake

**Ticker:** MU
**As-of date:** 2026-06-25
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MU/2026-06-25
**Version:** v1
**Generated:** 2026-06-25

## Summary

Ticker MU (Micron Technology) validated — 2-char US-listed equity with deep,
active options. Output directory created (empty → v1). UW CLI reachable and all
five datasets (darkpool, hotchains, oi, options, screener) carry data for the
as-of date 2026-06-25, so every downstream phase runs with `--date 2026-06-25`
and never touches live data. A prior MU deep-dive exists at
`research/MU/2026-06-23/` — phase 0.5 will diff self-history against it.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-06-25
- Latest available darkpool date: 2026-06-25
- Latest available oi date: 2026-06-25
- Latest available hotchains date: 2026-06-25
- Latest available screener date: 2026-06-25

## Ticker sanity

- Options activity (unusual_volume top 1): MU 2026-07-02 **150 put**, total_volume
  6015, open_interest 2, **vol_oi_ratio 3007.5**, total_premium $6,112, avg_iv
  4.46. Deep, active chain confirmed — not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, **[gap]**, 2026-04-27 →
  2026-06-25 (contiguous trading days). **Known non-contiguous gap flagged: yes**
  (no snapshots 2026-03-28 … 2026-04-24). Latest local date = as-of = 2026-06-25.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **1.12B** (Shs Outstand 1.13B; Short Float 3.71%) — carried to
  phase-2/3 for %-of-float normalization and to phase-7c short-interest gate.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); all
  lanes healthy this run.

## Prior versions

None for 2026-06-25 (this is v1). **Adjacent prior run:** `research/MU/2026-06-23/`
(2 trading days earlier) — phase 0.5 will compare self-history flow/positioning
deltas against it.

## Tool errors

None — all four intake probes returned valid JSON.
