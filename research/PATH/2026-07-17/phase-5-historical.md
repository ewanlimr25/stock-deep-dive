# Phase 5 — Historical Context & VRP

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Cites: phase-1-flow.md (5-day bullish sweep persistence — is it edge-positive?);
phase-3-positioning.md (structural call build — sustained?); phase-4-structure.md
(POSITIVE gamma — stable regime?); phase-2-dark-pool.md (buy-into-fade — persistent?).
**Gap-aware:** the local window has a 21-session hole 2026-03-28→2026-04-24; the
90d cumulative-flow `dates_covered` confirms it (jumps 2026-03-27→2026-04-27).
Trailing tools anchor to latest = as-of 2026-07-17 (reproducible today).

## Summary

The name is in a **durable long-gamma range with genuine but slow bullish
accumulation, on RICH implied vol** — a mixed-edge backdrop. IV30 is 0.675 at the
**59.7th percentile** (z −0.37, regime NORMAL over the 67 sessions actually
present), and **VRP is +0.289 → PREMIUM_SELLING**: IV (0.675) exceeds realized
(0.386) by ~29 vol points, so options are rich and this is a premium-*selling*
environment (favor credit / don't overpay for debit). Positioning is genuinely
building — **OI has risen 11 consecutive days (+337k net contracts, overall_trend
BUILDING)** and price has ground **+4.1% over 30d ($11.67→$12.15)** — but the
90-day cumulative premium flow is **MIXED** (bull $120.7M vs bear $116.6M, net only
+$4.0M), so this is a recent lean on a quarter-long near-balance, not a
stealth-accumulation stampede. The **GEX regime has been stably POSITIVE every
session for 30 days** (no flips; ZGL 7.5–8.5, spot rising 10.7→12.13) — the
mean-reversion cage is durable. The sobering datapoint: the **bullish_flow signal
backtest is 14.3% (n=7)** — historically weak, small sample, market-wide. Net:
the accumulation is real and slow, but the historical edge on *acting bullishly
via flow* is not established, and rich IV penalizes long premium.

## Key signals

- **VRP +0.289 → PREMIUM_SELLING** — IV30 0.675 vs RV30 0.386; options rich, sell
  premium / avoid naked debit `[HIST:vrp]`.
- **OI BUILDING 11 consecutive days, +337,036 net** over 30d `[HIST:oi_trend]` —
  sustained structural accumulation; corroborates phase-3.
- **bullish_flow backtest 14.3% win (n=7)** — market-wide base rate, weak and
  small-N; a conviction *downgrade* per the <0.45 heuristic `[HIST:signal_backtest]`.
- **GEX POSITIVE all 30d, zero flips** — durable long-gamma / range regime;
  ZGL 7.5–8.5 while spot rose 10.7→12.13 `[HIST:gex_time_series]`.
- **90d cumulative flow MIXED (+$4.0M net on ~$237M)** — not a stealth build; the
  bullish lean is recent, not quarter-deep `[HIST:cumulative_premium_flow]`.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore, vrp]`
IV percentile **59.7** (252-day lookback, **67 sessions actually present** — gap +
short history), iv_zscore **−0.37** (slightly below own recent mean), current IV30d
**0.675**, regime **NORMAL**. VRP **+0.289**, RV30 **0.386**, regime
**PREMIUM_SELLING**. Read together: IV is mid-high by percentile but rich versus
what the stock actually realizes — long options carry a vol headwind; the edge is
in *selling* vol (put-writes, spreads, call-writes vs stock) not buying it.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`
`net_flow +$4,048,962`; cumulative_bullish **$120.67M** vs cumulative_bearish
**$116.62M**; `trend_direction = MIXED`; 90 calendar days but **`dates_covered`
spans the 03-27→04-27 gap** (≈58 sessions). Near-balanced over the quarter — the
phase-1 5-day bullish persistence is a *recent* tilt riding on top of a balanced
base, not a season-long institutional build. Weakens the "stealth accumulation"
read.

### P/C ratio z-score (20d) `[HIST:pc_ratio_zscore]`
Current PCR **0.553**, mean 0.55-ish, **z +0.20** — dead-center, `extreme=null`.
No sentiment extreme in either direction; no contrarian setup. Sentiment is
neutral, consistent with phase-4's COMPLACENT (not fearful, not euphoric).

### GEX time series (30d) `[HIST:gex_time_series]`
Every session 2026-06-04 → 2026-07-17 reads **regime POSITIVE**; **no
regime_flip_dates**. ZGL trajectory 8.47 → ~6.8 while spot climbed 11.77 → 12.13,
i.e. the positive-gamma cushion *deepened* as price rose. The long-gamma /
mean-reversion regime (phase-4) is **stable, not a one-day artifact** — high
confidence the range behavior persists absent a catalyst.

### OI trend (30d) `[HIST:oi_trend]`
`overall_trend = BUILDING`, **consecutive_build_days = 11**, `total_net_oi_change
= +337,036`. A real, sustained OI accumulation — the structural call ownership
(phase-3) has been laddering up for 11 straight sessions. This is the strongest
*bullish* historical tell and the counterweight to the weak backtest.

### Multi-day trend (30d) `[HIST:trend]`
`date_range 2026-06-04 → 2026-07-17`, `days_analyzed 30`: **bullish_days 15 /
bearish_days 15** (evenly split daily flow), `price_change 11.67 → 12.15` (+4.1%),
`flow_direction_latest bullish`, `iv_rank_change 36.47 → 44.46` (IV rank rising).
A slow grind-up with balanced daily flow and modestly firming IV rank — orderly,
low-drama, consistent with the long-gamma range drifting higher.

### Price context (`fz`) `[HIST:rsi fz, 52w_proximity fz]`
**Unavailable** — `fz quote PATH` again returned a truncated fundamentals payload
(Price/RSI/SMA/52W all null; same truncation as phase-0/2). Advisory cross-check
skipped; no independent RSI/moving-average read this run. (Non-blocking.)

### Signal backtest `[HIST:signal_backtest]`
- `bullish_flow`, lookback 5d: **win_rate 14.3%, total_signals 7** (confirmed on a
  second run — not the empty stub). Market-wide base rate, tiny N.
- `dark_pool_accumulation`: `{"note":"no backtest results","total_signals":0}` →
  no edge measurement for the phase-2 signal class.
The 14.3% is historically edge-*negative* for bullish flow, but N=7 is too small
to be decisive; phase-9 must apply the N-conditional Kelly cap (N<10 = fall toward
the conviction bin, do not size on 0.143 literally).

## Tool calls
| Tool | Args | Result |
|---|---|---|
| historical iv-percentile-zscore | --symbol PATH --lookback-days 252 | 59.7 %ile, z −0.37, NORMAL, n=67 |
| historical vrp | --symbol PATH --realised-window-days 30 | +0.289, PREMIUM_SELLING |
| historical cumulative-premium-flow | --symbol PATH --days 90 | MIXED, +$4.0M net |
| historical pc-ratio-zscore | --symbol PATH --lookback-days 20 | z +0.20, no extreme |
| historical oi-trend | --symbol PATH --days 30 | BUILDING, 11 build-days, +337k |
| historical gex-time-series | --symbol PATH --days 30 --dte-max 45 | POSITIVE all 30d, 0 flips |
| historical trend | --symbol PATH --days 30 | +4.1%, flow 15/15, IVR rising |
| historical signal-backtest | --signal-type bullish_flow --lookback-days 5 (×2) | 14.3%, n=7 |
| historical signal-backtest | --signal-type dark_pool_accumulation --lookback-days 5 | n=0, no results |
| fz quote | PATH --agent | truncated (price context null) |

## Tool errors
- None. `fz quote` truncation handled as advisory-skip (not a tool error). All
  90d/252d windows cross the 03-28→04-24 gap — session counts quoted from each
  tool's own `dates_used`/`dates_covered`/series length, never the calendar span.

## Verdict for downstream

- **Volatility regime: RICH** — VRP +0.289, IV 59.7th %ile but ~29 vol points over
  realized. **Premium-SELLING environment** → phase-9 should favor credit/defined
  structures (put-writes to get long, call spreads, or stock) over naked long calls;
  a debit-call thesis pays a rich-IV tax.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2 / 5.** The
  accumulation is genuine (11-day OI build, +4% grind, 5-day sweep persistence) but
  the *measured* edge is weak/unproven: bullish_flow backtest 14.3% (n=7), 90d flow
  MIXED, and the long-gamma regime caps upside. Slow-bullish-but-caged, not a
  high-conviction directional edge.
- **Three specific datapoints:** IV %ile **59.7** · VRP **+0.289 (premium-selling)**
  · bullish_flow win-rate **14.3% (n=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.143
  win_rate_n:                7
  win_rate_source:           backtest
  ```
  N=7 < 10 → LOW confidence; market-wide base rate, not PATH-specific. Per
  `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`", apply the N-conditional cap
  (blend toward the conviction bin; do not Kelly-size on 0.143 literally). The
  RICH-IV / premium-selling regime is an independent size-down input.
- **Open questions:** Does the 11-day OI build reflect *directional* call buying or
  premium-*selling* structures (covered calls / put-writes) that the rich VRP would
  reward — i.e. is "smart money" here the buyer or the seller of these calls? Can
  the +4% grind clear the $13 gamma cap (phase-4) without the Sep-3 earnings
  catalyst? Fundamentals (phase-7b) and sentiment/SI (phase-7c) must weigh in
  before conviction is set.
