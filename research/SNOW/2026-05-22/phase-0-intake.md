# Phase 0 — Intake

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SNOW/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T15:03:41Z

## Summary

Ticker SNOW (Snowflake Inc.) validated. Output directory created (no prior run
for this date → v1). UW MCP reachable; latest available date for all five data
types is 2026-05-22, matching the requested as-of date — so every downstream UW
call will pass `date=2026-05-22` and never hit live data. SNOW shows live
options activity. Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-22
- Latest available darkpool date: 2026-05-22
- Latest available oi date: 2026-05-22
- Latest available hotchains date: 2026-05-22
- Latest available screener date: 2026-05-22

## Ticker sanity

- Options activity (`unusual_volume` top 1): `SNOW 2026-06-26 125C` —
  total_premium $1,234,425, total_volume 250, vol/OI 250, avg_iv 0.848. Options
  tape is active; not a thin name.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (31): 2026-03-13, 2026-03-16, 2026-03-17, 2026-03-18,
  2026-03-19, 2026-03-20, 2026-03-23, 2026-03-24, 2026-03-25, 2026-03-26,
  2026-03-27, **[gap: 2026-03-28 → 2026-04-26]**, 2026-04-27, 2026-04-28,
  2026-04-29, 2026-04-30, 2026-05-01, 2026-05-04, 2026-05-05, 2026-05-06,
  2026-05-07, 2026-05-08, 2026-05-11, 2026-05-12, 2026-05-13, 2026-05-14,
  2026-05-15, 2026-05-18, 2026-05-19, 2026-05-20, 2026-05-21, 2026-05-22.
  **Gap flagged: yes** (one-month non-contiguous gap late-Mar → late-Apr). The
  local set + the MCP set agree exactly, so phase-5 self-history percentiles are
  computed over ~31 sessions, not a contiguous 2+ months — phase-5 must caveat
  any "X-day" window that straddles the gap.
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

(none — v1)

## Tool errors

(none — all green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = 2026-05-22 is the *latest* available date → all UW calls pass
     `date=2026-05-22`; treat this as "today" for the blueprint.
  2. There is a ~1-month data gap (2026-03-28 → 2026-04-26); any historical
     window longer than ~20 sessions straddles it — caveat percentiles.
  3. SNOW options tape is liquid; the `2026-06-26 125C` print (vol/OI 250,
     $1.23M premium) is an early hint of fresh upside positioning to chase down
     in phase 1/3.
- **Open questions:** Is the current flow unusual for SNOW or a normal busy day?
  → phase 0.5 resolves via cross-sectional + self-history rank.
