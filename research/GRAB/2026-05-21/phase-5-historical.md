# Phase 5 — Historical Context & VRP

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Generated:** 2026-05-21T20:50:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Phase-5 sharply reframes the prior phases. **90-day cumulative premium flow
is NET BEARISH at -$6.28M** (bearish $16.6M vs bullish $10.3M)
[HIST:cumulative_premium_flow], and **26 of the last 30 trading days printed
bearish-net flow** with price falling from $3.91 (2026-04-27) to $3.50–$3.56
today — a roughly **10% drawdown** [HIST:historical_trend]. Against this
context, today's dark-pool block buy (phase-2) and covered-call signature
(phase-3) are the FIRST credible countertrend signal in nearly 30 sessions.
IV is **NORMAL at the 38th percentile** (IV30d = 44%, z = -0.46)
[HIST:iv_percentile_zscore], and VRP is **+14.1%** (IV30d 44% vs realised
30% — PREMIUM_SELLING regime) [HIST:vrp]. GEX regime has been
**stably POSITIVE for all 19 sampled days**, no regime flips
[HIST:gex_time_series]. OI is in a **4-day build** (consecutive_build_days
= 4) [HIST:oi_trend]. Net: the multi-week backdrop is bearish-with-
declining-vol; today is a potential inflection but a single-session signal
against a 30-day trend deserves caution.

## Key signals

- **90d cumulative premium flow: -$6,283,288 NET BEARISH**
  [HIST:cumulative_premium_flow] — institutional premium has been on the
  sell side for the past quarter.
- **30d historical trend: 26 bearish days / 4 bullish days**, price down
  ~10% peak-to-current [HIST:historical_trend] — strong downtrend that
  today is the first credible counterpunch to.
- **IV30d 44.04% = 38th percentile (NORMAL, z=-0.46)**
  [HIST:iv_percentile_zscore] — IV is below 1y average but not extreme; no
  vol-mean-reversion edge in either direction.
- **VRP +14.1% (PREMIUM_SELLING regime)** [HIST:vrp] — confirms phase-3's
  covered-call read; sell-premium structures (credit spreads, covered
  calls) are historically the edge here.
- **GEX regime POSITIVE every day for 30d, ZGL stable $2.07–$3.03**
  [HIST:gex_time_series] — long-gamma is structural, not transient. Mean
  reversion is the dominant intraday tape behavior.
- **OI: 4 consecutive build days, today +5,519 net OI**
  [HIST:oi_trend] — institutional positioning is being added, not unwound.

## Detailed findings

### IV regime (percentile + z-score + VRP)

| Metric | Value |
|--------|-------|
| current_iv30d | 0.4404 (44.04%) |
| iv_percentile (1y) | 37.93% |
| iv_zscore | -0.461 |
| regime | NORMAL |
| realised_vol (30d) | 0.299 |
| **VRP** | **+0.1414 (PREMIUM_SELLING)** |

IV is below the 1y mean but not at any vol extreme. Realised has been
~30% — quite tame for a small-cap EM tech name. VRP is +14% → the option
market is paying ~14 vol points of premium over realised, which is on the
high side for a sub-50% IV name. **Credit structures (sell premium) get
the VRP edge** per rubric heuristic.

### Cumulative premium flow (90d)

| Side | Total ($) |
|------|-----------|
| Bullish | $10,314,835 |
| Bearish | $16,598,123 |
| **Net** | **-$6,283,288 (BEARISH)** |
| Trend direction | BEARISH |
| Days covered | 30 sessions across 90 calendar days (2026-03-13 → 2026-05-21) |

Crucial context: **the institutional premium pump has been NET SHORT GRAB
for 90 days.** Today's dark-pool accumulation (phase-2) and covered-call
overlay (phase-3) are credible as a turn signal but need cross-confirmation
across more sessions before a high-conviction long can be sized.

### P/C ratio z-score (sentiment extremes)

| Metric | Value |
|--------|-------|
| current_pc_ratio | 0.1596 |
| mean_pc_ratio (20d) | 0.1869 |
| std | 0.1738 |
| z-score | -0.157 |
| extreme | NORMAL |

PC is below 1 (call-heavy book) but flat relative to its 20-day mean. **No
sentiment extreme** → no contrarian setup. Note: GRAB historically prints
PC < 0.2 (very call-heavy) due to the dominant covered-call OI base —
this is structural, not a sentiment tell.

### GEX time series (30d ZGL stability)

| Date | Spot | Total GEX | ZGL | Regime |
|------|------|-----------|-----|--------|
| 2026-04-27 | 3.91 | 38.7M | 3.03 | POSITIVE |
| 2026-04-28 | 3.84 | 41.9M | 3.01 | POSITIVE |
| 2026-04-29 | 3.78 | 24.6M | 2.38 | POSITIVE |
| 2026-04-30 | 3.77 | 29.0M | 3.02 | POSITIVE |
| 2026-05-01 | 3.61 | 40.8M | 3.02 | POSITIVE |
| 2026-05-04 | 3.60 | 188.4M | 3.02 | POSITIVE |
| 2026-05-05 | 3.70 | 304.2M | null | FULLY_POSITIVE |
| 2026-05-06 | 3.81 | 447.4M | 3.00 | POSITIVE |
| 2026-05-07 | 3.83 | 405.6M | 3.01 | POSITIVE |
| 2026-05-08 | 3.70 | 274.9M | 3.00 | POSITIVE |
| 2026-05-11 | 3.69 | 362.2M | 2.65 | POSITIVE |
| 2026-05-12 | 3.64 | 185.4M | 3.00 | POSITIVE |
| 2026-05-13 | 3.61 | 253.0M | 2.07 | POSITIVE |
| 2026-05-14 | 3.59 | 224.4M | 3.01 | POSITIVE |
| 2026-05-15 | 3.54 | 155.2M | 3.00 | POSITIVE |
| 2026-05-18 | 3.55 | 375.6M | 2.92 | POSITIVE |
| 2026-05-19 | 3.52 | 169.2M | 3.00 | POSITIVE |
| 2026-05-20 | 3.47 | 38.9M | 3.01 | POSITIVE |
| 2026-05-21 | 3.50 | 298.4M | null | FULLY_POSITIVE |

**regime_flip_dates: null** — no GEX regime flips in 30d. Long-gamma is
structural. Two days printed FULLY_POSITIVE (no ZGL exists because all
strikes are net long-gamma) — 2026-05-05 and today.

ZGL has hovered ~$3.00 with brief dips to $2.07–$2.65. The fact that
today's 365-DTE ZGL is **$2.63** (per phase-4) but the 45-DTE shows null
means the long-dated LEAP OI is what's holding the regime up.

### OI trend (30d)

`consecutive_build_days = 4`; net today +5,519 OI (110 increases vs 30
decreases by contract count). Multi-day OI build confirms institutional
positioning is being added (not closed). Top contracts driving the build
match the phase-3 detail (LEAP $3, $4, $5 calls being written).

### Multi-day historical trend (last 15 of 30 daily rows)

| Date | Close | Flow dir | Net flow ($) | IV30d | IV rank | PC ratio |
|------|-------|----------|--------------|-------|---------|----------|
| 2026-05-21 | 3.56 | bearish | -93,468 | 44.0% | 31.0 | 0.160 |
| 2026-05-20 | 3.51 | bearish | -123,613 | 37.9% | 14.1 | 0.140 |
| 2026-05-19 | 3.505 | bearish | -230,227 | 43.6% | 28.6 | 0.100 |
| 2026-05-18 | 3.54 | bearish | -67,370 | 48.2% | 40.5 | 0.091 |
| 2026-05-15 | 3.565 | bearish | -349,158 | 45.5% | 29.2 | 0.140 |
| 2026-05-14 | 3.57 | bearish | -308,195 | 42.7% | 26.2 | 0.086 |
| 2026-05-13 | 3.63 | bearish | -61,190 | 45.3% | 33.2 | 0.240 |
| 2026-05-12 | 3.64 | bearish | -134,514 | 43.8% | 29.2 | 0.891 (put spike) |
| 2026-05-11 | 3.65 | **bullish** | +259,695 | 46.1% | 35.2 | 0.180 |
| 2026-05-08 | 3.725 | **bullish** | +185,904 | 41.5% | 37.6 | 0.170 |
| 2026-05-07 | 3.79 | **bullish** | +18,523 | 43.7% | 28.9 | 0.078 |
| 2026-05-06 | 3.77 | bearish | -383,142 | 43.8% | 29.1 | 0.100 |
| 2026-05-05 | 3.681 | bearish | -27,296 | 46.3% | 49.6 | 0.150 |
| 2026-05-04 | 3.62 | bearish | -507,002 | 58.7% | 67.7 | 0.271 |
| 2026-05-01 | 3.67 | **bullish** | +91,663 | 58.5% | 67.1 | 0.180 |
| 2026-04-30 | 3.825 | bearish | -294,178 | 54.9% | 50.5 | 0.230 |

Pattern:
- **Bullish days are a clear minority** (only 4/30: May 1, 7, 8, 11) and
  they all printed at HIGHER prices than today. The trend has been to fade
  every bullish-flow bounce.
- **Today (2026-05-21) printed bearish flow** with net -$93K — even with
  the dark-pool block buy, the OPTIONS tape was net bearish. This is the
  signature of long-stock buying + offsetting options hedging.
- **Notable spike**: 2026-05-12 had PC ratio 0.891 — a putsurge day on
  bearish flow at $3.64 close. This was a defensive event (price was
  declining). Watch for repeat patterns.
- IV rank has compressed from ~67% (early May) to ~31% today — vol has
  bled out alongside the price drift.

### Signal backtest

`historical_signal_backtest(signal_type=dark_pool_accumulation)` returned
**no backtest results** (0 signals). The tool has no historical pattern
library for the "dark_pool_accumulation" signal type in this dataset. Re-
running with `bullish_flow` or `volume_spike` would test a different
hypothesis; we deliberately did NOT re-run because the dominant phase-1-4
signal IS dark-pool accumulation paired with covered-call overlay, not raw
bullish flow.

Treat the absence of backtest data as a phase-9 conviction CAP: we cannot
empirically verify the historical edge of this exact setup in GRAB.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=GRAB, lookback=252 | IV30d 44.0%, %ile 37.9%, z -0.46, NORMAL |
| `mcp__uw-pp__historical_vrp` | symbol=GRAB, realised=30d | VRP +14.1%, PREMIUM_SELLING regime |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=GRAB, days=90 | NET -$6.28M BEARISH |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=GRAB, lookback=20 | z -0.16, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | symbol=GRAB, days=30, dte_max=45 | POSITIVE all 19 days, ZGL stable, 0 flips |
| `mcp__uw-pp__historical_oi_trend` | symbol=GRAB, days=30, top_n=10 | 4 consecutive build days, +5,519 today |
| `mcp__uw-pp__historical_trend` | symbol=GRAB, days=30 | 26 bearish / 4 bullish flow days, price -10% |
| `mcp__uw-pp__historical_signal_backtest` | signal_type=dark_pool_accumulation, lookback=20, top_n=25 | 0 results (no pattern library) |

## Tool errors

(none — signal_backtest empty is informational, not an error)

## Verdict for downstream phases

- **Bias from this phase:** **NET BEARISH HISTORICALLY, but TODAY is a
  candidate turning point** (first credible accumulation signal in 30
  sessions). Tactical read: TURN-SETUP, not confirmed reversal.
- **Volatility regime:** PREMIUM_SELLING (VRP +14%) — favor CREDIT
  structures (put credit spreads, covered calls) over debit structures.
- **Conviction on EDGE-positivity of the today signal:** 2/5 — the
  backtest tool returned 0 results so we cannot historically validate;
  combined with 26/30 bearish days, the prior is against.
- **Three specific data points for phase-9:**
  1. IV percentile **37.93%** + VRP **+14.1%** → premium-selling structures
     preferred [HIST:iv_percentile_zscore, HIST:vrp].
  2. **90d net premium flow -$6.28M BEARISH** → conviction CAP on
     directional long; size moderate, not aggressive
     [HIST:cumulative_premium_flow].
  3. **30d range: $3.47 (low) → $3.91 (high), -10% trend**
     [HIST:historical_trend] → use $3.47 as recent support reference;
     break of $3.47 reasserts the bearish trend.
- **Open questions:**
  - Phase-7 `insights_price_vs_flow` should flag the divergence between
    today's dark-pool accumulation and the 90d net-bearish premium flow.
  - Phase-7 `insights_institutional_accumulation` will be the tiebreaker
    on whether to read today as a regime change or a one-off.
  - Phase-6 catalyst calendar must identify what drove the May 5–11
    bullish-flow cluster (those were the only 4 bullish days; a similar
    catalyst recurring would resolve the turn-setup).
