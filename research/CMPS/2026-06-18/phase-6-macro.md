# Phase 6 — Macro Overlay

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro is genuinely **mixed for CMPS, but the rate/Fed leg leans as a headwind** that
*aligns* with the bearish flow, while the sector-flow leg leans *against* it. The
**June 17 FOMC turned hawkish**: rates held at 3.50–3.75%, but the 2026 year-end dot
rose to **3.8% (from 3.4%)** — nine participants now see at least one *hike* this year,
amid Middle-East-conflict uncertainty and a new chair (Warsh). Yields backed up (10y
**4.49%**, 2y **4.20%**), and inflation is sticky (headline CPI **+4.17% YoY**, core
**+2.82%**, core PCE **+3.29%**) — a higher-for-longer backdrop that pressures
long-duration, pre-revenue biotech multiples. The UW market regime is
**TRANSITIONAL / PULLBACK_IN_UPTREND** ("half position sizes, defined-risk"). Against
that, **Healthcare options flow is a persistent INFLOW** (net +$219.6M today,
persistence 0.8) — adverse to a short. But the dominant CMPS driver is idiosyncratic:
the **COMP006 26-week durability readout (H2 2026)** and **NDA filing (Q4 2026)** are
exactly the binaries the Jan-2028 LEAP put is positioned ahead of.

## Key signals

- **FOMC 6/17 hawkish hold**: dots up to 3.8% 2026 y/e, hike-bias, Middle-East risk
  [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]
- Yields up: **10y 4.49%** (2y 4.20%, 2s10s +0.27 normal) — headwind for duration-
  sensitive biotech [MACRO:DGS10_2026-06-17 FRED]
- Sticky inflation: **CPI +4.17% YoY**, core +2.82%, core PCE +3.29%
  [MACRO:CPIAUCSL_2026-05 FRED]
- Regime **TRANSITIONAL / PULLBACK_IN_UPTREND**, "half sizes, defined-risk"; breadth
  weak (bullish_pct 38.6%) [MACRO:MarketRegime_2026-06-18 UW]
- **Healthcare sector INFLOW**, net +$219.6M, persistence 0.8 — *adverse* to the bear
  [MACRO:SectorFlowPersistence_2026-06-18 UW]
- **CMPS catalyst stack**: COMP006 26-wk durability data **H2 2026**, **NDA Q4 2026**,
  Breakthrough Therapy — the LEAP put's event horizon [MACRO:CMPS_catalyst WebSearch:compasspathways]

## Detailed findings

### Market regime (`[MACRO:MarketRegime_2026-06-18 UW]`)

- `regime` = **TRANSITIONAL — Mixed signals, reduce position size, wait for clarity**;
  `trend` = **PULLBACK_IN_UPTREND**; `trading_guidance` = "Half position sizes. Favor
  defined-risk strategies. Iron condors in range."
- SPY 746.74 (above 50sma 729.66, **below** 20sma 747.08), +1.77% 30d, −1.8% from
  90d high. Breadth weak: 2,421 bullish vs 3,853 bearish tickers (**bullish_pct 38.6%**).
- Sector rotation (premium): IN → Technology (+$629M), Financials, Cons. Cyclical;
  OUT → Comm Services, Industrials, Real Estate. Healthcare not in either extreme
  (mid-pack), consistent with phase-0.5.

### Inflation (FRED)

| Series | Latest | YoY | Read |
|--------|--------|-----|------|
| CPIAUCSL (headline) | 333.979 (May'26) | **+4.17%** | sticky/elevated |
| CPILFESL (core CPI) | 336.121 (May'26) | **+2.82%** | above target |
| PCEPILFE (core PCE) | 129.63 (Apr'26) | **+3.29%** | above 2% target |

[MACRO:CPIAUCSL_2026-05 FRED] [MACRO:CPILFESL_2026-05 FRED] [MACRO:PCEPILFE_2026-04 FRED]

### Labor (FRED)

- PAYEMS: May'26 159,001k = **+172k MoM** (Apr +179k, Mar +214k) — solid, slight
  deceleration. UNRATE **4.3%** (steady 4.3–4.4%). [MACRO:PAYEMS_2026-05 FRED]

### Rates (FRED + FOMC)

- DFF **3.63%**; FOMC 6/17 held target **3.50–3.75%** (unanimous on hold); **2026 y/e
  median dot 3.8%** (↑ from 3.4% Mar) → hike-bias. DGS10 **4.49%** (↑ from 4.43),
  DGS2 **4.20%** (↑ from 4.05), T10Y2Y **+0.27** (normal/positive curve).
  [MACRO:DFF_2026-06-17 FRED] [MACRO:T10Y2Y_2026-06-18 FRED]
  [MACRO:FOMC_2026-06-17 WebSearch:cnbc.com]

### Activity / Consumer

- Not separately pulled (single-name biotech; rate/Fed leg dominates the macro read).
  FOMC characterized activity as "expanding at a solid pace" despite Middle-East
  uncertainty.

### Sector overlay — Biotech/Healthcare

- Clinical-stage biotech is **long-duration and rate-sensitive**: rising 10y (4.49%)
  + a hawkish Fed dot (hike risk) compress speculative-biotech valuations → **mild
  headwind**, and one that *aligns* with the bearish CMPS flow.
- Drug calendar (idiosyncratic, dominant): COMP005 & COMP006 **both met Phase-3
  primary endpoints** (COMP006 on 2026-02-17); the open risks the LEAP put targets are
  the **COMP006 26-week durability data (H2 2026)** — durability is the historical
  knock on psychedelic antidepressants — and **NDA acceptance/FDA review (filing Q4
  2026 → decision 2027)**. [MACRO:CMPS_catalyst WebSearch:hcplive.com]

### Sector rotation (`[MACRO:SectorFlow_2026-06-18 UW]`)

- Healthcare today: net_flow **+$219,557,620** (call premium $374.4M vs put $154.8M).
  5-session: 6/12 +$3.85B, 6/15 +$229M, 6/16 +$153M, 6/17 −$42M, 6/18 +$220M;
  **persistence_score 0.8**, `trend` = **INFLOW**.
- **fz breadth cross-check (advisory):** market breadth mildly green (advancers 264 /
  decliners 238, **pct_green 52.49%**, top_mover SNDK); but the **Healthcare group is
  −0.62% on price today** (Fwd P/E 16.82, PEG 2.03). Mild **divergence**: flow leaning
  in while sector price is flat-to-down — colors the INFLOW read as "positioning, not
  yet price." [MACRO:sector_breadth fz EOD] [MACRO:group_valuation fz EOD]
- **Verdict vs thesis:** sector money is rotating **INTO** Healthcare and the rotation
  is persistent → **ADVERSE** to a bearish CMPS thesis (the bear fights sector inflow),
  though CMPS is the idiosyncratic outlier within it.

### Cross-name correlation (`[MACRO:Correlation_2026-06-18 UW]`)

- Concurrent blueprints for 2026-06-18: **CMPS, MARA, PATH**. Ran
  `uw risk portfolio-correlation --symbols CMPS,MARA,PATH --lookback-days 30`.
- `high_correlations` = **null** → no pair flagged ≥ the high threshold (≥0.70). The
  tool's `sector_breakdown` returned "Unknown" for all three (the known broken
  sector-field artifact — disregard the spurious "100% concentration" warning).
- Businesses are unrelated (CMPS biotech, MARA crypto-miner, PATH software) →
  intrinsic correlation low; **no cluster, no soft-watch pair**. (Raw pairwise
  coefficients were not exposed in this response; resting on the null high-corr flag +
  fundamental dissimilarity.)

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Biotech/CMPS |
|-----------|--------------|--------------|--------|------------------------|
| FOMC dots / hike-bias | y/e 3.8% (↑) | 2026-06-17 | WebSearch:federalreserve.gov | **headwind** (aligns w/ bear) |
| 10y yield | 4.49% (↑) | 2026-06-17 | FRED | **headwind** (duration) |
| Core PCE YoY | +3.29% | 2026-04 | FRED | headwind (higher-for-longer) |
| Headline CPI YoY | +4.17% | 2026-05 | FRED | headwind |
| Unemployment | 4.3% | 2026-05 | FRED | neutral |
| Market regime | TRANSITIONAL/pullback | 2026-06-18 | UW | headwind (cut size) |
| Healthcare sector flow | +$219.6M, persist 0.8 | 2026-06-18 | UW | **tailwind** (adverse to bear) |
| Healthcare price (fz) | −0.62% today | 2026-06-18 | fz EOD | neutral/mild |

## Catalyst calendar (next 30d+)

**Front-expiry implied (priced) move: ±4.14% / ≈$0.52** [CTX:implied_move]. Phase-9
sizes structures to this range; each binary below reads against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-07-17 | OPEX cliff (31.21% of OI, call-heavy; max-pain $12) | gamma/pin event | pin near $12–13 |
| ~2026-07-28/29 | Next FOMC meeting | rate path / hike-bias | macro, market-wide |
| 2026-07-30 | CMPS earnings (screener `next_earnings_date`; verify) | cash runway / pipeline update | can exceed ±4.14% |
| H2 2026 | **COMP006 26-week durability data** | **major binary** (durability risk) | far exceeds ±4.14% |
| Q4 2026 | **NDA submission to FDA** | regulatory milestone | binary, multi-month |

## Tool / source errors

- `fz groups --by sector --view valuation` is a top-level **array** (not `.rows`);
  first jq path errored, re-read by filtering the array on `.Name=="Healthcare"`
  (see value above). No data lost.
- `uw risk portfolio-correlation` did not expose a numeric pairwise matrix in this
  response (only `high_correlations`, null); sector field broken (known). Correlation
  verdict rests on the null high-corr flag + fundamental dissimilarity.

## Verdict for downstream phases

- **Net macro bias for CMPS:** **mild HEADWIND** — hawkish Fed + rising 10y + sticky
  inflation pressure long-duration biotech (this *aligns* with the bearish flow); the
  Healthcare sector INFLOW is the offsetting tailwind. Idiosyncratic catalysts
  dominate either way.
- **Conviction:** **3 / 5** — the rate/Fed headwind is real and directionally
  supportive of the bear, but biotech moves on data, not the 10y.
- **Top 2 datapoints phase-9 must cite:** (1) FOMC 6/17 hawkish dot to 3.8% + 10y
  4.49%; (2) UW regime TRANSITIONAL/pullback → "half sizes, defined-risk."
- **Top 2 catalysts for phase-9's calendar:** (1) **COMP006 26-week durability data,
  H2 2026** (the LEAP put's core binary); (2) **NDA filing Q4 2026** + the 7/30
  earnings / 7/17 OPEX nearer-term.
- **Sector-rotation verdict:** **ADVERSE** to the bearish thesis — Healthcare INFLOW,
  persistence **0.8** (phase-9 sizing-gate input: rotation gate trims a short).
- **Correlation verdict:** **No cluster (≥0.70) and no soft-watch (0.60–0.70)** flagged
  vs concurrent blueprints MARA, PATH (high_correlations null; unrelated businesses).
  Not a sizing constraint.
