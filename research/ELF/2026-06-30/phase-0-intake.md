# Phase 0 — Intake

**Ticker:** ELF
**As-of date:** 2026-06-30
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ELF/2026-06-30
**Version:** v1
**Generated:** 2026-07-01T00:14:41Z

## Summary

Ticker ELF (e.l.f. Beauty Inc) validated — 3-char alphanumeric US-listed equity.
Output directory created (empty → v1). UW CLI reachable and the as-of date
2026-06-30 is present in every dataset (options / darkpool / oi / hotchains /
screener, latest date = 2026-06-30). ELF shows live options activity. Local
parquet snapshot present (56 dates, 2026-03-13 → 2026-06-30) with one known
non-contiguous gap in April; DuckDB available. `fz` CLI is up but its live
fundamentals grid is currently degraded to 14/84 fields (no float) — advisory
lanes fall back to WebSearch. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: **2026-06-30** (n=56)
- Latest available darkpool date: **2026-06-30** (n=56)
- Latest oi / hotchains / screener date: **2026-06-30** (n=56 each)
- As-of 2026-06-30 confirmed present in all datasets (no as-of anchoring needed).

## Ticker sanity

- Options activity (unusual_volume top 1): **ELF 2026-07-31 $58 call** —
  total_volume=598, open_interest=2, vol_oi_ratio=299, total_premium=$961,252,
  avg_iv=0.594. Options are actively traded → proceed (not thin).
- Source parquet: `~/Documents/Stocks/All Options/bot-eod-report-2026-06-30.parquet`

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (n=56, options dataset):
  2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20, 03-23, 03-24, 03-25, 03-26,
  03-27, **[GAP]** 04-27, 04-28, 04-29, 04-30, 05-01, 05-04, 05-05, 05-06,
  05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18, 05-19, 05-20, 05-21,
  05-22, 05-26, 05-27, 05-28, 05-29, 06-01, 06-02, 06-03, 06-04, 06-05, 06-08,
  06-09, 06-10, 06-11, 06-12, 06-15, 06-16, 06-17, 06-18, 06-22, 06-23, 06-24,
  06-25, 06-26, 06-29, 06-30
- **Gap flagged: YES** — `2026-03-27 → 2026-04-27` is a ~31-day non-contiguous
  hole (no local data Mar 28–Apr 26). The 05-22→05-26 (Memorial Day) and
  06-18→06-22 (Juneteenth) jumps are ordinary holiday weekends, not gaps.
  Phase-5 historical percentiles must caveat the missing April window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (`fz --version` + `fz doctor` pass; ELF quote returns
  real data — company "e.l.f. Beauty Inc", sector present)
- `Shs Float`: **n/a this run** — the live Finviz fundamentals grid is degraded
  to 14/84 fields (Book/sh 19.13, Cash/sh 4.87, Market Cap 4.40B, EV 5.03B,
  Sales 1.64B, Income 26.32M, Employees 849, IPO Sep 22 2016). Float / Short
  Float / Price / technicals fields are absent from the current fetch (confirmed
  with `--json --no-cache --data-source live` — same 14 fields). Not a `fz`
  outage; the grid parser is returning a partial set today.
- **Downstream impact:** phase-2/3 %-of-float normalization and phase-7c short
  interest degrade to **WebSearch** fallback; phase-7b peer/breadth may still use
  `fz screener`/`fz group` (different endpoints, probe in-phase). Advisory only —
  never blocks the run.

## Prior versions

_None — this is v1._

## Tool errors

_None — all phase-0 probes returned exit 0. The `fz` 14-field grid is a data
degradation (documented above under Finviz augments), not a tool error._

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-06-30 is fully covered locally; every UW read should pass
     `--date 2026-06-30`.
  2. There is a **31-day April data hole** (2026-03-27 → 2026-04-27) — phase-5
     historical distributions and phase-0.5 self-history must caveat it.
  3. `fz` float/short/technicals are **unavailable** this run → phase-2/3 float
     normalization and phase-7c SI use WebSearch; do not fabricate a float number.
- **Open questions:** none for intake; hand off to phase 0.5 for cross-sectional
  and self-history context.
