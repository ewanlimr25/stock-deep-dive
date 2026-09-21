# Phase 5 — Historical Context & VRP

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18 (trailing tools anchor to latest available = 2026-06-18)
**Generated:** 2026-06-20T13:11:10Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bullish flow is **historically edge-weak and counter-trend.** Vol is cheap
(IV percentile **0**, LOW_IV, iv30d 0.588, z −1.277) but VRP is **FAIR** (−0.027, IV ≈
realized) so there's no strong vol edge — mildly favors long premium. The 90-day
cumulative premium flow is **net −$3.29M, MIXED/slightly bearish** — the bullish sweep
campaign (phase-1) is a *recent-week* event, not a sustained 90d build. OI is genuinely
**BUILDING** (10 consecutive days, +693,140 net OI, call-skewed). But the killer
context: the **`bullish_flow` signal-backtest win_rate is 37.5% (n=8, avg move −0.51%)**
— below the 0.45 edge floor — and price is in a **clear downtrend** (fz: −37% YTD, −48%
from 52w high, below SMA20/50/200, near 52w low $9.20). Dealer gamma is degrading: ZGL
collapsed **7.6 → 4.0 → 2.34** over the last 3 sessions with total_gex flipping negative.

## Key signals

- **IV cheap, vol bleeding:** iv_percentile **0** (LOW_IV, 48 sessions used), iv_zscore
  −1.277; iv_rank fell **70.94 → 34.55** over 30d [HIST:iv_percentile_zscore][HIST:trend].
- **VRP FAIR:** vrp −0.0269 (iv30d 0.5879 vs realised 0.6147) — no clear premium edge [HIST:vrp].
- **90d flow MIXED/slightly bearish:** cumulative_bullish $91.15M vs bearish $94.44M,
  net **−$3.29M**, trend MIXED [HIST:cumulative_premium_flow].
- **OI BUILDING:** overall_trend BUILDING, consecutive_build_days **10**, total_net_oi
  +693,140 [HIST:oi_trend].
- **Bullish_flow backtest below floor:** win_rate **37.5%**, n=8, avg_move −0.51%,
  in-sample [HIST:signal_backtest].
- **Counter-trend (fz, advisory):** RSI 41.7, SMA20 −7.7% / SMA50 −3.9% / SMA200 −21.0%,
  Perf YTD −37.3%, 48% below 52w high [HIST:rsi fz][HIST:52w_proximity fz].

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore][HIST:vrp]`

- current_iv30d 0.5879; iv_percentile **0** (LOW_IV); iv_zscore −1.277; **dates_used 48**
  (not 252 — the 1y lookback crosses the 2026-03-28→04-24 hole; true N=48).
- VRP **−0.0269**, regime **FAIR** ("IV close to realised — no clear edge"). RV30 0.6147.
- Read: vol is at the bottom of its (limited) range → **mild edge to long premium / debit**,
  but VRP says marginal. Vol has been bleeding (iv_rank 70.9 → 34.6 over 30d).

### Cumulative premium flow (90d, gap-aware) — `[HIST:cumulative_premium_flow]`

dates_covered = 49 sessions (2026-03-13 → 2026-06-18, **gap 03-28→04-24 excluded** — not a
contiguous 90 calendar days). cumulative_bullish $91,149,633 vs cumulative_bearish
$94,443,724 → **net_flow −$3,294,091, trend_direction MIXED.** The recent bullish sweep
campaign does **not** show up as a sustained 90d directional build.

### P/C ratio z-score — `[HIST:pc_ratio_zscore]`

current_pc_ratio 0.3348 vs mean 0.3728 (20d), std 0.1682, z −0.226 → **extreme: NORMAL.**
No sentiment extreme; PCR is unremarkable for the name.

### GEX time series (30d, dte≤45) — `[HIST:gex_time_series]`

regime_flip_dates **null** (label stayed POSITIVE — spot never crossed ZGL). BUT the
structure is **degrading**: ZGL fell **7.65 (6/16) → 4.02 (6/17) → 2.34 (6/18)** and
total_gex flipped **negative** on 6/12 (−14.0M), 6/17 (−1.2M), 6/18 (−7.3M). Confirms
phase-4's contradiction — the POSITIVE label is masking a thinning gamma cushion and
near-spot short gamma; vol-expansion risk is rising.

### OI trend (30d) — `[HIST:oi_trend]`

overall_trend **BUILDING**, consecutive_build_days **10**, total_net_oi_change **+693,140**.
Sustained accretion (call-skewed per phase-3) — the one genuinely persistent bullish
structural signal, though slow.

### Multi-day trend (30d, 2026-05-07 → 2026-06-18) — `[HIST:trend]`

price_change **10.93 → 10.27** (−6%); bullish_days 14 / bearish_days 16 (balanced, slight
bearish); flow_direction_latest bullish; iv_rank 70.94 → 34.55. Range-bound $9.47–$10.93,
spot mid-range. days_analyzed 30 / date_range 2026-05-07→06-18 (post-gap window).

### Price context (fz, advisory cross-check) — `[HIST:rsi fz][HIST:52w_proximity fz]`

| metric | value |
|--------|-------|
| RSI(14) | 41.71 (neutral-weak, not oversold) |
| vs SMA20 / 50 / 200 | −7.72% / −3.93% / −21.03% (below all) |
| Perf Month / YTD | −2.65% / **−37.34%** |
| 52W High | $19.84 (**−48.24%** below) |
| 52W Low | $9.20 (+11.63% above) |

**Strong structural downtrend; price below every major MA, closer to 52w low than high.**
The bullish options flow is **counter-trend** — tempers any fresh-breakout thesis. (Advisory;
not in Kelly `p`.)

### Signal backtest — `[HIST:signal_backtest]`

signal_type **bullish_flow**, win_rate **37.5%**, total_signals **8**, avg_move_pct
**−0.51%**. methodology_notes: "In-sample backtest — not a robust live edge." **Market-wide
base rate** for the signal class (no `--symbol`), not PATH-specific. Re-checked once; result
populated (not the empty stub). **37.5% < 0.45 floor → historically edge-negative.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows/N |
|------------------|---------------------|--------|
| `historical iv-percentile-zscore --lookback-days 252` | iv_pctile 0, z −1.277, LOW_IV ← top-level | N=48 |
| `historical vrp --realised-window-days 30` | vrp −0.0269, FAIR ← `.vrp/.regime` | 30 |
| `historical cumulative-premium-flow --days 90` | net −$3.29M, MIXED ← `.net_flow/.trend_direction` | 49 sess |
| `historical pc-ratio-zscore --lookback-days 20` | z −0.226, NORMAL ← `.zscore/.extreme` | 20 |
| `historical gex-time-series --days 30 --dte-max 45` | ZGL 7.65→2.34, gex flipped neg ← `.trajectory[]` | 30 |
| `historical oi-trend --days 30 --top-n 10` | BUILDING, 10 build-days, +693,140 ← `.overall_trend/...` | 30 |
| `historical trend --days 30` | 10.93→10.27, iv_rank 70.9→34.6 ← `.price_change/.iv_rank_change` | 30 |
| `historical signal-backtest --signal-type bullish_flow --lookback-days 5` | win_rate 37.5%, n=8, avg −0.51% ← top-level | n=8 |
| `fz quote PATH --agent` | RSI 41.7, −48% from 52w high ← `.fundamentals` | 1 |

## Tool errors

_none._ Gap caveat applied: `iv-percentile-zscore` used 48 sessions (1y window crosses the
03-28→04-24 hole); `cumulative-premium-flow` covers 49 sessions, not 90 calendar days. All
trailing tools anchor to latest = 2026-06-18 (= as-of), so reproducible at this run.

## DATA NOTE / CORRECTION

No corrections. GEX time series independently corroborates phase-4's POSITIVE-label
contradiction (ZGL collapse + negative total_gex on 6/12/6/17/6/18). All values via `jq`.

## Verdict for downstream

- **Volatility regime:** **Cheap-ish (LOW_IV, percentile 0) but FAIR VRP** → mild edge to
  **long premium / debit** over credit; vol has been bleeding (iv_rank 70.9→34.6).
- **Premium environment:** Premium-**buying** slightly favored on price (cheap IV), but the
  *directional* premium edge is weak — 90d flow is MIXED and the bullish_flow base rate loses.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5 (edge-NEGATIVE
  leaning).** Bullish_flow backtest 37.5%<0.45, 90d flow mixed, counter-trend price. The only
  durable positive is the 10-day OI build (slow).
- **Three specific datapoints:** IV %ile **0** (LOW_IV); VRP **−0.027** (FAIR); bullish_flow
  win rate **37.5%** (n=8, avg move −0.51%).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:             bullish_flow
  signal_backtest_win_rate: 0.375
  win_rate_n:               8
  win_rate_source:          backtest   # market-wide base rate, not PATH-specific; in-sample
  ```
- **Open questions:** Does the 10-day OI build + recent bullish sweep persistence override a
  37.5% base rate and a counter-trend, beaten-down chart? With IV cheap, is the right
  expression a defined-risk debit call structure rather than naked length — and is the heavy
  short interest (31.78%) the real swing factor (squeeze fuel vs sustained pressure)? Resolve
  in gates 7b/7c and the debate (8b).
