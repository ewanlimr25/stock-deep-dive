# Phase 0 — Intake

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/HOOD/2026-06-05
**Version:** v1
**Generated:** 2026-06-07T12:04:20-04:00

## Summary

Ticker validated (HOOD, US-listed equity — Robinhood Markets). As-of date
2026-06-05 supplied by user; all UW commands downstream receive
`--date 2026-06-05`. Output directory created (empty → v1). UW CLI reachable;
every dataset's latest local date equals the as-of date, so the run is fully
on-snapshot. Options activity confirmed. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-06-05
- Latest available darkpool date: 2026-06-05
- Latest available oi date: 2026-06-05 · hotchains: 2026-06-05 · screener: 2026-06-05
- (Per-dataset arrays are unsorted upstream; latest extracted via `sort|last`.)

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`): HOOD put,
  strike 77, expiry 2026-07-24, total_premium $54,649, total_volume 102,
  vol/OI 102 — active options market, not thin.
- jq path: `.results[0]` on validated JSON
  (source: `~/Documents/Stocks/All Options/bot-eod-report-2026-06-05.parquet`).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (40): 2026-03-13 → 2026-03-27 (11 sessions),
  then **gap 2026-03-30 → 2026-04-24** (known non-contiguous gap, flagged: yes),
  then 2026-04-27 → 2026-06-05 (29 contiguous sessions).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: 761.21M · `Shs Outstand`: 791.10M · `Short Float`: 4.96%
  (float carried to phase-2/3 for %-of-float normalization; short-float is a
  live `fz` read taken 2026-06-07, advisory only — phase-7c re-pulls with its
  own gate. jq path: `.fundamentals."Shs Float"` etc. on validated JSON.)
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Tool calls

| Command | jq path | Status |
|---|---|---|
| `uw historical available-dates --json` | `with_entries(.value \|= (sort\|last))` | ok |
| `uw options-flow unusual-volume --symbol HOOD --top-n 1 --date 2026-06-05 --json` | `.results[0]` | ok |
| local snapshot probe (`ls "$STOCKS_DIR/Stock Screener/"` + duckdb import) | n/a (shell) | ok |
| `fz doctor --agent` + `fz quote HOOD --agent` | `.fundamentals."Shs Float"` | ok |

## Prior versions

(none — v1)

## Tool errors

(none — all green)
