# Phase 10 — Audit & Confidence Score

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T21:40:00-04:00
**Audit scope:** phases 0–9 from
`/Users/ewan/Development/stock-deep-dive/research/FCX/2026-05-20/`.

## Summary

- **Dominant bias being audited:** LONG (range-bounded $55 → $65), per
  phase-9.
- **Raw confluence score:** **+24** (range −115 … +115).
- **Confluence score (0–100):** **60**.
- **Recommended conviction bin per rubric:** **0.65** (score band 50–64).
- **Phase-9 actual bin:** **0.65** — **MATCH**.
- **Contradictions logged:** **3** (phase-3, phase-5 partial, phase-8
  plurality misalignment).
- **Citation spot-check (3 sampled):** **3/3 resolve cleanly**.
- **Sanity checks:** **8/8 pass**.
- **Recommendation:** **Run is internally consistent and the trade
  blueprint is ready for action at the stated 0.65 / 5% size with the
  tightened invalidations already encoded.**

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | *"FCX in top-sweep cohort 5 of 5 sessions, consistency 1.00, dominant mixed, $54,380,015 cumulative sweep premium"* [FLOW:sweep_persistence@phase-1] — multi-session institutional engagement consistent with the LONG range-bounded thesis. |
| 2 — dark pool | **+** | *"block tier buy_ratio 0.69 ($6.55M, 4 prints) + large tier 0.601 ($42.3M, 218 prints) → +$11M inferred net institutional accumulation"* [DP:block_stratified@phase-2]. Mildly agrees; not `++` because no mega-tier print and the day's biggest single block was a $2.03M SELL at $59.27. |
| 3 — OI | **0** | *"59C Jun-18 OI 0 → 6,216 (+6,216, 88% ask, $3.23M)"* [OI:biggest_increases@phase-3] supports LONG, but *"65C Jul-17 OI −9,117 (33,172 → 24,055) on 14,478 vol — est 2,681 opens / 11,797 closes"* [OI:decrease_with_volume@phase-3] is institutional distribution at our exact short-leg strike. Cancels out → neutral. |
| 4 — structure | **+** | *"Spot $58.95 < ZGL $64.09, dealers SHORT GAMMA at spot; $65 strike net_gex +$1,437,659,056 (dominant long-gamma magnet)"* [STRUCT:gex@phase-4]. The magnet IS our target. Not `++` because the same map carries the $55 −$458M cascade trigger. |
| 5 — historical | **0** | *"IV30d 40.74%ile, VRP −7.43 pts (PREMIUM_BUYING regime)"* [HIST:iv_percentile_zscore][HIST:vrp@phase-5] supports the DEBIT structure choice — BUT *"bullish_flow signal backtest 26.7% win rate, avg −1.08% 5d move"* [HIST:signal_backtest@phase-5] and *"net 90d cumulative premium flow −$22.8M, BEARISH"* [HIST:cumulative_premium_flow@phase-5] argue against the LONG bias itself. Tied → neutral. |
| 6 — macro | **0** | *"Deutsche Bank PT $58 → $72 (Buy), consensus cluster $70–$81"* [MACRO:DBPT_2026-05-13@phase-6] supports the target — BUT *"Market regime TRANSITIONAL — bullish-flow breadth 34.7%, defined-risk only"* [MACRO:MarketRegime_2026-05-19@phase-6] forces sizing-down. Net tailwinds = headwinds → 0. |
| 7 — insights | **+** | *"Scenario COVERED_CALL at 20.6% confidence; explanation: 'Dark pool buying + call selling — yield enhancement, capping upside'"* [INSIGHT:conviction_matrix@phase-7]. The institutional pattern PRECISELY mirrors our long-lower-strike / short-upper-strike bull-call-spread structure. Not `++` because *FCX is absent from the bullish confluence top-100* [INSIGHT:signal_confluence@phase-7]. |
| 8 — agents | **−4 raw points** (4 agents executed; 1 LONG-aligned [+2], 3 non-aligned [−6]; earnings-scout intentionally skipped) | accumulation-hunter LONG conv 3 [+2]; contrarian-scanner NEUTRAL conv 2 [−2]; sweep-tracker RANGE conv 3 [−2]; risk-monitor NEUTRAL conv 4 [−2]. Net **−4**. **The plurality is non-directional, the highest-conviction agent (risk-monitor at 4) is NEUTRAL, and zero agents are SHORT.** |

**Raw score (sum):** +7 +7 +0 +7 +0 +0 +7 −4 = **+24**

**Confluence_score:** (24 + 115) / 230 × 100 = 139/230 × 100 = **60.4 → 60**

**Recommended bin:** **0.65** (score band 50–64 per
`rubrics/confluence-scoring.md`).

**Phase-9 actual bin:** **0.65** → **MATCH ✓**.

## Contradictions

Each entry follows the rubric format
`phase-N (topic): <conflict> — <suggested resolution>`.

- **phase-3 (OI positioning):** The 65C Jul-17 OI collapsed −9,117 on 14,478
  volume (est. 11,797 closes vs 2,681 opens), meaning the $1.54M ask-side
  sweep was lifting liquidity FROM a much larger institutional position-
  unwind, not initiating fresh momentum. This directly attacks the LONG
  thesis AT the structure's short-leg strike. — **Suggested resolution:
  TIGHTEN INVALIDATION** to include the signal-based trigger already
  encoded in phase-9 ("new 59C Jun-18 OI loses >1,000 in any session →
  close"). Phase-9 has done this; no further action needed.

- **phase-5 (historical, partial):** Cumulative 90d premium flow is **net
  bearish −$22.8M** (20 of 28 sessions bearish-flow days); market-wide
  bullish_flow signal backtest = **26.7% win rate, avg −1.08% 5d move**.
  Recent market regime punishes bullish-flow follow-through trades. —
  **Suggested resolution: WAIT FOR CONFIRMATION** is already baked into
  the post-trade checklist (re-check DP buy/sell ratio next session;
  ratchet to full position only on $64.09 reclaim, but cap still 5%).
  Additionally: HARD ENFORCE the 5% Kelly cap (phase-9 already at cap;
  do NOT exceed under any condition).

- **phase-8 (agent plurality):** **3 of 4 executed agents are non-
  directional** (1 NEUTRAL, 1 RANGE, 1 NEUTRAL-conviction-4). The
  highest-conviction agent is NEUTRAL, not LONG. — **Suggested
  resolution: NO ACTION on conviction (the 0.65 bin already encodes this
  via raw_score offset)** but **MONITOR for agent re-runs** — if any
  agent's view drifts toward SHORT in the next 2 sessions, downgrade
  conviction to 0.55 or close. The current trade is sized for "1
  out of 4 agents LONG with structural support from data" — fine as long
  as no agent flips outright bearish.

## Citation failures

Spot-checked 3 of 7 citations from phase-9's thesis (random sample):

| Citation | Resolution check | Result |
|----------|------------------|--------|
| **[DP:block_stratified@phase-2]** — "block buy_ratio 0.69 + large 0.601 = ~$11M net" | phase-2-dark-pool.md §"Tier breakdown" table rows: block buy_ratio = 0.69, large buy_ratio = 0.601; tier-net math: 76,294 − 34,200 = +42,094 (block) + 430,022 − 285,448 = +144,574 (large) ≈ +$11M at avg $59.4 | **✓ RESOLVES** |
| **[STRUCT:gex@phase-4]** — "$65 strike net_gex +$1.44B" | phase-4-structure.md §"GEX — per-strike map" table row: 65 → +1,437,659,056. Bolded as "DOMINANT LONG-GAMMA NODE — MAGNET". | **✓ RESOLVES** |
| **[MACRO:DBPT_2026-05-13@phase-6]** — "Deutsche Bank PT $58 → $72 (Buy)" | phase-6-macro.md §"FCX-specific catalysts" table row: "Deutsche Bank PT raise $58 → $72" with date 2026-05-13. WebSearch source: simplywall.st. | **✓ RESOLVES** |

**Citation failures: NONE.**

The four un-spot-checked thesis citations ([HIST:vrp@phase-5],
[INSIGHT:conviction_matrix@phase-7], [OI:biggest_increases@phase-3],
[AGENT:accumulation-hunter@phase-8]) were each tagged from sections that
have been read during the audit and exist verbatim in the cited phase MDs.

## Sanity checks

| Check | Pass? | Notes |
|-------|-------|-------|
| All `phase-*.md` files present in dir? | **✓** | phase-0 through phase-9 all exist (phase-10 being written now). |
| Phase-9 cites ≥3 distinct upstream datapoints? | **✓** | Citations summary lists **7** distinct datapoints (M-04 minimum is 3). |
| Conviction bin in {0.55, 0.65, 0.75, 0.85, 0.95}? | **✓** | 0.65. |
| ≥1 directional + ≥1 defined-risk structure? | **✓** | Bull call spread (directional primary) + put credit spread (defined-risk alternative). |
| Sizing math shown explicitly? | **✓** | p=0.65, b=1.66, raw_kelly=43.9%, fraction=0.25, cap=5%, final=5.00%. |
| Disclaimer at top of phase-9? | **✓** | "For research and educational use only. Not financial advice. Sizing and structures are illustrative." |
| Invalidation has all 3 categories (price/signal/macro)? | **✓** | Price ($55 close), Signal (DP ratio < 1.20, conviction matrix flip, 59C OI loss), Macro (CPI Jun-10, FOMC Jun-17, copper <$6). |
| Catalyst calendar populated? | **✓** | 7 dated catalysts with DTE inside the 30d window. |

## Final auditor note

The run is **internally consistent**. Confluence score 60 lands squarely in
the 0.65 conviction band and matches phase-9's chosen bin exactly. The
three contradictions logged (phase-3 65C unwind, phase-5 signal backtest,
phase-8 plurality) are each acknowledged in phase-9's invalidation triggers
and post-trade monitoring checklist, so the audit raises **no blocking
concerns**. The proposed trade — long FCX Jun-18 60/65 call debit spread
at $1.88, 5% of book risk, hard-stop $55 close — is ready for action; if
any single invalidation fires (or any agent flips outright SHORT on a
re-run), reduce or close per the encoded rules.
