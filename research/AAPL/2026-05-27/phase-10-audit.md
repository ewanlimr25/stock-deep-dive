# Phase 10 — Audit & Confidence Score

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T04:15:00Z
**Dominant bias audited:** RANGE (phase-9)

## Summary

**Confluence score 60/100 → recommended bin 0.65; phase-9 chose 0.55** (one notch
lower, by the documented phase-8b disconfirmation down-shift — consistent, not an
error). The run is **internally coherent**: every phase points the same way — *this
is a low-conviction, range-bound, fade-strength setup, not a directional long.* The
score sits just above the 50 "perfectly mixed" line because the **range mechanics
are strong and consistent** (long-gamma pin at 310 ‹phase-4 ++›, TRANSITIONAL
"iron-condors-in-range" regime ‹phase-6 ++›) while the residual **bullish
cross-currents are real but weak** (net +$17.4M flow, +24% trend, improving
ratings, tech-sector inflow) — they keep the score from going higher and are why
the desk landed on RANGE rather than SHORT. **0 hard contradictions (no phase
scored negative); all 3 spot-checked citations resolve; decision.json valid.**
The blueprint is ready for action as written — a small, defined-risk pin-harvest.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | 0 | "net_flow (bull−bear) +$17.42M", "call ask-side fraction 0.53" `[FLOW:insights_deep_dive]` — too weak/two-way to be directional; neutral for range (BUSY_NAME-capped) |
| 2 — dark pool | 0 | mega buy 0.867 is a "23-second closing-cross artifact", rank 14 `[DP:extended_hours]` — no genuine directional accumulation (BUSY_NAME-capped) |
| 3 — OI | 0 | smart-positioning "MIXED"; largest move a 300C "−12,646" unwind `[OI:decrease_with_volume]` — no directional structure |
| 4 — structure | ++ | "POSITIVE / long gamma", dominant wall "+109.5M" at 310 = spot pin `[STRUCT:gex]` — textbook range mechanic |
| 5 — historical | + | "RSI 78.85", "−0.31% from 52W high", IV "6.25 percentile" `[HIST:rsi fz]` — overbought-at-highs supports fade/mean-reversion |
| 6 — macro | ++ | regime "TRANSITIONAL — reduce position size, iron condors in range" `[MACRO:MarketRegime_2026-05-27]` — explicitly range-prescriptive |
| 7 — insights | 0 | conviction-matrix "DIRECTIONAL_LONG, confidence 17%"; "AAPL absent from bullish signal-confluence top-50" `[INSIGHT:signal_confluence]` — directional label at near-zero confidence = neutral |
| 7b — fundamentals | + | "tier_adjustment CAUTION", rich PE 37.6x + "MSPR −100" `[FUND:mspr_2026-05]` — caps upside, supports the no-long/fade read |
| 8 — agents | +8 | **4/4 RANGE**, avg conviction 2.0 (accumulation/sweep/contrarian/risk all RANGE) |

**Raw score (symmetric):** 0+0+0+15+7+15+0+7 + 8 = **52**
**Base score:** round((52 + 130) / 260 × 100) = **70/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.55 vs
bear_residual 0.85)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment CAUTION, crowd_state
CROWDED_LONG)
**Confluence_score:** 70 − 5 − 5 = **60/100**
**Recommended bin (band 50–64):** **0.65**
**Phase-9 actual bin:** **0.55** — MATCH-after-adjustment: the phase-8b
disconfirmation gate down-shifts the operating bin one notch (0.65 → 0.55) per
`rubrics/sizing-rubric.md` §"Risk gates". Deliberate and documented, not a
deviation error.

## Contradictions

**No phase scored `-` or `--`** — there are no hard contradictions to the RANGE
bias. The run's only tension is a *soft, sub-threshold* one worth recording for the
calibration loop:

- **Residual bullish cross-currents vs the fade-tilted range (phases 1/5/6/7).**
  The flow leans mildly bullish (+$17.4M), the stock is in a +24% uptrend with
  improving analyst ratings and a durable tech-sector inflow, while the
  structure/sentiment/fundamentals say range/fade. **Resolution applied:** phase-9
  correctly resolved to **RANGE (not SHORT)** and a *fade-strength* tilt, sizing the
  directional component to a token starter and recommending a defined-risk condor.
  **Watch datapoint:** a close **>315 on vol_x >1.2** would convert the bullish
  cross-current into a genuine breakout and invalidate the range — already encoded
  in phase-9's invalidation and monitoring checklist. No downgrade needed beyond the
  gates already applied.

## Citation failures

**None.** All 3 spot-checked phase-9 thesis citations resolve:
1. `[FLOW:insights_deep_dive]` → phase-1 §Whole-tape: "call ask-side fraction **0.53**",
   "net_flow … +$17.42M". ✓
2. `[STRUCT:gex]` → phase-4 §GEX: "**310** … **+109.5M** … dominant wall = spot pin". ✓
3. `[HIST:rsi fz]` → phase-5 §Price context: "RSI(14) **78.85**", "52W High 311.82
   (**−0.31%**)". ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in thesis + citations block).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → **0.55**.
- [✓] ≥1 directional (312.5/305 put debit spread) + ≥1 defined-risk (300/305–
  317.5/322.5 iron condor) structure.
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate (p_raw 0.857 → N-capped 0.75),
  not the bin.
- [✓] All five risk gates evaluated in phase-9: fundamentals **CAUTION**, sentiment
  **CAUTION** (CROWDED_LONG), correlation **AAPL↔NVDA 0.736 cluster**, rotation
  **aligned**, debate **disconfirmed**; context **BUSY_NAME_NORMAL_DAY** reflected
  (no top-of-band sizing).
- [✓] Structures sized to front-expiry expected move (±1.19% / $3.69); shorts
  (305/317.5) sit outside it; `expected_move` present in JSON.
- [✓] `decision.json` exists and passes `validate_decision.py` (**OK**), with
  `context`, `expected_move`, and `gates.sentiment` fields populated; `confluence_score`
  (60) and `recommended_bin` (0.65) backfilled.

## Final auditor note

The run is internally consistent and ready for action: every phase converges on a
**low-conviction, range-bound, fade-strength** read, the gate cascade
(two CAUTIONs + correlation cluster + debate disconfirm + BUSY_NAME context)
correctly floors size to a ~1% defined-risk pin-harvest, and the bias is honestly
**RANGE** rather than chasing the mildly-bullish flow into an overbought 52-week
high. No revision required — the only action item is to respect the up-invalidation
(close >315 on real volume) and net the AAPL↔NVDA correlation cluster before sizing.
