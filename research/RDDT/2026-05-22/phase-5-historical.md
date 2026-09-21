# Phase 5 — Historical Context & VRP

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0-intake.md (gap), phase-0.5-context.md,
phase-1-flow.md, phase-4-structure.md

## Summary

History **weakens the bearish directional case and favors a fade / two-sided
read.** Vol is **cheap** (IV30d 62.0%, IV percentile 16.7, regime LOW_IV) and
**VRP is −0.05 (PREMIUM_BUYING — realized 67.0% > implied 62.0%)**, so options are
underpriced vs how much RDDT actually moves → debit structures favored. Critically,
the **`bearish_flow` signal backtest win-rate is only 30% (n=10, 10-day horizon)** —
recent bearish-flow signals were mostly *faded* (the cohort rallied: AMD +20%/+11%,
TSLA +6.8%, QQQ +3.9%). Today's **P/C ratio is a +2.77σ BEARISH_EXTREME** (0.92 vs a
0.47 twenty-day mean) — a classic contrarian exhaustion flag. The 90-day cumulative
premium flow is **MIXED/balanced** (net −$5.8M on ~$800M total) — there is **no
persistent stealth bearish campaign**; the bearishness is concentrated in the recent
May down-leg. Structurally, today's GEX −$11.66M is the **most negative in the
30-session window**, and the only comparable FULLY_NEGATIVE readings (3/26 −7.3M,
3/27 −10.3M) coincided with RDDT's prior sharp drop to ~$121 — so short gamma *has*
accompanied real declines, the one piece that supports the bears. Net: cheap-vol,
premium-buying, contrarian-extreme tape where the bearish signal has poor historical
follow-through — argues for small size and respect for a snap-back.

> **Gap caveat (phase-0):** all "30-day"/"90-day"/"252-day" windows below are
> limited to the **31 sessions actually present** (2026-03-13→03-27, then
> 04-27→05-22; April 2026 absent). `iv_percentile` used 30 dates (not 252);
> cumulative flow "90d" = 31 sessions. Treat percentiles as ~6-week, not annual.

## Key signals

- **`bearish_flow` backtest win-rate 30% (n=10, 10d)** — below 0.45; bearish flow
  has been a **fade** in this tape [HIST:signal_backtest]
- **P/C z-score +2.77 → BEARISH_EXTREME** (0.92 vs 0.47 mean, σ0.16) — contrarian
  exhaustion flag [HIST:pc_ratio_zscore]
- **VRP −0.0501 → PREMIUM_BUYING**; IV percentile **16.7 (LOW_IV)** → cheap vol,
  buy premium [HIST:vrp] [HIST:iv_percentile_zscore]
- 90-day cumulative flow **MIXED** (bearish $406.6M vs bullish $400.8M, net
  −$5.8M) — **no persistent bearish build** [HIST:cumulative_premium_flow]
- Today GEX **−$11.66M = most negative in 30-session window**; FULLY_NEGATIVE GEX
  previously marked the 3/26–27 drop to $121 [HIST:gex_time_series]

## Detailed findings

### IV regime — [HIST:iv_percentile_zscore] [HIST:vrp]

- current_iv30d 0.6203; **iv_percentile 16.67; z-score −0.836; regime LOW_IV**
  (dates_used 30 — ~6-week percentile, not annual).
- **VRP −0.0501** (iv30d 0.6203 − realized 0.6704) → **PREMIUM_BUYING**. Implied
  vol sits *below* trailing realized — RDDT is moving more than options price.
  Favor **debit** structures; selling premium here is fighting realized.

### Cumulative premium flow (≈90d / 31 sessions) — [HIST:cumulative_premium_flow]

cumulative_bearish $406.6M vs cumulative_bullish $400.8M → **net −$5.79M,
trend_direction MIXED**. Over the full window the book is **balanced** — the
net-bearishness is ~0.7% of gross flow. This is **not** a stealth institutional
bearish accumulation (which the rubric would flag as high-confidence directional);
it is a recent-May tilt on top of a balanced base. Downgrades the "smart money is
positioning short" interpretation.

### P/C ratio z-score (sentiment extreme) — [HIST:pc_ratio_zscore]

current_pc 0.9157, mean 0.4656, std 0.1626 → **z +2.768 = BEARISH_EXTREME**.
RDDT structurally runs very call-heavy (~0.47 P/C); today's jump to 0.92 is a
2.8σ event. Per rubric (|z|>2 = sentiment extreme → contrarian setup possible).
Note the nuance vs phase-4: P/C *volume* spiked, but 25Δ skew stayed COMPLACENT
(puts not bid up) — a volume surge in puts without an IV-skew bid, consistent with
short-dated put *trading* (and call-writing) rather than panic tail-hedging.

### GEX time series (30 sessions) — [HIST:gex_time_series]

Regime is **highly unstable** — 7 zero-gamma flips in 30 sessions. Today
(2026-05-22) prints **total_gex −$11.66M, FULLY_NEGATIVE — the most negative in the
entire window.** The only prior comparable FULLY_NEGATIVE clusters: **3/26 (−7.3M,
spot $127) and 3/27 (−10.3M, spot $121.55)** — i.e. short gamma accompanied RDDT's
prior sharp decline, and 5/08 (−4.7M) and 5/12 (−0.6M) marked smaller down-days.
**Supports the bears:** RDDT's deepest short-gamma readings have coincided with its
worst price action. The down-leg from the 5/05 $172 high (POSITIVE GEX +14M) to
today (−11.66M) is a clean regime deterioration.

### OI trend (30 sessions) — [HIST:oi_trend]

consecutive_build_days 30; today net_oi_change +4,974 (362 contracts up vs 221
down). Today's top OI builds: 155C 0DTE +589, **190C 6/18 +514, 200C 6/18 +416**
(call writes, phase-3), plus 5/29 call builds (160C +407, 152.5C +360, 170C +351)
and 0DTE puts (135P +462, 142P +263). OI has accreted steadily over the window —
growing engagement — but today's builds are **call-write-heavy** (upside being
sold), consistent with phases 1/3, not fresh downside loading.

### Multi-day trend table (selected) — [HIST:historical_trend]

| Date | Close | net_flow $M | flow | IV rank | P/C |
|------|-------|-------------|------|---------|-----|
| 05-22 | 141.67 | **−6.98** | bearish | 18.7 | 0.92 |
| 05-21 | 150.04 | +2.26 | bullish | 21.0 | 0.43 |
| 05-20 | 146.72 | −6.57 | bearish | 22.0 | 0.59 |
| 05-08 | 155.70 | −5.30 | bearish | 13.7 | 0.37 |
| 05-05 | 171.97 | +4.45 | bullish | 26.5 | 0.16 |
| 05-01 | 166.48 | **+19.04** | bullish | 26.9 | 0.40 |
| 04-27 | 160.21 | +2.53 | bullish | 66.9 | 0.46 |
| 03-27 | 121.84 | −1.13 | bearish | 37.1 | 0.93 |

bearish_days 18 / bullish_days 12 over the window. The 5/05 $172 peak (after the
5/01 +$19M blow-off) has unwound to $141.67 — a −18% distribution. Today's −$6.98M
is the most negative net_flow shown.

### Signal backtest (current signal's edge) — [HIST:signal_backtest]

- **`bearish_flow`: win_rate 30.0%, total_signals 10, lookback 10d, avg_move 4.24%.**
  Of the 10 most-recent bearish-flow signals, only 3 resolved *down*; the rest
  rallied (AMD +20.5% & +11.0%, TSLA +6.8%, QQQ +3.9%, IWM +3.5%/+2.5%, GOOG −0.7%).
  **Market-wide, not RDDT-specific; n=10; window is a risk-on rebound tape** — so
  read as "bearish flow has recently been a fade," not a precise RDDT probability.
  Below the 0.45 rubric line → **downgrade bearish conviction**.
- **`dark_pool_accumulation`: no backtest results (n=0)** → win_rate_source null
  for the phase-2 accumulation signal; cannot quantify that edge here.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_trend` | RDDT, 30d | 18 bearish / 12 bullish days; peak $172 (5/05) → $141.67 |
| `historical_iv_percentile_zscore` | RDDT, 252 | pctile 16.7, LOW_IV (30 dates used) |
| `historical_vrp` | RDDT, 30 | VRP −0.05, PREMIUM_BUYING |
| `historical_cumulative_premium_flow` | RDDT, 90 | net −$5.8M, MIXED (balanced) |
| `historical_pc_ratio_zscore` | RDDT, 20 | z +2.77, BEARISH_EXTREME |
| `historical_gex_time_series` | RDDT, 30, dte45 | today −$11.66M = most negative; 7 flips |
| `historical_oi_trend` | RDDT, 30, top10 | +4,974 net today; call-write-heavy builds |
| `historical_signal_backtest` | bearish_flow, 10d | **win_rate 30%, n=10** |
| `historical_signal_backtest` | dark_pool_accumulation, 10d | no results, n=0 |

## Tool errors

None. **Data-quality caveat:** every multi-day window is gap-limited to ≤31
sessions (April absent). The MCP series did **not** appear to interpolate across the
hole (dates_covered lists confirm the gap), so the lines are trustworthy *as ≤31-session
series* — but percentiles/z-scores are ~6-week, not annual; treat confidence
accordingly.

## Verdict for downstream

- **Volatility regime:** CHEAP (IV pctile 16.7, rank 18.7) and **PREMIUM_BUYING**
  (VRP −0.05) → debit > credit for any directional expression.
- **Premium environment:** premium-BUYING; realized > implied. Do not sell vol.
- **Conviction today's (bearish) signal is HISTORICALLY EDGE-POSITIVE: 2/5.** The
  30% backtest win-rate, +2.77σ contrarian P/C extreme, MIXED 90d flow, and phase-2
  dip-buying all say the bearish flow has been a fade. The *one* bear support is the
  record-negative short-gamma reading, which historically tracked RDDT declines.
- **Three specific data points:** IV percentile **16.7**; VRP **−0.0501**; bearish_flow
  signal win-rate **30% (n=10)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bearish_flow
  signal_backtest_win_rate:  0.30
  win_rate_n:                10
  win_rate_source:           backtest
  ```
  Note: win_rate 0.30 with n=10 is both **low and small-sample** → phase-9 must
  apply the N-conditional cap (`rubrics/sizing-rubric.md`) AND treat <0.45 as a
  conviction downgrade. The 30% argues the directional *bear* trade is small-or-skip;
  if anything the edge has been on the *fade*.
- **Open questions:**
  - Does the record short-gamma (bear support) outweigh the 30% fade win-rate +
    dip-buying + contrarian P/C (bull/fade support)? → phase-8b debate (this is THE
    question).
  - Is there an RDDT-specific catalyst in the next 10 sessions, or is this pure
    technical/positioning unwind? → phase-6 (macro/calendar), phase-7c (sentiment).
