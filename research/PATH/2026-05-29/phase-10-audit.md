# Phase 10 — Audit & Confidence Score

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Dominant bias audited (phase-9):** RANGE with a slight long lean

## Summary

**Confluence score = 59 / 100** (base 64 − 5 debate penalty) → recommended bin
**0.65**; phase-9 sits one bin lower at **0.55** — an *intentional, rule-driven*
deviation (the phase-8b disconfirmation gate down-shifts the bin, and
`BUSY_NAME_NORMAL_DAY` forbids top-of-band sizing), not an error. The run is
**internally consistent on its data and honestly conservative on its conclusion**:
a low-conviction, defined-risk $11–$13 range skewed slightly long, sized to a
starter 1.25%. **One material data contradiction must be flagged**: UW's
`next_earnings_date = 2026-09-03` was **wrong** — PATH reported on **2026-05-28**,
which phases 0.5/1/6 carried as "no near-term catalyst" before phase-7c caught and
corrected it. The conclusion survives the correction (phase-7c/8/9 re-framed
correctly), but the early-phase framing was contaminated. Contradiction count: **2**
(phase-5 no-edge; the earnings-date error). 3/3 spot-checked citations resolve.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | `+` | Bullish prem $5.31M vs bearish $5.08M, P/C 0.35 — faint bullish, **capped at `+`** (BUSY_NAME_NORMAL_DAY) `[FLOW:insights_deep_dive]` |
| 2 — dark pool | `+` | Block tier **100% buy** (buy_ratio 1.0, $8.96M), pay-up at/above spot — **capped at `+`** (context) `[DP:block-stratified]` |
| 3 — OI | `+` | June-18 $12/$13/$15 call buildup above spot (non-0DTE) `[OI:biggest-increases]` |
| 4 — structure | `0` | Long gamma +$28.6M defines the *range* — supportive floor but $12 wall caps the upside; net neutral to a long lean `[STRUCT:gex]` |
| 5 — historical | `-` | bullish_flow win rate **0.50, n=8 (no edge)**; 90d flow balanced; price extended above 20/50 SMA `[HIST:signal-backtest]` |
| 6 — macro | `0` | Sector tailwind (Tech persistence 1/1) offset by TRANSITIONAL "half-size" regime + weak breadth `[MACRO:MarketRegime]` |
| 7 — insights | `+` | Composites split — confluence 5/6 bullish but conviction-matrix MIXED 6.7%; net weak-bullish `[INSIGHT:signal-confluence]` |
| 7b — fundamentals | `+` | **CONFIRM** — fwd PE 13.1, ROE 15.3%, net cash, only profitable name vs peers; 0 contradictions `[FUND:peer_pe fz]` |
| 8 — agents | `+` (+8) | 3 RANGE + 1 LONG align with bias (+2 each), sweep-tracker NEUTRAL (0); none SHORT |

**Raw score (symmetric):** 28 (phases 1–7b) + 8 (phase-8) = **+36**
**Base score:** round((36 + 130) / 260 × 100) = **64 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.60 vs
bear_residual 0.62)
**Sentiment penalty (phase-7c):** −0 (tier_adjustment = CONFIRM)
**Confluence_score:** **59 / 100**
**Recommended bin (50–64 band):** **0.65**
**Phase-9 actual bin:** **0.55** — **MISMATCH (intentional)**: the phase-8b
disconfirmation gate down-shifts the bin one step (0.65→0.55) per
`rubrics/sizing-rubric.md` §Risk gates; `BUSY_NAME_NORMAL_DAY` also bars
top-of-band sizing. The deviation is *downward* and rule-driven — permitted.

## Contradictions

- **phase-5 (historical):** the firing bullish_flow signal has **no historical
  edge** (50% win rate, n=8) and 90d premium flow is balanced, contradicting the
  constructive flow/DP lean. — *Resolution applied:* conviction held to the bottom
  of the band (0.55) and size cut to starter; Kelly `p` honestly set to 0.50, not
  the narrative bin.
- **phase-0/0.5/1/6 vs phase-7c (earnings-date error):** UW
  `next_earnings_date = 2026-09-03` is **incorrect** — PATH reported Q1 FY2027 on
  **2026-05-28**, so the 5/29 tape is the *post-earnings* day, not a quiet
  pre-catalyst session. Phases 0.5/1/6 framed it as "no near-term catalyst."
  — *Resolution applied:* phase-7c caught it via the news pull and re-framed the
  thesis (post-earnings guidance-raise recovery); phases 8/9 inherited the
  correction. **Calibration note:** the early phases should not trust UW's
  `next_earnings_date` blindly — cross-check against a news/fundamentals pull
  earlier (candidate patch: move a Finnhub `company-news` earnings-date check into
  phase-0 intake).

## Citation failures

(none — all 3 spot-checked citations resolved)
- `[DP:block-stratified]` "block tier 100% buy, $8.96M" → **resolves**,
  phase-2-dark-pool.md §Tier breakdown ✓
- `[STRUCT:gex]` "+$28.6M GEX, $12 wall +$11.4M, $11 pivot" → **resolves**,
  phase-4-structure.md §GEX ✓
- `[FUND:peer_pe fz]` "fwd PE 13.1, only profitable name vs FROG/GTLB/S/ZS" →
  **resolves**, phase-7b-fundamentals.md §Valuation ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + decision.json
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary)
- [✓] Conviction bin ∈ {0.55…0.95} → 0.55
- [✓] ≥1 directional ($12/$14 call debit spread) + ≥1 defined-risk (iron condor)
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate 0.50 (capped), not the bin
- [✓] All five risk gates evaluated (fundamentals CONFIRM / sentiment CONFIRM /
  correlation none / rotation aligned / debate disconfirmed→cut); phase-0.5
  `BUSY_NAME_NORMAL_DAY` reflected (starter size, no top-of-band)
- [✓] Structures sized to expected move; `expected_move` (1.63%/$0.19) in JSON;
  iron-condor breakevens ($10.53/$13.47) bracket the priced ~20d ±$0.85 range
- [✓] `decision.json` exists and **passes `validate_decision.py`** (incl.
  `context` / `expected_move` / `gates.sentiment`); confluence_score 59 +
  recommended_bin 0.65 backfilled

## Final auditor note

The run is **internally consistent and ready for action as a low-conviction,
defined-risk range** — every phase's data cross-checks, the sizing honestly
reflects a no-edge backtest and a disconfirmed debate, and the trade structures
match the desk-and-debate consensus ($11–$13 box, sell the wall / own the cheap
squeeze tail). The single blemish is **upstream, not in the conclusion**: UW's
stale earnings date contaminated the early-phase "no catalyst" framing before
phase-7c corrected it — the blueprint stands, but the calibration loop should add
an earlier earnings-date cross-check.
