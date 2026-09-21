# Phase 0 — Intake

**Ticker:** NOW
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NOW/2026-07-17
**Version:** v1
**Generated:** 2026-07-19 (run) for as-of 2026-07-17

## Summary

Ticker validated: **NOW = ServiceNow Inc** (Technology / Software - Application).
As-of close **$103.24** (prev_close $104.01, −0.74% on the day). Note the price is
**post-split** — ServiceNow previously traded ~$1,000, so option strikes in the
~$90–130 band (e.g. the strike-113 call surfaced by unusual-volume) are coherent
on the split-adjusted tape. UW CLI reachable; all datasets current to the as-of
date. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok**
- Latest available options date: **2026-07-17** (= as-of)
- Latest available darkpool date: **2026-07-17** (= as-of)
- Latest oi / screener / hotchains date: **2026-07-17** (all current)

## Ticker sanity

- Options activity (unusual_volume top 1): **NOW 2026-08-14 113C** — total_volume 121,
  open_interest 9, vol_oi_ratio 13.44, total_premium $61,756, avg_iv 0.761
  (`.results[0]`). Options are active; not thin.
- As-of price (screener parquet): **close=103.24, prev_close=104.01** (`ticker='NOW'`).

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates: **2026-03-13 → 2026-07-17** (67 dates). **Gap flagged: yes**
  — non-contiguous **2026-03-27 → 2026-04-27** (~1 month missing, incl. all of April
  1–24). Contiguous daily from 2026-04-27 onward. Phase-5 self-history percentiles
  must treat the pre-04-27 window as sparse.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (binary healthy) — **BUT partial snapshot this run**: `fz
  quote NOW --agent` returned only **14 of 84** fundamental fields (no Price / Shs
  Float / Short Float / Shs Outstand), consistent with a Finviz rate-limit /
  sniffed-API truncation. Company + sector/industry resolved correctly
  ("ServiceNow Inc", Technology / Software - Application).
- `Shs Float`: **n/a this run** (partial snapshot). Phase-2/3 %-of-float
  normalization will retry `fz`; on repeat failure, fall back to WebSearch float.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); on a
  continued partial, phase-7c falls back to WebSearch SI and phase-7b to Finnhub peers.

## Prior versions

None (v1).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | latest options/darkpool/oi/screener/hotchains = 2026-07-17 ← `.<ds>\|sort\|last` | keys |
| `uw options-flow unusual-volume --symbol NOW --top-n 1 --date 2026-07-17 --json` | 113C 2026-08-14, vol_oi 13.44 ← `.results[0]` | top-1 |
| duckdb `stock-screener-2026-07-17.parquet WHERE ticker='NOW'` | close=103.24, prev_close=104.01, full_name=SERVICENOW INC ← row | 1 |
| `fz quote NOW --agent` | company="ServiceNow Inc", 14/84 fields ← `.fundamentals\|length` | 1 |
| `ls "$STOCKS_DIR/Stock Screener/"` | 67 dates 2026-03-13→2026-07-17, gap 03-27→04-27 | dir |

## Tool errors

- `uw screener stock-screener --date 2026-07-17 --json | jq …` → jq parse error
  (Invalid numeric literal). The `uw screener` leaf output shape was not clean JSON
  under this filter; **worked around** by reading the local `stock-screener-*.parquet`
  via DuckDB for the price sanity check. Phase 0.5 will use the correct `uw screener`
  invocation/leaf.

## DATA NOTE / CORRECTION

Initial `uw options-flow unusual-volume` jq assumed an array (`.[0]`); actual shape
is an object with `.results[]`. Corrected to `.results[0]` before transcribing any
value — no wrong number persisted.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **NOW is post-split (~10:1), close $103.24** — read every strike/price on the
     split-adjusted tape; do NOT anchor to the old ~$1,000 quote.
  2. **Local data has a 03-27→04-27 gap** — phase-5 percentiles are sparse before
     2026-04-27; prefer the CLI/whole-tape over local self-history for that window.
  3. **fz snapshot was partial (14/84, no float)** — phases 2/3/7b/7c must re-probe
     `fz`; float-normalization and SI have a WebSearch fallback ready.
- **Open questions:** Is the −0.74% as-of day part of a larger trend? (phase 5).
  Is the flow genuinely unusual or a busy-name baseline? (phase 0.5).
