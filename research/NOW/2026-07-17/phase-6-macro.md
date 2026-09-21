# Phase 6 — Macro Overlay

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro is **neutral-to-mild-headwind for a high-multiple enterprise-software long, and
the regime itself prescribes exactly the premium-selling / defined-risk posture
phase-5 reached.** `uw risk market-regime` = **TRANSITIONAL / CHOPPY** with explicit
guidance: *"Half position sizes. Favor defined-risk strategies. Iron condors in
range."* Breadth is **bearish (38.4% bullish; 3,878 bearish vs 2,420 bullish
tickers)** and SPY sits below its 20- & 50-day SMAs (−0.94% 30d). Technology is the
**leading sector inflow (+$1.17B net, persistence 0.80, INFLOW)** — a sector
tailwind — **but NOW is not capturing it** (phase-0.5: semis/AI-infra lead, NOW is
the app-software laggard, −13.5%/30d). Rates are a mild drag: **10y 4.57%**, sticky
**CPI 3.4% YoY / Core PCE 3.4%**, pressuring long-duration growth multiples. The
standout risk flag is correlation: **NOW/PATH = 0.798 → a concurrent-blueprint
CLUSTER** phase-9 must size against. Net macro bias: **neutral-to-headwind**,
conviction 3/5.

## Key signals

- **Regime TRANSITIONAL/CHOPPY → "iron condors in range, defined-risk, half size"**
  `[MACRO:MarketRegime_2026-07-17 UW]`.
- **Bearish breadth 38.4% bullish** (3,878 vs 2,420) `[MACRO:MarketRegime_2026-07-17 UW]`.
- **Tech sector INFLOW +$1.17B, persistence 0.80** — sector tailwind, but NOW lagging
  `[MACRO:sector_flow_2026-07-17 UW]` `[MACRO:sector_flow_persistence UW]`.
- **NOW/PATH correlation 0.798 = CLUSTER** (≥0.70) among concurrent blueprints
  `[MACRO:portfolio_correlation UW]`.
- **10y 4.57%, CPI 3.4% YoY, Core CPI 2.5%** — mild multiple headwind
  `[MACRO:DGS10_2026-07-16 FRED]` `[MACRO:CPIAUCSL_2026-06 FRED]`.

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-17 UW]`

- **Regime: TRANSITIONAL** — "Mixed signals, reduce position size, wait for clarity";
  trend **CHOPPY**. **trading_guidance: "Half position sizes. Favor defined-risk
  strategies. Iron condors in range."**
- SPY 743.29: below 20sma (745.02) **and** 50sma (744.38); −0.94% 30d; −2.25% from
  90d high.
- Breadth: **bullish_pct 38.4%** (bearish_flow 3,878 / bullish_flow 2,420 of 6,298) —
  a **bearish tape**, corroborating phase-5's bearish_flow=100% backtest.
- Sector rotation: IN → Technology +$98.6M, Energy +$30.1M, Comm Svcs +$29.7M; OUT →
  Financials −$57.2M, Consumer Cyclical −$45.3M, Industrials.

### SPY recent action `[MACRO:SPY_trend UW]`

10-session (7/06→7/17): **751.28 → 743.29 (−1.1%)**, 3 bull / 7 bear days — mild
risk-off drift.

### Inflation (FRED) `[MACRO:CPIAUCSL_2026-06 FRED]`

| Series | Latest | YoY |
|---|---|---|
| CPI (CPIAUCSL) | 2026-06 = 332.568 | **3.4%** |
| Core CPI (CPILFESL) | 2026-06 = 336.065 | **2.5%** |
| Core PCE (PCEPILFE) | 2026-05 = 130.082 | **3.4%** |

Sticky-but-moderating; core CPI 2.5% is the encouraging leg, headline 3.4% still
above target. Mild headwind for rate-sensitive growth.

### Labor (FRED) `[MACRO:PAYEMS_2026-06 FRED]`

- Unemployment (UNRATE) **4.2%** (June, down from 4.3%).
- Nonfarm payrolls MoM **+57k** (June) — **soft**. Cuts both ways: supports Fed easing
  (tailwind) but signals slowing activity → softer enterprise IT budgets (headwind
  for NOW's demand narrative).

### Rates (FRED) `[MACRO:DGS10_2026-07-16 FRED]`

- 10y (DGS10) **4.57%**, 2y (DGS2) 4.16%, **2s10s +0.37 (normal, un-inverted)**.
- Fed funds effective (DFF) **3.63%** — Fed has eased off cycle highs; curve normalized.
- Broad USD (DTWEXBGS) 120.50 (7/10).
- 10y at 4.57% is the operative headwind for a long-duration ~high-multiple software
  name; not spiking, so **mild**, not acute.

### Activity / Consumer

Not separately pulled (single-ticker overlay; regime + rates + breadth are the
material inputs). ISM/U-Mich would only refine an already neutral-to-headwind read;
marked neutral by default.

### Sector overlay & rotation `[MACRO:sector_flow_2026-07-17 UW]`

- **Technology net_flow +$1.17B today** (call prem $7.94B vs put $6.76B) — the #1
  sector by net flow.
- **sector-flow-persistence: Technology persistence_score 0.80, trend INFLOW** (4 of
  last 5 days positive; only 7/16 negative −$3.36B).
- **BUT NOW is not participating:** phase-0.5 showed the tech bid is concentrated in
  **semis/AI-infra** (NVDA/CDNS/SNDK/DRAM), while NOW (app software) is −13.5%/30d and
  outside the leader pocket. So the sector tailwind is real for tech broadly but NOW
  is **diverging bearishly** from it — a relative-weakness flag.
- **Rotation verdict for the NOW thesis: NEUTRAL** (sector inflow exists, but the name
  is not capturing it; persistence 0.80 applies to the sector, not to NOW's laggard
  price action).
- `fz` breadth cross-check: **unavailable** (partial 14-field snapshot all session) —
  `[MACRO:sector_breadth fz EOD]` = n/a.

### Cross-name correlation (30d) `[MACRO:portfolio_correlation UW]`

Concurrent 2026-07-17 blueprints: **OKLO, PATH, RKT, SHOP** (correlated vs NOW).

| pair | correlation | flag |
|---|---|---|
| **NOW / PATH** | **0.798** | **CLUSTER (≥0.70)** — same automation/enterprise-SaaS bet |
| NOW / SHOP | 0.58 | soft-watch (0.60–0.70 band boundary; below, but adjacent) |
| NOW / OKLO | — | below threshold (nuclear — uncorrelated) |
| NOW / RKT | — | below threshold (mortgage — uncorrelated) |

Warning: tool sector field returned "Unknown" for all (known UW sector-field bug);
correlations themselves are valid (per memory: UW correlation coefficients work, only
the sector label is broken). **NOW/PATH 0.798 is a genuine cluster** — phase-9 must
cut NOW size if PATH is concurrently held.

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Technology/NOW |
|---|---|---|---|---|
| Market regime | TRANSITIONAL/CHOPPY | 2026-07-17 | UW | **headwind** (half size, defined-risk) |
| Breadth (bullish %) | 38.4% | 2026-07-17 | UW | **headwind** |
| Tech sector net flow | +$1.17B, persist 0.80 | 2026-07-17 | UW | tailwind (sector) / **neutral (NOW lagging)** |
| 10y yield | 4.57% | 2026-07-16 | FRED | mild headwind (multiple) |
| CPI YoY | 3.4% | 2026-06 | FRED | mild headwind |
| Core CPI YoY | 2.5% | 2026-06 | FRED | neutral-improving |
| NFP MoM | +57k | 2026-06 | FRED | mixed (Fed-dovish / demand-soft) |
| Unemployment | 4.2% | 2026-06 | FRED | neutral |

## Catalyst calendar (next 30d)

**Front-expiry implied move:** daily screener implied_move ±0.49% [CTX:implied_move_pct]
— BUT the binding number is the **earnings-event implied move ≈ ±10–12%** on the 7/24
expiry (phase-4: front IV 114%). Every binary below reads against ~±10–12%.

| Date | Event | Likely impact | vs expected move |
|---|---|---|---|
| **2026-07-22** | **ServiceNow Q2 FY26 earnings** (AMC, cross-check 7b/7c) | **dominant binary** | the ±10–12% *is* this event |
| ~2026-07-28/29 | FOMC meeting (approx; confirm) | rates/guidance | market-level, post-earnings |
| ~2026-08-12 | July CPI release (approx) | inflation | market-level, post-earnings |

Earnings (7/22) dwarfs everything — it lands before FOMC/CPI, so those are
second-order for the near-term NOW trade.

## Tool / source errors

None. FRED Path A worked (key present). `fz` breadth/valuation advisory lane
unavailable (partial snapshot). Correlation sector-label "Unknown" is the known UW
field bug, not a data failure — coefficients used as valid.

## DATA NOTE / CORRECTION

None — all values round-tripped through `jq`. FOMC/CPI dates flagged "approx" (not
pulled from a dated source this run); phase-9 should not treat those exact dates as
confirmed.

## Verdict for downstream

- **Net macro bias for NOW:** **neutral-to-headwind** (choppy risk-off regime +
  bearish breadth + elevated 10y vs a lagging high-multiple name; sector inflow
  doesn't reach NOW). Conviction **3/5**.
- **Top 2 datapoints phase-9 must cite:** (1) regime TRANSITIONAL/CHOPPY →
  *"defined-risk, iron condors in range, half size"*; (2) 10y 4.57% + bearish breadth
  38.4% as the multiple/tape headwind.
- **Top 2 catalysts for phase-9 calendar:** (1) **2026-07-22 earnings** (±10–12%
  implied) — the trade IS an earnings decision; (2) ~7/28 FOMC (post-earnings,
  second-order).
- **Sector-rotation verdict:** **NEUTRAL** — Technology INFLOW persistence 0.80, but
  NOW diverging bearishly (relative weakness); the sector tailwind is not NOW's.
- **Correlation verdict:** **CLUSTER — NOW/PATH 0.798** (cut NOW size if PATH held);
  NOW/SHOP 0.58 soft-watch; OKLO/RKT uncorrelated. Concurrent positions exist, gate
  active.
