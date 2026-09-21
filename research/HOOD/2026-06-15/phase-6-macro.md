# Phase 6 — Macro Overlay

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T12:40:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-4-structure.md, phase-5-historical.md

## Summary

Macro is **net neutral with a sector tailwind offset by a cautious broad tape**. UW
market-regime reads **TRANSITIONAL** ("reduce size, favor defined-risk") on weak
breadth (only **37.1% bullish-flow tickers**), yet **Technology is the dominant inflow
sector** (+$7.78B net options flow today, 5-day persistence **1.0**) and HOOD is
UW-tagged Technology — so the sector-rotation gate is **aligned**. The key resolution:
the phase-4 6/18 front-IV backwardation is **FOMC + quad-witching OPEX, not a HOOD
catalyst** — **FOMC decision is June 17** (99.6% no-change priced, range 3.50–3.75%)
and **June 19 is Juneteenth, shifting June quarterly OPEX to Thursday June 18**. HOOD
earnings are **Aug 5** (outside the 30-day window) — no idiosyncratic binary in the
horizon. Inflation is sticky (CPI 4.3% YoY / +0.5% MoM, Core 3.0%) while the Fed holds
after easing; 2s10s is +0.40 (dis-inverted). No correlation cluster with the only
concurrent blueprint (INTC).

## Key signals

- **Regime TRANSITIONAL**, breadth 37.1% bullish (3,927 bearish vs 2,320 bullish
  tickers); guidance "half size, defined-risk" `[MACRO:MarketRegime_2026-06-15 UW]`.
- **Technology = #1 inflow sector** +$7.78B net today, **persistence 1.0** (durable)
  `[MACRO:SectorFlow_2026-06-15 UW]` — HOOD's UW sector leading → rotation **aligned**.
- **FOMC June 17, 2026**, 99.6% no-change, range 3.50–3.75% (DFF 3.62)
  `[MACRO:FOMC_2026-06-17 WebSearch:polymarket.com]` — drives 6/18 IV, low drama.
- **June quarterly OPEX = Thu 6/18** (Juneteenth 6/19 holiday) — the gamma/pin event
  (phase-3 25% OI, phase-4 $100 wall / $85 max-pain).
- **No correlation cluster**: HOOD–INTC not flagged ≥0.70 (`high_correlations` null)
  `[MACRO:Correlation_2026-06-15 UW]`.

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-06-15 UW]`

regime **"TRANSITIONAL — Mixed signals, reduce position size, wait for clarity"**,
trend "DOWNTREND", trading_guidance "Half position sizes. Favor defined-risk
strategies. Iron condors in range." market_breadth: **bullish_pct 37.1%** (2,320
bullish / 3,927 bearish of 6,247 optionable). sector_rotation money-in: **Technology
+$327.7M**, Consumer Cyclical +$48.6M, Consumer Defensive +$26.5M; money-out:
Industrials −$33.1M, Basic Materials −$6.3M, Energy −$2.8M.
⚠️ Tool glitch: `spy.current=0`, `change_30d_pct=−100`, `above_20/50sma=false` are
computed off a broken `current=0` — disregard; the SPY-trend tool (below) gives the
real SPY level.

### Market context (UW SPY trend) `[MACRO:SPY_trend_2026-06-15 UW]`

SPY **759.57 → 754.83** over 10 sessions (−0.6%), 5 bull / 5 bear days, IV-rank 13.8 →
**14.4 (low)**, flow_direction_latest bearish. SPY (~755) sits **above** sma_20 (708)
and sma_50 (709) — so price is near highs but breadth/flow are soft: a tiring,
narrow tape, consistent with TRANSITIONAL.

### Inflation (FRED) `[MACRO:CPIAUCSL_2026-05 FRED]`

| Series | Latest (May'26 / Apr'26) | YoY | MoM |
|--------|--------------------------|-----|-----|
| CPI (CPIAUCSL) | 333.979 | **4.3%** | +0.5% (warm) |
| Core CPI (CPILFESL) | 336.121 | **3.0%** | +0.2% (tame) |
| PCE (PCEPI) | 130.902 (Apr) | **3.8%** | +0.4% |
| Core PCE (PCEPILFE) | 129.63 (Apr) | **3.3%** | +0.24% |

Sticky but moderating core; headline CPI +0.5% MoM is hot. Above the 2% target while
the Fed holds → mild restraint on multiple expansion.

### Labor (FRED) `[MACRO:PAYEMS_2026-05 FRED]`

NFP (PAYEMS) **159,001k** May (+172k MoM; Apr +179k). Unemployment (UNRATE) **4.3%**
(steady, 4.4→4.3 since Feb). Solid, stable labor → supportive of retail-trading
activity (HOOD revenue driver).

### Rates (FRED + FOMC) `[MACRO:DGS10_2026-06-12 FRED][MACRO:FOMC_2026-06-17 WebSearch:polymarket.com]`

DFF **3.62** (range 3.50–3.75%), SOFR **3.69**, DGS10 **4.48** (~flat 30d, 4.47),
DGS2 **4.09** (4.00 30d ago), **T10Y2Y +0.40** (dis-inverted/normal, mild steepening),
broad USD (DTWEXBGS) **119.51** (firming from 118.67). **FOMC June 17, 2026: 99.6%
no-change** priced — Fed on hold after an easing cycle. For a broker/fintech: on-hold
rates = neutral (cuts already banked support risk appetite & multiples; net-interest
revenue stable); steepening curve mildly risk-on.

### Activity / Consumer

Not separately pulled (single-name fintech overlay; FRED + regime sufficient).
ISM/U-Mich would be advisory only here — noted as not-run, not an error.

### Sector overlay (fintech/broker)

No fintech-specific regulatory catalyst surfaced in the window. HOOD fundamentals are
strong (Q1'26 rev +15% YoY to $1.07B, net deposits $18B/+22% ann., record Gold subs;
Q2 guide EPS $0.45 / rev $1.234B) `[MACRO:HOOD_Q1_2026 WebSearch:sec.gov]` — feeds
phase-7b. Recent events (Annual Mtg 6/2, Piper Sandler Fintech Conf 6/4) already
passed before as-of.

### Sector rotation `[MACRO:SectorFlow_2026-06-15 UW][MACRO:SectorFlowPersistence_5d UW]`

Today's net options flow by sector: **Technology +$7,779M** (dominant), Communication
Services +$975M, **Financial Services +$475M**, Industrials +$319M, Consumer Cyclical
+$243M, Healthcare +$229M. 5-day persistence_score: **Technology 1.0**, Financial
Services 1.0, most sectors 1.0 (Utilities 0.8, Consumer Cyclical 0.6) → the Tech/Fin
inflow is **durable, not a blip**.
- **Verdict: ALIGNED.** Whether HOOD is comped as UW-Technology (strong, +$7.78B,
  persistence 1.0) or economically as Financial Services (+$475M, persistence 1.0),
  smart money is rotating **into** its sector persistently — a tailwind for a bullish thesis.
- **`fz` breadth cross-check (advisory):** overall market pct_green **50.89%**
  (256 adv / 246 dec; top_mover WDC) — balanced, matching TRANSITIONAL. Group
  valuation: **Technology +3.38% today, P/E 40.16** (rich); **Financial +0.47%,
  P/E 17.92** (cheaper). Tech's +3.38% price-green corroborates the UW Tech inflow.
  `[MACRO:sector_breadth fz EOD][MACRO:group_valuation fz EOD]`

### Cross-name correlation `[MACRO:Correlation_2026-06-15 UW]`

Concurrent blueprint for 2026-06-15: **INTC**. `uw risk portfolio-correlation
--symbols HOOD,INTC --lookback-days 30`: **`high_correlations` is null** → the
HOOD–INTC pair is **not** flagged as a cluster (below the tool's high threshold; exact
coefficient not surfaced sub-threshold). `ticker_details` shows sector "Unknown" for
both (known broken sector-field issue — the "100% in Unknown" warning is the field bug,
not a real concentration). HOOD (broker/fintech) and INTC (semis) are different
industries; no diversification flag. **No cluster, no soft-watch.**

## Tailwind / Headwind table

| Datapoint | Latest | Release | Source | Impact on HOOD (fintech/broker) |
|-----------|--------|---------|--------|---------------------------------|
| Market regime | TRANSITIONAL, breadth 37.1% | 2026-06-15 | UW | **headwind** (cautious tape) |
| Tech sector flow | +$7.78B, persist 1.0 | 2026-06-15 | UW | **tailwind** (sector leading) |
| Fed funds / FOMC | 3.50–3.75%, hold 6/17 | 2026-06-17 | WebSearch | neutral |
| 2s10s | +0.40 (normal) | 2026-06-15 | FRED | mild tailwind |
| CPI YoY / MoM | 4.3% / +0.5% | 2026-05 | FRED | mild headwind (sticky) |
| Core CPI / Core PCE | 3.0% / 3.3% | 2026-05/04 | FRED | neutral (moderating) |
| Unemployment / NFP | 4.3% / +172k | 2026-05 | FRED | tailwind (consumer health) |
| Broad USD | 119.51 (firming) | 2026-06-12 | FRED | neutral |

## Catalyst calendar (next 30d)

**Front-expiry implied move: ±4.65% / $4.55** on $98.12 `[CTX:implied_move_pct]`.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| **2026-06-17** | FOMC decision | 99.6% no-change → low drama; could still move via dots/presser | likely **inside** ±4.65% |
| **2026-06-18** | June quarterly OPEX (quad witching; Juneteenth-shifted) | gamma/pin event — 25% of OI, $100 call wall, $85 max-pain | pin mechanics, not a move catalyst |
| 2026-08-05 | HOOD Q2 earnings | binary | **outside 30d** — not in near-term structures |

## Tool / source errors

- `uw risk market-regime` `spy` block partly glitched (`current=0`, `change_30d_pct=−100`)
  — disregarded; SPY level taken from `uw historical trend --symbol SPY`.
- `uw risk portfolio-correlation` `ticker_details.sector="Unknown"` (known broken
  sector field per project memory) — coefficient works but not surfaced when
  sub-threshold; `high_correlations` null = no cluster.
- FRED CPI/Core-CPI YoY initially errored on a `"."` missing observation; re-pulled
  with padded limit (16) filtering `"."` → CPI 4.3%, Core 3.0%. No bad value recorded.
- FRED key present (`.env`, len 32) → Path A used; no WebSearch fallback needed for
  rates/inflation/labor.

## Verdict for downstream phases

- **Net macro bias for HOOD:** **NEUTRAL** — sector-rotation tailwind (Tech leading,
  persistent) offset by a TRANSITIONAL/weak-breadth broad tape and sticky CPI; no
  idiosyncratic catalyst in-window. The FOMC (6/17) is low-drama but adds 2-day event
  risk into the 6/18 OPEX.
- **Conviction:** **3 / 5.**
- **Top 2 datapoints phase-9 must cite:** (1) regime TRANSITIONAL, breadth 37.1%
  bullish (size-down/defined-risk); (2) Technology sector inflow +$7.78B, persistence
  1.0 (sector aligned).
- **Top 2 catalysts phase-9 must calendar:** (1) **FOMC 6/17** (no-change priced,
  presser tail-risk); (2) **June OPEX 6/18** (gamma pin; resolves into the $100
  wall / $85 max-pain). HOOD earnings 8/5 noted but out-of-window.
- **Sector-rotation verdict:** **ALIGNED**, persistence **1.0** (Tech; Financials also
  1.0) — sizing gate: no rotation cut.
- **Correlation verdict:** **No cluster, no soft-watch** — HOOD–INTC `high_correlations`
  null (< high threshold). One concurrent blueprint (INTC); no size cut for correlation.

## Sources
- [FOMC June 2026 — Polymarket](https://polymarket.com/event/fed-decision-in-june-825)
- [Fed 2026 schedule — Yahoo Finance](https://finance.yahoo.com/personal-finance/banking/article/when-is-the-next-fed-meeting-full-schedule-150709698.html)
- [HOOD earnings date — Nasdaq](https://www.nasdaq.com/market-activity/stocks/hood/earnings)
- [HOOD Q1 2026 8-K — SEC](https://www.sec.gov/Archives/edgar/data/0001783879/000178387926000061/q12026robinhoodexhibit991.htm)
