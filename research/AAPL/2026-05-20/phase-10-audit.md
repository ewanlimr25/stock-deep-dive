# Phase 10 — Audit & Confidence Score

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-21T01:15:00Z
**Audited against:** phase-9-trade-plan.md (dominant bias: **LONG**)

## Summary

- **Raw confluence score:** **+87**
- **Normalized confluence score:** **88 / 100**
- **Recommended conviction bin:** **0.85** (80–89 band)
- **Phase-9 actual conviction bin:** **0.75**
- **Match status:** **MISMATCH (1-bin downgrade)** — documented in
  phase-9 §"Conviction deviation" with three concrete justifications;
  the auditor accepts the downgrade as a defensible position-sizing
  caution rather than a scoring error.
- **Formal contradictions (phases scored − or −−):** **0**
- **Soft tensions worth flagging in the contradictions log:** **2**
  (5-day bearish sweep persistence inside phase-1; TRANSITIONAL macro
  regime + binary CPI/FOMC inside the trade window inside phase-6).
- **Citation spot-check:** **3 / 3 resolved**.
- **Sanity checks:** **5 / 5 passed**.

The run is **internally consistent and ready for action** at the
phase-9 written conviction of 0.75.

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** (+7) | "$54.1M ask-side sweep of the 2028-01-21 $300 call, 10,608 contracts, avg $51.43" [FLOW:sweeps] is the dominant directional print, but the same phase also flags "5-day sweep persistence: AAPL top 5/5 sessions, dominant_direction=bearish, $1.054B aggregate" [FLOW:sweep_persistence] — net mild agree. |
| 2 — dark pool | **++** (+15) | "Mega-tier buy_ratio 0.794, $1,048,864,323 premium across 18 prints" [DP:block_stratified] plus "true after-hours buy: 762,382 sh @ $302.25 at +$0.635 above mid" [DP:largest]. Unambiguous institutional accumulation. |
| 3 — OI | **+** (+7) | "5/22 weekly OI builds skew bullish: C00305 +1,799 (net ask-bid +1,342), C00307.5 +1,127 (+1,291), C00310 +1,443 (+1,020), C00302.5 +2,053 (+684)" [OI:smart_positioning] and AAPL ranks #8 in pin risk at $300 [OI:pin_risk]. The LEAP roll not yet visible (T+1 issue) caps the score. |
| 4 — structure | **++** (+15) | "Regime POSITIVE, total GEX $648.7B" [STRUCT:gex] with "$1,383,658,924,735 GEX support_wall at $302.5; 0DTE ZGL $287.86" [STRUCT:today_gamma_flip] and "net DEX +$13.69T (public call-long → dealer hedge BUYS underlying)" [STRUCT:dex]. Conviction 5/5 in the phase itself. |
| 5 — historical | **++** (+15) | "IV percentile 14.29, regime LOW_IV" [HIST:iv_percentile_zscore], "29 consecutive build days" [HIST:oi_trend], "net flow +$487,526,488 bullish, trend_direction BULLISH" [HIST:cumulative_premium_flow], and "bullish_flow signal 66.7% win rate, +1.19% avg over 20 TD" [HIST:signal_backtest]. |
| 6 — macro | **+** (+7) | "Technology +$349,934,394 net sector inflow today (largest)" [MACRO:SectorRotation_2026-05-20] is the strongest tailwind, but partially offset by "April CPI +3.8% YoY (up from +3.3%)" [MACRO:CPI_2026-04] and TRANSITIONAL regime with 39.5% bullish breadth [MACRO:MarketRegime_2026-05-20]. |
| 7 — insights | **++** (+15) | "Scenario DIRECTIONAL_LONG, DP buy_ratio 0.672 … institutional directional bet" [INSIGHT:conviction_matrix], "ACCUMULATION, buy/sell ratio 2.05, VWAP $301.48" [INSIGHT:institutional_accumulation], "no divergence, price +16.03%, flow bullish" [INSIGHT:price_vs_flow]. |
| 8 — agents | **+6** | 3 LONG (accumulation-hunter, sweep-tracker, earnings-scout) at conviction 4 = +6 total; 2 NEUTRAL (contrarian-scanner, risk-monitor) at 0 contribution each. No SHORT votes. |

**Raw score:** +7 + 15 + 7 + 15 + 15 + 7 + 15 + 6 = **+87**

**Normalized:** round((87 + 115) / 230 × 100) = round(87.83) = **88 / 100**

**Recommended bin per rubric:** 0.85 (80–89 band)

**Phase-9 actual bin:** **0.75** — **MISMATCH (1-bin downgrade)**

**Audit ruling on the deviation:** **Acceptable.** Phase-9's
deviation note is specific, falsifiable, and risk-conservative:
(1) 2/5 agents NEUTRAL on size, (2) phase-1's 5-day sweep persistence
is the unresolved tension, (3) macro is TRANSITIONAL with binary
events inside the 30-DTE window. The rubric explicitly permits
downward sizing without explanation and downward conviction with
explanation. **No corrective action required.**

## Contradictions

**Formal contradictions (any phase scored `-` or `--`): NONE.**

**Soft tensions worth listing for the trader's awareness:**

- **phase-1 (flow) internal soft tension:** the **5-day sweep
  persistence flag ($1.054B, dominant_direction=bearish)** is real
  data that the phase-1 verdict, phase-7, and phase-8 contrarian-
  scanner all interpret as **roll mechanics** (bid-side closes of
  deep-ITM stock-replacement calls at delta 0.91+). That is a
  **plausible inference** but not a **measurement**. **Suggested
  resolution:** monitor `historical_cumulative_premium_flow` daily
  for 3 consecutive net-bearish sessions; if it triggers, the
  persistence flag was a leading signal and phase-9 should close
  per the signal-based invalidation rule.
- **phase-6 (macro) internal soft tension:** the **TRANSITIONAL
  regime + April CPI re-acceleration to 3.8% YoY** are the
  highest-probability invalidators in the 30-DTE window via the
  **June 11 CPI and June 17 FOMC catalysts**. Phase-9 already
  encodes both as macro-based invalidation triggers. **Suggested
  resolution:** none — phase-9 has handled this correctly with
  catalyst-day position reductions in its monitoring checklist.

## Citation failures

**None.** Spot-checked 3 of 7 citations from phase-9's thesis:

1. **[FLOW:sweeps]** $54,110,903 ask-side sweep of 2028-01-21 $300C,
   10,608 contracts, avg $51.43 — **resolves** in phase-1-flow.md
   §"Sweeps (ask vs bid)" table row 1: `300 C | 2028-01-21 | ask |
   $54.11M | 10,608 | 49 | $51.43`. ✓
2. **[DP:block_stratified]** Mega-tier buy_ratio 0.794, $1,048,864,323
   across 18 prints — **resolves** in phase-2-dark-pool.md §"Tier
   breakdown (single day)" row "Mega | ≥ $10M | 18 | $1,048,864,323
   | 2,755,182 | 715,006 | 0.794". ✓
3. **[STRUCT:today_gamma_flip]** $1,383,658,924,735 GEX support_wall
   at $302.5; 0DTE ZGL $287.86 — **resolves** in phase-4-structure.md
   §"Today gamma flip (0DTE walls)" rows "302.5 | +1,383,658,924,735
   | support_wall (largest)" and "0DTE ZGL | $287.86". ✓

## Sanity checks

- [x] All `phase-*.md` files present in `research/AAPL/2026-05-20/`
      (phase-0 through phase-10 — phase-10 is this file).
- [x] Phase-9 cites **7 distinct upstream datapoints** (≥3 required).
- [x] Phase-9 conviction bin **0.75** is in {0.55, 0.65, 0.75, 0.85,
      0.95}.
- [x] **At least 1 directional structure** (300/315 call debit spread
      6/19) and **at least 1 defined-risk structure** (297.5/287.5
      put credit spread 6/19).
- [x] **Sizing math shown explicitly:** Kelly p=0.75, b=3.4, raw
      Kelly 67.6%, suggested 16.9%, capped to 5%.

## Final auditor note

This run is **internally consistent**. Seven upstream phases all
agree on direction (LONG) with magnitudes ranging from `+` to `++`;
no phase scores against the thesis. The remaining tensions (phase-1's
5-day bearish sweep persistence and phase-6's binary macro window)
are correctly internalized into phase-9's invalidation rules and
monitoring checklist. The phase-9 PM deliberately downgraded
conviction one bin (0.85 → 0.75) for documented sizing-caution
reasons; the auditor accepts this as defensible discipline rather
than a scoring miss. **The blueprint is ready for action.**
