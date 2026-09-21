# Phase 0 — Intake

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/RDDT/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T00:00:00Z

## Summary

Ticker RDDT (Reddit, Inc., NYSE) validated as a US-listed equity with active,
liquid options. Output directory created fresh (no prior run). UW MCP reachable
and the as-of date 2026-05-22 is the latest available date across all five data
types (options, darkpool, oi, hotchains, screener). Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-22 (== as-of, good)
- Latest available darkpool date: 2026-05-22
- **Non-contiguous gap:** data jumps from 2026-03-27 to 2026-04-27 (the month
  of April 2026 is absent across every dataset). Phase 5 (historical) and phase
  0.5 (self-history) must treat the ~21-session local window as two blocks:
  late-Mar (2026-03-13 → 2026-03-27) and late-Apr→May (2026-04-27 → 2026-05-22).

## Ticker sanity

- Options activity (unusual_volume top 1): `RDDT 2026-05-29 142C` — total_volume
  763 vs open_interest 5 → **vol/OI 152.6**, total_premium $394,474, avg_iv 0.598.
  Confirms a live, actively-traded options surface with fresh positioning at the
  142 strike one week out. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (31 sessions): 2026-03-13, 03-16, 03-17, 03-18, 03-19,
  03-20, 03-23, 03-24, 03-25, 03-26, 03-27, **[gap]**, 04-27, 04-28, 04-29,
  04-30, 05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14,
  05-15, 05-18, 05-19, 05-20, 05-21, 05-22 (gap flagged: **yes** — April missing)
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

None — this is v1.

## Tool errors

None — all green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-05-22 is the latest local date; never call live data.
  2. There is a one-month data gap (April 2026 absent) — historical/self-history
     percentiles draw from ~31 sessions in two blocks, not a contiguous quarter.
  3. RDDT options are liquid; fresh vol/OI 152.6 at the 5/29 142C signals active
     near-dated positioning to chase down in phase 1.
- **Open questions:** What is the current spot, the recent trend, and is RDDT's
  flow unusual vs its own history and its sector? (→ phase 0.5)
