# Phase 0 — Intake

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/DOCN/2026-07-17
**Version:** v1
**Generated:** 2026-07-20T01:01:41Z

## Summary

Ticker DOCN (DigitalOcean) validated. Output directory created (empty → v1). UW
CLI reachable and all five datasets (options, darkpool, oi, hotchains, screener)
have data through the as-of date 2026-07-17. DOCN has live options activity.
Local parquet snapshot present with DuckDB available. `fz` is reachable but
returns a sparse fundamentals set for DOCN (float / short-float fields empty) —
float-normalization lanes degrade to WebSearch downstream. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets `["darkpool","hotchains","oi","options","screener"]`
- Latest available options date: 2026-07-17 (== as-of; no forward-look risk)
- Latest available darkpool date: 2026-07-17
- Latest oi / hotchains / screener: 2026-07-17
- Options dates ≤ as-of (last 5): 2026-07-13, -14, -15, -16, -17 (contiguous into as-of)

## Ticker sanity

- Options activity (unusual_volume top 1): DOCN 2026-07-24 **$123 call**,
  total_volume=461, open_interest=2, **vol_oi_ratio=230.5**, total_premium=$260,660,
  avg_iv=0.994. Confirmed live, non-thin near-dated call activity.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local screener dates: 2026-03-13 → 2026-07-17 (69 sessions). **Gap flagged: yes**
  — non-contiguous 2026-03-27 → 2026-04-27 (April 1–24 absent). Self-history
  percentiles (phase-0.5/5) must treat that window as missing, not zero.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (CLI + `doctor` green)
- `Shs Float`: **n/a** — `fz quote DOCN` returns a truncated fundamentals block
  (only Book/sh, Cash/sh, Dividend*, Employees, Enterprise Value, IPO, Income,
  Index, Market Cap, Payout, Sales present; Shs Float / Shs Outstand / Short Float
  / Price all null). Market Cap surfaced = **12.41B**.
- Impact: phase-2/3 % -of-float normalization and phase-7c short-interest lane fall
  back to WebSearch/Finnhub for DOCN. Not an abort condition (`lib/fz-recipes.md`).

## Prior versions

(none — v1)

## Tool errors

(none — all green; fz float fields empty is a data-coverage gap, not a tool error)

## DATA NOTE / CORRECTION

(none — all values round-tripped through `jq` on first read)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-07-17 has full data across all datasets — no as-of degradation.
  2. Near-dated $123 call (7/24 expiry) already screaming with vol/oi=230.5 —
     phase-1 must resolve whether this is opening directional flow or hedging.
  3. `fz` float/SI fields are empty for DOCN → use WebSearch for float & short
     interest in phases 2/3/7c; local screener has an April gap (skip, don't zero).
- **Open questions:** Is DOCN near an earnings/catalyst window (the 7/24-dated
  spike suggests a near-term event)? Resolve in phase-0.5 / phase-7c.
