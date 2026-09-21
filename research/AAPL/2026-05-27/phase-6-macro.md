# Phase 6 — Macro Overlay

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:25:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The macro frame is **TRANSITIONAL** — UW's regime engine literally prescribes
"reduce position size, favor defined-risk strategies, iron condors in range,"
which maps almost exactly onto AAPL's long-gamma/range-bound micro setup. The
market is in a slow uptrend (SPY +4.93% 30d, above 20/50 SMA) **but on weak
breadth** (only **37.1% of names with bullish flow**), and inflation is
**re-accelerating** (CPI YoY **3.78%**, +0.64% MoM) into a **divided, hawkish-
leaning Fed** (held 3.5–3.75% on a rare 8-4 split, "inflation is elevated"). For
AAPL specifically: **Technology sector flow is a durable tailwind** (persistence
score 1.0, $4.3B→$8.5B over 5 sessions), but that is offset by fading rate-cut
hopes, a narrow tape, and **no AAPL-specific catalyst for 30+ days** (earnings
7/30). **Net macro: NEUTRAL, leaning size-down** — the regime says trade smaller
and defined-risk, which is the dominant instruction here. **A correlation cluster
fires: AAPL↔NVDA 0.736.**

## Key signals

- Regime **TRANSITIONAL** ("reduce position size, defined-risk, iron condors in
  range"); SPY UPTREND +4.93% 30d, above 20/50 SMA `[MACRO:MarketRegime_2026-05-27 UW]`
- **Breadth weak: 37.1% bullish-flow tickers** (2,291 bull / 3,881 bear of 6,172) `[MACRO:market_breadth_2026-05-27 UW]`
- **CPI re-accelerating: YoY 3.78%, +0.64% MoM** (Apr); Core CPI 2.74% — inflation
  elevated, rate-cut path stalling `[MACRO:CPIAUCSL_2026-04 FRED]`
- Fed held **3.5–3.75%** (Apr 29, 8-4 split, hawkish bias); 10y 4.5%, 2s10s +0.48
  (dis-inverted) `[MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov]` `[MACRO:T10Y2Y_2026-05-27 FRED]`
- **Technology sector = durable INFLOW** (persistence 1.0, $8.5B today) → aligned
  for AAPL `[MACRO:sector_flow_persistence UW]`; **but AAPL↔NVDA corr 0.736 = cluster** `[MACRO:portfolio_correlation DUCKDB]`

## Detailed findings

### Market regime (UW: SPY + breadth)

- **regime: TRANSITIONAL** — "Mixed signals, reduce position size, wait for
  clarity." trading_guidance: "Half position sizes. Favor defined-risk strategies.
  Iron condors in range." trend: **UPTREND**.
- SPY: current 750.46, +4.93% 30d, above 20SMA & 50SMA. 10-day: price 742→750
  (+1.1%), but **4 bullish / 6 bearish days** and IV rank falling 27→17.6 (vol
  compressing) — grinding up choppily.
- **Breadth: bullish_pct 37.1%** (2,291 bullish vs 3,881 bearish of 6,172
  optionable). A narrow, mega-cap-led tape — index up, majority of names not.

### Inflation (FRED, latest)

| Series | Latest | Read |
|--------|--------|------|
| CPI YoY | **3.78%** (Apr 2026) | elevated, above target `[MACRO:CPIAUCSL_2026-04 FRED]` |
| CPI MoM | **+0.64%** | hot (~7.9% annualized) — re-accelerating |
| Core CPI YoY | 2.74% | firm `[MACRO:CPILFESL_2026-04 FRED]` |
| Core PCE (Mar) | 129.279 (+0.29% MoM) | firm `[MACRO:PCEPILFE_2026-03 FRED]` |

Inflation re-accelerating is the key macro **headwind** — it stalls the easing
cycle and pressures high-multiple equities. The Fed's own statement cited
"elevated" inflation and "global energy prices."

### Labor (FRED)

- PAYEMS: Apr 158,736k (+115k MoM; Mar +185k) — decelerating but positive.
- UNRATE: **4.3%** (Apr), steady 4.3–4.4% — slightly elevated, not breaking down.
  Soft-ish labor + firm inflation = mild stagflation tint, ambiguous for AAPL
  consumer demand.

### Rates (FOMC, SOFR, curve)

- **FOMC held at 3.5–3.75%** (Apr 28-29 2026). Rare **8-4 dissent** (1 dove wanted
  a cut, 3 hawks opposed easing-bias language). Hawkish lean given inflation.
- DFF 3.62% · 10y (DGS10) **4.50%** · 2y (DGS2) 4.01% · **2s10s +0.48** (normal,
  dis-inverted) · broad USD (DTWEXBGS) 119.3 (flat). No recession signal from the
  curve; 4.5% 10y is a mild valuation headwind for long-duration tech.

### Activity & Consumer

Not separately pulled (FRED rates/inflation/labor sufficient for a single-name
overlay; ISM/U-Mich would only refine an already-clear TRANSITIONAL read). Noted
as a minor gap, not material to the AAPL verdict.

### Sector overlay (Technology)

AAPL is classified **Technology** (marketcap $4.53T). Tech-specific drivers
(AI capex cycle, China demand, services growth, tariff/supply-chain headlines) are
the swing factors but no scheduled tech catalyst lands in the next 30 days.

### Sector rotation (UW)

- **`sector-flow-persistence`: Technology = persistence_score 1.0, trend INFLOW**,
  net_flow rising $4.30B (5/20) → $8.50B (5/27). The strongest, most *durable*
  sector inflow on the board → **ALIGNED** for an AAPL long.
- **Apparent divergence:** market-regime's daily directional `sector_rotation`
  flags **Technology as the biggest one-day net OUTFLOW (−$433.5M)** while
  Comm Services (+$84M, where META sits) and Consumer Cyclical (+$49M, TSLA) take
  the inflow. Reconciliation: the persistence tool measures *gross/durable* sector
  premium (authoritative for rotation durability); the regime figure is a *narrow
  one-day directional* delta. **Verdict: rotation ALIGNED & durable, with a
  one-day directional wobble** — net favourable, lightly caveated.
- **`fz` breadth cross-check (advisory):** all-sector breadth **46.9% green**
  (236 adv / 263 decl, avg +0.01%), top mover APP +10.4% — roughly balanced,
  corroborating the weak-breadth read. *(Captured 2026-05-28T11:43Z, one day after
  as-of — advisory only, slight look-ahead, does not set bias.)* `[MACRO:sector_breadth fz EOD]`

### Cross-name correlation (computed from local close — UW tool broken)

The UW `portfolio-correlation` tool returned `sector: Unknown` / `high_correlations:
null` (known-broken). Computed pairwise daily-return correlation from local
screener `close` over the **33 available sessions** instead:

| Pair | Corr | Flag |
|------|------|------|
| **AAPL ↔ NVDA** | **0.736** | **CLUSTER (≥0.70)** — phase-9 cuts size `[MACRO:portfolio_correlation DUCKDB]` |
| NVDA ↔ BABA | 0.592 | none (just under soft-watch) |
| AAPL ↔ BABA | 0.480 | none |

Concurrent blueprints for 2026-05-27: **AAPL, NVDA, BABA** (NVDA & BABA dirs exist
for the date). AAPL +24.3% / NVDA +17.9% / BABA −5.5% over the window. **A
simultaneous long-AAPL + long-NVDA is effectively one mega-cap-tech beta bet** —
the cluster gate fires.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on Technology/AAPL |
|-----------|--------|---------|--------|---------------------------|
| Tech sector flow (5d persistence) | INFLOW, score 1.0 | 2026-05-27 | UW | **tailwind** |
| SPY trend | UPTREND, +4.93% 30d | 2026-05-27 | UW | mild tailwind |
| Market breadth | 37.1% bullish | 2026-05-27 | UW | **headwind** (narrow) |
| Regime | TRANSITIONAL (size down) | 2026-05-27 | UW | **headwind** (size cap) |
| CPI YoY / MoM | 3.78% / +0.64% | Apr 2026 | FRED | **headwind** (sticky infl.) |
| Fed funds / stance | 3.5–3.75%, hawkish split | 2026-04-29 | WebSearch:federalreserve.gov | **headwind** (cuts stalling) |
| 10y yield | 4.50% | 2026-05-26 | FRED | mild headwind (duration) |
| 2s10s | +0.48 (normal) | 2026-05-27 | FRED | neutral |
| Broad USD | 119.3 (flat) | 2026-05-22 | FRED | neutral |

## Catalyst calendar (next 30d)

**Front-expiry implied move ±1.19% / $3.69** on ~$311 spot `[CTX:implied_move_pct]`
— phase-9 sizes structures to this priced range; it is *small* (low IV).

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| ~mid-Jun 2026 | FOMC (next meeting) | rate hold likely; bias language is the risk | macro, can exceed ±1.19% intraday |
| ~mid-Jun 2026 | May CPI release | hot print = tech headwind | macro |
| 2026-07-30 | **AAPL Q3 earnings** | **the** AAPL binary — but **outside 30d** | front-expiry IV does not price it |
| — | AAPL ex-dividend | last ex 2026-05-11 (passed); next ~Aug | none near-term |

**No AAPL-specific binary inside 30 days** → consistent with low IV (6th %ile),
contango, complacent skew, and the long-gamma pin. The pin breaks on a macro
surprise or a tech-tape/headline shift, not a scheduled AAPL event.

## Tool / source errors

- `uw risk portfolio-correlation` returned `sector: Unknown` / `high_correlations:
  null` (known-broken — see memory `data-source-workarounds`). Worked around by
  computing correlation from local screener close (DuckDB), tagged accordingly.
- FRED reachable with key (Path A) — no errors. `fz groups` valuation view
  returned no parseable rows (advisory, graceful skip). DGS10/DGS2 show a `.`
  (no-print) on 2026-05-25 (holiday/weekend) — used adjacent trading day.

## Verdict for downstream

- **Net macro bias for AAPL:** **NEUTRAL, leaning size-down.** Durable tech inflow
  (tailwind) is offset by a TRANSITIONAL regime, sticky/re-accelerating inflation,
  a hawkish-split Fed, and weak breadth. The regime's explicit instruction —
  *reduce size, defined-risk, range structures* — is the dominant takeaway and it
  reinforces every other phase's range-bound read.
- **Conviction:** **3/5** (clear regime signal).
- **Top 2 datapoints phase-9 must cite:** (1) **TRANSITIONAL regime / 37.1%
  breadth** `[MACRO:MarketRegime_2026-05-27 UW]`; (2) **CPI YoY 3.78% re-accelerating**
  `[MACRO:CPIAUCSL_2026-04 FRED]`.
- **Top 2 catalysts for phase-9 calendar:** (1) next FOMC + May CPI (~mid-June,
  macro); (2) **AAPL earnings 2026-07-30 (outside near-term window — flag that the
  trade horizon ends before it).**
- **Sector-rotation verdict:** **ALIGNED** (Technology persistent INFLOW,
  persistence_score **1.0**) — favourable, with a one-day directional caveat.
- **Correlation verdict:** **CLUSTER — AAPL↔NVDA 0.736** (concurrent NVDA
  blueprint same date) → **phase-9 sizing gate must cut size.** AAPL↔BABA 0.48,
  NVDA↔BABA 0.59 (no additional flag).

Sources:
- [FOMC statement, April 29 2026 (federalreserve.gov)](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260429a.htm)
- [Fed holds rates steady amid dissent, April 2026 (CNBC)](https://www.cnbc.com/2026/04/29/fed-interest-rate-decision-april-2026.html)
