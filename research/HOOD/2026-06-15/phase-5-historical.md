# Phase 5 — Historical Context & VRP

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T12:20:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bullish tilt sits inside a **+28% one-month rally** ($76.55→$98.12, 30
sessions) carried by **relentless OI accumulation (30 consecutive build days,
+1.7M net OI)** — a strong structural uptrend. But three historical reads temper the
trade: (1) **VRP is −0.10 → PREMIUM_BUYING** (IV 63.0% < realized 73.3%) — vol is
cheap, favor *debit* structures, not credit; (2) the **`bullish_flow` signal backtest
win-rate is only 28.6% (N=7)** — below the 0.45 edge floor, so the matching signal
class has historically *lost* recently; (3) 90-day cumulative premium flow is
**MIXED/balanced** (−$16M net over 46 sessions) and there were *more* bearish-flow
days (17) than bullish (13) over 30d — the rally was driven by underlying
accumulation + a short-gamma squeeze (5/22 fully-negative GEX at $73), **not** by
persistent options-premium chasing. Price is now stretched (+17–21% above SMA20/50,
RSI 65) at the $100 wall with a *freshly* positive (consolidation-prone) gamma regime.

## Key signals

- **+28.2% in 30 sessions** (76.55→98.12), 13 bullish / 17 bearish flow days
  `[HIST:trend]` — price-vs-flow divergence (accumulation/squeeze-led).
- **OI BUILDING 30 consecutive days**, +1,701,249 net OI `[HIST:oi_trend]` — strongest
  structural bull signal here.
- **VRP −0.1027 → PREMIUM_BUYING** (IV30d 63.0% vs realized 73.3%) `[HIST:vrp]` —
  favor long-premium/debit structures.
- **bullish_flow backtest win-rate 28.6%, N=7** `[HIST:signal_backtest]` — below 0.45
  edge floor → Kelly `p` de-rate.
- **GEX regime just flipped POSITIVE** (~4 sessions, after 13 flips/30d); 5/22 was
  FULLY_NEGATIVE at $73 (the squeeze launchpad) `[HIST:gex_time_series]`.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore][HIST:vrp]`

- current_iv30d **63.0%**, iv_percentile **46.67** (1y), iv_zscore −0.202, regime
  **NORMAL**. ⚠️ `dates_used = 45` over the 252-day request (gap + short history) —
  the percentile rests on **45 sessions**, treat as indicative.
- VRP **−0.1027**, regime **PREMIUM_BUYING** ("Vol cheap vs realised — favour premium
  buying"): IV30d 63.0% < realized_vol 73.3% (30d). Confirms phase-4's cheap-optionality
  read (complacent skew, IV rank 32) → **structure handoff: prefer debit over credit.**

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

net_flow **−$15,993,771** (cumulative_bullish $1.975B vs bearish $1.991B),
trend_direction **MIXED**. ⚠️ Gap-aware: `dates_covered` jumps 2026-04-27 → 2026-03-27
(the 21-session hole 03-28→04-24) — **N = 46 sessions**, not 90 calendar days. Read:
over the available window, options premium flow is essentially **balanced/slightly
bearish** — this rally is *not* a persistent stealth options-premium build.

### P/C ratio z-score (20d) `[HIST:pc_ratio_zscore]`

current_pc_ratio 0.3464, mean 0.3549, std 0.1135, **zscore −0.075, extreme NORMAL**.
Today's call-heaviness (PCR 0.346) is right at the 20-day mean → the call tilt is the
name's *normal* recent state, **not** a sentiment extreme (no contrarian fade signal;
also confirms the bullish tilt is persistent, not a one-day spike).

### GEX time series (30d) `[HIST:gex_time_series]`

**13 regime flips in 30 days** — highly unstable gamma. Trajectory: short-gamma /
NEGATIVE through most of May at $73–81 (incl. FULLY_NEGATIVE 5/22, GEX −$33M @ $73.63
— the squeeze launchpad), turning durably POSITIVE only from **6/10** onward (6/11
GEX $90M, 6/12 $147M, 6/15 $77.6M) as price cleared $87→98. The note: flips precede
realized-vol expansion (consistent with realized 73% > IV 63%). **The current positive
regime is only ~4 sessions old** — recent, not established; mean-reversion/consolidation
risk into 6/18.

### OI trend (30d) `[HIST:oi_trend]`

overall_trend **BUILDING**, **consecutive_build_days 30**, total_net_oi_change
**+1,701,249**, days_analyzed 30 (05-04→06-15, post-gap, clean). Relentless, unbroken
OI accumulation alongside the price rise — the single strongest structural bull data
point in this phase.

### Multi-day trend (30d) `[HIST:trend]`

days_analyzed 30, date_range 2026-05-04→2026-06-15 (clean, no gap), price_change
**76.55 → 98.12 (+28.2%)**, iv_rank_change 24.8 → 32.4 (mild IV-rank rise),
bullish_days **13** / bearish_days **17**, flow_direction_latest **bullish**.
Divergence: price rose 28% on a *minority* of bullish-flow days → accumulation/squeeze
mechanics, not flow-chasing.

### Price context (`fz`, advisory) `[HIST:rsi fz][HIST:52w_proximity fz]`

- RSI(14) **65.34** — elevated, approaching but not at overbought (70).
- Above SMA20 **+16.99%**, SMA50 **+21.40%** (short-term **stretched**); SMA200
  **−4.54%** (still below the 200-day) → sharp recovery rally, not yet a structural
  long-term breakout.
- Perf month **+21.59%**, Perf YTD **−13.24%**. 52W High 153.86 (**−36.23%** below),
  52W Low 63.51 (**+54.48%** above). Big recovery off lows, large overhead room to the
  52w high but extended near-term. Tempers a fresh-breakout chase.

### Signal backtest `[HIST:signal_backtest]`

- **bullish_flow** (matches phase-1 verdict): **win_rate 28.6%, total_signals 7**,
  avg_return null. Stable across two runs. Below the 0.45 edge floor → today's
  bullish-flow setup has *historically lost* recently. **Small N (7) = low confidence,
  but the signal is negative not absent.**
- **dark_pool_accumulation** (phase-2's signal): `{"note":"no backtest results",
  "total_signals":0}` on two runs → no usable rate.
- Market-wide base rates (no `--symbol`) — these are the signal *class* base rates
  across the tape, not HOOD-specific.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | N / window |
|------------------|--------------------------|-----------|
| `uw historical iv-percentile-zscore --symbol HOOD --lookback-days 252` | iv30d 63.0%, %ile 46.67, NORMAL ← `.iv_percentile` | dates_used 45 |
| `uw historical vrp --symbol HOOD --realised-window-days 30` | VRP −0.1027 PREMIUM_BUYING ← `.vrp/.regime` | 30d |
| `uw historical cumulative-premium-flow --symbol HOOD --days 90` | net −$16M MIXED ← `.net_flow` | 46 sessions (gap) |
| `uw historical pc-ratio-zscore --symbol HOOD --lookback-days 20` | z −0.075 NORMAL ← `.zscore/.extreme` | 20d |
| `uw historical gex-time-series --symbol HOOD --days 30 --dte-max 45` | 13 flips; POSITIVE since 6/10 ← `.regime_flip_dates` | 30 days |
| `uw historical oi-trend --symbol HOOD --days 30 --top-n 10` | BUILDING, 30 consec days, +1.70M ← `.consecutive_build_days` | 30 days |
| `uw historical trend --symbol HOOD --days 30` | +28.2%, 13 bull/17 bear ← `.price_change` | 30 days |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20` | win 28.6%, N 7 ← `.win_rate/.total_signals` | market-wide |
| `uw historical signal-backtest --signal-type dark_pool_accumulation …` | null, N 0 | market-wide |
| `fz quote HOOD --agent` | RSI 65.34, +17/21% vs SMA20/50, −36% vs 52wH | EOD |

## Tool errors

(none) — backtest empty stubs handled by re-run per protocol (bullish_flow stable at
28.6%/N7; dark_pool_accumulation genuinely 0 signals on both runs).

## DATA NOTE / CORRECTION

- Gap-awareness: the 252-day IV read used only **45 sessions** (`dates_used`) and the
  90-day cumulative flow only **46 sessions** (`dates_covered` shows the 03-28→04-24
  hole) — quoted as actual N, not calendar span. The 30-day trend/oi/gex windows
  (05-04→06-15) are post-gap and contiguous.
- Latest-anchor caveat: all trailing reads anchor to latest available = 2026-06-15
  (= as-of), so this run is as-of correct; a re-run after a new session would shift them.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** (IV30d 63% < realized 73%, VRP −0.10, IV %ile 47 /
  rank 32) → **PREMIUM-BUYING environment, favor debit (long-premium) structures.**
- **Premium-buying vs selling:** **BUYING** — credit/premium-selling structures are
  disadvantaged here (cheap vol); long calls / debit spreads are the vol-aligned vehicle.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2 / 5 (LOW).**
  Structural bull case is real (30 consecutive OI-build days, +28% trend, phase-2
  accumulation), but the *matching options signal* (bullish_flow) backtests at 28.6%
  (N=7, below 0.45), 90d premium flow is balanced, and price is stretched/recently
  flipped to mean-reverting positive gamma.
- **Three specific datapoints:** IV %ile **46.67**, VRP **−0.1027**, bullish_flow win
  rate **28.6% (N=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.286
  win_rate_n:                7
  win_rate_source:           backtest
  ```
  (Kelly `p` input — market-wide base rate, not HOOD-specific; small N + sub-0.45 rate
  → phase-9 must apply the N-conditional cap and size *down*. dark_pool_accumulation
  had 0 signals so cannot supply an alternative `p`.)
- **Open questions:** Does the relentless 30-day OI build (structural bull) outweigh the
  poor bullish_flow backtest (28.6%)? Is +28% in a month + RSI 65 + $100 wall a
  consolidation setup rather than a continuation? Does cheap vol (VRP −0.10) argue for a
  long-call/debit-spread expression of any bullish view rather than chasing stock?
