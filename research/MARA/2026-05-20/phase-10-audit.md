# Phase 10 — Audit & Confidence Score

**Ticker:** MARA
**As-of date:** 2026-05-19 EOD (trade 2026-05-20)
**Generated:** 2026-05-20T02:10:00-04:00
**Upstream phases audited:** phase-0 through phase-9

## Summary

**Confluence score: 85/100** — strong positive confluence around the
phase-9 thesis (**RANGE with mild bullish tilt, conviction 0.85**). The
85/100 lands precisely in the 80-89 band of the scoring rubric, which
maps to the **0.85 conviction bin** — **phase-9 is calibrated correctly,
NO mismatch.** Zero contradictions logged: no upstream phase received a
`-` or `--` score against the RANGE bias. All three spot-checked
citations from phase-9's thesis resolve cleanly to the cited phase MDs.
The full 10-phase artifact chain is internally consistent and ready for
action. The downside risks (bullish_flow signal-backtest fade,
BTC-cascade scenario, complacent skew with hidden 6P/Jun-18 hedge) are
**properly absorbed** in phase 9's invalidation block and sizing
deviation rather than producing internal contradictions.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **+** (+7) | "Sweep persistence: MARA 5/5 sessions, $30.15M cumulative; dominant_direction **mixed**" [FLOW:hot_chains_sweep_persistence] — confirms range, mild bullish tilt; phase-9 cites the same mixed/persistent signature |
| 2 — dark pool | **+** (+7) | "Block-tier buy_ratio 0.512 / large-tier 0.497 — **balanced** raw split; 5-day VWAP $12.74 above today's $12.30-$12.44 close" [DP:dark_pool_block_stratified] — gives both ends of the range ($11.75 floor, $13.20-$13.29 ceiling band) |
| 3 — OI positioning | **++** (+15) | "**13C/2026-05-22 OI 48,851** with net ask-bid -2,114 (heavy call write); **14C/2026-05-22 OI 45,322** (-1,753); 12P/5-22 +2,207 with -306 (put-writing)" [OI:oi_biggest_increases] — defines the mechanical $11-$13 range with explicit walls |
| 4 — structure | **++** (+15) | "Total GEX **+$22.6B POSITIVE**; **$13 strike net GEX $12,665,564,779** (largest in chain); ZGL $4.65; $11 strike -$1.16B (negative-GEX flip)" [STRUCT:gex] — single strongest mechanical pillar of the RANGE thesis |
| 5 — historical | **+** (+7) | "IV30 84%, **14.8th percentile**, z-score **-1.30**; VRP +13.8% PREMIUM_SELLING; 22 consecutive POSITIVE-GEX sessions; OI building 14 days; +67% prior rally now consolidating -6.9% off peak" [HIST:iv_percentile_zscore, vrp, gex_time_series, oi_trend, trend] — supports vol-selling vehicle + range geometry; signal_backtest 20% win rate noted as risk but absorbed in sizing |
| 6 — macro | **+** (+7) | "Market regime **TRANSITIONAL**; SPY 9 of 10 last days bearish-flow; Financial Services -$48.8M out; FOMC paused 3.50-3.75%; **MARA Q1 done 2026-05-11**; BTC consolidating $77K below $82K resistance" [MACRO:MarketRegime, FOMC, MARA_Q1, BTC] — mild macro headwind to direction supports range; absence of in-window catalyst supports range; correctly cited in phase-9 sizing deviation |
| 7 — insights | **++** (+15) | "Conviction matrix **MIXED**, confidence **0.13**; institutional_accumulation NEUTRAL (buy/sell 0.99); MARA **absent from both bullish and bearish** confluence top-100 lists" [INSIGHT:conviction_matrix, institutional_accumulation, signal_confluence] — UW composite says "no directional edge" → matches RANGE thesis exactly |
| 8 — agents | **+8** (4 of 4 aligned × 2 each) | All 4 active sub-agents converged: accumulation-hunter **RANGE**, contrarian-scanner **RANGE**, sweep-tracker **RANGE**, risk-monitor **NEUTRAL** (defensive); zero LONG or SHORT votes; mean conviction 2.75; earnings-scout skipped (next earnings 8/4) [AGENT:accumulation-hunter, contrarian-scanner, sweep-tracker, risk-monitor] |

**Raw score:** 7 + 7 + 15 + 15 + 7 + 7 + 15 + 8 = **+81**

**Max possible:** 7 phases × 15 + 5 agents × 2 = 105 + 10 = 115

**Confluence_score** = round((81 + 115) / 230 × 100) = round(85.22) = **85 / 100**

**Recommended bin per rubric:** **0.85** (the 80-89 band → 0.85)

**Phase-9 actual bin:** **0.85**

**Match status:** ✅ **MATCH — no conviction calibration issue**

## Contradictions

**None.** No upstream phase received a `-` or `--` score against the
phase-9 dominant bias (RANGE). The full confluence chain is unanimously
supportive of the non-directional thesis.

**Watch items (NOT contradictions — properly absorbed):**

- [HIST:signal_backtest] bullish_flow 20% win rate / -2.62% avg 10d
  over last 10 firings. This is a market-wide signal-degradation
  warning, not a MARA-specific contradiction. **Absorbed:** phase-9
  applies it as part of the sizing_deviation_reason (downward to 2.5%
  of book risk, half of the 5% cap).
- [INSIGHT:signal_confluence] MARA absent from both bullish and
  bearish top-100. **Absorbed:** phase-9 reads this as "no directional
  edge" (range-supportive), not as a negative signal against the
  thesis.
- [MACRO:BTC_2026-05-18] BTC bearish MACD at $77K below $82K
  resistance, with $74K downside support critical. **Absorbed:**
  phase-9 names "BTC closes below $74,200 support" as a macro-based
  invalidation condition, with hard-stop exit.
- [STRUCT:vanna_charm] Net vanna -922K means IV crush forces dealer
  selling. **Absorbed:** phase-9 invalidation block lists "daily GEX
  flip to NEGATIVE" as signal invalidation; the optional 6P/2026-06-18
  long-vol hedge addresses tail risk.

## Citation failures

**None.** Spot-checked 3 of phase-9's thesis citations:

1. **[STRUCT:gex] "$12.7B of net dealer GEX" at $13 wall**
   → Resolves to phase-4-structure.md §"GEX per strike (DTE ≤ 45)" line:
   `| 13.0 | **+$12,665,564,779** | Largest gamma wall (resistance + pin magnet) |`
   ✅ **RESOLVES**

2. **[OI:oi_biggest_increases] "48,851 contracts of 13C/5-22 with net
   ask-bid -2,114"**
   → Resolves to phase-3-positioning.md §"Largest OI increases" line:
   `| 13 | call | 2026-05-22 | 3 | +1,212 | 48,851 | -2,114 | bearish (heavy call write) |`
   Also confirmed in phase-3 §"Key signals" bullet.
   ✅ **RESOLVES**

3. **[HIST:iv_percentile_zscore] "IV at the 14.8th percentile (z-score
   -1.30)"**
   → Resolves to phase-5-historical.md §"IV regime + VRP" lines:
   `| 1y percentile | **14.8%** | bottom 15% of 1y range |`
   `| 1y z-score | **-1.30** | 1.3σ below 1y mean |`
   ✅ **RESOLVES**

All 3 spot-checks pass. Phase-9 citation hygiene is clean.

## Sanity checks

- [x] All `phase-*.md` files present in `/Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20/`
  - phase-0-intake.md ✓ (4.3 KB)
  - phase-1-flow.md ✓ (9.4 KB)
  - phase-2-dark-pool.md ✓ (9.2 KB)
  - phase-3-positioning.md ✓ (10.4 KB)
  - phase-4-structure.md ✓ (11.5 KB)
  - phase-5-historical.md ✓ (13.3 KB)
  - phase-6-macro.md ✓ (13.1 KB)
  - phase-7-insights.md ✓ (13.3 KB)
  - phase-8-agent-views.md ✓ (11.3 KB)
  - phase-9-trade-plan.md ✓ (14.7 KB)
  - phase-10-audit.md ✓ (this file)
- [x] Phase-9 cites ≥3 distinct upstream datapoints in thesis (cites **5**:
      [STRUCT:gex], [OI:oi_biggest_increases], [MACRO:MARA_Q1-2026
      WebSearch], [AGENT:*], [HIST:iv_percentile_zscore])
- [x] Phase-9 conviction bin is in {0.55, 0.65, 0.75, 0.85, 0.95} (**0.85**)
- [x] Phase-9 includes ≥1 directional + ≥1 defined-risk structure
  - Directional: Bull put credit spread 11/12 5/22 ✓
  - Defined-risk: Iron condor 11/12/13/13.5 5/22 ✓
  - (Plus optional convexity hedge: long 6P/6-18 ≤0.25%)
- [x] Sizing math shown explicitly (Kelly inputs, raw_kelly, fractional,
      cap, final, deviation_reason for both structures)
- [x] Phase-9 disclaimer line present at top
- [x] Phase-9 invalidation block covers all three rubric categories
      (price / signal / macro)
- [x] All upstream phases include their own "Tool calls" audit table
- [x] No tool errors silently swallowed (phase 0 surfaced the 5/20 ←
      5/19 date fallback verbatim; phase 7 surfaced the Yahoo HTTP 401
      verbatim; phase 6 documented the FRED skip)

## Watch / monitoring summary (forward-looking)

For the next-business-day open (2026-05-20) and beyond:

1. **Pre-market 2026-05-20**: check if BTC has held $74,200 overnight
   (per [MACRO:BTC_2026-05-18]). If breached, **DO NOT enter the
   bull put spread**; instead consider re-running phase-4 GEX to see
   if the $11 negative-GEX flip is now in play.
2. **At open 2026-05-20**: confirm MARA spot is within $12.00-$12.60
   band. If outside (e.g., gap to $13+ on overnight BTC rally, or to
   $11.50 on BTC dump), re-evaluate entry levels rather than chasing.
3. **Tuesday EOD 2026-05-19 (today, this run)**: structures should be
   entered Wed 2026-05-20 with full 3-DTE theta capture window through
   Friday 2026-05-22 OPEX.
4. **Daily through 2026-05-22**: re-run the daily monitoring checklist
   from phase-9.

## Final auditor note

The run is **internally consistent and ready for action**. The
85/100 confluence score matches the 0.85 conviction bin in phase-9
exactly, and the unanimous 4-of-4 phase-8 agent convergence on
non-directional bias removes the most common cause of mis-calibrated
single-name research (split-desk verdicts). Phase-9's deliberate
downward sizing deviation (5% cap → 2.5% per structure) appropriately
respects the documented residual risks (TRANSITIONAL macro,
signal-backtest fade, correlation cascade exposure) without
contradicting the thesis. **No revision to phase-9 is required.**

---

### Final blueprint location

- **Trade blueprint:** `/Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20/phase-9-trade-plan.md`
- **Audit (this file):** `/Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20/phase-10-audit.md`
- **Full research dir:** `/Users/ewan/Development/stock-deep-dive/research/MARA/2026-05-20/`

### Confluence score

**85 / 100** — strong positive confluence around the RANGE thesis
(0.85 conviction bin).
