# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-07-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-07-22
**Version:** v1
**Generated:** 2026-07-22

## Summary

Ticker validated (PATH = UiPath Inc., NYSE, Technology / Software — Infrastructure,
USA). Output directory created and empty → v1. UW CLI reachable; local parquet
snapshot present for the exact as-of date (2026-07-22). PATH carries live options
activity. `fz` reachable but returns a reduced fundamentals set for PATH (no
float/short fields) — float normalization and SI degrade to WebSearch/Finnhub
downstream. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** — datasets present: darkpool, hotchains, oi, options, screener
- Latest available options date: **2026-07-22** (= as-of; no staleness)
- Latest available darkpool date: **2026-07-22**
- Latest available oi date: **2026-07-22**
- Latest available screener date: **2026-07-22**

## Ticker sanity

- Options activity (unusual_volume top 1): **PATH 2026-08-21 P9.5** — total_volume 501, vol/OI 501 (OI=1), total_premium $17,243, avg_iv 0.672. Options are live and tradeable, not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (screener, n=71): 2026-03-13 → 2026-07-22.
  Contiguous within two blocks with a **known non-contiguous gap 2026-03-27 → 2026-04-27** (no snapshots 2026-03-30…2026-04-24). May-onward is dense/daily.
  - Gap flagged: **yes** (2026-03-27 → 2026-04-27). Phase-5 self-history must not span the gap as if contiguous.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (health check passed)
- `Shs Float`: **n/a** — `fz quote PATH --agent` returned a reduced 14-field fundamentals payload with no `Shs Float` / `Shs Outstand` / `Short Float` keys. Advisory float/short augments degrade: phase-7c falls back to **WebSearch SI/float**, phase-7b to **Finnhub peers**.
- Advisory context carried from `fz quote` (present fields): Market Cap **$5.54B**, Enterprise Value **$4.32B**, Sales (TTM) **$1.67B**, Income **$327.41M**, Book/sh **$3.66**, Cash/sh **$2.53**, Employees **3,981**, IPO **Apr 21, 2021**.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); this run treats every float/SI number as WebSearch-sourced until phase 7c.

## Prior versions

<none — v1>

## Tool errors

<none — all green>
