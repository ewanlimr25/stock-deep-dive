# Phase 6 — Macro Overlay

**Ticker:** RDDT
**Sector:** Communication Services (digital advertising / social platforms)
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T01:30:00-04:00
**Upstream phases cited:** phase-4-structure.md, phase-5-historical.md

## Summary

Macro regime is **TRANSITIONAL** with **bearish breadth** (35.7% of
tickers bullish on 5/18) and **Communication Services money flowing
OUT (-$20.5M)** alongside Technology (-$299.8M) — sector tape is a
**HEADWIND** for RDDT even though SPY is in a 30-day uptrend (+3.5%).
The most recent macro release was **April CPI on 2026-05-12 at +3.8%
headline / +2.8% core YoY** (sticky, above the Fed's 2% target). The
**FOMC held rates at 3.50–3.75% on April 29 with dovish dissent**
(Miran) and the **next FOMC meeting is June 16-17** (with SEP/dot-plot).
**No discrete macro catalyst falls inside the 5/22 front-end-IV
backwardation window** we identified in phase-4 — the 79% IV is
therefore best explained by 0DTE/weekly flow concentration around the
$160 strike + OPEX dynamics, not by a known event. The **8/21 IV
hump** (70%) maps cleanly to **RDDT Q2 2026 earnings** (likely
late-July / early-August, given Q1 reported 2026-04-30). Q1 itself
was a **+12.7% earnings reaction** and explains the historical_trend
+13.3% gap-up on 2026-05-01.

## Key signals

- Market regime **TRANSITIONAL**, SPY UPTREND but **breadth bearish
  35.7%** bullish-flow tickers
  [MACRO:MarketRegime_2026-05-18 UW].
- Sector rotation: **Communication Services -$20.5M outflow** on
  2026-05-18; Technology -$299.8M; cyclicals (Consumer Cyclical
  +$11.6M, Energy +$9.1M, Healthcare +$8.0M) are receiving the
  rotation — **headwind for RDDT**
  [MACRO:MarketRegime_2026-05-18 UW].
- **VIX 17.82** on 2026-05-18 (low absolute) but SPY MACD turning
  negative, highest-volume sell bar of the recent range — late-cycle
  euphoria with first cracks
  [MACRO:VIX_2026-05-18 WebSearch:tradingview.com].
- **April CPI +3.8% headline / +2.8% core YoY**, released 2026-05-12.
  Energy +3.8% MoM drove headline. Core sticky above the Fed's 2%
  target — supports the Fed-on-hold base case
  [MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov].
- **RDDT Q1 2026 earnings on 2026-04-30**: revenue **$663M +69% YoY**,
  EPS **$1.01 (+7x YoY)**, adj EBITDA $266M / 40% margin, stock +12.7%
  reaction. Needham target $300 post-print
  [MACRO:RDDT_Q1_2026-04-30 WebSearch:sec.gov].

## Detailed findings

### Market regime (UW `risk_market_regime`, 2026-05-18)

| Field | Value | Read |
|-------|-------|------|
| regime | **TRANSITIONAL — Mixed signals, reduce position size** | half size, defined risk |
| trend | UPTREND | |
| SPY current | 733.73 | |
| SPY 20D SMA | 726.78 (above) | |
| SPY 50D SMA | 692.47 (above) | |
| SPY 30D change | +3.53% | |
| SPY % from 90D high | -2.11% | not at highs, not at lows |
| Breadth bullish % | **35.7%** | bearish breadth despite uptrend |
| bullish tickers | 2,196 / 6,143 | |
| bearish tickers | 3,947 / 6,143 | majority |

Read: classic **late-cycle uptrend with deteriorating breadth** —
index level is fine but participation has narrowed. The "TRANSITIONAL"
label translates directly to the trading-guidance card: **half
position sizes, favor defined-risk strategies**. This sets a hard
ceiling on phase-9 sizing.

### Sector rotation (2026-05-18)

| Direction | Sector | Net flow |
|-----------|--------|----------|
| OUT | **Technology** | **-$299,789,934** |
| OUT | **Communication Services** | **-$20,540,205** |
| OUT | Basic Materials | -$17,333,493 |
| IN  | Consumer Cyclical | +$11,609,037 |
| IN  | Energy | +$9,105,853 |
| IN  | Healthcare | +$8,049,744 |

Read: rotation OUT of Tech + Comm Services INTO cyclicals (Consumer
Cyclical, Energy, Healthcare) is consistent with the SMH -5.9% and
AVGO -6.5% prints in the phase-5 signal_backtest. RDDT sits in
Communication Services — **structural sector headwind** on the same
day phases 1-4 saw isolated bullish flow on the name. This is the
**single biggest dissonance** in the workup.

### Inflation

| Series | Period | Print | YoY | Released | Source |
|--------|--------|-------|-----|----------|--------|
| CPI headline | April 2026 | +0.6% MoM | **+3.8%** | 2026-05-12 | BLS |
| CPI core | April 2026 | +0.4% MoM | **+2.8%** | 2026-05-12 | BLS |

Read: April CPI was **hot** — headline 3.8% (driven by energy +3.8%
MoM), core 2.8% (above Fed 2% target). Print landed inside our 90D
window (2026-05-12) and likely contributed to the 5/12 RDDT
distribution day (close $152.35, -4.5% from prior; flow -$3.8M net).

### Labor

| Series | Period | Print | Released | Source |
|--------|--------|-------|----------|--------|
| Nonfarm payrolls | April 2026 | **+115K** (vs +55K consensus) | 2026-05-02 | BLS |
| Unemployment rate | April 2026 | 4.3% (unchanged) | 2026-05-02 | BLS |
| Wage growth YoY | April 2026 | +3.6% | 2026-05-02 | BLS |

Read: labor beat estimate but soft in absolute terms; unemployment
rising-and-stable in low 4s. Mildly **tailwind** for consumer-facing
ad-spend names (RDDT) but the wage growth (3.6%) below CPI core
(2.8%? actually wage > inflation now) — consumer is OK, not strong.

### Rates / FOMC

| Datapoint | Value | Date | Source |
|-----------|-------|------|--------|
| Fed funds target | **3.50% – 3.75%** | 2026-04-29 (held) | federalreserve.gov |
| Dot plot signal | **1 cut in 2026** | 2026-04-29 SEP | yahoo finance live |
| Dissent | Miran preferred -25 bps; Hammack/Kashkari/Logan against easing bias | | |
| Next FOMC | **2026-06-16/17** with SEP | scheduled | federalreserve.gov |

Read: Fed is on hold with dovish dissent. Market is pricing **1 cut
in 2026** — modest accommodation. The sticky core CPI argues against
faster easing. For high-multiple ad-tech (RDDT trades at premium
multiples on hyper-growth), prolonged restrictive policy is a
**modest headwind**. The June FOMC is the next macro event with
binary potential.

### Activity / Consumer

Not pulled in detail (would require additional WebSearch / FRED) —
labor + CPI prints cover the dominant macro narrative for a 30-day
window. Flagged as low-priority for this ticker.

### RDDT-specific catalysts and news

| Date | Event | Impact |
|------|-------|--------|
| 2026-04-30 (after close) | **Q1 2026 earnings**: rev $663M (+69% YoY), EPS $1.01 (+7×), adj EBITDA margin 40%, DAU 126.8M (+17%) | **+12.7%** next-day reaction; explains historical_trend 5/01 +13.3% gap |
| 2026-03 (ongoing) | **Shopify integration** ramping (ecommerce advertising) | tailwind |
| Q2 print expected | **~late-July / early-August 2026** (assumption: ~90 days post-Q1) | catalyst; explains 8/21 IV hump in phase-4 |
| 2026-04 | Needham $300 PT post-print | bullish street view |

### Macro-event explanation for phase-4 backwardation

| Phase-4 finding | Macro explanation |
|-----------------|-------------------|
| 5/22 (4 DTE) IV 79.1% | **No discrete macro** inside window. Likely: weekly OPEX dynamics, 0DTE concentration on the $160 wall, residual post-CPI vol bleed-down |
| 8/21 IV 70.1% | **RDDT Q2 2026 earnings** (estimated late-Jul / early-Aug); 8/21 is the regular-third-Friday following earnings, picks up the residual event premium |

Note: this means the "event" priced into the front-end IV in phase-4
is **not** a known fundamental catalyst — it is positioning-driven.
This INCREASES the likelihood the front-end IV mean-reverts post-OPEX
(phase-5 vanna interpretation: vol crush → dealer selling).

## Tailwind / Headwind table

| Datapoint | Value | Date | Source | Impact on RDDT |
|-----------|-------|------|--------|-----------------|
| Market regime | TRANSITIONAL | 2026-05-18 | UW | **HEADWIND** (sizing cap) |
| Breadth | 35.7% bullish | 2026-05-18 | UW | HEADWIND |
| Comm Services flow | -$20.5M outflow | 2026-05-18 | UW | **HEADWIND** |
| Technology flow | -$299.8M outflow | 2026-05-18 | UW | HEADWIND (sector spillover) |
| Consumer Cyclical flow | +$11.6M | 2026-05-18 | UW | neutral (rotation away from RDDT) |
| VIX | 17.82 | 2026-05-18 | WebSearch | low absolute; rising trend = neutral-to-headwind |
| SPY 30D return | +3.53% | 2026-05-18 | UW | tailwind (index intact) |
| CPI core YoY | 2.8% (sticky) | 2026-05-12 | BLS | **HEADWIND** (Fed on hold) |
| NFP | +115K beat | 2026-05-02 | BLS | mild tailwind (consumer OK) |
| Fed funds | 3.50–3.75% hold | 2026-04-29 | FRB | HEADWIND (restrictive) |
| RDDT Q1 earnings | +12.7% reaction | 2026-04-30 | Reddit IR | tailwind (idiosyncratic) |
| Shopify ramp | ongoing | 2026-Q1 | Reddit IR | tailwind |
| Needham PT | $300 | 2026-04/05 | sell-side | tailwind |

Net: **HEADWIND-leaning** — RDDT has strong company-specific
tailwinds (earnings beat, Shopify) but the sector tape is bleeding
and the regime sizing-rule caps positioning.

## Catalyst calendar (next 30d, from 2026-05-20)

| Date | Event | Likely impact on RDDT |
|------|-------|------------------------|
| 2026-05-22 (Fri) | **Weekly OPEX + monthly OPEX week settle** | gamma pin / mean-revert risk; phase-4 $160 magnet operative |
| 2026-05-28 (Thu) | **FOMC minutes** (April 29 meeting) | tape-driven only; not RDDT-specific |
| Late May | **April PCE release** (typical last week of month) | second look at inflation; could move risk |
| 2026-06-06 (Fri) | **May NFP** | systemic |
| 2026-06-10 (Wed) | **May CPI** | systemic |
| **2026-06-16/17** | **FOMC meeting + SEP/dot-plot** | binary — dovish surprise = tailwind for high-multiple growth |
| ~late-July / early-August | **RDDT Q2 2026 earnings** | binary — explains 8/21 IV hump (phase-4) |

## Tool / source errors

- FRED skipped — `FRED_API_KEY` env var unset; FRED public CSV
  endpoint is blocked at CDN per skill spec. To enable automated
  rate / inflation / labor pulls, the user can register a free key
  at https://fred.stlouisfed.org/docs/api/api_key.html and export
  it in their shell rc. WebSearch fallback used for all
  macro-series datapoints; release dates and values cross-checked
  against BLS / federalreserve.gov where possible.

## Verdict for downstream phases

- **Net macro bias for RDDT:** **HEADWIND** (sector tape, restrictive
  Fed, transitional regime — sufficient to cap position sizing
  notwithstanding the strong Q1 beat).
- **Conviction:** 4 / 5 on the headwind read; the TRANSITIONAL regime
  guidance ("half position sizes, favor defined-risk strategies") is
  prescriptive and aligns with phase-5's "win rate 0% for bullish
  flow" warning.
- **Top 2 datapoints phase-9 must cite:**
  1. Market regime TRANSITIONAL + Comm Services -$20.5M sector
     outflow on 2026-05-18 → size at HALF normal, defined-risk only.
  2. RDDT Q1 2026 earnings beat (4/30, +12.7% reaction) — the
     idiosyncratic case for RDDT is intact; the broader concern is
     sector / regime, not the company.
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-06-16/17 FOMC** + SEP/dot-plot — first major macro fork.
  2. **RDDT Q2 2026 earnings, ~late-July / early-August** — the
     8/21 IV hump's underlying. Position-trade-wise this is the
     anchor for any long-vol structure beyond ~6 weeks.

## Sources

- [Reddit Q1 2026 Earnings Press Release](https://www.sec.gov/Archives/edgar/data/0001713445/000171344526000067/earningspressreleaseq126.htm)
- [Reddit Q1 2026 Earnings Transcript — Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/01/reddit-rddt-q1-2026-earnings-transcript/)
- [Reddit Q1 2026 Yahoo Highlights](https://finance.yahoo.com/markets/stocks/articles/reddit-inc-rddt-q1-2026-071857743.html)
- [FOMC April 29 2026 Statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm)
- [FOMC Meeting Calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- [BLS April 2026 CPI Release](https://www.bls.gov/news.release/cpi.nr0.htm)
- [BLS April 2026 NFP Release](https://www.bls.gov/news.release/empsit.nr0.htm)
- [Yahoo Live: Fed forecasts 1 cut in 2026](https://finance.yahoo.com/news/live/fed-meeting-live-updates-federal-reserve-holds-rates-steady-forecasts-1-rate-cut-in-2026-180216872.html)
