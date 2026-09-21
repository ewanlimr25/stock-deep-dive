# Phase 10 — Audit & Confidence Score

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Dominant bias audited:** RANGE (phase-9)

## Summary

**Confluence score 76 / 100** (strong positive confluence on the **RANGE**
classification — every signal phase confirms a capped, gamma-pinned range; none
contradicts it). Recommended conviction bin from the band: **0.75**. Phase-9 chose
**0.65** — an **intentional, documented one-bin-down** deviation (thin tradeable edge:
BUSY_NAME_NORMAL_DAY + IV at the 4.17th pctile + 7c CAUTION). **Contradiction count: 0.**
All three spot-checked citations resolve. The run is **internally consistent and ready
for action** as a small, defined-risk range trade.

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|-------|-------|--------------------------------------|
| 1 — flow | **+** | Net_flow −$1.61M (call *selling*), capped-upside, no put buying — confirms range `[FLOW:insights_deep_dive]`. *Capped at `+` by 0.5 BUSY_NAME_NORMAL_DAY.* |
| 2 — dark pool | **+** | Mild accumulation 56.8% buy = buy-write (range structure), outside top-30 DP `[DP:block-stratified]`. *Capped at `+` by context.* |
| 3 — OI | **++** | Call walls $14.5/$15/$16 cap upside AND the $14.5C selling built only +514 OI (no standing directional bet) `[OI:biggest-increases]`. |
| 4 — structure | **++** | LONG-GAMMA pin (ZGL $5.26), peak gamma +$36.4M at $14.5, max-pain $14, contango/normal skew/flat front-IV `[STRUCT:gex]`. |
| 5 — historical | **+** | 30d zero GEX regime flips (stable long-gamma) + VRP +6.3% premium-selling; offset by IV at 4.17 pctile (thin seller cushion) `[HIST:gex-time-series]`. |
| 6 — macro | **+** | Hawkish FOMC + sub-MA BTC + regime guidance "iron condors in range" all cap upside; BTC catalyst is the two-sided wildcard `[MACRO:MarketRegime]`. |
| 7 — insights | **+** | MIXED/NEUTRAL composite — MARA in neither signal-confluence list, conviction-matrix MIXED — which *is* range confirmation `[INSIGHT:conviction-matrix]`. |
| 7b — fundamentals | **+** | CONFIRM: 3 straight misses, ROE −52%, MSPR −100, peer laggard — weak business reinforces the cap (would VETO a long) `[FUND:earnings_surprise]`. |
| 8 — agents | **+ (4/4 align, +8)** | All four non-MISSING agents returned RANGE; earnings-scout MISSING (earnings >30d) `[AGENT:desk]`. |

**Raw score (symmetric):** (7+7+15+15+7+7+7+7) + 8 = **80**
**Base score:** round((80 + 130) / 260 × 100) = **81 / 100**
**Debate penalty (phase-8b):** −0 (NOT disconfirmed — bull_residual 0.75 > bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Sentiment VETO penalty:** −0 (not VETO)
**Confluence_score:** 81 − 5 = **76 / 100**
**Recommended bin:** **0.75** (band 65–79)
**Phase-9 actual bin:** **0.65** → **MISMATCH (intentional, documented down-deviation — conservative)**

## Contradictions

**None.** No signal phase scored `-` or `--` against the RANGE bias. The two genuine
*tensions* are risk caveats, not contradictions, and are already carried in phase-9:
- **IV at the 4.17th percentile** (phase-5) — cheap vol is a poor *level* to sell, though
  VRP +6.3% gives positive carry. → Already reflected in the **small 1.5% size** and the
  mandatory defined-risk (long wing) structures.
- **26.5% short float + Street Buy $17.70** (phase-7c) — squeeze fuel / bull cross-source
  against the bearish lean. → Captured by the **7c CAUTION gate (−5, size halved)** and the
  phase-8b strongest-bear-point carried into invalidation (close > $15 / BTC reclaims $65.2k).

## Citation failures

**None.** Spot-checked 3 of phase-9's thesis citations:
1. `[STRUCT:gex]` peak net_gex **+$36.4M at $14.5** / ZGL **$5.26** → **resolves** in
   phase-4-structure.md §GEX (per-strike table + regime block). ✓
2. `[OI:biggest-increases]` $14.5C 6/26 OI **+514** vs **63,005** volume → **resolves**
   in phase-3-positioning.md §Largest OI increases + DATA NOTE. ✓
3. `[MACRO:FOMC]` hawkish 6/17, 2026 dot **3.4%→3.8%** / `[MACRO:BTC]` BTC below
   **50d $65.7k / 200d $65.2k** MAs → **resolves** in phase-6-macro.md §Rates + §Sector
   overlay. ✓

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9 (+ this audit) + decision.json.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (4 citations across phases 1/3/4/5/6).
- ✓ Conviction bin 0.65 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ ≥1 directional (bear call spread) + ≥1 defined-risk (iron condor) structure present.
- ✓ Sizing math shown; Kelly p = phase-5 win-rate (p_raw 0.857 → N-capped 0.75, n=7), not the bin.
- ✓ All five risk gates evaluated (fundamentals CONFIRM / sentiment CAUTION / correlation none / rotation neutral / debate not-disconfirmed); BUSY_NAME_NORMAL_DAY reflected (size cut from 2.1% → 1.5%).
- ✓ Structures sized to expected move (front ±1.46%, 8-day ±4.1%; `expected_move` in JSON; short strikes outside the move).
- ✓ `decision.json` exists, includes `context`/`expected_move`/`gates.sentiment`, and passes `validate_decision.py` (re-validated after confluence/recommended_bin backfill).

## Final auditor note

The run is **internally consistent and ready for action**: nine signal phases plus a
unanimous four-agent desk all converge on a gamma-pinned $14–$15 range with no
contradicting evidence, and phase-9 correctly translates that into a **small (1.5%),
strictly defined-risk** premium-selling structure rather than a directional bet —
honoring the 7c squeeze CAUTION and the 8b reflexive-up-tail. No revision required; the
only live break is a **BTC reclaim of $65.2k**, which the plan already names as the
invalidation and the plan-B counter-trade.
