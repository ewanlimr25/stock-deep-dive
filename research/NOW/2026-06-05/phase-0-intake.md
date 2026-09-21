# Phase 0 — Intake

**Ticker:** NOW
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NOW/2026-06-05
**Version:** v1
**Generated:** 2026-06-06T11:57:19-04:00

## Summary

Ticker validated (NOW — US-listed equity, optionable). As-of date 2026-06-05
supplied by user → every UW command downstream receives `--date 2026-06-05`;
no live calls. Output directory created (was empty → v1). UW CLI reachable;
latest available options AND darkpool snapshots both cover the as-of date
exactly. Local parquet + DuckDB escape hatch available. `fz` healthy with
float snapshotted. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (datasets: darkpool, hotchains, oi, options, screener)
- Latest available options date: 2026-06-05 (jq: `.options | sort | last`)
- Latest available darkpool date: 2026-06-05 (jq: `.darkpool | sort | last`)
- As-of 2026-06-05 is fully covered — no staleness adjustment needed.

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`): present —
  `NOW` put, strike 65, expiry 2026-06-12, total_premium $68,150,
  total_volume 17,030, OI 22, vol/OI 774.1, avg_iv 1.634
  (jq: `.results[0]`). Options market active → proceed.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (40): 2026-03-13 … 2026-03-27, then 2026-04-27 … 2026-06-05
  (weekdays; 2026-05-25 absent = Memorial Day holiday, not a gap)
- **Gap flagged: yes** — known non-contiguous gap 2026-03-30 → 2026-04-24
  (≈4 weeks of missing snapshots). Phase 0.5 self-history and phase 5
  lookbacks must not assume continuity across that window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: **1.02B** · `Shs Outstand`: 1.03B · `Short Float`: 5.67%
  (jq: `.fundamentals."Shs Float"` etc. — carried to phase-2/3 for
  %-of-float normalization and to phase-7c as the SI seed)
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

(none — v1)

## Tool errors

(none — all probes green)

## Tool calls

| Command | jq path | Result |
|---|---|---|
| `uw historical available-dates --json` | `.options \| sort \| last` / `.darkpool \| sort \| last` | 2026-06-05 / 2026-06-05 |
| `uw options-flow unusual-volume --symbol NOW --top-n 1 --date 2026-06-05 --json` | `.results[0]` | put 65 2026-06-12, $68,150 prem |
| local snapshot probe (`ls "$STOCKS_DIR/Stock Screener/"`) | n/a (shell) | 40 dates, gap 2026-03-30→04-24 |
| `fz quote NOW --agent` | `.fundamentals."Shs Float"` | 1.02B |
