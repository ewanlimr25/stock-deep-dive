# Phase 5 — Historical Context & VRP

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

The historical context **contradicts a bullish directional read and endorses
premium-SELLING.** IV is at the **98.5th 1-year percentile** (z +1.84, regime
HIGH_IV) with **VRP +18.9 vol-points → PREMIUM_SELLING regime** ("options pricing
more vol than realised"). The 30-session trend is a **−13.5% DOWNTREND**
($119.36 → $103.24) into earnings, choppy (15 bull / 15 bear days), with IV rank
climbing 78→96.9. Most importantly, the market-wide signal backtests are lopsided:
**bullish_flow win-rate 14.3% (n=7, avg move −7.38%)** vs **bearish_flow 100.0%
(n=10, avg −5.22%)** over the last 5 days — the tape is actively punishing bullish
setups and rewarding bearish ones. GEX has whipsawed (7 regime flips/30d; went
FULLY_NEGATIVE during the mid-June drop to $92, i.e. short-gamma amplifies NOW's
selloffs). OI is BUILDING (7 consecutive days, +886k) — pre-earnings positioning,
both sides. **Verdict: today's faint-bullish flow is HISTORICALLY EDGE-NEGATIVE;
the edge is in selling rich premium, not buying direction.**

## Key signals

- **IV 98.5th pctile / z +1.84, HIGH_IV** — vol is richly bid `[HIST:iv_percentile_zscore]`.
- **VRP +0.189 → PREMIUM_SELLING** (IV30 75.9% vs RV30 57.0%) `[HIST:vrp]`.
- **bullish_flow backtest 14.3% win (n=7, −7.38% avg)** — bullish read is
  edge-negative `[HIST:signal_backtest]`.
- **bearish_flow backtest 100% win (n=10, −5.22% avg)** — bearish is the
  edge-positive class this week `[HIST:signal_backtest]`.
- **30d price −13.5%** ($119.36→$103.24), IV rank 78→96.9 `[HIST:trend]`; **GEX
  whipsaw, FULLY_NEGATIVE at the June lows** `[HIST:gex_time_series]`.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- current_iv30d **75.9%**, iv_percentile **98.51**, iv_zscore **+1.841**, regime
  **HIGH_IV** (dates_used **67** — spans the 03-28→04-24 gap; treat as 67 actual
  sessions, not a clean 252 calendar days).
- VRP: iv30d 75.9% − realised_vol 57.0% = **+18.88 vol-pts**, regime
  **PREMIUM_SELLING**. Options are overpricing realised vol → **favour credit /
  premium-selling structures**, corroborating phase-1's bid-side put writing and
  phase-3's 60-put write.

### Cumulative premium flow (90d ≈ 69 sessions, gap-crossing) `[HIST:cumulative_premium_flow]`

bullish $2.63B, bearish $2.52B, **net +$101.4M**, trend **MIXED**. Faintly
net-bullish over the window but not a persistent stealth build (dates_covered jumps
04-27→03-27 across the hole — read as ~69 sessions, gap excluded, per phase-0).

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current_pc **0.6321** vs 20d mean **0.409**, **z +1.286**, extreme **NORMAL**.
Today's P/C is ~1.3σ above its recent norm (more puts than usual — the
hedging/writing) but **not a contrarian extreme** (|z|<2).

### GEX time series (30d) `[HIST:gex_time_series]`

**Unstable — 7 regime flips in 30 sessions.** Path: POSITIVE early June (spot ~$120)
→ **FULLY_NEGATIVE 6/11–6/22 as spot collapsed to $92** (short-gamma amplified the
selloff, total_gex −$40M at the 6/18 low) → POSITIVE rebound into July ($111 by 7/13)
→ NEGATIVE 7/14–7/16 on the pullback → **POSITIVE again 7/17 (ZGL $101.21)**.
Takeaway: NOW's dealer gamma **flips negative on drawdowns**, so a downside earnings
break has a mechanical accelerant; the current long-gamma pin (phase-4) is fragile.

### OI trend (30d) `[HIST:oi_trend]`

overall_trend **BUILDING**, **7 consecutive build days**, total_net_oi_change
**+886,376**. Steady pre-earnings OI accumulation (both sides) — positioning, not a
one-sided conviction build.

### Multi-day trend (30 sessions, 2026-06-04 → 2026-07-17) `[HIST:trend]`

- **price_change: $119.36 → $103.24 (−13.5%)**
- bullish_days 15 / bearish_days 15 (evenly split — choppy, no clean trend day-count)
- iv_rank_change: 78.21 → **96.90** (rising into earnings)
- flow_direction_latest: bullish (single-day tag only)

### Price context (`fz`, advisory)

**Unavailable** — `fz` returned only its 14-field partial snapshot all session
(RSI/SMA50/SMA200/Perf YTD/52W High-Low all null). No independent EOD cross-check
this run. `[HIST:rsi fz]` = n/a, `[HIST:52w_proximity fz]` = n/a. (The UW trend
read stands alone: −13.5%/30d into earnings.)

### Signal backtest (current signal's edge) `[HIST:signal_backtest]`

Market-wide (no `--symbol`), lookback 5d, re-run to confirm non-stub:

| signal_type | win_rate | n (total_signals) | avg_move% |
|---|---|---|---|
| **bullish_flow** (matches phase-1 verdict) | **14.3%** | 7 | **−7.38%** |
| bearish_flow (comparison) | **100.0%** | 10 | −5.22% |

The bullish_flow class — the one phase-1's faint bullish lean maps to — is **deeply
edge-negative right now** (1-in-7, and those names fell 7.4% on average). bearish_flow
is the edge-positive class. Small N (7/10) = low confidence, but the sign is
unambiguous and consistent with the −13.5% trend.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows/N |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol NOW --lookback-days 252` | pctile 98.51, z 1.84, HIGH_IV ← `.iv_percentile/.regime` | 67 dates |
| `uw historical vrp --symbol NOW --realised-window-days 30` | VRP +0.1888, PREMIUM_SELLING ← `.vrp/.regime` | 1 |
| `uw historical cumulative-premium-flow --symbol NOW --days 90` | net +$101.4M, MIXED ← `.net_flow/.trend_direction` | ~69 |
| `uw historical pc-ratio-zscore --symbol NOW --lookback-days 20` | z +1.286, NORMAL ← `.zscore/.extreme` | 20 |
| `uw historical gex-time-series --symbol NOW --days 30 --dte-max 45` | 7 flips; FULLY_NEGATIVE at June lows ← `.regime_flip_dates/.trajectory` | 30 |
| `uw historical oi-trend --symbol NOW --days 30` | BUILDING, 7 consec, +886,376 ← `.overall_trend/.consecutive_build_days` | 30 |
| `uw historical trend --symbol NOW --days 30` | −13.5%, iv_rank 78→96.9 ← `.price_change/.iv_rank_change` | 30 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5` | 14.3% win, n=7, −7.38% ← `.win_rate/.total_signals` | market-wide |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5` | 100% win, n=10, −5.22% ← `.win_rate/.total_signals` | market-wide |

## Tool errors

None. `fz` price-context advisory lane unavailable (partial snapshot, non-blocking).

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq`. Latest-anchor caveat: latest available
date = 2026-07-17 = as-of, so trailing reads align with as-of this run; a re-run
after 2026-07-20+ (esp. post-earnings 7/22) will shift every trailing datapoint.

## Verdict for downstream

- **Volatility regime:** **RICH** (IV 98.5th pctile, VRP +18.9) → **PREMIUM-SELLING
  environment**; favour credit structures over debit.
- **Premium buying vs selling:** **SELLING** is the edge-aligned side.
- **Conviction that today's (bullish) signal is HISTORICALLY EDGE-POSITIVE: 1/5.**
  It is edge-NEGATIVE (backtest 14.3%, 30d −13.5% downtrend). The only edge-positive
  *directional* class is bearish_flow (100%/n10), and the cleanest edge overall is
  short-vol/premium-sell.
- **Three specific data points:** IV percentile **98.51**; VRP **+0.189**
  (PREMIUM_SELLING); bullish_flow signal win-rate **14.3%** (n=7).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bullish_flow          # matches phase-1 faint-bullish verdict
  signal_backtest_win_rate: 0.143
  win_rate_n:       7
  win_rate_source:  backtest
  # CAUTION for phase-9: p=0.143 << breakeven → a bullish directional trade is NOT
  # edge-positive. Market-wide base rate, not NOW-specific, N small (7).
  # Edge-positive alternatives: bearish_flow p=1.00 (n=10); short-vol/premium-sell
  # (VRP +0.189, IV pctile 98.5). Prefer a credit/premium-selling or defined-risk
  # structure over a naked long-delta bullish bet.
  ```
- **Open questions:** Given premium-selling edge + earnings binary (phase-4 ±10–12%
  implied), does the trade become a defined-risk premium-sell (e.g. iron condor /
  put spread) rather than directional? Does phase-6 macro confirm the risk-off tape
  the bearish_flow=100% backtest implies? Does phase-7b/7c fundamentals/sentiment
  give a reason the −13.5% downtrend continues or exhausts into the print?
