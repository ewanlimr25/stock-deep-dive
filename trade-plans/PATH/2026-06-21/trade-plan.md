# Trade Plan — PATH

**As-of date:** 2026-06-21
**Spot reference:** $10.27 (yfinance, last session 2026-06-19)
**Voice:** desk PM running an institutional book
**Built from:** `research/PATH/2026-06-18/` deep dive (~1 trading day old) + chart engine (yfinance, 371 sessions)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** **SUFFICIENT** — completeness 94%
- **Have:** options flow, dark pool, OI/positioning, dealer GEX/ZGL, historical win-rate, macro/sector, fundamentals, sentiment/short-interest, OHLCV chart + patterns, implied move, event calendar.
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | High-confidence pattern confirm (volume + flow on the break) | nice_to_have | manual read on the breakout day; engine caps at `medium` |
  | Live intraday tape for precise trigger timing | nice_to_have | `uw options-flow sweeps --symbol PATH` + intraday yfinance on entry day |
  | DP re-confirm at the $10 test | nice_to_have | `uw dark-pool block-stratified --symbol PATH` (need buy_ratio <0.45 to confirm short / >0.60 to confirm long) |

> Data is *sufficient*; the **edge** is not. The substrate's own read is *no directional
> edge* — so this is a **two-sided, trigger-gated watch**, not a green light to size today.

## 1. Direction & conviction

- **Bias:** **NEUTRAL / RANGE** (bearish-tilt-on-confirmation)
- **Conviction (M-01 bin):** **0.55** (floor — DIVERGENT cap)
- **Horizon:** 1–4w
- **Confluence score:** 33/100 (carried from deep dive)
- **Flow↔chart agreement:** **DIVERGENT** (flow LONG vs chart SHORT) → entry style is trigger-gated, defined-risk, two-sided.

### Thesis (≤3 sentences)
PATH is pinned in a $10–$11 range where the **chart ($10.07 H&S neckline) and the dealer
book ($10 gamma flip / put-wall) agree the $10 line decides everything** [CHART:head_shoulders][STRUCT:gex],
while the only bullish lane — a 5-session ask-side sweep campaign [FLOW:sweep_persistence]
— **backtests just 37.5%** (n=8) [HIST:signal_backtest] and the dark pool won't confirm it
(large-tier buy_ratio 0.48) [DP:block_stratified]. With flow pointing up and the chart
pointing down (**DIVERGENT**), the honest call is **no position until a level breaks**: a
confirmed close below $10 arms a short-gamma slide to the $9.20 shelf, while a reclaim of
$11 detonates the 31.78% short float [SENT:short_float] into a squeeze. Trade the break, not the range.

### Why it should work (the bearish tilt, if a level must break)
- Chart bearish confluence: price below sma20/50/200 + bearish MACD + a **medium bearish H&S** whose neckline ($10.07) = the $10 gamma flip [CHART:ma_stack][CHART:head_shoulders][STRUCT:gex].
- **Short gamma below spot** ($10 strike gex −8.69M): a close under $10 self-reinforces lower toward the $9.20 52w-low shelf [STRUCT:gex].
- **The lone bull signal has no edge:** bullish_flow backtests 37.5% (n=8, avg −0.51%) — a 5/5 sweep campaign that historically loses money is not a buy [HIST:signal_backtest].
- **Macro headwind:** hawkish FOMC dot-flip + TRANSITIONAL half-size regime; PATH is NOT in the +$9.36B Tech inflow [MACRO:FOMC_2026-06-17].

### Why it may fail (the honest other side — steelman)
- **DIVERGENT (top reason_against, L-0002):** a persistent ask-side bull sweep campaign, consistency 1.0, $2.27M, says smart money is leaning the *other* way [FLOW:sweep_persistence].
- **Squeeze fuel:** 31.78% short float, DTC 3.78, CROWDED_SHORT — in a short-gamma book a **reclaim of $10→$11 squeezes UP**, not down (ledger L-0004 trap) [SENT:short_float].
- **No distribution to confirm a short:** DP large-tier buy_ratio 0.48 is balanced, not selling [DP:block_stratified].
- **Poor short R:R from here:** spot is only +9.5% above the 52w low and basing into a symmetrical triangle — limited room before the $9.20–9.45 shelf [CHART:support_resistance].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| $11.00–11.29 | trigger (bull reclaim) / resistance | [STRUCT:max_pain] + [CHART:resistance ×6] + [CHART:fib_0.236] | reclaim & hold = squeeze armed; heaviest ceiling |
| $12.00 | resistance | [OI] + [CHART] | call wall / upside cap |
| $10.48–10.79 | resistance / fade zone | [CHART:cluster] + [CHART:sma50] + [DP] | interim range cap |
| **$10.00–10.23** | **trigger (bear) / support / gamma flip / put wall** | [CHART:head_shoulders] + [STRUCT:gex] + [DP:price_levels] | **the decisive line** |
| $9.20–9.45 | target / support | [CHART:support] (low_52w 9.38) | breakdown shelf |
| ~6.94 | target (tail) | [CHART:head_shoulders] ≈ [CHART:fib_1.272] | measured-move tail, not base case |

Moving averages: sma50 10.69 · sma200 13.01 · ema21 10.85. Fib (down-swing 17.94→9.20):
0.236 = 11.26, 0.382 = 12.54, 0.5 = 13.57, 0.618 = 14.60.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| Head & shoulders | bearish | medium | 6.94 (interim 9.20–9.45) | reclaim >$11 (head 13.2) | confirms on a daily close < $10.07; squeeze caveat (L-0004) |
| Symmetrical triangle | neutral | low | break-dependent | n/a | trade the break; $10 and $11 are the trendlines |
| Elliott working count | — | none | n/a | n/a | rules 1/3 → discard as directional input |

## 4. Upcoming events that move the tape (next ~30–60d)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | June CPI release | ? (− on hawkish print) | [MACRO:CPI] |
| 2026-07-17 | July monthly OPEX (3rd Fri) | ? (pin/gamma roll-off near $11) | [OI:OPEX] |
| 2026-07-28 | FOMC (hike risk live) | − | [MACRO:FOMC] |
| ~2026-09-03 | UiPath Q2 FY2027 earnings | ? (big vol event; outside window) | [FUND:next_earnings_date] |

No catalyst inside the 1–4w window → naked long premium bleeds theta. Prefer defined-risk / spreads.

## 5. Invalidation

- **Price-based:** two daily closes **< $10.00** confirm the bear tilt (target $9.20–9.45); conversely **reclaim & hold > $11** kills the bear tilt and arms the squeeze.
- **Signal-based:** DP large-tier buy_ratio **< 0.45** (distribution → confirms short) OR sweep-persistence consistency **< 0.6** (bull pillar gone) OR cumulative premium net bearish 3 sessions.
- **Macro-based:** hawkish CPI (7/15) or FOMC (7/28) surprise vs consensus, or RISK-OFF regime flip on Iran/energy.

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = 0.375 (n=8, src=backtest, the *bullish_flow* signal) → capped p = 0.375
- **Inputs:** b = 2.7 (blended scale-out payoff), fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (2.7×0.375 − 0.625)/2.7 = **0.144** → fractional ceiling **3.6%**
- **Risk gates (each can only cut):** fundamentals CAUTION · sentiment CROWDED_SHORT · correlation n/a · rotation neutral · debate disconfirmed=true · context BUSY_NAME_NORMAL_DAY
- **Final size:** **0.0%** of book — *watch-only*. **Deviation:** DIVERGENT flow↔chart + watch-only edge ceiling (L-0002) → 0% until a level breaks on confirmation; **planned starter ≤1.5%** on a confirmed trigger, scaling only on a second hold.

## 7. Plan A — pure stock (short, trigger-gated)

- **Direction:** SHORT (conditional — nothing on today)
- **Entry:** $9.95 — **trigger:** two consecutive daily closes **< $10.00** (H&S neckline + gamma flip) on >1.2× avg volume [CHART:head_shoulders][STRUCT:gex]
- **Stop:** $10.65 (≈1 ATR above entry; a reclaim back above the broken $10.48 shelf = failed breakdown) [CHART:stops]
- **Targets:** T1 $9.20 (52w-low shelf, take 50%) · T2 $8.50 (toward H&S tail, take 30%) · T3 ~$7.00 (H&S measured move, runner 20%)
- **Reward:risk to T1:** ~1.07R
- **Size:** 0% now → starter ≤1.5% on the confirmed break
- **One-liner:** Short ONLY on a confirmed close below the $10 neckline/gamma-flip; short gamma carries it to $9.20. No position until the break — and stand down if it reclaims $11 (squeeze).

## 8. Plan B — options (≥1 with target date + target price)

### B1 — directional (bear, trigger-gated)
- **Structure:** put debit spread (deploy only on a confirmed close < $10)
- **Strikes / expiry:** 10P / 9P / 2026-07-17
- **Target date / target price:** 2026-07-15 / $9.20
- **Debit/credit · breakeven · max loss:** $0.35 debit · $9.65 · $0.35
- **Est. payoff at target ($9.20):** ~$0.45 (≈1.3× on debit); ~$0.65 if it reaches ≤$9.00 at expiry
- **Why this structure:** cheap IV (iv_rank 34.55) favors a debit; the $1-wide spread caps cost so the squeeze tail can't hurt; expiry sits before FOMC (7/28). Target is ~5× a single front-expiry implied move (2.06%) → rich, hence **trigger-gated + defined-risk**, never naked.

### B2 — defined-risk alternative (two-sided, the pre-break stance)
- **Structure:** long strangle (owns either break on cheap IV; the aligned structure given short gamma + squeeze fuel — do NOT sell premium two-sided here)
- **Strikes / expiry:** 9.5P / 11C / 2026-07-17
- **Target date / target price:** 2026-07-15 / $9.20 (bear leg; bull leg objective $11.30 on a squeeze)
- **Debit/credit · breakeven · max loss:** $0.55 debit · $8.95 / $11.55 · $0.55
- **Why this structure:** the $10/$11 break is a genuine binary and IV is cheap, so owning both tails is coherent. **Caveat:** breakevens sit outside the implied move and there's no catalyst until CPI 7/15 — keep it **tiny** (≤0.5%) or stand aside; this bleeds theta if PATH just sits in the range.

## 9. Post-entry monitoring checklist

- [ ] Re-pull `uw options-structure gex` near any $10 test — confirm short gamma still building.
- [ ] Re-pull `uw dark-pool block-stratified` — need buy_ratio <0.45 to confirm the short / >0.60 to confirm a long reclaim.
- [ ] Trail stop to breakeven after T1 ($9.20).
- [ ] Watch CPI (7/15) and FOMC (7/28) — both can gap the tape; defined-risk caps the gap.
- [ ] Stand down the bear plan immediately on a reclaim & hold > $11 (squeeze).

## 10. Reasoning-ledger lessons applied

- **L-0002** (ACTIVE) — DIVERGENT flow↔chart is not a directional trade → capped at NEUTRAL/0.55, defined-risk only; divergence logged as the #1 reason_against.
- **L-0004** (CANDIDATE) — short-gamma + ~32% SI + bull sweep → a *reclaim squeezes up*; the bear plan is trigger-gated and defined-risk, never naked bearish premium into the squeeze fuel.
- **L-0001** (ACTIVE) — the symmetrical triangle is low-confidence → require a volume-confirmed break and size at starter until two closes hold.

## Citations (≥3, what the eval will spot-check)

1. [HIST:signal_backtest] — bullish_flow win-rate 0.375 (n=8, avg −0.51%) — `research/PATH/2026-06-18/phase-5-historical.md`
2. [DP:block_stratified] — large-tier buy_ratio 0.48 (non-confirmation) — `research/PATH/2026-06-18/phase-2-dark-pool.md`
3. [STRUCT:gex] — near-spot short gamma, $10 strike gex −8.69M, gamma flip $10 — `research/PATH/2026-06-18/phase-4-structure.md`
4. [FLOW:sweep_persistence] — bull campaign consistency 1.0, 5/5 sessions, $2.27M — `research/PATH/2026-06-18/phase-1-flow.md`
5. [CHART:head_shoulders] — bearish H&S, neckline 10.07, target 6.94 — `trade-plans/PATH/2026-06-21/chart.json`
6. [SENT:short_float] — 31.78% short float, DTC 3.78 — `research/PATH/2026-06-18/phase-7c-sentiment.md`

---
*Run `/trade-plan-eval PATH 2026-06-21` after taking (or passing on) the trade so the reasoning ledger learns from the outcome.*
