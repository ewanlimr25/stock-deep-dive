# Phase 10 — Audit & Confidence Score

**Ticker:** BABA · **As-of:** 2026-07-23 · **Generated:** 2026-07-24
**Dominant bias audited (phase-9):** **SHORT / fade** · **Spot:** $114.99

## Summary

**Confluence score = 50/100 (perfectly mixed).** Recommended conviction bin **0.65**; phase-9's
actual bin **0.55** — a **one-step-conservative deviation** driven by the mandated phase-8b debate
down-shift and the stacked 7b/7c CAUTION gates (a *downward* deviation, always allowed). The run is
**internally consistent**: every phase points the same *direction* (down/capped) but the score sits
at 50 because the edge is genuinely thin — the bearish flow is modest on a BUSY_NAME_NORMAL_DAY, and
one phase (phase-5) materially contradicts via the **+$625M bullish 90-day flow**. **1 contradicting
phase (phase-5).** All 3 spot-checked citations resolve. The blueprint is a coherent, honestly-sized
**very small defined-risk fade** — ready for action as written, not for upsizing.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | 5-session bearish sweep persistence, consistency 1.0, $76.53M, net_flow −$1.68M `[FLOW:sweep_persistence]` (capped at + by BUSY_NAME_NORMAL_DAY) |
| 2 — dark pool | **0** | Aggregate balanced (buy/sell 1.12, no mega prints); block-tier distribution (0.356) offset by large-tier accumulation (0.581) — phase-7 called it NEUTRAL `[DP:block_stratified]` |
| 3 — OI | **0** | Call-tilted build (14:2) reads bullish on its face but interpreted as overwriting; the $120 call wall as a *ceiling* supports the fade — nets neutral `[OI:oi_by_strike]` |
| 4 — structure | **+** | Short-gamma regime (spot < ZGL $119.71) + COMPLACENT skew (0.924) + $120 gamma cap all support a capped, downside-asymmetric fade `[STRUCT:gex]` `[STRUCT:term_skew]` |
| 5 — historical | **−** | `bearish_flow` backtest 87.5% supports the short, but **90d cumulative flow is net BULLISH +$625M with 30 build-days** — a genuine contradiction to a short `[HIST:cumulative_premium_flow]` |
| 6 — macro | **+** | HEADWIND: TRANSITIONAL/CHOPPY regime, Consumer-Cyclical outflow −$3.04B, China tariff/DoD-blacklist overhang — aligned with the fade `[MACRO:MarketRegime_2026-07-23]` |
| 7 — insights | **0** | Conviction-matrix MIXED (2.8%), signal-confluence <1 both directions — no directional edge; net call selling supports the fade but the composite finds no confluence `[INSIGHT:conviction_matrix]` |
| 7b — fundamentals | **+** | BEARISH/CAUTION: 0/4 beat-rate, EPS −17.8% confirm the bearish direction; CAUTION (not VETO) for cheap valuation + AI tailwind `[FUND:earnings_surprise]` |
| 8 — agents | **+ (3/5 align, 0 oppose)** | 3 SHORT (+2 each = +6), 1 NEUTRAL, 1 RANGE (0 each), **0 LONG** — desk avg conviction 2.4 `[AGENT:contrarian-scanner]` |

**Raw score (symmetric):** +7 +0 +0 +7 −7 +7 +0 +7 (phases 1–7b) = **+21**; phase-8 = **+6** → **+27**
**Base score:** round((27 + 130) / 260 × 100) = **60/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed: bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** 60 − 5 − 5 = **50/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **MISMATCH (conservative, −1 bin)**: driven by the phase-8b
debate down-shift gate (`rubrics/sizing-rubric.md` §5) stacked on the 7b/7c CAUTIONs + BUSY_NAME
context. Downward deviation is always permitted; **acceptable, not a blocker.** (A one-line
`## Conviction deviation` note in phase-9 would formalize it — recommended, not required.)

## Contradictions

- **phase-5 (historical): the +$625M net-bullish 90-day cumulative flow with 30 consecutive OI-build
  days contradicts a short** — the strongest single counter (and the phase-8b `strongest_bear_point`).
  *Resolution: already reflected — (a) invalidation tightened to a 3-consecutive-session bullish-flow
  flip; (b) size cut to ~0.6% (minimal); (c) conviction held at the floor bin 0.55. Phase-9's rebuttal
  (the bull flow bought no upside — price fell $115.4→$114.1 as it accreted → absorbed/overwriting) is
  logged but does not erase the contradiction; keep the position tiny and defined-risk.*

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[FLOW:sweep_persistence]` — "5-session bearish sweep, consistency 1.0, $76.53M" → **resolves** (phase-1-flow.md §Sweeps / Key signals). ✓
2. `[STRUCT:gex]` — "short-gamma regime, spot below ZGL $119.71" → **resolves** (phase-4-structure.md §GEX, regime NEGATIVE, ZGL $119.71). ✓
3. `[FUND:earnings_surprise]` — "0/4 beat-rate, latest −89.5%" → **resolves** (phase-7b-fundamentals.md §Earnings-surprise table). ✓

## Sanity checks

- [✓] All phase files present — 0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10, + decision.json.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 in the citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → **0.55**.
- [✓] ≥1 directional (put debit spread 115/110) + ≥1 defined-risk (iron condor) structure present.
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate **0.875 → capped 0.75** (n=8, backtest), not the bin.
- [✓] All five risk gates evaluated in phase-9 (fundamentals CAUTION, sentiment CAUTION/CROWDED_LONG,
  correlation none, rotation aligned, debate disconfirmed) — **3 fired**; phase-0.5
  **BUSY_NAME_NORMAL_DAY** reflected (no top-of-band sizing).
- [✓] Structures sized to front-expiry expected move (±1.56% / $1.78); `expected_move` in decision.json.
- [✓] `decision.json` exists and passes `validate_decision.py` (**OK**), with `context`,
  `expected_move`, `gates.sentiment`, and backfilled `confluence_score=50` / `recommended_bin=0.65`.
- [✓] Earnings-date uncertainty (mid-Aug vs UW 09-04) carried into structures (dated 08-14) and catalysts.

## Final auditor note

The run is **internally consistent and ready for action as a minimal, defined-risk fade** — every
phase agrees the tape is capped and downside-tilted, no agent is long, and the honest 50/100 score
correctly reflects a thin edge dominated by the $119–120 structural cap against a beaten-down, cheap,
bullish-90d-flow underlying. **No phase-9 revision required**; the one conservative bin-mismatch (0.55
vs recommended 0.65) is a deliberate, rubric-driven down-shift for the disconfirmed debate — leave it,
and keep the size at the ~0.6% floor with the invalidation on a $120 reclaim.
