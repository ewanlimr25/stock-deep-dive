# Phase 6 — Macro Overlay

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T16:20:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

> **Look-ahead guard:** as-of 2026-05-22, earnings 2026-05-27. Live WebSearch was
> deliberately omitted to avoid leaking post-5/22 information (especially the 5/27
> earnings outcome) into a point-in-time blueprint. UW point-in-time tools + FRED
> macro series (slow-moving, no single-name leakage) carry the overlay. FRED queries
> capped at `observation_end=2026-05-22`.

## Summary

The macro backdrop is **constructive-but-cautious, and it is not the driver** — the
5/27 earnings binary dominates. Market regime is **TRANSITIONAL** (SPY in an UPTREND
near 90d highs, but breadth weak at **38.1% bullish**), whose own guidance is "half
position sizes, favor defined-risk" [MACRO:MarketRegime_2026-05-22 UW] — a direct
echo of phases 4–5. SNOW's sector is a **tailwind**: Technology is the **largest and
accelerating** options inflow ($6.19B net today, rising five straight sessions,
persistence 1.0) [MACRO:sector_flow UW][MACRO:sector_flow_persistence UW]. The rate
backdrop is mildly supportive for software multiples — **Fed funds eased to 3.62%**,
core CPI **+2.74% YoY** near target, curve positively sloped (+43bp) — though 10y at
**4.57%** caps euphoria [MACRO:DFF_2026-05-21 FRED][MACRO:CPILFESL_2026-04 FRED]. One
portfolio flag: **SNOW/PATH correlation 0.626 (soft-watch)** among concurrent
blueprints [MACRO:portfolio_correlation UW].

## Key signals

- **Regime TRANSITIONAL → half size / defined-risk** (SPY uptrend but 38.1% breadth)
  [MACRO:MarketRegime_2026-05-22 UW].
- **Tech sector = largest, accelerating inflow** (+$6.19B today vs $3.46B on 5/18;
  persistence 1.0) — sector tailwind, `aligned` [MACRO:sector_flow_persistence UW].
- **Fed easing, core inflation near target:** DFF 3.62%, core CPI +2.74% YoY,
  headline +3.78% YoY — supportive for growth multiples [MACRO:DFF_2026-05-21 FRED]
  [MACRO:CPILFESL_2026-04 FRED][MACRO:CPIAUCSL_2026-04 FRED].
- **10y 4.57%, curve +43bp (positive):** moderate rates, normal curve — not a
  software headwind, but no tailwind from falling long rates either
  [MACRO:DGS10_2026-05-21 FRED][MACRO:T10Y2Y_2026-05-22 FRED].
- **SNOW/PATH 0.626 correlation** = soft-watch cluster among the day's blueprints
  [MACRO:portfolio_correlation UW].

## Detailed findings

### Market regime (UW) [MACRO:MarketRegime_2026-05-22 UW]

`regime` **TRANSITIONAL** — "Mixed signals, reduce position size, wait for clarity."
SPY $750.21, above 20SMA ($733.34) and 50SMA ($698.43), +5.08% 30d, only −0.26% from
the 90d high. **Breadth weak: 2,353 bullish vs 3,818 bearish tickers (38.1% bullish)**
across 6,171 names — index strength is narrow. Regime guidance: **"Half position
sizes. Favor defined-risk strategies."**

### Inflation (FRED) [MACRO:CPIAUCSL_2026-04 FRED][MACRO:CPILFESL_2026-04 FRED]

- Headline CPI Apr 2026 = 332.407 vs 320.302 a year ago → **+3.78% YoY**; MoM Mar
  +0.86%, Apr +0.64% (warm, energy/food-driven).
- Core CPI Apr 2026 = 335.423 vs 326.467 → **+2.74% YoY**; MoM Mar +0.20%, Apr +0.38%
  (tamer; approaching target).
- Core PCE (PCEPILFE) latest Mar 2026 = 129.279, rising ~+0.3%/mo.
- Read: disinflation largely complete on core, headline a touch sticky. Not a
  multiple-compression threat for software at this level.

### Labor (FRED) [MACRO:UNRATE_2026-04 FRED][MACRO:PAYEMS_2026-04 FRED]

Unemployment **4.3%** (Apr), flat-to-slightly-up over the year (4.4% Feb). Nonfarm
payrolls 158,736k (Apr) vs 158,621k (Mar) → +115k MoM — steady, cooling-but-not-
breaking labor market. Consistent with a soft landing.

### Rates (FRED) [MACRO:DFF_2026-05-21 FRED][MACRO:DGS10_2026-05-21 FRED][MACRO:DGS2_2026-05-21 FRED][MACRO:T10Y2Y_2026-05-22 FRED]

- Fed funds effective **3.62%** (well off the prior cycle peak → easing cycle
  underway).
- 10y **4.57%** (was 4.61–4.67% a few days prior — drifting down slightly); 2y
  **4.08%**.
- 2s10s **+0.43** (positively sloped, mild flattening from +0.54 on 5/19).
- Broad USD index 119.28 (mid-May), firm.
- Read: mid-easing-cycle, positive curve = a *mildly* supportive rate regime for
  long-duration software equity; the 4.57% 10y is the ceiling on multiple expansion.

### Sector rotation (UW) [MACRO:sector_flow UW][MACRO:sector_flow_persistence UW]

Today's `sector_flow`: **Technology net +$6.19B** (call prem $9.32B vs put $3.13B) —
**the largest of all sectors by a wide margin** (next: Consumer Cyclical +$1.08B,
Comm Services +$0.74B). `sector_flow_persistence` (5d): Technology trend **INFLOW**,
persistence **1.0**, and net flow has **accelerated** every session
($3.46B→$3.30B→$4.30B→$4.98B→$6.19B). Caveat: all 11 sectors print positive net flow
(calls>puts is structural), so persistence 1.0 is near-universal — the *discriminating*
fact is that Tech is the largest and accelerating. **Verdict: `aligned`** — smart
money is leaning into SNOW's sector, durably. (Note the regime tool's net-directional
"sector_rotation" lists Comm Services/Financials as *outflow* and omits Tech; that is
a different net measure — the gross premium inflow read above is the relevant one for
"is the sector in play.")

### Cross-name correlation (UW) [MACRO:portfolio_correlation UW]

Correlated SNOW against the 5 concurrent 2026-05-22 blueprints (ENPH, KWEB, NTAP,
PATH, SYM), lookback 30. Only one pair clears the 0.60 line: **SNOW/PATH = 0.626
(MODERATE / soft-watch)** — both high-beta software/automation names. No pair ≥ 0.70
(no hard cluster). NTAP (a data-infra peer also in a high-IV/earnings posture) did
*not* surface ≥0.60. The tool's sector lookup returned "Unknown" (yfinance miss) but
the price correlations computed cleanly. (Contrary to a prior note that this tool was
broken — it returned coefficients this run.)

## Tailwind / Headwind table

| Datapoint | Latest value | Release/obs date | Source | Impact on Technology/SNOW |
|-----------|--------------|------------------|--------|---------------------------|
| Market regime | TRANSITIONAL (38.1% breadth) | 2026-05-22 | UW | **headwind** (size-reducer, defined-risk) |
| Tech sector flow | +$6.19B, accelerating | 2026-05-22 | UW | **tailwind** (aligned, persistent) |
| Fed funds | 3.62% (easing) | 2026-05-21 | FRED | mild tailwind |
| Core CPI YoY | +2.74% | 2026-04 | FRED | neutral→mild tailwind (near target) |
| Headline CPI YoY | +3.78% | 2026-04 | FRED | neutral (sticky but not rising fast) |
| 10y yield | 4.57% | 2026-05-21 | FRED | neutral (caps multiple, not falling) |
| 2s10s | +0.43 (normal) | 2026-05-22 | FRED | neutral→mild tailwind |
| Unemployment | 4.3% | 2026-04 | FRED | neutral (soft landing) |
| SNOW/PATH corr | 0.626 | 2026-05-22 | UW | portfolio soft-watch |

## Catalyst calendar (next 30d)

**Front-event expected move ≈ ±13.3% / ±$23** (5/29 ATM straddle, phase-4
[STRUCT:gex DUCKDB]) — *not* the screener `implied_move_perc` 0.40%, which understates
the binary [CTX:implied_move_pct]. Size all structures to this cone.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| **2026-05-27 (postmarket)** | **SNOW Q1 earnings** | THE binary; dominates | defines the ±13% cone |
| 2026-05-22 → 05-27 | No major scheduled US macro release in the window | low | n/a |
| ~mid-June | Next CPI print + FOMC (post-horizon for a 5/29-expiry trade) | medium | beyond the event horizon |

## Tool / source errors

(none. FRED key present and used; all 10 series + YoY pair returned. WebSearch
intentionally not invoked — see look-ahead guard above. `portfolio_correlation`
sector field "Unknown" but coefficients valid.)

## Verdict for downstream phases

- **Net macro bias for SNOW:** **NEUTRAL-to-mild-tailwind.** Sector inflow (Tech
  largest, accelerating) + easing Fed + core inflation near target are supportive;
  TRANSITIONAL regime, weak breadth, and an index near highs are the offsetting
  caution. Macro is a *size/structure overlay*, not a directional driver — the 5/27
  earnings binary owns the outcome.
- **Conviction:** **3/5** (clean regime label, clear sector tailwind, clear rate
  backdrop; all slow-moving and well-sourced).
- **Top 2 datapoints phase-9 must cite:** (1) Regime TRANSITIONAL → "half size,
  defined-risk" [MACRO:MarketRegime_2026-05-22 UW]; (2) Tech sector flow +$6.19B
  accelerating, `aligned` [MACRO:sector_flow_persistence UW].
- **Top 2 catalysts for phase-9 calendar:** (1) **2026-05-27 SNOW earnings (±13.3%
  expected move)**; (2) no intervening macro release before the print — the trade is
  a clean single-catalyst event.
- **Sector-rotation verdict:** **`aligned`**, persistence 1.0 (Tech largest +
  accelerating) — a sizing *support*, not a cut.
- **Correlation verdict:** **soft-watch SNOW/PATH 0.626** (surface only; phase-9 need
  not cut size unless both are traded concurrently). No ≥0.70 cluster.
