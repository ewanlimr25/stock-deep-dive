# Phase 10 — Audit & Confidence Score

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Dominant bias audited:** NEUTRAL / RANGE (short-vol, downside tilt) — phase-9

## Summary

**Confluence score: 48 / 100** (mixed, just below midline) → **recommended bin
0.55–0.65**; **phase-9 actual bin 0.55 → MATCH.** The run is **internally
consistent**: every layer independently says the same thing — *there is no directional
edge, only a short-vol edge into a binary, and the downside tail is under-priced.* The
score sits near 50 because the signals are genuinely mixed on direction (the correct
reading of a BUSY_NAME_NORMAL_DAY with NOW absent from both bullish and bearish
signal-confluence), and the two one-sided penalties (debate disconfirmed −5, phase-7c
CAUTION −5) pull it to 48. **No phase strongly contradicts the thesis** (the thesis is
itself "no directional bet"), but the internal tensions (bullish price-vs-flow
divergence; the accumulation tool vs phase-2's closing-cross de-rate) are logged.
Zero fabricated numbers survived — several jq field-name traps were caught and
corrected in-phase. The blueprint is **ready as a WATCH-ONLY / defined-risk
recommendation**; it correctly declines to size a directional trade.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|---|---|---|
| 1 — flow | **0** | Mixed / faintly bullish but **delta-neutral (−$89k)**, "mixed" 5-day persistence — no directional confluence `[FLOW:greek_screener]` (capped at + by BUSY_NAME anyway) |
| 2 — dark pool | **0** | Balanced; mega buy_ratio 1.0 is **closing-cross facilitation**, large tier 0.488 — not accumulation `[DP:block_stratified]` (BUSY_NAME cap moot) |
| 3 — OI | **0** | Distributed, no cliff; biggest build a **put-write (7/24 60P +15,010)** — income tilt, not directional `[OI:smart_positioning]` |
| 4 — structure | **+** | **POSITIVE/long-gamma range + BACKWARDATION + COMPLACENT skew** = a clean short-vol setup supporting the thesis `[STRUCT:gex]` `[STRUCT:iv_term_structure]` |
| 5 — historical | **+** | **VRP +18.9 PREMIUM_SELLING; bullish_flow win 14.3% (n7)** — directly supports "no long edge, short-vol" `[HIST:vrp]` `[HIST:signal_backtest]` |
| 6 — macro | **0** | TRANSITIONAL/CHOPPY "defined-risk, half size" supports the *structure* but is a **headwind**, not directional confluence `[MACRO:MarketRegime_2026-07-17]` |
| 7 — insights | **0** | **COVERED_CALL (22%)**, and NOW **absent from both** bullish & bearish signal-confluence — explicitly mixed `[INSIGHT:conviction_matrix]` |
| 7b — fundamentals | **0** | **CAUTION** (1 contradiction): decelerating beats → miss, but quality intact + insider dip-buying — net neutral `[FUND:earnings_surprise]` |
| 8 — agents | **+6** | 4 NEUTRAL align (+8), 1 SHORT misaligns w/ NEUTRAL bias (−2); avg conviction ≈2.6, **zero bullish** |

**Raw score (symmetric):** phases (0+0+0+7+7+0+0+0 = **+14**) + agents (**+6**) = **+20**
**Base score:** round((20 + 130) / 260 × 100) = **58 / 100**
**One-sided gate penalties:**
- Debate (phase-8b) **disconfirmed** (bull 0.60 vs bear 0.70): **−5**
- Phase-7c `tier_adjustment` = **CAUTION**: **−5**
- Phase-7c VETO: n/a (0)

**Confluence_score: 58 − 5 − 5 = 48 / 100**
**Recommended bin:** 0.55–0.65 (band 30–49) → **0.55** (disconfirmation pins the floor)
**Phase-9 actual bin:** **0.55 → MATCH**

## Contradictions

No phase scored `-` or `--` — the thesis is non-directional, so the mixedness is
correctly captured as `0`s plus the one-sided penalties, not as contradictions. The
internal **tensions** (advisory, already reconciled upstream) are:

- **price-vs-flow DIVERGENCE** (phase-7): price −13.5% vs bullish flow — reconciled as
  *complacent/late flow*, not a reversal signal (bullish_flow backtest 14.3%).
  Resolution: **already reflected** — the thesis does not act on the bullish divergence.
- **institutional-accumulation 2.35 (phase-7) vs phase-2 "balanced"**: reconciled as
  closing-cross-weighted buying → weak accumulation. Resolution: **already reflected**
  in the COVERED_CALL framing.
- **contrarian-scanner SHORT(4) vs NEUTRAL plurality (phase-8)**: not a true conflict —
  the others agree the downside is the dominant risk. Resolution: **carried** into the
  invalidation + key_risks (downgrade cascade) and the put-spread structure.

## Citation failures

Spot-checked 3 of phase-9's thesis citations — **all resolve**:
1. `[HIST:signal_backtest]` bullish_flow **0.143 (n=7, −7.38%)** → phase-5 §Signal
   backtest table ✓
2. `[FLOW:greek_screener]` net delta-notional **−$89k** → phase-1 §IV outliers + Greeks ✓
3. `[INSIGHT:conviction_matrix]` **COVERED_CALL** "DP buying + call selling" → phase-7
   §Conviction matrix ✓

## Sanity checks

- [✓] All `phase-*.md` present (incl. 0.5, 7b, 7c, 8b) + `decision.json`
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 in citations summary)
- [✓] Conviction bin ∈ {0.55…0.95} → **0.55**
- [✓] ≥1 directional (100/90 put debit spread) + ≥1 defined-risk (85/90/115/120 iron
  condor) structure present
- [✓] Sizing math shown; Kelly `p = 0.143` is the **phase-5 win-rate** (not the bin);
  raw_kelly −0.40 → directional skip; final **0.0% watch-only**
- [✓] **All five** gates evaluated: fundamentals CAUTION, sentiment/crowd CAUTION+
  CROWDED_LONG, correlation NOW/PATH 0.798 CLUSTER, rotation neutral, debate
  disconfirmed — each cut applied
- [✓] Phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected (no top-of-band;
  final 0.0%)
- [✓] Structures sized to the front-expiry expected move (±11%); `expected_move` in
  JSON (front_expiry_pct 11.0)
- [✓] `decision.json` exists and **passes `validate_decision.py` (OK)** — incl.
  `context`, `expected_move`, `gates.sentiment`
- [✓] Disclaimer present atop phase-9

## Final auditor note

The run is **internally consistent and ready for action as a watch-only / defined-risk
recommendation** — nine layers, five agents, and an adversarial debate independently
converge that NOW into 7/22 offers **no directional edge, a genuine short-vol edge, and
an under-hedged downside tail**, and phase-9 correctly sizes that to **0% directional /
defined-risk-only**. No revision required; the single most important thing to carry is
that this is an **earnings-binary decision** (have the structure on before the 7/22
close or stand aside) with the **NOW/PATH 0.798 cluster** treated as one position.
