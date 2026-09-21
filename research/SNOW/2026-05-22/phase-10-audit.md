# Phase 10 — Audit & Confidence Score

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T18:05:00Z
**Dominant bias audited:** RANGE / NEUTRAL (downside-asymmetry tilt), conviction 0.55

## Summary

**Confluence score 46/100 — perfectly-mixed (slightly below 50), which is the correct
signature for a no-directional-edge event setup.** Recommended conviction bin
**0.55–0.65**; phase-9 chose **0.55 → MATCH** (low end, justified by zero directional
edge + two CAUTION gates). The chain is **internally consistent**: nine phases plus
two desk passes independently converge on "size-unusual, direction-neutral, ±13%
binary, defined-risk." **Two contradictions logged** (phase-7 divergence, phase-7b
caution) — both are *downside-caution* signals already absorbed by the downside-tilted,
two-tailed structure, not unresolved conflicts. The one genuine internal tension —
phase-3's capped-bullish 185/200 spread vs the phase-7/7b/7c downside caution — is the
two tails of the event and is explicitly structured for. All 3 spot-checked citations
resolve. `decision.json` validates. **Run is ready for action as a starter-size,
defined-risk event trade.**

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **0** | Net flow −$0.9M, ex-0DTE delta ≈ flat, two-sided sweeps [FLOW:delta_notional DUCKDB] — mixed, no directional edge (BUSY_NAME caps at + anyway). |
| 2 — dark pool | **0** | Balanced/mechanical: large-tier 0.604 vs mega closing SELL; no accumulation or distribution [DP:block_stratified]. |
| 3 — OI | **+** | The lone directional lean: 5/29 185C +5,046 ask-bought, capped by 200C writing = bull call spread [OI:biggest_increases]. |
| 4 — structure | **0** | Long-gamma pin $172.5 (+$23.8M) is directionally neutral pre-event; downside vanna −2,294 noted but pin dominates into the print [STRUCT:gex]. |
| 5 — historical | **0** | VRP +0.303 rich but 71.4% vol-realisation → defined-risk, no directional edge [HIST:vrp][HIST:signal_backtest]. |
| 6 — macro | **0** | TRANSITIONAL regime + weak 38.1% breadth offsets the aligned Tech sector inflow → net neutral [MACRO:MarketRegime_2026-05-22]. |
| 7 — insights | **−** | conviction_matrix MIXED + price_vs_flow DIVERGENCE ("+31.7% price vs bearish flow") — caution against the crowd long [INSIGHT:price_vs_flow]. |
| 7b — fundamentals | **−** | CAUTION: priced for perfection (P/S 12.7, +32% run), 38M insider shares sold / 0 bought — downside asymmetry [FUND:psTTM][FUND:insider_transactions]. |
| 8 — agents | **+ (5/5 align)** | All five returned RANGE/NEUTRAL aligned with the dominant bias → +2×5 = +10. |

**Raw score (symmetric):** 8 phases = (+7 −7 −7) = **−7**; phase-8 = **+10** → **raw = +3**
**Base score:** round((3 + 130) / 260 × 100) = **51 / 100**
**Debate penalty (phase-8b):** **−0** — NOT disconfirmed (bull_residual 0.65 > bear_residual 0.55)
**Sentiment penalty (phase-7c):** **−5** — tier_adjustment = CAUTION (crowded long w/o smart-money confirmation)
**Confluence_score:** 51 − 5 = **46 / 100**
**Context modifier applied:** phase-0.5 `BUSY_NAME_NORMAL_DAY` → phases 1 & 2 capped at `+` (both scored 0, within cap).
**Recommended bin:** 0.55–0.65 (46 → 30–49 band)
**Phase-9 actual bin:** **0.55 → MATCH** (low end; appropriate given no directional edge + two CAUTION gates).

## Contradictions

- **phase-7 (insights): price_vs_flow DIVERGENCE (+31.7% price vs net-bearish flow)** —
  contradicts any *long* read of the rally. *Resolution:* already reflected — bias is
  RANGE with a downside tilt, and the put-debit-spread structure profits on the
  divergence resolving down. Invalidation tightened: a dark-pool flip to accumulation
  (>0.65) or 3 net-bullish premium sessions exits the lean.
- **phase-7b (fundamentals): CAUTION — priced for perfection + insider selling** —
  contradicts chasing the long into the print. *Resolution:* already reflected — sizing
  cut one step for 7b CAUTION, and the structure is defined-risk/starter, not a naked
  long. No further action.
- **Noted tension (not a − score): phase-3 (+) capped-bull spread vs phase-7/7b/7c
  downside caution** — these are the two *tails* of the binary. *Resolution:* the
  two-tailed defined-risk design (put debit spread for the downside, condor/upside
  call-spread alternative) explicitly trades both; the phase-8b debate confirmed neither
  tail can be dismissed (residuals 0.65 vs 0.55). Consistent, not contradictory.

## Citation failures

(none — 3 of phase-9's thesis citations spot-checked, all resolve)

1. **[STRUCT:gex DUCKDB]** ±13.3% expected move → resolves: phase-4-structure.md
   §Summary/§Key signals "5/29 ATM straddle ($23.35) implies ≈ ±13.3%." ✓
2. **[INSIGHT:price_vs_flow]** "+31.7% price vs bearish flow" → resolves:
   phase-7-insights.md §Price vs flow "price up 31.7% … net flow −$902,406." ✓
3. **[FLOW:delta_notional DUCKDB]** earnings-week −$15M → resolves: phase-1-flow.md
   §Aggressor & delta-notional, 2–7DTE signed Δ-notional −0.015bn. ✓

## Sanity checks

- [✓] All `phase-*.md` present incl. phase-0.5, 7b, 7c, 8b (14 phase files + decision.json).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 in citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (165/150 put debit spread) + ≥1 defined-risk (iron condor).
- [✓] Sizing math shown; Kelly `p` = conviction-bin fallback (phase-5 `bullish_flow`
  0.923 backtest explicitly **rejected** — universe-wide, tiny-N, misaligned with RANGE
  bias — a justified fallback per the rubric).
- [✓] All five risk gates evaluated: fundamentals CAUTION (cut), sentiment CAUTION
  (cut), correlation soft-watch (no cut), rotation aligned (no cut), debate
  not-disconfirmed (no cut).
- [✓] Phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected — final size ~1%
  (starter), well below band top.
- [✓] Structures sized to the front-expiry expected move; `expected_move`
  (13.3% / $23.35) in decision.json.
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. `context`,
  `expected_move`, `gates.sentiment` fields); `confluence_score`/`recommended_bin`
  backfilled (46 / 0.55).

## Final auditor note

The run is **internally consistent and ready for action**: every independent
lens — flow, dark pool, OI, dealer structure, history, macro, UW composite, five
agents, and the adversarial debate — converges on the same conclusion, that SNOW into
its 5/27 print is a **size-unusual but direction-neutral, ±13% binary with no
smart-money-confirmed directional edge and an asymmetric downside.** Phase-9's
**starter-size (~1%), defined-risk, two-tailed** blueprint correctly expresses that
(downside put-debit-spread primary, neutral condor alternative), the 0.55 conviction
bin matches the 46 confluence score, and no revision is required — the only honest edge
here is *structure and discipline*, not direction.
