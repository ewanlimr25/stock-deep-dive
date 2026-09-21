# Phase 0 — Intake

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/AAPL/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** (none — root phase)

## Summary

Ticker AAPL validated as a US-listed equity with deep options activity. Output
directory created. Unusual Whales MCP reachable and 2026-05-20 confirmed as the
latest available date across all five data types (options, hotchains, OI,
darkpool, screener). Proceeding to phase 1.

## Key signals

- UW MCP fully reachable; no degraded mode required.
- AAPL options chain alive — top unusual-volume contract on 2026-05-20 is the
  **AAPL 282.5C 27-May-2026** with vol/OI = 225.75 and $3.17M premium on 1,806
  contracts vs OI = 8 [FLOW:unusual_volume]. Brand-new short-dated call
  position opening — flagged for phase 1 to investigate further.
- As-of date 2026-05-20 = latest UW snapshot date; no stale-data risk.

## Detailed findings

### UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-20
- Latest available darkpool date: 2026-05-20
- Latest available OI date: 2026-05-20
- Latest available hotchains date: 2026-05-20
- Latest available screener date: 2026-05-20

### Ticker sanity

| Field | Value |
|-------|-------|
| `underlying_symbol` | AAPL |
| Top unusual-volume contract | 282.5 call, expiry 2026-05-27 |
| `total_volume` | 1,806 |
| `open_interest` | 8 |
| `vol_oi_ratio` | 225.75 |
| `total_premium` | $3,169,000 |
| `avg_iv` | 34.71% |
| `trade_count` | 51 |

Reads as a freshly-opened, short-dated upside speculation. Downstream phases
should treat 282.5 as a key reference strike and watch the 5/27 expiry for
gamma effects.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | 5 data types, latest = 2026-05-20 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: AAPL, top-n: 1, date: 2026-05-20}` | 282.5C 5/27 — vol/OI 225.75, $3.17M premium |

## Tool errors

None.

## Prior versions

None (v1).

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no thesis yet)
- **Conviction:** 1
- **Three things later phases should remember:**
  1. As-of = 2026-05-20; pass `date=2026-05-20` to every UW call.
  2. 282.5C 5/27 is a fresh, large speculative print — investigate provenance
     in phase 1 (sweep vs block, bid/ask side).
  3. All five UW datasets are fresh; no fallback paths required.
- **Open questions:** What is AAPL's spot price on 2026-05-20? (needed to
  contextualize the 282.5 strike — phase 1 will pull it from flow context.)
