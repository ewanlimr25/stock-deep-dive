# Phase 6 — Macro Overlay

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T01:05:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-4-structure.md, phase-5-historical.md

## Summary

Market regime is **TRANSITIONAL** with mixed signals — SPY in an
established uptrend (above 20 & 50 SMA, +4.35% over 30d) but tape is
heavily bearish-flow (9 of last 10 sessions bearish-flow, breadth 34.7%
bullish). The UW playbook for TRANSITIONAL regimes is: **half position
sizes, defined-risk strategies only**. Sector rotation today shows money
flowing **OUT of Financial Services (-$48.8M)** — MARA's tagged sector
— and **INTO Technology (+$44M) and Energy (+$17M)**. Bitcoin (via IBIT
proxy) is consolidating around **$77K** with IBIT at $43.49 (-5.8% in
10 days, 7 of 10 bearish flow days) and BTC technicals turning neutral
(RSI 45, MACD bearish) at sub-$78K resistance. The next macro catalyst
is the **mid-June 2026 FOMC meeting** (~June 17-18), which aligns
exactly with the elevated **6/26 IV bump (111%)** observed in phase 4 —
implied vol is pricing a Fed-driven move into late June. **MARA Q1 2026
earnings were already reported on May 11**, missing revenue ($174.6M vs
$182.7M consensus) and posting a -$1.26B net loss ($-3.31 EPS vs -$2.20
estimated). The 5/11 stock peak at $13.39 coincided with this release —
the subsequent drop to $12.18 by 5/18 is the post-earnings reaction.
**Net macro bias: mildly headwind** — Financial Services rotation out
+ BTC consolidation + transitional market + recent earnings
disappointment all reduce the upside case.

## Key signals

- Market regime: **TRANSITIONAL**, UW guidance "half size + defined risk"
  [MACRO:MarketRegime_2026-05-19 UW]
- SPY uptrend but tape weak: 9 of 10 last sessions bearish-flow, net 10d
  flow strongly negative [MACRO:SPY_trend UW]
- Sector flow today: **Financial Services -$48.8M (MARA's tag)**, Tech
  +$44M, Energy +$17M [MACRO:SectorRotation_2026-05-19 UW]
- IBIT (BTC proxy): $43.49, **-5.8% in 10 days**, 7 of 10 bearish flow,
  IV rank only 10.7 [MACRO:IBIT_trend UW]
- BTC spot ~$76,900-$77,465 (May 18); resistance $78K-$82K; needs break
  $82K for $85-100K target [MACRO:BTC_2026-05-18 WebSearch:bitcoin.com /
  coindesk.com]
- **FOMC paused at 3.50%-3.75%** on 2026-04-29; Powell "no urgency to
  cut"; next meeting mid-June 2026 [MACRO:FOMC_2026-04-29
  WebSearch:federalreserve.gov]
- **MARA Q1 2026 earnings released 2026-05-11**: revenue miss $174.6M
  (consensus $182.7M), net loss -$1.26B / -$3.31 EPS, 35,303 BTC held,
  hashrate 72.2 EH/s (+33% YoY)
  [MACRO:MARA_Q1-2026_2026-05-11 WebSearch:stocktitan.net / sec.gov]
- ⚠️ **6/26 IV bump (111%, phase 4) now explained** = post-FOMC week
  + late-June OPEX cycle settlement [confluence with phase-4]

## Detailed findings

### Market regime (UW)

| Metric | Value |
|--------|-------|
| Regime label | **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity** |
| Trend | UPTREND |
| SPY current | $734.71 |
| SPY 20-SMA | $727.96 (above ✓) |
| SPY 50-SMA | $693.63 (above ✓) |
| SPY % from 90d high | -1.98% |
| SPY 30d change | +4.35% |
| Market breadth | 34.7% bullish (3,997 bearish vs 2,127 bullish tickers) |
| **Trading guidance** | **"Half position sizes. Favor defined-risk strategies."** |

**Reading:** SPY is mechanically in an uptrend, but breadth is
narrow-and-deteriorating (only 34.7% of optionable names show bullish
flow). The combination is classic late-cycle: index ticking higher on a
narrow group of names while the *median* stock is selling off. This
matches the phase-5 signal-backtest observation that bullish_flow had a
20% 10-day hit rate — most names are getting faded under an index up-tape.

### SPY 10-day trend

| Date | Close | Net flow | Direction | IV rank | PCR |
|------|-------|----------|-----------|---------|-----|
| 5/19 | 733.49 | -$27M | bearish | 30.6 | 1.18 |
| 5/18 | 738.65 | -$46M | bearish | 28.4 | 1.03 |
| 5/15 | 739.11 | -$42M | bearish | 27.2 | 1.03 |
| 5/14 | 748.17 | -$131M | bearish | 24.3 | 0.97 |
| 5/13 | 742.31 | -$172M | bearish | 27.4 | 1.19 |
| 5/12 | 738.18 | +$8M | **bullish** | 27.6 | 1.29 |
| 5/11 | 739.30 | -$63M | bearish | 29.4 | 1.31 |
| 5/8  | 737.33 | -$20M | bearish | 23.5 | 1.30 |
| 5/7  | 731.58 | -$7M | bearish | 23.7 | 1.14 |
| 5/6  | 733.83 | -$43M | bearish | 24.3 | 1.24 |

**Pattern:** sustained bearish flow with rising PCR (1.0-1.3 range
indicating put accumulation) under a slight downward bias from $748 high
to $733 today. **Hedging is increasing while index drifts off recent
highs.** A second leg lower in SPY is the elevated tail risk; if it
happens, high-beta crypto miners like MARA are first to dump.

### Sector rotation (today, 5/19)

**Money flowing IN (today):**
- Technology +$43,979,772
- Energy +$16,954,680
- Healthcare +$7,254,034

**Money flowing OUT:**
- Communication Services -$84,325,825
- Financial Services **-$48,789,451** ← MARA's tagged sector
- Consumer Cyclical -$26,986,324

**Reading:** Financial Services rotation out is a **headwind for MARA**.
But: MARA's *true* economic sensitivity is to BTC + AI compute, not
banks. Technology (+$44M) is a moderate offsetting tailwind via the AI
narrative (MARA's Q1 letter highlights AI/HPC transformation per the
ChainCatcher coverage). Net effect: mild headwind, not panic.

### Bitcoin / IBIT proxy

| Metric | Value |
|--------|-------|
| BTC spot range (May 18) | $76,900-$77,465 |
| Resistance levels | $77.7K, $78.5K, $79.4K, $82K |
| Support | $74.2K |
| Bullish breakout target | $85K-$100K (if break $82K) |
| Technicals | RSI 45 (neutral), MACD bearish |
| IBIT close 5/19 | $43.49 |
| IBIT 10d change | -5.8% |
| IBIT 10d flow direction | 7 of 10 bearish; net -$7.5M today |
| IBIT IV30 / IV rank | 38.1% / **10.7** |

**Reading:**
- BTC is consolidating $74-78K — not in a strong uptrend.
- IBIT IV rank of 10.7 is **very low** — BTC vol has compressed
  alongside equity vol. This is consistent with phase-5's IV crush
  observation in MARA. Low BTC vol = low MARA-beta amplification.
- IBIT flow is bearish 7 of 10 days — the BTC complex is not bid.
- For MARA to break the $13 phase-4 gamma wall, **BTC likely needs to
  break $82K** (per technical analyst consensus). At $77K with bearish
  MACD, that move is not imminent.

### Rates / FOMC

| Metric | Value | Source |
|--------|-------|--------|
| Fed funds rate (target) | 3.50%-3.75% | FOMC 2026-04-29 statement |
| Stance | "No urgency to cut" (Powell) | WebSearch:federalreserve.gov |
| Easing cycle | Paused since 2026 began | reporting consensus |
| Next FOMC | Mid-June 2026 (~Jun 17-18) | federalreserve.gov calendar |

**Reading:** Hawkish-pause stance is mildly negative for risk-on assets
(MARA, BTC). The next FOMC meeting is ~Jun 17-18 — and **phase 4
already flagged the 6/26 expiry IV bump to 111%**. That bump now has
a clean explanation: options market is pricing a Fed-driven move
through late June OPEX. **Treat 6/26 expiry as a known event-vol week.**

### MARA Q1 2026 earnings (release date: 2026-05-11)

This is the single most important macro datapoint for MARA — the catalyst
the prior weeks' OI build was positioning for.

| Item | Q1 2026 actual | Consensus | Variance |
|------|----------------|-----------|----------|
| Revenue | $174.6M | $182.7M | **-4.4% miss** |
| YoY revenue | -18.4% | — | down |
| Gross profit | $29.2M | — | -84.6% YoY |
| Operating loss | -$1.06B | — | massive |
| Net loss | -$1.26B | — | — |
| EPS | -$3.31 | -$2.20 | **miss by $1.11** |
| BTC held | 35,303 | — | $2.4B at $68,222/BTC |
| Hashrate | 72.2 EH/s | — | +33% YoY |

Source: SEC 8-K filing + StockTitan coverage, dated 2026-05-11.

**Stock reaction:**
- 5/11 close: $13.39 (pre-release high)
- 5/12 close: $12.72 (**-5.0%** post-earnings)
- 5/13-5/14: $12.75-$13.29 (bounce attempt)
- 5/15-5/19: $12.435 → $12.18 → $12.47 (digestion)

**Reading:** The market priced disappointment, but did NOT panic. Stock
held $12+ floor (above $11 phase-4 gamma flip). Two reasons it did not
collapse:
1. The Q1 results are widely viewed as a transitional quarter as MARA
   pivots toward AI/HPC compute (per ChainCatcher narrative).
2. The mining business operating expenses are linked to BTC price, and
   BTC was up significantly in Q1 — the loss reflects accounting
   treatment of digital asset impairment, not cash burn.

**This re-frames phase 3's OI buildup:** the heavy 13C/14C call writing
observed today (5/19) is **post-earnings covered-call writing** by
holders who are now capped on upside enthusiasm. It is NOT a new bear
trade — it's a "hold and harvest premium until next catalyst" structure.
Confirms the long-equity-collar interpretation from phase 3.

### Activity / Consumer (lower priority for crypto-miner)

Not separately fetched — for a high-beta crypto miner, ISM PMI and
consumer sentiment are 2nd-order. The primary drivers are BTC trend +
Fed stance + sector flow. Marked "neutral / lower priority" in the
table below.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on MARA |
|-----------|--------------|--------------|--------|----------------|
| Market regime | TRANSITIONAL | 2026-05-19 | UW | **HEADWIND** (half-size guidance) |
| SPY trend | uptrend but flow-bearish | 2026-05-19 | UW | neutral-headwind |
| Sector — Financial Services flow | -$48.8M (out) | 2026-05-19 | UW | **HEADWIND** |
| Sector — Technology flow | +$44M (in) | 2026-05-19 | UW | tailwind (AI angle) |
| BTC spot | $77K, consolidating | 2026-05-18 | WebSearch | neutral |
| IBIT 10d | -5.8% / IV rank 10.7 | 2026-05-19 | UW | neutral-headwind |
| FOMC pause + dot-plot | 3.50-3.75%, no rush | 2026-04-29 | WebSearch | mild HEADWIND |
| MARA Q1 earnings | revenue miss, -$1.26B net loss | 2026-05-11 | WebSearch | DIGESTED — overhang lifted but no upside catalyst |
| ISM Mfg PMI | (not pulled — low signal for miner) | n/a | — | neutral |
| Consumer sentiment | (not pulled) | n/a | — | neutral |

**Net macro overlay:** mild headwind. No single overwhelming negative,
but a stack of small negatives (sector rotation, BTC chop, transitional
regime) outweighs the two small positives (Tech inflows, earnings
overhang removed).

## Catalyst calendar (next 30 days from 2026-05-20)

| Date | Event | Likely impact |
|------|-------|---------------|
| 2026-05-22 | OPEX (Friday) | Pin to $12.5-$13 walls (phase 3/4 confluence) |
| 2026-05-25 | Memorial Day (US closed Mon 5/25) | Light volume week 5/26-5/29 |
| ~2026-05-30 | PCE inflation print (typical month-end) | Macro vol, modest impact |
| ~2026-06-06 | NFP / unemployment | Standard macro vol day |
| ~2026-06-13 | CPI release (typical Wednesday before FOMC) | High macro vol |
| **2026-06-17 to 06-18** | **FOMC meeting + dot plot** | **High vol — phase-4 6/26 IV bump confirmed** |
| 2026-06-18 | June monthly OPEX | Major dealer-rebalance event; MARA has 30K-50K OI in 10P/12C/13C/14C/15C/18C/20C/22C strikes |
| ~early Aug | MARA Q2 2026 earnings (3-month rhythm) | Out of 30-day window — note for phase 9 |

## Tool / source errors

- **FRED skipped** — no `FRED_API_KEY` env var set. Public CSV endpoint is
  blocked at CDN. To enable automated rate / inflation / labor pulls, the
  user can register a free key at
  https://fred.stlouisfed.org/docs/api/api_key.html and export it in
  their shell rc.
- All other data sources returned successfully.

## Verdict for downstream phases

- **Net macro bias for MARA:** **mildly HEADWIND**
- **Conviction:** 3/5 — multiple small negatives stack, no single decisive
  positive
- **Top 2 datapoints phase-9 must cite:**
  1. Market regime TRANSITIONAL → defined-risk + half-size sizing
     mandate (UW playbook explicit) [MACRO:MarketRegime_2026-05-19 UW]
  2. MARA Q1 2026 earnings already done 5/11; revenue miss but BTC
     holdings = $2.4B floor → no near-term catalyst, range trade
     thesis is supported [MACRO:MARA_Q1-2026_2026-05-11 WebSearch]
- **Top 2 catalysts phase-9 must put in the calendar:**
  1. **2026-05-22 OPEX (T+2 from trade date)** — pin to $12.5-$13
  2. **2026-06-17/18 FOMC + 2026-06-18 OPEX cluster** — primary vol
     catalyst inside next 30 days; confirms phase-4 IV-curve bump and
     defines the optimal *long-vol* expiry to own

## Sources

- [MARA Q1 2026 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001507605/000150760526000014/q12026earningsannouncement.htm)
- [MARA Q1 2026 results — StockTitan](https://www.stocktitan.net/news/MARA/mara-announces-first-quarter-2026-mfc4a3z4xgfu.html)
- [Bitcoin price levels May 2026 — bitcoin.com](https://news.bitcoin.com/bitcoin-price-outlook-turns-cautious-as-resistance-builds-near-78400/)
- [BTC technical levels — Coindesk](https://www.coindesk.com/markets/2026/05/07/three-signals-pointing-to-a-possible-bitcoin-move-to-usd85-000)
- [FOMC April 29 2026 statement — federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/files/monetary20260429a1.pdf)
- [FOMC calendar — federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
