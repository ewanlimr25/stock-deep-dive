# Phase 6 — Macro Overlay

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T21:05:00-0400
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md, phase-5-historical.md

## Summary

The catalyst phases 1–5 kept asking about is identified and it is **sector
beta, not idiosyncratic**: Broadcom's Wed-evening (Jun-3) earnings guided Q3 AI
chip sales to $16bn vs $17.2bn expected and did not raise its 2026 AI forecast,
triggering a two-day AI-infrastructure rout (AVGO −12%, MU/SNDK ~−12% Friday,
Nasdaq −4% Jun-5, ~$1T wiped) that NBIS rode down −12.27% ($259.67 → $227.81,
range $216.69–250.75). The macro overlay is **headwind-stacked** for a
high-multiple AI-infra name: UW regime "TRANSITIONAL — reduce position size",
SPY below its 20-SMA with VIX 16.7→21.51 in 10 sessions; inflation re-elevated
(CPI +3.78% YoY, core PCE +3.29%); Friday's strong jobs print (May NFP +172k,
U3 4.3%) plus 2y at 4.05% vs Fed funds 3.62% have the market pricing **hike**
risk into a Fed that held 8-4 in April; and U-Mich sentiment is at a record-low
44.8 on Hormuz-driven gasoline costs. The Jun-18 IV hump phase-4 found now has
a name: **FOMC June 16–17, the day before Jun-18 OPEX**, with May CPI on
June 10 in front of it. Correlation gate: NBIS is uncorrelated to the four
concurrent blueprints (max 0.222) — no cluster.

## Key signals

- `regime: "TRANSITIONAL — Mixed signals, reduce position size, wait for
  clarity"`, trend PULLBACK_IN_UPTREND, breadth 29.4% bullish (1,831 vs 4,390),
  guidance verbatim: "Half position sizes. Favor defined-risk strategies."
  `[MACRO:MarketRegime_2026-06-05 UW]`
- AVGO guide-down = the AI-capex repricing event; NBIS's −12.27% was complex-wide
  (MU −12%, SNDK −12%, Nasdaq −4%) `[MACRO:AVGO_guidance_2026-06-03
  WebSearch:cnbc.com/247wallst.com/thestreet.com]`
- Rates repricing hawkish: DGS2 4.05% (+17bp vs 30d), DGS10 4.47% (+8bp), DFF
  3.62% — 2y ~43bp ABOVE funds = hike-risk pricing; strong May jobs report cited
  as fuel `[MACRO:DGS2_2026-06-04 FRED]` `[MACRO:PAYEMS_2026-05 FRED]`
- Inflation sticky-hot: CPI +3.78% YoY (Apr), core CPI +2.74%, PCE +3.77%, core
  PCE +3.29% `[MACRO:CPIAUCSL_2026-04 FRED]` `[MACRO:PCEPILFE_2026-04 FRED]`
- **FOMC Jun 16–17 sits one day before the Jun-18 OPEX cliff** (phase-3: 20.9%
  of OI; phase-4: 143.6% IV hump) — the chain is pricing exactly this
  `[MACRO:FOMC_calendar WebSearch:federalreserve.gov]`
- Sector rotation: directional money flowing OUT of Communication Services
  (−$130.0M) and Technology (−$807.6M) on the day `[MACRO:MarketRegime UW]`;
  5-day gross call-tilt persists (score 1.0) but is collapsing in magnitude
  (CommSvc $1.34bn→$0.65bn; Tech $13.1bn→$3.8bn) `[MACRO:sector_flow_persistence UW]`

## Detailed findings

### Market regime (UW)

SPY $737.55 — below 20-SMA ($746.29), above 50-SMA ($713.51), −3.01% from 90-day
high, +0.51% over 30d. Breadth: 6,221 optionable tickers, 29.4% bullish flow.
Sector rotation (directional): in → Consumer Defensive +$13.3M, Healthcare
+$12.0M; out → **Technology −$807.6M, Communication Services −$130.0M**,
Consumer Cyclical −$125.1M. (Matches phase-0.5's DuckDB sector table within
~10%.) VIX proxy: 16.70 → **21.51** over the 10 sessions to 06-05
`[MACRO:VIX_trend UW]`. SPY 10d: 3 bullish / 7 bearish days, 745.64 → 737.55,
IV rank 21.4 → 34.2 `[MACRO:SPY_trend UW]`.

### Inflation

| Series | Latest (Apr-2026) | MoM | YoY | Source |
|---|---|---|---|---|
| CPI (CPIAUCSL) | 332.407 | +0.64% | **+3.78%** | `[MACRO:CPIAUCSL_2026-04 FRED]` |
| Core CPI (CPILFESL) | 335.423 | +0.38% | +2.74% | `[MACRO:CPILFESL_2026-04 FRED]` |
| PCE (PCEPI) | 130.902 | +0.40% | +3.77% | `[MACRO:PCEPI_2026-04 FRED]` |
| Core PCE (PCEPILFE) | 129.63 | +0.24% | **+3.29%** | `[MACRO:PCEPILFE_2026-04 FRED]` |

Headline running ~3.8% on energy (April FOMC statement cited "elevated
inflation partly due to rising energy prices"; Hormuz disruption in the UMich
release) — well above target, and the next print lands Jun-10.

### Labor

PAYEMS: May 159,001k (+172k MoM), Apr +179k, Mar +214k `[MACRO:PAYEMS_2026-05
FRED]`. UNRATE 4.3% (flat 3 months) `[MACRO:UNRATE_2026-05 FRED]`. Reporters
characterized Friday's report as "stronger-than-expected … fueling concerns
that the Federal Reserve could raise interest rates later this year"
`[MACRO:jobs_2026-06-05 WebSearch:invezz.com]` — the macro leg of Friday's
growth-stock derating.

### Rates

- April 28–29 FOMC: held at **3.50–3.75%**, vote 8-4 (Miran dissent for −25bp);
  "solid economic activity but elevated inflation"
  `[MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]`
- DFF 3.62% (Jun-4); SOFR 3.62% `[MACRO:DFF_2026-06-04 FRED]`
- DGS10 4.47% (vs 4.39% 30d ago); DGS2 **4.05%** (vs 3.88%) — front-end +17bp;
  T10Y2Y +0.38 (flattening from +0.50) `[MACRO:DGS10/DGS2/T10Y2Y_2026-06-04/05 FRED]`
- USD broad index 118.88, ~flat 30d `[MACRO:DTWEXBGS_2026-05-29 FRED]`
- 2y above funds rate = market prices net *tightening* risk — discount-rate
  headwind for a stock trading at +94% above its SMA200 (phase-5).

### Activity

ISM Manufacturing **54.0** (May, +1.3pt, highest since May-2022; 5th month
expanding); ISM Services **54.5** (May, 23rd month expanding)
`[MACRO:ISM_2026-06-01/03 WebSearch:prnewswire.com]`. Activity is *strong* —
which is precisely what feeds the hike narrative.

### Consumer

U-Mich Consumer Sentiment **44.8 May final — record low**, third straight
decline, on Hormuz-driven gasoline costs `[MACRO:UMich_2026-05
WebSearch:sca.isr.umich.edu via tradingeconomics]`. June prelim due ~Jun-12,
final Jun-26. (Conference Board May print not pulled — flagged as gap; UMich
covers the consumer read for a non-consumer name.)

### Sector overlay (AI infrastructure)

- **Broadcom (Jun-3 post-close):** Q3 AI chip sales guide $16bn vs $17.2bn
  consensus; 2026 AI forecast NOT raised → AVGO −12% Jun-4, complex-wide
  derating; MU −7.7% Jun-4 then ~−12% Jun-5, SNDK −12%, ARM −4.5%, MRVL −7%
  `[MACRO:AVGO_2026-06-03 WebSearch:cnbc.com/247wallst.com]`
- Jun-5: "Nasdaq falls 4% as semiconductor slide wipes $1T from markets"
  `[MACRO:tape_2026-06-05 WebSearch:thestreet.com]`
- NBIS-specific: coverage attributes the −12.27% to "broader cooling of the
  artificial intelligence infrastructure", **no company-specific news**
  `[MACRO:NBIS_2026-06-05 WebSearch:stockinvest.us]` — confirms phase-0.5's
  "beta, not idiosyncratic" hypothesis.

### Sector rotation

- Today (directional): CommServices **−$130.0M**, Tech −$807.6M — money OUT
  `[MACRO:MarketRegime UW]`.
- 5-day persistence (gross call−put premium): CommServices INFLOW,
  persistence_score **1.0**, but decaying $1.342bn → $0.653bn (−51%); Tech
  INFLOW 1.0, $13.14bn → $3.80bn (−71%) `[MACRO:sector_flow_persistence UW]`.
  Metric note: this tool's net_flow = call_premium − put_premium (gross mix),
  not aggressor-direction — the INFLOW label and the directional outflow
  coexist; the *decay rate* is the signal.
- **Verdict: `adverse`** — directional money is leaving the sector today and
  gross enthusiasm is halving week-over-week.
- `fz` breadth cross-check (advisory, captured 2026-06-06T23:51Z, 1d
  timeframe = Friday's session): 237 adv / 266 dec, pct_green 47.1%, avg −0.92%,
  worst mover **MU −13.25%** `[MACRO:sector_breadth fz EOD]`; CommServices group
  P/E 37.43 / Fwd 30.90, Change −1.63% — richest major sector after Tech
  `[MACRO:group_valuation fz EOD]`. Corroborates the adverse read.

### Cross-name correlation

Concurrent blueprints (research/*/2026-06-05): **CRM, NOW, PATH, RKT**.

- `uw risk portfolio-correlation --symbols NBIS,CRM,NOW,PATH,RKT --lookback-days 30`:
  flags CRM/NOW 0.863 (HIGH), CRM/PATH 0.820 (HIGH), NOW/PATH 0.759 (MODERATE);
  **no NBIS pair flagged**; tool returns no full matrix and sector lookup reads
  "Unknown" `[MACRO:portfolio_correlation UW]`.
- DuckDB cross-check on local screener closes (20 sessions, 05-08→06-05,
  no gap inside window) `[MACRO:correlation DUCKDB]`:

| Pair | ρ | | Pair | ρ |
|---|---|---|---|---|
| NBIS/CRM | **0.163** | | NBIS/PATH | **0.217** |
| NBIS/NOW | **0.222** | | NBIS/RKT | **−0.074** |

(Sibling cluster CRM/NOW 0.876, CRM/PATH 0.819, NOW/PATH 0.746 — corroborates
the UW tool but is not NBIS's gate.)
- **Verdict: no cluster, no soft-watch** — all NBIS pairs ≪ 0.60.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on AI-infra (NBIS) |
|---|---|---|---|---|
| AVGO AI guide | $16bn vs $17.2bn est | 2026-06-03 | WebSearch:cnbc.com | **headwind (the catalyst)** |
| Market regime | TRANSITIONAL, 29.4% bullish breadth | 2026-06-05 | UW | headwind |
| VIX | 16.7 → 21.51 (10 sess.) | 2026-06-05 | UW | headwind |
| CPI YoY | +3.78% | 2026-05-12 (Apr data) | FRED | headwind |
| Core PCE YoY | +3.29% | 2026-05 (Apr data) | FRED | headwind |
| NFP MoM | +172k, U3 4.3% | 2026-06-05 | FRED | headwind (fuels hike pricing) |
| DGS2 | 4.05% (+17bp/30d) | 2026-06-04 | FRED | headwind (long-duration multiple) |
| FOMC stance | hold 3.50–3.75%, 8-4 | 2026-04-29 | WebSearch:federalreserve.gov | neutral→headwind |
| ISM Mfg / Svcs | 54.0 / 54.5 | 2026-06-01 / 06-03 | WebSearch:prnewswire.com | neutral (strong activity, hawkish read) |
| U-Mich sentiment | 44.8 record low | 2026-05 final | WebSearch | neutral (not a consumer name) |
| USD broad | 118.88 ~flat | 2026-05-29 | FRED | neutral |
| Sector rotation | CommSvc −$130M day; gross tilt −51%/5d | 2026-06-05 | UW | **headwind (adverse)** |

## Catalyst calendar (next 30d)

Front-expiry expected move: the screener `implied_move_perc` (0.41%,
`[CTX:implied_move_pct]`) is flagged SUSPECT in phase-0.5; using IV-derived
ranges instead: IV30d 111.7% → **±7.0%/day, ±15.7%/week priced**; Jun-12 expiry
avg IV 132.1% (phase-4) → the chain prices roughly a ±13–16% move by Jun-12.
Each binary below is read against that.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| 2026-06-10 | May CPI (8:30 ET) | hot print → hike pricing ↑ → growth derate | inside ±13–16% wk unless extreme |
| 2026-06-12 | weekly OPEX (P/C OI 3.0; max-pain 235) | pin/gravity above spot | inside |
| 2026-06-16/17 | **FOMC** (+ SEP/dots) | the Jun-18 IV hump's event; hawkish = continuation | can exceed weekly range if surprise |
| 2026-06-18 | monthly OPEX — 20.9% of total OI | positioning reset; vol roll-off after | structural |
| 2026-06-26 | U-Mich June final; Jun-26 expiry (max-pain 230) | minor | inside |
| ongoing | AI-capex newsflow post-AVGO (peer guides, mega-cap capex) | sentiment driver both ways | episodic |
| 2026-08-06 | NBIS earnings (outside 30d) | the next idiosyncratic binary | — |

## Tool / source errors

- `uw risk portfolio-correlation` returned only threshold-flagged pairs (no
  full matrix; `sector_breakdown: {"Unknown": 5}`) — NBIS pairwise values
  computed from local screener closes instead (DuckDB, tagged above). Tool
  output that did return is quoted verbatim.
- Conference Board Consumer Confidence (May) not retrieved — U-Mich substituted;
  non-material for a non-consumer name.
- `fz` snapshots are live-captured (2026-06-06T23:51Z), not as-of-frozen;
  1d-change fields reflect the 06-05 session. Advisory only.

## Verdict for downstream phases

- **Net macro bias for NBIS:** **headwind** (sector-catalyst-driven derating +
  hawkish rates repricing into a record-multiple AI complex)
- **Conviction:** 4/5
- **Top 2 datapoints phase-9 must cite:**
  1. AVGO Jun-3 AI guide-down ($16bn vs $17.2bn) → complex-wide derate; NBIS's
     −12.27% was beta, with **no company-specific news**.
  2. DGS2 4.05% vs DFF 3.62% (+17bp/30d) on a +172k NFP — hike-risk pricing
     into the Jun-16/17 FOMC.
- **Top 2 catalysts for the phase-9 calendar:** Jun-10 May-CPI; Jun-16/17 FOMC
  (against the Jun-18 OPEX cliff holding 20.9% of OI).
- **Sector-rotation verdict:** **adverse** — persistence_score 1.0 on a gross
  call-tilt that is *decaying* −51%/5d while directional money exits
  (−$130M day). Phase-9 sizing gate input.
- **Correlation verdict:** **no cluster, no soft-watch** — NBIS max pairwise
  ρ = 0.222 (NOW); 4 concurrent blueprints named above. (Sibling CRM/NOW/PATH
  cluster ≥0.75 exists but excludes NBIS.)

Sources: [CNBC](https://www.cnbc.com/2026/06/04/chipmaker-equities-micron-marvell-broadcom-intel.html), [24/7 Wall St](https://247wallst.com/investing/2026/06/04/micron-drops-7-as-broadcoms-disappointing-ai-outlook-triggers-a-semiconductor-selloff/), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-05-2026), [WolfStreet](https://wolfstreet.com/2026/06/05/semiconductor-stocks-roll-over-micron-broadcom-tank-20-in-2-days-drag-rest-of-market-along/), [Invezz](https://invezz.com/ng/news/2026/06/05/micron-sandisk-stocks-slide-as-traders-exit-high-flying-ai-plays/), [StockInvest](https://stockinvest.us/stock/NBIS), [FederalReserve.gov](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm), [PRNewswire ISM Mfg](https://www.prnewswire.com/news-releases/manufacturing-pmi-at-54-may-2026-ism-manufacturing-pmi-report-302786165.html), [PRNewswire ISM Svcs](https://www.prnewswire.com/news-releases/services-pmi-at-54-5-may-2026-ism-services-pmi-report-302789082.html), [BLS CPI schedule](https://www.bls.gov/schedule/news_release/cpi.htm), [UMich Surveys](https://www.sca.isr.umich.edu/)
