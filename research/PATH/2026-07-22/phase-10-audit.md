# Phase 10 — Audit & Confidence Score

**Ticker:** PATH · **As-of:** 2026-07-22 · **Spot:** $10.53 · **Generated:** 2026-07-22
**Dominant bias audited:** NEUTRAL / RANGE (phase-9)

## Summary

**Confluence score: 49/100 — "perfectly mixed," which is exactly the honest read for a
no-directional-edge, trade-the-range call.** Recommended conviction bin **0.55–0.65**;
phase-9 chose **0.55** → **MATCH** (correctly at the conservative end, given the double
veto and the phase-8b disconfirmation). One phase scored net-negative (7b, the
fundamental long-veto). All three thesis citations resolve. The run is **internally
consistent**: every layer independently arrived at "impaired name, crowded both ways,
long-gamma range, no clean directional trade," and phase-9 faithfully translated that
into a defined-risk/flat posture with `final_size_pct = 0.0`.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | + | Genuinely two-sided: net-bearish today (net −$1.60M `[FLOW:insights_deep_dive]`) vs a 5-day bullish sweep campaign — supports the range/no-edge read. |
| 2 — dark pool | + | Balanced tape (large-tier 57.2% buy) but $16M block SELL and spot below the $11.90–12.50 supply `[DP:price_levels]` — mixed, upside-capped. |
| 3 — OI | 0 | Standing bullish LEAP base (Jan-27 41.2% OI) but trivial marginal builds, no pin/rolls `[OI:term_structure]` — nets neutral. |
| 4 — structure | + | POSITIVE gamma / range-bound (ZGL $6.92) with max-pain pin $11–11.5 `[STRUCT:gex]` `[STRUCT:max_pain]` — the core support for a RANGE thesis (kept at `+`, not `++`, because the DEX bid is event-contingent per vanna). |
| 5 — historical | + | Round-trip-flat 30d, VRP +0.18 premium-selling, bearish-flow base rate 10% (n=10) `[HIST:signal_backtest]` — a mean-reverting, range-favoring tape. |
| 6 — macro | 0 | Name-specific OpenAI headwind fully absorbed into the plan; sector tailwind bypasses PATH `[MACRO:SectorFlowPersistence]` — net neutral-to-adverse, not a directional confluence add. |
| 7 — insights | + | UW composite MIXED (3.7% conf), PATH absent both confluence lists, no reversal divergence `[INSIGHT:price_vs_flow]` — directly ratifies no-edge. |
| 7b — fundamentals | − | **FUNDAMENTAL VETO (long):** decent business but sustained insider selling (MSPR ≈ −100, −9.6M sh Mar-26 `[FUND:MSPR]`) + recent EPS miss lean bearish — capped at `−` (not `−−`) because underlying quality is intact; the veto is behavioral, not deterioration. |
| 8 — agents | + (4/4 align) | All four desk agents NEUTRAL/RANGE, avg conviction 2.0 `[AGENT:risk-monitor]` → +8 (each +2; earnings-scout skipped, not counted). |

**Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no cap on phases 1–2.

**Raw score (symmetric):** 7 + 7 + 0 + 7 + 7 + 0 + 7 − 7 + 8 = **+36**
**Base score:** round((36 + 130) / 260 × 100) = **64/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.65 = bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−10** (tier_adjustment VETO issued on a fresh directional short)
**Confluence score:** 64 − 5 − 10 = **49/100**
**Recommended bin:** **0.55–0.65** (49 sits at the top of the 30–49 band)
**Phase-9 actual bin:** **0.55** — **MATCH** (conservative end; also defensible as a permitted downward deviation even under the milder 7c-CAUTION reading that would score 54 → 0.65).

## Contradictions

- **phase-7b (fundamentals):** the fundamental picture leans bearish (sustained insider
  distribution + a recent EPS miss into the OpenAI de-rate) and **vetoes any
  bounce-as-accumulation long**, contradicting the bullish half of the mixed flow —
  **resolution: already honored** (phase-9 takes no long; `final_size_pct = 0.0`,
  directional watch-only). Maintain the defined-risk/flat posture; the veto is precisely
  why the plan is neutral rather than a dip-buy. No further downgrade needed.

## Citation failures

None — all three thesis spot-checks resolved:
1. `[MACRO:OpenAI_Presence]` → phase-6 confirms the 2026-07-22 OpenAI "Presence" launch drove the −13%. ✓
2. `[FUND:MSPR]` → phase-7b MSPR table shows ≈ −100 most months, −9.6M-share reduction Mar-2026. ✓
3. `[SENT:short_float]` → phase-7c records ~13–32% of float short, DTC 2.6–4.3. ✓

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10 + decision.json.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ ≥1 directional (bear put spread 10/9) + ≥1 defined-risk (iron condor 8.5/9.5p + 12/13c).
- ✓ Sizing math shown; Kelly `p` = phase-5 win-rate (bearish_flow 0.10, n=10, backtest), N-cap applied, raw_kelly −0.38 → 0% directional.
- ✓ All five risk gates evaluated in phase-9: fundamentals (VETO), sentiment/crowd (VETO/CROWDED_SHORT), correlation (none), rotation (adverse), debate (disconfirmed=true).
- ✓ Phase-0.5 `unusual_verdict` (GENUINELY_UNUSUAL) reflected in sizing (no-op, edge in `p`).
- ✓ Structures sized to the front-expiry expected move (±4.70%/$0.50); `expected_move` in JSON; 1× gap stays inside condor short strikes.
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. `context`, `expected_move`, `gates.sentiment`); confluence_score 49 + recommended_bin 0.55 backfilled.

## Final auditor note

The run is **internally consistent and ready for action as written** — a disciplined
"no-trade / defined-risk range carry" blueprint on a name that every layer (flow,
structure, fundamentals, positioning, desk, debate) independently reads as impaired and
two-sided. No phase-9 revision is required; the single negative axis (7b) is the
fundamental veto that the plan already respects, and the 49 score correctly places this
at the floor of the conviction range.
