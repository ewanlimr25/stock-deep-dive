# Phase 0 — Intake

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/GRAB/2026-05-21
**Version:** v1
**Generated:** 2026-05-21T00:00:00Z

## Summary

Ticker GRAB validated (Grab Holdings Ltd, NASDAQ). Output directory created
fresh — no prior runs found. UW MCP reachable and 2026-05-21 is the latest
available date across all data families (darkpool / hotchains / oi / options /
screener). Options activity exists but is THIN: at default `min_vol_oi_ratio=3`,
zero contracts returned; at `min_vol_oi_ratio=1, min_volume=50` only one
contract surfaced (2026-06-18 $3.50 call, vol=1499, OI=825). Proceeding to
phase 1 with a "low-liquidity options name" caveat that will be carried
through phase 9 sizing.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-21
- Latest available darkpool date: 2026-05-21
- Latest available OI date: 2026-05-21
- Latest available hotchains date: 2026-05-21
- Latest available screener date: 2026-05-21

## Ticker sanity

- Options activity (unusual_volume top 1 @ min_vol_oi_ratio=3): empty
- Options activity (unusual_volume top 1 @ min_vol_oi_ratio=1, min_vol=50):
  GRAB 2026-06-18 $3.50C, vol=1499, OI=825, premium=$28,764, avg_iv=47.5%
- Verdict: GRAB has live but THIN options activity — downstream phases must
  expect small premium magnitudes and treat single-print outliers carefully.

## Prior versions

(none — v1)

## Tool errors

(none)

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | (none) | 30 dates across all families, latest 2026-05-21 |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=GRAB, date=2026-05-21, top_n=1, min_vol_oi_ratio=3 | empty |
| `mcp__uw-pp__options_flow_unusual_volume` | symbol=GRAB, date=2026-05-21, top_n=5, min_vol_oi_ratio=1, min_volume=50 | 1 contract: Jun-18 $3.50C |

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** N/A
- **Three things later phases should remember:**
  1. GRAB is a low-priced (sub-$10) name; option strikes are quoted in $0.50
     increments — phase-3/4 strike clusters will look tight in absolute terms.
  2. Options volume is thin; default UW thresholds (`min_vol_oi_ratio=3`,
     `min_premium=100000`) will return empty for many tools. Lower thresholds
     when needed and note that signal magnitudes are SMALL.
  3. As-of date 2026-05-21 — every downstream UW call MUST pass
     `date=2026-05-21` to avoid leaking forward-looking data.
- **Open questions:** does the dark pool tape (institutional accumulation
  often happens off-exchange for sub-$10 names) show meaningfully more
  activity than the options tape?
