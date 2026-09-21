# Phase 6 — Macro Overlay

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-5-historical.md

## Summary

The macro backdrop is a **mild-to-moderate headwind** into MU's print, though the
idiosyncratic earnings binary swamps it. The market regime is **TRANSITIONAL** — SPY below
its 20-DMA (733.58, −1.23% 30d), only **34.2% of names with bullish flow**, defensive
rotation into Consumer Defensive/Healthcare — and the engine's own guidance is "**half
position sizes, favor defined-risk strategies, iron condors in range**," which maps almost
exactly onto an earnings vol-structure approach. **Technology sold off −3.94% today** (`fz`)
and is the largest *directional* flow outflow (regime tool −$546.7M; phase-0.5 had semis as
the #1 bearish names) — yet on the gross measure Tech is the most-active sector (+$3.85B) and
a **persistent 5-day inflow magnet (persistence 0.8, INFLOW)**. Reconciliation: semis are
being **net-sold directionally today (de-risking into MU's print) inside a sector that is
richly valued (P/E 38.6) but not abandoned**. Rates/inflation are benign (10y 4.51%, core CPI
+2.82% YoY, unemployment 4.3%, normal +34bp curve) — a mild valuation headwind for a +268%-YTD
name, no acute stress. **No concurrent blueprints** for 2026-06-23 → correlation gate skipped.

## Key signals

- Regime **TRANSITIONAL**: SPY below 20-DMA, 34.2% bullish-flow breadth, defensive rotation; guidance "half size, defined-risk, iron condors" `[MACRO:MarketRegime_2026-06-23 UW]`
- **Technology −3.94% today** (`fz`), P/E 38.63 / Fwd 26.82 — rich and selling off `[MACRO:group_valuation fz EOD]`
- Tech is biggest **directional outflow −$546.7M** (regime rotation) yet **persistent 5-day INFLOW (0.8)** on gross flow — sold today, not abandoned `[MACRO:sector_flow_persistence UW]`
- Rates benign: 10y **4.51%**, 2y 4.24%, **2s10s +0.34** (normal, steepening), Fed funds 3.63% `[MACRO:DGS10_2026-06-22 FRED]` `[MACRO:T10Y2Y_2026-06-23 FRED]`
- Breadth divergence: `fz` **56.9% of stocks green** on price but UW **34.2% bullish flow** — prices up, options flow defensive (caution) `[MACRO:sector_breadth fz EOD]`

## Detailed findings

### Market regime (UW) — `[MACRO:MarketRegime_2026-06-23 UW]`

- `regime` = **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"**;
  `trading_guidance` = "Half position sizes. Favor defined-risk strategies. Iron condors in range."
- `market_breadth`: bullish_flow 2,132 vs bearish_flow 4,104 tickers → **bullish_pct 34.2%** (broadly bearish flow).
- `spy`: current 733.58, above_50sma true / **above_20sma false**, change_30d −1.23%, −3.53% from 90d high; trend "PULLBACK".
- `sector_rotation`: OUT = **Technology −$546.7M**, Consumer Cyclical −$105.3M, Financial −$20.5M; IN = Consumer Defensive +$7.0M, Healthcare, Real Estate (defensive).

### SPY recent action — `[MACRO:trend_SPY UW]`

10-day: price 737.05 → 733.58, bullish_days 5 / bearish_days 5, flow_direction_latest **bearish**, iv_rank 34.8 → 36.1 (low absolute market vol — the vol is idiosyncratic to MU, not systemic).

### Rates / inflation / labor (FRED) — `[MACRO:* FRED]`

| Series | Latest | Date | Read |
|---|---|---|---|
| DGS10 (10y) | **4.51%** | 2026-06-22 | mild valuation headwind for rich growth |
| DGS2 (2y) | 4.24% | 2026-06-22 | — |
| T10Y2Y (2s10s) | **+0.34** (from +0.27) | 2026-06-23 | normal/positive, steepening (un-inverted) — benign |
| DFF (fed funds) | 3.63% | 2026-06-22 | mid-cycle (cut from peak) |
| CPILFESL (core CPI) | 336.121 vs 326.893 → **+2.82% YoY** | 2026-05 | moderating toward target — neutral |
| UNRATE | **4.3%** (flat YoY) | 2026-05 | stable labor — neutral |

Net: a **soft-landing / mid-cycle** macro. Nothing here is an acute semis catalyst; rates at
4.5% are a slow valuation drag on a 38× sector, not a near-term driver of MU's print.

### Sector overlay (semis) — `[MACRO:sector_flow UW]` `[MACRO:group_valuation fz EOD]`

- `options-flow sector-flow`: Technology **net_flow +$3.85B** — #1 sector by gross premium
  (Tech is always the most-trafficked; this is magnitude, not direction).
- `fz groups`: Technology **P/E 38.63, Fwd P/E 26.82, Change −3.94% today** — rich and red.
- Phase-0.5 cross-ref: semis own the bearish directional tape (MU/NVDA/SOXL/AMD/INTC/MRVL/
  SNDK/AVGO all top-12 bearish). The semi complex de-risked today, MU the leader (−12%).

### Sector rotation (durability) — `[MACRO:sector_flow_persistence UW]`

Technology `net_flow_by_day`: 06-16 +$5.13B, 06-17 −$0.07B, 06-18 +$9.36B, 06-22 +$6.76B,
06-23 +$3.85B → `persistence_score` **0.8**, `trend` **INFLOW** (positive 4 of 5 sessions).
**Verdict: ADVERSE-near-term / NEUTRAL-structural** — today's *directional* semis flow is
bearish (adverse to a long), but the sector remains a persistent gross-inflow magnet (not a
sector being exited). `fz` breadth cross-check: market 56.9% green but Tech −3.94% and UW
flow 34.2% bullish — the price-vs-flow divergence corroborates "defensive under the surface."

### Cross-name correlation — `[MACRO:portfolio_correlation UW]`

`ls research/*/2026-06-23/` → **MU is the only blueprint for this date**. No concurrent
positions to correlate against; correlation gate **skipped** (not a cluster risk).

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Semis/MU |
|---|---|---|---|---|
| Core CPI YoY | +2.82% | 2026-05 | FRED | neutral |
| Unemployment | 4.3% | 2026-05 | FRED | neutral |
| 10y yield | 4.51% | 2026-06-22 | FRED | mild headwind (valuation) |
| 2s10s | +0.34 (normal) | 2026-06-23 | FRED | neutral |
| Fed funds | 3.63% | 2026-06-22 | FRED | neutral (mid-cycle) |
| Market regime | TRANSITIONAL / reduce size | 2026-06-23 | UW | **headwind** |
| SPY vs 20-DMA | below (−1.23% 30d) | 2026-06-23 | UW | headwind |
| Tech sector today | **−3.94%** | 2026-06-23 | fz | **headwind (near-term)** |
| Tech directional flow | −$546.7M out | 2026-06-23 | UW | **headwind (today)** |
| Tech 5-day persistence | INFLOW 0.8 | 2026-06-16→23 | UW | tailwind (structural) |

## Catalyst calendar (next 30d)

**Front-expiry implied (priced) move: ±10.91% / ±$114.7** on a $1051.77 close
(`[CTX:implied_move_pct]`, phase-0.5) → ~$937 to ~$1166. Phase-9 sizes structures to this range.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-06-24 (postmarket)** | **MU fiscal-Q3 earnings (THE catalyst)** | binary gap, IV crush | **IS the ±10.91% expected move** |
| 2026-06-26 | Post-earnings weekly OPEX (19.4% of OI, max-pain $1050) | gamma/pin resolution | settles within/beyond the move |
| ~2026-07 (TBD) | Next FOMC / CPI (dates not confirmable on this as-of) | macro re-rate | secondary to the print |

> Note: a live macro-event search (FOMC/CPI exact dates) was **not** run — on this as-of the
> only reliable, point-in-time sources are FRED (used above) and the UW substrate; WebSearch
> would risk anachronistic results. The 06-24 earnings binary dominates the 30-day window.

## Tool / source errors

- FRED **used** (`FRED_API_KEY` present in repo `.env`) — rates/inflation/labor pulled via the
  JSON API (Path A). Daily series (DGS10/DGS2/DFF) show the latest *valued* obs is 2026-06-22
  (06-19 is a non-trading "." placeholder) — expected, not an error.
- WebSearch priority-3 macro-event pull intentionally skipped (anachronism risk on this
  as-of); FRED covered the quantitative backdrop.

## Verdict for downstream phases

- **Net macro bias for MU:** **HEADWIND (mild-moderate)** — risk-off TRANSITIONAL regime +
  semis sold directionally today + rich sector valuation; rates/inflation benign. The binary
  earnings event dominates; macro is a size-down argument, not a direction.
- **Conviction:** **3/5** (clear risk-off regime + tech −3.94%, but low systemic vol and a
  still-inflowing sector temper it).
- **Top 2 datapoints phase-9 must cite:** (1) Regime **TRANSITIONAL — "half size, defined-risk,
  iron condors"**; (2) **Tech −3.94% today / −$546.7M directional outflow** (semis de-risking
  into the print).
- **Top 2 catalysts for phase-9 calendar:** (1) **2026-06-24 postmarket MU earnings** (±10.91%);
  (2) **2026-06-26 weekly OPEX** (max-pain $1050, 19.4% of OI).
- **Sector-rotation verdict:** **ADVERSE (near-term)** for a long, **persistence 0.8** — semis
  net-sold today though the sector still draws gross inflow; aligns with caution/short lean,
  argues against a naked long. (phase-9 sizing gate input.)
- **Correlation verdict:** **No concurrent positions** (MU is the only 2026-06-23 blueprint) —
  no cluster, no soft-watch; gate not applicable.
