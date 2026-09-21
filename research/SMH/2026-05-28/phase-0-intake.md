# Phase 0 — Intake

**Ticker:** SMH
**As-of date:** 2026-05-28
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/SMH/2026-05-28
**Version:** v1
**Generated:** 2026-05-29T11:56:18Z
**Upstream phases cited:** (none — root phase)

## Summary

Ticker validated: **SMH** = VanEck Semiconductor ETF (US-listed, NASDAQ). Output
directory created. UW CLI reachable; **all five datasets** (darkpool, hotchains,
oi, options, screener) carry **2026-05-28** as their latest date, so this as-of
run is fully reproducible — no trailing-date drift. SMH has live, heavy options
activity. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-05-28**
- Latest available darkpool date: **2026-05-28**
- Latest oi / hotchains / screener date: **2026-05-28** (all aligned to as-of)

## Ticker sanity

- Options activity (unusual_volume top 1): **SMH 2026-06-26 565P** — total_premium
  $6,906,718, total_volume 3,740, OI 75, vol/OI **49.9×**, avg_IV 0.474. Not thin;
  a single near-50× vol/OI put print already stands out at intake.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (34): 2026-03-13 → 2026-03-27, **[gap]**, 2026-04-27 →
  2026-05-28. Gap flagged: **yes** (no data 2026-03-28 … 2026-04-26, ~1 month).
  Contiguous run for the recent window: 2026-04-27 → 2026-05-28 (22 sessions).
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`). The gap matters for phase-5 lookbacks longer
  than ~1 month and phase-0.5 self-history percentiles — flag any percentile that
  spans 2026-03-27/2026-04-27 as gap-affected.

## Finviz augments (`fz`)

- `fz_available`: **yes** (api reachable, auth not required, v1.0.0)
- `Shs Float`: **n/a** — SMH is an ETF; Finviz does not carry float / shares
  outstanding / short-float for it (`fz quote SMH` returns null for all three).
  Phase-2/3 %-of-float normalization is therefore **not available** for SMH; use
  raw notional and AUM/creation-unit context instead.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`). For an
  ETF the SI/float lanes degrade to n/a, but `fz` sector/peer **breadth** (the
  semis complex) remains usable and is the more relevant augment here. On any
  per-name failure, phase-7c falls back to WebSearch SI and phase-7b to Finnhub.

## Prior versions

(none — v1)

## Tool errors

(none — all green)

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. SMH is an **ETF** (basket of ~25 semis, heavily NVDA/TSM/AVGO-weighted) — so
     treat single-name "fundamentals" (phase-7b) and short-interest/float
     (phase-7c) as **basket/holdings reads**, not issuer reads. The quality veto
     becomes a holdings-quality + structure read, not an income-statement read.
  2. As-of 2026-05-28 == latest local + UW date → no as-of/trailing mismatch;
     every phase can use `--date 2026-05-28` safely and reproducibly.
  3. There is a **~1-month local-data gap** (2026-03-28 … 2026-04-26). Any
     phase-5 lookback or phase-0.5 percentile crossing it must be flagged
     gap-affected; the clean recent window is 2026-04-27 → 2026-05-28.
- **Open questions:** Is the 565P at intake a hedge against semis (an SMH basket
  hedge by an NVDA/AVGO holder) or a directional bearish bet? Resolve in phase 1/3.
