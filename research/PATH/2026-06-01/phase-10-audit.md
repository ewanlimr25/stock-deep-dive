# Phase 10 — Audit & Confidence Score

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T21:40:00-04:00
**Dominant bias audited:** RANGE (phase-9)

## Summary

**Confluence score 42/100** (mixed, leaning slight-negative on the *directional* axis) →
recommended conviction bin **0.55–0.65**; phase-9's actual bin **0.55** is a **MATCH** (at
the conservative end, correctly driven by the phase-8b disconfirmation and the 7c CAUTION).
The run is **internally consistent**: 14 phase artifacts present, all spot-checked citations
resolve, the sizing applies all five risk gates and the phase-0.5 context, and decision.json
validates. **Two contradictions** logged (phases 4 and 5 vs the directional lean) — both are
already *the reason* the blueprint is a defensive RANGE rather than a long, so they tighten
rather than break the thesis. The key framing note: scored against the *directional* thesis
the confluence is ~42 (no directional edge — which is exactly why the bias is RANGE); the
*structural* support for the range itself (long-gamma, $11/$13/$15 walls, premium-selling
VRP) is strong, so the low directional confluence is a feature, not a flaw, of this plan.

## Confluence scorecard

Scored against the **directional (bullish) lean** that the flow leaned toward and the
debate tested — a near-50 result is the signal that there is *no directional edge*, i.e.
the trade is correctly a RANGE.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **0** | Two-sided: net +$2.18M but the loudest print is a $2.31M bearish ATM put [FLOW:unusual_volume] |
| 2 — dark pool | **+** | Genuine accumulation — large-tier buy_ratio 0.634, +4.6M sh, VWAP $12.89 [DP:block_stratified] (suggestive band, below spot → not ++) |
| 3 — OI | **0** | Collar/range-capped; new builds two-sided (covered-call $14, put-sell $9–10) [OI:smart_positioning] |
| 4 — structure | **−** | Long-gamma mean-reversion + max-pain $11 + negative vanna oppose a directional long [STRUCT:max_pain] |
| 5 — historical | **−** | bullish_flow backtest 44.4% win / −1.25% avg (n=9) + RSI 73.9 overbought [HIST:signal_backtest] |
| 6 — macro | **+** | Technology #1 net-inflow sector, persistence 1, ALIGNED [MACRO:sector_flow_2026-06-01] |
| 7 — insights | **+** | ACCUMULATION + DIRECTIONAL_LONG, but only 26% confidence [INSIGHT:conviction_matrix] |
| 7b — fundamentals | **+** | CONFIRM, 0 contradictions — first GAAP profit, op margin −22%→+6% [FUND:operatingMarginTTM] |
| 8 — agents | **−8 (0/4 directional)** | 2 RANGE + 2 NEUTRAL, 0 LONG/SHORT — desk endorses no directional bet |

**Raw score (symmetric):** phases (0+7+0−7−7+7+7+7 = +14) + agents (−8) = **+6**
**Base score:** round((6 + 130) / 260 × 100) = **52/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.55 < bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION; no VETO)
**Context modifier (phase-0.5):** GENUINELY_UNUSUAL → no cap on phases 1–2 (n/a)
**Confluence_score:** 52 − 5 − 5 = **42/100**
**Recommended bin:** **0.55–0.65** (band 30–49)
**Phase-9 actual bin:** **0.55** → **MATCH** (conservative end, justified by disconfirmation + CAUTION)

> Framing note: had this been scored against the RANGE thesis literally, phases 3/4 (collar
> + long-gamma box) would score ++ and the confluence would read ~65 — i.e. the *range* is
> well-supported. The 42 reflects the *directional* axis, which is the right number to
> validate a 0.55 directional-conviction bin. Both readings agree on the action: a
> well-structured, low-conviction, defined-risk range.

## Contradictions

- **phase-4 (structure):** long-gamma mean-reversion + every near-expiry max-pain $11 +
  negative vanna (post-earnings IV crush → dealer selling) contradict a directional long —
  **resolution: this is the basis for the RANGE bias, not a long;** invalidation already
  set to the $11.70 / $15 range breaks. No change needed.
- **phase-5 (historical):** the `bullish_flow` signal is edge-negative (44.4% win, −1.25%
  avg, n=9) and price is overbought (RSI 73.9, +21% vs 20-day SMA) into the 200-day —
  **resolution: directional conviction downgraded to watch-only/skip** (p<0.50 SHORT-floor
  applied in sizing); the only expression is the defined-risk condor at starter size.

## Citation failures

None. Spot-checked 4 (3 required) from phase-9's thesis/citations — all resolve:
- `[STRUCT:gex]` GEX **POSITIVE +18.1M, $13 pin** → phase-4-structure.md ✓
- `[HIST:signal_backtest]` **win 44.4% (n=9)** → phase-5-historical.md ✓
- `[DP:block_stratified]` **buy_ratio 0.634** → phase-2-dark-pool.md ✓
- `[FUND:operatingMarginTTM]` **op margin −22%→+6% TTM** → phase-7b-fundamentals.md ✓

## Sanity checks

- [✓] All `phase-*.md` present incl. 0.5, 7b, 7c, 8b (14 artifacts + decision.json)
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (7 citations)
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → **0.55**
- [✓] ≥1 directional (call debit spread $13/$15) + ≥1 defined-risk (iron condor 11/12/15/16)
- [✓] Sizing math shown; Kelly **p = phase-5 win-rate 0.444** (n=9, backtest), N-cap applied
- [✓] All five risk gates evaluated: fundamentals CONFIRM · sentiment CAUTION · correlation
  none · rotation aligned · debate disconfirmed; phase-0.5 GENUINELY_UNUSUAL reflected (no-op)
- [✓] Structures sized to the front-expiry expected move (±6.32%); `expected_move` in JSON
- [✓] `decision.json` exists and **passes `validate_decision.py`** (incl. context /
  expected_move / gates.sentiment); confluence_score **42** + recommended_bin **0.55**
  backfilled and re-validated `OK`
- [✓] Disclaimer present at top of phase-9

## Final auditor note

The run is **internally consistent and ready for action as written**: every phase traces to
validated `jq`-parsed data, the lone directional contradictions (phases 4–5) are precisely
what justify the defensive RANGE framing, and the conviction (0.55) and starter size (0.5%)
correctly reflect a setup with real institutional accumulation + a genuine profitability
inflection but **no directional edge** (edge-negative backtest, disconfirmed debate, Street
target ≈ spot). No phase-9 revision required — execute as a small, defined-risk premium-sell
in the $12–$15 box, with the documented flip-long trigger above $15 and flip-down below
$11.70.
