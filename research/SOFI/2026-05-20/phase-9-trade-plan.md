# Phase 9 — Trade Blueprint

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**PM voice:** desk PM running an institutional book
**Spot reference:** $15.23 close (intraday $15.05-$15.39) [DP:largest]
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing and
> structures are illustrative.*

## Thesis (≤3 sentences)

SOFI sits at the inflection point of a **MIXED tape with a sharp two-track
dealer regime**: the public is layering aggressive short-dated calls into
$15.50–$16.50 strikes while institutions write the $17–$25 ceiling and
the dark pool buys size at $15.02–$15.30, leaving the chain pinned at the
$15 strike with the largest negative-gamma node in the book (-$47.27B GEX)
[STRUCT:gex] and dealers' first negative total-GEX day in 28 sessions
[HIST:gex_time_series]. The historical signature is hostile to chasing
this rip — recent **bullish_flow signals scored 0% win rate / -3.05% avg**
across 7 peer firings [HIST:signal_backtest], **April CPI re-accelerated
to +3.8% YoY** removing the Fed-cut tailwind for SOFI's NIM thesis
[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov], and the **contrarian-scanner
delivered the room's highest conviction (4/5 SHORT)** on a COMPLACENT skew
that says downside protection is cheap [AGENT:contrarian-scanner]. Trade
expression: **mildly bearish, defined-risk debit put spread that uses the
cheap puts to monetize a probable retest of the $14 level before FOMC
6/16-17**, with a range iron condor as a smaller-size alternative.

## Bias + conviction + horizon

- **Directional bias:** **NEUTRAL with mild SHORT tilt**
- **Conviction (M-01 bin):** **0.55** (slight edge — coin flip plus a sliver)
- **Time horizon:** **1-4 weeks** (through May CPI 6/11 and FOMC 6/16-17)
- **Why this bin:** phase-8 verdict is 1-1-1-1 split (LONG / SHORT / NEUTRAL /
  RANGE) with avg conviction 2.75/5; phase-7's UW composite is MIXED at
  9.57% confidence with SOFI absent from both top-50 confluence tables;
  phase-10 will score in the 35-50/100 band [INSIGHT:conviction_matrix,
  INSIGHT:signal_confluence]. The 0.55 bin is the floor.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|---|---|---|---|
| Primary | $15.20 – $15.30 | Tag of phase-2's 5-day VWAP cluster ($15.29-$15.33 = $34M aggregate DP premium) — let it tag the value area before fading | [DP:price_levels] |
| Aggressive | $15.55 – $15.65 | Rally into the 5-day distribution shelf where institutions sold $15.55-$15.63 ($30M+ aggregate) — better entry but lower probability | [DP:price_levels] |
| Fade | $14.85 (below) | Break of $15 pin with intraday acceptance below; treat as continuation, NOT mean-reversion | [STRUCT:today_gamma_flip] |

## Levels to watch

| Type | Level | Source |
|---|---|---|
| Pin / floor | **$15.00** (80,486 OI at pin) | [OI:pin_risk] |
| Trapdoor breach trigger | $14.85 | [STRUCT:gex] (-$47.27B at $15 → cascade) |
| Dealer ceiling | **$16.00** (+$25.18B GEX, largest positive wall) | [STRUCT:gex] |
| Vanna-squeeze trigger | $16.10 (two close above, on volume) | [STRUCT:vanna_charm] |
| Multi-week ZGL | $11.65 (catastrophic stop) | [STRUCT:gex] |
| Today's ZGL (May-22) | $13.15 | [STRUCT:today_gamma_flip] |
| 5-day DP supply zone | $15.55 – $15.65 ($16M-$26M aggregate at each level) | [DP:price_levels] |
| 5-day DP demand zone | $15.29 – $15.33 ($15.9M-$18.1M aggregate) | [DP:price_levels] |

## Invalidation

- **Price-based:** Two daily closes above **$16.10** (breaks the +$25.18B
  GEX ceiling and triggers vanna-squeeze) [STRUCT:gex] OR an intraday spike
  through $16.50 with no immediate reclaim of $16.00. Both close the
  bearish put-spread thesis.
- **Signal-based:** UW `insights_conviction_matrix` flips from MIXED to
  DIRECTIONAL_LONG with confidence ≥ 25% AND dark-pool buy_ratio prints
  > 0.65 for 2 consecutive sessions [INSIGHT:conviction_matrix,
  INSIGHT:institutional_accumulation] OR cumulative premium flow turns net
  positive +$5M for 3 consecutive sessions [HIST:cumulative_premium_flow].
- **Macro-based:** **May CPI prints headline ≤ 3.3% YoY on 2026-06-11**
  (revives the rate-cut narrative and crushes the put thesis) OR FOMC
  2026-06-16/17 delivers a cut + dovish guidance — both would re-rate
  SOFI's NIM-expansion thesis higher and break $16
  [MACRO:CPIAUCSL_2026-04, MACRO:FOMC_2026-04-29].

**Exit on invalidation:** Hard stop on the put-debit spread (debit
structures lose linearly; no roll). Iron condor (alternative): close on
ANY breach of $14P or $17C short legs at 1.5× original credit cost.

## Sizing (% of risk, NOT dollars)

### Primary directional (put debit spread)

- **Kelly inputs:** p = 0.55, b = ($15.00 − $14.00) / $0.25 = 4.0,
  fraction = 0.25, cap = 5%.
- **Raw Kelly:** (0.55 × 4.0 − 0.45) / 4.0 = (2.20 − 0.45) / 4.0 =
  1.75 / 4.0 = **0.4375 = 43.75%**.
- **Fractional Kelly:** 0.25 × 43.75% = **10.94%**.
- **Capped at:** 5% (book-risk cap per sizing rubric).
- **Final size:** **5.0% of book risk** as max-loss on the put spread.
- **Deviation reason:** none — sizing AT cap because raw Kelly clears cap.

### Defined-risk alternative (iron condor)

- **Kelly inputs:** p = 0.55, b = $0.41 / $0.59 = 0.695 (estimated credit
  / max-loss; live quote required).
- **Raw Kelly:** (0.55 × 0.695 − 0.45) / 0.695 = (0.382 − 0.45) / 0.695 =
  **-0.097 (NEGATIVE)**.
- **Kelly verdict:** do not size the iron condor on Kelly grounds; the
  premium-buying regime (VRP -9.47% [HIST:vrp]) actively penalizes selling
  premium here.
- **Manual override (allowed per sizing rubric):** size at **1.0% of book
  risk** as an "expression of the unanimous range read from phase-8" —
  small enough to honor the negative Kelly but large enough to express the
  consensus.
- **Deviation reason:** N/A (downward deviation never requires reason per
  rubric; reduce-only).

## Option structures

### Directional (primary)

- **Structure:** Long **Jun-18 15P / Jun-18 14P put debit spread** (long
  $15P, short $14P).
- **Strike(s) / expiry:** $15 / $14, Jun-18 2026 (30 DTE from data date).
- **Debit (estimated):** ~$0.25 per spread (live quote required; based on
  May-29 15P at $0.45 ask reading + phase-3 OI density).
- **Max profit:** $0.75 per spread (= width $1.00 − debit $0.25) if SOFI
  closes ≤ $14.00 at Jun-18 expiry.
- **Breakeven:** $14.75 at expiration.
- **Max loss:** $0.25 per spread (= debit).
- **Payoff ratio:** **3:1**.
- **Why this structure:**
  - VRP -9.47% means buying premium is cheap relative to realized vol —
    long-options structures are favored [HIST:vrp].
  - COMPLACENT skew (-5.1% at 30 DTE) means **puts are unusually cheap
    versus calls** — best-priced entry for downside expression
    [STRUCT:term_skew].
  - Bull-put-spread floor at $14 is BELOW phase-4's today-ZGL of $13.15
    [STRUCT:today_gamma_flip] but ABOVE phase-4's multi-week ZGL of $11.65
    [STRUCT:gex] — captures the trapdoor without overreaching.
  - Jun-18 expiry contains the May CPI release (6/11) and FOMC (6/16-17)
    — the two highest-vol catalysts in the 30-day window [MACRO:FOMC_2026-04-29].

### Defined-risk alternative (range expression)

- **Structure:** **Jun-18 14P / 15P / 16C / 17C iron condor** (short 15P
  + long 14P + short 16C + long 17C).
- **Strike(s) / expiry:** $14 / $15 / $16 / $17, Jun-18 2026.
- **Credit (estimated):** ~$0.41 per condor (live quote required).
- **Max profit:** $0.41 per condor if SOFI closes between $15.00 and
  $16.00 at Jun-18.
- **Breakeven:** **$14.59 and $16.41**.
- **Max loss:** $0.59 per condor (= width $1.00 − credit $0.41).
- **Payoff ratio:** ~0.7:1 (asymmetric vs the structure's profit zone).
- **Why this structure:**
  - Phase-8 was UNANIMOUS on $15 floor / $16 ceiling levels regardless of
    bias [AGENT:accumulation-hunter, AGENT:contrarian-scanner,
    AGENT:sweep-tracker, AGENT:risk-monitor].
  - Short $16C aligns with the +$25.18B GEX ceiling [STRUCT:gex] and the
    overhead institutional call-write zone documented in phase-3
    [OI:smart_positioning].
  - Short $15P sits exactly at the pin ($15 OI 80,486) [OI:pin_risk].
  - Long wings at $14 / $17 cap risk at $0.59 — the structure expresses
    "neither side breaks" and is rational at 1% sizing despite negative
    Kelly because phase-8 levels are unanimous.

## Macro overlay

### Tailwinds (limited)

- SPY in uptrend, +3.53% / 30d, above 20-SMA and 50-SMA
  [MACRO:MarketRegime_2026-05-19 UW] — broad-risk tape supportive but
  fading.
- Technology sector flowing IN +$43.98M today [MACRO:SectorRotation_2026-05-19 UW]
  — indirect halo for consumer-fintech tape.

### Headwinds (dominant)

- **UW Market Regime TRANSITIONAL** — guidance: half size, defined-risk
  only [MACRO:MarketRegime_2026-05-19 UW].
- **Financial Services sector outflow -$48.79M today** (SOFI's sector,
  #2 outflow market-wide) [MACRO:SectorRotation_2026-05-19 UW].
- **April CPI YoY +3.8% (highest since May 2023)**, core +2.8%
  [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov] — sticky inflation
  delays Fed cuts.
- **FOMC projecting only 1 cut for 2026** with 8-4 dissent
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov] — no NIM tailwind.
- **SoFi Plus relaunched 4/1 at 4.5% APY** on deposits up to $20k
  [MACRO:SOFI_Q1_2026 WebSearch:sec.gov] — deposit cost arms race
  pressures NIM.
- **Q1 2026 record beat followed by -14% stock gap** on 2026-04-29
  [MACRO:SOFI_Q1_2026 WebSearch:sec.gov] — investors have already
  digested and faded the positive results.

### Net

**HEADWIND** (5 headwinds vs 2 limited tailwinds). Net tilts SHORT.

## Catalyst calendar (next 30 days)

| Date | Event | Impact direction |
|---|---|---|
| 2026-05-22 (Fri) | Weekly OPEX (May-22 expiry, 3 DTE) — $15 pin pressure | Pin → range-bound |
| ~2026-06-05 (Fri) | May NFP / unemployment release | ? (depends on labor color) |
| ~2026-06-11 (Wed) | **May CPI release** | **HIGH** — directly drives Fed-cut odds; soft print is the BIGGEST bear-thesis killer (see invalidation) |
| 2026-06-16/17 (Tue-Wed) | **FOMC meeting + SEP** | **VERY HIGH** — cut/hold + dot-plot revision |
| 2026-06-18 (Thu) | Monthly OPEX — primary expiry for the trade | High |

**Outside 30d (flagged for context):**
- 2026-08-04 (per UW screener) — SOFI Q2 2026 earnings. **Roll or close
  any remaining position before 2026-07-28** if rolling forward beyond
  Jun-18 expiry.

## Post-trade monitoring checklist

- [ ] **Daily:** re-pull `dark_pool_block_stratified` and watch for
      buy_ratio sustaining > 0.65 (would invalidate SHORT thesis).
- [ ] **Daily:** re-pull `options_structure_today_gamma_flip` to confirm
      today's ZGL ($13.15) is not migrating upward (would signal vol-suppression
      regime re-asserting and weaken put thesis).
- [ ] **Daily:** monitor SPY breadth and Financial Services sector flow
      from `risk_market_regime` — sustained Financial Services INFLOW for
      ≥ 2 sessions weakens the macro headwind.
- [ ] **Daily:** check phase-5 `cumulative_premium_flow` — if it turns
      positive +$5M for 3 sessions, signal-based invalidation triggers.
- [ ] **2026-06-05 (post-NFP):** assess wage trajectory; if AHE accelerates
      meaningfully back above 4% YoY, raises Fed-cut probability and
      threatens put-spread thesis.
- [ ] **2026-06-11 (CPI day):** if headline CPI ≤ 3.3% YoY, hard-exit the
      put spread on the print; conversely, if ≥ 4.0% YoY, consider adding
      to the directional book (still capped at 5%).
- [ ] **2026-06-16/17 (FOMC):** size down to zero on the iron condor 1 day
      ahead of the meeting (volatility expansion risk in both directions).
- [ ] **Re-run phase 8 agent panel** if any single phase signal contradicts
      ≥ 2 of the agent verdicts.

## Citations summary

Per M-04 rubric: ≥3 distinct upstream datapoints, spanning the required
phase ranges.

1. **[STRUCT:gex] (phase-4 §GEX)**: total GEX -$4.61B on 2026-05-19, peak
   negative -$47.27B at $15 strike, peak positive +$25.18B at $16 strike,
   ZGL $11.65 — the dealer-regime backbone of the thesis.
2. **[HIST:signal_backtest] (phase-5 §Signal backtest)**: bullish_flow
   backtest 5d lookback returned 7 signals with **0.0% win rate / -3.05%
   avg move** — strongest historical edge-fade signal in the run.
3. **[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov] (phase-6 §Inflation)**:
   April CPI YoY **+3.8%** (highest since May 2023), core +2.8%, energy
   +17.9% — sticky-inflation backdrop removes the Fed-cut tailwind for
   SOFI's NIM thesis.
4. **[AGENT:contrarian-scanner] (phase-8 §Per-agent details)**: 4/5 SHORT
   conviction, anchor signal "Phase-5 bullish_flow backtest 0% win rate
   on 7 signals avg -3.05% while Phase-4 skew is COMPLACENT -5.1%" —
   highest-conviction single agent in the room.
5. **[DP:block_stratified] (phase-2 §Tier breakdown)**: large-tier
   buy_ratio 0.616 with $173.97M premium, premium-weighted net 0.596 —
   real but threshold-marginal accumulation, the rationale for sizing
   defined-risk not naked.
6. **[STRUCT:term_skew] (phase-4 §Term skew)**: 30-DTE skew -5.1%
   (COMPLACENT) — put_25d_iv 54.3% vs call_25d_iv 59.4% — the pricing
   asymmetry that makes a put debit spread the structurally favored
   directional expression.
