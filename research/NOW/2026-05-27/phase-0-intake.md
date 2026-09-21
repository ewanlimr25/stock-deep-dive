# Phase 0 — Intake

**Ticker:** NOW
**As-of date:** 2026-05-27
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/NOW/2026-05-27
**Version:** v1
**Generated:** 2026-05-28T12:09:04Z

## Summary

Ticker `NOW` validated (1–5 alphanumeric, US-listed). Output directory created.
UW CLI reachable; latest options and darkpool dates both equal the as-of date
(2026-05-27), so the run is fully reproducible to that snapshot. NOW carries
live options activity. Local parquet present (DuckDB available) with the known
non-contiguous gap (2026-03-27 → 2026-04-27). `fz` healthy. Proceeding to
phase 0.5.

> **Dataset note (carry forward):** All tools return a self-consistent snapshot
> in which **NOW trades at ~$102.12** with **~1.03B shares out / 1.02B float**.
> Every downstream phase treats tool output as authoritative and does NOT inject
> external/real-world priors about the issuer. Numbers below are the data of
> record for this run.

## UW availability

- `uw historical available-dates`: ok
- Latest available options date: 2026-05-27 (= as-of ✓)
- Latest available darkpool date: 2026-05-27 (= as-of ✓)
- Datasets present: darkpool, hotchains, oi, options, screener

## Ticker sanity

- Options activity (`unusual-volume` top 1): `NOW 2026-07-02 P65` — vol 250 /
  OI 1, vol/OI 250, total premium $5,750, avg IV 0.792. Confirms a live options
  tape. (Far-OTM micro-lot; just a liveness probe, not a signal.)

## Local data (escape hatch / gap-awareness)

- `local_data_available`: yes · `duckdb_available`: yes
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local dates (33): 2026-03-13 → 2026-03-27, **[GAP]**, 2026-04-27 →
  2026-05-27. **Gap flagged: yes** (one trading month missing: 2026-03-28 →
  2026-04-26). Phase-5 historical and phase-0.5 self-history must treat the
  series as two contiguous blocks, not one continuous window.
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: yes
- `Shs Float`: **1.02B** (Shs Outstand 1.03B; Short Float 5.67%; quoted price
  $102.12) — carried to phase-2/3 for %-of-float order-size normalization and to
  seed next run's `quote-drift`.
- Note: `fz` supplements SI/float/peer/breadth only (`lib/fz-recipes.md`); it is
  downside-only/advisory and never enters the Kelly `p`.

## Prior versions

None (v1).

## Tool errors

None — all Phase 0 probes returned clean.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. As-of 2026-05-27 is the latest snapshot — full reproducibility, no live-data drift.
  2. **Data-of-record: NOW ≈ $102.12, float 1.02B, short float 5.67%.** Use tool values, not external priors.
  3. Local history has a one-month hole (2026-03-28 → 2026-04-26); split self-history/percentile windows across the gap.
- **Open questions:** Is the current flow genuinely unusual vs NOW's own baseline? (→ phase 0.5)
