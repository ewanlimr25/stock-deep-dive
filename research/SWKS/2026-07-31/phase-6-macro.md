# Phase 6 — Macro Overlay

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`, `phase-4-structure.md`, `phase-5-historical.md`

## Summary

The macro backdrop is a **hawkish-hold Fed against sticky 3%+ inflation, a bear
steepener in rates, and a market the UW engine labels
`TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`** with only
**34.1% of optionable tickers bullish**. That is a headwind for a
high-multiple sector. **More importantly, this phase overturns
`phase-0.5-context.md`'s sector conclusion.** Phase 0.5 read
`options-flow sector-flow` and reported Technology **leading** the tape at
**+$2.78B**; that field is `call_premium − put_premium`. On the
**aggressor-adjusted** metric — `bullish_premium − bearish_premium`, the one
`uw risk market-regime` actually uses — **Technology was the single most net-SOLD
sector on the as-of date at −$187,715,752**, the largest outflow of all eleven.
SWKS's own RF/analog sub-cohort has been net-sold on **4 of the last 5 sessions**
(−$12.5M cumulative). **And the dominant fact for this name is not macro at all:
SWKS is a live merger-arb underlying.** Its 2026-07-28 print beat on revenue
($935M) and non-GAAP EPS ($1.08 vs $1.03 guided) but **eliminated the dividend
outright** — a 4.56% TTM yield — announced a **~$2B debt raise** to fund the Qorvo
cash consideration, and disclosed that **China's SAMR moved the review to Phase
III (final)**. That, not Apple, is why the stock fell 5.4%.

## Key signals

- **Market regime: `TRANSITIONAL — Mixed signals, reduce position size, wait for
  clarity`**; `trading_guidance`: *"Half position sizes. Favor defined-risk
  strategies. Iron condors in range."* Breadth **34.1% bullish** (2,142 bullish vs
  4,138 bearish of 6,280 optionable). `[MACRO:MarketRegime_2026-07-31 UW]`
- **Technology is the largest net-SOLD sector on an aggressor-adjusted basis:
  −$187,715,752** — the biggest outflow of eleven sectors, per
  `market-regime.sector_rotation.money_flowing_out`. **This contradicts the
  `sector-flow` reading carried in `phase-0.5-context.md`**; both are correct
  measurements of different quantities (see §Sector rotation). `[MACRO:MarketRegime_2026-07-31 UW]`
- **★ SWKS is a merger-arb underlying.** Qorvo holders receive **0.960 SWKS shares
  + $32.50 cash**; **China SAMR review is in Phase III (final)**; management is
  *"optimistic they can close within the calendar year,"* against formal guidance of
  early calendar 2027. Synergies guided at **$500M+**.
  `[MACRO:SWKS_QRVO_merger_2026-07-28 WebSearch:stocktitan.net]`
- **★ The dividend was eliminated** and **~$2B of new debt** announced to fund the
  cash leg, alongside a **$2B buyback**. `phase-0-intake.md` snapshotted the prior
  yield at **Dividend TTM 2.84 (4.56%)** with **Payout 91.35%** — that entire
  income-holder base is now structurally misaligned.
  `[MACRO:SWKS_dividend_elimination_2026-07-28 WebSearch:chartmill.com]`
- **Inflation is still ~1.3–1.7pts above target and the Fed is hawkish-hold.** June
  CPI **+3.46% YoY**, Core PCE **+3.29% YoY**; FOMC held 3.50–3.75% on 2026-07-29
  **9–3, with all three dissenters wanting a HIKE**. `[MACRO:CPIAUCSL_2026-06 FRED]` `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`
- **Bear steepener:** DGS10 **4.44 → 4.68 (+24bp in a month)**, DGS2 4.14 → 4.23
  (+9bp), T10Y2Y **+0.31 → +0.47** (normal, steepening). Rising long rates compress
  long-duration equity multiples. `[MACRO:DGS10_2026-07-30 FRED]` `[MACRO:T10Y2Y_2026-07-31 FRED]`
- **No correlation gate fires:** `SWKS/FSLR` pairwise **0.518** — below both the
  0.70 cluster threshold and the 0.60 soft-watch band. `[MACRO:PortfolioCorrelation_2026-07-31 UW]`

## Detailed findings

### Market regime (UW: SPY + breadth)

`uw risk market-regime --date 2026-07-31`:

| Field | Value |
|---|---|
| **`regime`** | **`TRANSITIONAL — Mixed signals, reduce position size, wait for clarity`** |
| `trend` | `UPTREND` |
| `trading_guidance` | *"Half position sizes. Favor defined-risk strategies. Iron condors in range."* |
| `spy.current` | **747.03** |
| `spy.sma_20` / `sma_50` | 745.69 / 744.99 |
| `spy.above_20sma` / `above_50sma` | **true / true** |
| `spy.change_30d_pct` | **+0.17%** |
| `spy.pct_from_90d_high` | **−1.76%** |
| `market_breadth.bullish_flow_tickers` | **2,142** |
| `market_breadth.bearish_flow_tickers` | **4,138** |
| **`market_breadth.bullish_pct`** | **34.1%** |
| `market_breadth.tickers_with_options` | 6,280 |

**The index is fine; the tape underneath is not.** SPY sits above both moving
averages and 1.76% off its 90-day high, but has gone **nowhere in 30 days
(+0.17%)** while **only one ticker in three shows bullish flow**. That divergence
is what produces the `TRANSITIONAL` label. The engine's own guidance —
**half position sizes, defined risk** — is a direct input to phase 9 and should be
applied as written.

Independent corroboration from `fz` (advisory, EOD, `captured_at`
2026-08-02T17:06:45Z reflecting the 2026-07-31 close):
`advancers` **221** vs `decliners` **281** of 503 S&P 500 names, `pct_green`
**43.94%**, `avg_change` **−0.13%**, `median_change` **−0.24%**, `top_mover`
**AMZN +15.32%**, `worst_mover` GDDY −16.70%.
`[MACRO:sector_breadth fz EOD]` — a narrow, mega-cap-carried tape: the median S&P
name was **down**, and the index was held up by one 15% mover. This is the same
picture the UW breadth reading gives from the options side.

### Inflation (FRED)

| Series | 2026-06 | 2026-05 | 2026-04 | 12mo ago (2025-06) | **YoY** |
|---|---|---|---|---|---|
| `CPIAUCSL` (CPI, all urban) | 332.568 | 333.979 | 332.407 | 321.435 | **+3.46%** |
| `CPILFESL` (Core CPI) | 336.065 | 336.121 | 335.423 | 327.658 | **+2.57%** |
| `PCEPI` (PCE) | 131.392 | 131.535 | 130.932 | 126.743 | **+3.67%** |
| `PCEPILFE` (Core PCE) | 130.266 | 130.094 | 129.663 | 126.121 | **+3.29%** |

`[MACRO:CPIAUCSL_2026-06 FRED]` `[MACRO:CPILFESL_2026-06 FRED]` `[MACRO:PCEPI_2026-06 FRED]` `[MACRO:PCEPILFE_2026-06 FRED]`

Headline CPI **fell month-over-month** (333.979 → 332.568, −0.42%) and headline PCE
likewise (131.535 → 131.392) — but **core is not cooperating**: Core CPI is flat
(336.121 → 336.065) and **Core PCE rose** (130.094 → 130.266). At **+3.29% YoY core
PCE** the Fed remains **~1.3 points above its 2% target**, which the FOMC statement
below shows is now a five-year overshoot. **Headwind** for rate-sensitive,
long-duration equity.

### Labor (FRED)

| Series | 2026-06 | 2026-05 | 2026-04 | 12mo ago |
|---|---|---|---|---|
| `PAYEMS` (thousands) | **158,984** | 158,927 | 158,798 | 158,478 |
| MoM Δ | **+57k** | +129k | — | — |
| `UNRATE` | **4.2%** | 4.3% | 4.3% | 4.1% |

`[MACRO:PAYEMS_2026-06 FRED]` `[MACRO:UNRATE_2026-06 FRED]`

Payroll growth has **decelerated to +57k** in June from +129k in May, and the
trailing 12-month total is **+506k (~42k/month)** — historically weak. Unemployment
**ticked down to 4.2%** from 4.3%, but is **above** the 4.1% of a year ago. A
cooling-but-not-breaking labour market: it removes the case for a hike without
supplying a case for cuts. **Neutral-to-mildly-tailwind** (it caps the hawkish
dissent) for a growth sector.

### Rates (FOMC, FRED)

**FOMC, 2026-07-28/29** `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov, cnbc.com]`:
- **Held at 3.50%–3.75% for the fifth consecutive meeting**, vote **9–3**.
- **All three dissenters — Hammack (Cleveland), Kashkari (Minneapolis), Logan
  (Dallas) — preferred to RAISE by ¼ point**, citing inflation above target for
  more than five years.
- Statement: economic activity expanding at a solid pace amid elevated uncertainty
  "owing in part to the conflict in the Middle East"; productivity and capital
  investment strong; job gains keeping pace.
- **Most officials now see end-2026 between 3.6% and 4.1%** — i.e. the central
  expectation includes **a hike**, not a cut.

| Series | Latest | 30d ago | Δ |
|---|---|---|---|
| `DFF` (fed funds effective) | **3.63** (2026-07-30) | 3.62 (2026-07-09) | +1bp |
| `SOFR` | 3.65 (2026-07-30) | 3.68 (2026-06-30) | −3bp |
| **`DGS10`** | **4.68** (2026-07-30) | 4.44 (2026-06-30) | **+24bp** |
| `DGS2` | 4.23 (2026-07-30) | 4.14 (2026-06-30) | +9bp |
| **`T10Y2Y`** | **+0.47** (2026-07-31) | +0.31 (2026-07-01) | **+16bp** |
| `DTWEXBGS` (broad USD) | 120.71 (2026-07-24) | 121.41 (2026-06-24) | −0.6% |

`[MACRO:DFF_2026-07-30 FRED]` `[MACRO:DGS10_2026-07-30 FRED]` `[MACRO:DGS2_2026-07-30 FRED]` `[MACRO:T10Y2Y_2026-07-31 FRED]` `[MACRO:DTWEXBGS_2026-07-24 FRED]` `[MACRO:SOFR_2026-07-30 FRED]`

**A classic bear steepener:** the long end rose 24bp while the front end barely
moved, steepening 2s10s to **+0.47** (comfortably **normal**, not inverted). Two
consequences for SWKS specifically:

1. **Multiple compression risk** for a 34.3× trailing-P/E sector (see below).
2. **★ Direct, company-specific cost.** SWKS announced a **~$2B debt raise** to
   fund the Qorvo cash consideration. A 24bp rise in the 10-year over the month
   preceding that raise is a **measurable headwind to the deal's financing cost**,
   and it is one of the few macro variables that transmits to this name mechanically
   rather than through sentiment. **Headwind, and unusually direct.**

The **weaker dollar** (−0.6% m/m) is a modest **tailwind** — SWKS books the large
majority of revenue overseas.

### Activity (ISM)

`[MACRO:ISM_Mfg_2026-06 WebSearch:prnewswire.com]` `[MACRO:ISM_Svcs_2026-06 WebSearch:ismworld.org]`

| Indicator | Jun 2026 | May 2026 | Read |
|---|---|---|---|
| ISM Manufacturing PMI | **53.3** | 54.0 | Expansion, 20th consecutive month; **decelerating (−0.7)** |
| ISM Services PMI | **54.0** | 54.5 | Expansion, 24th consecutive month; **decelerating (−0.5)** |

Both are **above 50 but rolling over**. **The July prints were NOT available as of
the 2026-07-31 as-of date** — ISM Manufacturing releases on the first business day
(**2026-08-03**) and Services on the third (**2026-08-05**). Both therefore land
**inside the next 30 days** and appear in the catalyst calendar. Net: expansion
intact, momentum fading. **Neutral-to-mild-headwind** for semis.

### Consumer

`[MACRO:UMich_2026-07 WebSearch:news.umich.edu]` `[MACRO:ConfBoard_2026-07-28 WebSearch:advisorperspectives.com]`

| Indicator | Jul 2026 | Jun 2026 | Jul 2025 |
|---|---|---|---|
| U-Michigan Consumer Sentiment | **55.2** | 49.5 | 61.7 |
| — Current Index | 54.8 | 47.7 | 68.0 |
| — Expectations Index | 55.4 | 50.7 | 57.7 |
| Conference Board Confidence | **90.8** | 92.2 (rev.) | — |
| — Present Situation | **114.9** (3rd consecutive decline) | 118.5 | — |
| — Expectations | 74.7 | 74.7 | — |

**The two series diverge, and the divergence matters for a handset-exposed name.**
U-Mich jumped 5.7 points to a five-month high on **falling gasoline prices** — but
is still **10.5% below** its year-ago level and near record lows in absolute terms.
Conference Board **fell** 1.4 points, with the labour-sensitive Present Situation
index down for a **third straight month**. Michigan tracks household finances and
inflation; the Conference Board tracks jobs. **Cheaper gas is lifting mood while the
job picture erodes.**

For SWKS this is a **headwind**: RF front-end content is levered to **smartphone
unit demand**, which is a discretionary, labour-sensitive purchase. A Present
Situation index falling for three months is the more relevant of the two series,
and it is going the wrong way.

### Sector overlay — semiconductors, and the merger

**★ The company-specific catalyst dominates every macro variable in this phase.**

SWKS reported **Q3 FY2026 on 2026-07-28 postmarket** (independently verified in
`phase-0.5-context.md` from the screener's `next_earnings_date` roll):

| Item | Reported | Consensus / guide |
|---|---|---|
| Revenue | **$935M** | $900–950M guided range — **beat** |
| Non-GAAP diluted EPS | **$1.08** | $1.03 guided midpoint — **beat** |
| GAAP operating income | $49M | |
| Non-GAAP operating income | $182M | |
| GAAP diluted EPS | $0.22 | |
| **Q4 FY26 revenue guide** | **$1.010–1.060B** | |
| **Q4 FY26 non-GAAP EPS guide** | **$1.27 midpoint** | consensus **$1.29** — **slight miss** |
| Q4 gross margin guide | **44–45%** | down from ~44.5–45.5%, on mobile mix + input-cost inflation |

CEO Phil Brace: *"We delivered a solid quarter with revenue and earnings above
expectations, reflecting consistent execution across the portfolio."* Mobile
performed well; Broad Markets grew YoY led by double-digit gains in automotive and
data center. `[MACRO:SWKS_Q3FY26_2026-07-28 WebSearch:globenewswire.com]`

**The stock fell −5.40% the next session anyway. The reasons are structural, not
operational** `[MACRO:SWKS_selloff_2026-07-29 WebSearch:investing.com, chartmill.com]`:

1. **★ The quarterly dividend was ELIMINATED outright**, tied to capital
   reallocation ahead of the Qorvo combination. `phase-0-intake.md` snapshotted
   **Dividend TTM 2.84 (4.56%)**, **Dividend Est. 2.48 (3.99%)**, **Payout
   91.35%** — SWKS was, until that evening, a ~4.5% yielder held substantially by
   income mandates. **Those holders are now forced sellers on a mandate basis, not
   a view basis.**
2. **~$2B of new debt** to fund the cash leg of the merger — a material leverage
   step-up on a $9.4B market cap, into a 10-year yield that rose 24bp over the
   month.
3. **China SAMR moved the Qorvo review to Phase III**, the final phase — progress,
   but Phase III is also where a deal either clears or gets conditioned.

**Merger terms** `[MACRO:SWKS_QRVO_terms_2026 WebSearch:sec.gov Form 425, stocktitan.net]`:
- Each QRVO share converts into **0.960 SWKS shares + $32.50 cash**.
- Synergies guided **$500M+**.
- Formal guidance: close **early calendar 2027**; management now *"optimistic"* about
  **late calendar 2026**, possibly by fiscal year-end (**late September 2026**).
- Offsetting bid: a **$2B share repurchase program** was authorised.

**Arithmetic on the as-of closes** (derived from validated screener values in
`phase-0.5-context.md`: SWKS 62.28, QRVO 90.57):

```
Deal value per QRVO share = 0.960 × 62.28 + 32.50 = 59.79 + 32.50 = $92.29
QRVO market price                                                = $90.57
Gross spread                                       = $1.72  =  1.86%
```

**A 1.86% gross spread implies the market assigns a high probability to the deal
closing.** Three consequences that every downstream phase must carry:

1. **SWKS now trades with a structural short from merger arbitrageurs.** The
   standard arb is long QRVO / **short 0.960 SWKS**. That is a persistent,
   price-insensitive supply of SWKS stock for as long as the deal is live — and it
   is a compelling alternative explanation for `phase-2-dark-pool.md`'s finding
   that dark-pool prints were **balanced-to-selling on the as-of day (buy_ratio
   0.461)** even as the shares were being absorbed on the two sessions prior.
2. **SWKS's price is now partly a function of QRVO's**, not purely its own
   fundamentals. This is a **regime change in what drives the stock**, and it
   post-dates every historical relationship phase 5 measured.
3. **Deal break is the tail risk that dominates everything else.** If SAMR blocks or
   heavily conditions the deal, the arb short covers (a violent upward squeeze in
   SWKS) while the standalone story loses $500M of guided synergies and carries $2B
   of debt raised for a transaction that will not happen. **Directionally ambiguous
   and very large** — precisely the kind of binary that
   `phase-4-structure.md`'s short-gamma regime would amplify.

**Apple read-through, re-assessed.** `phase-0.5-context.md` flagged AAPL's −7.35%
on the as-of date as a yellow flag. With the merger context, the ranking inverts:
**SWKS fell only −0.32% on the day its largest customer dropped 7.35%.** That is
not complacency — it is a stock whose price is now anchored by an arb ratio and a
$2B buyback authorisation, and which had **already** taken its own −5.40% hit two
sessions earlier. It also explains `phase-4-structure.md`'s otherwise-puzzling
finding that **25Δ put skew stayed NORMAL (1.042)** on that day.

### Sector rotation — **and a correction to phase 0.5**

`uw options-flow sector-flow --date 2026-07-31` (`net_flow` = call − put premium):
Technology **+$2,781,021,293**, ranked **1st of 11** — the figure
`phase-0.5-context.md` carried.

`uw risk market-regime --date 2026-07-31` (`sector_rotation`, aggressor-adjusted):

| Money flowing IN | | Money flowing OUT | |
|---|---|---|---|
| Consumer Cyclical | +$86,432,084 | **Technology** | **−$187,715,752** |
| Communication Services | +$38,048,537 | Industrials | −$20,923,260 |
| Consumer Defensive | +$3,916,924 | Financial Services | −$17,918,655 |

**These two are not in conflict — they measure different things, and the
distinction was verified rather than assumed.** Recomputing both metrics from the
2026-07-31 screener parquet (`is_index = false`):

| Sector | Σ(call − put premium) | Σ(bullish − bearish premium) |
|---|---|---|
| **Technology** | **+$2,823,293,867** | **−$187,715,752** |
| Consumer Cyclical | +$1,844,965,590 | +$86,432,084 |
| Communication Services | +$712,892,713 | +$38,048,537 |
| Financial Services | +$499,594,693 | −$17,918,655 |
| Industrials | −$103,002,789 | −$20,923,260 |
| Healthcare | +$79,476,645 | −$5,855,170 |

The parquet's aggressor-adjusted column **reproduces `market-regime`'s numbers
exactly** (Technology −187,715,752 ✓, Consumer Cyclical +86,432,084 ✓,
Communication Services +38,048,537 ✓). So:

- `sector-flow.net_flow` = **calls minus puts**, blind to who initiated. Technology
  is call-heavy because Technology is where the options volume is.
- `market-regime.sector_rotation` = **bullish minus bearish premium**, i.e.
  aggressor-adjusted. On this measure **Technology was the single most net-SOLD
  sector on 2026-07-31.**

**The aggressor-adjusted read is the meaningful one for direction** — it is the
same distinction `phase-1-flow.md` had to make at the single-name level, where the
call-heavy tape turned out to be a **selling** tape. **`phase-0.5-context.md`'s
"Technology is LEADING the tape" is hereby corrected to "Technology is call-heavy
but was the largest net-SOLD sector on the as-of date."** Recorded for phase 10.

`uw options-flow sector-flow-persistence --days 5` (`dates_covered` 2026-07-27 →
2026-07-31) reports Technology `persistence_score` **1.0**, `trend` **INFLOW** — but
on the **call−put** metric (its 2026-07-31 value of 2,781,021,293 matches
`sector-flow` exactly). Recomputed on the aggressor-adjusted metric:

| Date | Tech Σ(bull−bear) | Tech Σ(call−put) |
|---|---|---|
| 2026-07-27 | +$21.0M | +$373.7M |
| 2026-07-28 | +$143.6M | −$43.6M |
| 2026-07-29 | +$56.0M | +$235.3M |
| 2026-07-30 | +$806.6M | +$2,473.2M |
| **2026-07-31** | **−$187.7M** | +$2,823.3M |

**Aggressor-adjusted persistence = 0.8 INFLOW, broken on the as-of session** — and
broken hard, by the largest single-day outflow in the window. The sector had been
bought for four sessions; on the day Apple reported, it was sold.

**SWKS's actual sub-cohort is worse.** RF/analog (SWKS, QRVO, QCOM, NXPI, MCHP,
ADI, TXN), Σ(bullish − bearish):

| Date | RF/analog net |
|---|---|
| 2026-07-27 | −$8.01M |
| 2026-07-28 | −$5.26M |
| 2026-07-29 | −$1.15M |
| 2026-07-30 | +$8.05M |
| **2026-07-31** | **−$6.14M** |

**Net −$12.51M over five sessions, negative on 4 of 5.** Persistently out of favour
while the broader Technology sector was being bought — exactly the bifurcation
`phase-0.5-context.md` observed on price (MPWR +8.35%, AVGO +0.37% vs QCOM −2.63%,
NXPI −6.53%).

**`fz` valuation cross-check** (advisory, EOD 2026-07-31 close)
`[MACRO:group_valuation fz EOD]`:

| Group | Change | P/E | Fwd P/E | PEG | EPS next 5Y |
|---|---|---|---|---|---|
| **Technology (sector)** | **−0.49%** | **34.31** | 24.94 | **0.88** | 38.89% |
| **Semiconductors (industry)** | **+0.25%** | **34.28** | **28.75** | **0.56** | — |
| Semiconductor Equip. & Materials | −0.18% | 50.37 | 27.39 | 1.47 | — |
| Consumer Cyclical | +4.42% | 25.86 | 20.83 | 1.32 | 19.59% |
| Communication Services | +3.59% | 30.29 | 30.02 | 1.68 | 18.08% |

Semis closed **+0.25% — green on price while being net-sold on flow.** That is a
**divergence, not corroboration**, and it colors the rotation verdict toward
"contested" rather than "cleanly adverse." Note the Semiconductors industry PEG of
**0.56** is the cheapest growth-adjusted multiple in the table — cheapness is not
the sector's problem; **flow is**. Advisory only; does not set the macro bias.

**Rotation verdict: ADVERSE.** Aggressor-adjusted Technology flow is the largest
outflow of eleven sectors on the as-of date, aggressor-adjusted persistence broke
on that same session (0.8, sign-flipped), and SWKS's own RF/analog cohort has been
net-sold on 4 of the last 5 sessions. Against a **long** thesis this is **adverse**.
The `fz` price-breadth divergence (semis +0.25%) is noted and prevents this from
being scored as *strongly* adverse.

### Cross-name correlation

**Concurrent blueprints for 2026-07-31** (`ls -d research/*/2026-07-31/`):
`research/FSLR/2026-07-31/` and `research/SWKS/2026-07-31/`. One sibling position
exists, so the gate applies.

`uw risk portfolio-correlation --symbols SWKS,FSLR --lookback-days 30`:

| Pair | Correlation | Tool `warning` |
|---|---|---|
| **SWKS / FSLR** | **0.518** | `MODERATE` |

Additional tool output: `tickers_analyzed` 2; `sector_concentration` *"100% in top
sector"*; `warnings` *["CONCENTRATION: 100% of tickers in Unknown"]*.

**Both concentration warnings are spurious and are discarded**: the tool returned
`sector: "Unknown"`, `industry: "Unknown"` for **both** symbols
(`ticker_details[]`), so "100% in top sector" simply means "100% in the Unknown
bucket." The sector field is a known-broken field in this engine. Independently,
SWKS is Technology/Semiconductors and FSLR is Technology/Solar per the screener
parquet — related but not the same industry.

**Correlation verdict: NO GATE.** 0.518 sits **below the 0.60 soft-watch band** and
well below the 0.70 cluster threshold. No phase-9 size cut is warranted on
correlation grounds. Worth one line of context: 0.518 over 30 sessions is
meaningful but ordinary for two Technology-sector names in a period when the sector
moved together; a merger-arb-anchored SWKS should, if anything, **decorrelate
further** from the sector as the spread tightens.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Technology / RF-semis |
|---|---|---|---|---|
| **SWKS dividend elimination** | **suspended** (was 4.56% TTM) | 2026-07-28 | WebSearch:chartmill.com | **HEADWIND (severe, company-specific)** — forced income-mandate selling |
| **Qorvo merger, SAMR Phase III** | 0.960 SWKS + $32.50 cash; close late-2026/early-2027 | 2026-07-28 | WebSearch:sec.gov 425 | **HEADWIND (arb short) + binary tail** |
| **$2B debt raise for merger** | ~$2B, near-term | 2026-07-28 | WebSearch:seekingalpha.com | **HEADWIND** — leverage into a +24bp 10y |
| **$2B buyback authorised** | $2B | 2026-07-28 | WebSearch:globenewswire.com | **TAILWIND** — partial offset to arb supply |
| Q3 FY26 revenue / EPS | $935M / $1.08 non-GAAP | 2026-07-28 | WebSearch:globenewswire.com | **TAILWIND (mild)** — beat both |
| Q4 FY26 EPS guide | $1.27 mid vs $1.29 cons. | 2026-07-28 | WebSearch:investing.com | **HEADWIND (mild)** — slight miss; GM to 44–45% |
| **Market regime** | `TRANSITIONAL`, breadth 34.1% bullish | 2026-07-31 | UW | **HEADWIND** — half-size guidance |
| **Tech sector flow (aggressor-adj.)** | **−$187.7M**, largest outflow of 11 | 2026-07-31 | UW | **HEADWIND** |
| RF/analog cohort flow, 5d | −$12.51M, negative 4 of 5 sessions | 2026-07-27→31 | UW/DuckDB | **HEADWIND** |
| Semis industry price/valuation | +0.25%, PEG 0.56, Fwd P/E 28.75 | 2026-07-31 | `fz` EOD | **NEUTRAL** — cheap on growth, green on price |
| **FOMC** | Hold 3.50–3.75%, **9–3, 3 dissents to HIKE** | 2026-07-29 | WebSearch:federalreserve.gov | **HEADWIND** |
| Core PCE YoY | **+3.29%** | 2026-06 | FRED `PCEPILFE` | **HEADWIND** |
| CPI YoY | **+3.46%** (headline −0.42% MoM) | 2026-06 | FRED `CPIAUCSL` | **HEADWIND** (mixed: MoM cooling) |
| Core CPI YoY | +2.57% | 2026-06 | FRED `CPILFESL` | **NEUTRAL** |
| **10y yield** | **4.68%, +24bp m/m** | 2026-07-30 | FRED `DGS10` | **HEADWIND** — multiple + financing cost |
| 2s10s spread | **+0.47**, steepening, normal | 2026-07-31 | FRED `T10Y2Y` | **NEUTRAL** — no recession signal |
| Fed funds effective | 3.63% | 2026-07-30 | FRED `DFF` | **NEUTRAL** — anchored |
| Broad USD | 120.71, **−0.6% m/m** | 2026-07-24 | FRED `DTWEXBGS` | **TAILWIND (mild)** — majority-overseas revenue |
| Nonfarm payrolls | **+57k** MoM (May +129k) | 2026-06 | FRED `PAYEMS` | **NEUTRAL** — cooling caps hike risk |
| Unemployment | 4.2% (from 4.3%) | 2026-06 | FRED `UNRATE` | **NEUTRAL** |
| ISM Manufacturing PMI | **53.3** (from 54.0) | 2026-06 | WebSearch:prnewswire.com | **NEUTRAL** — expanding, decelerating |
| ISM Services PMI | **54.0** (from 54.5) | 2026-06 | WebSearch:ismworld.org | **NEUTRAL** — expanding, decelerating |
| U-Mich Sentiment | **55.2** (from 49.5; 61.7 y/y) | 2026-07 | WebSearch:news.umich.edu | **TAILWIND (mild)** — 5-month high on gas |
| Conf. Board Confidence | **90.8** (from 92.2); Present Situation **114.9, 3rd decline** | 2026-07-28 | WebSearch:advisorperspectives.com | **HEADWIND** — handset demand is labour-sensitive |

**Tally: 8 headwinds (2 severe and company-specific), 4 tailwinds (1 material),
8 neutral.** The macro overlay is **net headwind**, and the two heaviest items are
not macro at all.

## Catalyst calendar (next 30 days)

**Front-expiry implied move: ±9.10% / ±$5.67** on a $62.28 close
(`implied_move` 5.674921, `implied_move_perc` 0.0909807 — `[CTX:implied_move]`,
`phase-0.5-context.md`). Every binary below is read against that priced range.
Equivalent band: **$56.61 – $67.95**.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-08-03** (Mon) | **ISM Manufacturing PMI (July)** — 1st business day | Sector-wide risk tone; semis are cycle-levered | **Inside** ±9.10% |
| **2026-08-05** (Wed) | **ISM Services PMI (July)** — 3rd business day | Broad risk tone | **Inside** |
| ~**2026-08-07** (Fri) | **July employment report** (first Friday; date not independently verified) | Rate path; Conf. Board Present Situation already falling 3 months | **Inside** |
| ~**mid-August** | **July CPI** (typical ~12th; date not independently verified) | Direct on the 3-dissent hike debate | **Inside**, unless a large upside surprise |
| **Undated — any day** | **★ China SAMR Phase III decision on Qorvo** | **BINARY.** Approve ⇒ spread collapses, arb short covers. Block/condition ⇒ deal breaks, $500M synergies gone, $2B debt stranded, but arb short covers violently | **★ CAN EXCEED ±9.10% in either direction** — the only event on the board that can |
| **Undated — "near term"** | **★ ~$2B debt raise pricing** | Confirms leverage step-up; pricing vs a 4.68% 10y is the tell | Inside, but a re-rate risk |
| **2026-08-21** (Fri) | **OPEX — the 61.87% tracked-OI cliff**, max pain **$65.00** (+4.23%) | Pin/gravity; `phase-3-positioning.md`, `phase-4-structure.md` | **Well inside** ±9.10% |
| **2026-09-16/17** *(just outside 30d)* | Next FOMC | End-2026 dots span **3.6–4.1%** — a hike is in the central expectation | — |
| **2026-10-27** *(outside 30d)* | **SWKS FQ4 earnings** — verified, not stale (`phase-0.5-context.md`) | — | **No earnings risk inside a 1–8 week horizon** |

**Read:** the four scheduled macro prints all sit comfortably **inside** the priced
±9.10%. **Only the SAMR decision can exceed it**, it is **undated**, and it is
**directionally ambiguous** (approval compresses the arb spread and releases the
short; a block breaks the deal but also forces the short to cover). Phase 9 must
treat it as an **unhedgeable, two-sided, unscheduled binary** — which is a strong
argument for **defined-risk structures**, exactly as the UW regime engine's own
`trading_guidance` states.

## Tool / source errors

- `uw risk portfolio-correlation` returned `sector: "Unknown"` and
  `industry: "Unknown"` for **both** SWKS and FSLR, producing the spurious warnings
  `"CONCENTRATION: 100% of tickers in Unknown"` and
  `sector_concentration: "100% in top sector"`. This is the **known-broken sector
  field** in this engine. The **correlation coefficient itself (0.518) is
  unaffected and is used**; both concentration warnings are discarded.
- **ISM July prints unavailable at the as-of date.** ISM Manufacturing (July)
  releases 2026-08-03 and Services 2026-08-05 — **after** 2026-07-31. June figures
  are quoted, correctly labelled by their own release period. No July value was
  invented.
- **No paid source was accessed.** FRED was reached via the free JSON API with a
  key sourced from the repo-root `.env`; the blocked public chart-CSV endpoints were
  not attempted. All non-FRED macro came from WebSearch on public reporting.
- `fz` remains **DEGRADED** per `phase-0-intake.md` (14 of 84 quote fields), but the
  `breadth` and `groups` leaves used in this phase returned **complete, valid
  JSON** — the degradation is confined to `fz quote`.
- No `uw` command errored in this phase.

## DATA NOTE / CORRECTION

1. **★ Correcting `phase-0.5-context.md`'s sector verdict.** Phase 0.5 stated
   *"Technology is LEADING the tape (+$2.78B net, 1st of 11)."* That figure is
   `sector-flow`'s `net_flow` = **call premium − put premium**, which is blind to
   aggressor side. On the **aggressor-adjusted** metric that
   `uw risk market-regime` uses, **Technology was the largest net-SOLD sector on
   2026-07-31 at −$187,715,752**. Both numbers were re-derived from the
   2026-07-31 screener parquet and the aggressor-adjusted column **reproduces the
   `market-regime` output exactly** across all eleven sectors, confirming the
   field semantics rather than assuming them. **Corrected verdict: Technology is
   call-heavy but was being sold.** Phase 0.5's underlying observation — that
   SWKS's RF/analog sub-cohort was lagging — was **right**, and is now shown to
   have been true of the whole sector on that session.
2. **`sector-flow-persistence`'s `persistence_score: 1.0 / INFLOW` for Technology
   is measured on the call−put metric** (verified: its 2026-07-31 value
   2,781,021,293 equals `sector-flow`'s exactly). Recomputed on the
   aggressor-adjusted metric the score is **0.8, and the sign broke on the as-of
   session**. Both are reported; the aggressor-adjusted one is used for the verdict.
3. **The merger-arb spread (1.86%) is derived**, from two independently validated
   as-of closes already quoted in `phase-0.5-context.md` (SWKS 62.28, QRVO 90.57)
   and the deal ratio from the SEC Form 425 reporting (0.960 + $32.50). Arithmetic
   shown inline. It is **not** a quoted market spread and carries the usual
   caveats: it ignores the cash/stock election mechanics, any dividend adjustments
   (moot — SWKS's dividend is eliminated), borrow cost on the SWKS short, and the
   time value of the cash leg.
4. **YoY inflation figures are derived** as `latest / 12-months-prior − 1` from the
   raw FRED index levels quoted in the table (e.g. CPIAUCSL 332.568 / 321.435 − 1 =
   +3.46%). FRED's own `pc1` units were not requested; the levels are the primary
   values and the arithmetic is reproducible from them.
5. **Two catalyst dates are marked approximate and flagged as unverified** (July
   employment ~2026-08-07, July CPI ~mid-August). They were inferred from standard
   release cadence, not confirmed against a primary calendar, and are labelled as
   such in the table rather than presented as established.

## Verdict for downstream phases

- **Net macro bias for SWKS: HEADWIND.** Hawkish-hold Fed with three dissents
  wanting a **hike**, core PCE **+3.29%**, a **+24bp** move in the 10-year, a
  `TRANSITIONAL` regime with **34.1% bullish breadth** and explicit **half-size**
  guidance, and a sector that was the **largest net-sold of eleven** on the as-of
  date. Partially offset by a weaker dollar, a cooling labour market that caps hike
  risk, and a semis complex that is **cheap on growth-adjusted multiples (PEG
  0.56)** and closed green.
- **Conviction: 4 / 5.** High, because the two dominant findings are **hard,
  primary-source, company-specific facts** (dividend elimination; a live merger with
  disclosed terms and a Phase III regulatory review) rather than judgmental macro
  attribution — and because the sector-metric correction was **verified against the
  underlying parquet**, not asserted. Held below 5 because the two most important
  forward variables (SAMR timing, debt-raise pricing) are **undated and
  unknowable**, and because sector *impact* remains judgmental per the phase's own
  pitfall.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. **`TRANSITIONAL` regime, 34.1% bullish breadth, engine guidance "Half position
     sizes. Favor defined-risk strategies."** `[MACRO:MarketRegime_2026-07-31 UW]` —
     this is a direct, quantified instruction from the regime engine and should flow
     straight into sizing.
  2. **Technology aggressor-adjusted flow −$187,715,752 (largest outflow of 11
     sectors), with SWKS's RF/analog cohort net −$12.51M across 5 sessions and
     negative on 4 of them.** `[MACRO:MarketRegime_2026-07-31 UW]` — a long here is
     a long **against** the rotation.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **★ China SAMR Phase III decision on the Qorvo merger — UNDATED, BINARY, and
     the only event capable of exceeding the ±9.10% front-expiry implied move.**
     Two-sided: approval collapses the 1.86% arb spread and releases the arb short;
     a block strands $2B of debt and $500M of guided synergies while forcing that
     same short to cover. **Unhedgeable by timing ⇒ defined-risk structures only.**
  2. **2026-08-21 OPEX**, holding **61.87% of tracked OI**, max pain **$65.00
     (+4.23%)** — well inside the implied move, and the natural expiry for any
     defined-risk structure. Secondary: **ISM Manufacturing 2026-08-03** and
     **Services 2026-08-05**, both inside the priced range. **Note there is NO
     scheduled SWKS earnings inside a 1–8 week horizon** (next: 2026-10-27,
     verified).
- **Sector-rotation verdict: `ADVERSE`.** Aggressor-adjusted persistence score
  **0.8**, sign **broken on the as-of session** by the window's largest outflow;
  SWKS's own sub-cohort net-sold on 4 of 5 sessions. Tempered — not reversed — by
  the `fz` breadth divergence (Semiconductors **+0.25%** on price, PEG **0.56**).
  **Phase-9 sizing gate: apply the adverse-rotation cut.**
- **Correlation verdict: NO CLUSTER, NO SOFT-WATCH.** One concurrent blueprint
  exists for 2026-07-31 (**FSLR**); **SWKS/FSLR = 0.518**, below the 0.60
  soft-watch band and the 0.70 cluster threshold. **No size cut on correlation
  grounds.** The tool's `MODERATE` label and its two "100% concentration" warnings
  are artifacts of the broken `sector` field and are discarded.
- **★ Regime-change flag for phases 7b, 7c, 8, 8b and 9:** **SWKS is no longer a
  pure single-name semiconductor bet.** From 2026-07-28 it is (a) a **merger-arb
  underlying** carrying a structural arb short, (b) a **former 4.56% yielder whose
  income base has been evicted**, and (c) a **levering balance sheet** raising ~$2B
  into a rising long end. Every historical relationship phase 5 measured — the
  78-session self-history, the 30-session realized-vol series, the gamma regime —
  was estimated on a **different security than the one that now trades**. Phase 9
  must discount historical analogues accordingly, and phase 7b's quality veto
  should treat the dividend elimination and leverage step-up as **first-order**
  inputs, not footnotes.

**Sources:** [FOMC statement 2026-07-29](https://www.federalreserve.gov/monetarypolicy/files/monetary20260729a1.pdf) · [CNBC Fed rate decision July 2026](https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html) · [ISM Manufacturing PMI June 2026](https://www.prnewswire.com/news-releases/manufacturing-pmi-at-53-3-june-2026-ism-manufacturing-pmi-report-302814991.html) · [ISM PMI reports](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) · [Skyworks Q3 FY2026 results](https://www.globenewswire.com/news-release/2026/07/28/3334698/0/en/Skyworks-Delivers-Solid-Third-Quarter-Fiscal-Year-2026-Results-Announces-Key-Steps-Toward-Qorvo-Combination.html) · [SWKS Form 8-K Q3 FY2026](https://www.sec.gov/Archives/edgar/data/0000004127/000000412726000047/q3268-kex991earningsrelease.htm) · [Why Skyworks stock is tumbling](https://www.investing.com/news/stock-market-news/why-is-skyworks-solutions-stock-tumbling-today-93CH-4818935) · [SWKS suspends dividend amid Qorvo merger](https://www.chartmill.com/news/SWKS/Chartmill-51883-Skyworks-Solutions-NASDAQSWKS-Posts-EPS-Beat-Suspends-Dividend-Amid-Qorvo-Merger-Plans) · [SWKS $2B debt raise / Q4 guide](https://seekingalpha.com/news/4619955-skyworks-anticipates-1_010b-1_060b-q4-revenue-while-preparing-to-raise-about-2b-debt-for) · [Qorvo Form 425 merger terms](https://www.sec.gov/Archives/edgar/data/0001604778/000110465926064582/tm2614811d5_ex99-1.htm) · [SAMR review status](https://www.stocktitan.net/sec-filings/QRVO/425-qorvo-inc-business-combination-communication-2984a5db12ff.html) · [U-Michigan consumer sentiment July 2026](https://news.umich.edu/consumer-confidence-rises-for-second-straight-month-views-remain-downbeat-amid-high-prices/) · [Conference Board confidence July 2026](https://www.advisorperspectives.com/dshort/updates/2026/07/28/consumer-confidence-conference-board-july-2026)
