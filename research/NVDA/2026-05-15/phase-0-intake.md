# Phase 0 — Intake

**Ticker:** NVDA
**As-of date:** 2026-05-15 (most recent UW trading day; run executed 2026-05-17, a Sunday)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NVDA/2026-05-15
**Version:** v1
**Generated:** 2026-05-17T17:00:48Z

## Summary

Ticker validated. Output directory created at version 1. UW MCP reachable —
`historical_available_dates` returned a normal date list across all 5 data
families (options, hotchains, oi, darkpool, screener). Latest available
trading day is 2026-05-15 across all families — that is the as-of date used
for every downstream phase.

Options activity smoke test on NVDA returned a row, so the chain is active.
Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: **2026-05-15**
- Latest available darkpool date: **2026-05-15**
- Latest available hotchains date: **2026-05-15**
- Latest available oi date: **2026-05-15**
- Latest available screener date: **2026-05-15**
- Data continuity gap noted: 2026-04-27 → 2026-03-27 (one-month gap) — may
  limit some 30d+ historical lookbacks. Long-window historical tools (90d
  cumulative premium) will use whatever they have.

## Ticker sanity

- Options activity (unusual_volume top 1): `NVDA 50P 2026-06-05` — single
  far-OTM put trade (premium $2.5k, vol/OI 2500). Chain is live; this single
  outlier doesn't carry directional meaning but confirms the tape is open.

## Tool calls

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__historical_available_dates` | none | 26 dates across all families, latest 2026-05-15 |
| `mcp__uw-pp__options_flow_unusual_volume` | `symbol=NVDA, top-n=1` | 1 row returned |

## Tool errors

None.

## Prior versions

None (this is v1).
