# Phase A2 — Chart, Technicals & Patterns — INTC (2026-06-27)

**Tool call:** `python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker INTC --date 2026-06-27 --lookback 540 > chart.json` → `available: true`, source `yfinance`, 373 daily sessions. All datapoints below resolve to `chart.json`.

## Summary
INTC is a **parabolic uptrend** — full bullish MA stack (spot $128.32 > sma20 119.42 > sma50 108.39 > sma200 58.23), +120% above its 200-day, only −8.95% off the $140.94 52-week high set 5 sessions ago [CHART:ma_stack]. But the near-term has gone **two-sided and stalling**: price is in a broadening/expanding-volatility range, the last push to a new high came on **below-average volume (0.73× 20-day)**, and RSI is only **neutral (56.78)** despite being near 52-week highs — a momentum non-confirmation that echoes the deep dive's price-vs-flow bearish divergence [CHART:rsi14][CHART:vol_vs_avg]. **No clean chart pattern and no valid Elliott count were detected.** Net: the *primary trend is bullish but tiring at the top of a parabola* — the chart supports fading strength back to the pin, not a trend-reversal short.

## Key signals (tagged)
- Bullish primary structure: `ma_stack = bullish_stack`, +18.39% over sma50, +120.36% over sma200 [CHART:ma_stack][CHART:sma50][CHART:sma200].
- Near-term exhaustion tells: new 52w high (141.45, 2026-06-22) on **0.73× volume** + **neutral RSI 56.78** + MACD hist only +0.481 [CHART:vol_vs_avg][CHART:rsi14][CHART:macd].
- Broadening range (manual, low conf): highs 132.75→126.64→**141.45** with lows 102.40→**98.33** = higher-high *and* lower-low = volatility expansion / distribution risk [CHART:recent_pivots].
- High realized vol: ATR14 **9.97 (8.42%)** — stops must be wide; informs option width [CHART:atr14].
- Engine touch-based S/R clusters are **stale** (all $19–43, last touched 2025/early-2026, −67% to −85% away) — artifacts of the year-long base; ignore for a $128 trade [CHART:support_resistance].

## Detailed findings

### Trend / market structure
- 60-day regression: slope **+1.06%/day, direction up**, but `market_structure = range_or_transition` — the engine sees the huge zigzag (132.75 / 102.40 / 126.64 / 98.33 / 141.45 / 128.32) as a transition, not a clean trend [CHART:trend].
- MA stack fully bullish and steeply extended; ema9 128.46 ≈ spot (price sitting on its fast EMA after the pullback) [CHART:ema9].
- Read: textbook late-stage parabola — trend intact, slope unsustainable, range broadening.

### Momentum / volatility
- RSI14 **56.78 neutral** — the pullback from 141.45 has bled the overbought condition; not yet oversold [CHART:rsi14].
- MACD **bullish** but histogram thin (+0.481) — momentum flattening [CHART:macd].
- ATR14 **9.97 / 8.42%** → 1-ATR ≈ $10 daily range. Engine stops: short 1-ATR **138.29**, 1.5-ATR **143.28**; long 1-ATR **118.35**, 1.5-ATR **113.36** [CHART:stops].
- Volume 99.2M vs 136.3M avg = **0.73×** — fading participation into the high (bearish-leaning non-confirmation) [CHART:vol_vs_avg].
- Bollinger 96.47–142.37; spot mid-upper band, room both ways.

### Support / resistance (relevant cluster, chart × dealer confluence)
The engine's nearest *meaningful* resistances are recent swing highs; usable support comes from MAs/fibs/dealer levels, not the stale touch clusters.
- **Resistance 132.75–133** — swing high 2026-05-11 (`nearest_resistance`) **+ DP supply band $132–133** [CHART:swing_high][DP:price_levels]. The $130 call wall / gamma lid sits just under it [OI].
- **Resistance 141.45** — 52w high 2026-06-22 **+ DP supply $140.94** [CHART:high_52w][DP:price_levels].
- **Support 117–122 (the magnet)** — tight confluence: fib 0.236 = **117.26**, sma20 **119.42**, ema21 **122.09**, **+ $120 dealer gamma pin / max-pain** [CHART:fib_0.236][CHART:sma20][CHART:ema21][STRUCT:gex][OI]. This is the highest-value level on the board.
- **Support ~108** — sma50 108.39 [CHART:sma50].
- **Support ~102** — fib 0.382 = **102.29** ≈ swing low 2026-05-19 **102.40** [CHART:fib_0.382][CHART:swing_low]. Deeper: swing low 2026-06-05 **98.33** [CHART:swing_low].

### Fibonacci (dominant swing 38.95 → 141.45, up)
- Retracements: 0.236 **117.26**, 0.382 **102.29**, 0.500 90.20, 0.618 78.10 [CHART:fibonacci].
- Extensions: 1.272 **169.33**, 1.618 204.79 (only relevant if 141.45 breaks decisively).
- **Confluence calls:** 0.236 (117.26) lands inside the 117–122 dealer-pin shelf → the natural pullback target/long-defense. 0.382 (102.29) sits on the 5/19 swing low → the deeper "parabola failing" target.

### Patterns
- **flag / pennant:** none · **head & shoulders:** none · **double top/bottom:** none · **triangle:** none · **cup & handle:** none. `patterns_detected = []` [CHART:patterns].
- **Manual low-confidence observation (not engine-detected):** a **broadening/megaphone range** — successively wider swings with a higher high (141.45) and lower low (98.33). After a +247% YTD run this geometry is *distribution-consistent*, but it is unconfirmed and I do **not** assign it tradeable confidence. Confirmation would be a close below the 98.33 lower rail (bearish) or a sustained break/hold above 141.45 (bullish continuation).

### Elliott wave
- **Not detected** — `note: "pivot sequence not cleanly alternating"`. No working count; the broadening structure defeats a clean impulse/corrective label. No wave target asserted [CHART:elliott_wave].

## Verdict (for A3)
- **Chart bias: BULLISH primary trend, NEUTRAL near-term — conviction 3/5.** The trend is up and unbroken (MA stack), so the chart does **not** endorse a trend-reversal short; it only supports *fading strength toward the $120 pin* while price is capped under 132.75–133. A genuine bearish chart signal requires a close below ~117 (loss of the pin shelf) or below 98.33 (broadening-range break).
- **3 most important levels:**
  1. **117–122 support shelf** (fib 0.236 + sma20 + ema21 + $120 gamma pin/max-pain) — downside magnet & long-defense line.
  2. **132.75–133 resistance** (swing high + DP supply, $130 call-wall lid beneath) — fade-the-strength / short-entry line.
  3. **141.45 52w high** (+ DP supply $140.94) — breakout ceiling / bear invalidation.
- **Most credible pattern:** **none** (engine-clean). Only a low-confidence broadening-range distribution read; **the plan must not lean on it.** Per pattern rubric, no pattern is forced onto noise.
- **Chart × flow relationship: DIVERGENT** — bullish chart structure vs bearish flow/positioning. Confirms ledger **L-0002**: this is a range/fade context, not a directional trend trade. Carry to A3.
