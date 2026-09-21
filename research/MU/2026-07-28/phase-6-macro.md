# Phase 6 — Macro Overlay

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T22:20:00-04:00
**Upstream phases cited:** `phase-0.5-context.md` (sector epicenter, implied move), `phase-3-positioning.md` (7/31 OI cliff), `phase-4-structure.md` (IV humps), `phase-5-historical.md` (VRP)

## Summary

**The catalyst that every prior phase flagged as unknown is now identified, and it is
company/industry-specific, not macro: CXMT.** MU fell 8.85% on (1) **Chinese DRAM competitor
CXMT's capacity expansion** — ~200k wafers/month today, targeting **~300k by end-2026** and up
to **600k** from new Shanghai/Hefei fabs, aiming at **17% of global DRAM supply by 2028** — with
reports that **Apple is testing CXMT memory for China-sold devices**; and (2) a broader
reassessment of AI-capex durability, with **inventory normalisation across enterprise/cloud
running faster than expected**, historically the marker of a **DRAM pricing-cycle peak**. This
is precisely why `phase-0.5-context.md` found SPY **+0.24%** and NVDA **+0.25%** while
SNDK **-14.25%** and MU **-8.85%** — **the market had a good day and memory was liquidated.**
`fz breadth` confirms it independently: **70.97% of the S&P 500 closed green (357 advancers vs
145 decliners, median +1.39%) and the single worst performer in the index was SNDK at -14.25%.**

**The bear case is about 2027–28 and the present is still exceptional** — a tension phase-8b must
resolve. The DRAM market is currently in **shortage, not oversupply**: contract prices rose
**~93–98% QoQ in Q1 2026**, HBM commands a **5–8× DDR5 ASP premium** and remains supply-constrained,
CXMT's HBM3E mass production is only targeted for **2027**, and Micron's fiscal Q3 2026 non-GAAP
gross margin was **84.9%**. Today's tape repriced a *future* supply threat against a *present*
that is still extraordinary.

Macro proper is a mild tailwind and is **not** what moved MU. The UW regime is
**`TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`** with `trend = CHOPPY`,
SPY (740.86) **below both its 20-DMA (746.65) and 50-DMA (744.86)**, and options-flow breadth at
only **36.9% bullish**. Inflation is cooling (**June CPI 3.5% YoY, headline -0.4% MoM — the
largest monthly drop since April 2020; core 2.6%**) and labour is softening (**June payrolls
+57k vs 115k consensus; unemployment 4.2%**). **The dominant dated risk is tomorrow: the FOMC
decision on 2026-07-29 at 2:00 PM ET** (target 3.50–3.75%, **no SEP/dot plot**, Chair Kevin
Warsh press conference 2:30 PM) — **the exact event this skill's 2026-06-25 MU run named as its
macro invalidation trigger.**

## Key signals

- **Sector catalyst = CXMT DRAM expansion + Apple qualification + faster inventory
  normalisation.** [MACRO:CXMT_2026-07-28 WebSearch:tomshardware.com, fxleaders.com]
- **Counter-fact: DRAM is in shortage — Q1 2026 contract prices +93–98% QoQ; MU FQ3-26 non-GAAP
  GM 84.9%; CXMT HBM3E only in 2027.** [MACRO:DRAM_cycle_2026 WebSearch:semianalysis.com]
- **Regime `TRANSITIONAL`/`CHOPPY`; guidance: "Half position sizes. Favor defined-risk
  strategies."** SPY below 20- and 50-DMA; flow breadth **36.9% bullish**.
  [MACRO:MarketRegime_2026-07-28 UW]
- **FOMC decision 2026-07-29 14:00 ET — no dot plot.** [MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]
- **Technology net flow is +$34.2M on $14.19B gross (+0.24%) — 7th of 11 sectors — after a
  99% five-session collapse** ($3.235B → $0.034B). [MACRO:sector_flow_persistence UW]
- **S&P 500 price breadth 70.97% green, worst mover SNDK -14.25%.**
  [MACRO:sector_breadth fz EOD]
- **MU/SNDK correlation 0.904, MU/AMAT 0.865 — HIGH cluster.** [MACRO:portfolio_correlation UW]

## Detailed findings

### Market regime (UW: SPY + VIX + breadth)

`uw risk market-regime --date 2026-07-28`:

| field | value |
|---|---|
| **`regime`** | **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"** |
| `trend` | **`CHOPPY`** |
| **`trading_guidance`** | **"Half position sizes. Favor defined-risk strategies. Iron condors in range."** |
| `spy.current` | 740.86 |
| `spy.sma_20` / `above_20sma` | 746.65 / **false** |
| `spy.sma_50` / `above_50sma` | 744.86 / **false** |
| `spy.change_30d_pct` | +1.63% |
| `spy.pct_from_90d_high` | -2.57% |
| `market_breadth.bullish_pct` | **36.9%** |
| `market_breadth` counts | 2,320 bullish / 3,959 bearish of 6,279 optionable |

**SPY closed green (+0.24%) yet sits below both its 20- and 50-day moving averages**, only
+1.63% over 30 days and -2.57% from its 90-day high. **Options-flow breadth is decidedly weak at
36.9% bullish** — 3,959 tickers with bearish flow against 2,320 bullish.

**A notable divergence worth carrying forward:** UW's *flow* breadth says 36.9% bullish, while
`fz`'s *price* breadth says **70.97% of the S&P 500 closed green**. Price was broadly up; option
flow was broadly defensive. That is a classic late-stage / distribution signature and is
consistent with the regime label `TRANSITIONAL`.

**The tool's own guidance — "Half position sizes. Favor defined-risk strategies." — is a direct
input to phase-9 sizing and should be honoured.**

`sector_rotation` from the same call: **in** — Technology +$143,583,470, Communication Services
+$59,588,662, Healthcare +$13,533,377; **out** — Consumer Cyclical -$30,760,165, Industrials
-$28,464,792, Basic Materials -$11,916,641. *(These reconcile exactly with the independent
DuckDB sector aggregation in `phase-0.5-context.md`.)*

### Inflation

**FRED was not available for this run (see Tool / source errors) — all values via WebSearch,
release dates verified.**

| Series | Latest print | Period | Release date | vs consensus |
|---|---:|---|---|---|
| **CPI headline YoY** | **3.5%** | June 2026 | **2026-07-14** | **below 3.8% consensus** |
| **CPI headline MoM** | **-0.4%** | June 2026 | 2026-07-14 | **largest monthly decline since April 2020** |
| **Core CPI YoY** | **2.6%** | June 2026 | 2026-07-14 | softer than forecast, unchanged MoM |
| July 2026 CPI | *not yet released* | July 2026 | **due 2026-08-12** | — |

`[MACRO:CPI_2026-06 WebSearch:bls.gov]` — **A genuinely disinflationary print.** A -0.4% monthly
headline decline is a large, disorderly-looking move that nonetheless pulls YoY to 3.5% against
a 3.8% expectation, with core at 2.6%. **This is a tailwind for long-duration/growth equities
generally** and removes a hawkish justification from tomorrow's FOMC.

Core PCE (the Fed's official target measure) could not be sourced to a verified recent print
without FRED; **recorded as unavailable rather than estimated.**

### Labor

| Series | Latest print | Period | Release date |
|---|---:|---|---|
| **Nonfarm payrolls** | **+57,000** | June 2026 | **2026-07-02** |
| — vs consensus | 115,000 | | **large miss** |
| — prior (revised down) | +129,000 | May 2026 | |
| **Unemployment rate** | **4.2%** | June 2026 | 2026-07-02 |
| Labor-force participation | **61.5%** (-0.3pp) | June 2026 | 2026-07-02 |

`[MACRO:PAYEMS_2026-06 WebSearch:bls.gov, cnbc.com]` — **Labour is cooling meaningfully.** +57k
against 115k expected, with May revised down to +129k. The unemployment rate *fell* to 4.2% only
because participation dropped 0.3pp to 61.5% — a low-quality decline. **Dovish-leaning.**

*Caveat recorded honestly:* search results also surfaced a "+73,000 payrolls, unemployment 4.2%"
figure attributed to a July jobs report. **The July 2026 employment report is not due until
~2026-08-07 (after this run's as-of date), so that figure could not be from a released July 2026
print** — it is most likely a same-titled article from a prior year. **It is therefore NOT used
here.** The June 2026 report (released 2026-07-02) is the latest verified print.

### Rates (FOMC)

| item | value |
|---|---|
| **Next decision** | **Wednesday 2026-07-29, 2:00 PM ET** (press conference 2:30 PM) |
| Meeting dates | Tue 2026-07-28 – Wed 2026-07-29 (two-day) |
| **Current target range** | **3.50% – 3.75%** |
| Prior action | **Held** at the June 16–17, 2026 meeting |
| June guidance | inflation "remained elevated relative to its 2% goal" |
| **SEP / dot plot** | **NONE** — July is one of the four meetings without a SEP |
| Chair | Kevin Warsh |

`[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov, cmelitegroup.com]`

**This is the dominant dated risk in the entire run, and it lands tomorrow.** Three reasons it
matters more than usual for MU:

1. **It is the literal invalidation trigger from this skill's own prior MU blueprint.**
   `research/MU/2026-06-25/decision.json` named *"hawkish FOMC ~July 28-29 flips regime
   risk-off"* as its macro invalidation. That date has arrived.
2. **No dot plot** means the market must read the statement and Warsh's press conference alone —
   **a wider distribution of interpretations, hence higher realised vol into 2:30 PM.**
3. **The setup argues dovish.** June CPI 3.5%/core 2.6% (both soft) and payrolls +57k (a large
   miss) give the Fed room. **A dovish outcome is the single most plausible trigger for the
   vanna squeeze phase-4 identified** — IV collapse post-event → dealers short puts buy stock.
   Conversely a hawkish surprise into a `FULLY_NEGATIVE` gamma regime is the tail phase-3's
   penny-put buyers are paying for.

10y/2y/2s10s, DFF and SOFR levels could not be pulled without FRED and are **recorded as
unavailable rather than guessed.**

### Activity

| Series | Latest print | Period | Note |
|---|---:|---|---|
| **S&P Global US Manufacturing PMI** | **53.8** | July 2026 | from 53.9 in June; **missed 54.3 consensus** |

`[MACRO:PMI_2026-07 WebSearch:tradingeconomics.com]` — **Still comfortably expansionary and near
four-year highs**, but decelerating: production growth slowest since March, new orders weakest in
four months. **Mildly positive for semis end-demand; not a driver of today's move.** ISM
Manufacturing/Services official prints and the consumer surveys (U-Mich, Conference Board) could
not be sourced to verified recent releases within this run's search budget — **recorded as
unavailable, not estimated** (see Tool / source errors).

### Sector overlay — the actual catalyst

**The bear case (what moved the stock today):**

- **CXMT capacity.** ~**200,000 wafers/month** currently, targeting ~**300,000 wpm by end-2026**;
  new Shanghai and Hefei fabs could take total output toward **600,000 wpm**. CXMT targets
  **17% of global DRAM supply by 2028**, which would make China the **world's second-largest DRAM
  producer**. `[MACRO:CXMT_capacity WebSearch:tomshardware.com, semianalysis.com]`
- **Customer qualification risk.** Reports that **Apple is testing CXMT memory products for
  devices sold in China** — the first credible sign of tier-1 qualification, which is what turns
  capacity into share. `[MACRO:CXMT_Apple_2026-07-28 WebSearch:ts2.tech]`
- **Cycle-peak signalling.** *"Recent industry data suggests a faster-than-anticipated
  normalization of inventory levels across enterprise and cloud service providers, which has
  historically signaled a peak in the current DRAM pricing cycle."*
  `[MACRO:DRAM_inventory_2026-07 WebSearch:fool.com, benzinga.com]`
- **Sympathy damage confirms the read:** SNDK -14.25%, MU -8.85%, STX -8.53%, WDC -6.91%
  (memory/storage) and AMAT -7.82%, LRCX -7.54%, KLAC -6.18% (memory capex), versus
  **NVDA +0.25%, AVGO -0.60%, SPY +0.24%.**

**The bull counter-case (what the tape ignored today):**

- **The market is in SHORTAGE, not oversupply.** Global DRAM supply is failing to meet demand and
  **traditional DRAM contract prices rose ~93–98% QoQ in Q1 2026.**
  `[MACRO:DRAM_pricing_Q1-2026 WebSearch:semianalysis.com, useluminix.com]`
- **HBM economics remain exceptional** — a **5–8× ASP premium** over equivalent DDR5, with supply
  still constrained.
- **CXMT is not yet a competitor where it matters.** Its **HBM3E mass production target is 2027**,
  with only ~30,000 wspm allocated to HBM by end-2026 (55,000 by end-2027). Reports even suggest
  **CXMT's 64GB server DDR5 is priced ABOVE Samsung's** amid surging demand — i.e. it is
  currently absorbing shortage, not undercutting price.
- **Micron's own economics are extraordinary**: ~**24% global DRAM share** (behind Samsung 36%,
  SK Hynix 29%) and **fiscal Q3 2026 non-GAAP gross margin of 84.9%.**
- Per `phase-0-intake.md`'s `fz` snapshot: Market Cap **$926.70B** on **Sales $90.27B** and
  **Income $50.47B** — a trailing P/E near **18.4** against the **Technology sector's P/E of
  34.28 / forward 25.07** (`fz groups`). **MU is not priced as a bubble.**

**Net read: today priced a 2027–2028 competitive/supply threat into a 2026 that is still in
acute shortage with 84.9% gross margins.** That does not make the selloff wrong — cyclical
stocks top when the *second derivative* turns, not when earnings do — but it does mean **the
move is expectations-driven, not results-driven**, and is therefore reversible on any datapoint
that pushes the CXMT/oversupply timeline out. **This is the core of the phase-8b debate.**

### Sector rotation

`uw options-flow sector-flow --date 2026-07-28` (net_flow = call premium − put premium):

| sector | **net_flow** | call premium | put premium |
|---|---:|---:|---:|
| Healthcare | **+$206,036,868** | $351.3M | $145.3M |
| Communication Services | +$184,070,793 | $817.0M | $632.9M |
| Financial Services | +$167,011,253 | $445.9M | $278.9M |
| Consumer Defensive | +$112,453,336 | $173.6M | $61.2M |
| Industrials | +$69,112,103 | $800.9M | $731.8M |
| Energy | +$48,093,124 | $87.4M | $39.3M |
| **Technology** | **+$34,176,399** | **$7,110,424,253** | **$7,076,247,854** |
| Basic Materials | +$7,701,493 | $64.8M | $57.1M |
| Real Estate | +$2,737,815 | $23.2M | $20.5M |
| Utilities | -$11,973,379 | $92.1M | $104.0M |
| Consumer Cyclical | **-$250,032,481** | $993.9M | $1,243.9M |

**Technology carries $14.19B of gross premium — half the entire market — and nets to just
+$34.2M (+0.24%).** It ranks **7th of 11** on net flow despite being ~9× larger than any other
sector. Healthcare nets **six times more** on 1/28th the gross. **In relative-conviction terms
capital is rotating away from Technology**, exactly mirroring MU's own +1.0% net tilt on $2.83B
(phase-1).

`uw options-flow sector-flow-persistence --days 5` (`dates_covered` 2026-07-22 → 07-28):

| sector | `trend` | `persistence_score` | net flow by day (07-22 → 07-28) |
|---|---|---:|---|
| **Technology** | **INFLOW** | **1.0** | **3,234,855,760 → 767,224,280 → 966,664,074 → 366,844,565 → 34,176,399** |
| Healthcare | INFLOW | 1.0 | 456.7M → 30.7M → 132.5M → 85.4M → 206.0M |
| Financial Services | INFLOW | 1.0 | 184.5M → 136.2M → 145.1M → 149.8M → 167.0M |
| Consumer Defensive | INFLOW | 1.0 | 36.1M → 133.6M → 35.8M → 53.4M → 112.5M |
| Energy | INFLOW | 1.0 | 108.1M → 104.3M → 78.0M → 38.9M → 48.1M |
| Real Estate | INFLOW | 1.0 | 5.5M → 9.2M → 23.5M → 16.4M → 2.7M |
| Basic Materials | INFLOW | 1.0 | 35.7M → 15.5M → 18.3M → 9.0M → 7.7M |
| **Consumer Cyclical** | **OUTFLOW** | 0.8 | 154.7M → **-3,043.2M** → -672.7M → -386.1M → -250.0M |
| Industrials | OUTFLOW | 0.8 | -68.7M → -125.4M → -194.0M → -47.0M → +69.1M |
| Communication Services | INFLOW | 0.8 | 501.2M → -784.0M → 75.4M → 348.3M → 184.1M |
| Utilities | INFLOW | 0.8 | 38.3M → 9.8M → 3.6M → 15.0M → -12.0M |

**Technology's `persistence_score` of 1.0 with `trend = INFLOW` is technically bullish and
substantively hollow: the inflow has collapsed 99% in five sessions**, from $3.235B on 7/22 to
$34.2M today. The *sign* never flipped (hence perfect persistence), but the *magnitude* has
gone to zero. **This is a rotation dying, not a rotation reversing — and it is one bad session
away from flipping negative.**

**`fz` breadth cross-check (advisory)** — `fz breadth --group sector --agent`, captured
2026-07-29T01:42:17Z (post-close):

| field | value |
|---|---:|
| `total` / `advancers` / `decliners` | 503 / **357** / 145 |
| **`pct_green`** | **70.97%** |
| `avg_change` / `median_change` | +1.06% / **+1.39%** |
| `top_mover` | IQV **+13.94%** |
| **`worst_mover`** | **SNDK -14.25%** |

`[MACRO:sector_breadth fz EOD]` — **This is the cleanest single corroboration in the run.**
71% of the S&P 500 rose with a median gain of +1.39%, and **the worst-performing stock in the
entire index was a memory name.** The selloff was surgical.

`fz groups --by sector --view valuation` (Technology row) `[MACRO:group_valuation fz EOD]`:
`P/E` **34.28**, `Fwd P/E` **25.07**, `PEG` **0.89**, `EPS next 5Y` +38.32%, `Change` **-1.50%**,
Market Cap $31,003.98B. **Technology was the only major sector down on price breadth terms while
still showing net options inflow** — divergence, and MU sits far below the sector multiple.

**Rotation verdict for the emerging (bearish/defensive) MU thesis: NEUTRAL.** Headline
Technology flow is still net-*inflow* with perfect sign persistence (which argues *against*
maximum bearishness), but the 99% magnitude collapse and the outright liquidation of MU's own
memory sub-complex argue *for* it. **For a bullish MU thesis the same data is clearly ADVERSE.**

### Cross-name correlation

**No concurrent blueprints:** `ls research/*/2026-07-28/` returns **only
`research/MU/2026-07-28/`. MU is the sole blueprint for this date, so the correlation sizing
gate does not bind.** The tool was nonetheless run against MU's peer complex for context:

`uw risk portfolio-correlation --symbols MU,SNDK,WDC,STX,NVDA,AMAT,SPY --lookback-days 30`
(`tickers_analyzed = 7`):

| pair | correlation | warning |
|---|---:|---|
| WDC / STX | 0.950 | HIGH |
| **MU / SNDK** | **0.904** | **HIGH** |
| **MU / AMAT** | **0.865** | **HIGH** |
| SNDK / AMAT | 0.850 | HIGH |
| WDC / AMAT | 0.746 | MODERATE |
| SNDK / STX | 0.736 | MODERATE |
| **MU / WDC** | **0.731** | MODERATE |
| SNDK / WDC | 0.724 | MODERATE |
| **MU / STX** | **0.709** | MODERATE |
| STX / AMAT | 0.704 | MODERATE |

`warnings`: `["CONCENTRATION: 100% of tickers in Unknown", "HIGH CORRELATION: Some pairs move
nearly in lockstep — not truly diversified"]`

**Every MU pair in the memory/semicap complex is ≥0.709, and MU/SNDK at 0.904 is effectively the
same bet.** Neither MU/NVDA nor MU/SPY appeared in `high_correlations`, meaning both fall below
the tool's reporting threshold — **MU is tightly coupled to memory and loosely coupled to the
index**, exactly as today's price action showed.

**Practical consequence:** although no concurrent blueprint triggers the gate today, **any
future position in SNDK, WDC, STX or AMAT alongside MU is a single concentrated memory bet, not
diversification.** Phase-9 should record this as a standing constraint.

*(The `CONCENTRATION: 100% of tickers in Unknown` warning reflects the known-broken `sector`
field in this tool — the **correlation coefficients themselves are valid**; only the sector
label is degraded.)*

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Technology / memory |
|---|---|---|---|---|
| **CXMT capacity expansion** | 200k → 300k wpm (2026); 17% share target 2028 | 2026-07-28 | WebSearch:tomshardware.com | **HEADWIND (structural, 2027–28)** |
| **Apple testing CXMT memory** | qualification for China devices | 2026-07-28 | WebSearch:ts2.tech | **HEADWIND (severe if confirmed)** |
| **Cloud/enterprise inventory normalisation** | faster than expected | 2026-07 | WebSearch:fool.com | **HEADWIND (cycle-peak signal)** |
| **DRAM contract pricing** | **+93–98% QoQ** | Q1 2026 | WebSearch:semianalysis.com | **TAILWIND (strong)** |
| **HBM ASP premium** | 5–8× DDR5, supply-constrained | 2026 | WebSearch:semianalysis.com | **TAILWIND** |
| **MU non-GAAP gross margin** | **84.9%** | FQ3 2026 | WebSearch | **TAILWIND** |
| CXMT HBM3E timing | mass production **2027** | 2026 | WebSearch:techsoda | TAILWIND (near-term reprieve) |
| **CPI headline YoY** | **3.5%** (-0.4% MoM) | 2026-07-14 (Jun) | WebSearch:bls.gov | **TAILWIND** |
| **Core CPI YoY** | **2.6%** | 2026-07-14 (Jun) | WebSearch:bls.gov | **TAILWIND** |
| **Nonfarm payrolls** | **+57k** (vs 115k est) | 2026-07-02 (Jun) | WebSearch:cnbc.com | TAILWIND (dovish) / mild growth headwind |
| Unemployment rate | 4.2% (participation -0.3pp) | 2026-07-02 (Jun) | WebSearch:bls.gov | NEUTRAL |
| S&P Global Mfg PMI | 53.8 (from 53.9) | 2026-07 | WebSearch:tradingeconomics.com | NEUTRAL / mild tailwind |
| **Fed funds target** | **3.50–3.75%**, held in June | 2026-06-17 | WebSearch:federalreserve.gov | NEUTRAL pending 7/29 |
| **Market regime** | `TRANSITIONAL` / `CHOPPY`, 36.9% bullish breadth | 2026-07-28 | UW | **HEADWIND** |
| SPY vs 20/50-DMA | 740.86 below 746.65 / 744.86 | 2026-07-28 | UW | HEADWIND |
| **S&P price breadth** | **70.97% green**, worst = SNDK -14.25% | 2026-07-28 | fz EOD | **NEUTRAL for market, HEADWIND for memory** |
| **Technology net flow** | +$34.2M (+0.24%), **-99% in 5 sessions** | 2026-07-28 | UW | **HEADWIND** |
| Technology valuation | P/E 34.28, Fwd 25.07, PEG 0.89 | 2026-07-28 | fz EOD | NEUTRAL (MU cheap vs sector) |

## Catalyst calendar (next 30d)

**Front-expiry expected (implied) move: ±7.90% / ±$64.79** (`implied_move` = 64.7944,
`implied_move_perc` = 0.07904) [CTX:implied_move]. **Phase-9 must size structures to this priced
range** — every binary below is read against it.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-07-29 14:00 ET** | **FOMC decision + Warsh presser 14:30. No SEP/dot plot.** | **Dominant near-term risk.** Dovish → IV collapse → **vanna squeeze** (phase-4) → mechanical dealer buying. Hawkish → risk-off into `FULLY_NEGATIVE` gamma → amplified downside. | **Plausibly INSIDE ±7.9% for MU** (macro, not memory-specific), but it is the **binary that unlocks the vol path** |
| 2026-07-29 | 1-DTE expiry (3.43% of OI); the 815–835 call ladder (phase-1) | Gamma/pin churn around 820 | inside |
| **2026-07-31** | **Weekly expiry holding 18.38% of ALL OI, put/call OI 2.592, max pain 930** (phase-3/4) | Largest OI cliff in the chain; 291,008 puts expire | **Structural — first post-FOMC settlement** |
| ~2026-08-07 | July employment report (BLS) | Dovish/hawkish rate impulse | inside |
| **2026-08-07** | Expiry of the **55P (+24,412 contracts)** crash-tail build; **avg_iv hump 1.3592** (phase-4) | Tail hedges expire; unexplained IV bump | **flagged — no known catalyst** |
| **2026-08-12** | **July CPI release, 08:30 ET** | Confirms/denies the June disinflation | inside |
| 2026-08-14 | `avg_iv` hump 1.2554 (phase-4) | unexplained | **flagged — no known catalyst** |
| **2026-08-21** | **Monthly OPEX — 13.91% of OI, max pain 940, put/call 1.656** | Second-largest cliff | structural |
| ~2026-09-22 | **MU earnings** (`next_earnings_date`, UW) — **unverified, must be confirmed by 7b/7c** | The event that adjudicates the CXMT/cycle debate | **exceeds ±7.9%** on history |

**Two calendar notes for phase-9:**
- **The 8/07 and 8/14 IV humps (1.3592, 1.2554) have no identified catalyst.** They are not
  earnings, not CPI, not FOMC. Either an undisclosed industry event (memory pricing data
  releases, a conference) or residual structure from the tail-hedge build. **Recorded as an
  open question, not explained away.**
- **The 2026-10-16 IV hump (1.2188) is consistent with a ~9/22 earnings date** — the first
  monthly expiry that captures it. This is the second independent corroboration (phase-3's
  Sep-18 OI concentration was the first).

## Tool / source errors

1. **FRED skipped — no `FRED_API_KEY`** (neither env var nor repo `.env`; verified by
   `set -a; . ./.env; set +a; echo $FRED_API_KEY` → empty). Public CSV endpoint is blocked at
   the CDN. To enable automated rate / inflation / labor pulls, register a free key at
   https://fred.stlouisfed.org/docs/api/api_key.html and put it in `~/.zshrc` or the repo-root
   `.env`. **All macro series in this phase therefore come from WebSearch with verified release
   dates**, per Priority-3 fallback.
   **Consequently unavailable and NOT estimated:** `DGS10`, `DGS2`, `T10Y2Y` (2s10s sign),
   `DFF`, `SOFR`, `DTWEXBGS`, `PCEPI`/`PCEPILFE` (core PCE).
2. **ISM Manufacturing / ISM Services official prints and U-Mich / Conference Board consumer
   surveys** could not be sourced to verified recent releases within this run's search budget.
   **Recorded as unavailable rather than estimated.** The S&P Global Manufacturing PMI (53.8,
   July 2026) is reported in their place and labelled as such.
3. `uw options-flow sector-flow` row fields are **`total_premium_call` / `total_premium_put` /
   `net_flow`** — a first read using `.call_premium` / `.put_premium` returned `null`
   (see DATA NOTE).
4. `uw risk portfolio-correlation` emits `CONCENTRATION: 100% of tickers in Unknown` — the
   **known-broken `sector` field**. Coefficients are valid; the sector label is not.

## DATA NOTE / CORRECTION

1. **`sector-flow` field names:** first read used `.call_premium` / `.put_premium` / `.net_premium`
   and returned `null` for every sector. Correct paths are **`.total_premium_call`,
   `.total_premium_put`, `.net_flow`**. The sector table traces to those. No null was
   transcribed as a number.
2. **July payrolls figure rejected.** A "+73,000 payrolls" figure surfaced in search but the
   July 2026 employment report is not due until ~2026-08-07, **after** this run's as-of date.
   It is excluded; **June 2026 (+57k, released 2026-07-02) is used as the latest verified
   print.** This is exactly the "WebSearch results may be from older articles — always confirm
   release date" pitfall.
3. **Two distinct "Technology net flow" numbers appear and are not in conflict:**
   `market-regime.sector_rotation` reports **+$143,583,470** while `sector-flow` reports
   **+$34,176,399**. They are different metrics — the former matches the
   bullish−bearish premium aggregation reproduced in `phase-0.5-context.md` (+$143.6M via
   DuckDB), the latter is call−put premium. **Both are quoted with their source; neither is
   reconciled away.**
4. `fz breadth` `captured_at` is **2026-07-29T01:42:17Z** — i.e. after the 2026-07-28 US close.
   It is an EOD snapshot of the 7/28 session, correctly tagged `fz EOD`.

## Verdict for downstream phases

- **Net macro bias for MU: HEADWIND — but the headwind is INDUSTRY, not MACRO.** Macro proper
  (CPI 3.5%/core 2.6% cooling, payrolls +57k, PMI 53.8) is **neutral-to-dovish and mildly
  supportive** of long-duration equities. The damage is entirely sector-specific: **CXMT
  capacity + Apple qualification + faster inventory normalisation**, layered on a
  `TRANSITIONAL`/`CHOPPY` market whose own guidance is *"half position sizes."*
- **Conviction: 4 / 5.** The catalyst is identified, dated, corroborated across multiple
  independent outlets, and **mechanically consistent with the cross-sectional evidence**
  (SNDK the worst S&P stock; NVDA green; 71% of the index green). Held below 5 because the
  bear case is a 2027–28 forecast, the bull counter-facts (shortage, +93–98% QoQ pricing, 84.9%
  GM) are strong and current, and FRED-sourced rate data is missing.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. **`[MACRO:CXMT_2026-07-28 WebSearch]` — CXMT scaling 200k→300k wpm toward 17% of global
     DRAM by 2028, with Apple reportedly qualifying its memory** — the identified cause of the
     -8.85%, and a **structural** (not cyclical) re-rating risk. **Counterweight that must be
     cited alongside it: DRAM contract prices +93–98% QoQ in Q1 2026 and MU FQ3-26 non-GAAP
     gross margin 84.9% — CXMT's HBM3E is a 2027 event.**
  2. **`[MACRO:MarketRegime_2026-07-28 UW]` — `TRANSITIONAL`/`CHOPPY`, SPY below its 20- and
     50-DMA, flow breadth 36.9% bullish, with explicit tool guidance "Half position sizes.
     Favor defined-risk strategies."** This is a direct sizing constraint.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-07-29 14:00 ET — FOMC decision, no dot plot, Warsh presser 14:30.** Tomorrow. The
     binary that determines whether phase-4's vanna squeeze fires (dovish → IV collapse →
     mechanical dealer buying) or the `FULLY_NEGATIVE` gamma regime amplifies another leg down.
     **It is also the exact macro invalidation named by the prior 2026-06-25 MU blueprint.**
  2. **2026-07-31 — the weekly expiry holding 18.38% of all MU open interest** (291,008 puts vs
     112,250 calls, max pain 930), the first settlement after the FOMC. Secondary:
     **2026-08-12 July CPI** and **2026-08-21 monthly OPEX** (13.91% of OI).
- **Sector-rotation verdict: NEUTRAL** (for the emerging bearish/defensive thesis;
  **ADVERSE for any bullish thesis**). `trend = INFLOW`, **`persistence_score = 1.0`** for
  Technology — but net flow **collapsed 99% in five sessions** ($3.235B → $34.2M) and MU's own
  memory sub-complex was the worst-performing group on the tape. **Sign says inflow; magnitude
  says exhaustion.**
- **Correlation verdict: NO CONCURRENT POSITIONS — the gate does not bind.** MU is the only
  blueprint under `research/*/2026-07-28/`. **Context flagged for future runs: MU sits in a HIGH
  cluster — MU/SNDK 0.904, MU/AMAT 0.865, MU/WDC 0.731, MU/STX 0.709 (all ≥0.70).** Any
  simultaneous position in those names is the same bet; MU/NVDA and MU/SPY did not clear the
  tool's reporting threshold, confirming MU is coupled to *memory*, not to the index.
