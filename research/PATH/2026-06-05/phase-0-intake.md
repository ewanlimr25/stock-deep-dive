# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-06-05
**Version:** v1 (no prior files in this directory)
**Generated:** 2026-06-06T09:58:00-04:00

## Summary

Ticker validated (4-char US-listed equity, optionable). Output directory
created. UW CLI reachable; both options and darkpool datasets contain the
as-of date 2026-06-05. All downstream UW commands will carry
`--date 2026-06-05`. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (40 options dates, 40 darkpool dates)
- Latest available options date: 2026-06-05 (`.options | sort | last`)
- Latest available darkpool date: 2026-06-05 (`.darkpool | sort | last`)
- As-of date present in both datasets: yes (`index("2026-06-05") != null`)

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`): non-empty —
  PATH 2026-06-12 $5.5 call, total_premium $132,028, total_volume 213,
  OI 2, vol/OI 106.5 (jq `.results[0]`). Options chain is live; proceed.
  (Strike far below spot ~$11.24 — likely deep-ITM call; phase 1 to classify.)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (Stock Screener, 40): 2026-03-13 … 2026-03-27,
  2026-04-27 … 2026-06-05 (business days)
- **Gap flagged: yes** — known non-contiguous gap 2026-03-30 … 2026-04-24
  (nothing between 2026-03-27 and 2026-04-27). Phase 0.5 self-history and
  phase-5 lookbacks must not assume contiguity across that window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: **412.34M** (jq `.fundamentals."Shs Float"`) — carried to
  phase-2/3 for %-of-float normalization
- `Shs Outstand`: 455.76M · `Short Float`: **31.15%** (flag: very high —
  phase-7c positioning gate must examine squeeze/crowded-short dynamics)
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

None in this directory (v1). Prior PATH deep dives exist on other dates:
`research/PATH/{2026-05-18, 2026-05-22, 2026-05-29, 2026-06-01}` — the
2026-06-01 run is 4 calendar days old; phase 0.5 self-history should
reference it.

### Fundamental drift since 2026-06-01 (`fz quote-drift PATH --since 2026-06-01`)

Largest moves (jq over drift array):
- **Price 13.10 → 11.24** (−14.2%); Prev Close 11.72 → 11.67; day change −3.68%
- **RSI(14) 73.87 → 51.18** (overbought condition fully unwound)
- **Shs Outstand 520.44M → 455.76M** (−64.68M, −12.4% — major share-count
  reduction; phase 7b to verify buyback vs. data correction)
- Market Cap 6.82B → 5.85B; EV 5.58B → 4.62B; EV/Sales 3.34 → 2.77
- Forward P/E 14.53 → 12.47; P/E 21.61 → 18.54; PEG 1.22 → 1.04
- Perf Week +19.85% → −4.10%; Perf Month +27.18% → +7.05%; SMA20 distance
  +21.33% → +2.30% — the post-earnings spike has been almost fully faded
- Rel Volume 2.02 → 1.03; Volume 67.7M → 35.5M (still ~1× elevated vs 34.5M avg)
- Short Ratio 3.84 → 3.72

## Tool errors

None — all five intake probes returned valid JSON through jq.

## Tool calls

| Command | jq path | Result |
|---|---|---|
| `uw historical available-dates --json` | `.options/.darkpool \| sort \| last` | both 2026-06-05; 40 dates each |
| `uw options-flow unusual-volume --symbol PATH --date 2026-06-05 --top-n 1 --json` | `.results[0]` | $5.5C 06/12, $132k prem, 213 vol |
| local snapshot probe (`ls $STOCKS_DIR/Stock Screener/`) | n/a (shell) | 40 dates, gap 03-27→04-27, DUCKDB=yes |
| `fz quote PATH --agent` | `.fundamentals."Shs Float"` etc. | float 412.34M, SI 31.15% |
| `fz quote-drift PATH --since 2026-06-01 --agent` | full array | 41 fields moved (see above) |
