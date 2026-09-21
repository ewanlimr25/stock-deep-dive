# Phase 0 — Intake

**Ticker:** INTC
**As-of date:** 2026-06-26
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/INTC/2026-06-26
**Version:** v1
**Generated:** 2026-06-27T09:47:47-0400

## Summary

Ticker validated (INTC = Intel Corp, Technology / Semiconductors). Output directory
created empty (v1, no prior runs). UW CLI reachable and `available-dates` confirms the
as-of date 2026-06-26 is the latest date present across all five datasets. INTC carries
active, in fact unusually heavy, options flow. Local parquet snapshot + DuckDB present;
`fz` healthy. **Context flag:** the `fz` quote shows INTC at **$128.32 / $644.94B mkt cap**
— a dramatic re-rate vs. Intel's historical $20–40 range — which is internally consistent
with the as-of options tape (a strike-89 call line trading 25.4k contracts). As-of spot will
be re-anchored from UW data in phases 0.5/1/3. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (JSON validated). 5 datasets
  (options, darkpool, oi, hotchains, screener), 54 dates each, range
  **2026-03-13 → 2026-06-26**.
- Latest available options date: **2026-06-26** (= as-of; clean)
- Latest available darkpool date: **2026-06-26** (= as-of; clean)
- Latest available oi / hotchains / screener date: **2026-06-26**

## Ticker sanity

- Options activity (`unusual-volume --symbol INTC --top-n 1 --date 2026-06-26`):
  **non-empty** — top line is a `call` `strike=89` `expiry=2026-07-02`
  with `total_volume=25401`, `open_interest=3`, `vol_oi_ratio=8467`,
  `total_premium=$101.5M`. INTC is NOT thin; flagged for phase-1 follow-up
  (brand-new high-vol/OI deep-ITM-looking call line).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (54): 2026-03-13 … 2026-03-27, **[GAP]**, 2026-04-27 … 2026-06-26
  (full list: 03-13,16,17,18,19,20,23,24,25,26,27 | 04-27,28,29,30 | 05-01,04,05,06,07,08,11,12,13,14,15,18,19,20,21,22,26,27,28,29 | 06-01,02,03,04,05,08,09,10,11,12,15,16,17,18,22,23,24,25,26)
- **Gap flagged: YES** — non-contiguous hole **2026-03-27 → 2026-04-27** (≈1 month
  missing, late-March through most of April). Phase-5 self-history percentiles and
  phase-0.5 long-window cuts must treat N as gap-reduced, not assume contiguity.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (`fz doctor` green)
- `Shs Float`: **4.25B** (Shs Outstand 5.02B) — carried to phase-2/3 for %-of-float
  order-size normalization.
- Snapshot (advisory, EOD/live — not as-of-anchored): Price $128.32, Mkt Cap $644.94B,
  Short Float 3.39%, Short Ratio 1.07, Sector Technology / Semiconductors.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); the live
  price is advisory and will be reconciled against the UW as-of spot downstream.

## Prior versions

_None — this is v1._

## Tool errors

_None — all probes returned valid JSON._
