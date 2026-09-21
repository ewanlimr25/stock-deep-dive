# Phase 6 — Macro Overlay

**Ticker:** RKT
**As-of date:** 2026-05-20 (data sources: UW 2026-05-19, WebSearch as-of 2026-05-20)
**Generated:** 2026-05-20T01:05:00Z
**Upstream phases cited:** phase-4-structure.md, phase-5-historical.md

## Summary

The macro backdrop is **outright hostile to RKT**. The market regime is
**TRANSITIONAL** per UW (SPY uptrend but only 34.7% bullish breadth);
**Financial Services sector flow is -$48.8M net OUT** today
[MACRO:MarketRegime_2026-05-19 UW]. The April 2026 CPI print on 2026-05-12
came in at **+3.8% YoY** — the highest since May 2023 — triggering a
**spike in 30Y mortgage rates to ~6.58% by 5/20** from low-6% levels in
late April [MACRO:CPI_2026-04 WebSearch:multiple]. A **US-Iran war**
backdrop is keeping oil-driven inflation elevated and pressuring rates UP,
exactly the wrong macro for a mortgage originator. RKT already reported
**Q1 2026 earnings on May 7** ($2.82B adj revenue, $0.15 EPS,
$738M adj EBITDA — beat) [MACRO:RKT_Q126_2026-05-07 WebSearch:SEC], which
EXPLAINS the 5/8 spot peak at $15.69 and the subsequent decline.
**Earnings is NOT the 5/22 catalyst**; the closest scheduled macro events
on 5/22 are Conference Board LEI and State Employment Summary (10am ET) —
neither typically a 25-vol-point catalyst. **The 5/22 IV spike remains
partially unexplained;** phase-9 should treat it as a binary
mortgage-finance-peer or geopolitical-headline risk window.

## Key signals

- **Market regime: TRANSITIONAL** — UW classification on 2026-05-19. Trading
  guidance: "Half position sizes. Favor defined-risk strategies"
  [MACRO:MarketRegime_2026-05-19 UW].
- **Financial Services net flow = -$48.79M (out)** while Technology
  +$43.98M and Energy +$16.95M (in) [MACRO:SectorRotation_2026-05-19 UW].
  Sector rotation away from RKT's home.
- **30Y mortgage rate at 6.58% on 5/20** — up materially since the
  5/12 CPI print [MACRO:Mortgage30Y_2026-05-20 WebSearch:money.com].
- **April 2026 CPI YoY = +3.8%** (highest since May 2023), released 5/12 —
  inflation surprise drove the rate spike [MACRO:CPI_2026-04 WebSearch:multiple].
- **Iran war backdrop** keeping oil/inflation elevated and rates sticky
  high [MACRO:GeopoliticalRisk_2026-05 WebSearch:nora].
- **RKT Q1 2026 reported 5/7: beat** ($2.82B rev, $0.15 EPS, $738M
  EBITDA) — earnings is the explanation for the 5/8 $15.69 peak, NOT a
  future catalyst [MACRO:RKT_Q126_2026-05-07 WebSearch:SEC].
- **SPY trend: uptrend, +4.94% in 30d, $738.89 close, above 20/50-SMA**;
  breadth only 34.7% bullish — quality-uptrend with weak breadth
  [MACRO:SPY_2026-05-19 UW].

## Detailed findings

### Market regime (UW `risk_market_regime`)

```
date                  : 2026-05-19
trend                 : UPTREND
regime                : TRANSITIONAL — Mixed signals, reduce position size,
                        wait for clarity
spy.current           : 738.89
spy.change_30d_pct    : +4.94%
spy.above_20sma       : true (20SMA 728.17)
spy.above_50sma       : true (50SMA 693.71)
spy.pct_from_90d_high : -1.42%
market_breadth        : 34.7% bullish (2,127 / 6,124 tickers)
```

**Trading guidance for TRANSITIONAL:** "Half position sizes. Favor
defined-risk strategies." This directly anchors the position sizing
decision in phase-9.

### Sector rotation (UW)

| Sector | Net flow today |
|--------|----------------|
| Technology | +$43,979,771 |
| Energy     | +$16,954,680 (Iran war beneficiary) |
| Healthcare | +$7,254,034 |
| Communication Services | **-$84,325,825** |
| Financial Services | **-$48,789,451** ← RKT's sector |
| Consumer Cyclical | -$26,986,324 |

**RKT-specific implication:** money is flowing OUT of Financial Services
on the day RKT is showing institutional accumulation. The single-name
signal is fighting the sector rotation. This is the **#1 reason the
phase-5 bullish_flow backtest is 10%** — bullish single-name signals in
sectors with negative rotation are particularly unreliable.

### Inflation (WebSearch)

- **April 2026 CPI YoY = 3.8%** (highest since May 2023), released
  2026-05-12 [MACRO:CPI_2026-04 WebSearch:multiple].
- Mortgage rates spiked DIRECTLY in response to this print: 30Y went from
  ~6.36% on 5/14 to 6.58% by 5/20 [MACRO:Mortgage30Y WebSearch:money.com].
- **No CPI release scheduled in the 5/22 window**; next CPI release
  expected mid-June.

### Labor (WebSearch — partial)

- **May 22 release:** Conference Board Leading Economic Index (10am ET)
  + State Employment and Unemployment Summary (10am ET)
  [MACRO:LEI_2026-05-22 WebSearch:conferenceboard.org]
- Neither is a market-moving release for single-stock vol; useful regime
  context only.
- April US payrolls already released; June NFP expected first Friday of
  June 2026.

### Rates (WebSearch)

- **30Y mortgage rate (5/20):** 6.58% per Money.com survey
  [MACRO:Mortgage30Y_2026-05-20 WebSearch:money.com]
- Fannie Mae Housing Forecast (May 2026): expects 6.3% avg rate sticky
  through Q1 2027, drifting to 6.2% rest of year
  [MACRO:FannieMaeForecast_2026-05 WebSearch:thestreet.com]
- **March 18, 2026 FOMC SEP:** median forecast 1 cut in 2026, year-end
  median ~3.4% Fed funds rate; high/low outliers 2.25%-3.75%
  [MACRO:FOMC_2026-03-18 WebSearch:federalreserve.gov]
- **No May 2026 FOMC meeting** — schedule is March, April 28-29, June
  9-10. The 4/29 meeting has already passed; next is June 9-10.

### Activity & Consumer

- Not specifically surfaced in this run. SPY uptrend + Technology /
  Energy inflows suggest broad activity is resilient despite tight
  policy. Negative breadth (34.7% bullish) suggests the rally is
  narrowing, not broadening.

### Sector overlay — Mortgage / Financial Services

- **Mr. Cooper acquisition closed 2025-10-01** — RKT now operates
  $2.1T UPB servicing portfolio; ~1 in 6 US mortgages
  [MACRO:RKT_MrCooper_2025-10-01 WebSearch:prnewswire.com].
- Combined entity has scale advantage in servicing (low rate-sensitivity)
  but origination revenue (high rate-sensitivity) faces a hostile rate
  backdrop.
- **Q1 2026 results (5/7): beat** — adj revenue $2.82B (above high-end
  guide), adj EBITDA $738M, adj EPS $0.15.
- Despite the beat, RKT has SOLD off 19% from $15.69 (5/8) to $12.675
  (5/19) — the market is selling the news because forward origination
  outlook is degraded by the rate spike.

### Catalyst calendar (next 30d)

| Date | Event | Source | Likely impact on RKT |
|------|-------|--------|---------------------|
| 2026-05-22 | Conference Board LEI 10am ET | WebSearch:conferenceboard.org | Low — neutral macro tape |
| 2026-05-22 | State Employment Summary 10am ET | WebSearch:bls.gov | Low — neutral |
| 2026-05-22 | **UNKNOWN RKT-specific event?** | Inferred from 85.9% weekly IV | **HIGH (binary, unexplained)** |
| 2026-06-09 | Existing-Home Sales (April release) | WebSearch:nar.realtor | Medium — sector-driver |
| 2026-06-09 | FOMC meeting starts | WebSearch:federalreserve.gov | High — Fed dot-plot, rate path |
| 2026-06-10 | FOMC decision + Powell presser | WebSearch:federalreserve.gov | High — rate-cut probability is the swing factor |
| 2026-06-(mid) | May 2026 CPI release | WebSearch:bls.gov | High — does April's 3.8% repeat? |

### Tailwind / Headwind table

| Datapoint | Latest value | Release | Source | Impact on RKT |
|-----------|--------------|---------|--------|---------------|
| Market regime | TRANSITIONAL | 2026-05-19 | UW | **Headwind** (half-size, defined-risk) |
| Financial Services net flow | -$48.79M | 2026-05-19 | UW | **Headwind** (rotation away) |
| CPI YoY (April) | +3.8% | 2026-05-12 | WebSearch | **Major headwind** (rate spike) |
| 30Y mortgage rate | 6.58% | 2026-05-20 | WebSearch | **Major headwind** (origination drag) |
| FOMC median 2026 path | 1 cut, 3.4% YE | 2026-03-18 | WebSearch | Neutral (priced) |
| Iran war / oil | Elevated | Ongoing | WebSearch | **Headwind** (inflation persistence) |
| SPY uptrend | +4.94% 30d | 2026-05-19 | UW | Mild tailwind (broad risk-on) |
| Tech sector inflows | +$43.98M | 2026-05-19 | UW | Neutral (not RKT's sector) |
| RKT Q1 2026 beat | $0.15 EPS / $2.82B rev | 2026-05-07 | WebSearch:SEC | Mild tailwind (results good) |
| Mr. Cooper synergy | $2.1T UPB | Closed 2025-10-01 | WebSearch | Structural tailwind (medium-term) |

Net: 1 mild tailwind, 1 structural tailwind, 6 headwinds (3 major). Macro is
**materially against** any bullish single-name expression in RKT today.

## Tool / source errors

- **FRED skipped — no `FRED_API_KEY` env var set.** Public CSV endpoint is
  blocked at CDN. To enable automated rate / inflation / labor pulls, the
  user can register a free key at
  https://fred.stlouisfed.org/docs/api/api_key.html and export it in
  their shell rc. For this run, WebSearch coverage substituted for
  precise series values.
- **The 5/22 catalyst remains unexplained.** Q1 earnings already
  reported (5/7), no FOMC, no CPI, no major scheduled BEA release. The
  85.9% weekly IV may reflect:
  1. A scheduled RKT-specific event not visible in public search
     (investor day, refinancing, secondary, divest)
  2. A geopolitical-event window (Iran war headline risk concentrating
     into end of OPEX week)
  3. A mortgage-finance peer announcement (UWMC, COOP-related entities)
  4. An expected GSE / FHFA policy announcement
- Phase-9 must treat the 5/22 expiry IV as a partially-unknown binary
  event and size accordingly.

## Verdict for downstream phases

- **Net macro bias for RKT:** **HEADWIND** (overall mortgage-rate /
  sector-rotation environment is hostile to mortgage originators).
- **Conviction:** 4/5 on the macro headwind read.
- **Two datapoints phase-9 MUST cite in its macro overlay:**
  1. **30Y mortgage rate at 6.58% on 5/20 after April CPI surprise of
     +3.8%** — the immediate fundamental headwind for RKT origination
     [MACRO:Mortgage30Y_2026-05-20 WebSearch, MACRO:CPI_2026-04 WebSearch].
  2. **Market regime TRANSITIONAL + Financial Services sector flow
     -$48.79M** — UW regime explicitly recommends half-size
     defined-risk; sector rotation away from RKT [MACRO:MarketRegime_2026-05-19 UW].
- **Two catalysts phase-9 MUST put in the calendar:**
  1. **2026-05-22 unknown catalyst window** — 85.9% weekly IV is the
     market's price for it; treat as binary [STRUCT:iv_term_structure].
  2. **2026-06-10 FOMC decision + dot-plot update** — the only macro
     event in the trade window that can re-rate rate-sensitive RKT.

Sources:
- [Rocket Companies Form 8-K Q1 2026 earnings (SEC)](https://www.sec.gov/Archives/edgar/data/0001805284/000180528426000064/rkt-earningsrelease3312026.htm)
- [Rocket Companies Closes Mr Cooper Acquisition (PR Newswire)](https://www.prnewswire.com/news-releases/rocket-companies-closes-14-2-billion-acquisition-of-mr-cooper-302571783.html)
- [Today's Mortgage Rates May 19 2026 (US News)](https://money.usnews.com/loans/mortgages/articles/mortgage-rates-today-may-19-2026)
- [Current Mortgage Rates May 18-22 2026 (Money.com)](https://money.com/current-mortgage-rates/)
- [Mortgage Rates Today May 15 2026 (Norada Real Estate)](https://www.noradarealestate.com/blog/mortgage-rates-today-may-15-2026-trends/)
- [FOMC Dot Plot March 18 2026 SEP (Federal Reserve)](https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20260318.pdf)
- [Federal Reserve Board Calendar May 2026](https://www.federalreserve.gov/newsevents/2026-may.htm)
- [Conference Board Leading Economic Index](https://www.conference-board.org/topics/us-leading-indicators/)
- [State Employment and Unemployment Summary April 2026 (BLS)](https://www.bls.gov/news.release/laus.nr0.htm)
