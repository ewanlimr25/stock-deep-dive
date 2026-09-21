# Phase 5 — Historical Context & VRP

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

History frames today's bearish print as a **contrarian outlier against a strong
uptrend, not the start of a trend.** CMPS is +33% over the last 30 sessions ($9.39 →
$12.53), +81.6% YTD, with OI **BUILDING** 4 straight days (+61,955, call-heavy) and a
stably long-gamma dealer regime (last flip 2026-05-13). The single bearish datapoint
that *does* fire is loud: the P/C-ratio z-score is **+3.83 → BEARISH_EXTREME** (today's
1.36 vs a 20-day mean of 0.243), i.e. a 4-sigma sentiment spike on a normally
call-heavy name — which is exactly the profile a contrarian fades. VRP is **+5.03 →
PREMIUM_SELLING** (IV 93.8% > RV 88.8%), a headwind for *buying* the LEAP put. The
matching `bearish_flow` backtest reads 85.7% — but on **n=7, market-wide, in-sample**,
so it is suggestive at best. Net: the historical edge for a fresh bear here is weak;
the weight of context (trend, OI build, long-gamma, premium-selling, extreme P/C
z-score) leans the *other* way.

## Key signals

- **P/C z-score +3.83 → BEARISH_EXTREME** (today 1.36 vs mean 0.243) — 4σ sentiment
  spike, classic contrarian fade flag [HIST:pc_ratio_zscore]
- 30d uptrend **+33%** ($9.39→$12.53), 18 bullish vs 12 bearish days [HIST:trend]
- OI **BUILDING**, 4 consecutive build days, +61,955 net (call-heavy) [HIST:oi_trend]
- VRP **+5.03 → PREMIUM_SELLING** (IV30 93.8% > RV30 88.8%) → favor credit, headwind
  for debit puts [HIST:vrp]
- Dealer regime **stably long-gamma**, no flip since 2026-05-13 [HIST:gex_time_series]
- bearish_flow backtest **win_rate 85.7% but n=7**, market-wide, in-sample
  [HIST:signal_backtest]
- fz: **RSI 58.7 (not overbought)**, −15.1% off 52w high $14.76, +74% vs SMA200,
  +81.6% YTD [HIST:rsi fz, HIST:52w_proximity fz]

## Detailed findings

### IV regime (`[HIST:iv_percentile_zscore]`, `[HIST:vrp]`)

- current_iv30d **93.79%**; iv_percentile **72.92** (1y); iv_zscore **0.751**; regime
  **NORMAL** — over **48 sessions actually used** (gap-aware; not 252).
- **Tension to flag:** iv_percentile 72.92 (above-median) vs screener **iv_rank
  20.35** (near low of range). Reconciles as a few high-IV spike days stretching the
  rank range while current sits above the *typical* day — IV is mid-high, not cheap.
- VRP **+0.0503** (IV30 0.9379 − RV30 0.8876); regime **PREMIUM_SELLING**
  ("Options pricing more vol than realised — favour premium selling"). A debit LEAP
  put is bought into a premium-rich tape (less acute for a 582-DTE LEAP, but noted).

### Cumulative premium flow (`[HIST:cumulative_premium_flow]`, 49 sessions)

- cumulative_bullish $15,588,696 vs cumulative_bearish $15,308,717 → **net +$279,979**,
  `trend_direction` **MIXED**. Essentially balanced/slightly bullish over the window —
  today's −$595K bearish day is a clear outlier (ties to phase-0.5 self_pctile 0.0).

### P/C ratio z-score (`[HIST:pc_ratio_zscore]`, 20-day)

- current_pc_ratio **1.3641**, mean **0.243**, std 0.2926, **zscore +3.831**,
  `extreme` = **BEARISH_EXTREME**. The standout signal of the phase. |z|>2 → sentiment
  extreme. Cuts two ways: confirms the bearish print is statistically real **and**
  flags a contrarian fade (extreme bearishness on a call-loved uptrend name).

### GEX time series (`[HIST:gex_time_series]`, 30d)

- Recent regime POSITIVE/FULLY_POSITIVE throughout; **flip dates only 2026-05-08/
  05-12/05-13** (volatile $9–11 period). **No flip in >5 weeks** → dealer hedging
  stable, long-gamma. Spot climbed ~$9.76 → $12.53 over the window (~+28%).

### OI trend (`[HIST:oi_trend]`, 30d)

- overall_trend **BUILDING**; consecutive_build_days **4**; total_net_oi_change
  **+61,955**. Sustained accretion into a call-heavy book → structurally bullish
  positioning, against which today's put is contrarian.

### Multi-day trend (`[HIST:trend]`, 2026-05-07 → 2026-06-18, 30 sessions)

- price_change **$9.39 → $12.53 (+33.4%)**; bullish_days **18**, bearish_days **12**;
  flow_direction_latest **bearish** (today); iv_rank_change **14.49 → 20.35**.
- Historical daily PCR mostly 0.03–0.74 (call-heavy norm), confirming today's 1.36 is
  anomalous.

### Price context (`fz`, advisory) (`[HIST:rsi fz]`, `[HIST:52w_proximity fz]`)

- RSI(14) **58.68** (neutral — *not* overbought, so not a textbook exhaustion top);
  price $12.53 = **−15.11% below 52w high $14.76**, **+456.9% above 52w low $2.25**;
  SMA20 +3.09% / SMA50 +23.98% / SMA200 **+74.17%**; Perf YTD **+81.59%**.
- Read: parabolic momentum biotech, mild pullback from highs, momentum intact. A
  fresh bear fights a powerful trend; RSI gives no overbought cover for the fade.

### Signal backtest (`[HIST:signal_backtest]`, bearish_flow, market-wide)

- **win_rate 85.7%**, **total_signals 7**, avg_move_pct **−1.45%**, direction tally
  down=6 / up=1. `methodology_notes`: "In-sample backtest — not a robust live edge",
  lookback in trading days, positional selection. **Base rate of the bearish_flow
  signal *class* across the tape, not CMPS-specific.** High rate, tiny N → low
  confidence; phase-9 applies the N-conditional Kelly cap.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical iv-percentile-zscore --lookback-days 252` | iv_pctile 72.92, z 0.751, NORMAL ← `.iv_percentile`; dates_used=48 | 48 sess |
| `uw historical vrp --realised-window-days 30` | vrp +0.0503, PREMIUM_SELLING ← `.vrp,.regime` | 30d |
| `uw historical cumulative-premium-flow --days 90` | net +$279,979 MIXED ← `.cumulative_bullish-.cumulative_bearish` | 49 sess |
| `uw historical pc-ratio-zscore --lookback-days 20` | z +3.831 BEARISH_EXTREME ← `.zscore,.extreme` | 20d |
| `uw historical gex-time-series --days 30` | no flip since 05-13 ← `.regime_flip_dates` | 30d |
| `uw historical oi-trend --days 30` | BUILDING, 4 build days, +61,955 ← `.overall_trend,.consecutive_build_days` | 30d |
| `uw historical trend --days 30` | +33.4%, 18/12 bull/bear ← `.price_change,.bullish_days` | 30 sess |
| `uw historical signal-backtest --signal-type bearish_flow` | win_rate 85.7%, n=7 ← `.win_rate,.total_signals` | 7 sig |
| `fz quote CMPS` | RSI 58.68, 52wH −15.11%, YTD +81.59% ← `.fundamentals` | EOD |

## Tool errors

<none — all green. Gap-aware: every trailing window crosses the 2026-03-28→04-24 hole,
so reported N is the tool's own session count (iv: 48, cpf: 49, trend: 30), not the
calendar span. Trailing commands anchor to latest available date = 2026-06-18 (= as-of),
so this run is reproducible; a re-run after a new session lands will shift these reads.>

## DATA NOTE / CORRECTION

- iv_percentile (72.92) vs iv_rank (20.35) discrepancy reconciled in §IV regime — both
  reported; neither re-read (they measure different things, both valid).

## Verdict for downstream phases

- **Volatility regime:** **FAIR-to-RICH / PREMIUM-SELLING** (VRP +5.03; IV pctile 73
  but rank 20). Debit structures face a mild vol headwind near-term.
- **Environment:** **premium-SELLING** — favors credit over debit; a long LEAP put is
  swimming against VRP (mitigated by its 582-DTE tenor).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2 / 5.** The lone
  support is a weak backtest (85.7%, n=7, in-sample, market-wide). Everything else —
  +33% trend, 4-day OI build, stable long-gamma, premium-selling VRP, and a +3.8σ
  P/C extreme that itself flags a *fade* — leans against a fresh bear.
- **Three specific datapoints:** IV percentile **72.92** · VRP **+0.0503
  (PREMIUM_SELLING)** · bearish_flow win-rate **0.857 (n=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.857
  win_rate_n:       7
  win_rate_source:  backtest
  ```
  (Market-wide base rate, in-sample — apply the small-N Kelly cap; this is NOT a
  CMPS-specific win rate.)
- **Open questions:** Is the +3.8σ P/C extreme a smart-money front-run of a catalyst
  (phase-7b/7c) or a fade-able outlier on a momentum name? Does the OI build continue
  bullish on 6/19+ while the new put sits orphaned (phase-3 follow-through)?
