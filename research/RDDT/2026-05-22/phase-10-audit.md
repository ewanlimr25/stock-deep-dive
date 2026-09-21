# Phase 10 — Audit & Confidence Score

**Ticker:** RDDT
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Dominant bias audited:** NEUTRAL (phase-9), range/two-sided, boundary-traded

## Summary

**Confluence score: 50 / 100 — "perfectly mixed signals."** This is the honest,
internally-consistent result for a dive that resolved to *no tradeable edge*: the
bearish flow is real but negative-edge (30% backtest win-rate), the dark-pool buy and
the bearish flow offset, the fundamentals **VETO** a short, the debate ended in a
**tie (disconfirmed)**, and the desk endorsed **zero clean shorts**. Recommended bin
from the score is **0.65** (band 50–64); phase-9 chose **0.55** — one bin **more
conservative**, which the auditor **endorses** given the negative Kelly edge and the
8b disconfirmation. **One contradiction** logged (phase-6 macro: the Meta-Forum
catalyst is the lone clean directional argument and the range's break-risk). All three
spot-checked phase-9 citations resolve. `decision.json` valid. The run is **internally
consistent and ready** — as a **WATCH with boundary-triggered, starter-size,
defined-risk debit structures**, not as a directional position.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|----------------------------|
| 1 — flow | 0 | Bearish ex-0DTE ($12.19M bull vs $19.54M bear `[FLOW:aggressor_ex0dte]`) but self-undermined by the 5-day BULLISH sweep campaign ($30.3M, 5/5) — directional lean cancels. |
| 2 — dark pool | 0 | Block-tier buy 0.735 `[DP:block_stratified]` *opposes* the bearish flow, but large tier 0.526 / mega empty → the offset is itself the two-sided read. |
| 3 — OI | + | Only 2 contracts >+500, both **calls written**, no put loading `[OI:biggest_increases]` → confirms there is no clean directional conviction to fade. |
| 4 — structure | 0 | FULLY SHORT GAMMA −$11.66M (downside accel) `[STRUCT:gex]` exactly offset by net vanna +961 squeeze coil `[STRUCT:vanna_charm]` → genuinely two-sided. |
| 5 — historical | + | `bearish_flow` win-rate **30%** (n=10) `[HIST:signal_backtest]` + P/C z +2.77 contrarian extreme + MIXED 90d flow → confirms no bear edge. |
| 6 — macro | − | **Meta "Forum"** competitive launch `[MACRO:RDDT_news]` is a genuine clean bearish catalyst — the one real directional argument and the range's downside break-risk. |
| 7 — insights | ++ | Conviction matrix **MIXED**, RDDT **absent** from bearish signal-confluence top-30 `[INSIGHT:signal_confluence]` → textbook confirmation of the neutral thesis. |
| 7b — fundamentals | 0 | `tier_adjustment = VETO` of the bearish flow `[FUND]` (rev +70.6%, EPS +460%, 4/4 beats, PEG 0.095) — **this is a FUNDAMENTAL VETO of the bear signal**; it is *why* phase-9 went neutral, so it neither confirms nor contradicts the NEUTRAL thesis (scored 0, veto noted). |
| 8 — agents | +4 | accumulation NEUTRAL (+2), contrarian LONG (−2, took a side), sweep NEUTRAL (+2), risk RANGE (+2); earnings-scout MISSING. Net aligns with NEUTRAL. |

**Raw score (symmetric, 8 phases + desk):** 0+0+7+0+7−7+15+0 + 4 = **+26**
**Base score:** round((26 + 130) / 260 × 100) = **60 / 100**
**Sentiment penalty (phase-7c CAUTION):** −5
**Debate penalty (phase-8b disconfirmed, bull 0.65 vs bear 0.65):** −5
**Confluence_score:** **50 / 100**
**Recommended bin (band 50–64):** **0.65**
**Phase-9 actual bin:** **0.55** → **MISMATCH (phase-9 one bin more conservative — ENDORSED:** negative Kelly edge + 8b disconfirmation justify the floor; the conviction bin is narrative confidence, and the narrative is "no edge".)
**Context modifier (phase-0.5 GENUINELY_UNUSUAL):** no cap applied to phases 1–2.

## Contradictions

- **phase-6 (macro):** The Meta "Forum" launch + Google AI-Overviews + CEO insider
  selling form a genuine bearish catalyst that could break the range down — the lone
  clean directional argument against a NEUTRAL call. — **Resolution: tighten
  invalidation** (already done: phase-9's `< 140 confirmed close` bear trigger and the
  put-debit-spread carry are gated to fire only on this) **and wait for confirmation**
  (a definitive Forum-adoption / RDDT-DAU headline is the datapoint that resolves the
  bull/bear tie — on the monitoring checklist).

## Citation failures

None — all three spot-checked:
1. `[FLOW:aggressor_ex0dte]` "$12.19M bullish vs $19.54M bearish ex-0DTE" → **resolves**
   (phase-1-flow.md §Aggressor & delta-notional split). ✓
2. `[STRUCT:gex]` "total GEX −$11,655,250, FULLY_NEGATIVE, no zero-gamma flip" →
   **resolves** (phase-4-structure.md §GEX). ✓
3. `[HIST:signal_backtest]` "bearish_flow win_rate 30.0%, n=10" → **resolves**
   (phase-5-historical.md §Signal backtest). ✓

## Sanity checks

- [✓] All `phase-*.md` present incl. phase-0.5, 7b, 7c, 8b (14 files + decision.json).
- [✓] Phase-9 thesis cites ≥3 distinct upstream datapoints (5: FLOW, STRUCT, HIST, FUND, DEBATE).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (put debit spread 140/120) + ≥1 defined-risk (call debit spread 145/160).
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate (0.30, n=10, backtest), N-capped, negative raw Kelly → directional skip; final 0% (watch).
- [✓] All five risk gates evaluated: fundamentals VETO, sentiment CAUTION, correlation none, sector adverse-soft, debate disconfirmed. Context `GENUINELY_UNUSUAL` reflected (no top-of-band; edge is negative).
- [✓] Structures sized to the front-expiry expected move; `expected_move` in JSON (8% weekly IV-derived; screener 0.56% flagged as 1-day).
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. context / expected_move / gates.sentiment fields). confluence_score 50 + recommended_bin 0.65 backfilled.

## Final auditor note

The run is **internally consistent**: every phase points to the same conclusion from a
different angle — a fundamentally-strong, oversold, heavily-shorted name where the
bearish tape is real but negative-edge and vetoed, leaving **no clean directional
trade**. Phase-9 correctly resolved this to **WATCH / boundary-only / starter
defined-risk** rather than forcing a position; the only action item is to let the
$140 / $147–150 boundaries and the Meta-Forum adoption data resolve the tie before
committing risk.
