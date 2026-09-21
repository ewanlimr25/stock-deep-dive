# Phase 0 — Intake

**Ticker:** RDDT
**As-of date (requested):** 2026-05-20
**Effective data anchor:** 2026-05-18 (latest UW parquet across all data types)
**Output dir:** `/Users/ewan/Development/stock-deep-dive/research/RDDT/2026-05-20/`
**Version:** v1
**Generated:** 2026-05-19T00:00:00-04:00

## Summary

RDDT ticker validated (US-listed equity, has active options chain).
Output directory created. UW MCP reachable; `historical_available_dates` returned
27 trading days across darkpool, hotchains, oi, options, and screener feeds.
The user-supplied as-of date (2026-05-20) precedes the latest available UW
parquet (2026-05-18) so all downstream tool calls will use
`date=2026-05-18`. This is documented under Tool errors. Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available **options** date: 2026-05-18
- Latest available **darkpool** date: 2026-05-18
- Latest available **OI** date: 2026-05-18
- Latest available **hotchains** date: 2026-05-18
- Latest available **screener** date: 2026-05-18

Earliest dates in window: 2026-03-13. There is a visible gap between
2026-03-27 and 2026-04-27 (one month) — every UW history-style call must
treat 2026-04-27 as the start of contiguous recent data.

## Ticker sanity

- `options_flow_unusual_volume` (date=2026-05-18, top_n=1):
  RDDT 2026-11-20 105P, vol 141, OI 1, vol/OI 141, premium $107,811,
  avg IV 71.7%. Confirms RDDT has tradeable options with at least some
  fresh-position activity.

## Prior versions

None — this is v1.

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume {symbol: RDDT, top_n: 1, date: 2026-05-20}`
  → `no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options`.
  Decision: fall back to `date=2026-05-18` for all UW calls. Output directory
  name preserves the user-requested 2026-05-20 anchor.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Use `date=2026-05-18` for every UW tool call.
  2. There is a one-month gap (2026-03-27 → 2026-04-27) in the UW history;
     any rolling-window calc must avoid spanning the gap silently.
  3. RDDT options show fresh-position activity well out the curve
     (Nov-2026 105P vol/OI=141) — flag this in phase 1 / 3.
- **Open questions:** what is RDDT's last-print price and is there an upcoming
  catalyst (earnings) inside the 6-month options window? Phase 6 to confirm.
