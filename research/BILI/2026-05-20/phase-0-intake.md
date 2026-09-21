# Phase 0 — Intake

**Ticker:** BILI
**As-of date:** 2026-05-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BILI/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T09:30:00-04:00

## Summary

Ticker BILI (Bilibili Inc., NASDAQ ADR) validated. Output directory created.
UW MCP reachable and returns data through 2026-05-19. Because today (2026-05-20)
is not yet present in the UW dataset (last EOD parquet is `bot-eod-report-2026-05-19.parquet`),
all subsequent phases will pass `date=2026-05-19` and treat the as-of date as a
pre-open snapshot for the 2026-05-20 session. Unusual-volume smoke-test
returned a near-dated (2026-05-22 expiry) $18.5 put contract with vol/OI 5.08x,
confirming live options activity. Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-19
- Latest available darkpool date: 2026-05-19
- Latest available OI date: 2026-05-19
- Latest available hot-chains date: 2026-05-19
- Latest available screener date: 2026-05-19

Note: the available-dates list has a 1-month gap (2026-03-27 to 2026-04-27)
which constrains some `historical_*` lookbacks in phase 5.

## Ticker sanity

- Options activity (unusual_volume top 1, date=2026-05-19):
  - Contract: BILI 2026-05-22 $18.5 PUT
  - Volume: 604 / OI: 119 / vol-OI ratio: 5.08
  - Avg IV: 79.0%
  - Premium: $14,346
- Interpretation: BILI trades liquid weeklies. Near-dated put activity is
  the first flow datapoint and will be re-examined in phase 1.

## Prior versions

None (v1).

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective data date = 2026-05-19 (one trading day before as-of).
  2. There is a March 30 → April 24 historical gap; phase 5 lookbacks must
     account for it (use longest unbroken window).
  3. Initial put activity at the $18.5 strike (very near-dated, 2026-05-22)
     suggests the spot is likely in the high-teens / low-20s. Phase 1 should
     verify with sweeps & top premium trades.
- **Open questions:**
  - What is BILI's spot price as of 2026-05-19 close? (will be sourced from
    UW flow records and dark-pool ticker summary in phase 1/2.)
  - Is there an upcoming earnings catalyst inside the May/June expiry stack?
    (phase 7 `insights_earnings_play` will confirm.)
