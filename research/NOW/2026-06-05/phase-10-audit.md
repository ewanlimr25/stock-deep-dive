# Phase 10 — Audit & Confidence Score

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T14:15:00-04:00
**Dominant bias audited:** RANGE (109.7–120, bearish skew on a confirmed floor break) — from phase-9-trade-plan.md

## Summary

**Confluence score: 58 / 100** (base 68, −5 debate disconfirmation, −5
sentiment CAUTION) → **recommended bin 0.65**; phase-9's actual bin is
**0.55 — a justified one-bin MISMATCH** (the sizing rubric's debate gate
mandates a down-shift, documented in phase-9 §Conviction deviation).
**One scored contradiction** (phase-7b `--`, the fundamental veto), one
internally-mixed phase (6, scored 0). The run is internally consistent:
every gate was evaluated, the directional leg is correctly demoted to
trigger-conditional carry-only, and `decision.json` validates OK after
backfill.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 0.5 — context (modifier) | cap | `BUSY_NAME_NORMAL_DAY` → phases 1–2 capped at `+` (universe pctile total prem 99.0 but self net-dir pctile 10.3 [CTX:self_pctile DUCKDB]) |
| 1 — flow | + (capped) | Two-way, seller-dominated tape: "calls −$15.58M / puts −$17.42M net SOLD ex-0DTE, net delta ≈ −$0.01bn flat" [FLOW:aggressor_ex0dte DUCKDB] — the range signature; bearish persistence ($377.9M 5/5 [FLOW:sweep_persistence]) supplies the bearish skew |
| 2 — dark pool | + (capped) | "tier buy_ratios 0.461/0.477 — balanced sell-lean" [DP:block_stratified]; the $200M overhead shelf at 117.9–120 [DP:price_levels] defines the audited range ceiling |
| 3 — OI | ++ | The wall map IS the blueprint: "120 call wall net +19,858; no put wall until 100 (−11.0%)/90 (−19.9%)" [OI:oi_by_strike]; 6/18 cliff 20.9% of OI [OI:term_structure] — capped above, trapdoor below |
| 4 — structure | ++ | "regime POSITIVE — dealers net long gamma, expect mean-reversion" with ZGL 109.7 and shelves 110/125/130 bracketing the range [STRUCT:gex]; split max-pain magnets 120 (6/12) / 108 (6/18) [STRUCT:max_pain] are two-sided gravity |
| 5 — historical | + | Round-trip 100→136→112 with P/C z +6.093 BEARISH_EXTREME [HIST:pc_ratio_zscore] and RSI 54.5 [HIST:rsi fz] — mean-reversion/extremes support range; the 87.5% (N=8) bearish_flow base rate [HIST:signal_backtest] keeps it `+` not `++` (argues trend-down) |
| 6 — macro | 0 | Internally mixed vs RANGE: regime guidance literally "Iron condors in range. Half position sizes" [MACRO:MarketRegime_2026-06-05] supports it, but VIX 21.51 (+40%) + hike repricing (Dec odds 43% [MACRO:FedWatch]) is range-break fuel — net neutral to the audited bias |
| 7 — insights | + | Composites unanimously balanced: conviction-matrix MIXED 2.1%, accumulation NEUTRAL 0.92, divergence false [INSIGHT:conviction_matrix, INSIGHT:institutional_accumulation] — "no edge in the middle" agrees with edges-only RANGE |
| 7b — fundamentals | **--** (hard rule) | `tier_adjustment = VETO` — **fundamental veto called out**: beat-and-raise (FY26 sub guide ↑ to $15,735–15,775M [FUND:guidance]) + $50B buyback contradict the plan's bearish skew on ≥2 axes; capped at `--` per rubric |
| 8 — agents | +4 (3 of 4 align) | accumulation-hunter NEUTRAL +2, contrarian-scanner RANGE +2, sweep-tracker NEUTRAL +2, risk-monitor SHORT −2 [AGENT:phase-8]; earnings-scout skipped by rule (not MISSING) |

**Raw score (symmetric):** +7 +7 +15 +15 +7 +0 +7 −15 = **+43** (phases) + **+4** (agents) = **+47**
**Base score:** round((47+130)/260×100) = **68 / 100**
**Debate penalty (phase-8b):** −5 — `disconfirmed=true` (bull_residual 0.65 vs bear_residual 0.65) [DEBATE:bear_residual]
**Sentiment penalty (phase-7c):** −5 — `tier_adjustment=CAUTION` (crowd_state CROWDED_LONG, 6σ late-bearish margin) [SENT:verdict]
**Confluence_score:** **58 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55 — MISMATCH, justified**: phase-9 §Conviction deviation documents the sizing-rubric gate-5 down-shift (debate disconfirmation also acts on the bin, not only the score). Internally consistent with both rubrics as written; calibration should watch whether this double application (score −5 *and* bin down-shift) over-penalizes.

## Contradictions

- **phase-7b (fundamentals): `--`** — bullish beat-and-raise + $50B buyback
  + 0 insider sells of conviction vs the plan's bearish skew —
  **resolution applied:** directional leg demoted to trigger-conditional,
  defined-risk, carry-only at ≤0.5% (watch-only standing); invalidation
  tightened with the 135P-OI close-vs-open check. No further action needed;
  do NOT trade the break without the trigger.
- *(color, not scored `-`)* phase-6 is internally split (pro-range guidance
  vs range-break vol regime) — resolution: the plan's "no entries within
  24h of CPI/FOMC" monitoring rule covers it.

## Citation failures

(none — all spot-checks resolve)

- `[STRUCT:gex] ZGL 109.7` → phase-4-structure.md §GEX: "zero_gamma_level 109.7" ✓ (grep: 5 hits)
- `[HIST:pc_ratio_zscore] z +6.093` → phase-5-historical.md: "z = +6.093, extreme = BEARISH_EXTREME" ✓ (3 hits)
- `[DP:price_levels] 119.36 = $148,352,419` → phase-2-dark-pool.md §Price levels ✓ (2 hits)
- `[FLOW:sweep_persistence] $377,864,816` → phase-1-flow.md §Key signals ✓ (2 hits)

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9 + decision.json (ls verified)
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (8 listed in Citations summary)
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- ✓ ≥1 directional (110/100 bear put spread, trigger-conditional) + ≥1 defined-risk (95/100/125/130 iron condor)
- ✓ Kelly p = phase-5 win-rate: p_raw 0.875 → N-cap (n=8<10) → p 0.75; math shown (raw_kelly 0.658, fraction 0.25, cap 5%)
- ✓ All five gates evaluated in the sizing block: 7b VETO (fired), 7c CAUTION (fired), correlation cluster PATH@0.759 (fired), rotation (not fired, reasoned), debate (fired); phase-0.5 `BUSY_NAME_NORMAL_DAY` reflected (no top-of-band)
- ✓ Structures sized to the expected move: derived front-expiry ±10.4%/±$11.65 in `decision.json` (screener 0.38% correctly rejected as unit-suspect, documented in phases 0.5/6/9)
- ✓ `decision.json` exists and `validate_decision.py` prints **OK** after the confluence backfill (score 58, bin 0.65, audit path set); `context`/`expected_move`/`gates.sentiment` fields populated
- ✓ Tool errors surfaced verbatim where they occurred (sweep-persistence `--date` flag, Yahoo 401, Finnhub paid endpoints, MSPR empty, GEX-ts ZGL noise)

## Final auditor note

The run is internally consistent and ready for action as written: a
58-score mixed-confluence RANGE blueprint whose only hard contradiction
(the 7b fundamental veto) is already neutralized by the trigger-conditional,
carry-only treatment of the bearish leg — the discipline holds as long as
nobody shorts before 109.7 actually breaks. The chief calibration watch
items are the N=8 backtest `p` (thin), the unresolved 135P close-vs-open
question (first OI snapshot after as-of resolves it), and whether the
debate's double penalty (−5 score *and* one-bin down-shift) proves too
conservative when marked to market.
