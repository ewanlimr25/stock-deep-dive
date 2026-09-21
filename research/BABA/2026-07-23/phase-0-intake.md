# Phase 0 — Intake

**Ticker:** BABA
**As-of date:** 2026-07-23
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/BABA/2026-07-23
**Version:** v1
**Generated:** 2026-07-24T11:48:32Z

## Summary

Ticker validated (BABA — Alibaba Group Holding Ltd ADR, US-listed). Output
directory created fresh for as-of date 2026-07-23. UW CLI reachable; local
options + darkpool snapshots both current through 2026-07-23 (matches the
requested as-of exactly — fully as-of reproducible). Options activity confirmed.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: 2026-07-23
- Latest available darkpool date: 2026-07-23

## Ticker sanity

- Options activity (unusual_volume top 1): BABA 2026-08-21 **112 PUT** —
  total_volume 326, open_interest 7, **vol/OI 46.6**, total_premium $147,456,
  avg_iv 0.470, trade_count 29. Options are active (not thin).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-07-23 (73 dates). **Gap flagged: yes**
  — non-contiguous between **2026-03-27 and 2026-04-27** (a ~1-month hole; no
  local parquet for early-to-mid April). Contiguous daily coverage resumes
  2026-04-27 onward. Later phases (5 historical, 0.5 self-history) must treat any
  April window as data-absent, not zero-signal.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (doctor green)
- `Shs Float`: **n/a** — Finviz returns only a reduced fundamental set for BABA
  (14 fields: Book/sh, Cash/sh, Dividend*, Employees, Enterprise Value, IPO,
  Income, Index, Market Cap, Payout, Sales). No `Shs Float`, `Short Float`,
  `Shs Outstand`, or price/valuation multiples — expected for a foreign ADR (FPI).
- Note: because `fz` carries no float/SI for this ADR, phase-7c falls back to
  **WebSearch** for short interest / float / borrow, and phase-7b to Finnhub +
  WebSearch for peers/estimates. `fz` remains usable only for the sparse
  fundamentals above (advisory). Consistent with the memory note that FPIs are
  structurally sparse in Finviz/MSPR.

## Prior versions

None for as-of 2026-07-23 (v1). Note: earlier BABA deep-dive runs exist for
different as-of dates (research/BABA/2026-05-20, research/BABA/2026-05-27) — those
are separate dated blueprints, not prior versions of this run.

## Tool errors

None. (Initial `unusual-volume` read was piped with an array-index jq path; the
command output is an object under `.results` — re-run with `.results[0]` parsed
cleanly. No number was transcribed from the errored buffer.)
