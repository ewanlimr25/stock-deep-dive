# Phase 5 — Historical Context & VRP

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

History is a **caution flag on the bull thesis.** The matching signal-class backtest
(`bullish_flow`) is **edge-negative — win_rate 20.0% (N=5), avg forward move −0.05%** —
below the 0.45 "historically loses" line (tiny N, market-wide base rate). The
**90-day cumulative premium flow is net BEARISH (−$2.01M)** and the 30-day tape is
17 bearish days vs 13 bullish, with price having **peaked ~$7.65 on 05-28 (a −$3.34M
distribution day at the top) and bled to $5.95** — today's bullish sweep is counter to
a multi-week distribution. Price sits **below its 20/50/200-day SMAs, RSI 40, −64% from
the 52-week high** (full downtrend). Dealers have been **long-gamma for 30 straight
sessions, no regime flip** — durably range-suppressing (reinforces phase-4's "$6 pin, not
breakout"). The two redeeming positives: **VRP is negative (−0.17, realized vol 105% >
implied 88%) → PREMIUM-BUYING regime** (options are cheap vs how much ENVX actually moves
— vol pricing *favors* the debit-call structure), and **OI has built for 30 consecutive
days (+193,235)** — sustained structural interest. Net: real flow, poor historical odds,
cheap premium.

## Key signals

- **`bullish_flow` backtest: win_rate 20.0%, N=5, avg_move −0.05%** `[HIST:signal_backtest]`
  — stable across 5/10/20-day horizons; edge-negative, low-N, market-wide base rate.
- **90d cumulative premium flow NET BEARISH −$2,010,725** (bull $25.26M / bear $27.27M),
  trend MIXED `[HIST:cumulative_premium_flow]` — the multi-week backdrop is *not* bullish.
- **VRP −0.1737, PREMIUM_BUYING** (iv30d 87.9% vs realized 105.3%) `[HIST:vrp]` — options
  cheap vs realized; the *one* clean tailwind for buying the $6 calls.
- **GEX long-gamma 30/30 days, no regime flip** `[HIST:gex_time_series]` — stable
  range-suppression; **OI BUILDING 30 consecutive days, +193,235** `[HIST:oi_trend]`.
- **Full downtrend** `[HIST:trend; rsi fz; 52w_proximity fz]`: price $5.95 < SMA20 (−15.9%)
  < SMA50 (−12.9%) < SMA200 (−23.0%), RSI 40.2, −63.9% from 52W high $16.49, +28.9% above
  52W low $4.61. Counter-trend bull bet.

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore, vrp]`

`current_iv30d 87.9%`, `iv_percentile 45.28`, `iv_zscore −0.454`, regime **NORMAL**
(`dates_used 53` — the "252-day" lookback has only 53 sessions locally; gap-aware). IV is
*mid-range* for the name, not rich. **VRP −0.1737** (`realised_vol 105.3%` > `iv30d 87.9%`),
regime **PREMIUM_BUYING** — "vol cheap vs realised — favour premium buying." Favors **debit**
structures (long the $6 calls) over credit.

### Cumulative premium flow (90d / 54 sessions, spans the gap) — `[HIST:cumulative_premium_flow]`

`cumulative_bullish $25,256,246`, `cumulative_bearish $27,266,971`, **`net_flow −$2,010,725`**,
`trend_direction MIXED`. `dates_covered` = **54 sessions** (includes the 2026-03-13…03-27
cluster across the 03-28→04-24 hole — not a contiguous 90-calendar-day window). The
aggressor-weighted multi-week flow leans **net bearish**, so today's +$442K bullish print is
the exception, not the trend.

### P/C ratio z-score (20d) — `[HIST:pc_ratio_zscore]`

`current_pc_ratio 0.1977` vs `mean 0.3492` (`std 0.2317`), **`zscore −0.654`, extreme NORMAL.**
Today is more call-heavy than the name's 20-day norm but **not a 2-sigma sentiment extreme** —
no contrarian-fade trigger.

### GEX time series (30d) — `[HIST:gex_time_series]`

`days_analyzed 30`, **`regime_flip_dates null`** — **POSITIVE/long-gamma every session**,
ZGL oscillating $2.5–$4.5 (06-26 = $3.5). The dealer regime is **stable and range-suppressing**;
no recent flip means no vol-expansion trigger has fired. Directly reinforces phase-4.

### OI trend (30d) — `[HIST:oi_trend]`

`overall_trend BUILDING`, **`consecutive_build_days 30`**, `total_net_oi_change +193,235`.
Persistent month-long OI accumulation. Caveat: phase-3 shows the chain is chronically
call-heavy *and* the 90d premium flow is net bearish — so part of this build may be
covered-call / short-hedge OI rather than pure directional accumulation (phase-7c/8b to weigh).

### Multi-day trend (30d) — `[HIST:trend]`

`date_range 2026-05-14 → 2026-06-26`, `days_analyzed 30`, **bullish_days 13 / bearish_days 17**,
`price_change 6.3 → 5.95`, `iv_rank_change 21.8 → 42.5`, `flow_direction_latest bullish`.
Path: ran to **$7.65 on 05-28** then sold off (note the **−$3.34M net-flow day at the 05-28
top** = distribution into strength) down to $5.95. IV rank roughly doubled as price fell.

### Price context (`fz`, advisory cross-check) — `[HIST:rsi fz, 52w_proximity fz]`

RSI(14) **40.2** (weak, *not* oversold), price **below all SMAs** (20: −15.9%, 50: −12.9%,
200: −23.0%), Perf Month −20.67% / YTD −18.60%, **−63.9% from 52W high $16.49**, +28.9% above
52W low $4.61. An independent EOD confirm that the bull flow is **counter-trend**, with room
to fall to the $4.61 low before "cheap" on a 52-week basis. Advisory — not in the Kelly `p`.

### Signal backtest (current signal's edge) — `[HIST:signal_backtest]`

`signal_type bullish_flow`, **`win_rate 20.0%`**, **`total_signals 5`**, `avg_move_pct −0.05`,
stable across lookback 5/10/20. Methodology: forward-move-agreement, in-sample, positional,
**market-wide (not ENVX-specific), N=5 → low confidence.** Below 0.45 → historically loses.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | N |
|------------------|--------------------------|---|
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20` | win_rate 20.0%, N=5 ← `.win_rate,.total_signals` (re-run ×2 stable) | 5 |
| `uw historical vrp --symbol ENVX --realised-window-days 30` | VRP −0.1737, PREMIUM_BUYING ← `.vrp,.regime` | obj |
| `uw historical iv-percentile-zscore --symbol ENVX --lookback-days 252` | %ile 45.28, z −0.454, NORMAL ← `.iv_percentile,.iv_zscore` (dates_used 53) | 53 |
| `uw historical cumulative-premium-flow --symbol ENVX --days 90` | net −$2,010,725 ← `.net_flow` (54 sessions, spans gap) | 54 |
| `uw historical pc-ratio-zscore --symbol ENVX --lookback-days 20` | z −0.654, NORMAL ← `.zscore,.extreme` | obj |
| `uw historical gex-time-series --symbol ENVX --days 30 --dte-max 45` | 30/30 POSITIVE, flips null ← `.regime_flip_dates` | 30 |
| `uw historical oi-trend --symbol ENVX --days 30 --top-n 10` | BUILDING, 30 build days ← `.consecutive_build_days` | 30 |
| `uw historical trend --symbol ENVX --days 30` | 13 bull / 17 bear; peak $7.65 05-28 ← `.daily_data` | 30 |
| `fz quote ENVX --agent` | RSI 40.2, <all SMAs ← `.fundamentals` | obj |

## Tool errors

<none — all reads round-tripped through jq>

## DATA NOTE / CORRECTION

- Gap-awareness: `iv_percentile_zscore.dates_used` = 53 and `cumulative_premium_flow`
  covers 54 sessions **including the 2026-03 cluster across the 03-28→04-24 hole** — these
  are *available-session* counts, not contiguous calendar windows. The 30-day `trend`,
  `gex-time-series`, and `oi-trend` windows (start 05-14/05-…) sit **after** the hole and are
  contiguous. No silent interpolation detected (date arrays explicit).

## Verdict for downstream phases

- **Volatility regime:** options **CHEAP vs realized (VRP −0.17, PREMIUM_BUYING)** despite
  87.9% absolute IV; IV %ile mid (45). Favor **debit/long-premium** structures.
- **Premium environment:** **premium-BUYING**, but the **multi-week flow direction is net
  bearish** (−$2.0M/90d) — buy premium, but don't assume the tape is on your side.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: LOW (2/5).** Backtest 20%
  (N=5), 90d net-bearish, full downtrend, durable long-gamma cap. Offsets: cheap VRP +
  30-day OI build. The flow is real; the historical odds are not.
- **Three datapoints:** IV %ile **45.28**; VRP **−0.1737 (PREMIUM_BUYING)**; bullish_flow
  win_rate **0.20 (N=5)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bullish_flow
  signal_backtest_win_rate:   0.20
  win_rate_n:                 5
  win_rate_source:            backtest
  ```
  Market-wide base rate, N=5 → **very low confidence**; phase-9 applies the N-conditional
  cap (`sizing-rubric.md`). Either way 0.20 is a red flag — size small.
- **Open questions:** Is the 30-day OI build directional or covered/short-hedge (90d bearish
  flow argues partly the latter)? Does the cheap VRP justify the long-call despite the
  downtrend, or is "catching the knife" at $5.95 (still +29% above the 52W low) premature?
