# Phase 0 — Intake

**Ticker:** RKT
**As-of date (requested):** 2026-05-20
**Effective UW data date:** 2026-05-19 (2026-05-20 not yet posted)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/RKT/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** (none — initial intake)

## Summary

Ticker RKT (Rocket Companies, mortgage origination & fintech) validated and
options activity confirmed. UW MCP reachable but the requested date
`2026-05-20` has no parquet posted yet — latest available across all UW data
types is `2026-05-19`. All downstream phases will pass `date=2026-05-19` to UW
tools and label findings as "T-1 snapshot" relative to the requested 2026-05-20
analysis date. Proceeding to phase 1.

## Key signals

- UW historical data is up-to-date through 2026-05-19 across darkpool,
  hotchains, OI, options, and screener feeds [TOOL:historical_available_dates].
- RKT shows live unusual volume on the 2026-06-18 12.5C with vol/OI=109 and
  $22.6k premium — confirms ticker has tradeable single-name options
  flow [FLOW:unusual_volume].

## Detailed findings

### Date resolution

- User requested as-of: `2026-05-20` (today, per `currentDate`).
- Latest UW data: `2026-05-19` across all 5 data types.
- **Effective query date passed to all UW tools downstream: `2026-05-19`.**
- Output directory keeps the requested `2026-05-20` label per skill convention
  (the directory is named after the analysis-of date, not the data date).

### UW availability check

```
historical_available_dates → returned full date arrays for:
  - darkpool   (latest 2026-05-19, oldest 2026-03-13)
  - hotchains  (latest 2026-05-19)
  - oi         (latest 2026-05-19)
  - options    (latest 2026-05-19)
  - screener   (latest 2026-05-19)
```

### Ticker sanity (RKT)

| Field | Value |
|------|-------|
| `underlying_symbol` | RKT |
| `option_type` | call |
| `strike` | 12.5 |
| `expiry` | 2026-06-18 |
| `total_premium` | $22,622 |
| `total_volume` | 218 |
| `open_interest` | 2 |
| `vol_oi_ratio` | 109× |
| `avg_iv` | 0.631 (63.1% IV) |

Vol/OI=109 on a $12.5 short-dated call is a clean opening-flow signal — these
are not roll/close trades. 63.1% avg IV is elevated for a large-cap financial
and consistent with the M&A-driven environment RKT has traded in since the
Mr. Cooper deal closed.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{}` | OK — 28 dates per feed, latest 2026-05-19 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: RKT, top_n: 1, date: 2026-05-20}` | ERROR — no parquet for 2026-05-20 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: RKT, top_n: 1, date: 2026-05-19}` | OK — 2026-06-18 12.5C, vol/OI 109 |

## Tool errors

`mcp__uw-pp__options_flow_unusual_volume` with `date=2026-05-20`:
```
Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options
```
Mitigation: shifted effective query date to 2026-05-19 (last available).

## Prior versions

(none — v1)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** N/A
- **Three things later phases should remember:**
  1. **All UW calls must use `date=2026-05-19`** — 2026-05-20 has no data yet.
  2. **RKT trades like a small-mid cap financial** (≈63% IV on near-dated
     strikes); position/IV-rank comparisons should benchmark against
     mortgage-finance peers (UWMC, COOP-merger context, GHLD), not large
     banks.
  3. **The Mr. Cooper acquisition closed in 2025**, so RKT today reflects
     combined Rocket + Mr. Cooper economics — phase-6 macro must check
     prevailing 30-yr mortgage rate as the primary fundamental driver.
- **Open questions:**
  - Is current flow net-bullish, net-bearish, or noise? → phase 1
  - Are institutions absorbing supply quietly? → phase 2
  - Is dealer GEX positive or negative? → phase 4
