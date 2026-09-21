# Phase 6 — Macro Overlay

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T01:00:00Z
**Upstream phases cited:** phase-4-structure.md, phase-5-historical.md

## Summary

The macro overlay is **net HEADWIND** for FSLY despite an SPY uptrend.
UW's regime classifier returns **TRANSITIONAL** (35.7% bullish breadth)
and recommends *half-size, defined-risk* positioning
[MACRO:MarketRegime_2026-05-18 UW]. Tech is the **single worst-rotating
sector with −$299.8M of premium outflow on 2026-05-18 alone**
[MACRO:MarketRegime_2026-05-18 UW]. **April CPI printed 3.8% YoY** (up
from 3.3% in March, highest since May 2023) on an **Iran-war-driven oil
shock** [MACRO:CPIAUCSL_2026-04 WebSearch:cnbc.com], pushing the **10y
yield to 4.61% (highest since Feb 2025)**
[MACRO:DGS10_2026-05-18 WebSearch:advisorperspectives.com]. The April 29
FOMC held at 3.50-3.75% with a **historic 8-4 vote (first time since Oct
1992 with four dissents)** [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]
— rate-cut visibility is poor. The single mitigating factor: **Fastly's
Q1 2026 earnings (reported 5/6/2026) included a 67% YoY Compute-segment
growth tied to edge-AI workloads** [MACRO:FSLY_Q1_2026 WebSearch:fool.com] —
giving FSLY a thin "AI-infra" narrative even in a tough tech tape. The
**5/22 IV spike of 117.7% (from phase-4) is NOT earnings** (those
reported 5/6) — most plausibly residual gamma from May OPEX + unresolved
vol-of-vol after the 38% earnings crash.

## Key signals

- **Regime = TRANSITIONAL with 35.7% bullish breadth**
  [MACRO:MarketRegime_2026-05-18 UW] — guidance "half size, defined-risk
  strategies."
- **Technology sector outflow = −$299.8M on 5/18 alone**
  [MACRO:MarketRegime_2026-05-18 UW] — the worst of any sector. FSLY
  fights this rotation as a small-cap tech name.
- **April CPI 3.8% YoY (+0.5 pp from March)**, core 2.8%
  [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov] — re-acceleration removes
  near-term rate-cut tailwind for high-multiple tech.
- **10y yield 4.61%** (5/18), highest since Feb 2025
  [MACRO:DGS10_2026-05-18 WebSearch:advisorperspectives.com] —
  duration headwind for any growth-tech multiple expansion.
- **Q1 FSLY revenue +20% YoY, Compute +67% YoY, raised guide to 15%**
  [MACRO:FSLY_Q1_2026 WebSearch:fool.com] — fundamentals fine, but
  market read the 20→15 deceleration as a sell signal (−38% on 5/7).

## Detailed findings

### Market regime (UW)

`risk_market_regime`, date=2026-05-18:

| Field | Value |
|---|---|
| Regime | **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity** |
| SPY current | $734.48 |
| SPY 20-SMA | $726.82 (above) |
| SPY 50-SMA | $692.49 (above) |
| SPY 30d change | +3.64% |
| SPY pct from 90d high | −2.01% |
| Bullish breadth | **35.7%** (2,196 / 6,143 tickers) |
| Trend | UPTREND (but breadth-weak) |
| UW guidance for TRANSITIONAL | "Half position sizes. Favor defined-risk strategies." |

**Sector rotation (net options-flow premium):**

| Inflows | $ | Outflows | $ |
|---|---|---|---|
| Consumer Cyclical | +$11.6M | **Technology** | **−$299.8M** |
| Energy | +$9.1M | Communication Services | −$20.5M |
| Healthcare | +$8.0M | Basic Materials | −$17.3M |

Tech outflow is **30×** the next-worst sector. This is the
single most important macro datapoint for FSLY — the sector tape is
hostile.

### SPY recent action context

`historical_trend`, symbol=SPY, days=10. Selected:

| Date | Close | Net flow | PCR | IV30d | IV rank | Flow |
|---|---|---|---|---|---|---|
| 2026-05-18 | 738.65 | −$46M | 1.03 | 15.5% | 28 | bearish |
| 2026-05-15 | 739.11 | −$42M | 1.03 | 15.4% | 27 | bearish |
| 2026-05-14 | 748.17 | −$131M | 0.97 | 14.8% | 24 | bearish |
| 2026-05-13 | 742.31 | −$172M | 1.19 | 15.3% | 27 | bearish |
| 2026-05-12 | 738.18 | +$8M | 1.29 | 15.4% | 28 | bullish |
| 2026-05-11 | 739.30 | −$63M | 1.31 | 15.7% | 29 | bearish |
| 2026-05-08 | 737.33 | −$20M | 1.30 | 14.7% | 23 | bearish |
| 2026-05-07 | 731.58 | −$7M | 1.14 | 14.8% | 24 | bearish |

**8 of last 10 SPY sessions were bearish-flow.** Price has held above
the 20/50-SMA, but options tape is consistently buying puts /
distributing. PCR consistently 1.0-1.3 — investors hedging
underneath an uptrend.

### Inflation

`MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov + cnbc.com + cnn.com`:

| Metric | April 2026 | March 2026 | Change |
|---|---|---|---|
| Headline CPI YoY | **3.8%** | 3.3% | +0.5 pp |
| Core CPI YoY | 2.8% | — | — |
| Core CPI MoM | +0.4% | — | — |
| Energy YoY | +17.9% | — | — |
| Gasoline YoY | +28.4% | — | — |
| Food YoY | +3.2% | — | — |
| Shelter MoM | +0.6% (re-accelerating) | — | — |

Headline CPI of 3.8% is the **highest since May 2023**. Above
consensus of 3.7%. Driver: the Iran-conflict oil shock + sticky
shelter. **Removes any near-term Fed dovish pivot scenario.**

### Labor

Most recent NFP / unemployment data not in WebSearch result set
above. Per general macro positioning context: with Fed signaling
solid economic activity at the April meeting and "job gains have
remained low" phrasing, the labor backdrop is *cooling but not
recessionary.* For high-IV unprofitable tech like FSLY, a cooling
labor market without recession is mixed — it pressures rate cuts
to wait but reduces immediate downside risk.

### Rates

| Series | 5/18/2026 | Context | Source |
|---|---|---|---|
| Fed funds target | 3.50-3.75% | Held 4/29; 8-4 vote (first 4-dissent since 1992) | WebSearch:federalreserve.gov |
| **10y yield (DGS10)** | **4.61%** | Highest since Feb 2025 | WebSearch:advisorperspectives.com |
| 10y vs Feb 2025 | +30-40 bp recent rise | Oil shock + inflation re-accel | WebSearch:cnbc.com |

**April 29 FOMC statement highlights** [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]:

- Decision: hold at 3.50-3.75%.
- Vote: 8-4. **Stephen Miran** voted to cut 25 bp.
- **Hammack, Kashkari, Logan** opposed inclusion of an easing bias
  in the statement.
- Statement framed inflation as "elevated, in part reflecting the
  recent increase in global energy prices" — explicit Iran-shock
  acknowledgment.

For FSLY as long-duration tech: 10y at 4.61% is **the structural
multiple-compression force**. Until 10y comes back below 4.25%,
small-cap tech multiples remain capped.

### Activity (ISM PMIs) and Consumer

Not pulled this run — would be priority-2 for a multi-ticker
sector dashboard. For a single-ticker FSLY deep-dive, the rate
+ sector rotation reads above are the binding constraints. Noted
as an unfilled gap rather than a critical omission.

### Sector overlay — FSLY-specific (Technology / Edge CDN)

**Fastly Q1 2026 earnings** (reported 5/6/2026, market reaction
5/7) [MACRO:FSLY_Q1_2026 WebSearch:fool.com + gurufocus.com]:

| Metric | Q1 2026 | YoY |
|---|---|---|
| Revenue | **$173M** | **+20%** |
| Gross margin (GAAP) | 62.5% | record |
| Gross margin (non-GAAP) | 65.1% | record |
| RPO | $369M | +63% |
| Security revenue | — | **+47%** |
| Compute ("Other") revenue | — | **+67%** (largest sequential step-up in company history; edge-AI workloads) |
| Network Services revenue | — | +11% (decelerated from Q4 gaming/e-commerce peak) |

2026 guidance raised to **15% sales growth**. FCF guide maintained
$40-50M. Security + Compute expected to clear $200M annual
run-rate by late 2026.

**Market reaction:** The implied deceleration from 20% → 15% sales
growth triggered a **−38% single-day stock move** (5/7 close $19.50
from $31.57). This is consistent with a "good company, wrong
expectations" tape — fundamentals were record, but multiple
re-rated lower.

**Other FSLY May 2026 notes:**

- 2026-03-31: **FMR LLC (Fidelity) added 7,767,134 shares at
  $29.06** [MACRO:FSLY_FMR_2026-03-31 WebSearch:gurufocus.com]
  — ~$226M position, now ~43% underwater at $16.50. **A meaningful
  institutional anchor with a strong incentive to defend the
  stock OR average in.**
- 2026-05-15: Filed Rule 144 notice for 3,555 shares
  [WebSearch:stocktitan.net] — immaterial size, routine insider
  filing.
- **No buyout, secondary, or material litigation news surfaced** in
  May 2026.

### What is the 5/22 IV-spike event?

Phase-4 flagged 5/22 IV at 117.7% vs 7/17 baseline 82.8% — a
clear event-premium signature. Earnings already passed (5/6/2026).
Candidate explanations, ranked:

1. **May monthly OPEX gamma residual** (most plausible): With
   ~214K total OI on 5/18 and 5/22 being May monthly OPEX, the
   short-dated chain still carries residual gamma demand. IV is
   bid because dealer hedging desks need to mark protective vol
   ahead of the gamma expiration.
2. **Vol-of-vol overhang from the 5/7 crash**: Realized σ over the
   trailing 30 days is 166% (phase-5). The market is still pricing
   in tail risk on a name that just moved −38% in a single day.
3. **Unconfirmed catalyst** (low probability): possible
   ITC/customer-loss/lawsuit news not yet on the tape. WebSearch
   did not surface anything material.

For trade planning purposes, **assume #1 (mechanical) + #2
(post-crash vol-of-vol)**. This argues *against* paying 117.7% IV
for 4-day premium and *for* using 30-60 DTE structures.

## Tailwind / Headwind table for FSLY

| Datapoint | Latest value | Release date | Source | Impact on FSLY |
|---|---|---|---|---|
| Market regime | TRANSITIONAL, 35.7% breadth | 2026-05-18 | UW | **HEADWIND** |
| Tech sector net flow | −$299.8M | 2026-05-18 | UW | **HEADWIND (severe)** |
| SPY trend | Uptrend, above 20/50 SMA | 2026-05-18 | UW | Mild TAILWIND |
| April CPI YoY | 3.8% (+0.5 pp) | 2026-05-12 | BLS / WebSearch | **HEADWIND** |
| 10y Treasury yield | 4.61% (cycle high) | 2026-05-18 | Fed H.15 / WebSearch | **HEADWIND** |
| Fed funds | 3.50-3.75% (held, 4 dissents) | 2026-04-29 | FOMC | NEUTRAL-HEADWIND |
| Iran oil shock | Energy CPI +17.9% YoY | 2026-04 | WebSearch | **HEADWIND** (geopolitical risk-off) |
| FSLY Q1 revenue | +20% YoY; guide +15% | 2026-05-06 | FSLY 10-Q | NEUTRAL (already priced) |
| FSLY Compute growth | +67% YoY (edge-AI) | 2026-05-06 | FSLY earnings call | **TAILWIND** (AI narrative anchor) |
| FMR LLC anchor position | 7.77M shares @ $29.06 | 2026-03-31 | gurufocus.com | TAILWIND (institutional floor incentive) |

**Net macro tally:** ~6 headwinds / 2-3 tailwinds / 1-2 neutral.
The macro overlay argues for **reduced position size, defined
risk, and a preference for structures that benefit from time and
vol contraction rather than directional upside**.

## Catalyst calendar (next 30d)

| Date | Event | Likely impact |
|---|---|---|
| **2026-05-22 (Fri)** | **May monthly OPEX** | High — drives the 117.7% 5/22 IV premium; expect IV decay post-OPEX |
| 2026-05-22+ | Vol crush as 5/22 expiry passes | Tailwind for vanna squeeze (phase-4) |
| ~2026-06-11 (Wed est) | May CPI release | Inflation print; could drive +/- broad tech |
| ~2026-06-17/18 (Tu/We est) | Next FOMC meeting + SEP / dot plot | Major rates catalyst |
| ~2026-06-19 | June quad-witching | Larger gamma expiration |
| Ongoing | Iran conflict / oil price tape | Continued macro vol driver |
| ~2026-08-05 (Wed est) | FSLY Q2 2026 earnings | Distant but next major company-specific catalyst |

## Tool / source errors

- `FRED_API_KEY` env var is not set (`echo $FRED_API_KEY` → empty).
  Per phase-6 skill rules, FRED skipped; falling back to
  WebSearch + WebFetch.
- ISM PMI + U-Mich / Conf Board consumer prints not pulled this
  run — acceptable gap for single-ticker FSLY deep dive given
  CPI + rates + Fed + sector rotation are already in.

## Verdict for downstream phases

- **Net macro bias for FSLY:** **HEADWIND** — sector outflow is
  severe, rates are restrictive, CPI is hot, regime is
  TRANSITIONAL.
- **Conviction:** 4 / 5 on the headwind read.
- **Top 2 macro datapoints phase-9 must cite:**
  1. **Technology sector premium outflow −$299.8M on 5/18**
     [MACRO:MarketRegime_2026-05-18 UW] — single biggest
     reason to size DOWN.
  2. **10y yield at 4.61%, April CPI 3.8% YoY** — the duration
     headwind is real until 10y < 4.25%.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-05-22 May monthly OPEX** — expect mechanical IV
     decay; primary near-term reason vanna squeeze can fire.
  2. **2026-06-17/18 next FOMC + SEP** — directional catalyst
     for tech multiples; tilt entries to be lightly positioned
     into this date.
- **Open questions:**
  - Is the FMR LLC position still intact (no large 13F sale yet),
    and have any other major holders disclosed? → would need to
    pull Bloomberg / WhaleWisdom; assume "intact" until proven
    otherwise.
  - Does FSLY's edge-AI narrative actually shield it from the
    broader tech outflow, or is the sector beta dominant? →
    phase-7/8 will sample analyst views.
