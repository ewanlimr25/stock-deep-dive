# Phase 10 — Audit & Confidence Score

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T21:38:00Z
**Inputs audited:** phase-0 → phase-9 + decision.json

## Summary

**Confluence score: 50/100 — perfectly mixed**, which is the *correct* outcome for a thesis
that concluded there is **no clean directional edge**. The dominant bias (phase-9) is NEUTRAL
with a downside skew; the evidence splits cleanly — a genuine bull tell (dark-pool 100%-buy
accumulation) against a heavier bear stack (fundamental VETO, China-consumption headwind,
short-gamma-down, crowded long) — and the 8b debate disconfirmed both directions (0.55/0.55).
**Recommended bin from the 50–64 band is 0.65; phase-9 chose 0.55** — one notch more
conservative, which is *justified* (and not a defect) given the VETO, the true disconfirmation,
and the resulting **0%/watch-only sizing**. **2 contradictions** logged (phase-2, phase-7),
both already neutralized in phase-9 as watch-only with squeeze invalidation. All 3 spot-checked
citations resolve. decision.json validates. **The run is internally consistent and ready as a
"stand-aside / harvest-vol-only-if-forced" blueprint.**

## Confluence scorecard

Scored against phase-9's NEUTRAL/**down-skew** lean (the directional tilt within the neutral call),
so "+" = supports the defensive/down-skew/sell-vol read, "−" = argues the bullish counter.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **0** | Genuinely two-sided: "net +$1.12M, calls 61% but biggest print a downside 110P $1.945M" [FLOW:insights_deep_dive] — neither side. |
| 2 — dark pool | **−** | Contradicts the down-skew: "block tier 100% BUY $17.09M, $4.8M lift @97.35 above mid" [DP:block_stratified] — the bull tell. (BUSY_NAME cap n/a — it's a contradiction.) |
| 3 — OI | **+** | "7/8 fresh builds inferred bearish — calls written, puts bought" [OI:smart_positioning] — hedged/defensive supports the down-skew. |
| 4 — structure | **+** | "FULLY_NEGATIVE −$12.8M, −$8.63M at strike 95" [STRUCT:gex] — downside accelerant + vol-crush support the sell-vol/down read. |
| 5 — historical | **+** | "$102→96.58 drift; China peers FUTU −13%/TIGR −14%; VRP +0.072 premium-selling" [HIST:signal_backtest, HIST:vrp]. |
| 6 — macro | **+** | "China April retail +0.2% YoY (weakest since Dec '22) + Temu de-minimis removed" [MACRO:ChinaRetail_2026-04] — clear headwind. |
| 7 — insights | **−** | Contradicts the down-skew: "DIRECTIONAL_LONG (22.73% conf), bullish price/flow divergence" [INSIGHT:price_vs_flow]. |
| 7b — fundamentals | **+** | VETO that **supports** the down-skew: "EPS −13.2% TTM, rev 49%→9.65%, Q4 miss −15.6%" [FUND:epsGrowthTTMYoy] (the "VETO≤−−" cap binds only when it contradicts the bias; here it agrees). |
| 8 — agents | **+ (≈+6)** | 4 of 5 align with NEUTRAL/down-skew (contrarian SHORT, earnings-scout & risk-monitor lean short, accumulation-hunter RANGE); sweep-tracker's mild long lean nets against. |

**Raw score (symmetric):** phases 0 −7 +7 +7 +7 +7 −7 +7 = **+21**; phase-8 **+6** → **raw +27**
**Base score:** round((27 + 130) / 260 × 100) = **60/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.55 vs bear_residual 0.55)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION, CROWDED_LONG)
**Confluence_score:** 60 − 5 − 5 = **50/100**
**Recommended bin:** **0.65** (50–64 band)
**Phase-9 actual bin:** **0.55** — **MISMATCH (conservative)**: phase-9 sat one notch below the band,
justified by the 7b VETO + 8b disconfirmation + the resulting 0%/watch-only size. Acceptable
(downward deviation always permitted).

## Contradictions

- **phase-2 (dark pool):** 100%-buy block accumulation ($17.09M, lift above mid) is a genuine
  *bullish* signal contradicting the down-skew — and it is the debate's `strongest_bear_point`.
  **Resolution: already neutralized** — phase-9 keeps direction watch-only and sets a >104
  reclaim/vanna-bid as explicit invalidation; *wait for confirmation* (does a beat fire the squeeze?).
- **phase-7 (insights):** UW `DIRECTIONAL_LONG` + bullish price/flow divergence argue the long.
  **Resolution: down-rated at source** — confidence only 22.73%, PDD absent from the bullish
  confluence leaderboard; phase-9 already treats it as a low-confidence baseline, not a trade trigger.

(No phase scored `--`. The two `−` phases are the bull case, correctly carried as the live risk
to a defensive lean rather than ignored.)

## Citation failures

None — 3 of 3 phase-9 thesis citations spot-checked and resolved:
1. `[STRUCT:iv_term_structure]` "5/29 IV 98.3% vs back ~42%" → **resolves** (phase-4 §IV term structure). ✓
2. `[DP:block_stratified]` "block tier 100% buy $17.09M" → **resolves** (phase-2 §Tier breakdown). ✓
3. `[FUND:epsGrowthTTMYoy]` "EPS −13.2% TTM" → **resolves** (phase-7b §Growth profile). ✓

## Sanity checks

- ✓ All phase files present (0, 0.5, 1–7, **7b, 7c**, 8, **8b**, 9) + decision.json.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (6 listed).
- ✓ Conviction bin ∈ {0.55…0.95} (0.55).
- ✓ ≥1 directional (bear put spread, watch-only) + ≥1 defined-risk (iron condor) structure.
- ✓ Sizing math shown; Kelly `p` = conviction-bin fallback (0.55) — **justified**: phase-5
  `dark_pool_accumulation` backtest returned `total_signals 0` / `win_rate_source null`.
- ✓ All five risk gates evaluated: fundamentals **VETO**, sentiment **CAUTION**, correlation
  **none** (no concurrent blueprint; KWEB 0.81 soft-watch), rotation **neutral/lean-adverse**,
  debate **disconfirmed**. Context **BUSY_NAME_NORMAL_DAY** reflected (not sized at band top).
- ✓ Structures sized to the front-expiry expected move (`expected_move` 5.69% / $5.50 in JSON;
  IC shorts at ~1.2–1.35× implied).
- ✓ decision.json exists and **passes `validate_decision.py`** (incl. `context`,
  `expected_move`, `gates.sentiment`/`crowd_state`). `final_size_pct 0.0` consistent with
  negative raw Kelly + gates (validator confirmed).

## Final auditor note

The run is **internally consistent**: every phase is cited, the lone bullish signals (DP
accumulation, UW divergence) are logged as contradictions and carried as the live risk rather than
buried, and the sizing honestly resolves to **watch-only/0%** because the raw Kelly is negative and
the fundamental VETO + debate disconfirmation leave no edge to size. **No revision needed** — the
blueprint's correct conclusion is "**stand aside on direction; the only non-disconfirmed edge is
selling the 98% event vol with defined risk, and even that does not clear the gates for a sized
position.**" The two levels that would change the call are explicit and monitorable: a post-print
reclaim/hold **>104** (bull/squeeze fires) or a break/hold **<95** (short-gamma cascade confirms the bear).
