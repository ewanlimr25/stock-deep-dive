# Phase 5 — Historical Context & VRP

**Ticker:** DOCN
**As-of date:** 2026-07-17 (== latest available → trailing reads are as-of reproducible)
**Generated:** 2026-07-20T01:52:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The single most important context this phase adds: **DOCN has crashed ~34% in 30
days — from $180.50 (6/04) to $118.91 (7/17)** — and today's IV rank 99 / IV
percentile **100** is the volatility of a *falling* stock, not an accumulation
setup. IV30d 114.6% vs realized 71.2% gives **VRP +0.434 → a PREMIUM-SELLING
regime** (options are very rich even after the drop). The dealer GEX regime
**flipped 6 times** during the June–July slide (violent, unstable) and has only
now settled back to POSITIVE (long gamma) at $119, pinning a $115–128 range into
**8/4 earnings**. Crucially, the **`bullish_flow` signal backtests at a 14.3%
win-rate** — today's mild bullish tape (phase-1) is *historically edge-negative*.
This reframes the whole workup: **fallen name basing at $115–120, rich vol,
premium-selling favored, bullish conviction not supported by history.**

## Key signals

- **Price −34% in 30d: $180.50 → $118.91** `[HIST:trend]` — the decisive context
  every earlier phase read without: this is a downtrend, not a base being bought.
- **IV percentile 100, z +2.03, regime HIGH_IV** (IV30d 114.6%) over 67 sessions
  `[HIST:iv_percentile_zscore]` — vol at the top of its 1-year range.
- **VRP +0.434, regime PREMIUM_SELLING** (IV 114.6% ≫ realized 71.2%)
  `[HIST:vrp]` — favor credit / premium-selling structures, not long premium.
- **`bullish_flow` backtest win-rate 14.3% (n=7)** `[HIST:signal_backtest]` —
  market-wide base rate; a bullish read here has been a historical loser → this is
  the Kelly `p` and it caps size hard.
- **6 GEX regime flips in 30d** (POSITIVE↔NEGATIVE, 6/22–7/06) `[HIST:gex_time_series]`
  — dealer hedging was unstable through the crash; now settled POSITIVE at spot.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore][HIST:vrp]`

- iv_percentile **100** / iv_zscore **+2.027** / regime **HIGH_IV**, current IV30d
  **114.6%**, over **67 sessions used** (gap-aware N, not 252 calendar — the
  2026-03-28→04-24 hole per phase-0).
- VRP **+0.434**: IV30d 114.6% − realized30 71.2%. Regime **PREMIUM_SELLING** —
  "options pricing more vol than realised — favour premium selling." Vol is rich in
  both absolute (100th pctile) and relative (VRP) terms.

### Price + IV trajectory (30d, 2026-06-04 → 07-17) `[HIST:trend]`

| Date | Close | IV rank |
|------|-------|---------|
| 06-04 | $180.50 | 90.2 |
| 06-17 | $177.81 | 83.6 |
| 06-23 | $157.18 | 93.2 |
| 06-26 | $139.28 | 87.1 |
| 07-07 | $137.04 | 97.8 |
| 07-10 | $130.18 | 92.5 |
| 07-15 | $119.65 | 98.8 |
| **07-17** | **$118.91** | **99.1** |

A persistent, accelerating decline after ~6/17; IV rose *as* price fell (classic
downside vol). 30d flow: **bullish_days 16 / bearish_days 14** — near-even, i.e.
repeated dip-buying attempts that kept failing. This recontextualizes the upside
LEAP OI (180C/200C, phase-1/3): those strikes were near-money in early June and are
now stranded ~50% OTM — consistent with phase-3's **180C Nov OI −430** (holders
closing stranded calls), not fresh bullish opening.

### Cumulative premium flow (90d / 68 sessions) `[HIST:cumulative_premium_flow]`

- net_flow **+$39.9M** (cumulative_bullish $389.8M vs bearish $349.9M ≈ 52.7%
  bull), trend_direction **BULLISH**. Interpretation: a *mild* persistent
  dip-buying bid across the decline — real but not dominant, and it has been on the
  wrong side of a −34% move. Not a stealth-accumulation confirmation.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

- current 0.864, mean 0.756, std 0.964, **z +0.113, extreme NORMAL** — no
  sentiment extreme; no contrarian trigger. (Std is very wide, so the tape's P/C
  has swung a lot during the crash.)

### GEX time series (30d regime stability) `[HIST:gex_time_series]`

- **6 regime flips** in 30 days: 6/22 P→N (spot 162), 6/25 N→P (145), 6/29 P→N
  (147), 6/30 N→P (157), 7/01 P→N (144), 7/06 N→P (133). Dealer gamma was
  whipsawing violently through the decline (trend-amplifying NEGATIVE stretches
  contributed to the slide). It has settled **POSITIVE** into 7/17 at $119 (ZGL 70)
  — a fresh long-gamma stabilization, but young and earnings-threatened.

### OI trend (30d) `[HIST:oi_trend]`

- overall_trend **BUILDING**, total_net_oi_change **+109,810**,
  consecutive_build_days **0**. OI accumulated through the decline (puts + stranded
  calls) but not in a steady consecutive build — episodic, consistent with a
  falling stock attracting both hedgers and bottom-fishers.

### Price context (`fz`, advisory)

- `fz quote DOCN` returns **null** for RSI/SMA20-50-200/Perf/52W (the same sparse
  fundamentals block noted in phase-0) → **no independent fz price cross-check
  available**. Skipped per `lib/fz-recipes.md` graceful-degrade. (The UW trajectory
  above already establishes the down-trend and IV context.)

### Signal backtest `[HIST:signal_backtest]`

- signal-type **bullish_flow** (matched to phase-1's mild-bullish verdict):
  **win_rate 14.3%, total_signals 7**, avg_return null. Market-wide base rate
  (tool has no `--symbol`) over the trailing 5d lookback. Well below the 0.45
  edge floor → **bullish setups have been losing** — downgrade any bullish
  conviction regardless of how the tape looks.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | N |
|---------|--------------------------|---|
| `historical iv-percentile-zscore --lookback-days 252` | pctile 100, z +2.03 ← `.iv_percentile`,`.iv_zscore` | 67 sess |
| `historical vrp --realised-window-days 30` | VRP +0.434, PREMIUM_SELLING ← `.vrp`,`.regime` | 30 |
| `historical trend --days 30` | 180.5→118.91 ← `.price_change`; 16/14 ← `.bullish_days`/`.bearish_days` | 30 (6/04–7/17) |
| `historical cumulative-premium-flow --days 90` | net +$39.9M BULLISH ← `.net_flow`,`.trend_direction` | 68 sess |
| `historical pc-ratio-zscore --lookback-days 20` | z +0.113 NORMAL ← `.zscore`,`.extreme` | 20 |
| `historical gex-time-series --days 30` | 6 flips ← `.regime_flip_dates\|length` | 30 |
| `historical oi-trend --days 30` | BUILDING, +109,810 ← `.overall_trend`,`.total_net_oi_change` | 30 |
| `historical signal-backtest --signal-type bullish_flow` | 14.3%, n=7 ← `.win_rate`,`.total_signals` | mkt-wide |

## Tool errors

(none — all eight calls returned valid JSON. `fz` price-context fields null =
data-coverage gap, not a tool error; cross-check skipped.)

## DATA NOTE / CORRECTION

- Gap-aware N: iv-percentile used **67 sessions** (not 252), cum-premium **68**;
  the 2026-03-28→04-24 hole is excluded — do not annualize across it.
- As-of 2026-07-17 == latest available, so the trailing-anchored reads
  (iv-pctile, vrp realized leg, trend, cum-flow, gex-ts, oi-trend, backtest) are
  reproducible at this as-of; a future re-run after new sessions would shift them.

## Verdict for downstream phases

- **Volatility regime:** **RICH** — IV 100th pctile, z +2, VRP +0.434.
- **Environment:** **PREMIUM-SELLING** — sell expensive optionality; long-premium
  (debit) structures are fighting a −$0.43 VRP headwind and a post-earnings crush.
- **Conviction that today's signal is historically edge-positive:** **1–2/5 for a
  bullish read** (bullish_flow backtests 14.3%; stock in a −34% downtrend). Edge is
  *positive* only for range/premium-selling framing (long gamma + rich VRP).
- **Three specific datapoints:** IV percentile **100**; VRP **+0.434**;
  bullish_flow win-rate **14.3% (n=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.143
  win_rate_n:                7
  win_rate_source:           backtest   # market-wide base rate, NOT DOCN-specific
  ```
- **Open questions:** Is the −34% crash fundamentally driven (guidance cut /
  competitive) or macro/sector de-rate? (phase-6/7b). What did DOCN do historically
  through earnings after a big pre-print drawdown — bounce or continuation?
  (phase-7c earnings behavior). Is $115 a real floor (put-wall + DP support) or a
  shelf before continuation?
