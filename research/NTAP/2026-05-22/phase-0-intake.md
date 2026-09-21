# Phase 0 — Intake

**Ticker:** NTAP (NetApp, Inc. — US-listed equity, NASDAQ)
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NTAP/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T00:00:00Z

## Summary

Ticker validated (NTAP, 4 chars, alphanumeric, US-listed equity). Output
directory created and empty. UW MCP reachable — all five datasets (darkpool,
hotchains, oi, options, screener) carry the as-of date 2026-05-22. NTAP shows
materially unusual options activity. All downstream UW calls will pass
`date=2026-05-22`; no live data will be called. Proceeding to phase 0.5.

**Early flag for downstream:** the single most-unusual contract is a
**185-strike call expiring 2026-06-18 with vol/OI ratio 551** ($284K premium,
493 trades), and **avg IV is 68.8%** — far above a storage-hardware name's
baseline. Elevated IV + concentrated near-dated call buying is consistent with
an imminent catalyst. NTAP (fiscal year ends late April) historically reports
**fiscal Q4 earnings in the last week of May** — phases 5, 7b, and especially
the earnings-aware tools must check whether earnings fall inside the trade
window.

## UW availability

- `historical_available_dates`: **ok** (no error)
- Latest available options date: **2026-05-22** (matches as-of)
- Latest available darkpool date: **2026-05-22** (matches as-of)
- OI / hotchains / screener latest: **2026-05-22** (all aligned)

## Ticker sanity

- Options activity (`unusual_volume` top 1): **NTAP 185C 2026-06-18** —
  `vol_oi_ratio=551.17`, `total_volume=3307`, `open_interest=6`,
  `total_premium=$284,370`, `trade_count=493`, `avg_iv=0.6885`.
  Source: `bot-eod-report-2026-05-22.parquet`. Options activity is **rich**, not
  thin — full workflow applicable.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (31): 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20,
  03-23, 03-24, 03-25, 03-26, 03-27, **[GAP]**, 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22.
- **Gap flagged: YES** — non-contiguous between **2026-03-27 and 2026-04-27**
  (one month missing). Phase 5 historical look-backs and phase-0.5 self-history
  percentiles must treat the series as two segments, not one continuous window.
- Note: MCP is primary; local DuckDB is opt-in for cuts the MCP can't express
  (`lib/duckdb-cuts.md`).

## Prior versions

None — this is v1.

## Tool errors

None — all green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read yet)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Elevated avg IV (68.8%) + 551x vol/OI near-dated call buying = a catalyst
     is likely priced; confirm whether **NTAP earnings fall in the trade window**
     (fiscal Q4, typically late May).
  2. Local data has a **one-month gap (03-27 → 04-27)** — segment any
     multi-month look-back.
  3. Data is complete and aligned across all five UW datasets for 2026-05-22;
     no degradation expected.
- **Open questions:** exact earnings date; whether the unusual call flow is
  directional conviction or a vol/earnings play (resolve in phases 1, 5, 7b).
