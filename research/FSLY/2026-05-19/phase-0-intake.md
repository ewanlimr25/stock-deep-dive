# Phase 0 — Intake

**Ticker:** FSLY
**As-of date:** 2026-05-19
**Effective data date:** 2026-05-18 (latest available across all UW data types)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/FSLY/2026-05-19
**Version:** v1
**Generated:** 2026-05-19T00:00:00Z

## Summary

Ticker FSLY (Fastly, Inc., NYSE-listed CDN/edge cloud) validated as a US
optionable equity. Output directory created clean. UW MCP reachable and all
five data categories (darkpool, hotchains, oi, options, screener) most-recent
date = `2026-05-18`. Because the requested as-of `2026-05-19` post-dates the
latest available trading-day bar, every downstream UW call will pass
`date=2026-05-18` and downstream phases will treat that as the *effective*
snapshot. Run proceeds.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: `2026-05-18`
- Latest available darkpool date: `2026-05-18`
- Latest available OI date: `2026-05-18`
- Latest available hotchains date: `2026-05-18`
- Latest available screener date: `2026-05-18`

## Ticker sanity

- Options activity (`options_flow_unusual_volume` top 1, date=2026-05-18):
  - `FSLY 2026-05-22 C 16.5`
  - total_volume = 153, open_interest = 4, vol_oi_ratio = 38.25
  - avg_iv = 1.0184 (≈101.8%), total_premium = $10,650, trade_count = 30
  - Headline read: small-notional but highly speculative short-dated upside
    flow already showing up at the surface — flags FSLY as a low-float / high-
    IV name worth a closer look. Real signal density will be determined by
    phase 1+.

## Versioning decision

This is v1 — directory was empty prior to this run. No "Prior versions"
section needed.

## Effective-date convention (used by all downstream phases)

- All UW tool calls will pass `date=2026-05-18`.
- All `historical_*` ranges anchor right-edge to `2026-05-18`.
- "As-of 2026-05-19" appears only in headers; "Effective: 2026-05-18" is the
  trading-day snapshot the analysis is built on.

## Prior versions

(none — v1)

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. FSLY trades with elevated single-name IV (>100% on near-dated calls).
     Premium-buying strategies will be expensive; premium-selling will be
     more attractive *if* directional bias survives the rest of the workup.
  2. Open interest on near-dated strikes is extremely thin (OI = 4 on the
     headline call). Liquidity and pin-risk math in phase 3/4 must account
     for this — fills may be poor.
  3. Effective data snapshot is 2026-05-18, one calendar day behind the
     requested as-of. Any "today's flow" language in later phases must
     resolve to 2026-05-18 close.
- **Open questions:**
  - Is the short-dated speculative buying part of a larger pattern (sweeps,
    multileg, sector rotation), or one-off retail? → phase 1.
  - Is FSLY actually thin across the chain or just at this strike? → phase 1
    (DTE/expiry heatmap) + phase 3 (OI map).
