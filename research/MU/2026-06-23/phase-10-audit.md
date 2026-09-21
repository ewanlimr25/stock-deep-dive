# Phase 10 — Audit & Confidence Score

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Dominant bias audited:** NEUTRAL / RANGE (phase-9)

## Summary

The run is **internally consistent and ready for action** — and the action it correctly
prescribes is **near-zero**. Confluence score **38/100** (below the 50 "perfectly mixed"
midpoint), reflecting a genuinely two-sided event with a *slight bearish directional tilt*
(bearish_flow 88.9% backtest, price-vs-flow divergence, semis sold, macro headwind) partially
offset by *strongly bullish fundamentals* (EPS +412%, 100% beat rate) and the dark-pool
mega-tier buy. That maps to the **0.55–0.65 band → recommended bin 0.55**, which **MATCHES**
phase-9's chosen 0.55. Three phases carry a bearish lean (5, 6, 7); none kills the NEUTRAL
thesis — they justify it. All three thesis citations resolve. The disconfirmed debate (0.60 ≤
0.60) and the negative range-Kelly drove phase-9 to a **WATCH-ONLY / 0% sized** posture, which is
the honest call into a binary with no edge. `decision.json` validates `OK`.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|---|---|---|
| 1 — flow | **0** | Net flow only −$145.2M (3.7% of $3.92B directional premium), PCR 1.013 — two-sided, no clean direction [FLOW:insights_deep_dive]. (phase-0.5 GENUINELY_UNUSUAL → no cap applied) |
| 2 — dark pool | **+7** | Mega-tier buy_ratio 0.859 is the lone mild-bullish lean [DP:block_stratified] — but overall institutional-accumulation is NEUTRAL and the $553M block is a post-close print |
| 3 — OI | **0** | Near-term put-heavy (06-26 PCR 2.13) vs LEAP call-heavy (2027-12-17 PCR 0.32) — balanced hedge-now/long-later [OI:term_structure] |
| 4 — structure | **0** | Skew COMPLACENT (put IV 110.9% ≈ call IV 110.4%), short-gamma → directionally symmetric, built for magnitude not a side [STRUCT:term_skew] |
| 5 — historical | **−7** | bearish_flow 88.9% (n=9) vs bullish_flow 0.0% (n=8) + price-vs-flow bearish divergence + −11.9% today → mild bearish tilt [HIST:signal_backtest] |
| 6 — macro | **−7** | Regime TRANSITIONAL, Tech −3.94% today, semis directional outflow −$546.7M → headwind [MACRO:MarketRegime] |
| 7 — insights | **−7** | conviction-matrix MIXED (4.7%) but the one clean signal is the bearish price-vs-flow DIVERGENCE [INSIGHT:price_vs_flow] |
| 7b — fundamentals | **0** | `tier_adjustment=VETO`, **but it vetoes the SHORT** (improving underlying: EPS +412%, PEG 0.287) [FUND:earnings_surprise] — a bullish signal that *removes the short option*, not a thesis-kill. Against a NEUTRAL thesis it neither confirms nor contradicts "no direction." *Scoring note: the rubric's "VETO ⇒ −−" presupposes bearish fundamentals vetoing a long; the sign is inverted here, so the mechanical floor is not applied — scored 0 with the veto called out.* |
| 8 — agents | **+10** (5/5 align) | All five agents return NEUTRAL/RANGE, aligning with phase-9's NEUTRAL bias → +2 each [AGENT:phase-8] |

**Raw score (symmetric):** 0+7+0+0−7−7−7+0 (phases) + 10 (agents) = **−4**
**Base score:** round((−4 + 130) / 260 × 100) = **48/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.60 ≤ bear_residual 0.60)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** 48 − 5 − 5 = **38/100**
**Recommended bin:** **0.55** (band 30–49 → 0.55–0.65; lower end given the disconfirmed debate + bearish tilt)
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-5 (historical):** the bearish_flow 88.9% / bullish_flow 0.0% backtest + price-vs-flow
  bearish divergence give the run a directional-DOWN tilt that the NEUTRAL thesis must respect —
  *resolution:* **tighten invalidation** to the $1000 put-wall break (already in phase-9
  invalidation), and note the bearish lean is the reason the optional bull call spread is
  flagged "optional/small," not a core long.
- **phase-6 (macro):** semis being sold (Tech −3.94%, −$546.7M directional outflow) is a real
  headwind to any long — *resolution:* **wait for confirmation** post-print; the macro is a
  size-down argument already honored by the 0% / watch-only sizing.
- **phase-7 (insights):** the bearish price-vs-flow divergence is the cleanest directional
  signal and it points down — *resolution:* **downgrade conviction** (already at the 0.55 floor)
  and keep direction NEUTRAL; the divergence is offset by the bullish fundamentals (7b) and
  mega-tier DP buy (2), which is precisely why the net call is "no direction."

*Cross-cutting note:* the bullish phases (7b fundamentals, 2 DP mega-buy) and the bearish phases
(5, 6, 7) genuinely offset — that mutual cancellation IS the NEUTRAL thesis. The score of 38
(slightly bearish of 50) faithfully encodes "mixed, with a slight bearish lean the defined-risk
posture neutralizes."

## Citation failures

None — all three thesis spot-checks resolve:
1. `[FLOW:insights_deep_dive]` net flow −$145.2M, PCR 1.013 → **confirmed** in phase-1-flow.md §Whole-tape aggregate. ✓
2. `[STRUCT:gex]` GEX NEGATIVE, ZGL 1495.2 ≫ spot $1053.58 → **confirmed** in phase-4-structure.md §GEX. ✓
3. `[FUND:earnings_surprise]` 100% beat rate (4/4), EPS +412% YoY, PEG 0.287 → **confirmed** in phase-7b-fundamentals.md §Earnings-surprise / §Valuation. ✓

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + decision.json
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (7 listed in §Citations summary)
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- ✓ ≥1 directional (bull call debit spread 1080/1200 07-17) + ≥1 defined-risk (iron condor 905/935P+1170/1200C 06-26)
- ✓ Sizing math shown; Kelly `p` = phase-5 win-rate (p_raw 0.889 → N-capped 0.75; range-structure raw_kelly −0.24 → 0% per the negative-Kelly rule)
- ✓ All five risk gates evaluated: fundamentals VETO(-short), sentiment CAUTION, correlation none, sector-rotation adverse, debate disconfirmed
- ✓ Phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` reflected (no-op on `p`; event-driven → size for the binary = 0%)
- ✓ Structures sized to the front-expiry expected move (condor shorts 935/1170 outside the ±10.91% band $937/$1166); `expected_move` present in JSON (10.91% / $114.7)
- ✓ `decision.json` exists and passes `validate_decision.py` ("OK"); `context`, `expected_move`, `gates.sentiment` fields populated
- ✓ `final_size_pct = 0.0` is consistent with the negative range-Kelly (ceiling 0); no forbidden upward deviation

## Final auditor note

The chain is internally consistent: every phase points to the same conclusion — **a genuine
binary vol event with no directional edge**, where the disciplined posture is to **stand aside
(0% sized)** and, only if forced, express the IV-100 crush through a small defined-risk iron
condor. Phase-9 needs no revision; the one judgment a reviewing PM should ratify is the
WATCH-ONLY sizing — it is the rubric-correct output of a negative range-Kelly plus a
disconfirmed debate, not an omission.
