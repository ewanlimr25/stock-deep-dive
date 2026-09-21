# Phase 0 — Intake

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ENPH/2026-05-22
**Version:** v1 (no prior run in this dir)
**Generated:** 2026-05-25T22:43:20Z

## Summary

Ticker validated (ENPH — Enphase Energy, US-listed equity, optionable). Output
directory created empty (v1 run). UW MCP reachable — `historical_available_dates`
returns all five datasets through 2026-05-22, matching the as-of date. ENPH has
active options flow. **All downstream UW calls will pass `date=2026-05-22`** (as-of
supplied → no live data). Proceeding to phase 0.5.

## UW availability

- `historical_available_dates`: **ok** — all 5 datasets (options, darkpool, oi,
  hotchains, screener) present.
- Latest available options date: **2026-05-22** (= as-of) ✓
- Latest available darkpool date: **2026-05-22** (= as-of) ✓
- Latest available oi date: **2026-05-22** ✓
- **Known non-contiguous gap confirmed in MCP date list too:** 2026-03-27 → 2026-04-27
  (the 2026-03-28→04-24 hole). Any `historical_*` lookback that appears smooth across
  late-March/April must be cross-checked against this gap (phase-5 caveat).

## Ticker sanity

- Options activity (`unusual_volume` top 1, date=2026-05-22):
  **ENPH 2026-05-29 $57 PUT** — vol 445 / OI 15 (vol/OI 29.7×), premium $36.2K,
  **avg_iv 0.937 (≈94%)**. Not empty → ticker is liquid. The near-term ~94% IV is a
  flag to carry forward: ENPH is a high-vol name; phase-4/7c must judge whether IV is
  rich vs its own history (VRP).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (31 sessions): 2026-03-13, 03-16, 03-17, 03-18, 03-19,
  03-20, 03-23, 03-24, 03-25, 03-26, 03-27, **[gap]**, 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18,
  05-19, 05-20, 05-21, 05-22. **Gap flagged: yes** (2026-03-28→04-24, 21-session hole).
- As-of 2026-05-22 snapshot present → DuckDB escape hatch usable for this run.
- Note: MCP is primary; local DuckDB is opt-in for the three cuts the MCP can't
  express (`lib/duckdb-cuts.md`), tagged `[… DUCKDB]`.

## Prior versions

None (v1).

## Tool errors

None — all green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = 2026-05-22; pass `date=2026-05-22` to **every** UW call.
  2. ENPH near-term IV ≈ 94% — a high-vol name; structure must respect VRP and skew.
  3. Local self-history window is **non-contiguous** (21-session March/April hole) —
     state true session counts, never annualize across the gap.
- **Open questions:** Is today's flow unusual for ENPH, or a normal busy day?
  (→ phase 0.5 context.)
