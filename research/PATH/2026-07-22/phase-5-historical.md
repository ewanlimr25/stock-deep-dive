# Phase 5 — Historical Context & VRP

**Ticker:** PATH · **As-of:** 2026-07-22 · **Spot:** $10.57 · **Generated:** 2026-07-22
**Latest available date (trailing-anchor):** 2026-07-22
**Upstream:** phase-1-flow.md (mixed: bearish today / 5-day bullish campaign), phase-2 ($12 overhead), phase-4 (long-gamma, premium context)

## Summary

Today is a **violent ~11.5% down day off a rally high**: the GEX trajectory shows PATH
ran from ~$10 (late June) to a **$12.28 peak on 2026-07-20**, held $11.95 on 7/21, then
**crashed to $10.57 today** — a full **round-trip** (30-day price change 10.75 → 10.70,
flat, but via a +17% run and a −11.5% one-day break). Volatility is **NORMAL** (IV
57th 1-yr percentile, IV30d 67.5%, z −0.37), and VRP is **+0.18 → premium-selling**
regime (IV richer than 49.6% realized) — *though today's crash will lift forward
realized and compress that edge.* OI has been **BUILDING for 14 consecutive sessions**
(+349k net) — the LEAP bullish accumulation is genuine and sustained, now caught
underwater by the crash. The signal base rates cut against a fresh short: market-wide
**bearish_flow has won only 10% (n=10)** over the recent window while **bullish_flow
won 100% (n=5)** — a mean-reverting-up tape where bearish setups have failed. Dealer
regime has been **POSITIVE (long-gamma) every one of the last 30 sessions, no flips.**

## Key signals

- **~11.5% crash today off a $12.28 (7/20) high** — GEX trajectory spot path: $12.28 (7/20) → $11.95 (7/21) → **$10.57 (7/22)** `[HIST:gex_time_series]`.
- **OI BUILDING 14 consecutive days, +349k net** — sustained (bullish LEAP) accumulation, `overall_trend=BUILDING` `[HIST:oi_trend]`.
- **bearish_flow base rate 10% (n=10) vs bullish_flow 100% (n=5)** — market-wide; recent tape punishes shorts, rewards dips `[HIST:signal_backtest]`.
- **VRP +0.18, PREMIUM_SELLING** (IV 67.5% > RV 49.6%) — favors credit structures, *pre-crash caveat* `[HIST:vrp]`.
- **IV NORMAL** — 57th 1-yr percentile, z −0.37; no vol extreme `[HIST:iv_percentile_zscore]`.
- **90-day cumulative flow balanced** — bull $123.98M vs bear $121.81M, net +$2.17M, MIXED `[HIST:cumulative_premium_flow]`.
- **P/C ratio NOT extreme** — 0.419 vs 20d mean 0.459, z −0.10 `[HIST:pc_ratio_zscore]`.

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- IV percentile **57.14** (1-yr, dates_used 70), iv_zscore **−0.365**, IV30d **67.5%**, regime **NORMAL**.
- VRP **+0.1794**, realized-vol30 **49.6%**, regime **PREMIUM_SELLING** ("Options pricing more vol than realised — favour premium selling").
- **Caveat:** RV30 is trailing and does **not** yet reflect today's −11.5% move; forward realized will jump, so the premium-selling edge is softer than the static +0.18 suggests. Treat as "IV fair-to-slightly-rich, not a clean vol sale into the 7/24 event."

### Cumulative premium flow (90d / 71 sessions) `[HIST:cumulative_premium_flow]`

Cumulative bullish **$123.98M** vs bearish **$121.81M** → net **+$2.17M** (+0.9% tilt),
`trend_direction=MIXED`. **Gap-aware:** `dates_covered` spans 2026-03-13…03-27 then
jumps to 2026-04-27→07-22 — the 21-session hole is excluded; this is **71 sessions**,
not a contiguous 90 calendar days. Read: over the quarter PATH flow is genuinely
**two-sided with a whisker-bullish net** — no dominant stealth directional build in
*premium* terms (the build is in *OI/structure*, below).

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

Current 0.419 vs 20-day mean 0.459 (std 0.40), z **−0.101**, extreme **NORMAL**. No
sentiment extreme → no contrarian trigger from positioning ratios.

### GEX time series (30d) `[HIST:gex_time_series]`

**Regime POSITIVE on all 30 sessions; `regime_flip_dates=null`** (spot never crossed
the ~$7 ZGL). The instructive series is the **price path**:

| date | spot | total_gex | ZGL |
|---|---|---|---|
| 2026-06-22 | 10.13 | +0.23M | 7.73 |
| 2026-07-01 | 11.60 | +37.0M | 6.75 |
| 2026-07-06 | 12.00 | +12.1M | 7.51 |
| 2026-07-16 | 12.04 | +22.0M | 6.67 |
| **2026-07-20** | **12.28** | +11.5M | 6.72 |
| 2026-07-21 | 11.95 | +12.4M | 7.60 |
| **2026-07-22** | **10.57** | **+3.8M** | 6.92 |

Total_gex **collapsed from ~$12–23M to $3.8M today** as spot fell away from the
call-heavy $12–15 strikes — long-gamma is thinning but still positive. No short-gamma
flip, so the −11.5% was **not** a dealer-amplified gamma unwind; it reads as a
fundamental/news-driven repricing (→ phase-6/7b must find the cause).

### OI trend (30d) `[HIST:oi_trend]`

`overall_trend=BUILDING`, **consecutive_build_days=14**, total_net_oi_change **+349,167**.
A sustained 14-session OI build — the LEAP call accumulation (phase-3's Jan-2027 41%
cliff) grew steadily through the rally. This is the strongest *structural* bull tell,
now stress-tested by today's crash: the campaign is offside intraday.

### Multi-day trend `[HIST:trend]`

30d (2026-06-09→07-22): **14 bullish / 16 bearish days**, price 10.75 → 10.70 (net
flat via round-trip), IV rank 46.2 → 45.6, **flow_direction_latest = bearish**.
Balanced-to-slightly-heavy-bearish day count; the net-flat price masks the +17%/−11.5%
whipsaw.

### Price context (`fz`)

**Omitted** — `fz quote PATH --agent` returned a reduced payload again (RSI/SMA/52W
all null, consistent with phase-0). No independent EOD momentum cross-check available;
UW GEX-trajectory price path used instead. (Advisory-only lane; absence never affects
sizing.)

### Signal backtest `[HIST:signal_backtest]` (market-wide base rates)

| signal_class | win_rate | n (total_signals) | note |
|---|---|---|---|
| bullish_flow | **100.0%** | 5 | tiny N — low confidence |
| bearish_flow | **10.0%** | 10 | marginal N |

**Market-wide, not PATH-specific** (the tool takes no `--symbol`). The recent regime
rewards dip-buying and punishes fresh shorts. Both N are small (<10 / =10) → phase-9
must shrink heavily toward the conviction bin. The 10% bearish base rate is a real
**headwind to a continuation-short thesis** in this tape.

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| IV %ile/z | `uw historical iv-percentile-zscore --symbol PATH --lookback-days 252 --json` | `.{iv_percentile,iv_zscore,current_iv30d,regime,dates_used}` |
| VRP | `uw historical vrp --symbol PATH --realised-window-days 30 --json` | `.{vrp,realised_vol,regime,interpretation}` |
| cum flow | `uw historical cumulative-premium-flow --symbol PATH --days 90 --json` | `.{cumulative_bullish,cumulative_bearish,net_flow,trend_direction,dates_covered}` |
| P/C z | `uw historical pc-ratio-zscore --symbol PATH --lookback-days 20 --json` | `.{current_pc_ratio,mean_pc_ratio,zscore,extreme}` |
| GEX TS | `uw historical gex-time-series --symbol PATH --days 30 --dte-max 45 --json` | `.trajectory[].{date,spot,total_gex,zero_gamma_level,regime}` `.regime_flip_dates` |
| OI trend | `uw historical oi-trend --symbol PATH --days 30 --top-n 10 --json` | `.{overall_trend,consecutive_build_days,total_net_oi_change}` |
| trend | `uw historical trend --symbol PATH --days 30 --json` | `.{bullish_days,bearish_days,price_change,iv_rank_change,flow_direction_latest,date_range}` |
| backtest | `uw historical signal-backtest --signal-type bullish_flow\|bearish_flow --lookback-days 5 --top-n 20 --json` | `.{win_rate,total_signals}` |

## Tool errors

<none> (fz price-context lane returned null fields — recorded as advisory-absent, not an error).

## Verdict for downstream

- **Volatility regime: IV FAIR (57th %ile, NORMAL), VRP +0.18 premium-selling — but softening as today's crash lifts forward realized.** Not a clean short-vol setup into 7/24.
- **Premium environment: mildly premium-SELLING** (credit-favoring) — but the 7/24 backwardation (phase-4) means front-vol is bid for a reason; don't sell naked front premium into the event.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2/5 for a continuation short** (bearish base rate 10%, n=10, in a dip-buying tape) — the base rates actively favor a **mean-reversion bounce** off the crash toward the $11 long-gamma pin, *conditional on the 7/24 catalyst not confirming genuinely bad news.*
- **Three specific data points:** IV percentile **57.1**; VRP **+0.18** (PREMIUM_SELLING); bearish_flow signal win-rate **10% (n=10)** / bullish_flow **100% (n=5)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow (today's dominant flow) — BUT see note
  signal_backtest_win_rate:  0.10
  win_rate_n:                10
  win_rate_source:           backtest
  # ALTERNATE (if phase-8/9 concludes a mean-reversion LONG):
  #   signal_class: bullish_flow · win_rate 1.00 · n 5 · source backtest
  # BOTH are market-wide base rates, tiny N → apply heavy N-conditional shrink
  # toward the conviction bin (sizing-rubric §Choosing p). Neither is PATH-specific.
  ```
- **Open questions:**
  - **WHY did PATH crash 11.5% today?** GEX shows no dealer-amplified unwind → fundamental/news driven. Earnings, guidance pre-announcement, downgrade, or software-sector rotation? → phase-6, phase-7b MUST resolve before any directional sizing.
  - Is the 14-day OI build (bullish campaign) about to capitulate (offside longs) or defend the $10 put wall? → phase-6 catalyst + phase-8 desk views.
  - Does the poor bearish base rate + long-gamma pin + DEX bid outweigh today's momentum, i.e. is this a mean-reversion long or a broken-uptrend short? → phase-8/8b to adjudicate.
