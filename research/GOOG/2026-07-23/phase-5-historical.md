# Phase 5 — Historical Context & VRP

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Latest-anchor note:** trailing commands anchor to latest available date = 2026-07-23
(= as-of; reproducible today). Window is the 72-session cluster; the 21-session hole
(2026-03-28→04-24) predates it, so 30d/90d reads here are gap-free within the cluster.
**Upstream:** phase-4 (long-gamma today, max-pain 350 above spot, complacent skew,
backwardation), phase-3 (OI mixed/building), phase-1 (bearish premium spike)

## Summary

The single most important historical fact: **2026-07-23 is itself a breakdown day
— GOOG fell ~7.1% from 342.95 (07-22 close) to 318.59** in one session (30-day
path 353.32 → 318.34, −9.9%). That one move explains the entire tape: the put
spike (phase-1), overhead DP supply at 341–351 (phase-2), backwardation (phase-4),
and the P/C bearish extreme below. **Yet the vol response is muted**: IV30d 0.324
sits at only the **54.9th 1-yr percentile** (regime NORMAL, z −0.23), while realized
vol ran to **39.7%** — so **VRP is −0.073 → PREMIUM_BUYING** (options cheap vs
realized; favor *debit*/long-premium structures). The setup is genuinely two-sided:
bearish momentum and a 2.2-σ P/C **BEARISH_EXTREME** and an 85.7% bearish_flow
backtest (N=7) pull one way; a **balanced 90-day flow** (net only +$29M bullish),
the complacent IV, and phase-4's mean-reversion structure pull the other. The GEX
regime has been **unstable (7 flips in 30 days)**, so today's long-gamma cushion is
not a reliable floor — it could flip negative if the breakdown extends.

## Key signals

- **Today = −7.1% breakdown** (342.95 → 318.59); 30d price −9.9%, 17 bearish vs 13
  bullish days, latest flow bearish. `[HIST:trend]` `[HIST:gex_time_series]`
- **VRP −0.073 → PREMIUM_BUYING** (IV30d 0.324 vs realized 0.397) — vol cheap vs
  realized; favor debit structures. `[HIST:vrp]`
- **IV only 54.9th %ile / NORMAL** despite the drop — no panic priced (ties to
  phase-4 complacent skew). `[HIST:iv_percentile_zscore]`
- **P/C z-score +2.21 = BEARISH_EXTREME** (today 0.71 vs 20d mean 0.46, σ 0.116) —
  contrarian fade flag. `[HIST:pc_ratio_zscore]`
- **90d flow BALANCED / MIXED**: cum bullish $6.661B vs bearish $6.632B, net
  **+$28.8M** — today's bearish tilt is a *spike*, not a persistent campaign.
  `[HIST:cumulative_premium_flow]`
- **OI BUILDING — 18 consecutive build days**, +822,569 net OI/30d. `[HIST:oi_trend]`
- **bearish_flow backtest win 85.7%, N=7** (market-wide base rate, low-confidence).
  `[HIST:signal_backtest]`

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore]` `[HIST:vrp]`
IV30d 0.3235, **percentile 54.93** (NORMAL), z −0.226, dates_used 71. VRP **−0.0733**
(realised_vol 0.3968 > IV30d 0.3235) → "Vol cheap vs realised — favour premium
buying." A 7% drop with mid-percentile IV = the market is not paying up for
protection → complacency (phase-4 skew 1.002 agrees).

### Cumulative premium flow (90d) — `[HIST:cumulative_premium_flow]`
net_flow **+$28.8M** over 72 covered sessions, trend_direction **MIXED**. Essentially
balanced — no stealth 60d+ directional build in either direction. Today's bearish
skew does not extend a campaign; it is an event-day spike.

### P/C ratio z-score — `[HIST:pc_ratio_zscore]`
current 0.7126, mean 0.4558, σ 0.1164, **z +2.206, extreme BEARISH_EXTREME**. GOOG
normally trades very call-heavy (mean P/C 0.46); today's jump to 0.71 is a 2.2-σ
shift toward puts — a genuine sentiment extreme, contrarian-fade candidate.

### GEX time series (30d) — `[HIST:gex_time_series]`
Regime **unstable: 7 flips** in 30 days (POSITIVE↔NEGATIVE), ZGL swinging 87–398.
Trajectory: spot 354–371 in mid-June, oscillating 337–369 through mid-July, then
342.95 (07-22) → **318.59 (07-23)**. Today POSITIVE, ZGL 187.5, but total_gex −48.4M
(same regime/sign quirk as phase-4). Instability caveat: the long-gamma cushion is
not dependable; a further break could flip the regime negative (trend-amplifying).

### OI trend (30d) — `[HIST:oi_trend]`
overall_trend **BUILDING**, **18 consecutive build days**, total_net_oi_change
+822,569. Sustained engagement into the breakdown (phase-3: two-sided build).

### Multi-day trend (30d, 2026-06-10 → 2026-07-23) — `[HIST:trend]`
price 353.32 → 318.34; iv_rank 36.8 → 38.3; **13 bullish / 17 bearish days**; latest
flow **bearish**. The name spent June in the 350–371 zone and lost that shelf in
July, capped by the 07-23 gap-down.

### Price context (`fz`)
`fz quote GOOG` returned **null** for RSI/SMA20-50-200/Perf/52W (mega-cap field gap,
same as phase-0). Advisory cross-check **skipped** — no `[HIST:rsi fz]` /
`[HIST:52w_proximity fz]` this run. From UW data alone, price is ~10% off its
30-day high and freshly broke down; RSI would read oversold, but unconfirmed.

### Signal backtest — `[HIST:signal_backtest]`
`--signal-type bearish_flow --lookback-days 5`: **win_rate 85.7%, total_signals 7**,
vol_realisation_rate null. Market-wide base rate for the bearish_flow class, **N=7
→ low confidence** (< 10 firings). Suggestive that fresh bearish_flow has paid, but
too thin to lean on hard; phase-9 must apply the N-conditional Kelly cap.

## Tool calls
| Tool | Args | jq path |
|---|---|---|
| historical iv-percentile-zscore | --symbol GOOG --lookback-days 252 | `.{iv_percentile,iv_zscore,current_iv30d,regime,dates_used}` |
| historical vrp | --symbol GOOG --realised-window-days 30 | `.{vrp,iv30d,realised_vol,regime}` |
| historical cumulative-premium-flow | --symbol GOOG --days 90 | `.{cumulative_bullish,cumulative_bearish,net_flow,trend_direction}` |
| historical pc-ratio-zscore | --symbol GOOG --lookback-days 20 | `.{current_pc_ratio,mean_pc_ratio,zscore,extreme}` |
| historical gex-time-series | --symbol GOOG --days 30 --dte-max 45 | `.{trajectory[],regime_flip_dates[]}` |
| historical oi-trend | --symbol GOOG --days 30 --top-n 10 | `.{overall_trend,consecutive_build_days,total_net_oi_change}` |
| historical trend | --symbol GOOG --days 30 | `.{price_change,bullish_days,bearish_days,flow_direction_latest,daily_data[]}` |
| historical signal-backtest | --signal-type bearish_flow --lookback-days 5 --top-n 20 | `.{win_rate,total_signals}` (market-wide) |
| fz quote | GOOG --agent | null RSI/SMA/52W (skipped) |

## Tool errors
- `historical gex-time-series` payload is `.trajectory[]` / `.regime_flip_dates[]`,
  not `.series` — read the correct keys.
- `fz quote GOOG` fundamentals lack RSI/SMA/Perf/52W (mega-cap field set); advisory
  price-context cross-check skipped, not an error.

## Verdict for downstream

- **Volatility regime: FAIR-to-CHEAP.** IV NORMAL (54.9 %ile) but **PREMIUM_BUYING**
  (VRP −0.073, RV 39.7% > IV 32.4%). Vol is cheap relative to how much the stock is
  actually moving → **favor DEBIT / long-premium structures** over credit.
- **Premium environment: BUYING** (debit-favored). Do not sell naked premium into a
  freshly-broken-down name with realized > implied.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 3 / 5.** The
  bearish_flow backtest (85.7%) supports the short direction but N=7 is thin, the
  90d flow is balanced (spike, not campaign), and the P/C extreme + phase-4
  mean-reversion structure argue a counter-bounce is likely first. Two-sided.
- **Three specific datapoints:** IV percentile **54.93**; VRP **−0.0733**
  (PREMIUM_BUYING, realized 39.7%); bearish_flow win **85.7%** (N=7).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.857
  win_rate_n:                7
  win_rate_source:           backtest      # market-wide base rate, NOT GOOG-specific; N=7 → shrink
  ```
- **Open questions:**
  - **What catalyst drove the 7% single-day drop on 2026-07-23?** (No earnings until
    Nov-4.) This is the pivotal unknown — regulatory/antitrust, AI-competition
    headline, downgrade, or Comm-Services rotation. → **phase-6 must find it**;
    phase-7b/7c weigh whether it is a fundamental re-rate (thesis-defining).
  - Is the drop the start of a trend (GEX could flip negative) or an overshoot into
    a long-gamma/complacent-IV mean-reversion bounce? → phase-8/8b arbitrate.
