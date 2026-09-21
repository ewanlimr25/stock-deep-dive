# Phase 0 — Intake

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15 (2026-05-18 is a Monday; latest UW data is Fri 2026-05-15)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/LRCX/2026-05-18/
**Version:** v1
**Generated:** 2026-05-18T00:00:00Z

## Summary

Ticker validated (LRCX = Lam Research Corp, US-listed semicap equipment maker).
Output directory created. UW MCP reachable. Latest available data is Fri
2026-05-15 — that date will be used for all `date=` parameters downstream.
LRCX has live options flow (unusual put volume on Jul-17 170P, vol/OI = 251.5).
Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-15
- Latest available darkpool date: 2026-05-15
- Latest available OI date: 2026-05-15
- Latest available hot-chains date: 2026-05-15
- Latest available screener date: 2026-05-15

Note: UW data has a coverage gap between 2026-03-27 and 2026-04-27 (roughly 1
month). Historical lookbacks that cross this window should be flagged.

## Ticker sanity

- Options activity (unusual_volume top 1):
  `LRCX 2026-07-17 170P` — vol 1006, OI 4, vol/OI 251.5, prem $112.8k, avg IV 72.8%.
  Tape clearly active.

## Run metadata

- Skill: stock-deep-dive
- Phase-0 file: phase-0-intake.md
- Downstream phases will read `--as-of 2026-05-18` as a request label but use
  `date=2026-05-15` in every UW tool call. Each phase MD will state both.

## Prior versions

(none — v1)

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** neutral (data availability check only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Use `date=2026-05-15` for every UW call. Do NOT pass `2026-05-18`.
  2. There is a ~1-month UW data gap (03-27 → 04-27); any historical/trend
     window that spans it is partially blind.
  3. First flow read shows aggressive **put** opening (251x vol/OI) on a
     Jul-17 170P. Phase 1 must investigate whether that is a hedge, a
     directional bearish bet, or part of a spread.
- **Open questions:** is LRCX in earnings window? When is next earnings?
  (Phase 5/6 to confirm.)
