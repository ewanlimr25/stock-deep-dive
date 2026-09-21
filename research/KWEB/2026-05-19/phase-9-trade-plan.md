# Phase 9 — Trade Blueprint

**Ticker:** KWEB
**As-of date:** 2026-05-19 (effective; user requested 2026-05-20 — UW data ended 5/19)
**PM voice:** desk PM running an institutional book
**Spot reference:** $28.34 (close $28.28) — [STRUCT:gex] / [INSIGHT:deep_dive]
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative.*

## Thesis (≤3 sentences)

KWEB is set up for a **constructive mean-revert toward the $29 dealer
magnet over the next 1–4 weeks**: phase-1's 5-day bearish sweep
persistence is dominated by **bid-side call OVERWRITING (call ask/bid
24,148 / 77,729 ratio 0.31, $94.9M cumulative)** [FLOW:sweep_persistence
/ INSIGHT:conviction_matrix] rather than directional put-buying, while
phase-3's **28-strike put SELL-to-open at $665K premium (OI +11,461,
5.4×)** [OI:smart_positioning] establishes a hard institutional floor
exactly at this week's lows. The 2026-05-20 **US-China tariff truce
extension headline** (Boeing 200-jet purchase + $30B reciprocal cuts,
[MACRO:USChinaTariff_2026-05-20]) just removed the bearish catalyst
that the chain was hedging, and the **POSITIVE GEX regime ($17.79B at
$29, $10.75B at $30, ZGL $23.81)** [STRUCT:gex] biases the path to a
$29 pin within the trade window. Sub-agents back this: phase 8 split
**2 LONG / 2 RANGE / 0 SHORT** with sweep-tracker at conviction 4
calling a Monday gap toward $29 [AGENT:sweep-tracker].

## Bias + conviction + horizon

- **Directional bias:** **LONG** (range-anchored — entries at $28
  support, target $29 magnet / $30 call-wall ceiling)
- **Conviction (M-01 bin):** **0.65** (moderate edge — more likely
  than not, with real disconfirming evidence from phase-2 mega-tier
  distribution and phase-5 bearish-flow backtest 100% win rate)
- **Time horizon:** **1-5d primary** (truce catalyst window); **1-4w
  secondary** (Jun 18 OPEX horizon)
- **Why this bin** (one sentence): phase-10 estimated confluence
  score lands in the 50-64 band, anchoring 0.65 per the
  confluence-scoring rubric — strong tactical thesis but real
  contradictions (mega-tier DP distribution, sector outflows) prevent
  going to 0.75.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| Primary | **$28.05** | tag of $28.06 DP cluster + 28P put-write floor holds | [DP:price_levels] $28.06 = $71M / 2.53M sh 5-day cluster; [OI:smart_positioning] May 29 28P OI 13,565 |
| Aggressive | **$28.50** | reclaim of intraday mean above $28.50 with positive sector flow | [STRUCT:today_gamma_flip] $28.5 strike GEX +$104M transition (first positive); [MACRO:SectorRotation_2026-05-19] confirm sector flow positive |
| Fade | **$30.46** | rejection at overhead distribution band $30.46-30.61 | [DP:price_levels] cluster $30.46-30.61 ~$127M institutional inventory (overhead) |

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Support — institutional floor | **$28.00** | [OI:smart_positioning] May 29 28P sold-to-open, $665K premium |
| Support — DP cluster | **$28.06** | [DP:price_levels] $71M 5-day premium |
| Resistance — primary magnet | **$29.00** | [STRUCT:gex] +$17,793M GEX (largest single strike) |
| Resistance — call wall ceiling | **$30.00** | [STRUCT:gex] +$10,752M GEX; [OI:smart_positioning] Jun 30C net ask−bid −6,018 |
| Resistance — distribution zone | **$30.46-30.61** | [DP:price_levels] ~$127M trailing-5d institutional inventory |
| Gamma flip (45-DTE) | **$23.81** (ZGL) | [STRUCT:gex] zero_gamma_level |
| Today's 0DTE flip | **$23.50** | [STRUCT:today_gamma_flip] atm_flip_strike |
| Short-gamma cliff (invalidation) | **$27.00** | [STRUCT:gex] -$7,098M GEX (largest negative) |
| Largest near-OPEX pin | n/a — KWEB not in 14-DTE pin list | [OI:pin_risk] KWEB absent (Jun 18 OPEX = 30 DTE) |

## Invalidation

- **Price-based:** **Two daily closes below $27.00** (negative-gamma
  cliff). The trade thesis depends on dealers staying long-gamma
  above the ZGL; sustained closes below $27 flip the regime to
  trend-acceleration and remove the magnet-to-$29 logic.
- **Signal-based:** Phase-7 `insights_conviction_matrix` DP buy_ratio
  drops **below 0.35** on the next refresh (deeper mega-tier
  distribution); OR `historical_cumulative_premium_flow` turns net
  bearish for **3 consecutive sessions** (currently MIXED at +$4.14M
  on $200M each side — a clean directional bear-tilt would mark the
  range bias broken).
- **Macro-based:** **US-China tariff truce extension explicitly walked
  back / rejected** within 5 sessions of the 2026-05-20 announcement;
  OR UW `risk_market_regime` flips from TRANSITIONAL to **RISK-OFF**.

**Exit on invalidation:** tranche exit — close 50% of the directional
debit spread at first invalidation (price OR signal), 50% at the
secondary. Put credit spread → roll out 30 days OR close at 75% of
max loss, whichever comes first.

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:**
  - p = **0.65** (M-01 bin)
  - Entry = $28.05, Stop = $26.95, Target = $30.00 (long underlying-
    equivalent for Kelly math)
  - Reward = $30.00 − $28.05 = $1.95
  - Risk = $28.05 − $26.95 = $1.10
  - **b = 1.95 / 1.10 = 1.773**
  - fraction = 0.25, cap_pct = 5
- **Raw Kelly:** `(0.65 × 1.773 − 0.35) / 1.773` = `(1.152 − 0.35) / 1.773` = **0.452 (45.2%)**
- **Suggested size:** `min(0.452 × 0.25 × 100, 5)` = `min(11.3, 5)` = **5.0% of book risk**
- **Final size:** **5.0%** (cap binds)
- **Deviation reason (if any):** None — at cap. If phase-10 confluence
  falls below 50, downsize to 3.0% (manual 60% haircut).

## Option structures

### Directional (primary)

- **Structure:** **Long Jun 18 / 29-31 call debit spread (1×1)**
- **Strike(s) / expiry:** Buy KWEB 2026-06-18 29C / Sell KWEB
  2026-06-18 31C
- **Debit/credit:** ~$0.53 net debit (29C ~$0.85 mid vs 31C ~$0.32
  mid, sourced from [OI:biggest_increases] avg prices $0.74 and
  $0.278)
- **Breakeven:** $29.53
- **Max profit:** $1.47 (at or above $31.00 at expiry)
- **Max loss:** $0.53
- **Reward / risk:** **2.77 : 1**
- **Strike selection rationale:** 29C sits on the **largest positive
  GEX wall ($17.79B)** [STRUCT:gex] — natural magnet. Short 31C caps
  at the +$2.61B GEX strike and rides the **call-overwriting tape
  from phase 3** [OI:smart_positioning] (Jun 30C net ask−bid −6,018,
  Jun 32C −1,665). Spread expiry catches the tariff-truce
  confirmation, June FOMC, and the **Jun 18 OPEX cliff (167K OI at
  31C, 98K at 30C)** — and naturally pins between 29 and 31.
- **Why a debit spread vs naked call:** IV30 at 0th percentile
  [HIST:iv_percentile_zscore] and VRP −3.92% [HIST:historical_vrp]
  argue debit > credit on a pure vol basis, but the structure
  *spreads* the debit to defray IV-rich short leg risk and limits
  exposure if a partial truce reversal triggers a fade.

### Defined-risk alternative

- **Structure:** **Short Jun 18 / 27-26 put credit spread (1×1)**
- **Strike(s) / expiry:** Sell KWEB 2026-06-18 27P / Buy KWEB
  2026-06-18 26P
- **Debit/credit:** ~**$0.26 net credit** (27P bid $0.46 today per
  phase 1; 26P ~$0.20 estimated)
- **Breakeven:** $26.74
- **Max profit:** $0.26 (if KWEB > $27 at June expiry)
- **Max loss:** $0.74
- **Reward / risk:** 0.26 : 0.74 ≈ **0.35 : 1** (typical credit
  spread asymmetry; offset by ~70% probability of full profit if the
  range holds)
- **Strike selection rationale:** Short 27P leverages the **$28
  institutional floor from phase 3** [OI:smart_positioning] and stays
  *inside* the −$7.10B short-gamma cliff at $27 [STRUCT:gex] — i.e.
  trade is intact unless the invalidation triggers.
- **Why this complementary structure:** if the desk is sceptical of
  the directional debit working (e.g. believes the range thesis but
  not the upside breakout), the put credit spread monetizes the
  *floor-defense* observation alone without requiring a $29 print.
  Can be sized as a stand-alone or as a third of the directional
  position.

**Combined sizing:** 5.0% book risk = 3.5% to directional debit
spread + 1.5% to defined-risk credit spread. Both expire 2026-06-18
to OPEX-align.

## Macro overlay (cite phase-6)

**Tailwinds:**
- 2026-05-20 **US-China tariff truce extension proposal** (Boeing
  200-jet + $30B reciprocal) [MACRO:USChinaTariff_2026-05-20] — direct
  KWEB-positive; explains phase-4 52.6% IV on May 22 expiry
- **FOMC 2026-04-29 dovish lean** (Miran dissent for cut, easing bias
  in statement) [MACRO:FOMC_2026-04-29] — mild risk-asset tailwind
- **15th Five-Year Plan tech self-reliance** structural narrative
  [MACRO:ChinaTechPolicy_2026]
- China **Q1 2026 GDP +5.0% YoY** [MACRO:ChinaQ1GDP_2026-04-16]

**Headwinds:**
- **China April retail sales +0.2% YoY (40-month low)**
  [MACRO:ChinaRetail_2026-04] — fundamental drag on consumption-
  driven KWEB constituents (BABA, JD, PDD, Meituan)
- April industrial production +4.1% YoY (miss)
- UW market regime **TRANSITIONAL, breadth 34.7%**
  [MACRO:MarketRegime_2026-05-19] — risk-reduction recommended
- **Sector outflows Comm Services −$84M, Consumer Cyclical −$27M**
  [MACRO:SectorRotation_2026-05-19] — KWEB's parent buckets

**Net:** **Tactical TAILWIND for the next 5–10 sessions** (truce
catalyst dominates), reverting to **HEADWIND-LEANING** beyond that as
weak China-consumption data continues to bite earnings. The trade
window matches this — debit-spread structure exits before the
HEADWIND tilt becomes the dominant input.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|------|-------|------------------|
| 2026-05-21/22 | US-China tariff truce confirmation window | **+** (large) |
| 2026-05-22 | KWEB May 22 weekly expiry (IV 52.6%) | **+** if truce confirmed; risk-off if slips |
| Mid-Jun | China May activity data (NBS) | ? (likely confirms slowdown) |
| 2026-06-15 | China May retail sales / IP | **-** if April-like miss |
| 2026-06-16/17 | **FOMC meeting** — possible cut start | **+** (mild) for risk-on |
| 2026-06-18 | **KWEB Jun OPEX** (167K @ 31C; 98K @ 30C; 13.6K @ 29P) | dealer-gamma cliff — expect $29-31 pin |

## Post-trade monitoring checklist

- [ ] **Daily**: re-check phase-7 `insights_conviction_matrix` DP
  buy_ratio. Trigger downgrade if it drops below 0.35.
- [ ] **Daily**: monitor phase-5 `historical_cumulative_premium_flow`
  daily delta. 3 consecutive net-bear days = invalidation.
- [ ] **Daily**: check phase-6 `risk_market_regime`. RISK-OFF flip =
  macro invalidation.
- [ ] **Daily**: track sector rotation. **Comm Services + Consumer
  Cyclical net flow MUST turn neutral or positive within 2 sessions
  for the LONG thesis to keep its 0.65 conviction**.
- [ ] **Every refresh**: re-run phase-1 `sweep_persistence` (5-day
  scan). If dominant_direction stays bearish for another 2 sessions
  AFTER today, downgrade to 0.55 and consider closing 50%.
- [ ] **Pre-trade**: confirm Jun 29/31 call spread bid-ask is tight
  (<10c wide); reject the fill if mid > $0.65.
- [ ] **Pre-trade**: confirm Jun 27/26 put credit spread credit ≥
  $0.20 net (else not enough premium for the risk).
- [ ] **After phase-10 audit**: if confluence score < 50, downsize
  combined position to 3.0% book risk and skip the directional
  debit leg (run credit-spread only).

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Listed here
for the phase-10 spot-check:

1. **[FLOW:sweep_persistence]** — KWEB dominant_direction=bearish,
   sessions_in_top 5/5, total_sweep_premium **$94,897,773** — see
   `phase-1-flow.md` §"Sweep persistence over 5 sessions".
2. **[DP:block_stratified]** — mega-tier buy_ratio **0.000** on
   **$25,871,032** total premium (913,698 sh) — see
   `phase-2-dark-pool.md` §"Tier breakdown".
3. **[OI:smart_positioning]** — KWEB 260529 28P OI Δ **+11,461 (5.4×)**,
   prev_bid_vol 6,300 vs prev_ask_vol 621 → inferred_direction
   **bullish (put sell-to-open)** — see `phase-3-positioning.md`
   §"Largest OI increases".
4. **[STRUCT:gex]** — KWEB net GEX at $29 = **+$17,793,645,641**;
   ZGL = **$23.81**; regime POSITIVE — see `phase-4-structure.md`
   §"GEX — per-strike profile".
5. **[HIST:iv_percentile_zscore]** — IV30d **30.24%**, percentile **0**,
   z-score **−1.82**, regime LOW_IV — see `phase-5-historical.md`
   §"IV regime".
6. **[MACRO:USChinaTariff_2026-05-20]** — China-Boeing 200-jet +
   Kuala Lumpur tariff truce extension proposal; reciprocal $30B
   cuts — see `phase-6-macro.md` §"US-China relations — fresh tape".
7. **[AGENT:sweep-tracker]** — LONG, conviction 4, target $29 magnet
   pin Monday — see `phase-8-agent-views.md` §"sweep-tracker".
