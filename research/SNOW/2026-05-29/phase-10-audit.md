# Phase 10 — Audit & Confidence Score

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Dominant bias audited (phase-9):** RANGE / fade-the-$255-wall

## Summary

**Confluence score = 69 / 100** (base 74 − 5 sentiment-CAUTION penalty) →
recommended bin **0.75**; phase-9 deviated **down one bin to 0.65** (a permitted
downward move) on the phase-7b short-veto + the unrefuted squeeze tail. **The run
is internally consistent and unusually well-aligned** — flow (distribution),
structure (long-gamma pin), history (RSI-87 parabola), and insights (bearish
divergence) all point to the same fade/range read, and the phase-8b debate
**cleared** it (bull 0.70 vs bear 0.58, not disconfirmed). The one genuine tension
is **phase-7b: the strong-buy hyper-grower fundamentals VETO a *short*** — which
contradicts a fade direction — and phase-9 resolved it correctly by making the
trade **defined-risk only (no naked short)**. **No earnings-date contamination
this run** — the 5/27 earnings was cross-checked at intake (the lesson from the
PATH run was applied). Contradiction count: **1** (phase-7b vs the fade,
intentional and resolved). 3/3 spot-checked citations resolve.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | `+` | Largest sweep is a $14M bid-side call sale; gross $232M call premium is ITM-0DTE closing; net bull/bear slightly bearish `[FLOW:sweeps]` |
| 2 — dark pool | `++` | **Mega tier net seller, buy_ratio 0.401** (516K sold vs 345K), closing blocks at the $255.55 high `[DP:block-stratified]` |
| 3 — OI | `0` | Mixed — ITM calls closed (supports fade) but fresh OTM $280–$350 calls opened (continuation, against fade) `[OI:biggest-increases]` |
| 4 — structure | `++` | **Long gamma +$35.2M, walls $255 (+$9.1M) / $250 (+$7.2M) straddle spot — pinned** `[STRUCT:gex]` |
| 5 — historical | `++` | **RSI 86.9, +53.8% above SMA20, +52% run** — parabolic, mean-reversion supports the fade `[HIST:rsi fz]` |
| 6 — macro | `0` | Tech sector leading (headwind for a fade) offset by TRANSITIONAL "iron condors in range" regime `[MACRO:MarketRegime]` |
| 7 — insights | `+` | **price-vs-flow bearish divergence** ("price +77.5% but flow bearish"), conviction-matrix MIXED 0.6% `[INSIGHT:price-vs-flow]` |
| 7b — fundamentals | `-` | **VETO of the short** — strong-buy hyper-grower (+29% rev, 3/3 beats, target $284) contradicts a fade direction `[FUND:peer_pe fz]` |
| 8 — agents | `+` (+10) | 4 RANGE + 1 NEUTRAL-down-skew all align with the fade/range; 0 LONG / 0 SHORT |

**Raw score (symmetric):** 7+15+0+15+15+0+7−7 = **+52** (phases) + **+10** (phase-8)
= **+62**
**Base score:** round((62 + 130) / 260 × 100) = **74 / 100**
**Debate penalty (phase-8b):** **−0** (NOT disconfirmed — bull 0.70 vs bear 0.58)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** **69 / 100**
**Recommended bin (65–79 band):** **0.75**
**Phase-9 actual bin:** **0.65** — **MISMATCH (intentional downward deviation)**:
the phase-7b VETO on the short direction and the unrefuted phase-8b >$262 squeeze
tail are real disconfirming evidence; a downward bin move is permitted and honest.

## Contradictions

- **phase-7b (fundamentals) vs the fade bias:** SNOW is a strong-buy hyper-grower
  (+29% revenue, 3/3 beats, target $284, Recom 1.40) — the fundamentals **VETO a
  directional short**, which contradicts a fade direction. — *Resolution applied:*
  phase-9 expresses the fade as **defined-risk only** (bear call spread / iron
  condor, no naked short), and deviated conviction down to 0.65. The fundamental
  strength is *why* the trade is capped-risk, not a directional short.
- *(Phases 3 and 6 scored `0` — genuine mixed/neutral, not contradictions: phase-3
  has offsetting ITM-close vs OTM-open flow; phase-6 has sector-tailwind vs
  range-regime. Both correctly neutral.)*

## Citation failures

(none — all 3 spot-checked resolved)
- `[DP:block-stratified]` "mega tier net seller 0.401, 516K sold vs 345K" →
  **resolves**, phase-2-dark-pool.md §Tier breakdown ✓
- `[STRUCT:gex]` "long gamma +$35.2M, walls $255 +$9.1M / $250 +$7.2M" →
  **resolves**, phase-4-structure.md §GEX ✓
- `[INSIGHT:price-vs-flow]` "bearish divergence, price +77.5% but flow bearish" →
  **resolves**, phase-7-insights.md §Price vs flow ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + decision.json
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary)
- [✓] Conviction bin ∈ {0.55…0.95} → 0.65
- [✓] ≥1 directional (bear call spread $265/$280) + ≥1 defined-risk (iron condor)
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate 0.50 (capped), with the
  range/fade proxy caveat noted
- [✓] All five risk gates evaluated (fundamentals **VETO**-short / sentiment
  **CAUTION** / correlation **none** (ρ 0.478 vs PATH) / rotation **adverse** to
  fade / debate **not disconfirmed**); phase-0.5 GENUINELY_UNUSUAL reflected (no
  cap, edge in data)
- [✓] Structures sized to expected move; `expected_move` (0.55%/$1.40 daily,
  ~±$6.3 over June-18) in JSON; condor profit zone $240–$265 contains the 1σ move
- [✓] `decision.json` exists and **passes `validate_decision.py`**;
  confluence_score 69 + recommended_bin 0.75 backfilled
- [✓] **Earnings date cross-checked at intake** (5/27 AMC) — no contamination
  (PATH-run lesson applied)

## Final auditor note

This is a **clean, well-aligned, internally consistent fade/range blueprint** —
the distribution, gamma pin, parabolic extension, and flow divergence all
corroborate, the debate cleared the thesis, and the one tension (strong
fundamentals vs a fade) was correctly resolved by forcing a defined-risk,
no-naked-short structure. **Ready for action** as a defined-risk iron condor /
bear call spread at the $255 wall, sized small (1.0%) per the half-size regime and
the sentiment-CAUTION gate, with the >$262 dealer-short-call squeeze as the live
invalidation to monitor.
