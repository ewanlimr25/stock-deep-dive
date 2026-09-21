# Phase 10 — Audit & Confidence Score

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T22:50:00-0400
**Upstream phases cited:** all (phases 0–9 + decision.json)

## Summary

**Confluence score: 41/100** (base 51 − 10 for the phase-7c VETO penalty; no
debate penalty). Recommended bin from the 30–49 band: **0.55–0.65**; phase-9
chose **0.55 → MATCH** (bottom of band, consistent with two fired vetoes).
**Contradiction count: 5** (phases 3, 4, 5, 6 mildly contradict the RANGE
thesis; phase-7b is a hard-rule `--`). The run is internally consistent: every
contradiction is *directional-bearish pressure against a deliberately
non-directional thesis*, and phase-9 handled each one by gating the bearish
expression to watch-only rather than ignoring it. A score of 41 — just below
"perfectly mixed" — is exactly what a double-vetoed, stand-aside,
defined-risk-carry blueprint should score: the data is fighting itself, and
the plan says so.

## Confluence scorecard

(Dominant bias scored against: **RANGE** — phase-9. Context modifier:
phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` → no cap on phases 1–2.)

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | + | Ex-0DTE customer delta-notional ≈ **+$0.000bn** and net_flow −$9.6M on $460M gross — a two-way tape agrees with RANGE; the 5/5 bearish sweep persistence keeps it from `++` [FLOW:delta_notional DUCKDB] [FLOW:sweep_persistence] |
| 2 — dark pool | ++ | All tiers balanced — mega 0.518 / block 0.523 / large 0.497 on $814.46M — direct institutional-balance evidence for a range read [DP:block_stratified] |
| 3 — OI | − | Fresh ask-biased put builds (Jun-12 205P +6,871, twice running) and an all-put-wall ≤30-DTE map argue directional-bear, not range [OI:biggest_increases] [OI:oi_by_strike] |
| 4 — structure | − | `regime: FULLY_NEGATIVE`, ZGL null, biggest node at spot — an amplification regime contradicts a mean-reverting box (max-pain 235/230 above spot only partially offsets) [STRUCT:gex] [STRUCT:max_pain] |
| 5 — historical | − | VRP −0.0841 (realized 120.1% > implied 111.7%), 30/30 OI build days, GEX flip 06-03 — a trending/expanding tape with an 87.5% (N=8) bearish base rate mildly fights a range thesis [HIST:vrp] [HIST:signal_backtest] |
| 6 — macro | − | Net **headwind** at 4/5 conviction (AVGO guide-down, DGS2 +17bp, rotation adverse) — directional pressure against a neutral box [MACRO:AVGO_guidance_2026-06-03] [MACRO:DGS2_2026-06-04 FRED] |
| 7 — insights | ++ | Conviction-matrix **MIXED** (0.503), institutional-accumulation **NEUTRAL** (1.01), absent from both confluence screens at min-score 1 — the composite engine's strongest possible agreement with RANGE [INSIGHT:conviction_matrix] [INSIGHT:institutional_accumulation] |
| 7b — fundamentals | −− | **Hard rule: `tier_adjustment = VETO` scores at most `--`** — the directional (bear-lean) thesis is fundamentally vetoed (4/4 beats, ARR +54% QoQ contradict the flow on 2 of 3 axes) [FUND:earnings_surprises] |
| 8 — agents | +8 (4/4 align) | accumulation-hunter NEUTRAL, contrarian-scanner NEUTRAL, sweep-tracker RANGE, risk-monitor NEUTRAL — all four align with RANGE/stand-aside (+2 each); earnings-scout rule-skipped (0) [AGENT:all] |

**Raw score (symmetric):** +7 +15 −7 −7 −7 −7 +15 −15 +8 = **+2** (range −130…+130)
**Base score:** round((2 + 130) / 260 × 100) = **51/100**
**Gate penalties (one-sided):** phase-8b disconfirmed = false (bull_res 0.65 vs
bear_res 0.55) → −0 · phase-7c `VETO` → **−10**
**Confluence_score: 41/100**
**Recommended bin (30–49):** 0.55–0.65
**Phase-9 actual bin:** 0.55 → **MATCH**

## Contradictions

- **phase-3 (OI):** Pre-slide bearish put accumulation (205P +6,871 ask-biased
  ×2 sessions) contradicts the balanced-range read — *resolution: tighten
  invalidation* — phase-9 already arms the bear trigger at a daily close <220
  with sweep extension; keep it.
- **phase-4 (structure):** FULLY_NEGATIVE gamma means the box edges (205/250)
  will be *run through*, not defended, if tested — *resolution: tighten
  invalidation* — phase-9's same-day ±1.5×ATR clause covers this; honor it
  without waiting for the second close.
- **phase-5 (historical):** Negative VRP + 30-day OI build = an expanding-vol
  tape that historically punishes short-vol range structures — *resolution:
  downgrade conviction* (done: 0.55) and prefer the calendar over the condor
  (done: condor flagged not-preferred, half-sleeve).
- **phase-6 (macro):** 4/5-conviction headwind with adverse rotation pressures
  the downside edge of the box — *resolution: wait for confirmation* — the
  Jun-10 CPI is the nearest datapoint that resolves hawkish-break vs
  relief-squeeze; carry sleeve only until then.
- **phase-7b (fundamentals — VETO, `--`):** The directional bear thesis is
  **fundamentally vetoed** (improving earnings trend + growth contradict the
  flow on 2 of 3 axes) — *resolution: downgrade conviction* (applied: bear
  expression is watch-only/0%; the veto is the reason the bias is RANGE and
  not SHORT).

## Citation failures

(none — spot-check of 3+:)

1. `[FLOW:delta_notional DUCKDB]` "+0.265 −0.365 −0.195 +0.295 ≈ +0.000bn" →
   resolves to phase-1-flow.md §"Aggressor split ex-0/1DTE" table ✓
2. `[DP:block_stratified]` "mega 0.518 / block 0.523 / large 0.497, $814,456,252" →
   resolves to phase-2-dark-pool.md §"Tier breakdown" ✓
3. `[FUND:earnings_surprises]` "4/4 beats, +20.17% → +59.14%" → resolves to
   phase-7b-fundamentals.md §"Earnings-surprise history" table ✓
4. `[SENT:short_float fz semi-monthly]` "22.43% / 45.10M / DTC 2.54" → resolves
   to phase-7c-sentiment.md §"Short interest & borrow" ✓

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10(this) +
  decision.json (15 artifacts; `ls` verified)
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (8 in citations summary,
  spanning FLOW/DP/FUND/SENT/STRUCT/MACRO/HIST)
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- ✓ ≥1 directional (Jun-26 220/200 put debit spread — armed/watch-only,
  veto-marked) + ≥1 defined-risk (220 put calendar primary; 190/200/250/260
  iron condor alternative)
- ✓ Sizing math shown: p_raw 0.875 (n=8, backtest) → N-cap 0.75; b=1.67;
  raw_kelly 0.600; suggested 5.0%; final 0.0% directional after gates
- ✓ All five risk gates evaluated: fundamentals VETO / sentiment VETO
  (crowd CROWDED_SHORT) / correlation none (max ρ 0.222) / rotation adverse
  (half-step cut on carry) / debate disconfirmed=false — and the phase-0.5
  `GENUINELY_UNUSUAL` context check applied (no-op)
- ✓ Structures sized to expected move: ±15.7%/$35.8 front-expiry in
  `expected_move` (screener field flagged suspect, IV-derived substitute);
  condor explicitly flagged narrower-than-expected-move
- ✓ `decision.json` exists, backfilled (confluence_score 41, recommended_bin
  0.55, paths.audit) and `validate_decision.py` prints
  `OK: … valid DeepDiveDecision` (re-run post-backfill)
- ⚠ Note (not a failure): `sizing.deviation_reason` is populated to *document a
  downward forced cut* (5.0% → 0.0% by dual veto). The rubric requires a reason
  only for upward deviations; downward needs none. Kept for the calibration
  record; no upward deviation occurred.

## Final auditor note

The run is internally consistent and ready for action as written: a
double-vetoed, conviction-0.55, RANGE blueprint whose only live risk is a ≤1%
defined-risk carry sleeve, with the directional expression correctly parked
behind falsifiable triggers (close <220 + sweep extension, or 250 reclaim) and
both veto gates quoted in sizing. No revision to phase-9 required; the one
discipline item for the holder is to treat phase-4's amplification regime as
license to exit the carry on the *first* qualifying break, not the second
close.
