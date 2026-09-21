# Phase 10 — Audit & Confidence Score

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Dominant bias audited:** SHORT (defined-risk fade) — phase-9

## Summary

**Confluence score: 68/100** (mildly positive — the dominant SHORT/fade bias is
supported by 7 of 8 phases, fought only by fundamentals). **Recommended bin (table):
0.75; phase-9 actual: 0.65 — MISMATCH, deliberate downward deviation** documented in
phase-9 (justified by the phase-7b fundamentals VETO + phase-0.5 BUSY_NAME context +
the phase-8b post-settlement bounce risk). **One contradiction** (phase-7b, the
fundamental veto). The run is **internally consistent**: every composite/raw cut tells
the same story — a high-quality semi distributed at the top by its 76% owner — and the
single contradiction (the business is *good*) is exactly why the plan is a small,
defined-risk fade rather than a naked short. All 3 spot-checked citations resolve.
**Ready for action as written.**

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|:---:|---------------------------|
| 1 — flow | `+` | Call SELLING > buying ex-0/1DTE (5,885 vs 4,171 ct), net −$0.3M — mildly bearish; capped at `+` by BUSY_NAME context `[FLOW:aggressor_ex0dte DUCKDB]` |
| 2 — dark pool | `+` | $83M 5-day DP supply cluster at $91–92 + pre-market sell blocks; intraday buy_ratio only 0.573 (suggestive); capped at `+` by context `[DP:price_levels]` |
| 3 — OI | `+` | Near-term defensive: $120 Jun calls SOLD + $85 Jun puts BOUGHT, ITM calls closing `[OI:smart_positioning]` |
| 4 — structure | `++` | Short gamma, spot $81.04 < ZGL $86.37; COMPLACENT skew; backwardation; vanna→selling `[STRUCT:gex]`, `[STRUCT:term_skew]` |
| 5 — historical | `+` | +91% over window / +87.5% vs 200-DMA, latest flow bearish; tempered by 90d cumulative flow +$15.7M BULLISH `[HIST:trend]`, `[HIST:cumulative_premium_flow]` |
| 6 — macro | `+` | Tech net outflow −$433.5M (largest sector) + hawkish Fed + TRANSITIONAL regime; tempered by CHIPS/easing structural tailwind `[MACRO:sector_rotation_2026-05-27 UW]` |
| 7 — insights | `+` | price-vs-flow DIVERGENCE TRUE (price +60.6% vs bearish flow); composite otherwise MIXED `[INSIGHT:price_vs_flow]` |
| 7b — fundamentals | `--` | **VETO** — 4/4 beats, fortress B/S, +30.7% fwd EPS contradict the SHORT on 2 axes; flow is a pullback, not a short `[FUND:earnings_surprise]` |
| 8 — agents | `+` (2/4 align, 2 neutral-fade, 0 opposed) | 2 SHORT (+2 each), 2 NEUTRAL-fade (0); net +4 |

**Raw score (symmetric):** 42 (eight phases: +7+7+7+15+7+7+7−15) + 4 (agents) = **46**
**Base score:** round((46 + 130) / 260 × 100) = **68/100**
**Debate penalty (phase-8b):** −0 — `disconfirmed=false` (bull_res 0.75 vs bear_res 0.65)
**Sentiment penalty (phase-7c):** −0 — `tier_adjustment=CONFIRM` (crowd confirms the fade)
**Confluence_score:** **68/100**
**Recommended bin:** **0.75** (65–79 band)
**Phase-9 actual bin:** **0.65** — **MISMATCH (deliberate downward deviation, documented)**

## Contradictions

- **phase-7b (fundamentals):** the business is genuinely high-quality (4/4 earnings
  beats avg +15%, LT-debt/equity 0.089, +30.7% fwd EPS, fresh dividend/buyback), which
  **contradicts a bearish/short thesis** `[FUND:earnings_surprise]`. **Resolution
  (already applied):** the VETO down-shifts the trade to **defined-risk only** (no
  naked short, directional size = 0%), conviction taken to the **lower** 0.65 bin, and
  the downside target kept conservative (gap-fill, not collapse — the dividend/buyback
  + $79.95 mean target floor the move). This is the correct handling, not an unresolved
  conflict.

## Citation failures

None — all 3 spot-checked phase-9 thesis citations resolve:
1. `[SENT:insider_block WebSearch:bloomberg.com]` → phase-7c §Key signals / News flow:
   "Mubadala $1.91B / 22M-share block … marketed $86.30–86.80 … settles 05-28." ✓
2. `[STRUCT:gex]` → phase-4 §GEX: "regime NEGATIVE … ZGL $86.37 … spot $81.04." ✓
3. `[MACRO:sector_rotation_2026-05-27 UW]` → phase-6 §Market regime/Sector rotation:
   "Technology −$433.5M … largest sector outflow." ✓

## Sanity checks

- [✓] All phase files present (phase-0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, + this audit, + decision.json)
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary)
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65
- [✓] ≥1 directional (put debit spread) + ≥1 defined-risk (bear call credit spread)
- [✓] Sizing math shown; Kelly p = phase-5 win-rate 0.583 (n=12, backtest), N-capped
- [✓] All five risk gates evaluated: fundamentals VETO / sentiment CONFIRM /
      correlation FIRED (cluster) / rotation aligned / debate not-disconfirmed; and
      phase-0.5 BUSY_NAME_NORMAL_DAY reflected (directional vetoed to 0; carry starter)
- [✓] Structures sized to front-expiry expected move (±13.6% in `expected_move`);
      targets/stop inside the priced move, defined-risk survives a single-gap
- [✓] `decision.json` exists and passes `validate_decision.py` ("OK"); `context`,
      `expected_move`, `gates.sentiment` fields present; confluence_score 68 +
      recommended_bin 0.75 backfilled
- [✓] Disclaimer present at top of phase-9

## Final auditor note

The run is **internally consistent and ready for action**: an exceptionally clean
signal stack (strategic-owner $1.91B distribution at the parabolic top, short-gamma
dealer positioning, complacent skew, tech rotation out) all point the same direction,
and the lone contradiction — a high-quality underlying — is correctly converted from a
veto-of-the-short into the *reason* the trade is a small, defined-risk fade with a
conservative target rather than a naked short. The only judgment a reviewing PM should
re-confirm is the **05-28 block-settlement timing** (phase-8b's strongest bear point):
the edge is in the next few sessions, and a hard bounce off settlement toward $86
closes the window — so the credit spread (theta-positive) is preferable to the debit,
and the position should be lifted into any reclaim of the $86.37 ZGL.
