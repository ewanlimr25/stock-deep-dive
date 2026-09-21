# Phase 0 — Intake

**Ticker:** NVO (Novo Nordisk A/S — ADR, NYSE)
**As-of date:** 2026-05-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NVO/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00-04:00
**Upstream phases cited:** (none — this is the root phase)

## Summary

Ticker validated: NVO is a US-listed ADR with active options. UW MCP is
reachable with full data coverage through the requested as-of date
(2026-05-20). Output directory created clean. Smoke checks reveal an
immediately notable signal — a $37 put expiring 2026-06-18 with vol/OI = 88.5×
— flagged for phase 1 to characterize.

## Key signals

- Latest UW data date across all datatypes = 2026-05-20 [intake:historical_available_dates]
- NVO options confirmed active; unusual put activity already visible on the smoke test [FLOW:unusual_volume]
- Run is v1 — no prior research artifacts in this directory

## Detailed findings

### UW availability

| Datatype | Latest date | Status |
|----------|-------------|--------|
| darkpool | 2026-05-20 | ok |
| hotchains | 2026-05-20 | ok |
| oi | 2026-05-20 | ok |
| options | 2026-05-20 | ok |
| screener | 2026-05-20 | ok |

All UW datatypes have the as-of date in coverage. No fallbacks needed.

### Ticker sanity

`options_flow_unusual_volume(symbol=NVO, date=2026-05-20, top_n=1)` returned 1
row. Top unusual contract:

| Field | Value |
|-------|-------|
| option_type | put |
| strike | 37.00 |
| expiry | 2026-06-18 |
| open_interest | 34 |
| total_volume | 3,010 |
| vol/OI | 88.5× |
| total_premium | $57,130 |
| avg_iv | 0.461 (46.1%) |
| trade_count | 2 |

Two trades drove all 3,010 contracts — a single block-sized opening flow on a
deep OTM short-dated put. Phase 1 must determine whether this was bought or
sold, retail or institutional, and whether premium was paid at ask (bearish
positioning) or hit on bid (yield-harvesting put sale).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{compact: true}` | All 5 datatypes cover 2026-05-20 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: NVO, date: 2026-05-20, top_n: 1}` | 1 row: $37 P 06/18, vol/OI 88.5× |

## Tool errors

None.

## Prior versions

None — this is v1.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of date is 2026-05-20 — every UW call below must include `date=2026-05-20`.
  2. A $37 put 06/18/2026 with vol/OI 88.5× and only 2 trades is the first
     anomaly to disambiguate in phase 1 (open vs close, side of book).
  3. NVO trades as an ADR — dark pool prints and option volumes can be
     thinner than US-domiciled peers; do not over-weight low-volume signals
     in phase 2.
- **Open questions:** What is the spot price for NVO on 2026-05-20, the IV
  rank, and the recent realized vs implied skew? Phase 1 and Phase 4 own those.
