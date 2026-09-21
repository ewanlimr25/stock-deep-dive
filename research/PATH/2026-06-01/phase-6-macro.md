# Phase 6 — Macro Overlay

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:40:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The +12% move is now explained: **UiPath reported Q1 FY27 earnings (~2026-06-01) and
beat** — revenue ~$418M (+17% YoY), **first-ever GAAP operating profit**, **raised FY27
guidance to $1.776–1.781B**, ARR ~$1.9B, NRR 109% — so today's spike is a *fundamental
re-rate amplified by the 31% short float*, not a vacuum squeeze. The macro tape is
supportive but narrow: regime **TRANSITIONAL/UPTREND with weak breadth (40% bullish)**,
and the engine's own guidance is "**half position sizes, favor defined-risk, iron condors
in range**" — which lines up precisely with the long-gamma / premium-selling read of
phases 4–5. PATH's **sector is the single strongest tailwind**: Technology is the #1
net-inflow sector (+$13.1B today), persistence score **1**, accelerating five sessions
straight. The rates backdrop (CPI 3.78%, Core 2.74% disinflating, Fed funds 3.62% in a
cutting cycle, un-inverted 2s10s +0.42, VIX 16) is a soft-landing tailwind for
long-duration growth. Net macro bias: **mild tailwind**, but the next binary —
**FOMC 6/16–17 (dot plot) coincident with the Jun-18 OPEX cliff** — sits 16 days out and
should be sized for.

## Key signals

- **Catalyst = Q1 FY27 earnings beat** (rev +17%, first GAAP op profit, raised guide) —
  fundamental, not pure squeeze [MACRO:PATH_earnings_2026-06-01 WebSearch:stockstotrade.com]
- **Technology = #1 inflow sector** +$13.1B net today, persistence score **1**,
  accelerating → PATH sector **ALIGNED** [MACRO:sector_flow_2026-06-01 UW]
- **Regime TRANSITIONAL/UPTREND, breadth 40%** → "half size, defined-risk, iron condors"
  [MACRO:MarketRegime_2026-06-01 UW]
- **Soft-landing rates:** Core CPI YoY **2.74%**, Fed funds **3.62%** (cutting), 10y 4.45%,
  2s10s **+0.42 un-inverted**, VIX 16 [MACRO:CPILFESL_2026-04 FRED][MACRO:DFF_2026-05-29 FRED]
- **Next binary: FOMC 6/16–17 (dot plot) = Jun-18 OPEX cliff** (max-pain $11), 16d out
  [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov]

## Detailed findings

### Market regime (UW: SPY + VIX + breadth) `[MACRO:MarketRegime_2026-06-01 UW]`

- `regime` = **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"**;
  `trend` = UPTREND; `trading_guidance` = **"Half position sizes. Favor defined-risk
  strategies. Iron condors in range."**
- SPY $758.54, above 20/50 SMA, +5.55% 30d, −0.23% from 90d high (near highs).
- **Breadth weak:** 2,483 bullish vs 3,715 bearish tickers = **40.1% bullish** — a narrow,
  top-heavy tape (cross-checked by `fz` breadth pct_green **41.55%**, advancers 209 /
  decliners 294) [MACRO:sector_breadth fz EOD].
- VIX 10d **17.82 → 16.05** (low, declining) — risk-on/complacent, but falling IV feeds
  the phase-4 vanna "dealer selling" headwind.
- SPY 10d: $738.65 → $758.54 (+2.7%), 4 bull / 6 bear days, flow_direction_latest bearish.

### Inflation (FRED) `[MACRO:CPIAUCSL_2026-04 FRED][MACRO:CPILFESL_2026-04 FRED]`

| Series | Latest (Apr 2026) | YoY | Read |
|--------|-------------------|-----|------|
| CPI (CPIAUCSL) | 332.407 | **3.78%** | sticky-ish headline |
| Core CPI (CPILFESL) | 335.423 | **2.74%** | **disinflating toward target** |

Core at 2.74% supports the Fed's cutting path → constructive for long-duration growth.

### Labor (FRED) `[MACRO:PAYEMS_2026-04 FRED][MACRO:UNRATE_2026-04 FRED]`

- Nonfarm payrolls Apr **158,736k** (+115k MoM; Mar +185k) — modest, cooling but positive.
- Unemployment **4.3%** (steady 4.3–4.4% all year). A soft-but-stable labor market — the
  soft-landing signature.

### Rates (FRED) `[MACRO:DFF_2026-05-29 FRED][MACRO:DGS10_2026-05-29 FRED]`

- Fed funds effective **3.62%** (a cutting cycle vs the prior peak) — easing tailwind.
- 10y **4.45%**, 2y **3.98%**, **2s10s +0.42** (positively sloped / un-inverted — recession
  signal cleared). 10y at 4.45% is the one mild headwind for a long-duration growth name.

### Activity / Consumer

- ISM PMIs / U-Mich not separately pulled; the regime UPTREND + soft-landing rates picture
  is sufficient for a single-name overlay (marked neutral). No sector-specific macro shock.

### Sector overlay — Software / Automation / Agentic AI

- The bull narrative is sector-thematic: **agentic AI orchestration** ("UiPath for Coding
  Agents" — governing/testing coding agents like Claude Code inside CI/CD) and the
  WorkFusion AML/KYC tooling (Forrester named UiPath a Leader, Q2 2026 Document Mining
  Wave). PATH is riding the same AI-software bid lifting the Tech tape
  [MACRO:PATH_product_2026-05-28 WebSearch:timothysykes.com].
- `fz` Technology group valuation: sector P/E **41.6**, Fwd P/E 29.7, PEG 1.23, EPS next
  5Y +33.7%, **Change +2.96% today** (sector green) [MACRO:group_valuation fz EOD]. Rich
  but growth-justified; PATH's own valuation is a phase-7b question.

### Sector rotation (`sector-flow` + persistence)

- **Technology net flow today +$13,141,729,905** = **rank #1** of all sectors (next:
  Consumer Cyclical +$2.0B). Call premium $18.6B vs put $5.5B.
- **`sector-flow-persistence`: Technology persistence_score = 1 (max), trend INFLOW**,
  net flow rising 05-26 $8.7B → 06-01 $13.1B (accelerating).
- **Verdict: ALIGNED.** Smart money is rotating durably INTO PATH's sector — the strongest
  single confirmation in the deep dive. Caveat (phase-0.5): the *leaders* are semis
  (NVDA/MU/SNDK); PATH is software-adjacent, so it rides the tide rather than leading it.

### Cross-name correlation (`uw risk portfolio-correlation`)

- `ls research/*/2026-06-01/` → **PATH is the only blueprint for 2026-06-01**. **No
  concurrent positions to correlate against** → correlation gate **skipped** (not run with
  a single symbol). No cluster/soft-watch risk flagged.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on Software/Tech |
|-----------|--------|---------|--------|--------------------------|
| Technology net flow | +$13.1B (#1, persist 1) | 2026-06-01 | UW | **tailwind (strong)** |
| Core CPI YoY | 2.74% | 2026-04 | FRED | tailwind (rate-cut support) |
| Fed funds | 3.62% (cutting) | 2026-05-29 | FRED | tailwind |
| 2s10s | +0.42 (un-inverted) | 2026-06-01 | FRED | neutral→tailwind |
| 10y yield | 4.45% | 2026-05-29 | FRED | mild headwind (duration) |
| Market breadth | 40.1% bullish | 2026-06-01 | UW | headwind (narrow tape) |
| VIX | 16.05 (falling) | 2026-06-01 | UW | neutral (IV-crush risk) |
| Earnings beat + GAAP profit | Q1 FY27 | ~2026-06-01 | WebSearch | tailwind (already +12% priced) |

## Catalyst calendar (next 30d)

**Front-expiry implied (priced) move: ±6.32% / ≈$0.83** [CTX:implied_move_pct] — size
structures to this; each binary below reads against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-06-05 | Weekly OPEX (4 DTE) | gamma pin near $13 | inside ±6.3% |
| **2026-06-16/17** | **FOMC + dot plot/SEP** | rate-path repricing, broad | can exceed ±6.3% |
| **2026-06-18** | **Monthly OPEX cliff** (max-pain $11, 110k OI) | pin/un-pin; coincides w/ FOMC | the key date |
| 2026-09-03 | Next earnings (Q2 FY27) | — | outside 30d window |

The FOMC-day-into-OPEX cluster (6/16–18) is the dominant near-term risk node; the just-
passed earnings means **post-event IV crush** is the base case into it (premium-selling
edge, phase-5 VRP).

## Tool / source errors

- FRED returned **empty observation arrays for PCEPI, PCEPILFE, SOFR, DTWEXBGS** on this
  run (transient API/series issue; CPI covers inflation, DFF/DGS cover rates) — not
  re-chased; non-critical for a single-name overlay. All other series parsed clean.
- `uw historical trend --symbol VIX` returned a usable 10d print (17.82→16.05).

## Verdict for downstream phases

- **Net macro bias for PATH:** **mild TAILWIND** — Technology is the #1 persistent inflow
  sector and the rates/soft-landing backdrop supports growth; tempered by weak breadth
  (narrow tape) and the TRANSITIONAL "half-size / defined-risk" regime.
- **Conviction:** **3/5.**
- **Top 2 datapoints phase-9 must cite:** (1) Technology #1 inflow, persistence 1
  (ALIGNED); (2) regime TRANSITIONAL → "half size, defined-risk, iron condors in range."
- **Top 2 catalysts for phase-9 calendar:** (1) **FOMC 6/16–17 (dot plot)**; (2) **Jun-18
  monthly OPEX cliff** (max-pain $11) — they coincide.
- **Sector-rotation verdict:** **ALIGNED**, persistence_score **1** (durable INFLOW).
- **Correlation verdict:** **No concurrent positions** (PATH only blueprint for
  2026-06-01) — gate skipped, no cluster risk.
- **Open questions:** Does the earnings beat's quality survive the phase-7b fundamental
  veto (is the "first GAAP profit" durable or one-off)? And does the 31% short float
  (phase-7c) still have squeeze fuel after a +12% day, or is the easy covering done?
