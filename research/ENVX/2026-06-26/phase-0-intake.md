# Phase 0 — Intake

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/ENVX/2026-06-26
**Version:** v1
**Generated:** 2026-06-27T14:47:39Z

## Summary

Ticker ENVX (Enovix Corp — silicon-anode battery) validated. Output directory
created (v1, no prior run). UW CLI reachable and the as-of date 2026-06-26 is
present across all five datasets (options / darkpool / oi / hotchains / screener).
Options activity confirmed. **Headline context for downstream gates: ENVX carries
a 26.00% short float on a 188.93M share float at $5.95 — a heavily-shorted,
low-priced name where squeeze/positioning dynamics will dominate the read.**
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (JSON OK, 54 dates per dataset)
- Latest available options date: 2026-06-26 (matches as-of)
- Latest available darkpool date: 2026-06-26
- Latest available oi / hotchains / screener: 2026-06-26
- **Non-contiguous gap flagged:** local history jumps 2026-03-27 → 2026-04-27
  (no late-March/early-April data); also a 2026-06-18 → 2026-06-22 weekend/holiday
  break. Phase-5 self-history must treat the March/April gap as missing, not zero.

## Ticker sanity

- Options activity (unusual_volume top 1): `ENVX 2026-06-26 C2.5` —
  total_volume=364, open_interest=16, vol_oi_ratio=22.75, total_premium=$123,250,
  avg_iv=42.77%. 0DTE call print on as-of day; not thin. (Full flow read in phase 1.)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (options, n=54): 2026-03-13 … 2026-03-27, **[gap]**,
  2026-04-27 … 2026-06-26 (contiguous trading days thereafter except the
  2026-06-18→06-22 weekend break). Gap flagged: **yes** (2026-03-27 → 2026-04-27).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: 188.93M (Shs Outstand 217.70M) — carried to phase-2/3 for
  %-of-float normalization.
- Snapshot extras: Price $5.95, **Short Float 26.00%** (carried to phase-7c
  short-interest gate; this is a primary risk lane for this name).
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

<none — v1>

## Tool errors

<none — all green>

## DATA NOTE / CORRECTION

<none — all reads round-tripped through jq on first pass>

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Low-priced ($5.95), small-float (188.93M) name with a **26% short float** —
     positioning/squeeze mechanics are central; phase-7c gate is load-bearing.
  2. As-of 2026-06-26 fully present locally; March/April gap means phase-5
     self-history percentiles run on the post-04-27 window only.
  3. On-day flow includes a 0DTE $2.5 call burst (vol/oi 22.75) — verify in
     phase 1 whether it's part of a directional sweep tape or isolated lotto.
- **Open questions:** Is the 26% short float static or rising? (phase-7c). Is the
  options tape genuinely directional or noise on a cheap name? (phase 1).
