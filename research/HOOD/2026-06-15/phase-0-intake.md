# Phase 0 — Intake

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/HOOD/2026-06-15
**Version:** v1
**Generated:** 2026-06-16T11:43:31Z

## Summary

Ticker HOOD (Robinhood Markets) validated — 4-char US-listed equity with deep
options activity. Output directory created fresh (no prior run → v1). UW CLI
reachable and every dataset (options/darkpool/oi/hotchains/screener) carries data
through the as-of date 2026-06-15, so all downstream phases will run as-of
reproducible with `--date 2026-06-15`. Local parquet snapshot + DuckDB both
present; `fz` healthy. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets `["darkpool","hotchains","oi","options","screener"]`
- Latest available **options** date: 2026-06-15 (== as-of ✓)
- Latest available **darkpool** date: 2026-06-15 (== as-of ✓)
- Latest available **oi** date: 2026-06-15 · **hotchains**: 2026-06-15 · **screener**: 2026-06-15

## Ticker sanity

- Options activity (unusual_volume top 1): `HOOD` 2026-07-10 **$96 put**,
  vol 726 / OI 3 → **vol_oi_ratio 242**, total_premium $351,588, avg_iv 0.656
  (source `All Options/bot-eod-report-2026-06-15.parquet`). Deep, active options — not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (recent window): 2026-05-26, 05-27, 05-28, 05-29,
  06-01, 06-02, 06-03, 06-04, 06-05, 06-08, 06-09, 06-10, 06-11, 06-12, 06-15
  (gap flagged: **no** — recent window is contiguous trading days; 05-30/05-31 and
  06-06/06-07 are weekends)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **760.74M** (Shs Outstand 791.10M; Short Float 4.52%) — carried to
  phase-2/3 for %-of-float normalization
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); used
  downside-only/advisory.

## Prior versions

(none — v1)

## Tool errors

(none — all green)
