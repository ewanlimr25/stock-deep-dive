# Phase 0 — Intake

**Ticker:** SYM (Symbotic Inc., NASDAQ)
**As-of date (requested):** 2026-05-22
**As-of date (effective):** 2026-05-21 (latest available UW parquet; 2026-05-22 has no data — likely current trading day not yet closed/loaded)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SYM/2026-05-22
**Version:** v1
**Generated:** 2026-05-22T15:03Z

## Summary

Ticker SYM validated as a US-listed equity (Symbotic Inc.). Output directory
created. UW MCP reachable. Requested as-of date 2026-05-22 has no parquet data,
so all downstream UW tool calls will use `date=2026-05-21` (the most recent
available trading session). Ticker has live options activity (puts trading
~5.7x OI on the 2026-06-05 39 strike), so the deep dive can proceed.

## UW availability

- `historical_available_dates`: ok
- Latest available darkpool date: **2026-05-21**
- Latest available options date: **2026-05-21**
- Latest available OI date: **2026-05-21**
- Latest available hotchains date: **2026-05-21**
- Latest available screener date: **2026-05-21**
- Date gap noted: 2026-03-28 → 2026-04-26 is missing from the dataset (likely
  a feed outage); downstream phases that walk historical ranges should be
  aware that ~4 weeks in late March / late April 2026 are unavailable.

## Ticker sanity

- Options activity (unusual_volume top 1 on 2026-05-21):
  - `SYM 2026-06-05 P39` — vol 120, OI 21, vol/OI 5.71, avg IV 82.99%, total
    premium $2,250. New put position opening on a near-dated 39 strike. Avg
    IV ~83% suggests SYM is a high-vol name (likely a 2-3 vol regime stock).
- Conclusion: options are tradeable but not deeply liquid at the single-strike
  level. Expect downstream "low premium" / "thin chain" caveats relative to
  mega-caps.

## Phase plan (downstream as-of override)

All `mcp__uw-pp__*` tool calls in phases 1–7 will pass `date=2026-05-21`
unless the tool specifies a different (e.g., historical lookback) date.

## Prior versions

None (v1).

## Tool errors

- `options_flow_unusual_volume(symbol=SYM, top-n=1, date=2026-05-22)` →
  `Error: no parquet file for 2026-05-22 in /Users/ewan/Documents/Stocks/All Options`
  → resolved by rolling to 2026-05-21.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective as-of is **2026-05-21**, not 2026-05-22.
  2. SYM is a high-IV name (~83% on near-dated puts) — IV percentiles and
     vol structure will be a key part of the thesis.
  3. Data gap 2026-03-28 → 2026-04-26 — historical lookbacks must skip or
     flag this window.
- **Open questions:** What is the current spot price for SYM? What is the
  recent earnings cadence (next print date)? Both will be answered in
  phase 1 and phase 6.
