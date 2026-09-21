# Phase 0 — Intake

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SHOP/2026-07-17
**Version:** v1
**Generated:** 2026-07-19 (run date) · as-of 2026-07-17

## Summary

Ticker SHOP (Shopify Inc — Technology / Software - Application, Canada) validated.
Output directory created fresh (v1). UW CLI reachable; options + darkpool data
present through the as-of date 2026-07-17. SHOP has active, unusual options flow.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets {darkpool, hotchains, oi, options, screener}
- Latest available options date: 2026-07-17 (matches as-of)
- Latest available darkpool date: 2026-07-17 (matches as-of)
- Recent options dates present: 2026-07-01 … 2026-07-17 (contiguous trading days)

## Ticker sanity

- Options activity (unusual_volume top 1): SHOP 2026-07-24 $147 call —
  total_volume 572, vol_oi_ratio 572, total_premium $19,446, avg_iv 0.773
  (`.results[0]`). Active, healthy options tape → proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local screener dates (last 15): 2026-06-26, 06-29, 06-30, 07-01,
  07-02, 07-06, 07-07, 07-08, 07-09, 07-10, 07-13, 07-14, 07-15, 07-16, 07-17
  (gap flagged: no — contiguous trading days through as-of)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (CLI + doctor healthy)
- `Shs Float`: n/a — SHOP `fz quote --agent` returned a **partial** fundamentals
  cut (14 keys: Book/sh 9.61, Cash/sh 4.43, Market Cap 160.34B, Enterprise Value
  154.77B, Income 1.33B, Sales 12.37B, Employees 7600, Index NDX, IPO 2015-05-21;
  Shs Float / Short Float / Price absent). Sector=Technology, Industry=Software -
  Application, Country=Canada resolved cleanly.
- Note: because the float/short-float fields did not populate, phase-2/3
  %-of-float normalization and the phase-7c short-interest gate will fall back to
  WebSearch (borrow/HTB was WebSearch-only regardless). Market Cap ≈ $160.3B is
  carried forward as the size anchor.

## Prior versions

<none — v1>

## Tool errors

<none — all green; fz float fields absent is a partial-data condition, not a tool error>
