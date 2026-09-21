# Phase 5 — Historical Context & VRP

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:31:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

The defining fact only the multi-day series reveals: **today was a +12% breakout day** —
PATH closed $13.11 vs $11.71 on 2026-05-29, reclaiming its 200-day SMA out of a
beaten-down $9.48–11.71 April/May base (the stock is still −20% YTD and −34% below its
52-week high). Against that, the historical backdrop is *not* a stealth bull build:
**cumulative 90-day premium flow is MIXED** ($73.4M bullish vs $72.3M bearish, net only
+$1.1M over 36 sessions), so today's 100th-percentile bullish print (phase-0.5) is an
**outlier spike, not the continuation of a campaign**. IV is fair-to-cheap by its own
1-year history (40th percentile) yet **rich vs realized — VRP +0.139, regime
PREMIUM_SELLING**. The bullish-flow signal class has been **edge-negative recently
(win 44.4%, avg move −1.25%, n=9)**. OI has nonetheless built for 30 straight sessions
(+784k, direction-neutral), and the GEX regime is stably long-gamma. Net: a sharp,
overbought breakout spike into 200-day resistance, in a premium-selling, mean-reverting
regime — consolidation/mean-reversion is the base case; the **31% short float is the
only clean upside catalyst**.

## Key signals

- **+12% breakout day**: spot $11.71 (05-29) → **$13.11 (06-01)**, reclaiming 200-day SMA
  [HIST:gex_time_series][HIST:trend]
- **Cumulative 90d flow MIXED**: bull $73.4M ≈ bear $72.3M, net +$1.1M, trend_direction
  MIXED — no persistent build [HIST:cumulative_premium_flow]
- **VRP +0.139, PREMIUM_SELLING** (iv30d 72.3% vs realized 58.4%) [HIST:vrp]
- **IV percentile 40th** (1y, z −0.66), regime NORMAL, 35 sessions used [HIST:iv_percentile_zscore]
- **bullish_flow backtest: win 44.4%, n=9, avg move −1.25%** (edge-negative, market-wide);
  dark_pool_accumulation: **no results (null)** [HIST:signal_backtest]
- **OVERBOUGHT & extended**: RSI 73.9, +21.3%/+22.0% above 20/50-day SMA, at 200-day
  (+0.70%), −20% YTD, −34% from 52w high [HIST:rsi fz][HIST:52w_proximity fz]
- **OI BUILDING 30 consecutive days** (+783,961 net OI), overall_trend BUILDING
  [HIST:oi_trend]

## Detailed findings

### IV regime (percentile + z-score + VRP)

- `iv-percentile-zscore`: iv_percentile **40**, iv_zscore −0.662, current_iv30d **72.3%**,
  `dates_used` **35** (gap-aware N), regime **NORMAL**. IV sits mid-low in its own 1-year
  range — not historically expensive *on an absolute-percentile basis*.
- `vrp`: **+0.1388** (iv30d 72.3% − realized 58.4%), regime **PREMIUM_SELLING** —
  "Options pricing more vol than realised — favour premium selling." So while IV's
  *percentile* is moderate, it is **rich relative to what the stock actually delivers**
  → credit structures are favoured over debit. [HIST:vrp]

### Cumulative premium flow (90d → 36 sessions, gap-crossing)

- `cumulative_bullish` $73,414,323 vs `cumulative_bearish` $72,291,605 → `net_flow`
  **+$1,122,718**, `trend_direction` **MIXED**. `dates_covered` = 36 sessions
  (2026-03-13 → 06-01, incl. the 03-28→04-24 gap). **No 60d+ persistent directional
  build** — the heuristic for high-confidence stealth accumulation does NOT fire. Today's
  +$2.18M is a one-day outlier against a 3-month balance. [HIST:cumulative_premium_flow]

### P/C ratio z-score (sentiment extreme?)

- `pc-ratio-zscore`: current 0.2589 vs 20d mean 0.3948, **zscore −0.612**, `extreme`
  **NORMAL**. Call-heavy today but only mildly below its own mean — **not** a contrarian
  sentiment extreme. [HIST:pc_ratio_zscore]

### GEX time series (regime stability)

- 30-session `trajectory`: regime **POSITIVE on 29 of 30 sessions** (single 1-day flip to
  NEGATIVE on 2026-05-05, back POSITIVE 05-06; last flip 18 sessions ago). ZGL hovered
  $6.5–8.1 throughout. **Stable long-gamma / mean-reversion regime — no recent flip**, so
  no "transition → larger ranges" flag.
- Spot path: chopped $9.48–10.93 through April/early-May, base-built $10.5–11.7 mid-May,
  then **$11.71 → $13.11 on 06-01 (+12%)**. Notably, price *rose through* the long-gamma
  (dealer mean-reversion) headwind — a mild bullish tell, consistent with short-covering
  pressure overwhelming the pin. [HIST:gex_time_series]

### OI trend

- `oi-trend`: overall_trend **BUILDING**, `consecutive_build_days` **30**,
  `total_net_oi_change` **+783,961**, days_analyzed 30. Sustained structural position
  growth (the phase-3 LEAP-call base + collar legs) — but premium flow (above) is
  balanced, so this is *position accumulation, not directional conviction*. [HIST:oi_trend]

### Multi-day trend table

- `trend` (days_analyzed 30, range 2026-03-23 → 06-01): bullish_days **13**, bearish_days
  **17**, price_change **$12.13 → $13.10**, iv_rank_change 45.7 → 53.3, flow_direction_latest
  **bullish**. Net: a grind with more down-days than up-days, capped by today's spike. The
  30 "sessions" span the gap — calendar ≠ continuous. [HIST:trend]

### Price context (`fz`, advisory EOD cross-check)

| Metric | Value | Read |
|--------|-------|------|
| RSI(14) | **73.87** | **overbought** |
| price vs SMA20 | **+21.33%** | sharply extended short-term |
| price vs SMA50 | **+22.04%** | extended |
| price vs SMA200 | **+0.70%** | **at the 200-day (decision line)** |
| Perf YTD | **−20.07%** | beaten-down name |
| 52W High | $19.84 (**−33.97%** below) | far from highs |
| 52W Low | $9.20 (**+42.39%** above) | well off the low |

The bullish flow is chasing a **+12% spike into overbought territory, right at the
200-day SMA** — a textbook stall/resistance zone. This *tempers* a clean-breakout thesis
(advisory; does not enter Kelly `p`). [HIST:rsi fz][HIST:52w_proximity fz]

### Signal backtest (current signal's historical edge)

- `bullish_flow` (matches phase-1's mild bullish net): **win_rate 44.4%, total_signals 9,
  avg_move_pct −1.25%**. Below the 0.45 line and a *negative* average forward move →
  historically edge-negative (low N=9, market-wide base rate). [HIST:signal_backtest]
- `dark_pool_accumulation` (phase-2's signal): **no backtest results, total_signals 0**
  (re-run once per protocol — still empty) → not usable; `win_rate_source` for it is null.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | N |
|---------|--------------------------|---|
| `historical iv-percentile-zscore --lookback-days 252` | iv_pctile 40, iv30d 72.3% ← `.iv_percentile`,`.current_iv30d`; N ← `.dates_used`=35 | 35 |
| `historical vrp --realised-window-days 30` | VRP +0.139, PREMIUM_SELLING ← `.vrp`,`.regime` | 30 |
| `historical cumulative-premium-flow --days 90` | net +$1.1M MIXED ← `.net_flow`,`.trend_direction` | 36 |
| `historical pc-ratio-zscore --lookback-days 20` | z −0.612 NORMAL ← `.zscore`,`.extreme` | 20 |
| `historical gex-time-series --days 30` | POSITIVE 29/30, +12% spot move ← `.trajectory[]`,`.regime_flip_dates` | 30 |
| `historical oi-trend --days 30` | BUILDING, +784k, 30 build days ← `.overall_trend`,`.total_net_oi_change` | 30 |
| `historical trend --days 30` | 13 bull / 17 bear days ← `.bullish_days`,`.bearish_days` | 30 |
| `historical signal-backtest bullish_flow` | win 44.4% n=9 avg −1.25% ← `.win_rate`,`.total_signals`,`.avg_move_pct` | 9 |
| `fz quote PATH` | RSI 73.87, +21% vs SMA20 ← `.fundamentals."RSI (14)"`,`.SMA20` | EOD |

## Tool errors

<none — `gex-time-series` and `oi-trend` nest their series under `trajectory`/`daily_data`
rather than a `series` key; re-extracted the correct fields. No fabricated values.>

## Verdict for downstream phases

- **Volatility regime:** IV **fair-to-cheap by 1-year percentile (40th)** but **rich vs
  realized (VRP +0.139)** → net a **premium-SELLING** environment. Favor credit / defined-
  risk-short-vol structures over naked debit longs.
- **Premium environment:** **premium-selling** (VRP>0, long-gamma, vol-suppressed).
- **Is today's signal historically edge-positive? NO / WEAK — conviction 2/5.** bullish_flow
  base rate 44.4% / −1.25% avg; cumulative 90d flow MIXED (no build); price overbought
  (RSI 74) and +21% extended into 200-day resistance. The lone structural positive is the
  30-session OI build (direction-neutral) and price rising through the gamma pin.
- **Three datapoints:** IV percentile **40**; VRP **+0.139 (PREMIUM_SELLING)**; bullish_flow
  win-rate **44.4% (n=9, avg −1.25%)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow
  signal_backtest_win_rate:   0.444
  win_rate_n:                 9
  win_rate_source:            backtest
  ```
  (Kelly `p` = 0.444, n=9 → low confidence, below break-even; phase-9 applies the
  N-conditional cap and should lean to the small/defined-risk end. dark_pool_accumulation
  backtest returned no results → not usable as `p`.)
- **Open questions:**
  1. Can the 31% short float (phase-0/7c) force a squeeze that overrides the long-gamma
     pin + max-pain-$11 gravity, or does the spike mean-revert into the $13 pin?
  2. What catalyzed the +12% one-day move (no earnings until Sep)? Phase-6/7c must
     identify it — a fundamental catalyst vs a pure short-squeeze changes the whole thesis.
