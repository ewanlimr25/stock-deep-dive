# Phase 10 — Audit & Confidence Score

**Ticker:** PATH
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T13:15:00-04:00
**Dominant bias audited:** RANGE ($11–$12 core / $10–$13 outer, into Jun-18 OPEX) — from phase-9-trade-plan.md

## Summary

**Confluence score: 65/100** (base 70, −5 phase-7c CAUTION penalty, −0 debate)
→ **recommended bin 0.75**; phase-9 chose **0.65 — MISMATCH, but covered by a
documented downward `## Conviction deviation`** (conservative deviation is
permitted; upward would not be). **Contradiction count: 1** (phase-7's
composite labels the name DIRECTIONAL_LONG against the RANGE thesis — at
21.4% confidence, its lowest tier). All three spot-checked citations resolve.
All sanity checks pass; `decision.json` backfilled
(confluence_score=65, recommended_bin=0.75) and re-validated `OK`. The run is
internally consistent and ready for action as written.

## Confluence scorecard

Context modifier active: phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` →
phases 1–2 capped at `+`.

| Phase | Score | Justification (quoted datapoint) |
|---|---|---|
| 1 — flow | + (capped) | Two-way equilibrium: derived net_flow **+$55,591 on $4.72M** traded; sweep persistence 5/5 sessions `dominant_direction: "mixed"` [FLOW:insights_deep_dive][FLOW:sweep_persistence] — the tape itself is the range argument. Cap binds (would otherwise lean ++). |
| 2 — dark pool | + (capped) | Floor + ceiling in one phase: large-tier buy_ratio 0.638 absorbing the 11.11–11.14 flush vs **100% of 5-day price memory overhead ($11.83–$12.97, ~$103M)** [DP:block_stratified][DP:price_levels]. |
| 3 — OI | ++ | Verdict verbatim "income positioning inside an expected **$11–$13 range**": put wall $11 (net −12,197), call walls $12/+13,105 and $13/+23,495, Aug $12C +3,379 *written* (net_ask_bid −1,557), Jun-18 $11P 89%-closed [OI:oi_by_strike][OI:smart_positioning][OI:position_rolls]. |
| 4 — structure | ++ | Long-gamma `POSITIVE` (+$4,446,767, ZGL 7.57 ≪ spot) with max-pain magnets **06/12 → $12, 06/18 → $11** and the $12–$13 positive-GEX dampener band [STRUCT:gex][STRUCT:max_pain]. |
| 5 — historical | + | 90d cumulative `MIXED` (−$2,765,415), P/C z −0.072 `NORMAL`, 13/17 day split — equilibrium signatures; cushion decay 28.6M→4.4M [HIST:gex_time_series] keeps this from ++. |
| 6 — macro | 0 | Genuinely two-sided for a RANGE thesis: regime guidance verbatim "Iron condors in range" supports it, while adverse Tech rotation (−$807.6M) + CPI/FOMC binaries are the range-breaker risk [MACRO:MarketRegime_2026-06-05 UW]. |
| 7 — insights | **−** | Composite scenario `DIRECTIONAL_LONG` (conf. 21.4%) + `ACCUMULATION` (1.84) [INSIGHT:conviction_matrix][INSIGHT:institutional_accumulation] — labels a *long*, not a range; mild contradiction despite the bottom-tier confidence. |
| 7b — fundamentals | 0 | `CONFIRM` (0 contradictions) is bullish-for-the-business, directionally agnostic for a 1-4w range; buyback pads the floor, decel-model risk caps the re-rate [FUND:financials_reported]. NA/CONFIRM adds nothing by rule. |
| 8 — agents | +8 (4/4 align) | accumulation-hunter RANGE, contrarian-scanner RANGE, sweep-tracker NEUTRAL, risk-monitor NEUTRAL — all four non-directional with matching $11/$12–13 levels (+2 each); earnings-scout skipped (0) [AGENT:all]. |

**Raw score (symmetric):** 7+7+15+15+7+0−7+0+8 = **52** (range −130…+130)
**Base score:** round((52+130)/260×100) = **70**/100
**Gate penalties (one-sided):** phase-8b disconfirmed = false (bull 0.65 vs
bear 0.55) → −0 · phase-7c `CAUTION` → **−5** · (no 7c VETO)
**Confluence_score:** **65**/100
**Recommended bin:** **0.75** (band 65–79)
**Phase-9 actual bin:** 0.65 — **MISMATCH (downward), documented** in
phase-9 `## Conviction deviation` (7c CAUTION + regime half-size guidance +
unrefuted bear point on the $11 floor). A conservative deviation is
explicitly permitted; the audit accepts it and notes the score sits at the
band's bottom edge (65) — one point lower and the bins would match.

## Contradictions

- **phase-7 (UW insights):** composite labels PATH `DIRECTIONAL_LONG` +
  `ACCUMULATION` while the run's thesis is RANGE — the label is the bullish
  NBBO reading of prints phase-2 scored mixed (0.638 suggestive), at the
  matrix's lowest confidence tier (21.4%). **Resolution: wait for
  confirmation** — phase-9 already encodes it: the $12.20 volume-reclaim
  trigger converts this contradiction into the Plan B call spread, and the
  monitoring checklist watches the Sep $10C/$15C OI conversion that would
  upgrade the long case. No conviction change required beyond the downward
  deviation phase-9 already took.

## Citation failures

None. Spot-checked 3 of 6:
1. `[OI:oi_by_strike] put wall $11 net_oi −12,197` → phase-3-positioning.md
   §Tradeable-horizon walls, row "11 | 5,715 | 17,912 | −12,197" ✓
2. `[STRUCT:max_pain] 06/18 → 11.0 (dist −2.09%, P/C 0.356)` →
   phase-4-structure.md §Max pain table, row "2026-06-18 | 11.0 | −2.09 |
   0.356" ✓
3. `[HIST:signal_backtest] bullish_flow win_rate 0.0%, total_signals 8` →
   phase-5-historical.md §Signal backtest ("win_rate 0.0% · total_signals
   8") ✓

## Sanity checks

- ✓ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9 +
  decision.json (ls verified; 15 files)
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (6 listed, spanning
  OI/STRUCT/HIST/MACRO/AGENT/SENT)
- ✓ Conviction bin 0.65 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}
- ✓ ≥1 directional (Sep 10/15 call debit spread, conditional) + ≥1
  defined-risk (Jun-18 9/10P–13/14C iron condor)
- ✓ Sizing math explicit: p_raw 0.00 (backtest, n=8) → N-cap (<10 → 0.75) →
  p = 0.00 → raw_kelly −0.40 → directional 0% (negative-edge rule applied;
  no bin fallback since win_rate_source=backtest)
- ✓ All five risk gates evaluated in phase-9 sizing block (7b CONFIRM no-op /
  7c CAUTION cut / correlation none / rotation adverse cut / debate no-cut)
  and phase-0.5 `BUSY_NAME_NORMAL_DAY` reflected (no top-of-band)
- ✓ Structures sized to expected move: `expected_move` block in JSON
  (±2.238% / $0.252); FOMC gap of priced magnitude does not breach condor
  short strikes; Sep spread spans earnings with capped vega
- ✓ `decision.json` exists, backfilled (confluence_score 65, recommended_bin
  0.75, paths.audit set) and `validate_decision.py` → `OK` (context /
  expected_move / gates.sentiment fields present)

## Audit-trail observations (non-blocking)

- Three first-pass jq shape misses (hot-chains `option_symbol`,
  term-structure `.term_structure[]`, GEX `net_gex`) were each corrected
  before any value was transcribed — recorded in the respective phase DATA
  NOTEs; no fabrication surface.
- Phase-7c overturned phase-1's HTB hypothesis for the deep-ITM prints
  (borrow EASY 0.29%) — correction logged in 7c; classification change only,
  no number affected.
- Trailing-tool anchor risk is nil this run (latest available date = as-of),
  but `sweep-persistence` ran without `--date` (flag unsupported) — flagged
  in phase-1 for calibration reproducibility.

## Final auditor note

The run is internally consistent: nine scored phases produce a 65/100
confluence for RANGE with a single, well-understood contradiction (the UW
composite's low-confidence long label), and phase-9's only deviation is
conservative and documented. Blueprint is ready for action as written — the
0% directional book, gated 0.5% condor budget, and pre-armed $12.20 squeeze
plan correctly express a 65-score range thesis with a soft floor into two
macro binaries.
