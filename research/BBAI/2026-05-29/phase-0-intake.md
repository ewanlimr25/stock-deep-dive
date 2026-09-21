# Phase 0 — Intake

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BBAI/2026-05-29
**Version:** v1
**Generated:** 2026-05-31T13:28:00-04:00

## Summary

Ticker BBAI (BigBear.ai Holdings) validated as a US-listed equity with active
options. Output directory created (empty → v1). UW CLI reachable; latest
available data date for all datasets is 2026-05-29, matching the requested
as-of, so the run is fully as-of reproducible. Local parquet snapshot present
(DuckDB available) with a known non-contiguous gap between 2026-03-27 and
2026-04-27. `fz` healthy; float snapshotted (473.71M) with a notably high
26.37% short float carried forward to phase-7c. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-05-29
- Latest available darkpool date: 2026-05-29
- Latest available oi date: 2026-05-29
- Latest available hotchains date: 2026-05-29
- Latest available screener date: 2026-05-29

## Ticker sanity

- Options activity (unusual_volume top 1): `BBAI 2026-06-18 P$5.50` — total_premium
  $29,056, total_volume 372, open_interest 8, vol_oi_ratio 46.5, avg_iv 1.0605
  (source: `/Users/ewan/Documents/Stocks/All Options/bot-eod-report-2026-05-29.parquet`).
  BBAI has live, unusual options activity → proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (35): 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20,
  03-23, 03-24, 03-25, 03-26, 03-27, **[gap]** 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29.
  **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27 (the
  full month of April pre-27 is absent locally). Phase-5 self-history percentiles
  must treat the series as ~35 trading days with that hole, not a continuous span.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 473.71M (Shs Outstand 477.01M → ~99.3% of shares float; very low
  insider/locked block) — carried to phase-2/3 for %-of-float normalization.
- `Short Float`: 26.37% (snapshotted at intake; semi-monthly settlement figure) —
  carried to phase-7c as a squeeze/positioning input. **High** short float is a
  material two-sided setup (squeeze fuel vs. crowded-short conviction).
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

(none — v1)

## Tool errors

- `uw dark-pool recent --symbol BBAI …` → `Error: unknown flag: --symbol`
  (probe only; the dark-pool leaf uses different flags — handled correctly in
  phase 2. `available-dates` already confirms darkpool latest = 2026-05-29.)
- `uw --version` → `Error: unknown flag: --version` (cosmetic; CLI confirmed
  working via `available-dates` and `unusual-volume`).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical available-dates --json` | ok; all datasets latest = 2026-05-29 |
| `uw options-flow unusual-volume --symbol BBAI --top-n 1 --json` | 1 result (P$5.50 6/18, vol/OI 46.5) → options active |
| `ls "$STOCKS_DIR/Stock Screener/"` | 35 local dates; gap 03-27→04-27 |
| `fz quote BBAI --agent` | float 473.71M, shs_out 477.01M, short_float 26.37% |

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-05-29 is the latest data date — fully reproducible; pass
     `--date 2026-05-29` to every leaf that accepts it.
  2. Short float is high at 26.37% (fz) and float ≈ shares outstanding (473.71M /
     477.01M) — phase-7c squeeze/positioning gate is live; phases 2/3 should
     normalize order/wall sizes against the 473.71M float.
  3. Local self-history has an April gap (03-27 → 04-27) — phase-5 percentile
     math must account for the discontinuity.
- **Open questions:** none for intake.
