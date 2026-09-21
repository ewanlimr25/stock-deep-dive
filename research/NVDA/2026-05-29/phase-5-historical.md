# Phase 5 — Historical Context & VRP

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T14:10Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

Today's signals sit in a **neutral, no-edge-from-vol historical context**: IV is
**fair** (VRP +0.016, IV30d 40.2% ≈ realized 38.6%), IV percentile **44th
(NORMAL)**, and P/C z-score **+0.15 (no sentiment extreme)** — nothing is
stretched. The GEX regime has been **stably POSITIVE (dealers long gamma) every
session in the window** (last flip 2026-03-25), confirming phase-4's
mean-reverting read is structural, not a one-day artifact. The dominant
multi-day backdrop is the **−10.4% pullback over 10 sessions** (235.74→211.14)
inside a still-intact longer uptrend (price > SMA50/SMA200 per `fz`). The
signal-backtest for the operative **bearish_flow** signal is a coin-flip
(**win_rate 50%, n=8**, small) — but the two NVDA-specific firings (May 26 & 27)
both resolved **down** (−1.6%, −0.7%). 90-day cumulative premium flow is
**net −$292M (MIXED)**. **Net: this is a low-vol, mean-reverting, no-historical-
edge tape. The bearish lean from phases 2–4 has only a weak (50%, tiny-N)
empirical backtest behind it → phase-9 should size small and lean on the
conviction bin, not the backtest. Conviction that today is edge-positive: 2/5.**

## Key signals

- [HIST:vrp] **VRP +0.0158, regime FAIR** (IV30d 40.22% vs realized 38.63%) — no
  premium-buying or -selling edge; IV ≈ RV.
- [HIST:iv-percentile-zscore] IV percentile **44.12 (NORMAL)**, z-score −0.344,
  current IV30d 40.22% over **34 dates** (gap-shortened window).
- [HIST:pc-ratio-zscore] P/C z-score **+0.148 (NORMAL)** — current 0.424 vs
  20-day mean 0.416; **no sentiment extreme**, no contrarian trigger.
- [HIST:gex-time-series] **Regime stably POSITIVE all window** (last flip
  2026-03-25 NEG→POS); 2026-05-29 total_gex +$263M, zgl ~1.6% — phase-4's
  long-gamma/mean-reversion read is **persistent**, not a blip.
- [HIST:signal-backtest] **bearish_flow win_rate 50.0% (n=8)**, avg move 0.73%;
  the two NVDA firings (05-26, 05-27) both went **down**. Small-N, in-sample —
  low confidence.

## Detailed findings

### IV regime (percentile + z-score + VRP)

- VRP **+0.0158 → FAIR**; IV30d 40.22%, realized30 38.63%. No structural edge for
  buying or selling premium — directional structures should be near-delta-neutral
  on vega, not vol bets.
- IV percentile **44th** of trailing window (34 dates, NORMAL), z −0.344 — IV is
  mid-range, slightly below average. Cheap-enough for debit structures but not a
  screaming buy.

### Cumulative premium flow (90d)

- cumulative_bullish $22.83B vs cumulative_bearish $23.13B → **net −$291.9M**,
  `trend_direction: MIXED` over 35 sessions present (gap 03-28→04-26 excluded —
  `dates_covered` confirms the hole). The 90-day net is **mildly negative** — no
  stealth institutional *accumulation* signature; if anything a slight bearish
  premium lean over the quarter.

### P/C ratio z-score

- z +0.148, `extreme: NORMAL`. Sentiment is unremarkable — neither capitulation
  nor euphoria. No contrarian setup.

### GEX time series (regime stability)

| date | regime | total_gex | zgl |
|------|--------|-----------|-----|
| 05-22 | POSITIVE | $132.8M | — |
| 05-26 | POSITIVE | $413.3M | — |
| 05-27 | POSITIVE | $192.9M | — |
| 05-28 | POSITIVE | $469.8M | — |
| 05-29 | POSITIVE | $263.0M | ~1.6% |

No regime flip since 2026-03-25. **Dealers have been long gamma throughout the
pullback** — which explains why the −10% decline has been an orderly grind rather
than a crash: long-gamma dealers buy dips. The phase-4 mean-reversion regime is
the persistent state.

### OI trend

- `overall_trend: BUILDING`, **30 consecutive build days**, total_net_oi_change
  +12,845,016. OI is steadily accreting — but recall phase-3: the recent marginal
  builds are aggressor-balanced/written calls + downside puts, not clean bullish
  accumulation. Rising OI into a falling price = positions being layered both ways.

### Multi-day trend table (IV rank collapse alongside price)

| date | close | IV rank | P/C |
|------|-------|---------|-----|
| 05-14 | 235.74 | 76.58 | 0.376 |
| 05-20 | 223.47 | 60.99 | 0.457 |
| 05-21 | 219.51 | 34.16 | 0.432 |
| 05-22 | 215.33 | 27.26 | 0.470 |
| 05-27 | 212.60 | 30.51 | 0.396 |
| 05-29 | 211.14 | 40.65 | 0.424 |

Note IV rank **collapsed** from ~77 (05-14) to ~27–40 even as price fell ~10% —
i.e. the decline came *with falling implied vol*, a calm/orderly pullback (no fear
bid in options), consistent with the long-gamma regime. price_change over the
full 30-session window: 172.7 → 211.14 (the early-window 172.7 is pre-gap, late
March — do not read as a contiguous +22%).

### Price context (`fz`, advisory cross-check)

- [HIST:rsi fz] **RSI(14) 49.4** — dead neutral, no oversold bounce setup.
- [HIST:52w_proximity fz] **−10.74% from 52w high** (236.54), **+58.85% above 52w
  low** (132.92). Perf YTD +13.2%, Perf Month +0.9%.
- SMA stack: price **−2.0% vs SMA20** (below short-term), **+5.9% vs SMA50**,
  **+12.5% vs SMA200** — a **short-term pullback within an intact longer uptrend**.
  Tempers the bearish read: the longer trend is still up; this is a correction,
  not (yet) a breakdown.

### Signal backtest (bearish_flow — operative signal per phases 2–4)

- **win_rate 50.0%, total_signals 8**, avg_move 0.73%, lookback 5 trading days.
- NVDA-specific firings: 2026-05-27 −0.69%, 2026-05-26 −1.64% (both **down** =
  bearish signal "won" on NVDA). Other names (MU/AMD/SNDK) went up (semis bounce),
  dragging the basket win-rate to 50%.
- Methodology caveat (tool's own): "in-sample backtest — not a robust live edge."
  Small N → low confidence; do not over-anchor.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw historical vrp --symbol NVDA --realised-window-days 30 --json` | FAIR, VRP +0.016 |
| `uw historical iv-percentile-zscore --symbol NVDA --lookback-days 252 --json` | 44th pctile, NORMAL (34 dates) |
| `uw historical pc-ratio-zscore --symbol NVDA --lookback-days 20 --json` | z +0.15, NORMAL |
| `uw historical gex-time-series --symbol NVDA --days 30 --dte-max 45 --json` | stably POSITIVE, no flip since 03-25 |
| `uw historical oi-trend --symbol NVDA --days 30 --top-n 10 --json` | BUILDING, 30 consec days |
| `uw historical cumulative-premium-flow --symbol NVDA --days 90 --json` | net −$292M, MIXED |
| `uw historical trend --symbol NVDA --days 30 --json` | IV rank collapse w/ price; orderly pullback |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | win_rate 50%, n=8 |
| `fz quote NVDA --agent` | RSI 49.4, −10.7% from 52w high, >SMA50/200 |

## Tool errors

```
# Gap-awareness: iv-percentile-zscore reports dates_used=34, cumulative-premium-flow
# dates_covered shows the 03-28→04-26 hole explicitly. No silent interpolation
# observed. Trailing tools (iv/pc z-scores, oi-trend, cumulative-flow, backtest)
# anchor to latest available date (2026-05-29) — a re-run after a new session shifts
# these reads (latest-anchor caveat).
# trend `total_volume`/`net_premium` per-day fields returned None (not populated);
# close/iv_rank/pcr used instead — cross-checks phase-0.5 self-history exactly.
```

## Verdict for downstream phases

- **Volatility regime:** FAIR (IV ≈ RV; 44th pctile) — **no vol edge**; cheap-enough
  for debit but not a vol play.
- **Environment:** neither premium-buying nor -selling favored (VRP ~0).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5** —
  bearish_flow backtest is a 50% coin-flip on tiny N; longer trend still up (fz),
  which cuts against the near-term bearish lean.
- **Three specific datapoints:** IV percentile **44.12**; VRP **+0.0158 (FAIR)**;
  bearish_flow signal **win_rate 50.0% (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.50
  win_rate_n:                8
  win_rate_source:           backtest
  ```
  (Small N=8 → phase-9 must apply the N-conditional cap; effectively fall back
  toward the conviction bin per `rubrics/sizing-rubric.md`.)
- **Open questions:** Does macro/sector (phase-6) push the 210 gamma-hinge?
  Does fundamentals (7b) / sentiment (7c) add a downside catalyst, or does the
  intact longer uptrend + neutral RSI argue this pullback simply mean-reverts up
  inside the 210–220 range?
