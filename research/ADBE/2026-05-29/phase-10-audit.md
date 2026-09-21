# Phase 10 — Audit & Confidence Score

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T20:24:00Z
**Audits:** phase-0 through phase-9 + decision.json

## Summary

**Confluence score 43 / 100** (mixed, tilting weak-positive before penalties; net
below 50 after the debate + sentiment cuts). Recommended conviction bin **0.55**
(30–49 band) — **MATCHES** phase-9's actual 0.55. The run is **internally consistent
and the blueprint is honest**: it correctly converts an eye-catching bullish-flow
day into a **token / defined-risk-only long** once the isolation of the signal, the
rich pre-earnings vol, the long-gamma pin-down, the coin-flip backtest, and the two
CAUTION gates + disconfirmed debate are weighed. Two phases actively contradict the
dominant LONG bias (OI = call-writing; structure = max-pain pins below spot) and are
logged. The principal degradation is **phase-8: all five desk sub-agents failed on
the agent-runtime session limit (0 tokens)** — phase-8 therefore contributes **0** to
confluence and the desk read is an orchestrator synthesis, not independent agents.
A secondary integrity note: phases 7, 7b, 7c were **corrected within the run** after
fabricated figures (from a pre-flush draft) were caught and replaced with the real
Finnhub/fz data.

## Confluence scorecard

Dominant bias scored against = **LONG** (weak). Context (phase-0.5) =
GENUINELY_UNUSUAL → **no `+` cap** on phases 1–2.

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | net call premium **+$12.27M**, calls 2.3× puts, P/C 0.468 [FLOW:insights_deep_dive] — bullish but isolated (no sweep-persistence, no smart-money row) |
| 2 — dark pool | **+** | mega buy_ratio 0.953 / large 0.639 [DP:block_stratified] — buy-leaning, but ~37% is closing-auction → de-rated, hence + not ++ |
| 3 — OI | **−** | fresh 260C/280C builds **inferred SOLD** (net ask-bid −478) [OI:smart_positioning] — positioning contradicts the long |
| 4 — structure | **−** | long-gamma + **max-pain 245/250 below spot** [STRUCT:max_pain] — chain pins down/range, against an up-breakout |
| 5 — historical | **0** | signal win-rate **0.50 (n=8)** [HIST:signal_backtest] — no edge; 90d tilt only +$96.8M (mild) |
| 6 — macro | **0** | Tech sector ALIGNED +$11.6B [MACRO:sector_flow_persistence UW] offset by CPI +3.78% + TRANSITIONAL regime |
| 7 — insights | **+** | UW composite **DIRECTIONAL_LONG** but confidence **41.3%** on auction-contaminated DP [INSIGHT:conviction_matrix] — weak bullish |
| 7b — fundamentals | **0** | NEUTRAL: cheapest software multiple P/E 15.1/PEG 0.79 [FUND:peer_pe fz] **vs** insider MSPR −40.53 [FUND:mspr_2026-04] → CAUTION, net 0 |
| 8 — agents | **0** | **all 5 sub-agents MISSING (session limit, 0 tokens)** → no independent agent contribution |

**Raw score (symmetric):** +7+7−7−7+0+0+7+0 = **+7** (phase-8 = 0)
**Base score:** round((7 + 130) / 260 × 100) = **53 / 100**
**Sentiment penalty (phase-7c):** −5 (tier_adjustment = CAUTION, adverse revisions)
**Debate penalty (phase-8b):** −5 (disconfirmed = true; bull_res 0.55 vs bear_res 0.65)
**Confluence_score:** 53 − 5 − 5 = **43 / 100**
**Recommended bin:** **0.55** (43 → 30–49 band → 0.55–0.65, low end given disconfirmed + 2 CAUTION gates)
**Phase-9 actual bin:** **0.55** — **MATCH**

## Contradictions

- **phase-3 (OI):** fresh near-money call OI is being **written (sold-to-open), not
  bought** [OI:smart_positioning] — contradicts the bullish-long read.
  *Resolution:* **wait for confirmation** — only upgrade the directional long if a
  later session shows calls being *bought* to open (positive net ask-bid) rather than
  written; until then the put-credit-spread/range expression is correct.
- **phase-4 (structure):** long-gamma regime + **max-pain 245/250 sit below spot**
  [STRUCT:max_pain] — the chain's gravity pulls price down/sideways, against an
  up-breakout through the 260 wall. *Resolution:* **downgrade the directional /
  prefer defined-risk** — phase-9 already does this (token directional, range
  premium-harvest preferred); tighten invalidation to the 238 shelf break.

## Citation failures

None — 3 spot-checked, all resolve:
1. `[FLOW:insights_deep_dive]` net +$12.27M / P/C 0.468 → phase-1 §Whole-tape
   aggregate (call_premium $46.62M, put $20.43M, net_flow +$12,273,462). ✓
2. `[HIST:signal_backtest]` win 0.50 (n=8) → phase-5 §Signal backtest + sizing
   handoff block. ✓
3. `[FUND:peer_pe fz]` P/E 15.1, PEG 0.79 → phase-7b §Valuation (cheapest in the
   software peer table). ✓

## Sanity checks

- [✓] All phase MDs present (phase-0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10)
- [✓] phase-9 cites ≥3 distinct upstream datapoints (6 listed)
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55
- [✓] ≥1 directional (call debit spread 260/280) + ≥1 defined-risk (put credit
  spread 245/235)
- [✓] Sizing math shown; Kelly p = phase-5 win-rate **0.50 (n=8)**, N-capped, not the
  bin
- [✓] All 5 risk gates evaluated: fundamentals **CAUTION**, sentiment **CAUTION**,
  correlation **soft-watch (0.688, no cut)**, sector rotation **aligned**, debate
  **disconfirmed** — four of five cut size to ~0.3%
- [✓] phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` reflected (not sized
  top-of-band; the unusualness is directional, not turnover)
- [✓] Structures sized to expected move; `expected_move` in JSON (front 0.295% /
  $0.77, with the 6/12 earnings-vol caveat)
- [✓] `decision.json` exists and passes `validate_decision.py` → **OK** (incl.
  `context`, `expected_move`, `gates.sentiment`/`crowd_state`); confluence_score 43
  and recommended_bin 0.55 backfilled
- [⚠] **phase-8: all five sub-agents MISSING (agent-runtime session limit, 0 tokens)**
  — phase-8 scored 0; desk read is an orchestrator synthesis, flagged for the
  calibration loop as a degraded (non-independent) input
- [⚠] **Within-run data corrections:** phases 7/7b/7c were rewritten after fabricated
  figures (pre-flush draft) were caught — final files use the real Finnhub/fz output
  (P/E 15.1, PEG 0.79, MSPR Apr −40.53, Recom 2.41, conviction-matrix DIRECTIONAL_LONG
  41.3%, deteriorating analyst revisions). Phase-0.5 and phase-6 also carry logged
  in-run corrections (DuckDB percentile flushed late → verdict upgraded to
  GENUINELY_UNUSUAL; CPI YoY math fixed 5.34%→3.78%).

## Final auditor note

The run is **internally consistent and ready as a research blueprint**: it resists
the obvious trap (treating a 99.6th-percentile bullish-flow day as a green-light
long) and lands on the defensible desk conclusion — **token/defined-risk only, or
wait for the 6/11 print** — with the contradicting phases (OI writing, structural
pin-down) and both quality gates properly cutting size. Two caveats temper
confidence and should be weighed by any reader: phase-8's desk view is an
orchestrator stand-in (sub-agents unavailable), and several mid-run datapoint
corrections were required — both are logged above and neither changes the directional
conclusion, which rests on the (verified) flow, structure, historical, and gate data.
