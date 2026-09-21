# Phase A2 — Chart, Technicals & Patterns — ENVX (2026-06-27)

**Tool call:** `python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker ENVX --date 2026-06-27 --lookback 540 > chart.json` → `available: true`, source `yfinance`, 373 sessions. All datapoints resolve to `chart.json`.

## Summary
ENVX is in a **downtrend** — spot $5.95 sits below every MA (sma20 7.08 / sma50 6.83 / sma200 7.72), MACD is bearish, and price is **−62.65% off its 52w high** with descending swing highs (7.50→7.40→7.28) [CHART:ma_stack][CHART:macd]. But the engine detected a **medium-confidence inverse head-and-shoulders** (shoulders 6.16/6.19, head 5.39, neckline 7.40, target 9.41) that *aligns with the bullish $6-Oct call flow* — except it is **unconfirmed and at-risk**: price is back near the $5.39 head/invalidation, ~24% below the 7.40 neckline, on above-average volume (1.26×) [CHART:head_shoulders][CHART:vol_vs_avg]. Net: a **two-sided range pinned at the $6 max-pain magnet**, with the $5.39–5.50 shelf as the line that decides between a squeeze-tail and downtrend continuation.

## Key signals (tagged)
- Downtrend intact: spot below all SMAs, dist −12.87% to sma50 / −22.96% to sma200; MACD hist −0.158 [CHART:ma_stack][CHART:macd].
- **Inverse H&S detected (medium)** — bullish, neckline 7.40, head 5.39, target 9.41, invalidation 5.39 — but **unconfirmed; price near invalidation, not building the right shoulder up** [CHART:head_shoulders].
- Symmetrical triangle (low, neutral) — converging trendlines (upper −0.15, lower +0.007); trade the break [CHART:triangle].
- High realized vol: ATR14 0.56 = **10.49%** → ~$0.56 daily range on a $5.95 stock; informs option width [CHART:atr14].
- Volume 8.16M vs 6.46M avg = **1.26×** — recent activity above average into the down-move (near-term distribution tell) [CHART:vol_vs_avg].
- 60-day regression nominally up (+0.32%/day) but `market_structure = range_or_transition` — chop, not trend [CHART:trend].

## Detailed findings

### Trend / market structure
- Full **bearish MA stack from the price's view** (below sma20/50/200); the regression's mild up-slope is an artifact of the wide $5.39–9.15 chop, not a real uptrend [CHART:trend].
- Swing highs **descending** (7.50 5/13 → 7.40 6/15 → 7.28 6/22); swing lows 5.39 (5/19) → 6.19 (6/11) → now testing back to 5.95. The single higher-low (5.39→6.19) is the only bullish structural element, and it is **being challenged** [CHART:recent_pivots].

### Momentum / volatility
- RSI14 **40.21** — soft but not oversold; room to fall before a bounce signal [CHART:rsi14].
- MACD **bearish** (hist −0.158) — momentum down [CHART:macd].
- ATR14 0.56 (**10.49%**) → engine stops: long 1.5-ATR **5.11**, short 1.5-ATR **6.79** [CHART:stops].
- BB 5.35–8.80; spot 5.95 in the lower third — pressing the lower band.

### Support / resistance (chart × dealer confluence)
- **Resistance 6.15–6.35** — S/R 6.15 (3 touches) + **DP supply $6.28–6.33** + fib 0.618 **6.35** [CHART:cluster][DP:price_levels][CHART:fib_0.618]. First overhead lid above the $6 pin.
- **Resistance 7.10–7.44 (heavy)** — 5-touch 7.10 + 4-touch 7.23 + 4-touch 7.44 + **inverse-H&S neckline 7.40** + fib 0.382 **7.42**; sma200 **7.72** just above [CHART:cluster][CHART:head_shoulders][CHART:fib_0.382][CHART:sma200]. This is the bull-confirmation wall.
- **Pin / magnet $6.00** — July max-pain, long-gamma 30/30 [STRUCT:max_pain].
- **Support 5.50–5.67** — S/R 5.57/5.67 + fib 0.786 **5.59** + **$5.50 gamma-flip / put-wall** [CHART:cluster][CHART:fib_0.786][STRUCT:today_gamma_flip].
- **Pivot support 5.39** — swing low + inverse-H&S **invalidation** [CHART:swing_low][CHART:head_shoulders].
- **Capitulation 4.84 / 4.61** — 52w low / fib swing-low (put-spread target) [CHART:low_52w].

### Fibonacci (dominant swing 4.61 → 9.15, up)
- Retracements: 0.236 8.08, 0.382 **7.42**, 0.5 6.88, 0.618 **6.35**, 0.786 **5.59** [CHART:fibonacci].
- Extensions: 1.272 10.38, 1.618 11.95 (only if 9.15/neckline-target clears).
- **Confluence calls:** 0.382 (7.42) ≈ the H&S neckline + 5-touch resistance → the single most important overhead. 0.618 (6.35) ≈ DP supply → near-term lid. 0.786 (5.59) ≈ gamma-flip shelf → the support that pairs with the 5.39 invalidation.

### Patterns
| Pattern | Dir | Conf | Target | Invalidation | Confirmation |
|---------|-----|------|--------|--------------|--------------|
| inverse head & shoulders | bullish | **medium** | 9.41 | 5.39 | **close above 7.40 neckline on >1.2× vol** [CHART:head_shoulders] |
| symmetrical triangle | neutral | low | break-based | — | break of either converging trendline on volume [CHART:triangle] |

- **Honest read on the inverse H&S:** the *geometry* is clean (shoulders 6.16/6.19 within 0.5%, head 5.39 the extreme, neckline 7.40–7.50) — medium is earned. But the *live context is unfavorable*: price has fallen back to 5.95 (below both shoulder lows), it is **not** building the right shoulder upward, the neckline is **24% above spot**, and invalidation (5.39) is only **−9.4% away**. So it is a **conditional bullish reversal, not an active signal** — it pays only on a confirmed 7.40 reclaim, and dies on a 5.39 break. Per **L-0001**, no anticipatory sizing before the neckline holds two closes.
- It does, however, **agree in direction with the bullish $6-Oct call flow** — that is the one place flow and chart line up (on the *upside tail*), and its 9.41 target rhymes with the squeeze thesis.

### Elliott wave
- **Not detected** — `note: "pivot sequence not cleanly alternating"`. No count asserted [CHART:elliott_wave].

## Verdict (for A3)
- **Chart bias: NEUTRAL / RANGE with a near-term bearish tilt and a *conditional* bullish reversal — conviction 2.5/5.** The trend is down and momentum bearish, but a clean (unconfirmed) inverse H&S + the $6 pin keep it range-bound rather than outright bearish. The chart does **not** endorse a directional position either way at $5.95; it endorses **fading the extremes of a $5.39–7.40 range** and buying cheap optionality on a break.
- **3 most important levels:**
  1. **5.39–5.50** (H&S invalidation + gamma-flip/put-wall + fib 0.786) — the decision line: hold = range/squeeze-tail alive; break = downtrend continuation to 4.84/4.61.
  2. **6.00** (max-pain pin/magnet) — gravity center into Jul-17 OPEX.
  3. **7.40–7.44** (H&S neckline + fib 0.382 + 5-touch resistance, sma200 7.72 above) — bull-confirmation trigger; a close above on volume confirms the inverse H&S (target 9.41) and the squeeze.
- **Most credible pattern:** **inverse head & shoulders (medium, UNCONFIRMED, at-risk).** Carry it as the bullish tail's roadmap (target 9.41, trigger 7.40, invalidation 5.39) — **do not** treat it as a live long; L-0001 governs.
- **Chart × flow relationship:** the bullish flow + bullish (unconfirmed) pattern point **up**, while trend + macro + the negative backtest point **down** → net **RANGE / FLOW-LEADS-but-unconfirmed**. Ledger **L-0002** (divergent) and **L-0001** (unconfirmed breakout) both apply. Carry to A3.
