# Phase 0 — Intake

**Ticker:** SMR
**As-of date:** 2026-06-16
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SMR/2026-06-16
**Version:** v1
**Generated:** 2026-06-17T11:44:43Z
**Upstream phases cited:** (none — first phase)

## Summary

Ticker **SMR** (NuScale Power Corp) validated. Output directory created and
empty → this is **v1**. UW CLI reachable; all five datasets
(options/darkpool/oi/hotchains/screener) carry the requested as-of date
**2026-06-16**, which is also the latest available date. SMR has live options
activity. Local parquet snapshot + DuckDB are both present (escape hatch
usable). `fz` healthy; float snapshotted. Proceeding to phase 0.5.

**Heads-up for downstream phases:** SMR trades at **$9.89** with **short float
18.12%** — a low-priced, heavily-shorted name. Phase-7c must treat the short
interest as a first-order positioning input (squeeze/borrow risk both ways).

## UW availability

- `uw historical available-dates --json`: **ok** (exit 0, parsed)
- Latest available options date: **2026-06-16** (as-of matches latest)
- Latest available darkpool date: **2026-06-16**
- Latest oi / hotchains / screener date: **2026-06-16** (all aligned)
- As-of 2026-06-16 confirmed present in both `options` and `darkpool` arrays
  (length-1 select match each). Arrays sorted before taking latest
  (`sort | last`) per known unsorted-array trap.

## Ticker sanity

- Options activity (`unusual-volume --top-n 1 --date 2026-06-16`): **present** —
  top row `SMR 2026-06-18 C5.5`, `total_premium=170359`, `total_volume=368`,
  `open_interest=2`, `vol_oi_ratio=184`, `avg_iv=4.5367`. Not thin; proceed.
  (C5.5 is deep-ITM at $9.89 spot — noted, not interpreted here.)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local screener dates (gap flagged: **yes**):
  `2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20, 03-23, 03-24, 03-25, 03-26,
  03-27, [GAP] 04-27, 04-28, 04-29, 04-30, 05-01, 05-04, 05-05, 05-06, 05-07,
  05-08, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18, 05-19, 05-20, 05-21, 05-22,
  05-26, 05-27, 05-28, 05-29, 06-01, 06-02, 06-03, 06-04, 06-05, 06-08, 06-09,
  06-10, 06-11, 06-12, 06-15, 06-16`
  - **Non-contiguous gap: 2026-03-27 → 2026-04-27** (~1 month missing). Phase-5
    self-history percentiles must treat the pre-gap block separately.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **335.44M** (Shs Outstand 346.11M) — carried to phase-2/3 for
  %-of-float normalization.
- `Short Float`: **18.12%** (carried to phase-7c as a first-order gate input).
- Spot price (advisory): **$9.89**.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

(none — v1)

## Tool errors

(none — all reads green and jq-parsed)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. SMR is a **$9.89 low-priced name with 18.12% short float** — positioning
     (phase-7c) and squeeze dynamics are central, not peripheral.
  2. As-of 2026-06-16 == latest available data across all datasets; full
     fidelity, no staleness penalty.
  3. Local screener history has a **2026-03-27→04-27 gap**; phase-5 must split
     pre/post-gap windows.
- **Open questions:** What is driving the heavy short interest, and is the flow
  on 06-16 squeeze-positioning or hedging? (phases 1, 3, 7c)
