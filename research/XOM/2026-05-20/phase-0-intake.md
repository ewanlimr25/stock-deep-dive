# Phase 0 — Intake

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18 (latest available across all UW data types)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/XOM/2026-05-20
**Version:** v1
**Generated:** 2026-05-19T00:00:00Z

## Summary

Ticker validated (XOM = Exxon Mobil, NYSE-listed, deep options market). Output
directory created at the user-requested as-of date `2026-05-20`. UW MCP smoke
test passed: `historical_available_dates` returned five non-empty data type
arrays and `options_flow_unusual_volume` returned a non-empty result for XOM.

Important data-date caveat: the most recent date in every UW data type
(darkpool, hotchains, oi, options, screener) is **2026-05-18**. The user-supplied
as-of `2026-05-20` is one trading day forward of the latest ingested data;
no panel for 2026-05-19 or 2026-05-20 yet exists. **All downstream phases will
pass `date=2026-05-18`** to UW tools and explicitly label this as the "effective
data anchor." Where intraday or post-close behavior for 2026-05-19 / 2026-05-20
matters (e.g. macro headlines, oil-tape moves), phase 6 will use WebSearch to
patch the gap.

Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-18
- Latest available darkpool date: 2026-05-18
- Latest available OI date: 2026-05-18
- Latest available hotchains date: 2026-05-18
- Latest available screener date: 2026-05-18
- Date-coverage caveat: there is a visible gap in mid-Apr 2026 (2026-04-27 →
  2026-03-27) across all data types. This may affect any 30-day rolling
  metrics in phase 5 (historical). Phases that touch >30d lookbacks should
  treat the early-April window as "missing" rather than "zero."

## Ticker sanity

- Options activity (`options_flow_unusual_volume` top 1):
  - `XOM 2026-08-21 185C` — vol 171, OI 6, vol/OI 28.5, premium $55,968,
    avg IV 32.82%
  - Confirms XOM has live, dated options flow on 2026-05-18.

## Prior versions

None — first run for this `<SYMBOL>/<DATE>` directory.

## Tool errors

None.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | 5 data types × 27 dates each, latest 2026-05-18 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: XOM, top-n: 1, date: 2026-05-18}` | 1 result: 2026-08-21 185C, vol/OI 28.5 |

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective data anchor is **2026-05-18**, not the user-supplied 2026-05-20 —
     all `date=` args go to 2026-05-18.
  2. UW date coverage has a hole in early-to-mid April 2026 (2026-04-26 →
     2026-03-28 are missing). Bound `30d` historical windows by available
     dates, not by calendar.
  3. XOM smoke-test contract `2026-08-21 185C` (Aug expiry, ~3M out) showed
     vol/OI 28.5× at 32.8% IV — a useful tape sample but DTE-heavy contracts
     should not anchor the flow read in phase 1 by themselves.
- **Open questions:**
  - Is the 2026-05-19/2026-05-20 gap due to a market holiday, or simply
    pending ingestion? Phase 6 should WebSearch a US market calendar before
    drawing macro conclusions about "fresh" 2026-05-20 news.
