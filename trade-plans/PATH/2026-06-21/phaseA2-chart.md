# Phase A2 — Chart, Technicals & Patterns — PATH (2026-06-21)

**Tool call:** `python3 lib/chart_engine.py --ticker PATH --date 2026-06-21 --lookback 540`
→ `chart.json` (`available: true`, source **yfinance**, 371 daily sessions).

## Summary

PATH is a beaten-down ($10.27, −46.8% off the 52w high, +9.5% above the 52w low)
software name trading **below all three key MAs** (sma20 11.13 / sma50 10.69 / sma200
13.01) with a **bearish MACD** and a **downtrend LH/LL** swing structure — yet it is
**compressing into a symmetrical triangle** just above the 52w-low shelf, RSI a neutral
41.7. The engine's most credible pattern is a **medium-confidence bearish head-&-shoulders**
whose **neckline ($10.07) sits exactly on the deep-dive $10 gamma-flip / put-wall** — so the
chart and the dealer book agree that **$10 is the line that decides everything**.

## Key signals (tagged)

- Price < sma20/50/200; dist −3.9% to sma50, −21.0% to sma200 [CHART:ma_stack]
- MACD hist −0.148 bearish [CHART:macd]; RSI14 41.7 neutral [CHART:rsi14]
- Structure `downtrend_LH_LL` but 60-day regression flat-up (+0.07%/day) → **basing/coiling**, not trending down hard [CHART:trend]
- ATR14 0.68 (**7.07% daily** — high vol; wide stops required) [CHART:atr14]
- Volume 45.2M vs 48.7M 20-day avg (0.93×, below average → no distribution thrust) [CHART:vol_vs_avg]
- **H&S (medium, bearish)**: neckline 10.07, head 13.2, target 6.94 [CHART:head_shoulders]
- **Symmetrical triangle (low)**: converging trendlines, trade the break [CHART:triangle]
- Fib 0.236 (11.26) ≈ heaviest resistance 11.29 (6 touches) ≈ $11 max-pain pin → **confluence ceiling** [CHART:fib_0.236]

## Detailed findings

### Trend / structure
Lower-highs since the 6/1 spike to $13.2 (→ $11.08 on 6/15) and a marginally lower
low (10.42 5/29 → 10.07 6/12) give `downtrend_LH_LL`. But the 60-day regression is
*flat-to-up* and the swings are converging (triangle), so this reads as a **bearish-tilted
basing range**, not a clean impulsive downtrend. Below sma50/200 keeps the medium-term
tape bearish; reclaiming sma50 (10.69) would be the first repair.

### Momentum / volatility
RSI 41.7 neutral (no oversold cushion, no bull momentum). MACD bearish but shallow
(−0.148). ATR 7.07% means a $0.68 daily range — **stops must clear ~1.5 ATR**
($1.02) or get whipped. Volume below average → neither capitulation nor accumulation
thrust on the tape.

### Support / resistance (ranked; confluence with dealer/OI flagged)
| Level | Touches | Role | Confluence |
|-------|---------|------|------------|
| **11.29** | 6 | resistance | **fib 0.236 (11.26) + $11 max-pain/pin [OI] + call wall $12 above** → ceiling |
| 11.05 / 11.42 | 4 / 4 | resistance | upper triangle line / supply shelf |
| **10.48** | 4 | resistance | ≈ sma50 10.69 + DP supply 10.79 [DP] → interim cap |
| **10.07** | 3 | **support / H&S neckline** | **= $10 gamma-flip / put-wall [STRUCT] + DP support 10.23 just above [DP]** → the decisive line |
| 9.45 / 9.24 | 3 / 2 | support | 52w-low shelf (low_52w 9.38) → breakdown target zone |

The single tradeable confluence: **$10.00–10.23** (chart neckline + DP support + gamma
flip + put wall) on the downside, and **$11.00–11.29** (pin + heaviest resistance + fib)
on the upside. The range between is no-man's-land.

### Fibonacci (down-swing 17.94 → 9.20)
Retracements: 0.236 **11.26**, 0.382 12.54, 0.5 13.57, 0.618 14.6. The **0.236 lines up
with the 11.29 resistance and the $11 pin** — a high-value short/fade zone and the exact
level the bull must reclaim. Downside extension 1.272 = **6.82**, which corroborates the
H&S target 6.94 (both far below the 52w low → treat as tail, not base case).

### Patterns (per `pattern-rubric.md`)
- **Head & shoulders — bearish — `medium`.** Head 13.2 (6/1), shoulders ~11.1–11.3,
  neckline **10.07**. *Confirmation:* a **daily close below 10.07** on rising volume.
  *Measured target:* 6.94 (engine) — **cap to a realistic interim 9.20–9.45** (52w-low +
  DP support); only extend toward ~6.9 on a momentum cascade. *Invalidation:* back above
  the head 13.2 (structurally, a reclaim & hold of $11 already negates the right-shoulder
  break). **Not promoted to `high`:** no volume confirmation and flow *disagrees* (5-session
  bull sweep + 31.78% SI), so a neckline **reclaim could squeeze** instead — see L-0004.
- **Symmetrical triangle — neutral — `low`.** Upper line −0.020/day, lower +0.044/day,
  converging. *Trade the break:* the $10 and $11 confluence lines ARE the two trendlines —
  whichever breaks on volume sets the next leg.
- **Flag / double top-bottom / cup&handle — none detected.**

### Elliott wave — NOT a count here
`detected: false`, `rules_passed 1/3`, confidence `none`. Interpretation
"impulse_down_wave5_pending" with a wave-5 projection of 10.2 — i.e. essentially *at spot*.
**Discard as a directional input** (fails 2 of 3 hard rules); it adds nothing the H&S
doesn't already say.

## Verdict for downstream

- **Chart bias: BEARISH-leaning, but range-bound / knife-edge — conviction 3/5.**
  Below all MAs + bearish MACD + a medium bearish H&S argue lower; basing triangle, neutral
  RSI, proximity to the 52w-low shelf, and the bull-sweep/short-squeeze counterforce stop it
  from being a high-conviction short. **The break of $10 vs $11 resolves it.**
- **Top 3 levels:**
  1. **$10.00–10.23** (H&S neckline 10.07 + gamma flip + put wall + DP support) — *the trigger line.*
  2. **$11.00–11.29** (max-pain pin + heaviest resistance + fib 0.236) — *the bull-reclaim ceiling.*
  3. **$10.48–10.79** (chart 10.48 + sma50 + DP supply 10.79) — *interim range cap / fade zone.*
- **Most credible pattern:** bearish **H&S**, confirm on a **daily close < $10.07**, interim
  target **$9.20–9.45**, invalidation = reclaim & hold **> $11**. Carries the squeeze caveat.
