# Phase 0 — Intake

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/HOOD/2026-05-27
**Version:** v1
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** (none — first phase)

## Summary

Ticker HOOD (Robinhood Markets, US-listed equity) validated. Output directory
created fresh (v1, no prior run). UW CLI reachable and all five datasets
(options, darkpool, hotchains, oi, screener) carry the as-of date 2026-05-27.
HOOD has active options. Local parquet snapshot + DuckDB present; `fz` healthy.
Proceeding to phase 0.5 (context).

## UW availability

- `uw historical available-dates`: ok (exit 0)
- Latest available options date: 2026-05-27 (matches as-of)
- Latest available darkpool date: 2026-05-27 (matches as-of)
- Latest hotchains date: 2026-05-27 · Latest oi date: 2026-05-27 · Latest screener: 2026-05-27
- All UW commands downstream will pass `--date 2026-05-27` where the flag exists.

## Ticker sanity

- Options activity (unusual_volume top 1): `HOOD` 2026-07-02 P74 — vol 346 / OI 8,
  vol/OI 43.25, total premium $159,317, avg IV 0.575. Healthy options activity,
  not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (screener): 2026-03-13, 2026-03-16, 2026-03-17, 2026-03-18,
  2026-03-19, 2026-03-20, 2026-03-23, 2026-03-24, 2026-03-25, 2026-03-26, 2026-03-27,
  **[GAP]**, 2026-04-27, 2026-04-28, 2026-04-29, 2026-04-30, 2026-05-01, 2026-05-04,
  2026-05-05, 2026-05-06, 2026-05-07, 2026-05-08, 2026-05-11, 2026-05-12, 2026-05-13,
  2026-05-14, 2026-05-15, 2026-05-18, 2026-05-19, 2026-05-20, 2026-05-21, 2026-05-22,
  2026-05-26, 2026-05-27
- **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27 (the month
  of 2026-03-30 → 2026-04-24 is absent locally). Phase-5 self-history percentiles must
  treat the available window as ~2 discontinuous blocks, not one continuous 50-day run.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 761.05M (Shs Outstand 791.10M; Short Float 4.96%) — carried to
  phase-2/3 for %-of-float normalization and to phase-7c for the SI gate.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); all
  lanes healthy so no degrade needed.

## Prior versions

(none — v1)

## Tool errors

(none — all checks green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-05-27 is the *latest* available date in every dataset — this is a
     current-edge run; trailing/leading windows anchor here.
  2. Local self-history has a one-month gap (2026-03-30 → 2026-04-24) — phase-5 must
     not assume a contiguous lookback.
  3. Float = 761.05M, Short Float 4.96% (fz snapshot) — use for order-size-as-%-float
     in phases 2/3 and the SI gate in 7c.
- **Open questions:** none for intake.
