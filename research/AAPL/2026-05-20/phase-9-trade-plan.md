# Phase 9 — Trade Blueprint

**Ticker:** AAPL
**As-of date:** 2026-05-20
**PM voice:** desk PM running an institutional book
**Spot reference:** $302.25 close ([HIST:historical_trend] phase-5; intraday print $300.68 [STRUCT:gex] phase-4)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative.*

## Thesis (≤3 sentences)

Today's tape recorded a **single coordinated institutional package** —
**$54.1M ask-side sweep of the 2028-01-21 $300C LEAP** [FLOW:sweeps]
crossed at 16:00:43 UTC within seconds of an **$1.05B mega-tier dark
pool buy cluster at $302.25 with buy_ratio 0.794** [DP:block_stratified],
including a true after-hours 762k-share lift at +21bp above mid
[DP:largest]. That program operates inside a structural setup that
strongly favors continuation: **POSITIVE GEX $648.7B with a $1.38T
0DTE support wall at $302.5** [STRUCT:today_gamma_flip], **IV at the
14.3rd percentile of the trailing year** [HIST:iv_percentile_zscore],
**29 consecutive sessions of net OI build** [HIST:oi_trend], and
**Technology +$349.9M net sector flow today — the largest single
sector inflow on the tape** [MACRO:SectorRotation_2026-05-20].
Three of five analyst sub-agents vote LONG with conviction 4; the
two NEUTRAL voters explicitly ratify the directional thesis but flag
**sizing/crowding/event-risk** as constraints [AGENT:risk-monitor],
[AGENT:contrarian-scanner].

## Bias + conviction + horizon

- **Directional bias:** **LONG**
- **Conviction (M-01 bin):** **0.75**
- **Time horizon:** **1-4w** (debit spread) / **1-3m** (LEAP-aligned position)
- **Why this bin:** Phase-10 confluence is estimated at **88** (raw
  +87 → normalized 88), which would map to the **0.85 band** by the
  confluence-scoring rubric. I am downgrading one notch to **0.75**
  (see `## Conviction deviation` below).

## Conviction deviation

Rubric maps confluence 88 → conviction 0.85. I am writing **0.75**
for these specific, falsifiable reasons:

1. **Two of five agents NEUTRAL on size, not direction** — the
   contrarian-scanner and risk-monitor both explicitly ratify the
   bull case but argue concentration + binary-event exposure should
   cap gross.
2. **Phase-1's 5-day sweep persistence ($1.054B,
   dominant_direction=bearish) [FLOW:sweep_persistence] is not fully
   resolved** by any other phase. The phase-1 / phase-8 contrarian-
   scanner interpretation is that it's "roll mechanics," but that's
   inference, not measurement.
3. **Macro is TRANSITIONAL** [MACRO:MarketRegime_2026-05-20] with
   the **June 11 CPI** and **~June 17 FOMC + dot plot** falling
   squarely inside any 30-DTE structure's window — binary tail
   risks that the confluence score does not penalize directly.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary    | $300.00 | Pullback tag of DP cluster $300.23 (5-day) AND intraday hold above $297.84 | [DP:price_levels] phase-2 |
| Aggressive | $298.00 | Flush to 5-day DP shelf $297.84/$298.21 AND DEX still positive on intraday | [DP:price_levels] phase-2, [STRUCT:dex] phase-4 |
| Fade       | $310.00 | Rejection at 5/22 weekly C00310 OI cliff (24,221 contracts) | [OI:biggest_increases] phase-3 |

The primary entry uses the dealer long-gamma cushion. The aggressive
entry uses the same support shelf the institutional buyer used on the
5-day window. The fade is a directional pivot trade — if AAPL is
rejected at $310, the upside is capped by dealer short-gamma above
that line and the long-only thesis pauses for re-validation.

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support (primary) | **$297.84** | [DP:price_levels] phase-2 ($1.13B 5-day premium) |
| Support (secondary) | $298.21 | [DP:price_levels] phase-2 ($1.31B 5-day premium) |
| Resistance (primary) | **$302.25** | [DP:largest] phase-2 ($1.18B today's clearing) + [INSIGHT:institutional_accumulation] phase-7 |
| Resistance (secondary) | $310.00 | [OI:biggest_increases] phase-3 (5/22 C00310 OI 24,221) |
| Gamma flip (0DTE) | $287.86 | [STRUCT:today_gamma_flip] phase-4 |
| Gamma trapdoor | $295.00 | [STRUCT:gex] phase-4 (net_gex flips sharply negative below $295) |
| Largest pin (≤7DTE) | $300.00 | [OI:pin_risk] phase-3 (pin_score 515,576) |
| Mega OI strike (monthly) | $300.00 (6/18) | [OI:decrease_with_volume] phase-3 (OI 80,746) |

## Invalidation

- **Price-based:** two consecutive daily closes below **$295.00**
  (gamma trapdoor) [STRUCT:gex] OR any intraday break of **$287.86**
  (today's 0DTE ZGL) without immediate reclaim same session
  [STRUCT:today_gamma_flip].
- **Signal-based:** phase-7 `insights_conviction_matrix` flips from
  DIRECTIONAL_LONG to HEDGED_LONG on next-day refresh
  [INSIGHT:conviction_matrix], OR phase-2 mega-tier DP buy_ratio
  drops below 0.55 on next-day [DP:block_stratified], OR phase-5
  `historical_cumulative_premium_flow` turns net negative for 3
  consecutive sessions [HIST:cumulative_premium_flow].
- **Macro-based:** **June 11 CPI** prints headline >3.8% YoY (above
  April print) OR core >2.8% YoY (above April core) — would force
  Fed pause/hawkish repricing and likely trigger AAPL gamma flip
  [MACRO:CPI_2026-04]. OR June FOMC drops easing bias / dot plot
  shifts higher [MACRO:FOMC_2026-04-29].

**Exit on invalidation:** **Hard stop, 100% close** on price-based
trigger (debit spreads cannot be rolled cheaply). **Tranche on
signal-based:** close 50% on first signal trigger, 50% if a second
signal fires within 5 sessions. On **macro-based** (hot CPI), close
100% before the FOMC if the CPI alone triggers a >2% AAPL gap down.

## Sizing (% of risk, NOT dollars)

For the primary directional structure (300/315 call debit spread
6/19 — see below):

- **Kelly inputs:**
  - p = **0.75** (conviction bin)
  - Entry = $5.00 net debit
  - Target = $13.50 (90% of max profit, exit at $310.00–$312.50 spot
    by mid-June — see structures section)
  - Stop = $2.50 net debit (50% of debit; matches a daily close
    below $295)
  - Payoff: target − entry = $13.50 − $5.00 = $8.50
  - Risk: entry − stop = $5.00 − $2.50 = $2.50
  - **b = 8.50 / 2.50 = 3.4**
- **Raw Kelly:** (0.75 × 3.4 − 0.25) / 3.4 = (2.55 − 0.25) / 3.4
  = 2.30 / 3.4 = **0.676 (67.6%)**
- **Suggested:** 0.676 × 0.25 fraction = **16.9%** of book risk
- **Cap:** 5% of book risk
- **Final size:** **5.0%** of book risk on max loss of the debit
  spread.
- **Deviation reason:** none (capped at the rubric ceiling, no upward
  deviation).

Translation: if the book runs $5M of total risk, the max acceptable
debit-spread max loss across this position is $250k. Each
300/315 6/19 spread caps loss at $500/contract → up to ~500
contracts. Recommended starting tranche: 30–40% of the cap on the
primary entry, scale to full on aggressive entry confirmation.

## Option structures

### Directional (primary)

- **Structure:** **Long call debit spread**
- **Strikes / expiry:** **Buy 6/19/26 $300 call, Sell 6/19/26 $315 call**
- **Net debit:** ~$5.00 per spread (model estimate — confirm at order
  entry; 6/18 300C avg today $7.42 [OI:decrease_with_volume],
  6/18 315C interpolated ~$2.40 from term IV 26.9%
  [STRUCT:iv_term_structure])
- **Spread width:** $15.00
- **Max profit:** $10.00 per spread (200% on debit)
- **Max loss:** $5.00 per spread (the net debit)
- **Breakeven:** $305.00 at expiry
- **Why this structure:** (1) **IV at 14.3rd percentile is cheap**
  enough that a long-vega leg is attractive [HIST:iv_percentile_zscore];
  (2) the 30-DTE expiry **straddles the WWDC keynote (~6/8–12) and
  expires 2 sessions after June FOMC (~6/17)** — captures both
  catalysts without sleeping through them
  [MACRO:FOMC_2026-04-29], [MACRO:AAPL_Q3FY26]; (3) the 300 long
  strike sits on the **largest near-term OI strike (80,746 contracts)
  and the institutional LEAP buyer's anchor strike**
  [OI:decrease_with_volume], [FLOW:sweeps].

### Defined-risk alternative

- **Structure:** **Put credit spread** (sell the dealer-long-gamma
  cushion)
- **Strikes / expiry:** **Sell 6/19/26 $297.50 put, Buy 6/19/26
  $287.50 put**
- **Net credit:** ~$2.70 per spread (model estimate from term IV
  26.9% [STRUCT:iv_term_structure])
- **Spread width:** $10.00
- **Max profit:** $2.70 per spread (the credit)
- **Max loss:** $7.30 per spread (width − credit)
- **Breakeven:** $294.80 at expiry
- **Why this structure:** Sells premium against the **5-day DP support
  shelf $297.84/$298.21** ($2.4B+ aggregate premium)
  [DP:price_levels] AND the **gamma trapdoor $295**
  [STRUCT:gex] AND **0DTE ZGL $287.86** [STRUCT:today_gamma_flip].
  The short strike sits at a level the institutional buyer would
  defend; the long strike sits below the 0DTE ZGL where the dealer
  regime flips and the trade is correctly invalidated.
- **Use this as a supplement** (≤30% of total directional risk) or
  as a stand-alone for desks unwilling to pay debit; the lower payoff
  ratio (Kelly 1.86% before cap) means it does NOT scale to the
  same 5% size as the primary.

## Macro overlay

**Tailwinds:**

- Technology sector **+$349.9M net inflow today (largest sector
  inflow)** [MACRO:SectorRotation_2026-05-20]
- SPY **above 20-SMA + 50-SMA, +5.28% trailing 30d**
  [MACRO:MarketRegime_2026-05-20]
- AAPL **Q2 FY26 $111.2B rev +17% YoY, EPS beat 3.6%** already
  printed and absorbed [MACRO:AAPL_Q2FY26]
- ISM Manufacturing 52.7, **ISM Services 53.6 (22nd consecutive
  expansion)** [MACRO:ISMServices_2026-04]

**Headwinds:**

- **April CPI re-accelerated to 3.8% YoY (from 3.3%)**, energy
  +17.9% [MACRO:CPI_2026-04] — narrows Fed cut path
- Market regime **TRANSITIONAL with 39.5% bullish breadth** —
  narrow leadership [MACRO:MarketRegime_2026-05-20]
- **June 17 FOMC + dot plot inside the trade window**
  [MACRO:FOMC_2026-04-29] — single largest binary event
- **June 11 CPI inside the trade window** — second consecutive hot
  print would break the long-gamma melt-up

**Net:** **mixed-tailwind** — the sector tailwind and structural
dealer bid carry the trade; the inflation/Fed track is the gating
risk inside the 30-DTE window.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-22** | Weekly OPEX (5/22 weekly) — AAPL 310C OI 24,221 [OI:biggest_increases] | Pin pressure into close; mean-reversion |
| 2026-05-30 (est) | April PCE inflation release | Mirrors CPI; risk +/− |
| 2026-06-06 (est) | May 2026 NFP / jobs report | Above 100k = neutral; below 50k = risk-off |
| **2026-06-08 to 06-12 (est)** | **Apple WWDC 2026 keynote** | AAPL-specific ±2–4% [MACRO:AAPL_Q3FY26] |
| **2026-06-11 (est)** | **May 2026 CPI release** | Critical — hot = invalidation; cool = squeeze fuel [MACRO:CPI_2026-04] |
| **2026-06-17 (est)** | **June FOMC + first 2026 dot plot** | Largest binary in window [MACRO:FOMC_2026-04-29] |
| 2026-06-19 | June monthly OPEX — AAPL 6/18 300C OI 80,746 [OI:decrease_with_volume] | Pin pressure to $300 |

## Post-trade monitoring checklist

- [ ] **Daily:** Re-pull `mcp__uw-pp__dark_pool_block_stratified` —
      watch mega-tier `buy_ratio` for drop below 0.55
      [DP:block_stratified].
- [ ] **Daily:** Re-pull `mcp__uw-pp__options_structure_gex` and
      confirm regime stays POSITIVE; alert if ZGL crosses above spot
      [STRUCT:gex].
- [ ] **Daily:** Re-pull
      `mcp__uw-pp__historical_cumulative_premium_flow` — invalidate
      if 3 consecutive sessions net bearish [HIST:cumulative_premium_flow].
- [ ] **T+1 (2026-05-21):** Verify the 2028-01-21 $300C OI jumped by
      ~10,000 contracts to confirm the LEAP package is a new long
      and not a same-day round-trip [FLOW:sweeps], [OI:biggest_increases].
- [ ] **2026-06-11 (CPI day):** Pre-event, reduce position 25%; post-
      event, scale back up only if headline ≤ 3.8% and core ≤ 2.8%
      [MACRO:CPI_2026-04].
- [ ] **2026-06-17 (FOMC day):** Pre-FOMC, reduce position to ≤50%
      of full size to mitigate dot-plot surprise [MACRO:FOMC_2026-04-29].
- [ ] **On any single-day close below $295:** close 100% per the
      hard-stop rule [STRUCT:gex].

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed
here for phase-10 spot-check:

1. **[FLOW:sweeps] — $54,110,903 ask-side sweep of AAPL 2028-01-21
   $300C, 10,608 contracts, avg price $51.43** — phase-1-flow.md
   §"Sweeps (ask vs bid)" row 1.
2. **[DP:block_stratified] — Mega-tier buy_ratio 0.794, $1,048,864,323
   premium across 18 prints** — phase-2-dark-pool.md §"Tier
   breakdown (single day)".
3. **[STRUCT:today_gamma_flip] — $1,383,658,924,735 GEX support_wall
   at $302.5; 0DTE ZGL $287.86** — phase-4-structure.md §"Today
   gamma flip (0DTE walls)".
4. **[HIST:iv_percentile_zscore] — IV30 22.92%, IV percentile 14.29,
   z-score −1.154, regime LOW_IV** — phase-5-historical.md §"IV
   regime".
5. **[MACRO:SectorRotation_2026-05-20] — Technology sector
   +$349,934,394 net flow (largest sector inflow today)** —
   phase-6-macro.md §"Market regime (UW)".
6. **[INSIGHT:conviction_matrix] — Scenario DIRECTIONAL_LONG, DP
   buy_ratio 0.672, "Dark pool buying + aggressive call purchases —
   institutional directional bet"** — phase-7-insights.md
   §"Conviction matrix".
7. **[AGENT:earnings-scout] — LONG conviction 4, "Own the
   WWDC+earnings combo via 30-DTE 300/315 debit call spreads with
   IV at 14th percentile"** — phase-8-agent-views.md
   §"earnings-scout".
