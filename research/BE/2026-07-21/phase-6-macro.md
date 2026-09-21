# Phase 6 — Macro Overlay

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T08:32:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

The macro backdrop is **caution-with-a-secular-tailwind, headed into a
double-catalyst week.** The UW market regime is **TRANSITIONAL** — "half position
sizes, favor defined-risk strategies" — with weak breadth (37.5% of names
bullish) even as SPY holds its 20/50-SMA uptrend (748.28, −1.6% from 90d high).
BE's *sector of record* (Industrials) is **neutral-to-adverse** (the regime's
rotation model tags it a net-outflow −$8.9M; the raw sector-flow has it mildly
positive +$33.5M, mid-pack), but BE's *real* driver — **AI-data-center power
demand** — is aligned with the day's dominant inflow, **Technology (+$746M
regime / +$2.46B sector-flow)**. Macro rates are a background **headwind**:
sticky inflation (headline CPI **3.73% YoY**, core PCE **3.41%**), a cooling but
positive labor print (NFP **+57k**), Fed funds **3.63%** with the curve
normalized (2s10s **+0.37**), and the **10y at 4.60%** — higher-for-longer is a
cost-of-capital drag on a capital-intensive fuel-cell builder. Everything is
subordinate to the **7/28 earnings (after close) → 7/29 FOMC** double catalyst,
both inside the 7/31 weekly OPEX, against a priced **~10.6% implied move**.

## Key signals

- **Market regime TRANSITIONAL** — "half position sizes, favor defined-risk"; breadth 37.5% bullish `[MACRO:MarketRegime_2026-07-21 UW]`
- **BE earnings 2026-07-28 (after close)** — consensus adj EPS $0.41 (vs $0.10 y/y), rev +106.5% to $828M, AI-datacenter thesis `[MACRO:BE_earnings_2026-07-28 WebSearch:businesswire.com]`
- **FOMC 2026-07-29**, hold expected at 3.50–3.75%, no SEP — lands day after BE print `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`
- **Industrials rotation neutral-to-adverse** (regime out −$8.9M; sector-flow +$33.5M; persistence 0.8) — BE thematically Tech-aligned `[MACRO:sector_flow_2026-07-21 UW]`
- **Rates headwind:** 10y 4.60%, Fed 3.63%, core PCE 3.41% YoY, headline CPI 3.73% `[MACRO:DGS10_2026-07-20 FRED]` `[MACRO:PCEPILFE_2026-05 FRED]`

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-07-21 UW]`

`regime` = **TRANSITIONAL — Mixed signals, reduce position size, wait for
clarity**. SPY 748.28 (above 20SMA 744.98 & 50SMA 744.88, +0.21% 30d, −1.59% from
90d high); `trend` UPTREND but breadth weak — **2,350 bullish vs 3,914 bearish
tickers (37.5% bullish)**. VIX field null. `trading_guidance`: *"Half position
sizes. Favor defined-risk strategies. Iron condors in range."* This is a direct
size-down instruction that phase-9 must honor.

### Inflation (FRED) — sticky, above target

| Series | Latest | YoY |
|--------|--------|-----|
| Headline CPI (CPIAUCSL) | 332.568 (2026-06) | **+3.73%** `[MACRO:CPIAUCSL_2026-06 FRED]` |
| Core CPI (CPILFESL) | 336.065 (2026-06) | **+2.81%** `[MACRO:CPILFESL_2026-06 FRED]` |
| Core PCE (PCEPILFE) | 130.082 (2026-05) | **+3.41%** `[MACRO:PCEPILFE_2026-05 FRED]` |

Inflation remains above the Fed's 2% PCE target (web coverage cites an
energy-driven CPI surge amid Middle-East tensions) — anchors the Fed's hold.

### Labor (FRED)

NFP (PAYEMS) 158,984k (2026-06), **MoM +57k** (prior +129k) — decelerating but
positive. Unemployment (UNRATE) **4.2%** (2026-06). A soft-landing-ish labor
market, not a recession signal. `[MACRO:PAYEMS_2026-06 FRED]` `[MACRO:UNRATE_2026-06 FRED]`

### Rates (FRED + FOMC)

Fed funds effective (DFF) **3.63%** (2026-07-20), target 3.50–3.75%. 10y (DGS10)
**4.60%**, 2y (DGS2) **4.21%**, 2s10s (T10Y2Y) **+0.37** (normalized/un-inverted).
Broad USD (DTWEXBGS) 120.53. **FOMC 2026-07-29** expected hold (no SEP). A 4.60%
10y is a valuation headwind for long-duration growth / capex-heavy names like BE.
`[MACRO:DGS10_2026-07-20 FRED]` `[MACRO:DFF_2026-07-20 FRED]` `[MACRO:FOMC_2026-07-29 WebSearch:federalreserve.gov]`

### Activity / Consumer

Not separately pulled (ISM/U-Mich) — the two dominant near-term drivers are the
company print and the FOMC, both dated below; broad activity is captured by the
TRANSITIONAL regime. (Advisory omission, not a data error.)

### Sector overlay — BE's catalysts `[MACRO:BE_earnings_2026-07-28 WebSearch:businesswire.com]`

BE is the **AI-data-center-power** proxy. Consensus for the 7/28 print: **adj EPS
$0.41** (vs $0.10 prior-year), **revenue $828.4M, +106.5% YoY** — a
growth-acceleration story driven by data-center power demand (Oracle, AEP,
Texas/Spain projects). **Key risk flagged by analysts: delays in the large Oracle
(ORCL)/AEP projects** could hit forward numbers; BE is also doubling production
capacity in 2026 (execution/margin risk). This binary dominates the setup.

### Sector rotation `[MACRO:sector_flow_2026-07-21 UW]` / `[MACRO:sector_flow_persistence UW]`

- **Today's sector-flow:** Industrials net_flow **+$33.5M** (8th of 11 sectors) —
  mildly positive but dwarfed by Technology **+$2.46B** and Comm Services $592M.
- **Regime rotation model:** money flowing **OUT** of Industrials (−$8.86M),
  Financials (−$43.9M), Energy (−$3.0M); **IN** to Technology (+$746.6M).
- **5-session persistence:** Industrials `persistence_score` **0.8** (fairly
  consistent), same band as Tech/Utilities; several defensives at 1.0.
- **`fz` breadth cross-check:** skipped — `fz` sector reads unavailable this
  session (degraded quote, phase-0); no independent breadth overlay.
- **Verdict:** **neutral-to-adverse** for a strict Industrials read, but BE trades
  on the **Tech/AI-power** theme, which *is* the day's inflow leader — so
  thematically **aligned**, sector-of-record **neutral**. Net tag: **neutral**
  (the AI-power tailwind offsets the Industrials outflow; not a clean adverse).

### Cross-name correlation `[MACRO:portfolio_correlation UW]`

**No concurrent positions to correlate against** — BE is the only blueprint under
`research/*/2026-07-21/`. Correlation gate skipped (single symbol). No cluster /
soft-watch pair to flag for phase-9.

## Tailwind / Headwind table

| Datapoint | Latest value | Release | Source | Impact on Industrials / BE |
|-----------|--------------|---------|--------|----------------------------|
| AI-datacenter power demand | rev +106.5% YoY guide | 2026-07 | WebSearch:tipranks | **tailwind** (secular) |
| Technology sector inflow | +$2.46B today | 2026-07-21 | UW | **tailwind** (BE is AI-power proxy) |
| Market regime | TRANSITIONAL / half-size | 2026-07-21 | UW | **headwind** (size-down) |
| Core PCE YoY | +3.41% | 2026-05 | FRED | headwind (sticky → Fed hold) |
| 10y Treasury | 4.60% | 2026-07-20 | FRED | **headwind** (capex cost) |
| Fed funds / FOMC | 3.63%, hold exp. | 2026-07-29 | FRED/WebSearch | neutral (priced hold) |
| NFP MoM | +57k | 2026-06 | FRED | neutral (soft-landing) |
| Industrials rotation | −$8.9M (regime) / +$33.5M (flow) | 2026-07-21 | UW | neutral |
| 2s10s | +0.37 (normal) | 2026-07-21 | FRED | neutral |

## Catalyst calendar (next 30d)

**Front-expiry implied (expected) move: ±10.6% / ±$23.89** `[CTX:implied_move_pct]`
(screener implied_move_perc 0.1056; earnings-driven, 7/24→7/31 weeklies price it).

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| **2026-07-28 (AMC)** | **BE Q2 earnings** (EPS $0.41e, rev +106.5%e) | **HIGH — binary** | move *is* the ±10.6% |
| **2026-07-29 2pm** | **FOMC** decision (hold 3.50–3.75% exp.) | med — macro vol on top | adds to the ±10.6% |
| ~2026-08-01 | July NFP (labor) | low-med | inside |
| ongoing | Oracle/AEP project timing | med (guidance risk) | inside/exceeds if delay |

## Tool / source errors

<none blocking.> FRED key present (`.env`) — Path A used successfully for 10
series. VIX field null in `market-regime` (used breadth + SPY trend instead). ISM
/ U-Mich not pulled (dominated by the 7/28–7/29 binaries; advisory omission). `fz`
sector breadth unavailable (degraded quote). Correlation gate skipped (single
blueprint).

## Verdict for downstream phases

- **Net macro bias for BE:** **NEUTRAL** — a genuine secular AI-power tailwind
  (Tech inflows, +106% revenue guide) offset by a **TRANSITIONAL/size-down
  regime**, a **4.6% 10y rates headwind**, and sticky inflation. Not a clean
  tailwind; not a headwind either.
- **Conviction:** **3 / 5.**
- **Top 2 datapoints phase-9 must cite:** (1) regime **TRANSITIONAL — half
  position sizes / defined-risk** (a direct sizing constraint); (2) **10y 4.60% +
  core PCE 3.41%** (rates/valuation headwind on a capex-heavy name).
- **Top 2 catalysts for phase-9 calendar:** (1) **BE Q2 earnings 2026-07-28 AMC**
  (the ±10.6% binary); (2) **FOMC 2026-07-29** (macro vol the next morning).
- **Sector-rotation verdict:** **neutral** — Industrials outflow (−$8.9M regime)
  offset by AI-power/Tech alignment; persistence 0.8. Not an adverse gate, but not
  a tailwind either.
- **Correlation verdict:** **no concurrent positions** (BE sole blueprint for
  2026-07-21) — no cluster/soft-watch to cut size against.
