# Phase 0 — Intake

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/OKLO/2026-07-17
**Version:** v1
**Generated:** 2026-07-18T00:00:00Z

## Summary

Ticker OKLO (Oklo Inc — advanced-nuclear / SMR developer, pre-revenue) validated as a
US-listed equity with active options. Output directory created fresh (no prior run).
UW CLI reachable; options, darkpool, OI and screener parquet all present through the
as-of date 2026-07-17. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-07-17 (matches as-of)
- Latest available darkpool date: 2026-07-17
- Latest available OI date: 2026-07-17 · screener: 2026-07-17
- **Coverage gap flag:** the options date list is non-contiguous — a block from
  2026-04-28 → 2026-06-30 is dense but there is a hole between **2026-04-27 and
  2026-03-27** (all of early April missing). Not relevant to a 2026-07-17 as-of run
  (recent history is complete: every session 2026-06 → 2026-07-17 present), but
  phase-5 long-lookback percentiles should note it.

## Ticker sanity

- Options activity (unusual_volume top 1): OKLO **2026-07-24 $41.5 call** — total_volume
  2428, total_premium $519,149, open_interest 125, **vol/OI 19.4**, avg_iv 0.9085 (~91%).
  Confirms liquid, aggressively-traded options with very high IV. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local Stock-Screener dates (recent tail): 2026-07-08, -09, -10, -13, -14,
  -15, -16, -17 (contiguous recent window present; gap flagged: yes for the deeper
  April hole noted above, no for the recent window).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't express
  (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (CLI + doctor healthy) — **but `fz quote OKLO` returned a
  degraded 14-field fundamentals block with NO float / short-float / shares-outstanding
  fields.** Present fields: Market Cap 7.15B, Enterprise Value 4.95B, Book/sh 15.18,
  Cash/sh 12.69, Income −128.92M (net loss TTM), Sales 0.00M (pre-revenue), Employees
  205, IPO Jul 08 2021.
- `Shs Float`: **n/a** (not present in this snapshot). Phase-2/3 %-of-float
  normalization will fall back; phase-7c short-interest lane must retry a fuller `fz`
  recipe or WebSearch.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); the missing
  float here means those lanes degrade to WebSearch/Finnhub as designed.

## Prior versions

(none — v1)

## Tool errors

None fatal. Two schema notes surfaced during probing (handled, not errors):
- `uw options-flow unusual-volume` returns `{results:[...], source}`, not a bare array —
  read via `.results[0]`.
- `fz quote OKLO --agent` returned a partial 14-field fundamentals block (float/short
  absent). Recorded as a degraded-source condition, not a fatal error.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. OKLO is **pre-revenue** (Sales ~0, net loss −$128.9M) with a $7.15B market cap —
     this is a story/theme name; fundamentals phase-7b will almost certainly be a
     downside veto lens, not support.
  2. Options are **very high IV (~91%)** and aggressively traded (vol/OI 19.4 on the
     front-week $41.5 call) — flow signal quality is high but premium is expensive.
  3. `fz` float/short is **unavailable this run** — phase-7c must source short interest
     from WebSearch; do not silently report float-normalized sizes in phase-2/3.
- **Open questions:** current spot price and where $41.5 sits relative to it (resolve in
  phase 0.5 / phase 1); recent catalyst driving the 91% IV.
