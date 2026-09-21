# Phase 5 — Historical Context & VRP

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:32:00-04:00
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The historical frame **tempers** the phase-2 anomaly. IV sits mid-range (44th 1y
percentile, z −0.53, IV30d 65.6%, regime NORMAL) and **VRP is +0.084 → PREMIUM_SELLING**
(IV 65.6% > RV 57.2%) — options are slightly rich, favoring credit over debit
structures. Ninety-day cumulative options flow is **balanced/MIXED** (bull $114.3M vs
bear $111.5M, net +$2.8M) — there is **no persistent directional options accumulation**;
the darkpool is the only real signal. Dealer regime has been **stably long-gamma for 30
straight sessions (no flips)**, and price has **churned sideways $11.72 → $11.85 (+1.1%)
over that month — even the $644M 07-09 block did not move it out of range.** OI has
built **7 consecutive sessions** (call-skewed). The `dark_pool_accumulation` **signal
backtest returned no data (total_signals 0)** → no empirical win-rate; phase-9 sizes on
the conviction bin. Net: an unusual print sitting inside a sideways, premium-selling,
long-gamma consolidation — the anomaly is real but historically **unproven** and,
critically, **price-inert so far**.

## Key signals

- **VRP +0.0837, regime PREMIUM_SELLING** (IV30 65.6% vs RV30 57.2%) `[HIST:vrp]` — sell premium, don't buy it.
- **IV percentile 44.4 (1y), z −0.53, regime NORMAL** `[HIST:iv_percentile_zscore]` — vol is unremarkable; no cheap-vol tailwind for long options.
- **90d cumulative flow MIXED**: bull $114.3M vs bear $111.5M, net **+$2.8M** over 64 sessions `[HIST:cumulative_premium_flow]` — options flow has no directional edge.
- **GEX stably POSITIVE 30/30 sessions, zero regime flips**; total_gex decayed 28.6M→15.6M, ZGL 7.9→5.70 `[HIST:gex_time_series]` — durable long-gamma/range regime.
- **Price sideways: 11.72 → 11.85 over 30d** (bull 13 / bear 17 days, latest flow bearish) `[HIST:trend]` — the 07-09 mega-block was **absorbed without a price break**.
- **OI building 7 consecutive sessions** (net +11,044 on 07-13, top build $18 Jan-27 call) `[HIST:oi_trend]` — steady call-OI accretion under a flat price.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore / vrp]`
- current_iv30d **0.6557**, iv_percentile **44.44** (1y), iv_zscore **−0.534**, regime **NORMAL**, dates_used **63** (gap-aware).
- VRP **+0.0837**, realised_vol30 **0.572**, regime **PREMIUM_SELLING**. IV modestly rich vs realized → **credit structures favored**; long premium fights a negative carry.

### Cumulative premium flow (90d / 64 sessions) `[HIST:cumulative_premium_flow]`
- cumulative_bullish **$114,259,480**, cumulative_bearish **$111,499,499**, net_flow **+$2,759,981**, trend_direction **MIXED**. Two-and-a-half months of essentially balanced options flow — corroborates phase-1's "no options edge."

### P/C ratio z-score `[HIST:pc_ratio_zscore]`
- pc_ratio **0.265**, z **−0.662** — call-skewed but **not extreme** (|z| < 1). No contrarian sentiment signal; the call skew is the name's normal state.

### GEX time series (30d) `[HIST:gex_time_series]`
- 30 sessions 2026-05-29 → 2026-07-13, **regime POSITIVE every day, regime_flip_dates null**. total_gex 28.6M → 15.6M, ZGL 7.9 → 5.70. Durable long-gamma — no dealer-hedging regime change to expand ranges.

### OI trend (30d) `[HIST:oi_trend]`
- **consecutive_build_days 7**, overall_trend building. 07-13: 144 contracts increasing vs 66 decreasing, net_oi_change +11,044; top builds $18 Jan-27 call (+3,742) and $13 Jul-17 call (+2,548). Steady call-OI accumulation beneath a flat tape.

### Multi-day trend (30d) `[HIST:trend]`
- date_range 2026-05-29 → 2026-07-13, days_analyzed 30, bullish_days 13 / bearish_days 17, **price_change 11.72 → 11.85**, iv_rank 43.3 → 40.4, flow_direction_latest **bearish**. A tight sideways consolidation; the 07-09 block did not break it.

### Price context (`fz`)
- Skipped — `fz quote PATH` carries no RSI/SMA/52W/Perf fields (reduced fundamentals block; `fz_available=yes` but technicals null). UW trend above stands in: price is mid-consolidation ~$11.8, flat over 30d.

### Signal backtest `[HIST:signal_backtest]`
- `--signal-type dark_pool_accumulation --lookback-days 5`: **`{note:"no backtest results", total_signals:0}`** on both the initial run **and the mandated re-run**. No empirical base rate available for this signal class on the current tape → `win_rate_source=null`.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | 
|---------|--------------------------|
| `historical iv-percentile-zscore --lookback-days 252` | pctile 44.4, z −0.53 ← `.iv_percentile`,`.iv_zscore` |
| `historical vrp --realised-window-days 30` | +0.0837 PREMIUM_SELLING ← `.vrp`,`.regime` |
| `historical cumulative-premium-flow --days 90` | net +$2.76M MIXED ← `.net_flow`,`.trend_direction` |
| `historical pc-ratio-zscore --lookback-days 20` | z −0.66 ← `.z_score` |
| `historical gex-time-series --days 30` | POSITIVE 30/30, no flips ← `.trajectory`,`.regime_flip_dates` |
| `historical oi-trend --days 30` | 7 build days ← `.consecutive_build_days` |
| `historical trend --days 30` | 11.72→11.85 flat ← `.price_change` |
| `historical signal-backtest --signal-type dark_pool_accumulation` (×2) | total_signals 0 ← `.total_signals` |

## Tool errors

- `signal-backtest` returned the empty stub on both runs — recorded as `win_rate_source=null` per the phase rule (not a harness error; no history for this signal class).
- **Gap note:** all trailing lookbacks anchor to latest date 2026-07-13; the 90d/252d windows span the known 2026-03-28→04-24 hole (dates_used 63, dates_covered 64 — the true N, not calendar days). No sign of silent interpolation across the gap.

## DATA NOTE / CORRECTION

- Correct fields: IV z is `.iv_zscore` (not `.zscore`); cumulative flow is `.net_flow`/`.cumulative_bullish`; GEX series is `.trajectory` (not `.series`). First pass used wrong keys → nulls; values above trace to corrected paths.

## Verdict for downstream

- **Volatility regime:** FAIR-to-slightly-RICH — IV 44th pctile, **VRP +0.084 PREMIUM_SELLING**. Favor credit structures; long premium carries negative.
- **Environment:** premium-SELLING; options flow directionally balanced (90d net +$2.8M); durable long-gamma range.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5.** The darkpool print is genuinely unusual, but (a) no backtest base rate, (b) 90d options flow is a coin-flip, (c) price is inert — a month of consolidation, unmoved by the $644M block. Unproven, not disproven.
- **Three specific datapoints:** IV %ile **44.4**, VRP **+0.084**, signal win-rate **null (n=0)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              dark_pool_accumulation
  signal_backtest_win_rate:  null
  win_rate_n:                0
  win_rate_source:           null
  ```
- **Open questions:** Is the flat post-block price *coiling accumulation* (bullish) or *mechanical absorption of an offering/index cross* (non-directional)? Only phase-6 news resolves it. Does the premium-selling VRP argue for expressing any bullish view via short puts / covered structures rather than long calls?
