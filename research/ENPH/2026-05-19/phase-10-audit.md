# Phase 10 — Audit & Confidence Score

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW data 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-0 through phase-9 (full chain)

## Summary

The run is **internally consistent in its signal stack but has one
methodological mismatch the auditor must call out**. Raw confluence score
**+53** maps to a normalized **confluence_score = 73 / 100**, which per
`rubrics/confluence-scoring.md` falls in the **65–79 band → recommended
conviction bin 0.75**. **Phase-9 chose 0.65** on the basis of phase-8's
2-2-1 plurality split (genuinely MIXED desk), without writing a
`## Conviction deviation` section as the rubric requires for departures
from the band. The deviation is **downward and conservative** so it is
acceptable per the sizing rubric's general posture (smaller is always
allowed without justification), but a strict reading of `rubrics/
confluence-scoring.md` line 38–43 (the score → bin table) would call
this a **MISMATCH**. **Two phases score `−` (mildly contradictory)**:
phase-5 (cohort backtest 14.3% win rate) and phase-6 (TRANSITIONAL macro
+ Tech sector outflow). Both are explicitly factored into phase-9's
sizing downscale (Kelly 5.0% → practical 3.5%) and the choice to deploy
defined-risk iron condor alongside the directional call spread.
**Citation spot-check: 3 of 3 cited datapoints in phase-9's thesis
resolve cleanly to upstream phase files. No citation failures.**

## Confluence scorecard

Per `rubrics/confluence-scoring.md` scoring axes
(`++` +15 / `+` +7 / `0` 0 / `−` −7 / `−−` −15) vs the **dominant
phase-9 bias LONG (0.65 conviction)**:

| Phase | Score | Justification (datapoint quoted) |
|-------|-------|------------------------------------|
| 1 — flow | **++** | "5/5 bullish sweep persistence, $55,813,662 cumulative premium, consistency_score 1.00" [FLOW:hot_chains_sweep_persistence] + $14.8M Jun-2027 $70C combo leg [FLOW:top_premium_trades] = strongest possible persistence print. |
| 2 — dark pool | **++** | "Large-tier buy_ratio **0.634** on $100,009,416 premium across 549 trades" [DP:block_stratified]; "9 of top 12 single blocks trade above NBBO mid (buy-aggressor)" [DP:largest]. |
| 3 — OI | **++** | "Jun-2026 $50 call OI **+4,985 to 26,273** (most-owned strike on chain), ask-vol 9,652 vs bid-vol 6,374, net_ask_bid +3,278 bullish" [OI:biggest_increases][OI:smart_positioning]; "11 of 13 top-OI-Δ contracts inferred bullish." |
| 4 — structure | **++** | "$50 strike net_gex **+$2,782,892,560** (largest gamma wall on chain); total GEX +$4.42B, ZGL $15.01, regime POSITIVE; DEX +$92.3B call-heavy → dealers BUY underlying on rallies" [STRUCT:gex][STRUCT:dex]. |
| 5 — historical | **−** | "historical_signal_backtest(bullish_flow, 20d): cohort win_rate **14.3%** (2 of 14) / avg_move **−2.18%**" [HIST:signal_backtest] — direct disconfirmer of naked-long sizing despite same-day signal alignment. |
| 6 — macro | **−** | "UW regime **TRANSITIONAL** — 'half size, defined-risk'" + "Technology sector **−$151,018,206 outflow**" [MACRO:MarketRegime_2026-05-15 UW][MACRO:SectorRotation_2026-05-15 UW] + "residential ITC expired 2025-12-31" [MACRO:OBBBA_2025-07-04 WebSearch:arnoldporter.com] — sector drag + structural residential headwind. |
| 7 — insights | **+** | "Signal confluence **5/6**, scenario **DIRECTIONAL_LONG**, institutional_accumulation buy/sell ratio **1.71×**" [INSIGHT:signal_confluence][INSIGHT:conviction_matrix][INSIGHT:institutional_accumulation] — strong bullish baseline; **NOT** `++` because confidence_pct only 18.4%. |
| 8 — agents | **0** | 2 LONG (`accumulation-hunter`, `sweep-tracker`) ×+2 = +4; 2 SHORT (`contrarian-scanner`, `earnings-scout`) ×−2 = −4; 1 NEUTRAL (`risk-monitor`) ×0 = 0. **Sum = 0**. |

### Raw score math

| Component | Value |
|---|---|
| Phase 1 | +15 |
| Phase 2 | +15 |
| Phase 3 | +15 |
| Phase 4 | +15 |
| Phase 5 | −7 |
| Phase 6 | −7 |
| Phase 7 | +7 |
| Phase 8 | 0 |
| **Raw score** | **+53** |

### Normalized confluence score

```
confluence_score = round( (raw_score + 115) / 230 * 100 )
                 = round( (53 + 115) / 230 * 100 )
                 = round( 168 / 230 * 100 )
                 = round( 73.04 )
                 = 73
```

**Confluence_score: 73 / 100.**

### Band mapping (per rubric)

| Score band | Recommended conviction bin |
|------------|----------------------------|
| 0–29 | 0.55 — or revisit |
| 30–49 | 0.55–0.65 |
| 50–64 | 0.65 |
| **65–79** | **0.75** |
| 80–89 | 0.85 |
| 90–100 | 0.95 |

- **Recommended bin:** **0.75**
- **Phase-9 actual bin:** **0.65**
- **Match status:** **MISMATCH** (downward, by one bin)

Phase-9's stated rationale (quoted verbatim): *"Phase-8 desk is split
2 LONG / 2 SHORT (vol-short) / 1 NEUTRAL with avg conviction 3.6 →
MIXED setup → rubric band 0.55–0.65; the ENPH-specific accumulation
stack is qualitatively stronger than the failed megacap cohort,
justifying the upper end of the MIXED band rather than 0.55."*

**Auditor read:** the deviation is **defensible and conservative**, but
strict interpretation of `rubrics/confluence-scoring.md` (which maps
*score* → *bin*, NOT *plurality* → *bin*) requires either:
1. Phase-9 use **0.75** (and reflect the desk split via the sizing
   downscale only), or
2. Phase-9 add an explicit `## Conviction deviation` section justifying
   the move to 0.65.

Phase-9 has a sizing-deviation note (5% → 3.5%) but **no formal
conviction-deviation note**. **Recommendation:** add a one-paragraph
`## Conviction deviation` block to phase-9 (or, in a re-run, reconcile to
0.75 and run a slightly larger sizing target). For this run, the auditor
accepts the deviation as documented in this audit.

## Contradictions

- **phase-5 (historical context):** `historical_signal_backtest` shows
  **14.3% win rate / −2.18% avg over 20d** for the bullish_flow cohort
  (megacap-tech basket: QQQ, SMH, META, AVGO, TSLA, NVDA, GOOGL, QCOM,
  CNC, AAPL, UNH) — direct base-rate disconfirmer of any naked-long
  ENPH structure in this regime.
  **→ Resolution: TIGHTEN INVALIDATION + DOWNGRADE SIZE.** Phase-9
  applies both: tranche-exit on two-day close < $48 (tighter than the
  rubric's tightest), and voluntary sizing downscale to 3.5% (vs Kelly
  5.0% cap). **Already applied.**

- **phase-6 (macro overlay):** UW regime **TRANSITIONAL** with own
  guidance "half size, defined-risk"; **Technology sector −$151M
  outflow** on 2026-05-15; **breadth only 35.9% bullish** — sector and
  regime drag.
  **→ Resolution: DEFINED-RISK STRUCTURES.** Phase-9 deploys both a
  call SPREAD (not naked calls) and an iron CONDOR (not short straddle),
  capping max loss in both structures. **Already applied.**

## Citation failures

Spot-check of 3 citations from phase-9's thesis paragraph:

1. **[DP:block_stratified]** "Large-tier buy_ratio 0.634 on $100M premium
   across 549 trades."
   - **Resolves to:** phase-2-dark-pool.md §"Tier breakdown" table:
     `large | 549 | $100,009,416 | 1,229,409 | 708,432 | 0.634`.
   - **Match: ✓**

2. **[FLOW:hot_chains_sweep_persistence]** "5-of-5 bullish sweep
   persistence with $55.8M cumulative premium."
   - **Resolves to:** phase-1-flow.md §"Sweep persistence (5-day)" table:
     `sessions_in_top: 5 of 5`, `total_sweep_premium (5d): $55,813,662`,
     `dominant_direction: bullish`, `consistency_score: 1.00`.
   - **Match: ✓**

3. **[STRUCT:gex]** "$50 wall worth +$2.78B in net GEX."
   - **Resolves to:** phase-4-structure.md §"GEX (total + per-strike top
     10 + zero gamma level)" table: `50 | +2,782,892,560 | Dominant
     call-wall / support pivot`.
   - **Match: ✓**

**All 3 citations resolve. No citation failures.**

## Sanity checks

- [✓] **All `phase-*.md` files present** in
  `/Users/ewan/Development/stock-deep-dive/research/ENPH/2026-05-19/`:
  phase-0 (2,112 B), phase-1 (11,965 B), phase-2 (8,790 B), phase-3
  (10,180 B), phase-4 (12,505 B), phase-5 (14,121 B), phase-6 (14,968 B),
  phase-7 (12,723 B), phase-8 (10,241 B), phase-9 (16,198 B). After this
  write, phase-10 will also be present.
- [✓] **Phase-9 cites ≥3 distinct upstream datapoints** in the thesis:
  6 distinct citations listed (DP buy_ratio, sweep persistence, $50C OI
  Δ, $50 GEX wall, OBBBA policy, cohort backtest disconfirmer).
- [✓] **Conviction bin is in {0.55, 0.65, 0.75, 0.85, 0.95}**: 0.65 ✓
  (but **MISMATCHED** with rubric recommended 0.75 — see § band mapping
  above).
- [✓] **≥1 directional + ≥1 defined-risk structure present**:
  - Directional: Long Call Spread Jul-17 $50/$55, debit ~$3.10.
  - Defined-risk: Iron Condor Jun-18 $48P/$45P/$58C/$63C, credit ~$1.05.
- [✓] **Sizing math shown explicitly**: Kelly inputs (p=0.65, b=1.857),
  raw_kelly 46.16%, ×0.25 fraction = 11.54%, capped at 5%, **with
  voluntary downscale to 3.5% practical deploy and explicit
  sizing_deviation_reason (downward) referencing phase-5 backtest + UW
  TRANSITIONAL guidance**.
- [✓] **Disclaimer present** at top of phase-9: "For research and
  educational use only. Not financial advice. Sizing and structures are
  illustrative."

## Final auditor note

The run is **internally consistent** on the signal stack: 4 phases score
`++` bullish (1, 2, 3, 4), 1 scores `+` (7), 2 score `−` (5, 6, both
properly factored into phase-9's defensive structure choice), and phase-8
nets to 0 (genuinely split desk). The single material discrepancy is the
**0.65 vs 0.75 conviction bin mismatch**: phase-9 used phase-8's
plurality split (MIXED) to anchor the bin, while the rubric scores raw
confluence and would put this at 0.75. The deviation is downward and
conservative, so it does not break the trade — but **phase-9 should
either** (a) add a `## Conviction deviation` section to formally document
the choice **or** (b) lift conviction to 0.75 in a re-run and reflect
desk uncertainty through sizing only. **The trade plan as written is
ready for action with the auditor caveat documented here**; the
defined-risk structures and tranche-exit invalidation provide enough
margin of safety that the 0.65 vs 0.75 bin difference does not
materially change the deploy.
