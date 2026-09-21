# Phase 10 — Audit & Confidence Score

**Ticker:** GRAB
**As-of date:** 2026-05-21
**Generated:** 2026-05-21T21:35:00Z
**Auditor scope:** all upstream phases 0–9 in
`/Users/ewan/Development/stock-deep-dive/research/GRAB/2026-05-21/`

## Summary

Phase-9 bias = **LONG (modest), 0.55 conviction**. Raw confluence score
**+39 / ±115** which normalizes to **67/100** — within the "65–79" band
that the rubric maps to a **0.75 conviction bin**. Phase-9 chose **0.55**,
i.e. **two bins BELOW the rubric recommendation** — this is a
DOWNWARD deviation which the rubric explicitly allows without explanation
(sizing-rubric: "always allowed to be smaller"). The deviation is
intentional and defensible because (a) the TRANSITIONAL UW regime
[MACRO:MarketRegime_2026-05-21 UW] explicitly recommends "half position
sizes", (b) two phases (1 and 5) print bearish-aligned signals
contradicting the LONG bias, and (c) `insights_conviction_matrix`
confidence is only 26.81% [INSIGHT:conviction_matrix]. **The run is
internally consistent and the trade plan is ready for action with the
conservative sizing already baked in.** Two contradictions logged; all
three spot-checked citations resolve.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| **1 — flow** | **-** (-7) | "GRAB: 5/5 sessions in top sweep activity, bearish dominant, total_sweep_premium $847,155" [FLOW:sweep_persistence] — multi-day momentum signal still printing against the LONG bias; today's tape is mixed (LEAP $4 straddle) and softens the signal but does not reverse it. |
| **2 — dark pool** | **++** (+15) | "$2.91M block — 817,675 sh at $3.56 NBBO mid, 21:02Z post-bell + block-tier buy_ratio 1.00 + large-tier buy_ratio 0.608" [DP:largest, DP:block_stratified] — unambiguous institutional accumulation. |
| **3 — OI** | **+** (+7) | "Net premium-weighted call writing ~$237K SELL vs ~$110K BUY on LEAP strikes; +159 OI 2026-10 $4P opened on ask = covered-call overlay on long stock" [OI:smart_positioning, OI:biggest_increases] — consistent with hedged-long, mildly supportive. |
| **4 — structure** | **++** (+15) | "365-DTE GEX POSITIVE regime, ZGL $2.63 (26% below spot), $245.4M GEX at $4 strike (dominant magnet); 25Δ 30DTE skew -0.079 = COMPLACENT" [STRUCT:gex, STRUCT:term_skew] — long-gamma + bullish-skew confluence. |
| **5 — historical** | **-** (-7) | "90d cumulative premium flow NET -$6,283,288 BEARISH (bullish $10.3M vs bearish $16.6M); 26 of 30 days printed bearish flow; price -10% from $3.91 → $3.55" [HIST:cumulative_premium_flow, HIST:historical_trend] — sustained multi-week bearish trend that today's accumulation is the first credible counter to. |
| **6 — macro** | **+** (+7) | "Tech sector inflow $297M + Financial Services +$15.3M today; Fed funds 3.50–3.75% with 4 dissenters (most since 1992); UW regime TRANSITIONAL (half-size guidance)" [MACRO:SectorRotation_2026-05-21 UW, MACRO:FOMC_2026-04-29 WebSearch:federalreserve.gov, MACRO:MarketRegime_2026-05-21 UW] — net mild tailwind, capped by regime caveat. |
| **7 — insights** | **+** (+7) | "conviction_matrix = DIRECTIONAL_LONG with confidence_pct = 26.81; institutional_accumulation = ACCUMULATION at 2.91× buy/sell ratio (1.75M vs 0.6M sh); price_vs_flow no divergence" [INSIGHT:conviction_matrix, INSIGHT:institutional_accumulation, INSIGHT:price_vs_flow] — UW composite is LONG but confidence is unusually low (caps the score at + not ++). |
| **8 — agents (4 of 5)** | **+2 / ±10** | 1 LONG (accumulation-hunter, conv 3, +2), 2 RANGE (contrarian-scanner conv 2, sweep-tracker conv 2 → 0 each), 1 NEUTRAL (risk-monitor conv 2 → 0), 1 MISSING (earnings-scout, next earnings 2026-07-30 > 30d). Net contribution: **+2**. |

**Raw score:** -7 + 15 + 7 + 15 - 7 + 7 + 7 + 2 = **+39 / ±115**
**Confluence_score:** (39 + 115) / 230 × 100 = **67 / 100**
**Recommended conviction bin (65–79 band):** **0.75**
**Phase-9 actual bin:** **0.55**
**Match status:** **MISMATCH — phase-9 deviated 2 bins LOWER**

### Mismatch analysis (allowed by rubric)

Per `rubrics/sizing-rubric.md`: "Phase-9 may set `final_size_pct <
suggested_size_pct` without explanation (always allowed to be smaller)."
The same principle applies to conviction bin selection — downward
deviation from the score-recommended bin is permitted without a formal
`deviation_reason`. Phase-9 provided the reason anyway in its "Why this
bin" line: TRANSITIONAL regime + 90d bearish trend + low UW confidence.

The downward deviation is **defensible and conservative** — exactly what
the auditor wants to see. If phase-9 had picked 0.85 or 0.95, that
would have been an upward deviation requiring a `sizing_deviation_reason`
that the data does not currently support.

## Contradictions

- **phase-1 (flow):** `sweep_persistence` shows 5/5 sessions bearish with
  cumulative $847K [FLOW:sweep_persistence] versus phase-9's LONG bias —
  **Suggested resolution:** TIGHTEN INVALIDATION. Phase-9's signal-based
  invalidation already references `cumulative_premium_flow` (3-day) flip;
  consider adding a hard "if sweep_persistence dominant_direction stays
  bearish for 3 more sessions AND price < $3.50, exit early" rule.
  Confirmed already partially addressed in phase-9 monitoring checklist
  (daily premium flow check).

- **phase-5 (historical):** 90d net premium flow -$6.28M BEARISH and
  26-of-30 days bearish flow [HIST:cumulative_premium_flow,
  HIST:historical_trend] versus phase-9's LONG bias —
  **Suggested resolution:** WAIT FOR CONFIRMATION. accumulation-hunter
  agent explicitly noted that "conviction is capped until a second
  session of confirmation" [AGENT:accumulation-hunter]. Phase-9 honors
  this by sizing at 0.55 (below the recommended 0.75 bin) and entering
  on a $3.50–$3.52 retest. If 2026-05-22 prints another bearish flow
  day, phase-9 should defer entry by one more session.

## Citation failures

(none — all spot-checks below resolved)

### Citation spot-checks (3 from phase-9 thesis)

1. **[DP:largest]** — "$2.91M block executed at 21:02Z, 817,675 shares at
   $3.56 NBBO-mid" — **VERIFIED** in phase-2-dark-pool.md §Largest blocks
   table row 1: "executed_at 2026-05-21T21:02:29Z, price 3.56, size
   817,675, premium $2,910,923, NBBO bid 3.55 / ask 3.57, trade_vs_mid
   ~0.00 (mid)". ✓ RESOLVES.

2. **[STRUCT:gex]** — "$245M LEAP GEX at $4 strike, ZGL $2.63" —
   **VERIFIED** in phase-4-structure.md §GEX 365 DTE table:
   "strike 4.0 → net_gex 245,418,226" and the line "total_gex
   $1,053,800,004 — POSITIVE regime, ZGL = $2.63". ✓ RESOLVES.

3. **[HIST:cumulative_premium_flow]** — "Net 90d flow -$6,283,288
   BEARISH" — **VERIFIED** in phase-5-historical.md §Cumulative premium
   flow: "cumulative_bullish $10,314,835, cumulative_bearish
   $16,598,123, net -$6,283,288, trend_direction BEARISH". ✓ RESOLVES.

## Sanity checks

- [✓] All `phase-*.md` files present in `research/GRAB/2026-05-21/`
  (phases 0 through 9, plus this audit makes 11 total).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (cites 7 in the
  Citations summary; thesis paragraph alone references 4 — DP:largest,
  INSIGHT:institutional_accumulation, STRUCT:gex, HIST:cumulative_premium_flow,
  HIST:vrp, MACRO:MarketRegime, AGENT:accumulation-hunter).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} — phase-9 = 0.55.
- [✓] At least 1 directional + 1 defined-risk structure present —
  phase-9 has both: call debit spread (directional) + put credit spread
  (defined-risk).
- [✓] Sizing math shown explicitly — Kelly inputs (p=0.55, b=1.50,
  fraction=0.25), raw Kelly 25%, suggested 6.25%, TRANSITIONAL halving
  to 3.13%, final 3.0%.
- [✓] Disclaimer line present at top of phase-9.
- [✓] Invalidation has all 3 categories (price, signal, macro).
- [✓] Catalyst calendar covers next 30d with FOMC and OPEX dates.

## Final auditor note

The run is **internally consistent** and ready for action. The
confluence score of 67/100 normally maps to a 0.75 conviction bin,
but **phase-9's deliberate down-shift to 0.55 is the correct judgment
call** given the (a) TRANSITIONAL regime, (b) phase-1 and phase-5
contradictions, and (c) low 26.81% conviction-matrix confidence — a
0.75 bin would over-state the actual structural strength of the setup
in a way that risks pulling forward gains on a single-institution
accumulation signal that has not yet been confirmed by a second
session. **No revisions required.** Optional improvement: add a
1-session deferral trigger if 2026-05-22 prints bearish flow ≥-$200K
again (this aligns the entry trigger with the accumulation-hunter's
"second session of confirmation" caveat).
