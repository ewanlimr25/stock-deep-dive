# Phase 5 — Historical Context & VRP

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:03:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

ADBE options are **historically expensive into earnings**: IV30d **59.6%**, **100th
percentile / z +1.99** over the trailing year (HIGH_IV) [HIST:iv_percentile_zscore],
and VRP **+0.162** (IV30 59.6% vs realized 43.4%) — a **PREMIUM-SELLING** regime
[HIST:vrp]. Today's net-bullish flow is real but its multi-week backdrop is only
**mildly positive**: 90-day cumulative premium flow is **net +$96.8M bullish**
($1.331B bull vs $1.234B bear over 35 sessions) — i.e. a slight bull tilt that is
**not** a strong stealth accumulation signal [HIST:cumulative_premium_flow]. The
30-day trend table shows ADBE **chopping 234–256 for six weeks then gapping to a
259.21 close on 5/29** (the day of this study) — today is a breakout *attempt* from
a multi-week range, on the most net-bullish flow day in the window. The decisive
sizing input — **`signal-backtest bullish_flow` win_rate = 50.0% (n=8)** — says the
firing signal has **no historical edge** (coin-flip) on the 5-day horizon
[HIST:signal_backtest]. P/C z-score −1.28 (NORMAL, not extreme). Price context is
neutral-to-constructive: RSI 58.8, above SMA50 but **−14.7% below SMA200** and
**−38.5% off the 52-week high** (deep-in-the-doghouse mega-cap mid-bounce).

## Key signals

- **IV30d 100th percentile, z +1.99 — HIGH_IV** → options richest in a year
  [HIST:iv_percentile_zscore].
- **VRP +0.162, PREMIUM_SELLING** (IV 59.6% ≫ realized 43.4%) → structure should
  *sell* vol, not buy it [HIST:vrp].
- **`signal_backtest` bullish_flow win_rate 50.0% (n=8)** — the firing signal is a
  **coin flip** historically; Kelly p has no edge [HIST:signal_backtest].
- **90d cumulative premium flow net +$96.8M bullish** (only +8% bull-over-bear) —
  mild tilt, not stealth accumulation [HIST:cumulative_premium_flow].
- **Price: 6-week 234–256 range, gapping to 259.21 today** — breakout attempt;
  RSI 58.8, +6% above SMA50 but −14.7% vs SMA200, −38.5% off 52wk high
  [HIST:rsi fz][HIST:52w_proximity fz].

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore]` / `[HIST:vrp]`

- IV30d **0.5961**, **iv_percentile 100**, z **+1.989**, regime **HIGH_IV**
  (dates_used 34 — the gap-truncated trailing window, see caveat).
- VRP **+0.1617** (IV30 0.5961 − realized30 0.4344), regime **PREMIUM_SELLING** —
  "options pricing more vol than realized; favour premium selling." Strong steer
  toward **credit/defined-risk structures over long premium**, reinforcing
  phase-4's complacent-skew + earnings-kink read.

### Cumulative premium flow (90d) — `[HIST:cumulative_premium_flow]`

Net **+$96,767,730 bullish** (cum_bull $1,330,618,400 vs cum_bear $1,233,850,670)
across **35 sessions** (gap-spanning — true N, not 90 calendar days). The bull tilt
is real but **modest (~+8%)** — this is *not* the "+persistent ≥60d" stealth-build
signature that would justify high directional confidence. It corroborates a lean,
not a conviction long.

### P/C ratio z-score — `[HIST:pc_ratio_zscore]`

Current P/C **0.468**, 20d mean 0.659, z **−1.277**, extreme **NORMAL**. Today's
call-tilt is below the recent mean (more call-heavy than usual) but **not a 2σ
sentiment extreme** — no contrarian trigger.

### GEX time series — `[HIST:gex_time_series]`

Returned **count 0 / empty** this run (no multi-day ZGL series produced). Treated
as a data gap — phase-4's single-day positive-GEX/long-gamma read stands, but the
**regime-stability / flip-date** history is unavailable. See Tool errors.

### OI trend (30d) — `[HIST:oi_trend]`

**30 consecutive build days**, today net_oi_change **+11,057** (460 contracts up
vs 178 down). OI is **steadily accreting**, consistent with a name being
positioned into earnings — but phase-3 showed today's marginal builds are
**inferred call-writing**, so the accretion is not unambiguously directional-long.

### Multi-day trend (gap-aware, 30 rows) — `[HIST:trend]`

| Date | Close | IV rank | P/C | Flow |
|------|-------|---------|-----|------|
| 05-29 | **259.21** | **100** | 0.47 | bullish |
| 05-28 | 241.44 | 97.2 | 0.63 | bearish |
| 05-27 | 238.24 | 96.1 | 0.73 | bullish |
| 05-22 | 244.76 | 82.3 | 0.92 | bullish |
| 05-20 | 253.37 | 89.9 | 0.89 | bullish |
| 05-15 | 247.61 | 84.7 | 0.49 | bullish |
| 05-08 | 253.06 | 53.9 | 0.60 | bearish |
| 05-01 | 250.71 | 51.1 | 0.50 | bearish |
| 04-27 | 239.31 | 62.1 | 0.78 | bearish |
| 03-27 | 234.84 | 58.3 | 1.31 | bearish |
| 03-20 | 248.15 | 38.1 | 1.03 | bullish |

**14 bullish / 16 bearish days** over the window — a genuinely **mixed** 6-week
tape that has chopped **234–256**, with **today's 259.21 the high of the range** on
a one-day +7pt jump and a fresh IV-rank spike to 100. So today is a **breakout
attempt out of a two-month base**, on heavy call flow, but with no trend
established yet and IV maxed.

### Price context (`fz`, advisory) — `[HIST:rsi fz]` / `[HIST:52w_proximity fz]`

RSI(14) **58.75** (constructive, not overbought), price **+6.04% above SMA50**,
**−14.71% below SMA200**, **Perf YTD −25.94%**, **−38.5% below the 52-wk high
(421.48)** and **+15.65% above the 52-wk low (224.13)**. ADBE is a **beaten-down
mega-cap bouncing off its base, still in a longer-term downtrend** (below
SMA200). The bullish flow is a counter-trend bounce attempt, not a high momentum
breakout — tempers chase-risk on the long, but RSI leaves room before overbought.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --symbol ADBE --lookback-days 252` | IV30 0.596, pctile 100, z +1.99, HIGH_IV |
| `uw historical vrp --symbol ADBE --realised-window-days 30` | VRP +0.162, PREMIUM_SELLING |
| `uw historical cumulative-premium-flow --symbol ADBE --days 90` | net +$96.8M bull (35 sessions) |
| `uw historical pc-ratio-zscore --symbol ADBE --lookback-days 20` | z −1.28, NORMAL |
| `uw historical gex-time-series --symbol ADBE --days 30 --dte-max 45` | **empty (count 0)** — see Tool errors |
| `uw historical oi-trend --symbol ADBE --days 30 --top-n 10` | 30 build days, today +11,057 |
| `uw historical trend --symbol ADBE --days 30` | 14 bull/16 bear; 234–256 range, 259.21 today |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20` | **win_rate 50.0%, n=8**, avg move −0.43% |
| `fz quote ADBE` (price context) | RSI 58.8, +6% SMA50, −14.7% SMA200, −38.5% off 52wH |

## Tool errors

- `uw historical gex-time-series --symbol ADBE` returned `count 0` / empty — no
  multi-day ZGL series. Regime-stability history unavailable; phase-4's single-day
  long-gamma read used instead. Not surfaced as an engine error (empty return).
- **Latest-anchor caveat:** `iv-percentile-zscore`, `pc-ratio-zscore`, `oi-trend`,
  `cumulative-premium-flow`, `signal-backtest`, and `vrp`'s realized leg anchor to
  the **latest available date (2026-05-29 = as-of here)**; a re-run after a new
  session would shift them.
- **Gap caveat:** the 30d/90d windows span the **2026-03-28→04-24 hole**;
  `dates_used`/`n_dates` (34/35) are the *true* session counts, not calendar spans.

## Verdict for downstream phases

- **Volatility regime:** **RICH (IV pctile 100, VRP +0.162 premium-selling).**
  Favor **credit/defined-risk**; long premium is paying top-of-range vol into a
  binary.
- **Premium environment:** premium-**selling**.
- **Conviction that today's signal is historically edge-positive:** **2 / 5.** The
  flow is unusually one-sided (phase-0.5) but the **backtest win-rate is 50%
  (coin-flip, n=8)** and the 90d tilt is only mild — there is **no demonstrated
  historical edge** for the bullish_flow signal on the 5-day horizon.
- **Three specific datapoints:** IV %ile **100** [HIST:iv_percentile_zscore]; VRP
  **+0.162** [HIST:vrp]; signal win-rate **0.50 (n=8)** [HIST:signal_backtest].
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.50
  win_rate_n:                8
  win_rate_source:           backtest
  ```
  Kelly p_raw = 0.50; N-cap for n<10 = 0.75 (non-binding); **p = 0.50** → win-rate
  sizing map = **half size or less**; SHORT-side floor n/a (long). The 0.50 edge is
  the dominant size-limiter for this trade.
- **Open questions:** Does today's 259.21 breakout from the 234–256 base hold, or
  mean-revert in the long-gamma regime toward the 250 pin? Is the 30-day OI build
  directional or (per phase-3) call-writing? Will earnings 6/11 resolve the
  range — i.e. is the right expression *waiting for the print* rather than chasing
  the pre-earnings IV?
