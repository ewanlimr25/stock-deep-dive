# Phase 0 — Intake

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/KWEB/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T00:00:00Z

## Summary

Ticker validated (KWEB = KraneShares CSI China Internet ETF, US-listed). Output
directory created. UW MCP reachable and the as-of date 2026-05-22 is the latest
available date across all five datasets (options/darkpool/oi/hotchains/screener).
KWEB shows live options activity. Local parquet snapshot present with DuckDB
available. Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-22 (matches as-of)
- Latest available darkpool date: 2026-05-22 (matches as-of)
- Note: a non-contiguous gap exists between 2026-03-27 and 2026-04-27 (no data
  for the ~1-month window). Phase-5 historical and phase-0.5 self-history must
  treat the local series as two contiguous blocks (Mar 13–27, then Apr 27–May 22).

## Ticker sanity

- Options activity (unusual_volume top 1): KWEB 2026-06-26 33.5C, vol 1000,
  OI 11, vol/OI 90.9, avg_iv 0.392. Confirms tradable options chain. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20, 03-23,
  03-24, 03-25, 03-26, 03-27, **[gap]**, 04-27, 04-28, 04-29, 04-30, 05-01,
  05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18,
  05-19, 05-20, 05-21, 05-22 (gap flagged: **yes** — 03-27 → 04-27)
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

(none — v1)

## Tool errors

(none — all green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. KWEB is a **China-internet ETF** — macro/regime phases must treat
     China policy, ADR delisting risk, USD/CNY, and US-China relations as the
     dominant exogenous drivers, not US single-name fundamentals.
  2. Local series has a **one-month gap (03-27 → 04-27)** — any z-score /
     percentile over the full local window is built on two blocks, not a
     continuous ~50-day tape.
  3. As-of = latest available date, so this is a **current-edge** read, not a
     backtest into a known future.
- **Open questions:** Is the 2026-05-22 flow unusual for KWEB or a normal busy
  day? (phase 0.5 answers.)
