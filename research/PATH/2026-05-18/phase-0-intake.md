# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-18 (requested) — effective data date **2026-05-15** (latest available)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-05-18
**Version:** v1
**Generated:** 2026-05-18T00:00:00-04:00

## Summary

Ticker PATH validated. UW MCP reachable across all data families (options,
darkpool, OI, hotchains, screener, historical). Requested as-of date is
2026-05-18 (Monday) but the latest available data snapshot is 2026-05-15
(prior Friday close). All downstream phases will pass `date=2026-05-15` to
UW tools. Options activity confirmed — PATH `2026-07-17 $15C` traded 666
contracts on OI of 4 (vol/OI 166.5×), so the name is liquid enough to
deep-dive.

## UW availability

- `historical_available_dates`: ok
- Latest available **options** date: 2026-05-15
- Latest available **darkpool** date: 2026-05-15
- Latest available **OI** date: 2026-05-15
- Latest available **hotchains** date: 2026-05-15
- Latest available **screener** date: 2026-05-15
- Date gap detected: no data between **2026-03-27** and **2026-04-27** (one
  full month missing in the historical archive). Phase 5 must work around
  this when looking at multi-month trends — anchor to the 2026-04-27 →
  2026-05-15 window or accept a March-only earlier window.

## Ticker sanity

- Options activity (unusual_volume top 1):
  - Contract: `PATH 2026-07-17 $15 Call`
  - Volume: 666 / OI: 4 / vol-OI ratio: **166.5×**
  - Total premium: **$22,063**
  - Avg IV on contract: 88.2%
  - Trade count: 23
- Verdict: small-cap-style options activity (premium << $1M on the headline
  contract). Likely "thin" overall — phase 1 must check broader flow before
  assigning conviction.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | All data families ok; latest 2026-05-15 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: PATH, top-n: 1, date: 2026-05-15}` | 1 contract, 166.5× vol/OI, $22k premium |

## Prior versions

(none — v1)

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Effective data date is **2026-05-15**, NOT 2026-05-18 — every UW call
     must pass `date=2026-05-15` to keep the snapshot consistent.
  2. PATH is a **small-cap** software name (UiPath, ~$3-5B mkt cap range
     historically) — premium figures will look small vs mega-caps. Calibrate
     conviction by **vol/OI ratios and relative sizing**, not absolute $.
  3. There is a **March-27 → April-27 archive gap**. Historical trend phase
     (5) must explicitly acknowledge this and use the 2026-04-27 →
     2026-05-15 window for "recent month" comparisons.
- **Open questions:** Is the May-15 single-contract spike a one-off lottery
  ticket or part of a broader call-side accumulation pattern? Phase 1
  must resolve.
