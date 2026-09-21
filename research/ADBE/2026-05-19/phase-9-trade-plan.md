# Phase 9 — Trade Blueprint

**Ticker:** ADBE
**As-of date:** 2026-05-19 (effective; user-requested 2026-05-20 unavailable in data store)
**PM voice:** desk PM running a $5-50M options-overlay book
**Spot reference:** **$255.05** close (phase-5 trend table) / intraday range $252-$264 (phase-1)
**Upstream phases cited:** phase-1 through phase-8 (all)

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

Institutions are running a **hedged-long COVERED_CALL overlay** into the
**Wed 2026-06-11 AMC earnings** event: dark-pool ACCUMULATION at $173.8M
with mega buy_ratio 1.00 and a single $24.1M ticket at $261.86 +$4.71 over
mid `[DP:largest]`, combined with **17 consecutive OI build days
(+219,392 contracts)** including +1,135 new 5/22 $265 calls being WRITTEN
`[OI:smart_positioning]`, while UW's composite classifier tags the scenario
**COVERED_CALL** `[INSIGHT:conviction_matrix]`. The structural setup
**objectively favors premium selling**: IV rank 89.6 / z+2.27, VRP +11.35
vol-pts, COMPLACENT 30d skew (P/C 1.006), $260 = +$484M gamma magnet
`[STRUCT:gex] [HIST:iv_percentile_zscore] [STRUCT:term_skew]`. Net bias =
**RANGE with a constructive-bull skew inside the $245-$275 box**;
directional debit/long-call alternatives are explicitly NOT supported by
the multi-agent desk (0 of 5 agents called for naked direction).

## Bias + conviction + horizon

- **Directional bias:** **RANGE** (with bullish skew inside the box)
- **Conviction (M-01 bin):** **0.75**
- **Time horizon:** **1-4 weeks** (centered on 2026-06-11 earnings + 6/17 FOMC)
- **Why this bin** (one sentence citing expected phase-10 confluence): six
  of seven phases (2, 3, 4, 5, 6, 7) align with the RANGE-COVERED_CALL
  thesis at "+" or "++" strength, only phase-1 (raw flow) reads mildly
  contradictory, and phase-8 contributes net +2 (3 RANGE / 1 LONG-as-credit
  / 1 NEUTRAL) — expected confluence score ~75 maps to the 0.75 bin per
  rubric.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | $255-$257 (current zone) | Open both structures on a tag of the **5d institutional VWAP $255.64** with intraday spot ≤ $257 | `[DP:price_levels]` 5d VWAP $255.64 |
| **Aggressive** | $250-$252 | A flush to the **$252 DP cluster ($36.2M / 6 trades)** or the 5/19 close ~$252 — open at 1.25× normal width on the put-side spread | `[DP:price_levels]` $252 cluster |
| **Fade (plan B)** | Open above $268 / reject at $270 | If spot rips to $268+ post-FOMC dovish surprise, ADD to the upper call-spread leg only (don't open the put side) — turns the condor into a call-credit hedge against a melt-up | `[STRUCT:gex]` $270 +$336M wall |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| **Hard support / 5/13 trough** | **$234.80** | `[HIST:trend]` 5/13 close (gamma washout low) |
| **DP demand shelf** | **$236-$237** | `[DP:price_levels]` $15.8M + $14.0M aggregated |
| **Negative-GEX cliff** | **$245** | `[STRUCT:gex]` strike GEX −$55.5M, with −$101.8M at $240 just below |
| **5d institutional VWAP** | **$255.64** | `[DP:price_levels]` $133.4M / 521,767 sh / 34 trades |
| **Zero Gamma Level (45-DTE)** | **$259.48** | `[STRUCT:gex]` |
| **Mega gamma wall / 5/22 pin** | **$260** (+$484M GEX) | `[STRUCT:gex]` + `[STRUCT:today_gamma_flip]` ($313M on 5/22-only) |
| **Mega DP buyer level** | **$261.86** ($24.1M, +$4.71 over mid) | `[DP:largest]` |
| **Covered-call cap** | **$265** (call OI 1,513 WRITTEN, net_ask_bid −786) | `[OI:smart_positioning]` |
| **Secondary call wall** | **$270** (+$336M GEX) | `[STRUCT:gex]` |
| **Long-dated speculative target** | **$280-$305** (Aug-21 / Jun-18 OTM call OI builds) | `[OI:biggest_increases]` 6/18 $305C +499, 8/21 $400C +318 |

## Invalidation

Per `rubrics/invalidation-rubric.md`, all three categories required:

- **Price-based:** **Two consecutive daily closes below $245** (enters
  the −$408M short-gamma corridor $220-$245 per `[STRUCT:gex]`) **OR**
  an intraday break of **$236-$237 DP shelf** with no immediate reclaim
  `[DP:price_levels]`. Either fires → exit the bull-skewed condor /
  step aside.
- **Signal-based:** UW `insights_conviction_matrix` flips from
  **COVERED_CALL → DIRECTIONAL_SHORT** on the next daily refresh
  `[INSIGHT:conviction_matrix]` **OR** `insights_institutional_accumulation`
  reverses to **DISTRIBUTION** (buy/sell ratio < 1.0 with falling
  total DP premium for 2 sessions) `[INSIGHT:institutional_accumulation]`.
- **Macro-based:** Either (a) **2026-06-11 ADBE earnings reaction
  exceeds ±12%** in either direction (i.e., breaks the ±9% implied move
  by >3 vol points) `[STRUCT:iv_term_structure]` — this is a tail-vol
  outcome that overwhelms the structure; **OR** (b) **June FOMC ~6/17
  delivers a hawkish 25bps HIKE or a "cuts deferred to 2027" guide**
  with SPY > 1.5% gap-down — TRANSITIONAL regime flips to RISK-OFF
  `[MACRO:FOMC_2026-04-29 WebSearch:cnbc.com]` (4-dissent backdrop
  makes this non-trivial probability).

**Exit on invalidation:** **Tranche exit** — close 50% on first
invalidation trigger fired, 50% on confirmation by the second.
Iron-condor structure favors closing rather than rolling once short-strike
breach occurs.

## Sizing (% of risk, NOT dollars)

### Primary credit structure: iron condor 6/18 245/235 P x 275/285 C

- **Estimated mid prices (modelled from phase-1 tape; verify at open):**
  - Sell 6/18 $245 P: ~$5.50 credit (from 6/05 $267.5P=$15 ref scaled down for delta)
  - Buy 6/18 $235 P: ~$3.00 debit
  - Sell 6/18 $275 C: ~$5.00 credit
  - Buy 6/18 $285 C: ~$3.50 debit
- **Net credit:** ~$4.00
- **Wing width:** $10 each side
- **Max profit:** $4.00 (spot finishes between $245 and $275 at expiry)
- **Max loss:** $10 − $4 = **$6.00** per spread
- **Breakevens:** $249.00 (down) and $279.00 (up)
- **Kelly inputs:** p = 0.75, b = max_profit / max_loss = 4/6 = **0.667**
- **Raw Kelly:** (0.75 × 0.667 − 0.25) / 0.667 = (0.500 − 0.250) / 0.667 = **0.375**
- **Suggested size:** 0.375 × 0.25 × 100 = **9.4%** → **CAPPED at 5%** of book risk per `cap_pct`
- **Final size:** **5% of book risk** (i.e., max-loss across all condor contracts ≤ 5% of book)
- **Deviation reason:** none (downward from suggested is always allowed; rubric cap binds).

### Directional satellite: Aug-21 $260/$280 call debit spread

- **Estimated mid prices** (longer-dated → less vol-crush risk + captures
  Firefly traction + buyback bid):
  - Long 8/21 $260 C: ~$12.50 debit
  - Short 8/21 $280 C: ~$5.50 credit
- **Net debit:** ~$7.00
- **Width:** $20
- **Max profit:** $13.00 (spot ≥ $280 at expiry)
- **Max loss:** $7.00 (spot ≤ $260 at expiry)
- **Breakeven:** $267.00
- **Kelly inputs:** p = 0.65 (longer horizon = lower conviction), b = 13/7 = **1.857**
- **Raw Kelly:** (0.65 × 1.857 − 0.35) / 1.857 = (1.207 − 0.350) / 1.857 = **0.462**
- **Suggested size:** 0.462 × 0.25 × 100 = **11.5%** → **CAPPED at 5%** of book risk
- **Final size:** **2.5% of book risk** (HALF of cap, per risk-monitor
  agent's correlation overlay — ADBE long is a software-beta proxy; do not
  size full alongside any CRM/NOW/INTU/XLK longs)
- **Deviation reason:** explicit DOWNWARD deviation (allowed without
  justification) — risk-monitor's `[AGENT:risk-monitor] ADBE-CRM corr
  0.877` informs the 50% haircut.

**Combined book risk: ≤ 7.5% of book** (5% condor + 2.5% Aug debit
spread), well inside the rubric ceiling.

## Option structures

### Directional (primary, bullish satellite)

- **Structure:** **8/21 $260 / $280 call debit spread**
- **Strikes / expiry:** Long 1× $260C, Short 1× $280C, 2026-08-21
  (94 DTE)
- **Net debit:** ~$7.00
- **Breakeven:** $267.00
- **Max loss:** $7.00 per spread (= 35% of width)
- **Why this structure:**
  1. Captures the **structural buyback bid + Firefly AI catalyst** that
     should dominate the 60-90d horizon — independent of the 6/11
     earnings outcome.
  2. **Avoids paying the 89.6 IV rank on the front** — 8/21 IV is 49.8%
     vs front-month 62.0%, so debit pricing is structurally cheaper
     `[STRUCT:iv_term_structure]`.
  3. Strikes pinned to phase-4 GEX walls ($260 magnet, $280 secondary
     wall) and phase-3 OI ($305 call OI build +499 — ITM target).

### Defined-risk alternative (primary credit, the workhorse)

- **Structure:** **6/18 iron condor 245/235 P × 275/285 C**
- **Strikes / expiry:** Short 1× 245P, Long 1× 235P, Short 1× 275C,
  Long 1× 285C, 2026-06-18 (30 DTE)
- **Net credit:** ~$4.00
- **Breakevens:** $249.00 / $279.00
- **Max loss:** $6.00 per condor
- **Why this structure:**
  1. **6/18 expiry captures BOTH earnings (6/11) and the June FOMC
     (~6/17)** in a single decay window — no roll risk.
  2. Strikes sit OUTSIDE the ±9% implied earnings move
     (~$232-$278) on the call side ($275/$285 above $278 BE) and
     INSIDE on the put side ($245/$235 below $232 floor) — **deliberately
     skewed bullish: more wiggle room above than below**, exploiting
     the dealer DEX +$39.7B bid floor `[STRUCT:dex]` and dark-pool
     accumulation `[DP:block_stratified]`.
  3. Captures the **10-vol-point earnings kink crush** (57% IV today →
     ~47% post-print expected) `[STRUCT:iv_term_structure]`.
  4. $260 mega gamma magnet (+$484M) anchors the center of the
     condor at max-profit zone `[STRUCT:gex]`.

## Macro overlay (cite phase-6)

### Tailwinds

- **Tech sector net inflow +$43.98M today**, largest sector inflow
  `[MACRO:SectorRotation_2026-05-19 UW]` — relative-strength bid for ADBE.
- **XLK flow direction BULLISH** on 5/19 vs SPY 9/10 bearish flow days
  `[MACRO:XLK_2026-05-19 UW]` — sector internals favor ADBE.
- **ADBE $25B buyback authorized Apr 2026** = structural multi-quarter
  bid `[MACRO:ADBE_Buyback_2026-04 WebSearch:fool.com]`.
- **Firefly AI Assistant + Anthropic Claude partnership** —
  product-cycle catalyst with ARR > $250M growing +45% q/q in Q1
  `[MACRO:ADBE_Firefly_2026-04-15 WebSearch:news.adobe.com]`.
- **Q1 FY26 prior-quarter print: revenue $6.40B (+12% YoY), op CF $2.96B**
  — strong fundamental base into Q2 print
  `[MACRO:ADBE_Q1_FY26 WebSearch:tradingkey.com]`.

### Headwinds

- **April CPI 3.8% YoY** (hottest since May 2023, +0.6% m/m headline)
  `[MACRO:CPI_2026-04 WebSearch:cnbc.com]` — sticky inflation pushes
  rate-cut timing OUT, generic duration-asset headwind.
- **FOMC 8-4 dissent**, 3 regional presidents (Hammack/Kashkari/Logan)
  dissenting AGAINST easing-bias language `[MACRO:FOMC_2026-04-29
  WebSearch:cnbc.com]` — uncertain forward path, dollar/rate risk.
- **Market regime TRANSITIONAL** with breadth 34.7% bullish
  `[MACRO:MarketRegime_2026-05-19 UW]` — half-position sizing.
- **"Mixed Wall Street Sentiment" + "Legal Headwinds" + "CEO Exit"
  qualifiers** in coverage `[MACRO:ADBE_Coverage_2026 WebSearch:tikr.com]`
  — non-trivial overhang.
- **Energy +17.9% YoY (Iran war)** — inflation-shock vector that
  could re-shape Fed guidance into the post-earnings 6/17 FOMC
  `[MACRO:CPI_2026-04 WebSearch:cnbc.com]`.

### Net

**MIXED — ticker-specific tailwind inside a broad-market headwind.**
This is exactly the setup that favors a DEFINED-RISK CREDIT structure
over outright direction.

## Catalyst calendar (next 30d, 2026-05-19 → 2026-06-18)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-22** (3 DTE) | May standard monthly OPEX | Neutral — $260 pin per `[STRUCT:today_gamma_flip]` |
| ~2026-05-30 | Apr 2026 PCE release (BEA monthly) | ± (tests CPI 3.8% trend) |
| ~2026-06-06 | May 2026 NFP | ± |
| ~2026-06-11 | May 2026 CPI release | ± (Fed setup) |
| **2026-06-11 AMC (Wed)** | **ADBE Q2 FY26 earnings — EPS $5.67 / rev $6.43B guide** | **PRIMARY — IV crush ~10 vol-pts**, direction depends on print |
| ~2026-06-17/18 | **June 2026 FOMC + SEP/dot plot** | ± — stacked AFTER ADBE earnings; hawkish surprise compounds tail risk |
| **2026-06-18 (30 DTE)** | **June monthly OPEX** — iron condor expiry | Structure resolves here |

## Post-trade monitoring checklist

- [ ] **Daily**: re-pull `mcp__uw-pp__options_structure_gex` for ADBE
  and confirm ZGL stays in $258-$262 band; flag if ZGL drops below
  $250 (regime flip risk per `[HIST:gex_time_series]`).
- [ ] **Daily**: re-pull `mcp__uw-pp__dark_pool_ticker_summary` /
  `dark_pool_block_stratified` for ADBE; confirm block buy_ratio
  stays > 0.55 (accumulation continuity).
- [ ] **Each Mon/Wed/Fri**: re-pull `mcp__uw-pp__insights_conviction_matrix`
  for ADBE; FLIP from COVERED_CALL to anything else = SIGNAL invalidation.
- [ ] **Daily**: re-pull `mcp__uw-pp__historical_cumulative_premium_flow`
  with days=5; if net flow goes negative for 3 consecutive sessions →
  signal-based invalidation triggered.
- [ ] **Pre-6/11 close**: take a snapshot of `iv_term_structure` and
  `front_end_iv_ratio` 60 minutes before earnings; if 6/12 IV has not
  expanded above 60%, the implied move is being repriced lower → BAIL
  on the short call wing.
- [ ] **6/11 AMC**: ADBE prints earnings. Have stop levels armed at
  $235 (lower break) and $283 (upper break) for the next-day open.
- [ ] **6/12 open**: if spot inside $249-$279 box → let condor decay
  toward 6/18 expiry. If spot outside the box → execute tranche exit
  protocol.
- [ ] **6/17/18 FOMC**: take SEP / dot plot delta into account on any
  remaining open exposure; close the Aug debit spread if FOMC delivers
  a 25bps HIKE (not a cut).
- [ ] **Weekly**: re-check ADBE/CRM, ADBE/NOW, ADBE/INTU correlation
  via `mcp__uw-pp__risk_portfolio_correlation` — if any pair drops
  below 0.70 = ADBE is breaking idiosyncratic, RECHECK if accumulation
  thesis is intact.

## Citations summary (M-04: ≥3 distinct upstream datapoints)

Phase-10 will spot-check that each citation tag resolves to an exact
quotable line in the named upstream phase MD:

1. **`[DP:largest]` $24,106,138 mega block @ $261.86, +$4.706 over mid,
   92,057 shares, 1 trade — phase-2-dark-pool.md § "Largest blocks"**
2. **`[OI:smart_positioning]` 5/22 $265C +1,135 OI with net_ask_bid
   −786 (calls SOLD by institutions) — phase-3-positioning.md
   § "Largest OI increases"**
3. **`[INSIGHT:conviction_matrix]` scenario tag = COVERED_CALL,
   confidence 13.45%, DP buy_ratio 0.615, call_ask 14,359 vs
   call_bid 15,513 — phase-7-insights.md § "Conviction matrix"**
4. **`[STRUCT:gex]` Zero Gamma Level $259.48 vs spot $258.07; $260
   strike net_gex +$483,971,528 — phase-4-structure.md § "GEX
   (45-DTE, per-strike top features)"**
5. **`[HIST:iv_percentile_zscore]` IV30d 0.5555, percentile 100,
   z-score +2.27, regime HIGH_IV — phase-5-historical.md § "IV
   regime"**
6. **`[MACRO:ADBE_Q2_2026-06-11 WebSearch:tipranks.com]` Adobe Q2
   FY26 earnings 2026-06-11, EPS guide $5.67, revenue guide $6.43B —
   phase-6-macro.md § "Sector overlay — ADBE-specific catalysts"**
7. **`[AGENT:accumulation-hunter]` 5/14 trough-day block buy_ratio
   0.942 on $19.8M (13 trades) — phase-8-agent-views.md §
   "accumulation-hunter — LONG / conv 4 / 1-4w"**
8. **`[AGENT:risk-monitor]` ADBE/CRM corr 0.877, ADBE/NOW 0.867 —
   phase-8-agent-views.md § "risk-monitor — NEUTRAL / conv 2 / 1-4w"**

**Tag density: 8 distinct upstream datapoints cited in the thesis,
levels, and sizing rationale — well above the M-04 minimum of 3.**

---

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative. Verify all option mid-prices at
> open before placing orders.*
