# Phase 0 — Intake

**Ticker:** INTC
**As-of date:** 2026-06-15
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/INTC/2026-06-15
**Version:** v1
**Generated:** 2026-06-16T01:24:55Z

## Summary

Ticker INTC validated (US-listed equity, has options). Output directory created
fresh — no prior run for this date, so this is **v1**. UW CLI reachable; latest
available options and darkpool dates are both **2026-06-15** (= as-of, fully
reproducible). Local parquet snapshot present with DuckDB available. `fz` healthy
— INTC quotes **$127.86**, float **4.25B**. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-06-15**
- Latest available darkpool date: **2026-06-15**
- Datasets present: `darkpool`, `hotchains`, `oi`, `options`, `screener`

## Ticker sanity

- Options activity (unusual_volume top 1): **INTC 2026-06-18 P132** — total_volume
  599, vol_oi_ratio 599, total_premium $399,536, avg_iv 1.103 (110%). Options
  tape is live and active.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (Stock Screener): 2026-03-13 → 2026-03-27, **[gap]**,
  2026-04-27 → 2026-06-15 (contiguous trading days).
  - **Gap flagged: yes** — a ~1-month hole between **2026-03-27 and 2026-04-27**
    (no local screener parquet for early/mid April). Phase-5 historical and
    phase-0.5 self-history must treat any April-anchored lookback as incomplete.
  - 46 dates available; the most recent ~7 weeks (2026-04-27→2026-06-15) are dense.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **4.25B** (Shs Outstand 5.02B; Short Float 3.18%; Price $127.86)
  — carried to phase-2/3 for %-of-float normalization, and seeds next run's
  `quote-drift`.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on
  `no`, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

None — this is v1 for INTC / 2026-06-15.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | options_latest=2026-06-15 ← `.options\|sort\|last`; darkpool_latest=2026-06-15 | whole |
| `uw options-flow unusual-volume --symbol INTC --top-n 1 --date 2026-06-15 --json` | P132 vol=599 ← `.results[0]` | top-1 |
| `ls "$STOCKS_DIR/Stock Screener/"` | 46 dates, gap 03-27→04-27 | whole |
| `fz quote INTC --agent` | float=4.25B, short_float=3.18%, price=127.86 ← `.fundamentals` | snapshot |

## Tool errors

None — all probes green.

## DATA NOTE / CORRECTION

None — first reads stood. (Note: INTC prints $127.86 in this as-of snapshot; the
P132 strike in the unusual-volume probe is just OTM, consistent with that price —
not a data anomaly.)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only — no directional read)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of = latest local date (2026-06-15) → every UW read is fully reproducible
     with `--date 2026-06-15`; no live fallbacks needed.
  2. **Local gap 2026-03-27 → 2026-04-27** — any lookback crossing April is
     incomplete; phase-5 must flag it.
  3. INTC ≈ **$127.86**, float **4.25B**, short_float **3.18%** — carry for
     %-of-float sizing (phase 2/3) and the SI gate (phase 7c).
- **Open questions:** Is the current flow genuinely unusual for INTC or a busy
  large-cap's normal day? → phase 0.5 resolves via cross-sectional + self-history rank.
