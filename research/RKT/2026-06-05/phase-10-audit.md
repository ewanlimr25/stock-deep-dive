# Phase 10 — Audit & Confidence Score

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T19:00:00-04:00
**Dominant bias audited:** SHORT (from phase-9-trade-plan.md)

## Summary

**Confluence score: 51/100** (base 61, −5 debate disconfirmation, −5 phase-7c
CAUTION) → **recommended bin 0.65**; phase-9 chose **0.55** — a downward,
gate-mandated deviation (phase-8b disconfirmation down-shifts one bin per
`rubrics/sizing-rubric.md` §Risk gates) — **acceptable, conservative
direction**. Contradiction count: **2** (phase-3 OI, phase-7b fundamentals
VETO). The run is internally consistent: a near-mixed tape (51 ≈ "perfectly
mixed" 50) correctly produced a watch-only directional envelope
(`final_size_pct 0.0`) with a starter-budget defined-risk carry. All three
spot-checked citations resolve. `decision.json` backfilled and re-validated
`OK`.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|---|---|---|
| 0.5 — context (modifier) | cap | `unusual_verdict = BUSY_NAME_NORMAL_DAY` → phases 1–2 capped at `+` (self_pctile_net_dir 38.5, outside top-50 all boards) |
| 1 — flow | **+** (+7, capped) | "derived net_flow **−$209,751**; calls 8,042 ask vs 12,773 bid, puts 7,706 ask vs 3,119 bid ex-0DTE [FLOW:aggressor_ex0dte DUCKDB]; biggest print an opening **sale** of 3,460 Jul-10 $14.5C" — bearish tilt, would not exceed `+` even uncapped (LEAP bullish undertow) |
| 2 — dark pool | **+** (+7, capped) | "block-tier derived sell_ratio **0.883** high-confidence; no DP cluster below $12.65 [DP:block_stratified, price_levels]" — distribution-leaning ex-cross |
| 3 — OI | **−** (−7) | "all 3 qualifying builds **bullish** call-side (Sep-18 $13C +2,971, ask 2,258 vs bid 1,155 [OI:biggest_increases]); Jan-27 $9.2 synthetic-long signature" — positioning contradicts the SHORT |
| 4 — structure | **0** | split: short-gamma pocket ($13 net_gex −4.59M) + DEX dealer-sell agree, but max-pain magnets **above** spot ($14/$14.5 [STRUCT:max_pain]) + armed vanna squeeze contradict — net neutral |
| 5 — historical | **++** (+15) | "price 13.67→12.65, 19/30 bearish days, total GEX −97% in 5 sessions [HIST:gex_time_series]; bearish_flow win_rate 87.5% [HIST:signal_backtest]; −27.5% below SMA200, +2.18% off 52w low [HIST:52w_proximity fz]" — trend, signal class and cushion all bearish |
| 6 — macro | **++** (+15) | "30y mortgage 6.588–6.69% rising off 6.09% low [MACRO:Mortgage30Y_2026-06-05]; U-Mich record-low 44.8; TRANSITIONAL regime, VIX 21.51 +40% d/d; L-1 unlock 06-30" — 4/5-conviction headwind for the name |
| 7 — insights | **+** (+7) | "scenario COVERED_CALL ('capping upside'), divergence false, flow_sentiment bearish [INSIGHT:conviction_matrix, price_vs_flow]; lone bullish composite (ACCUMULATION 5.3) is a closing-cross artifact — overridden with cause" |
| 7b — fundamentals | **--** (−15, VETO cap) | "**fundamental VETO**: 4/4 beats (+25.6% to +50.5%) [FUND:earnings_surprises], rev +75.31% TTM, Q1 OCF +$1.857B — 2 of 3 axes contradict the SHORT; directional thesis is fundamentally vetoed" |
| 8 — agents | **0** (2 aligned, 2 not) | sweep-tracker SHORT (+2), risk-monitor SHORT (+2), accumulation-hunter NEUTRAL (−2), contrarian-scanner NEUTRAL (−2); earnings-scout skipped (excluded) |

**Raw score (symmetric):** +7 +7 −7 +0 +15 +15 +7 −15 +0 = **+29** (range −130…+130)
**Base score:** round((29+130)/260×100) = **61**/100
**Debate penalty (phase-8b):** −5 — `disconfirmed = true` (bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** −5 — `tier_adjustment = CAUTION` (improving revisions vs bear thesis)
**Confluence_score: 51/100**
**Recommended bin (table):** 0.65 (band 50–64)
**Phase-9 actual bin:** 0.55 — **MISMATCH, downward**: phase-9 applied the
phase-8b gate's mandatory one-bin down-shift on top of the band ("Why this
bin" note present). Downward deviations are always allowed; no action.

## Contradictions

- **phase-3 (OI positioning):** every qualifying OI build was bullish
  call-side (Sep-18 $13C +2,971 ask-skewed; smart-positioning 3/3 bullish;
  Jan-27 synthetic-long) while the thesis is SHORT — *resolution:* tighten
  invalidation (already done — the $13.26/$13.50 reclaim triggers) and **wait
  for confirmation**: Monday's OI must confirm the Jul-10 $14.5C short
  (~+3,400) for the cap leg to stand; if instead the call builds accelerate,
  exit the carry.
- **phase-7b (fundamentals): VETO** — the business is improving on 2 of 3
  axes against a bearish thesis — *resolution:* **downgrade conviction +
  directional 0%** (applied: bin 0.55, `final_size_pct 0.0`, carry-only
  defined-risk at starter budget). The audit flags explicitly: **the
  directional thesis is fundamentally vetoed**; the blueprint survives only as
  a defined-risk, mechanics-driven carry into 06-30.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[FLOW:aggressor_ex0dte DUCKDB]` "calls net-sold 12,773 bid vs 8,042 ask;
   puts net-bought 7,706 vs 3,119" → resolves to phase-1-flow.md §DuckDB §A
   table (exact values present) ✓
2. `[DP:price_levels]` "no dark-pool shelf below $12.65" → resolves to
   phase-2-dark-pool.md §Price levels ("no cluster below $12.65 in the top
   15") ✓
3. `[HIST:gex_time_series]` "47.6M → 1.33M (−97%) in five sessions" → resolves
   to phase-5-historical.md §GEX time series (47,609,090 (05-29) → 1,333,718
   (06-05)) ✓

## Sanity checks

- [✓] All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, **7b**, **7c**, 8,
  **8b**, 9, decision.json (ls verified; 15 artifacts)
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 in Citations summary,
  spanning FLOW/DP/HIST/MACRO/FUND/DEBATE)
- [✓] Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- [✓] ≥1 directional (12.5/11 put debit spread, veto-marked carry) + ≥1
  defined-risk (14.5/16 call credit spread) structure present
- [✓] Sizing math shown; Kelly p = phase-5 win-rate 0.875 N-capped to 0.75
  (n=8 < 10), not the conviction bin; SHORT-side floor n/a (p ≥ 0.50)
- [✓] All five risk gates evaluated in phase-9 §Sizing (7b VETO fired → 0%
  directional; 7c CAUTION fired → step cut; correlation none; rotation
  neutral; 8b disconfirmed fired → bin down-shift + step cut); phase-0.5
  `BUSY_NAME_NORMAL_DAY` reflected (no top-of-band size)
- [✓] Structures sized to the front-expiry expected move (±1.198% / $0.1514
  [CTX:implied_move_pct]; √t-scaled check + catalyst-gap check in phase-9
  §Option structures; `expected_move` block in decision.json)
- [✓] `decision.json` exists, `confluence_score` 51 + `recommended_bin` 0.65
  backfilled, `validate_decision.py` → **OK** (incl. `context`,
  `expected_move`, `gates.sentiment` fields; VETO↔final_size_pct=0 rule
  enforced and passing)

## Final auditor note

The run is internally consistent and ready for action **as filed**: a 51/100
near-mixed confluence honestly produced a watch-only directional envelope with
a 1%-budget defined-risk carry, and every bullish composite that survived
upstream (ACCUMULATION artifact, max-pain magnets) was either explained or
priced into the fade plan. Phase-9 needs no revision; the two contradictions
(bullish OI builds, fundamental veto) are correctly converted into tightened
invalidation and the zeroed directional size, and the calibration loop should
judge this blueprint by its carry structure, not a directional claim.
