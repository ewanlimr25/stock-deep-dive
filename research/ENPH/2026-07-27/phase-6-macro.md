# Phase 6 — Macro Overlay

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T21:25:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-4-structure.md`, `phase-5-historical.md`

## Summary

**The macro is a headwind, the sector is a catastrophe, and there are two binaries
in the next 48 hours.** `uw risk market-regime` returns
**`"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"`**,
`trend = "CHOPPY"`, with `bullish_pct = 35.2%` of 6,279 optionable tickers and SPY
**below both its 20- and 50-day SMAs**. The tool's own `trading_guidance` is
*"Half position sizes. Favor defined-risk strategies."* — a direct sizing input
for phase-9.

Rates are moving **against** a residential-solar name. `DGS10` rose **+28bp in a
month** (4.41% → 4.69%) and `DGS2` +22bp, while the June SEP dot plot lifted the
median year-end 2026 rate to **3.8% from 3.4% in March**, with **9 of 18 officials
penciling in at least one *hike*** this year. Residential solar is financed
demand; the entire curve moving up is a first-order headwind.

But the dominant fact is sectoral and structural, not cyclical. **The Section 25D
residential clean-energy credit expired 2025-12-31**, terminated by the One Big
Beautiful Bill Act nearly a decade early. Ohm Analytics expects Q2 interconnections
**−25%+ YoY** and full-year installs **−22%**; BloombergNEF describes an industry
**"collapse" in 2026 that will not recover to 2023 levels within the decade**.
ENPH's own Q1'26 US revenue fell **−23%** (US = 83% of revenue) and it cut **6% of
its workforce**. Consensus for tomorrow is **$292.2M revenue (−19.6% YoY)** and
**$0.46 EPS (−33.3% YoY)** — with **~$85M of guided revenue being non-recurring
"safe harbor" shipments** and management already flagging **~3pp of tariff-driven
gross-margin compression**.

**This is the "why" behind everything phases 1–5 measured.** The −40.6% since
2026-05-22, the persistent bearish sweep campaign, the put-heavy dealer book, the
24 sessions of `FULLY_NEGATIVE` gamma — all sit on top of a demand base that has
been legislated away.

The one genuinely adverse-to-bears reading: **Technology sector flow is
`persistence_score = 1` / `trend = "INFLOW"` — 5 of 5 sessions positive.**

## Key signals

- **`regime = "TRANSITIONAL — Mixed signals, reduce position size, wait for
  clarity"`**, `trend = "CHOPPY"`, `bullish_pct = 35.2%`, SPY below 20d **and** 50d
  SMA [MACRO:MarketRegime_2026-07-27 UW].
- **Two binaries in 48h: ENPH earnings 2026-07-28 postmarket (±12.25% implied),
  then FOMC statement 2026-07-29 14:00 ET**
  [MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov].
- **`DGS10` +28bp in 30 days to 4.69%**; June dot plot median YE-2026 **3.8%** vs
  3.4% in March, **9 of 18 see a hike** [MACRO:DGS10_2026-07-24 FRED],
  [MACRO:FOMC_SEP_2026-06-17 WebSearch:federalreserve.gov].
- **Section 25D expired 2025-12-31**; installs guided **−22% FY**, sector
  "collapse" per BNEF; ENPH **−38% since 2026-06-03**
  [MACRO:25D_expiry_2025-12-31 WebSearch:pv-tech.org], [MACRO:BNEF WebSearch:marketwise.com].
- **Technology sector flow `persistence_score = 1`, `trend = "INFLOW"`, 5/5
  sessions** — the strongest counter-signal to a bearish ENPH thesis
  [MACRO:sector_flow_persistence_2026-07-27 UW].
- **Divergence:** UW flow says Technology INFLOW; `fz` says the Technology group
  **closed −0.90%** on the day [MACRO:group_valuation fz EOD].

## Detailed findings

### Market regime

`uw risk market-regime --date 2026-07-27`:

| Field | Value |
|---|---|
| **`regime`** | **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"** |
| `trend` | **CHOPPY** |
| `trading_guidance` | **"Half position sizes. Favor defined-risk strategies. Iron condors in range."** |
| `spy.current` | 739.09 |
| `spy.sma_20` / `above_20sma` | 746.66 / **false** |
| `spy.sma_50` / `above_50sma` | 745.00 / **false** |
| `spy.change_30d_pct` | +0.65% |
| `spy.pct_from_90d_high` | −2.8% |
| `market_breadth.bullish_flow_tickers` | 2,208 |
| `market_breadth.bearish_flow_tickers` | **4,071** |
| `market_breadth.bullish_pct` | **35.2%** |
| `market_breadth.tickers_with_options` | 6,279 |

**SPY is below both its 20- and 50-day averages** with only **35.2%** of 6,279
optionable names showing bullish flow — 1.84 bearish names for every bullish one.
The index is only −2.8% from its 90-day high, so this is a **broadening-weakness**
tape, not a drawdown: the index is held up by a narrow cohort while the median
name is being sold. That is precisely the environment in which a small-cap with a
broken story keeps bleeding regardless of the index.

`sector_rotation` (from the same call):

| Money flowing IN | $ | Money flowing OUT | $ |
|---|---|---|---|
| Communication Services | +72,620,658 | Consumer Cyclical | −84,596,545 |
| **Technology** | **+20,987,302** | Financial Services | −19,216,449 |
| Consumer Defensive | +12,828,155 | Utilities | −9,993,022 |

✅ **These reconcile exactly with phase-0.5's independent DuckDB sector aggregate**
(Comm Svcs +$72.6M, Technology +$21.0M, Cons Cyclical −$84.6M). Two independent
code paths, identical numbers — a useful validation of both.

**The `trading_guidance` is a phase-9 input, not decoration.** "Half position
sizes. Favor defined-risk strategies" is the regime tool's explicit instruction
and it compounds with every other de-rating in this run.

### Inflation

FRED, via the JSON API (key present in repo `.env`):

| Series | Latest | Prior | 2 prior | 12mo ago | **YoY** |
|---|---|---|---|---|---|
| `CPIAUCSL` | **332.568** (2026-06) | 333.979 (05) | 332.407 (04) | 321.435 (2025-06) | **+3.46%** |
| `CPILFESL` (core) | **336.065** (2026-06) | 336.121 (05) | 335.423 (04) | 327.658 (2025-06) | **+2.57%** |
| `PCEPI` | **131.527** (2026-05) | 130.938 (04) | 130.403 (03) | 126.380 (2025-05) | **+4.07%** |
| `PCEPILFE` (core) | **130.082** (2026-05) | 129.667 (04) | 129.343 (03) | 125.790 (2025-05) | **+3.41%** |

[MACRO:CPIAUCSL_2026-06 FRED], [MACRO:CPILFESL_2026-06 FRED],
[MACRO:PCEPI_2026-05 FRED], [MACRO:PCEPILFE_2026-05 FRED]

Headline CPI **fell month-over-month** (333.979 → 332.568, −0.42%) and core CPI was
essentially flat (336.121 → 336.065). At **+2.57% YoY core CPI** the inflation
picture is close to target.

⚠️ **But the PCE series tell a different and more hawkish story**: headline PCE at
**+4.07%** and core PCE at **+3.41%** YoY. Headline PCE running *above* headline
CPI is unusual (PCE normally runs below), and **core PCE — the Fed's preferred
gauge — at 3.41% is materially above the 2% target.** Values were recomputed from
the raw index levels rather than taken from any secondary source; the ordering is
as reported. This is the most plausible explanation for the June dot plot's hawkish
shift and directly contradicts any "rate cuts are coming" read that a
2.57% core-CPI print alone might suggest.

**Impact on ENPH: headwind.** Persistent core PCE keeps policy tight and keeps
consumer financing costs elevated for a discretionary, credit-financed purchase.

### Labor

| Series | Latest | Prior | 2 prior | MoM Δ |
|---|---|---|---|---|
| `PAYEMS` (thousands) | **158,984** (2026-06) | 158,927 (05) | 158,798 (04) | **+57k** (May: +129k) |
| `UNRATE` | **4.2%** (2026-06) | 4.3% (05) | 4.3% (04) | −0.1pp |

[MACRO:PAYEMS_2026-06 FRED], [MACRO:UNRATE_2026-06 FRED]

Payroll growth **more than halved** (+129k → +57k) while unemployment *ticked down*
to 4.2%. A softening-but-not-breaking labor market: enough cooling to worry about
consumer demand, not enough to force the Fed's hand toward cuts.

**Impact on ENPH: mild headwind.** Residential solar is a large discretionary
household capital outlay; decelerating job growth pressures the demand pool
without delivering the offsetting rate relief a genuine slowdown would bring.

### Rates

| Series | Latest | ~30d ago | Δ |
|---|---|---|---|
| `DFF` | **3.63%** (2026-07-24) | 3.63% (07-03) | **0bp** |
| `SOFR` | 3.64% (2026-07-24) | 3.62% (06-24) | +2bp |
| **`DGS10`** | **4.69%** (2026-07-24) | 4.41% (06-24) | **+28bp** |
| **`DGS2`** | **4.33%** (2026-07-24) | 4.11% (06-24) | **+22bp** |
| `T10Y2Y` | **+0.34** (2026-07-27) | +0.31 (06-25) | +3bp, **not inverted** |
| `DTWEXBGS` | 120.7105 (2026-07-24) | 121.412 (06-24) | **−0.58%** |

[MACRO:DGS10_2026-07-24 FRED], [MACRO:DGS2_2026-07-24 FRED],
[MACRO:T10Y2Y_2026-07-27 FRED], [MACRO:DFF_2026-07-24 FRED],
[MACRO:DTWEXBGS_2026-07-24 FRED], [MACRO:SOFR_2026-07-24 FRED]

**FOMC context** [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov],
[MACRO:FOMC_2026-07-29 WebSearch:cmelitegroup.com]:

- Target range held at **3.50%–3.75%** on 2026-06-17, unchanged since December 2025.
- **June SEP dot plot: median year-end 2026 rate 3.8%, up sharply from 3.4% in
  March. Nine of eighteen officials penciled in at least one *increase* this year.**
- **Next meeting: July 28–29, 2026. Statement 2026-07-29 at 14:00 ET**, press
  conference 14:30. **No new dot plot** (SEP is published at only four of eight
  meetings).

**This is the single most ENPH-relevant macro fact in the phase.** The policy
rate has not moved, but **the whole curve has repriced upward** — the 10-year is
+28bp in a month and the Fed's own median dot now implies *hikes* rather than
cuts. Residential solar economics are a spread trade between the levelized cost of
solar and the homeowner's financing rate; a 28bp move in the 10-year (and the
mortgage/HELOC/solar-loan rates that track it) directly compresses that spread.

The curve is **normal (+34bp) and steepening**, so this is not a recession signal —
it is a **higher-for-longer** signal, which is the worst configuration for ENPH:
no demand relief from rate cuts, and no offsetting flight-to-quality bid.

**Impact on ENPH: clear headwind.**

### Activity

| Indicator | Latest | Prior | Release |
|---|---|---|---|
| **ISM Manufacturing PMI** | **53.3** | 54.0 (May) | 2026-06 |
| S&P Global US Mfg PMI (flash) | **53.8** | 53.9 (Jun) | 2026-07 |
| ISM Services PMI | **not retrieved** | — | — |

[MACRO:ISM_MFG_2026-06 WebSearch:prnewswire.com],
[MACRO:SPGlobalMfgPMI_2026-07 WebSearch:tradingeconomics.com]

ISM Manufacturing at **53.3** marks a **20th consecutive month of expansion**,
though down 0.7pp from May. The July S&P Global flash at 53.8 missed the 54.3
consensus. Expansion, decelerating slightly.

⚠️ **ISM Services PMI and consumer-confidence readings for July 2026 could not be
retrieved** — search returned July *2025* Services data. **Recorded as unavailable
rather than substituted with a stale print** (see `## Tool / source errors`).

**Impact on ENPH: neutral.** ENPH's demand problem is regulatory and rate-driven,
not industrial-cycle driven. A manufacturing PMI in the low 50s tells us nothing
about whether homeowners install solar.

### Consumer

**Not retrieved.** U-Michigan Consumer Sentiment and Conference Board Consumer
Confidence for July 2026 were not returned by search. **Not fabricated, not
back-filled from an older print.** Marked `n/a` in the tailwind/headwind table.

This is a genuine gap in this phase: consumer confidence is arguably the *most*
relevant soft indicator for residential solar demand. Phase-9 should treat the
consumer channel as **unmeasured**, and the `PAYEMS`/`UNRATE` data above as the
only direct read on household capacity.

### Sector overlay — the decisive finding

The residential-solar demand base has been **legislated away**, and this is not a
forecast but an event that has already happened:

- **Section 25D Residential Clean Energy Credit expired 2025-12-31**, terminated by
  the One Big Beautiful Bill Act (signed 2025-07-04) — roughly a decade ahead of
  its original 2034 sunset. Systems completed in 2026 or later **do not qualify for
  the 30% credit** [MACRO:25D_expiry_2025-12-31 WebSearch:pv-tech.org],
  [MACRO:OBBBA_2025-07-04 WebSearch:solarpermitsolutions.com].
- **Ohm Analytics:** Q2 2026 solar interconnections **−25%+ YoY**; full-year
  installations **−22%** [MACRO:OhmAnalytics_Q2-2026 WebSearch:marketwise.com].
- **BloombergNEF:** the industry faces a **"collapse" in 2026** and is **not
  expected to recover to 2023 record levels within the next decade**
  [MACRO:BNEF_2026 WebSearch:marketwise.com].
- **Peer price action since 2026-06-03:** SEDG **−33%**, **ENPH −38%**, RUN −16%
  [MACRO:solar_peers_2026-07 WebSearch:marketwise.com].
- **ENPH-specific:** Q1'26 US revenue **−23% YoY**, with the **US at 83% of total
  revenue**; workforce cut **6%** earlier this year
  [MACRO:ENPH_Q1-2026 WebSearch:marketwise.com], [MACRO:ENPH_Q1-2026 WebSearch:pv-tech.org].

**Tomorrow's print, in this context**
[MACRO:ENPH_Q2-2026_preview WebSearch:tradingview.com/zacks]:

| Item | Value |
|---|---|
| Zacks consensus revenue | **$292.2M** (**−19.6% YoY**) |
| Zacks consensus EPS | **$0.46** (**−33.3% YoY**) |
| Company guidance range | **$280–310M** |
| — of which **"safe harbor" shipments** | **~$85M (≈29% of the midpoint)** |
| IQ Battery shipments guided | 100–110 MWh |
| Guided tariff impact on GM | **≈ −3 percentage points** |
| Positives cited | PowerMatch launch (2026-05), IQ9N microinverter for Europe (2026-06), US commercial microinverter expansion |

⚠️ **The ~$85M of safe-harbor shipments is a quality-of-revenue flag for phase-7b.**
Safe-harbor volume is demand *pulled forward* to qualify under expiring credit
provisions — it is non-recurring by construction. Nearly **29% of guided revenue**
is therefore borrowed from future quarters. A "beat" driven by safe-harbor
shipments is not evidence of demand stabilisation, and phase-7b/8b must not read
it as such.

**Impact on ENPH: severe structural headwind.** This is the mechanism behind every
bearish measurement in phases 1–5.

### Sector rotation

`uw options-flow sector-flow --date 2026-07-27` (net = call premium − put premium):

| Sector | `net_flow` | Call premium | Put premium |
|---|---|---|---|
| **Technology** | **+366,844,565** | 6,450,776,219 | 6,083,931,654 |
| Communication Services | +348,281,698 | 869,903,286 | 521,621,588 |
| Financial Services | +149,843,233 | 419,076,216 | 269,232,983 |
| Healthcare | +85,410,184 | 258,245,066 | 172,834,882 |
| Consumer Defensive | +53,427,583 | 97,751,554 | 44,323,971 |
| Energy | +38,919,696 | 80,348,294 | 41,428,598 |
| Real Estate | +16,437,881 | 24,125,570 | 7,687,689 |
| Utilities | +15,012,374 | 86,088,378 | 71,076,004 |
| Basic Materials | +8,993,131 | 49,902,606 | 40,909,475 |
| Industrials | −47,026,950 | 604,270,697 | 651,297,647 |
| Consumer Cyclical | **−386,132,358** | 946,109,053 | 1,332,241,411 |

⚠️ **Two different "net flow" definitions coexist in the CLI.** `sector-flow`
computes `total_premium_call − total_premium_put` (Technology **+$366.8M**), while
`risk market-regime`'s `sector_rotation` and the screener compute
`bullish_premium − bearish_premium` (Technology **+$21.0M**). **A 17× difference on
the same sector, same date.** Neither is wrong; they measure different things
(gross call-vs-put premium vs directionally-classified premium). **Downstream
phases must not compare the two.** The directional measure (+$21.0M) is the more
meaningful one and is what phase-0.5 used.

`uw options-flow sector-flow-persistence --days 5` (2026-07-21 → 07-27):

| Sector | `persistence_score` | `trend` | Net flow by day (07-21 → 07-27, $M) |
|---|---|---|---|
| **Technology** | **1.0** | **INFLOW** | 2,462.5 → 3,234.9 → 767.2 → 966.7 → **366.8** |
| Energy | 1.0 | INFLOW | 84.3 → 108.1 → 104.3 → 78.0 → 38.9 |
| Financial Services | 1.0 | INFLOW | 251.1 → 184.5 → 136.2 → 145.1 → 149.8 |
| Healthcare | 1.0 | INFLOW | 144.7 → 456.7 → 30.7 → 132.5 → 85.4 |
| Real Estate | 1.0 | INFLOW | 10.2 → 5.5 → 9.2 → 23.5 → 16.4 |
| Basic Materials | 1.0 | INFLOW | 29.0 → 35.7 → 15.5 → 18.3 → 9.0 |
| **Utilities** | **1.0** | **INFLOW** | 20.3 → 38.3 → 9.8 → 3.6 → 15.0 |
| Consumer Defensive | 1.0 | INFLOW | 49.1 → 36.1 → 133.6 → 35.8 → 53.4 |
| Communication Services | 0.8 | INFLOW | 591.9 → 501.2 → −784.0 → 75.4 → 348.3 |
| Industrials | 0.8 | **OUTFLOW** | 33.5 → −68.7 → −125.4 → −194.0 → −47.0 |
| Consumer Cyclical | 0.6 | **ROTATING** | 307.7 → 154.7 → −3,043.2 → −672.7 → −386.1 |

**Verdict: ADVERSE to a bearish ENPH thesis — with three material qualifications.**

Technology posts a **perfect `persistence_score = 1` and `trend = "INFLOW"`, 5 of
5 sessions positive**. Taken at face value, shorting a Technology name while smart
money persistently buys the sector is the wrong side of the rotation. This is the
strongest counter-signal in the run and phase-8b must weigh it. However:

1. **The inflow is decelerating hard** — $2,462M → $3,235M → $767M → $967M →
   **$367M**. Today's reading is **11% of Wednesday's**. The sign is persistent;
   the *force* is collapsing.
2. **ENPH shares no economic driver with the names carrying it.** Phase-0.5
   established the Technology tape is led by SNDK/MU/PLTR/MSFT/NBIS (AI and
   memory), and that **ENPH ranks 59th most net-bearish of 531 Technology names**.
   Finviz classifies ENPH as Technology / **Solar**; its real comps are SEDG, RUN
   and the utility complex. **"Technology is bid" is close to meaningless for a
   residential-solar hardware maker.**
3. **Price breadth contradicts the flow.** See the `fz` cross-check below.

Note also **Utilities is `persistence_score = 1` INFLOW** — solar's nearer
economic neighbour is *also* being bought. That is a genuine, if weak,
mitigating datapoint for the bear case.

**`fz` breadth + valuation cross-check (advisory)**
[MACRO:sector_breadth fz EOD], [MACRO:group_valuation fz EOD]:

`fz breadth --group sector --agent` (`captured_at 2026-07-28T00:39:38Z`,
`dataset "sec_all"`, `timeframe "1d"`):

| Field | Value |
|---|---|
| advancers / decliners | **328 / 175** |
| `pct_green` | **65.21%** |
| avg / median change | +0.77% / +0.82% |
| total | 503 |
| `top_mover` | **WDAY +9.01%** |
| `worst_mover` | **SNDK −11.02%** |

`fz groups --by sector --view valuation --agent`:

| Sector | P/E | Fwd P/E | PEG | **Change** |
|---|---|---|---|---|
| Consumer Defensive | 26.64 | 20.66 | 2.98 | +1.56% |
| Communication Services | 28.76 | 28.47 | 1.58 | +1.55% |
| Consumer Cyclical | 28.15 | 19.90 | 1.49 | +1.12% |
| Financial | 17.99 | 14.83 | 1.49 | +0.95% |
| Healthcare | 30.71 | 18.18 | 2.11 | +0.50% |
| Basic Materials | 21.17 | 13.68 | 1.17 | +0.30% |
| Industrials | 38.94 | 28.67 | 2.04 | +0.13% |
| Real Estate | 32.23 | 30.05 | 2.91 | −0.22% |
| **Technology** | **34.82** | **25.58** | **0.89** | **−0.90%** |
| **Utilities** | 20.60 | 16.24 | 1.74 | **−1.02%** |
| Energy | 18.77 | 12.64 | 1.30 | −2.41% |

**Two divergences worth recording:**

- **Technology closed −0.90% — the second-worst sector of eleven — on the same day
  UW reports persistent sector INFLOW.** Options premium went in; price went down.
  That is precisely the pattern phase-1 documented at the single-name level
  (`call_ask_share = 0.475` — calls being *sold*), and it suggests a chunk of the
  "inflow" is **call writing and put buying rather than bullish accumulation.**
  **This materially weakens the ADVERSE rotation verdict.**
- **`pct_green = 65.21%` (fz, S&P 500 price breadth) vs `bullish_pct = 35.2%`
  (UW, 6,279 optionable names, flow breadth).** Not a contradiction — different
  universes and different measures (price vs flow) — but the gap is instructive:
  **large caps rose while the broad flow tape leaned bearish.** Consistent with the
  narrow-index/weak-median read above. A $4.84B small cap sits with the median, not
  the index.
- Note the day's `worst_mover` was **SNDK −11.02%** — the very name that led
  phase-0.5's bullish-flow ranking at **+$58.1M**. A vivid same-day reminder that
  a big bullish premium print is not a forecast.

### Cross-name correlation

`uw risk portfolio-correlation --symbols ENPH --lookback-days 30`:

```json
{"high_correlations":null,"sector_breakdown":{"Unknown":1},
 "sector_concentration":"100% in top sector","tickers_analyzed":1,
 "ticker_details":[{"industry":"Unknown","sector":"Unknown","symbol":"ENPH"}],
 "warnings":["CONCENTRATION: 100% of tickers in Unknown"]}
```

`ls -d research/*/2026-07-27/` returns **only `research/ENPH/2026-07-27/`**.

**Verdict: no concurrent positions to correlate against.** The tool was run with
the single symbol (rather than skipped) and returned `tickers_analyzed = 1`,
`high_correlations = null`. The correlation sizing gate is **not applicable** to
this run.

Note the `sector`/`industry` fields returned **"Unknown"** — the known-broken
sector field on this tool (correlation coefficients themselves are reliable; the
sector labelling is not). The `"CONCENTRATION: 100% in Unknown"` warning is an
artifact of a one-symbol call, not a finding.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on **Solar / Technology** |
|---|---|---|---|---|
| **Section 25D credit** | **Expired** | **2025-12-31** | WebSearch:pv-tech.org | 🔴 **severe headwind** |
| Residential installs (Ohm) | **−22% FY, −25%+ Q2 YoY** | 2026 Q2 | WebSearch:marketwise.com | 🔴 **severe headwind** |
| Industry outlook (BNEF) | **"collapse", no recovery to 2023 in a decade** | 2026 | WebSearch:marketwise.com | 🔴 **severe headwind** |
| ENPH Q1'26 US revenue | **−23% YoY** (US = 83% of rev) | 2026 Q1 | WebSearch:pv-tech.org | 🔴 headwind |
| ENPH guided tariff GM hit | **≈ −3pp** | Q2'26 guide | WebSearch:tradingview.com | 🔴 headwind |
| **`DGS10`** | **4.69% (+28bp/30d)** | 2026-07-24 | FRED | 🔴 **headwind** |
| `DGS2` | 4.33% (+22bp/30d) | 2026-07-24 | FRED | 🔴 headwind |
| FOMC dot plot (June SEP) | **median YE26 3.8%** (vs 3.4% Mar); 9/18 see a hike | 2026-06-17 | WebSearch:federalreserve.gov | 🔴 **headwind** |
| Core PCE YoY | **+3.41%** | 2026-05 | FRED | 🔴 headwind (keeps policy tight) |
| Headline PCE YoY | +4.07% | 2026-05 | FRED | 🔴 headwind |
| Core CPI YoY | **+2.57%** | 2026-06 | FRED | 🟡 mild tailwind (near target) |
| Headline CPI YoY | +3.46% (MoM **−0.42%**) | 2026-06 | FRED | 🟡 mild tailwind |
| `PAYEMS` MoM | **+57k** (from +129k) | 2026-06 | FRED | 🟡 mild headwind |
| `UNRATE` | 4.2% (from 4.3%) | 2026-06 | FRED | ⚪ neutral |
| `DFF` / `SOFR` | 3.63% / 3.64%, **flat 30d** | 2026-07-24 | FRED | ⚪ neutral |
| `T10Y2Y` | **+0.34, not inverted, steepening** | 2026-07-27 | FRED | ⚪ neutral (no recession signal) |
| `DTWEXBGS` | 120.71 (**−0.58%**/30d) | 2026-07-24 | FRED | 🟢 mild tailwind (weaker USD ⇒ Europe rev) |
| ISM Manufacturing PMI | 53.3 (20th mo. expansion) | 2026-06 | WebSearch:prnewswire.com | ⚪ neutral |
| S&P Global Mfg PMI (flash) | 53.8 (miss vs 54.3) | 2026-07 | WebSearch:tradingeconomics.com | ⚪ neutral |
| **Market regime** | **TRANSITIONAL / CHOPPY**, breadth 35.2% | 2026-07-27 | UW | 🔴 headwind |
| SPY vs 20d / 50d SMA | **below both** (739.09 vs 746.66 / 745.00) | 2026-07-27 | UW | 🔴 headwind |
| **Technology sector flow** | **`persistence 1.0`, INFLOW 5/5** | 2026-07-27 | UW | 🟢 **tailwind (the counter-signal)** |
| Utilities sector flow | `persistence 1.0`, INFLOW | 2026-07-27 | UW | 🟢 mild tailwind |
| Technology price change | **−0.90%** (2nd worst of 11) | 2026-07-27 | fz EOD | 🔴 headwind (contradicts the flow) |
| ISM Services PMI | **n/a — not retrieved** | — | — | ⚪ unmeasured |
| U-Mich / Conf. Board | **n/a — not retrieved** | — | — | ⚪ unmeasured |

**Tally: 11 headwinds (5 severe), 4 tailwinds (2 of them mild), 5 neutral,
2 unmeasured.**

## Catalyst calendar (next 30d)

> **Front-expiry implied move: ±12.25% / ±$4.65** → post-event range
> **$33.36 – $42.66** [CTX:implied_move_pct]. Phase-9 must size every structure to
> this priced range; each binary below is read against it.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-07-28, postmarket** | **ENPH Q2 2026 earnings** (consensus $292.2M / $0.46; guide $280–310M incl. ~$85M safe-harbor; ~3pp tariff GM hit) | **Dominant.** Sole determinant of the next 2 weeks | **IS the ±12.25% move** |
| **2026-07-29, 14:00 ET** | **FOMC statement** (no dot plot); target 3.50–3.75% held since Dec 2025 | Second-order but same-week; rate path is a direct solar-demand input | Typically **inside** ±12.25% for a single name, but lands **while ENPH is still gapping** |
| 2026-07-31 | **Front-week option expiry** — 16,897 OI, only ~2,000 contracts inside the implied move; the **positive-gamma island expires** | Removes the sole long-gamma cushion (`today_total_gex = +1,047,168`) | inside |
| ~2026-08-01 | ISM Manufacturing PMI (July) | Low relevance for solar | inside |
| ~2026-08-07 | Nonfarm payrolls (July) | Consumer-capacity read | inside |
| ~2026-08-12 | CPI release (July) | Feeds the higher-for-longer question | inside |
| **2026-08-21** | **Monthly OPEX** — **18.64%** of total OI, $40 put wall (7,888) and $35 put wall (3,734) | Large put-heavy expiry; max pain $50 is an ITM artifact (`phase-4-structure.md`) | inside |
| ~2026-08-26 | Ohm Analytics / SEIA Q3 install data | Confirms or refutes the −22% FY trajectory | inside |

⚠️ **The FOMC/earnings collision is the defining calendar risk of this setup.**
ENPH gaps on its own number Tuesday night, then trades that gap **into a Fed
statement on Wednesday afternoon** — with a `FULLY_NEGATIVE` gamma surface
(`phase-4-structure.md`) that amplifies whatever direction results. **Any phase-9
structure with a stop inside ±12.25% is likely to be taken out by path, not
thesis.**

## Tool / source errors

No `uw`, `fz`, `curl` or FRED call errored; all exited 0 and round-tripped through
`jq`. FRED Path A was used (`FRED_API_KEY` present in the repo-root `.env`); the
blocked chart-CSV endpoint was **not** attempted, per the phase-6 reality check.
Five items recorded:

1. **ISM Services PMI (July 2026) — not retrieved.** Search returned a July **2025**
   Services article. **Not substituted with the stale print.** Marked `n/a`.
2. **U-Michigan Consumer Sentiment and Conference Board Consumer Confidence
   (July 2026) — not retrieved.** Same handling. This is the most consequential gap
   in this phase, since consumer confidence is a direct residential-solar demand
   input. Phase-9 should treat the consumer channel as **unmeasured**.
3. **`sector-flow` vs `market-regime.sector_rotation` use different `net_flow`
   definitions** — `total_premium_call − total_premium_put` (Tech **+$366.8M**) vs
   `bullish_premium − bearish_premium` (Tech **+$21.0M**), a **17× gap on the same
   sector and date**. Both quoted with their definitions; **never compared**.
   Flagged for phase-10.
4. **`portfolio-correlation` returns `sector: "Unknown"`, `industry: "Unknown"`.**
   Known-broken sector field on this tool. Coefficients are unaffected (and none
   were produced here — `tickers_analyzed = 1`). The
   `"CONCENTRATION: 100% in Unknown"` warning is a one-symbol artifact, **not** a
   risk finding.
5. **`fz breadth --group sector --agent` returns a single aggregate object**
   (503 S&P constituents), **not a per-sector table** — exactly as the phase-6 note
   warns. Per-sector data was therefore taken from
   `fz groups --by sector --view valuation`, keyed by `Name`.

## DATA NOTE / CORRECTION

- **All YoY inflation figures are my arithmetic on raw FRED index levels**, not
  returned fields: e.g. CPI `332.568 ÷ 321.435 − 1 = +3.46%`. The `observations[12]`
  element under `sort_order=desc&limit=14` was verified to be exactly 12 months
  prior for each series.
- **Rate "~30d ago" values use the 21st non-missing observation** (FRED daily
  series carry `"."` for holidays), so the comparison dates vary slightly by series
  (06-24 to 07-03) and are quoted individually rather than assumed uniform.
- **SPY SMA / breadth figures come from `risk market-regime`**, not recomputed.
- **`market-regime.sector_rotation` reconciles exactly with phase-0.5's DuckDB
  aggregate** (Tech +$21.0M, Comm Svcs +$72.6M, Cons Cyclical −$84.6M). Recorded as
  a positive cross-validation, not a correction.
- **Headline PCE (+4.07%) exceeding headline CPI (+3.46%) is unusual** and was
  re-derived from the index levels before publication. The values are as returned;
  the ordering is reported as observed and flagged rather than smoothed.
- No value written in this phase was corrected after first read.

## Verdict for downstream phases

- **Net macro bias for ENPH: HEADWIND (strong).** 11 headwinds to 4 tailwinds, and
  the headwinds are structural (a repealed tax credit, a −22% install year, a
  "collapse" outlook) while the tailwinds are technical and decaying (a Technology
  flow inflow that fell to 11% of its Wednesday level and whose sector still
  **closed −0.90%**). The macro regime tool independently says
  **"reduce position size, wait for clarity."**
- **Conviction: 4 / 5.** The sector evidence is documentary rather than inferential —
  25D expiry is a matter of enacted law, not a forecast — and it is corroborated by
  ENPH's own reported numbers (Q1 US revenue −23%, 6% workforce cut) and by peer
  price action (SEDG −33%, RUN −16%). Held to 4 rather than 5 because two consumer
  indicators are unmeasured, and because the Technology/Utilities rotation signals
  genuinely cut the other way.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. **Section 25D expired 2025-12-31 (OBBBA); FY-2026 installs guided −22%, Q2
     interconnections −25%+ YoY; BNEF sees no recovery to 2023 levels within a
     decade.** [MACRO:25D_expiry_2025-12-31 WebSearch:pv-tech.org],
     [MACRO:OhmAnalytics_Q2-2026 WebSearch:marketwise.com]
  2. **`DGS10` +28bp in 30 days to 4.69%, with the June dot plot lifting median
     YE-2026 to 3.8% (from 3.4%) and 9 of 18 officials projecting a hike** —
     higher-for-longer directly compresses residential-solar financing economics.
     [MACRO:DGS10_2026-07-24 FRED], [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-07-28 postmarket — ENPH Q2 2026 earnings.** Consensus $292.2M / $0.46;
     guide $280–310M of which **~$85M (~29%) is non-recurring safe-harbor**;
     ~3pp tariff GM headwind. **This *is* the ±12.25% implied move.**
  2. **2026-07-29 14:00 ET — FOMC statement.** ENPH will trade its earnings gap
     directly into the Fed, under `FULLY_NEGATIVE` gamma. **Path risk, not just
     outcome risk.**
- **Sector-rotation verdict: `ADVERSE` (to a bearish thesis), `persistence_score = 1.0`,
  `trend = "INFLOW"` (Technology, 5/5 sessions).** ⚠️ **Heavily qualified** and
  phase-9 should apply the rotation gate at **partial weight**: the inflow decayed
  from $2,462M to $367M across the window (**−85%**), the sector nonetheless
  **closed −0.90%** on `fz` EOD data, and ENPH ranks **59th most net-bearish of 531
  Technology names** while sharing no economic driver with the AI/memory names
  driving the sector aggregate. Utilities (solar's nearer neighbour) is also
  `persistence 1.0 INFLOW`, which is the more genuine — if weaker — mitigant.
- **Correlation verdict: no concurrent positions.** `ls -d research/*/2026-07-27/`
  returns only `research/ENPH/2026-07-27/`; `portfolio-correlation` run with the
  single symbol returned `tickers_analyzed = 1`, `high_correlations = null`.
  **No cluster (≥0.70) and no soft-watch (0.60–0.70) pair.** The correlation sizing
  gate does not bind this run.
- **Open questions:**
  - Consumer confidence and ISM Services are **unmeasured** for July 2026. Does any
    other read on household discretionary capacity exist? → **phase-7b/7c**
  - **~$85M of guided revenue is safe-harbor pull-forward.** How much of the
    revenue base is genuinely recurring, and what does that do to FY-2027? →
    **phase-7b** (the fundamentals veto)
  - How large were ENPH's **actual** last four earnings-day moves? Still
    unanswered from phase-4/5; it determines whether a 12.25% implied move is rich
    or cheap. → **phase-7b**
  - Technology flow says INFLOW while Technology price says **−0.90%** and ENPH's
    own call flow is **sold** (`call_ask_share = 0.475`). Is the "inflow" actually
    call writing? → **phase-8b**
