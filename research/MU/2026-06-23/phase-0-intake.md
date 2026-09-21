# Phase 0 — Intake

**Ticker:** MU
**As-of date:** 2026-06-23
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MU/2026-06-23
**Version:** v1 (no prior phase files in this directory)
**Generated:** 2026-06-23

## Summary

Ticker MU (Micron Technology) validated. Output directory created and empty → v1.
UW CLI reachable; all five datasets current through the as-of date 2026-06-23, so
this run is fully reproducible (as-of = latest available, not a trailing anchor).
MU has live, deep options activity. `fz` available; float snapshotted. Proceeding
to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (datasets: darkpool, hotchains, oi, options, screener)
- Latest available options date: **2026-06-23** (as-of date present in `.options` ✓)
- Latest available darkpool date: **2026-06-23**
- Latest available oi date: **2026-06-23**
- Latest available hotchains date: **2026-06-23**

## Ticker sanity

- Options activity (unusual_volume top 1): `MU` 2026-07-17 **1075c**, total_premium=**$2,949,636**,
  vol_oi_ratio=**248**, total_volume=248, avg_iv=1.1227 — deep, live options tape (not thin).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local screener dates: 2026-03-13 → 2026-03-27, **[gap]**, 2026-04-27 → 2026-06-23
  (gap flagged: **yes** — non-contiguous 2026-03-27 → 2026-04-27, ~1 month missing;
  irrelevant to this as-of since recent history is dense and contiguous from 2026-04-27).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **1.12B** (Shs Outstand 1.13B; Short Float 3.35%) — carried to phase-2/3
  for % -of-float normalization and to phase-7c as the SI seed.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

(none — v1)

## Tool errors

(none — all green)

## DATA NOTE / CORRECTION

(none — all values round-tripped through `jq` on first read)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-06-23 = latest available date for all datasets → fully reproducible, no trailing-anchor risk.
  2. Float = 1.12B shares, Short Float = 3.35% (low) — use for order-size %-of-float in phases 2/3 and SI gate in 7c.
  3. MU options tape is deep and liquid (a "busy name") — phase 0.5 must judge whether today's flow is genuinely unusual vs normal.
- **Open questions:** What is MU's cross-sectional rank in the semiconductor universe today, and is its flow elevated vs its own recent baseline? (phase 0.5)
