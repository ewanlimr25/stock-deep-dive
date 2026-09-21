# Phase 10 — Audit & Confidence Score

**Ticker:** SMH
**As-of date:** 2026-05-28
**Generated:** 2026-05-29T14:30:00Z
**Dominant bias audited:** RANGE (range-lean, premium-selling) — phase-9

## Summary

**Confluence score 60/100 → recommended bin 0.65 → MATCHES phase-9's actual 0.65.**
The run is **internally consistent with zero hard contradictions** (no phase scored
`-`/`--`); the score sits in the "mixed-with-a-lean" zone because the strongest
structural supports (the dealer pin, the rich-IV premium-selling edge, the regime's
literal "iron condors in range" call) are genuinely qualified by a MIXED conviction
matrix, a price/flow divergence, an extreme-extension reversal risk, and the
phase-7c CAUTION gate (−5). The two neutral (`0`) scores — dark pool (ETF mechanics)
and insights (MIXED matrix + divergence offsetting the premium-sell endorsement) —
are honest neutrals, not buried conflicts. **Ready for action as written:** a
defined-risk, starter-size (1.25%) range premium-sale, with $585 as the bright-line
invalidation.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Net flow −$21.0M but hedging into strength; net options Δ only −$0.38bn `[FLOW:delta_notional DUCKDB]` (capped at + by BUSY_NAME context) |
| 2 — dark pool | **0** | Mixed/mildly distributive, LOW conviction; mega 0.314 = AH-at-close ETF redemption mechanics `[DP:block_stratified]` — genuinely neutral for a range thesis |
| 3 — OI | **+** | Net put OI +86,442 vs call +10,858, but 530P 05-29→06-05 is a **roll** = hedge maintenance, not a fresh short `[OI:biggest_increases DUCKDB]` |
| 4 — structure | **+** | Long-gamma cushion $595–650 + DEX +$3.95bn buy-dips pin $600–620 `[STRUCT:dex]`; qualified by net-short-gamma −$26.5M + the $550 trapdoor `[STRUCT:gex]` |
| 5 — historical | **+** | VRP +0.089 PREMIUM_SELLING + bearish_flow 55.6% vs bullish 100% (don't short) `[HIST:signal_backtest]`; extension/short-gamma qualify |
| 6 — macro | **+** | Regime TRANSITIONAL, "iron condors in range," breadth 40.6% `[MACRO:MarketRegime_2026-05-28 UW]`; fragile (top-calling, binary June-5) keeps it + not ++ |
| 7 — insights | **0** | conviction-matrix MIXED (4.5%) + price-vs-flow DIVERGENCE `[INSIGHT:price_vs_flow]` offset the `high_iv_sell_premium` endorsement — net neutral |
| 7b — fundamentals | **0** | NA — SMH is an ETF; single-name quality veto does not apply (holdings PEG 0.93 is advisory only) `[FUND:peer_pe fz]` |
| 8 — agents | **+ (3/4 align)** | NEUTRAL×2 + RANGE×1 align (+6), contrarian LONG dissents (−2) → net +4 `[AGENT:risk-monitor]` |

**Raw score (symmetric):** +7+0+7+7+7+7+0+0 (phases 1–7b) **+4** (phase 8) = **+39**
**Base score:** round((39 + 130) / 260 × 100) = **65/100**
**Debate penalty (phase-8b):** −0 (NOT disconfirmed — bull_residual 0.65 vs bear_residual 0.60)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** 65 − 5 = **60/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.65** → **✓ MATCH**

## Contradictions

**None.** No phase scored `-` or `--`. A RANGE thesis is the "centre" most signals are
consistent with; the genuine downside risk (the $585 short-gamma trapdoor + June-5
NFP) is carried as **invalidation**, not as a phase contradiction. Watch-items rather
than contradictions:
- The phase-7 **price/flow divergence** (price +31.9% vs bearish flow) is a leading
  reversal signal — already reflected in the mildly-bearish skew, the $585
  invalidation, and the directional put-debit-spread alternative. Resolution: **tighten
  invalidation** (close the put wing on two closes below $585) — already specified.
- The lone phase-8 **contrarian LONG dissent** — its point ("the crowded hedge side
  has been wrong all rally") is the real upside risk to the put wing. Resolution:
  **already priced** (call wing fades the cap; bullish_flow 100% noted as a key risk).

## Citation failures

**None.** Spot-checked 3 of phase-9's thesis citations:
1. `[STRUCT:dex]` DEX +$3.95bn, dealers buy dips → resolves to phase-4-structure.md
   §DEX (`net_dex +3,952,471,499`, "dealer hedge is to BUY underlying"). ✓
2. `[HIST:vrp]` VRP +0.089 PREMIUM_SELLING → resolves to phase-5-historical.md §IV
   regime (`vrp 0.089`, regime PREMIUM_SELLING, IV 46.2% vs RV 37.3%). ✓
3. `[HIST:signal_backtest]` bearish 55.6% vs bullish 100% → resolves to
   phase-5-historical.md §Signal backtest (bearish_flow 55.6% N=9, bullish_flow 100%
   N=6). ✓

## Sanity checks

- ✓ All phase files present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + decision.json.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (6 in citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- ✓ ≥1 directional (put debit spread 590/565) + ≥1 defined-risk (iron condor) structure.
- ✓ Sizing math shown; Kelly `p` = phase-5 backtest win-rate 0.556 (n=9), N-capped 0.75, half-map ceiling 2.5%.
- ✓ All five risk gates evaluated: fundamentals NA, **sentiment CAUTION (fired, cut half→starter)**, correlation none, rotation neutral, debate not-disconfirmed; context BUSY_NAME_NORMAL_DAY reflected (no top-of-band, → 1.25% starter).
- ✓ Structures sized to front-expiry expected move (±1.71%); `expected_move` in JSON; defined-risk caps a single NFP/FOMC gap within max loss.
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. `context`,
  `expected_move`, `gates.sentiment`); `confluence_score`/`recommended_bin` backfilled (60 / 0.65).

## Final auditor note

The run is internally consistent and decision-ready: every phase points to the same
picture — a parabolic, richly-hedged semis basket pinned by dealer long-gamma where
the edge is **selling over-priced IV in a defined-risk range, not betting direction**,
and the conviction (0.65) and starter size (1.25%) correctly reflect both that edge
and its real tail (the $585 June-5 trapdoor). No phase needs revision; the single
thing that would force a re-think is a decisive break of $585, which the plan already
names as hard invalidation and the trigger to flip the put wing into the bearish
debit-spread tail.
