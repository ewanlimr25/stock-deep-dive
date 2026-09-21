# Phase 5 — Historical Context & VRP

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

**The defining fact: today (6-25) is MU's post-earnings reaction day.** Earnings
printed **after close 2026-06-24** (`next_earnings_date` rolled 06-24 → 09-22 on
the 6-25 snapshot), and MU **gapped +15.8% (1048.51 → 1213.56) to a marginal new
all-time high** on ~75M shares (vs ~48M prior) with IV crushing 93 → 77. The price
path is a violent round-trip: 1211 (6-22) → **−13.2% crash to 1052 (6-23)** →
flat into the print (6-24) → **+15.8% earnings pop to 1213.56 (6-25)**, leaving
today's close **right at the 6-22 high (1211.38)** — a clean ~1211-1213 supply
ceiling / potential double-top. The realized whiplash is why **realized vol is
122.5% vs implied 91.5% → VRP −0.31 = PREMIUM_BUYING** (options are cheap relative
to how much MU actually moves — favor debit/long-premium structures). IV percentile
is NORMAL (52nd of 1y, N=52); P/C z-score NORMAL (0.74). The trend is powerful but
**parabolic and extended: +325% YTD, at the 52-week high, +188% above the 200-day
MA**. The 90-day cumulative flow is **MIXED** (+$687M net on $72.7B gross over 53
sessions) — today's +$279M is a one-day reaction spike, **not** a persistent
stealth build. Bullish-flow signal backtest: **60% win, but N=5 (weak)**.

## Key signals

- **Today = post-earnings (6-24 AC) reaction: +15.8% gap to ATH 1213.56**, IV 93→77 `[HIST:trend]`
- **VRP −0.31 → PREMIUM_BUYING** (RV 122.5% ≫ IV 91.5%): options cheap, favor debit structures `[HIST:vrp]`
- **Parabolic extension: +325% YTD, 52wk high, +188% over SMA200, RSI 64.5** `[HIST:rsi fz / 52w_proximity fz]`
- **90d cumulative flow MIXED (+$687M / $72.7B, 53 sess)** — today is a spike, not a 60d build `[HIST:cumulative_premium_flow]`
- **Bullish_flow backtest 60% win, N=5** (small, market-wide base rate) `[HIST:signal_backtest]`

## Detailed findings

### IV regime (percentile + z-score + VRP) `[HIST:iv_percentile_zscore / vrp]`

- `current_iv30d` 0.9151 (91.5%); `iv_percentile` **51.92 (NORMAL)**; `iv_zscore`
  0.207; `dates_used` 52 (gap-affected — 252-cal-day lookback has 52 real sessions).
- VRP: iv30d 0.9151 vs **realised_vol 1.2252**; **vrp −0.3102**; regime
  **PREMIUM_BUYING** — *"Vol cheap vs realised — favour premium buying."*
- Read: IV is *high absolute* (91%) but *normal for MU's own year*, and **realized
  exceeds implied by 31 vol points** — the post-earnings whiplash means MU moves
  more than options price in. **Structure implication for phase-9: prefer DEBIT /
  long-premium (call spreads, long calls) over credit/premium-selling.** Note this
  partly offsets phase-4's vanna-crush headwind: yes IV is falling, but RV is so
  high that owning gamma still pays if the move continues.

### Cumulative premium flow (90d → 53 sessions) `[HIST:cumulative_premium_flow]`

- `net_flow` **+$687.5M**; cum_bullish $72.77B vs cum_bearish $72.08B;
  `trend_direction` **MIXED**; window 2026-03-13 → 06-25 (**53 sessions, spans the
  21-session gap**).
- Net +$687M on $72.7B gross = **+0.95% net tilt** — essentially **balanced over 3
  months**. Today's +$279M bullish spike is **~41% of the entire 53-session net** in
  one day — confirming this is a reaction-day event, NOT a stealth institutional
  accumulation campaign (undercuts any "60-day persistent build" read).

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

- current_pc 1.0258, mean 0.9248, std 0.1364, **zscore 0.74, extreme NORMAL**. No
  sentiment extreme — today's slightly-elevated P/C is within range; no contrarian
  trigger from this lens.

### GEX time series (regime stability) `[HIST:gex_time_series]`

- 30 sessions; regime **stably POSITIVE** except a **1-day flip to NEGATIVE on
  2026-06-23** (spot 1053, the −13% crash day) → back to **POSITIVE on 6-24**. The
  flip is the earnings-week vol spike; the regime has **re-normalized to long-gamma**
  (consistent with phase-4's POSITIVE read). No persistent short-gamma regime — so
  no structural trend-amplification tailwind; dealers damp moves now.

### OI trend `[HIST:oi_trend]`

- `overall_trend` **BUILDING**; **consecutive_build_days 30**; total_net_oi_change
  **+4,742,095** contracts over 30 sessions. Sustained OI accumulation across the
  entire run — positions building (both calls and puts, per phase-3) as MU trended
  up. A real engagement signal, but not directionally clean on its own.

### Multi-day trend table `[HIST:trend]` (price_change 803.63 → 1213.56; bullish 20 / bearish 10 days)

| date | close | net_flow | P/C | iv_rank | flow_dir |
|------|-------|----------|-----|---------|----------|
| 2026-06-25 | **1213.56** | +$279M | 1.025 | 77.1 | bullish (earnings pop) |
| 2026-06-24 | 1048.51 | +$26M | 1.04 | 92.9 | bullish (earnings AC) |
| 2026-06-23 | 1051.77 | −$146M | 1.012 | 100 | **bearish (−13.2%)** |
| 2026-06-22 | 1211.38 | +$214M | 0.929 | 100 | bullish |
| 2026-06-18 | 1133.99 | +$522M | 1.123 | 94.1 | bullish |
| 2026-06-17 | 1043.19 | +$48M | 0.92 | 95.9 | bullish |
| 2026-06-16 | 1020.76 | −$193M | 0.944 | 96.9 | bearish |
| 2026-06-15 | 1087.99 | +$78M | 0.92 | 100 | bullish |

**Key levels fall out of the path:** resistance/supply **~1211-1213** (6-22 high =
6-25 close, a double-top zone & the phase-2 DP shelf); support **~1134** (6-18
close, heavy DP shelf); recent pivot low **~1048-1052** (6-23/6-24). Month is +51%,
20:10 bullish days — uptrend intact but realized-vol-violent.

### Price context (`fz`, independent EOD) `[HIST:rsi fz / 52w_proximity fz]`

| Metric | Value | Read |
|--------|-------|------|
| RSI(14) | **64.54** | elevated, NOT >70 (the 6-23 −13% crash reset it) |
| vs SMA20 | +18.40% | extended |
| vs SMA50 | +53.88% | very extended |
| vs SMA200 | **+188.36%** | parabolic |
| Perf YTD | **+325.20%** | parabolic |
| 52W High | 1213.56 (**0.00%**) | **AT the high** |
| 52W Low | 103.38 (+1073.9%) | 10.7× off the low in 1y |

This independent read **confirms extreme extension**: MU sits at its 52-week high,
+325% YTD, nearly 3× its 200-day average. RSI 64.5 (not yet overbought) is the one
non-extreme reading — courtesy of the 6-23 shakeout. **Major mean-reversion risk**
hand-off to phase-7c (positioning gate) and phase-8b (debate).

### Signal backtest `[HIST:signal_backtest]`

- `signal_type` bullish_flow; **win_rate 60.0%**; **total_signals 5**; (market-wide,
  not MU-specific; 5-day lookback). 60% > the 0.45 "historically loses" line — edge
  is *mildly* positive, but **N=5 is below the 10-firing confidence floor** → treat
  as weak; phase-9 must shrink it heavily toward base rate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows / N |
|------------------|--------------------------|----------|
| `historical iv-percentile-zscore --lookback-days 252` | iv_pctile 51.92 NORMAL ← `.iv_percentile,.regime` | 52 sess |
| `historical vrp --realised-window-days 30` | vrp −0.3102 PREMIUM_BUYING ← `.vrp,.regime` | 30d |
| `historical cumulative-premium-flow --days 90` | net +$687.5M MIXED ← `.net_flow,.trend_direction` | 53 sess |
| `historical pc-ratio-zscore --lookback-days 20` | z 0.74 NORMAL ← `.zscore,.extreme` | 20d |
| `historical gex-time-series --days 30 --dte-max 45` | flip 6-23 POS→NEG→POS 6-24 ← `.regime_flip_dates` | 30 sess |
| `historical oi-trend --days 30` | BUILDING, 30 consec days, +4.74M ← `.overall_trend,.consecutive_build_days` | 30 sess |
| `historical trend --days 30` | 803.63→1213.56, bull 20/bear 10 ← `.price_change,.bullish_days` | 30 sess |
| `historical signal-backtest --signal-type bullish_flow --lookback-days 5` | 60.0%, N=5 ← `.win_rate,.total_signals` | mkt-wide |
| `fz quote MU` | RSI 64.5, +325% YTD, 52wk high ← `.fundamentals.*` | EOD |

## Tool errors

None. (Gap-aware: `iv-percentile-zscore.dates_used`=52, `cumulative-premium-flow`
N=53 across the 03-28→04-24 hole — quoted as actual session counts, not calendar
spans. `trend.daily_data` carries no `total_premium` field — premium read from the
screener self-history in phase-0.5 instead; no number transcribed from a null.)

## DATA NOTE / CORRECTION

**Corrects phase-0.5.** Phase-0.5 inferred earnings "≈June 23 (continuation)." The
screener `next_earnings_date` series (06-24 on every snapshot through 6-24, →
09-22 on 6-25) plus the GEX regime flip (6-23) and the +15.8% gap (6-24→6-25 close)
**pin earnings to after-close 2026-06-24**, making **6-25 the reaction day**, not a
continuation day. All downstream phases should treat today as **post-earnings
reaction at a marginal new ATH**, with the next earnings binary far off (9-22).

## Verdict for downstream phases

- **Volatility regime:** **CHEAP vs realized → PREMIUM-BUYING** (VRP −0.31; RV 122.5%
  ≫ IV 91.5%). Favor **debit / long-premium** structures; avoid naked premium
  selling. IV percentile NORMAL (52nd) — not a vol-rank extreme either way.
- **Premium-buying vs selling environment:** **BUYING** — confirmed.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3 / 5.** The
  premium-buying regime is a genuine structural edge for owning gamma, and the
  uptrend is intact (20/10 bullish days, 30d OI build). But it's offset by (a) the
  **parabolic extension** (+325% YTD, 52wk high) = high reversion risk, (b) the
  **marginal-new-high-at-resistance** (1213 = 6-22 double-top), (c) **90d flow MIXED**
  (today is a spike), and (d) the **weak N=5 backtest**.
- **Three specific datapoints:** IV percentile **51.92 (NORMAL)**; **VRP −0.31
  (PREMIUM_BUYING)**; signal **win-rate 0.60 / N=5**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.60
  win_rate_n:                5
  win_rate_source:           backtest
  ```
  (Market-wide base rate, not MU-specific; N=5 is below the 10-firing floor — apply
  the N-conditional shrink in `rubrics/sizing-rubric.md`.)
- **Open questions:** Does the +15.8% earnings pop hold above the 1211-1213
  double-top (continuation) or fade back to 1134 (round-trip)? Is the premium-buying
  edge enough to justify owning gamma into a positive-gamma, IV-deflating tape
  (phase-4 vanna headwind)? Phase-7b (is the earnings beat fundamentally justified
  at +325% YTD?) and phase-7c (is positioning euphoric/crowded?) are now pivotal.
