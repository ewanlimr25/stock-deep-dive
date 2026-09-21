# Phase 0 — Intake

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NVDA/2026-05-29
**Version:** v1
**Generated:** 2026-05-30T11:50Z

## Summary

Ticker NVDA validated (US-listed equity, Technology, optionable, mega-cap
~$5.18T). Output directory created; fresh v1 run. UW CLI reachable and returns
the requested as-of date (2026-05-29) across all 5 datasets. Local parquet
substrate present with DuckDB available; `fz` (Finviz) augments healthy and its
live price (211.14) matches the as-of screener close exactly. Proceeding to
phase 0.5 (context).

**Ground-truth anchor (verified from `stock-screener-2026-05-29.parquet`):**
NVDA **close 211.14**, prev_close 214.25 (**−1.45% on the day**), total_volume
148.4M vs avg30 161.2M (0.92× — a below-average-volume down day). 52-wk range
132.92 – 236.54. Next earnings **2026-08-26** (no earnings catalyst inside any
near-term option window).

## UW availability

- `uw historical available-dates`: ok (all 5 datasets latest = 2026-05-29)
- Datasets present: darkpool, hotchains, oi, options, screener (n=35 dates each)
- Latest available options date: 2026-05-29 · Latest darkpool: 2026-05-29
- **Known non-contiguous gap:** dates run 2026-03-13 → 2026-03-27, then jump to
  2026-04-27 → 2026-05-29 (no data 2026-03-28 → 2026-04-26). Phase-5 historical
  and phase-0.5 self-history must treat this gap explicitly.

## Ticker sanity

- Options activity (unusual_volume top 1): NVDA 2026-06-10 **217.5 put**,
  vol 644, OI 1, vol/OI 644, premium $414.5K. Confirms a deeply liquid options
  chain with strikes centered near the ~211 spot. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Screener files use prefix **`stock-screener-<DATE>.parquet`** (not
  `screener-`). Available local dates (35): 2026-03-13, 16, 17, 18, 19, 20, 23,
  24, 25, 26, 27, **[gap]**, 04-27, 28, 29, 30, 05-01, 04, 05, 06, 07, 08, 11,
  12, 13, 14, 15, 18, 19, 20, 21, 22, 26, 27, 28, 29
  (gap flagged: **yes**, 2026-03-28 → 04-26 missing).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 23.27B (Shs Outstand 24.22B; Short Float 1.28%; fz live Price
  211.14 — matches as-of close). Carried to phase-2/3 for %-of-float normalization.
- **Caveat:** `fz` is a *live* snapshot, not as-of-reproducible. Today the live
  price coincides with the 2026-05-29 close, so float/SI are usable as-of; treat
  any future drift as live, not historical (`uw-cli-mcp-parity` memo).
- Note: on `fz_available=no`, phase-7c falls back to WebSearch SI, phase-7b to
  Finnhub peers.

## Prior versions

(none — v1)

## Tool errors

(none — all green)
