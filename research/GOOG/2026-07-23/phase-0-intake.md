# Phase 0 — Intake

**Ticker:** GOOG
**As-of date:** 2026-07-23
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/GOOG/2026-07-23
**Version:** v1
**Generated:** 2026-07-24T01:18:35Z

## Summary

Ticker validated (GOOG — Alphabet Inc. Class C, US-listed mega-cap equity).
Output directory created fresh (no prior run for this date). UW CLI reachable
and the as-of date 2026-07-23 is the latest available across options, darkpool,
and OI datasets — no as-of/latest gap. GOOG shows active (in fact heavy) options
flow. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (returned keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: **2026-07-23** (= as-of, no gap)
- Latest available darkpool date: **2026-07-23** (= as-of, no gap)
- Latest available OI date: **2026-07-23** (= as-of, no gap)

## Ticker sanity

- Options activity (unusual_volume top 1): **GOOG 2026-07-31 332.5C** —
  vol 721 / OI 2 → vol/OI ratio 360.5, total premium $177,338, avg IV 0.378.
  Confirms live, unusual options activity (short-dated OTM calls). Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local screener dates (tail): 2026-07-08 … 2026-07-23, contiguous
  through the as-of date (gap flagged: **no**)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (`fz doctor` healthy)
- `Shs Float`: **n/a** — GOOG's `fz quote` fundamentals payload does not carry
  the `Shs Float` / `Shs Outstand` / `Short Float` fields in this run (mega-cap
  field-set). Phase-2/3 %-of-float normalization will fall back to Finnhub /
  WebSearch share counts if needed; phase-7c SI will source from `fz` short-
  interest recipe or WebSearch.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

<empty for v1>

## Tool errors

<none — all probes green>
