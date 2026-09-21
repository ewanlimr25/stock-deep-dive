# Phase 10 — Audit & Confidence Score

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T02:35Z
**Dominant bias audited:** RANGE (50–60 box, tactical bearish tilt at the top) — from phase-9-trade-plan.md

## Summary

**Confluence score: 48/100** (base 58, −5 debate-disconfirmed, −5 phase-7c
CAUTION) → recommended bin **0.55** — phase-9's actual bin is **0.55: MATCH**
(via the 30–49 band plus the phase-8b mandated down-shift). Contradiction
count: **3** (phases 4, 5, 6 each score `-` against the RANGE thesis — all
three are the same underlying objection: an unresolved exogenous driver
amplified by short gamma fights a stabilization thesis). All three
spot-checked citations resolve. All sanity checks pass; `decision.json`
backfilled and re-validated `OK`. The run is internally consistent: a
mixed-signal name, honestly scored as mixed, sized accordingly (0.6% after
three fired gates).

## Confluence scorecard

Context modifier check (phase-0.5): `unusual_verdict = GENUINELY_UNUSUAL` →
no cap on phases 1–2.

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | + (+7) | Two-sided under a bearish surface: bid sweeps $49.8M led by Jan-27 LEAP profit-taking *inside* a 5/5-bullish $339,924,997 campaign [FLOW:sweep_persistence], and the 6,759× 55P/56C strangle SOLD at bid is a direct range bet [FLOW:top_premium_trades]. |
| 2 — dark pool | + (+7) | "Mixed — two-way churn, mild buy lean": block buy_ratio 0.588, large 0.535, mega tier EMPTY [DP:block_stratified] — no directional conviction = range-consistent. |
| 3 — OI | + (+7) | The walls bracket the box exactly: 50 put_wall (net_oi −45,730) / 60 call_wall (+13,669) ≤30DTE [OI:oi_by_strike]; "hedged-bearish front, structurally-bullish back" is a two-sided book. |
| 4 — structure | − (−7) | Short gamma across 44–59 (total_gex −$64,788,860; 54 = −$30.7M) with net DEX −$253.6M sell-hedge [STRUCT:gex/dex] — amplification fights a range/pin thesis until spot ≥55–60; the max-pain 55 magnet [STRUCT:max_pain] only partially offsets. |
| 5 — historical | − (−7) | bearish_flow class backtest 87.5% win / avg −2.73% over 5d [HIST:signal_backtest] implies directional follow-through, and RV30 113.7% > IV30 109.0% [HIST:vrp] means the tape has been breaking priced ranges for a month. |
| 6 — macro | − (−7) | Net HEADWIND 4/5: BTC ≈$60k −18% w/w (primary driver, unresolved) [MACRO:BTC_2026-06-05], CPI re-accelerating, two binaries (06/10, 06/16-17) inside the window — argues trend, not stabilization. (The regime engine's own "iron condors in range" guidance supports the *structure*, not the stabilization odds.) |
| 7 — insights | + (+7) | The composite literally reads no-direction: conviction-matrix "MIXED" at confidence_pct 4.4, signal-confluence ≤2/6 both ways, institutional-accumulation "NEUTRAL" (1.19) [INSIGHT:*] — range-aligned. |
| 7b — fundamentals | + (+7) | fundamental_signal NEUTRAL, verbatim verdict "two-sided chop with a quality floor" (rev +97.29% TTM vs two straight misses) [FUND:*]. (Gate effect — CAUTION — was applied in sizing, not here.) |
| 8 — agents | +8 (4/4 align ±2) | contrarian-scanner RANGE (+2); accumulation-hunter, sweep-tracker, risk-monitor NEUTRAL with the identical 50/60 map and explicit no-directional verdicts (+2 each). earnings-scout skipped (0). |

**Raw score (symmetric):** +7+7+7−7−7−7+7+7 = **+14** (phases) + **+8** (agents) = **+22**
**Base score:** round((22+130)/260×100) = **58**/100
**Gate penalties (one-sided):** −5 phase-8b disconfirmed (bull_residual 0.65 vs bear_residual 0.65 — tie → attacker) · −5 phase-7c CAUTION (CROWDED_SHORT front-week + contrary analyst momentum)
**Confluence_score:** **48**/100
**Recommended bin:** 0.55 (band 30–49 → 0.55–0.65; phase-8b down-shift selects 0.55)
**Phase-9 actual bin:** 0.55 — **MATCH**

## Contradictions

- **phase-4 (structure):** Short-gamma amplification (44–59 pit, −$64.8M)
  directly fights the range/pin thesis the plan trades — the debate's
  strongest_bear_point came from here. *Resolution applied:* tightened
  invalidation (two closes <50 / one close >62 — both walls are exits, not
  averaging zones) and entries placed only at the box edges, never at spot.
- **phase-5 (historical):** bearish_flow 87.5%/−2.73% 5d class edge + RV>IV
  argue downside follow-through against range-hold. *Resolution applied:*
  conviction kept at the bottom bin (0.55) and the directional structure
  expresses the bearish tilt (55/50 put spread on a 60-rejection), so the
  class edge is traded WITH, not against; signal-invalidation includes the
  3-session cumulative-flow trigger.
- **phase-6 (macro):** BTC-transmitted headwind + two in-window binaries
  contradict stabilization. *Resolution applied:* macro invalidation hinges
  on hard BTC levels ($56k/$65k) and the CPI core >0.4% trigger; condor is
  closed (not rolled) before FOMC; weekend-gap risk named as key_risk #1.
  Residual: if BTC gaps hard either way Monday, the plan exits — wait-for-
  confirmation is built in via the entry triggers (no fill at spot).

## Citation failures

(none — 3 of 3 spot-checks resolved)

1. `[OI:biggest_increases] 50P 06/12 +29,735, 81% at ask` → phase-3-positioning.md
   §Largest OI increases: row shows oi_diff_plain +29,735, prev_ask_volume
   22,718 vs prev_bid_volume 5,342 → 22,718/28,060 = 81.0% ✓
2. `[STRUCT:gex] total_gex −$64,788,860, flip ~59.5–60` → phase-4-structure.md
   §GEX: total_gex −64,788,860; per-strike 59 = −$1.14M, 60 = +$2.39M (sign
   change) ✓
3. `[FLOW:sweep_persistence] $339,924,997, 5/5 dominant-bullish` →
   phase-1-flow.md §Key signals: sessions_in_top=5, consistency_score=1.0,
   total_sweep_premium=339,924,997 ✓

## Sanity checks

- [✓] All phase files present: 0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, decision.json
  (15 files verified by `ls`)
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (8 in Citations summary,
  spanning OI/STRUCT/FLOW/HIST/MACRO/AGENT/DEBATE)
- [✓] Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- [✓] ≥1 directional (55/50 put debit spread 06/26) + ≥1 defined-risk (iron
  condor 45/50/60/65 06/18)
- [✓] Sizing math shown; Kelly p from phase-5 backtest (p_raw 0.875, n=8 →
  N-cap 0.75), not the bin
- [✓] All five risk gates evaluated: 7b CAUTION (cut), 7c CAUTION (cut),
  correlation soft-watch (no cut, surfaced), rotation adverse-to-bullish (no
  cut vs RANGE bias, surfaced), 8b disconfirmed (bin down-shift + cut);
  phase-0.5 GENUINELY_UNUSUAL reflected (no-op, stated)
- [✓] Structures sized to the expected move (`expected_move` block: ±18.3%/
  $9.97 front, ±22.9% to 06/18; condor explicitly framed as walls-hold inside
  1σ with capped max-loss)
- [✓] `decision.json` exists, backfilled (confluence_score 48,
  recommended_bin 0.55, paths.audit), `validate_decision.py` → **OK**
  (includes `context`, `expected_move`, `gates.sentiment`)

## Final auditor note

The run is internally consistent and ready for action at the stated size: a
genuinely mixed book (two-sided flow, neutral composite, quality floor)
fighting a one-directional macro driver, correctly resolved into a
bottom-bin, defined-risk, edges-only range plan at 0.6% with three gates
fired and honest invalidation on both walls. The one structural tension the
desk must respect — short gamma + RV>IV + weekend BTC risk against any
stabilization bet — is documented in all three `-` phases and carried into
key_risks; no revision of phase-9 required, but the Monday 06/08 checks
(LEAP-selling recurrence, Jan-27 OI resolution, BTC level) are load-bearing
and should be run before any fill.
