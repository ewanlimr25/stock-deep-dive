# Phase 0 — Intake

**Ticker:** FSLR
**As-of date:** 2026-07-20
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/FSLR/2026-07-20
**Version:** v1
**Generated:** 2026-07-20

## Summary

Ticker FSLR validated (First Solar, US-listed equity). Output directory created.
UW CLI reachable and current through the as-of date. FSLR carries active,
unusual options flow. Proceeding to phase 0.5 (context).

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-07-20 (= as-of ✓)
- Latest available darkpool date: 2026-07-20
- Latest available oi date: 2026-07-20
- Latest available hotchains date: 2026-07-20
- Latest available screener date: 2026-07-20

## Ticker sanity

- Options activity (unusual_volume top 1): FSLR 2026-07-24 **175P** — vol 755 /
  OI 26 (vol/OI **29.0×**), total premium $15.1k, avg IV 86.0%. Active, unusual
  short-dated flow present → not a thin name.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-07-20 (69 sessions). **Non-contiguous
  gap flagged: yes** — a break between 2026-03-27 and 2026-04-27 (~one month
  missing). Contiguous from 2026-04-27 onward. Self-history percentiles (phase
  0.5) and phase-5 historical should treat the pre-gap block separately.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes (doctor OK)
- `Shs Float`: **n/a** — `fz quote FSLR --agent` returned a partial fundamentals
  payload (14 fields: Market Cap, Sales, Income, EV, Book/sh, etc.; float /
  short-float / price fields absent this pull). Phase-2/3 %-of-float
  normalization will fall back to a WebSearch/Finnhub float, and phase-7c short
  interest degrades to its WebSearch source. Not a blocker.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

- Prior FSLR run exists at `research/FSLR/2026-05-18/` (different date — not a
  same-day re-run, so this remains **v1** for 2026-07-20). That run is available
  for phase-5/phase-9 self-history reference (~2 months prior).

## Tool errors

None. (Initial `unusual-volume` jq indexed the wrapper object with `.[0]`
instead of `.results[0]`; corrected on re-run — value above traces to
`.results[0]` on validated JSON.)
