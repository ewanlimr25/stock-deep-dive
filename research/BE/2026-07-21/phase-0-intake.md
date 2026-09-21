# Phase 0 — Intake

**Ticker:** BE
**As-of date:** 2026-07-21
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BE/2026-07-21/
**Version:** v1
**Generated:** 2026-07-22T07:57:00Z

## Summary

Ticker BE (Bloom Energy Corp — NYSE) validated. Output directory created (empty,
v1 run). UW CLI reachable and all datasets (options / darkpool / oi) carry
data through the as-of date 2026-07-21. Options are actively traded (unusual-
volume top hit is a 2026-07-24 110-put, vol/OI 50.6). Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-07-21** (matches as-of ✓)
- Latest available darkpool date: **2026-07-21**
- Latest available OI date: **2026-07-21**

## Ticker sanity

- Options activity (unusual_volume top 1): **BE 2026-07-24 P110** — total_volume
  18,478 · open_interest 365 · vol_oi_ratio **50.62** · total_premium $159,994 ·
  avg_iv 3.084. Rich, liquid options tape → full workup warranted.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-07-21 (contiguous trading days)
  with the **known non-contiguous gap 2026-03-27 → 2026-04-27** (no data
  2026-03-30 … 2026-04-24). Gap flagged: **yes** — phase-5 self-history must
  treat that window as missing, not as a flat/quiet regime.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (binary present, `fz doctor` green)
- `Shs Float`: **n/a** — `fz quote BE` returned a degraded/partial 14-field
  fundamentals block (Book/sh 3.24, Cash/sh 8.76, Enterprise Value 61.89B,
  Employees 2214, …) that did **not** include Shs Float / Shs Outstand / Short
  Float / Price. Not carried forward.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`). With
  no float snapshot, phase-2/3 %-of-float normalization degrades to advisory,
  and phase-7c falls back to WebSearch for short interest / float, phase-7b to
  Finnhub peers. Never aborts.

## Prior versions

<none — v1>

## Tool errors

<none — all green>

## DATA NOTE / CORRECTION

- `fz quote BE` first read returned nulls for float/short/price; re-verified the
  fundamentals block only carries 14 keys for BE this snapshot (none of them the
  float set). Recorded as `Shs Float = n/a` rather than transcribing a null as a
  number. No other value re-read.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Full data coverage through as-of 2026-07-21 across all UW datasets — no
     as-of degradation; every phase can use `--date 2026-07-21`.
  2. Local self-history gap 2026-03-27 → 2026-04-27 — phase-5 percentiles must
     exclude that window, not average over it.
  3. No `fz` float snapshot → phase-7c SI/float comes from WebSearch; treat any
     %-of-float figure in phases 2/3 as advisory, not sourced.
- **Open questions:** direction, catalyst, and whether the heavy near-dated put
  volume (110P vol/OI 50.6) is hedging vs. directional — resolved in phases 1–4.
