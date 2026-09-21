# Phase 10 — Audit & Confidence Score

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T02:45:00-04:00
**Upstream phases audited:** phase-0 through phase-9
**Dominant bias under audit (phase-9):** LONG (buy-the-dip), conviction
0.65, horizon 1-4w

## Summary

Confluence score **63 / 100**, which maps to recommended conviction
bin **0.65** per `rubrics/confluence-scoring.md` — **EXACT MATCH** with
phase-9's chosen bin. The run is **internally consistent**: 3 strongly-
positive phases (FLOW, DP, STRUCT) and a positive INSIGHT/OI partial
are offset by **2 contradicting phases** (HIST -- and MACRO -) and a
**dead-tied agent panel** (1 LONG / 1 SHORT / 2 NEUTRAL = 0 net).
Both contradictions are **already structurally mitigated in phase-9**:
the HIST `bullish_flow` 0% backtest is reflected in the half-Kelly
sizing (2.5% vs 5% cap); the MACRO TRANSITIONAL regime is reflected
in the defined-risk-only structure choice and macro-based invalidation
triggers. **Three of three citation spot-checks resolved.** No sanity
failures. Recommended action: **proceed with phase-9 as written.**

## Confluence scorecard

| # | Phase | Score | Justification (cited datapoint) |
|---|-------|-------|----------------------------------|
| 1 | flow | **++** | "RDDT consistency_score 1.0, 5/5 sessions, $24.91M bullish sweep premium" [FLOW:hot_chains_sweep_persistence] — phase-1 §Sweep persistence (5-session) |
| 2 | dark pool | **++** | "block-tier buy_ratio 0.793 on $26.26M premium, 14 trades; post-close 6,468-share print at $159.11 vs NBBO mid $157.75 (+$1.36)" [DP:block_stratified, DP:dark_pool_extended_hours] — phase-2 §Tier breakdown + §Largest blocks |
| 3 | OI positioning | **+** | "5/22 160C OI 2,300→3,592 (+1,292), 6/18 160C OI 1,050→1,693 (+643)" [OI:biggest_increases] — phase-3 §Largest OI increases. Score `+` rather than `++` because only 4 contracts cleared the +500 threshold and the 6/18 160C carries a covered-call (bearish) net_ask_bid signature (-787) |
| 4 | structure | **+** | "total GEX +$1.261B, $160 wall +$622.7M (49% of chain), ZGL $158.39 vs spot $158.89" [STRUCT:gex] — phase-4 §GEX. Score `+` not `++` because spot was only $0.50 above ZGL and the regime had flipped POS→NEG by 2026-05-19 per [HIST:gex_time_series] |
| 5 | historical | **−−** | "`bullish_flow` 5d backtest win_rate 0.0%, avg_move −3.05%, n=7 across MSFT/AAPL/UPS/QQQ/SMH/META/AVGO; RDDT own 5/19 close $154.91 (−2.64%)" [HIST:signal_backtest, HIST:historical_trend] — phase-5 §Signal backtest. Strongly contradicts the LONG bias: the exact signature firing in phases 1-4 has been a contrarian indicator this week, and the next-day reality check on the anchored data shows the thesis already being tested |
| 6 | macro | **−** | "Market regime TRANSITIONAL + Comm Services -$20.5M outflow + Tech -$299.8M outflow on 2026-05-18" [MACRO:MarketRegime_2026-05-18] — phase-6 §Market regime + §Sector rotation. Mildly contradicts: sector tape is bleeding even though SPY index is intact, but the idiosyncratic Q1 beat partially offsets so `-` rather than `--` |
| 7 | insights | **+** | "DIRECTIONAL_LONG scenario, confidence 22.25%; signal_confluence score 5/6 with factors {bullish_flow, low_pcr, dp_accumulation, oi_building, low_iv_cheap_options}" [INSIGHT:conviction_matrix, INSIGHT:signal_confluence] — phase-7. Label is bullish but model self-reports only 22% confidence, so `+` rather than `++` |
| 8 | agents | **0 (split panel)** | LONG = accumulation-hunter (+2), SHORT = contrarian-scanner (−2), NEUTRAL = sweep-tracker (0), NEUTRAL = risk-monitor (0); earnings-scout MISSING (skipped per spec). Net = **0**. |

**Raw score:**
```
+15 (phase 1, ++)
+15 (phase 2, ++)
 +7 (phase 3, +)
 +7 (phase 4, +)
−15 (phase 5, −−)
 −7 (phase 6, −)
 +7 (phase 7, +)
  0 (phase 8, split panel)
─────
 +29
```

**Confluence_score:** `round((29 + 115) / 230 × 100)` = `round(62.6)` =
**63 / 100**

| Score band | Recommended conviction bin |
|------------|----------------------------|
| 0–29 | 0.55 |
| 30–49 | 0.55–0.65 |
| **50–64** | **0.65** ← lands here |
| 65–79 | 0.75 |
| 80–89 | 0.85 |
| 90–100 | 0.95 |

**Recommended bin:** **0.65**
**Phase-9 actual bin:** **0.65**
**Match:** ✓ **MATCH**

## Contradictions

- **phase-5 (historical) [SCORE −−]:** `historical_signal_backtest`
  bullish_flow returns 0.0% win rate / −3.05% avg 5d move across the 7
  most recent tape-wide signals, and RDDT's own next-session
  (2026-05-19) printed −2.64% with `historical_gex_time_series` flipping
  POSITIVE → NEGATIVE. The bullish-flow signature firing in phases 1-4
  has been a contrarian fade in the current regime. **Suggested
  resolution applied in phase-9:** (a) downgrade conviction (chose
  0.65 bin not 0.75 despite phases 1+2+4+7 all supportive); (b) tighten
  invalidation (hard stop at $154 with secondary at $150); (c) wait for
  confirmation at entry ($154 retest required — no chase). All three
  resolutions are present.

- **phase-6 (macro) [SCORE −]:** UW `risk_market_regime` returns
  TRANSITIONAL with prescriptive guidance "Reduce position size, favor
  defined-risk strategies"; Communication Services net outflow −$20.5M
  and Technology net outflow −$299.8M on 2026-05-18 confirm a sector
  rotation AWAY from RDDT's neighborhood. **Suggested resolution
  applied in phase-9:** (a) downgrade sizing (chose 2.5% of book risk
  vs 5% Kelly cap, explicit deviation_reason cited); (b) added
  macro-based invalidation (regime flip to RISK-OFF triggers exit;
  Comm Services outflow > $50M for 2 days triggers escalation;
  hawkish FOMC on 6/16-17 triggers structure roll). Resolutions are
  present.

Both contradictions are accounted for in phase-9's structure design.
No further down-shift required.

## Citation failures

Spot-check of 3 citations from phase-9's thesis paragraph:

1. ✓ **[DP:block_stratified] "buy_ratio 0.793 on $26.26M single-session"**
   → `grep block phase-2-dark-pool.md`: "block (≥$1M) | 14 | **$26.257M**
   | 131,141 | 34,193 | **0.793**". **RESOLVES.**

2. ✓ **[HIST:signal_backtest] "0% 5-day win rate"**
   → `grep signal_backtest phase-5-historical.md`: "win 0%, avg
   -3.05% (n=7)" + table with MSFT/AAPL/UPS/QQQ/SMH/META/AVGO + final
   line "**win_rate** | | | | **0.0%**". **RESOLVES.**

3. ✓ **[MACRO:MarketRegime_2026-05-18] "TRANSITIONAL + Comm Services
   -$20.5M sector outflow"**
   → `grep TRANSITIONAL phase-6-macro.md`: "regime | **TRANSITIONAL —
   Mixed signals, reduce position size**" + sector rotation table
   showing "Communication Services | -$20,540,205". **RESOLVES.**

All three resolved. No citation failures.

## Sanity checks

- [x] All `phase-*.md` files present (phase-0 through phase-9 = 10
  files; verified via `ls -la`).
- [x] Phase-9 cites ≥3 distinct upstream datapoints — actually cites
  **6** in §Citations summary.
- [x] Phase-9 conviction bin is in {0.55, 0.65, 0.75, 0.85, 0.95} —
  chose **0.65**.
- [x] Phase-9 has ≥1 directional + ≥1 defined-risk structure — has
  TWO defined-risk structures (7/17 155/175 call debit spread =
  directional defined-risk; 6/18 150/145 put credit spread =
  defined-risk income alternative). Both have explicit
  strike/expiry/debit/credit/breakeven/max-loss.
- [x] Phase-9 sizing math shown explicitly — Kelly formula written
  out with p=0.65, b=3.75, raw_kelly=55.67%, suggested=13.92%, capped
  at 5%, final at 2.5% with deviation_reason cited
  ([MACRO:MarketRegime_2026-05-18] + [HIST:signal_backtest] +
  [AGENT:risk-monitor]).
- [x] Phase-9 disclaimer line present at top.
- [x] Phase-0 documented the as-of-date / data-anchor discrepancy
  (2026-05-20 requested, 2026-05-18 used) in Tool errors section.
- [x] Every phase MD cites at least one prior phase by file path
  (verified by spot-check).
- [x] Citation tags follow `rubrics/citation-conventions.md` taxonomy
  ([FLOW:], [DP:], [OI:], [STRUCT:], [HIST:], [MACRO:], [INSIGHT:],
  [AGENT:]).

All sanity checks pass.

## Final auditor note

The run is **internally consistent and ready for action as written**.
Confluence 63/100 with a 0.65 conviction bin is the correct
calibration for a setup where institutional accumulation is real but
the short-term tape and macro regime are actively fading the same
signature — phase-9's response (half-Kelly sizing, defined-risk
structures, $154 hard stop, buy-the-dip-only entry mandate, monitor
checklist that re-runs the contradicting phases daily) is the
textbook way to express that asymmetry, and the two negative-score
contradictions (phase-5 HIST −−, phase-6 MACRO −) are explicitly
addressed by named mitigations in the trade plan rather than ignored.
