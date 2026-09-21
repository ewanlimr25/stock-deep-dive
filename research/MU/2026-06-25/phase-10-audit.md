# Phase 10 — Audit & Confidence Score

**Ticker:** MU
**As-of date:** 2026-06-25
**Generated:** 2026-06-25
**Dominant bias audited:** LONG (structural; near-term actionable = wait/fade-the-rip)

## Summary

**Confluence score: 44 / 100** — *slightly net-negative-to-mixed* against the LONG
bias. The data does not endorse a fresh long *here*: the bullish flow (phase-1) and
strong fundamentals (phase-7b) are real, but the dark pool is balanced (phase-2), OI
is mixed/hedged (phase-3), dealer structure caps upside (phase-4, scored `-`), the
desk is non-directional (phase-8, −4), the crowd is saturated long (phase-7c CAUTION,
−5 penalty), and the debate disconfirmed the entry (phase-8b, −5 penalty). **Score 44
→ recommended bin 0.55-0.65; phase-9 chose 0.55 → MATCH** (the gated low end is
correct). **Internal contradiction count: 1 strong (phase-4).** The run is internally
consistent and the blueprint's own conclusion — *right idea, wrong entry, token size,
wait for the $1,134 pullback* — is faithfully scored by the confluence math.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | #1 single-name net-bullish universe-wide, +$279M, calls 2.79× `[FLOW:insights_deep_dive]` — but two-way/mixed sweeps cap it at `+` |
| 2 — dark pool | **0** | #1 DP name $29.31B yet tiers balanced (mega 0.47) `[DP:block_stratified]` — engagement without direction = neutral (a non-confirmation of the long) |
| 3 — OI | **0** | 1200 call_heavy (net +37k) bullish, but new build put-dominated ~5:1 `[OI:biggest_increases]` — mixed/hedged = neutral |
| 4 — structure | **−** | POSITIVE-GEX long-gamma + vanna selling as IV deflates + max-pain 1,040 (−14.5%) `[STRUCT:max_pain]` — structure caps upside & pulls down vs a fresh long |
| 5 — historical | **+** | VRP −0.31 PREMIUM_BUYING + uptrend intact `[HIST:vrp]`, tempered by +325%-YTD parabola & N=5 backtest |
| 6 — macro | **0** | Memory supercycle tailwind vs TRANSITIONAL "reduce-size" regime, breadth 35.4% `[MACRO:MarketRegime_2026-06-25]` — genuinely mixed |
| 7 — insights | **0** | signal-confluence <1 both directions, conviction-matrix MIXED, accumulation NEUTRAL `[INSIGHT:conviction_matrix]` — composite is mixed |
| 7b — fundamentals | **+** | BULLISH: 4/4 beats, fwd P/E 8.4, best-in-class margins `[FUND:fwd_pe]` — but `tier_adjustment CAUTION` (insider selling) keeps it at `+`, not `++` |
| 8 — agents | **−4** | accumulation-hunter NEUTRAL (−2), contrarian RANGE (−2), sweep-tracker NEUTRAL (−2), risk-monitor LONG (+2); earnings-scout MISSING (excluded) — desk did not endorse the long |

**Raw score (symmetric):** phases (+7+0+0−7+7+0+0+7 = **+14**) + agents (**−4**) = **+10**
**Base score:** round((10 + 130) / 260 × 100) = **54 / 100**
**Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no cap on phases 1-2 (applied).
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.60 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (`tier_adjustment = CAUTION`, CROWDED_LONG); VETO penalty N/A
**Confluence_score:** 54 − 5 − 5 = **44 / 100**
**Recommended bin:** 0.55-0.65 (score in 30-49 band) → low end **0.55** given three fired gates
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-4 (structure):** Dealer structure (POSITIVE-GEX long-gamma, vanna selling
  while IV deflates 93→77, near-expiry max-pain at 1,040 = −14.5%) mechanically caps
  upside and pulls toward support — it *contradicts a fresh long at the 1,211-1,213
  double-top.* → **Resolution: already handled** — phase-9 down-weighted to a token
  0.3% size, made the *primary entry the $1,134 pullback* (not spot), and set the
  aggressive long to require a >$1,255 close on rising IV (which would flip vanna to a
  bid). No further action; the contradiction is the reason the trade is not "buy here."
- *(Non-scored non-confirmations: phases 2, 3, 6, 7 all scored `0` — balanced/mixed,
  not contradictory. They correctly withhold confirmation rather than oppose; the
  audit notes them as the reason confluence sits below 50.)*

## Citation failures

Spot-checked 3 of phase-9's thesis citations — **all resolve**:
1. `[FUND:fwd_pe]` forward P/E 8.4 → phase-7b-fundamentals.md §Valuation (fz fwd P/E 8.39). ✓
2. `[FLOW:insights_deep_dive]` net_flow +$279M, calls 2.79× → phase-1-flow.md §Whole-tape aggregate. ✓
3. `[DP:block_stratified]` mega buy_ratio 0.47 → phase-2-dark-pool.md §Tier breakdown. ✓

(none failed)

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + `decision.json`.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (5: fwd_pe, insights_deep_dive, price_vs_flow, block_stratified, max_pain).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✓ ≥1 directional (Sep-18 1150/1350 call debit spread) + ≥1 defined-risk (Jul-17 1100/1000 put credit spread).
- ✓ Sizing math shown; Kelly `p` = phase-5 backtest win-rate (0.60, n=5, capped 0.75 → 0.60), not the bin.
- ✓ All five gates evaluated: fundamentals CAUTION, sentiment CAUTION/CROWDED_LONG, correlation none, rotation aligned, debate disconfirmed. `unusual_verdict = GENUINELY_UNUSUAL` reflected (no-op, edge in `p`).
- ✓ Structures sized to front-expiry expected move (±3.93% / ±$47.39); `expected_move` in `decision.json`.
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. `context`, `expected_move`, `gates.sentiment`); confluence_score 44 + recommended_bin 0.55 backfilled and re-validated `OK`.

## Final auditor note

The run is **internally consistent and ready as a watch-and-wait blueprint, not a buy
ticket**: every lane that should confirm a chase (dark pool, OI, structure, the desk,
the crowd, the debate) declines to, and the confluence score (44) plus the token 0.3%
size honestly reflect that — the edge is a fundamentally-cheap supercycle long *on a
pullback to $1,134*, deliberately not a chase of the +15.8% gap into the 1,211-1,213
double-top. No phase-9 revision required; the one structural contradiction (phase-4)
is already priced into the entry plan and the size.
