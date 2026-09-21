# Phase 5 — Historical Context & VRP

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:09:11-0400
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bearish tilt lands on a name that has **parabolically re-rated** — INTC is up
**+247.75% YTD**, **6.8× off its 52-week low ($18.97)**, and now sits **9.3% below its
52-week high ($141.45)** after a **+10.7% 30-session rally ($115.93 → $128.32)** that
stalled this week (−4.23%). So the bearish flow/OI is a **distribution / fade-the-extended-
rally** setup, not a breakdown from weakness. The vol regime is **HIGH** (iv30d 92.3%,
88.7th percentile, z +1.31) and **premium-selling** (VRP **+5.95**, IV 92% > realized
86%) — meaning outright long puts are **expensive**; defined-risk/credit structures are
favored. The signal has a **positive but thin historical edge**: `bearish_flow` backtest
**win_rate 66.7%, n=9, avg forward move −10.55%**. Tempering factors: the **90-day
cumulative premium is essentially balanced** (+$57.5M, MIXED) — today's bearishness is
*recent*, not a 90-day campaign; the **P/C z-score is NORMAL** (no sentiment extreme);
the **GEX regime has been stably long-gamma for 30 days** (0 flips); and fading a +248%
momentum name carries real squeeze risk. **Gap caveat:** the "252-day" IV lookback used
only **53 sessions present** (21-session hole 03-28→04-24) — treat the percentile as a
~2.5-month read, not a true year.

## Key signals

- **Price extension**: +247.75% YTD, 9.28% below 52W high $141.45, +120% above SMA200
  [HIST:perf_ytd fz][HIST:52w_proximity fz].
- **HIGH_IV regime**: iv30d 92.3%, iv_percentile 88.68 (over 53 sessions), z +1.31
  [HIST:iv_percentile_zscore].
- **VRP +5.95 → PREMIUM_SELLING** (IV 92.3% vs realized 86.4%) — favor credit/spreads
  [HIST:vrp].
- **bearish_flow backtest: win_rate 66.7%, n=9, avg move −10.55%** — positive edge, small
  N [HIST:signal_backtest].
- **90d premium BALANCED** (bull $10.06B vs bear $10.00B, net +$57.5M, MIXED) — bearishness
  is recent, not entrenched [HIST:cumulative_premium_flow].

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value | Read |
|---|---|---|
| `current_iv30d` | 0.9232 | Very high absolute IV |
| `iv_percentile` | 88.68 | High — but over **`dates_used=53`** (thin, gap-reduced) |
| `iv_zscore` | +1.31 | ~1.3σ rich |
| `regime` | HIGH_IV | — |
| `vrp` | **+0.0595** | IV 92.3% − realized 86.4% → modestly rich |
| VRP regime | **PREMIUM_SELLING** | "Options pricing more vol than realised — favour premium selling" |

Both IV and realized vol are extreme (~86–92%); INTC is moving violently. The +6-point
VRP says options are *modestly* rich — enough to favor **credit/defined-risk** over naked
long premium, but not a screaming vol sale.

### Cumulative premium flow (90d)

`cumulative_bullish $10,059.5M` vs `cumulative_bearish $10,002.1M` → `net_flow +$57.5M`,
`trend_direction = MIXED`. Over the trailing window the directional premium is a coin-flip
— **no sustained institutional directional campaign.** Today's bearish tilt is a *fresh*
development, which both (a) makes it a genuine change worth noting and (b) means it lacks
the multi-week confirmation a stealth-accumulation thesis would have. (Gap/latest-anchor
caveats apply; ~53 sessions actually present.)

### P/C ratio z-score (sentiment extreme?)

`current_pc_ratio 0.5819`, `mean 0.5773`, `std 0.1706`, **`zscore 0.027`, `extreme =
NORMAL`.** No sentiment extreme — the bearish positioning is **measured, not crowded**
(coheres with phase-4's COMPLACENT skew). No contrarian/fade-the-crowd signal in either
direction.

### GEX time series (regime stability)

`days_analyzed 30`, **`regime_flip_dates = null`** — no zero-gamma crossings in 30
sessions. The **long-gamma regime is entrenched** (phase-4 confirmed for today). Dealers
have been dampening vol throughout; a regime flip (toward short-gamma trend amplification)
would require spot to fall ~$100 to the $27 ZGL — not a near-term risk. Implication: the
bearish move, if it comes, is more likely a **controlled grind than a gamma-fueled cascade.**

### OI trend (30d)

`overall_trend = BUILDING`, `consecutive_build_days = 30`, `total_net_oi_change
+3,560,474`. OI has grown every session for 30 days — heavy position accumulation through
the rally. Phase-3 shows the **newest** layer of that build (today) rotating into **puts**
— i.e. the 30-day call-heavy accumulation is now being hedged/faded.

### Multi-day trend table (30d, `trend`)

| Field | Value |
|---|---|
| `date_range` | 2026-05-14 → 2026-06-26 (30 sessions, post-gap — clean) |
| `price_change` | $115.93 → $128.32 (**+10.7%**) |
| `iv_rank_change` | 82.77 → 94.11 (**rising into the rally**) |
| `bearish_days / bullish_days` | **17 / 13** (slight bearish majority) |
| `flow_direction_latest` | **bearish** |

Rising IV *into* a price rally is unusual (vol normally falls on the way up) — it signals
demand for protection/upside-uncertainty even as price rose, and a market bracing for a
big move. Now flow has flipped bearish at the high.

### Price context (`fz`, advisory cross-check)

| Metric | Value | Read |
|---|---|---|
| RSI(14) | **56.78** | Neutral — NOT overbought (−4.2% week cooled it) |
| Price vs SMA20 / 50 / 200 | +7.45% / +18.39% / **+120.36%** | Extended, esp. vs SMA200 |
| Perf Week / Month / YTD | −4.23% / +5.38% / **+247.75%** | Parabolic YTD, stalling near-term |
| 52W High | **141.45 (−9.28%)** | = phase-2 $140.94 supply; topped & pulled back |
| 52W Low | 18.97 (+576.61%) | 6.8× off the low |

This is the single most important framing for the trade: **a +248% YTD parabola that
printed its high at ~$141, pulled back ~9% to $128, and is now seeing bearish institutional
flow/OI.** RSI 56.8 (not extreme) + long-gamma regime argue against an *imminent* crash;
but the extension + fresh bearish positioning argue for a **pullback/mean-reversion** lean.
Counter-trend on a momentum monster — squeeze risk is real. [HIST:rsi fz][HIST:52w_proximity fz]

### Signal backtest (current signal's historical edge)

`signal_type bearish_flow`, **`win_rate 66.7%`**, `total_signals 9`, `avg_move_pct −10.55%`.
Methodology (verbatim): in-sample, market-wide, positional within yfinance bars — "not a
robust live edge." So `p = 0.667` is a **market-wide base rate** of the bearish_flow signal
class (not INTC-specific), on a **small N=9** → moderate confidence; phase-9 applies the
N-conditional Kelly cap.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows/N |
|---|---|---|
| `historical iv-percentile-zscore --lookback-days 252` | iv_pctile 88.68, z +1.31, HIGH_IV ← `.iv_percentile,.dates_used=53` | 53 sess |
| `historical vrp --realised-window-days 30` | VRP +0.0595, PREMIUM_SELLING ← `.vrp,.regime` | 30 |
| `historical cumulative-premium-flow --days 90` | net +$57.5M, MIXED ← `.net_flow,.trend_direction` | ~53 sess |
| `historical pc-ratio-zscore --lookback-days 20` | z 0.027, NORMAL ← `.zscore,.extreme` | 20 |
| `historical gex-time-series --days 30 --dte-max 45` | regime_flip_dates null ← `.regime_flip_dates` | 30 |
| `historical oi-trend --days 30` | BUILDING, 30 consec, +3.56M ← `.overall_trend,.consecutive_build_days` | 30 |
| `historical trend --days 30` | +10.7% price, 17/13 bear/bull, latest bearish ← `.price_change,.bearish_days` | 30 |
| `historical signal-backtest --signal-type bearish_flow --lookback-days 5` | win 66.7%, n=9, −10.55% ← top-level `.win_rate,.total_signals` | n=9 |
| `fz quote INTC --agent` | RSI 56.78, YTD +247.75%, 52WH −9.28% ← `.fundamentals` | EOD |

## Tool errors

None. **Gap/latest-anchor data note (not an error):** trailing tools anchor to the latest
date (= as-of 2026-06-26); the 252-day IV lookback used only `dates_used=53` (21-session
hole 03-28→04-24), and the 90d cumulative spans ~53 present sessions. The 30d `trend`
window (05-14→06-26) is post-gap and clean. Percentiles are ~2.5-month reads, not a full
year — confidence accordingly tempered.

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq` on first read.

## Verdict for downstream phases

- **Volatility regime:** **RICH / HIGH** (iv30d 92.3%, 88.7th pctile, z +1.31) — but only
  *modestly* rich vs realized (VRP +6). **Premium-SELLING** environment.
- **Premium-buying vs -selling:** **premium-SELLING** → for the bearish lean, prefer
  **bear call (credit) spreads or put debit spreads**, NOT naked long puts (expensive at
  92% IV).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3 / 5** — backtest
  is positive (66.7%) but N=9 and market-wide; the setup is **counter-trend on a +248%
  parabola** (squeeze risk), with no 90-day campaign behind it; offset by the clean,
  extended, just-pulled-back price structure.
- **Three specific datapoints:** IV percentile **88.68** (over 53 sess); VRP **+0.0595**
  (premium-selling); signal win-rate **66.7%** (n=9, avg −10.55%).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               bearish_flow
  signal_backtest_win_rate:   0.667
  win_rate_n:                 9
  win_rate_source:            backtest
  ```
  (Market-wide base rate, small N → phase-9 must apply the N-conditional cap;
  `rubrics/sizing-rubric.md` §"Choosing the Kelly `p`".)
- **Open questions:**
  - Can a counter-trend bearish trade work on a name +248% YTD with 86% realized vol, or
    does momentum/squeeze risk dominate? (risk-monitor / contrarian lens in phase-8.)
  - With VRP positive and IV at the 88th pctile, is the right expression a **structure
    short** (credit spread) rather than directional puts? (phase-9 structure choice.)
  - Does fundamentals (phase-7b) justify the 248% re-rate, or is it sentiment-driven and
    thus more vulnerable to the fade? (phase-7b quality veto is pivotal here.)
