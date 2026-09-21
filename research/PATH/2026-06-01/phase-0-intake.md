# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc., NYSE)
**As-of date:** 2026-06-01
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-06-01
**Version:** v1 (directory was empty — no prior run)
**Generated:** 2026-06-01T20:07:10-04:00

## Summary

Ticker validated as a US-listed optionable equity (UiPath Inc.). Output directory
created. UW CLI reachable and current — latest available data date is **2026-06-01**,
exactly matching the requested as-of, so every downstream tool will receive
`--date 2026-06-01` where the flag exists. PATH shows live, aggressive options
activity (a $371K call sweep, vol/OI 167×). Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-06-01** (min 2026-03-13, n=36)
- Latest available darkpool date: **2026-06-01** (min 2026-03-13, n=36)
- Latest available oi / hotchains / screener date: **2026-06-01** (all n=36)
- As-of 2026-06-01 is the freshest date in the corpus → fully reproducible, no
  trailing-date drift.

## Ticker sanity

- Options activity (`unusual-volume` top 1): **PATH 2026-06-05 $5.50 CALL** —
  total_premium $371,476, total_volume 501, open_interest 3, vol_oi_ratio 167×,
  avg_iv 4.77. Confirms an actively-traded options chain. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (36): 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20,
  03-23, 03-24, 03-25, 03-26, 03-27, **‖gap‖**, 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29, 06-01.
- **Gap flagged: yes** — non-contiguous hole 2026-03-27 → 2026-04-27 (~1 month
  missing). Phase-5 historical lookbacks and any DUCKDB self-history percentiles
  must treat the corpus as ~36 trading days split across two blocks, not a
  continuous ~2.5-month run.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **412.34M** (Shs Outstand 520.44M) — carried to phase-2/3 for
  %-of-float normalization of block / sweep sizes.
- `Short Float`: **31.15%** snapshot — unusually high; this is a heavily-shorted
  name. Flagged now so phase-7c (positioning gate) treats short-squeeze / borrow
  dynamics as a first-order factor, not a footnote.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

<none — this is v1>

## Tool errors

<none — all probes green>

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-06-01 == latest data date → reproducible, pass `--date 2026-06-01`.
  2. PATH carries a **31.15% short float** on a 412.34M float — squeeze/borrow is
     a first-order positioning factor (phase-7c gate).
  3. Local corpus has a **one-month gap (03-27 → 04-27)**; treat history as two
     blocks (phase-5).
- **Open questions:** Is the current call-sweep activity directional conviction or
  short-dated lottery/hedging? (phase-1 to resolve.)
