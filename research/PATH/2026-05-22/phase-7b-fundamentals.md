# Phase 7b — Deep Fundamentals & Quality Veto (FINNHUB)

**Ticker:** PATH (UiPath Inc.) — US equity
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-7-insights.md, phase-2-dark-pool.md, phase-5-historical.md

## Summary

The underlying business **quality is solid and CONFIRMS (does not veto) the mild long-lean**
from phases 2/3/4/7. UiPath is a **profitable, debt-free, high-gross-margin (83%) software
company** with **+12.6% TTM revenue growth** and a clean balance sheet (current ratio 2.48,
no long-term debt, beta 0.93), trading at a **reasonable PE 20 / PS 3.5** — and **near its
52-week low** ($10.99 vs range $9.20–$19.84, i.e. ~45% off the high). The two most recent
quarters **both beat** (+7.4%, +15.5% EPS surprise), so trailing earnings momentum is
positive. The genuine blind spot: **forward EPS/revenue consensus is paid-tier (403)** and
**MSPR insider data is empty**, so I can't see whether estimates are being cut into the
05-28 print — but nothing in the available data deteriorates on ≥2 axes, so **no veto**.
The real fundamental overhang is structural, not statremental: decelerating growth + the
agentic-AI-vs-RPA disruption debate. `tier_adjustment = CONFIRM`, `contradiction_count = 0`.

## Key signals

- **Gross margin 83.2% TTM**, net margin 17.5%, ROE 15.3% — quality SaaS economics [FUND:grossMarginTTM] · [FUND:roeTTM]
- **Revenue growth +12.65% TTM YoY** — positive but decelerating [FUND:revenueGrowthTTMYoy]
- **2/2 recent earnings beats:** Q ending 2026-03-31 actual $0.30 vs est $0.26 (**+15.5%**); 2025-12-31 $0.16 vs $0.149 (**+7.4%**) [FUND:earnings_surprise]
- **Clean balance sheet:** current ratio 2.48, **no LT debt**, beta 0.93 [FUND:currentRatioQuarterly]
- **Valuation reasonable & near 52w low:** PE 20.1, PS 3.53, PB 3.22; price $10.99 vs 52w $9.20–$19.84 [FUND:peTTM] · [FUND:52WeekLow]

## Detailed findings

### Valuation (vs peers)

PE(TTM) **20.1**, PS(TTM) **3.53**, PB **3.22**, PEG n/a. Peers (Finnhub): GEN, RBRK, FROG,
**S** (SentinelOne), DLB, NTSK, **GTLB**, CVLT, QLYS, **VRNS**, MSFT. PATH at ~3.5× sales sits
on the **cheaper end** of the security/dev-tools software cohort (high-growth names like S,
GTLB trade richer) — consistent with a de-rated, beaten-down name. Cheap-ish, not a deep
value trap given it's profitable. (Metric ratios are TTM-current; for a 2026-05-22 as-of the
TTM runs through the Jan-2026 quarter — pre the 05-28 print — so it is approximately
point-in-time; flagged per phase guidance.)

### Growth profile

Revenue **+12.65% YoY (TTM)** — positive but clearly decelerated from UiPath's historical
20-30%+. Gross margin **83.2%** (top-tier SaaS); operating margin **3.52% GAAP** (thin —
profitability leans on scale + interest income on the cash pile), net margin **17.5%**. The
growth-deceleration + thin-GAAP-margin combo is the fundamental tension: the multiple holds
only if growth stabilizes. Not deteriorating enough to veto, but the key thing the 05-28
guide will be judged on.

### Earnings-surprise history

| Period | Actual EPS | Estimate | Surprise % |
|--------|-----------:|---------:|-----------:|
| 2026-03-31 (FQ4'26) | $0.30 | $0.2597 | **+15.5%** |
| 2025-12-31 (FQ3'26) | $0.16 | $0.149 | **+7.4%** |

**Beat-rate 2/2** on the available history (free tier returned only 2 distinct quarters).
Positive earnings momentum into the print — a CONFIRM for the long-lean. (Caveat: 2-quarter
sample; not the full 8-quarter beat-rate the rubric prefers.)

### Forward consensus

**Unavailable — `eps-estimate` and `revenue-estimate` both 403 "You don't have access"
(paid-tier).** This is the material blind spot: I cannot see whether the Street is revising
the 05-28 numbers up or down, nor the implied guide. Phase-7c (analyst revisions via
WebSearch/Finnhub news) must try to fill this.

### Balance-sheet & cash-flow

Statements endpoint not pulled in detail; proxying from metrics: **current ratio 2.48** (very
liquid), **no long-term debt** (`longTermDebtEquity` null), ROA 9.98%. UiPath is known to
carry a large net-cash position with positive FCF — the balance sheet is a strength and
removes solvency risk from the thesis. No red flag.

### Insider signal (MSPR)

**No data** — `insider-sentiment` returned an empty array for 2025-05-22→2026-05-22. Per the
rubric, absence is a *weak* signal, **not** bullish; this axis is simply unobserved (NA).

### Peers

GEN, RBRK, FROG, S, DLB, NTSK, GTLB, CVLT, QLYS, VRNS, MSFT — enterprise software / security
/ dev-tools. Relative value: PATH is cheaper on sales than the faster-growers, reflecting its
growth deceleration and the RPA-disruption discount.

## Red flags

1. **Decelerating revenue growth** (12.6%, down from historical highs) + thin GAAP operating
   margin (3.5%) — the multiple is growth-dependent.
2. **Forward consensus invisible** (paid-tier) — cannot confirm estimate direction into the
   binary print; trailing beats ≠ guaranteed guide.
3. **Secular overhang:** agentic-AI / genAI as both opportunity and disruption risk to the
   legacy RPA franchise — a narrative the 05-28 call will address (qualitative).

None of these is a *deterioration on ≥2 axes*, so no veto — but #1 and #3 are real risks.

## Tool / source calls (audit trail)

| Endpoint | Status | Result |
|----------|--------|--------|
| `/stock/metric?metric=all` | ✅ | PE 20.1, GM 83.2%, rev growth 12.65%, ROE 15.3%, no LT debt |
| `/stock/earnings?limit=8` | ✅ (2 qtrs) | 2/2 beats (+15.5%, +7.4%); filtered ≤ 2026-05-22 |
| `/stock/eps-estimate` | ❌ 403 | paid-tier, skipped |
| `/stock/revenue-estimate` | ❌ 403 | paid-tier, skipped |
| `/stock/peers` | ✅ | 11 software/security peers + MSFT |
| `/stock/insider-sentiment` (MSPR) | ✅ (empty) | no data for the window |

## Tool / source errors

- `eps-estimate` / `revenue-estimate`: HTTP 403 "You don't have access to this resource" —
  **paid-tier, skipped**. Forward-consensus direction unavailable; flagged as the key blind
  spot for phase-9 (and handed to phase-7c).
- MSPR returned empty (no insider-sentiment rows) — unobserved, not bearish.

## Verdict for downstream — quality gate

```
fundamental_signal:  NEUTRAL-to-BULLISH   (solid quality, positive earnings momentum, reasonable valuation near 52w low)
tier_adjustment:     CONFIRM              (no deterioration on ≥2 axes → no cut, no veto)
contradiction_count: 0                    ({earnings_trend: CONFIRM, growth/margins: CONFIRM/neutral, insider_MSPR: NA})
key_risks:           ["decelerating rev growth (12.6%) + thin GAAP op margin → multiple is growth-dependent",
                      "forward consensus invisible (paid-tier) — cannot see estimate direction into 05-28 guide",
                      "agentic-AI/RPA disruption narrative is the 05-28 call's swing factor"]
```

- **Phase-9 effect:** no-op (CONFIRM). The fundamentals **support** reading phase-2's
  accumulation as genuine rather than distribution-into-strength — UiPath is a profitable,
  debt-free, beaten-down quality name, not a melting ice cube. This *removes the distribution
  veto* on the long-lean, but per phase-7b rules it **cannot raise** conviction.
- **Open question carried:** the entire thesis hinges on the 05-28 *guide* (which trailing
  beats don't determine and forward consensus would have shown). The defined-risk framing
  from phases 5–6 remains the right posture into an un-seeable binary.
