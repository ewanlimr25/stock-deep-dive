# Phase 6 — Macro Overlay

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The macro regime is **hawkish and risk-off-leaning — a clear headwind for a
rate-sensitive, high-multiple, retail-flow-dependent fintech like HOOD.** Inflation is
**sticky and re-accelerating** (headline CPI +3.78% YoY, +0.64% MoM in April; core PCE
+3.29% YoY), driven by an **Iran-war oil/inflation shock**, and the Fed has turned
**hawkish**: the April 28-29 FOMC held at **3.5–3.75% with four dissents (most since
1992)** and the May-20 minutes show officials **see a rate HIKE ahead if inflation
stays elevated** (SEP median: only one cut in 2026). Yields have risen accordingly
(2y +25bp, 10y +21bp over ~6 weeks). UW market regime is **TRANSITIONAL** with weak
breadth (37% bullish) and explicit guidance to "**half position sizes, favor defined-
risk, iron condors in range**." Technology was today's **largest net-directional
outflow (−$433M)** — mildly adverse rotation for a Tech-classified name. The lone
offset is HOOD's **idiosyncratic growth story** (prediction markets, SpaceX IPO access,
AI tools), but that engine *depends on* the very retail risk appetite a hawkish Fed
suppresses. **Net macro bias: HEADWIND (conviction 4/5).** The June 16-17 FOMC is the
key in-window catalyst.

## Key signals

- **Fed hawkish:** held 3.5–3.75%, **4 dissents**, minutes flag a possible **HIKE**;
  median **1 cut in 2026** — Iran-war inflation [MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov].
- **Inflation re-accelerating:** CPI **+3.78% YoY** (+0.64% MoM Apr), core PCE **+3.29%
  YoY** [MACRO:CPIAUCSL_2026-04 FRED][MACRO:PCEPILFE_2026-04 FRED] — headwind for rich multiples.
- **Yields up:** 10y **4.50%** (+21bp/6wk), 2y **4.01%** (+25bp); 2s10s +0.48 (normal)
  [MACRO:DGS10_2026-05-26 FRED][MACRO:DGS2_2026-05-26 FRED][MACRO:T10Y2Y_2026-05-27 FRED].
- **Regime TRANSITIONAL**, breadth 37.1% bullish, SPY uptrend but +0.0% off 90d high;
  guidance: half size / defined risk [MACRO:MarketRegime_2026-05-27 UW].
- **Tech = largest net-directional outflow −$433M today** [MACRO:sector_rotation UW];
  HOOD–AAPL corr **0.685 (soft-watch)** [MACRO:portfolio_correlation DUCKDB].

## Detailed findings

### Market regime (UW: SPY + VIX + breadth) [MACRO:MarketRegime_2026-05-27 UW]

regime **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity."**
breadth: 2,291 bullish vs 3,881 bearish flow tickers → **37.1% bullish** (weak). SPY
**UPTREND** (753.24, above 20/50 SMA, +5.84% 30d, −0.1% from 90d high). trading_guidance:
**"Half position sizes. Favor defined-risk strategies. Iron condors in range."** A
melting-up index on narrow breadth — classic late-cycle, fragile tape.

### Inflation (CPI, PCE) — FRED, release 2026-04 (April data)

| Series | Apr 2026 | YoY | MoM (Mar→Apr) | Read |
|--------|----------|-----|---------------|------|
| CPI (CPIAUCSL) | 332.407 | **+3.78%** | **+0.64%** | hot, re-accelerating |
| Core CPI (CPILFESL) | 335.423 | +2.74% | +0.38% | sticky |
| PCE (PCEPI) | 130.902 | +3.77% | +0.40% | hot |
| Core PCE (PCEPILFE) | 129.63 | **+3.29%** | +0.24% | above target |

[MACRO:CPIAUCSL_2026-04 FRED][MACRO:CPILFESL_2026-04 FRED][MACRO:PCEPI_2026-04 FRED][MACRO:PCEPILFE_2026-04 FRED].
The April headline MoM (+0.64%, ~7.9% annualized) is the worrying print — consistent
with the Iran-war oil pass-through the Fed minutes cite. **Headwind** for cut hopes.

### Labor (NFP, unemployment) — FRED

PAYEMS (000s): Jan 158,592 → Feb 158,436 (**−156k**) → Mar 158,621 (+185k) → Apr
158,736 (**+115k**). Choppy with a Feb contraction; Apr modest. UNRATE: 4.3% (Apr), flat
4.3–4.4% all year [MACRO:PAYEMS_2026-04 FRED][MACRO:UNRATE_2026-04 FRED]. Labor is
soft-but-stable — not weak enough to force cuts, removing the dovish offset to inflation.
**Neutral.**

### Rates (FOMC, SOFR, 10y/2y, 2s10s) — FRED + WebSearch

- DFF **3.62%**, SOFR **3.63%** (5/26-27) — policy band 3.5–3.75%
  [MACRO:DFF_2026-05-26 FRED][MACRO:SOFR_2026-05-27 FRED].
- DGS10 **4.50%** (5/26) vs 4.29% (4/15) → **+21bp**; DGS2 **4.01%** vs 3.76% → **+25bp**
  — market pricing FEWER cuts / sticky inflation [MACRO:DGS10_2026-05-26 FRED][MACRO:DGS2_2026-05-26 FRED].
- 2s10s **+0.48** (normal/un-inverted) [MACRO:T10Y2Y_2026-05-27 FRED]; broad USD 119.29
  (flat) [MACRO:DTWEXBGS_2026-05-22 FRED].
- **FOMC 2026-04-29:** held 3.5–3.75%, **4 "no" votes (most since 1992)**; **May-20
  minutes: officials see a HIKE ahead if inflation stays elevated**; SEP median **1 cut
  in 2026** [MACRO:FOMC_2026-04-29 WebSearch:cnbc.com][MACRO:FOMC_SEP_2026 WebSearch:finance.yahoo.com].
  **Strong headwind** for long-duration growth/fintech.

### Activity / Consumer (ISM, U-Mich, Conf. Board)

Not separately pulled (FRED rate/inflation/labor + FOMC sufficient for a single-name
overlay; ISM/sentiment would only refine an already-clear hawkish read). Treated
**neutral/unweighted**; the regime label + breadth already capture activity risk.

### Sector overlay — HOOD-specific catalysts [WebSearch]

HOOD idiosyncratic narrative (fundamental color for phase-7b/7c):
- **Tailwinds:** prediction markets (~$3B April revenue, 2nd-biggest month ever);
  **SpaceX IPO retail-access**; new AI trading tools (+3% reaction); Trump/CFTC
  favorable on prediction-market jurisdiction [MACRO:HOOD_catalysts WebSearch:fool.com].
- **Drags:** crypto revenue **−47% YoY to $134M** in Q1 2026; stock debated "below $80"
  (= our 76.23) [MACRO:HOOD_crypto WebSearch:fool.com].
- These are **retail-risk-appetite-dependent** — they amplify in risk-on, fade in the
  hawkish/risk-off regime above. Earnings 2026-07-29 (outside 30d window).

### Sector rotation (UW sector-flow + persistence; fz breadth cross-check)

- **Net-directional (today):** `market-regime` shows money flowing **OUT of Technology
  −$433.5M** (largest outflow), Healthcare −$15.3M, Cons. Defensive −$7.2M; flowing
  **IN**: Comm. Services +$84.5M, Cons. Cyclical +$49.1M, **Financial Services +$35.5M**
  [MACRO:sector_rotation UW]. HOOD is UW-classified **Technology** (adverse today) but
  functionally **Financial Services / fintech** (mild inflow) — split read.
- **Persistence (5d, gross total premium):** Technology trend **INFLOW**, persistence
  **1.0**; Financial Services **INFLOW**, persistence **1.0** [MACRO:sector_flow_persistence UW].
  Caveat: persistence here tracks *gross* premium (Tech always largest, $8.5B today),
  **not direction** — it does not contradict the negative *directional* read above.
- **fz breadth cross-check (advisory, captured 2026-05-28):** market pct_green **40.76%**
  (205 adv / 298 dec), avg change −0.05%, worst mover SNPS −6.36% (a tech name)
  [MACRO:sector_breadth fz EOD]. Confirms a weak/risk-off tape.
- **fz group valuation (advisory):** Technology P/E **39.6** / Fwd 28.3 / PEG 1.19;
  Financial P/E **17.2** / Fwd 13.9 [MACRO:group_valuation fz EOD]. HOOD trades on the
  rich Tech multiple profile → most exposed to the rising-rate de-rating.
- **Rotation verdict:** **mildly ADVERSE** — Tech net-directional outflow + risk-off
  breadth outweigh the small Financial-Services inflow; aligns with phase-0.5's "HOOD
  lagging within its sector."

### Cross-name correlation (`uw risk portfolio-correlation`)

- Concurrent blueprint for 2026-05-27: **AAPL** (`research/AAPL/2026-05-27/`).
- UW `portfolio-correlation` returned `sector:"Unknown"` for both and **no coefficient**
  (the tool's correlation engine is broken — known issue). **Computed from local
  screener daily-return close instead:** **CORR(HOOD, AAPL) = 0.685 over 32 sessions**
  [MACRO:portfolio_correlation DUCKDB].
- **0.685 is in the 0.60–0.70 soft-watch band** (not a ≥0.70 cluster). Surface only:
  long-HOOD + long-AAPL is moderately correlated, but not a hard size-cut cluster.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on HOOD (Tech/fintech) |
|-----------|--------|---------|--------|-------------------------------|
| CPI YoY | +3.78% (MoM +0.64%) | 2026-04 | FRED | **headwind** |
| Core PCE YoY | +3.29% | 2026-04 | FRED | **headwind** |
| Fed funds / stance | 3.62%, hike risk, 4 dissents | 2026-04-29 | WebSearch/FRED | **strong headwind** |
| 10y yield | 4.50% (+21bp/6wk) | 2026-05-26 | FRED | **headwind** (multiple de-rate) |
| 2y yield | 4.01% (+25bp) | 2026-05-26 | FRED | **headwind** |
| 2s10s | +0.48 (normal) | 2026-05-27 | FRED | neutral |
| Unemployment | 4.3% (stable) | 2026-04 | FRED | neutral |
| Broad USD | 119.29 (flat) | 2026-05-22 | FRED | neutral |
| Market regime | TRANSITIONAL, 37% bull | 2026-05-27 | UW | **headwind** |
| Tech net-dir flow | −$433M (out) | 2026-05-27 | UW | mild **headwind** |
| HOOD catalysts | pred. mkts / SpaceX / AI | May 2026 | WebSearch | tailwind (risk-on dependent) |
| Crypto rev | −47% YoY | Q1 2026 | WebSearch | headwind |

## Catalyst calendar (next 30d)

Front-expiry implied move **±3.29% / ±$2.51** (5/29 front) [CTX:implied_move_pct] —
size structures to this priced range; each binary read against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-06-05 (est) | May NFP / jobs | hot wages → hawkish | a beat likely > ±3.3% if jolts vol |
| 2026-06-10/11 (est) | May CPI | **Iran-war oil risk → hot** | a hot print could exceed ±3.3% |
| **2026-06-16/17** | **FOMC** | **hike/hawkish-hold risk** | regime-defining; > ±3.3% on a surprise |
| 2026-07-29 | HOOD Q2 earnings | binary | outside 30d window |

## Tool / source errors

- `uw risk portfolio-correlation` returned `Unknown` sectors and **no correlation
  coefficient** for HOOD/AAPL (engine broken) → computed CORR=0.685 from local screener
  close via DuckDB (per data-source workaround).
- `sector-flow` / `sector-flow-persistence` `net_premium` parsed null in first jq cut;
  raw `net_flow_by_day` + `trend` resolve it. (FRED key WAS present — no FRED skip.)
- FRED CPI/PCE 2025-10 prints are `"."` (missing/government-shutdown gap) — YoY computed
  off 2025-04 base, unaffected.

## Verdict for downstream

- **Net macro bias for HOOD:** **HEADWIND.** Sticky/re-accelerating inflation + hawkish
  Fed (hike risk) + rising yields + weak-breadth TRANSITIONAL regime is squarely adverse
  for a rate-sensitive, rich-multiple, retail-flow-dependent fintech. The idiosyncratic
  growth story is real but risk-appetite-dependent (the regime suppresses that appetite).
- **Conviction:** **4/5** (the macro signals are unusually aligned and explicit).
- **Top 2 datapoints phase-9 must cite:** (1) **CPI +3.78% YoY / Fed hike-risk**
  [MACRO:FOMC_2026-04-29]; (2) **Regime TRANSITIONAL, "half size / defined risk"**
  [MACRO:MarketRegime_2026-05-27 UW].
- **Top 2 catalysts for the phase-9 calendar:** (1) **FOMC 2026-06-16/17** (in window);
  (2) **May CPI ~2026-06-10/11** (Iran-war hot-print risk).
- **Sector-rotation verdict:** **mildly ADVERSE** (persistence_score 1.0 on gross premium,
  but Tech net-*directional* flow −$433M today; Financial-Services inflow only partly
  offsets) — a phase-9 sizing down-tick, not a veto.
- **Correlation verdict:** **soft-watch — HOOD–AAPL 0.685** (0.60–0.70 band) vs the
  concurrent AAPL/2026-05-27 blueprint. Surface to phase-9; no hard cluster cut (<0.70).
