# Phase 10 — Audit & Confidence Score

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T14:05:00Z
**Dominant bias audited (phase-9):** RANGE (capped $92–100; long lean only on pullback/breakout)

## Summary

**Confluence score ≈ 58/100** (moderate confluence around the *range* read) →
recommended conviction bin **0.65**; phase-9 set **0.55**, a deliberate 1-bin
conservative down-shift for the phase-8b disconfirmation + negative directional Kelly.
**No hard contradictions of the RANGE thesis** — the only signals scored against it are
mild (the directional-long lean in phases 7/2 vs a pure range). The run is **internally
consistent**: every phase agrees this is a capped, mean-reverting $92–100 range, not a
chase, and the sizing correctly resolves to **0% directional / watch**. All 15 phase
files present; all 5 spot-checked citations resolve; `decision.json` validates.

## Confluence scorecard (scored vs the RANGE bias: "+"=supports a capped range, "−"=argues a breakout)

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | + | Two-sided/MIXED tape (net only +$8.68M, sweep dominant_direction MIXED [FLOW:sweep_persistence]) → no breakout impulse, supports range. |
| 2 — dark pool | 0 | ACCUMULATION (buy/sell 1.7 [DP:block_stratified]) is directional-up but broad/late-cycle and absorbed under the $100 cap → neutral for a range read. |
| 3 — OI | + | $100 call wall (net_oi +98,818 [OI:oi_by_strike]) + $97/$100 covered-call overwrite cap upside = defines the range ceiling. |
| 4 — structure | ++ | LONG GAMMA / POSITIVE GEX +$77.6M, ZGL ~$26 [STRUCT:gex] → "expect mean-reversion, reduced vol" — textbook range confirmation. |
| 5 — historical | 0 | Extended +28%/RSI 65 + edge-negative backtest (28.6% [HIST:signal_backtest]) supports "move done → range," but 30 consecutive OI-build days argue drift → net neutral. |
| 6 — macro | 0 | Regime TRANSITIONAL (breadth 37.1% [MACRO:MarketRegime]) is choppy/neutral; sector tailwind offset by a cautious tape → neutral. |
| 7 — insights | 0 | DIRECTIONAL_LONG but confidence only 14% [INSIGHT:conviction_matrix]; low-conviction directional lean → neutral for range. |
| 7b — fundamentals | 0 | BULLISH quality but tier CAUTION (decel earnings, PE 46.6/PEG 2.48 [FUND:metric]) → capped, neutral for range. |
| 8 — agents | + (3/4 align RANGE) | accumulation-hunter/contrarian/sweep-tracker RANGE (+2 each), risk-monitor LONG (−2); earnings-scout skipped → net +4. |

**Raw score (symmetric):** +7+0+7+15+0+0+0+0 (phases) +4 (agents) = **+33**
**Base score:** round((33+130)/260×100) = **63/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.55 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** −0 (tier_adjustment = CONFIRM)
**Confluence_score:** **58/100**
**Recommended bin:** **0.65** (50–64 band)
**Phase-9 actual bin:** **0.55** — 1 bin below recommended (**conservative, intended**):
phase-9 applied the sizing-rubric phase-8b-disconfirmation down-shift + the negative
directional Kelly (p 0.286 < 0.50). A downward deviation is always permitted; this
slightly double-counts the debate (also in the −5 score penalty) but erring conservative
is acceptable for a downside-gated skill. Not a problematic mismatch.

## Contradictions

No phase scored `-` or `--` against the RANGE bias — there are no hard contradictions of
the dominant thesis. The notable *tensions* (sub-contradictions worth carrying, none
thesis-breaking):
- **phase-2 vs phase-9 (range):** genuine accumulation (buy/sell 1.7) is a directional-up
  signal absorbed under the $100 cap — *resolution: tighten invalidation* — a confirmed
  >$100.53 close ends the range thesis (breakout-long), already in phase-9's aggressive entry.
- **phase-8 internal:** risk-monitor dissents LONG vs the RANGE plurality — *resolution:
  already reconciled* (it is a small-size long inside the same $92–100 band, not a
  breakout call).

## Citation failures

None — 3+ spot-checked and all resolve:
- `[DP:block_stratified]` mega buy_ratio **1.00** → present (phase-2 §Tier breakdown). ✓
- `[STRUCT:gex]` **$100 +$18.17M** gamma wall → present ×6 (phase-4 §GEX). ✓
- `[HIST:signal_backtest]` **28.6% (N=7)** → present (phase-5 §Signal backtest). ✓
- `[OI:oi_by_strike]` **net_oi +98,818** → present (phase-3 §OI walls). ✓
- `[DEBATE]` bull **0.55** / bear **0.65** → present (phase-8b §Verdict). ✓

## Sanity checks

- [✓] All phase files present — 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10.
- [✓] Phase-9 thesis cites ≥3 distinct upstream datapoints (DP, STRUCT, OI, HIST, FUND, DEBATE — 5+).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (95/102 call debit spread) + ≥1 defined-risk (iron condor) structure.
- [✓] Sizing math shown; Kelly p = phase-5 win-rate **0.286** (n=7, backtest, N-capped 0.75) → raw_kelly −1.14 → directional **0%**.
- [✓] All five risk gates evaluated: fundamentals CAUTION (cut), sentiment CONFIRM, correlation none, sector aligned, debate disconfirmed (down-shift+cut). Context GENUINELY_UNUSUAL reflected (no top-of-band).
- [✓] Structures sized to the front-expiry expected move (±4.65%/$4.55; `expected_move` in JSON); call-spread width $7 > expected move; condor short strikes at the expected-move boundary (flagged: a full up-gap breaches the call breakeven → starter-size only).
- [✓] `decision.json` exists, includes `context`/`expected_move`/`gates.sentiment`, and passes `validate_decision.py` (re-validated after backfill below).

## Final auditor note

The run is **internally consistent and ready for action as written** — every phase
converges on a capped, long-gamma $92–100 range with genuine-but-late accumulation, and
phase-9 correctly resolves that to a **watch / defined-risk, 0%-directional** posture
rather than chasing a fresh long at $98 into a four-way $100 ceiling with a 28.6%
backtest. No revision required; the single highest-value monitor is the phase-2 DP
buy/sell ratio and phase-4 GEX sign — a flip in either (distribution, or GEX negative)
is the cleanest invalidation of the range floor.
