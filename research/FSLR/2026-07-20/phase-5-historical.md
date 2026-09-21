# Phase 5 — Historical Context & VRP

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Version:** v1 · **Generated:** 2026-07-20
**Latest available date (trailing-anchor):** 2026-07-20 (= as-of ✓)
**Cites:** phase-4-structure.md (FULLY_NEGATIVE GEX today); phase-1-flow.md
(bearish net_flow, IV rank 99); phase-3-positioning.md (OI building).

## Summary

Today's bearish signal sits inside an **established multi-week downtrend with a
rich-vol, premium-selling backdrop and a stable short-gamma regime.** FSLR has
fallen **−26.4% in 30 sessions ($279.01 → $205.31)**, with **18 bearish vs 12
bullish flow-days** and the latest flow-direction **bearish**. IV is at **1-year
highs** (IV percentile **98.5**, z **+1.22**, HIGH_IV) and **VRP = +0.19**
(IV30 76.4% − RV30 57.3%) → a **PREMIUM_SELLING** environment (options pricing
more vol than the stock is realizing). The dealer regime has been **persistently
FULLY_NEGATIVE (short gamma) since 2026-07-13** — six straight sessions — so
phase-4's amplification read is a *stable regime*, not a one-day artifact, and it
has coincided with the leg from $224 → $205. The current-signal edge is
**positive but small-sample**: the `bearish_flow` class backtests **90.0% win,
N=10**. Net: history says today's bearish flow is edge-positive, the trend is your
friend, but IV is rich (long premium is expensive) and the sample is thin.

## Key signals

- **[HIST:trend]** Price **$279.01 → $205.31 (−26.4%)** over 30 sessions; 18
  bearish / 12 bullish days; latest flow **bearish** — an entrenched downtrend.
- **[HIST:gex_time_series]** **Persistently FULLY_NEGATIVE since 07-13** (6
  sessions; ZGL null throughout) — short-gamma regime is *stable*, tracking the
  decline from $280 (POSITIVE, early June) to $206 today.
- **[HIST:vrp]** VRP **+0.19**, regime **PREMIUM_SELLING** ("options pricing more
  vol than realised — favour premium selling").
- **[HIST:iv_percentile_zscore]** IV percentile **98.5** (z +1.22), regime
  **HIGH_IV** — 1-year IV extreme (earnings + decline).
- **[HIST:signal_backtest]** `bearish_flow` win rate **90.0%**, **N=10** (market-
  wide base rate, low-confidence sample) → the Kelly `p` input for phase-9.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` / `[HIST:vrp]`
- current IV30d **76.4%**, IV percentile **98.5** (252d lookback, 68 sessions
  actually used — gap-aware), z **+1.22**, regime **HIGH_IV**.
- Realized vol30 **57.3%**; **VRP +0.19 → PREMIUM_SELLING**. Debit/long-premium
  structures are expensive here; the historical edge is in *selling* vol — but see
  the earnings caveat (phase-4 IV crush is the reward, direction risk is the cost).

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`
Net_flow **+$9.3M**, trend **MIXED** — cum bullish $1.054B vs cum bearish $1.045B
over 69 dates present. **No persistent stealth directional build** either way; the
directional signal is a recent-week phenomenon, not a 90-day campaign. (Tempers
the phase-1 bearish conviction slightly — this is a fresh tilt on a downtrend, not
a long-running distribution.)

### P/C ratio z-score `[HIST:pc_ratio_zscore]`
current P/C **0.418** vs 20d mean **1.016** (std 0.80) → z **−0.75**, **NORMAL**.
Today is call-heavy vs its own 20-day norm but **not** a sentiment extreme
(|z|<2); no contrarian trigger. (Note: this is premium-weighted P/C; the *call*
premium is being sold — see phase-1.)

### GEX time series (30d regime trajectory) `[HIST:gex_time_series]`
regime_flip_dates = null; trajectory shows the transition:
- **Early June:** POSITIVE (long gamma), spot ~$279, total GEX +$7–11M, ZGL ~$70–190.
- **Late June:** whipsaw POSITIVE↔FULLY_NEGATIVE as spot fell $263 → $232.
- **07-13 → 07-20:** **FULLY_NEGATIVE every session**, ZGL null, spot $220 → $206.
The short-gamma regime is entrenched and has accompanied the down-leg — dealer
hedging has been *amplifying*, not dampening, the fall. Empirically these flips
precede realized-vol expansion (tool note) → larger ranges into earnings.

### OI trend (30d) `[HIST:oi_trend]`
overall_trend **BUILDING**, total_net_OI change **+171,974**, but
consecutive_build_days = **1** — OI is net-higher over 30d yet not in a sustained
day-over-day build. Consistent with phase-3's modest fresh positioning.

### Multi-day trend table (recent, from `trend.daily_data`) `[HIST:trend]`
Range 2026-06-05 → 2026-07-20; IV-rank change 100 → 99.1 (elevated throughout);
price $279 → $205. Flow alternated (bull/bear) but net **18 bearish / 12 bullish**
days with the **latest = bearish**. Vol/IV have stayed pinned near the top of the
range the entire window (earnings-anchored + declining tape).

### Price context (fz)
**Unavailable this run** — `fz quote FSLR` returned a partial payload (RSI/SMA/52W
all null). Substitute from UW trend: price is **−26.4% over 30 sessions** and at
$205 sits near the low of the visible window (down from $279), i.e. **not
overbought — in an established downtrend near recent lows.** (Advisory; not in the
Kelly `p`.)

### Signal backtest `[HIST:signal_backtest]`
`--signal-type bearish_flow`, 5-day lookback: **win_rate 90.0%, total_signals 10**
(re-run confirmed, not the empty stub). Market-wide base rate for the bearish-flow
signal class — **not FSLR-specific** — over a small N=10. Edge-positive but
low-confidence sample.

## Tool calls
| Tool | Args | Result |
|------|------|--------|
| historical iv-percentile-zscore | FSLR, 252d | pctile 98.5, z +1.22, HIGH_IV (68 sess) |
| historical vrp | FSLR, rw 30d | VRP +0.19, PREMIUM_SELLING |
| historical cumulative-premium-flow | FSLR, 90d | net +$9.3M, MIXED (69 dates) |
| historical pc-ratio-zscore | FSLR, 20d | z −0.75, NORMAL |
| historical gex-time-series | FSLR, 30d, dte 45 | FULLY_NEGATIVE since 07-13 |
| historical oi-trend | FSLR, 30d | BUILDING, +172k, 1 build-day |
| historical trend | FSLR, 30d | −26.4%, 18 bear/12 bull, latest bearish |
| historical signal-backtest | bearish_flow, 5d (market-wide) | 90.0% win, N=10 |

## Tool errors
None. Gap-aware: iv-percentile used **68** of 252 calendar days (the 2026-03-28→
04-24 hole excluded); trend/gex windows (06-05→07-20) sit entirely *after* the gap,
so no cross-hole interpolation. fz technicals absent (partial payload) — noted, not
an error. Trailing tools anchor to latest date = 07-20 (= as-of).

## Verdict for downstream

- **Volatility regime:** **RICH** — IV percentile 98.5, VRP +0.19,
  **PREMIUM_SELLING**. Long-premium structures are expensive; edge favors selling
  vol / defined-risk credit — but earnings (07-30) makes naked short-vol dangerous.
- **Environment:** **premium-SELLING**, short-gamma (amplifying), entrenched
  downtrend. Today's bearish flow is *with* the trend and the dealer regime.
- **Conviction today's signal is HISTORICALLY EDGE-POSITIVE: 3.5/5** — direction
  aligns with a −26% downtrend + stable short gamma + a 90% (N=10) backtest, but
  the 90d flow is MIXED (no long build), the sample is thin, and rich IV caps how
  cheaply the bearish view can be expressed.
- **Three data points:** IV percentile **98.5**; VRP **+0.19 (PREMIUM_SELLING)**;
  `bearish_flow` win rate **90% (N=10)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.90
  win_rate_n:                10
  win_rate_source:           backtest   # market-wide base rate, NOT FSLR-specific; N=10 → apply low-N cap
  ```
- **Open questions:**
  - With IV rich (VRP +0.19) and short gamma, is the best expression a *defined-risk
    debit put spread* (pay up but capped) or a *credit call spread* (sell the rich
    upside vol against the $240 wall)? Phase-9 to choose given the earnings crush.
  - Does the persistent short-gamma regime survive earnings, or does the vanna bid
    (phase-4) flip it POSITIVE post-event as it did intermittently in late June?
  - N=10 backtest — does phase-9 cap Kelly at the low-N tier despite the 90% rate?
