# Phase 6 — Macro Overlay

**Ticker:** FSLR **Sector:** Technology / Solar
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-4-structure.md`, `phase-5-historical.md`

## Summary

**The macro is a headwind, the sector policy is a two-sided story, and
phase-0.5's "Technology is being sold" framing was wrong — it must be
corrected.** The FOMC held at **3.50–3.75% on 2026-07-29 with a rare
three-way dissent, all three wanting a *hike*.** Core PCE runs **3.29% YoY**,
well above target, and the 10-year has backed up **24bp in a month to 4.68%**.
For a capital-intensive, project-finance-dependent industry that is a direct
headwind, and FSLR's **Beta of 1.76** amplifies it.

**The correction:** phase 0.5 read Technology's −$187.7M net bullish−bearish
premium as the sector being sold, and phase 5 carried that forward as an open
question. Extending the same DuckDB measure across five sessions shows
Technology at **+21.0, +143.6, +56.0, +806.6, −187.7 ($M)** — cumulative
**+$839.5M**, positive on four of five days. **Today is a one-day reversal
after the largest inflow of the week, not a rotation out.** UW's own
`sector-flow-persistence` agrees on its own metric (`persistence_score 1`,
`trend INFLOW`). Phase 9 should treat sector rotation as **aligned**, not
adverse.

The company-specific news is genuinely strong and explains the two-day pop.
FSLR reported Q2 on **2026-07-30** with **EPS $3.92 versus a $2.86 estimate —
a 37% beat** — net income $423M, adjusted EBITDA $644M, **~57% gross
margin**, a **45.1 GW backlog through 2030**, and reaffirmed 2026 guidance.
Revenue fell 4% YoY to $1.06B and cash dropped from $2.4B to $1.7B.

Policy cuts both ways, and the timing is pointed: **Section 45X manufacturing
credits survive through 2032** and FSLR expects **$2.10–2.19B** from them in
2026 — an enormous, durable subsidy to precisely its US-manufacturing model.
But the **45Y/48E project credits entered an expedited phaseout for projects
beginning construction after 2026-07-04** — a date now **27 days past**. The
subsidy has been moved from FSLR's *customers* to FSLR's *factories*.

`uw risk market-regime` returns **"TRANSITIONAL — Mixed signals, reduce
position size, wait for clarity"** with breadth at just **34.1% bullish**
(2,142 vs 4,138 tickers), and its explicit guidance is **"Half position
sizes."** That is a direct phase-9 sizing input.

## Key signals

- **FOMC held 3.50–3.75%, 9–3, with three dissents preferring a HIKE**
  (Hammack, Kashkari, Logan) `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`
- **Core PCE +3.29% YoY, headline PCE +3.67%, CPI +3.46%** (June 2026) —
  inflation not at target `[MACRO:PCEPILFE_2026-06 FRED]`
- **10y at 4.68%, +24bp in 30 days**; 2s10s **+0.47**, steepening and normal —
  a direct headwind to solar project economics `[MACRO:DGS10_2026-07-30 FRED]`
- **Market regime TRANSITIONAL; guidance "Half position sizes"**; breadth
  34.1% bullish `[MACRO:MarketRegime_2026-07-31 UW]`
- **Technology 5-day net bullish−bearish +$839.5M, positive 4 of 5 days** —
  today's −$187.7M is an outlier, not a trend `[MACRO:sector_flow_persistence DUCKDB]`
- **FSLR Q2 EPS $3.92 vs $2.86 est (+37%)**, EBITDA $644M, GM ~57%, backlog
  45.1 GW `[MACRO:FSLR_Q2_2026-07-30 WebSearch:gurufocus.com]`
- **45X credits preserved to 2032; FSLR expects $2.10–2.19B in 2026**
  `[MACRO:45X_policy WebSearch:novoco.com]`
- **45Y/48E phaseout for construction starting after 2026-07-04 — already
  past** `[MACRO:45Y48E_phaseout WebSearch:novoco.com]`
- **Payrolls slowing: +57k June vs +129k May**; unemployment 4.2%
  `[MACRO:PAYEMS_2026-06 FRED]`
- **U-Mich sentiment 55.2 final July, up from 49.5**; 1y inflation
  expectations 4.2% (from 4.6%) `[MACRO:UMich_2026-07-31 WebSearch:cnbc.com]`

## Detailed findings

### Market regime (UW)

| Field | Value |
|-------|-------|
| `regime` | **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"** |
| `trend` | UPTREND |
| `trading_guidance` | **"Half position sizes. Favor defined-risk strategies. Iron condors in range."** |
| SPY current | 747.03 |
| SPY vs SMA20 / SMA50 | above both (745.69 / 744.99) |
| SPY 30d change | **+0.17%** |
| SPY from 90d high | −1.76% |
| Bullish-flow tickers | 2,142 |
| Bearish-flow tickers | **4,138** |
| **Bullish %** | **34.1%** |
| Tickers with options | 6,280 |

**A textbook narrow tape.** SPY is above both moving averages and technically
in an UPTREND, yet it has gained **0.17% in 30 days** and only **34.1% of
optionable names carry bullish flow**. The index is being held up by a
handful of mega-caps — corroborated by `fz breadth`: of 503 S&P constituents,
**221 advancers vs 281 decliners, `pct_green` 43.94%, median change −0.24%**,
with **AMZN +15.32%** as top mover.

Two direct phase-9 inputs: the tool's **"Half position sizes"** guidance, and
its preference for **defined-risk structures** — which converges independently
with phase-5's PREMIUM_SELLING verdict.

Note the tension with `phase-0.5-context.md`'s news scan: *"S&P 500 books its
first July decline since 2014"* alongside *"US Stocks Rally to End a Turbulent
Month."* Both are true — a weak month ending with a strong day.

### Inflation (FRED)

| Series | Jun-2026 | May-2026 | Apr-2026 | **YoY** |
|--------|---------:|---------:|---------:|--------:|
| `CPIAUCSL` | 332.568 | 333.979 | 332.407 | **+3.46%** |
| `CPILFESL` (core) | 336.065 | 336.121 | 335.423 | **+2.57%** |
| `PCEPI` | 131.392 | 131.535 | 130.932 | **+3.67%** |
| `PCEPILFE` (core) | 130.266 | 130.094 | 129.663 | **+3.29%** |

Headline CPI and PCE **fell month-over-month** in June (332.568 from 333.979;
131.392 from 131.535) while **core PCE rose** (130.266 from 130.094). The
divergence — softening headline, sticky core — is precisely what produced the
three hawkish FOMC dissents. **Core PCE at 3.29% is 129bp above target.**

**Impact on solar: headwind.** Persistent core inflation keeps real rates
elevated, and utility-scale solar is among the most discount-rate-sensitive
asset classes in the market.

### Labor (FRED)

| Series | Jun-2026 | May-2026 | Apr-2026 |
|--------|---------:|---------:|---------:|
| `PAYEMS` (level, k) | 158,984 | 158,927 | 158,798 |
| **MoM change** | **+57k** | +129k | — |
| `UNRATE` | **4.2%** | 4.3% | 4.3% |

**Payroll growth more than halved** (+129k → +57k) while unemployment *fell*
to 4.2%. Slowing job creation with a firm unemployment rate is the classic
late-cycle signature — and it is why the Committee held despite three
dissents.

**Impact on solar: mildly positive.** A softening labour market is the main
argument for the cuts that would relieve the rate pressure on project
finance.

### Rates (FRED + FOMC)

| Series | Latest | 30 days prior | Δ |
|--------|-------:|--------------:|--:|
| `DFF` | 3.63% (07-30) | — | — |
| `SOFR` | 3.65% (07-30) | — | — |
| `DGS2` | 4.23% (07-30) | 4.14% (06-30) | **+9bp** |
| `DGS10` | **4.68%** (07-30) | 4.44% (06-30) | **+24bp** |
| `T10Y2Y` | **+0.47** (07-31) | +0.31 (07-01) | **+16bp steeper** |
| `DTWEXBGS` | 120.71 (07-24) | 121.41 (06-24) | −0.6% (softer USD) |

**FOMC, 2026-07-29:**
- Held the target range at **3.50%–3.75%**, a **9–3** vote — the **fifth
  consecutive hold**.
- **Three dissents — Hammack, Kashkari and Logan — all preferring a 25bp
  *increase*.** A three-way dissent is rare and signals genuine disagreement
  over whether policy is tight enough.
- Statement: *"Economic activity is expanding at a solid pace despite elevated
  uncertainty that owes, in part, to the conflict in the Middle East,"* with
  inflation **elevated relative to the 2% goal**.

**This is the single most important macro fact for FSLR.** The long end is
selling off (+24bp) while the curve steepens — the market is pricing *more*
term premium, not imminent easing. Utility-scale solar competes on levelized
cost of energy, which is dominated by the cost of capital. **A 24bp move in
the 10-year meaningfully degrades project IRRs across FSLR's customer base.**

Note the interaction with FSLR's balance sheet: cash fell **$2.4B → $1.7B**
while capex expands (South Carolina, Louisiana). Higher-for-longer rates raise
the cost of funding that build-out.

**Impact on solar: clear headwind — the strongest negative in this phase.**

### Activity (ISM)

| Index | Latest | Prior | Note |
|-------|-------:|------:|------|
| ISM Manufacturing PMI | **53.8** (Jul) | 53.9 (Jun) | Missed 54.3 est; **6th month expanding** |
| ISM Services PMI | 54.0 (Jun) | 54.5 (May) | July release **2026-08-05** |

Both comfortably above 50 but decelerating. June Services detail: business
activity and new orders slowed while employment rebounded to 51.2 — its first
expansion in four months.

**Impact on solar: neutral.** Expansion supports industrial electricity
demand; the deceleration argues against a capex acceleration.

### Consumer

| Index | Latest | Prior |
|-------|-------:|------:|
| U-Michigan Sentiment (final Jul) | **55.2** | 49.5 (Jun) |
| U-Mich prelim Jul | 54.4 | — |
| 1-year inflation expectations | **4.2%** | 4.6% (Jun) |
| Conference Board Confidence | Rose 2nd straight month | — |

A **5.7-point jump** in U-Michigan, beating the preliminary 54.4, driven by
falling gasoline prices and softer inflation prints. Consumers' 1-year
inflation expectation fell 40bp to 4.2% — though still double the Fed's
target, which is why the Committee remains cautious.

**Impact on solar: neutral-to-mildly-positive.** Residential solar is
sentiment-sensitive, but FSLR is a **utility-scale** thin-film manufacturer
with essentially no residential exposure — so the read-through is weak.

### Sector overlay — solar-specific catalysts (the dominant driver)

**FSLR Q2 2026 results, reported 2026-07-30 (the event behind this run):**

| Metric | Q2 2026 | Q2 2025 |
|--------|--------:|--------:|
| Net sales | **$1.06B** (−4% YoY) | — |
| Net income | **$423M** | $342M |
| **Diluted EPS** | **$3.92** | $3.18 |
| **Consensus EPS** | **$2.86** | — |
| **Surprise** | **+37.1%** | — |
| Adjusted EBITDA | $644M | $560M |
| Gross margin | **~57%** | — |
| Cash | $1.7B | $2.4B (YE-2025) |
| Backlog | **45.1 GW through 2030** | — |
| 2026 guidance | **Reaffirmed** | — |

**Policy — the two-sided core of the FSLR thesis:**

| Item | Status | Impact |
|------|--------|--------|
| **Section 45X** manufacturing credits | **Preserved through 2032**; FSLR monetized **$1.6B in 2025**, expects **$2.10–2.19B in 2026** | **Major structural tailwind** |
| **45Y / 48E** project credits | **Expedited phaseout for projects beginning construction after 2026-07-04** — 27 days past | **Demand headwind beyond backlog** |
| IEEPA tariffs | **+$89M net benefit** in Q2 gross margin | Tailwind (realized) |
| Section 301 tariffs | Assumed to apply in H2 | Headwind |
| Net tariff impact (guided) | **−$60M to −$80M** for the year | Modest headwind |
| Capacity | 25 GW global / **14 GW US** by end-2026; South Carolina Phase I on track for H2 2026 | Structural |

**The policy structure has inverted in FSLR's favour on manufacturing and
against it on demand.** 45X pays FSLR directly for every US-made module
through 2032 — roughly **$2.1B annually against a $22.7B market cap**, i.e.
~9% of market cap per year in subsidy. Meanwhile the credits that made its
*customers'* projects work are phasing out, with the qualifying construction
date already behind us.

That tension is the most credible explanation for the stock's **YTD −19.22%**
against a **+37% earnings beat** — and it is exactly the puzzle in the
surfaced headline *"Why Solar Stocks Have Fallen Despite Strong Earnings and
Bullish Outlook."* **The market is discounting a post-45Y/48E demand cliff
that the 45.1 GW backlog defers but does not eliminate.**

### Sector rotation

**Two UW metrics disagree because they measure different things** — the same
distinction `phase-1-flow.md` established at the single-name level.

`uw options-flow sector-flow` (today), where `net_flow = call premium − put
premium`:

| Sector | net_flow ($) | Call prem | Put prem |
|--------|-------------:|----------:|---------:|
| **Technology** | **+2,781,021,293** | 8,111,529,787 | 5,330,508,494 |
| Consumer Cyclical | +1,841,619,593 | | |
| Communication Services | +656,316,523 | | |
| Financial Services | +499,594,693 | | |
| Energy | +78,135,697 | | |
| Healthcare | +72,300,875 | | |
| Consumer Defensive | +39,406,223 | | |
| Basic Materials | +5,019,500 | | |
| Real Estate | −1,016,954 | | |
| Utilities | −5,546,758 | | |
| Industrials | −171,008,916 | | |

`uw risk market-regime`'s `sector_rotation`, which uses **bullish − bearish**
premium, reports **Technology −187,715,752** — matching phase-0.5's
independent DuckDB figure exactly.

**Both are correct.** Calls out-trade puts in Technology every day, so
`call − put` is structurally positive and says little about direction;
`bullish − bearish` is the directional measure. **`sector-flow`'s
`persistence_score = 1` for Technology is therefore near-meaningless** — it
scores sign-consistency on a metric that is almost never negative.

The informative version, computed on the directional measure across the same
five sessions:

| Sector | 07-27 | 07-28 | 07-29 | 07-30 | 07-31 | **5d total** |
|--------|------:|------:|------:|------:|------:|-------------:|
| **Technology** | +21.0 | +143.6 | +56.0 | **+806.6** | **−187.7** | **+839.5** |
| Communication Services | +72.6 | +59.6 | +75.9 | +41.3 | +38.0 | +287.4 |
| Consumer Cyclical | −84.6 | −30.8 | −98.0 | −9.3 | +86.4 | −136.3 |
| Industrials | +9.5 | −28.5 | −68.0 | −1.2 | −20.9 | −109.1 |
| Financial Services | −19.2 | +10.4 | −46.1 | +17.8 | −17.9 | −55.0 |
| Healthcare | +7.2 | +13.5 | +5.3 | +13.4 | −5.9 | +33.5 |
| Utilities | −10.0 | +2.7 | +30.7 | +2.2 | +3.4 | +29.0 |
| Basic Materials | −6.2 | −11.9 | −10.3 | −2.4 | −3.7 | −34.5 |
| Consumer Defensive | +12.8 | +5.6 | −13.0 | −1.5 | +3.9 | +7.8 |
| Energy | −2.7 | −1.5 | −12.3 | 0.0 | +1.1 | −15.4 |
| Real Estate | −1.1 | +0.9 | −0.6 | +11.0 | −0.4 | +9.8 |

**Technology is the strongest sector of the week on the directional measure
(+$839.5M), positive on four of five days.** Today's −$187.7M follows
**+$806.6M** the day before — mega-cap earnings (AMZN +15.32%, AAPL) drove a
massive inflow on 07-30 and today saw it partially given back. **This is
one-day mean reversion, not rotation out of Technology.**

**Rotation verdict: `aligned`.** The sector FSLR sits in is receiving
persistent directional inflow.

**`fz` breadth cross-check (advisory, EOD 2026-08-01T00:42Z):** S&P 500
**221 advancers / 281 decliners, `pct_green` 43.94%**, avg change −0.13%,
median −0.24%. Technology group **Change −0.49%**. So **price breadth is
mildly negative while five-day flow is strongly positive** — a divergence
worth flagging: money is being committed in options faster than it is showing
up in prices. It colors but does not override the `aligned` verdict.

**`fz` group valuation (advisory):** Technology **P/E 34.31, Fwd P/E 24.94,
PEG 0.88** — **the lowest PEG of all eleven sectors**, versus Industrials 1.96,
Healthcare 2.07, Real Estate 3.03. Technology is the cheapest sector relative
to its growth rate. FSLR's own P/E is **13.01** (`fz screen --view overview`,
`phase-0.5-context.md`) — **62% below its sector**.

### Cross-name correlation

`ls research/*/2026-07-31/` returns **only `research/FSLR/2026-07-31/`**.

`uw risk portfolio-correlation --symbols FSLR --lookback-days 30` was run and
returned:

```json
{"tickers_analyzed":1,"high_correlations":null,
 "sector_breakdown":{"Unknown":1},"sector_concentration":"100% in top sector",
 "ticker_details":[{"symbol":"FSLR","sector":"Unknown","industry":"Unknown"}],
 "warnings":["CONCENTRATION: 100% of tickers in Unknown"]}
```

**No concurrent positions to correlate against** — FSLR is the only blueprint
for this date, so the correlation gate does not apply. The
`"CONCENTRATION: 100% in Unknown"` warning is an artifact of a single-symbol
call plus the tool's known broken `sector` field (it returns `"Unknown"`
rather than `Technology`); **the coefficient machinery itself is unaffected**
and there were no pairs to compute.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Solar/Tech |
|-----------|--------------|--------------|--------|----------------------|
| FOMC decision | Hold 3.50–3.75%, 9–3, **3 hawkish dissents** | 2026-07-29 | WebSearch:federalreserve.gov | **HEADWIND** |
| 10y Treasury | **4.68%** (+24bp/30d) | 2026-07-30 | FRED `DGS10` | **HEADWIND** (strongest) |
| 2s10s spread | +0.47 (steepening) | 2026-07-31 | FRED `T10Y2Y` | HEADWIND |
| Core PCE YoY | **+3.29%** | 2026-06 | FRED `PCEPILFE` | HEADWIND |
| Core CPI YoY | +2.57% | 2026-06 | FRED `CPILFESL` | neutral |
| Headline CPI YoY | +3.46% (MoM −0.42%) | 2026-06 | FRED `CPIAUCSL` | neutral |
| Nonfarm payrolls | **+57k** (from +129k) | 2026-06 | FRED `PAYEMS` | mildly TAILWIND (eases Fed) |
| Unemployment | 4.2% (from 4.3%) | 2026-06 | FRED `UNRATE` | neutral |
| Fed funds effective | 3.63% | 2026-07-30 | FRED `DFF` | neutral |
| Broad USD | 120.71 (−0.6%/30d) | 2026-07-24 | FRED `DTWEXBGS` | mildly TAILWIND |
| ISM Manufacturing | 53.8 (miss vs 54.3) | 2026-07 | WebSearch:tradingeconomics.com | neutral |
| ISM Services | 54.0 | 2026-06 | WebSearch:seekingalpha.com | neutral |
| U-Mich sentiment | **55.2** (from 49.5) | 2026-07-31 | WebSearch:cnbc.com | neutral (utility-scale) |
| Market regime | **TRANSITIONAL, "half size"** | 2026-07-31 | UW | **HEADWIND** |
| Market breadth | **34.1% bullish** (2,142/4,138) | 2026-07-31 | UW | HEADWIND |
| S&P breadth (price) | 43.94% green, median −0.24% | 2026-08-01 | `fz` EOD | mildly HEADWIND |
| Tech 5d directional flow | **+$839.5M**, 4 of 5 days positive | 2026-07-27→31 | UW + DUCKDB | **TAILWIND** |
| Tech PEG | **0.88 — lowest of 11 sectors** | 2026-08-01 | `fz` EOD | TAILWIND |
| **Section 45X credits** | **Preserved to 2032; $2.10–2.19B for FSLR in 2026** | 2026 | WebSearch:novoco.com | **MAJOR TAILWIND** |
| **45Y/48E phaseout** | **Construction start after 2026-07-04 excluded** | 2026-07-04 | WebSearch:novoco.com | **MAJOR HEADWIND** |
| IEEPA tariff benefit | **+$89M** in Q2 GM | 2026-07-30 | WebSearch:kavout.com | TAILWIND (realized) |
| Section 301 tariffs | Assumed H2; net −$60–80M FY | 2026-07-30 | WebSearch | mild HEADWIND |
| FSLR Q2 EPS | **$3.92 vs $2.86 est (+37%)** | 2026-07-30 | WebSearch:gurufocus.com | **TAILWIND** |
| FSLR backlog | 45.1 GW through 2030 | 2026-07-30 | WebSearch:quiverquant.com | TAILWIND |
| FSLR revenue | $1.06B, **−4% YoY** | 2026-07-30 | WebSearch:quiverquant.com | HEADWIND |
| FSLR cash | **$1.7B from $2.4B** | 2026-06-30 | WebSearch:quiverquant.com | HEADWIND |

**Tally: 8 headwinds, 7 tailwinds, 8 neutral** — with the two largest items on
each side (45X vs 45Y/48E) being sector-policy, not macro.

## Catalyst calendar (next 30 days)

**Front-expiry implied move: ±0.76% / $1.61** (`implied_move` 1.611,
`implied_move_perc` 0.0076247) `[CTX:implied_move_pct]`. **This is a
post-earnings reading and contains no event premium** — phase-4 confirmed
`front-end-iv-ratio` **FLAT at 1.001**, so the options market prices **no
scheduled catalyst inside the next 30 days**. A 21-day 1σ move is roughly
**√21 × 0.76% ≈ 3.5%**.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-08-05 | **ISM Services PMI (July)** | Low — sector read-through weak | inside ±3.5% |
| ~2026-08-07 | **Nonfarm payrolls (July)** | Medium — a second sub-100k print revives cut pricing (rate-sensitive positive) | inside ±3.5% |
| **2026-08-07** | **Weekly OPEX** (P/C OI 1.503, 3,084 OI) | Low, but the most put-skewed near expiry | inside |
| ~2026-08-12 | **CPI (July)** | **Medium-high** — core is what drove 3 hawkish dissents; a hot print pushes the 10y further and hits solar directly | could exceed ±3.5% |
| **2026-08-21** | **Monthly OPEX** — 29,922 OI (13.34% of tracked), P/C 1.166, richest IV on the curve (79.6%) | **High (mechanical)** — where phase-1's 1,900-lot $230 block expires and phase-2's dealer hedge unwinds | **structural, not directional** |
| Late Aug | **Jackson Hole symposium** | Medium — the venue for signalling given the 3 dissents | could exceed ±3.5% |
| ~2026-09-16/17 | **Next FOMC** | High — but **outside the 30-day window** | n/a |
| 2026-10-29 | **FSLR Q3 earnings** | High — **outside the window** (`next_earnings_date`, phase 0.5) | n/a |

**The window is unusually clean of company-specific catalysts.** Earnings are
90 days out and no FOMC falls inside 30 days. **The dominant scheduled event
is mechanical, not fundamental: the 2026-08-21 OPEX.**

## Tool / source errors

No command errored — all UW, FRED (12/12 series) and `fz` calls exited 0 and
every payload parsed. FRED was available via **Path A** (`FRED_API_KEY`
present in the repo-root `.env`); the blocked chart-CSV path was not
attempted.

Findings that qualify the output:

1. **`uw options-flow sector-flow` and `uw risk market-regime` report opposite
   signs for Technology** (+$2.781B vs −$187.7M) because `sector-flow`'s
   `net_flow` is **call premium − put premium** while `market-regime`'s
   `sector_rotation` is **bullish − bearish premium**. Not a bug, but the
   field name invites exactly the misreading phase 0.5 made.
2. **`sector-flow-persistence`'s `persistence_score` is computed on the
   call−put metric**, which for Technology is structurally positive. Its
   `score = 1` is not evidence of directional persistence. The DuckDB
   bullish−bearish series above is the informative substitute.
3. **`uw risk portfolio-correlation` returns `sector: "Unknown"` for FSLR** —
   the known broken sector field. Coefficients are unaffected; there were
   none to compute with a single symbol.
4. **`fz breadth --group sector --agent` returns a single aggregate object**
   (`advancers`/`decliners`/`pct_green`/`top_mover`) covering `sec_all`
   (503 names), **not a per-sector table**, exactly as the phase-6 guidance
   warns. Per-sector figures came from `fz groups --by sector --view valuation`.
5. **`fz` data is EOD-stamped `2026-08-01T00:42:04Z`** — after the 2026-07-31
   close. Correct for an as-of-close read.
6. **`sector-flow-persistence` does not accept `--date`** (run without it);
   returned `dates_covered` ends 2026-07-31 = the as-of date, so the window is
   correct here but would be wrong on a historical re-run — the same
   latest-anchor defect logged in phases 1, 2 and 5.

## DATA NOTE / CORRECTION

**Correction to `phase-0.5-context.md`.** That phase wrote:
*"Technology is the most-sold sector on the options tape today by a factor of
9× the next-worst"* and handed phase 6 the question of whether this was
tech-wide de-risking or single-name distribution. It also flagged for phase 9
that FSLR's bearish premium *"may be sector beta."*

**The one-day snapshot was real but the inference was wrong.** Extended to
five sessions, Technology is **+$839.5M cumulative and positive on four of
five days** — the best sector of the week on the directional measure. Today's
−$187.7M immediately follows **+$806.6M**, the largest single-day sector
inflow of the week. `phase-5-historical.md`'s open question *"Is Beta 1.76
into the worst-performing sector an acceptable risk?"* rests on the same
mistaken premise and is **resolved**: FSLR is not in a sector being sold.

**The sector-rotation gate is therefore `aligned`, not `adverse`, and must
not cut size in phase 9.** Phase 10 should verify that phase 9 applied the
corrected verdict rather than phase-0.5's original framing.

No numbers were mis-transcribed; the correction is one of interpretation,
and it arises from measuring five sessions instead of one.

## Verdict for downstream phases

- **Net macro bias for FSLR: HEADWIND (moderate).** The rate complex is the
  binding constraint — 10y **+24bp to 4.68%**, curve steepening, core PCE
  **3.29%**, three FOMC members voting to *hike* — against a
  **capital-cost-sensitive** industry with **Beta 1.76**. The regime is
  **TRANSITIONAL** with **34.1%** bullish breadth and explicit **"half
  position sizes"** guidance. Offsetting this: sector flow is **aligned**,
  Technology has the **lowest PEG of any sector (0.88)**, FSLR trades at a
  **P/E of 13.01**, and **45X delivers ~$2.1B/yr against a $22.7B market
  cap**. **The macro does not veto a long; it caps its size and argues for
  defined risk.**
- **Conviction: 3 / 5.** The macro inputs are well-sourced, current and
  internally consistent (rates, inflation and the FOMC all say the same
  thing). Held below 4 because the two decisive drivers — 45X versus the
  45Y/48E phaseout — are **policy judgments about future demand**, not
  measurable quantities, and reasonable analysts will weigh them differently.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. **`[MACRO:DGS10_2026-07-30 FRED]` — 10y at 4.68%, +24bp in 30 days**,
     with **`[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`** three
     dissents preferring a hike. The core headwind to solar project
     economics and the reason a long here is a *tactical* trade, not a
     structural one.
  2. **`[MACRO:45X_policy WebSearch:novoco.com]` — 45X preserved through 2032,
     $2.10–2.19B expected in 2026 (~9% of market cap annually)** against
     **`[MACRO:45Y48E_phaseout WebSearch:novoco.com]`** — the credits that
     drive customer demand are phasing out for construction beginning after
     **2026-07-04**. This tension is the FSLR thesis in one line and the best
     explanation for **−19.22% YTD on a +37% EPS beat**.
- **Top 2 catalysts for phase-9's calendar:**
  1. **2026-08-21 monthly OPEX** — 29,922 OI (13.34% of tracked), P/C 1.166,
     richest IV on the curve (79.6%), where phase-1's 1,900-lot $230 block
     expires and phase-2's 72,200-share dealer hedge unwinds. **Mechanical,
     high-confidence, and the natural expiry anchor for any structure.**
  2. **~2026-08-12 CPI (July)** — core inflation is what produced the hawkish
     dissents; a hot print pushes the 10y higher and transmits directly to
     solar. **The only scheduled macro release in the window with a plausible
     move exceeding the ±3.5% 21-day 1σ.**
- **Sector-rotation verdict: `aligned`.** Technology 5-day net directional
  flow **+$839.5M**, positive 4 of 5 sessions; UW `persistence_score` 1
  (`trend: INFLOW`) on its own metric. **Caveat:** the score is computed on
  call−put premium and overstates persistence; the aligned verdict rests on
  the DuckDB directional series. **Advisory divergence:** price breadth is
  mildly negative (43.94% green, Tech −0.49%) while flow is positive.
  **No size cut from this gate.**
- **Correlation verdict: no concurrent positions.** FSLR is the only
  blueprint for 2026-07-31; `portfolio-correlation` was run with the single
  symbol and returned `high_correlations: null`, `tickers_analyzed: 1`. **No
  cluster (≥0.70), no soft-watch (0.60–0.70). Gate does not apply — no size
  cut.**
- **Additional phase-9 sizing input (not a formal gate):** `uw risk
  market-regime` `trading_guidance` reads **"Half position sizes. Favor
  defined-risk strategies. Iron condors in range."** This converges
  independently with phase-5's **PREMIUM_SELLING** verdict (VRP +0.3587) and
  phase-4's **COMPLACENT** skew. **Three phases now independently point to
  defined-risk, premium-selling structures over directional debit
  positions.**
