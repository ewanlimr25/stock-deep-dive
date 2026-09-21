# Phase A2 — Chart, Technicals & Patterns — MU — 2026-06-26

Tool: `python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker MU --date 2026-06-26 --lookback 540`
→ `chart.json` (available:true, source yfinance, 372 sessions).

## Summary

MU is in a **strong, clean, but parabolic Stage-2 uptrend** sitting **exactly at
its all-time high** (spot 1213.56 = 52-wk high, **0.0% off the high**) and
**riding the upper Bollinger band** (1212.18) — i.e. fully extended, **+53.9%
above the 50-MA and +188% above the 200-MA** [CHART:sma50][CHART:sma200].
Momentum is bullish but *cooling, not euphoric* (RSI14 64.5 **neutral**, MACD
bullish) — the +15.8% earnings gap has been digested sideways rather than chased,
which is constructive for a *continuation later* but argues against *chasing now*.
**Critically: the engine confirms NO classical chart pattern** — the deep dive's
"1211-1213 double top" is a discretionary resistance read, **not** an engine-
validated reversal (per pattern-rubric I will not force it). ATR is enormous at
**$95 / 8.5%**, which dominates stop and option-width sizing.

## Key signals (tagged)

- **At/!-ATH, upper-band ride** — spot 1213.56 = high_52w; bb_upper 1212.18; price
  pinned to the band ceiling [CHART:bb_upper][CHART:high_52w]. Stretched.
- **Bullish MA stack, parabolic distance** — spot > ema9 1089 > sma20 1025 >
  ema21 1005 > sma50 789 > sma200 421; +188% over 200-MA [CHART:ma_stack].
- **Trend intact** — 60-day regression up +1.19%/day, `market_structure =
  uptrend_HH_HL` [CHART:trend]. Last swings: 06-03 high 1089 → 06-09 low 854 →
  new ATH 1213 (higher high, higher low) [CHART:recent_pivots].
- **Momentum cooling, not topping** — RSI14 64.5 neutral (room before 70),
  MACD_hist +2.57 bullish [CHART:rsi14][CHART:macd].
- **Volume elevated** — 82.1M vs 56.3M 20-day avg = **1.46x** [CHART:vol_vs_avg]
  (earnings-gap + chase volume; cuts both ways — could be distribution).
- **No overhead structure, thin near support** — nearest_resistance = **null**
  (blue sky above); touch-clustered support only appears far below (437↓), so
  **near-term support is MA/fib/dealer-derived, not tested price** [CHART:support_resistance].

## Detailed findings

### Trend / structure
Textbook Stage-2 uptrend: bullish stack, positive regression, HH-HL. But the
*distance* is the warning — +188% over the 200-MA and pinned to the upper
Bollinger is a **late-stage / climax-risk** posture, not an early trend. The
trend says "long bias"; the location says "not here."

### Momentum / volatility
RSI 64.5 (neutral) is the constructive surprise — a sideways post-gap digestion
reset momentum without a price drop, the classic setup for *either* a continuation
break *or* a lower-high failure. ATR14 = **$95.41 (8.53%)** → a 1-ATR daily swing
is ±$95; any stock stop tighter than ~1 ATR will be noise-stopped. Expected move
front-expiry ±3.93% (±$47, from the deep dive [CTX:implied_move]) is *less* than
1 ATR — option structures must respect this width.

### Support / resistance (ranked, near-term-relevant)
The touch-clustered S/R is useless here (all ≥64% below — the parabola is too
steep to have tested shelves nearby). The **operative near-term ladder** is
MA/fib/dealer confluence:

| Level | Type | Source |
|-------|------|--------|
| **1255** | overhead breakout line / fib swing-high anchor | [CHART:fib_swing_high] + deep-dive aggressive entry |
| **1212-1213** | spot = ATH + upper Bollinger | [CHART:high_52w][CHART:bb_upper] |
| **1134** | first pullback-buy shelf (dark-pool) | [DP:price_levels] (deep dive) — *not* a chart-touch level |
| **1024-1040** | **major confluence shelf**: sma20 1025 + fib 0.236 = 1028 + max-pain 1040 | [CHART:sma20][CHART:fib_0.236][STRUCT:max_pain] |
| **1005** | ema21 | [CHART:ema21] |
| **854 / 789** | 06-09 swing low / sma50 | [CHART:swing_low][CHART:sma50] |

**Confluence call-out:** the **1024-1040** band is where the chart (sma20, fib
0.236) and the dealer book (max-pain 1040) line up — that is the *high-value*
deeper pullback-buy zone, and the deep dive's **1052** invalidation sits just
above it (a clean "defend the shelf or the parabola round-trips" line).

### Fibonacci
Dominant swing 294.86 → 1255.00 (up) [CHART:fibonacci]. Retracements: 0.236 =
**1028** (≈ sma20/max-pain cluster — meaningful), 0.382 = 888, 0.5 = 775. A shallow
0.236 pullback is all a healthy parabola usually gives — consistent with the
1024-1040 buy shelf. Extensions: 1.272 = **1516**, 1.618 = 1848 → these are the
*measured continuation targets* if 1255 breaks (shape A4's upside, not a promise).

### Patterns
**None engine-confirmed** — flag, H&S, double-top/bottom, triangle, cup-handle
all `detected: false`; Elliott `detected: false` ("pivot sequence not cleanly
alternating") [CHART:patterns]. Honest reporting per pattern-rubric:
- The **"double top" at 1211-1255 is discretionary, confidence `low`/`none`** —
  the engine sees a *single new ATH*, not two equal tested tops with a confirmed
  neckline. Treat 1213-1255 as a **resistance/decision zone**, not a reversal
  pattern. It only becomes a tradeable top on a *failure pattern* (lower high +
  close back below ~1134); it becomes a continuation on a *close > 1255*.
- No measured bearish target is justified (no confirmed pattern → no projection).
- **Elliott:** no valid count (rules_passed n/a, not cleanly alternating) →
  contributes nothing; do not infer a "wave 5 top."

## Verdict (for A3)

- **Chart bias: BULLISH trend / NEUTRAL-to-cautious tactical.** Conviction
  **3/5** — the trend and the bullish flow *agree on direction* (so this is an
  **ALIGNED**, not divergent, flow↔chart read; L-0002's hard neutral does not
  fire), but price location is poor: at ATH, upper-band, +188% over 200-MA, no
  overhead structure, distributive dark pool. The edge is on a **pullback**, not
  at spot.
- **3 most important levels:** (1) **1255** breakout line (above = blue sky,
  aggressive-long trigger); (2) **1134** first pullback-buy shelf; (3)
  **1024-1040** major confluence support (sma20/fib0.236/max-pain) with **1052**
  the invalidation just above.
- **Most credible "pattern":** none confirmed — the operative read is a
  **parabolic uptrend at a 1213-1255 decision zone**. Confirmation triggers:
  *bull* = daily close **> 1255** on >1.2x vol (L-0001: starter until two closes
  hold); *bear/fade* = rejection + lower high then daily close **< 1134**.
