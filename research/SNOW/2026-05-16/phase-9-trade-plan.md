# Phase 9 — Trade Blueprint

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date 2026-05-15)
**PM voice:** desk PM running a $5-50M options-overlay book
**Spot reference:** $157.625 close 2026-05-15 (phase-1-flow.md / phase-5-historical.md)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and structures are illustrative.*

## Thesis (≤3 sentences)

SNOW is being **distributed at the share level while options bulls pay 92nd-percentile premium**, and the very pattern firing today has a **20% historical win rate over 5d** [HIST:signal_backtest]. The phase-4 dealer structure pins spot toward the **$160 GEX magnet** (+$2.31B net GEX) [STRUCT:gex] inside a positive-gamma regime that is **only 2 sessions old**, so the cleanest expression is to **SELL the 5/29 IV crush around the $150-$180 institutional range** [STRUCT:iv_term_structure, OI:biggest_increases] and own a **defined-risk hedge against a positive earnings squeeze toward $170** [STRUCT:gex, AGENT:sweep-tracker]. The plurality of the desk (4 of 5 phase-8 agents) endorses this; the lone LONG (sweep-tracker) targets the same $160 magnet for a short-horizon trade [AGENT:sweep-tracker].

## Bias + conviction + horizon

- **Directional bias:** **RANGE / SHORT-VOL** (with a tactical short-bias overlay above $160).
- **Conviction (M-01 bin):** **0.75**.
- **Time horizon:** **1-4w** (through 2026-05-27 earnings + 5/29 IV crush).
- **Why this bin:** phase-10 will likely score confluence in the 80-89 band (5 of 7 upstream phases are `++` or `+`, BLOCK-tier DP and signal backtest are decisive, but phase-1 contradicts and GEX regime is fresh). I deviate **DOWN** to 0.75 — see `## Conviction deviation`.

## Conviction deviation

Setting conviction to **0.75** rather than the 0.85 implied by phase-10's likely confluence score because:
1. **Binary event risk:** 2026-05-27 SNOW earnings is a hard, unbounded fat-tail event (phase-6 catalyst calendar). Confluence math doesn't price unknown reaction asymmetry.
2. **GEX regime is 2 sessions old** with a one-day flip-and-revert precedent (2026-04-29 → 2026-04-30) [HIST:gex_time_series]. The dealer-hedge mechanics underpinning the $160 magnet thesis could flip on Monday 5/18.
3. **Phase-8 agent average conviction is 2.6/5 = 0.52** — the analyst desk is collectively more humble than a pure 7-phase confluence score implies. I split the difference at 0.75.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | $157-$160 | Iron condor on tag of the $160 gamma magnet OR pullback to $157 (5/15 close) | [STRUCT:gex] |
| Aggressive | $162-$165 | Stretch above $162.50 dealer wall complex on light volume → SELL into the strength, condor extends short-call legs to $185 | [STRUCT:gex] |
| Fade | $151-$152.50 | Tag of 5-day DP absorption cluster → tighten the iron condor by rolling short-put leg DOWN to $145 (gain credit + extend range) | [DP:price_levels] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Primary support | **$151-$152.50** | [DP:price_levels] 5-day cluster $54M absorbed at $151.46-$152.94 |
| Secondary support | $150.74 | [DP:price_levels] / [OI:biggest_increases] coincides with 5/22 150P put-write build |
| **Hard regime invalidation** | **$154.56** | [STRUCT:gex] Zero Gamma Level — below this dealers flip short-gamma, vol expands |
| Primary resistance | **$160** | [STRUCT:gex] $2,311M net GEX wall — single largest absorbing strike |
| Secondary resistance | $170 | [STRUCT:gex] $855M net GEX wall |
| Call-write headwind | $180 | [OI:biggest_increases] 6/18 180C +929 OI bid-side built (institutions short calls) |
| Tail resistance | $200 | [OI:biggest_increases] 5/29 + 6/18 200C combined ~9,039 OI bid-side built |
| Largest pin (5/15 OPEX) | n/a (SNOW absent from pin_risk top 25) | [OI:pin_risk] |

## Invalidation

- **Price-based:** Two consecutive daily closes **below $154.56** (the ZGL) [STRUCT:gex]. This breaks the long-gamma dealer regime that underpins the $160 magnet thesis. Single-day breach with reclaim same session does NOT trigger.
- **Signal-based:** Phase-4 GEX prints **NEGATIVE** on the next-day refresh (regime flip), OR phase-5 cumulative_premium_flow turns net BEARISH for 3 consecutive sessions [HIST:cumulative_premium_flow]. Either fires → close 50% of the iron condor and re-evaluate.
- **Macro-based:** **2026-05-27 SNOW earnings**: any post-print spot move **outside $145-$185** (the iron condor's profitable range minus a $5 buffer) invalidates the thesis automatically — but this is a known, scheduled event captured in the structure's max-loss.

**Exit on invalidation:** **TRANCHE** — close 50% of the condor on first invalidation trigger (price or signal), close remaining 50% on confirmation of the second.

## Sizing (% of risk, NOT dollars)

**Iron condor (primary structure) Kelly math:**
- **Kelly inputs:** p = 0.75 (conviction bin), b = credit/max_risk
- **Expected mids (5/29 expiry, IV 107.6%):**
  - Sell 150P ≈ $6.00, Buy 140P ≈ $2.50 → put-side credit $3.50, put-side max risk $6.50
  - Sell 180C ≈ $4.00, Buy 190C ≈ $2.00 → call-side credit $2.00, call-side max risk $8.00
  - **Net credit ≈ $5.50, max loss either side ≈ $4.50** (width $10 − credit $5.50)
- **Payoff ratio:** b = $5.50 / $4.50 = **1.222**
- **Raw Kelly:** (0.75 × 1.222 − 0.25) / 1.222 = (0.917 − 0.25) / 1.222 = **0.546 = 54.6%**
- **Fractional Kelly (0.25):** 54.6% × 0.25 = **13.6%**
- **Hard cap:** **5.0% of book risk** in max-loss terms.
- **Final size:** **5.0%** of book risk (capped).
- **Deviation reason:** none (we cap, not exceed).

If book max-loss-risk budget is $1M, max condor loss = $50k → ~111 contracts (111 × $4.50 × 100 = $49,950). If $5M, ~555 contracts.

## Option structures

### Directional (primary) — bear call spread, 5/29

The trade within the SHORT-VOL thesis that is purely directional-short (no put-side):

- **Structure:** **Bear call vertical spread (sell-the-rip on the upper bound)**
- **Strike(s) / expiry:** **Short 175C / Long 195C, expiry 2026-05-29**
- **Estimated debit/credit:** **Net credit ≈ $4.50** (short 175C ~$6 − long 195C ~$1.50)
- **Breakeven (at expiry):** **$179.50** (short strike $175 + credit $4.50)
- **Max profit:** **$4.50** per spread (full credit retained if SNOW ≤ $175 at 5/29)
- **Max loss:** **$15.50** per spread (width $20 − credit $4.50)
- **Why this structure:** $175-$180 is the dealer call-write headwind from phase-3 (6/18 180C OI +929 bid-side). Spot has to rally **+11%** in 14 days through the $160 GEX magnet AND through $170 secondary wall to even reach the short strike. IV percentile 92 means we are SELLING rich premium [HIST:iv_percentile_zscore]. Defined-risk variant of "fade the bullish flow." Negative-skewed Kelly because of the asymmetric risk/reward — use this only if book has appetite for a single-sided fade with limited absolute upside.

### Defined-risk alternative — iron condor 5/29 (THIS IS THE PRIMARY TRADE)

- **Structure:** **Iron condor** (short strangle with wing protection)
- **Strike(s) / expiry:** **Long 140P / Short 150P / Short 180C / Long 190C, expiry 2026-05-29**
- **Estimated debit/credit:** **Net credit ≈ $5.50** per spread
- **Breakevens (at expiry):** **$144.50 (down)** and **$185.50 (up)**
- **Max profit:** **$5.50** per spread (kept in full if SNOW closes between $150 and $180 on 5/29)
- **Max loss:** **$4.50** per spread (10pt width − $5.50 credit, either side fully ITM)
- **Why this structure:** Captures **VRP +13.3%** (phase-5) and the IV rank 97 (phase-5) into the 5/27 earnings IV crush. Short strikes anchor at phase-3 OI clusters (150P institutional put-write, 180C institutional call-write — we are aligned WITH the same institutions). Long wings cap risk through the binary earnings event. Maximum profit zone ($150-$180) is exactly the range phase-8 agents agreed on. The $160 GEX magnet from phase-4 sits centrally inside the profitable range.

### Optional contrarian alternative (NOT primary) — long call spread 6/26

For book members who agree with **sweep-tracker** that the phase-1 $145C-buyer is constructing a 145/210 call spread for 6/26 and want to ride alongside:

- **Structure:** Long call vertical (debit) spread
- **Strike(s) / expiry:** **Long 145C / Short 210C, expiry 2026-06-26**
- **Estimated debit:** $22.30 (145C avg ask, phase-1 sweep) − $3.08 (210C avg, phase-3 OI) ≈ **$19.20**
- **Breakeven:** **$164.20** at expiry
- **Max profit:** **$45.80** per spread (width $65 − debit $19.20) — capped at $210
- **Max loss:** **$19.20** (debit)
- **Why this is NOT the primary:** it ignores phase-5's 20% bullish_flow win rate, fights phase-2's BLOCK-tier distribution, and pays full 81% IV premium right before earnings IV crush. ONLY use if you specifically believe sweep-tracker's "same actor constructed the spread" thesis and are willing to size half against the desk's plurality.

## Macro overlay (cite phase-6)

- **Tailwinds (modest):**
  - AI Data Cloud product narrative intact (Dataiku Cobuild, Bedrock Data, Valid Systems, OSI leadership) [MACRO:SNOW_news_2026-05-15 WebSearch].
  - SPY uptrend, +5.35% 30d, above 20/50 SMAs [MACRO:MarketRegime_2026-05-15 UW].
  - SNOW YTD -28% provides oversold context — analyst PTs still 40-70% above spot [MACRO:RBC_PT_2026-05-15 WebSearch].

- **Headwinds (dominant):**
  - **UW regime TRANSITIONAL — "half position sizes"** [MACRO:MarketRegime_2026-05-15 UW].
  - **Technology sector outflow -$151M on 5/15** (largest sector outflow on tape) [MACRO:SectorRotation_2026-05-15 UW].
  - **April CPI YoY 3.8% (highest since May 2023), Core 2.8%** [MACRO:CPIAUCSL_2026-04 WebSearch:cnbc.com].
  - **10y Treasury 4.59% (+10bps, one-year high)** — duration headwind for high-multiple growth [MACRO:DGS10_2026-05-15 WebSearch:advisorperspectives].
  - **RBC PT cut $245 → $220 on 5/15** [MACRO:RBC_PT_2026-05-15 WebSearch].

- **Net:** **HEADWIND** — supportive of the RANGE/short-vol thesis (no macro catalyst to drive SNOW above the $180 short call strike absent an earnings beat). Macro tilt reinforces the iron condor and the bear call spread.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| 2026-05-21 AMC | WDAY, ZM, TTWO earnings (software cohort) | Sympathy + / − for SNOW |
| 2026-05-26 AMC | **ZS earnings** | **Direct cohort tell** for SNOW IV direction next day |
| **2026-05-27 AMC** | **SNOW Q1 FY27 earnings, ~$1.32B revenue consensus** | **BINARY** — implied move ±9-12% from 5/29 IV |
| 2026-05-28 AMC | OKTA, DLTR, BBY earnings | Cohort fadeout day |
| 2026-06-05 (likely) | May NFP | Labor strength → multiples headwind |
| 2026-06-13 (likely) | May CPI release | Inflation continuation risk |
| 2026-06-16-17 | FOMC + SEP | Hawkish surprise risk |

## Post-trade monitoring checklist

- [ ] **Daily**: re-pull `options_structure_gex` for SNOW. If GEX flips NEGATIVE or ZGL moves above spot → close 50% of the condor.
- [ ] **Daily**: re-pull `dark_pool_block_stratified` for SNOW. If BLOCK-tier buy_ratio crosses >0.55 (vs today's 0.304), the distribution thesis is breaking → re-evaluate.
- [ ] **Each session 5/18 through 5/26**: re-check `options_structure_iv_term_structure`. The 5/29 IV kink (107.6%) is the trade's premium source — if it collapses pre-event, take profit early. If it expands (e.g., to >120%), tighten short strikes.
- [ ] **2026-05-26 AMC**: monitor ZS earnings reaction. A ZS miss + cohort-IV pump could blow out 5/29 SNOW IV further before crush. Consider widening wings or rolling out to 6/5 expiry on the day.
- [ ] **2026-05-27 EOD (pre-print)**: trim the iron condor to no more than the max-loss budget you can stomach in a single 24h window. Optional: buy a 5/29 ATM straddle wing for $1-1.50 as additional insurance.
- [ ] **2026-05-28 09:35 ET**: post-earnings, evaluate close vs the $150/$180 short strikes. If spot is inside, hold to expiration for full credit. If outside, close immediately (do not "hope").
- [ ] **2026-05-29 close**: confirm expiry settlement.

## Citations summary

Minimum 3 distinct upstream datapoints for the thesis. Listed here for phase-10 audit:

1. **[HIST:signal_backtest] bullish_flow win rate = 20%, avg move -1.07% over 5 trading days** — phase-5-historical.md §Signal backtest. Source tool: `mcp__uw-pp__historical_signal_backtest`.
2. **[STRUCT:gex] $160 net_gex = +$2,311,523,013, total_gex = +$4,833,651,697, ZGL = $154.56** — phase-4-structure.md §GEX. Source tool: `mcp__uw-pp__options_structure_gex`.
3. **[DP:block_stratified] BLOCK-tier ($1M-$10M) buy_ratio = 0.304 on $16,674,154 premium / 8 trades** — phase-2-dark-pool.md §Tier breakdown. Source tool: `mcp__uw-pp__dark_pool_block_stratified`.
4. **[STRUCT:iv_term_structure] 5/29 avg IV = 107.6% vs 5/22 = 71.2% vs 6/18 = 84.9% (earnings kink)** — phase-4-structure.md §IV term structure. Source tool: `mcp__uw-pp__options_structure_iv_term_structure`.
5. **[HIST:iv_percentile_zscore] IV30 = 86.83%, percentile = 92, z = +1.305, regime HIGH_IV** — phase-5-historical.md §IV regime. Source tool: `mcp__uw-pp__historical_iv_percentile_zscore`.
6. **[HIST:vrp] VRP = +13.3% (IV30 86.83 − RV30 73.53), PREMIUM_SELLING regime** — phase-5-historical.md §VRP. Source tool: `mcp__uw-pp__historical_vrp`.
7. **[INSIGHT:conviction_matrix] scenario = MIXED, confidence = 1.82%, DP buy_ratio = 0.482** — phase-7-insights.md §Conviction matrix. Source tool: `mcp__uw-pp__insights_conviction_matrix`.
8. **[OI:biggest_increases] 5/22 150P +930 OI (bullish put-write) AND 6/18 180C +929 OI (bearish call-write)** — phase-3-positioning.md §Largest OI increases. Source tool: `mcp__uw-pp__oi_biggest_increases`.
9. **[MACRO:DGS10_2026-05-15 WebSearch] 10y Treasury 4.59% (+10bps, one-year high)** — phase-6-macro.md §Rates. Source: WebSearch advisorperspectives.com.
10. **[AGENT:plurality] 4 of 5 desk analysts converge on RANGE/SHORT-VOL/defined-risk** — phase-8-agent-views.md §Tally.
