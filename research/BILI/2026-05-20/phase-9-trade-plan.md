# Phase 9 — Trade Blueprint

**Ticker:** BILI (Bilibili Inc. ADR, NASDAQ — Communication Services)
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T11:00:00-04:00
**PM voice:** Desk PM running an options-overlay book.
**Spot reference:** **$19.94** (phase-1 EOD top-premium underlying_price stamps,
EOD close $20.03 per phase-5 trend) — use **$20.00** as round working spot
for strike selection.
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md,
phase-6-macro.md, phase-7-insights.md, phase-8-agent-views.md

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

BILI just printed a strong **Q1 2026 beat (revenue +7% YoY, advertising +30%
YoY, first meaningfully-profitable quarter at 7.8% adj margin)** [MACRO:BILI_Q1_2026_2026-05-19
WebSearch:sec.gov], and institutions used the post-print dip to clear a
**$5.91M block-tier dark-pool buy_ratio = 1.00 ($2.46M at $19.65, $1.99M at
$18.82, all at-or-above NBBO mid)** [DP:largest], identity-matched to an
**$235k ask-side sweep of Jan-2027 $25 calls (1067 contracts at one
timestamp)** [FLOW:top_premium_trades] and a **−849-contract close of May-29
$25 calls** [OI:decrease_with_volume] — the textbook signature of a desk
rolling out a directional long. Dealers are now in a **fresh POSITIVE-gamma
regime (GEX +$226.8M, $20 strike alone +$117.6M, ZGL $19.11)**
[STRUCT:gex,HIST:gex_time_series], so the $20 magnet pins price into the 5/22
weekly OPEX while the institutional positioning ladder (long Jan-27 $25C /
short Jan-27 $30C / short Jul $30C / short weekly $17-$17.5 puts / long
8/21 $18 protective put) [OI:smart_positioning,biggest_increases] explicitly
**caps upside near $22-$25 over the next 4 weeks** — making a tight debit
call spread the structure that survives both the bull and bear sub-agent
readouts [AGENT:accumulation-hunter,contrarian-scanner].

## Bias + conviction + horizon

- **Directional bias:** **LONG (capped)** — plurality of phases 1–8
  conviction-weighted (LONG sum 7 vs SHORT sum 4 vs RANGE/NEUTRAL sum 4).
- **Conviction (M-01 bin):** **0.65** (moderate edge).
- **Time horizon:** **1-4w** (target exit by 2026-06-13, pre-FOMC).
- **Why this bin:** confluence is positive but constrained — dark-pool
  accumulation and post-earnings IV crush are clean signals, but
  Communication Services sector flow today is the worst in the market
  (-$84.3M) [MACRO:SectorRotation_2026-05-19 UW], BILI is **absent** from
  UW's bullish-confluence top-50 [INSIGHT:signal_confluence], and the
  Jul-17 $30 call OI build of +2,421 ALL bid-side
  [OI:biggest_increases] is institutional **call-writing** that caps upside.
  Pre-audit guess: phase-10 confluence ~60-65.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| **Primary** | **$19.65 – $19.85** | Pullback to today's block-tier DP cluster (189,972 sh / $3.73M / 8 trades cleared here) | [DP:price_levels] / [DP:largest] |
| **Aggressive** | **$19.11 – $19.25** | Tag of Zero-Gamma-Level — bounce off long-gamma cushion floor | [STRUCT:gex] (ZGL = $19.11) |
| **Fade** | **$22.30 – $22.50** | Rejection at 5-day DP overhead supply ($10.5M aggregate at $22.34 + $22.45) — switch to short-side / harvest defined-risk credit spread | [DP:price_levels] / [OI:biggest_increases] (22.5 put-roll strike) |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Lower base support | **$18.82** | [DP:largest] $1.99M opening-block absorption at NBBO ask |
| ZGL / gamma-regime line | **$19.11** | [STRUCT:gex] ZGL today |
| Primary DP accumulation | **$19.65** | [DP:price_levels] $3.73M / 189,972 sh / 8 trades |
| Magnet / pin | **$20.00** | [STRUCT:gex] +$117.6M (51.8% of total GEX) |
| First resistance | **$22.00–$22.50** | [STRUCT:gex] +$17.1M wall + [DP:price_levels] $10.5M 5-day overhead + [OI:biggest_increases] 5/22 $22C OI 2,512 |
| Institutional cap | **$25.00** | [OI:smart_positioning] Jan-27 $25C long-anchor, Jul-17 $30 short-write ceiling implies $25-$30 range |
| Hard upside ceiling | **$30.00** | [OI:biggest_increases] Jul-17 $30C +2,421 short-write |
| Pin risk (this week) | **none for BILI** | [OI:pin_risk] BILI absent — pin watch belongs to BABA $135 + FXI $37 (China sympathy) |

## Invalidation

- **Price-based:** **Two daily closes below $18.82** (the block-tier dark
  pool ask-fill at the regular-hours open). If breached: ZGL ($19.11) has
  already failed and price is mechanically accelerating through the
  -$5.4M negative-GEX zone at $17.5 [STRUCT:gex,DP:largest].
- **Signal-based:** **Conviction matrix flips from DIRECTIONAL_LONG to
  HEDGED_LONG** on a phase-7 daily refresh [INSIGHT:conviction_matrix],
  OR Phase-2 dark-pool **block-tier buy_ratio drops below 0.55** for two
  consecutive sessions [DP:block_stratified], OR cumulative-premium-flow
  turns net bearish for 3 consecutive sessions
  [HIST:cumulative_premium_flow].
- **Macro-based:** **6/17 FOMC delivers a hawkish surprise** under the new
  Fed chair [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov], OR
  US-China tariff escalation hits the China-ADR sympathy basket on a
  single-day >2σ move in KWEB / FXI [MACRO:KWEB_YTD_2026
  WebSearch:aol.com], OR Comm Services sector outflow >$150M/day on phase-6
  re-pull [MACRO:SectorRotation_2026-05-19 UW].

**Exit on invalidation:** **Hard stop** (close 100% at price-based level).
The defined-risk debit-spread structure is debit, so we close not roll.

## Sizing (% of risk, NOT dollars)

- **Kelly inputs:**
  - p = **0.65** (conviction bin)
  - Entry (debit-spread mid-mark estimate): **$0.85**
  - Stop (≈ half-debit if $18.82 breaks): **$0.40**
  - Target (max profit at expiry if BILI ≥ $22): **$2.00**
  - b = |target − entry| / |entry − stop| = ($2.00 − $0.85) / ($0.85 − $0.40) = $1.15 / $0.45 = **2.56**
  - fraction = 0.25, cap_pct = 5
- **Raw Kelly:** (0.65 × 2.56 − 0.35) / 2.56 = (1.664 − 0.35) / 2.56 = **0.513 = 51.3%**
- **Fractional-Kelly suggestion:** 0.25 × 51.3% = **12.8%** → capped at 5%
  → **suggested_size_pct = 5.0%**.
- **Final size: 3.0% of book max loss.**
- **Deviation reason (downward):** TRANSITIONAL market regime
  [MACRO:MarketRegime_2026-05-19 UW] mandates half-size; phase-7
  confluence is sub-threshold for BILI [INSIGHT:signal_confluence]; phase-8
  risk-monitor explicitly cited max 0.25R [AGENT:risk-monitor]; downward
  deviation is always permitted by the sizing rubric.

(Translation: at this size, max-loss of the spread sits at **3.0%** of the
book's at-risk budget. Use this as your premium-debit ceiling when sizing
contracts.)

## Option structures

### Directional (primary) — **June 18 $20 / $22 debit call spread**

- **Structure:** debit call spread (long $20C, short $22C).
- **Strike(s) / expiry:** **BILI Jun-18-2026 $20 Call / $22 Call (30 DTE).**
- **Estimated debit:** **~$0.85** ($85 per contract) at current 48% IV30d
  [HIST:iv_percentile_zscore] and inverted skew [STRUCT:term_skew].
- **Estimated breakeven at expiry:** **$20.85** (long strike + debit).
- **Max loss:** **$0.85 / contract** (the debit; hard floor).
- **Max profit:** **$1.15 / contract** ($2.00 spread width − debit).
- **Max profit at expiry trigger:** BILI close ≥ $22.00 on 2026-06-18.
- **Why this structure:**
  - **Strike rationale:** Long $20 = ATM at the dominant **+$117.6M GEX
    magnet** [STRUCT:gex]; short $22 = below the **+$17.1M GEX wall** and
    the **$22.30-$22.50 5-day DP overhead supply** [DP:price_levels] +
    the institutional 5/22 $22C wall (2,512 OI) [OI:biggest_increases].
  - **Expiry rationale:** 6/18 is monthly OPEX; spans the **6/17 FOMC**
    (event-risk overhang) — therefore we **target exit by 2026-06-13** to
    crystallize value pre-FOMC, accepting partial time decay. The 30-DTE
    horizon aligns with the agent-consensus 1-4w bias.
  - **Vol environment:** IV percentile 0 (LOW_IV) [HIST:iv_percentile_zscore]
    and VRP −3.87% (realized > implied) [HIST:vrp] → **buying premium is
    structurally favored**. The inverted call skew [STRUCT:term_skew] means
    we pay a small premium for the long $20 call but collect a fair price
    on the short $22 call — net neutral.

### Defined-risk alternative — **June 18 $18 / $19 put credit spread**

- **Structure:** put credit spread (sell $19P, buy $18P).
- **Strike(s) / expiry:** **BILI Jun-18-2026 $19 Put / $18 Put.**
- **Estimated credit:** **~$0.30** ($30 per contract) — puts are cheap in
  the inverted-skew environment [STRUCT:term_skew].
- **Breakeven at expiry:** **$18.70** (short strike − credit).
- **Max profit:** **$0.30 / contract** (the credit).
- **Max loss:** **$0.70 / contract** ($1.00 width − credit).
- **When to use this instead:** if entry zone fills above the primary
  ($19.65-$19.85) — i.e., you've missed the pullback and BILI is trading
  $20+. The credit spread monetizes the institutional put-write program
  [OI:biggest_increases] (5/22 $17/$17.5 puts at 488+441 OI all bid-side)
  by selling premium AT the lower band that institutional desks have
  already declared they're willing to take stock at. Breakeven $18.70 sits
  just below the lower DP support cluster $18.82-$18.98 [DP:price_levels].
- **Rationale:** Acknowledges contrarian-scanner's
  [AGENT:contrarian-scanner] thesis that **upside is capped at $22-$25**;
  a put credit spread captures range-bound behavior without paying for a
  directional call.

## Macro overlay

**Tailwinds**
- **BILI Q1 2026 earnings beat** (revenue +7% YoY / adj profit +62% YoY /
  advertising +30% YoY / DAU +8%) [MACRO:BILI_Q1_2026_2026-05-19
  WebSearch:sec.gov].
- **SPY +5.16% over 30d, in uptrend above 20+50 SMA** [MACRO:MarketRegime_2026-05-19
  UW] — broad equity backdrop is constructive (mild beta tailwind).
- **IV at LOW_IV regime** post-event crush [MACRO:BILI_IV_2026-05-19
  UW/HIST:iv_percentile_zscore] — long-premium structures are
  structurally favored.

**Headwinds**
- **Communication Services sector flow today −$84.3M (largest outflow
  sector)** [MACRO:SectorRotation_2026-05-19 UW] — BILI's own sector is
  bleeding.
- **Market regime: TRANSITIONAL — UW guidance: half size, defined-risk**
  [MACRO:MarketRegime_2026-05-19 UW]. Breadth 34.7% bullish only.
- **April CPI +3.8% YoY sticky; Iran-war oil spike**
  [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov] — risk-off geopolitical
  backdrop.
- **6/17 FOMC under NEW Fed chair** — first dot plot under new leadership
  [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov] — high event risk
  on 6/16-17.
- **China ADR sector weak — KWEB −16% YTD, ongoing US-China tariff
  escalation, VIE delisting overhang** [MACRO:KWEB_YTD_2026
  WebSearch:aol.com,china-briefing.com].

**Net:** **MIXED with single-name tailwind dominant short-term but sector
+ macro headwinds capping upside.** This is exactly why the trade is
sized at 3% (not 5%) and structured as a defined-risk debit spread (not
a naked long call).

## Catalyst calendar (next 30 days)

| Date | Event | Impact direction (BILI) |
|---|---|---|
| 2026-05-22 (Fri, T+2) | 5/22 weekly OPEX | **+ neutral** — $20 GEX magnet pin expected [STRUCT:today_gamma_flip] |
| 2026-05-25 (Mon) | US Memorial Day holiday | n/a (volume light, spread risk) |
| 2026-05-29 (Fri) | 5/29 weekly OPEX | + neutral |
| ~2026-06-04 | ISM Services PMI release (US) | ? macro risk |
| ~2026-06-06 | NFP release (US) | ? macro risk |
| ~2026-06-10 | May CPI release (US) | ? macro risk |
| **2026-06-16/17** | **FOMC + new Fed chair's first dot plot** | **− HIGH event risk** [MACRO:FOMC_2026-06-17] — **trade exit target: 2026-06-13** |
| 2026-06-18 (Thu) | Monthly OPEX (our expiry) | Position should be CLOSED by now |
| Late-Aug 2026 | BILI Q2 2026 earnings | + (separate trade) — institutional 8/21 $18 protective put OI build aligns [OI:biggest_increases] |

## Post-trade monitoring checklist

- [ ] **Daily**: re-pull `dark_pool_block_stratified` for BILI — confirm
  block-tier buy_ratio stays ≥ 0.55 [DP:block_stratified]. If it inverts
  for 2 consecutive sessions, signal-based invalidation fires.
- [ ] **Daily**: re-pull `options_structure_gex` — confirm BILI total GEX
  stays POSITIVE and ZGL stays ≤ spot − 1.5% [STRUCT:gex]. If ZGL crosses
  above spot or total GEX flips negative, gamma regime has broken.
- [ ] **Daily**: re-pull `risk_market_regime` and re-check Comm Services
  sector flow [MACRO:SectorRotation]. If Comm Services net flow continues
  at <$-100M/day for 3 consecutive sessions, sector headwind is
  intensifying.
- [ ] **Daily**: re-pull `insights_conviction_matrix` for BILI. If
  scenario flips from DIRECTIONAL_LONG to HEDGED_LONG or DIRECTIONAL_SHORT,
  exit. [INSIGHT:conviction_matrix]
- [ ] **Daily**: monitor BILI vs KWEB and FXI close-on-close correlation
  (use the 0.81-0.82 risk-monitor reference). If China-ADR basket cracks
  below their respective 30-day lows, exit on the sympathy cascade flag
  raised by [AGENT:risk-monitor].
- [ ] **Pre-FOMC (by 2026-06-13 EOD)**: close or flatten position
  regardless of direction. Do not carry the 6/17 FOMC event in this trade.
- [ ] **Watch for**: any China-ADR delisting headline, ANT Group / VIE
  policy news, BILI ad-revenue guidance update — these are the asymmetric
  tail risks that override the technical setup.
- [ ] **Re-run skill on 2026-05-27**: full re-pull of phases 1-5 + phase-7
  to capture mid-window updates ahead of FOMC.

## Citations summary

Minimum 3 distinct upstream datapoints (M-04 requirement). Spot-check
candidates for phase-10:

1. **[DP:largest] (phase-2-dark-pool.md §Largest blocks)** — block-tier
   dark-pool buy_ratio = 1.00, $5.91M total (3 trades / 307,752 shares):
   $2.46M at $19.65 +$0.005 above NBBO mid; $1.99M at $18.82 +$0.005
   above mid; $1.46M at $18.975 at mid.
2. **[FLOW:top_premium_trades] (phase-1-flow.md §Bullish bloc)** —
   Jan-2027 $25 call $235,084 ask-side sweep, 1067 contracts across 41
   prints, all at $2.20 / IV 59.5% / delta 0.41 / single timestamp
   18:28:07Z = institutional buy program.
3. **[OI:biggest_increases] (phase-3-positioning.md §Largest OI
   increases)** — Jul-17 $30 call OI +2,421 contracts (676 → 3,097, +358%),
   prev_ask 7 vs prev_bid 2,532 → institutional **call writing** ceiling.
4. **[STRUCT:gex] (phase-4-structure.md §GEX per-strike)** — Total GEX
   = +$226,786,819 POSITIVE; ZGL $19.11; $20 strike = +$117,596,555
   (51.8% of total) = dominant gamma magnet.
5. **[MACRO:BILI_Q1_2026_2026-05-19 WebSearch:sec.gov]
   (phase-6-macro.md §Tailwind/Headwind table)** — Q1 2026 revenue RMB
   7.47B (+7% YoY), adjusted net profit +62% YoY (margin 5.2% → 7.8%),
   advertising +30% YoY, DAU +8% YoY.
6. **[INSIGHT:conviction_matrix] (phase-7-insights.md §Conviction
   matrix)** — DIRECTIONAL_LONG, confidence 22.09%, DP buy_ratio 0.626
   (above 0.6 bull threshold).
7. **[AGENT:accumulation-hunter] (phase-8-agent-views.md §Per-agent
   details)** — LONG bias, conviction 4/5, "Real institutions bought
   the earnings beat in size at $18.82-$19.65 and rolled long-dated
   upside; ride them to $22.50 with hard stop $18.82."
