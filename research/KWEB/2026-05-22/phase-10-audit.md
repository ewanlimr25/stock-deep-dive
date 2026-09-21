# Phase 10 — Audit & Confidence Score

**Ticker:** KWEB
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Dominant bias audited:** RANGE (downside lean, long-convexity expression) — phase-9

## Summary

**Confluence score 57/100 → recommended bin 0.65; phase-9 ran 0.55 (one notch
conservative — MINOR MISMATCH, defensible).** The chain is **internally
consistent**: every phase converges on the same read — a genuinely **mixed,
non-directional setup** where a bullish lit-options skew is unconfirmed by (and
mildly contradicted by) the share tape, the only clean edge is **cheap vol**, and
two downside gates (7b/7c CAUTION) plus a TRANSITIONAL regime compress the trade to
a **0.5% probe**. Only **one phase contradicts** the dominant bias (phase-1's
bullish flow, which the thesis explicitly reframes as the divergence/upside-tell).
All three spot-checked citations resolve. `decision.json` valid. **Ready for action
as written** — a low-conviction, defined-risk, cheap-convexity range trade.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **−** | Bullish lit skew (net **+$2.65M**, P/C 0.25 `[FLOW:insights_deep_dive]`) is the one directional pull *against* the range/downside-lean. |
| 2 — dark pool | **+** | Block **distribution** (mega buy_ratio **0.0**, block **0.306** `[DP:block_stratified]`) into the low supports the cautious/downside lean (de-rated for ETF/near-mid caveats). |
| 3 — OI | **+** | **Two-sided/capped** — bull calls matched by writing 29.5-32, June walls trimmed, **not pinned** `[OI:smart_positioning]` — the textbook range read. |
| 4 — structure | **0** | Genuinely two-way: short-gamma at spot (can trend) + long-gamma cap 29-31 + **vanna-squeeze if IV falls** `[STRUCT:gex]` `[STRUCT:vanna_charm]`. |
| 5 — historical | **+** | **IV 3.33 pctile + VRP −0.039** `[HIST:vrp]` (buy-vol) and a −12% downtrend support the long-convexity/downside-lean core. |
| 6 — macro | **0** | Two-sided: firm USD + transitional regime (headwind) vs summit/stimulus tailwind `[MACRO:USChina_summit_2026-05-15]`. |
| 7 — insights | **0** | `conviction_matrix` MIXED, institutional NEUTRAL — confirms "mixed," but `price_vs_flow` DIVERGENCE is a bullish offset `[INSIGHT:conviction_matrix]`. |
| 7b — fundamentals | **+** | **CAUTION** — BABA 4 straight misses, latest −89.5% `[FUND:earnings_surprise]` — supports the cautious/downside lean (not VETO). |
| 8 — agents | **+ (5/5 align)** | All five non-directional (NEUTRAL/RANGE), avg conviction 2.6 → +2×5 = **+10**. |

**Raw score (symmetric):** −7 +7 +7 +0 +7 +0 +0 +7 +10 = **+31**
**Base score:** round((31 + 130)/260 × 100) = **62/100**
**Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no cap on phases 1–2.
**Debate penalty (phase-8b):** disconfirmed = **false** (bull_res 0.70 vs bear_res 0.60) → **−0**
**Sentiment penalty (phase-7c):** `CAUTION` → **−5**
**Confluence_score:** 62 − 5 = **57/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** → **MISMATCH (one notch conservative)**

## Contradictions

- **phase-1 (flow):** the bullish lit call skew (net +$2.65M, P/C 0.25) is the lone
  directional signal pulling against the RANGE/downside-lean thesis. **Resolution:
  already handled + tighten invalidation** — phase-9 reframes it as the unconfirmed
  divergence (phase-2/3/7c show no institutional/fund confirmation) and sets the
  **>$29 sustained-close flip-long** invalidation precisely to respect it. **Wait
  for confirmation:** a >$27.95 reclaim on rising volume would validate the bull tell
  and the trade should flip to the call side (phase-9 "fade/plan-B" entry).

## Citation failures

None — all three thesis citations spot-checked and resolved:
1. `[FLOW:insights_deep_dive]` net +$2.65M / P/C 0.25 → **resolves** (phase-1 §Whole-tape: net_flow +$2,646,982, P/C 0.2506). ✓
2. `[DP:block_stratified]` mega 0.0 / block 0.306 → **resolves** (phase-2 §Tier breakdown). ✓
3. `[HIST:iv_percentile_zscore]` IV 3.33 pctile → **resolves** (phase-5 §IV regime: iv_percentile 3.33). ✓

## Sanity checks

- ✓ All phase files present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + `decision.json`.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (7 listed).
- ✓ Conviction bin ∈ {0.55…0.95} (0.55).
- ✓ ≥1 directional (Jun 27/24 put debit spread) + ≥1 defined-risk (Jun 25P/29C long strangle).
- ✓ Sizing math shown; Kelly `p` = **justified fallback** (backtest win-rate 1.00 is
  directional bullish_flow, bias-mismatched to RANGE + non-KWEB → fell back to
  conviction-bin p=0.55, documented). Defensible and only *reduces* size.
- ✓ All five risk gates evaluated (fundamentals CAUTION, sentiment CAUTION, correlation
  none, rotation neutral, debate false) + context `GENUINELY_UNUSUAL` reflected.
- ✓ Structures sized to expected move (±8.5% monthly; `expected_move` block in JSON);
  defined-risk debits cap single-headline gap risk (N4 satisfied).
- ✓ `decision.json` exists and passes `validate_decision.py` (OK); `confluence_score`/
  `recommended_bin` backfilled (57 / 0.65); `paths.audit` set.
- ⚠ **Minor mismatch:** phase-9 bin 0.55 vs recommended 0.65. Acceptable — the two
  CAUTION gates and the genuinely low *tradeable* edge justify the conservative bin;
  it does not change the gated 0.5% size. Phase-9 should ideally carry a one-line
  `## Conviction deviation` note; flagged here for the record.

## Final auditor note

The run is **internally consistent and ready for action**: nine of nine signal reads
cohere around a low-conviction, non-directional, cheap-convexity range trade with a
downside lean, and the single contradiction (phase-1 bullish flow) is explicitly
managed by the >$29 flip-long invalidation and the strangle's covered upside tail.
The only revision worth making is cosmetic — document the deliberate 0.55-vs-0.65
conviction deviation — since the gated **0.5% probe** size and defined-risk debit
structures already encode the appropriate caution; do **not** upsize on the 57
confluence, as the edge lives in the cheap vol, not in any directional confluence.
