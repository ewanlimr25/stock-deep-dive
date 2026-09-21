# Phase 0 — Intake

**Ticker:** ADBE
**As-of date (effective):** 2026-05-19
**As-of date (requested):** 2026-05-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ADBE/2026-05-19
**Version:** v1
**Generated:** 2026-05-19T00:00:00Z

## Summary

Ticker validated (ADBE, NASDAQ, Adobe Inc.). Output directory created. UW MCP
reachable across all data types (darkpool, hotchains, oi, options, screener).
User-requested as-of date `2026-05-20` has no parquet file in the UW data store
yet, so the run falls back to the **latest available trading date `2026-05-19`**
and every downstream phase will pass `date=2026-05-19` to UW tools.
Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: **2026-05-19**
- Latest available darkpool date: **2026-05-19**
- Latest available OI date: **2026-05-19**
- Latest available hotchains date: **2026-05-19**
- Latest available screener date: **2026-05-19**

Recent trading dates loaded (most-recent first): 2026-05-19, 2026-05-18,
2026-05-15, 2026-05-14, 2026-05-13, 2026-05-12, 2026-05-11, 2026-05-08,
2026-05-07, 2026-05-06, 2026-05-05, 2026-05-04, 2026-05-01, 2026-04-30,
2026-04-29, 2026-04-28, 2026-04-27. There is a ~one-month gap before
2026-03-27 — historical lookbacks deeper than ~17 sessions may have sparse data.

## Ticker sanity

- Options activity (unusual_volume top 1):
  `ADBE 2026-05-22 $262.5 PUT` — vol_oi_ratio **65.5**, volume 131, OI 2,
  total_premium $88,957, avg_iv 0.5585. Confirms an active, listed options
  chain with new-position opening flow at the 262.5 put strike for the next
  weekly expiry. (Source parquet: `bot-eod-report-2026-05-19.parquet`.)

## Date-handling decision

Because the user requested `--as-of 2026-05-20` but the latest UW data is
`2026-05-19`, this run treats the **effective as-of date** as `2026-05-19`.
Rationale: the skill forbids live data when an as-of date is supplied; the
nearest deterministic snapshot is the most recent EOD parquet. All phase MDs
will state the effective date in their header and every UW call will pass
`date=2026-05-19` explicitly to keep the snapshot frozen.

## Prior versions

None — this is a v1 run.

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume(symbol=ADBE, top-n=1, date=2026-05-20)`
  → `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All
  Options`. Resolved by falling back to `date=2026-05-19`.

## Verdict for downstream phases

- **Bias from this phase:** neutral (operational only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective as-of = **2026-05-19**, not the requested 2026-05-20.
  2. Historical data is dense from 2026-04-27 → 2026-05-19; deeper history
     exists only back to ~2026-03-13 with a one-month gap — keep lookbacks
     ≤ ~30 sessions to stay on solid ground.
  3. The very first unusual-volume hit was a near-dated **262.5 put** with a
     65× vol/OI ratio and 56% IV — a downside-skew data point to confirm or
     refute in phase 1.
- **Open questions:** What is spot? What is implied move into the next event?
  (Resolved in phase 1.)
