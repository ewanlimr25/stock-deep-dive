# Phase 10 — Audit & Confidence Score

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:37:27-0400
**Dominant bias audited:** SHORT (tactical range-fade, watch-only directional)

## Summary

**Confluence score: 55 / 100** (perfectly-mixed is 50). **Recommended bin (band 50–64):
0.65; phase-9 actual: 0.55** — the gap is intentional and correct: phase-9 applied the
**phase-8b disconfirmation gate** (one-bin down-shift) on top of the band. The run is
**internally consistent**: a genuine, multi-lane *near-term bearish* read (flow + OI +
insights + macro) sits against a single, decisive **fundamental VETO (phase-7b, −−)** —
and phase-9 resolved that tension honestly by reducing the directional short to
**watch-only** and permitting only **small defined-risk carry structures** that expire
before the Jul-23 earnings binary. **One contradiction logged (7b VETO)**, all three
spot-checked citations resolve, and `decision.json` validates. **No revision required.**

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | 5/5-session bearish sweep persistence, consistency 1.0, $925.2M `[FLOW:sweep_persistence]`; net_flow −$50.9M — but magnitude is financing-obscured (deep-ITM delta-one), a direction-not-volume signal → mild, not strong. |
| 2 — dark pool | **0** | Continuous LARGE tier balanced 51.9% buy ($2,083.6M/11,191) and the MEGA all-buy is a Russell-rebalance artifact `[DP:block_stratified]` — mechanically neutral, neither confirms nor refutes. |
| 3 — OI positioning | **++** | New OI ~73% bearish (32,299 vs 12,250); Jul-17 $130 put **+11,442 (ratio 4.11)** while 12 call strikes shed −9,237 `[OI:smart_positioning][OI:biggest_increases]` — cleanest, structural (not financing) bearish read. |
| 4 — structure | **0** | Genuinely double-edged: max-pain pulls down ($120–125) `[STRUCT:max_pain]` but the LONG-GAMMA regime (ZGL $27.26, GEX +30.4M) actively resists the move `[STRUCT:gex]` — net mixed. |
| 5 — historical | **+** | `bearish_flow` backtest win_rate 66.7% (n=9) `[HIST:signal_backtest]`, price extended +247.75% YTD into a fade — but counter-trend, premium-selling, small N → mild. |
| 6 — macro | **+** | Technology = #1 directional outflow −$637.8M `[MACRO:sector_rotation]`, hawkish Fed + CPI 4.27% — supports the short, but sector-wide (not idiosyncratic) with an AI-boom counter-tail. |
| 7 — insights | **+** | price-vs-flow **DIVERGENCE** (price +10.7% vs flow −$50.9M) + COVERED_CALL conviction-matrix `[INSIGHT:price_vs_flow][INSIGHT:conviction_matrix]` — bearish, with the ACCUMULATION false-positive correctly discarded. |
| 7b — fundamentals | **−−** (VETO) | **FUNDAMENTAL VETO**: 4/4 EPS beats, +45.76% fwd EPS, insiders net-buying `[FUND:earnings_surprise][FUND:mspr_2026-05]` contradict the short on 2 axes → naked directional short vetoed to watch-only. |
| 8 — agents | **+ (5/5 align)** | 4 SHORT + 1 RANGE-bearish, avg conviction 2.2 → +2 ×5 = +10. |

**Phase-0.5 context modifier:** `unusual_verdict = GENUINELY_UNUSUAL` → no cap on phases
1–2 (the bearish edge is genuine cross-sectionally and self-relative).

- **Raw score (symmetric):** +7 +0 +15 +0 +7 +7 +7 −15 +10 = **+38**
- **Base score:** round((38 + 130)/260 × 100) = **65 / 100**
- **Debate penalty (phase-8b):** **−5** (DISCONFIRMED — bull_residual 0.65 vs bear_residual 0.65; attacker ≥ defender)
- **Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
- **Confluence_score:** 65 − 5 − 5 = **55 / 100**
- **Recommended bin (band 50–64):** **0.65**
- **Phase-9 actual bin:** **0.55** → **MISMATCH (intentional, downward)** — phase-9 applied
  the phase-8b one-bin down-shift (sizing-rubric gate 5) on top of the band. A *more
  conservative* bin than the band is always permitted; not a deviation requiring
  justification.

## Contradictions

- **phase-7b (fundamentals): −− VETO** — the underlying business is *improving* (4/4 EPS
  beats, +45.76% fwd EPS growth, insiders net-buying) while the flow says short; this
  directly contradicts a directional SHORT. **Resolution (already applied in phase-9):**
  directional size → **watch-only / 0%**; express only as **small defined-risk carry**
  spreads; **hard-exit before Jul-23 earnings**; carry the strongest_bear_point (the
  "flow is hedging, not shorting" + V-bounce demand) in the invalidation block.

(Phases 2 and 4 scored `0` — genuinely mixed, not contradictions.)

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[INSIGHT:price_vs_flow]` — "price +10.7% but flow bearish (net −$50.9M)" → **resolves**
   in phase-7-insights.md §Price vs flow. ✓
2. `[OI:biggest_increases]` — "PUT 130 Jul-17 +11,442 OI, ratio 4.11" → **resolves** in
   phase-3-positioning.md §Largest OI increases. ✓
3. `[FUND:peer_pe fz]` — "only loss-maker in peer group, +247.75% YTD, 29–33% above
   analyst targets" → **resolves** in phase-7b-fundamentals.md §Valuation. ✓

## Sanity checks

- [✓] All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, **7b**, **7c**, 8, **8b**, 9, 10.
- [✓] Phase-9 thesis cites **5** distinct upstream datapoints (≥3).
- [✓] Conviction bin **0.55** ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- [✓] **1 directional** (bear put debit spread 128/120) + **1 defined-risk** (bear call
  credit spread 135/140) — both expire Jul-17, before earnings.
- [✓] Sizing math shown; Kelly **p = 0.667** = phase-5 `signal_backtest_win_rate`
  (n=9, capped 0.75) — not the conviction bin.
- [✓] **All five risk gates** evaluated: fundamentals **VETO**, sentiment **CAUTION**,
  correlation **none** (INTC-only blueprint; MU ρ0.954 soft-watch), rotation **aligned**,
  debate **disconfirmed**. Phase-0.5 `GENUINELY_UNUSUAL` reflected (no top-of-band size;
  noted the unusualness is direction/premium not volume).
- [✓] Structures sized inside the **±22% Jul-17 expected move** (`expected_move` in JSON);
  target $120 (−6.5%) is conservative vs the priced move; neither structure straddles the
  Jul-23 earnings gap.
- [✓] `decision.json` exists and **passes `validate_decision.py`** (incl. `context`,
  `expected_move`, `gates.sentiment`; VETO→final_size_pct 0.0 enforced).

## Final auditor note

The run is **internally consistent and ready for action as written** — a low-conviction
(0.55) tactical bearish *bias* that the chain supports near-term but the fundamentals
**veto** as a directional position, correctly resolved into a **watch-only directional
call plus small, defined-risk, pre-earnings carry spreads** toward the $120 pin. No phase
contradicts another except the deliberate fundamental veto, which phase-9 honored rather
than overrode; **no revision required.**
