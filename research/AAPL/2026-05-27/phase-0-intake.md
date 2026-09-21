# Phase 0 — Intake

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/AAPL/2026-05-27
**Version:** v1
**Generated:** 2026-05-28T02:49:02Z

## Summary

Ticker AAPL validated (US-listed mega-cap equity). Output directory created and
empty → v1 run. UW CLI reachable; AAPL has live options activity on the as-of
date. Local parquet snapshot present (DuckDB available) with a known
non-contiguous gap (2026-03-27 → 2026-04-27). `fz` healthy; float snapshotted.
Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-05-27**
- Latest available darkpool date: **2026-05-27**
- Earliest available date (all datasets): **2026-03-13** (33 trading dates)

## Ticker sanity

- Options activity (unusual_volume top 1): `AAPL 480C 2026-11-20` — total_volume 377,
  vol/OI 377, total_premium $11,641, avg_iv 0.272. **Options active.**

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (33): 2026-03-13, -16, -17, -18, -19, -20, -23, -24, -25,
  -26, -27, **[gap]** 2026-04-27, -28, -29, -30, 2026-05-01, -04, -05, -06, -07,
  -08, -11, -12, -13, -14, -15, -18, -19, -20, -21, -22, -26, -27
- **Gap flagged: yes** — one month missing between 2026-03-27 and 2026-04-27.
  Phase-5 historical lookbacks and phase-0.5 self-history percentiles must treat
  the local window as ~2.5 months of trading days, not a contiguous quarter.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **14.67B** (Shs Outstand 14.69B) — carried to phase-2/3 for
  %-of-float order-size normalization.
- `Short Float`: **0.92%** · `fz` spot price: **310.85** (seed for phase-0/5/9
  price context; advisory only).
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

None (v1).

## Tool errors

None — all intake probes green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. Local window is non-contiguous (one-month gap Mar-27 → Apr-27); 33 dates total.
  2. AAPL float ≈ 14.67B shares, short float 0.92% (very low) — for %-of-float math.
  3. Reference spot ≈ $310.85 (fz) on as-of date.
- **Open questions:** whether AAPL flow today is unusual vs its own busy-name
  baseline — answered in phase 0.5.
