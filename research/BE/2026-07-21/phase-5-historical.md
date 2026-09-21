# Phase 5 — Historical Context & VRP

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:25:00Z
**Upstream phases cited:** phase-4-structure.md, phase-1-flow.md, phase-3-positioning.md, phase-0-intake.md

## Summary

The historical lens turns today's flow into a **bounce-confirmation story, not a
fresh breakout.** BE **peaked ~$345.85, collapsed to a $197.06 low yesterday
(7/20), then rallied +14.8% to $226.26 today (7/21)** — and *today* is when flow
flipped to its record net-bullish lean (phase-0.5). Institutions wrote puts and
built LEAP calls at the exact 197.5 floor where price just bottomed — a
high-conviction bottom-confirmation. IV is **pinned at the 1-year max (100th
pctile, z +2.81)** and **VRP is +0.49 (PREMIUM_SELLING regime)** — options price
far more vol than realized, so **credit/premium-selling structures are the
historically edge-positive expression** (validating the phase-1 put-writers).
Two caveats keep conviction honest: the **90-day cumulative flow is net −$441M
(mixed-to-bearish)** — today is a bullish outlier against a heavy-selling
backdrop — and this is a bounce **within a −35%-from-peak downtrend**. OI has
built **30 consecutive days** (+1.29M) into the 7/28 print, and the bullish_flow
signal class backtests at **85.7% but on only N=7** (low-confidence, in-sample).

## Key signals

- **Price path 345.85 → 197.06 (7/20 low) → 226.26 (+14.8% today)** — flow confirms
  the bounce off the 197 floor `[HIST:trend]`
- **IV percentile 100, z +2.81, regime HIGH_IV** (iv30d 1.77, N=69) — 1yr max `[HIST:iv_percentile_zscore]`
- **VRP +0.4935, regime PREMIUM_SELLING** (IV 1.77 vs RV 1.28) — favor credit `[HIST:vrp]`
- **90d cumulative flow net −$441M (MIXED)** — today bullish against a bearish 90d tape `[HIST:cumulative_premium_flow]`
- **OI BUILDING 30 consecutive days, +1,289,076 net** — heavy positioning into earnings `[HIST:oi_trend]`
- **bullish_flow backtest win 85.7%, N=7, avg move +2.75%** (in-sample, low-N) `[HIST:signal_backtest]`

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` / `[HIST:vrp]`

- iv30d **1.7725**, `iv_percentile` **100**, `iv_zscore` **+2.814**, `regime`
  HIGH_IV over **N=69 sessions** (gap-adjusted). IV is at its 1-year ceiling —
  the earnings event + the 345→197→226 round-trip have maxed implied vol.
- VRP **+0.4935** (iv30 1.7725 − realised_vol 1.279), `regime`
  **PREMIUM_SELLING** — "Options pricing more vol than realised — favour premium
  selling." The phase-1 put-write campaign is trading *with* the VRP.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

cumulative_bullish $5.23B vs cumulative_bearish $5.67B → **net −$441,014,631**,
`trend_direction` MIXED, over 70 sessions covered (spans the 03-28→04-27 gap). The
90-day tape leans **net bearish** — today's +$25.5M bullish day is a *reversal
signal against* that backdrop, which cuts both ways: strong if it's a genuine
turn, weak if it's a one-day bounce in flow.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current_pc 2.0459 vs 20d mean 1.4988, z **+0.853**, `extreme` **NORMAL**. Today's
elevated P/C (from heavy put *volume*) is only +0.85σ — **not** a sentiment
extreme, so no contrarian-fade trigger. Consistent with phase-1 (the puts are
written, not panic-bought).

### GEX time series (30d) `[HIST:gex_time_series]`

Unstable dealer regime — **3 regime flips** in 30d: 2026-06-23 POS→NEG (spot
321), 06-25 NEG→POS, 06-30 POS→NEG, now FULLY_NEGATIVE (phase-4). The repeated
flips + the 321→226 slide = a high-range, trend-amplifying month. Expect wide
post-earnings ranges (reinforces phase-4 short-gamma read).

### OI trend (30d) `[HIST:oi_trend]`

`overall_trend` **BUILDING**, `consecutive_build_days` **30**, `total_net_oi_change`
**+1,289,076**. Uninterrupted 30-session OI accumulation into the 7/28 print —
positioning is being layered on aggressively, not unwound.

### Multi-day trend table `[HIST:trend]` (N=30, 2026-06-08 → 2026-07-21)

- `bullish_days` **9** vs `bearish_days` **21** (70% down days) — a month-long
  decline.
- `price_change` window endpoints **253.57 → 226.26** (−10.8%); intra-window
  **max 345.85, min 197.06** — the real path is a ~35%-from-peak drawdown to a
  7/20 capitulation low, then the +14.8% 7/21 bounce.
- `iv_rank_change` **56.4 → 98.78** — fear/IV ramped throughout.
- `flow_direction_latest` **bullish** — the last session (today) is the bullish
  inflection.

### Price context (`fz`) — omitted

`fz quote BE` returned a degraded 14-field block with **null RSI / SMA50 / SMA200
/ Perf / 52W** (same partial response as phase-0). No independent EOD technical
cross-check available; skipped per spec (advisory only).

### Signal backtest `[HIST:signal_backtest]` (bullish_flow, market-wide)

`win_rate` **85.7%**, `total_signals` **N=7**, `avg_move_pct` **+2.75%**.
Methodology (verbatim): *"fraction of signals where forward move agrees with the
signal's direction … In-sample backtest — not a robust live edge."* High base
rate but **N=7 is below the 10-firing confidence floor** — phase-9 must apply the
N-conditional Kelly cap, not size on 0.857 naively. This is a **market-wide base
rate** for the signal class, not a BE-specific rate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | N / anchor |
|------------------|--------------------------|------------|
| `historical iv-percentile-zscore --symbol BE --lookback-days 252` | pctile 100, z +2.81 ← `.iv_percentile/.iv_zscore` | N=69, latest-anchored 2026-07-21 |
| `historical vrp --symbol BE --realised-window-days 30` | vrp +0.4935 PREMIUM_SELLING ← `.vrp/.regime` | latest-anchored |
| `historical cumulative-premium-flow --symbol BE --days 90` | net −$441M ← `.net_flow/.trend_direction` | 70 sessions (gap) |
| `historical pc-ratio-zscore --symbol BE --lookback-days 20` | z +0.853 NORMAL ← `.zscore/.extreme` | 20d |
| `historical gex-time-series --symbol BE --days 30` | 3 flips ← `.regime_flip_dates` | 30d |
| `historical oi-trend --symbol BE --days 30` | BUILDING 30d, +1.29M ← `.overall_trend/.consecutive_build_days` | 30d |
| `historical trend --symbol BE --days 30` | 197.06 low 7/20 → 226.26 ← `.daily_data[]｜.price`; max 345.85/min 197.06 | 30d, 6/08–7/21 |
| `historical signal-backtest --signal-type bullish_flow --lookback-days 5` | win 85.7%, N=7 ← `.win_rate/.total_signals` (top-level) | market-wide |

## Tool errors

<none — all eight reads valid JSON.> **Latest-anchor note:** every trailing
command (iv-pctile, vrp, pc-z, oi-trend, gex-series, trend, cumulative-flow,
signal-backtest) anchors to the latest available date, which **equals the as-of
2026-07-21**, so this run is point-in-time-correct; a re-run after 7/22+ (incl.
the 7/28 earnings) would shift every trailing read.

## DATA NOTE / CORRECTION

- Apparent conflict — GEX series spot 321 (6/23) vs trend endpoints 253.57→226.26
  — resolved: NOT a data error. `daily_data` min/max is 197.06/345.85, so the
  stock round-tripped 345→197→226 inside the window; the trend `price_change` field
  only reports the two window *endpoints* (6/08 & 7/21), masking the peak/trough.
  Verified via `.daily_data[]｜.price`.

## Verdict for downstream phases

- **Volatility regime:** **RICH** (IV 100th pctile, z +2.81, VRP +0.49) →
  **premium-SELLING** environment. Favor **credit structures** (put spreads sold /
  cash-secured puts), not long premium — long options bleed the IV crush.
- **Historically edge-positive?** **Yes, qualified.** Today's bullish flow confirms
  a bounce off a triple-verified 197 floor in a premium-selling regime (edge-
  positive), and OI has built 30 straight days. But it is a bounce **within a
  downtrend**, the 90d flow is net −$441M, and the 85.7% backtest is only N=7.
  Net conviction: **3.5 / 5** on the signal being edge-positive.
- **Three specific datapoints:** IV %ile **100** (z +2.81); VRP **+0.4935**
  (PREMIUM_SELLING); bullish_flow win-rate **85.7% / N=7**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.857
  win_rate_n:                7
  win_rate_source:           backtest
  ```
  (Kelly `p` = 0.857 but **N=7 < 10** → apply the N-conditional cap in
  `rubrics/sizing-rubric.md`; this is a market-wide base rate, not BE-specific.)
- **Open questions:** Will the 7/28 earnings realize the ~10.6% implied move
  (short-gamma says likely)? Does the fundamental picture (phase-7b) justify the
  bounce, or is the −35% drawdown fundamentally warranted? Is the 197 low a
  durable floor or a waypoint lower if the print misses?
