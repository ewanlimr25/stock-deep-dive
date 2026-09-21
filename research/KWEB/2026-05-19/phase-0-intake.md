# Phase 0 — Intake

**Ticker:** KWEB
**As-of date requested:** 2026-05-20
**As-of date (effective):** 2026-05-19
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/KWEB/2026-05-19
**Version:** v1
**Generated:** 2026-05-20T00:00:00Z

## Summary

Ticker KWEB (KraneShares CSI China Internet ETF) validated and confirmed
active in UW options dataset. UW MCP reachable. The user requested as-of
2026-05-20 but UW data is only available through 2026-05-19 (the prior
trading session), so all downstream phases will pass `date=2026-05-19` to
UW tools. Output directory created at the effective-date path.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-19
- Latest available darkpool date: 2026-05-19
- Latest available OI date: 2026-05-19
- Latest available hotchains date: 2026-05-19
- Latest available screener date: 2026-05-19

A multi-week gap exists between 2026-03-27 and 2026-04-27 in the
available-dates index. Historical lookbacks that need pre-April data must
be reviewed for survivorship of the gap; the trailing ~16 trading days
(2026-04-27 → 2026-05-19) are dense and intact.

## Ticker sanity

- Options activity (`unusual_volume` top 1, date=2026-05-19): KWEB
  2026-06-18 30.5 C, volume 18,231 vs OI 56 (vol/OI 325.6),
  total_premium $656,297, avg_iv 33.8%. Confirms KWEB has a deep,
  trafficked listed-options market — proceeding to phase 1.

## Date-handling decision

The skill's intake rule says "if user supplied a date … pass date=<as-of>
downstream". Since 2026-05-20 returns "no parquet file" from UW, the
effective downstream date for all phase-1+ tool calls is **2026-05-19**.
Each phase will explicitly note the requested-vs-effective mismatch in
its own tool-calls table.

## Prior versions

(none — this is v1)

## Tool errors

| Tool | Args | Error |
|------|------|-------|
| `mcp__uw-pp__options_flow_unusual_volume` | `{symbol: KWEB, top-n: 1, date: 2026-05-20}` | `no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options` (fallback to 2026-05-19 succeeded) |

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. The effective UW data date is **2026-05-19**, not 2026-05-20 — every UW call must pass `date=2026-05-19`.
  2. KWEB is a China-internet ETF; macro phase must address China policy, USD/CNH, and US-listed ADR delisting risk.
  3. Single front-month call (30.5C 2026-06-18, vol/OI 326x, $656K premium) is the only sample-flow datapoint so far — does NOT yet constitute a thesis; phase 1 needs the full flow scan.
- **Open questions:** Is the 30.5C call buyer aggressive (ask-side sweep) or a closing seller? Phase 1 will answer via sweep + smart-money endpoints.
