# Phase 6 — Macro Overlay

**Ticker:** SNOW (sector: Technology / data-cloud software) · **As-of:**
2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-5-historical.md (parabolic/overbought) · phase-4 (pin
$250–$255) · phase-0.5 (Software/AI LEADING, SNOW a credible participant)

## Summary

The macro backdrop is **more favourable for SNOW than for a small-cap** — SNOW
*is* one of the mega-cap Software/AI names capturing the persistent sector bid —
but the regime caution and SNOW's own extreme extension dominate. The Fed is
**easing** (fed funds **3.62%**, un-inverted 2s10s **+0.46**), a long-duration
tailwind, with inflation still sticky (**core PCE 3.29% YoY**, 10y **4.45%**).
**Technology leads the flow tape persistently** (persistence **1/1**, INFLOW) and
SNOW belongs to the leading mega-cap cohort — so unlike PATH (a small-cap
laggard), the mega-cap concentration is a **tailwind** here. But UW tags the
regime **TRANSITIONAL — "half size, defined-risk, iron condors in range"** with
**weak breadth (36.3% bullish)**, and SNOW is already RSI-87 parabolic into a
$255 gamma pin (phase-4/5). **Correlation gate (active this run): SNOW vs the
concurrent PATH blueprint = 0.478** `[CTX:price_corr DUCKDB]` — *below* the 0.60
soft-watch, so **no cluster, no size cut**. Net macro: **mild tailwind, hard
defined-risk steer.**

## Key signals

- **Tech sector flow leadership, persistent, SNOW in the cohort** — net +$11.6B
  today, persistence **1/1**, INFLOW `[MACRO:SectorFlowPersistence_2026-05-29 UW]`.
  Tailwind (SNOW is a leader, not a laggard).
- **Regime TRANSITIONAL, "half size / defined-risk / iron condors in range"**
  `[MACRO:MarketRegime_2026-05-29 UW]` — direct sizing/structure guidance.
- **Weak breadth (36.3% bullish)** despite SPY uptrend
  `[MACRO:MarketBreadth_2026-05-29 UW]` — narrow, top-heavy tape; the bid is
  exactly in the mega-caps SNOW belongs to (double-edged: SNOW benefits, but it's
  a crowded leadership trade).
- **Easing cycle + un-inverted curve** — fed funds 3.62%, 2s10s +0.46
  `[MACRO:DFF_2026-05-28 FRED][MACRO:T10Y2Y_2026-05-28 FRED]` — duration tailwind.
- **Correlation vs PATH = 0.478** `[CTX:price_corr DUCKDB]` — no cluster; the two
  concurrent blueprints are not a redundant bet.

## Detailed findings

### Market regime (UW)
TRANSITIONAL; SPY UPTREND; breadth 36.3% bullish; Technology money flowing in
(+$533M rotation, +$11.6B net flow). Guidance: *"Half position sizes. Favor
defined-risk strategies. Iron condors in range."*

### Inflation / Labor / Rates (FRED — same prints as the 2026-05-29 tape)
- Core PCE **3.29% YoY** (Apr), core CPI 2.74%, headline CPI 3.78%
  `[MACRO:PCEPILFE_2026-04 FRED]` — sticky above target.
- NFP +115k (Apr), unemployment 4.3% — soft-landing labor.
- Fed funds **3.62%** (easing); 10y **4.45%**, 2y 3.99%, **2s10s +0.46**
  (normalized) `[MACRO:DGS10_2026-05-28 FRED]`; USD broad 119.3.

### Sector overlay (data-cloud / AI software)
The easing cycle + AI-capex narrative supports software multiples, and the bid is
concentrated **exactly in the mega-cap/AI cohort SNOW now belongs to** (post-beat,
"AI winner" — phase-0.5). Read-through is **direct and positive** — but it's a
*crowded leadership* trade into an overbought tape, so the macro tailwind doesn't
override the phase-5 extension risk.

### Sector rotation (UW flow)
Technology net +$11.6B, **persistence 1/1**, INFLOW, accelerating. **Verdict:
ALIGNED** with a long thesis and SNOW is a genuine beneficiary (not a laggard).
Caveat: weak broad breadth (38.8% green) → the strength is narrow/crowded.

### Cross-name correlation (gate ACTIVE)
- `uw risk portfolio-correlation --symbols SNOW,PATH` returned `high_correlations:
  null` / `matrix: null` (known tool gap on some pairs — see project memory).
  **Fallback (DuckDB, 35-session screener close returns):** SNOW~PATH ρ = **0.478**
  `[CTX:price_corr DUCKDB]`.
- **0.478 < 0.60 soft-watch threshold → no cluster, no size cut.** The concurrent
  PATH and SNOW blueprints are only moderately correlated — diversified, not the
  same bet. (Prior-run memory's 0.626 reflected a different window.)

## Tailwind / Headwind table
| Datapoint | Latest | Release | Source | Impact on SNOW |
|---|---|---|---|---|
| Tech sector flow | +$11.6B, persist 1 | 2026-05-29 | UW | **tailwind** (SNOW a leader) |
| Fed funds | 3.62% | 2026-05-28 | FRED | tailwind (easing) |
| 2s10s | +0.46 | 2026-05-28 | FRED | tailwind |
| Core PCE YoY | 3.29% | 2026-04 | FRED | headwind (caps cuts) |
| 10y yield | 4.45% | 2026-05-28 | FRED | mild headwind |
| Market breadth | 36.3% bullish | 2026-05-29 | UW | **headwind** (narrow/crowded) |
| Regime | TRANSITIONAL | 2026-05-29 | UW | **headwind** (half size) |

## Catalyst calendar (next 30d)
**Front-expiry implied move ±0.55%/day** `[CTX:implied_move]` (post-earnings IV
crush). **Earnings already passed 2026-05-27** (beat); next **2026-08-26**
(outside window). Near-term binaries are macro-only:
| Date (approx) | Event | Impact | vs expected move |
|---|---|---|---|
| ~mid-Jun | May CPI | sector rate read | macro |
| ~early-Jun | May NFP | labor/rate read | macro |
| ~mid-Jun | FOMC (if scheduled) | easing-path signal | macro |

No idiosyncratic SNOW catalyst in the window — the thesis is post-earnings drift /
mean-reversion, not event-driven.

## Tool / source errors
- `uw risk portfolio-correlation` returned null matrix for SNOW,PATH (documented
  tool gap); used DuckDB screener-close fallback (ρ 0.478).
- `market-regime` VIX field null (used breadth + guidance).

## Verdict for downstream

- **Net macro bias for SNOW: MILD TAILWIND** (mega-cap Tech leadership is SNOW's
  cohort) **with a hard defined-risk / half-size regime caveat** and a
  narrow-breadth/crowded-leadership flag.
- **Conviction: 3 / 5.**
- **Top 2 datapoints phase-9 must cite:** (1) Tech sector flow persistence 1/1
  (SNOW a leader, aligned), (2) Regime TRANSITIONAL "half size / defined-risk".
- **Top 2 catalysts:** (1) **Earnings passed 2026-05-27** (post-earnings drift,
  no near-term catalyst until 8/26), (2) macro CPI/NFP/FOMC in June (sector beta).
- **Sector-rotation verdict: ALIGNED** (Tech persistence 1/1, SNOW a beneficiary)
  — qualified by narrow breadth / crowded leadership.
- **Correlation verdict: NO cluster** — SNOW vs PATH ρ **0.478** (< 0.60); gate
  does not fire, no size cut.
