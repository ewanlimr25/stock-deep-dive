# Phase 10 — Audit & Confluence Score

**Ticker:** NVDA
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T16:05Z
**Inputs audited:** phase-0 through phase-9 + 7b/7c/8b + decision.json

## Summary

The chain is **internally consistent** — its central feature is a *deliberate,
well-documented tension* (bearish institutional flow vs elite/cheap fundamentals)
that every downstream phase handles explicitly rather than papering over. No hard
contradictions; four soft tensions, all resolved. **Confluence score: 44/100 —
Band D (weak / mixed) → conviction 0.55**, which **matches phase-9 exactly**. The
low score is correct and informative: this is a genuinely conflicted, range-bound
setup, and the blueprint's RANGE / 0.55 / watch-only (0.0% recommended,
defined-risk condor optional ≤1.0%) conclusion is the honest output of that
conflict. Phase-9 sizing correctly reflects every gate (7b VETO, 8b disconfirm,
BUSY_NAME_NORMAL_DAY, TRANSITIONAL regime). decision.json validates `OK`.

## Contradiction matrix

| Phases | Fact A | Fact B | Type | Resolution |
|--------|--------|--------|------|------------|
| 1 vs 2 | Flow net +$17.3M, call-tilted (mildly bullish) [FLOW] | DP mega-tier buy_ratio 0.003, $10.4B sold (distribution) [DP] | **Soft tension** | Aggressor-adjusted flow is near-balanced (+$17.3M) and calls were *written* (phase-3); the institutional *stock* tape is the higher-quality signal → bearish lean, capped by 7b. Reflected in RANGE bias. |
| 1 vs 3 | Big 215-225 call builds look bullish [FLOW] | Same calls inferred *written/sold* (net_ask_bid −17K) [OI] | Soft tension | phase-3 smart-positioning shows the builds are sold (overwriting), consistent with phase-2 distribution. Not a bullish signal. |
| 2/7 vs 7b | DP/UW composite = DIRECTIONAL_SHORT / DISTRIBUTION [DP/INSIGHT] | Fundamentals ELITE → VETO the short [FUND] | Soft tension (by design) | Per rubric: 7b is downside-only; it cannot make NVDA a long but *vetoes the directional short* → forces RANGE/neutral, not SHORT. |
| 6 vs 9 | Tech sector tailwind (persistence 1/1, $11.6B) [MACRO] | Phase-9 not a directional long | Soft tension | The tailwind floors downside (prevents the short) but NVDA lags its sector (15th) and the live tape sells → supports RANGE, not LONG. |
| 0.5 vs 9 | BUSY_NAME_NORMAL_DAY [CTX] | Phase-9 size | Consistency check | **Consistent**: phase-9 recommended 0.0% deployed, directional 0% — context honored. |
| 8b vs 9 | disconfirmed = true (toss-up) [DEBATE] | Phase-9 size/bin | Consistency check | **Consistent**: phase-9 took the 0.55 floor bin and cut to watch-only — disconfirm reflected. |

**No hard contradictions.** All material disagreements are the expected
flow-vs-fundamentals and flow-vs-dark-pool tensions, each explicitly resolved.

## Confluence score breakdown

| Component | Max | Score | Justification |
|-----------|-----|-------|---------------|
| Flow alignment | 20 | **10** | Mixed: net +$17.3M but aggressor-balanced, calls written, intraday fade — internally split. |
| Dark pool confirm | 15 | **0** | DP distribution (buy_ratio 0.003) *contradicts* the mildly-bullish flow direction. |
| OI / positioning | 15 | **7** | Two-sided builds, net slightly bearish (−9,376) — neutral. |
| Dealer / GEX | 10 | **10** | Positive-gamma pin 215-230 *supports* the RANGE thesis. |
| Historical edge | 10 | **5** | bearish_flow backtest win-rate 0.50 (0.5–0.6 band), n=8 small. |
| Macro alignment | 10 | **5** | Sector tailwind (inflow 1/1) vs TRANSITIONAL half-size regime — net neutral. |
| Fundamentals (7b) | 10 | **0** | tier_adjustment = VETO. |
| Agent consensus | 10 | **7** | 4/4 agents agreed NEUTRAL/RANGE (earnings-scout skipped) — 4-of-5 equivalent. |
| **Total** | **100** | **44** | **Band D — weak / mixed** |

## Resolved contradictions

All four soft tensions resolved in-line (matrix above). The governing resolution:
**the live institutional tape (dark-pool distribution + UW DIRECTIONAL_SHORT) is
the strongest directional signal, but the fundamental VETO + sector inflow floor
forbid expressing it as a short — so the chain correctly collapses to RANGE /
neutral with 210 as the binary swing level.** Every phase from 7b onward applied
this consistently.

## Open risks (carried into the blueprint)

1. **The 210 level is a single point of failure.** The entire RANGE thesis hinges
   on 210 holding (positive-gamma) vs breaking (negative-gamma trapdoor → trend
   short). A SPY wobble on a beta-2.23 name resolves this fast.
2. **VRP is FAIR** — the optional iron condor has *no vol edge*; it is a pure
   gamma-pin range bet, not premium harvesting.
3. **Small backtest N (8) and a 50% win-rate** mean the empirical edge is
   effectively nil — the only justified action is watch-only.
4. **Mechanical-print ambiguity:** the $10.4B "distribution" is largely one
   closing-cross block — if index/rebalance rather than informed selling, the
   bearish lean weakens further toward pure neutral.

## Final confluence score + band

**44 / 100 → Band D (weak / mixed) → conviction 0.55.**
**Matches phase-9's 0.55 — no deviation.** This is a low-edge, range-bound,
watch-only setup. The score correctly penalizes the flow/DP contradiction and the
fundamental VETO; it correctly credits the clean positive-gamma structure and the
unanimous agent read. A Band-D run should be **traded small and defined-risk, or
not at all** — exactly what phase-9 prescribes (recommended deployment **0.0% /
watch-only** since three gates fired; iron condor documented as an optional ≤1.0%
defined-risk carry, not a Kelly-sanctioned position).

## decision.json patch confirmation

Set `confluence_score = 44` and `recommended_bin = 0.55` (Band D's conviction bin —
the JSON field is the numeric bin per schema, not the letter band) in
`decision.json`. `final_size_pct = 0.0` (watch-only) since raw Kelly = 0 and three
gates fired (upward deviation forbidden). Validated with
`schemas/validate_decision.py` → **OK**.
