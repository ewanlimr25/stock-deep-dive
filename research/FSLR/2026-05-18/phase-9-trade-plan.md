# Phase 9 — Trade Blueprint

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**PM voice:** desk PM running an institutional options-overlay book
**Spot reference:** $234.48 close 2026-05-15 [STRUCT:gex] / $236.5 EOD prints from [DP:largest]
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

FSLR has a **structurally long-gamma dealer book** (total GEX +$452M, ZGL
$121.35, $250 strike = +$228M GEX magnet [STRUCT:gex]) that has absorbed a
+19.58% trailing-30d rally without divergence (price-vs-flow aligned bullish
[INSIGHT:price_vs_flow]) and a **two-tenor institutional $280 call campaign**
(Mar-2027 280C $1.39M ask single print, Δ0.48, vol/OI=10× [FLOW:options_flow_sweeps]
+ Dec-2026 280C +434 OI/$24.72 avg [INSIGHT:deep_dive]) — institutions are
laddering directional exposure ahead of the **Section 232 polysilicon tariff
decision** (presidential window open through ~late June 2026
[MACRO:Sec232_polysilicon_pending]), which the May-22 IV bump (58.2% vs 54%
neighbors [STRUCT:iv_term_structure]) and the $1.27M put-hedge layer
(May-22 230P / May-29 220P [FLOW:options_flow_sweeps]) are pricing as a
binary near-term event. The trade is **LONG via a defined-risk call debit
spread targeting the $250 gamma magnet** [AGENT:sweep-tracker], with a
**half-size discipline** mandated by the UW TRANSITIONAL regime
[MACRO:MarketRegime_2026-05-15] and the bullish_flow signal backtest's
26.3% win rate over 19 recent firings [HIST:signal_backtest].

## Bias + conviction + horizon

- **Directional bias:** **LONG**
- **Conviction (M-01 bin):** **0.75**
- **Time horizon:** **1-4 weeks** (carry through the Section 232 window;
  out by Q2 earnings 2026-07-30).
- **Why this bin** (one sentence citing phase-10 confluence): Phase-10
  pre-compute scores confluence at ~67/100 (band 65–79 → bin 0.75): five
  phases (1, 2, 3, 4, 6) align bullish, phase-7 composite is neutral, and
  phase-5's signal-backtest contradiction is real but mild; the phase-8
  agent vote is 2 LONG / 1 RANGE / 1 NEUTRAL with universal level
  convergence on support/resistance/invalidation.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **$233.00–$234.50** | Pull-in to the densest 5-day DP acceptance band ($234.54/$234.60/$234.90 cluster = $24M aggregate premium [DP:price_levels]) and hold above the dealer-buy zone | [DP:price_levels] + [STRUCT:gex] |
| **Aggressive** | **$237.50+** | Close above the upper DP shelf at $237 ($3.4M premium, the thinnest level on the board) with intraday volume confirmation — gamma-magnet pull engages to $240/+$142M GEX then $250/+$228M GEX | [DP:price_levels] + [STRUCT:gex] |
| **Fade (plan B)** | **$249.50–$250.50** | Tag the +$228M GEX magnet at $250 on Sec 232 *announcement*; trim 50% of directional and roll the rest into a short call-credit spread at $260/$270 against the long $240/$260 spread | [STRUCT:gex] + [AGENT:contrarian-scanner] |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Hard support | **$219.95** | Single $16.69M 5d crossing block (institutional floor) [DP:price_levels] |
| Primary support | **$231.62** | Largest 5d DP cluster $17.49M / 75K sh / 10 trades [DP:price_levels] |
| Acceptance support | **$234.54–$235.78** | Densest trade-count zone (17+12+12+3+5 trades; ~$30M premium) [DP:price_levels] |
| Negative-gamma wall (1y) | **$230** | −$46.5M GEX strike (45-DTE) [STRUCT:gex] |
| 0DTE resistance flip | **$230** | 0DTE −$29.9M GEX [STRUCT:today_gamma_flip] |
| Upside resistance shelf | **$237.00** | Thinnest upper DP level $3.4M [DP:price_levels] |
| Primary gamma target | **$240** | +$142M GEX wall (45-DTE); 0DTE +$293M support_wall [STRUCT:gex] + [STRUCT:today_gamma_flip] |
| Primary gamma magnet | **$250** | +$228M GEX (largest cluster in chain) [STRUCT:gex] |
| LEAP target ceiling | **$280** | Two-tenor 280C build (Dec-2026 +434 OI, Mar-2027 +480 vol) [INSIGHT:deep_dive] + [FLOW:options_flow_sweeps] |
| Zero-gamma flip (regime) | **$121.35** | Disaster floor — 48% below spot [STRUCT:gex] |

## Invalidation

- **Price-based:** **Two consecutive daily closes below $230** — breaks
  through the −$46.5M GEX put wall [STRUCT:gex], loses the long-gamma
  cushion, and clears the way to the $224–228 air gap toward the $219.95
  single-block institutional floor [DP:price_levels]. Universally endorsed
  by all 4 phase-8 agents.
- **Signal-based:** **`insights_conviction_matrix` flips from MIXED to
  HEDGED_LONG or DIRECTIONAL_SHORT** (currently MIXED with 1.66%
  confidence [INSIGHT:conviction_matrix]) **OR** dark-pool
  `institutional_accumulation` signal flips from NEUTRAL to DISTRIBUTION
  [INSIGHT:institutional_accumulation] **OR** large-tier DP buy_ratio
  falls below 0.50 for two consecutive sessions
  (currently 0.535 [DP:block_stratified]).
- **Macro-based:** **Section 232 polysilicon tariff decision delivers NO
  TARIFF / NO ACTION** [MACRO:Sec232_polysilicon_pending] — the
  idiosyncratic upside catalyst that justifies the binary asymmetry is
  removed; in this case, exit 100% same-day (no roll). **Secondary:** UW
  market regime flips from TRANSITIONAL to RISK-OFF
  [MACRO:MarketRegime_2026-05-15] with Tech-sector outflow extending
  beyond −$250M for two sessions.

**Exit on invalidation:** **Tranche exit** — close 50% on first
invalidation, 50% on second. Call debit spreads pencil this way because
remaining premium is recoverable on partial moves.

## Sizing (% of risk, NOT dollars)

**Kelly inputs (primary directional call debit spread):**

- **p** = 0.75 (M-01 conviction bin)
- **Entry assumption:** debit $8.50 on Jul-17 $240/$260 call debit spread
- **Target:** stock at $250 → spread worth ~$11.50 (~75% intrinsic capture by July
  if catalyst lands within window) → profit $3.00
- **Stop:** stock breaks $230 → debit spread loses ~50% of value to ~$4.25 →
  loss $4.25
- **Payoff ratio b** = |target - entry| / |entry - stop| in spread-value
  terms = 3.00 / 4.25 = **0.71**

  Note: at-target value of $11.50 is the *interim* not max ($20 width). I'm
  modeling a partial-win not the max-win because catalyst timing is
  uncertain and theta will erode the long-call faster than the short-call.

- **Raw Kelly:** (p × b − (1 − p)) / b = (0.75 × 0.71 − 0.25) / 0.71
  = (0.533 − 0.25) / 0.71 = **0.398** → **39.8%**
- **Fractional Kelly (0.25):** 39.8% × 0.25 = **9.95%**
- **Cap (5% of book risk):** 5.0%
- **Suggested size:** **5.0%** (cap binds)
- **Final size:** **3.0%** (voluntary reduction below suggested)
- **Deviation reason:** none required for reduction below suggested.
  Reduction rationale (informational): risk-monitor flagged a correlation
  triple-stack (Tech beta + solar-policy beta + Sec 232 binary
  [AGENT:risk-monitor]); the bullish_flow signal backtest is 26.3% in the
  current regime [HIST:signal_backtest]; UW TRANSITIONAL regime guidance
  is "half position sizes" [MACRO:MarketRegime_2026-05-15].

## Option structures

### Directional (primary)

- **Structure:** Long call debit spread
- **Strike(s) / expiry:** **Long Jul-17-2026 $240C / Short Jul-17-2026
  $260C** (61 DTE from 2026-05-18)
- **Debit/credit:** ~$8.50 debit (estimated from phase-1 reference prices —
  Jul-17 $270C printed at $9.12 bid earlier in the session
  [FLOW:options_flow_sweeps]; assume Jul $240C ≈ $15, Jul $260C ≈ $6.50)
- **Width:** $20
- **Breakeven:** $248.50 underlying at expiry
- **Max profit:** $11.50 (if stock ≥ $260 at expiry)
- **Max loss:** $8.50 (debit)
- **Why this structure:** Jul-17 expiry sits **after** the Section 232
  decision window closes (≈late June) but **before** Q2 earnings 2026-07-30
  — no earnings IV crush exposure. The $240/$260 spread crosses both the
  +$142M call wall and brackets the +$228M $250 magnet, capturing the full
  gamma-magnet pull mechanism described in [STRUCT:gex]. IV is mid-range
  (IV30 52.8%, IV rank 37.8 [HIST:iv_percentile_zscore]) so debit cost is
  fair-priced; VRP +9.8 vol pts [HIST:vrp] argues mildly against pure
  long-vol but the structural advantage of long-gamma + binary catalyst
  outweighs the premium-selling tailwind for a directional debit. The
  long leg captures dealer hedge-bid mechanics through the $240 wall; the
  short leg caps the trade *exactly* at the magnet — accepting capped
  upside in exchange for ~30% lower premium than a naked long call.

### Defined-risk alternative (premium harvest, optional secondary)

- **Structure:** Short put credit spread (May-22 weekly)
- **Strike(s) / expiry:** **Short May-22-2026 $230P / Long May-22-2026 $225P**
  (4 DTE from 2026-05-18)
- **Debit/credit:** ~$1.00 net credit (May-22 230P ≈ $4.50, May-22 225P ≈
  $3.50 [FLOW:options_flow_sweeps])
- **Width:** $5
- **Breakeven:** $229.00 underlying at expiry
- **Max profit:** $1.00 (full credit, if stock ≥ $230 at expiry)
- **Max loss:** $4.00 ($5 width − $1 credit)
- **Why this structure:** Harvests the **May-22 IV bump** (58.2% IV vs
  54.1% for May-29 [STRUCT:iv_term_structure]) at strikes that sit at /
  below the −$46.5M GEX put wall [STRUCT:gex] and below the $231.62 DP
  acceptance cluster [DP:price_levels]. VRP regime is PREMIUM_SELLING
  (+9.8 vol pts) [HIST:vrp]. Endorsed by [AGENT:risk-monitor]. Sized
  small (≤2%) and complementary to the directional debit — pairs with
  the call spread to harvest theta on the downside while the directional
  leg captures the upside. **Catalyst-timing caveat:** if the Section
  232 decision arrives within the 4-DTE window with a *negative*
  outcome, this spread carries asymmetric loss risk; close on Sec 232
  no-tariff headline immediately.
- **Sizing for this leg:** 2.0% of book risk (separate from the 3.0%
  directional sizing; combined book deployment ≤5%).

## Macro overlay (cite phase-6)

**Tailwinds:**
- **Section 232 polysilicon tariff decision pending, window open through
  ~late June 2026** — FSLR is the largest US-domiciled CdTe (non-poly)
  manufacturer; a tariff disproportionately costs competitors and is a
  near-pure tailwind for FSLR [MACRO:Sec232_polysilicon_pending].
- **FEOC/FEOP Treasury interim guidance + July-4 deadline** for 10%
  bonus ITC — FSLR's vertically-integrated US supply chain is
  FEOC-clean by construction [MACRO:FEOC_2026 WebSearch:utilitydive.com].
- **Section 45X advanced manufacturing production credit** already
  driving FSLR Q1 gross margin to 46.6% (vs 40.8% YoY) [MACRO:FSLR_Q1_2026-04-30].
- **ISM Mfg PMI 52.7 (April, 4th consec expansion month)** — mild
  utility-scale capex tailwind [MACRO:ISM_2026-04].
- **Analyst consensus 30 Buy / 5 Hold / 1 Sell, median PT $277** — sell-side
  is constructive [MACRO:AnalystConsensus_2026-05].

**Headwinds:**
- **UW market regime TRANSITIONAL** — only 35.9% bullish-flow breadth,
  Tech sector daily flow −$151M (FSLR tagged Technology)
  [MACRO:MarketRegime_2026-05-15].
- **Headline CPI +3.8% YoY (April), highest since May 2023** — Iran-war
  energy spike pushed inflation reacceleration; bad for rate-sensitive
  growth [MACRO:CPI_2026-04 WebSearch:bls.gov].
- **FOMC held 3.50–3.75% with 8–4 split** (largest dissent since 1992) —
  Fed policy frozen; no imminent rate cuts [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- **Bullish_flow signal backtest 26.3% win rate / −1.26% avg 20d** across
  19 recent firings [HIST:signal_backtest] — the broader regime is
  hostile to naive bullish-flow setups.

**Net:** **Idiosyncratic tailwind > broad headwind for FSLR.** The Section
232 catalyst dominates the immediate horizon; broad-tape headwinds set
the sizing ceiling rather than reverse the bias.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| **2026-05-18 → ~2026-06-29** | **Section 232 polysilicon presidential decision window** | **+** (likely, asymmetric) |
| **~2026-05-22** | One-week IV-bump expiry (matches May-22 58.2% IV [STRUCT:iv_term_structure]) — implied catalyst timing | **+/−** (binary) |
| ≤2026-06-30 | Treasury FEOC interim rulemaking guidance | + |
| ~2026-06-06 | May NFP release | broad-tape |
| ~2026-06-11 | May CPI release | broad-tape (rate-sensitive sectors) |
| 2026-06-16–17 | June FOMC + dot plot | broad-tape |
| 2026-07-04 | FEOC deadline for 10% bonus ITC | + |
| 2026-07-30 | FSLR Q2 2026 earnings (outside 30d window) | n/a here |

## Post-trade monitoring checklist

- [ ] Daily: re-check `dark_pool_block_stratified` large-tier buy_ratio —
      thesis intact if ≥0.50, weak if <0.50 [DP:block_stratified].
- [ ] Daily: re-check `options_structure_gex` total GEX and ZGL — regime
      should remain POSITIVE with ZGL well below spot. If ZGL crosses up
      through $200 OR regime flips NEGATIVE, exit half [STRUCT:gex].
- [ ] Daily: scan for any Section 232 / FEOC headline from
      regulations.gov, BIS, Treasury, or major solar trade publications
      (pv-tech.org). Any "no tariff" headline = same-session exit
      [MACRO:Sec232_polysilicon_pending].
- [ ] Each major session: re-check `insights_conviction_matrix` — flip
      from MIXED → HEDGED_LONG or DIRECTIONAL_SHORT is a
      signal-invalidation trigger [INSIGHT:conviction_matrix].
- [ ] Phase-1 re-run on any "tariff decision imminent" news leak — look
      for new ATM long-dated calls and net flow >$5M same-side in one
      session [FLOW:options_flow_sweeps].
- [ ] Phase-4 re-run if intraday breaks $230 OR $240 — gamma map updates
      drive trade-management decisions [STRUCT:today_gamma_flip].
- [ ] Re-invoke `earnings-scout` agent in late June (within 30d of
      2026-07-30 earnings) — earnings is post-trade-window but reading
      earnings positioning is sensible for re-entry.
- [ ] Weekly: rerun `historical_signal_backtest` — if bullish_flow win
      rate climbs above 50% market-wide, broader regime is healing and
      sizing can be normalized [HIST:signal_backtest].

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed here for
audit:

1. **`$250 strike net GEX = +$228,076,645`** — primary gamma magnet anchor
   for target selection
   [STRUCT:gex] — phase-4-structure.md §GEX
2. **`Mar-2027 $280C $1,668,000 ASK premium, vol/OI = 10.0, Δ = 0.479`** —
   institutional directional anchor
   [FLOW:options_flow_sweeps] / [FLOW:options_flow_unusual_volume] — phase-1-flow.md §Sweeps
3. **`5-day dark-pool cluster $231.62 = $17,493,100.50 premium`** —
   primary support level
   [DP:price_levels] — phase-2-dark-pool.md §Price levels
4. **`Section 232 polysilicon decision window open through ~late June 2026`** —
   dominant idiosyncratic catalyst
   [MACRO:Sec232_polysilicon_pending] — phase-6-macro.md §Sector overlay
5. **`Bullish_flow signal backtest win rate 26.3% / avg −1.26% across 19 firings`** —
   sizing constraint
   [HIST:signal_backtest] — phase-5-historical.md §Signal backtest
6. **`UW market regime TRANSITIONAL — half position sizes`** — sizing
   guidance source
   [MACRO:MarketRegime_2026-05-15] — phase-6-macro.md §Market regime
7. **`Phase-8 plurality LONG 2/4, universal levels $231.62 / $250.00 /
   close < $230`** — agent confluence
   [AGENT:sweep-tracker] / [AGENT:accumulation-hunter] — phase-8-agent-views.md §Agent verdicts table

(Phase-10 will spot-check at least 2 of these.)
