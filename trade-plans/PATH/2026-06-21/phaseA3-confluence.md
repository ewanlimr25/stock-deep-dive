# Phase A3 — Confluence: Direction, Reasons, Levels, Events — PATH (2026-06-21)

Fuses the 2026-06-18 deep-dive substrate (flow/DP/OI/structure/macro/fundamentals/
sentiment/debate) with the A2 chart layer. Gap-audit verdict: **SUFFICIENT** (data),
edge ceiling **watch-only** on the unconfirmed direction.

## Step 1 — directional votes

| Lane | Read | Vote |
|------|------|------|
| Flow (A1) | call prem $1.87M > put $0.67M, P/C 0.335, **5-session ask-side bull sweep**, consistency 1.0 [FLOW] | **LONG** |
| Dark pool (A2) | large-tier buy_ratio **0.48** — won't confirm, balanced (not distribution) [DP] | NEUTRAL |
| Positioning (A3) | max-pain/largest pin **$11** above spot (mild magnet) + call wall $12 (resistance) [OI] | NEUTRAL |
| Dealer (A4) | near-spot **short gamma**, $10 gex −8.69M, gamma flip $10 (unstable, break-prone) [STRUCT] | **SHORT** |
| Historical (A5) | bullish_flow win-rate **37.5%** (n=8, avg −0.51%) — the bull signal has no edge [HIST] | **SHORT** |
| Chart trend (B3) | downtrend LH/LL, price < sma20/50/200, MACD bearish [CHART] | **SHORT** |
| Chart pattern (B4) | **bearish H&S** (medium), neckline 10.07 [CHART] | **SHORT** |
| Macro/sector (C1) | hawkish FOMC, TRANSITIONAL half-size regime; Tech inflow but PATH not participating [MACRO] | **SHORT** |

**Plurality = bearish (5 short / 2 neutral / 1 long).** Fundamentals (CAUTION) and
sentiment (CROWDED_SHORT) gates can only *cut*.

## Step 2 — flow ↔ chart agreement: **DIVERGENT**

Flow points **LONG** (persistent bull sweep campaign), the chart points **SHORT**
(downtrend + bearish H&S). They point opposite ways → **DIVERGENT**. Per
`direction-rubric.md` Step 2 and ledger **L-0002**, a divergent read is **NEUTRAL/RANGE
by default, defined-risk fade only — never a full directional size**. The divergence is
the top `reason_against` below.

## Step 3 — conviction bin (adjustment trail)

| Step | Input | Result |
|------|-------|--------|
| Confluence band | deep-dive confluence_score 33 → recommended_bin | 0.55 |
| 1. Agreement modifier | **DIVERGENT → cap 0.55** | 0.55 |
| 2. Risk gates | fundamentals CAUTION + sentiment CROWDED_SHORT + debate_disconfirmed | floor held 0.55 |
| 3. Context | BUSY_NAME_NORMAL_DAY → no top-of-band | 0.55 |
| 4. Staleness | deep dive ~1 trading day old → no cut | 0.55 |
| 5. Gap audit | SUFFICIENT → no cut | 0.55 |

**Conviction = 0.55 (floor).** **Bias = NEUTRAL / RANGE, bearish-tilt-on-confirmation.**
Horizon = **1–4w**. This extends the deep dive's NEUTRAL/0.55/size-0% read: the chart
adds two bearish votes but the DIVERGENT cap and 32% squeeze fuel keep it a *watch*, not
a short. **No naked directional size until a level breaks.**

## Step 4 — reasons for / against (goal #3)

**reasons_for** — *why the higher-probability resolution, IF a level breaks, is the downside:*
1. Chart bearish confluence: price below all MAs, MACD bearish, and a medium bearish **H&S whose neckline ($10.07) sits on the $10 gamma flip** — chart and dealer book agree on the break line [CHART:head_shoulders][STRUCT:gex].
2. **Short gamma below spot** ($10 gex −8.69M): a close below $10 is self-reinforcing toward the $9.20 52w low — dealers sell into weakness [STRUCT:gex].
3. **The only bull lane has no edge:** bullish_flow backtests **37.5%** (n=8, avg −0.51%); a 5/5 sweep campaign that historically loses is not a buy signal [HIST:signal_backtest].
4. **Macro headwind:** hawkish FOMC dot-flip + TRANSITIONAL half-size regime is duration-negative for beaten-down software, and PATH is *not* in the +$9.36B Tech inflow [MACRO:FOMC_2026-06-17].

**reasons_against** — *the bull steelman (why not to short here):*
1. **DIVERGENT flow↔chart (top steelman, L-0002):** a 5-session ask-side bull sweep campaign, consistency **1.0**, $2.27M, contradicts the bearish chart outright — smart money is leaning the *other* way on the tape [FLOW:sweep_persistence].
2. **31.78% short float, DTC 3.78, CROWDED_SHORT** is squeeze fuel: in a short-gamma book a **reclaim of $10→$11 squeezes UP**, not down (ledger **L-0004** trap pattern) [SENT:short_float].
3. **Dark pool is NOT distributing** — large-tier buy_ratio 0.48 is balanced, not selling; there is no smart-money confirmation for a short [DP:block_stratified].
4. **Poor short R:R from here:** spot is only +9.5% above the 52w low and basing into a symmetrical triangle; ~$0.85 of room to the $9.20–9.45 shelf vs an $11 squeeze tail makes a fresh short a bad entry *before* the $10 break [CHART:support_resistance].

*Watchable flip trigger (reappears in invalidation):* **reclaim & hold > $11** negates the
bear tilt and arms the squeeze.

## Step 5 — level ladder (dual-confirmed preferred)

| Role | Level | Sources |
|------|-------|---------|
| Bull-reclaim ceiling | **$11.00–11.29** | max-pain/pin $11 [OI/STRUCT:max_pain] + heaviest resistance 11.29 ×6 [CHART] + fib 0.236 11.26 [CHART:fib_0.236] |
| Call wall (upside cap) | $12.00 | [OI] + chart 12.35 [CHART] |
| Interim resistance / fade | **$10.48–10.79** | chart 10.48 ×4 [CHART] + sma50 10.69 [CHART:sma50] + DP supply 10.79 [DP] |
| Spot | 10.27 | [CHART:spot] |
| **Decisive line / neckline / gamma flip / put wall** | **$10.00–10.23** | H&S neckline 10.07 [CHART:head_shoulders] + gamma flip/put wall $10 [STRUCT:gex] + DP support 10.23 [DP] |
| Breakdown shelf (bear target) | **$9.20–9.45** | 52w-low shelf 9.24/9.45 [CHART] + low_52w 9.38 |
| H&S measured tail | ~6.9 | H&S target 6.94 [CHART] ≈ fib ext 1.272 6.82 [CHART:fib] (tail, not base case) |
| Long stop (1.5 ATR) | $9.25 | [CHART:stops] |
| Short stop (1.5 ATR) | $11.29 | [CHART:stops] (= reclaim ceiling) |

## Step 6 — event calendar (goal #4)

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-07-15 | June CPI release | ? / − on hawkish print | [MACRO:CPI] |
| 2026-07-17 | July monthly OPEX (3rd Fri) | ? (pin/gamma roll-off near $11) | [OI:OPEX] |
| 2026-07-28 | FOMC (hike risk live) | − duration headwind | [MACRO:FOMC] |
| ~2026-09-03 | UiPath Q2 FY2027 earnings | ? (big vol event; screener 09-03 vs phase-6 ~09-08) | [FUND:next_earnings_date] |
| ongoing | Iran/energy → RISK-OFF tail | − | [MACRO:MarketRegime] |

No catalyst inside the 1–4w window → directional/long-vol option premium bleeds theta;
prefer cheap-defined-risk or spreads, not naked long premium.

## Invalidation (deep-dive rubric)

- **price:** two daily closes **< $10.00** → bear tilt **confirmed**, target $9.20–9.45;
  conversely **reclaim & hold > $11** → bear tilt **dead**, squeeze armed (bull trigger).
- **signal:** DP large-tier buy_ratio **< 0.45** (distribution → confirms short) OR
  sweep-persistence consistency **< 0.6** (bull pillar gone) OR cumulative premium flow net
  bearish 3 consecutive sessions [INSIGHT:institutional_accumulation].
- **macro:** hawkish surprise at June CPI (7/15) or FOMC (7/28) vs consensus, or RISK-OFF
  regime flip on Iran/energy [MACRO:FOMC_2026-06-17].

## Ledger lessons applied

- **L-0002 (ACTIVE):** DIVERGENT → capped at NEUTRAL/0.55, defined-risk only; divergence is the #1 reason_against.
- **L-0004 (CANDIDATE):** short-gamma + 32% SI + bull sweep → a *reclaim squeezes up*; the bear plan must be **trigger-gated and defined-risk**, never carry naked bearish premium into the squeeze fuel.
- **L-0001 (ACTIVE):** symmetrical triangle is low-confidence → require a **volume-confirmed** break and size at starter until two closes hold.

## Verdict for downstream

- `bias` = NEUTRAL (range, bearish-tilt-on-confirmation); `conviction` = 0.55; `horizon` = 1–4w
- `agreement` = **DIVERGENT** → A4 entry style = **trigger-gated, two-sided, defined-risk**
- Level ladder + events + invalidation as above; ≥4 distinct upstream lanes cited.
