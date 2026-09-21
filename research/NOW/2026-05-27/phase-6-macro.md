# Phase 6 — Macro Overlay

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:52:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro is **genuinely two-sided — supportive at the index level, adverse at the
sector level.** The broad backdrop favors risk: **Fed funds 3.62% (easing cycle),
2s10s normalized (+0.48), unemployment stable 4.3%, SPY in an uptrend near highs.**
But the tape is **TRANSITIONAL** (UW regime: "reduce size, defined-risk", only
**37.1% bullish-flow breadth**), inflation is still **sticky** (core CPI +0.38%
MoM), and most important for this name, **Technology is the single largest
net-directional OUTFLOW sector today (−$433.5M) with full 5-session persistence
(1.0)** — smart money is rotating *out* of tech. That resolves phase-0.5's yellow
flag **ADVERSE**. The mitigant: NOW is **negatively correlated with the AI-beta
tech leaders** (NVDA −0.44, AAPL −0.31), so it's decoupled from the rotation and
is a portfolio *diversifier*, not a stacked bet. Net macro bias: **neutral-to-mild
headwind**, with the regime itself arguing for reduced size.

## Key signals

- **UW regime TRANSITIONAL** — "Half position sizes. Favor defined-risk." Breadth 37.1% bullish `[MACRO:MarketRegime_2026-05-27 UW]`
- **Technology net outflow −$433.5M** (largest of any sector), **persistence 1.0** → adverse & durable for NOW `[MACRO:sector_rotation_2026-05-27 UW]`
- **Correlation: NOW negatively correlated** to AAPL −0.31 / NVDA −0.44 / BABA −0.37 → **no cluster, a diversifier** `[MACRO:correlation_2026-05-27 DUCKDB]`
- **Fed funds 3.62%, 2s10s +0.48 normalized** → easing cycle + no recession curve signal = risk tailwind `[MACRO:DFF_2026-05-26 FRED]` `[MACRO:T10Y2Y_2026-05-27 FRED]`
- **SPY uptrend** ($750.46, +4.93% 30d, −0.22% from 90d high, >20/50-SMA) `[MACRO:MarketRegime_2026-05-27 UW]`

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-05-27 UW]`

- `regime` **TRANSITIONAL** — "Mixed signals, reduce position size, wait for clarity." `trading_guidance`: "Half position sizes. Favor defined-risk strategies. Iron condors in range." `trend` UPTREND.
- `market_breadth`: **37.1% bullish** (2,291 bullish vs 3,881 bearish tickers / 6,172) — weak breadth despite the index uptrend (narrow market).
- `spy`: $750.46, above 20SMA ($735.29) & 50SMA ($700.07), +4.93% 30d, −0.22% from 90d high → **constructive index tape**.

### Rates (FRED, real 2026 prints) `[MACRO:*_FRED]`

| series | latest | read |
|--------|--------|------|
| DFF (fed funds) | **3.62%** (05-26) | mid-easing cycle — **tailwind** for duration/growth |
| DGS10 (10y) | 4.50% (05-26) | moderate — neutral |
| DGS2 (2y) | 4.01% (05-26) | — |
| T10Y2Y (2s10s) | **+0.48** (05-27) | normalized/un-inverted → no recession signal — neutral-to-mild tailwind |

Fed has eased to 3.625% (from the prior 5.25–5.50% peak); a normalized curve +
ongoing cuts is the classic backdrop for a beaten-down growth name to re-rate —
**supportive of the NOW bounce thesis at the macro level.**

### Inflation & labor (FRED) `[MACRO:*_FRED]`

- CPIAUCSL **332.407** (Apr 2026) vs 330.293 (Mar) → **MoM +0.64%** (hot single month). Core CPILFESL **335.423** (Apr) vs 334.165 → **MoM +0.38%** (~4.6% annualized — **still above target, sticky**). → **mild headwind**: limits how fast the Fed can keep easing.
- UNRATE **4.3%** (Apr, flat from Mar) → stable, soft-landing — neutral/supportive.

### Sector rotation (the NOW-relevant signal) `[MACRO:sector_rotation UW]`

- **`market-regime` net-directional rotation:** money **IN** → Communication Services +$84.5M, Consumer Cyclical +$49.1M, Financial Services +$35.5M. Money **OUT** → **Technology −$433.5M** (by far the largest), Healthcare −$15.3M, Consumer Defensive −$7.2M.
- **Persistence (5d):** Technology **persistence_score 1.0** — the tech-flow sign has been fully consistent over 5 sessions → the rotation is **durable, not a one-day blip.**
- (`sector-flow`'s +$8.5bn Tech "net_flow" is *gross* premium — Tech is simply the biggest sector by volume; the directional read above is the one that matters.)
- **Verdict: ADVERSE** for a NOW long — bullish single-name flow swimming against a persistent sector outflow. **BUT** see correlation: NOW is decoupled from the tech being sold.
- **fz breadth cross-check (advisory, live EOD 2026-05-28):** overall market 46.9% green (236 adv / 263 dec, avg +0.01%) — soft/mixed, corroborates the weak UW breadth. Top mover APP +10.4% (Consumer-Cyclical/adtech — an *inflow* sector). `[MACRO:sector_breadth fz EOD]`

### Cross-name correlation `[MACRO:correlation DUCKDB]`

- UW `portfolio-correlation` returned broken sector metadata ("Unknown", `high_correlations: null`) — **computed from local screener closes instead** (known workaround, 32 sessions).
- Concurrent blueprints for 2026-05-27: **AAPL, BABA, NVDA**.

| pair | corr (30d, 32 sessions) | flag |
|------|--------------------------|------|
| NOW–AAPL | **−0.31** | no cluster |
| NOW–NVDA | **−0.44** | no cluster (diversifier) |
| NOW–BABA | **−0.37** | no cluster |
| (AAPL–NVDA) | +0.74 | their cluster, not NOW's |

- **No pair ≥0.60.** NOW is **negatively correlated** to every concurrent long → it *reduces* book risk rather than stacking it. Phase-9: **no correlation size-cut; mild diversification credit.** This also blunts the sector headwind — NOW does not trade like the AI-beta tech being rotated out of.

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on Tech/NOW |
|-----------|--------|---------|--------|--------------------|
| Fed funds (DFF) | 3.62% | 2026-05-26 | FRED | **tailwind** (easing) |
| 10y (DGS10) | 4.50% | 2026-05-26 | FRED | neutral |
| 2s10s (T10Y2Y) | +0.48 | 2026-05-27 | FRED | neutral / mild tailwind |
| Core CPI MoM | +0.38% | 2026-04 | FRED | **headwind** (sticky) |
| Unemployment | 4.3% | 2026-04 | FRED | neutral (soft landing) |
| Market regime | TRANSITIONAL, 37% breadth | 2026-05-27 | UW | **headwind** (size down) |
| SPY trend | uptrend, near highs | 2026-05-27 | UW | tailwind (risk-on) |
| **Tech sector flow** | **−$433.5M, persist 1.0** | 2026-05-27 | UW | **headwind** (adverse, durable) |

## Catalyst calendar (next 30d)

**Front-expiry implied (priced) move: ±4.07% / $4.15** `[CTX:implied_move]` — phase-9
sizes structures to this range; each binary below read against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| ~2026-06-10 | May CPI release | sticky-core risk; hot print = headwind (rates up) | could exceed ±4% if surprise |
| ~2026-06-16/17 | **June FOMC** (8x/yr cadence) | hold-vs-cut + dots; dovish = tailwind | likely exceeds ±4% on surprise |
| 2026-06-18 | Monthly OPEX | gamma/pin mechanics (phase-3/4) | inside |
| 2026-07-22 | **NOW earnings** | the real binary — **OUTSIDE 30d** (51 DTE) | n/a this window |

**No NOW-specific binary in the next 30 days** — the trade is macro/flow-driven,
not event-driven, until the 7/22 earnings (which sits beyond near-term structures).

## Tool / source errors

- `uw risk portfolio-correlation`: returned sector "Unknown" for all symbols and
  `high_correlations: null` — metadata/correlation engine non-functional for these
  tickers. **Worked around** via DuckDB on local screener closes (tagged DUCKDB).
- FOMC/CPI dates are standard-cadence estimates (2026 FOMC schedule: Jun 16–17),
  not WebSearch-confirmed; treat dates as ±1–2 days.

## Verdict for downstream

- **Net macro bias for NOW:** **NEUTRAL-to-MILD-HEADWIND.** Index/rates backdrop
  (Fed easing, soft landing, SPY uptrend) is supportive of a beaten-down growth
  bounce; offset by a TRANSITIONAL regime (size down), sticky core CPI, and the
  **persistent Technology outflow**. The regime guidance itself = **reduce size /
  defined-risk** — a direct phase-9 input.
- **Conviction:** **3/5** (clear tailwinds AND clear headwinds — genuinely mixed).
- **Top 2 datapoints phase-9 must cite:** (1) Fed funds **3.62%, easing cycle**
  (tailwind); (2) **Technology net outflow −$433.5M, persistence 1.0** (adverse rotation).
- **Top 2 catalysts for phase-9 calendar:** (1) **June FOMC ~6/16–17**; (2) **May
  CPI ~6/10**. (NOW earnings 7/22 is outside the near-term structure window.)
- **Sector-rotation verdict:** **ADVERSE** (Tech −$433.5M, persistence 1.0) —
  phase-9 sizing gate: a rotation headwind, **but materially softened** by NOW's
  decoupling (negative corr to the tech being sold).
- **Correlation verdict:** **NO cluster, NO soft-watch.** NOW negatively correlated
  to all concurrent blueprints (max |ρ| 0.44, all negative) → **diversification
  credit, no size cut.** Concurrent: AAPL, BABA, NVDA.
