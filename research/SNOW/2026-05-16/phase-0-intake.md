# Phase 0 — Intake

**Ticker:** SNOW
**As-of date:** 2026-05-16
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SNOW/2026-05-16
**Version:** v1
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** (none — phase 0)

## Summary

SNOW (Snowflake Inc.) intake validated. Output directory created clean (no prior runs). UW MCP reachable; latest data date is 2026-05-15 (Friday). The user-supplied as-of date 2026-05-16 is a Saturday, so every downstream UW tool call will use `date=2026-05-15` (the most recent business day at-or-before the as-of). The directory name remains `2026-05-16` per user spec. Options activity check returned a meaningful unusual-volume hit (SNOW Jun-26-26 145C, vol/OI 314.7, $2.1M premium), so proceeding to phase 1.

## Key signals

- UW MCP available; latest snapshot 2026-05-15 across darkpool, hotchains, oi, options, screener [INTAKE:historical_available_dates].
- SNOW options market is live and trading unusually — top vol/OI = 314.67 on 145C Jun-26-26 [FLOW:options_flow_unusual_volume].
- Effective query date = **2026-05-15** for all downstream tools.

## Detailed findings

### UW availability

`historical_available_dates` returned identical date series across all data types. The five most-recent business days available are:

| Rank | Date |
|------|------|
| 1 | 2026-05-15 |
| 2 | 2026-05-14 |
| 3 | 2026-05-13 |
| 4 | 2026-05-12 |
| 5 | 2026-05-11 |

Note: there is a visible gap in the available-dates series between 2026-04-27 and 2026-03-27 (no data for 2026-04-28 through 2026-05-03 backwards into March-end). This is a server-side data archive characteristic; recent dates are dense.

### Ticker sanity

`options_flow_unusual_volume symbol=SNOW top_n=1 date=2026-05-15` returned:

| Field | Value |
|-------|-------|
| underlying_symbol | SNOW |
| option_type | call |
| strike | 145 |
| expiry | 2026-06-26 |
| total_volume | 944 |
| open_interest | 3 |
| vol_oi_ratio | 314.67 |
| total_premium | $2,104,220 |
| trade_count | 11 |
| avg_iv | 0.808 (80.8%) |

This is a clear new-position opening on a $145 strike call expiring ~6 weeks out, suggesting at least one directional buyer is paying up for upside exposure. Phase 1 will validate whether this is a single block or distributed.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{compact: true}` | latest=2026-05-15 across all data types |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: SNOW, top_n: 1, date: 2026-05-15, compact: true}` | 145C Jun-26-26, vol/OI=314.67, premium=$2.10M |

## Tool errors

None.

## Prior versions

None — this is v1.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only; the one observed contract is bullish but not yet contextualized).
- **Conviction:** N/A (intake).
- **Three things later phases should remember:**
  1. All UW calls must use `date=2026-05-15`, not `date=2026-05-16` (no data for Saturday).
  2. There is at least one meaningful upside call buyer at $145 strike expiring 2026-06-26 — phase 1 should follow this thread.
  3. Avg IV on the unusual-volume hit was 80.8% — anchor for IV regime check in phase 5.
- **Open questions:** Is the unusual-volume buyer a sweep / floor / institutional block? Is there confirming dark-pool flow? Spot price on 2026-05-15 (needed for OTM-ness math) — must extract from phase 1 / 2.
