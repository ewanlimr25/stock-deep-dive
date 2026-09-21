# Phase 0 — Intake

**Ticker:** GFS
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/GFS/2026-05-27
**Version:** v1
**Generated:** 2026-05-28T00:00:00Z (run timestamp)

## Summary

Ticker validated: GFS = GlobalFoundries Inc. (NASDAQ, semiconductor foundry).
Output directory created (fresh v1 run). UW CLI reachable; latest available
options/darkpool date is exactly the as-of date (2026-05-27), so this is an
as-of reproducible run. GFS confirmed to carry live options. Local parquet
snapshot present with a known ~1-month gap (2026-03-27 → 2026-04-27). `fz`
healthy: float **132.68M** vs **548.42M** shares out (~24% — the rest is
strategic/insider, consistent with Mubadala majority ownership), short float
**7.08%**. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-05-27** (matches as-of)
- Latest available darkpool date: **2026-05-27** (matches as-of)
- All five datasets (darkpool, hotchains, oi, options, screener) span
  2026-03-13 → 2026-05-27, 33 trading days each.

## Ticker sanity

- Options activity (unusual_volume top 1): **GFS 2026-07-17 $120 CALL**
  (vol 1,308 / OI 150, vol/OI 8.72, total premium $260.9k, avg IV 0.90).
  Confirms tradable options chain — not a thin name.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (33): 2026-03-13, 03-16, 03-17, 03-18, 03-19, 03-20,
  03-23, 03-24, 03-25, 03-26, 03-27, **[GAP]**, 04-27, 04-28, 04-29, 04-30,
  05-01, 05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15,
  05-18, 05-19, 05-20, 05-21, 05-22, 05-26, 05-27
- **Gap flagged: yes** — non-contiguous between 2026-03-27 and 2026-04-27
  (≈1 month missing). Phase-5 historical and any DuckDB self-history percentile
  must treat the window as two segments, not one continuous series.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **132.68M** (Shs Outstand 548.42M → float ≈24% of shares out;
  ~75% strategic/insider held). Carried to phase-2/3 for %-of-float
  normalization of block/OI sizes.
- `Short Float`: **7.08%** (semi-monthly settlement, ~2-week lag) — elevated;
  carried to phase-7c as a squeeze/positioning input.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`).

## Prior versions

None — this is v1.

## Tool errors

None — all intake probes green.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **Low float / high short float.** Float 132.68M (~24% of shares out),
     short float 7.08% — a tight, squeeze-prone setup. Normalize all block/OI
     sizes against the 132.68M float, not shares outstanding.
  2. **Data gap 2026-03-27 → 2026-04-27.** Treat self-history/percentile
     windows as two segments; do not interpolate across the gap.
  3. **As-of reproducible.** Latest local date == as-of (2026-05-27), so every
     `uw` call must pass `--date 2026-05-27` where the flag exists.
- **Open questions:** none for intake.
