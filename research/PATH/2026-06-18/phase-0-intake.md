# Phase 0 — Intake

**Ticker:** PATH (UiPath Inc., NYSE)
**As-of date:** 2026-06-18
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/PATH/2026-06-18
**Version:** v1
**Generated:** 2026-06-20T12:55:27Z

## Summary

Ticker validated (PATH = UiPath Inc., US-listed equity). Output directory created
(empty → v1). UW CLI reachable; all 5 datasets cover the as-of date 2026-06-18.
PATH has live options activity. fz available. **Flag for downstream:** short float
is **31.78%** (very high — squeeze/positioning relevant) and price is ~$10.27 (a
low-dollar name, so $5.50 strikes are live). Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: ok (datasets: darkpool, hotchains, oi, options, screener)
- Latest available options date: 2026-06-18 (as-of date present ✓)
- Latest available darkpool date: 2026-06-18 (as-of date present ✓)
- Latest oi / hotchains / screener date: 2026-06-18 (all present ✓)

## Ticker sanity

- Options activity (unusual_volume top 1): `PATH` $5.50 **call**, expiry 2026-06-18,
  total_premium=$257,886, total_volume=557, open_interest=66, vol_oi_ratio=8.44,
  avg_iv=0.953 ← elevated IV. Not thin.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: 2026-03-13 → 2026-03-27, then **2026-04-27 → 2026-06-18**
  (gap flagged: **yes** — non-contiguous, no data 2026-03-30 … 2026-04-24).
  Phase-5 self-history must respect this gap; ~6 weeks of contiguous data lead into
  the as-of date.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **391.72M** (Shs Outstand 455.76M; carried to phase-2/3 for
  %-of-float normalization)
- `Short Float`: **31.78%** (snapshot — heavy short positioning; feeds phase-7c gate)
- Price snapshot: $10.27
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

_none — v1_

## Tool errors

_none — all green_

## DATA NOTE / CORRECTION

_none — first reads stood._

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **Short float 31.78%** — extreme; positioning gate (7c) and contrarian/squeeze
     framing matter; any bullish flow must be weighed against squeeze fuel vs. bear
     conviction.
  2. Low-dollar name (~$10.27) — strikes are tightly spaced ($5.50 calls live);
     premium magnitudes will look small in absolute $ — normalize by float / OI.
  3. Data gap 2026-03-30 → 2026-04-24; contiguous window is 2026-04-27 → 2026-06-18
     (~38 sessions). Phase-5 percentiles drawn only from the contiguous block.
- **Open questions:** Is the heavy short float being pressed (bearish flow) or faded
  (bullish squeeze flow)? Resolve in phases 1–4 and the 7c gate.
