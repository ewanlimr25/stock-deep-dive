# Phase 10 — Audit & Confidence Score

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T01:20:00Z
**Audits:** phase-0-intake.md → phase-9-trade-plan.md (all 10 files present)

## Summary

**Confluence score: 79 / 100.** This places the run in the upper half of the
**65–79 band**, which maps to the **0.75 conviction bin** per
`rubrics/confluence-scoring.md`. **Phase-9 chose 0.75 — MATCH.** The dominant
bias under audit is a hybrid: **RANGE through 2026-05-22 OPEX, then
SHORT-leaning via a long bear-put debit spread into the 2026-06-18 FOMC
expiry**, with a defined-risk 5/22 iron condor as the theta-harvest companion.
**Two partial contradictions** are logged (phases 2 and 3 contain elements
that contradict the *directional* leg even while supporting the *range* leg);
both are addressed by phase-9's structural choices. **All three spot-checked
citations resolve**. The run is internally consistent and ready for action.

## Confluence scorecard

| Phase | Score | Justification (datapoint quoted from cited phase) |
|---|---|---|
| 1 — Flow | **+** | "Net ask-side put premium ($3.1M ask) exceeds net ask-side call premium ($1.43M ask) in top-5 trades" — defensive flow corroborates the bear-leaning directional leg ([FLOW:top_premium_trades], phase-1 §Largest premium prints). Wing-OTM put IV outliers ($31-$49 strikes at 1.9-2.5 IV, [FLOW:iv_outliers]) confirm tail-hedge demand. |
| 2 — Dark Pool | **+** | Block-tier buy_ratio 0.754 on $14.95M ([DP:block_stratified]) is a mild accumulation signal that supports the **range floor** at $166.63 ($243.6M / 1.46M shares / 40 trades, [DP:price_levels]) and the $174-$179 institutional cost-basis ceiling that bounds the range. *Partially contradicts* the bear directional leg — see Contradictions §1. |
| 3 — OI | **+** | Call walls of 34,457 OI at $180 and 37,952 OI at $190 ([OI:biggest_increases], phase-3 §Largest OI increases) define the upside of the 5/22 OPEX range. Bullish-leaning OI direction count (12/8) is real but capped by the walls. *Partially contradicts* the bear directional leg — see Contradictions §2. |
| 4 — Structure | **++** | "Avg IV 2026-06-18 = 143.0% vs surrounding monthlies at 75-78%" ([STRUCT:iv_term_structure]) is the **single loudest signal in the entire workup** — defines the trade's binary anchor at June 16-17 FOMC. ZGL $174.79 and short-gamma 45-DTE regime ([STRUCT:gex]) align with phase-2 ceiling. |
| 5 — Historical | **+** | "IV30 percentile 33rd, VRP -4.34%, FAIR regime" ([HIST:iv_percentile_zscore, HIST:vrp]) directly favors the long-premium structure choice over short-premium. Bearish_flow signal 100% win rate / -4.45% / n=8 already partially paid out (MSTR's own signal delivered -7.28%), tempering the directional aggressiveness. |
| 6 — Macro | **++** | "April CPI +3.8% YoY (up from +3.3%, hottest since May 2023) released 2026-05-12" ([MACRO:CPI_2026-04 WebSearch:bls.gov]) plus CME FedWatch 65% June hold ([MACRO:FOMC_2026-06-17 WebSearch:cmegroup.com]) defines the directional bear-lean tilt with high conviction. |
| 7 — Insights | **0** | conviction_matrix MIXED with 3.66% confidence ([INSIGHT:conviction_matrix]) and MSTR absent from both bullish AND bearish signal_confluence top-50 ([INSIGHT:signal_confluence]) — UW composite explicitly refuses to take a side. Genuinely neutral; supports the "wait-for-catalyst" framing without confirming or denying direction. |
| 8 — Agents | **+ (4/4 align, +8)** | All four non-MISSING agents returned NEUTRAL with conviction 2/5 and explicitly named the June 18 binary as the only place edge exists. accumulation-hunter: "wait for mega-tier confirmation". contrarian-scanner: "crowd isn't extreme enough to fade". sweep-tracker: "tape is loud but two-sided". risk-monitor: "cap MSTR at 0.5x normal size, defined-risk debit structures only". All four endorse the phase-9 frame. |

**Raw score:** +7 +7 +7 +15 +7 +15 +0 +8 = **+66**
**Confluence_score:** (66 + 115) / 230 × 100 = **78.7 → 79 / 100**
**Recommended bin (per rubric 65-79 band):** **0.75**
**Phase-9 actual bin:** **0.75** → **MATCH ✓**

## Contradictions

Two partial conflicts flagged. Neither overturns the thesis but each has been
addressed in phase-9 — recording for transparency:

1. **phase-2 (Dark Pool): block-tier buy_ratio 0.754 contradicts pure bear directional.**
   - Detail: While `large_tier` is balanced at 0.519, the smaller `block_tier`
     ($1M-$10M trades) buy_ratio of 0.754 on $14.95M premium is a mild
     accumulation signal. A pure bearish reading would expect this to lean ≤
     0.5.
   - Resolution applied in phase-9: The bear leg is structured as a
     **debit-spread with capped downside**, not a naked short, and is sized
     at 2.5% of book risk (0.5× the 5% cap). Invalidation includes a hard
     stop on block_tier buy_ratio falling < 0.50, which would confirm the
     accumulation read is breaking down.

2. **phase-3 (OI): bullish-leaning OI direction count (12/8 strikes, 4:1
   premium-weighted bullish) contradicts pure bear directional.**
   - Detail: Day-of OI buildup at $165C, $167.5C, $170C, $175C, $190C, plus
     put-selling at $160P, $175P, $152.5P, infers a moderately bullish near-
     OPEX positioning skew. The $170C +8,654 OI is the day's hottest strike.
   - Resolution applied in phase-9: The trade design is **two-stage** — the
     iron condor body captures the bullish-bias pin from $160 to $180
     directly (this is monetizing the same positioning skew); the bear put
     spread is on a DIFFERENT expiry (6/18, post-FOMC) and is sized
     separately. Invalidation also includes "spot close > $174.79 on volume"
     which would flip the bear thesis if the bullish positioning extends.

**No `--` strong contradictions detected.**

## Citation failures

Spot-checked 3 citations from phase-9 thesis:

| # | Citation | Phase | Datapoint claimed | Found in source? |
|---|----------|-------|-------------------|------------------|
| 1 | `[STRUCT:iv_term_structure]` | phase-4-structure.md | "MSTR 2026-06-18 avg_iv = 143.0% vs neighbors at 75-78%" | ✓ — phase-4 §IV term structure shows expiry 2026-06-18 avg_iv 1.4301 (143.0%), May 22 93.2%, May 29 77.1%, Jun 5 78.3%, Jun 12 75.2%, Jun 26 78.7% |
| 2 | `[MACRO:CPI_2026-04 WebSearch:bls.gov]` | phase-6-macro.md | "April CPI +3.8% YoY (up from +3.3%), released 2026-05-12" | ✓ — phase-6 §Inflation: "Headline CPI YoY +3.8%", "Prior month +3.3%", "released 2026-05-12" |
| 3 | `[AGENT:risk-monitor]` | phase-8-agent-views.md | "fresh `risk_portfolio_correlation`: IBIT/MSTR 0.864, COIN/MSTR 0.803" | ✓ — phase-8 §risk-monitor top_risk verbatim contains these correlations |

**All 3 citations resolve. No citation failures.**

## Sanity checks

- [✓] All `phase-*.md` files present (phase-0 through phase-9 — 10 files in
      `/Users/ewan/Development/stock-deep-dive/research/MSTR/2026-05-20/`)
- [✓] phase-9 cites **≥ 3 distinct upstream datapoints** (cites 6 in
      Citations Summary: STRUCT:iv_term_structure, MACRO:CPI_2026-04,
      AGENT:risk-monitor, DP:price_levels, HIST:iv_percentile_zscore + HIST:vrp,
      STRUCT:today_gamma_flip)
- [✓] Conviction bin is one of `{0.55, 0.65, 0.75, 0.85, 0.95}` — bin is 0.75
- [✓] **≥ 1 directional structure present**: long $160/$140 bear put debit
      spread, June 18 2026 expiry
- [✓] **≥ 1 defined-risk structure present**: 5/22 iron condor
      ($155/$160/$180/$185)
- [✓] Sizing math shown explicitly — Kelly inputs p, b, raw_kelly, fraction,
      cap, deviation_reason all documented for both structures
- [✓] **Disclaimer line present** at top of phase-9: "For research and
      educational use only. Not financial advice. Sizing and structures are
      illustrative."
- [✓] **Invalidation has all three categories** (price-based, signal-based,
      macro-based) with concrete falsifiable triggers
- [✓] **Catalyst calendar present** with FOMC and May CPI explicitly listed
- [✓] **Post-trade monitoring checklist** present, 7 items (target was ≥ 4)

## Phase-by-phase data-availability audit

| Phase | Tool errors logged | Mitigations applied |
|---|---|---|
| 0 | 1 (date pivot 2026-05-20 → 2026-05-19) | Documented in §As-of pivot; all downstream tools used 2026-05-19 |
| 1 | 0 | — |
| 2 | 0 | — |
| 3 | 0 | — |
| 4 | 0 | — |
| 5 | 0 | — |
| 6 | 1 (FRED_API_KEY unset → CSV CDN blocked) | WebSearch + UW fallback used; every macro datapoint carries explicit source tag |
| 7 | 2 (Yahoo HTTP 401 on fundamentals; analyst_vs_flow returned no analyst payload) | Macro overlay (phase-6) supplied fundamental context (BTC NAV math, debt wall); no analyst anchor used in phase-9 |
| 8 | 1 (earnings-scout intentionally skipped — earnings 2026-07-30 is out of window) | Confluence math correctly used 4 agents not 5 |
| 9 | 0 | — |

**Total upstream tool errors: 5, all documented and mitigated.**

## Final auditor note

The run is **internally consistent and ready for action**. Phase-9's
conviction of 0.75 sits exactly in the band the confluence math recommends
(79/100, 65-79 band → 0.75). Both contradictions (phase-2 mild accumulation,
phase-3 bullish OI skew) are addressed structurally — the iron-condor body
*monetizes* the bullish positioning while the bear put spread sits on a
different expiry — and the explicit invalidation rules will catch a flip in
either before the trade incurs full max loss. The single largest source of
remaining uncertainty is the June 16-17 FOMC binary, which is by design the
catalyst the trade is built around; **the recommended re-run date of
2026-06-12 (post-May CPI, pre-FOMC week) is the correct check-in moment**.

## Confluence score histogram (visual)

```
Phase 1 (Flow):        +  ███▌
Phase 2 (Dark Pool):   +  ███▌
Phase 3 (OI):          +  ███▌
Phase 4 (Structure):   ++ ████████  ← loudest signal
Phase 5 (Historical):  +  ███▌
Phase 6 (Macro):       ++ ████████  ← directional anchor
Phase 7 (Insights):    0  ─
Phase 8 (Agents):      +8 ████  (4/4 align)

Raw: +66 / 115 max
Confluence: 79 / 100 → 0.75 conviction bin ✓ MATCH phase-9
```

— *End phase-10 audit.*
