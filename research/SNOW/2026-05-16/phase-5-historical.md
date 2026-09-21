# Phase 5 — Historical Context & VRP

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

SNOW is in a **HIGH-IV, PREMIUM-SELLING regime that just regime-flipped to long-gamma 1-2 days ago**. IV30 = 86.8% sits at the **92nd percentile** of the trailing year (z = +1.30); realized vol = 73.5%, giving VRP = **+13.3%** (favor selling, not buying, premium). The 26-day cumulative options premium flow is BULLISH (+$59.7M net) but only **5% net of $1.1B gross** — a modest skew, not a runaway. P/C ratio has collapsed from extreme put-heavy readings in mid-March (P/C 8.04 on 3/19) to extreme call-heavy today (P/C 0.23, z = -1.59) — a complete sentiment regime change in 2 months. **The bullish_flow signal backtest over the last 5d shows just a 20% win rate with avg move -1.07%** — meaning today's bullish-flow signature has been a CONTRARIAN fade lately. OI has built for 20 consecutive days (+257k contracts since 3/13). GEX has quadrupled from $1.25B (5/14) to $4.83B (5/15) — a brand-new, fragile long-gamma regime.

## Key signals

- **IV at 92nd percentile, z = +1.30** [HIST:iv_percentile_zscore]: current IV30 = 86.8% is HIGH_IV vs trailing 252d. Premium is rich.
- **VRP = +13.3% (PREMIUM_SELLING)** [HIST:vrp]: IV30 86.8% vs RV30 73.5%. Sellers of premium have positive expected edge here.
- **Bullish-flow backtest win rate = 20%, avg move -1.07%** [HIST:signal_backtest]: today's signature has FAILED 8 of 10 times across the recent universe. Treat phase-1's bullish bias as contrarian-risk.
- **P/C z-score = -1.59** [HIST:pc_ratio_zscore]: 0.23 today vs 20d mean 0.60. Sentiment regime change from put-heavy March → call-heavy May. Not yet extreme, but moving fast.
- **GEX 4x explosion** [HIST:gex_time_series]: 5/13 $665M → 5/14 $1.25B (flip POSITIVE) → 5/15 $4.83B. Long-gamma regime is **2 days old, structurally fragile**; the only prior intra-window flip (4/29→4/30) reverted next day.

## Detailed findings

### IV regime (percentile + z-score + VRP)

[HIST:iv_percentile_zscore]:
```
current_iv30d: 86.83%
iv_percentile: 92
iv_zscore:     +1.305
regime:        HIGH_IV
dates_used:    25 (252-day lookback)
```

[HIST:vrp]:
```
iv30d:           86.83%
realized_vol30:  73.53%
vrp:             +13.30%
regime:          PREMIUM_SELLING
interpretation: Options pricing more vol than realised — favour premium selling.
```

The reading is clear: **selling premium has a positive theoretical edge**. This is reinforced by the structural setup from phase-4 (positive GEX, mean-reverting tape).

**IV30 trajectory (most recent 10 sessions, from historical_trend [HIST:trend]):**

| Date | Close | IV30 | IV rank |
|---|---|---|---|
| 2026-05-15 | $157.625 | 86.83% | 97.08 |
| 2026-05-14 | $150.76 | 85.36% | 94.54 |
| 2026-05-13 | $152.37 | 85.97% | 95.59 |
| 2026-05-12 | $151.98 | 82.31% | 89.34 |
| 2026-05-11 | $151.50 | 83.08% | 90.65 |
| 2026-05-08 | $152.33 | 87.68% | 97.47 |
| 2026-05-07 | $153.72 | 88.56% | **100.00** |
| 2026-05-06 | $139.74 | 76.08% | 86.25 |
| 2026-05-05 | $141.67 | 77.32% | 88.88 |
| 2026-05-04 | $144.21 | 77.78% | 89.43 |

IV rank peaked at 100 on 5/7 and has stayed at 89-97 for 7 of the last 9 sessions — **IV is bid for an event** (consistent with phase-4's earnings kink on the 5/29 expiry).

### Cumulative premium flow (90d / 26 trading days)

[HIST:cumulative_premium_flow]:
```
cumulative_bullish: $583,322,564
cumulative_bearish: $523,598,048
net_flow:           +$59,724,516
trend_direction:    BULLISH
```

Net bullish skew of **+5.4% of gross** ($59.7M / $1.10B). Bullish, yes, but **not an avalanche**. This is consistent with the phase-1 read that 5/15 was net bullish but with two-way action.

### P/C ratio z-score (sentiment extreme y/n)

[HIST:pc_ratio_zscore]:
```
current_pc_ratio:  0.23
mean_pc_ratio:     0.596
std_pc_ratio:      0.231
zscore:            -1.586
extreme:           NORMAL (just shy of -2 threshold)
```

Cross-reference [HIST:trend] P/C series:

| Date | P/C |
|---|---|
| 2026-05-15 | 0.23 |
| 2026-05-14 | 0.33 |
| 2026-05-13 | 0.33 |
| 2026-05-12 | 0.47 |
| 2026-05-11 | 0.48 |
| 2026-05-08 | 0.49 |
| 2026-05-07 | 0.48 |
| ... | ... |
| 2026-03-19 | **8.04** |
| 2026-03-18 | 2.07 |
| 2026-03-17 | 1.90 |
| 2026-03-16 | 1.87 |

In mid-March 2026, SNOW had **catastrophic put-heavy regimes** (P/C up to 8.04× normal volume on 3/19, when bullish premium was $190M vs put premium $324M). This was likely an event-driven hedging spike (Q4 earnings 3/16-3/19 timing fits prior years). By late-April / May, P/C has collapsed to 0.23-0.49 — a **complete sentiment regime change** from defensive to speculative-bullish in 8 weeks. SNOW closed at $174.20 on 3/23 then sold off to $136.07 by 4/30 (-22%), and has since rallied back to $157.63 (+15.8% off the lows). The current call-heavy P/C aligns with the rally.

**Phase-10 contradiction watch:** P/C z = -1.59 is NEAR but not AT extreme (-2 sigma). Phase 7's contrarian scanner may flag this differently than phase 1's bullish-flow conclusion.

### GEX time series (regime stability over 26 days)

[HIST:gex_time_series]:
```
days_analyzed: 26
regime_flip_dates:
  - 2026-04-29: NEGATIVE → POSITIVE (spot 140.24, ZGL 80.01)
  - 2026-04-30: POSITIVE → NEGATIVE (spot 136.07, ZGL 169.85)  ← flipped back next day!
  - 2026-05-14: NEGATIVE → POSITIVE (spot 151.26, ZGL 75.7)    ← current regime
```

The 4/29 → 4/30 flip-and-revert is the cautionary precedent: regime "flipped POSITIVE" for one day, then snapped back to NEGATIVE the very next session. The current 5/14 → 5/15 POSITIVE regime is **only 2 sessions old** and not yet proven durable.

**Total GEX trajectory:**

| Date | Spot | Regime | total_gex | ZGL |
|---|---|---|---|---|
| 2026-03-13 | 177.65 | NEGATIVE | $9.2M | 196.80 |
| 2026-03-27 | 152.57 | FULLY_NEGATIVE | -$2.4M | null |
| 2026-04-27 | 144.29 | NEGATIVE | $39.5M | 162.29 |
| 2026-05-01 | 140.64 | NEGATIVE | $115.7M | 148.00 |
| 2026-05-07 | 152.95 | NEGATIVE | $634.9M | 157.74 |
| 2026-05-13 | 152.51 | NEGATIVE | $664.9M | 157.57 |
| **2026-05-14** | **151.26** | **POSITIVE** | **$1,251M** | **75.7** |
| **2026-05-15** | **157.60** | **POSITIVE** | **$4,834M** | **154.56** |

GEX **quadrupled in 2 days** (5/13 $665M → 5/15 $4,834M). This is a structural shift, driven by massive call-heavy build (consistent with phase-3's bid-side call writes that put dealers long $billions in calls). The ZGL move from $75.70 (5/14) to $154.56 (5/15) is a healthy normalization toward spot — meaning the regime is becoming more reflective of actual positioning. Still, this is fresh; **a single-day reversion is possible** if any of the big call-write positions get unwound.

### OI trend (sustained buildup vs spike vs decay)

[HIST:oi_trend]:
```
days_analyzed:        26
consecutive_build_days: 20
overall_trend:        BUILDING
total_net_oi_change:  +257,502 contracts (26 days)
```

Top OI-build days in the window:
- 4/27: net +23,496 (big buildup day, post-3/27 vol of -230, kick off of new positioning)
- 5/11: net +19,316
- 5/4: net +16,747
- 5/14: net +15,703
- 5/15: net +12,873 (today)

The 20-day consecutive build is the most important fact: **institutional positions have been ADDED daily, not rotated**. Combined with phase-2's distributive block-tier DP, this paints a picture of **stock-side distribution overlapping with options-side accumulation** — institutions are reducing share exposure while simultaneously adding derivative exposure. Possible interpretation: **converting from shares to derivative-leveraged exposure** (cheaper carry for tail-risk hedging?), or **two separate institutional cohorts on opposite sides**.

### Multi-day trend table (key columns from [HIST:trend])

| Date | Close | Flow dir | Net flow | IV rank | P/C |
|---|---|---|---|---|---|
| 2026-05-15 | 157.62 | bullish | +$984k | 97.08 | 0.23 |
| 2026-05-14 | 150.76 | bullish | +$196k | 94.54 | 0.33 |
| 2026-05-13 | 152.37 | bearish | -$2.58M | 95.59 | 0.33 |
| 2026-05-12 | 151.98 | bearish | -$3.14M | 89.34 | 0.47 |
| 2026-05-11 | 151.50 | bullish | +$857k | 90.65 | 0.48 |
| 2026-05-08 | 152.33 | bearish | -$2.60M | 97.47 | 0.49 |
| 2026-05-07 | 153.72 | bullish | +$5.47M | 100.00 | 0.48 |
| 2026-05-06 | 139.74 | bearish | -$491k | 86.25 | 0.52 |
| 2026-05-05 | 141.67 | bearish | -$292k | 88.88 | 0.66 |
| 2026-05-04 | 144.21 | bullish | +$1.92M | 89.43 | 0.45 |
| 2026-05-01 | 141.00 | bullish | +$2.12M | 81.09 | 0.46 |
| 2026-04-30 | 136.32 | bullish | +$2.99M | 85.29 | 0.68 |
| 2026-04-29 | 141.22 | bearish | -$1.78M | 86.05 | 0.63 |
| 2026-04-28 | 142.56 | bullish | +$1.10M | 82.21 | 0.47 |
| 2026-04-27 | 144.25 | bullish | +$3.68M | 88.04 | 1.02 |
| 2026-03-27 | 152.80 | bearish | -$921k | 55.50 | 1.30 |
| 2026-03-26 | 162.33 | bullish | +$8.65M | 46.50 | 0.78 |
| 2026-03-19 | 175.40 | bullish | +$51.5M | 39.05 | **8.04** |

Counts over 26 days: **15 bullish days vs 11 bearish days** — mild bullish lean. But the largest negative-flow day was 3/18 (-$40.9M, IV rank 39.99) — that was the SELLOFF that took SNOW from $175 to $136. The current rally has been backed by smaller, less-conviction flows.

### Signal backtest (bullish_flow over last 5d)

[HIST:signal_backtest] (signal_type=bullish_flow, lookback_days=5, top_n=20):

```
total_signals: 10
win_rate:      20.0%
avg_move_pct: -1.07%
```

Detailed results:

| Ticker | Signal date | Price on signal | Price after 5d | Δ% | Direction |
|---|---|---|---|---|---|
| TSLA | 2026-05-13 | $445.27 | $422.24 | -5.17% | down |
| NVDA | 2026-05-13 | $225.83 | $225.32 | -0.23% | down |
| GOOGL | 2026-05-13 | $402.62 | $396.78 | -1.45% | down |
| META | 2026-05-13 | $616.63 | $614.23 | -0.39% | down |
| QQQ | 2026-05-13 | $714.71 | $708.93 | -0.81% | down |
| NVDA | 2026-05-12 | $220.78 | $225.32 | **+2.06%** | **up** |
| QCOM | 2026-05-12 | $210.31 | $201.49 | -4.19% | down |
| CNC | 2026-05-12 | $59.31 | $58.27 | -1.75% | down |
| AAPL | 2026-05-12 | $294.80 | $300.23 | **+1.84%** | **up** |
| UNH | 2026-05-12 | $396.39 | $393.85 | -0.64% | down |

Only **NVDA (5/12) and AAPL (5/12)** worked. The signal failed for TSLA, NVDA (5/13), GOOGL, META, QQQ, QCOM, CNC, UNH. SNOW itself was not in the recent signals universe (probably because it just printed its bullish signal today, 5/15).

This is the single most important fact in phase-5: **the very pattern fired today on SNOW has historically been a contrarian fade signal**. Phase 9 must downgrade conviction or invert the trade based on this.

### Caveat on signal universe

The 5-day window is small (10 signals) and recent (5/12-5/13). A 60-day lookback might give a different read. Treat the 20% win rate as **directional warning**, not statistical certainty. But the AVG MOVE -1.07% is the more informative number — even when the move was right (2 of 10), the magnitude was small (+2.06%, +1.84%), and the failures were larger (-5.17%, -4.19%). Risk-reward on the bullish-flow signal is currently negative.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol=SNOW, lookback=252 | IV30 86.8%, percentile 92, z +1.30, HIGH_IV |
| `mcp__uw-pp__historical_vrp` | symbol=SNOW, window=30 | VRP +13.3%, PREMIUM_SELLING |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol=SNOW, days=90 | net +$59.7M BULLISH out of $1.10B gross |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol=SNOW, lookback=20 | PC 0.23, z -1.59, NORMAL extreme tier |
| `mcp__uw-pp__historical_gex_time_series` | symbol=SNOW, days=30, dte_max=45 | 3 flips; current POSITIVE since 5/14; GEX 4x explosion |
| `mcp__uw-pp__historical_oi_trend` | symbol=SNOW, days=30, top_n=10 | 20-day build streak, +257k contracts net |
| `mcp__uw-pp__historical_trend` | symbol=SNOW, days=30 | 15 bullish / 11 bearish days; IV rank 89-97 cluster |
| `mcp__uw-pp__historical_signal_backtest` | signal_type=bullish_flow, lookback=5, top_n=20 | **win_rate 20%, avg_move -1.07%** |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime:** **RICH (HIGH_IV)**. IV at 92nd percentile, VRP +13.3% — favors **credit / premium-selling structures over debit structures** for any directional view.
- **Premium-buying vs selling environment:** **SELL premium** is theoretically edge-positive. Phase-1's debit call buys (e.g. $145C Jun-26-26 paid $23.60 at 80.9% IV) are paying very rich premium relative to historical realized.
- **Conviction that today's bullish signal is HISTORICALLY EDGE-POSITIVE: 1/5 (LOW).** Backtest win rate 20% over recent window. Phase 9 should consider FADING the bullish flow rather than following it, or at minimum size very small if going long.
- **Three specific data points for phase-9:**
  1. **IV percentile = 92** — too rich to buy debit structures comfortably; if expressing a bullish view, use call spreads (sell premium overhead) rather than naked calls.
  2. **VRP = +13.3%** — short-vol structures (e.g., short strangle through the 5/29 earnings event) have positive theta and historical edge.
  3. **Bullish_flow win rate = 20% over 5d** — the highest-conviction historical signal in the entire phase 5 read is the **contrarian fade**. Treat phase-1 as a setup for a SHORT or for a defined-risk premium-sell, not a debit long.
- **Open questions:**
  - The 5/29 IV kink from phase-4 + the IV rank 89-97 cluster of recent days = earnings is imminent. Confirm SNOW Q1 FY27 report date in phase-6 (likely 5/27-5/29 window per term structure).
  - Is the bullish_flow signal universe biased toward late-cycle FOMO names? If yes, the 20% win rate is regime-specific, not signal-specific. But still applies to the current regime.
  - The 4/29 → 4/30 GEX flip-and-revert pattern: is the current 5/14 → 5/15 POSITIVE flip going to revert when 5/15 expiry OI burns off and the 5/22/5/29 chain takes over?
