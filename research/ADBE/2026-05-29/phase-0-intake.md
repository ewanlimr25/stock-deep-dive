# Phase 0 — Intake

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ADBE/2026-05-29
**Version:** v1
**Generated:** 2026-05-30T19:37:25Z

## Summary

Ticker ADBE (Adobe Inc., NASDAQ) validated. Output directory created. UW CLI
reachable and the as-of date 2026-05-29 is the latest available options/darkpool
date locally. Options activity confirmed present. Local parquet substrate and
DuckDB both available; `fz` (Finviz) augment available with float snapshotted.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date (hotchains): 2026-05-29
- Latest available darkpool date: 2026-05-29
- As-of date 2026-05-29 is present in both lists — all downstream `uw` calls pass
  `--date 2026-05-29` where the flag exists.

## Ticker sanity

- Options activity (unusual_volume top 1): `ADBE 2026-06-05 C277.5` —
  total_volume 285, open_interest 4, vol_oi_ratio 71.25, total_premium $32,534,
  avg_iv 0.488. Options are active. Source:
  `/Users/ewan/Documents/Stocks/All Options/bot-eod-report-2026-05-29.parquet`.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (35): 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20,
  03-23, 03-24, 03-25, 03-26, 03-27, **[gap]** 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29.
- **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27
  (the known ~1-month hole). Phase-5 long-lookback and phase-0.5 self-history
  percentiles must treat the local window as two contiguous blocks
  (mid-Mar..03-27 and 04-27..05-29), not a continuous 11-week run.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 403.40M (Shs Outstand 406.00M; Short Float 4.70%) — carried to
  phase-2/3 for %-of-float normalization, and seeds next run's `quote-drift`.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`);
  contributions are downside-only/advisory.

## Prior versions

(none — v1)

## Tool errors

(none — all green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = 2026-05-29; pass `--date 2026-05-29` to every `uw` leaf that takes it.
  2. Shs Float = 403.40M, Short Float = 4.70% — normalize block/OI sizes against this.
  3. Local data has a Mar-27 → Apr-27 gap; self-history/historical lookbacks must
     not assume contiguity.
- **Open questions:** none for intake.
