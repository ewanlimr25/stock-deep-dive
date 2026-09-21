# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc., NYSE)
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T00:00:00Z

## Summary

Ticker `PATH` validated (UiPath Inc., US-listed equity, 4 chars alphanumeric). Output
directory created and empty → this is a v1 run. UW MCP reachable;
`historical_available_dates` returns 31 dates across all five datasets, with
`2026-05-22` (the as-of date) present in every dataset. PATH has live options
activity on the as-of date. Local parquet snapshot present with DuckDB available,
so the escape hatch and self-history cuts are usable. Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: **ok** — all five datasets (darkpool, hotchains, oi,
  options, screener) return the same 31-date list.
- Latest available options date: **2026-05-22** (= as-of; live data NOT called).
- Latest available darkpool date: **2026-05-22**.
- **Known non-contiguous gap:** data runs `2026-03-13 → 2026-03-27`, then jumps to
  `2026-04-27 → 2026-05-22` (≈1-month hole over early/mid April). Phase 5
  historical lookbacks must treat the windows as two contiguous blocks, not one.

## Ticker sanity

- Options activity (unusual_volume top 1, date=2026-05-22): **PATH 2026-05-29 $17
  call** — `total_volume=801`, `open_interest=82`, `vol_oi_ratio=9.77`,
  `avg_iv=153.9%`, `total_premium=$1,598`. New short-dated position opening; very
  high IV on this contract. PATH is therefore options-active near the $17 line.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (31, matching MCP): `2026-03-13, 03-16, 03-17, 03-18,
  03-19, 03-20, 03-23, 03-24, 03-25, 03-26, 03-27, 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22` — **gap flagged: yes** (2026-03-27 → 2026-04-27).
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`), tagged ` DUCKDB`.

## Prior versions

None — v1.

## Tool errors

None — all green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a.
- **Three things later phases should remember:**
  1. PATH trades near $17; a 2026-05-29 $17 call is opening with 154% IV — very
     elevated near-term implied vol (earnings/event suspicion → check phase-0.5/7b).
  2. Data has a ~1-month gap (2026-03-27 → 2026-04-27); historical percentiles
     must not interpolate across it.
  3. As-of is 2026-05-22; pass `date=2026-05-22` to every UW tool, never live.
- **Open questions:** Is the 154% IV an earnings event (UiPath typically reports
  late May / early June)? Phase 0.5 and 7b should resolve the catalyst.
