# Phase 6 — Macro Overlay

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:56:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-5-historical.md

## Summary

Macro is a **net HEADWIND for RKT, partially cushioned by its post-merger servicing
book.** The decisive series for a mortgage lender — the **30-year mortgage rate — is
RISING (6.43% → 6.49% → 6.55%** over three weeks) while the **10y sits sticky at
4.57%**, even as Fed funds holds at **3.63%**. Higher long/mortgage rates suppress
origination/refi volume (RKT's core), though the Mr. Cooper servicing book (acquired
Oct-2025) partly offsets this — MSR values *rise* as prepayments slow, so the
combined entity is less of a pure "rates-down" bet than legacy Rocket. The market
regime is **TRANSITIONAL** ("reduce position size, wait for clarity") with weak
breadth (38.4% bullish). The dominant near-term catalyst is a **back-to-back cluster:
FOMC 07-29 (hold expected, but June minutes show a 9–8 split on a *hike* → hawkish
tail) immediately followed by RKT Q2 earnings 07-30** — exactly the event the phase-1
straddle and phase-4 ATM short-gamma pocket are positioned for. RKT has **no
correlation cluster** with the day's other blueprints.

## Key signals

- **30y mortgage rate 6.55%, rising +12bps in 2 weeks** → origination headwind `[MACRO:MORTGAGE30US_2026-07-16 FRED]`
- **FOMC 07-29 (hold expected; 9–8 split on a hike = hawkish tail) → RKT earnings 07-30** → back-to-back catalyst cluster `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`
- **Market regime TRANSITIONAL, breadth 38.4% bullish, SPY below 20/50-SMA** → risk-off tilt, size-down `[MACRO:MarketRegime_2026-07-17 UW]`
- **Financial Services net call-premium INFLOW +$270.9M, persistence 1/1 (5d)** — but bearish aggressor tilt (phase-0.5) → sector active but defensive `[MACRO:sector-flow-persistence UW]`
- **RKT uncorrelated with OKLO/PATH/SHOP** (only PATH/SHOP flagged 0.707) → diversifying, no size cut `[MACRO:portfolio-correlation UW]`

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-17 UW]`

- **Regime: TRANSITIONAL** — "Mixed signals, reduce position size, wait for clarity."
- SPY 743.29, **below 20-SMA (745.02) and 50-SMA (744.38)**, −0.94% 30d, −2.25% from
  90d high.
- Breadth: **2,420 bullish vs 3,878 bearish tickers → 38.4% bullish** (of 6,298).
  A soft, defensive tape → general headwind; corroborates the "size-down" caution.

### Inflation `[MACRO:CPIAUCSL_2026-06 FRED]`

- CPI (CPIAUCSL): **332.568 (Jun)**, 333.979 (May), 332.407 (Apr) — flat-to-slightly-
  down MoM, inflation **contained**. Fed Chair Warsh noted "inflation risks eased in
  recent weeks." Mildly supportive of *eventual* cuts, but not enough to pull long
  rates down now.

### Labor `[MACRO:UNRATE_2026-06 FRED]`

- Unemployment: **4.2% (Jun)**, down from 4.3% (May/Apr). Labor solid → reduces Fed
  urgency to cut → keeps long/mortgage rates elevated → indirect headwind for RKT.

### Rates `[MACRO:DGS10/DGS2/T10Y2Y/DFF/MORTGAGE30US FRED]`

| Series | Latest | Prior | Read |
|---|---|---|---|
| **MORTGAGE30US** | **6.55%** (07-16) | 6.49 (07-09) / 6.43 (07-02) | **rising → origination headwind** |
| DGS10 (10y) | 4.57% (07-16) | ~4.55–4.58 | sticky-high |
| DGS2 (2y) | 4.16% (07-16) | ~4.13–4.18 | stable |
| T10Y2Y (2s10s) | **+0.37** (07-17) | 0.42 (07-15) | normal but **flattening** |
| DFF (Fed funds eff.) | 3.63% | flat | target range 3.50–3.75% |

FOMC (WebSearch): **07-28/29 meeting, decision Wed 07-29 2:00pm ET.** Consensus =
**hold**; but June minutes show policymakers **split 9-to-8 on a 2026 hike** (sticky-
inflation hawks) → the risk skew is toward a *hawkish* surprise, which would lift
rates further and pressure RKT. Rising mortgage rates already price some of this.

### Activity / Consumer

Not separately pulled (ISM/U-Mich) — for a single rate-sensitive mortgage name the
rate complex above is dispositive; activity/consumer indices are second-order.
Marked neutral, justified by relevance (phase-6 pitfall: mark neutral when uncertain).

### Sector overlay (mortgage-specific)

- RKT is now a **diversified housing-finance platform**: Rocket origination + **Mr.
  Cooper servicing** (closed Oct-2025) + **Redfin real-estate** (closed Jul-2025).
  Q1 2026 adjusted revenue **~$2.94B (+117–127% YoY** on the acquisitions), GAAP net
  income $297M; **Q2 guidance $2.7–2.9B adj. revenue** (the 07-30 print marks against
  this). Cost synergies emerging ($140M from Redfin in <6mo).
- **Key nuance:** the servicing book is a **natural rate hedge** — rising rates slow
  prepayments and lift MSR marks, cushioning origination weakness. So the rising-rate
  headwind is *muted* vs legacy pure-Rocket. Integration execution (buyouts offered
  Mar-2026) is now as much the story as rates.

### Sector rotation `[MACRO:sector-flow / sector-flow-persistence UW]`

- **Financial Services today: net call-put premium +$270.9M** (call $532.5M vs put
  $261.7M), **5-day persistence score 1/1, trend INFLOW** (positive all 5 sessions:
  244M/381M/412M/170M/271M).
- **Reconciliation with phase-0.5** (which had Financials as the *most bearish* sector
  at −$57.2M): the two metrics differ — `sector-flow` measures **call-minus-put
  premium** (call-heavy = +$270M), phase-0.5 measured **bullish-minus-bearish
  aggressor premium** (net seller of calls/buyer of puts = −$57M). Both true: the
  sector trades lots of calls but the aggressor side is bearish — the same
  **call-writing** pattern seen in RKT itself. So the "INFLOW" is *activity*, not
  conviction longs.
- **Verdict: NEUTRAL** — the sector is active and not being abandoned (mildly
  supportive of a range/not-collapse read), but the aggressor bearishness aligns with
  RKT's own defensive flow. Not a clean tailwind or headwind for the thesis.
- `fz` breadth cross-check: **skipped** — RKT's `fz` payload is reduced
  (phase-0/7c); advisory-only lane, its absence changes nothing.

### Cross-name correlation `[MACRO:portfolio-correlation UW]`

- Concurrent 2026-07-17 blueprints: **OKLO, PATH, SHOP, RKT** (4 dirs found).
- 30-day pairwise: **only PATH/SHOP flagged (0.707, MODERATE)** — **RKT is in NO
  high-correlation pair** (its corr to each of OKLO/PATH/SHOP is <0.60).
- **Verdict: no cluster for RKT** → no correlation-driven size cut. RKT diversifies
  the book. (Sector field reads "Unknown" — the known UW sector-field bug; the
  *coefficients* are valid, per data-source note.)

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on RKT (mortgage) |
|---|---|---|---|---|
| 30y mortgage rate | 6.55% | 2026-07-16 | FRED | **Headwind** (origination) / partial tailwind (servicing MSR) |
| 10y Treasury | 4.57% | 2026-07-16 | FRED | Headwind (sticky-high) |
| 2s10s | +0.37 | 2026-07-17 | FRED | Neutral (normal, flattening) |
| Fed funds / FOMC | 3.63% / hold-w-hike-tail | 07-29 | FRED/WebSearch | **Headwind-skew** (hawkish tail) |
| CPI | 332.57 (flat) | 2026-06 | FRED | Mild tailwind (contained) |
| Unemployment | 4.2% | 2026-06 | FRED | Neutral (keeps rates up) |
| Market regime | TRANSITIONAL / 38.4% breadth | 2026-07-17 | UW | **Headwind** (risk-off) |
| Sector flow (Financials) | +$270.9M call inflow, persist 1 | 2026-07-17 | UW | Neutral |

## Catalyst calendar (next 30d)

**Front-expiry implied move: ±0.63% / ~$0.09 (1-day)** `[CTX:implied_move_pct]` — but
the **earnings-tenor** move is materially larger: the phase-1 Jul-24 ATM straddle
(~$0.96 combined premium, ~6.6% of spot for a 7-DTE pre-earnings expiry) and iv30d
0.694 imply an **earnings move of roughly ±8–10%** — the phase-9 range structures
must be sized to *that*, not the 1-day figure.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-07-29** | **FOMC decision (2pm ET)** | Hold expected; hawkish/hike tail → rate spike risk | can move RKT independent of earnings |
| **2026-07-30** | **RKT Q2 2026 earnings** | Guidance vs $2.7–2.9B adj rev; integration/synergy update | **~±8–10% implied** (straddle-priced) |

These two land **back-to-back**, inside the 08-21 options tenor — the dominant risk
event and precisely what the ATM long-gamma-short-pocket + straddle are positioned for.

## Tool / source errors

None. FRED API key present and all series returned (no CDN block — JSON API host).
`fz` breadth intentionally skipped (reduced RKT payload, advisory lane).

## DATA NOTE / CORRECTION

The `sector-flow` "+$270.9M INFLOW" vs phase-0.5 "−$57.2M most-bearish" apparent
contradiction is **not** an error — different metrics (call−put premium vs
bullish−bearish aggressor premium); reconciled in the rotation section rather than
silently dropped. Correlation `sector: Unknown` is the known UW sector-field bug; the
correlation coefficients themselves are valid and used.

## Verdict for downstream phases

- **Net macro bias for RKT: HEADWIND** (rising mortgage/long rates into a hawkish-tail
  FOMC + soft market regime), **cushioned** by the Mr. Cooper servicing hedge and
  contained inflation. Not a collapse setup — a "grind against a rate headwind with a
  binary event" setup.
- **Conviction: 3 / 5** — the rate direction is clearly adverse and well-sourced, but
  the servicing hedge and RKT's diversification blunt the transmission, and the market
  regime caution is broad, not RKT-specific.
- **Top 2 datapoints phase-9 must cite:** (1) 30y mortgage rate **6.55% rising**
  (origination headwind); (2) market regime **TRANSITIONAL / 38.4% breadth** (size-down).
- **Top 2 catalysts phase-9 must calendar:** (1) **FOMC 07-29**; (2) **RKT Q2 earnings
  07-30** (~±8–10% implied) — back-to-back.
- **Sector-rotation verdict: NEUTRAL**, persistence score **1/1** (active but defensive
  call-writing; neither aligned nor adverse to the thesis).
- **Correlation verdict: NO cluster** — RKT uncorrelated with OKLO/PATH/SHOP (only
  PATH/SHOP 0.707, RKT absent). No size cut; RKT diversifies the book.
- **Open questions:** does the fundamentals veto (7b) confirm the integration is
  accretive (servicing offsetting origination) or flag GAAP-loss/dilution risk from
  the all-stock deals? Does sentiment/positioning (7c) show short interest building
  into the rate headwind + earnings?
