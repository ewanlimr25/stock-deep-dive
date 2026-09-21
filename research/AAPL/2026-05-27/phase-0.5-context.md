# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:52:00Z
**Upstream phases cited:** phase-0-intake.md

## Summary

AAPL is **cross-sectionally extreme but self-historically ordinary** today. It
ranks **9th in the entire optionable universe** on net bullish premium (~7th
among single names, behind META/TSLA/ASTS/IREN/APP/AXTI), placing it in the
**top 0.2%** (99.8th universe pctile) on both total and net-directional premium.
But against its own 33-session window, today's net-directional premium of
**$17.4M sits right at AAPL's window mean ($17.79M)** — self-pctile only **71.9**
(below the 80 GENUINELY_UNUSUAL bar) — and **total option volume is *below* its
own 30-day average** (vol_x 0.82, outside the universe top-50 on volume-vs-avg).
IV rank is low-mid (32, universe pctile 37). **Verdict: BUSY_NAME_NORMAL_DAY** —
the bullish tilt is genuine but unremarkable in magnitude *for AAPL*; phases 1–2
confluence is therefore capped at `+` (not `++`) per the scoring rubric.

## Universe ranking (today, 2026-05-27)

AAPL net bullish premium **rank 9 of universe** `[CTX:universe_rank_net_dir]`:

| Rank | Ticker | net_flow ($) | Note |
|------|--------|--------------|------|
| 1 | SPXW | 111.4M | index (set aside) |
| 2 | META | 61.7M | mega-cap tech |
| 3 | TSLA | 54.8M | mega-cap |
| 4 | ASTS | 32.5M | space |
| 5 | IREN | 30.8M | bitcoin/AI |
| 6 | APP | 29.1M | adtech |
| 7 | AXTI | 25.3M | semi |
| 8 | SOXL | 24.4M | semi 3x ETF |
| **9** | **AAPL** | **17.4M** | **<<< this name** |
| 11 | SPY | 14.4M | index (set aside) |
| 12 | AMZN | 12.5M | mega-cap |

- **Universe percentiles (DuckDB §C, today, all ~optionable names):**
  total premium **99.8** · net-directional **99.8** · IV rank **37.0** ·
  volume-vs-avg **57.4** `[CTX:universe_pctile DUCKDB]`.
- AAPL is outside the top-50 on **volume-vs-average** (today's volume is *not*
  unusual vs its own 30-day average) — the volume leaders are illiquid microcaps
  (PRA, MBC, XCEM with absurd >1000x ratios), not AAPL.

## Sector read

Today's bullish tape is **tech/semis-led**: of the top single-name bullish flows,
META (mega-cap tech), TSLA, then a cluster of semis/AI/space (ASTS, IREN, APP,
AXTI, SOXL). **Technology is in favour today** and AAPL is *participating* in that
leadership, not leading it (rank 9, behind META). This is a green-ish backdrop for
the macro phase (phase-6) to confirm: name strong + sector strong = the favourable
cross-sectional configuration, **but** AAPL lags the mega-cap leader (META) and the
hotter semis. No yellow flag (name is not strong into a sector being sold).

## Self-history (DuckDB §C — parquet present, N=33 sessions)

| Metric | Today | Window mean | Window max | Self-pctile |
|--------|-------|-------------|------------|-------------|
| net-directional premium | $17.4M | $17.79M | $156.47M | **71.9** `[CTX:self_pctile DUCKDB]` |
| total premium | (top of range) | — | — | **93.8** |
| volume-vs-avg (vol_x) | 0.82 | 0.72 | — | (below 1.0) |

**Read:** Today's *net bullish* premium is essentially **AAPL's average day** —
its own max net-directional day in the window was $156M, ~9x larger. Total
premium is near its window high (93.8 pctile = busy), but that busyness is *broad
two-way activity*, not concentrated directional conviction. Volume is below its
own 30-day average. **This is the signature of a busy mega-cap on a normal day,
not a name being aggressively positioned.**

## Source

CLI (`uw screener` bullish/bearish, volume-vs-average, iv-rank; `uw insights
deep-dive`) **+ DuckDB §C** (exact universe + self-history percentiles; parquet
present for 2026-05-27, N=33 sessions, non-contiguous — gap Mar-27→Apr-27).
"Outside top-N" recorded for: volume-vs-average, high-IV-rank.

## Verdict for downstream — `[CTX:]` block (phases 1, 5, 9 read verbatim)

```
universe_pctile_total_prem:  99.8
universe_rank_net_dir:       9
sector_leadership:           TECHNOLOGY is leading today (AAPL participating, not leading; lags META)
iv_rank:                     32.05
implied_move_pct:            1.19          # implied_move $3.69 on ~$311 spot; feeds phase-9 N4
self_pctile_net_dir:         71.9          # DuckDB, N=33 — BELOW the 80 unusual bar
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

- **Bias from this phase:** neutral (context only — sets no directional bias).
- **Conviction modifier:** caps phases 1–2 confluence at `+` (not `++`); see
  `rubrics/confluence-scoring.md` and `rubrics/sizing-rubric.md` context modifier.
- **Three things later phases should remember:**
  1. Cross-sectionally top 0.2% / rank 9, but **self-pctile only 72** and
     today's net_dir ≈ window mean — magnitude is *average for AAPL*.
  2. Volume is **below** AAPL's own 30-day average (vol_x 0.82) — no volume thrust.
  3. IV rank 32 (low-mid) and **next earnings 2026-07-30** — no near-term earnings
     catalyst; implied move only 1.19%.
- **Open questions:** Is the rank-9 bullish premium led by genuine directional
  sweeps/blocks or by 0DTE/short-dated pin noise? → phase-1 to resolve (note the
  top OI changes are 0–2DTE 310–315 calls, hinting at short-dated/pin activity).
