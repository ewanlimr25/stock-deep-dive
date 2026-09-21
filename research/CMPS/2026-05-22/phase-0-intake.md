# Phase 0 — Intake

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/CMPS/2026-05-22
**Version:** v1
**Generated:** 2026-05-26T00:00:00Z

## Summary

Ticker `CMPS` (COMPASS Pathways plc — clinical-stage psychedelic/biotech, US
ADR on Nasdaq) validated. Output directory created fresh (v1). UW MCP reachable;
options + dark pool + OI + hot-chains + screener all carry data through the
as-of date 2026-05-22. Options activity confirmed (July $13 call, vol/OI 12.8,
avg IV ~103%) — high-IV clinical-stage profile, **not** thin. Proceeding to
phase 0.5. As-of date is set, so **every** UW tool downstream receives
`date=2026-05-22`; no live data.

## UW availability

- `historical_available_dates`: **ok**
- Latest available options date: 2026-05-22 (matches as-of)
- Latest available darkpool date: 2026-05-22 (matches as-of)
- **Known gap:** data is non-contiguous between **2026-03-27 → 2026-04-27**
  (~1 trading month absent across all datasets). Phase 5 (historical) and
  phase 0.5 (self-history) must treat any window spanning that gap as
  discontinuous.

## Ticker sanity

- Options activity (unusual_volume top 1): `CMPS 2026-07-17 C13.0` — total_volume
  4,894 vs OI 383 (vol/OI **12.78**), total_premium $735,214, avg_iv **1.031
  (~103%)**, 271 trades. Confirms a live, high-IV single-name options market.
- Source parquet: `All Options/bot-eod-report-2026-05-22.parquet`.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, then **gap**, then
  2026-04-27 → 2026-05-22 (31 dates total; gap flagged: **yes**).
- Note: MCP is primary; local DuckDB is opt-in only for cuts the MCP can't
  express (`lib/duckdb-cuts.md`), tagged ` DUCKDB`.

## Prior versions

_None — this is v1._

## Tool errors

_None — all intake checks green._

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a.
- **Three things later phases should remember:**
  1. CMPS is a clinical-stage psychedelics biotech ADR — expect binary
     catalyst risk (trial readouts/FDA), structurally high IV (~100%), and
     headline-driven gaps. Treat flow as event-anticipatory, not trend.
  2. There is a hard data gap **2026-03-27 → 2026-04-27**; any multi-week
     historical/trend window crossing it is discontinuous — annotate, don't
     interpolate.
  3. As-of is 2026-05-22; pass `date=2026-05-22` to every UW tool. No live data.
- **Open questions:** Is the current options market genuinely unusual for CMPS,
  or is ~$0.7M July-call premium just a normal day for this name? (→ phase 0.5
  cross-sectional + self-history context resolves this.)
