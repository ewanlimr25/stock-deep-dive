# Phase 5 — Historical Context & VRP

**Ticker:** BABA · **As-of:** 2026-07-23 (trailing tools anchor to latest = 2026-07-23)
**Generated:** 2026-07-24
**Upstream:** phase-4 (short-gamma flip); phase-1 (bearish-leaning flow → backtest
`bearish_flow`); phase-0 gap note (2026-03-28→04-24 hole).

## Summary

IV is **rich vs its own year** (IV30d 47.2%, **84.5th percentile**, z +1.09, regime HIGH_IV)
but **VRP is FAIR** (IV 47.2% vs realized 48.2% → VRP −0.011) — realized vol has kept pace, so
there is **no clean premium-buy/sell edge from vol alone.** The important tension for the trade:
the **90-day cumulative premium flow is net BULLISH (+$625M, bull $3.14B vs bear $2.51B)** and
OI has **built 30 consecutive sessions** (BUILDING, +1.39M net) — a constructive medium-term
backdrop — yet the **latest flow is bearish**, the dealer regime **flipped POSITIVE→NEGATIVE on
2026-07-21** (short gamma, phase-4), and the **`bearish_flow` signal backtests 87.5% (n=8, avg
move −3.52%)**. Net read: **a fresh short-term bearish/pullback tilt inside a broader
constructive, range-bound tape** ($114–118 chop, IV rank rising 40→61 over 30d). The bearish
edge is real but small-N and cuts against the bullish 90d flow — tactical, not structural.

## Key signals

- **IV rich vs 1y, fair vs realized** — 84.5th pctile / z +1.09, but VRP −0.011 FAIR `[HIST:iv_percentile_zscore]` `[HIST:vrp]`
- **90d cumulative flow net BULLISH +$625M** — constructive backdrop that caps the bearish
  conviction `[HIST:cumulative_premium_flow]`
- **`bearish_flow` backtest 87.5% win, n=8, avg −3.52%** — strong but small-N base rate
  `[HIST:signal_backtest]`
- **Dealer regime unstable — 6 flips/30d, latest POS→NEG on 2026-07-21** (short gamma now)
  `[HIST:gex_time_series]`
- **30 consecutive OI-build days** (+1.39M net); 30d trend 19 bull / 11 bear days, price
  ~flat ($115.4→$114.1), IV rank 40→61 `[HIST:oi_trend]` `[HIST:trend]`

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- IV30d **47.17%**, **iv_percentile 84.51** (HIGH_IV), z-score **+1.086**. dates_used **71**
  (window crosses the 2026-03-28→04-24 gap — N=71 *available* sessions, not a contiguous span).
- VRP = IV30d − RV30 = 47.17% − 48.24% = **−0.011**, regime **FAIR** — *"IV close to realised —
  no clear edge from VRP alone."* So the high 1y percentile is a rich-IV *level*, but not a rich
  *risk premium*: realized vol is running just as hot. Slight lean to defined-risk/premium-neutral
  structures over naked long premium.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

Cumulative **bullish $3.14B vs bearish $2.51B → net +$625M**, trend_direction **BULLISH**
(72 sessions covered, crosses the gap). **The medium-term flow backdrop is bullish** — today's
marginally-bearish tape (phase-1 net −$1.68M) is a blip against a constructive quarter. This is
the single strongest counter to the short-term bearish thesis and caps its conviction.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

current PC **0.372** vs 20d mean 0.478, z **−0.382**, extreme **NORMAL**. Call-heavier than usual
but **not** a sentiment extreme — no contrarian trigger.

### GEX time series (30d) `[HIST:gex_time_series]`

**6 regime flips in 30 days** — a highly unstable dealer regime. Flip dates: 07-01 (NEG→POS),
07-06 (POS→NEG), 07-08 (NEG→POS), 07-14 (POS→NEG), 07-15 (NEG→POS), **07-21 (POS→NEG, spot
118.08, ZGL 119.15)**. BABA has been in **short gamma since 2026-07-21** — phase-4's negative GEX
is a 2-session-old flip, not a stable state. Frequent flips ⇒ **larger intraday ranges expected**,
whipsaw risk elevated.

### OI trend (30d) `[HIST:oi_trend]`

**30 consecutive build days**, total net OI change **+1.39M**, overall_trend **BUILDING**. Daily
net-OI changes are uniformly positive (e.g. +54k, +41k, +37k in mid-June). Sustained OI
accumulation — consistent with the bullish 90d premium flow; direction not specified by the tool
but phase-3 showed today's build is call-tilted.

### Multi-day trend table (30d) `[HIST:trend]`

| Field | Value |
|-------|-------|
| date_range | 2026-06-10 → 2026-07-23 (30 sessions) |
| bullish days / bearish days | **19 / 11** |
| price change | $115.38 → **$114.06** (~−1.1%, effectively flat/chop) |
| IV rank change | **40.2 → 61.2** (rising) |
| flow_direction_latest | **bearish** |

Read: a **range-bound month** ($114–118) with more bullish-flow days than bearish, flat price, but
**rising IV rank** — the market is paying up for vol into a sideways tape, and the latest session
tipped bearish.

### Price context (`fz`)

**Omitted** — `fz` returns a null RSI/SMA/52W/Perf set for this ADR (phase-0: reduced Finviz
fundamentals for BABA). No independent EOD cross-check available; not a gate.

### Signal backtest `[HIST:signal_backtest]`

`signal-type = bearish_flow`, lookback 5d, **market-wide base rate** (not BABA-specific):
**win_rate 87.5%**, **total_signals n=8**, **avg_move_pct −3.52%**. High hit-rate and a
meaningful −3.5% average down-move when it fires — **but n=8 is below the 10-firing
low-confidence threshold**, and it conflicts with BABA's own bullish 90d flow. Treat as a
supportive-but-soft tactical edge; phase-9 must apply the N-conditional Kelly cap.

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| IV pctile/z | `uw historical iv-percentile-zscore --symbol BABA --lookback-days 252` | `.{current_iv30d,iv_percentile,iv_zscore,regime,dates_used}` |
| VRP | `uw historical vrp --symbol BABA --realised-window-days 30` | `.{iv30d,realised_vol,vrp,regime}` |
| 90d flow | `uw historical cumulative-premium-flow --symbol BABA --days 90` | `.{cumulative_bullish,cumulative_bearish,net_flow,trend_direction}` |
| PC z | `uw historical pc-ratio-zscore --symbol BABA --lookback-days 20` | `.{current_pc_ratio,zscore,extreme}` |
| GEX flips | `uw historical gex-time-series --symbol BABA --days 30 --dte-max 45` | `.regime_flip_dates[]` |
| OI trend | `uw historical oi-trend --symbol BABA --days 30 --top-n 10` | `.{consecutive_build_days,total_net_oi_change,overall_trend}` |
| trend | `uw historical trend --symbol BABA --days 30` | `.{date_range,bullish_days,bearish_days,price_change,iv_rank_change,flow_direction_latest}` |
| backtest | `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20` (market-wide) | `.{win_rate,total_signals,avg_move_pct}` |

## Tool errors

None. All trailing tools anchor to the latest available date = **2026-07-23** (= as-of), so this
run is as-of reproducible. Windows crossing the **2026-03-28→04-24 gap** are quoted at their true
available-N (`dates_used=71`, `dates_covered=72`) per `[[uw-available-dates-unsorted]]` /
`[[calibration-2026-05-30-aborted]]` gap discipline — no annualization across the hole.

## Verdict for downstream

- **Volatility regime: RICH by level (84.5th pctile), FAIR by risk-premium (VRP −0.011).** Not a
  clean premium-buy or premium-sell environment; lean **defined-risk / spreads** over naked premium.
- **Environment:** premium-neutral. IV rank rising into a range-bound tape → **vol-of-vol** risk
  (6 GEX flips/30d) argues against short-vol without a hedge.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 3/5.** The `bearish_flow`
  backtest (87.5%, avg −3.5%) is supportive, but small-N (8) and **directly opposed by the bullish
  90d cumulative flow** → the honest edge is a **short-term tactical pullback**, not a structural
  short. The constructive medium-term backdrop is the reason conviction isn't higher.
- **Three specific datapoints:** IV percentile **84.5**; VRP **−0.011 (FAIR)**; `bearish_flow`
  win rate **0.875 (n=8, avg −3.52%)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.875
  win_rate_n:                8
  win_rate_source:           backtest   # market-wide base rate, NOT BABA-specific; n<10 → low-confidence, apply N-cap; conflicts with bullish 90d flow
  ```
- **Open questions:** Does the 90d-bullish vs 5d-bearish split resolve to a **range-fade** (short
  $118–120, cover $110–112) rather than a directional short? Does phase-6 macro carry a China/
  tariff catalyst that would let the short-gamma regime break $112 (the complacent-skew tail)?
