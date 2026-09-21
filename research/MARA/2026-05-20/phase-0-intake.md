# Phase 0 — Intake

**Ticker:** MARA
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19 (latest UW parquet available; 2026-05-20 not yet in archive — flagged below)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00-04:00
**Upstream phases cited:** none (root phase)

## Summary

Ticker `MARA` (Mara Holdings, Inc. — bitcoin miner, US-listed NASDAQ) validated.
Output directory created. UW MCP archive reachable; latest parquet date is
`2026-05-19`, so all downstream UW calls in this run will pin `date=2026-05-19`
even though the user-requested as-of is `2026-05-20`. This is a one-business-day
gap (overnight; 2026-05-20 EOD parquet not yet generated at orchestration
time). Run proceeds with v1 artifacts.

## Key signals

- UW archive latest: `2026-05-19` across all data types (darkpool, hotchains, oi, options, screener) [INTAKE:historical_available_dates]
- MARA has live options activity — top unusual-volume contract is the 2026-06-18 14.5C with vol/OI 15.9x on 223 contracts [INTAKE:options_flow_unusual_volume]
- IV on that contract is ~89% — consistent with crypto-miner equity vol regime, not a stale name

## Detailed findings

### Input validation

- Ticker: `MARA` → uppercase 4 chars, alphanumeric → valid.
- As-of: `2026-05-20` → normalized; data pinned to `2026-05-19` (latest parquet).
- Directory: created at `/Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20/`.
- Versioning: v1. No prior `phase-*.md` in this dir.

### UW MCP availability

`mcp__uw-pp__historical_available_dates` returned 5 data-type arrays:

| Data type | Latest available |
|-----------|------------------|
| darkpool  | 2026-05-19 |
| hotchains | 2026-05-19 |
| oi        | 2026-05-19 |
| options   | 2026-05-19 |
| screener  | 2026-05-19 |

All 5 streams agree on the same latest date — clean cutover. No 2026-05-20
file yet (orchestration time precedes EOD parquet generation).

### Ticker sanity

`mcp__uw-pp__options_flow_unusual_volume(symbol=MARA, top_n=1, date=2026-05-19)`
returned 1 row:

| Field | Value |
|-------|-------|
| underlying_symbol | MARA |
| option_type | call |
| strike | 14.5 |
| expiry | 2026-06-18 |
| total_volume | 223 |
| open_interest | 14 |
| vol_oi_ratio | 15.93 |
| total_premium | $9,691 |
| avg_iv | 0.889 (88.9%) |

→ Options chain is live and quoting. Premium is modest ($9.7K) but vol/OI of
15.9x on a 30-DTE OTM call is a marker of new positioning, not roll/close.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_available_dates` | `{compact: true}` | 5 streams, latest 2026-05-19 |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: MARA, top_n: 1, date: 2026-05-20}` | **errored** (no parquet for 2026-05-20) |
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: MARA, top_n: 1, date: 2026-05-19}` | 1 row: 2026-06-18 14.5C, vol/OI 15.9 |

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume(symbol=MARA, top_n=1, date=2026-05-20)` →
  `Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options`.
  **Resolution:** pin downstream UW calls to `date=2026-05-19`. Macro context
  (phase 6) and trade plan (phase 9) will treat the analysis as
  "EOD 2026-05-19, executable 2026-05-20 open".

## Prior versions

None (v1).

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. All UW calls must use `date=2026-05-19`. Treat this as "Tuesday close" data
     for a "Wednesday open" trade.
  2. MARA is a high-IV crypto-miner — phase 4 (structure) and phase 5
     (historical IV) should expect IV in the 70-100 range and a heavy
     gamma/vanna profile around BTC volatility.
  3. Top unusual-volume contract is a 30-DTE 14.5 call — note that strike for
     dealer-positioning crosschecks in phase 4 and confluence in phase 10.
- **Open questions:**
  - Where is spot MARA on 2026-05-19 close? (needed for ITM/OTM context in
    every later phase — to be sourced from phase 1's top_premium_trades or
    phase 4's GEX call's underlying price field.)
  - BTC spot / regime — needed for phase 6.
