# Phase 5 — Historical Context & VRP

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:44:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bullish flow sits inside a **counter-trend bounce in a badly damaged
name.** NOW is **−33% YTD, −51.7% from its 52-week high ($211→$102), and still 28%
below its 200-day SMA** — but it bottomed at $87.05 on 2026-05-13, ripped **+18%
to $103.42 by 5/18**, and has since **consolidated tight ($99.69–$103.42) for ~8
sessions** right under the $103.30 resistance. Vol regime is **HIGH_IV in level
(81st pctile of 32 sessions) but cheap vs realized — VRP −0.165, PREMIUM_BUYING**
(realized 0.747 ≫ IV 0.582), so **debit/long-premium structures are the
edge-positive way to express the bull view.** OI has **built 30 consecutive days
(+1.09M)** — sustained engagement. The bullish_flow signal backtests 85.7% win,
but **n=7, in-sample → low confidence.** GEX regime is unstable (frequent flips).

> **Gap caveat (mandatory):** every "lookback" here is **gap-compressed** — the
> snapshot has a 21-session hole (2026-03-28→04-24). The "252d" IV percentile used
> **32 sessions**, the "90d" cumulative flow **33 sessions**, the "30d" trend spans
> 03-18→05-27 with the hole excluded. Quoted N, not calendar span. Trailing
> commands anchor to the latest date (2026-05-27).

## Key signals

- **VRP −0.165 → PREMIUM_BUYING** (IV30d 0.582 vs realized 0.747) — favor **debit** structures `[HIST:vrp]`
- **IV percentile 81.25 / z +0.665 / HIGH_IV** — but only **32 sessions** in window (not a true 1y) `[HIST:iv_percentile_zscore]`
- **Price: −33% YTD, −51.7% off 52w high, +12.9% on month, RSI 57** (neutral, not overbought) `[HIST:rsi fz]` `[HIST:52w_proximity fz]`
- **OI BUILDING 30 consecutive days, +1,088,629** (total OI ~799k→1.4M) — sustained positioning `[HIST:oi_trend]`
- **bullish_flow backtest: win_rate 85.7%, n=7** (in-sample, market-wide) → **low-confidence Kelly p** `[HIST:signal_backtest]`

## Detailed findings

### IV regime `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- `current_iv30d` 0.5818, `iv_percentile` **81.25**, `iv_zscore` +0.665, `regime` HIGH_IV (over **32 dates**, not 252).
- `vrp` **−0.1652**, `realised_vol` 0.747, `regime` **PREMIUM_BUYING** — "Vol cheap vs realised — favour premium buying." The violent $113→$87→$103 round-trip drove realized far above implied; even "high" IV is underpriced vs the actual path. **→ buy debit, don't sell premium.**

### Cumulative premium flow (33 sessions) `[HIST:cumulative_premium_flow]`

- `cumulative_bullish` $1,010.5M vs `cumulative_bearish` $965.0M → `net_flow` **+$45.5M**, `trend_direction` **MIXED** (51.1% / 48.9%). A *slight* net-bullish lean over the window, **not** a clean persistent stealth build — engagement is growing (OI) but premium direction has been two-way.

### P/C ratio z-score `[HIST:pc_ratio_zscore]`

- `current_pc_ratio` 0.284 vs 20d mean 0.366, `zscore` **−0.601**, `extreme` **NORMAL**. Call-heaviness is *within* NOW's normal range — **no contrarian P/C extreme** (tempers, slightly, phase-4's complacent-skew flag).

### Multi-day trend (price + flow) `[HIST:trend]`

| date | close | flow | iv_rank | net_flow $ |
|------|-------|------|---------|------------|
| 03-18 | 113.71 | bearish | 43.1 | −5.5M |
| 03-27 | 99.41 | bearish | 73.2 | −3.0M |
| **[21-session gap]** | | | | |
| 04-27 | 90.45 | bearish | 61.3 | −2.2M |
| 04-30 | 88.31 | bearish | 57.9 | −6.8M |
| **05-13** | **87.05** ◀ low | bearish | 58.5 | −3.6M |
| 05-15 | 95.16 | bullish | 65.3 | +12.2M |
| 05-18 | 103.42 | bullish | 69.3 | +15.8M |
| 05-20 | 103.30 | bearish | 74.0 | −0.1M |
| 05-21 | 99.69 | bearish | 63.3 | −7.8M |
| 05-22 | 102.13 | bullish | 59.0 | +13.0M |
| 05-26 | 100.02 | bullish | 64.3 | +2.0M |
| **05-27** | **102.12** | bullish | 63.1 | +5.0M |

`price_change` 113.71→102.12 (−10% over window); `iv_rank_change` 43.1→63.1; flow
**14 bullish / 16 bearish days**. The shape: crash → **V-bottom 5/13 → +18% rip →
8-session consolidation under $103.30.** Today's bull flow is building **at the top
of that range, into resistance.**

### Price context (`fz`, independent EOD cross-check) `[HIST:* fz]`

- RSI(14) **57.03** (neutral — room before overbought); price **+7.97% vs SMA20**, **+4.65% vs SMA50** (short/intermediate uptrend), **−28.09% vs SMA200** (major downtrend intact).
- **Perf YTD −33.34%**, Perf Month **+12.90%**; **52w high $211.48 (−51.7%)**, 52w low $81.24 (+25.7%). ATR(14) **$5.68 (~5.6%/day)** — wide; phase-9 stops must respect this.
- Read: **fallen angel mid-recovery.** Tactically constructive (above 20/50-SMA, RSI room), structurally still broken (below 200-SMA, half its high). The bull trade is a **bounce-continuation**, not a trend breakout — phase-6/7 must explain the −33% YTD.

### GEX time series `[HIST:gex_time_series]`

- **Unstable regime** — 8 POSITIVE↔NEGATIVE flips in the window (4/30, 5/01, 5/04, 5/06, 5/15, 5/21, 5/22, **5/26**). ZGL erratic (values from None to 117). Most recent flip **5/26 POSITIVE→NEGATIVE** (spot 100.58, ZGL 105.42) → confirms today's short-gamma read but flags **low ZGL stability** (treat as ±2% band) and **a regime flip within 5d → expect larger intraday ranges.**

### OI trend `[HIST:oi_trend]`

- `overall_trend` **BUILDING**, `total_net_oi_change` **+1,088,629**, `consecutive_build_days` **30**. Total OI roughly doubled (799k→1.4M) across the recovery — sustained, growing positioning interest (engagement up even as premium *direction* stayed mixed).

### Signal backtest `[HIST:signal_backtest]`

- `signal_type` bullish_flow, `win_rate` **85.7%**, `total_signals` **7**, `avg_move_pct` **+5.06%** (5 trading-day horizon). Market-wide, NOT NOW-specific (results: AAPL/TSLA/MCHP/etc., 6 up / 1 down). Methodology note: **"In-sample backtest — not a robust live edge."** Per the pitfall, **n=7 < 10 → low confidence**; phase-9 must apply the N-conditional Kelly cap.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --symbol NOW --lookback-days 252` | pctile 81.25, HIGH_IV, **32 dates** |
| `uw historical vrp --symbol NOW --realised-window-days 30` | VRP −0.165, PREMIUM_BUYING |
| `uw historical pc-ratio-zscore --symbol NOW --lookback-days 20` | z −0.601, NORMAL |
| `uw historical cumulative-premium-flow --symbol NOW --days 90` | net +$45.5M, MIXED, 33 dates |
| `uw historical trend --symbol NOW --days 30` | V-bottom 5/13 $87 → +18% → consol; 14/16 bull/bear days |
| `uw historical gex-time-series --symbol NOW --days 30` | 8 regime flips, latest 5/26 →NEGATIVE, ZGL unstable |
| `uw historical oi-trend --symbol NOW --days 30` | BUILDING, +1.09M, 30 consec days |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5` | win 85.7%, n=7 (in-sample) |
| `fz quote NOW` | RSI 57, −33% YTD, −51.7% off 52w high, ATR $5.68 |

## Tool errors

None. (Caveat, not error: all UW lookback windows are gap-compressed — N stated above. No evidence the CLI interpolated across the hole; `dates_covered`/`dates_used` confirm the gap is *excluded*, not filled.)

## Verdict for downstream

- **Volatility regime:** HIGH in level (81st pctile/32 sessions) but **CHEAP vs realized — PREMIUM_BUYING (VRP −0.165).** Favor **debit/long structures** (buy calls / call debit spreads). Selling premium is the wrong side here.
- **Conviction (is today's signal HISTORICALLY EDGE-POSITIVE?): 3/5.** Supports: premium-buying regime, 30-day OI build, short-gamma squeeze potential, 85.7% backtest. Drags: counter-trend (below 200-SMA, −33% YTD), stalled at $103.30 resistance, MIXED premium history, **backtest n=7**, complacent skew.
- **Three specific data points:** IV percentile **81.25** (of 32 sessions) · VRP **−0.165** (premium-buying) · bullish_flow win_rate **85.7% (n=7)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.857
  win_rate_n:                7
  win_rate_source:           backtest
  ```
  ⚠️ n=7 < 10 → in-sample, low confidence. Apply `rubrics/sizing-rubric.md`
  N-conditional cap (do NOT size full Kelly on a 7-sample in-sample rate).
- **Open questions:**
  1. **Why is NOW −33% YTD / −51% off highs?** Phase-6 (macro) + phase-7b (fundamentals) must source the de-rating — is the bounce a dead-cat or a real bottom?
  2. Does the stall at $103.30 (= 5/20 high = DP supply = below ZGL $104.62) break or reject? The whole bull thesis hinges on clearing it.
