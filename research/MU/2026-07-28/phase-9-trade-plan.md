# Phase 9 — Trade Blueprint

**Ticker:** MU
**As-of date:** 2026-07-28
**PM voice:** desk PM running an institutional book
**Spot reference:** $820.53 (`phase-0.5-context.md` / screener close; range 789.09–848.36, prev close 900.20)
**Upstream phases cited:** phase-0.5 through phase-8b

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

Institutions distributed MU into weakness today — the mega-tier dark-pool `buy_ratio` of 0.803
is a closing-auction artifact that inverts to **0.227 in regular hours (77% selling), with the
buy ratio *lowest* at the lowest prices (0.411 in the $790s)** `[DP:block_stratified]` — and they
did it inside a **`FULLY_NEGATIVE` gamma regime with `zero_gamma_level = null`, where the largest
negative-gamma strike ($800, -6,527,065) is the same level as the dominant put wall, the heaviest
distribution bin, and the written put strike** `[STRUCT:gex]`. But the tape carries no
directional information to trade on — **net customer delta is -$41M ex-0DTE on a $926.7B cap**
`[FLOW:delta_notional DUCKDB]`, 75 sessions of cumulative flow net **+0.16% of gross** with
`trend_direction = MIXED` `[HIST:cumulative_premium_flow]`, and **realised vol of 109.12%
exceeds implied of 96.04%** so every downside structure costs more than the move it targets
`[HIST:vrp]`. **The desk is flat: phase-8 returned SHORT 2 / NEUTRAL 2 / LONG 0 at average
conviction 2.5** `[AGENT:phase-8]`, phase-7b `VETO`s the short on a business compounding revenue
at **+166.98%** with 4/4 beats `[FUND:revenueGrowthTTMYoy]`, and the phase-8b debate closed
**disconfirmed at 0.65 vs 0.65** `[DEBATE:residuals]`.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL**
- **Conviction (M-01 bin):** **0.55**
- **Time horizon:** **1-5d** (through the 2026-07-29 FOMC and the 2026-07-31 expiry, then re-assess)
- **Why this bin:** the confluence stack is weak and self-cancelling — phases 1, 3, 5 and 8 are
  neutral/mixed against bearish reads in phases 2, 4 and 6, giving a **4–3 neutral plurality**;
  phase-7's `conviction_matrix` prints **`MIXED` at 8.2% confidence** `[INSIGHT:conviction_matrix]`;
  and the phase-8b disconfirmation down-shifts the bin one step from 0.65 to **0.55**. Phase-10
  should score this in the low band; if it lands materially higher I will take the deviation, not
  the bin.

### Note on bias selection (auditable)

Per `rubrics/sizing-rubric.md`, the 7b veto and the 8b debate **cannot set the bias** — they only
cut size and conviction. **The NEUTRAL bias is therefore taken from the plurality of phases 1–8
on their own terms, not from the gates:** phase-1 MIXED, phase-3 mixed/defensive, phase-5 no edge
either way, phase-8 tied 2-2 → **four neutral**; phase-2 DISTRIBUTION, phase-4 short-gamma,
phase-6 HEADWIND → **three bearish** (phase-7 straddles at "nominally mild-bullish, substantively
neutral-to-bearish"). **The lean within NEUTRAL is unambiguously bearish, and every conditional
trigger below is written to reflect that** — but the plurality is neutral and the executable
recommendation is flat.

## Entry zones

**All three are CONDITIONAL RE-ENTRY TRIGGERS, not live orders — final directional size is 0%
(see Sizing).** Nothing is put on today.

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$870** | **Daily close above 870** — the `atm_flip_strike`, above which dealer gamma turns positive and hedging damps rather than amplifies. This *invalidates the bearish lean* and is the trigger to consider a small LONG, not a short. | `[STRUCT:today_gamma_flip]` |
| **Aggressive** | **$800** | **Two daily closes below 800** — the four-way convergence strike (largest negative GEX -6,527,065 · put wall net -32,711 OI · heaviest DP distribution bin · written put strike). Confirms the bearish path toward 750; only then does a short have a defined objective. | `[OI:oi_by_strike]` `[STRUCT:gex]` |
| **Fade** | **$900 – $930** | **Rejection at the contested 900 battleground or the 930 max-pain magnet** while regular-hours DP `buy_ratio` stays <0.45 — sell the rally if the distribution signature persists. This is the plan-B counter-trade if MU bounces without repairing structure. | `[OI:oi_by_strike]` `[STRUCT:max_pain]` `[DP:block_stratified]` |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| **Support (primary)** | **$800** — `put_wall_support`, 84,213 OI, net -32,711, `distance_pct` -2.39 | `[OI:oi_by_strike]` |
| Support (session) | **$789.09** — today's intraday low; already breached after hours to **$780.00** | `[HIST:screener_low]` `[DP:extended_hours]` |
| Support (secondary) | **$750** — `put_wall_support` (41,151 OI, net -20,571, -8.49%) and third-largest negative GEX (-3,851,698); the strike the six-session put-writing campaign is underwriting | `[OI:oi_by_strike]` `[STRUCT:gex]` `[OI:biggest_increases DUCKDB]` |
| **Resistance** | **$900** — tagged `call_wall_resistance` but **net_oi only +6,115 against 29,455 puts: a two-sided battleground, NOT a clean ceiling** | `[OI:oi_by_strike]` |
| Resistance (supply) | **$966 – $992** — ~$0.32B of 7/22–7/23 dark-pool supply overhead; plus prior closes 900.20 ($1.57B) and 920.95 ($1.31B) | `[DP:price_levels]` |
| **Gamma flip** | **$870** — `atm_flip_strike` (0DTE/7-29 expiry). **Note `zero_gamma_level = null` across the full 45-DTE surface — there is no long-gamma refuge below 870** | `[STRUCT:today_gamma_flip]` `[STRUCT:gex]` |
| **Largest pin / max pain** | **$930** (2026-07-31, +13.47%, P/C OI 2.592, 403,258 OI) and **$940** (2026-08-21, +14.69%) — **indicative only**: MU failed `pin-risk` entirely (0 of 25 rows) and gamma beats max-pain gravity at 13–15% distance | `[STRUCT:max_pain]` `[OI:pin_risk]` |

**Price-context colour (advisory, does not affect sizing):** **RSI is 40.29 — NOT oversold** —
and MU still sits **+61.28% above its 200-DMA** while **-34.62% from its 52-week high**, with
**ATR 83.13 (10.1% of spot)** `[HIST:rsi fz]` `[HIST:52w_proximity fz]`. There is no
momentum-exhaustion signal and no valuation floor nearby; a mean-reversion to the 200-DMA implies
roughly **-38%** from spot. **Do not treat -32% off the high as "washed out."**

## Invalidation

Because the recommendation is flat, these are the conditions that would **establish** a position
rather than close one; they are written to the same falsifiable standard.

- **Price-based:** **Two daily closes below $800** (phase-3 largest-OI strike / phase-4 largest
  negative-GEX strike) establishes the bearish path with a $750 objective. **Symmetrically, one
  daily close above $870** (`atm_flip_strike`) invalidates the bearish lean outright by restoring
  positive dealer gamma. A move beyond **ATR × 1.5 = ±$124.70** (to <$695.83 or >$945.23) inside
  the horizon voids this blueprint entirely and requires a fresh run.
  `[OI:oi_by_strike]` `[STRUCT:today_gamma_flip]` `[HIST:atr fz]`
- **Signal-based:** **Regular-hours dark-pool mega `buy_ratio` flipping above 0.55 for two
  consecutive sessions** kills the distribution thesis (this is phase-8's accumulation-hunter's
  own stated invalidation, and it is the most diagnostic single signal in the run because the
  0.227 is the strongest unrefuted claim from the debate). Secondary: **`total_gex` turning
  positive / a `zero_gamma_level` reappearing** on the phase-4 daily refresh would end the
  amplification regime. Tertiary: **cumulative premium flow turning net against the lean for
  three consecutive sessions** `[DP:block_stratified]` `[STRUCT:gex]` `[HIST:cumulative_premium_flow]`.
- **Macro-based:** **The FOMC decision on 2026-07-29 at 14:00 ET (no SEP, Warsh presser 14:30).**
  A dovish outcome — supported by June CPI at **3.5% headline / 2.6% core** and payrolls at
  **+57k vs 115k consensus** — collapses the 151–152% front-week implied vol and would likely
  carry MU back toward 870; a hawkish surprise into a `FULLY_NEGATIVE` gamma book with
  `net_dex` -$9.12B gets mechanically amplified lower. **Secondary sector trigger: any
  confirmation or denial of Apple qualifying CXMT memory, or a DRAM contract-price print that
  dates the cycle peak.** `[MACRO:FOMC_2026-07-29]` `[MACRO:CPI_2026-06]` `[MACRO:CXMT_2026-07-28]`

**Exit on invalidation: HARD STOP.** Both illustrative structures are defined-risk
(debit/credit spreads), so max loss is bounded at entry and no discretionary stop is required.
If a position is ever established on the triggers above, close 100% at the stated level — do not
average into a `FULLY_NEGATIVE` gamma regime with a 10.1% ATR.

## Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** `p_raw` = **0.80** (`signal_class = bearish_flow`, `win_rate_n` = **10**,
  `win_rate_source` = `backtest`) → N-conditional cap for `10 ≤ n < 20` is **0.85** →
  **capped p = min(0.80, 0.85) = 0.80** `[HIST:signal_backtest]`
  - *Qualifiers carried from phase-5 that phase-10 must see:* this is a **market-wide** base rate
    (`signal-backtest` takes no `--symbol`), the tool self-disclaims **"In-sample backtest — not a
    robust live edge"**, n=10 sits at the low-confidence floor, and the **class-match is imperfect
    — phase-1's flow verdict was MIXED, not `bearish_flow`.** The bearish evidence comes from
    phases 2/4/6, for which no backtest exists (`dark_pool_accumulation` returned 0 signals).
- **Kelly inputs:** b = |entry − target| / |stop − entry| = (820.53 − 750) / (870 − 820.53) =
  70.53 / 49.47 = **1.4257**; fraction = **0.25**; cap_pct = **5**
- **Raw Kelly:** (0.80 × 1.4257 − 0.20) / 1.4257 = **0.6597** →
  suggested = min(0.6597 × 0.25 × 100, 5) = min(16.49%, 5%) = **5.00%**
- **Win-rate map ceiling:** p = 0.80 ≥ 0.70 → **full** (up to cap_pct). Kelly and the map agree at
  **5.00%** pre-gate.
- **Risk gates — all five, in order:**

  | # | Gate | Value | Effect |
  |---|---|---|---|
  | 1 | **Fundamentals (phase-7b)** | **`VETO`** (`contradiction_count` = 2: earnings_trend + growth/margins) | **Directional size → watch-only / 0%, regardless of Kelly.** Defined-risk carry only, marked "fundamentals-vetoed". |
  | 2 | **Sentiment / crowd (phase-7c)** | **`CAUTION`**, `crowd_state` = **`CROWDED_LONG`** | Cut one size step (full → half). Subsumed by gate 1, but recorded. |
  | 3 | **Correlation cluster (phase-6)** | **none active** — MU is the only blueprint under `research/*/2026-07-28/` | No cut. **Standing constraint recorded:** MU/SNDK **0.904**, MU/AMAT **0.865**, MU/WDC 0.731, MU/STX 0.709 — any future concurrent position in those names is the same bet. |
  | 4 | **Sector rotation (phase-6)** | **`neutral`** — Technology `trend = INFLOW`, `persistence_score` 1.0, but net flow collapsed 99% in five sessions ($3.235B → $34.2M) | No cut (sign persists; magnitude exhausted). |
  | 5 | **Debate (phase-8b)** | **`disconfirmed = true`** — bull_residual **0.65** vs bear_residual **0.65** | **Down-shift conviction bin one (0.65 → 0.55) AND cut one size step.** |

- **Context modifier (phase-0.5):** `unusual_verdict = **BUSY_NAME_NORMAL_DAY**` — option volume
  **0.84× its own 30-day average**, self-percentile 64.9 on net direction. **Sizing at the top of
  the band is forbidden**; MU's $3.025B of premium is its normal day, not a signal.
- **Final size: 0.00% of book risk (WATCH-ONLY).** The phase-7b `VETO` is dispositive on its own;
  the 7c `CAUTION`, the 8b disconfirmation and the `BUSY_NAME_NORMAL_DAY` context all point the
  same way, and phase-6's `market-regime` guidance independently reads **"Half position sizes.
  Favor defined-risk strategies."**
- **Deviation reason:** **none — no upward deviation is permitted; three gates fired.**

**The honest statement of the problem, from the debate:** the bearish objective is $750, **-8.6%**
from spot. The daily ATR is **10.1%** and the front-expiry implied move is **±7.90%**. **The move
being forecast is smaller than one average session of noise**, so any survivable stop is wider
than the target — an inverted risk-reward before the FOMC binary is even priced. That is why
size is zero rather than small.

## Option structures

**Front-expiry expected move: ±7.90% / ±$64.79** (`implied_move` 64.7944, `implied_move_perc`
0.07904) `[CTX:implied_move]`. Both structures below use the **$100-wide 800/900 Oct-16 spread =
12.2% of spot = 1.54× the priced move** — deliberately wider than the expected move so the
structure is not capped before the move completes. **Both legs are prices actually observed on
today's tape** (`phase-1-flow.md` §Largest premium prints), not model estimates:
**900P Oct-16 traded at $196.45** (Δ -0.518, IV 0.92) and **800P Oct-16 traded at $122.25**
(Δ -0.385, IV 0.91).

**Catalyst-gap check (N4):** a single-catalyst move of ±$64.79 puts MU at **$755.74 / $885.32**.
Both structures are defined-risk spreads, so **max loss is fixed at entry and a gap of the
expected-move magnitude cannot exceed the stop.** ✓ Expiry 2026-10-16 sits **after** the
2026-09-22 earnings date — see the IV note below.

### Directional (primary) — **VETOED, DO NOT PUT ON**

- **Structure:** put debit spread (bearish) — **`fundamentals-vetoed, documented for the record only`**
- **Strike(s) / expiry:** long **900** put / short **800** put, **2026-10-16** (80 DTE)
- **Debit/credit:** **debit $74.20** (196.45 − 122.25)
- **Breakeven:** **$825.80** (900 − 74.20) — i.e. MU must simply close below spot at expiry
- **Max loss:** **$74.20** per spread (9.0% of spot) · **Max profit:** $25.80 · **R:R 0.35 : 1**
- **Why this structure:** it is the cleanest expression of the bearish structural read — the 900
  strike is phase-3's contested battleground and the 800 strike is the four-way convergence pivot,
  so the spread monetises exactly the zone the distribution occurred in. **And it demonstrates
  why the trade is rejected:** at IV 91–92% you risk $74.20 to make $25.80, and the position is
  already in-the-money at entry, meaning virtually all the edge is priced. **Size = 0%.**

### Defined-risk alternative — **carry only, token size, fundamentals-permitted**

- **Structure:** put credit spread (neutral-to-bullish) — the inverse of the above
- **Strike(s) / expiry:** short **900** put / long **800** put, **2026-10-16**
- **Debit/credit:** **credit $74.20**
- **Breakeven:** **$825.80**
- **Max loss:** **$25.80** per spread (**3.1% of spot**) · **Max profit:** $74.20 · **R:R 2.88 : 1**
- **Why this structure:** it is the only expression in this run that both gates tolerate — it
  aligns with phase-7b's `VETO` (which says do not be short a business compounding at +166.98%
  revenue with 4/4 beats and 5.1% debt/equity) while capping loss at 3.1% of spot into a regime
  where ATR is 10.1%. **It requires MU to hold above $825.80 by 2026-10-16 — above today's close
  — so it is NOT a free carry**, and phase-7c would `VETO` a genuine long thesis
  (`crowd_state = CROWDED_LONG`, institutions distributing). **Token size only, and only after
  the FOMC resolves.**

**A note on what the market is telling you through these two prices:** the 800/900 October spread
is priced at **74.20 / 25.80**, i.e. the market assigns roughly **74%** to MU being below $825.80
in eleven weeks. **The bearish view is already the consensus price.** That is the strongest single
argument against paying up for it.

**Structure explicitly NOT recommended, and why:** phase-6's `market-regime` guidance suggests
*"Iron condors in range"*, and a short-premium structure would monetise the 800–900 range. **I am
declining it** because phase-5 returns **`vrp = -0.1308` — realised 109.12% against implied
96.04%, `regime = PREMIUM_BUYING`** `[HIST:vrp]`. **Selling volatility that is already 13 points
below realised, in a `FULLY_NEGATIVE` gamma regime with a 10.1% ATR, is a negative-carry trade.**
The theoretically correct expression of the VRP finding is **long premium** (a straddle/strangle
at the 30–45 day tenor where IV ≈ 96–103% against realised 109%) — **but no call quote at that
tenor was observed in today's tape, and I will not fabricate a debit.** If pursued, the
constraint is: **total debit must be below ~7.9% of spot (~$64.79)**, or the structure needs more
than the priced move just to break even.

**IV / earnings note:** the 2026-10-16 expiry **straddles the 2026-09-22 earnings date** and
carries the elevated `avg_iv` of **1.2188** versus 0.9893 at 2026-09-04 and 0.9203 at 2026-11-20
`[STRUCT:iv_term_structure]` — i.e. **you are paying an earnings premium on both legs.** Because
both structures are *spreads*, the vega is largely offset and post-earnings IV crush is close to
neutral. **A single-leg version of either would be badly exposed to it.**

## Macro overlay (cite phase-6)

- **Tailwinds:**
  - `[MACRO:DRAM_pricing_Q1-2026]` DRAM is in **shortage, not oversupply** — traditional contract
    prices **+93–98% QoQ in Q1 2026**; HBM at a **5–8× DDR5 ASP premium**, supply-constrained.
  - `[MACRO:CPI_2026-06]` June CPI **3.5% YoY headline (-0.4% MoM, largest decline since April
    2020), core 2.6%** — both below consensus. Disinflationary; removes a hawkish justification.
  - `[MACRO:PAYEMS_2026-06]` payrolls **+57k vs 115k consensus**, May revised to +129k — dovish-leaning.
  - `[MACRO:CXMT_capacity]` CXMT's **HBM3E mass production is not targeted until 2027** — the
    competitive threat is 18 months from mattering where margins actually are.
- **Headwinds:**
  - `[MACRO:CXMT_2026-07-28]` CXMT scaling **200k → 300k wafers/month** toward **17% of global
    DRAM supply by 2028**, with **Apple reportedly testing CXMT memory for China-sold devices**.
  - `[MACRO:DRAM_inventory_2026-07]` **faster-than-anticipated inventory normalisation** across
    enterprise/cloud — historically the marker of a DRAM pricing-cycle peak.
  - `[MACRO:MarketRegime_2026-07-28]` regime **`TRANSITIONAL` / `CHOPPY`**, SPY below both its
    20-DMA (746.65) and 50-DMA (744.86), flow breadth **36.9% bullish**; guidance **"Half position
    sizes."**
  - `[MACRO:sector_flow_persistence]` Technology net flow **collapsed 99% in five sessions**
    ($3.235B → $34.2M), ranking 7th of 11 despite carrying half the market's premium.
- **Net: MIXED — and the mix is the point.** Macro proper is **neutral-to-dovish and supportive**;
  the damage is **entirely industry-specific**. SPY closed **+0.24%**, NVDA **+0.25%**, and
  **70.97% of the S&P 500 was green** while SNDK fell **-14.25%** `[MACRO:sector_breadth fz EOD]`.

## Catalyst calendar (next 30d)

**Front-expiry expected move: ±7.90% / ±$64.79** `[CTX:implied_move]` — read each row against it.

| Date | Event | Impact direction | vs expected move |
|---|---|---|---|
| **2026-07-29 14:00 ET** | **FOMC decision + Warsh presser 14:30. No SEP/dot plot. Target 3.50–3.75%.** | **?** — the binary. Dovish → front-week IV (151–152%) collapses, likely carries MU toward 870. Hawkish → amplified lower through 800 in a `FULLY_NEGATIVE` book. | plausibly **inside** ±7.9% for MU (macro, not memory-specific) — but it unlocks the vol path |
| 2026-07-29 | 1-DTE expiry (3.43% of OI); the 815–835 call ladder | ? | inside |
| **2026-07-31** | **Weekly expiry holding 18.38% of ALL MU open interest** — 291,008 puts vs 112,250 calls, P/C OI 2.592, max pain 930 | ? — first settlement after the FOMC | **structural** |
| ~2026-08-07 | July employment report (BLS) | ? | inside |
| **2026-08-07** | Expiry of the **55P (+24,412 contracts @ $0.01)** crash-tail build; unexplained `avg_iv` hump **1.3592** | ? | **flagged — no known catalyst** |
| **2026-08-12** | **July CPI release, 08:30 ET** | ? — confirms or denies June's disinflation | inside |
| 2026-08-14 | Unexplained `avg_iv` hump **1.2554** | ? | **flagged — no known catalyst** |
| **2026-08-21** | **Monthly OPEX — 13.91% of OI, max pain 940, P/C OI 1.656** | ? | structural |
| *2026-09-22* | *MU earnings (outside 30d; corroborated by fiscal calendar + the Oct-16 IV hump)* | ? | **exceeds ±7.9%** on history |

## Post-trade monitoring checklist

- [ ] **Regular-hours dark-pool `mega.buy_ratio`, daily — and always excluding post-close prints.**
      Two consecutive sessions above **0.55** kills the distribution thesis; sustained below 0.45
      confirms it. *This is the single most diagnostic number in the run — do not read the
      all-session figure.* `[DP:block_stratified]`
- [ ] **`uw options-structure gex` daily: does `zero_gamma_level` reappear and does `total_gex`
      turn positive?** The `FULLY_NEGATIVE` regime is the reason stops are unworkable; its end is
      the precondition for any directional position. `[STRUCT:gex]`
- [ ] **Tomorrow's OI file (7/29) — did today's ~$28.4M of 750/800 put selling ADD to the
      six-session campaign or net against it?** This run could not see it (OI settles overnight;
      the window was 7/27→7/28). It is the cleanest test of whether a committed counterparty is
      still underwriting 750–800. `[OI:biggest_increases DUCKDB]`
- [ ] **The FOMC at 2026-07-29 14:00 ET and the front-week IV response.** If IV collapses from
      151–152% and MU does *not* rally, the vanna-squeeze upside case is dead and the bearish
      structural read strengthens materially. `[MACRO:FOMC_2026-07-29]` `[STRUCT:vanna_charm]`
- [ ] **The next semi-monthly short-interest settlement** — the current 3.21% / 36.21M figure
      predates the entire drawdown (FINRA settles 2026-06-30). `[SENT:short_float fz semi-monthly]`
- [ ] **Analyst downgrades.** 51 of 56 at buy-or-better with **one** sell rating and zero
      downgrades through a -32% decline; the first genuine downgrade cycle is the sentiment
      trigger this name has not yet had. `[SENT:recommendation]`
- [ ] **Any confirmation/denial of Apple qualifying CXMT memory, or a dated DRAM contract-price
      rollover** — the single fact that would convert the bear case from forecast to event.
      `[MACRO:CXMT_2026-07-28]`

## Citations summary

Minimum 3 distinct upstream datapoints (M-04). Listed for phase-10 spot-check:

1. **`[DP:block_stratified]`** — mega-tier `buy_ratio` **0.803 all-session → 0.227 regular-hours**
   (3 buys / 57,902 sh vs 9 sells / 196,620 sh); every tier <0.5 in regular hours; price-bin buy
   ratio **0.411 in the $790s, 0.419 in the $800s vs 0.497 in the $820s** —
   `phase-2-dark-pool.md` §Tier breakdown / §Price levels. *(phases 1–4: today's tape)*
2. **`[FLOW:delta_notional DUCKDB]`** — net customer delta **-$178M all-tape, -$41M ex-0DTE** on a
   $926.7B cap; calls net sold **-$45.76M**, puts net sold **-$74.32M**; `bullish_premium` =
   ask-calls (645.19) + bid-puts (**784.17**) reconciling to UW's 1,429,357,672 to the dollar —
   `phase-1-flow.md` §Whole-tape aggregate. *(phases 1–4: today's tape)*
3. **`[HIST:vrp]`** — `vrp` **-0.1308**, realised **1.0912** vs `iv30d` **0.9604**,
   `regime = PREMIUM_BUYING`; plus `iv_percentile` **48.65** over 74 actual sessions —
   `phase-5-historical.md` §IV regime. *(phases 5–7: historical context)*
4. **`[STRUCT:gex]`** — `regime = FULLY_NEGATIVE`, `total_gex` **-45,676,510**,
   **`zero_gamma_level = null`**, largest negative strike **$800 at -6,527,065** —
   `phase-4-structure.md` §GEX. *(phases 1–4: today's tape)*
5. **`[MACRO:CXMT_2026-07-28]`** — CXMT 200k → 300k wpm toward 17% of global DRAM by 2028; Apple
   testing CXMT memory; against DRAM contract prices **+93–98% QoQ** and CXMT HBM3E only in 2027 —
   `phase-6-macro.md` §Sector overlay. *(phase 6: macro)*
6. **`[AGENT:phase-8]` / `[DEBATE:residuals]`** — desk vote **SHORT 2 / NEUTRAL 2 / LONG 0**,
   average conviction **2.5**; debate closed **bull 0.65 vs bear 0.65 → `disconfirmed = true`** —
   `phase-8-agent-views.md`, `phase-8b-debate.md`. *(phase 8: agent verdict)*
7. **`[HIST:signal_backtest]`** — `bearish_flow` `win_rate` **0.80**, `total_signals` **10**,
   market-wide and in-sample (the Kelly `p`) — `phase-5-historical.md` §Signal backtest.
8. **`[FUND:revenueGrowthTTMYoy]`** — revenue **+166.98% TTM YoY**, EPS **+700.71%**, gross margin
   **72.57%**, 4/4 beats, `peTTM` 18.43 vs `peNormalizedAnnual` **108.93** —
   `phase-7b-fundamentals.md` §Valuation / §Growth. *(the veto)*
