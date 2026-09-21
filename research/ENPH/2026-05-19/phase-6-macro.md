# Phase 6 — Macro Overlay

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-4-structure.md (5/22 IV catalyst), phase-5-historical.md

## Summary

Macro overlay is **mixed-to-mildly-headwind for ENPH** despite UW's
trend-positive market read. UW's `risk_market_regime` labels the tape
**TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"
[MACRO:MarketRegime_2026-05-15 UW]**: SPY in uptrend (above 20/50 SMA,
+4% 30d) but **bullish breadth is only 35.9%** (2,207 bullish vs 3,949
bearish-flow tickers on 6,156 with options) and **sector rotation shows
money flowing OUT of Technology (-$151M)** alongside Consumer Cyclical
(−$97M) and Financial Services (−$34M), into Energy / Consumer Defensive
/ Communication Services. **ENPH is classified Technology**, so the
sector flow is a direct **headwind**. The crucial ticker-specific finding:
**phase-4's 5/22 IV spike to 121.3% is NOT a forward earnings event** —
ENPH Q1 2026 was reported on or about 2026-05-13 [MACRO:ENPH_Q1_2026
WebSearch:investing.com], beating EPS $0.47 vs $0.44 consensus, with the
**IQ9S-3P Commercial Microinverter pre-order announcement driving a
+10–13% pop on 2026-05-13** [MACRO:ENPH_IQ9S-3P_2026-05-13
WebSearch:stockstotrade.com]. The 121% IV is **residual vol-of-vol from
the 3-day +41.3% rally**, not a clean binary catalyst. Macro rates: Fed
held 3.50–3.75% on **2026-04-29 with 4 dissents (most since 1992)** —
on hold, internally split [MACRO:FOMC_2026-04-29
WebSearch:federalreserve.gov]. Solar policy: **residential ITC expired
12/31/2025** under the OBBBA (One Big Beautiful Bill, signed 2025-07-04),
but **commercial ITC stays 30% through 2032** and **TPO leases qualify
through 2027** [MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com]. This
splits ENPH's setup: **headwind to residential cash-purchase microinverters,
tailwind to commercial IQ9S-3P + TPO channel rotation**.

## Key signals

- **UW regime TRANSITIONAL, breadth 35.9% bullish, SPY +4.01% 30d**
  [MACRO:MarketRegime_2026-05-15 UW] — favor defined-risk strategies,
  half position size per UW's own guidance.
- **Sector flow: Technology −$151,018,206 (largest outflow on the board)**
  [MACRO:SectorRotation_2026-05-15 UW] — direct headwind for ENPH as a
  Technology-classified name.
- **Fed funds 3.50–3.75% held on 2026-04-29; 4 dissents (1 dovish, 3
  hawkish-leaning)** [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]
  — rate-cut path is slow and contested; modest headwind for residential
  solar consumer financing.
- **Residential ITC for cash-purchase solar EXPIRED 2025-12-31** under
  the OBBBA [MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com] —
  structural residential headwind; mitigated by commercial 30% intact
  through 2032 and TPO 48E through 2027.
- **ENPH Q1 2026 already reported (~2026-05-13): EPS $0.47 vs $0.44
  consensus; Q2 guide $280–310M revenue including $85M safe-harbor
  shipments; IQ9S-3P pre-orders opened**
  [MACRO:ENPH_Q1_2026 WebSearch:investing.com,stockstotrade.com] —
  the 5/22 IV spike is post-event vol-of-vol decay + lingering
  policy-headline risk, **NOT a fresh binary event**.

## Detailed findings

### Market regime (UW: SPY + breadth + sector rotation)

`risk_market_regime` (date=2026-05-15):

| Field | Value |
|---|---|
| **regime** | **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity** |
| trend | UPTREND |
| spy.current | $738.65 |
| spy.above_20sma | true ($725.30) |
| spy.above_50sma | true ($691.37) |
| spy.change_30d_pct | +4.01% |
| spy.pct_from_90d_high | −1.45% |
| breadth.bullish_pct | **35.9%** (2,207 / 6,156 tickers) |
| breadth.bearish_flow_tickers | 3,949 |
| sector_inflow_top | Energy +$7.67M, Consumer Defensive +$6.00M, Communication Services +$5.29M |
| sector_outflow_top | **Technology −$151,018,206**, Consumer Cyclical −$96,719,081, Financial Services −$34,409,787 |

UW's own trading guidance for TRANSITIONAL regime: **"Half position sizes.
Favor defined-risk strategies."**

### SPY 10-day flow context

`historical_trend` symbol=SPY, days=10:

| Date | Close | Flow Direction | Net Flow ($M) | IV30d | IV Rank | PCR |
|---|---|---|---|---|---|---|
| 2026-05-15 | $739.11 | bearish | −42.1 | 0.154 | 27.2 | 1.03 |
| 2026-05-14 | $748.17 | bearish | −131.3 | 0.148 | 24.3 | 0.97 |
| 2026-05-13 | $742.31 | bearish | −171.6 | 0.153 | 27.4 | 1.19 |
| 2026-05-12 | $738.18 | bullish | +7.8 | 0.154 | 27.6 | 1.29 |
| 2026-05-11 | $739.30 | bearish | −63.1 | 0.157 | 29.4 | 1.31 |
| 2026-05-08 | $737.33 | bearish | −20.0 | 0.147 | 23.5 | 1.30 |
| 2026-05-07 | $731.58 | bearish | −6.7 | 0.148 | 23.7 | 1.14 |
| 2026-05-06 | $733.83 | bearish | −42.7 | 0.149 | 24.3 | 1.24 |
| 2026-05-05 | $723.76 | bullish | +3.9 | 0.149 | 23.6 | 1.36 |
| 2026-05-04 | $718.01 | bearish | −15.8 | 0.155 | 28.3 | 1.29 |

- **8 of 10 SPY sessions are bearish flow.** Index is grinding up on price
  but the options tape underneath is consistently put-heavy and net-bearish.
- VIX-proxy IV30d at 15.4% with IV Rank 27 = **low absolute vol** at the
  SPY level — the macro tape is calm-on-price but worried-in-options.
- This is a **late-cycle melt-up pattern**: tape goes up, breadth narrows,
  protection demand rises in size if not in price.

### Inflation (CPI, PCE)

**Skipped** for this run — no `FRED_API_KEY` env var set, so the FRED
JSON API is unavailable. WebSearch returns sufficient single-ticker macro
context without specific CPI / PCE prints; phase-9 should not need monthly
inflation levels for the trade plan. See `## Tool / source errors` below
for FRED setup instructions.

### Labor (NFP, unemployment)

**Skipped** for the same reason. Labor read is implicit in the FOMC
language below ("job gains have remained low").

### Rates (FOMC, dot plot, SOFR, 10y/2y, 2s10s)

`WebSearch: "FOMC May 2026 meeting statement rate decision"` and
`federalreserve.gov`:

- **Most recent FOMC decision: 2026-04-29.** Target range held at
  **3.50% – 3.75%**.
- **Four dissents** — most since late 1992:
  - **Stephen Miran**: dovish, wanted 25bp cut.
  - **Beth Hammack, Neel Kashkari, Lorie Logan**: opposed inclusion of
    easing bias in the statement (hawkish-leaning resistance to dovish
    pivot).
- Powell press conference flagged **oil-shock uncertainty from Middle
  East conflict** as a complicating factor — inflation still above 2%
  target, labor market slowing.
- Yahoo Finance live update (search result): "Federal Reserve forecasts 1
  rate cut in 2026" — implies the dot-plot midpoint is now ONE cut by
  year-end vs prior multi-cut expectations.
- **Next FOMC meeting**: per typical schedule, ~**2026-06-17** (calendar
  not directly verified but consistent with 7-week cadence).

**Reading:** Fed is on hold with internal division; the marginal news risk
is hawkish (3 of 4 dissents resisted dovish bias). For ENPH:
- **Mild headwind to residential solar consumer financing** (loan rates
  stay near 7–8%).
- **Mild tailwind via lower duration risk premium** if rates stop rising.
- **Net: marginal headwind, not catalytic.**

### Activity (ISM Mfg PMI, ISM Services PMI)

Not searched in this run; not load-bearing for a single-ticker solar/
microinverter trade. Phase-9 may flag if a major ISM release lands in
the trade window.

### Consumer (U-Mich, Conference Board)

Not searched in this run; same rationale.

### Sector overlay (solar / renewable energy)

`WebSearch: "residential solar" OR "solar tariff" OR "IRA" policy May 2026 Enphase`:

- **OBBBA (One Big Beautiful Bill), signed 2025-07-04** by President
  Trump: ended the 30% residential clean-energy credit for cash-purchase
  systems on **2025-12-31**.
  - **Impact on ENPH**: residential cash channel structurally impaired.
- **Third-Party Owned (TPO) systems remain eligible** for the 48E
  commercial credit through end of 2027. Channel shift to TPO leases /
  PPAs is the workaround for residential.
- **Commercial ITC remains 30% through 2032**, stepping down to 26% in
  2033 and 22% in 2034.
  - **Impact on ENPH**: IQ9S-3P commercial three-phase microinverter is
    perfectly timed for this channel — confirmed by the IQ9S-3P pre-order
    announcement on 2026-05-13 that drove a 10–13% rally
    [MACRO:ENPH_IQ9S-3P_2026-05-13 WebSearch:stockstotrade.com].
- **Safe harbor shipments** $85M in ENPH's Q2 2026 guidance reflect
  customers locking in equipment ahead of policy uncertainty / further
  changes — a known dynamic but not a fresh catalyst.
- **No specific tariff event** found for the 5/15–5/22 window. The 5/22
  IV is **vol-of-vol from the 3-day +41% rally and ongoing policy
  positioning**, not a clean binary.

### ENPH Q1 2026 earnings (already reported, ~2026-05-13)

`WebSearch: ENPH Enphase Energy earnings May 2026`:

| Item | Value |
|---|---|
| Reporting date | ~2026-05-13 (earnings call transcript dated May 2026) |
| Q1 2026 adjusted EPS | **$0.47** (vs $0.44 forecast — beat) |
| Q1 2026 revenue | **$282.9M** (vs $281.89M forecast — narrow beat) |
| Q2 2026 revenue guidance | $280M – $310M |
| Q2 IQ Battery shipments | 100–110 MWh |
| Q2 safe-harbor shipments | ~$85M |
| Headline product | **IQ9S-3P Commercial Microinverter** — U.S. pre-orders opened 2026-05-13; +10–13% intraday pop |
| Long-term platform | **IQ Solid-State Transformer** for AI data center racks; demos late 2026, volume shipments 2028 |

**Reading:**
- **Q1 was already reported** — the 5/22 IV at 121% is residual, not a
  fresh earnings event.
- The IQ9S-3P announcement is the **bullish catalyst that already
  printed** — phase-1's call sweeping is chasing this confirmed news.
- The **IQ Solid-State Transformer / AI data center angle** explains the
  Jun-2027 $70C / $45P LEAP combo from phase-1: this is **AI-thematic
  positioning on a long horizon** with the IRA/policy / earnings noise in
  near term as the price discovery vehicle.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Solar / ENPH |
|---|---|---|---|---|
| UW regime | TRANSITIONAL | 2026-05-15 | UW | **Headwind** — half size, defined risk |
| Sector rotation: Tech | −$151M outflow | 2026-05-15 | UW | **Headwind** — ENPH is in Tech |
| SPY breadth bullish | 35.9% | 2026-05-15 | UW | Headwind — narrow tape |
| SPY 30d | +4.01% | 2026-05-15 | UW | Tailwind — risk-on price action |
| FOMC funds rate | 3.50–3.75% (held) | 2026-04-29 | WebSearch:federalreserve.gov | Mild headwind — residential financing |
| FOMC dissents | 4 (1 dovish / 3 anti-easing-bias) | 2026-04-29 | WebSearch:federalreserve.gov | Mild headwind — slow-cut path |
| OBBBA residential ITC sunset | Expired 2025-12-31 | 2025-07-04 (signed) | WebSearch:arnoldporter.com | **Structural headwind** to residential cash channel |
| Commercial ITC | 30% through 2032 | OBBBA | WebSearch:arnoldporter.com | **Tailwind** for IQ9S-3P commercial |
| TPO / 48E credit | Eligible through 2027 | OBBBA | WebSearch:irs.gov | Mitigant — TPO channel still works |
| ENPH Q1 2026 beat | EPS $0.47 / Rev $282.9M | ~2026-05-13 | WebSearch:investing.com | **Tailwind** — already in price |
| IQ9S-3P pre-orders | Live 2026-05-13 | 2026-05-13 | WebSearch:stockstotrade.com | **Tailwind** — already drove +10–13% pop |
| IQ Solid-State Transformer | Demos late 2026 | 2026-05 disclosure | WebSearch:stockstotrade.com | **Tailwind (long-dated)** — explains LEAP combo |
| Middle East oil shock | Powell flagged | 2026-04-29 | WebSearch:federalreserve.gov | Neutral / ambiguous for ENPH |

**Net macro overlay: mildly headwind on the index/sector side, mildly
tailwind on ticker-specific company news, neutral on rates.** Phase-9
should respect UW's "half size, defined risk" guidance and lean toward
defined-risk option structures.

## Catalyst calendar (next 30d)

| Date | Event | Likely impact on ENPH |
|---|---|---|
| 2026-05-19 (this run) | Open of trading week post +41% rally | Mean-reversion risk if no follow-through |
| 2026-05-22 (Fri) | Front-month IV spike implied event (PHASE-4 flag) — most likely **vol-of-vol decay / further IQ9S-3P pre-order updates** | Neutral-to-bullish; main risk is **IV crush** if no news arrives |
| 2026-05-26 (Mon, observed Memorial Day) | US holiday — partial vol pull-forward | Neutral |
| 2026-06-05 (Fri) | **May Nonfarm Payrolls release** (BLS) | Indirect; hot NFP → rate-hold extended, mild headwind |
| 2026-06-11 (Thu, est.) | **May CPI release** (BLS) | Indirect; hot CPI → similar headwind |
| **2026-06-17 (Wed)** | **Next FOMC meeting + SEP** | Major macro event; dovish surprise = tailwind for solar financing |
| 2026-06-18 (Thu) | **Monthly OPEX** (ENPH heaviest OI at $50C, 26,273 contracts) | Mechanical — phase-3 / phase-4 levels matter most here |
| Late July (est.) | ENPH Q2 2026 earnings | Will appear in phase-6 of any run after late June |

## Tool / source errors

- **FRED skipped** — no `FRED_API_KEY` env var set. Public CSV endpoint
  is blocked at CDN. To enable automated rate / inflation / labor pulls,
  the user can register a free key at
  https://fred.stlouisfed.org/docs/api/api_key.html and `export
  FRED_API_KEY=…` in `~/.zshrc`. WebSearch on FOMC/policy was sufficient
  for this single-ticker macro overlay.

## Verdict for downstream phases

- **Net macro bias for ENPH:** **mildly headwind on regime/sector,
  tailwind on ticker-specific product news, neutral on rates.**
  Aggregate: **mildly headwind / mixed.**
- **Conviction:** **3 / 5** that macro should be a modest drag on
  position sizing, not a thesis-killer.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. **Sector rotation Technology −$151M outflow on 2026-05-15**
     [MACRO:SectorRotation_2026-05-15 UW] — direct ETF/index drag on ENPH.
  2. **OBBBA residential ITC expired 2025-12-31; commercial 30% intact
     through 2032; TPO 48E through 2027**
     [MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com] — ENPH's bull
     case depends on commercial IQ9S-3P + TPO rotation, not residential
     cash channel.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-06-17 FOMC meeting + SEP** — most binary macro event in the
     30d window.
  2. **2026-06-18 Monthly OPEX** — mechanical levels at $50C OI center
     dominate trade-management.
- **Trade-structure implications:**
  - Avoid the 5/22 expiry as a debit-call target (vol crush risk if no
    news arrives; IV at 121% pays for a binary that may not materialize).
  - **Prefer 6/18 monthly OPEX or 7/17 expiries** for directional debit
    structures — long enough to be past the 5/22 IV decay and the FOMC
    event, short enough to capture the IQ9S-3P momentum.
  - For credit/defined-risk: 5/22 short-vertical or iron-condor structures
    benefit from the IV crush — but require willingness to be wrong on
    direction.
