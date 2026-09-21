# Phase 0 — Intake

**Ticker:** PYPL
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19 (latest UW parquet available — see note)
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PYPL/2026-05-20
**Version:** v1
**Generated:** 2026-05-20T00:00:00-04:00

## Summary

Ticker validated (PYPL, US-listed equity, optionable). Output directory created
fresh — no prior versions. UW MCP reachable. The user-supplied as-of date
2026-05-20 has no parquet yet (T+1 EOD lag), so every downstream UW call will
pass `date=2026-05-19`. The output directory remains `2026-05-20` per the
user's request; analysts should treat "as-of" semantically as "session ending
2026-05-19, viewed pre-open 2026-05-20." Proceeding to phase 1.

## UW availability

- `historical_available_dates`: ok
- Latest available options date: 2026-05-19
- Latest available darkpool date: 2026-05-19
- Latest available OI date: 2026-05-19
- Latest available hotchains date: 2026-05-19
- Latest available screener date: 2026-05-19

## Ticker sanity

- Options activity (`options_flow_unusual_volume` top 1, date=2026-05-19):
  PYPL 2026-06-12 $36 put — total_volume 2,280, OI 15, vol/OI 152, avg_iv 37.3%,
  trade_count 64, total_premium $6,050. **Confirmed live options market with
  unusual activity already present on most-recent session.**

## Date-handling protocol for downstream phases

- Every UW tool call MUST pass `date=2026-05-19` (not 2026-05-20).
- If a tool errors with "no parquet for 2026-05-19", fall back one further
  available date (2026-05-18) and log it in that phase's `## Tool errors`.
- Citations should tag dates as `[FLOW:2026-05-19]` etc. for the audit trail.

## Prior versions

None (v1).

## Tool errors

- `mcp__uw-pp__options_flow_unusual_volume(symbol=PYPL, top-n=1, date=2026-05-20)`
  → "Error: no parquet file for 2026-05-20 in /Users/ewan/Documents/Stocks/All Options".
  Resolved by re-running with `date=2026-05-19`.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** N/A
- **Three things later phases should remember:**
  1. Effective data date is 2026-05-19 — pass it explicitly to every UW tool.
  2. PYPL has live unusual volume already — there is a real flow story here,
     not a thin-trader artifact.
  3. The Jun 12 $36 put is the first "hot" contract seen — watch whether
     puts dominate phase-1 sweeps.
- **Open questions:** What is spot PYPL at the 2026-05-19 close? (resolved in
  phase 1 via flow data containing underlying mid).
