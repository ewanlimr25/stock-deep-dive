# Phase 5 — Historical Context & VRP

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The historical view re-frames every prior phase. KWEB just lived through
a **+5% pop into $30.59 on 2026-05-13** followed by a **−7.6% slide to
today's $28.28 close in 5 sessions** [HIST:historical_trend] — *exactly
the window of the 5-day bearish sweep persistence* flagged in
phase 1 [FLOW:sweep_persistence]. IV30 has compressed from a recent
peak of 39.0% (IV rank 88.8 on May 13) to **30.2% / IV rank 45.3 today**
[HIST:historical_trend / iv_percentile_zscore] — a textbook post-spike
vol-crush. The IV30d sits at **0th percentile / z-score -1.82** in the
available 27-day lookback window [HIST:iv_percentile_zscore], and **VRP
= -3.92% (IV 30.2% vs realized 34.2%)** [HIST:historical_vrp] — IV
**below realised vol = a premium-BUYING regime** (debit structures
asymmetric). GEX history shows the dealer regime flipped **from
NEGATIVE to POSITIVE on 2026-05-13** (the high day) and has held
positive for 5 consecutive sessions [HIST:historical_gex_time_series].
Cumulative 90-day net premium flow is **MIXED ($4.14M net bullish on
$200M each side)** [HIST:historical_cumulative_premium_flow] — no long-
window directional accretion. PCR z-score is **-0.46 (NORMAL)**
[HIST:historical_pc_ratio_zscore]. Bearish-flow signal backtest over
the trailing 20 days yielded **win_rate 100% (N=8, avg next-20d move
-4.45%)** [HIST:historical_signal_backtest] — but the sample is
SMALL-N and dominated by large-caps (MU, MSTR, TSLA, NVDA, NDX, SPY,
GLD), not KWEB itself.

## Key signals

- **IV30d at 30.24%, IV percentile 0, z-score -1.82 in 252d window**
  [HIST:iv_percentile_zscore] → LOW_IV regime; cheap optionality.
- **VRP = -3.92%, regime FAIR but value negative** — IV below realised
  → debit / premium-buying structures have an edge
  [HIST:historical_vrp].
- **GEX regime flipped POSITIVE on 2026-05-13** and has held 5 sessions
  [HIST:historical_gex_time_series]. ZGL has dropped from $30+ in
  March-April to **$23.81 today**, a ~$6 widening of the long-gamma
  envelope. The regime swing is recent and may not be stable.
- **OI buildup: 20 consecutive build days** [HIST:historical_oi_trend]
  → sustained institutional engagement with the chain, not a one-day
  spike. Today's net OI Δ +18,100 over 236 contracts adding vs 55
  shrinking — broad-based addition.
- **Bearish-flow signal backtest: 100% win rate, avg -4.45% next 20d
  (N=8)** [HIST:historical_signal_backtest] — but SMALL sample and the
  population skews large-cap/index. Use as a **weak positive prior**
  for bearish thesis, NOT a high-confidence directional edge.

## Detailed findings

### IV regime [HIST:iv_percentile_zscore / historical_vrp]

| Metric | Value |
|--------|-------|
| Current IV30d | 30.24% |
| IV percentile (252d lookback, dates_used=27) | **0** |
| IV z-score | **-1.82** |
| Regime | LOW_IV |
| Realised vol (30d) | 34.17% |
| **VRP** | **-3.92%** |
| VRP regime | FAIR (tool label) — value-negative |

KWEB IV is at the **bottom of its 1y range** in the available window;
the tool warns only 27 dates were usable in the 252-day lookback (due
to data gaps in March-April). Realised vol is RUNNING ABOVE IV — IV is
cheap relative to what's actually being delivered. This argues
**debit structures** (long puts, long calls, long straddles) over
**credit structures** (short premium). The Dec '26 29-strike straddle
buyer from phase 1 [FLOW:top_premium_trades] is on the *correct side*
of the VRP signal.

### Cumulative premium flow (90d) [HIST:historical_cumulative_premium_flow]

| Field | Value |
|-------|-------|
| Cumulative bullish premium | $201,728,771 |
| Cumulative bearish premium | $197,584,404 |
| Net flow | **+$4,144,367** |
| Trend direction | **MIXED** |
| Sessions covered | 28 (gap-corrected) |

A net $4M tilt on $200M each side = **0.5% imbalance**, statistically
indistinguishable from random over 90 days. There is no "stealth
institutional build" signature in either direction over the long
window. The bearish persistence from phase 1 is a **5-day burst** on
top of a flat 90-day base, not a sustained accretion.

### P/C ratio z-score [HIST:historical_pc_ratio_zscore]

| Field | Value |
|-------|-------|
| Current PCR | 0.16 |
| Mean PCR (20d) | 0.2639 |
| Std PCR | 0.2238 |
| Z-score | -0.464 |
| Extreme classification | **NORMAL** |

PCR is below trailing mean (less put activity than usual) but well
within 1 SD. No sentiment extreme. Note that PCR 0.16 itself is low
in absolute terms — KWEB is a call-skewed product, consistent with
phase 4's complacent skew (calls richer than puts) [STRUCT:term_skew].

### GEX time series — 30-session regime trajectory [HIST:historical_gex_time_series]

Regime flip dates (most recent 5):

| Date | From | To | Spot | ZGL | ZGL Δ |
|------|------|-----|------|------|-------|
| 2026-05-04 | NEGATIVE | POSITIVE | $28.71 | $24.00 | -4.79 |
| 2026-05-05 | POSITIVE | NEGATIVE | $28.64 | $30.50 | +6.50 |
| 2026-05-06 | NEGATIVE | POSITIVE | $29.56 | $28.92 | -1.58 |
| 2026-05-12 | POSITIVE | NEGATIVE | $29.01 | $29.50 | -0.02 |
| 2026-05-13 | NEGATIVE | POSITIVE | $30.53 | $24.50 | -5.00 |

Total GEX trajectory:
- March 13–27: NEGATIVE regime, total GEX $1.6B–6B, ZGL $30-32.
- April 27 – May 5: NEGATIVE → toggling, total GEX expanding from $7B
  to $26B.
- May 6 – May 11: POSITIVE regime forms, total GEX grows from $114B
  to $152B (May 7 peak).
- May 12: brief NEGATIVE flip on dip to $29.01.
- **May 13: total GEX explodes to $280.9B** as KWEB pushes to $30.53
  — extreme call concentration, dealers heavily long gamma at the
  high.
- May 14–19: total GEX bleeds down from $141B → $30.5B as the chain
  unwinds with the price.

The picture: KWEB ran into peak dealer long-gamma at $30.50 (May 13),
which capped further upside via dealer selling. Since then dealers
have been unwinding their long-gamma exposure (call OI closes, see
phase 3 −35K 33C), and the ZGL has *fallen* from $24.50 to $23.81,
widening the positive-gamma envelope. **Recent regime stability: 5
sessions** — modest history, not stable enough to assume permanence.

### OI trend [HIST:historical_oi_trend]

- **Consecutive build days: 20** (continuous OI accretion).
- Today: 236 contracts with OI increases, 55 with decreases, net OI Δ
  **+18,100** across the chain.
- Top builds (per phase 3 detail): 28P May 29 +11,461, 30.5C May 29
  +7,449, Jan'27 15P +6,929, 29.5C May 29 +6,008, Jun 29C +2,925.

20-day build is a *sustained engagement* signature — institutional
desks are actively in the name even as price gyrates. Combined with
the MIXED 90-day premium flow, this looks like **active two-way
positioning**, not directional accumulation or distribution.

### Multi-day historical trend (28 sessions) [HIST:historical_trend]

| Date | Close | Flow dir | IV30d | IV rank | PCR | Net flow |
|------|-------|----------|-------|---------|-----|----------|
| 2026-05-19 | 28.28 | bearish | 0.302 | 45.31 | 0.16 | -$226K |
| 2026-05-18 | 28.06 | bearish | 0.318 | 51.96 | 0.19 | -$1.15M |
| 2026-05-15 | 28.18 | bearish | 0.337 | 63.83 | 0.15 | -$2.24M |
| 2026-05-14 | 29.20 | bullish | 0.367 | 76.96 | 0.16 | +$4.63M |
| **2026-05-13** | **30.59** | **bullish** | **0.390** | **88.80** | **0.05** | **+$8.70M** |
| 2026-05-12 | 29.15 | bullish | 0.339 | 62.83 | 0.21 | +$17K |
| 2026-05-11 | 29.59 | bullish | 0.344 | 65.40 | 0.12 | +$818K |
| 2026-05-08 | 29.52 | bullish | 0.342 | 63.09 | 0.07 | +$6.09M |
| 2026-05-07 | 29.52 | bearish | 0.354 | 70.37 | 0.15 | -$1.93M |
| 2026-05-06 | 29.76 | bullish | 0.343 | 64.88 | 0.10 | +$8.44M |
| 2026-05-05 | 28.54 | bearish | 0.335 | 56.65 | 0.74 | -$606K |
| 2026-05-04 | 28.59 | bullish | 0.317 | 51.83 | 0.06 | +$649K |
| 2026-05-01 | 28.78 | bullish | 0.314 | 49.85 | 0.08 | +$489K |
| 2026-04-30 | 28.80 | bearish | 0.316 | 45.07 | 0.24 | -$1.51M |
| 2026-04-29 | 28.01 | bullish | 0.313 | 49.47 | 0.35 | +$42K |
| 2026-04-28 | 28.11 | bullish | 0.319 | 52.43 | 0.38 | +$1.38M |
| 2026-04-27 | 28.36 | bearish | 0.319 | 52.42 | 0.33 | -$796K |
| 2026-03-27 | 27.91 | bearish | 0.391 | 32.64 | 0.30 | -$2.39M |
| 2026-03-26 | 28.20 | bearish | 0.371 | 28.97 | 0.90 | -$8.75M |
| 2026-03-25 | 29.14 | bullish | 0.333 | 21.89 | 0.23 | +$1.25M |
| 2026-03-24 | 28.28 | bullish | 0.352 | 25.40 | 0.46 | +$286K |
| 2026-03-23 | 28.44 | bearish | 0.368 | 28.39 | 0.89 | -$12.57M |
| 2026-03-20 | 28.23 | bullish | 0.356 | 26.08 | 0.48 | +$265K |
| 2026-03-19 | 29.09 | bearish | 0.365 | 27.28 | 1.32 | -$2.51M |
| 2026-03-18 | 29.45 | bearish | 0.368 | 28.46 | 0.20 | -$173K |
| 2026-03-17 | 30.42 | bullish | 0.355 | 26.00 | 0.37 | +$2.49M |
| 2026-03-16 | 30.64 | bullish | 0.358 | 26.47 | 0.25 | +$1.24M |
| 2026-03-13 | 30.16 | bullish | 0.396 | 33.60 | 0.27 | +$2.19M |

Pattern:
- Bullish_days: 16 / Bearish_days: 12 over 28 sessions — count tilt is
  modestly bullish.
- **Latest run: 5 consecutive bearish-flow days (May 13 bullish was
  the inflection), price drawdown $30.59 → $28.28 (−7.6%)**.
- Volume / call premium peaked May 13 at $61.4M call premium (PCR
  collapsed to 0.05) — that was the climactic call-buying day right
  before the reversal. **Classic exhaustion top in the chain.**
- IV30 peaked on May 13 (39.0%) and has compressed -22% since (now
  30.2%). The IV bleed is consistent with the GEX-positive dealer-
  long-gamma regime suppressing realised vol.
- March data: a similar mini-cycle — $30.64 high March 16 → $27.91 low
  March 27 = -8.9% drawdown. Two prior 8% drawdown episodes inside the
  available window.

### Bearish-flow signal backtest [HIST:historical_signal_backtest]

Tool ran market-wide over the trailing 20d:

| Date | Ticker | Signal price | Price +20d | Move |
|------|--------|--------------|------------|------|
| 2026-05-15 | MU | $725.29 | $698.74 | -3.66% |
| 2026-05-15 | MSTR | $177.56 | $164.63 | -7.28% |
| 2026-05-15 | TSLA | $422.35 | $404.11 | -4.32% |
| 2026-05-15 | NVDA | $225.49 | $220.61 | -2.16% |
| 2026-05-14 | NDX | 29,580 | 28,818 | -2.57% |
| 2026-05-14 | SPY | $748.17 | $733.73 | -1.93% |
| 2026-05-14 | MU | $776.01 | $698.74 | -9.96% |
| 2026-05-14 | GLD | $427.21 | $411.50 | -3.68% |

- **Total signals: 8**
- **Win rate: 100%**
- **Avg next-20d move: -4.45%**

Caveats: (i) sample size N=8 is small; (ii) **KWEB itself is NOT in
the backtest population**; (iii) the firings are concentrated in
large-caps and indices (broad-market risk-off bias). This is a *weak
positive prior* for the bearish-flow read — the type of signal that's
been working market-wide. **It does not say "KWEB will drop 4.45%"**,
it says "when this signature has fired recently, the market has
delivered downside follow-through about 4-5% on average over 20 days".

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `historical_iv_percentile_zscore` | `{symbol: KWEB, lookback-days: 252}` | IV 30.24%, percentile 0, z -1.82, regime LOW_IV |
| `historical_vrp` | `{symbol: KWEB, realised-window-days: 30, date: 2026-05-19}` | VRP -3.92%, regime FAIR |
| `historical_cumulative_premium_flow` | `{symbol: KWEB, days: 90}` | Net +$4.14M, MIXED |
| `historical_pc_ratio_zscore` | `{symbol: KWEB, lookback-days: 20}` | PCR 0.16, z -0.46, NORMAL |
| `historical_gex_time_series` | `{symbol: KWEB, days: 30, dte-max: 45}` | 5 regime flips; current POSITIVE since 2026-05-13 |
| `historical_oi_trend` | `{symbol: KWEB, days: 30, top-n: 10}` | 20 consecutive build days, net +18,100 today |
| `historical_trend` | `{symbol: KWEB, days: 30}` | 16 bullish / 12 bearish days; latest 5 bearish |
| `historical_signal_backtest` | `{signal-type: bearish_flow, lookback-days: 20, top-n: 20}` | win 100%, avg -4.45% (N=8, KWEB not in sample) |

## Tool errors

None.

## Verdict for downstream phases

- **Volatility regime:** **CHEAP** — IV30 30.2% at 0th percentile of
  available 1y window, sitting BELOW 30d realised (34.2%). VRP -3.92%.
- **Premium-buying vs premium-selling environment:** **PREMIUM-BUYING**
  — debit structures (long puts, long calls, long straddles) carry
  positive expectancy versus realised vol. This *directly contradicts*
  the institutional behaviour we observed in phase 3 (28P sold-to-open
  = premium SELLING). The tension means either (a) institutions
  believe forward realised vol will compress further (their put-write
  is correct), or (b) they're harvesting premium against an underlying
  position and don't care about pure vol edge. Phase 10 audit must
  flag.
- **Conviction (today's signal historically edge-positive):** 3 / 5.
  The 100% bearish-flow win rate (N=8) is encouraging but underpowered
  for KWEB-specific inference. Weighted against IV at 0th percentile
  (vol-buy edge) and the +5 sessions of POSITIVE GEX (range-suppress),
  net is medium conviction.
- **Three specific data points for phase 9:**
  1. **IV30d 30.24%, IV percentile 0, VRP -3.92%** — cheap optionality
     → favor debit structures over credit.
  2. **GEX regime flipped POSITIVE on 2026-05-13 with peak GEX $280.9B**
     — recent inflection; not yet a stable, multi-week regime. Stop
     levels should respect ZGL $23.81 and the negative-GEX cliff at
     $27.
  3. **Bearish-flow signal market-wide win rate 100%, avg -4.45% over
     20d (N=8)** — weak-positive prior for a bearish KWEB bias.
- **Open questions:**
  - The **VRP-says-buy-premium vs phase-3-says-sell-premium**
    contradiction is the single biggest unresolved analytical
    question. Phase 7 insights composite and phase 8 PM voice should
    resolve.
  - May 13 was an extreme-call-buying day (PCR 0.05, call premium
    $61M, total GEX peak $281B) followed by a 7.6% drop in 5
    sessions. This is a CLASSIC blow-off-top pattern. Phase 7 / 8
    should consider whether the *next leg* is mean-reversion DOWN
    (continuation), or whether the sell-off is complete and a base is
    forming around the $28 floor (the put-write thesis from phase 3).
