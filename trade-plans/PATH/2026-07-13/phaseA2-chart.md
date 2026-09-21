# Phase A2 — Chart, Technicals & Patterns

**Tool call:** `python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker PATH --date 2026-07-13 --lookback 540` → exit 0, `available: true`, source **yfinance** (373 daily sessions). Raw output: `chart.json` (this dir). No errors.

## Summary

PATH at **11.85** is three weeks into a +24.7% up-leg off double equal lows at
9.88/9.87 (Jun-18/Jun-26) [CHART:swing_low], holding a shallow pullback from the
Jul-7 swing high 12.31 [CHART:swing_high]. Momentum confirms (MACD bullish, RSI
60.9, last volume 1.47× the 20-day average) but the 60-day structure is still
`range_or_transition`, price sits under a heavy confluence ceiling first at
**12.34–12.35** and then at **12.95–13.28**, and **no chart pattern is detected**
by the engine — this is a trend-transition base, not a named setup.

## Key signals (tagged)

- Spot 11.85 > sma20 10.92 > sma50 10.91 but **below sma200 12.95** (−8.5%); ma_stack `mixed` [CHART:ma_stack]
- ema9 11.51 > ema21 11.20, price above both — short-term momentum stack intact [CHART:ema9]
- RSI14 **60.94** (neutral, upper half — room before overbought) [CHART:rsi14]
- MACD histogram **+0.124, bullish** [CHART:macd]
- ATR14 **0.65 (5.84%/day)** — a high-vol name; stops must respect this [CHART:atr14]
- Last-session volume **90.8M vs 61.9M avg20 = 1.47×** [CHART:volume]
- 52w: −38.6% off the 19.29 high, +26.3% above the 9.38 low [CHART:52w]
- 60-day regression **+0.12%/day, direction up**, but `market_structure: range_or_transition` [CHART:trend]

## Detailed findings

### Trend / market structure

The June sequence: 13.20 spike high (Jun-1) → sell-off to **9.88 (Jun-18)** and a
retest at **9.87 (Jun-26)** — equal lows to the cent-level (±0.1%) — then an
impulsive rally to **12.31 (Jul-7)**, which took out the Jun-15 interim high 11.08
(first higher high), and a shallow pullback now holding 11.85. Since late June the
tape prints HL→HH; the engine still labels the 60-day window `range_or_transition`
because the window includes the full down-up round trip. Read: **transition from
downtrend to range/early-uptrend — bullish-leaning, not yet a confirmed uptrend.**
Divergence to note: 60-day regression is up, but price remains below the sma200
(12.95), so the larger frame is still repair, not trend.

### Momentum / volatility

MACD bullish, RSI 60.9 with headroom, and the pullback from 12.31 has held above
ema9 (11.51). Bollinger: 9.56 / 12.28 — spot is in the upper half; the first
resistance (12.34) sits right at the upper band, so a push through it would need
a band-walk / volatility expansion. ATR 0.65 → a 1-ATR stop from spot is ~11.20,
1.5-ATR ~10.88 [CHART:stops].

### Support / resistance — and confluence with the flow substrate

Ranked chart levels, flagged where they line up with deep-dive dealer/DP levels
(the tradeable ones):

| Zone | Chart evidence | Flow/dealer confluence | Read |
|------|----------------|------------------------|------|
| **11.80–11.85** | spot; pullback holding above ema9 11.51 | **$678.8M DP shelf @ 11.80** [DP:price_levels] | the defended level — the long trigger zone. NOTE: the shelf sits *above* the chart's structural supports — the DP buyer is defending higher than the chart requires |
| **11.42 / 11.29** | supports, 4 and **6** touches [CHART:support_resistance] | 0.382 retrace of the 9.87→12.31 leg ≈ 11.38 | first structural net under the shelf |
| **11.05 / 11.00** | support, 4 touches (last 06-15) | **largest OI pin $11.00** [OI:pin] | the magnet if the shelf fails |
| **10.48–10.69** | support 10.48 (4 touches) | fib 0.236 (10.69) [CHART:fib_0.236]; $10 put wall below [OI:put_wall] | last support before the 9.87 lows |
| **12.28–12.35** | resistance **12.34 (5 touches, last 07-07)** + BB upper 12.28 | **fib 0.500 = 12.35** [CHART:fib_0.500] | first ceiling; the Jul-7 rejection point. Break+hold converts range→uptrend |
| **12.95–13.28** | sma200 12.95 + resistance 13.28 (4 touches, Jun-1 spike) | **$13 gamma wall** [STRUCT:gex] + fib 0.618 = 13.09 [CHART:fib_0.618] | the major supply zone — 4-way confluence; realistic swing target and the fade zone |
| **13.56 / 15.44** | resistances (5 and 4 touches, 2025–Jan 2026) | fib 0.786 = 14.15 | beyond the horizon unless the squeeze fires |

### Fibonacci

Dominant swing: **15.50 → 9.20 down-swing**; retracements 0.382 = 11.61 (roughly
where spot consolidates), **0.500 = 12.35** (coincides with the 5-touch 12.34
resistance — the key near ceiling), **0.618 = 13.09** (inside the 12.95–13.28
supply zone with the sma200 and the $13 gamma wall). Extensions (7.49 / 5.31)
are downside-swing extensions — irrelevant unless the base fails badly.

### Patterns (engine: pattern-rubric.md discipline)

**None detected.** All six detectors (flag, head-&-shoulders, double, triangle,
cup-&-handle, Elliott) returned `detected: false`; `patterns_detected: []`.
Per the rubric: confidence `none` — do not force a pattern onto noise.

*Manual observation (structural fact, NOT a pattern call):* the Jun-18/Jun-26
equal lows 9.88/9.87 form a double-bottom-**like** base, but no intervening
neckline pivot registered between the two lows, which is why the detector
(correctly) rejected it. No measured target is claimed from it. Its value is as
**invalidation architecture**: two tested, defended lows at ~9.87.

### Elliott wave

`detected: false` — "pivot sequence not cleanly alternating." **No working count
is reportable.** Targets in this plan come from level/fib confluence only.

## Verdict

- **Chart bias: bullish (moderate), conviction 3/5.** Up-leg with momentum
  confirmation and a defended base, capped by unbroken overhead supply and an
  unconfirmed larger structure (below sma200, `range_or_transition`).
- **Three most important levels:**
  1. **11.80** — DP-shelf/spot defense zone (chart net 11.42/11.29 just below)
  2. **12.34–12.35** — 5-touch resistance + fib 0.500 + BB upper: the range→trend trigger
  3. **12.95–13.28** — sma200 + $13 gamma wall + fib 0.618 + 4-touch resistance: target/fade zone
- **Most credible pattern: none** (engine-clean). The tradeable structure is the
  *base-and-transition*: equal lows 9.87/9.88 → HH 12.31 → shallow hold above the
  DP shelf. Confirmation trigger for the next leg: **daily close > 12.35 on
  >1.2× avg volume**; structural invalidation: **daily close < 11.29** (6-touch
  support; the deep dive's tighter 11.60 signal-invalidation sits above it).
- L-0001 note for A3: this is **flow-leads** (DP shelf defended at/above spot),
  not a chart-leads pattern breakout — but if entry is taken on the 12.35 break
  instead of the shelf-hold, L-0001's break-confirmation + starter-size rule applies.
