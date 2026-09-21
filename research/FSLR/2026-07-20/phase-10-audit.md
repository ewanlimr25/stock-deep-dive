# Phase 10 — Audit & Confidence Score

**Ticker:** FSLR · **As-of:** 2026-07-20 · **Version:** v1 · **Generated:** 2026-07-20
**Dominant bias (phase-9):** SHORT (mild) · **Phase-9 conviction:** 0.55

## Summary

**Confluence score = 45 / 100** — *mixed, with the data mildly fighting the short.*
The bearish tactical trio (flow, OI, structure, trend) is real and internally
consistent, but it is offset by **dark-pool accumulation (phase-2, −)**, a
**bullish/CAUTION fundamental read (phase-7b, −)**, a **MIXED composite that scores
FSLR on neither confluence side (phase-7)**, and a **desk that did not endorse the
short (phase-8, net −2)** — then docked −5 for the **disconfirmed debate** and −5
for the **phase-7c CAUTION**. Recommended bin (band 30–49) = **0.55–0.65**;
phase-9's **0.55 is a MATCH** at the low end. The run is **internally consistent and
honest about its own weakness**: it correctly resolves to a minimal (~0.6%),
defined-risk, event-timed short rather than a conviction position. **3 contradictions
logged; 3/3 citations resolve; all sanity checks pass.**

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** | "5-session persistent **bearish** sweep campaign, consistency 1.0, $16.3M" [FLOW:sweep_persistence] — agrees, but capped at `+` (BUSY_NAME_NORMAL_DAY) and much is vol-selling. |
| 2 — dark pool | **−** | "Large-tier **63.9% BUY**, $17.9M" [DP:block_stratified] + $205 buy-shelf — mild **accumulation contradicts** the short. |
| 3 — OI | **+** | "Aug 290C **sold-to-open** +3,254, Aug 190P bought +1,362; 2/3 smart-positioning bearish" [OI:smart_positioning] — agrees. |
| 4 — structure | **+** | "**FULLY_NEGATIVE** short gamma, DEX **−$226M**, dealers sell underlying" [STRUCT:gex][STRUCT:dex] — strongly agrees, but the vanna-squeeze-if-$200-holds keeps it at `+`. |
| 5 — historical | **+** | "**−26.4%** 30-session downtrend; bearish_flow backtest **90% (n=10)**" [HIST:trend][HIST:signal_backtest] — agrees; tempered by VRP PREMIUM_SELLING + MIXED 90d flow. |
| 6 — macro | **0** | Tech #1 outflow (aligned) vs **solar-policy tailwind** (adverse) net out [MACRO:sector_rotation][MACRO:SolarPolicy] — mixed for a single name. |
| 7 — insights | **0** | "FSLR **absent from both** bullish & bearish confluence top-40; MIXED, conf 7.5%" [INSIGHT:signal_confluence] — genuinely mixed, no clean stack. |
| 7b — fundamentals | **−** | "fundamental_signal **BULLISH**, CAUTION; fwd P/E 12.3, +27% growth" [FUND:valuation] — quality **contradicts** the short (CAUTION, not VETO → `−`). |
| 8 — agents | **net −2** | 2 SHORT (+2 each) vs 3 NEUTRAL/RANGE non-endorsing (−2 each); **0 LONG** but no desk majority for the short [AGENT:phase-8]. |

**Raw score (symmetric):** +7 −7 +7 +7 +7 +0 +0 −7 −2 = **+12**
**Base score:** round((12 + 130) / 260 × 100) = **55/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** 55 − 5 − 5 = **45/100**
**Recommended bin:** **0.55–0.65** (band 30–49)
**Phase-9 actual bin:** **0.55** → **MATCH** (at the low end of the band, appropriate given the disconfirmed debate + two CAUTION gates)

## Contradictions

- **phase-2 (dark pool):** large-tier 63.9% buy ($17.9M) and the $205.31
  institutional shelf are *accumulation into* the short's target — **tighten
  invalidation**: the short only confirms on a daily close below $205.31; a
  persisting/expanding buy-shelf is the exit tell (already encoded in phase-9's
  signal invalidation).
- **phase-7b (fundamentals):** a cheap (12.3× fwd), +27%-growth, unlevered
  compounder with a policy tailwind is not a fundamental short — **downgrade
  conviction** (done: CAUTION cut + bin at floor 0.55) and keep the position
  **defined-risk only**.
- **phase-8 (agents, net −2):** the desk produced no majority for the short (2 of
  5), only a lean — **keep size minimal** (done: ~0.6%, three gate-cuts) and treat
  as a tactical, event-timed trade, not a core position.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. **[FLOW:sweep_persistence]** "5-session, consistency 1.0, $16.3M" → resolves to
   phase-1-flow.md §Key signals ✓
2. **[STRUCT:dex]** "DEX −$226M, dealers hedge by selling underlying" → resolves to
   phase-4-structure.md §DEX ✓
3. **[HIST:trend]** "−26.4% 30-session downtrend" → resolves to phase-5-historical.md
   §Summary/§trend ✓

## Sanity checks

- ✓ All phase files present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10, decision.json).
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in thesis + citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✓ ≥1 directional (Aug-21 205/190 put debit spread) + ≥1 defined-risk (Aug-21
  220/230 call credit spread).
- ✓ Sizing math shown; Kelly p = phase-5 backtest win-rate 0.90 → N-capped 0.85
  (not the bin).
- ✓ All five risk gates evaluated: fundamentals CAUTION, sentiment CAUTION,
  correlation none, rotation aligned, debate disconfirmed. Phase-0.5
  BUSY_NAME_NORMAL_DAY reflected (floor sizing, no top-of-band).
- ✓ Structures sized to the ±5.31% front-expiry expected move; `expected_move`
  present in decision.json (front_expiry_pct 5.31, abs 10.89).
- ✓ decision.json exists, backfilled (confluence_score 45, recommended_bin 0.55),
  and passes `validate_decision.py` → **OK**.

## Final auditor note

The run is **internally consistent and ready for action as written** — a minimal,
defined-risk, earnings-timed *tactical* short whose size (~0.6%) and floor
conviction (0.55) honestly reflect a 45/100 confluence where a real bearish
flow/structure/trend trio is genuinely offset by dark-pool accumulation, cheap-and-
growing fundamentals, a policy tailwind, and a live post-earnings vanna-squeeze.
**No revision required**; the single most important thing to watch is the $200 line
into 07-30 — a break confirms the short toward $190, a hold flips the mechanics
(vanna bid) and triggers phase-9's fade plan.
