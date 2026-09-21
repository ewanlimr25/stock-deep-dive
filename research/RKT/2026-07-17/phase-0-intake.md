# Phase 0 — Intake

**Ticker:** RKT
**As-of date:** 2026-07-17
**Output dir:** /Users/ewan/Development/stock-deep-dive/research/RKT/2026-07-17
**Version:** v1
**Generated:** 2026-07-19T19:17:00-04:00
**Upstream phases cited:** (none — first phase)

## Summary

Ticker RKT (Rocket Companies Inc — Mortgage Finance, Financial sector) validated
and uppercased. Output directory created fresh (v1). UW CLI reachable; the as-of
date **2026-07-17 is the latest available date across all five datasets**
(options / darkpool / oi / hotchains / screener), so this is a clean point-in-time
read. Options activity confirmed present (thin but live). Local parquet snapshot
present with DuckDB available. `fz` reachable but its `quote --agent` payload for
RKT returns only a reduced fundamentals subset (no float / short-float field) —
phase-7c will fall back to WebSearch for SI/float. Proceeding to phase 0.5.

## UW availability

- `uw historical available-dates`: **ok** (keys: darkpool, hotchains, oi, options, screener)
- Latest available options date: **2026-07-17** (= as-of ✓)
- Latest available darkpool date: **2026-07-17**
- Latest oi / hotchains / screener date: **2026-07-17** each
- Note: options-date array spans 2026-03-13 → 2026-07-17 with a visible
  non-contiguous gap between **2026-03-27 and 2026-04-27** (≈1 month missing).
  Well outside any lookback this run needs; flagged for phase-5 gap-awareness only.

## Ticker sanity

- Options activity (unusual_volume top 1, `--date 2026-07-17`): **live** —
  top row is an Aug-14 **$15 put**, total_volume 322, OI 12, total_premium $44,540,
  avg_iv 0.709. Options exist but premium/volume are modest → **thin options name**;
  flow phases should weight per-contract prints carefully rather than assume depth.

## Local data (escape hatch / gap-awareness)

- `local_data_available`: **yes** · `duckdb_available`: **yes**
- `STOCKS_DIR`: /Users/ewan/Documents/Stocks
- Available local screener dates (recent tail): 2026-07-08, -09, -10, -13, -14,
  -15, -16, **-17** (gap flagged: no gap in recent window; older Mar/Apr gap noted above)
- Note: the `uw` CLI is primary; local DuckDB is opt-in for cuts the CLI can't
  express (`lib/duckdb-cuts.md`).

## Finviz augments (`fz`)

- `fz_available`: **yes** (version + doctor both green)
- `Shs Float`: **n/a** — `fz quote RKT --agent` returned only {Book/sh, Cash/sh,
  Market Cap 41.14B, Enterprise Value 69.84B, Income 239.36M, Sales 8.33B,
  Employees 23,500, IPO Aug-06-2020, …}; no float / short-float / shs-outstanding
  field in the payload. Phase-7c will source SI/float via WebSearch; phase-2/3
  %-of-float normalization degrades to advisory.
- Context carried forward: **Market Cap $41.14B**, **EV $69.84B**, **Sales $8.33B
  TTM**, **Income $239.36M** (Rocket Companies, post-2025 M&A scale — mortgage
  origination + servicing).

## Prior versions

None for 2026-07-17. Earlier RKT deep dives exist on **2026-05-20** and
**2026-06-05** in `research/RKT/` — not the same date, so no versioning applies;
phase-0.5 self-history may reference them for drift context.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical available-dates --json` | latest options/darkpool/oi/hotchains/screener = 2026-07-17 ← `.<ds>[] \| sort \| tail -1` | all datasets |
| `uw options-flow unusual-volume --symbol RKT --top-n 1 --date 2026-07-17 --json` | top=Aug14 $15P, vol 322, prem $44,540 ← `.results[0]` | top-1 |
| `fz quote RKT --agent` | MktCap 41.14B, EV 69.84B, Sales 8.33B ← `.fundamentals` | full |
| local: `ls "$STOCKS_DIR/Stock Screener/"` | latest local = 2026-07-17; DUCKDB=yes | dir listing |

## Tool errors

None. (`fz quote` succeeded but carries a reduced field set for RKT — a data-scope
limitation, not a tool error; recorded above.)

## DATA NOTE / CORRECTION

Initial `jq` on unusual-volume used `.data`/`.results[0]` paths that returned null
because the payload nests under `.results`. Re-read against `.results[0]` and all
values above trace to that validated path. `fz` float fields probed via both
`fz quote` and `fz screener`; neither returned a float value → recorded n/a
rather than transcribed.

## Verdict for downstream phases

- **Bias from this phase:** neutral (intake only)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. RKT is a **thin options name** — top unusual-volume print is a $44.5k-premium
     put; treat single large prints as signal but don't assume liquidity depth.
  2. As-of **2026-07-17 is the true latest date** on every dataset → point-in-time
     read is clean; no staleness adjustment needed.
  3. `fz` float / short-float is **unavailable** for RKT via CLI → phase-7c SI/float
     and phase-2/3 %-of-float go to WebSearch/advisory. Market cap $41.14B, EV
     $69.84B carried as scale anchors.
- **Open questions:** current spot price and recent range (phase 0.5 / phase 1);
  whether the modest options premium reflects a genuinely quiet tape or just a
  low-multiple large-cap that trades mostly in stock.
