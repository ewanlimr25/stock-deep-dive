# Phase A2 — Chart, Technicals & Patterns — ELF (2026-06-30)

**Tool call:** `python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker ELF --date 2026-06-30 --lookback 540 > chart.json` → `available: true`, source `yfinance`, 373 sessions. All datapoints resolve to `chart.json`.

## Summary
ELF is in a sharp **V-recovery uptrend** — recent swing structure is clean **HH/HL** (low 48.82 6/05 → high 70.30 6/16 → higher-low 61.53 6/23 → now $74, a new local high), price is above rising sma20 60.9 / sma50 59.77, and MACD is bullish [CHART:market_structure][CHART:macd]. **But it is extended and overbought**: RSI 72.7, spot pressing the upper Bollinger (74.53), sitting exactly on the **fib 0.5 (73.16)** half-retrace of the prior decline, +23.8% over the 50-day, and still **−11.96% below the 200-day (84.05)** [CHART:rsi14][CHART:fib_0.5]. Two low-confidence patterns bracket the read: a **cup-and-handle** (rim 68.4, target 84.29 ≈ sma200) says more upside, while an **Elliott impulse whose wave-5 target (71.57) is already met** says the up-leg is maturing [CHART:cup_handle][CHART:elliott_wave]. Net: the chart **CONFIRMS the bullish flow direction** but flags the exact same caution the flow does — **buy dips, cap targets, don't chase $74.**

## Key signals (tagged)
- Uptrend confirmed near-term: `market_structure = uptrend_HH_HL` (low 48.82 → 70.30 → higher-low 61.53 → 74) [CHART:market_structure][CHART:recent_pivots].
- Overbought/extended: RSI **72.7**, spot on BB upper 74.53, at **fib 0.5 73.16**, wave-5 target (71.57) exceeded [CHART:rsi14][CHART:elliott_wave].
- Repairing, not repaired: below **sma200 84.05** (−11.96%), −49.55% off the 52w high 146.67 [CHART:sma200].
- 60-day regression is nominally down (−0.09%/day) — an artifact of the earlier May decline in the window; the *recent* structure is up [CHART:trend].
- Volume only 1.04× average — the push lacks an accumulation surge (mild non-confirmation) [CHART:vol_vs_avg].
- ATR14 3.85 (5.49%) → engine stops: long 1.5-ATR **68.22**, short 1.5-ATR **79.78** [CHART:stops].

## Detailed findings

### Trend / market structure
- **Near-term uptrend (HH/HL)** off the 6/05 low 48.82; the 6/23 higher-low 61.53 confirms the higher-low sequence [CHART:recent_pivots]. Price > sma20 (60.9) > sma50 (59.77), both rising.
- **Longer-term still below sma200 84.05** — the recovery has retraced half the decline (fib 0.5) but has not repaired the broken 200-day. This is a *recovery within a larger downtrend*, not a fresh secular uptrend.

### Momentum / volatility
- RSI14 **72.7 overbought** — the first genuine overbought reading of the bounce; historically a pause/pullback zone, not a fresh-entry zone [CHART:rsi14].
- MACD **bullish** (hist +1.373) — momentum still up, no bearish cross yet [CHART:macd].
- ATR14 3.85 (5.49%) → ~$3.85 daily range; stops long 1-ATR **70.15** / 1.5-ATR **68.22** [CHART:stops].
- BB 47.26–74.53; spot **on the upper band** — statistically stretched, mean-reversion risk.

### Support / resistance (chart × dealer confluence)
- **Support $68–71 (the primary dip-buy shelf)** — chart support **70.84** (3 touches, last 6/16) + **$70 gamma wall +1.03M** + cup rim **68.4** + fib 0.382 **67.42** + long 1.5-ATR 68.22 [CHART:cluster][STRUCT:gex][CHART:cup_handle][CHART:fib_0.382]. Dealers buy dips here in long-gamma.
- **Resistance / cap $75–79** — chart resistance **75.85** (last 2026-01-02) / **77.82** (3-touch) / 79.30 + **$75 gamma wall +681k** + fib 0.618 **78.91** [CHART:cluster][STRUCT:gex][CHART:fib_0.618]. The capped-target zone.
- **Major floor $59–65** — chart support **59.58** (3-touch) + swing low **61.53** + sma50 **59.77** + **ZGL 59.97** + max-pain **$59–63** + **$64–65 institutional DP shelf** + fib 0.236 **60.31** [CHART:cluster][CHART:swing_low][STRUCT:gex][DP:price_levels][CHART:fib_0.236]. The deep dip-buy / thesis-defense; **loss of ZGL 59.97 flips dealers short-gamma (hard stop)**.
- **Overhead objective ~84** — sma200 **84.05** ≈ cup target **84.29** ≈ (fib 0.786 87.09 above) [CHART:sma200][CHART:cup_handle]. The stretch target if $75–80 clears.

### Fibonacci (dominant swing 97.5 → 48.82, down — measures the bounce)
- Retracements: 0.236 **60.31**, 0.382 **67.42**, 0.5 **73.16**, 0.618 **78.91**, 0.786 87.09 [CHART:fibonacci].
- **Confluence calls:** spot $74 sits on **fib 0.5 (73.16)** — the classic half-retrace decision point (resistance until cleared). 0.382 (67.42) ≈ cup rim / $70 shelf → dip-buy. 0.236 (60.31) ≈ the $59–62 floor. 0.618 (78.91) ≈ the $75–79 cap.

### Patterns
| Pattern | Dir | Conf | Target | Invalidation | Confirmation |
|---------|-----|------|--------|--------------|--------------|
| cup & handle | bullish | **low** | 84.29 | 49.57 | close above the 68.4 rim (already reclaimed) → hold on pullbacks; decisive close > $75–77 [CHART:cup_handle] |
| Elliott impulse (wave-5 pending) | bullish/exhausting | **low** | 71.57 (met) | — | 2/3 rules (wave-2 breached wave-1 origin → rule 1 FAIL); wave-5 target already exceeded = **up-leg maturing** [CHART:elliott_wave] |

- **Honest read:** both are **low confidence** and point in near-term-opposite directions — the cup says "continuation to ~84," the Elliott count says "wave 5 is done (71.57 met), expect a corrective pullback." Per the pattern rubric I do **not** promote either. Their *agreement* is the useful part: **a pullback toward the 68–71 rim/shelf is the high-value entry, and $84 (sma200) is the natural ceiling of this leg.** The Elliott count is a hypothesis (2/3 rules) that reinforces the "don't chase $74" discipline; it does **not** set the bias (flow+trend do).

### Elliott wave (detail)
- Interpretation: **impulse_up, wave-5 pending**; rules_passed **2/3** — wave-2 retraced beyond wave-1's origin (rule 1 fails), wave-3 not shortest (pass), wave-4 no overlap (pass). wave5_projection **71.57** — **already exceeded by spot $74**, i.e. the projected impulse target is met → treat as **near-exhaustion working count**, low confidence [CHART:elliott_wave].

## Verdict (for A3)
- **Chart bias: BULLISH near-term but EXTENDED/OVERBOUGHT — conviction 3/5.** The chart *confirms* the bullish flow direction (uptrend HH/HL, above rising 20/50, MACD up, cup toward 84) but *at a poor entry* (RSI 72.7, fib 0.5, BB upper, wave-5 met). It endorses **dip-buying $68–71 / $59–65, capping targets $75–80/84, and NOT chasing $74** — exactly the deep dive's plan.
- **3 most important levels:**
  1. **$68–71 support shelf** ($70 gamma wall + 3-touch 70.84 + cup rim 68.4 + fib 0.382) — primary dip-buy; dealers defend in long-gamma.
  2. **$75–79 cap** ($75 gamma wall + 75.85/77.82 + fib 0.618) — capped target; aggressive breakout trigger = a confirmed close above $75.
  3. **$59–65 major floor** (ZGL 59.97 + sma50 + max-pain + 61.53 higher-low + $64–65 shelf + fib 0.236) — deep dip-buy / hard-stop line (ZGL loss = short-gamma flip).
- **Most credible pattern:** **cup & handle (low, bullish, target 84.29 ≈ sma200)** — carry it as the bullish roadmap; per **L-0001** any breakout add above the rim/$75 must be confirmation-triggered (close on >1.2× volume), not anticipated. The Elliott count (low, wave-5 met) is the exhaustion counter-hint.
- **Chart × flow relationship: CONFLUENT bullish** (both up), with a shared *extended-entry* caution. Not divergent → conviction taken normally from the band (0.55 given the caps/regime); dip-buy entry style. Carry to A3.
