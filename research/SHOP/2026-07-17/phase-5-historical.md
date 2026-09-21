# Phase 5 — Historical Context & VRP

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md

## Summary

Two horizons disagree, and that is the headline. **Near-term (5d) the tape rewards
bearish flow**: the `bearish_flow` signal class backtests **100% win (n=10, avg 5d
move −5.22%)** while `bullish_flow` is **failing at 14.3% (n=7)** — the current
regime punishes longs and pays shorts. **But the medium-term structure is bullish**:
90-day cumulative premium is **net +$125M bullish** (BULLISH trend), OI has been
**BUILDING 30 straight days** (+284k net contracts), and price rose **116.04 → 123.56
(+6.5%)** over 30 sessions. So today's phases-1–4 downside lean is a **pullback within
a bullish accumulation base**, not a trend break. **Vol is RICH** — IV at the **98.5th
percentile** (z +2.03, IV30 0.75) with **VRP +0.31 → PREMIUM_SELLING regime** — so a
bearish expression should lean **credit / spread**, not outright long puts. P/C
z-score is **NORMAL** (0.9185, z −0.002): no sentiment extreme, no contrarian trigger.

## Key signals

- **`bearish_flow` backtest: 100% win, n=10, avg 5d move −5.22%** (in-sample,
  market-wide). `[HIST:signal_backtest]`
- **`bullish_flow` backtest: 14.3% win, n=7** — bullish flow is not working now. `[HIST:signal_backtest]`
- **90d cumulative premium net +$125M BULLISH** (bull $803M / bear $678M, 68 dates). `[HIST:cumulative_premium_flow]`
- **IV 98.5th percentile, z +2.03; VRP +0.31 → PREMIUM_SELLING** (IV30 0.75 vs RV30
  0.45). `[HIST:iv_percentile_zscore] [HIST:vrp]`
- **OI BUILDING 30 consecutive days** (+284k); price +6.5% over the window. `[HIST:oi_trend] [HIST:trend]`

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore] [HIST:vrp]`

- IV percentile **98.51** (over **67 dates used**, not the full 252 — lookback data
  limited/gap-affected; low-confidence on the exact percentile but clearly rich),
  iv_zscore **+2.031**, current IV30d **0.7529**, regime `HIGH_IV`.
- VRP **+0.3065** (IV30 0.7529 − RV30 0.4464), regime **PREMIUM_SELLING** —
  "Options pricing more vol than realised — favour premium selling." → phase-9 should
  prefer **credit structures / debit spreads** over naked long premium.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

cumulative_bullish **$803.4M** vs cumulative_bearish **$678.4M** → **net +$125.0M,
trend BULLISH** (68 dates). The durable premium base is bullish; the last-8-session
bearish tilt (phase-0.5) is a small counter-trend inside it.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current 0.9185, mean 0.919, std 0.298, **z −0.002 → NORMAL**. Sentiment sits exactly
at its 20-day mean — **no extreme, no contrarian setup**.

### GEX time series (regime flips) `[HIST:gex_time_series]`

Whippy in late June — flips 6/25 POS→NEG (spot 113), 6/26 NEG→POS (116.75), **6/29
POS→NEG (spot 115, ZGL 134.35)** — then **stable NEGATIVE (short-gamma) since ~6/29**,
ZGL parked ~134 while spot climbed 115→123.56. The +6.5% up-move happened *inside*
short gamma (amplification cuts both ways); spot still **below** ZGL 134.98. No fresh
flip in the last 5 days → current short-γ regime is ~3 weeks mature, not a transition.

### OI trend `[HIST:oi_trend]`

overall_trend **BUILDING**, **consecutive_build_days 30**, total_net_oi_change
**+284,119**. Sustained buildup (not a spike/decay) — corroborates the bullish 90d
premium as genuine position accumulation, not churn.

### Multi-day trend (30d: 2026-06-04 → 07-17) `[HIST:trend]`

price_change **116.04 → 123.56 (+6.5%)**, bullish_days 13 / bearish_days 17,
iv_rank_change **50.65 → 85.65** (vol re-rated up hard), flow_direction_latest
**bearish**. A grind higher on rising IV, with the most recent flow turning bearish.

### Price context (`fz`)

`fz quote` returned a **partial cut again** — RSI(14), SMA50/200, Perf, 52W High/Low
all null (same degraded-quote condition as phase-0). **Advisory cross-check omitted**
(`fz_available=yes` but the technical fields did not populate). Does not affect Kelly `p`.

### Signal backtest (the Kelly `p` input) `[HIST:signal_backtest]`

`--signal-type bearish_flow --lookback-days 5` (market-wide): **win_rate 100.0%,
n (total_signals) = 10, avg_move_pct −5.22%.** Methodology note: *"In-sample
backtest — not a robust live edge... selection is positional within the yfinance bar
series."* → treat as a **directional confirmation, not a literal 100% edge**; small
N + in-sample demand a hard cap in phase-9 sizing. Contrast: `bullish_flow` 14.3%
(n=7); `dark_pool_accumulation` returned the empty stub (n=0).

## Tool calls (audit trail)

| Command | Key value ← `jq` path | N |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol SHOP --lookback-days 252` | 98.51, z +2.03 ← `.iv_percentile,.iv_zscore` | 67 dates |
| `uw historical vrp --symbol SHOP --realised-window-days 30` | +0.3065, PREMIUM_SELLING ← `.vrp,.regime` | 30d |
| `uw historical cumulative-premium-flow --symbol SHOP --days 90` | +$125.0M BULLISH ← `.net_flow,.trend_direction` | 68 dates |
| `uw historical pc-ratio-zscore --symbol SHOP --lookback-days 20` | z −0.002 NORMAL ← `.zscore,.extreme` | 20d |
| `uw historical gex-time-series --symbol SHOP --days 30` | stable NEG since 6/29 ← `.regime_flip_dates` | 30d |
| `uw historical oi-trend --symbol SHOP --days 30` | BUILDING, 30 build days ← `.overall_trend,.consecutive_build_days` | 30d |
| `uw historical trend --symbol SHOP --days 30` | +6.5%, ivr 50.6→85.6 ← `.price_change,.iv_rank_change` | 30d |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5` | 100%, n=10, −5.22% ← `.win_rate,.total_signals,.avg_move_pct` | 10 |

## Tool errors

<none> — but two data-quality caveats: (1) IV percentile used only 67 dates (not
252) → gap/limited-history, exact percentile low-confidence; (2) `fz` technical
fields null (partial quote) → fz price-context cross-check skipped. Latest-anchor
note: all trailing commands anchor to latest available date = 2026-07-17 (= as-of).

## DATA NOTE / CORRECTION

VRP/IV field names corrected on second read (`.vrp`, `.iv_percentile`,
`.cumulative_bullish`/`.cumulative_bearish`/`.net_flow`, `.regime_flip_dates`).
Values above trace to those exact paths.

## Verdict for downstream phases

- **Volatility regime:** RICH — IV 98.5 %ile, VRP +0.31, PREMIUM_SELLING. **Sell/spread
  premium, don't buy it outright.**
- **Environment:** near-term rewards bearish flow (bearish_flow 100%/n10 vs bullish
  14%/n7); medium-term is bullish accumulation (90d +$125M, OI building 30d).
- **Conviction that TODAY's signal is edge-positive:** 3/5 — the **near-term (≤5–10d)
  bearish fade is edge-positive**, but only tactically; the medium-term base fights a
  sustained short. This is a **pullback-fade, not a position short.**
- **Three datapoints:** IV %ile **98.5**; VRP **+0.31**; bearish_flow win **100% (n=10,
  −5.22% avg)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  1.00
  win_rate_n:                10
  win_rate_source:           backtest
  ```
  Caveat for phase-9: market-wide, in-sample, small N → apply the N-conditional cap
  hard; do NOT size to a literal 100% `p`. The bullish 90d base is a size-down flag.
- **Open questions:** Does the fundamental/valuation picture (phase-7b) justify the
  medium-term bullish base, or is the stock stretched (mcap $160B, sales $12.4B →
  ~13× sales)? Does sentiment/positioning (phase-7c) show crowding that a near-term
  fade could squeeze?
