# Phase 10 — Audit & Confidence Score

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T01:35:00Z
**Upstream phases audited:** phase-0 through phase-9

## Summary

**Confluence score:** **67 / 100** → recommended conviction bin **0.75**.
**Phase-9 actual conviction:** **0.55** → **MISMATCH (more conservative than
audit recommends)**. Per `sizing-rubric.md` this is an *allowed downward
deviation* (always permitted, no escape-hatch required). The downward
deviation is justified by phase-9 itself: the 6.7% recent `bullish_flow`
backtest base rate, the risk-monitor's "HALF normal" recommendation, and
the unstable GEX regime (13 flips in 28 sessions) all support a more
defensive sizing posture than the raw confluence number alone would
indicate.

The run is **internally consistent** with **2 mildly contradicting phases**
(phase-5 historical and phase-6 macro), both of which phase-9 explicitly
addressed in its invalidation rubric and structure choice. All 3 spot-checked
citations in phase-9 resolved cleanly. The trade plan is **ready for
desk-PM review**.

## Confluence scorecard

Dominant thesis from phase-9: **RANGE with long-side asymmetric overlay,
range $133–$140, conviction 0.55, defined-risk-only sizing**.

| Phase | Score | Justification (datapoint) |
|-------|:-----:|---------------------------|
| 1 — flow | **+** | "Net ASK calls $5.69M vs BID puts $0.37M; 5-day sweep persistence $217M, consistency 1.0" — directionally supports the long overlay; the *campaign* exists, but only the upside leg of the range thesis benefits [FLOW:sweep_persistence]. |
| 2 — dark pool | **++** | "5-day price levels: dominant overhead $140.87/$145.81/$144.15 = $88M ABOVE spot; new lower cluster $133.40/$134.50 = emerging support BELOW spot" — both wings of the iron condor sit on real DP-anchored levels [DP:price_levels]. |
| 3 — OI positioning | **++** | "BABA #40 in pin-risk table, pin strike $135, distance 0.51%, OI 21,302, 3 DTE pin score 105,465" PLUS "May 22 (3 DTE) $137-$142C strip ALL bid-side dominant = institutional call-writing" — pin gravity + ceiling exactly matches the IC short strikes [OI:pin_risk] [OI:biggest_increases]. |
| 4 — dealer structure | **++** | "Spot $135.70 / ZGL $135.66 / $140 wall +$8.5B GEX / $130 trapdoor −$985M GEX" — this IS the trade structure; phase-9 is built directly on this map [STRUCT:gex]. |
| 5 — historical | **−** | "bullish_flow 20d backtest: 6.7% win rate (1/15), avg −1.62%" — recent market-wide base rate is hostile to the long overlay, and phase-9 cited this as the primary reason for sizing below the suggested cap [HIST:signal_backtest]. |
| 6 — macro | **−** | "Market regime TRANSITIONAL, breadth 34.7%, Consumer Cyclical sector flow −$27M, April CPI 3.8% YoY, Fed 1-cut path for 2026" — every macro vector is mildly hostile to the long-duration AI-capex thesis [MACRO:MarketRegime_2026-05-19 UW] [MACRO:CPI_2026-04]. |
| 7 — UW insights | **0** | "Conviction matrix MIXED, confidence_pct 2.81; institutional accumulation NEUTRAL ratio 1.12; BABA not in top-50 bullish OR bearish confluence" — the composite is genuinely mixed and matches phase-9's mixed thesis without leaning either way [INSIGHT:conviction_matrix]. |
| 8 — agents | **+2** | 2 RANGE / 1 SHORT (conv 4) / 1 LONG (conv 3); plurality matches RANGE bias of phase-9 [AGENT:accumulation-hunter] [AGENT:risk-monitor] (+2 each); contrarian SHORT does not match (−2); sweep-tracker LONG = partial match (0); net +2. |

**Raw score:** +7 + 15 + 15 + 15 − 7 − 7 + 0 + 2 = **+40**

**Confluence_score:** round((40 + 115) / 230 × 100) = **67 / 100**

**Recommended bin (per `confluence-scoring.md` table):** 65–79 → **0.75**

**Phase-9 actual bin:** **0.55** → **MISMATCH (2 bins lower than recommended)**

Per `sizing-rubric.md`:
> "Phase-9 may set `final_size_pct < suggested_size_pct` without explanation
> (always allowed to be smaller)."

Therefore the mismatch is **permitted** and consistent with the rubric.
Phase-9's documented reasons (risk-monitor HALF rec + phase-5 backtest +
regime flip frequency) align with the conservative posture.

## Contradictions

- **phase-5 (historical):** The `bullish_flow` signal backtest over the last
  20 trading days produced only 6.7% wins and an average −1.62% move (15
  signals: TSLA −7.4%, AVGO −4.1%, GOOGL −4.5%, MSFT −1.2%, AAPL −0.43%,
  etc.). This is a market-wide cohort that systematically failed in the
  exact window today's BABA bullish positioning emerged from — *the same
  signature, the same week*. — **Resolution applied by phase-9:** downgrade
  conviction from suggested 0.75 to 0.55, prefer defined-risk over naked
  long, and document the macro-invalidation trigger (June 17–18 FOMC
  hawkish surprise) for the directional leg.

- **phase-6 (macro):** The market regime is TRANSITIONAL with narrow
  breadth (34.7% bullish), the Consumer Cyclical sector saw −$27M outflow
  today, April CPI hit a 3-year high at 3.8% YoY on an Iran-war energy
  shock, and the Fed's April 29 dot plot allows only one 2026 cut with
  hawkish dissent. None of these favor a long-duration AI-capex growth
  story. — **Resolution applied by phase-9:** structures cap profit at the
  realistic resistance ($150 short leg of the call spread); the iron condor
  is defined-risk and exploits the very vol crush the macro headwind
  creates; June FOMC is named as the macro-based hard invalidation with
  pre-emptive exit 24h prior.

## Citation failures

None. Spot-checked 3 of the 7 citations in phase-9's `## Citations summary`:

1. **[STRUCT:gex]** — phase-9 claims "Total GEX +$16.48B, ZGL $135.66,
   $140 wall +$8.51B, $130 trapdoor −$985M."
   - Verified in `phase-4-structure.md §GEX — per-strike concentration`
     table: total_gex = 16,481,931,618; zero_gamma_level = 135.66; strike
     140 net_gex = +8,507,386,927; strike 130 net_gex = −984,891,005.
   - **PASS** — all four numbers match within rounding.
2. **[FLOW:sweep_persistence]** — phase-9 claims "BABA 5/5 sessions in top,
   consistency 1.0, $217M cumulative sweep premium."
   - Verified in `phase-1-flow.md §Sweep persistence` table: sessions_in_top
     5, consistency_score 1.0, total_sweep_premium $217,119,527.
   - **PASS**.
3. **[HIST:signal_backtest]** — phase-9 claims "20d window 15 signals, 6.7%
   win rate, avg −1.62%, samples include TSLA −7.4%, AVGO −4.1%, GOOGL
   −4.5%."
   - Verified in `phase-5-historical.md §Signal backtest`: total_signals 15,
     win_rate "6.7%", avg_move_pct −1.62; per-row check: TSLA 2026-05-13
     −7.36%, AVGO 2026-05-14 −4.10%, GOOGL 2026-05-13 −4.53%.
   - **PASS** (TSLA cite rounded from −7.36% to −7.4% — acceptable).

All three citations resolved. No `## Citation failures` to log.

## Sanity checks

- [x] All `phase-*.md` files present in
      `/Users/ewan/Development/stock-deep-dive/research/BABA/2026-05-20/`:
      phase-0, phase-1, phase-2, phase-3, phase-4, phase-5, phase-6,
      phase-7, phase-8, phase-9, phase-10 (this file) = **11 files**.
- [x] Phase-9 cites ≥3 distinct upstream datapoints (cites 7 in the
      `## Citations summary` block).
- [x] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} (= **0.55**).
- [x] ≥1 directional structure (Jul 17 $140/$150 call debit spread) AND
      ≥1 defined-risk structure (May 29 $128/$132/$140/$143 iron condor).
- [x] Sizing math shown explicitly for BOTH structures (Kelly formula,
      p/b inputs, raw_kelly value, fraction, cap, final, deviation notes).
- [x] Disclaimer line present at top of phase-9.
- [x] Phase-9 invalidation lists all three categories (price / signal /
      macro) with concrete falsifiable triggers.
- [x] Phase-9 catalyst calendar present with table format.
- [x] Phase-9 monitoring checklist has ≥4 items (has 7).

## Internal consistency cross-check

| Element | Phase 9 says | Upstream agreement |
|---------|--------------|-------------------|
| Spot reference | $135.69–$135.70 | phase-0, phase-1 ($135.56), phase-2, phase-3 ($135.69), phase-4 ($135.70), phase-7 (VWAP $135.70) — **AGREE within $0.14 (one tick of intraday drift)** |
| Range floor | $133–$134.50 | phase-2 DP cluster $133.40 (19 trades) and $134.50 (23 trades); phase-8 all four agents cite $133–$134.50 floor — **AGREE** |
| Range ceiling | $140 | phase-3 $137–$142 covered-call strip; phase-4 +$8.5B GEX wall; phase-8 all four agents converge on $140 — **AGREE** |
| Trapdoor (invalidation) | $130 | phase-4 −$985M GEX; phase-8 risk-monitor cites identical level — **AGREE** |
| LEAP target | $145–$150 | phase-1 Jan27 $150C $2.43M ASK + Mar27 $145C $1.89M paired; phase-2 5-day DP cluster $145.81; phase-3 Jun 18 $150C OI 34,204; phase-4 GEX +$2.08B at $145 / +$2.15B at $150 — **AGREE** |
| Conviction 0.55 | 0.55 | Audit recommends 0.75; phase-9 chose 0.55. **MISMATCH — but documented and permitted** |
| Sizing 2.50% + 1.50% = 4.00% | combined | Below 5% cap; respects risk-monitor HALF rec — **CONSISTENT** |

## Final auditor note

The run is **internally consistent** and the trade plan is **ready for
desk-PM action with the standard "review at first OPEX touch" cadence**.
Phase-9's deliberate downward sizing deviation from the audit-recommended
0.75 bin to the 0.55 bin is a *defensible conservative call* given the
phase-5 backtest hostility, the phase-8 risk-monitor's HALF recommendation,
and the structural fragility of the regime (13 GEX flips in 28 sessions).
The two flagged contradictions (phase-5 and phase-6) are correctly
addressed by both the structure choice (defined-risk on both legs) and
the explicit macro-invalidation trigger at the June FOMC. **No revision
to phase-9 is required.**
