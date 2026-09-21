# Phase 6 — Macro Overlay

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T14:30Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The macro backdrop is **mildly constructive but cautious**: SPY is in an
**UPTREND** (above 20/50 SMA, +6.3% 30d, −0.2% from 90d high), inflation is
cooling toward target (Core CPI **2.74% YoY**), the Fed is clearly mid-easing
(fed funds **3.62%**, down from cycle highs), the curve is **un-inverted (2s10s
+0.46)**, and 10y yields are **stable at 4.45%** — a soft-landing / rate-relief
tape that is generically supportive of long-duration tech. The single most
important macro signal for NVDA: **Technology has maximum flow persistence
(score 1/1, 5 straight sessions of net inflow, accelerating to $11.6B on
05-29)** — smart money is durably rotating *into* the sector. **That is a
tailwind for an NVDA long and a headwind to the bearish lean from phases 2–4.**
The offsetting caution: the UW market-regime label is **TRANSITIONAL** ("half
position sizes, favor defined-risk") with weak breadth (only 36.3% of names
bullish). No earnings until Aug-26; front-expiry implied move is a tiny **±0.45%
($0.95)**. Correlation gate: NVDA is **uncorrelated/negatively correlated** with
the two concurrent blueprints (PATH −0.38, SNOW −0.10) — **no cluster risk.**
**Net macro bias: mild TAILWIND for the sector, tempered by a transitional,
narrow-breadth regime. Conviction 3/5.**

## Key signals

- [MACRO:MarketRegime_2026-05-29 UW] Regime **TRANSITIONAL** ("reduce size, favor
  defined-risk, iron condors in range"); SPY UPTREND, +6.31% 30d, −0.21% from 90d
  high; **breadth weak: 36.3% bullish** (2,247 bull / 3,940 bear of 6,187).
- [MACRO:SectorFlowPersistence_2026-05-29 UW] **Technology persistence_score 1/1,
  trend INFLOW** — net flow by day 05-22 $6.2B → 05-26 $8.7B → 05-29 **$11.6B**
  (accelerating). The durable sector tailwind. NVDA's sector is *the* leader.
- [MACRO:CPILFESL_2026-04 FRED] **Core CPI 2.74% YoY** (headline CPI 3.78%) —
  disinflation toward target; supportive of duration/tech multiples.
- [MACRO:DFF_2026-05-28 FRED] **Fed funds 3.62%**, [MACRO:T10Y2Y_2026-05-28 FRED]
  **2s10s +0.46 (normal)**, 10y 4.45% (≈flat 30d) — easing cycle, un-inverted
  curve, stable rates = benign for risk assets.
- [MACRO:portfolio-correlation_2026-05-29] NVDA vs concurrent blueprints:
  **NVDA-PATH −0.38, NVDA-SNOW −0.10** (21 sessions, local closes [DUCKDB]) — **no
  cluster** (both < 0.60); NVDA diversifies, not concentrates, the book.

## Detailed findings

### Market regime (UW: SPY + breadth)

SPY 756.48, above 20SMA (739) and 50SMA (704), +6.31% 30d, just −0.21% off the
90d high → **UPTREND**. But the flow-breadth is weak (36.3% bullish), so UW labels
the tape **TRANSITIONAL** and prescribes **half-size, defined-risk**. The index is
strong while participation narrows — a late-cycle, mega-cap-led tape, which both
helps NVDA (it's the mega-cap leader) and warns (narrow leadership is fragile).

### Inflation (FRED, latest 2026-04 prints)

| series | latest | YoY | read |
|--------|--------|-----|------|
| CPIAUCSL (headline) | 332.41 (Apr) | **3.78%** | sticky-ish |
| CPILFESL (core) | 335.42 (Apr) | **2.74%** | near target — tailwind |
| PCEPILFE (core PCE) | 129.63 (Apr) | — | level only |

Core CPI 2.74% supports the easing path and long-duration tech valuations.

### Labor (FRED)

- PAYEMS +115k MoM (Apr) — **softening** vs trend; UNRATE **4.3%** (Apr). A
  cooling-not-collapsing labor market = supports continued Fed cuts (tailwind for
  rate-sensitive growth), but the softening is worth monitoring.

### Rates (FRED, 2026-05-28)

- Fed funds **3.62%** (mid-easing), SOFR-area in line; **10y 4.45%** (≈ 4.42% 30d
  ago — flat), **2y 3.99%**, **2s10s +0.46 (un-inverted/normalizing)**. Stable
  rates + positive curve = no rates headwind for tech right now.

### Sector overlay (semis/AI)

No new chip-export or AI-capex headline forced into this as-of read; the dominant
semis catalyst remains the AI-capex cycle, reflected in the Tech inflow
persistence below. (No earnings for NVDA until Aug-26.)

### Sector rotation (UW sector-flow + persistence)

- **Today's sector-flow:** Technology net **+$11.62B** — #1 by a wide margin
  (next: Financials +$1.40B, Comm Svcs +$1.06B). Money flowing IN: Tech, Energy,
  Utilities; OUT: Comm Svcs −$104M, Cons Cyclical −$50M, Materials −$20M.
- **5-session persistence: Technology score 1/1, trend INFLOW**, accelerating
  ($6.2B→$11.6B). This is a **durable** rotation, not a one-day blip.
- **Verdict vs thesis:** rotation is **aligned** with an NVDA *long* and **adverse**
  to the phase-2/3/4 bearish lean. The sector tailwind is the strongest single
  argument *against* fading NVDA here.
- [MACRO:sector_breadth fz EOD] `fz` breadth (sec_all, captured 2026-05-30, ~1d
  stale): pct_green **38.77%**, advancers 195 / decliners 308, **top mover DELL
  +32.8%** — broad breadth weak but the tech leaders (DELL) are the standouts,
  corroborating the UW "narrow, tech-led" read. Advisory only.

### Cross-name correlation (concurrent blueprints)

Concurrent as-of-2026-05-29 blueprints: **NVDA, PATH, SNOW**. UW
`portfolio-correlation` returned `high_correlations: null` (known-broken pairwise
output — `data-source-workarounds`); computed from 21 sessions of local screener
closes instead [DUCKDB]:

| pair | corr (21d daily returns) | flag |
|------|--------------------------|------|
| NVDA–PATH | **−0.38** | none (diversifying) |
| NVDA–SNOW | **−0.10** | none |
| PATH–SNOW | +0.42 | soft only between the others |

No pair involving NVDA reaches the 0.60 soft-watch threshold. **No cluster, no
correlation size-cut for NVDA.**

## Tailwind / Headwind table

| Datapoint | Latest value | Release | Source | Impact on Tech/NVDA |
|-----------|--------------|---------|--------|--------------------|
| Tech flow persistence | score 1/1, INFLOW $11.6B | 2026-05-29 | UW | **tailwind** |
| Core CPI YoY | 2.74% | 2026-04 | FRED | tailwind |
| Fed funds / easing | 3.62% | 2026-05-28 | FRED | tailwind |
| 2s10s | +0.46 (normal) | 2026-05-28 | FRED | tailwind |
| 10y yield | 4.45% (flat 30d) | 2026-05-28 | FRED | neutral |
| SPY trend | UPTREND, −0.2% from high | 2026-05-29 | UW | tailwind |
| Market breadth | 36.3% bullish (TRANSITIONAL) | 2026-05-29 | UW | **headwind** |
| Payrolls | +115k (softening) | 2026-04 | FRED | neutral/slight headwind |

## Catalyst calendar (next 30d)

**Front-expiry implied (expected) move: ±0.45% / $0.95** [CTX:implied_move]
(`implied_move` 0.948, `implied_move_perc` 0.0045 — a *very* tight 1-day priced
range; phase-9 sizes structures to this).

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| 2026-06-05 | 7-DTE OPEX (heavy 0DTE/weekly OI build) | pin/gamma | inside ±0.45%/day |
| 2026-06-18 | June monthly OPEX | OPEX/gamma pull toward 195–200 (negative-gamma + put-build levels, not a max-pain calc) | multi-day, can exceed |
| ~mid-June | CPI / FOMC (recurring) | rates re-rate | could exceed if surprise |
| 2026-08-26 | **NVDA earnings** | binary (OUT of near-term window) | far |

No binary earnings catalyst inside the near-term option windows — this is a
flow/positioning/macro tape, not an event setup.

## Tool / source errors

```
# uw risk portfolio-correlation: high_correlations=null, sectors "Unknown" —
#   known-broken pairwise output; correlation computed from local screener closes
#   (data-source-workarounds memo).
# fz breadth: sec_all snapshot captured 2026-05-30 (≈1 day after as-of) — live,
#   not as-of reproducible; used advisory only.
# FRED: macro series have ~1-month publication lag (latest CPI = 2026-04); normal.
```

## Verdict for downstream phases

- **Net macro bias for NVDA:** mild **TAILWIND** (Tech inflow persistence + easing
  + uptrend), tempered by a **TRANSITIONAL, narrow-breadth** regime (half-size).
- **Conviction:** 3/5.
- **Top 2 datapoints phase-9 must cite:** (1) **Tech flow persistence 1/1, INFLOW
  $11.6B** (sector tailwind); (2) **regime TRANSITIONAL, 36.3% breadth → half-size,
  defined-risk**.
- **Top 2 catalysts for phase-9 calendar:** (1) **June 18 monthly OPEX** (OPEX/gamma
  pull toward the 195–200 negative-gamma/put-build levels — not a max-pain calc);
  (2) **NVDA earnings 2026-08-26** (far, not near-term).
- **Sector-rotation verdict:** **ALIGNED (to long) / ADVERSE (to the bearish
  lean)**, persistence score **1/1** — the durable sector inflow is the key
  counterweight to phases 2–4.
- **Correlation verdict:** **No cluster.** NVDA–PATH −0.38, NVDA–SNOW −0.10 (both
  < 0.60). No correlation size-cut for NVDA. (PATH–SNOW +0.42 concerns those two,
  not NVDA.)
