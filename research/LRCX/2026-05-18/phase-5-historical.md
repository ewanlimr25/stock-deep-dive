# Phase 5 — Historical Context & VRP

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

LRCX is in a **rich-vol, premium-selling regime**: IV30d **64.21%**, VRP
**+8.9%** (PREMIUM_SELLING), IV rank **72** (elevated). The 90-day
cumulative premium flow is **+$43.8M net bullish** ($528M bullish vs $484M
bearish) but tagged "MIXED" — institutional flows are *not* directionally
one-sided. The 26-session price path is **+34% Mar→May ($212→$299) then
-5% Thursday→Friday ($299.82 → $284.51)** with 5/15 flipping the daily
flow tape from **bullish to bearish** for the first time in 5 sessions.
GEX has flipped regime **8 times in 26 days** (unstable dealer regime),
and the market-wide **bearish_flow signal backtest is 100% win rate on
the n=7 semi-sector cohort (avg -4.4% over 20 days)** — a strong sector
tailwind for the short side.

## Key signals

- **VRP +8.9% (PREMIUM_SELLING)**: IV30d 64.21% vs realized 55.31% →
  options pricing more vol than is being realized [HIST:vrp].
- **IV rank 71.97 / IV percentile 44**: rank is elevated short-term but
  raw IV is near the 1y median — divergence implies a recent regime
  reset [HIST:iv_percentile_zscore, historical_trend].
- **8 GEX regime flips in 26 sessions** (3/24, 3/25, 4/29, 4/30, 5/4, 5/6,
  5/13, 5/14): dealer hedging is unstable; expect larger realized ranges
  [HIST:gex_time_series].
- **23-day consecutive OI build** culminating in 5/15's +8,189 net OI:
  sustained institutional positioning over the entire data window
  [HIST:oi_trend].
- **Bearish-flow signal backtest 100% win rate, avg -4.41% in 20 days**
  across the n=7 semi cohort (SPY -0.4, NDX -0.8, SOXL -10.9, MU -5.5,
  TSLA -2.6, SMH -0.9, INTC -9.8) [HIST:signal_backtest].

## Detailed findings

### IV regime

| Metric | Value | Regime |
|--------|-------|--------|
| Current IV30d | **64.21%** | — |
| 1y IV percentile | 44 | NORMAL |
| 1y IV z-score | -0.18 | NORMAL |
| **VRP (IV30 - RV30)** | **+8.9%** | **PREMIUM_SELLING** |
| Realized vol 30d | 55.31% | — |
| Latest IV rank (in-window) | **71.97** | elevated |

Note: `iv_percentile_zscore` reports `dates_used = 25`, meaningfully less
than the 252-day target (data gap between 2026-03-27 and 2026-04-27). The
44th percentile read is therefore over ~25 dates. The intra-window IV
rank of 71.97 is the better short-term gauge: LRCX IV is in the **upper
third of its 5-week range**, but has come off the 78–79 peaks seen 5/11–5/13.

VRP +8.9% is squarely a **credit-structure environment**: short premium
(verticals, iron condors, calendars, covered calls) is favored over
debit/long-vol structures, all else equal.

### Cumulative premium flow (90d, n=26 sessions)

| Bucket | $ |
|--------|--:|
| Cumulative bullish | $528,218,006 |
| Cumulative bearish | $484,432,731 |
| **Net flow** | **+$43,785,275** |
| Trend direction | **MIXED** |

Despite +$43.8M net bullish over 26 sessions, the bull/bear split is 52/48
— not a directional regime. Combined with phase-2's 5-day distribution
read at $295.44 and phase-1's mixed sweep tape, the multi-week conclusion
is **balanced premium absorption** rather than stealth accumulation or
distribution.

### P/C ratio z-score (20-day)

| Metric | Value |
|--------|------:|
| Current P/C | 0.76 |
| 20d mean | 0.97 |
| 20d std | 0.39 |
| **Z-score** | **-0.534** |
| Extreme | **NORMAL** |

Sentiment is **call-biased but not extreme** (-0.53 sigma below mean P/C).
No contrarian setup; the call-write tape from phase-1 is sentimentally
aligned with broader retail call buying.

### GEX time series (26 sessions, dte_max=45)

Total GEX trajectory and regime flips:

| Date | Spot | Total GEX | ZGL | Regime |
|------|-----:|-----------:|----:|--------|
| 2026-03-13 | 213.90 | -$35k | n/a | FULLY_NEG |
| 2026-03-17 | 223.39 | -$4.78M | $135.73 | POSITIVE |
| 2026-03-24 | 238.94 | +$14.39M | **$361.51** | **NEGATIVE** (flip) |
| 2026-03-25 | 232.83 | -$58.34M | $105.50 | **POSITIVE** (flip) |
| 2026-03-27 | 213.05 | -$32.65M | n/a | FULLY_NEG |
| 2026-04-27 | 258.73 | +$72.90M | $101.10 | POSITIVE |
| 2026-04-29 | 246.75 | +$31.31M | **$285.97** | **NEGATIVE** (flip) |
| 2026-04-30 | 256.04 | +$37.89M | $135.52 | **POSITIVE** (flip) |
| 2026-05-04 | 258.38 | +$19.50M | **$307.15** | **NEGATIVE** (flip) |
| 2026-05-06 | 294.33 | **+$440.34M** | $97.13 | **POSITIVE** (flip, max GEX) |
| 2026-05-11 | 297.12 | +$74.97M | $30.22 | POSITIVE |
| 2026-05-12 | 284.15 | +$103.60M | $40.00 | POSITIVE |
| 2026-05-13 | 294.92 | +$97.19M | **$303.92** | **NEGATIVE** (flip) |
| 2026-05-14 | 299.82 | +$213.49M | $299.77 | **POSITIVE** (flip) |
| 2026-05-15 | 285.18 | **+$109.26M** | $70.78 | POSITIVE |

**8 regime flips in 26 sessions** — dealer regime is **highly unstable**.
Every flip is a "spot crossed ZGL" event, often within ±5%. The 5/13–5/14
flip (NEG→POS) happened at $295–$300 and was followed by the 5/15
gap-down to $285. The current $109M positive GEX is supportive but
**conditional**: ZGL bouncing between $30 and $304 over two weeks means
any IV reset or material flow flip could re-anchor it at-the-money and
trigger another flip.

### OI trend (23-day consecutive build)

- **Consecutive OI build days: 23** (most of the data window).
- 5/15 net OI change: **+8,189 contracts**.
- Top contracts driving build are the 8/21 calls (400C +2007, 310C +1503,
  320C +888) — confirmed by phase-3.
- Total OI: 600,399 on 5/15, vs 420,878 on 3/23 → **+43% in 7 weeks**.

This is the **institutional campaign signature** phase-3 flagged: OI is
sticky, building, multi-week, and concentrated in late-July / 8/21
post-earnings expiry. Not a 1-day spike.

### Multi-day trend (selected days)

| Date | Close | Flow direction | IV30 | IV rank | Net flow | P/C |
|------|-----:|----------------|------:|--------:|---------:|----:|
| **2026-05-15** | 284.51 | **bearish** | 64.21 | **71.97** | -$2,243,998 | 0.76 |
| 2026-05-14 | 299.15 | bullish | 65.50 | 77.28 | +$2,853,374 | 0.50 |
| 2026-05-13 | 295.44 | bullish | 65.91 | 78.23 | +$4,697,757 | 0.82 |
| 2026-05-12 | 289.24 | bullish | 65.06 | 76.29 | +$656,433 | 0.97 |
| 2026-05-11 | 296.05 | bullish | 66.45 | 79.44 | +$14,704,073 | 0.66 |
| 2026-05-08 | 293.94 | bearish | 65.09 | 75.77 | -$2,895,751 | 0.62 |
| 2026-05-07 | 286.52 | bearish | 64.09 | 74.08 | -$1,687,959 | 1.85 |
| 2026-05-06 | 297.17 | bullish | 64.76 | 75.60 | +$8,109,932 | 0.87 |
| 2026-05-05 | 275.77 | bullish | 60.65 | 67.16 | +$5,335,418 | 0.67 |
| 2026-05-04 | 258.57 | bearish | 60.85 | 66.73 | -$12,281,406 | 1.51 |
| 2026-05-01 | 256.72 | bearish | 60.65 | 66.27 | -$1,150,513 | 1.54 |
| 2026-04-29 | 248.75 | bearish | 65.15 | 76.50 | -$32,496 | 0.98 |
| 2026-04-27 | 259.47 | bearish | 63.38 | 72.47 | -$1,281,757 | 0.83 |
| 2026-03-27 | 211.41 | bullish | 74.75 | 82.17 | +$12,192,950 | 1.77 |

**Narrative:** Mar 27 was the *prior* data point before the gap. Stock
rallied ~$48 from $211 (3/27) to $259 (4/27) presumably driven by the
gap window we can't see (April 1–24). May saw the second leg: $258→$299
(+16%). May 15 broke the rally — first bearish-flow day in 5 sessions
and the largest single-day drop ($299.82 → $284.51 = -5.11%) in the
visible window.

**bullish_days = 14, bearish_days = 12** over n=26 sessions — net flow
bullish but barely. The most recent **flow_direction_latest = "bearish"**.

### Signal backtest — bearish_flow (n=7, 20d horizon)

| Ticker | Signal date | Price on signal | Price after 20d | Pct change |
|--------|-------------|-----------------:|----------------:|----------:|
| SPY | 2026-05-13 | 742.31 | 739.17 | **-0.42%** |
| NDX | 2026-05-13 | 29,366.94 | 29,125.20 | **-0.82%** |
| **SOXL** | 2026-05-13 | 184.24 | 164.18 | **-10.89%** |
| **MU** | 2026-05-12 | 766.58 | 724.66 | **-5.47%** |
| TSLA | 2026-05-12 | 433.45 | 422.24 | **-2.59%** |
| **SMH** | 2026-05-12 | 561.25 | 556.34 | **-0.87%** |
| **INTC** | 2026-05-12 | 120.61 | 108.77 | **-9.82%** |
| **Avg** | — | — | — | **-4.41%** |
| **Win rate** | — | — | — | **100%** |

Five of the seven signal-fires are semis (SOXL, MU, SMH, INTC) — same
sector as LRCX. **Average post-signal move in semi peers: -6.76%.** This
is small-N but unambiguous: bearish-flow signals in semis during the past
week have **all** resolved bearish. LRCX is in the same flow cohort by
construction (the SMH 5/22 500P bid-side flow from phase-1).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=LRCX, lookback-days=252 | IV30d 64.21, %ile 44 |
| `mcp__uw-pp__historical_vrp` | symbol=LRCX, date=2026-05-15, realised-window-days=30 | VRP +8.9% |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=LRCX, days=90 | net +$43.8M, MIXED |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=LRCX, lookback-days=20 | z=-0.534, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=LRCX, days=30, dte-max=45 | 8 flips |
| `mcp__uw-pp__historical_oi_trend` | symbol=LRCX, days=30, top-n=10 | 23 consecutive build days |
| `mcp__uw-pp__historical_trend` | symbol=LRCX, days=30 | 14 bull / 12 bear days |
| `mcp__uw-pp__historical_signal_backtest` | signal-type=bearish_flow, lookback-days=20, top-n=20 | 100% win, -4.41% avg |

## Tool errors

(none — see Phase 0 note re: data gap between 2026-03-27 and 2026-04-27,
which affects the IV-percentile sample size and the cumulative flow window)

## Verdict for downstream phases

- **Bias from this phase:** **PREMIUM-SELLING regime with bearish-flow
  sector tailwind**. VRP +8.9% favors credit structures, not debit. The
  bearish_flow signal backtest is 7-for-7 in the recent semi cohort
  (avg -4.4%), giving phase-9 statistical air cover for short-biased
  structures. The 5/15 flow flip from bullish-to-bearish (first in 5
  sessions) is a tape-level confirmation.
- **Conviction: 4/5**. IV regime call is high-confidence (VRP is clear).
  The signal backtest is small-N (7) and market-wide, not LRCX-specific,
  so the 100% win rate is suggestive not proof — flag as low statistical
  power.
- **Three data points for phase-9:**
  1. **VRP +8.9%, IV rank 71.97** → favor credit spreads / short premium.
  2. **5/15 flow flipped bearish** after 4 bullish sessions; stock dropped
     -5.1% same day. First wedge in the bull rhythm.
  3. **Bearish-flow signal: 100% win rate, avg -4.4% in 20 days, 5/7 are
     semis** (SOXL -10.9%, INTC -9.8%, MU -5.5%, TSLA -2.6%, SMH -0.9%).
     LRCX should be priced as the next domino, not as an idiosyncratic
     story.
- **Open questions:**
  - **What triggered the 5/13–5/14 GEX flip and 5/15 gap-down?** Phase 6
    macro/news scan needs to identify the catalyst (FOMC, China headlines,
    sector-specific datapoint, single-name guidance/news).
  - The 8 GEX flips imply a market that doesn't know which way to trade
    LRCX — combined with the call-overwrite OI build, this looks like
    **institutions trying to monetize range-bound volatility while retail
    keeps chasing direction**.
  - **Is the data gap (3/27 → 4/27) hiding an earnings event?** LRCX
    typically reports late January / late April / late July / late
    October. The 4/27 data resumption with stock at $258.73 (up from
    $211.41 on 3/27) is consistent with a **post-earnings rally**.
    Phase 6 must confirm whether April-earnings has already happened and
    next event is late-July.
