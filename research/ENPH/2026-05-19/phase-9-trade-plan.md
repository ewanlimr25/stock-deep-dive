# Phase 9 — Trade Blueprint

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW data 2026-05-15)
**PM voice:** desk PM running an institutional book
**Spot reference:** **$52.94** (close 2026-05-15, sourced from
phase-7 `insights_deep_dive.uw_screener` + phase-1 top_premium_trades
intraday range $52.11–$53.31)
**Upstream phases cited:** phase-1 through phase-8

> *For research and educational use only. Not financial advice. Sizing
> and structures are illustrative.*

## Thesis (≤3 sentences)

**ENPH has three independent institutional accumulation fingerprints
firing in alignment** — dark-pool large-tier **buy_ratio 0.634 on $100M
premium across 549 trades** [DP:block_stratified], **5-of-5 bullish sweep
persistence with $55.8M cumulative premium** [FLOW:hot_chains_sweep_persistence],
and a **roll-up of Jun-2026 OI from $45/$60 calls into the $50/$55
strikes with $50C OI now 26,273** [OI:biggest_increases] — stacked on
top of a **POSITIVE-gamma dealer regime with the $50 wall worth +$2.78B
in net GEX** [STRUCT:gex] and a real commercial-channel tailwind from
**OBBBA preserving the 30% ITC for commercial solar through 2032 paired
with ENPH's IQ9S-3P commercial microinverter pre-order launch on
2026-05-13** [MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com]
[MACRO:ENPH_IQ9S-3P_2026-05-13 WebSearch:stockstotrade.com]. The
**single largest disconfirmer is phase-5's cohort backtest of bullish_flow
showing 14.3% win rate / −2.18% avg over 20d** [HIST:signal_backtest]
across the megacap-tech cohort, and **phase-4's inverted skew (−0.10,
calls richer than puts)** [STRUCT:term_skew] which signals crowded
long-side positioning — these argue for **defined-risk structures with
the trade size halved from raw Kelly**, not a thesis flip.

## Bias + conviction + horizon

- **Directional bias:** **LONG** (mild)
- **Conviction (M-01 bin):** **0.65**
- **Time horizon:** **1-4w** (target 6/18 monthly OPEX and 7/17 expiry as
  primary expiry choices; avoid 5/22 IV-rich)
- **Why this bin** (one sentence): Phase-8 desk is split 2 LONG / 2 SHORT
  (vol-short) / 1 NEUTRAL with avg conviction 3.6 → MIXED setup → rubric
  band 0.55–0.65; the ENPH-specific accumulation stack is qualitatively
  stronger than the failed megacap cohort, justifying the upper end of
  the MIXED band rather than 0.55.

## Entry zones

| Entry type | Price | Trigger condition | Source |
|------------|-------|-------------------|--------|
| **Primary** | **$51.50** | Tag of phase-2 at-spot DP accumulation cluster $51.14–$51.56 ($7.5M / 145k shares) | [DP:price_levels] |
| Aggressive | $50.20 | Test of the gamma wall $50 strike with hold of intraday low | [STRUCT:gex] |
| Fade | $54.50 | Rejection at phase-2 DP resistance cluster $53.19–$53.50 with phase-1 sweep flow turning bid-side puts | [DP:price_levels] [FLOW:sweeps] |

**Primary entry rationale:** the DP cluster at $51.14–$51.56 is where
554 large-tier blocks executed last week with buy_ratio 0.634. A
**pullback into this zone on the next 1–3 sessions** is the textbook
"buy where institutions bought" entry. Initiate **50% of the position at
$51.50** and **layer the remaining 50% on either a hold of $51.00 OR a
break above $53.50** (confirmation breakout).

## Levels to watch

| Type | Level | Source |
|------|-------|--------|
| Primary support | **$48.01** | [DP:price_levels] (5-day cluster $3.72M / 77,459 sh) |
| Secondary support | $51.14–$51.56 | [DP:price_levels] (at-spot cluster $7.5M / 145k sh) |
| Resistance #1 | **$53.50** | [DP:price_levels] (resistance cluster $2.83M / 53k sh) |
| Resistance #2 (extension target) | $55.00 | [OI:biggest_increases] Jun-26 $55C OI 7,292 building |
| Gamma flip / dealer pivot | **$50.00** | [STRUCT:gex] net_gex +$2.78B = largest wall |
| Short-gamma activation | **$40.00** | [STRUCT:gex] net_gex −$1.81B; below = negative-gamma trap |
| Long-term institutional floor | $37–$42 | [DP:price_levels] deep base $13.6M / 347k sh |
| Largest pin (OPEX week) | n/a | [OI:pin_risk] (ENPH absent — next OPEX 6/18, outside 7d window) |

## Invalidation

Per `rubrics/invalidation-rubric.md`, all three categories must be
concrete and falsifiable.

- **Price-based:** **Two consecutive daily closes below $48.01** (the
  phase-2 DP support cluster). Tightest of the three options — phase-3
  pin level not available (no OPEX window); phase-4 ZGL $15 is too
  loose to act on.
- **Signal-based:** **DP buy_ratio drops below 0.45 OR phase-7
  institutional_accumulation signal flips to DISTRIBUTION** on a daily
  re-pull. Either condition would invalidate the "accumulation continues"
  pillar of the thesis [INSIGHT:institutional_accumulation]
  [DP:block_stratified].
- **Macro-based:** **Hawkish surprise at the 2026-06-17 FOMC** (no cut
  signaled, dot-plot revised upward) combined with **Technology sector
  outflow exceeding −$200M cumulative** over the 5d post-FOMC
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]
  [MACRO:SectorRotation_2026-05-15 UW]. Either alone is mild; both
  together = thesis cracked.

**Exit on invalidation:** **TRANCHE EXIT** — close 50% on first
invalidation firing (e.g., two-day close < $48); close remaining 50% on
the second (e.g., DP signal flip OR FOMC + Tech outflow combination).
Rationale: at 0.65 conviction with mixed desk, full-exit-on-first
violation is too brittle; a tranche exit preserves capital while
retaining optionality on the LEAP-buyer's medium-term setup.

## Sizing (% of risk, NOT dollars)

Per `rubrics/sizing-rubric.md`:

- **Kelly inputs:**
  - p = **0.65** (conviction bin)
  - Entry: $51.50
  - Target: **$58.00** (above resistance #2 $55, anchored to the
    Aug-26 $60C ask-side sweep zone from phase-1)
  - Stop: **$48.00** (price-based invalidation)
  - b = |target − entry| / |entry − stop| = |58 − 51.50| / |51.50 − 48|
      = 6.50 / 3.50 = **1.857**
- **raw_kelly** = (p × b − (1 − p)) / b
  = (0.65 × 1.857 − 0.35) / 1.857
  = (1.207 − 0.35) / 1.857
  = 0.857 / 1.857
  = **0.4616** (46.16%)
- **× fraction 0.25** = 0.1154 = **11.54%**
- **× 100** = 11.54%
- **Cap_pct ceiling: 5.0%**
- **suggested_size_pct** = min(11.54%, 5.0%) = **5.0%**
- **Final size:** **5.0% of book risk** (at the cap)
- **Deviation reason (if any):** **none** — final = suggested = cap; no
  upward deviation. **However** the desk is genuinely split (phase-8
  2-2-1), and I am voluntarily **scaling down to 3.5% of book risk in
  practice** to respect the cohort backtest red flag and TRANSITIONAL
  macro regime per UW's own guidance. **Final practical deploy: 3.5%.**

  > Phase-10 should note: deviation_reason is DOWNWARD (always allowed
  > without justification), driven by phase-5 backtest 14.3% win rate
  > and phase-6 UW TRANSITIONAL "half size" guidance.

## Option structures

### Directional (primary) — Long Call Spread, July 17 expiry

| Spec | Value |
|---|---|
| **Structure** | **Long call spread (debit vertical)** |
| **Strike(s)** | Long Jul-2026 $50 call / Short Jul-2026 $55 call |
| **Expiry** | **2026-07-17** (63 DTE from 5/15) |
| **Debit (est.)** | ~$3.10 per spread (using phase-1 reference: Jul-17 $45C avg_price $10.58, Jul-17 $55C avg_price $5.79; $50C interpolates to ~$8.0; spread ≈ $8.0 − $4.9 ≈ $3.10) |
| **Breakeven** | $50 + $3.10 = **$53.10** |
| **Max loss** | $3.10 per spread = full debit |
| **Max gain** | ($55 − $50) − $3.10 = **$1.90 per spread** |
| **Risk/reward** | 1 : 0.61 (max gain / max loss) |
| **Strikes anchored to** | [OI:biggest_increases] Jun-26 $50C +4,985 OI (the dealer-pin) and $55C +3,714 OI (the resistance breakout target) |

**Why this structure:** IV rank 84.97 [INSIGHT:deep_dive] makes naked
long calls a losing trade against IV crush; the spread halves the vega
and keeps the directional capture. **The 7/17 expiry sits past the
5/22 IV decay window and past 6/17 FOMC, but stops before 7/28
earnings** [MACRO:ENPH_Q1_2026 WebSearch:investing.com] — so no IV-crush
or earnings-risk distortion. The $50/$55 strike pair is anchored to the
dealer wall and the next OI build, both directly from phase-3.

**Sizing translation:** 3.5% of book risk / $3.10 max loss per spread =
**~11.3 spreads per $1,000 of book risk**. (PM scales by their actual
book.)

### Defined-risk alternative — Iron Condor, June 18 expiry

| Spec | Value |
|---|---|
| **Structure** | **Iron Condor (short volatility)** |
| **Strikes** | Short Jun-2026 $48 put / Long Jun-2026 $45 put / Short Jun-2026 $58 call / Long Jun-2026 $63 call |
| **Expiry** | **2026-06-18** (34 DTE from 5/15 — monthly OPEX, heaviest OI concentration) |
| **Credit (est.)** | ~$1.05 net credit (put-side $0.55 from $48/$45 spread; call-side $0.50 from $58/$63 spread; IV-rich crush tailwind) |
| **Breakevens** | $48 − $1.05 = **$46.95** (downside) / $58 + $1.05 = **$59.05** (upside) |
| **Max loss** | $3 (wing width) − $1.05 (credit) = **$1.95 per condor** |
| **Max gain** | $1.05 per condor (full credit if both wings expire OTM) |
| **Risk/reward** | 1 : 0.54 — credit-to-max-loss |
| **Strikes anchored to** | Short $48P at phase-2 DP support cluster [DP:price_levels]; long $45P at phase-4 secondary gamma support [STRUCT:gex]; short $58C above phase-1 ask-side Aug $60C sweep zone [FLOW:sweeps]; long $63C beyond phase-1 sweep cluster ceiling. |

**Why this alternative:** monetizes the IV crush directly — phase-5 VRP
+0.115 means IV > realized by ~12 vol points, and phase-7 confidence_pct
of only 18.4% suggests the directional read is uncertain enough that
**non-directional vol selling captures the highest-confidence factor in
the run** (the IV-rich + post-event + no-binary-in-30d combo). Aligns
with both SHORT-vol agent votes in phase-8 [AGENT:earnings-scout]
[AGENT:contrarian-scanner]. The Jun 18 expiry **sidesteps the 7/28
earnings risk** while capturing the FOMC date inside the structure — the
PM accepts FOMC vol expansion as the primary risk.

**Sizing translation:** at 3.5% book risk and $1.95 max loss per
condor = **~17.9 condors per $1,000 of book risk**.

**Combo deployment:** **deploy BOTH structures in parallel at 1.75%
book risk each** (totaling 3.5% combined) — the call spread captures
directional upside, the iron condor monetizes IV crush + pins; they
HEDGE each other if ENPH chops sideways (condor wins, spread bleeds
mildly).

## Macro overlay

- **Tailwinds:**
  - **Commercial ITC 30% through 2032** [MACRO:OBBBA_2025-07-04
    WebSearch:arnoldporter.com] — direct tailwind for IQ9S-3P commercial
    microinverter channel.
  - **IQ9S-3P pre-orders opened 2026-05-13** [MACRO:ENPH_IQ9S-3P_2026-05-13
    WebSearch:stockstotrade.com] — already drove the +10–13% pop but
    momentum from product launches typically extends 2–4 weeks.
  - **IQ Solid-State Transformer demos late 2026** [MACRO:ENPH_IQ9S-3P_2026-05-13
    WebSearch:stockstotrade.com] — supports the LEAP-thematic Jun-2027
    combo from phase-1, gives medium-term holding patience.
  - **SPY uptrend, +4.01% 30d, above 20/50 SMA** [MACRO:MarketRegime_2026-05-15
    UW] — trend tailwind.

- **Headwinds:**
  - **UW regime TRANSITIONAL — "half size, defined-risk"**
    [MACRO:MarketRegime_2026-05-15 UW] — directly drove the 5.0% → 3.5%
    sizing voluntary downscale.
  - **Technology sector −$151,018,206 outflow on 2026-05-15**
    [MACRO:SectorRotation_2026-05-15 UW] — ENPH is Tech-classified;
    correlated drag.
  - **SPY breadth only 35.9% bullish** [MACRO:MarketRegime_2026-05-15 UW]
    — narrow tape.
  - **Residential ITC expired 2025-12-31** [MACRO:OBBBA_2025-07-04
    WebSearch:arnoldporter.com] — structural drag on residential
    cash-purchase channel; TPO partially mitigates through 2027.
  - **Fed on hold at 3.50–3.75% with 4 dissents** [MACRO:FOMC_2026-04-29
    WebSearch:federalreserve.gov] — solar consumer financing stays
    expensive.

- **Net:** **MIXED, mild headwind** on regime/sector; **mild tailwind**
  on company-specific commercial / AI-data-center catalyst stack.

## Catalyst calendar (next 30d)

| Date | Event | Impact direction |
|---|---|---|
| 2026-05-19 (Tue) | This deep-dive publication; week resumes post +41% 3-day rally | Mean-reversion risk |
| 2026-05-22 (Fri) | Front-month IV decay (the 121% IV bleed) | **+** for iron condor put-credit side; **−** for any debit position open into this week |
| 2026-05-26 (Mon) | US holiday (Memorial Day observed) | Neutral |
| 2026-06-05 (Fri) | May Nonfarm Payrolls release | Indirect; hot NFP → rate-hold extended, mild headwind |
| 2026-06-11 (Thu, est.) | May CPI release | Indirect; hot CPI → similar headwind |
| **2026-06-17 (Wed)** | **FOMC + SEP** | Major macro vol expansion; **risk for iron condor**, neutral for call spread (Jul expiry, post-event) |
| **2026-06-18 (Thu)** | **Monthly OPEX** — iron condor expiry | Mechanical — iron condor settlement; spot pins likely toward $50/$55 |
| **2026-07-17 (Fri)** | **Call spread expiry** | Trade window closes |
| 2026-07-28 (Tue, est.) | ENPH Q2 2026 earnings | OUT of our trade window for both structures — no earnings exposure |

## Post-trade monitoring checklist

- [ ] **Daily re-pull of `dark_pool_block_stratified` for ENPH** — confirm
  buy_ratio holds ≥0.55. If it drops below 0.45, tranche-exit per
  invalidation rubric.
- [ ] **Daily DEX sign check via `options_structure_dex`** — net DEX must
  remain positive call-heavy. Flip to put-heavy = bearish positioning
  shift.
- [ ] **Daily skew check via `options_structure_term_skew`** — if 25Δ
  skew normalizes from −0.10 toward +0.05 (puts re-bid above calls), the
  crowd is unwinding and the inverted-skew signal is exhausted; downgrade
  conviction.
- [ ] **IV30d decay path** — if IV30d falls from 95% toward 65% over
  the next 5 sessions, iron condor is winning the vol trade; consider
  taking 50% off at 50% max profit.
- [ ] **$50 wall hold via daily close** — if ENPH closes < $50 for two
  consecutive sessions, dealer hedging mechanics weaken; consider rolling
  the call spread strikes lower OR cutting it entirely.
- [ ] **Monitor Tech sector flow daily** — phase-6 said −$151M; if
  another −$100M day prints, sector drag is accelerating and ENPH likely
  goes with it.
- [ ] **5/22 IV decay (vol-of-vol resolution)** — if 5/22 expiry IV
  collapses from 121% to <80% without a news event, no surprise hit;
  thesis intact. If IV stays >100% into 5/21, a news event is brewing —
  re-evaluate before close.

## Citations summary

The thesis (M-04) cites these **6 distinct upstream datapoints**, well
above the ≥3 minimum:

1. **[DP:block_stratified]** — Large-tier buy_ratio **0.634** on
   **$100,009,416** premium, **549 trades**, 2026-05-15 (phase-2
   §Detailed findings).
2. **[FLOW:hot_chains_sweep_persistence]** — sessions_in_top **5 of 5**,
   total_sweep_premium **$55,813,662**, consistency_score **1.00**
   (phase-1 §Sweep persistence).
3. **[OI:biggest_increases]** — Jun-2026 $50 call OI **+4,985 to 26,273**
   (phase-3 §Largest OI increases).
4. **[STRUCT:gex]** — $50 strike net_gex **+$2,782,892,560** (phase-4
   §GEX); total GEX +$4.42B, regime POSITIVE.
5. **[MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com]** — Commercial
   ITC 30% through 2032; residential ITC expired 2025-12-31 (phase-6
   §Sector overlay).
6. **[HIST:signal_backtest]** — bullish_flow cohort 14.3% win rate /
   −2.18% avg over 20d (phase-5 §Signal backtest) — DISCONFIRMER
   explicitly cited as the reason for the half-Kelly sizing and the
   iron-condor alternative.

Additional supporting citations referenced in the trade structures:
- **[INSIGHT:conviction_matrix]** — DIRECTIONAL_LONG, confidence_pct
  18.4% (phase-7).
- **[STRUCT:term_skew]** — Skew −0.10, COMPLACENT (phase-4).
- **[AGENT:earnings-scout]** — IV-crush thesis (phase-8).
- **[AGENT:contrarian-scanner]** — crowded-long warning (phase-8).
- **[MACRO:MarketRegime_2026-05-15 UW]** — TRANSITIONAL, half-size
  guidance (phase-6).
- **[MACRO:SectorRotation_2026-05-15 UW]** — Tech −$151M outflow (phase-6).
- **[MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]** — 4 dissents
  (phase-6).
