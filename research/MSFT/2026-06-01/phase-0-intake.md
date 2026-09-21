# Phase 0 — Intake

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/MSFT/2026-06-01
**Version:** v1
**Generated:** 2026-06-02T10:50:46Z

## Summary

Ticker MSFT validated (4-char US-listed equity). Output directory created and
empty → this is a **v1** run. UW CLI reachable and the requested as-of date
**2026-06-01 is the latest available date in every UW dataset** (options,
darkpool, oi, hotchains, screener), so the run is fully reproducible and uses no
live data. MSFT shows heavy options activity. `fz` (Finviz) and DuckDB both
available. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (object keyed by dataset:
  darkpool/hotchains/oi/options/screener). NB: the per-dataset arrays are
  **unsorted** — must `sort` before taking max (a raw `.[-1]` is wrong).
- Latest available options date: **2026-06-01** (= as-of; 36 dates total)
- Latest available darkpool date: **2026-06-01**
- Latest available oi / hotchains / screener date: **2026-06-01** (all four)

## Ticker sanity

- Options activity (`unusual-volume` top 1, `--date 2026-06-01`): **MSFT 460P,
  exp 2026-06-01**, `total_volume`=41,284, `open_interest`=5, `vol_oi_ratio`=8256.8,
  `total_premium`=$5,189,075, `avg_iv`=0.0302. Confirms a liquid, active options
  tape. (`source`: `All Options/bot-eod-report-2026-06-01.parquet`)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: `/Users/ewan/Documents/Stocks`
- Available local dates (36, screener): `2026-03-13, 03-16, 03-17, 03-18, 03-19,
  03-20, 03-23, 03-24, 03-25, 03-26, 03-27, 04-27, 04-28, 04-29, 04-30, 05-01,
  05-04, 05-05, 05-06, 05-07, 05-08, 05-11, 05-12, 05-13, 05-14, 05-15, 05-18,
  05-19, 05-20, 05-21, 05-22, 05-26, 05-27, 05-28, 05-29, 06-01`
- **Gap flagged: YES** — non-contiguous: **2026-03-27 → 2026-04-27** (~1 month of
  trading days missing). Phase-5 historical and phase-0.5 self-history must treat
  the window as two segments (mid-Mar and late-Apr→Jun), not a continuous 36-day
  run. The recent contiguous block (04-27 → 06-01, ~26 sessions) is the usable
  near-term history.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes**
- `Shs Float`: **7.31B** (Shs Outstand 7.43B; Short Float 1.06%) — carried to
  phase-2/3 for %-of-float normalization of dark-pool prints and OI walls.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); used
  downside-only/advisory. Both gates (7b Finnhub peers, 7c WebSearch SI) have
  live primary sources, so `fz` adds rather than substitutes here.

## Prior versions

None — v1.

## Tool errors

None. (First `available-dates` jq used `.[-1]` on an unsorted array and
mis-reported the max as 2026-03-13; corrected by `sort|last` → 2026-06-01.
Recorded under DATA NOTE, not a tool error — the tool returned valid JSON.)

## DATA NOTE / CORRECTION

- **Field:** latest available date per UW dataset.
  **Wrong value (first read):** `options_last = 2026-03-13` via `.options[-1]`.
  **Corrected value:** `2026-06-01` via `.options | sort | last`.
  **Cause:** the `available-dates` arrays are returned **unsorted**; positional
  indexing is invalid. All later phases must `sort` before taking min/max of any
  `available-dates` array. The as-of date is present in every dataset.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only).
- **Conviction:** n/a.
- **Three things later phases should remember:**
  1. As-of **2026-06-01** is the latest data date in all UW datasets — pass
     `--date 2026-06-01` everywhere the flag exists; never call live data.
  2. **Data gap 2026-03-27 → 2026-04-27** — historical/self-history windows are
     two segments; the clean recent block is **04-27 → 06-01 (~26 sessions)**.
  3. `Shs Float = 7.31B`, Short Float `1.06%` (low) — carry for %-of-float and
     the phase-7c short-interest gate.
- **Open questions:** none for intake.
