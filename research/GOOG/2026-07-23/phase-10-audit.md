# Phase 10 — Audit & Confidence Score

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Dominant bias audited:** LONG (mean-reversion) / RANGE — phase-9

## Summary

**Confluence score: 54/100** (base 59 − 5 for phase-7c CAUTION) → **recommended bin
0.65**. Phase-9 chose **0.55** — one bin **more conservative** than recommended, a
justified downward deviation (see Sanity checks). Two contradicting phases (flow,
macro). The run is **internally consistent**: it correctly identifies a genuinely
mixed, low-confluence setup and sizes a small, defined-risk fade rather than
forcing a directional call. Score 54 ≈ "barely-positive-of-mixed," which is the
honest read of a mean-reversion long whose backbone (structure, fundamentals,
positioning) leans its way while flow and macro lean against it.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | `-` | Net bearish −$49.4M, top-25 prints 100% puts `[FLOW:top_premium_trades]` — the flow the thesis *fades*; directionally contra a long (tempered by heavy two-sided put-writing). |
| 2 — dark pool | `0` | Tiers balanced (mega buy_ratio 0.522) `[DP:block_stratified]` — no accumulation/distribution; genuinely neutral (overhead 341–346 supply is a cap, not a directional contradiction). |
| 3 — OI | `+` | Put ladder substantially *written* + Aug-21 upside calls closing `[OI:smart_positioning]` — no one-way bearish build; mildly supports "the short isn't real." |
| 4 — structure | `++` | Long-gamma (ZGL 187.5 ≪ spot), max-pain 350 above, vanna-squeeze-up `[STRUCT:gex]` `[STRUCT:max_pain]` — the backbone of the mean-reversion thesis. |
| 5 — historical | `+` | P/C z +2.21 BEARISH_EXTREME + 90d flow balanced +$28.8M + PREMIUM_BUYING `[HIST:pc_ratio_zscore]` `[HIST:vrp]` — contrarian/exhaustion reads support the fade (offset by the bearish_flow backtest + downtrend). |
| 6 — macro | `-` | Regime TRANSITIONAL/risk-off "half size," 10y 4.67%, FOMC 07-29 in window `[MACRO:MarketRegime_2026-07-23]` — a bounce headwind (earnings-cleared IV-crush is the offsetting tailwind). |
| 7 — insights | `0` | UW composite MIXED at 2.9% confidence, GOOG <1 on both confluence directions `[INSIGHT:conviction_matrix]` — explicitly neutral (price-vs-flow ALIGNED-bearish noted as a tension). |
| 7b — fundamentals | `+` | fundamental_signal BULLISH; the VETO targets the *rejected short*, so for the LONG it **CONFIRMS** (ROE 50.8%, +24% rev) `[FUND:tier_adjustment]` — not `++` because the capex/FCF overhang caps upside. |
| 8 — agents | `+2` | contrarian LONG (+2); accumulation-hunter RANGE, sweep-tracker NEUTRAL, risk-monitor RANGE (0 each); earnings-scout skipped — **zero SHORT** `[AGENT:phase-8]`. |

**Raw score (symmetric):** −7 +0 +7 +15 +7 −7 +0 +7 +2 = **+24**
**Base score:** round((24 + 130)/260 × 100) = **59/100**
**Debate penalty (phase-8b):** −0 (NOT disconfirmed — bull_residual 0.65 vs bear_residual 0.55)
**Sentiment penalty (phase-7c):** −5 (tier_adjustment = CAUTION)
**Confluence_score:** **54/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **MISMATCH (conservative by one bin)**

Context modifier (phase-0.5): `unusual_verdict = GENUINELY_UNUSUAL` → no cap on
phases 1–2 (the unusualness was *bearish*; the thesis fades it, so no top-of-band size).

## Contradictions

- **phase-1 (flow):** bearish premium + 100%-put top prints contradict the long — the
  thesis explicitly *fades* this flow. **Resolution: tighten invalidation** (daily close
  < 310) and keep size at starter; **wait for confirmation** that `sweep_persistence`
  stays "mixed" (not clean bearish) and that IV begins to crush before adding.
- **phase-6 (macro):** TRANSITIONAL/risk-off regime, rising 10y, FOMC 07-29 inside the
  window contradict a bounce. **Resolution: defend/flatten into FOMC**, keep defined-risk
  structures only, half-size already applied via the phase-7c CAUTION gate.

## Citation failures

None — all three thesis citations spot-checked resolve:
1. `[FUND:capex]` $195–205B + first negative FCF → phase-7b-fundamentals.md §Summary/Cash-flow ✓
2. `[HIST:pc_ratio_zscore]` +2.21 BEARISH_EXTREME (0.71 vs 20d mean 0.46) → phase-5-historical.md §P/C z-score ✓
3. `[STRUCT:max_pain]` 350 (near) / 365 (Aug-21), ~10–15% above spot → phase-4-structure.md §Max pain ✓

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + decision.json
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary)
- ✓ Conviction bin ∈ {0.55,…,0.95} → 0.55
- ✓ ≥1 directional (320/340 call debit spread) + ≥1 defined-risk (310/300 put credit spread)
- ✓ Sizing math shown; Kelly `p` correctly **NOT** taken from the phase-5 backtest (that
  was `bearish_flow`, the opposite direction) → conviction-bin fallback 0.55, capped ≤0.65
- ✓ All five risk gates evaluated (fundamentals CONFIRM-for-long / sentiment CAUTION /
  correlation none / rotation neutral / debate not-disconfirmed); phase-0.5
  `unusual_verdict` reflected (no top-of-band size)
- ✓ Structures sized to front-expiry expected move (1.57% / $4.99 in `expected_move`);
  target ≈1.3× the ~4-week move, FOMC gap does not breach the 300 stop
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. context /
  expected_move / gates.sentiment); confluence_score 54 + recommended_bin 0.65 backfilled
- ⚠ **Bin mismatch (acceptable):** phase-9 actual 0.55 vs recommended 0.65 — a *downward*
  (conservative) deviation, permitted and justified in phase-9's "why this bin" note
  (backtest is the wrong direction; UW confidence 2.9%; debate held only 0.65 vs 0.55).

## Final auditor note

The run is internally consistent and ready for action as a **small, defined-risk,
tactical mean-reversion long** — every phase's signed contribution is honestly
scored, the two contradicting phases (flow, macro) are logged with resolutions, and
phase-9's conservative 0.55 bin (one below the 0.65 the 54 score recommends) is the
right call given the backtest points the opposite way and the trade fights an
ALIGNED-bearish momentum read. No revision required; the only live judgment for the
desk is whether a 54-confluence, ~1.25%-size fade clears the bar to put on at all —
a defensible "small or pass," not a conviction trade.
