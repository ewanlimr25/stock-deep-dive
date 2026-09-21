# Phase 6 — Macro Overlay

**Ticker:** PATH (UiPath Inc., Technology / AI-automation software)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:15:43Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro is a **net headwind** for PATH. The **FOMC held at 3.50–3.75% on 2026-06-17 (the day
before as-of) but flipped HAWKISH** — the dot plot now signals **≥1 hike in 2026** (median
3.8%, up from 3.4%), erasing the prior cut and pushing easing into 2027–28, citing an
inflation spike from the Iran war / global energy prices. That is adverse for a beaten-down,
duration-sensitive AI-software name. The UW regime is **TRANSITIONAL** ("half position
sizes, favor defined-risk") with weak breadth (38.6% bullish). The one offset is that
**Technology is the top sector inflow** (+$629M net, persistence 0.8 — durable), but per
phase-0.5 that leadership is **semis-led** (top mover SNDK) and **PATH is not
participating**. PATH~MARA correlation is **0.079** (the only concurrent blueprint) — **no
cluster, fully diversified**.

## Key signals

- **FOMC hawkish flip (2026-06-17):** hold 3.50–3.75%, dot plot → ≥1 hike 2026, cuts to
  2027–28, inflation/Iran-energy driven [MACRO:FOMC_2026-06-17 WebSearch:federalreserve.gov].
- **Regime TRANSITIONAL:** "Half position sizes. Favor defined-risk." breadth 38.6% bullish
  [MACRO:MarketRegime_2026-06-18 UW].
- **Technology sector inflow, durable:** sector-flow net +$9.36B (largest); regime
  money_in Technology +$629M; persistence 0.8 — but semis-led, PATH absent [MACRO:sector_flow UW][MACRO:sector_flow_persistence UW].
- **Risk backdrop mixed:** SPY 746.74 (+1.8% from 90d high, above 50sma/below 20sma), VIX
  **16.4 and falling** (21.5→16.4) [MACRO:SPY_2026-06-18 UW][MACRO:VIX_2026-06-18 UW].
- **No cluster:** PATH~MARA daily-return corr **0.079** (n=48) [MACRO:correlation DUCKDB].

## Detailed findings

### Market regime (UW) — `[MACRO:MarketRegime_2026-06-18 UW]`

regime **TRANSITIONAL — "Mixed signals, reduce position size, wait for clarity"**;
trading_guidance **"Half position sizes. Favor defined-risk strategies. Iron condors in
range."**; trend PULLBACK_IN_UPTREND. SPY 746.74 (above_50sma true, above_20sma false,
+1.77% 30d, −1.8% from 90d high). Breadth: bullish_pct **38.6%** (2,421 bullish vs 3,853
bearish of 6,274) — **weak**.

### Inflation (FRED) — `[MACRO:CPIAUCSL_2026-05 FRED]`

| Series | Latest | YoY |
|--------|--------|-----|
| CPI (CPIAUCSL) | 333.979 (May 2026) | **+4.3%** (elevated) |
| Core CPI (CPILFESL) | 336.121 (May 2026) | **+3.0%** |
| Core PCE (PCEPILFE) | 129.63 (Apr 2026) | — |

Inflation elevated (energy/Iran spike per FOMC) — the reason for the hawkish pivot. Headwind.

### Labor (FRED) — `[MACRO:PAYEMS_2026-05 FRED][MACRO:UNRATE_2026-05 FRED]`

NFP **+172k MoM** (May 2026; level 159,001k); Unemployment **4.3%** (stable). Solid labor →
supports the Fed's no-cut stance (headwind for rate-cut hopes).

### Rates (FRED + FOMC) — `[MACRO:DFF_2026-06-17 FRED][MACRO:DGS10_2026-06-17 FRED]`

Fed funds effective **3.63%** (in the 3.50–3.75 band). DGS10 **4.49%** (down from 4.67% 30d
ago — but the 6/17 hawkish surprise pressures yields back up). DGS2 4.20%. **2s10s +0.27**
(T10Y2Y, normalized/positive — un-inverted). FOMC dot plot **flipped to a hike** (median
end-2026 3.8%). Net: the rate path turned **less friendly to duration/growth**.

### Activity / Consumer

Not separately pulled (advisory; FOMC characterizes activity as "expanding at a solid pace"
despite Middle East uncertainty). No incremental signal needed for this single-name overlay.

### Sector overlay (Technology / AI software)

PATH is enterprise AI-automation software — **long-duration, valuation-sensitive**. The
hawkish Fed + elevated inflation + Iran-energy risk-off is a **headwind** for the
unprofitable-growth software cohort specifically (worse than for cash-rich mega-cap tech or
the semis catching the AI-capex bid).

### Sector rotation (UW) — `[MACRO:sector_flow UW][MACRO:sector_flow_persistence UW]`

- Technology net sector flow **+$9.36B today** (largest of all sectors); regime
  money_flowing_in Technology **+$629M**. Persistence score **0.8** (durable, 4/5 sign-consistent).
- **Verdict: `aligned` (sector tailwind) — BUT semis-led, PATH not participating.** Per
  phase-0.5, PATH is outside top-50 on every directional metric while MU/SNDK/INTC/MRVL lead.
  The sector inflow does **not** accrue to PATH directly.
- **fz breadth cross-check (advisory):** advancers 264 / decliners 238, pct_green **52.49%**,
  top_mover **SNDK** (semiconductor) — corroborates a *semis-led* tech tape, not software
  [MACRO:sector_breadth fz EOD]. (`fz groups` valuation view did not parse — skipped.)

### Cross-name correlation (UW + DuckDB) — `[MACRO:correlation DUCKDB]`

Concurrent blueprints for 2026-06-18: **MARA**. `uw risk portfolio-correlation PATH,MARA`
returned `high_correlations: null` (sector field "Unknown" — known broken). DuckDB
return-correlation over 48 sessions: **PATH~MARA = 0.079** → far below the 0.60 soft-watch
threshold. **No cluster; the two positions are diversified.**

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Tech/AI-software |
|-----------|--------------|--------------|--------|----------------------------|
| FOMC hawkish dot-plot flip | hold 3.50–3.75%, ≥1 hike 2026 | 2026-06-17 | WebSearch:federalreserve.gov | **headwind** |
| CPI YoY | 4.3% | 2026-05 | FRED | headwind |
| Core CPI YoY | 3.0% | 2026-05 | FRED | mild headwind |
| Fed funds effective | 3.63% | 2026-06-17 | FRED | headwind (no cuts) |
| 10y yield | 4.49% (↓ from 4.67% 30d) | 2026-06-17 | FRED | neutral (may reverse up) |
| 2s10s | +0.27 (normalized) | 2026-06-18 | FRED | neutral-positive |
| VIX | 16.4 (↓ from 21.5) | 2026-06-18 | UW | tailwind (aids vanna-bid if it holds) |
| Technology sector flow | +$9.36B, persistence 0.8 | 2026-06-18 | UW | tailwind (sector) — but PATH absent |
| Market regime | TRANSITIONAL, half-size | 2026-06-18 | UW | headwind (sizing) |
| Breadth | 38.6% bullish | 2026-06-18 | UW | headwind |

## Catalyst calendar (next 30d)

**Front-expiry implied (expected) move: ±2.06% / ±$0.21** [CTX:implied_move]. Phase-9 sizes
structures to this priced range; binaries below read against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-06-17 (passed, day before as-of) | FOMC hold + hawkish dot-plot | headwind (already absorbed) | — |
| ~2026-07-15 | June CPI release | high — inflation path post-Iran | could exceed ±2.06% |
| ~2026-07-28/29 | Next FOMC meeting | high — hike risk live | could exceed ±2.06% |
| ongoing | Iran / Middle East conflict, energy prices | risk-off swing factor (VIX, duration) | tail risk |
| **2026-09-08** | **UiPath Q2 FY2027 earnings** | **outside 30d window** | n/a near-term |

**No PATH-specific earnings catalyst in the next 30 days** (Q1 FY2027 already reported early
June → consistent with the iv_rank crush 70.9→34.6, phase-5). Near-term path is macro-driven.

## Tool / source errors

- `uw risk portfolio-correlation` sector field returns "Unknown" (known-broken per project
  memory) and `high_correlations: null`; coefficient computed via DuckDB instead.
- `fz groups --by sector --view valuation` did not parse a Technology row — skipped (advisory).
- FRED CPI YoY required explicit `observation_start` to avoid a stray "." value; recomputed cleanly.

## Verdict for downstream

- **Net macro bias for PATH:** **HEADWIND** (hawkish Fed flip + elevated inflation + Iran
  risk-off + TRANSITIONAL half-size regime outweigh the semis-led tech inflow PATH isn't capturing).
- **Conviction:** **3/5.**
- **Top 2 datapoints phase-9 must cite:** (1) **FOMC 2026-06-17 hawkish dot-plot flip** (≥1
  hike 2026) — duration headwind; (2) **TRANSITIONAL regime, "half position sizes"** — explicit
  sizing cap.
- **Top 2 catalysts for phase-9 calendar:** (1) **Next FOMC ~2026-07-28/29** (hike risk live);
  (2) **June CPI ~2026-07-15** + ongoing **Iran/energy** risk-off. (No PATH earnings until ~Sept 8.)
- **Sector-rotation verdict:** **`aligned` (Technology inflow, persistence 0.8)** — BUT
  semis-led and **PATH not participating**, so treat the tailwind as not fully accruing
  (effectively neutral-for-PATH). Phase-9 sizing input: aligned/0.8 with the participation caveat.
- **Correlation verdict:** **No cluster, no soft-watch.** PATH~MARA = 0.079 (n=48). One
  concurrent blueprint (MARA); diversified.
