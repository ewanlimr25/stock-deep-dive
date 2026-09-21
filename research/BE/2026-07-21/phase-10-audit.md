# Phase 10 — Audit & Confidence Score

**Ticker:** BE
**As-of date:** 2026-07-21
**Generated:** 2026-07-22T09:22:00Z
**Dominant bias audited:** RANGE (premium-selling, bullish-lean) — phase-9

## Summary

**Confluence score 54/100** (mildly-positive-of-mixed) → **recommended conviction
bin 0.65**. Phase-9 chose **0.55** — one notch *more conservative* than
recommended, a permitted downward deviation driven by the explicit 8b
disconfirmation and 7b CAUTION gates. The run is **internally consistent and
honest about its own tension**: the bullish-flow headline is correctly
re-read as put-SELLING (range/premium-selling), and the two genuine
counter-signals — phase-2 dark-pool **distribution** and phase-7 composite
**DIRECTIONAL_SHORT/DISTRIBUTION** — are logged as contradictions, not buried.
**2 contradictions**, **0 citation failures**, all sanity checks pass,
`decision.json` valid. The blueprint is ready for action as a **small,
defined-risk, wings-bought premium-sell**, not a conviction long.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** | Puts net **SOLD $25.7M** (bid $44.0M vs ask $18.3M) `[FLOW:sweeps]` — genuinely two-sided/contested, supports selling premium in a range but not a clean `++` |
| 2 — dark pool | **−** | Institutional-accumulation **DISTRIBUTION** (buy/sell 0.58), mega-tier 88.6% sold `[DP:block_stratified]` — supply overhang contradicts the floor-holds lean |
| 3 — OI | **+** | Put wall **197.5 (net −31,125 OI)** + 250 call wall define the exact range the thesis trades `[OI:oi_by_strike]` |
| 4 — structure | **0** | Backwardation + VRP **confirm** the sell-front-vol edge, but **FULLY_NEGATIVE GEX / 197.5 trapdoor** threatens the range holding `[STRUCT:gex]` — net mixed |
| 5 — historical | **+** | **VRP +0.4935, PREMIUM_SELLING** (IV 1.77 vs RV 1.28) `[HIST:vrp]` — the core premium-selling edge; tempered by net-bearish 90d flow |
| 6 — macro | **0** | Regime **TRANSITIONAL — "favor defined-risk / iron condors in range"** aligns, but "half position sizes" + 10y 4.6% are size-down headwinds `[MACRO:MarketRegime_2026-07-21]` — wash |
| 7 — insights | **−** | Composite **DIRECTIONAL_SHORT (15.4%) + DISTRIBUTION**; BE absent from bullish confluence top-40 `[INSIGHT:conviction_matrix]` — leans against the bullish-lean |
| 7b — fundamentals | **+** | **BULLISH / CAUTION**: 4/4 beats, +106.5% guide support the floor holding; capped by insider MSPR selling `[FUND:earnings_surprise]` `[FUND:MSPR]` |
| 8 — agents | **+10** | **5/5 align** with the non-directional range/premium-selling thesis (3 RANGE + 2 NEUTRAL, 0 directional) `[AGENT:*]` |

**Raw score (symmetric):** 7 − 7 + 7 + 0 + 7 + 0 − 7 + 7 + 10 = **+24**
**Base score:** round((24 + 130) / 260 × 100) = **59/100**
**Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no cap on phases 1–2 (none applied)
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_res 0.65 vs bear_res 0.65)
**Sentiment penalty (phase-7c):** −0 (`CONFIRM`, not CAUTION/VETO)
**Confluence_score:** **54/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **MISMATCH (one notch more conservative)**. Acceptable: downward deviations need no escape-hatch justification; driven by the explicit 8b + 7b gates in sizing. Not flagged as an error.

## Contradictions

- **phase-2 (dark pool):** DP tape reads **DISTRIBUTION** (mega-tier 88.6% sold, institutional-accumulation 0.58) against the bullish-lean floor-holds assumption — *resolution:* **tighten invalidation** (already: daily close < 197.5 = trapdoor) and hold size at **starter** (done); the bought 185 wing caps the tail.
- **phase-7 (insights):** UW composite tags **DIRECTIONAL_SHORT (low-conf) + DISTRIBUTION** and BE ranks in neither confluence extreme — *resolution:* already reflected by choosing **RANGE, not LONG**, and by the starter size; **wait for post-print confirmation** (IV compression + net_flow ≥ 0) before any add.

Both contradictions are the reason the trade is small, defined-risk, and
range-framed rather than a directional long — they are *priced into* the
blueprint, not ignored.

## Citation failures

*None.* Spot-checked 3 of phase-9's thesis citations:
1. `[FLOW:sweeps]` puts net SOLD $25.7M — ✓ resolves to phase-1-flow.md §Sweeps (bid $44.02M vs ask $18.30M).
2. `[HIST:vrp]` VRP +0.4935 PREMIUM_SELLING — ✓ resolves to phase-5-historical.md §IV regime.
3. `[STRUCT:gex]` FULLY_NEGATIVE, worst strike 197.5 (−4.84M) — ✓ resolves to phase-4-structure.md §GEX.

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10) + `decision.json`
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary)
- [✓] Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- [✓] ≥1 directional (Jan-2027 300/350 call debit spread) + ≥1 defined-risk (205/185 put credit spread)
- [✓] Sizing math shown; Kelly p = phase-5 win-rate 0.857 → N-capped 0.75 (not the bin)
- [✓] All 5 risk gates evaluated: fundamentals CAUTION (cut), sentiment CONFIRM (no-op), correlation none, rotation neutral, debate disconfirmed (cut + bin down-shift); phase-0.5 `GENUINELY_UNUSUAL` reflected (no-op, noted)
- [✓] Structures sized to front-expiry expected move ±10.6% / $23.89; `expected_move` in JSON; N4 check confirms a −10.6% gap does not breach the $198.50 breakeven
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. context / expected_move / gates.sentiment); confluence_score 54 + recommended_bin 0.65 backfilled

## Final auditor note

The run is **internally consistent and ready for action**: it correctly diagnoses
that BE's "record-bullish" flow is institutional put-writing into 100th-percentile
IV, converges the whole desk on a defined-risk range/premium-selling trade, and
honestly carries the two real counter-signals (DP distribution, composite
short-lean) as size-cutting contradictions rather than explaining them away.
Phase-9's 0.55 conviction is one notch below the confluence-implied 0.65 — a
conservative, defensible choice given the 8b tie and the 7b insider-selling
caution; no revision required, though a PM comfortable with the 4/4-beat base rate
could justify the 0.65 the score supports.
