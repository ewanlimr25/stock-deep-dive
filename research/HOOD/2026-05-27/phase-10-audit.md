# Phase 10 — Audit & Confidence Score

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Dominant bias audited:** RANGE (mild distributive / fade-the-pop tilt), conviction 0.55

## Summary

**Confluence score: 48/100** (just below the 50 "perfectly mixed" line) →
**recommended bin 0.55** (30–49 band, lower end given the gate stack). **Phase-9 actual
bin 0.55 — MATCH.** The run is **internally consistent**: the RANGE/no-directional-edge
conclusion is corroborated across phases 1–6, and the one phase that reads bullish on its
face — phase-7's UW composite (signal-confluence 5/6, DIRECTIONAL_LONG, ACCUMULATION) — is
coherently **debunked as artifact** by the DuckDB decompositions in phases 1, 2, and 4
(closing-auction "accumulation", balanced aggressor split). **One contradiction logged**
(phase-7), resolved by tightening invalidation at the 78 reclaim rather than upgrading.
All three spot-checked citations resolve. `decision.json` valid.

## Confluence scorecard

Scored as directional confluence toward the phase-9 RANGE-with-fade tilt (0 = no
directional information / pure mixed; + = supports the capped/fade read; − = pulls the
other way). Phase-0.5 `BUSY_NAME_NORMAL_DAY` caps phases 1–2 at `+`.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **0** | Net flow **+$1.07M** trivial; aggressor split call ask $17.6M ≈ bid $18.9M [FLOW:aggressor_ex0dte DUCKDB] — no directional edge. |
| 2 — dark pool | **+** | Regular-session DP **40.8% above mid** (offered) vs closing-auction 94.8% [DP:session_split DUCKDB] — mild intraday distribution supports the fade (capped at + by context). |
| 3 — OI | **0** | Two-sided premium-selling: 80C +3,396 written, 69–72 puts sold [OI:smart_positioning] — range, no directional build. |
| 4 — structure | **+** | Spot 76.2 below **ZGL 77.85**, +gamma cap 78–80, **vanna selling** on falling IV [STRUCT:gex][STRUCT:vanna_charm] — capped/fade tilt. |
| 5 — historical | **0** | IV 15.6th pctile, **14 bull / 16 bear days, +1.8%** [HIST:trend] — choppy/flat, confirms no-edge. |
| 6 — macro | **+** | Hawkish Fed (hike risk), **CPI +3.78% YoY**, Tech net-dir **−$433M** [MACRO:FOMC_2026-04-29][MACRO:sector_rotation] — headwind supports the defensive/fade lean. |
| 7 — insights | **−** | UW **signal-confluence 5/6** + DIRECTIONAL_LONG nominally contradict the fade [INSIGHT:signal_confluence] — but artifact (see Contradictions). |
| 7b — fundamentals | **0** | fundamental_signal **NEUTRAL** — strong quality (rev +41.5%, op margin 46%) offsets the latest miss + insider selling; tier CAUTION [FUND:operatingMarginTTM]. |
| 8 — agents | **+ (4/4 align, 1 MISSING)** | accumulation-hunter, contrarian, sweep-tracker, risk-monitor all RANGE/NEUTRAL; earnings-scout MISSING (ER >30d) → +2×4. |

**Raw score (symmetric):** phases = 0+7+0+7+0+7−7+0 = **+14**; agents = **+8** → **+22**
**Base score:** round((22 + 130) / 260 × 100) = **58**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.55 vs bear_residual 0.85)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment CAUTION)
**Confluence_score:** 58 − 5 − 5 = **48/100**
**Recommended bin:** **0.55** (30–49 band → 0.55–0.65; lower end given two CAUTION gates + adverse rotation + disconfirmed debate)
**Phase-9 actual bin:** **0.55 — MATCH**

## Contradictions

- **phase-7 (insights):** UW signal-confluence scores HOOD **5/6 bullish** with
  conviction-matrix DIRECTIONAL_LONG and institutional-accumulation ACCUMULATION — a
  direct contradiction of the RANGE/fade bias. **Resolution:** the factors are artifact —
  the "accumulation" is the 16:00 closing auction (phase-2 §Session split), the
  "bullish_flow" is a balanced aggressor split netting +$1.07M (phase-1 §Aggressor split),
  and "oi_building" is two-sided premium-selling (phase-3). Phase-7's own analysis already
  debunks them (conviction-matrix confidence just 17.5%). **Tighten invalidation at the 78
  reclaim** and **wait for genuine *intraday* DP buying** before treating any long as real;
  do not upgrade conviction.
- **Watch (not scored −, but flagged):** the bullish analyst target **$100.70 (+32%)** and
  the real AI-agent-trading / SpaceX-IPO catalyst (phase-6/7c) pull bullish against the
  fade. These are the legitimate bull-case seeds; the fade is invalidated if price holds
  >78 (gamma flip) — that is where the catalyst would be winning.

## Citation failures

None — all three spot-checked thesis citations resolve:
1. `[DP:session_split DUCKDB]` "intraday DP 40.8% above mid vs closing-auction 94.8%" →
   **resolves** in phase-2-dark-pool.md §Session split (40.8% / 94.8% table). ✓
2. `[FLOW:aggressor_ex0dte DUCKDB]` "call ask $17.6M ≈ bid $18.9M, net +$1.07M" →
   **resolves** in phase-1-flow.md §Aggressor split (call ask $17.61M, bid $18.88M). ✓
3. `[STRUCT:gex]` "ZGL 77.85, +gamma wall 80 (+$13.3M)/78 (+$12.2M)" → **resolves** in
   phase-4-structure.md §GEX (ZGL 77.85; 80 +$13.25M; 78 +$12.24M). ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + decision.json.
- [✓] Phase-9 thesis cites ≥3 distinct upstream datapoints (5 in citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (put debit spread 75/70) + ≥1 defined-risk (bear call spread 80/82.5).
- [✓] Sizing math shown; Kelly p_raw 0.909 surfaced then **justifiably discarded** (signal-
  class mismatch — bullish_flow vs RANGE thesis; HOOD absent from the backtest set;
  in-sample) → fallback to conviction bin p=0.55.
- [✓] All five risk gates evaluated: fundamentals CAUTION, sentiment CAUTION (CROWDED_LONG),
  correlation soft-watch (HOOD-AAPL 0.685, no cut), rotation adverse, debate disconfirmed.
- [✓] `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected — no top-of-band sizing; final 0.5%.
- [✓] Structures sized to front-expiry expected move (±3.29%/$2.51 in `expected_move`); the
  N4 check **rejected a tight iron condor** (59% IV one-sigma ≫ condor width) in favor of a
  one-sided call spread.
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. context / expected_move
  / gates.sentiment); confluence_score + recommended_bin backfilled below and re-validated.

## Final auditor note

The run is internally consistent and ready for action **as a watch / defined-risk-only
blueprint** — the central finding (no directional edge; the bullish surface signals are
closing-auction and balanced-flow artifacts) is corroborated by independent DuckDB
decompositions and survived the adversarial debate (long disconfirmed 0.85 vs 0.55). No
revision needed: phase-9's 0.55 conviction sits one notch below the 0.55–0.65 band midpoint,
which the gate stack (two CAUTIONs + adverse rotation + disconfirmed debate + BUSY_NAME
context) fully justifies — the only action is to fade strength into 78–80 in token size, or
simply wait for a *held* break of 78 (long) or 75 (short) to define a real trade.
