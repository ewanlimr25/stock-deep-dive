# Phase 6 — Macro Overlay

**Ticker:** NVDA (sector: Technology / Semiconductors)
**As-of date:** 2026-05-15
**Upstream phases cited:** phase-4-structure.md (IV backwardation pointing
to 05-22 event), phase-5-historical.md (HIGH_IV regime)
**Generated:** 2026-05-17T17:16Z

## Summary

The macro overlay is **MIXED-TO-HEADWIND** for NVDA over the next 30 days.
The headline risk is **the May 20 earnings print** (confirmed below), which
explains all the phase-4 / phase-5 IV stress. Beyond earnings, the broader
backdrop is **TRANSITIONAL with Technology as the worst-flow sector**: UW
regime label is "TRANSITIONAL — Mixed signals, reduce position size, wait
for clarity" and the **Technology sector saw $-151M in net options flow
outflow today** while Energy and Consumer Defensive saw inflows. CPI came
in **HOT at 3.8% YoY headline** (released 05-12, highest since May 2023),
which pressures the cut path and compresses tech multiples. The chip-policy
backdrop is **mildly positive but operationally stalled** — H200 China
exports were approved (Dec 2025, 25% tariff) but no deliveries have
materialized as of mid-May 2026.

## Key signals

- **NVDA Q1 FY2027 earnings: Wednesday 2026-05-20, AFTER market close**,
  call at 5:00 PM ET. Consensus: EPS $1.77, revenue ~$78.8B (+78% YoY)
  `[MACRO:NVDA_Earnings_2026-05-20 WebSearch:fool.com,spglobal.com]`. This
  is the dominant near-term catalyst and explains the phase-4 backwardation.
- **Market regime: TRANSITIONAL**, SPY $739.17, +5.35% 30d, in uptrend
  above 20/50 SMA, but breadth narrow (35.9% bullish flow)
  `[MACRO:MarketRegime_2026-05-15 UW]`. Guidance: "half position sizes,
  defined-risk".
- **Technology = worst sector by options flow today**: -$151M net outflow
  `[MACRO:SectorFlow_2026-05-15 UW]`. Direct headwind for NVDA.
- **CPI April 2026 headline +3.8% YoY** (released 2026-05-12), highest
  since May 2023; core +2.8% YoY `[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov]`.
- **Fed funds median path:** Dec 2025 dot plot showed 3.4% median for
  end-2026 (one cut), with 7 officials wanting no cuts
  `[MACRO:FOMC_DotPlot_2025-12 WebSearch:cnbc.com]`. April 29 FOMC released
  a statement; hot CPI on 05-12 likely pushes the cut further out.
- **China chip policy:** H200 approved for China sale with 25% tariff
  (Dec 2025 Trump policy); BIS case-by-case review. **No actual deliveries
  yet** as of mid-May 2026; Beijing has effectively blacklisted H20
  `[MACRO:ChinaChipExports_2026-05 WebSearch:bis.gov,scmp.com]`.

## Detailed findings

### Market regime (UW `risk_market_regime`, 2026-05-15)

| Field | Value |
|-------|-------|
| Regime | **TRANSITIONAL** |
| Trend | UPTREND |
| SPY current | $739.17 |
| SPY 20-SMA | $723.80 (above) |
| SPY 50-SMA | $690.04 (above) |
| SPY 30d Δ | +5.35% |
| % from 90d high | -1.38% |
| Bullish flow tickers | 2,207 / 6,156 (**35.9%**) |
| Bearish flow tickers | 3,949 |

Trading guidance for TRANSITIONAL: *"Half position sizes. Favor
defined-risk strategies."* — this directly informs phase-9 sizing and
structure choice.

### Sector rotation (UW today)

| Sector | Net flow $ | Direction |
|--------|-----------|-----------|
| Energy | +$7,673,649 | INFLOW |
| Consumer Defensive | +$6,001,187 | INFLOW |
| Communication Services | +$5,288,456 | INFLOW |
| Financial Services | -$34,409,787 | OUTFLOW |
| Consumer Cyclical | -$96,719,081 | OUTFLOW |
| **Technology** | **-$151,018,206** | **OUTFLOW (worst)** |

NVDA sits in the worst-flow sector today. This is a real signal — option
buyers are de-grossing tech ahead of NVDA earnings, the marquee Mag7 print.

### Inflation (CPI / Core CPI / PCE)

| Series | Latest | Date | YoY | Source |
|--------|--------|------|-----|--------|
| CPI headline | (Apr) | 2026-05-12 release | **+3.8%** | BLS via WebSearch |
| Core CPI | (Apr) | 2026-05-12 | +2.8% | BLS |
| Core PCE | (Mar) | last release | n/a in this run | — |

April CPI of 3.8% is the highest since May 2023 — energy-led. Tech valuations
typically compress when CPI surprises hot because terminal-rate expectations
re-price upward.

### Labor (NFP / unemployment)

Not directly queried in this dry-run — would require FRED `PAYEMS` and
`UNRATE` pulls. Production runs should add. Latest NFP release would be
early May for April data. Not flagged as a near-term swing factor for
NVDA over the next 30d.

### Rates (Fed, treasuries)

| Field | Value | Source |
|-------|-------|--------|
| Fed funds median (end-2026) | 3.4% (one cut from Dec 2025 dot plot) | CNBC / FRED `FEDTARMD` |
| Last FOMC statement | 2026-04-29 | federalreserve.gov |
| Next FOMC | Likely 2026-06-17/18 (6 weeks from 04-29) | inferred — confirm in production |
| 10y / 2y / 2s10s | not pulled this run | — |
| DXY | not pulled this run | — |

The April 29 statement preceded the hot 05-12 CPI; next FOMC will have to
reconcile sticky inflation against a slowing-but-positive growth backdrop.
For NVDA: higher-for-longer rates compress AI capex assumptions modestly.

### Activity (ISM PMI, consumer confidence)

Not pulled this dry-run; production runs should add ISM Mfg, ISM Services,
U-Mich and Conference Board. For NVDA-relevant macro, the chip-cycle has
been carried by hyperscaler capex announcements rather than ISM swings.

### Sector overlay — NVDA / semis

Specific catalysts mapped from WebSearch:

1. **NVDA Q1 FY2027 earnings: 2026-05-20 AMC** — Wall St expects $1.77 EPS,
   $78.8B revenue (+78% YoY). Focus: **Q2 guidance** and **Blackwell GPU
   supply/demand**. Data Center expected $72.8B (vs $53.8B June 2025 estimate,
   +35%).

2. **China chip exports (H200 approval, Dec 2025):** $5.4T market-cap
   re-rating happened on that headline; now operationally stalled. No
   deliveries; Beijing has blacklisted H20 and is directing Chinese firms
   to local alternatives. Probability of any positive Q2 guidance lift from
   China is LOW.

3. **AI capex narrative:** $1T cumulative hyperscaler AI spend question
   remains the primary thesis. Q2 guidance is the test.

## Tailwind / Headwind table for NVDA sector

| Datapoint | Latest | Release | Source | Impact on NVDA |
|-----------|--------|---------|--------|----------------|
| Market regime | TRANSITIONAL | 2026-05-15 | UW | **NEUTRAL** |
| SPY trend | UPTREND, +5.35% 30d | 2026-05-15 | UW | **TAILWIND** |
| Tech sector flow | -$151M today | 2026-05-15 | UW | **HEADWIND** |
| CPI YoY | +3.8% | 2026-04-30 / 05-12 | BLS | **HEADWIND** |
| Core CPI YoY | +2.8% | 2026-05-12 | BLS | NEUTRAL |
| Fed funds path | 3.4% median end-26 (1 cut) | Dec 2025 dot plot | CNBC/FRED | NEUTRAL → HEADWIND if CPI sticks |
| NVDA earnings (5/20) | Consensus +78% rev YoY | 2026-05-20 | spglobal.com | **BINARY CATALYST** |
| China chip exports | H200 approved (Dec 2025) | 2025-12-08 | bis.gov | TAILWIND (priced in) |
| China deliveries | Zero as of mid-May | 2026-05 | scmp.com | HEADWIND (vs hopes) |
| Beijing blacklisting H20 | active | 2026-Q1 | tomshardware | HEADWIND |

**Net macro read for NVDA over next 30d:** **mildly HEADWIND** —
TRANSITIONAL regime + tech-sector outflow + hot CPI compress the bullish
case; the binary May-20 earnings event dominates everything else.

## Catalyst calendar (next 30d)

| Date | Event | Likely impact |
|------|-------|---------------|
| **2026-05-20 AMC** | **NVDA Q1 FY2027 earnings + Q2 guidance** | **BINARY** — primary catalyst |
| 2026-05-30 (approx) | PCE April release | + if cool, - if hot |
| 2026-06-01 (approx) | ISM Manufacturing May | indirect (tech demand proxy) |
| 2026-06-03 (approx) | ISM Services May | indirect |
| 2026-06-05 (approx) | NFP May release | indirect (rate path) |
| 2026-06-11 (approx) | CPI May release | + if cool, - if hot |
| 2026-06-17/18 (approx) | FOMC | dot-plot revision possible |

## Tool / source errors

- WebSearch did not surface the specific May 2026 FOMC SEP — the most
  recent confirmed SEP in results was March 18, 2026. Notable May FOMC
  statement (April 29-released) details were referenced but not deeply
  retrieved. Production runs should WebFetch `federalreserve.gov` for the
  actual statement text.
- FRED series IDs (CPIAUCSL, PAYEMS, UNRATE, DGS10, T10Y2Y, DTWEXBGS,
  SOFR) were not directly queried via WebFetch in this dry-run — UW regime
  + WebSearch sufficed for the macro overlay. Production runs that need
  precise values should add WebFetch calls to `fred.stlouisfed.org/...`
  for the public CSV endpoints.

## Verdict for downstream phases

- **Net macro bias for NVDA:** **mildly HEADWIND** (TRANSITIONAL regime,
  tech outflow, hot CPI) overlaid with a **binary 5/20 earnings catalyst**.
- **Conviction on macro tilt:** 3/5.
- **Top 2 datapoints phase-9 must cite in its macro overlay:**
  1. NVDA earnings 2026-05-20 AMC (the dominant near-term swing factor).
  2. UW market regime TRANSITIONAL + Technology -$151M sector flow today.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-05-20 NVDA earnings** (BINARY).
  2. **2026-06-17/18 FOMC** (dot-plot revision possible after the hot
     CPI; affects multi-month tech valuation tail).

Sources:
- [Nvidia Reports Its Fiscal 2027 Q1 Earnings on May 20 — Motley Fool](https://www.fool.com/investing/2026/05/13/nvidia-reports-its-fiscal-2027-q1-earnings-may-20/)
- [Nvidia earnings preview Q1 2027 — S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/05/nvidia-earnings-preview-q1-2027)
- [CPI inflation April 2026 — CNBC](https://www.cnbc.com/2026/05/12/cpi-inflation-april-2026-.html)
- [Consumer Price Index — April 2026 (BLS PDF)](https://www.bls.gov/news.release/pdf/cpi.pdf)
- [Fed Outlook 2026 — iShares](https://www.ishares.com/us/insights/fed-outlook-2026-interest-rate-forecast)
- [Federal Reserve Board — FOMC statement April 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm)
- [Department of Commerce revises license review policy for semiconductors exported to China — BIS](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)
- [Nvidia prepares H200 shipments to China — Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/nvidia-prepares-h200-shipments-to-china-as-chip-war-lines-blur)
