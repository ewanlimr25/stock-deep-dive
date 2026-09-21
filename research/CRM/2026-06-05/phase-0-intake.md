# Phase 0 — Intake

**Ticker:** CRM
**As-of date:** 2026-06-05
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/CRM/2026-06-05
**Version:** v1 (this date dir was empty; prior run exists at `research/CRM/2026-05-29/` — see Prior versions)
**Generated:** 2026-06-06T15:47:00-04:00

## Summary

Ticker validated (CRM, US-listed mega-cap equity, Salesforce Inc). Output
directory created. UW CLI reachable; latest local options AND darkpool date =
2026-06-05, exactly matching the requested as-of date — no staleness. CRM has
live options activity. `fz` healthy; float snapshotted. All downstream UW
commands will pass `--date 2026-06-05` where supported. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok — datasets: darkpool, hotchains, oi, options, screener
- Latest available options date: 2026-06-05 (sorted; arrays are unsorted upstream)
- Latest available darkpool date: 2026-06-05

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-06-05`): present —
  CRM 2026-07-02 145P, total_volume 101, OI 13, vol/OI 7.77, premium $2,030
  (`.results[0]` of `uw options-flow unusual-volume`). Not thin; full-size chain.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (40): 2026-03-13 … 2026-03-27, then **GAP**, 2026-04-27 … 2026-06-05
  (contiguous weekdays within each segment; gap flagged: **yes** — 2026-03-28→2026-04-26 missing)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (`fz doctor` clean)
- `Shs Float`: **792.65M** · Shs Outstanding: 819.00M · Short Float: **7.91%**
  (carried to phase-2/3 for %-of-float normalization; 7.91% short float is
  elevated for a $152B mega-cap — flag for phase-7c positioning gate)
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

- None in this date dir (v1). Prior full run exists at `research/CRM/2026-05-29/`.
- **`fz quote-drift CRM --since 2026-05-29`** (fundamental drift since prior run):
  - Price 191.10 → **185.66** (−2.85%); day change on 6/05: −1.64%
  - RSI(14) 60.51 → **51.02** (momentum cooled to neutral)
  - SMA20 +6.74% → +2.23%; SMA50 +5.69% → +2.40%; SMA200 −13.64% → **−15.66%** (still far below 200d)
  - ATR(14) 8.27 → **9.60**; Volatility (W/M) 4.79%/3.94% → 5.16%/4.29% (vol expanding)
  - Market cap 156.51B → 152.06B (−$4.45B); EV 187.22B → 182.77B
  - Forward P/E 12.37 → **11.95**; PEG 0.99 → 0.94; P/FCF 10.68 → 10.37 (cheapening)
  - Insider Trans −0.14% → **+0.38%** (flipped net-positive); Inst Own 93.39% → 93.27%
  - Short Ratio 4.71 → 4.46; Avg Volume 13.31M → 14.06M
  - Target Price 248.11 → 247.46 (sell-side ~+33% above spot)
  - Dividend ex-date upcoming: **2026-06-11**

## Tool errors

None — all probes returned valid JSON.
