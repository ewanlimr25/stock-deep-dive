# Phase 10 — Audit & Confidence Score

**Ticker:** KWEB
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Phase-9 dominant bias scored against:** **LONG** (range-anchored;
target $29 magnet / $30 ceiling; primary 1-5d, secondary 1-4w)

## Summary

Raw audit score **+19** → confluence score **58 / 100** (50-64 band).
Recommended conviction bin per rubric: **0.65**. Phase-9 actual bin:
**0.65** → **MATCH**. **2 contradictions** logged (phase 1 + phase 2),
both already addressed in phase-9's invalidation triggers. **All 3
spot-checked citations resolve** to upstream datapoints. **All 9
sanity checks pass.** Run is **internally consistent and ready for
desk action at the conviction level published**.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **−** | "KWEB 5-day sweep_persistence dominant_direction=bearish, sessions_in_top 5/5, total_sweep_premium **$94,897,773** [FLOW:sweep_persistence]" contradicts LONG; offset partially by today's deep-ITM Jun 20C ask buy ($631.5K, delta 0.95) and Jan'27 27P bid liquidation ($330K) [FLOW:top_premium_trades]. |
| 2 — dark pool | **−** | "Mega-tier buy_ratio **0.000** on $25,871,032 (913,698 sh, two prints at -0.5¢ / -1.5¢ below NBBO mid) [DP:block_stratified]" contradicts LONG. Offset by block-tier buy_ratio 0.677 and large-tier 0.536, but the mega-tier signal is unambiguous. |
| 3 — OI positioning | **+** | "KWEB 260529 28P OI Δ **+11,461 (5.4×)**, prev_bid_vol 6,300 vs ask 621 → put SELL-to-open, $665K premium [OI:smart_positioning]" is the single strongest new opening in the chain and directly defends the $28 entry price for the LONG thesis. |
| 4 — dealer structure | **++** | "Net GEX at $29 = **+$17,793,645,641** (largest positive strike), ZGL **$23.81**, regime POSITIVE [STRUCT:gex]" strongly supports the LONG-to-$29 magnet thesis with a 16% positive-gamma envelope. |
| 5 — historical | **0** | Competing signals balance: "IV30d **30.24%**, percentile **0**, VRP **-3.92%** [HIST:iv_percentile_zscore / historical_vrp]" supports LONG via cheap debit structures; "bearish-flow signal backtest win_rate 100%, avg -4.45% (N=8) [HIST:historical_signal_backtest]" contradicts. Net neutral. |
| 6 — macro | **+** | "2026-05-20 US-China tariff truce extension proposal (Boeing 200-jet, $30B reciprocal cuts) [MACRO:USChinaTariff_2026-05-20]" supports LONG; offset by sector outflows Comm Services -$84.3M and Consumer Cyclical -$27.0M [MACRO:SectorRotation_2026-05-19 UW] and weak China April retail sales +0.2% YoY [MACRO:ChinaRetail_2026-04]. Net mild +. |
| 7 — UW insights | **0** | "conviction_matrix scenario **MIXED** at **8.28% confidence** [INSIGHT:conviction_matrix]"; KWEB absent from both bullish and bearish signal_confluence top 50. Genuinely neutral. YINN (China-bull 3x) scored 5 bullish factors providing cross-asset confirmation but not direct on KWEB. |
| 8 — agents | **+ (2 of 4 align)** | sweep-tracker LONG conv 4 (+2), contrarian-scanner LONG conv 3 (+2), accumulation-hunter RANGE (0), risk-monitor RANGE (0). Earnings-scout MISSING (skipped, ETF). Net agent contribution: **+4**. |

**Raw score:** **−7 − 7 + 7 + 15 + 0 + 7 + 0 + 4 = +19**
**Confluence_score:** `round((19 + 115) / 230 × 100)` = **58 / 100**
**Recommended bin (per confluence-scoring rubric, 50-64 band):** **0.65**
**Phase-9 actual bin:** **0.65** → **MATCH** ✓

## Contradictions

- **Phase 1 (flow):** 5-day bearish sweep persistence $94.9M directly
  contradicts the LONG bias. **Suggested resolution: TIGHTEN
  INVALIDATION** — phase-9 already encodes this as "phase-5
  `historical_cumulative_premium_flow` turns net bearish for 3
  consecutive sessions → invalidation". Additionally, the phase-7
  framing parses much of this persistence as **call overwriting** not
  outright bearish directional, which is structurally consistent with
  the LONG-anchored-range thesis. The contradiction is documented but
  partially de-fanged.
- **Phase 2 (dark pool):** Mega-tier DP buy_ratio 0.000 on $25.87M
  (913,698 sh) is a clean institutional distribution signal that
  contradicts LONG. **Suggested resolution: TIGHTEN INVALIDATION** —
  phase-9 already encodes this via "phase-7 `insights_conviction_matrix`
  DP buy_ratio drops below 0.35 = invalidation". Sizing is already at
  the 5% cap with a deviation-down clause to 3.0% if confluence falls
  below 50; this absorbs the residual risk. **Additional note:** the
  EOD 19:56:41Z mega-print (424,185 sh @ $28.32) executed *before* the
  tariff truce headline broke at 2026-05-20; if the seller knew about
  the truce in advance, the print would have likely been smaller — so
  the most likely read is a *non-informed liquidator* (index unwind
  or rebalancing flow), which would weaken its predictive value for
  the LONG thesis without invalidating it. The audit does NOT raise
  the score on this speculation; it is logged as context only.

## Citation spot-check

Three citations spot-checked from phase-9's thesis:

| # | Citation | Phase | Resolution |
|---|----------|-------|------------|
| 1 | `[FLOW:sweep_persistence]` — KWEB dominant_direction=bearish, sessions_in_top 5/5, total_sweep_premium $94,897,773 | phase-1-flow.md §"Sweep persistence over 5 sessions" | **RESOLVES** ✓ — table row matches exactly. |
| 2 | `[OI:smart_positioning]` — KWEB 260529 28P OI Δ +11,461 (5.4×), prev_bid_vol 6,300 vs prev_ask_vol 621 → bullish (put sell-to-open) | phase-3-positioning.md §"Largest OI increases" | **RESOLVES** ✓ — all values match: 11,461 OI Δ, 5.4× ratio, 6,300 bid vol, 621 ask vol. |
| 3 | `[STRUCT:gex]` — KWEB net GEX at $29 = +$17,793,645,641; ZGL = $23.81; regime POSITIVE | phase-4-structure.md §"GEX — per-strike profile" | **RESOLVES** ✓ — $29 row +$17,793,645,641; ZGL $23.81 — confirmed. |

## Citation failures

None. All 3 spot-checked citations resolve to upstream datapoints with
matching numeric values.

## Sanity checks

| Check | Result |
|-------|--------|
| All `phase-*.md` files present in dir (0–9) | ✓ |
| Phase-9 cites ≥3 distinct upstream datapoints in thesis / citations | ✓ (7 distinct datapoints) |
| Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} | ✓ (0.65) |
| ≥1 directional structure present | ✓ (Jun 29/31 call debit spread) |
| ≥1 defined-risk structure present | ✓ (Jun 27/26 put credit spread) |
| Sizing math shown (Kelly formula explicit) | ✓ (p=0.65, b=1.773, raw_kelly 45.2%, final 5.0% capped) |
| Disclaimer line at top of phase 9 | ✓ |
| Invalidation has price + signal + macro categories | ✓ |
| Catalyst calendar lists ≥3 next-30d events | ✓ (6 events) |

## Cross-phase contradictions worth noting (sub-audit)

Beyond the formal `-` scores, the run contains internal tensions that
the desk should keep in mind even though they don't change the
recommended bin:

1. **Phase 3 vs Phase 5 — premium-selling vs premium-buying regime.**
   Phase 5 says VRP −3.92% (premium-BUYING regime favored). Phase 3
   shows institutions are *selling* premium (28P sold-to-open at
   $665K, Jun 30C net bid-side ask-bid −6,018). Either the
   institutions are wrong about forward realized vol, OR they are
   harvesting against a stock position they hold and don't care about
   pure vol edge. Phase 9 picks the *debit* side via the call debit
   spread (consistent with the VRP read) but also publishes a put
   credit spread (consistent with the institutional behaviour). Both
   structures are defensible; running both is consistent with the
   data.

2. **Phase 2 (UW composite) institutional_accumulation NEUTRAL vs
   phase 2 (stratified) mega-tier 0.000 buy_ratio.** The composite
   blends tiers and loses the asymmetry. Phase 9 correctly invokes
   the stratified read, not the composite, for the invalidation
   trigger. This is the right choice but is worth flagging so the PM
   doesn't get confused by reading the composite tool tomorrow.

3. **Phase 1 5-day persistence reads as bearish in the raw tool; the
   parsed picture from phase 3 (call overwriting, not put buying) is
   directionally less bearish.** The audit holds the raw `-` score on
   phase 1 even though parsed phase 3 partially absorbs it — to avoid
   double-counting the same flow as both a contradiction and a
   support.

## Final auditor note

The run is **internally consistent and ready for desk action**. The
LONG-range-anchored thesis at conviction 0.65 is justified by the
phase-4 dealer structure (positive gamma magnet to $29), the phase-3
floor defense (28P sold-to-open), and the phase-6 tariff-truce
catalyst that broke post-close on 2026-05-20. The phase-1 / phase-2
contradictions are real but are already absorbed by phase-9's
invalidation triggers and the 5% sizing cap; **the desk should
execute the published structures with the explicit understanding that
the bearish persistence + mega-tier DP distribution are documented
risks, not unknown unknowns**.

**Audit verdict:** **PASS — confluence 58/100, bin 0.65 MATCH, no
citation failures, 2 contradictions logged and mitigated**.
