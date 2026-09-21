# Phase 0 — Intake

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19 (latest available across all UW datasets)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SOFI/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z

## Summary

Ticker SOFI (SoFi Technologies, Inc., NASDAQ) validated as a US-listed equity with active
options markets. Output directory created at the requested 2026-05-20 path. UW MCP
server is reachable; however, no parquet exists yet for the requested as-of date
2026-05-20 — the latest available date across all UW data types (options, oi, darkpool,
hotchains, screener) is **2026-05-19**. All downstream phases will pass
`date=2026-05-19` to UW tools and flag this one-trading-day gap in their citations.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: **2026-05-19**
- Latest available darkpool date: **2026-05-19**
- Latest available oi date: **2026-05-19**
- Latest available hotchains date: **2026-05-19**
- Latest available screener date: **2026-05-19**
- Coverage gap noted: 2026-04-02 through 2026-04-24 absent (likely data-feed gap;
  reduces availability of trailing-30d historical comparisons in phase 5).

## Ticker sanity

- `options_flow_unusual_volume` (top 1, date=2026-05-19):
  - **SOFI 2026-06-05 12.5C** — vol 336, OI 2, vol/OI 168×, premium $96,742,
    avg IV 65.04%.
- Options activity: healthy. Single-name optionable equity with meaningful
  unusual-volume signal even at the top-1 contract level.

## Prior versions

None — v1.

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume(symbol=SOFI, date=2026-05-20, top-n=1)`
  → `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options`.
  Resolved by falling back to effective data date 2026-05-19 (latest available).

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a.
- **Three things later phases should remember:**
  1. All UW calls must use `date=2026-05-19` (not 2026-05-20).
  2. SOFI shows real near-dated speculative call interest (12.5C, ~17d to expiry,
     168× vol/OI) — phase 1 must investigate whether this is broad or one-off.
  3. Coverage gap 2026-04-02 → 2026-04-24 limits trailing-30d historical context
     in phase 5; use trailing-60d windows where possible.
- **Open questions:** what is the current spot price, sector context (consumer
  fintech vs. neobank vs. credit), and is there a known catalyst (e.g. June FOMC,
  earnings cadence) in the next 30 days?
