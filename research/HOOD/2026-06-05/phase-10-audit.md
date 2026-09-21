# Phase 10 — Audit & Confidence Score

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T14:30:00-04:00
**Upstream phases cited:** all (0 → 9 + decision.json)

## Summary

**Confluence score: 66/100** (base 71 − 5 phase-7c CAUTION penalty; phase-8b
disconfirmed=false adds no penalty). Recommended bin: **0.75**; phase-9 took
**0.65** — a MISMATCH, but a *downward* deviation explicitly documented in
phase-9 §Conviction deviation (split agent desk + 7b VETO), which the rubric
permits. Contradiction count: **1** (phase-7b, the fundamental VETO — capped
at `--` per the hard rule). All sanity checks pass; all spot-checked citations
resolve mechanically (grep-verified). The run is internally consistent: every
composite, agent, and gate that refused to confirm the short was carried into
sizing rather than smoothed over — the blueprint correctly ends at directional
watch-only with a ≤1.25% defined-risk carry.

## Confluence scorecard (dominant bias: SHORT)

| Phase | Score | Justification (quoted datapoint) |
|---|---|---|
| 0.5 — context (modifier) | no cap | `unusual_verdict` GENUINELY_UNUSUAL (direction): net-dir 0.6th universe pctile / 7.7th self pctile `[CTX:universe_pctile DUCKDB]` — phases 1–2 uncapped |
| 1 — flow | **++** (+15) | "5/5 sessions bearish-dominant, consistency 1.0, total_sweep_premium $317,794,122 [FLOW:sweep_persistence]"; both legs aligned ex-0DTE (calls −$11.23M / puts +$3.02M) |
| 2 — dark pool | **0** | block-tier buy_ratio 0.543 / large 0.540 — inside the 0.45–0.55 balanced band; "no distribution signature" = refusal to confirm, not contradiction |
| 3 — OI | **+** (+7) | front-month 87–93 calls written (bid-dominant) + put walls 75/70 held — but Sep 90/95/120C bought ask-side keeps it two-way |
| 4 — structure | **++** (+15) | "regime NEGATIVE … ZGL 87.45 vs spot 81.81" + "Jun-18 max_pain_strike 80, −3.0%, total_oi 391,214 [STRUCT:max_pain]" |
| 5 — historical | **+** (+7) | bearish_flow win_rate 87.5% but N=8 (cap applies); 4/5 sessions bearish (Σ −$39.9M); 90d cum-flow flat −$14.3M tempers |
| 6 — macro | **++** (+15) | "TRANSITIONAL — reduce position size", breadth 29.4%, VIX 21.51, hike repricing, Tech-cohort outflow −$807.6M — aligned on every axis |
| 7 — insights | **+** (+7) | flow bearish & no divergence, but conviction-matrix MIXED @8.4% and no confluence stack — direction confirmed, magnitude refused |
| 7b — fundamentals | **−−** (−15) | **FUNDAMENTAL VETO** (hard-rule cap): 2 of 3 axes contradict the short — Malka ~$36M at 80.39–83.45 [FUND:insider_transactions] + 41.5% rev / 41.1% net margin [FUND:metric] |
| 8 — agents | **+4** | sweep-tracker SHORT +2, risk-monitor SHORT +2, accumulation-hunter NEUTRAL 0, contrarian-scanner NEUTRAL 0, earnings-scout skipped 0 |

**Raw score (symmetric):** 15+0+7+15+7+15+7−15+4 = **+55** (range −130…+130)
**Base score:** round((55+130)/260×100) = **71**/100
**Gate penalties (one-sided):** phase-8b disconfirmed=false (bull_res 0.65 vs
bear_res 0.55) → −0 · phase-7c CAUTION → **−5** · phase-7c VETO n/a → −0
**Confluence_score:** **66/100**
**Recommended bin:** 0.75 (band 65–79)
**Phase-9 actual bin:** 0.65 — **MISMATCH (downward deviation, documented)**:
phase-9 §Conviction deviation cites the 2-SHORT/2-NEUTRAL desk split (phase-8
heuristic: split → 0.55–0.65 + defined-risk) and the 7b VETO. Downward
deviations are permitted without an escape hatch; auditor accepts.

## Contradictions

- **phase-7b (fundamentals): VETO** — the bearish flow thesis runs against an
  improving, hyper-profitable franchise (+41.5% rev TTM, 41.12% net margin)
  whose best-informed insider bought ~$36M open-market inside the trade's
  profit zone (80.39–83.45). **Resolution applied by phase-9 (verified):**
  directional short downgraded to watch-only/0%, carry restricted to
  defined-risk structures ≤1.25% book risk, Malka/SpaceX named in
  invalidation + key_risks, and a monitoring tripwire added (a second
  distinct open-market buyer = exit). This is the textbook VETO handling —
  no further action.

(No other phase scored `-` or `--`. Phase-2's 0 is a genuine neutral, not an
averaged-away conflict — the DP's failure to confirm is priced into the bin
deviation.)

## Citation failures

(none — all six phase-9 citations grep-resolve in their cited files:)

| Citation | Grep target | File | Hits |
|---|---|---|---|
| [FLOW:sweep_persistence] | `317,794,122` | phase-1-flow.md | 2 ✓ |
| [STRUCT:max_pain] | Jun-18 max-pain 80 table row | phase-4-structure.md | 2 ✓ |
| [HIST:signal_backtest] | `87.5%` | phase-5-historical.md | 5 ✓ |
| [MACRO:MarketRegime_2026-06-05 UW] | `TRANSITIONAL` | phase-6-macro.md | 6 ✓ |
| [FUND:insider_transactions] | `80.3944` | phase-7b-fundamentals.md | 1 ✓ |
| [DEBATE:strongest_bear_point] | `strongest_bear_point` | phase-8b-debate.md | 2 ✓ |

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10(this) +
  decision.json (15 artifacts, `ls`-verified)
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (6 listed, spot-checked)
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} (0.65)
- ✓ ≥1 directional (84/80 put debit spread) + ≥1 defined-risk (86/90 call
  credit spread) structure present, strikes anchored to OI walls/max-pain
- ✓ Sizing math shown: p_raw 0.875 → N-cap (n=8<10) → p 0.75; b 1.0; raw
  Kelly 0.50; map ceiling full; Kelly p is the phase-5 win-rate, not the bin
- ✓ All five risk gates evaluated in phase-9: fundamentals VETO (fired),
  sentiment CAUTION (fired), correlation none, rotation aligned, debate
  not-disconfirmed; phase-0.5 `unusual_verdict` reflected (GENUINELY_UNUSUAL
  → no-op, stated)
- ✓ Structures sized to expected move with the implied-vs-realized caveat
  recorded in `expected_move` (0.727% implied vs ±6% realized)
- ✓ `decision.json` exists, backfilled (confluence_score 66, recommended_bin
  0.75, paths.audit) and `validate_decision.py` prints **OK** (incl.
  `context` / `expected_move` / `gates.sentiment`; first validation caught
  the VETO→final_size_pct=0 convention, fixed before backfill)
- ✓ Disclaimer present at top of phase-9

## Final auditor note

The run is internally consistent and ready for action *as written*: a bearish
structural-drift thesis (flow + gamma + OPEX gravity + macro all aligned, 66
confluence) that the fundamental and sentiment gates correctly compress into a
watch-only directional stance with a small defined-risk carry into Jun-18 —
the chain's disagreements (balanced dark pool, MIXED composites, insider
buying) are all visible in the final sizing rather than averaged away. No
revision to phase-9 required; the single watch-item for the desk is the
SpaceX-IPO-access date, which converts the strongest bear point from risk to
realized invalidation the moment it gaps the name above 85.
