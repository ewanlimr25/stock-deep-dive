# Phase 10 — Audit & Confidence Score

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T20:52:00-04:00
**Dominant bias audited:** LONG (constructive lean, conviction 0.65) — phase-9

## Summary

**Confluence score: 57 / 100** — a **mildly-positive, genuinely-mixed** stack. The
recommended conviction bin from the score band (50–64 → **0.65**) **MATCHES** phase-9's
actual bin (0.65). The run is **internally consistent**: the constructive lean rests on
the accumulation + fundamental + structural lanes (phases 2/3/4/7b all `+`), fought by a
real bearish-flow lane (phase-1 `−`) and a macro headwind (phase-6 `−`), with phase-7
neutral (MIXED/divergence) and the desk split 2-LONG/2-RANGE/1-NEUTRAL (phase-8 net
−2). The phase-8b debate was **not disconfirmed** (bull 0.65 > bear 0.55) and phase-7c
is **CONFIRM**, so **no gate penalties** applied. **2 contradictions** logged (flow,
macro) — both already reflected in phase-9's small, defined-risk, range-aware sizing.
All 3 spot-checked citations resolve. Ready for action **as a low-conviction,
defined-risk constructive lean**, not a sized directional bet.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **−** | Whole-tape net-directional **−$364,914**, calls net sold `[FLOW:insights_deep_dive]` — raw flow leans bearish vs the long (reframed as overwriting, hence not `−−`). Capped at `+` on the agree side by BUSY_NAME, but it's a contradiction here. |
| 2 — dark pool | **+** | Large-tier **buy_ratio 0.651** / composite 1.46 `[DP:block_stratified]` — accumulation; capped at `+` (not `++`) by phase-0.5 BUSY_NAME_NORMAL_DAY. |
| 3 — OI | **+** | Call-writing + put-selling collar + **+45k Mar-27 $19C** around a long `[OI:smart-positioning]` — constructive/range, reframes flow as overwriting. |
| 4 — structure | **+** | **DEX +$51.1M, dealers must BUY underlying** + long-gamma cage `[STRUCT:dex/gex]` — supportive bid (ATM short-gamma pocket tempers to `+`, not `++`). |
| 5 — historical | **+** | Price **+9.9%/30d + OI BUILDING 4 days** `[HIST:trend/oi-trend]` — constructive trend; docked from `++` by rich IV / net-bearish cumulative flow. |
| 6 — macro | **−** | **30y mortgage 6.55% rising + TRANSITIONAL regime + hawkish FOMC tail** `[MACRO:MORTGAGE30US/MarketRegime/FOMC]` — headwind vs the long. |
| 7 — insights | **0** | conviction-matrix **MIXED (9.3%)** + price-vs-flow **DIVERGENCE** `[INSIGHT:conviction-matrix/price-vs-flow]` — genuinely two-sided. |
| 7b — fundamentals | **+** | `fundamental_signal BULLISH` — **4/4 EPS beats, +75% rev growth** `[FUND:earnings_surprise]`; docked from `++` by P/E 171x / thin margins. Not a VETO of the traded (long) thesis. |
| 8 — agents | **−2** | **2/5 align** with LONG (accumulation-hunter, earnings-scout = +2 each); 3 non-aligned RANGE/NEUTRAL = −2 each → net **−2**. Zero SHORT. |

**Raw score (symmetric):** −7 +7 +7 +7 +7 −7 +0 +7 −2 = **+19**
**Base score:** round((19 + 130) / 260 × 100) = **57 / 100**
**Debate penalty (phase-8b):** **−0** (NOT disconfirmed — bull_residual 0.65 > bear_residual 0.55)
**Sentiment penalty (phase-7c):** **−0** (tier_adjustment = CONFIRM, not CAUTION/VETO)
**Confluence_score:** **57 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.65** → **MATCH**

## Contradictions

- **phase-1 (flow):** raw whole-tape flow is net-bearish (−$364,914, calls sold) against
  a long thesis — **resolution: already tightened invalidation** (long dies on two closes
  < $13.50 and on a dark-pool buy_ratio flip < 0.50). The reframe (overwriting, not
  distribution) is supported by phases 3/7b/2 but is an *assumption* — monitor the DP
  buy_ratio daily to confirm it holds.
- **phase-6 (macro):** rising 30y mortgage rate + TRANSITIONAL regime + hawkish FOMC tail
  are a genuine headwind — **resolution: downgrade/size-down already applied** (final
  size 1.5%, defined-risk only; macro-based invalidation = hawkish 07-29 surprise). The
  servicing-book hedge (Mr. Cooper) partially offsets, which is why it's `−` not `−−`.
- *(phase-8 net −2 is the desk's non-commitment to a directional lean, not a distinct
  data contradiction — it is the reason conviction is 0.65, not higher.)*

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[DP:block_stratified]` buy_ratio 0.651 (1,426 trades, $191.2M) → **resolves** in
   phase-2 §Tier breakdown. ✓
2. `[FUND:earnings_surprise]` 4/4 beats, EPS $0.04→$0.15 → **resolves** in phase-7b
   §Earnings-surprise history. ✓
3. `[HIST:trend]` +9.9% over 30 sessions / 18-of-30 bearish-flow days → **resolves** in
   phase-5 §Multi-day trend. ✓

## Sanity checks

- [✓] All `phase-*.md` present incl. phase-0.5, 7b, 7c, 8b (14 artifacts + decision.json).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- [✓] ≥1 directional (call debit spread) + ≥1 defined-risk (put credit spread) structure.
- [✓] Sizing math shown; Kelly `p` = conviction-bin fallback (0.65) — justified: the
      phase-5 `bearish_flow` win-rate (1.00/n=10) is inapplicable to a constructive trade
      and `dark_pool_accumulation` backtest is null (`win_rate_source=null`).
- [✓] All five risk gates evaluated (fundamentals CONFIRM, sentiment CONFIRM, correlation
      none, rotation neutral, debate not-disconfirmed) — none fired.
- [✓] phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected — size held **below**
      the 2.5% half-band ceiling (final 1.5%).
- [✓] Structures sized to expected move (`expected_move.front_expiry_pct 6.6`,
      earnings-tenor ±8–10%); both defined-risk so a single-catalyst gap ≤ max loss (N4).
- [✓] `decision.json` exists, `confluence_score`/`recommended_bin` backfilled (57 / 0.65),
      and `validate_decision.py` prints **OK** (incl. context/expected_move/sentiment fields).

## Final auditor note

The run is **internally consistent and ready for action as a low-conviction (0.65),
defined-risk, constructive-range lean** — the confluence score (57) and both risk-gate
passes independently reproduce phase-9's own conclusion, and the two contradictions
(bearish flow, macro headwind) are already priced into the small size and tight
$13.50 / hawkish-FOMC invalidation. No revision required; the single highest-value
monitor is the **dark-pool large-tier buy_ratio** — if it rolls under 0.50, the whole
"overwriting-not-distribution" reframe (and the long lean) is void before the 07-30 event.
