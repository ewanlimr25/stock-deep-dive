# Phase A2 — Chart, Technicals & Patterns

**Ticker:** FSLR **As-of:** 2026-06-21 **Source:** yfinance (371 sessions)
**Tool call:** `chart_engine.py --ticker FSLR --date 2026-06-21 --lookback 540` → `chart.json` (`available:true`)

> *For research and educational use only. Not financial advice.*

## Summary

FSLR ran **parabolically** from the April base (~$185) to a blow-off high of
**$320.95 on 2026-06-03** [CHART:swing_high], then corrected **~22%** to **$248.66
on 2026-06-10** [CHART:swing_low], bounced to **$279.18 on 2026-06-12**, and has
since drifted to **$257.70**. The larger trend is still up (spot > sma50 $236.68 >
sma200 $233.30; +79% off the 52w low) but **short-term momentum has rolled over**:
price is below ema9 $266.32 / ema21 $265.25 / sma20 $278.12, MACD hist −5.99
(bearish), RSI 48.5 (neutral). Net: a **post-blow-off consolidation / range
($248–$280)**, not a fresh trend entry — `market_structure: range_or_transition`
[CHART:trend]. **No classical chart pattern is confirmed.**

## Key signals (tagged)

- **Blow-off + mean-revert:** +73% April→Jun-3 then −22% in 5 sessions [CHART:swing_high/swing_low]. Parabola digested, not resumed.
- **Major confluence floor $248–$252** (see below) — the make-or-break level [CHART:support + CHART:fib_0.5].
- **Overhead wall $278–$288** = sma20 $278.12 + Jun-12 high $279.18 + S/R $280.41 (3 touches) + fib 0.236 $288.39 [CHART:resistance].
- **Momentum cooled:** MACD bearish, price under the 9/21 EMAs — bulls must *reclaim* $260→$266 to flip the short-term tape [CHART:macd_state/ema21].
- **Volatility wide:** ATR14 **$16.34 (6.77%)** — stops must be ATR-scaled or they get noise-stopped [CHART:atr14].

## Trend / structure

- **Regression (60d):** slope +0.75%/day, direction **up** — but labeled
  `range_or_transition` because the last two swings (Jun-3 high → Jun-10 low →
  Jun-12 lower-high $279 → now $257) are **carving a range, not extending** [CHART:trend].
- **MA stack:** `mixed`. Spot is above the slow MAs (sma50/200, +8.9%/+10.5%) but
  **below all the fast ones** (ema9/21, sma20). Classic mid-correction posture:
  primary trend up, secondary trend down.
- **52-week:** −19.0% off the $318.25 high; +79.4% above the $143.67 low.

## Momentum / volatility

| Metric | Value | Read |
|--------|-------|------|
| RSI14 | 48.5 | neutral — no oversold bounce signal, no overbought warning |
| MACD hist | −5.99 | **bearish** — momentum negative since the blow-off |
| ATR14 | 16.34 (6.77%) | high — size stops ≥1 ATR |
| Vol vs 20d avg | 1.2× | mild elevation, no climactic spike now |

## Support / resistance — ranked, with cross-substrate confluence

**The tradeable confluence is where chart levels line up with the fresh 6/18 gamma/pin map (A1).**

| Zone | Chart evidence | Flow/structure confluence (A1, 6/18) | Verdict |
|------|----------------|--------------------------------------|---------|
| **$248–$252 (FLOOR)** | S/R $248.24 (4 touches, Jun-10) + $251.62 (3) + **fib 0.500 $251.97** + swing low $248.66 [CHART] | **$250 gamma magnet +$4.33M** (largest); 7/10 max-pain $250 | **★ make-or-break support** |
| $260–$261 | S/R $260.50 (1 touch) [CHART] | **$260 gamma magnet +$3.38M**; max-pain $260 (7/02/7/17/7/31); 6/26 max-pain $265 | **immediate overhead pin** |
| $265–$268 | **ema21 $265.25 / ema9 $266.32** + fib 0.382 $268.25 [CHART] | $270 gamma +$2.31M above | reclaim line (flip short-term bull) |
| $274–$288 (CEIL) | sma20 $278.12 + Jun-12 high $279.18 + S/R $274.97/$280.41 + fib 0.236 $288.39 [CHART] | $280 gamma +$1.13M (old LEAP target) | blow-off retest band |
| $234–$236 (deep) | S/R $234.07 + fib 0.618 $235.69 + sma50 $236.68 [CHART] | old $230 put wall −$0.40M | deep support / invalidation shelf |
| $321 | parabolic high $320.95 [CHART:swing_high] | — | the high to beat |

## Fibonacci (dominant swing $182.99 → $320.95, up)

- **0.500 = $251.97** and **0.618 = $235.69** bracket the two support shelves;
  the **0.5 sits dead-center of the $248–$252 floor** → high-value confluence.
- 0.382 = $268.25 (overhead, near the EMAs); 0.236 = $288.39 (ceiling band).
- Extensions 1.272 = $358.48 / 1.618 = $406.21 — only relevant if a new high prints.

## Patterns — honest call: **none confirmed**

- flag / head-&-shoulders / double-top-bottom / triangle / cup-&-handle → **all
  `detected: false`** [CHART:patterns]. The post-parabola range has not yet formed
  a clean, tradeable geometry. **No pattern is being forced onto the noise.**
- **Elliott (working count, hypothesis only):** `interpretation:
  impulse_down_wave5_pending`, **confidence none, rules_passed 1/3**
  (wave-2-not-beyond-origin ✗, wave-3-not-shortest ✓, wave-4-no-overlap ✗),
  `wave5_projection $259.96` [CHART:elliott_wave]. With 1/3 rules it is **not
  tradeable**; at most it weakly hints the corrective down-leg is **near
  exhaustion around the $250–$260 magnet box** — consistent with the floor, but it
  does **not** set bias. Per pattern-rubric, no promotion.

## ATR-based stop reference [CHART:stops]

- Long: 1-ATR stop **$241.36**, 1.5-ATR **$233.19** (below sma50 / fib 0.618).
- Short: 1-ATR stop **$274.04**, 1.5-ATR **$282.21** (above the ceiling band).

## Verdict (for A3)

- **Chart bias: NEUTRAL / RANGE (mildly constructive on the higher timeframe)** —
  conviction **2/5**. Primary trend up, secondary trend down; price boxed
  $248–$280. The chart does **not** endorse chasing here; it endorses **buying the
  $248–$252 floor with a stop, or fading the $278–$288 ceiling**, and waiting for a
  **reclaim of $260→$266** before any momentum-long.
- **3 most important levels:**
  1. **$248–$252** — confluence floor (gamma $250 + swing low + fib 0.5 + S/R). Hold = range intact; **2 closes below = trend damage**.
  2. **$260 → $266** — the pin + EMA reclaim line that flips the short-term tape bullish.
  3. **$278–$280** — blow-off retest band; close above reopens $321.
- **Most credible pattern:** **none** — report the structure (post-blow-off range)
  honestly; the only "carry" item is the weak Elliott hint that downside is near
  exhaustion at the floor, used as *context*, not a signal.
- **Confirmation triggers to hand A3:** long-confirm = close **> $266** on >1.2×
  avg vol (reclaim EMAs); short/fade-confirm = rejection at $278–$280 **or** 2
  closes **< $248**.
