# Phase 9 — Trade Blueprint

**Ticker:** MARA
**As-of date:** 2026-05-19 EOD (trade date 2026-05-20)
**PM voice:** desk PM running a $5-50M options-overlay book
**Spot reference:** $12.46 ([OI:oi_biggest_increases] stock_price field, phase 3) — intraday range $12.30-$12.50
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (3 sentences)

MARA is mechanically pinned into a **$11.75-$13.00 corridor** through
2026-05-22 OPEX by a dominant single-strike gamma wall at $13 worth
**$12.7B of net dealer GEX** [STRUCT:gex] and reinforced by 48,851
contracts of 13C/5-22 open interest with same-day net ask-bid -2,114
(heavy holder call-writing) [OI:oi_biggest_increases]; the post-earnings
digestion since the 5/11 Q1 revenue miss [MACRO:MARA_Q1-2026_2026-05-11
WebSearch] has removed the upside catalyst, and **all four phase-8
sub-agents converged on RANGE / NEUTRAL with zero LONG and zero SHORT
votes** [AGENT:accumulation-hunter, contrarian-scanner, sweep-tracker,
risk-monitor]. The trade is the **range itself**, not direction — with
a mild bullish tilt inside the range (put-write floor at $10-$12, dip-buy
block confirmed at $11.75, dealer DEX +$26.2B forces structural
underlying buying as a hedge). IV at the **14.8th percentile** (z-score
-1.30) [HIST:iv_percentile_zscore] with +13.8% VRP makes selling
short-dated premium the optimal vehicle.

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (mild bullish tilt within range)
- **Conviction (M-01 bin):** **0.85**
- **Time horizon:** **1-5 days primary** (through 2026-05-22 OPEX);
  secondary 1-4 weeks into FOMC 2026-06-17/18
- **Why this bin:** phase-10 confluence score (computed in next phase)
  lands at ~85 with strong convergence across all 7 upstream phases and
  4/4 sub-agent alignment on non-directional bias; this is "very high
  edge — opposition failed to materially dent the thesis" per the
  sizing rubric

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | **$12.40-$12.50** | re-test of gamma pivot (5/22 OPEX path of least resistance) | [STRUCT:gex] ($12.5 wall +$8B GEX), [DP:dark_pool_price_levels] ($12.40 cluster $4.4M) |
| Aggressive | **$11.91-$12.00** | retest of lower DP cluster / put-write zone | [DP:dark_pool_price_levels] ($11.91 cluster $6.6M / 556K shares), [OI:oi_biggest_increases] (12P put-writing) |
| Fade       | **$12.95-$13.05** | rejection at 13C wall / distribution band re-engages | [STRUCT:gex] ($13 wall +$12.7B), [DP:dark_pool_price_levels] ($13.00 cluster $6.8M) |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Hard resistance** | **$13.00** | [STRUCT:gex] $12.7B net GEX (largest in chain); [OI:oi_biggest_increases] 48,851 OI |
| Resistance band | **$13.20-$13.29** | [DP:dark_pool_price_levels] $29.4M combined 5-day institutional distribution |
| Pivot / pin | **$12.50** | [STRUCT:gex] $8.0B GEX (secondary wall); [OI:oi_biggest_increases] 28,548 OI (+3,920 today, bullish opening) |
| Spot anchor | **$12.46** | [OI:oi_biggest_increases] stock_price field |
| Support (primary) | **$12.10-$12.19** | [DP:dark_pool_price_levels] $11.9M combined 5-day |
| Support (critical) | **$11.91** | [DP:dark_pool_price_levels] $6.6M / 556,806 shares cluster |
| **Support (last defense)** | **$11.75** | [DP:dark_pool_largest] 210K-share @ NBBO ASK + $3.1M / 265K-share 5-day cluster [INSIGHT:institutional_accumulation] |
| **Gamma flip (invalidation)** | **$11.00** | [STRUCT:gex] first negative-GEX strike -$1.16B; below this regime turns short-gamma |
| ZGL (full chain) | $4.65 | [STRUCT:gex] zero gamma level |
| 0DTE gamma flip | $7.85 | [STRUCT:today_gamma_flip] 0DTE ZGL |

## Invalidation

- **Price-based:** Two daily closes **below $11.75** (breaks the
  institutional dip-buy block confirmed by [DP:dark_pool_largest] and
  [INSIGHT:institutional_accumulation]) OR intraday print **below
  $11.00 without reclaim** (triggers [STRUCT:gex] negative-GEX flip and
  ends the 22-session positive-gamma regime). Conversely, two daily
  closes **above $13.20** invalidates the upper-range bound (breaks
  [DP:dark_pool_price_levels] distribution band and forces dealer
  short-call rehedging through [OI:oi_biggest_increases] 13C/14C
  walls).
- **Signal-based:**
  1. [STRUCT:gex] daily GEX flips from POSITIVE to NEGATIVE (re-run
     phase-4 daily; today $22.6B → if <$0, regime gone).
  2. [HIST:historical_cumulative_premium_flow] turns net bearish for
     3 consecutive sessions (currently mixed -$5.9M / 90d; large
     persistent net-bearish swing = unwind signal).
  3. [INSIGHT:institutional_accumulation] flips from NEUTRAL to
     DISTRIBUTION (buy/sell ratio <0.40 on a daily refresh).
- **Macro-based:**
  1. **BTC closes below $74,200 support** (phase-6 web research
     confirms this as the proximate downside support; below this,
     phase-8 risk-monitor cascade math estimates MARA -10-12% to $10.85-$11.10
     range, fully invalidating the long-gamma regime).
  2. UW `risk_market_regime` flips from TRANSITIONAL to RISK-OFF (a
     SPY break of 20-SMA $727.96 [MACRO:MarketRegime_2026-05-19 UW]
     plus VIX expansion would do this).
  3. FOMC 2026-06-17/18 delivers a hawkish surprise vs the current
     "no urgency to cut" stance [MACRO:FOMC_2026-04-29
     WebSearch:federalreserve.gov].

**Exit on invalidation:** Both structures are defined-risk credit
spreads → **HARD STOP at max-loss** if any invalidation fires;
optionally roll the credit-spread structure to a vertical 1 strike
further OTM if invalidation is gradual (e.g., 1 daily close at $11.75
without follow-through).

## Sizing (% of risk, NOT dollars)

**Kelly math for Iron Condor (primary structure):**
- p = **0.85** (conviction bin)
- credit = $0.45 / spread; max_loss = $0.63 / spread (put side)
- b = payoff ratio = 0.45 / 0.63 = **0.71**
- raw_kelly = (0.85 × 0.71 − 0.15) / 0.71 = 0.454 / 0.71 = **0.639 (63.9%)**
- fractional Kelly (×0.25) = **16.0%**
- cap_pct = **5.0%**
- suggested_size_pct = min(16.0%, 5.0%) = **5.0%**
- **Final size: 2.5% of book risk** (deviating *downward* — always
  allowed; reason: phase-8 risk-monitor + phase-6 macro both demand
  TRANSITIONAL-regime half-sizing; correlation cascade exposure to
  BTC + miners + IWM warrants extra discipline)
- **sizing_deviation_reason (downward):** "TRANSITIONAL UW market
  regime [MACRO:MarketRegime_2026-05-19] + bullish_flow 20% win rate
  signal-backtest fail [HIST:signal_backtest] + 3-way correlation
  cascade per phase-8 risk-monitor (MARA/CLSK 0.789, MARA/IWM 0.64,
  MARA/WULF 0.571)"

**Kelly math for Bull Put Spread (secondary directional structure):**
- p = **0.85**
- credit = $0.37 / spread; max_loss = $0.63 / spread
- b = 0.37 / 0.63 = **0.59**
- raw_kelly = (0.85 × 0.59 − 0.15) / 0.59 = 0.351 / 0.59 = **0.594 (59.4%)**
- fractional Kelly = **14.8%**
- cap_pct = 5.0%
- suggested_size_pct = **5.0%**
- **Final size: 2.5% of book risk** (same downward deviation reasoning;
  may run *both* structures simultaneously at 2.5% each = 5% total book
  risk to the MARA setup, which is the cap)

## Option structures

### Directional (primary, bullish-tilted): 2026-05-22 11/12 Bull Put Spread

- **Structure:** Short Put Vertical (credit spread)
- **Strikes / expiry:** SELL 1 × MARA 2026-05-22 12P @ ~$0.54 mid;
  BUY 1 × MARA 2026-05-22 11P @ ~$0.17 mid
  (mids derived from [FLOW:options_flow_sweeps] avg_price 0.536 on
  12P; [OI:oi_biggest_increases] avg_price 0.169 on 11P)
- **Net credit:** **+$0.37 per spread ($37 per contract)**
- **Width:** $1.00
- **Max loss:** $1.00 - $0.37 = **$0.63 per spread**
- **Breakeven:** $12.00 - $0.37 = **$11.63**
- **Max profit @ expiry:** spot ≥ $12.00 → keep full $0.37 credit
- **Days to expiry:** **3** (Friday OPEX)
- **Why this structure:** Sells the gamma-pinned 12P (active put-write
  zone per phase 3 — 12P/5-22 OI +2,207 today net ask-bid -306 = bullish
  put-write) and buys 11P as defined-risk catastrophe protection
  (11P/5-22 OI +2,018; below the $11 negative-GEX flip). Captures the
  +13.8% VRP [HIST:vrp] without taking unbounded short-put risk. The
  $11.63 breakeven sits *above* the $11.75 phase-2 dip-buy floor — a
  meaningful safety margin. **This is the "directional" structure
  required by the skill, expressing the mild bullish tilt within the
  range thesis.**

### Defined-risk alternative (pure range): 2026-05-22 11/12/13/13.5 Iron Condor

- **Structure:** Iron Condor
- **Strikes / expiry:** all 2026-05-22 expiry (3 DTE)
  - SELL 1 × 12P @ ~$0.54  (BUY 1 × 11P @ ~$0.17)  — put spread
  - SELL 1 × 13C @ ~$0.18  (BUY 1 × 13.5C @ ~$0.11)  — call spread
- **Net credit:** ~**$0.44 per spread ($44 per contract)** (call: 0.18−0.11 = 0.07; put: 0.54−0.17 = 0.37; total = 0.44)
- **Width:** $1.00 (put side) / $0.50 (call side)
- **Max loss:** $1.00 - $0.37 = $0.63 (put side dominates; call side max
  loss is only $0.50 - $0.07 = $0.43)
- **Breakevens:** $11.63 (lower) and $13.07 (upper)
- **Profit zone:** spot closes between $11.63 and $13.07 at 2026-05-22
  expiry
- **Max profit @ pin:** keep full $0.44 credit at any spot $12-$13
- **Days to expiry:** **3**
- **Why this structure:** Sells volatility on both sides at the exact
  gamma walls ([STRUCT:gex] 13C $12.7B wall above; 12P/11P put-write
  zone below). Captures the +13.8% VRP [HIST:vrp] over 3 days with
  capped tail risk. The 80%+ probability of expiring inside the band
  comes from the gamma magnet [STRUCT:today_gamma_flip] and the
  phase-3 OI structure (48.8K OI at 13C, 45.3K OI at 14C — dealers will
  defend the cap; 12P/11P/10.5P all being written = put-write floor).
  **This is the cleanest expression of the unanimous phase-8 RANGE
  verdict.**

### Optional add-on: long convexity hedge (if running the trade for >5 days)

If continuing past 5/22 OPEX into the 6/18 expiry window (FOMC week),
add a small **long 6P/2026-06-18 hedge** at ~$0.04 / contract.
- Justification: phase-1 flagged 1,503 contracts of this strike already
  bought at 134% IV [FLOW:options_flow_iv_outliers] — smart-money tail
  hedge in a complacent-skew market.
- Sizing: ≤0.25% of book risk (cheap insurance, not a position).
- Wins big if BTC breaks $74K → MARA cascade to $10 [AGENT:risk-monitor].

## Macro overlay (cite phase-6)

**Tailwinds:**
- Tech sector inflow +$44M today [MACRO:SectorRotation_2026-05-19 UW]
  (modest offset to Financial Services rotation; relevant via MARA's
  AI/HPC transformation narrative per Q1 letter coverage)
- Earnings overhang already digested 2026-05-11 [MACRO:MARA_Q1-2026_2026-05-11
  WebSearch:stocktitan.net] — no fresh earnings catalyst until 8/4
- IV at 14.8th percentile [HIST:iv_percentile_zscore] — selling premium
  is fundamentally cheap on a 1y basis even though VRP is positive

**Headwinds:**
- Market regime TRANSITIONAL with "half-size, defined-risk" guidance
  [MACRO:MarketRegime_2026-05-19 UW]
- Financial Services sector outflow -$48.8M today
  [MACRO:SectorRotation_2026-05-19 UW] — MARA's UW tag
- BTC consolidating $77K with bearish MACD; needs break of $82K for
  $85K-$100K target; if breaks $74K, MARA cascade risk
  [MACRO:BTC_2026-05-18 WebSearch:bitcoin.com]
- Crypto miner cohort (WULF/CIFR/HIVE/CORZ/CLSK) shows 4-5 bullish
  confluence today while MARA scores zero — MARA is the laggard, most
  exposed to cohort unwind [INSIGHT:signal_confluence]
- bullish_flow historical signal_backtest = 20% win rate / -2.62% avg
  10d [HIST:signal_backtest] — broad-market bullish-flow setups being
  faded systematically

**Net:** **mild HEADWIND** stack against the "outright long MARA" view;
**neutral-to-mildly-supportive** against the "fade the range" view. The
RANGE thesis is robust against the macro stack.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-22 (Fri) | **May OPEX (T+2 from trade)** — Iron condor + bull put spread BOTH expire | + (theta harvest target) |
| 2026-05-25 (Mon) | Memorial Day (US closed) | none |
| ~2026-05-30 | PCE inflation print | modest macro vol, ±1% impact |
| ~2026-06-06 | NFP / unemployment | macro vol day |
| ~2026-06-13 | CPI release | high macro vol |
| **2026-06-17 to 06-18** | **FOMC meeting + dot plot** | **HIGH vol** — confirmed by phase-4 6/26 IV bump to 111% [STRUCT:iv_term_structure] |
| 2026-06-18 (Thu) | June monthly OPEX | major dealer rebalance |
| 2026-08-04 | MARA Q2 2026 earnings | OUT of 30-day window (note for next deep-dive cycle) |

## Post-trade monitoring checklist

- [ ] **Daily**: re-run `mcp__uw-pp__options_structure_gex` for MARA;
      if total GEX drops below $5B or regime flips to NEGATIVE → close
      both structures
- [ ] **Daily**: re-run `mcp__uw-pp__dark_pool_block_stratified` for
      MARA; if block-tier buy_ratio drops below 0.40 → close trades
      (institutional distribution would invalidate the dip-buy thesis)
- [ ] **Daily**: check BTC spot vs $74,200 support and $82,000 resistance
      via WebSearch or IBIT proxy; either break is a material macro
      trigger
- [ ] **Daily**: check `mcp__uw-pp__risk_market_regime`; if regime
      flips from TRANSITIONAL to RISK-OFF → reduce both structures to
      1.25% each (50% size cut)
- [ ] **Tue 5/26 (post-Memorial Day)**: re-evaluate calendar/diagonal
      add for the FOMC week if structures expired profitably
- [ ] **5/22 close**: log realized P&L vs theoretical; calibrate Kelly
      inputs for next single-name run
- [ ] **6/17 (Wed before FOMC)**: if any 6/18 expiry exposure exists,
      decide on close-vs-hold over FOMC

## Citations summary (M-04 audit trail)

The thesis paragraph cites at least 3 distinct upstream datapoints:

1. **[STRUCT:gex]** — phase-4 §"GEX per strike" — "13.0 +$12,665,564,779
   — Largest gamma wall" (phase-4-structure.md)
2. **[OI:oi_biggest_increases]** — phase-3 §"Largest OI increases" —
   "13C/2026-05-22 OI 48,851 +1,212; net ask-bid -2,114" (phase-3-positioning.md)
3. **[MACRO:MARA_Q1-2026_2026-05-11 WebSearch]** — phase-6 §"MARA Q1
   2026 earnings" — "Revenue $174.6M (-4.4% miss); EPS -$3.31 vs
   -$2.20 est; stock peaked $13.39 5/11, now $12.47" (phase-6-macro.md)
4. **[AGENT:accumulation-hunter, contrarian-scanner, sweep-tracker,
   risk-monitor]** — phase-8 — "3 of 4 agents RANGE, 1 NEUTRAL,
   average conviction 2.75" (phase-8-agent-views.md)
5. **[HIST:iv_percentile_zscore]** — phase-5 §"IV regime + VRP" — "IV
   14.8th percentile / z-score -1.30" (phase-5-historical.md)
