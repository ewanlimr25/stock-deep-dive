# Phase 6 — Macro Overlay

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:38:00-04:00
**Upstream phases cited:** phase-2-dark-pool.md, phase-0.5-context.md, phase-5-historical.md

## Summary

Macro is **neutral-to-mild-tailwind** for PATH, but the tape is cautious. The UW
regime is **TRANSITIONAL** with SPY in a shallow uptrend ($749, +3.3% 30d, above
20/50-SMA) yet **weak breadth (33.8% bullish flow)** and a **defensive rotation**
today (money into Energy/Healthcare/Utilities; regime tool flags Tech directional
premium −$516M). The saving grace: the **5-session sector-flow-persistence shows
Technology in durable INFLOW (persistence score 1, positive every day 07-07→07-13)** —
medium-term smart money is leaning into tech even as today's snapshot cools.
Rates are supportive: Fed funds **3.62%** (easing cycle), 2s10s **+0.36 (normal)**,
core CPI **2.82% YoY** and core PCE **3.41% YoY** (moderating), unemployment **4.2%**
(solid) — a falling-rate backdrop that helps long-duration software valuations.
**Critically, the 07-09 mega-block has NO public offering or 13D/activist filing** —
it coincided with a *bullish* PATH catalyst (Maestro Case AI launch, stock +3.33%
that day), which argues against the distribution/offering interpretation and for
genuine accumulation (or a neutral portfolio-transition cross). No PATH binary
catalyst inside 30 days (earnings 2026-09-03). Conviction 3/5.

## Key signals

- **Regime TRANSITIONAL** — "Half position sizes. Favor defined-risk strategies. Iron condors in range" `[MACRO:MarketRegime_2026-07-13 UW]`; SPY UPTREND but breadth weak.
- **Breadth weak: 33.8% bullish** (2,116 bullish vs 4,149 bearish of 6,265 optionable) `[MACRO:MarketRegime_2026-07-13 UW]` — broadly defensive tape.
- **Technology sector-flow-persistence: INFLOW, score 1** (net +$1.2B–$4.1B/day, 07-07→07-13) `[MACRO:SectorPersistence_2026-07-13 UW]` — durable tech inflow = medium-term aligned for PATH.
- **07-09 block un-attributed to any offering/13D** — coincided with Maestro Case AI launch, PATH +3.33% `[MACRO:UiPath_2026-07-09 WebSearch:stockstotrade.com]` — supports accumulation over distribution.
- **Rates easing / curve normal**: DFF 3.62%, 2s10s +0.36, core PCE 3.41% YoY moderating `[MACRO:DFF/T10Y2Y_2026-07-13 FRED]` — duration tailwind for software.

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-13 UW]`
- regime **TRANSITIONAL**; trend **UPTREND**; SPY $749.17, above 20-SMA ($744.4) & 50-SMA ($742.0), +3.27% 30d, −1.48% from 90d high.
- breadth: bullish_pct **33.8%** (weak). guidance: half size, defined-risk, iron condors.

### Inflation (FRED) `[MACRO:CPILFESL/PCEPILFE_2026-05 FRED]`
- Core CPI (May): 336.121, **YoY +2.82%** (MoM +0.21%). Approaching target.
- Core PCE (May): 130.082, **YoY +3.41%** (MoM +0.32%). Still mildly sticky but easing.

### Labor (FRED) `[MACRO:UNRATE_2026-06 FRED]`
- Unemployment **4.2%** (Jun), down from 4.3% (May/Apr). Solid, no recession signal.

### Rates (FRED) `[MACRO:DFF/DGS10/DGS2/T10Y2Y_2026-07 FRED]`
- Fed funds effective **3.62%** (easing cycle underway). 10y **4.56%**, 2y **4.21%**, **2s10s +0.36 (normalized, un-inverted)**. Mildly restrictive-to-neutral; disinflation + easing = duration-friendly.

### Sector overlay (software / enterprise-automation)
- PATH-specific: **Maestro Case** AI-native case-management launch (07-09) drove +3.33%; earlier July coverage noted "AI wins meet analyst caution." Product momentum is real; sell-side is cautious on valuation. AI-automation theme is a live tailwind.

### Sector rotation (`sector-flow` + persistence)
- Today's `sector-flow`: Technology **net_flow +$1.21B** (call prem $6.19B vs put $4.98B) — gross-positive.
- Regime `sector_rotation.money_flowing_out`: **Technology −$516M** (largest outflow) vs inflows to Energy/Healthcare/Utilities — a *defensive* one-day tilt.
- `sector-flow-persistence`: Technology **trend INFLOW, persistence_score 1**, positive net flow 5/5 sessions ($1.4B → $2.8B → $3.2B → $4.1B → $1.2B).
- **Verdict: ALIGNED (medium-term)** — durable tech inflow supports a constructive PATH lean; tempered by today's defensive snapshot and phase-0.5's finding that *software specifically* was mid-pack. Call it **aligned but not a strong tailwind.**
- `fz` breadth cross-check skipped — `fz breadth`/`groups` not pulled cleanly for this sector cut; UW persistence stands.

### Cross-name correlation
- **No concurrent positions** — PATH is the only blueprint for 2026-07-13 (`ls research/*/2026-07-13/`). Correlation gate skipped; no cluster risk.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on Software |
|-----------|--------|---------|--------|--------------------|
| Fed funds effective | 3.62% (easing) | 2026-07-10 | FRED | tailwind (duration) |
| Core PCE YoY | 3.41% | 2026-05 | FRED | neutral (sticky but easing) |
| Core CPI YoY | 2.82% | 2026-05 | FRED | tailwind (near target) |
| Unemployment | 4.2% | 2026-06 | FRED | neutral/tailwind |
| 2s10s | +0.36 (normal) | 2026-07-13 | FRED | neutral |
| Market breadth | 33.8% bullish | 2026-07-13 | UW | headwind (weak) |
| Tech sector persistence | INFLOW, score 1 | 2026-07-13 | UW | tailwind (medium-term) |
| Today's sector tilt | Tech −$516M, defensive | 2026-07-13 | UW | headwind (near-term) |
| PATH AI catalyst (Maestro Case) | +3.33% | 2026-07-09 | WebSearch | tailwind |

## Catalyst calendar (next 30d)

Front-expiry implied move **±5.3% / ≈±$0.63** `[CTX:implied_move_pct]` — size structures to this range.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| ~mid-late Jul 2026 | CPI print (June) | rates read-through | market-level; indirect |
| ~late Jul 2026 | FOMC meeting (approx.) | easing-path signal | market-level; indirect |
| **2026-09-03** | **PATH earnings** | **binary — OUTSIDE 30d** | far exceeds ±5.3% when it lands |
| ongoing | AI-automation product news | idiosyncratic tailwind | can exceed ±5.3% intraday |

**No PATH binary inside 30 days** — this is not an earnings play; the horizon is a technical/flow-driven swing inside the long-gamma box.

## Tool / source errors

- FRED key present and working (repo `.env`). All series returned.
- `fz breadth --group sector` returns a single aggregate object (not per-sector); PATH-sector breadth cross-check omitted — advisory only, no impact on verdict.

## Verdict for downstream

- **Net macro bias for PATH:** **NEUTRAL-to-mild-TAILWIND.** Easing rates + disinflation + durable tech inflow + a live AI catalyst vs weak breadth + cautious "half-size" regime + today's defensive rotation.
- **Conviction:** 3/5.
- **Top 2 datapoints phase-9 must cite:** (1) Regime TRANSITIONAL / breadth 33.8% bullish → "half position sizes, defined-risk"; (2) 07-09 block has **no offering/13D** and coincided with a **+3.33% AI-catalyst day** → accumulation-consistent, not distribution.
- **Top 2 catalysts for phase-9 calendar:** (1) **No binary inside 30d** (earnings 2026-09-03); (2) front-expiry implied move ±5.3% — the box the trade lives in.
- **Sector-rotation verdict:** **ALIGNED**, persistence_score **1** (durable tech inflow) — mild positive sizing input, not a strong tailwind (software mid-pack today).
- **Correlation verdict:** **No concurrent positions** (PATH only blueprint for the date) — no cluster/soft-watch; gate not applicable.
