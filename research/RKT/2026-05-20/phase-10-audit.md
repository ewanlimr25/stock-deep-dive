# Phase 10 — Audit & Confidence Score

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T02:35:00Z
**Upstream phases cited:** phase-0 through phase-9

## Summary

- **Phase-9 dominant bias being audited:** RANGE-with-long-skew (defined-risk,
  vol-relative, modest long delta into the 5/22 IV dislocation).
- **Confluence score: 59 / 100** → recommended conviction bin per
  `rubrics/confluence-scoring.md` = **0.65**.
- **Phase-9 actual conviction bin: 0.55** → **MISMATCH (one bin
  conservative downward)**. Per `rubrics/sizing-rubric.md`, downward
  deviation is always allowed without explanation; phase-9 explicitly
  notes risk-monitor's 0.5R sizing factor.
- **Contradiction count: 3** (phase-2 dark pool, phase-6 macro,
  phase-7 UW insights). All three are explicitly acknowledged in
  phase-9 and addressed via tight invalidation triggers + reduced
  sizing.
- **Citation spot-check: 3 of 3 resolve.**
- **Sanity checks: all 5 pass.**
- **Run is internally consistent and ready for action** with the stated
  invalidation guards.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** | "RKT 5/5 sessions, consistency_score 1.0, dominant_direction bullish, total_sweep_premium $5,016,354" [FLOW:sweep_persistence]. Supports long-skew direction; full bull score withheld because today's intraday net premium is -$170k (slight bearish flow tilt). |
| 2 — dark pool | **−** | "Mega tier 100% SELL ($60.23M); block tier 89% SELL" [DP:block_stratified]. Direct contradiction of long lean; the dollar-weighted institutional flow is distribution. Mild (not strong) contradict because the large tier (257 trades, $50.5M, 59.3% buy) is net accumulation, partially offsetting. |
| 3 — OI | **++** | "Net direction by OI Δ: Bullish-tagged 8,858 contracts vs Bearish-tagged 3,054 — Bull/bear OI ratio = 2.9×" [OI:smart_positioning]. Strong agreement with long-skew bias; Aug 14C +3,610 BTO + Jan-28 10P SOLD = structural bullish positioning above and floor below. |
| 4 — structure | **++** | "5/22 weekly IV = 85.9% vs 5/29 = 67.6%" [STRUCT:iv_term_structure] + "$13 strike -$292M 0DTE GEX wall + $14 +$289M positive gamma magnet" [STRUCT:today_gamma_flip, STRUCT:gex]. This is the phase that DIRECTLY underwrites the entire phase-9 thesis. |
| 5 — historical | **+** | "IV30 60.1%, 33rd percentile, VRP -4.05% → premium-BUYING regime" [HIST:iv_percentile_zscore, HIST:vrp]. Supports phase-9's debit-structure choice. Limited to mild (not strong) because the bullish_flow signal_backtest shows 10% win rate / -1.57% avg — significant counterweight to direction. |
| 6 — macro | **−** | "30Y mortgage rate 6.58% on 5/20; April CPI +3.8% YoY; Financial Services net flow -$48.79M; TRANSITIONAL regime" [MACRO:Mortgage30Y, MACRO:CPI_2026-04, MACRO:SectorRotation_2026-05-19 UW]. Macro is outright hostile to any RKT long. Phase-9 acknowledges and adapts via half-sizing and explicit macro-based invalidation triggers. |
| 7 — insights | **−−** | "Conviction Matrix: DIRECTIONAL_SHORT at 49.36% confidence; Institutional Accumulation: DISTRIBUTION (b/s 0.32); Price vs Flow: aligned-bearish, -12.28% 30d" [INSIGHT:conviction_matrix, INSIGHT:institutional_accumulation, INSIGHT:price_vs_flow]. UW's composite stack reads RKT as a clean directional short — the strongest contradiction in the chain. |
| 8 — agents | **+6 (4-of-5)** | LONG×1 (sweep-tracker +2), SHORT×1 (accumulation-hunter −2), NEUTRAL×2 (contrarian, risk-monitor +2 each), RANGE×1 (earnings-scout +2). The desk's structural convergence on "defined-risk vol-relative" matches phase-9 [AGENT:earnings-scout, AGENT:risk-monitor]. |

**Raw score:** 7 − 7 + 15 + 15 + 7 − 7 − 15 + 6 = **+21**

**Confluence score:** `(21 + 115) / 230 × 100 = 59.1` → **59 / 100**

**Recommended bin (per `rubrics/confluence-scoring.md` band 50–64):**
**0.65**

**Phase-9 actual bin:** **0.55** (one bin BELOW recommendation)

**Match status:** MISMATCH — downward deviation. Allowed without
explanation per `rubrics/sizing-rubric.md`. Phase-9 nonetheless
explained: "agent risk-monitor mandates 0.5× factor for TRANSITIONAL
regime; bullish_flow backtest at 10% win rate; net defined-risk debit"
— acceptable justification for the conservative bin.

## Contradictions

- **phase-2 (dark pool):** Mega-tier 100% SELL + block-tier 89% SELL
  ($82M aggregate of distribution) directly contradicts a long lean.
  **Suggested resolution:** **tighten invalidation** — phase-9 already
  applies a price-based hard stop at $11.51 (0DTE ZGL) and a
  signal-based stop if mega/block buy_ratio stays below 0.40 for two
  more sessions. ✓ Acceptable. No further action required.

- **phase-6 (macro):** Hostile macro stack — 30Y mortgage 6.58% rising,
  CPI +3.8% surprise, Financial Services -$48.8M flow, TRANSITIONAL
  regime explicitly recommending half-size + defined-risk.
  **Suggested resolution:** **downgrade conviction** AND
  **add macro-based hard stops**. Phase-9 does both: chose bin 0.55
  (one below recommended), and added concrete hard stops at 30Y > 6.75%,
  Brent > $95, FS flow < -$50M for second session. ✓ Acceptable.

- **phase-7 (UW insights):** UW composite Conviction Matrix returns
  DIRECTIONAL_SHORT at 49.36% confidence; Institutional Accumulation
  returns DISTRIBUTION; Price vs Flow shows no divergence (both
  bearish). This is the **strongest single contradiction** in the chain.
  **Suggested resolution:** **wait for confirmation** — specifically,
  phase-9 should require either (a) a dark-pool buy_ratio inversion
  above 0.55 OR (b) a sweep_persistence extension to 6/6 sessions OR
  (c) a successful close above $13.20 BEFORE adding to the position
  beyond the initial 2.5% tranche. Phase-9 includes the "ADD trigger"
  conditional in the monitoring checklist. ✓ Acceptable. **However,
  the auditor recommends phase-9 should NOT enter the FULL initial
  size at-market on 5/20 — split the entry: half at-open, half on
  either the $12.52 mega-VWAP touch OR a $13.20 reclaim**, which would
  effectively wait-for-confirmation on the phase-7 contradiction.
  This is a minor refinement, not a blocking issue.

## Citation failures

(none — all three thesis citations resolve)

## Citation spot-check

1. **[STRUCT:iv_term_structure]** — "2026-05-22 weekly IV at 85.9%
   vs 2026-05-29 weekly at 67.6%."
   **Verify location:** `phase-4-structure.md` §IV term structure.
   **Resolves:** ✓ Table row: `2026-05-22 | 3 | 85.9% | 1,209` and
   `2026-05-29 | 10 | 67.6% | 437`.

2. **[STRUCT:today_gamma_flip]** — "$13 strike carries -$292M of 0DTE GEX;
   total 0DTE GEX = -$406M; ZGL 0DTE = $11.51."
   **Verify location:** `phase-4-structure.md` §Today's gamma flip.
   **Resolves:** ✓ Block reads `today_total_gex = -406,545,704; today_zero_gamma = $11.51`
   and the key walls table row `$13.0 | -$291,852,000 | Primary resistance`.

3. **[FLOW:sweep_persistence]** — "RKT 5/5 sessions, consistency 1.0,
   dominant bullish, $5.02M cumulative."
   **Verify location:** `phase-1-flow.md` §Sweep persistence.
   **Resolves:** ✓ Code block reads
   `ticker: RKT / sessions_in_top: 5 / consistency_score: 1.0 /
   dominant_direction: bullish / total_sweep_premium: $5,016,354`.

## Sanity checks

- [x] All `phase-*.md` files present in
      `/Users/ewan/Development/stock-deep-dive/research/RKT/2026-05-20/`
      (phases 0–10 confirmed)
- [x] Phase-9 cites ≥3 distinct upstream datapoints (cited 7 in summary)
- [x] Conviction bin is one of {0.55, 0.65, 0.75, 0.85, 0.95} (0.55 ✓)
- [x] ≥1 directional structure present (6/18 $13/$14 call debit spread)
- [x] ≥1 defined-risk alternative present (5/22 short $14C / 7/17 long
      $13C diagonal)
- [x] Sizing math shown explicitly (Kelly: p=0.55, b=2.33, raw=35.7%,
      suggested=5%, final=2.5%)
- [x] Disclaimer line is present at top of phase-9

## Final auditor note

The run is **internally consistent and ready for action** with three
caveats explicitly handled: (1) the phase-7 UW composite DIRECTIONAL_SHORT
classification is the loudest contradiction and is partially mitigated by
the downward conviction-bin deviation, the half-size sizing, and the
defined-risk-only structure choice; (2) the auditor's only refinement is
to split the entry rather than enter full size at-market on 5/20 — this
respects the "wait for confirmation" resolution to the phase-7
contradiction without forcing a rewrite of phase-9; (3) the 5/22 catalyst
remains unidentified, so the trade is intentionally structured to
survive a binary outcome with defined max loss = $0.30 per spread on the
directional vertical and ~$0.55 per spread on the diagonal.

**Trade blueprint location:**
`/Users/ewan/Development/stock-deep-dive/research/RKT/2026-05-20/phase-9-trade-plan.md`

**Audit verdict:** APPROVED for execution at sizing ≤2.5% of book risk,
with the auditor's split-entry refinement recommended.
