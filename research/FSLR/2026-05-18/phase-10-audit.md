# Phase 10 — Audit & Confidence Score

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T01:50:00Z
**Phase-9 dominant bias being scored:** **LONG** (conviction 0.75)

## Summary

The FSLR run achieves a **confluence score of 67/100**, which maps to the
**recommended conviction bin 0.75**. Phase-9's actual conviction bin is
**0.75 — MATCH.** One mild contradiction (phase-5) and one
genuinely-neutral phase (phase-7) were correctly handled in phase-9 via
voluntary size reduction (3% vs 5% suggested) and via inclusion of a
defined-risk credit-spread leg complementing the directional debit
spread. All three sampled citations resolve cleanly to their cited
phase files. All template/structure sanity checks pass. **The run is
internally consistent and ready for action with the sizing discipline
phase-9 already encodes.**

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — Flow | **+** | "Net call ask − call bid = +$1.63M; Mar-2027 280C $1.668M ask sweep vol/OI = 10×" [FLOW:options_flow_sweeps] + [FLOW:options_flow_unusual_volume]. Two-sided 250C tape and $1.27M put hedge prevent a `++` but bullish net is clear. |
| 2 — Dark pool | **+** | "Large-tier buy_ratio = 0.535 on $61.0M / 377 trades" [DP:block_stratified]; intraday +5.8% rally absorbed; $1.82M buyer paid +$0.47 above ask at $235.87 [DP:largest]. Mild accumulation. |
| 3 — OI | **+** | "Standing Jan-2027 $380C: OI 9,037 at $10.56 avg ≈ $9.5M of legacy bullish LEAP premium" [OI:oi_decrease_with_volume]. Today's deltas were OPEX-distorted (empty) but the standing leverage is real and aligns with the two-tenor $280C build phase-1/phase-7 detected. Weak +, but +. |
| 4 — Structure | **++** | "Total GEX +$452,282,889 POSITIVE; ZGL $121.35 vs spot $234.48; $250 strike net_gex = +$228,076,645" [STRUCT:gex] + "DEX +$18.33B; call_dex 9× put_dex; dealer hedge BUYS underlying" [STRUCT:dex]. Cleanest pro-thesis phase. |
| 5 — Historical | **−** | "bullish_flow signal_backtest win_rate = 26.3%, avg_move = −1.26% across 19 firings" [HIST:signal_backtest]. A real contradictor; market-wide bullish-flow setups have lost on average. Mitigated, not eliminated, by FSLR's idiosyncratic catalyst. |
| 6 — Macro | **+** | "Section 232 polysilicon presidential decision window open through ~late June 2026" [MACRO:Sec232_polysilicon_pending] + "FSLR is the largest US-domiciled CdTe (non-poly) manufacturer — tariff is near-pure idiosyncratic tailwind." Broad tape is TRANSITIONAL/headwind, idiosyncratic catalyst dominates. |
| 7 — Insights | **0** | "Conviction matrix scenario = MIXED, confidence 1.66%" [INSIGHT:conviction_matrix] + "FSLR absent from both top-100 bullish and top-100 bearish confluence lists at min_score=1" [INSIGHT:signal_confluence]. Genuinely neutral composite — composite tools don't measure dealer structure or binary catalyst, which is where the thesis lives. |
| 8 — Agents | **+ (2/4 align)** | accumulation-hunter LONG (+2), sweep-tracker LONG (+2), contrarian-scanner RANGE (0 — mild misalign, not opposite), risk-monitor NEUTRAL (0 — mild misalign), earnings-scout MISSING (0). Plurality LONG; universal level convergence at $231.62 / $250.00 / close < $230. |

**Raw scoring math:**

```
Phase 1:  +7
Phase 2:  +7
Phase 3:  +7
Phase 4: +15
Phase 5:  -7
Phase 6:  +7
Phase 7:   0
Phase 8: +2 + 2 + 0 + 0 + 0 = +4
---------------------
Raw total: +40
Normalized: (40 + 115) / 230 × 100 = 64.3 / 1 ≈ 67  (round half up)
```

Wait — recompute: (40 + 115) = 155; 155 / 230 = 0.6739; × 100 = 67.39 → **round to 67**.

| Field | Value |
|-------|-------|
| **Raw score** | **+40** |
| **Confluence score** | **67/100** |
| **Recommended conviction bin** | **0.75** (band 65–79) |
| **Phase-9 actual bin** | **0.75** |
| **Match?** | ✓ **MATCH** |

## Contradictions

- **phase-5 (historical, score −):** The market-wide `bullish_flow`
  `historical_signal_backtest` over the past 20 trading days posted a
  **26.3% win rate with −1.26% avg 20-day move** across 19 firings
  [HIST:signal_backtest]. This is a genuine systemic headwind to any
  naive bullish-flow long. **Suggested resolution:** Phase-9 already
  applied the correct mitigation by **voluntarily sizing the
  directional leg to 3.0% of book risk** (well below the 5% Kelly cap
  derived from 0.75 conviction × 0.71 payoff ratio × 0.25 fractional
  Kelly = 9.95% pre-cap), and by **adding a defined-risk credit-spread
  alternative** that does not depend on bullish_flow's market-wide hit
  rate. No further action required.

- **phase-7 (insights, score 0, NOT a contradiction but flagged for
  transparency):** The composite tools returned MIXED at 1.66%
  confidence and NEUTRAL accumulation [INSIGHT:conviction_matrix,
  institutional_accumulation]; phase-7 itself called out that these
  composites do not measure phase-4's dealer-structure inputs or
  phase-6's binary catalyst. **Suggested resolution:** Phase-9 correctly
  anchored conviction on phase-4 + phase-6 rather than phase-7's
  surface read, with the caveat that *if* phase-7 flips to
  DIRECTIONAL_SHORT or HEDGED_LONG on a daily refresh, that becomes a
  signal-based invalidation trigger — which phase-9 lists.

No phase scored `--`. No killer contradictions.

## Citation spot-check

Sampled 3 of phase-9's thesis/citations citations:

| # | Cited claim (phase-9) | Cited tag | Resolves? | Evidence (verbatim) |
|---|----------------------|-----------|-----------|---------------------|
| 1 | "Total GEX +$452M, ZGL $121.35, $250 strike = +$228M GEX magnet" | [STRUCT:gex] | ✓ | phase-4-structure.md §GEX: "Total GEX: **+$452,282,889**", "Zero Gamma Level: **$121.35**", "**250** \| **+$228,076,645**". |
| 2 | "Mar-2027 280C $1.39M ask single print, Δ0.48, vol/OI=10×" | [FLOW:options_flow_sweeps] | ✓ | phase-1-flow.md §Largest premium prints: "19:30:52 \| Call \| 280 \| 2027-03-19 \| **$1,390K** \| ASK \| **0.479** \| 57.5% \| 236.26" and §New positioning: "Call \| 280 \| 2027-03-19 \| 48 \| 480 \| **10.0×**". |
| 3 | "Bullish_flow signal backtest 26.3% win rate, −1.26% avg 20d, n=19" | [HIST:signal_backtest] | ✓ | phase-5-historical.md §Signal backtest: "**Win rate** \| **26.3%**", "**Avg move** \| **−1.26%**", "Total signals \| 19". |

**All 3 citations resolve cleanly.** No citation failures.

## Citation failures

(none — all spot-checks passed)

## Sanity checks

- [✓] All `phase-*.md` files (0–10) present in `research/FSLR/2026-05-18/`.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (it cites **7** in the
      Citations summary).
- [✓] Phase-9 conviction bin is one of {0.55, 0.65, 0.75, 0.85, 0.95}: **0.75**.
- [✓] Phase-9 has ≥1 directional structure (long call debit spread
      Jul-17-2026 $240/$260) **and** ≥1 defined-risk alternative (short
      put credit spread May-22-2026 $230/$225).
- [✓] Phase-9 shows sizing math explicitly (Kelly with p=0.75, b=0.71,
      raw_kelly 39.8%, fractional 9.95%, cap 5%, final 3.0% voluntarily
      reduced).
- [✓] Phase-9 has a `## Invalidation` block with all three categories
      (price, signal, macro), each with concrete falsifiable triggers.
- [✓] Phase-9 disclaimer line present at the top.
- [✓] Phase-9 ticks the strikes off real OI / gamma walls (the $240
      and $260 strikes match phase-4 GEX clusters; the $230 put-credit
      strike sits at the −$46.5M GEX wall).
- [✓] Phase-9 expiry choice (Jul-17) explicitly avoids both the Section
      232 window risk (closes after late June) and the Q2 earnings IV
      crush (2026-07-30, after expiry).
- [✓] Macro overlay every bullet tagged with [MACRO:…].
- [✓] Catalyst calendar sourced from phase-6.

## Final auditor note

**The run is internally consistent and ready for action.** The single
real contradiction (phase-5's bullish_flow backtest contradiction at
26.3% win rate) is acknowledged by phase-10, correctly handled by
phase-9 via voluntary size reduction to 3.0% and the addition of a
defined-risk credit-spread leg, and does not invalidate the LONG bias
which is dominantly supported by the phase-4 dealer structure
(++ rating) and the phase-6 idiosyncratic Section 232 catalyst (+ rating).
Phase-9's 0.75 conviction bin matches the recommended bin from the
67/100 confluence score; **no revision required**.
