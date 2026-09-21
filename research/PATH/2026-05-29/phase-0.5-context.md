# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-0-intake.md (price $11.72, short float 31.15%, float 412M)

## Summary

PATH had a **busy options session in absolute/percentile terms but a weak,
near-balanced net-directional signal.** On the local screener
(`stock-screener-2026-05-29.parquet`, ~6,000 optionable names) PATH sits in the
**95.3rd percentile on total option premium** and **93.3rd on net-directional
premium**, and its own 35-session history puts today at the **97.1st percentile
for total premium** — i.e. one of the busiest options days for the name in the
local window. **But** the net flow is essentially flat: bullish premium $5.31M
vs bearish $5.08M (`uw insights deep-dive`), and on the order-book net basis
*both* calls (net −$160K) and puts (net −$393K) saw net **selling**, netting to
only a mild bullish lean (puts sold harder than calls). Much of the gross call
volume is **0DTE** (the top OI changes are all same-day-expiry 12C/12.5C/13C).
High heat, low conviction. PATH is **not** in the top-50 single names on either
the bullish or bearish premium board — those are dominated by software/AI
mega-caps — so the percentile (cross-universe) read, not the leaderboard, is the
honest one here.

## Universe ranking

- Net-bullish premium leaderboard (top-50, single names): PATH **outside top-50**.
  Leaders: MSFT (+$136M), DELL (+$122M), ORCL (+$60M), PLTR (+$57M), NOW (+$46M),
  CRWD (+$43M), plus IGV (software ETF) #11 — a clean **software/AI-led tape**.
- Net-bearish premium leaderboard: PATH **outside top-50** (leaders are index
  SPXW/SPX/SPY hedging + ASTS/GOOG/TSLA/INTC).
- Volume-vs-average (ratio ≥ 2): PATH **outside top-80** in *absolute* ratio
  terms (it is a high-baseline name, ~36.6M avg share volume), yet its
  cross-universe percentile on the option/share-volume metric is 92.8 — high
  relative rank, unremarkable absolute multiple.
- Exact universe percentiles `[CTX:universe_pctile DUCKDB]`: total premium
  **95.3**, net-directional **93.3**, IV-rank **58.4**, vol-vs-avg **92.8**.

## Sector read

Today's directional tape is **software/AI-led and in favour**: MSFT, ORCL, NOW,
CRWD, PLTR all top of the bullish board, IGV (software ETF) #11, with OKTA, DDOG,
DOCN, ADBE, CRM also bid. PATH is a Technology/software name, so its **sector is
leading** — a cross-sectional tailwind, not a headwind. This is the *favourable*
configuration (name-strong-into-strong-sector); hands phase-6 a sector-in-favour
prior. Caveat for phase-6: the strength is concentrated in profitable mega-cap /
AI-infrastructure software, not necessarily small-cap unprofitable automation
software like PATH.

## Self-history

`[CTX:self_pctile DUCKDB]` across **35 available local sessions** (non-contiguous
— the 2026-03-28→04-26 gap means this is 35 *available* days, not a calendar
window): net-directional premium **73.5th** percentile, total premium **97.1st**
percentile. Read: busiest activity day, only moderately elevated direction.

## Source

`uw insights deep-dive` + `uw screener bullish-bearish` (both directions) +
`uw screener volume-vs-average` (CLI) **plus** DuckDB §C exact percentiles
(universe + 35-session self-history). "Outside top-50/80" recorded as
information, not error.

## Verdict for downstream

```
universe_pctile_total_prem:  95.3
universe_rank_net_dir:       outside top-50 (universe pctile 93.3)
sector_leadership:           Software/Tech is LEADING today (in favour)
iv_rank:                     43.3 (insights) / 58.4 universe-pctile
implied_move_pct:            1.63% (daily implied move, uw insights)
self_pctile_net_dir:         73.5  (35-session window)
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Why BUSY_NAME_NORMAL_DAY, not GENUINELY_UNUSUAL:** activity percentiles clear
the bar (95th universe / 97th self on total premium) but the *directional*
criteria do not — self net-dir percentile 73.5 (< 80 threshold), net flow is
near-balanced with both calls and puts net-sold, and the call volume that
inflates the gross is dominated by 0DTE pin/lottery strikes. Per
`rubrics/confluence-scoring.md`, **phases 1–2 confluence is capped at `+`
(not `++`)**: the tape is heavy but the conviction is not clean-directional.
Downstream phases should treat the bullish lean as *tentative* and lean on
positioning/OI/structure (phases 3–4) and the heavy 31% short float (phase 7c)
to resolve direction.
