# Phase 10 — Audit & Confidence Score

**Ticker:** PATH · **As-of:** 2026-07-17 · **Version:** v1
Dominant bias audited: **LONG (slight, accumulation-backed)** — phase-9.

## Summary

**Confluence score: 46/100** (band 30–49 → recommended bin **0.55–0.65**).
Phase-9's actual bin **0.55 = MATCH** (bottom of the band, the honest place for a
QUIET, disconfirmed, negative-Kelly setup). The run is **internally consistent**:
every phase corroborates the same picture — genuine institutional accumulation
trapped in a dealer-capped $11.88–$13 range with a negative empirical edge and a
headwind macro — and the low score is *correct*, not a defect. Two phases mildly
contradict the LONG (5-historical: weak backtest + rich VRP; 6-macro: hawkish
Fed/rising VIX), the phase-8b debate disconfirmed the long (−5 penalty), and the
phase-0.5 QUIET verdict capped the flow phases at 0. No hard contradictions, no
fabrications, all citations resolve. **Ready for action as written** — a
watch-only / defined-risk-carry range trade, not a directional recommendation.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **0** | 5-day sweep-persistence bullish (5/5, $6.19M) `[FLOW:sweep_persistence]` but **QUIET verdict caps 1–2 at 0**; net_flow only +$182k, biggest print a two-sided roll. |
| 2 — dark pool | **0** | Large tier **65.7% buy** ($258M) `[DP:block_stratified]` = real accumulation, but **QUIET caps at 0** (PATH outside DP top-40, mega tier empty). |
| 3 — OI | **+** | Chain **call-owned every tenor** (P/C 0.05–0.57), Nov $16C +4,255, no rolls `[OI:term_structure]` — structurally bullish (docked: same OI is the $13 cap). |
| 4 — structure | **0** | GEX **POSITIVE** + DEX supportive bid, but **$13 hard cap + max-pain $11–$11.5** `[STRUCT:gex]` = range, net-neutral for a directional long. |
| 5 — historical | **−** | OI building 11 days but **bullish_flow backtest 14.3% (n=7)** + **VRP +0.289 rich** + 90d MIXED `[HIST:signal_backtest]` — weak/negative edge for a long. |
| 6 — macro | **−** | **TRANSITIONAL "half size" + hawkish Fed (63% Sept-hike) + VIX +12% d/d** `[MACRO:FOMC]` — headwind for high-multiple software (tech-inflow tailwind partial offset). |
| 7 — insights | **+** | **DIRECTIONAL_LONG** + institutional-accumulation ACCUMULATION (1.96) `[INSIGHT:conviction_matrix]` — but 26.1% conf, absent from confluence top-60. |
| 7b — fundamentals | **0** | `tier_adjustment = NA` (no Finnhub key) `[FUND:balance_sheet]` — qualitatively high-quality/non-contradicting, but NA scores 0 per rule. |
| 8 — agents | **+2** | accumulation-hunter LONG (+2); contrarian NEUTRAL / sweep NEUTRAL / risk-monitor RANGE (0 each); earnings-scout skipped. Net +2. |

**Raw score (symmetric):** 0+0+7+0−7−7+7+0+2 = **+2**
**Base score:** round((2 + 130) / 260 × 100) = **51/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.55 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** −0 (tier_adjustment = CONFIRM)
**Confluence_score:** **46/100**
**Recommended bin:** **0.55–0.65** (band 30–49) → **0.55** (low end, given disconfirmed + QUIET)
**Phase-9 actual bin:** **0.55** — **MATCH**

## Contradictions

- **phase-5 (historical):** the LONG's empirical edge is *negative* — bullish_flow
  backtest 14.3% (n=7) and VRP +0.289 (rich IV penalizes long premium) fight the
  directional thesis. — **Resolution applied:** phase-9 sized directional to **0%**
  (negative Kelly) and expressed the trade as a premium-*selling* range harvest, which
  turns the rich VRP into an edge. Correctly handled.
- **phase-6 (macro):** hawkish Fed + rising VIX + "half-size" regime are a headwind for
  a high-multiple growth long. — **Resolution applied:** conviction held at the floor
  (0.55), directional size 0, defined-risk pre-earnings structures only, with FOMC
  Jul-29 and VIX>20 written as explicit macro invalidations. Correctly handled.

(Phases scored `0` are not contradictions — they are QUIET-capped or NA, i.e. thin
confirmation, not conflict.)

## Citation failures

None — 3 of phase-9's thesis citations spot-checked, all resolve:
1. `[DP:block_stratified]` "large tier 65.7% buy" → phase-2 §Tier breakdown (`large buy_ratio 0.657`). ✓
2. `[HIST:oi_trend]` "11 consecutive days +337k" → phase-5 §OI trend (`consecutive_build_days 11, +337,036`). ✓
3. `[STRUCT:gex]` "peak +6.03M at $13, ZGL $6.78" → phase-4 §GEX (`$13 +6,034,671; zero_gamma_level $6.78`). ✓

## Sanity checks

- [✓] All phase files present (0, 0.5, 1–7, **7b, 7c, 8, 8b, 9**) + `decision.json`.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- [✓] Conviction bin ∈ {0.55…0.95} → **0.55**.
- [✓] ≥1 directional (Sep-18 $12.5/$14 call debit spread) + ≥1 defined-risk (Aug-21 iron condor).
- [✓] Sizing math shown; Kelly `p = 0.143` = phase-5 empirical win-rate (not a bin fallback); raw_kelly −0.169 → directional 0.
- [✓] All five risk gates evaluated: fundamentals **NA**, sentiment/crowd **CONFIRM/CROWDED_SHORT**, correlation **none (OKLO <0.70)**, rotation **aligned**, debate **DISCONFIRMED (fired)**.
- [✓] Phase-0.5 `unusual_verdict = QUIET` reflected in sizing (starter cap → 0 directional).
- [✓] Structures sized to front-expiry expected move; `expected_move` (1.13% / $0.14) in JSON, with the N4 tightness check documented on the condor.
- [✓] `decision.json` exists and passes `validate_decision.py` → **OK** (incl. `context`, `expected_move`, `gates.sentiment` fields).

## Final auditor note

The run is **internally consistent and ready for action** — every phase points to the
same conclusion (real but slow accumulation, dealer-caged at $13, negative empirical
edge, headwind macro), and phase-9 correctly translated that into a **watch-only
directional stance with a defined-risk range harvest**, not a bought thesis. No
revision needed; the 46/100 confluence and 0.55 conviction are the honest, matched
read — the single actionable idea is *sell the rich-IV $11–$13 range pre-earnings and
keep the $12.5/$14 call spread as a small Sep-3 catalyst lottery*, invalidated fast on
a close beyond $11.85 or $13.10.
