# Phase 10 — Audit & Confidence Score

**Ticker:** PATH
**As-of date:** 2026-08-12
**Generated:** 2026-08-13T04:15:00Z
**Upstream phases cited:** phase-0 through phase-9

## Summary

Confluence score: **59/100** → recommended bin **0.65**. Phase-9's actual
bin is **0.55** — a documented **MISMATCH**, but a justified one: phase-9's
own "Conviction deviation" note explains that the sizing rubric's separate
debate-disconfirmation rule (down-shift the bin by one, independent of the
confluence-score penalty already applied) drove the further step down from
0.65 to 0.55. This audit confirms that deviation is correctly sourced and
not an unexplained drift. **1 contradiction logged** (phase-7b, hard-capped
at `--` per the VETO rule). **1 minor citation-attribution note** (not a
hard failure). All sanity checks pass. **The run is internally consistent
and ready for action as a defined-risk, range-bound plan** — not ready for
any directional conviction beyond what phase-9 already gated to zero.

## Confluence scorecard

Dominant bias scored against: **RANGE** (phase-9's actual bias).

| Phase | Score | Justification (quote a datapoint) |
|---|---|---|
| 1 — flow | **+** (capped from `++` by `BUSY_NAME_NORMAL_DAY`) | Whole-tape net_flow ≈ −$44,378 on $3.33M gross, dominant LEAP chain tagged `dominant_direction="mixed"` — about as clean a range-supporting (non-directional) read as the tape offers [FLOW:sweep_persistence] |
| 2 — dark pool | **0** | `large`-tier `buy_ratio=0.678` is a real but "suggestive" mild bullish lean — not strong enough to score as range-confirming or range-contradicting on its own [DP:block_stratified] |
| 3 — OI | **+** | Today's actual OI change was a broad call unwind (−4,048 vs −982 puts) and `biggest-increases` was a net wash (2 bullish/2 bearish) — de-risking, consistent with a range/consolidation read, not fresh directional conviction [OI:decrease_with_volume] |
| 4 — structure | **++** | Dealer regime `POSITIVE` (long gamma), zero regime flips — this IS the mechanical basis for range-bound/mean-reverting price action [STRUCT:gex] |
| 5 — historical | **+** | "Today is a pause, not a fresh entry signal" (phase-5's own verdict) — smallest OI-build day of the 29-day streak, VRP `PREMIUM_SELLING` favors range/credit strategies over chasing either direction [HIST:vrp] |
| 6 — macro | **++** | `market-regime` trading guidance explicitly reads "Iron condors in range" — the most direct endorsement of a RANGE thesis any tool in this dive produces [MACRO:MarketRegime_2026-08-12] |
| 7 — insights | **+** | `price-vs-flow` DIVERGENCE flags reversal-risk against chasing the rally; `conviction-matrix=COVERED_CALL` explicitly reads "capping upside" — both range-supporting, tempered by the (artifact-affected) `institutional-accumulation=ACCUMULATION` directional lean [INSIGHT:price_vs_flow] |
| 7b — fundamentals | **−−** (hard-capped, VETO) | `tier_adjustment=VETO`, `contradiction_count=2` (earnings-trend miss + insider MSPR at the −100 floor) — **this is a fundamental veto and is called out as such**, not merely a mild contradiction [FUND:insider_MSPR] |

**Raw score (symmetric, phases 1–7b):** 7+0+7+15+7+15+7−15 = **43**

**Phase 8 (agent desk, ±2 each vs. RANGE bias):** 4 agents (accumulation-
hunter, sweep-tracker, earnings-scout, risk-monitor) verdict `NEUTRAL` →
aligned with RANGE, +2 each = +8. 1 agent (contrarian-scanner) verdict
`SHORT` → literal bias-field mismatch with RANGE, −2 (even though its
target level $13.89–$13.93 sits *inside* phase-9's own support band and its
invalidation at $16.50 matches phase-9's condor short strike almost exactly —
scored strictly on the stated bias field, per the rubric's literal ±2 rule,
not partial credit for directional compatibility). **Phase-8 raw: +8−2 = +6**

**Raw score (total):** 43 + 6 = **49**
**Base score:** round((49+130)/260×100) = round(68.85) = **69**
**Debate penalty (phase-8b):** −5 (`disconfirmed=true`; bull_residual 0.65
vs. bear_residual 0.75)
**Sentiment penalty (phase-7c):** −5 (`tier_adjustment=CAUTION`)
**Confluence_score:** 69 − 5 − 5 = **59/100**
**Recommended bin:** 0.65 (50–64 band)
**Phase-9 actual bin:** 0.55 — **MISMATCH, but documented and justified**
(phase-9's "Conviction deviation" section cites the sizing rubric's
independent debate-disconfirmation down-shift rule, applied on top of, not
instead of, the confluence-score penalty already reflected above).

## Contradictions

- **phase-7b (fundamentals):** Directional flow bias (mildly bullish across
  phases 2/4/5) is contradicted by 2 of 3 fundamental axes — most recent
  quarter missed EPS by −7.86% (breaking a beat streak) and insider MSPR sat
  at the −100 floor in the freshest available month, both landing directly
  ahead of the 2026-09-03 print [FUND:earnings_surprise][FUND:insider_MSPR].
  **Resolution: phase-9 already applied the maximal response** — the
  directional structure is sized to 0%/watch-only per the VETO gate, and
  only a pre-earnings, earnings-avoiding defined-risk structure carries any
  size. No further tightening needed; the gate did its job.

No other phase scored `-` or `--`.

## Citation failures

5 of 6 spot-checked citations resolve cleanly:

1. `[HIST:oi_trend]` "29 of 30 sessions net OI-building" → confirmed in
   phase-5-historical.md (`consecutive_build_days=29`,
   `total_net_oi_change=+318,061`). ✓
2. `[FUND:insider_MSPR]` "−100 (max bearish) in July 2026" → confirmed in
   phase-7b-fundamentals.md's MSPR table (`2026-07 | −100`). ✓
3. `[MACRO:MarketRegime_2026-08-12]` "TRANSITIONAL... iron condors in
   range" → confirmed verbatim in phase-6-macro.md. ✓
4. `[DEBATE:bear_residual]` "0.75 ≥ 0.65" → confirmed in phase-8b-debate.md's
   disconfirmation verdict block. ✓
5. `[INSIGHT:price_vs_flow]` "DIVERGENCE: Price is up 32.1%..." → confirmed
   verbatim in phase-7-insights.md. ✓

**One minor attribution note (not a hard failure):** phase-9's thesis
sentence tags "…inside an unbroken long-gamma dealer regime" as
`[STRUCT:gex]`, but the specific "unbroken / zero regime flips across 30
sessions" sub-claim is actually sourced from phase-5's `gex-time-series`
(`[HIST:gex_time_series]`), not phase-4's single-day `gex` read
(`[STRUCT:gex]` only establishes *today's* regime is `POSITIVE`). The
underlying fact is true and does resolve — just to a different phase than
the tag names — which brushes against citation-conventions.md's "don't
aggregate multiple sources into a single tag" rule. **Recommendation:**
phase-9 should split this into `[STRUCT:gex][HIST:gex_time_series]` on any
future revision. Not severe enough to invalidate the thesis or trigger a
`## Citation failures`-level block on its own.

## Sanity checks

- [x] All `phase-*.md` files present, including `phase-0.5`, `phase-7b`,
      `phase-7c`, and `phase-8b` (confirmed via directory listing — 15
      files, all expected phases present)
- [x] Phase-9 cites ≥3 distinct upstream datapoints (6 listed in its
      Citations summary)
- [x] Conviction bin is one of {0.55, 0.65, 0.75, 0.85, 0.95} — **0.55**
- [x] ≥1 directional (put debit spread, 0% sized/watch-only) + ≥1
      defined-risk (iron condor, 1.0% sized) structure present
- [x] Sizing math shown explicitly; Kelly `p` is the conviction-bin
      fallback (justified — phase-5's `win_rate_source=null`, 0 historical
      `dark_pool_accumulation` firings), correctly capped at ≤0.65 and then
      further reduced to 0.55 by the debate gate
- [x] All five risk gates evaluated in phase-9's sizing block:
      fundamentals (`VETO`), sentiment (`CAUTION`), correlation (`none`),
      sector rotation (`neutral`), debate (`disconfirmed`)
- [x] Phase-0.5 `unusual_verdict=BUSY_NAME_NORMAL_DAY` explicitly reflected
      in phase-9's sizing context check
- [x] Structures sized with reference to the front-expiry expected move
      (±3.29%/±$0.50, `expected_move` present in `decision.json`) and an
      explicit 1-sigma-vs-strike-distance sanity note in the trade plan
- [x] `decision.json` exists and passes `validate_decision.py`

## 5b. Backfill + validate `decision.json`

Backfilling `confluence_score=59` and `recommended_bin=0.65` (leaving
phase-9's actual `conviction=0.55` untouched — that field records what the
plan actually used, not the recommendation).

## Final auditor note

The run is internally consistent: every phase's individual verdict is
correctly carried into phase-8's desk vote, phase-8b's debate, and phase-9's
sizing, with no upstream contradiction left unresolved — the one phase that
scored `--` (7b's fundamental veto) already drove the maximal, correct
response (directional size to zero) rather than being noted and ignored.
**Ready for action as published: a defined-risk, pre-earnings iron condor at
1.0% size, with the directional put spread retained for reference only and
explicitly not to be taken until the fundamental veto clears** (realistically,
not before the 2026-09-03 print resolves one way or the other).
