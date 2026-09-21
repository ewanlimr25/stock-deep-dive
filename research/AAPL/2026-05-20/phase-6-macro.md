# Phase 6 — Macro Overlay

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T23:55:00Z
**Upstream phases cited:** phase-0-intake.md, phase-2-dark-pool.md, phase-5-historical.md

## Summary

The market regime is **TRANSITIONAL with an UPTREND** — SPY $741.25 sits
above 20-SMA ($728.29) and 50-SMA ($693.76) and is up 5.28% over the
trailing 30 days, but **breadth is bearish: only 39.5% of optionable
tickers are net-bullish today** [MACRO:MarketRegime_2026-05-20 UW]. The
narrow leadership is **explicitly Tech-positive**: Technology
$+349.9M net flow today, the biggest sector inflow on the tape,
followed by Consumer Cyclical ($+87.2M) and Industrials ($+41.3M).
Energy and Communication Services are net out [MACRO:SectorRotation_2026-05-20 UW].

The macro **headwind** is inflation: **April 2026 CPI re-accelerated
to 3.8% YoY (from 3.3% in March), with core 2.8% YoY and energy
+17.9% YoY driven by the Middle East / Iran-related supply shock**
[MACRO:CPI_2026-04 WebSearch:bls.gov]. The Fed held at **3.50–3.75% at
the 4/29/26 FOMC with an easing bias in the statement** despite three
dissents arguing against the bias and one dissenting in favor of a
cut [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]. The
**next dot-plot release is June 2026 FOMC** — that meeting (~30 days
out) is the dominant near-term macro catalyst.

For AAPL specifically: **Q2 FY26 earnings already printed on
2026-04-30** ($111.2B revenue +17% YoY, $2.01 EPS beat by 3.6%) and
**next earnings is 2026-07-30** [MACRO:AAPL_Q2FY26 WebSearch:sec.gov].
That places the LEAP buyer (phase-1) in a post-earnings, pre-WWDC
window with no near-term company-specific event risk and the next
binary catalyst 71 days out — perfectly aligned with the LEAP buyer's
duration choice and the LEAP-buyer-as-anchor thesis.

Net macro bias for AAPL: **tailwind from sector rotation + clean
post-earnings calendar**, partially offset by **the inflation
re-acceleration / Fed-on-hold risk** which mostly hurts longer-duration
unprofitable tech rather than AAPL's cash-flow-heavy profile.

## Key signals

- **TRANSITIONAL regime with UPTREND, breadth 39.5% bullish**
  [MACRO:MarketRegime_2026-05-20 UW]. Trading guidance: half position
  sizes, favor defined-risk strategies.
- **Tech sector +$349.9M net inflow** [MACRO:SectorRotation_2026-05-20 UW]
  — biggest sector inflow; AAPL participates directly.
- **April CPI +3.8% YoY (vs 3.3% prior), core +2.8%**
  [MACRO:CPI_2026-04 WebSearch:bls.gov]. Inflation
  re-acceleration is a headwind to Fed cuts and the long-duration
  growth multiple.
- **FOMC 4/29/26 held at 3.50–3.75% with easing bias retained**
  [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]. Next dot
  plot June 2026 — phase-9 must put it on the catalyst calendar.
- **AAPL next earnings 2026-07-30 (Q3 FY26)** — **71 days from today**,
  comfortably outside any near-term debit-spread window
  [MACRO:AAPL_Q3FY26 WebSearch:9to5mac.com]. No company-specific
  binary inside 30 days.

## Detailed findings

### Market regime (UW)

| Field | Value |
|-------|-------|
| `regime` | TRANSITIONAL — Mixed signals, reduce position size, wait for clarity |
| `trend` | UPTREND |
| SPY current | $741.25 |
| SPY 20-SMA | $728.29 |
| SPY 50-SMA | $693.76 |
| SPY 30d % | +5.28% |
| SPY from 90d high | −1.1% |
| Bullish flow tickers | 2,425 / 6,139 = **39.5%** |
| Bearish flow tickers | 3,714 / 6,139 |

| Sector | Flow today |
|--------|-----------|
| **Technology** | **+$349,934,394** |
| Consumer Cyclical | +$87,223,364 |
| Industrials | +$41,272,245 |
| Consumer Defensive | −$1,784,285 |
| Communication Services | −$16,735,377 |
| **Energy** | **−$67,509,274** |

**Reading:** Trend is up but participation is narrow (≈40% of names
are bullish, 60% are bearish). The bid is concentrated in **growth /
tech / cyclicals**; defensive and energy are bleeding. AAPL fits the
beneficiary cohort directly.

### SPY recent action (10d)

10-day SPY flow: **2 bullish days vs 8 bearish days** despite price
up. Today (5/20) flipped to bullish flow (+$63.7M net). SPY IV30
15.27%, IV rank 26.9 — calm tape. PCRs running 0.9–1.3, mostly above
parity = put-heavy (consistent with phase-4 complacent skew picking
up the AAPL-specific component but SPY broad index is more cautious).

### Inflation (CPI / PCE)

| Series | Latest print | Date | YoY | MoM |
|--------|--------------|------|-----|-----|
| CPI all-items | 3.8% | Apr 2026 | **+3.8% (up from +3.3%)** | +0.6% |
| Core CPI (ex food/energy) | 2.8% | Apr 2026 | **+2.8% (up from +2.6%)** | +0.4% |
| Energy CPI component | — | Apr 2026 | **+17.9%** | — |
| Food CPI component | — | Apr 2026 | +3.2% | — |

**Driver:** Middle East / Iran-related oil price shock. **FRED API
key not available — values sourced via WebSearch:bls.gov.**

PCE / Core PCE not directly fetched (BLS reports CPI; BEA reports PCE
and the April 2026 PCE release falls in late-May — beyond the as-of
date). Treat headline + core CPI as the inflation read of record for
this run.

### Labor (NFP)

| Field | Value | Source |
|-------|-------|--------|
| NFP April 2026 | **+115k** (vs +55k consensus) | [MACRO:NFP_2026-04 WebSearch:bls.gov] |
| NFP March 2026 (revised) | +185k | |
| Unemployment rate | 4.3% (steady) | |
| Labor force participation | 61.8% (lowest since late-2021) | |
| Avg hourly earnings MoM | +0.2% | |
| Avg hourly earnings YoY | +3.6% | |

**Reading:** Labor is **cooling but not breaking** — beats consensus
on headline but participation falling. Wage growth at 3.6% is no
longer driving services inflation. Consistent with a Fed comfortable
holding rates while monitoring.

### Rates

- **Fed funds target range: 3.50–3.75%** (held at 4/29/26 FOMC)
- **Easing bias retained in statement** (3 hawk dissents, 1 dove
  dissent who wanted to cut now)
- **Next FOMC: June 2026** (date TBD per search, ~6/17/26 historical
  pattern) — **first dot-plot release** since March
- 10y / 2y yields and 2s10s spread: not fetched (FRED API key
  unavailable; WebSearch suffices for the qualitative read)

### Activity (ISM)

| Index | April 2026 | March 2026 | Direction |
|-------|-----------|-----------|-----------|
| ISM Manufacturing PMI | **52.7** | 52.7 | 4th consecutive expansion month |
| ISM New Orders | 54.1 | 53.5 | accelerating |
| ISM Production | 53.4 | 55.1 | decelerating |
| **ISM Services PMI** | **53.6** | 54.0 | **22nd consecutive expansion month** |

**Reading:** Twin expansion in mfg and services. **Tailwind for
broad earnings power, including AAPL services/products mix.** ISM
Prices index surged — confirms the energy-driven CPI re-acceleration.

### Consumer (U-Mich, CB)

Not fetched in this run (no time-critical signal in the trade window;
phase-9 will note as a known unknown). [MACRO:Consumer skipped — WebSearch:not-run]

### Sector overlay — AAPL / Tech specifics

- **Q2 FY26 results released 2026-04-30:** Revenue $111.2B (+17% YoY,
  beat); EPS $2.01 (+22% YoY, beat by 3.6%). Already absorbed by the
  tape.
- **Next earnings: 2026-07-30 (Q3 FY26 = June quarter).** **71 days
  out.**
- **WWDC keynote 2026:** Per Apple convention, early June (likely
  6/8–6/12/26) — known catalyst window for AI / software roadmap. Not
  earnings, but historically moves AAPL ±2-4%.
- **Iran / Middle East risk:** Direct exposure is limited (no major
  AAPL manufacturing in the Gulf), but indirect via consumer
  spending if oil sustained > $90.
- **China:** Not fetched in this run. AAPL has structural China
  exposure both for sales and supply chain — phase-9 should flag as
  unscored unknown.

## Tailwind / Headwind table

| Datapoint | Latest | Date | Source | Impact on AAPL / Tech |
|-----------|--------|------|--------|----------------------|
| Tech sector flow | +$349.9M | 2026-05-20 | UW | **Tailwind** |
| SPY 30d return | +5.28% | 2026-05-20 | UW | Tailwind |
| Market breadth (% bullish) | 39.5% | 2026-05-20 | UW | Headwind (narrow leadership) |
| CPI YoY | 3.8% | 2026-04 | WebSearch:bls.gov | Headwind (delays Fed cuts) |
| Core CPI YoY | 2.8% | 2026-04 | WebSearch:bls.gov | Headwind |
| Energy CPI YoY | +17.9% | 2026-04 | WebSearch:bls.gov | Headwind to multiples |
| NFP MoM | +115k | 2026-04 | WebSearch:bls.gov | Neutral (modest cooling) |
| Unemployment | 4.3% | 2026-04 | WebSearch:bls.gov | Neutral |
| Fed funds | 3.50–3.75% (hold + easing bias) | 2026-04-29 | WebSearch:federalreserve.gov | Neutral |
| ISM Mfg | 52.7 | 2026-04 | WebSearch:prnewswire.com | Tailwind |
| ISM Services | 53.6 | 2026-04 | WebSearch:prnewswire.com | Tailwind |
| AAPL Q2 FY26 | $111.2B rev +17% | 2026-04-30 | WebSearch:sec.gov | Tailwind (post-print run) |

## Catalyst calendar (next 30d, as of 2026-05-20)

| Date (est) | Event | Likely impact |
|------------|-------|---------------|
| **2026-05-30 (est)** | **Apr 2026 PCE inflation** | Mirrors CPI direction — if hot, headwind |
| 2026-06-06 (est) | May 2026 NFP / jobs report | Above 100k = neutral; below 50k = risk-off shock |
| **2026-06-08–12 (est)** | **Apple WWDC 2026 keynote** | AAPL-specific ±2–4% move; AI roadmap |
| 2026-06-11 (est) | May 2026 CPI release | Critical — second consecutive hot print would hurt; cool print is squeeze fuel |
| **2026-06-17 (est)** | **June FOMC + dot plot** | Largest single calendar event of the next 30d |
| 2026-06-19 | June monthly OPEX (AAPL OI 80,746 @ $300C) | Pin pressure into Friday close |

## Tool / source errors

- **FRED skipped — no `FRED_API_KEY` env var set.** Public CSV
  endpoint is blocked at CDN. To enable automated rate / inflation /
  labor pulls, the user can register a free key at
  https://fred.stlouisfed.org/docs/api/api_key.html and export it in
  their shell rc.
- **PCE (April 2026) not fetched** — release date 2026-05-30 falls
  after the as-of date.
- **U-Michigan / Conference Board consumer surveys not fetched** —
  no acute trade-plan implication; deferred.
- **China / supply-chain news not fetched** — known unknown flagged
  to phase-9.

## Verdict for downstream phases

- **Net macro bias for AAPL:** **modest TAILWIND** — sector inflow
  + post-earnings clean window + LEAP-friendly duration. **Tempered
  by** inflation re-acceleration + narrow breadth.
- **Conviction:** 3 / 5. Strong sector bid but TRANSITIONAL regime
  and a known macro event (June FOMC + dot plot) within the trade
  window cap the directional confidence.
- **Top 2 datapoints phase-9 must cite:**
  1. **Tech sector +$349.9M net flow today** (UW) — direct
     positive carry for AAPL relative-strength theses.
  2. **April CPI re-accelerated to 3.8% YoY** (WebSearch:bls.gov) —
     the macro risk vector that could break the long-gamma melt-up
     if the next CPI print (6/11/26) stays hot.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-06-17 (est): June FOMC + dot plot** — the single biggest
     macro event inside any 30-day debit structure's lifetime.
  2. **2026-06-08–12 (est): Apple WWDC keynote** — AAPL-specific
     ±2–4% move catalyst, falls *exactly* inside any 25–30 DTE
     debit call spread window.
