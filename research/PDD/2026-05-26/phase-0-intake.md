# Phase 0 — Intake

**Ticker:** PDD
**As-of date:** 2026-05-26
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PDD/2026-05-26
**Version:** v1
**Generated:** 2026-05-26T20:16:00Z

## Summary

PDD (PDD Holdings Inc., NASDAQ ADR — Pinduoduo / Temu parent) validated as a
US-listed ADR with active options. Output directory created fresh (v1). UW MCP
reachable; latest available date for every dataset (options, darkpool, oi,
hotchains, screener) is 2026-05-26, exactly matching the as-of date — so this is
a same-day workup, no staleness. Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-26
- Latest available darkpool date: 2026-05-26
- Latest available oi date: 2026-05-26
- **Data gap flag:** the available-date series is non-contiguous — it runs
  2026-03-13 → 2026-03-27, then **skips all of April 1–24**, resuming 2026-04-27
  → 2026-05-26. Phase-5 historical lookbacks must treat the ~1-month hole as
  missing data, not as a flat tape. The trailing window (2026-04-27 → 05-26, ~21
  sessions) is contiguous and is the usable recent-history block.

## Ticker sanity

- Options activity (unusual_volume top 1): `PDD 2026-06-05 104C` — total_volume
  5,956 vs open_interest 33 (vol/OI **180.5**), total_premium $1,147,257, avg_iv
  0.656. Confirms liquid, actively-traded options with fresh same-day position
  opening in near-dated calls. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, then 2026-04-27 → 2026-05-26
  (gap flagged: **yes** — April 1–24 absent). Local screener dates match the MCP
  `historical_available_dates` list exactly.
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

None — this is v1.

## Tool errors

None — all intake calls green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = latest available date (2026-05-26); this is a same-day read, treat
     all flow as current, not stale.
  2. ~1-month data gap (April 1–24) exists — phase-5 must not interpolate across
     it; usable contiguous recent block is 2026-04-27 → 2026-05-26 (~21 sessions).
  3. Same-day fresh call opening already visible (`2026-06-05 104C`, vol/OI 180) —
     phase-1 should resolve whether this is bullish initiation or hedging.
- **Open questions:** spot price, sector context, and whether 05-26 flow is
  unusual vs PDD's own baseline (phase-0.5).
