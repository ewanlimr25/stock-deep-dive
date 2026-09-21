# Phase 9 — Trade Blueprint

**Ticker:** LRCX
**As-of date:** 2026-05-18 (data: 2026-05-15)
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $284.51 close 5/15 (phase-1, phase-7)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

LRCX is a **fade-the-rally short into 5/22 OPEX week**: institutions
distributed $1.36B of stock into the $289–$300 dark-pool shelf last week
**[DP:price_levels]** while simultaneously building a $11M+ post-earnings
call-overwrite at 8/21 310/400 **[OI:biggest_increases]**, and a
post-rally **price-vs-flow divergence is now flashing** (+29% price /
-$2.2M bearish flow / IV rank 72) **[INSIGHT:price_vs_flow]** with the
historical bearish-flow signal at 100% win and -6.76% in semi peers over
20d **[HIST:signal_backtest]**. The catalyst is named and concrete —
**Samsung Electronics strike begins 2026-05-21**, which is what 5/22 IV
74.5% backwardation is already pricing **[MACRO:Samsung_strike_2026-05-15
WebSearch:tradingkey.com], [STRUCT:front_end_iv_ratio]**. Trade premise:
sell the institutional wall at $295.44 and buy downside into the $260
gamma hole over 1–4 weeks.

## Bias + conviction + horizon

- **Directional bias:** **SHORT** (plurality of phases 1-8: 2 SHORT + 2
  NEUTRAL agents accepting the SHORT framework; 0 LONG voters in phase-8)
- **Conviction (M-01 bin):** **0.75**
- **Time horizon:** **1-4w** (covers 5/21 strike start → 5/22 OPEX →
  6/18 OPEX; stays clear of 6/16-17 FOMC if exit is early)
- **Why this bin (phase-10 preview):** pre-computed confluence score
  ≈87 → maps to 0.85 band per `rubrics/confluence-scoring.md`. **See
  `## Conviction deviation` below for the downgrade to 0.75.**

### Conviction deviation

Pre-computed phase-10 confluence score is **87** (raw +85 normalized),
which maps to the **0.85 bin** per the rubric. I am deviating downward
to **0.75** because:

1. **Phase-8 NEUTRAL dissent is a sizing dissent, not a direction
   dissent** — contrarian-scanner and sweep-tracker both explicitly
   refuse to size up the short despite agreeing with $295.44 resistance.
   The 0.85 bin requires "opposition failed to materially dent the
   thesis"; here the opposition DID dent it on sizing.
2. **Phase-4 long-gamma regime (+$109M GEX, ZGL $70.78) structurally
   buffers downside** — dealers buy dips, suppressing realized vol. The
   $260 gamma hole only opens if $280 cracks; until then the path to
   the target is slow.
3. **Samsung-strike "sell the rumor, buy the news" trap** — strike
   resolution between 5/21 and 5/22 OPEX could collapse 5/22 IV from
   74.5% → 65%, triggering vanna-driven dealer buying (-49k net vanna
   from phase-4) and a squeeze back to $295.

Net: the data alignment is real, but **sizing risk is asymmetric to the
upside** in the near term. 0.75 is the honest bin.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | $289–$291 | First bounce into the 5-day cluster shelf (5d cluster at $289.24 = $361M premium); supply re-engages | [DP:price_levels], [OI:biggest_increases] 8/21 290C |
| **Aggressive** | $294–$296 | Tag of the $295.44 institutional wall with rejection (closing red below); aligned with 5/22 295C bid-side $1.13M write | [DP:price_levels], [FLOW:sweeps] |
| **Fade (counter)** | Reclaim $292 from below on rising volume AND bullish-flow flip | If primary thesis breaks: SHORT exits and the LONG re-entry zone is a reclaim of $295.44 with confirming flow | [INSIGHT:price_vs_flow] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Support 1** | **$280** (gamma node +$30.5M, phase-4 largest positive 45-DTE GEX strike) | [STRUCT:gex] |
| **Support 2 (target)** | **$260** (-$53.5M GEX hole, also Jan'27 260P bid $1.03M, 5/22 260P OI 6,653) | [STRUCT:gex], [FLOW:top_premium_trades] |
| **Resistance 1** | **$289.24** (5d DP cluster $361M) | [DP:price_levels] |
| **Resistance 2 (primary)** | **$295.44** (5d DP cluster $627M, 5/22 295C write strike) | [DP:price_levels], [FLOW:sweeps] |
| **Resistance 3 (ceiling)** | **$310** (8/21 310C +1,503 OI write, post-earnings cap) | [OI:biggest_increases] |
| Gamma flip (ZGL) | $70.78 (far below — informational only; means deeply in long-gamma regime) | [STRUCT:gex] |
| Largest pin (5/22 OPEX) | **NONE** — LRCX not in `oi_pin_risk` top-25 | [OI:pin_risk] |
| Vol pivot | 5/22 IV 74.5% vs 6/18 67.8% (ratio 1.099 = BACKWARDATION); collapse > 1.05 → bullish dealer mechanics | [STRUCT:front_end_iv_ratio] |

## Invalidation

- **Price-based:** Two daily closes above **$295.44** (5-day DP wall);
  OR an intraday print above $300 with no immediate reclaim of $295.
  Either triggers full close on the directional structure.
- **Signal-based:** (a) **Net DEX flips sharply more positive** on
  phase-4 daily refresh with spot rallying (would indicate fresh call
  buying, not writing) [STRUCT:dex]; OR (b) `historical_cumulative_premium_flow`
  flips net bullish for 3 consecutive sessions [HIST:cumulative_premium_flow];
  OR (c) `insights_conviction_matrix` flips from MIXED to DIRECTIONAL_LONG
  [INSIGHT:conviction_matrix].
- **Macro-based:** (a) **Samsung Electronics strike averted, paused, or
  resolved publicly before 5/21**
  [MACRO:Samsung_strike_2026-05-15 WebSearch:tradingkey.com]; OR
  (b) UW `risk_market_regime` flips from TRANSITIONAL to RISK-ON
  [MACRO:MarketRegime_2026-05-15 UW]; OR (c) a meaningfully dovish
  surprise from the 6/16-17 FOMC reverses the discount-rate headwind
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].

**Exit on invalidation:**
- Directional structure (long put): **hard stop, close 100% at price
  invalidation; tranche 50/50 at signal vs macro invalidation**.
- Credit spread: **close or roll** to next expiry if 5/22 295/305
  short call goes ITM with > 7 calendar days to expiry; close 100% at
  price invalidation.

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:**
  - p = **0.75** (conviction bin, deviation noted)
  - Long-put entry $290, target $260, stop $296
  - b = |entry − target| / |stop − entry| = |290 − 260| / |296 − 290|
    = 30 / 6 = **5.00**
  - fraction = 0.25 (fractional Kelly)
- **Raw Kelly:**
  - raw_kelly = (p × b − (1 − p)) / b
  - = (0.75 × 5.00 − 0.25) / 5.00
  - = (3.75 − 0.25) / 5.00
  - = 3.50 / 5.00
  - = **0.70 (70% of edge — large because b is high)**
- **Suggested size:** 0.70 × 0.25 × 100 = **17.5%** of book risk
- **Cap binds:** cap_pct = 5
- **Final size: 5% of book risk** (Kelly suggests more; cap is the
  binding constraint, no deviation upward).
- **Deviation reason (upward):** none. The cap binds at 5%.

For the **credit spread alternative**, the max loss per contract
($7.50 × 100 = $750) must be sized so that the total max loss across
all contracts ≤ 5% of book risk. On a $1M book that's 66 contracts;
on a $10M book, 666 contracts. Scale linearly.

## Option structures

### Directional (primary) — Long put

- **Structure:** Long 6/18 290P
- **Strike(s) / expiry:** 1× **2026-06-18 LRCX 290 put**
- **Debit (est):** ~**$17–18** (using 6/18 IV ~67.8% from `[STRUCT:iv_term_structure]`,
  31 DTE, ATM-leaning; reference 6/18 270P @ $11.72 from
  `[OI:decrease_with_volume]` and 6/18 310P @ $36.66 from
  `[FLOW:sweeps]`; 6/18 290P interpolates around $17)
- **Breakeven:** $290 − $17.50 = **$272.50**
- **Max loss:** debit paid (≈ $17.50/contract = $1,750)
- **Max gain:** $290 − $0 − $17.50 = $272.50 if it goes to zero by
  6/18; realistic exit at $260 target = $30 − $17.50 = **$12.50/contract
  (71% of debit)**
- **Why this structure:** IV rank 72 [HIST:iv_percentile_zscore] is
  rich, so a long put pays for vol — but the **vega exposure is offset
  by phase-4's vanna negativity**: if IV stays bid through 5/22 the
  put gains; if IV crushes, the 6/18 long-dated tenor mutes the damage
  vs a 5/22 put. Captures the $260 gamma hole [STRUCT:gex] with
  31 DTE of room.

### Defined-risk alternative — Bear call spread (premium-sell)

- **Structure:** 5/22 **295/305 bear call credit spread**
- **Strike(s) / expiry:** Sell 1× **2026-05-22 LRCX 295C**, Buy 1×
  **2026-05-22 LRCX 305C** (same ratio; 10-wide)
- **Credit (est):** ~**$2.50** (5/22 295C avg $7.21 bid-side from
  `[FLOW:top_premium_trades]`; 5/22 305C est ~$4.50 by interpolation
  from 5/22 300C avg $6.10 in `[FLOW:top_premium_trades]` and 5/22
  330C avg ~$0.50 from `[OI:biggest_increases]`-adjacent prints)
- **Breakeven:** $295 + $2.50 = **$297.50**
- **Max loss:** $10 − $2.50 = **$7.50/contract = $750**
- **Max gain:** $2.50 = **$250/contract** (33% of width)
- **Why this structure:** sells into the **two compounding edges**:
  (a) the $295.44 institutional dark-pool wall [DP:price_levels]
  doubles as the call-write strike from phase-1 [FLOW:sweeps]; and
  (b) the 5/22 IV at 74.5% has a 7-point premium over 6/18 IV
  [STRUCT:front_end_iv_ratio] that will collapse no matter how the
  Samsung strike plays out — IV crush is a near-tautological gain over
  4 calendar days. Pairs with **VRP +8.9% premium-selling regime**
  [HIST:vrp].

## Macro overlay (cite phase-6)

**Tailwinds (modest, all medium/long-term):**
- WFE 2026 sector growth **+9% YoY to $135B** [MACRO:WFE_2026 WebSearch:semi.org].
- LRCX Q3 fiscal earnings beat **$1.47 vs $1.36 (+8.1%)** on 2026-04-22
  [MACRO:LRCX_earnings_2026-04-22 WebSearch:marketbeat.com].
- June quarter guidance **$6.60B ±$400M revenue, $1.65 ±$0.15 EPS**
  intact [MACRO:LRCX_earnings_2026-04-22 WebSearch:quartr.com].

**Headwinds (acute, near-term):**
- **Samsung Electronics strike begins 2026-05-21**
  [MACRO:Samsung_strike_2026-05-15 WebSearch:tradingkey.com] — the
  proximate catalyst.
- **Tech sector outflow -$151M on 5/15 (largest single-sector outflow)**
  [MACRO:MarketRegime_2026-05-15 UW].
- **Market regime TRANSITIONAL** ("reduce position size, wait for
  clarity") [MACRO:MarketRegime_2026-05-15 UW].
- **CPI YoY +3.8% April, up from 3.3%** [MACRO:CPI_2026-04 WebSearch:cnbc.com] —
  hottest since May 2023, defers rate cuts.
- **FOMC forecasts only 1 cut in 2026** [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- **China = ~33% of global WFE with 50%-local-equipment policy**
  [MACRO:WFE_2026 WebSearch:yolegroup.com] — structural revenue
  concentration risk.

**Net:** **NEAR-TERM HEADWIND**, medium-term mixed-to-tailwind. The
trade horizon (1-4w) sits squarely inside the headwind window.

## Catalyst calendar (next 30d)

| Date | Event | Source | Impact direction |
|------|-------|--------|------------------|
| **2026-05-21** | **Samsung Electronics strike begins** | WebSearch:tradingkey.com | **(-)** acute headwind, the proximate catalyst |
| **2026-05-22** | **Weekly OPEX (Friday)** | calendar | (kinked IV 74.5%); short-side IV crush captured by credit spread |
| 2026-06-11 (est) | May CPI release | BLS schedule | (?) if hot, multi-compression for Tech |
| 2026-06-13 (est) | May PPI release | BLS schedule | (?) input-cost read |
| **2026-06-16–17** | **FOMC June meeting** | Fed calendar | **(?)** binary; possible dot-plot revision |
| **2026-06-18** | **Quarterly OPEX** | calendar | major gamma flush (target exit window for 6/18 puts) |
| 2026-07-29 or 08-05 | LRCX Q4 fiscal 2026 earnings | Company | outside trade horizon; 8/21 IV bump captures this |

## Post-trade monitoring checklist

- [ ] **Daily 4pm:** re-pull `mcp__uw-pp__options_structure_gex` and
      `mcp__uw-pp__options_structure_dex` — flag any net-DEX flip more
      positive or GEX regime flip [STRUCT:gex, STRUCT:dex].
- [ ] **Daily:** re-pull `mcp__uw-pp__historical_cumulative_premium_flow`
      with `days=5` — exit if net flow flips bullish 3 sessions in a row
      [HIST:cumulative_premium_flow].
- [ ] **Daily:** re-pull `mcp__uw-pp__insights_conviction_matrix` — exit
      if flips from MIXED to DIRECTIONAL_LONG [INSIGHT:conviction_matrix].
- [ ] **Daily (until 5/22):** track 5/22 IV vs 6/18 IV via
      `options_structure_front_end_iv_ratio` — credit spread thesis is
      explicitly the collapse of this kink [STRUCT:front_end_iv_ratio].
- [ ] **News scan 5/19–5/22:** Samsung Electronics strike status. Any
      resolution headline = exit credit spread fast (IV crush flips against
      gamma); long put can stay on but downgrade size.
- [ ] **Watchlist correlation check:** monitor SMH, AMAT, MU, INTC for
      sympathetic moves — if any one of them breaks down through analogous
      support, LRCX likely follows (risk-monitor flag).
- [ ] **Sizing discipline:** if any other semi-short is added to the book,
      cap aggregate semi exposure at half of single-name max (risk-monitor's
      portfolio constraint [AGENT:risk-monitor]).

## Citations summary

The thesis paragraph cites ≥3 distinct upstream datapoints (M-04
requirement). Listed here for phase-10 audit spot-check:

1. **[DP:price_levels]** — "$1.36B distributed into $289–$300 shelf
   last week, $295.44 = $627M / 2.12M shares / 65 trades cluster" →
   `phase-2-dark-pool.md` §Detailed findings → 5-day price-level
   clusters table.
2. **[OI:biggest_increases]** — "8/21 310C +1,503 OI, 8/21 400C +2,007
   OI, $11M+ post-earnings call-overwrite" → `phase-3-positioning.md`
   §Largest OI increases table.
3. **[INSIGHT:price_vs_flow]** — "+29% price, -$2.2M bearish flow, IV
   rank 71.97, divergence=TRUE" → `phase-7-insights.md` §Price vs flow.
4. **[HIST:signal_backtest]** — "bearish-flow signal 100% win rate,
   semi cohort avg -6.76% over 20d" → `phase-5-historical.md`
   §Signal backtest table.
5. **[MACRO:Samsung_strike_2026-05-15 WebSearch:tradingkey.com]** —
   "Samsung Electronics strike begins May 21, 2026" →
   `phase-6-macro.md` §LRCX-specific catalysts and §Catalyst
   calendar.
6. **[STRUCT:front_end_iv_ratio]** — "5/22 IV 74.5% / 6/18 IV 67.8%,
   ratio 1.099 = BACKWARDATION" → `phase-4-structure.md` §Front-end
   IV ratio.
7. **[STRUCT:gex]** — "Total +$109M GEX, ZGL $70.78, biggest negative
   GEX hole at $260 = -$53.5M" → `phase-4-structure.md` §GEX (45 DTE).
8. **[STRUCT:dex]** — "Net DEX +$9.3B, dealers short-call → buy
   underlying" → `phase-4-structure.md` §DEX (45 DTE).
9. **[FLOW:top_premium_trades]** — "5/22 295C bid-side $0.92M, 5/22
   300C bid-side $0.97M" → `phase-1-flow.md` §Largest premium prints.
10. **[AGENT:accumulation-hunter]** — "Yield-harvest over-write, not
    stealth bid" → `phase-8-agent-views.md` §accumulation-hunter
    verdict block.
