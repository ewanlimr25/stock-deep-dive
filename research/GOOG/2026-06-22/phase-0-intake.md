# Phase 0 — Intake

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/GOOG/2026-06-22
**Version:** v1 (no prior runs in this dir)
**Generated:** 2026-06-22

## Summary

Ticker GOOG (Alphabet Inc. Class C) validated as a US-listed equity with active
options. Output directory created (empty → v1). UW CLI reachable; the as-of date
2026-06-22 is present in every dataset (options / darkpool / oi / hotchains /
screener), so the run is fully as-of reproducible — no anchoring to a trailing
latest. Local parquet + DuckDB present; `fz` healthy with float snapshotted.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (JSON parsed; 5 datasets, 50 dates each)
- Latest available options date: **2026-06-22** (= as-of)
- Latest available darkpool date: **2026-06-22** (= as-of)
- Latest oi / hotchains / screener date: **2026-06-22** (all = as-of)

## Ticker sanity

- Options activity (unusual_volume top 1): **GOOG 2026-07-02 $347.5 CALL** —
  `total_premium=$489,883`, `total_volume=648`, `open_interest=3`,
  `vol_oi_ratio=216`, `avg_iv=0.3545`. Healthy, liquid options tape; not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (Stock Screener, 50): 2026-03-13, 03-16, 03-17, 03-18,
  03-19, 03-20, 03-23, 03-24, 03-25, 03-26, 03-27, **[gap]** 04-27, 04-28, 04-29,
  04-30, 05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14,
  05-15, 05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29, 06-01,
  06-02, 06-03, 06-04, 06-05, 06-08, 06-09, 06-10, 06-11, 06-12, 06-15, 06-16,
  06-17, 06-18, 06-22.
  - **Gap flagged: yes** — known non-contiguous gap 2026-03-27 → 2026-04-27
    (~1 month missing). Recent window (May–Jun) is dense and contiguous except the
    expected 06-19 Juneteenth market holiday (06-18 → 06-22). Phase-5 self-history
    percentiles should treat the pre-04-27 block as a separate regime.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **5.07B** (Shs Outstand 5.46B; Short Float 0.89%; Price $348.78)
  — carried to phase-2/3 for %-of-float order-size normalization.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); it is
  downside-only/advisory and never enters the Kelly `p`.

## Prior versions

None — this is v1 for GOOG / 2026-06-22.

## Tool errors

None. All five intake reads (available-dates, unusual-volume, DuckDB import,
local ls, fz quote) round-tripped through `jq` / exit 0.
