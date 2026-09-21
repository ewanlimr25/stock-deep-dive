# Phase 10 — Audit & Confidence Score

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Audited thesis (phase-9 bias):** RANGE (downside-fatter tail), conviction 0.55, 1-4w

## Summary

**Confluence score: 47 / 100** (just below perfectly-mixed 50) → recommended bin
**0.55**; phase-9 actual bin **0.55 → MATCH.** The run is **internally consistent**: the
signals genuinely cohere around a *defensive / no-directional-edge* read, not a directional
setup, which is exactly what a sub-50 confluence behind a RANGE thesis should look like. **3
contradiction phases** (1, 3, 7b — all the *constructive* lanes), each a mild-not-strong
counter that phase-9 already absorbed by declining to size a long. Both one-sided gates
fired (debate disconfirmed −5, phase-7c CAUTION −5). All three thesis citations resolve;
all sanity checks pass; `decision.json` validates. The blueprint is **ready as written —
its headline recommendation is WATCH-ONLY / starter-only defined-risk**, which is the
honest output of a 47-confluence, p=0.50, four-gate run.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **−** | Fresh near-money call buying is a mild *bullish* lean that cuts against the downside-defensive thesis — but low-conviction, and net-bearish premium is an artifact `[FLOW:unusual_volume]`. |
| 2 — dark pool | **+** | Heaviest 5-day clusters sit OVERHEAD as supply ($367.46, $1.57B) and the mega-buy is hollow (0.764 = 14 trades; whole-book 0.562 NEUTRAL) — supports the range-cap `[DP:price_levels][DP:block_stratified]`. |
| 3 — OI | **−** | Fresh OI is UPSIDE calls $370-410 (7/2 370C +5,216) — the one lane positioning *long*, against the downside lean `[OI:biggest_increases]`. |
| 4 — structure | **0** | Short-gamma is two-sided for a range thesis: max-pain pulls up ($360-365) while the $340 −GEX (−5.79M) accelerates down — genuinely neutral `[STRUCT:gex][STRUCT:max_pain]`. |
| 5 — historical | **+** | Fresh 30-day low, first long→short-gamma flip in 21 sessions, IV rich, backtest 50% — supports defensive/no-edge `[HIST:gex_time_series][HIST:signal_backtest]`. |
| 6 — macro | **+** | HEADWIND: idiosyncratic catalyst cluster (AI-talent exodus, FCF −47%) + hawkish FOMC + Comm Services #1 outflow −$118M `[MACRO:Alphabet_2026-06-22][MACRO:FOMC_2026-06-17]`. |
| 7 — insights | **+** | Composite MIXED at 6.2% confidence, absent both confluence lists — confirms no directional edge `[INSIGHT:conviction_matrix]`. |
| 7b — fundamentals | **−** | fundamental_signal BULLISH (rev +17%, EPS +48%, target $433.76 +24%, relative-strength leader) mildly contradicts a downside lean — but `tier_adjustment CAUTION` mitigates `[FUND:metric][FUND:recom fz]`. |
| 8 — agents | **+ (+10; 5/5 align)** | 0 LONG; 3 NEUTRAL + 1 RANGE + 1 SHORT all align with the non-directional/defensive dominant bias (+2 each) `[AGENT:risk-monitor]`. |

**Raw score (symmetric):** (−7 +7 −7 +0 +7 +7 +7 −7) + (+10) = **+17**
**Base score:** round((17 + 130) / 260 × 100) = **57 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.55 vs
bear_residual 0.75)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION; CROWDED_LONG)
**Context modifier (phase-0.5):** GENUINELY_UNUSUAL → no cap on phases 1–2 (and they
weren't `++` anyway).
**Confluence_score:** 57 − 5 − 5 = **47 / 100**
**Recommended bin:** **0.55** (band 30–49 → 0.55–0.65; the gate stack + p=0.50 favor the
floor)
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-1 (flow):** mild bullish call-heavy lean contradicts the downside-defensive
  tilt — *resolution:* **already absorbed** — the lean is low-conviction and the
  net-bearish premium is a flagged LEAP-roll artifact; phase-9 took RANGE, not a long.
  **Tighten invalidation:** only deploy the downside structure on a confirmed break < $340.
- **phase-3 (OI):** fresh upside call OI $370–410 contradicts the downside lean —
  *resolution:* **wait for confirmation** — that build buys into the $362–371 supply and
  includes covered-writing; require a whole-book DP buy_ratio >0.62 + a two-close reclaim
  of $362 before treating it as a real long signal.
- **phase-7b (fundamentals):** BULLISH quality + $433.76 target + relative-strength
  leadership contradict a downside lean — *resolution:* **do not press a short** — the
  quality is a multi-month floor argument (not a 1-4w edge); CAUTION already cut size, and
  it is the reason the plan is RANGE/defined-risk rather than an outright bearish position.

## Citation failures

None. All three phase-9 thesis citations spot-checked and resolve:
1. `[STRUCT:gex]` total_gex **−3,838,225**, regime FULLY_NEGATIVE, ZGL null →
   phase-4-structure.md §GEX ✓
2. `[HIST:gex_time_series]` first POSITIVE→FULLY_NEGATIVE flip in 21 sessions;
   **$396.99→$348.78** → phase-5-historical.md §GEX time series ✓
3. `[DP:block_stratified]` mega buy_ratio **0.764**; whole-book 0.562 NEUTRAL →
   phase-2-dark-pool.md §Tier breakdown ✓

## Sanity checks

- [✓] All phase files present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, **7b**, **7c**, 8, **8b**, 9,
  10) + `decision.json`.
- [✓] Phase-9 thesis cites ≥3 distinct upstream datapoints (6 cited).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (put debit spread 345/330) + ≥1 defined-risk (iron condor) structure.
- [✓] Sizing math shown; Kelly p = phase-5 **bullish_flow backtest 0.50 (n=8, backtest)**,
  not a bin fallback.
- [✓] All five risk gates evaluated (fundamentals CAUTION, sentiment CAUTION, correlation
  none, rotation adverse, debate disconfirmed); phase-0.5 `GENUINELY_UNUSUAL` reflected
  (no-op, noted not a clean tradeable edge).
- [✓] Structures sized to the front-expiry expected move (±2.63% / $9.18); `expected_move`
  present in `decision.json`; 7/17 expiry deliberately pre-earnings.
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. `context`,
  `expected_move`, `gates.sentiment`/`crowd_state`); `confluence_score` 47 +
  `recommended_bin` 0.55 backfilled and re-validated **OK**.

## Final auditor note

The run is **internally consistent and ready for action exactly as written** — and "as
written" means **WATCH-ONLY by default, starter-only defined-risk if expressed**. A
47-confluence (below mixed-50), a coin-flip empirical win-rate (0.50, n=8), four firing
risk gates, a disconfirmed debate, and a zero-LONG desk all point the same way: this is a
**no-edge, vol-expansion inflection where the correct institutional action is to wait** for
the $340-break or $362-reclaim trigger rather than force a position. Phase-9's bin (0.55)
matches the recommended floor; no revision required.
