# Phase 10 — Audit & Confidence Score

**Ticker:** USAR (USA Rare Earth, Inc.)
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T11:45:00-04:00
**Audited bias:** **LONG** (per phase-9-trade-plan.md)

## Summary

**Confluence score: 70 / 100** — strong-positive confluence on the LONG
bias to a $25 target. **Recommended bin per rubric: 0.75.**
**Phase-9 actual bin: 0.65** → **MISMATCH (deviated DOWN by 1 bin),
EXPLICITLY DOCUMENTED.** The deviation is well-reasoned and aligned
with phase-8 risk-monitor + phase-7 conviction_matrix confidence
(14.1%) + phase-7 signal_confluence absence in both bullish AND
bearish top-100. **One material contradiction** logged (phase-1 net
flow bearish today), resolved via phase-9's tight $19.46-close
invalidation. **All 3 spot-checked citations resolve.** **All sanity
checks pass.** Run is internally consistent and ready for action with
the conservative sizing already in place.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **−** | "Net call premium $3,017,909 vs put premium $2,829,686; net flow today net-bearish -$813,975; biggest sweep was 6/18 $18P ASK $349,878" — today's tape tilts bearish in $-terms even after acknowledging the structured-spread nuance [FLOW:options_flow_sweeps] |
| 2 — dark pool | **+** | "Large-tier `buy_ratio` 0.623, $18,618,110 premium across 118 trades; top print $505,960 @ $19.46 at NBBO ask" — accumulation real but capped by $24.18–$25.95 supply band [DP:block_stratified + DP:price_levels] |
| 3 — OI | **+** | "2028-01-21 $40P, +283 OI all-bid, $682,030 premium — biggest dollar LEAP commitment is BULLISH (synthetic long via deep-ITM put sale)" [OI:oi_smart_positioning] |
| 4 — structure | **++** | "$25 strike net_gex = +$383,535,631 (chain's dominant gamma node); ZGL $24.98; net DEX +$411,611,718 → dealers BUY underlying" — strongest structural confirmation for the upside thesis [STRUCT:gex + STRUCT:dex] |
| 5 — historical | **+** | "VRP -11.93% / IV percentile 22.22% / regime PREMIUM_BUYING" — vol is cheap on USAR's own scale; debit structures favored [HIST:vrp + HIST:iv_percentile_zscore] |
| 6 — macro | **+** | "Cantor Fitzgerald Overweight, PT $35" (+72% upside) + "Q1 EPS BEAT +42.9%" 2026-05-13 — countered by China critical-mineral supply return + TRANSITIONAL regime [MACRO:CantorFitzgerald_PT35 + MACRO:USAR_Q1_2026 + MACRO:ChinaCritMin_2025-11-09] |
| 7 — insights | **+** | "Conviction matrix DIRECTIONAL_LONG (14.1% confidence); Institutional accumulation B/S 1.65; Price-vs-flow DIVERGENCE flag" — supports thesis but low UW-composite confidence caps strength [INSIGHT:conviction_matrix + INSIGHT:institutional_accumulation] |
| 8 — agents | **+ (4/4 = 2L/2N/0S, 1 SKIP)** | accumulation-hunter LONG +2; contrarian-scanner LONG +2; sweep-tracker NEUTRAL 0; risk-monitor NEUTRAL 0; earnings-scout SKIPPED (next earnings 2026-08-10, > 30d) |

### Raw score computation

```
Phase 1:  −7
Phase 2:  +7
Phase 3:  +7
Phase 4: +15
Phase 5:  +7
Phase 6:  +7
Phase 7:  +7
Phase 8:  +4   (+2 acc-hunter, +2 contrarian, 0 sweep, 0 risk, SKIP)
─────────────
Raw:     +47

confluence_score = round( (47 + 115) / 230 × 100 ) = round(70.43) = 70
```

**Confluence score: 70 / 100**

### Bin mapping

| Score band | Recommended bin |
|------------|------------------|
| 65–79      | **0.75**         |

- **Rubric-recommended bin:** 0.75
- **Phase-9 actual bin:** 0.65
- **Match status:** **MISMATCH (−1 bin)** — phase-9 documented a
  conviction deviation in its `## Conviction deviation` section citing
  (1) phase-7 conviction_matrix confidence 14.1%, (2) phase-8
  risk-monitor sleeve cap mandate, and (3) phase-7 signal_confluence
  absence on both sides. Auditor accepts the downward deviation as
  consistent with the rubric's "always allowed to be smaller" clause
  and well-reasoned given the TRANSITIONAL macro regime.

## Contradictions

The only phase scored negatively (`−`) is phase-1:

- **phase-1 (options flow)**: Net flow today was net-bearish
  (bearish_premium $2.82M vs bullish_premium $2.00M, net -$813k) and
  the largest single sweep was an ask-side 6/18 $18 PUT for $349k.
  This contradicts the LONG bias in directional dollar-weighted flow
  terms. **Suggested resolution: tighten invalidation** — phase-9
  ALREADY tightened to "two daily closes below $19.46" which is
  exactly the price level where today's biggest at-ask DP buy print
  sits, plus a 60-minute reclaim window on an intraday $18.00 break.
  This is the correct response to the contradiction and **no further
  resolution is needed**. **Status: ADDRESSED.**

No `--` scores. No other contradictions.

## Citation failures

Spot-checked 3 thesis citations:

1. **`[DP:dark_pool_largest]`** — claim: "$505,960 at NBBO ask on
   $19.46". Phase-2 §Largest blocks table row:
   `14:16:55 | 19.460 | 19.45/19.46 | +0.005 | 26,000 | $505,960 | At ask — buy`
   → **✓ RESOLVES**.

2. **`[STRUCT:gex]`** — claim: "$25 strike +$383M GEX, ZGL $24.98".
   Phase-4 §GEX top-strikes table:
   `25 | +$383,535,631 | + | Mega gamma magnet / pin from above` and
   `Zero Gamma Level: $24.98` → **✓ RESOLVES**.

3. **`[HIST:vrp]`** — claim: "VRP at -11.93% (vol cheap vs realized
   110%)". Phase-5 §VRP block:
   `IV30d 98.95%, realised_vol30d 110.88%, VRP -11.93%, regime PREMIUM_BUYING`
   → **✓ RESOLVES**.

**Citation failures: NONE.** 3 of 3 resolve cleanly.

## Sanity checks

- [✓] **All `phase-*.md` files present** in `research/USAR/2026-05-20/`:
  phase-0 through phase-10 (this file) — 11 files total once this
  phase writes.
- [✓] **Phase-9 cites ≥3 distinct upstream datapoints** in thesis
  (actual: 7 listed in citation summary covering phases 2/3/4/5/6/8).
- [✓] **Conviction bin in {0.55, 0.65, 0.75, 0.85, 0.95}** — actual
  0.65.
- [✓] **≥1 directional + ≥1 defined-risk structure present** — debit
  call vertical (6/18 $20/$25) + put credit spread (6/18 $17/$14).
- [✓] **Sizing math shown** — Kelly inputs (p=0.65, b=8.33),
  raw_kelly=60.8%, fractional 15.2%, cap 5%, final 1.5% with
  documented downward deviation rationale.
- [✓] **Disclaimer line present** at top of phase-9.
- [✓] **Upstream chain consistency** — every phase MD cites ≥1 prior
  phase by path, no orphan claims observed.

All checks pass.

## Final auditor note

The run is **internally consistent and ready for action**. The LONG
bias to $25 is supported by an unusually strong structural confluence
([STRUCT:gex] $25 magnet + [DP:price_levels] $25 supply + [STRUCT:gex]
ZGL $24.98 all stacking at the same level) and corroborated by today's
dark-pool accumulation and the bullish 2028 LEAP put-write, with the
only material contradiction (today's net-bearish flow tape) properly
absorbed into a tight invalidation at the $19.46 dark-pool floor. The
**conviction-bin deviation from 0.75 down to 0.65 is appropriate and
documented**, reflecting genuine regime caution (TRANSITIONAL +
risk-monitor sleeve cap + UW 14.1% confidence) rather than thesis
weakness. Trade is **fit for the recommended 1.5% book-risk sizing**
and the 6/18 expiry / 6/17 hard-exit framing avoids the FOMC + OPEX
collision risk identified in the phase-6 catalyst calendar.
