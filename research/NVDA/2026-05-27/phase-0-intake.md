# Phase 0 — Intake

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NVDA/2026-05-27
**Version:** v1
**Generated:** 2026-05-28T02:14:10Z

## Summary

Ticker validated (NVDA, US-listed equity). Output directory created. UW CLI
reachable with latest options + darkpool dates both at the as-of date
(2026-05-27). NVDA shows liquid, unusual options activity. Local parquet
snapshot present with DuckDB available; `fz` healthy. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-05-27
- Latest available darkpool date: 2026-05-27
- Data keys present: darkpool, hotchains, oi, options, screener

## Ticker sanity

- Options activity (unusual_volume top 1): NVDA 2026-06-08 $190 call,
  total_premium $1,720,036, vol/OI 820, avg_iv 0.455 — liquid, not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (screener): 2026-03-13 → 2026-03-27, then
  2026-04-27 → 2026-05-27.
- **Gap flagged: yes** — non-contiguous ~1-month hole between 2026-03-27 and
  2026-04-27 (no data 2026-03-30 → 2026-04-24). Phase-5 historical and
  phase-0.5 self-history must treat the local window as two segments, not one
  continuous series.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 23.27B (Shs Outstand 24.22B; Short Float 1.22%) — carried to
  phase-2/3 for %-of-float normalization and to seed next run's `quote-drift`.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`);
  downside-only/advisory, never enters Kelly `p`.

## Prior versions

(none — v1)

## Tool errors

(none — all checks green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = 2026-05-27 is the latest available date for BOTH options and
     darkpool — this is a current, fully-populated snapshot.
  2. NVDA float = 23.27B shares (Short Float 1.22% — low). Use 23.27B as the
     denominator for %-of-float block/OI normalization in phases 2/3.
  3. Local data has a non-contiguous gap (2026-03-27 → 2026-04-27); self-history
     percentiles must not assume a continuous series across it.
- **Open questions:** none for intake.
