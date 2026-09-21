# Phase 6 — Macro Overlay

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro splits by horizon, matching phases 4–5. **Medium-term backdrop is a TAILWIND
for long-duration tech:** disinflation is intact (headline CPI **−0.42% MoM**, core CPI
flat), the Fed is easing (funds **3.63%**, range 3.50–3.75%), the **2y is falling**
(4.26→4.16 in a week, more cuts priced), **2s10s is positive +0.37** (curve
normalized), and the dollar is soft. **But the immediate regime is TRANSITIONAL /
CHOPPY** — SPY 743 is below its 20- and 50-day SMAs and −2.25% from its 90d high, VIX
has risen **15.6 → 18.8** in 10 sessions, and breadth is weak (**38.4% bullish flow**;
fz **29% green**). UW's own guidance: *"Half position sizes. Favor defined-risk
strategies."* Crucially for a SHOP short: **Technology is the #1 durable inflow sector**
(+$98.6M rotation in today, +$1.17B net flow, **persistence 0.8**) — fading SHOP fights
its sector. And **SHOP correlates 0.707 with PATH**, a concurrent blueprint → a
**cluster** flag. No catalyst lands before next-week (7/24) expiry; FOMC (7/29) and
SHOP earnings (8/5) sit just beyond it.

## Key signals

- **Regime TRANSITIONAL/CHOPPY** — SPY below 20/50 SMA, VIX 15.6→18.8, half-size
  guidance. `[MACRO:MarketRegime_2026-07-17 UW]`
- **Technology = #1 inflow sector, durable** (+$98.6M today, net flow +$1.17B,
  persistence 0.8, INFLOW) → **adverse for a SHOP short**. `[MACRO:SectorFlow_2026-07-17 UW]`
- **SHOP/PATH correlation 0.707 → CLUSTER** (PATH is a concurrent 7/17 blueprint). `[MACRO:PortfolioCorr_2026-07-17 UW]`
- **Disinflation + easing**: CPI −0.42% MoM, Fed funds 3.63%, 2y 4.16% falling, 2s10s
  +0.37 → medium-term tech tailwind. `[MACRO:CPIAUCSL_2026-06 FRED] [MACRO:DGS2_2026-07-16 FRED]`
- **Catalysts beyond the 7/24 window**: FOMC 7/29, SHOP earnings 8/5. `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov] [MACRO:SHOP_Q2_2026-08-05 WebSearch:stocktitan.net]`

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-17 UW]`

`regime = "TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"`.
SPY 743.29 (below 20sma 745.02 & 50sma 744.38, −0.94% 30d, −2.25% from 90d high),
trend **CHOPPY**, guidance *"Half position sizes. Favor defined-risk strategies. Iron
condors in range."* Breadth: **2,420 bullish vs 3,878 bearish** flow tickers = **38.4%
bullish** (weak). VIX **15.57 → 18.77** over 10d (rising ~20% → risk premium building).

### Inflation `[MACRO:CPIAUCSL_2026-06 FRED] [MACRO:CPILFESL_2026-06 FRED] [MACRO:PCEPILFE_2026-05 FRED]`

- Headline CPI: Jun 332.568 vs May 333.979 = **−0.42% MoM** (outright decline — soft print).
- Core CPI: Jun 336.065 vs May 336.121 = **~flat** (cooling).
- Core PCE (latest May): 130.082 vs Apr 129.667 = +0.32% MoM.
→ **Disinflationary** — supports the easing path. **TAILWIND** for growth multiples.

### Labor `[MACRO:PAYEMS_2026-06 FRED] [MACRO:UNRATE_2026-06 FRED]`

Payrolls Jun 158,984k vs May 158,927k = **+57k MoM** (soft but positive); unemployment
**4.2%** (down from 4.3%). Cooling, not cracking → **soft-landing, NEUTRAL-to-tailwind**.

### Rates `[MACRO:DFF_2026-07-16 FRED] [MACRO:DGS10_2026-07-16 FRED] [MACRO:DGS2_2026-07-16 FRED] [MACRO:T10Y2Y_2026-07-17 FRED]`

Fed funds effective **3.63%** (range 3.50–3.75%). 10y **4.57%** (from 4.62 on 7/13,
easing). 2y **4.16%** (from 4.26, falling faster → more cuts priced). **2s10s +0.37**
(normalized/steepening). Dollar (DTWEXBGS) **120.50**, softening. → **TAILWIND** for
long-duration growth like SHOP.

### Activity / Consumer

Not separately pulled (single-name overlay; FRED rate/inflation/labor sufficient).
ISM/U-Mich would only refine, not change, the disinflation+easing read. Skipped per
scope.

### Sector overlay + rotation `[MACRO:SectorFlow_2026-07-17 UW] [MACRO:SectorFlowPersistence UW]`

- **Technology net flow +$1.17B today** (call prem $7.94B / put prem $6.76B) — the
  strongest sector inflow. Rotation IN: Tech +$98.6M, Energy +$30M, Comm Svcs +$29.7M;
  OUT: Financials −$57M, Consumer Cyclical −$45M.
- **Persistence 0.8, trend INFLOW** — net_flow_by_day 7/13…7/17: +1.21B, +2.78B,
  +2.26B, **−3.36B**, +1.17B (4 of 5 up) → **durable** Tech inflow.
- **fz breadth cross-check** `[MACRO:sector_breadth fz EOD]`: market **29.2% green**
  (147 adv / 356 dec); **Technology group price −1.09% today** (P/E 35.2, Fwd P/E 25.9,
  P/S 7.48, PEG 0.91) `[MACRO:group_valuation fz EOD]`. So Tech was **red on price but
  bid on flow** — smart money buying the dip. SHOP −1.2% ≈ its sector's −1.09% (its
  price weakness is largely tape/sector; the divergence is in its **flow**, which is
  net-bearish while the sector's is net-bullish).
- SHOP valuation stretch: mcap $160.3B / sales $12.4B ≈ **13× sales** (vs Tech group
  7.5×) → a premium name; sensitive to multiple compression on any risk-off leg.
- **Rotation verdict vs a bearish SHOP thesis: ADVERSE** (sector durably bought).

### Cross-name correlation `[MACRO:PortfolioCorr_2026-07-17 UW]`

Correlated against concurrent 7/17 blueprints **OKLO, PATH** (`--lookback-days 30`):
**SHOP/PATH = 0.707 → CLUSTER (≥0.70)**. SHOP/OKLO not flagged (<0.60). Sector field
returned "Unknown" for all three — the **known UW correlation sector-field bug**; the
coefficient 0.707 is valid. → phase-9 **cuts size** if SHOP and PATH are taken the same
direction.

## Tailwind / Headwind table

| Datapoint | Latest value | Release/asof | Source | Impact on Technology/SHOP |
|---|---|---|---|---|
| Headline CPI MoM | −0.42% | Jun 2026 | FRED | **Tailwind** (disinflation) |
| Core CPI MoM | ~flat | Jun 2026 | FRED | Tailwind |
| Fed funds | 3.63% (3.50–3.75) | 2026-07-16 | FRED | **Tailwind** (easing) |
| 2y yield | 4.16% (falling) | 2026-07-16 | FRED | **Tailwind** |
| 2s10s | +0.37 | 2026-07-17 | FRED | Tailwind (normalized) |
| USD (broad) | 120.50 (soft) | 2026-07-10 | FRED | Mild tailwind |
| Market regime | TRANSITIONAL/CHOPPY | 2026-07-17 | UW | **Headwind (near-term)** |
| VIX | 15.6→18.8 | 2026-07-17 | UW | Headwind (near-term) |
| Breadth (bullish flow) | 38.4% | 2026-07-17 | UW | Headwind |
| Tech sector rotation | +$98.6M, persistence 0.8 | 2026-07-17 | UW | **Adverse to SHOP short** |
| SHOP P/S | ~13× (vs sector 7.5×) | 2026-07-17 | fz | Headwind on risk-off |

## Catalyst calendar (next 30d)

Front-expiry implied move: the screener `implied_move_perc` (0.49%) is **unreliable**
(phase-4 flagged; inconsistent with IV 75% / RV 45%). RV-based **1-week expected move
≈ ±6% (~$7–8)**, roughly the phase-3 116–130 structural range. **No scheduled catalyst
inside the 7/24 tradeable window** — the near-term fade is a pure flow/positioning play.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| 2026-07-29 | **FOMC** (no SEP) | Rate hold/cut; broad tech beta | Beyond 7/24 expiry |
| 2026-08-05 (BMO) | **SHOP Q2 earnings** | Major idiosyncratic binary | Beyond 7/24; large move risk |

## Tool / source errors

<none> — FRED key present, all series returned. `fz groups` needed a flexible
`jq` path (rows are a bare array, not under `.rows`); resolved. UW correlation sector
field "Unknown" is the documented bug (coefficients valid).

## Verdict for downstream phases

- **Net macro bias for SHOP:** **split** — medium-term **TAILWIND** (disinflation +
  easing + durable Tech inflow), near-term **HEADWIND/CHOPPY** (transitional regime,
  weak breadth, rising VIX). For a **near-term bearish fade**: broad tape is
  supportive (risk-off chop can drag SHOP), but **sector rotation is ADVERSE**.
- **Conviction:** 3/5.
- **Top 2 datapoints phase-9 must cite:** (1) regime TRANSITIONAL + "half position
  sizes" guidance; (2) Technology durable inflow (+$98.6M, persistence 0.8) = adverse
  to a short.
- **Top 2 catalysts for the calendar:** FOMC 2026-07-29; SHOP Q2 earnings 2026-08-05
  (BMO). Both **after** the 7/24 window — a near-term trade must be closed or rolled
  before 8/5.
- **Sector-rotation verdict:** **ADVERSE** (to a bearish thesis), persistence **0.8**.
- **Correlation verdict:** **SHOP/PATH = 0.707 → CLUSTER** (phase-9 size cut vs the PATH
  blueprint); OKLO no flag.
