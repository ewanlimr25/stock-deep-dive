# Phase 6 — Macro Overlay

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Upstream phases cited:** phase-0.5-context.md, phase-5-historical.md

## Summary

The macro split is **strong structural tailwind vs cautious near-term regime**. The
*fundamental* backdrop is squarely supportive of memory semis: a **soft-landing
macro** (core CPI +0.2% MoM, core PCE +0.3% MoM moderating; unemployment steady
4.3%; payrolls +172k), an **easing Fed** (funds 3.63%, cut well off cycle highs),
**falling long yields** (10y 4.41%, down from 4.50%) and a **normalized curve**
(2s10s +31bps) — a benign, lower-discount-rate environment for long-duration
growth. On top of that sits a confirmed **AI memory supercycle**: DRAM contract
prices +90-95% QoQ in 1Q26, **HBM sold out for 2026** (~25% of DRAM wafers),
hyperscaler capex >$600B (+40% YoY), BofA DRAM revenue +51% YoY — Micron is one of
three makers controlling >95% of DRAM. **This fundamentally justifies the parabolic
run** (phase-5: +325% YTD). The offset: the **near-term UW market regime is
TRANSITIONAL — "reduce position size, wait for clarity"** with only **35.4% bullish
breadth** and SPY below its 20-SMA, and MU is **leading a *narrow* memory rally**
(Tech sector flow is +$3.68B / #1, but ~$3.45B of that *is MU itself*; SNDK +22%
top mover, AAPL −6% worst). Net: a real structural tailwind, tactically tempered by
a deteriorating, narrow tape.

## Key signals

- **AI memory supercycle confirmed** — DRAM +90% QoQ, HBM sold out 2026, capex +40% `[MACRO:memory_cycle_2026 WebSearch:trendforce.com]`
- **Soft-landing + easing Fed**: funds 3.63%, 10y 4.41% (falling), core CPI moderating `[MACRO:DFF_2026-06-24 FRED / DGS10_2026-06-24 FRED]`
- **UW regime TRANSITIONAL — "reduce size"**, breadth 35.4% bullish `[MACRO:MarketRegime_2026-06-25 UW]`
- **Tech = #1 sector inflow +$3.68B, persistence 1.0 INFLOW** — but concentrated in MU `[MACRO:sector_flow_2026-06-25 UW]`
- **Narrow leadership**: SNDK +22% / AAPL −6% — memory up, megacap software down `[MACRO:sector_breadth fz EOD]`

## Detailed findings

### Market regime (UW) `[MACRO:MarketRegime_2026-06-25 UW]`

- `regime`: **TRANSITIONAL — "Mixed signals, reduce position size, wait for
  clarity."**
- Breadth: 2,210 bullish vs **4,026 bearish** tickers = **35.4% bullish** (weak,
  risk-off internals).
- SPY: above_50sma true, **above_20sma false** (rolling over short-term); 10d
  737.76 → 734.3, **4 bullish / 6 bearish days**. The index is soft.
- **Read: the broad tape is a HEADWIND** — the regime explicitly says reduce size,
  which directly caps phase-9 sizing on an already-extended name.

### Inflation (FRED) `[MACRO:CPILFESL_2026-05 FRED / PCEPILFE_2026-05 FRED]`

- Core CPI (CPILFESL): 334.165 → 335.423 → **336.121** (May); MoM **+0.21%**.
- Core PCE (PCEPILFE): 129.343 → 129.667 → **130.082** (May); MoM **+0.32%**.
- **Moderating** — consistent with the easing cycle. Tailwind (keeps the Fed cutting).

### Labor (FRED) `[MACRO:PAYEMS_2026-05 FRED / UNRATE_2026-05 FRED]`

- Payrolls (PAYEMS): +179k (Apr), **+172k (May)** — resilient.
- Unemployment (UNRATE): **4.3%** steady (Mar/Apr/May). Soft landing — neutral-to-tailwind.

### Rates (FRED) `[MACRO:DFF_2026-06-24 FRED / DGS10_2026-06-24 FRED / T10Y2Y_2026-06-25 FRED]`

- Fed funds (DFF): **3.63%** (6-24) — well off cycle highs, **easing cycle**.
- 10y (DGS10): **4.41%** (6-24), down from 4.50% (6-23) — **falling**.
- 2y (DGS2): 4.11% (6-24), down from 4.16%.
- 2s10s (T10Y2Y): **+0.31** (6-25) — **normalized/positive** (un-inverted).
- Broad USD (DTWEXBGS): 120.40 (6-18) vs 119.39 — firming mildly.
- **Read: TAILWIND** — easing Fed + falling long yields lower the discount rate on
  long-duration growth (semis benefit most).

### Activity / Consumer

- Not separately pulled (ISM/U-Mich) — the FRED soft-landing read (steady 4.3%
  unemployment, moderating inflation, resilient payrolls) is sufficient for a
  single-name overlay. Marked neutral.

### Sector overlay — AI memory supercycle `[MACRO:memory_cycle_2026 WebSearch:trendforce.com / skhynix.com]`

- DRAM contract prices **+90-95% QoQ in 1Q26** (PC DRAM >100%); memory shortage.
- **HBM sold out for 2026**, ~25% of DRAM wafer supply, HBM demand +70% YoY; HBM
  revenue ~$35B (2025) → ~$60B (2026).
- Hyperscaler capex **>$600B in 2026 (+40% YoY)**; supply locked via multi-year deals.
- Micron = 1 of 3 DRAM makers (>95% share, with Samsung & SK Hynix).
- **Read: strong structural TAILWIND** — this is the fundamental engine behind MU's
  +325% YTD; the rally is *earnings-justified*, not pure multiple expansion
  (phase-7b confirms the multiple).

### Sector rotation `[MACRO:sector_flow_2026-06-25 UW / sector_flow_persistence UW]`

- `sector-flow`: **Technology net_flow +$3,684M — #1 of all sectors** (next:
  Healthcare +$369M). Consumer Cyclical worst at −$806M.
- `sector-flow-persistence`: Technology **persistence_score 1.0, trend INFLOW**, net
  inflow every session 6-18→6-25 ($9.4B → 6.8 → 3.8 → 2.4 → **3.7B** — durable but
  **decelerating** from the 6-18 peak).
- **Caveat (important):** MU's own bullish premium today was ~$3.45B (phase-1) — so
  the +$3.68B "Tech inflow" **is essentially MU**. The sector tailwind is **real but
  circular/narrow**, not broad tech strength.
- **`fz` breadth cross-check** `[MACRO:sector_breadth fz EOD]`: tech 305 adv / 198
  decl = **60.6% green**, avg +0.56%; **top_mover SNDK +21.97%**, **worst AAPL
  −6.12%**. Corroborates: memory/storage ripped, megacap software sold — narrow,
  pocket-specific leadership.
- **`fz` group valuation** `[MACRO:group_valuation fz EOD]`: Technology P/E 37.2, Fwd
  P/E 26.0, **PEG 0.97**, EPS next-5Y +38% — sector not egregiously priced vs growth
  (MU's *own* valuation assessed in phase-7b).
- **Verdict: ALIGNED** (smart money is in MU's sector, persistently) — but flagged
  **narrow/concentrated**, so the alignment is weaker than the raw +$3.68B suggests.

### Cross-name correlation `[MACRO:portfolio_correlation UW]`

- **MU is the only blueprint for 2026-06-25** (`ls research/*/2026-06-25/` → MU only).
  **No concurrent positions to correlate against — gate skipped.** (Context note: MU
  and SNDK are clearly co-moving today as the memory pair, a soft-watch worth noting
  if a SNDK blueprint is opened.)

## Tailwind / Headwind table

| Datapoint | Latest value | Release date | Source | Impact on Semis/Memory |
|-----------|--------------|--------------|--------|------------------------|
| AI memory supercycle | DRAM +90% QoQ, HBM sold out | 2026 | WebSearch | **tailwind (structural)** |
| Fed funds | 3.63% (easing) | 2026-06-24 | FRED | tailwind |
| 10y yield | 4.41% (falling) | 2026-06-24 | FRED | tailwind |
| Core CPI MoM | +0.21% | 2026-05 | FRED | tailwind (moderating) |
| Core PCE MoM | +0.32% | 2026-05 | FRED | neutral/tailwind |
| Unemployment | 4.3% (steady) | 2026-05 | FRED | neutral (soft landing) |
| Payrolls MoM | +172k | 2026-05 | FRED | tailwind |
| 2s10s | +0.31 (normalized) | 2026-06-25 | FRED | neutral/tailwind |
| Tech sector flow | +$3.68B #1, persist 1.0 | 2026-06-25 | UW | tailwind (but = MU itself) |
| Market regime | TRANSITIONAL, breadth 35.4% | 2026-06-25 | UW | **headwind (reduce size)** |
| SPY 10d | 737.76→734.3, 4/6 days | 2026-06-25 | UW | mild headwind |

## Catalyst calendar (next 30d)

**Front-expiry implied move ±3.93% / ±$47.4** `[CTX:implied_move]` — phase-9 sizes
structures to this priced range; binaries below read against it.

| Date | Event | Likely impact | vs expected move |
|------|-------|---------------|------------------|
| ~2026-07-14/15 | June CPI release (BLS) | rates/risk-appetite | macro, ±X market-wide |
| ~2026-07-28/29 | FOMC meeting + rate decision | easing-cycle cut watch | macro, ±X market-wide |
| ongoing | DRAM/HBM contract-price prints, hyperscaler capex updates | memory-specific | could exceed ±3.9% on a surprise |
| 2026-09-22 | **MU next earnings** (far) | next binary | well beyond 30d |

*FOMC/CPI exact dates not pinned by WebSearch — quoted as the standard schedule
(late-July FOMC, mid-July CPI); confirm before trading the dates.*

## Tool / source errors

- **Apparent UW conflict (surfaced, not an error):** `market-regime.sector_rotation`
  shows Technology **−$71M (flowing out)** while `sector-flow` shows Technology
  **+$3.68B (flowing in, #1)**. These are different metrics — the regime's rotation
  field appears to net megacap-software selling (AAPL/MSFT/AMZN, phase-0.5) against a
  count/change basis, while `sector-flow` is **net call−put premium** dominated by
  MU. The `sector-flow` + persistence read is the relevant one for MU; recorded
  transparently.
- FRED: all series returned (key present). YoY not computed (limit=4 pull) — MoM
  run-rates used instead; directionally sufficient.

## Verdict for downstream phases

- **Net macro bias for MU:** **MIXED — strong structural tailwind, cautious tactical
  regime.** The AI-memory supercycle + easing Fed + falling yields are a genuine,
  earnings-backing tailwind; the TRANSITIONAL regime (35% breadth, "reduce size") +
  narrow leadership are a real near-term headwind that caps sizing. Lean **mild
  tailwind on fundamentals, headwind on tape** → **net neutral-to-slightly-positive
  with an explicit size cap.**
- **Conviction:** **3 / 5.**
- **Top 2 datapoints phase-9 must cite:** (1) **AI memory supercycle** (DRAM +90%
  QoQ, HBM sold out, capex +40%) — the fundamental engine; (2) **UW regime
  TRANSITIONAL, breadth 35.4%, "reduce size"** — the sizing governor.
- **Top 2 catalysts for phase-9 calendar:** (1) **~July 28-29 FOMC** (easing-cycle
  cut watch); (2) **ongoing DRAM/HBM pricing + hyperscaler capex prints** (the
  memory-specific catalysts that can move MU >±3.9%). No MU earnings until 9-22.
- **Sector-rotation verdict:** **ALIGNED, persistence 1.0** — but flagged
  **narrow/concentrated** (the inflow is largely MU) and **decelerating** ($9.4B→3.7B
  over 5 sessions). Phase-9 sizing input: aligned but discount the magnitude.
- **Correlation verdict:** **No concurrent positions** (MU is the only 2026-06-25
  blueprint) — gate skipped. Soft note: MU↔SNDK are co-moving (memory pair).
