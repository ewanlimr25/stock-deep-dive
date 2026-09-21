# Phase 10 — Audit & Confidence Score

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Upstream phases cited:** phase-0 through phase-9
**Generated:** 2026-05-17T17:31Z

## Summary

**Confluence score: 87/100** for the **RANGE-with-IV-crush** thesis.
That maps to recommended conviction bin **0.85** by the rubric. Phase-9
chose bin **0.55** — a 2-bin downgrade. The mismatch is intentional and
correctly justified by phase-9 (the rubric is designed for directional bias
confluence; high RANGE-thesis confluence does NOT translate into high
directional conviction, and the negative-Kelly math on the iron condor is
the binding constraint). **The run is internally consistent and the
conviction deviation is legitimate.**

Zero contradictions detected. Three citations spot-checked and all
resolved. All 10 phase files are present.

## Confluence scorecard

For the dominant phase-9 thesis: **RANGE between $219.44 and $235.74 on
the 05-22 chain, expressed as a defined-risk iron condor + the
IV-crush carry**.

| Phase | Score | Justification (quoting datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **0** | "Bias from this phase: cautiously bullish (LEAP signature dominates; near-term pin clouds the picture). Conviction 3/5." `[FLOW:summary]` LEAP signal is multi-month and doesn't directly support OR contradict the 1-5d RANGE thesis. Net neutral. |
| 2 — dark pool | **++** (+15) | "Primary support $219.44 ($2.25B 5d); primary resistance $235.74 ($1.36B 5d)." `[DP:price_levels]` These are the exact strike anchors for the iron condor — direct confirmation. Mega-tier sell skew (buy_ratio 0.421) also mildly supports the bearish tilt. |
| 3 — OI | **+** (+7) | "Wall of short calls at 237.5–240 acts as resistance" + "$220 pin gravity" `[OI:smart_positioning]` `[OI:pin_risk]`. Directly supports the RANGE upper-bound and the gravity-zone bottom. The 250C +45,567 OI bullish reach is a tail risk noted in phase-9. |
| 4 — structure | **++** (+15) | "POSITIVE gamma regime, $230 = $7.69T gamma wall, front-end IV ratio 1.41 BACKWARDATION, COMPLACENT skew." `[STRUCT:today_gamma_flip]` `[STRUCT:front_end_iv_ratio]` `[STRUCT:term_skew]` All structural reads support RANGE + IV-crush — this is the textbook setup. |
| 5 — historical | **++** (+15) | "IV percentile 100, VRP +0.1086 (PREMIUM_SELLING), 90d net flow +$200M (FLAT vs +36% price)." `[HIST:iv_percentile_zscore]` `[HIST:vrp]` `[HIST:cumulative_premium_flow]` 100th-percentile IV + premium-selling regime + flat 90d flow vs big price move = textbook short-vol + range setup. |
| 6 — macro | **+** (+7) | "TRANSITIONAL regime — half size, defined-risk." `[MACRO:MarketRegime_2026-05-15 UW]` Tech sector outflow + hot CPI slight bearish edge. Earnings 5/20 IS the catalyst that creates the IV-crush opportunity — so a tailwind for the strategy, not a contradiction. |
| 7 — insights | **++** (+15) | "Conviction matrix MIXED, institutional accumulation NEUTRAL, price_vs_flow DIVERGENCE TRUE." `[INSIGHT:conviction_matrix]` `[INSIGHT:institutional_accumulation]` `[INSIGHT:price_vs_flow]` Composite tools concur the directional bias is muddled — supports RANGE + bearish tilt. |
| 8 — agents | **+10** | 5/5 agents returned NEUTRAL or RANGE; 0 LONG; 0 SHORT. Each contributes +2 = +10 total. `[AGENT:accumulation-hunter]` `[AGENT:contrarian-scanner]` `[AGENT:sweep-tracker]` `[AGENT:earnings-scout]` `[AGENT:risk-monitor]` Maximum agent alignment. |

**Raw score:** 0 + 15 + 7 + 15 + 15 + 7 + 15 + 10 = **+84**

**Confluence_score normalized:** (84 + 115) / 230 × 100 = **86.5 → round to
87/100**.

**Recommended bin** (per rubric): score 80–89 → **0.85**.
**Phase-9 actual bin:** **0.55**.
**Result:** **MISMATCH (-2 bins)** — see Conviction deviation analysis
below.

## Conviction deviation analysis

The mismatch is **legitimate** and **already explained in phase-9 §Bias +
conviction**. Three reasons the rubric's 0.85 is the wrong number here
and 0.55 is correct:

1. **Rubric mismatch — directional vs RANGE thesis.** The confluence
   rubric is designed for *directional* bias confluence (LONG or SHORT).
   For a RANGE thesis, high confluence means "all signals confirm
   range-bound behavior," which is structurally very different from "all
   signals confirm an UP or DOWN bet." The 0.55 directional-conviction
   bin reflects that there is NO directional bet — phase-9's directional
   bias is RANGE with a *mild* bearish tilt only.

2. **Negative-Kelly math on the iron condor.** Phase-9 walked through
   raw_kelly = -0.50 at p=0.55, b=0.43. The structure is below Kelly
   threshold under any defensible probability estimate ≤0.75. Per the
   sizing rubric, this MUST trigger smaller size — and the directional-
   conviction bin should reflect that the bet is being taken under
   carry-edge rather than probabilistic-edge.

3. **Binary 5/20 event.** Phase-6 confirmed earnings AMC in 3 trading
   days (counting from Monday after the 05-15 close). Binary events
   are a known exception to mechanical sizing — the rubric's 0.85 would
   imply "near-certain edge", which is false. Phase-9's 0.55 is honest
   about the binary nature.

**Audit conclusion:** the bin deviation is a CORRECT use of phase-9's
deviation escape hatch. **No revision required.**

## Contradictions

**None.** All eight scored phases returned 0, + or ++. No phase scored
`-` or `--` against the RANGE thesis.

Notable near-contradictions worth tracking (would become real contradictions
if data shifts):
- **Phase-1 LEAP buying** — supports a multi-month bullish view that
  could OVERRIDE the RANGE thesis if it shows up in cumulative_premium_flow
  next week. Monitor: if `historical_cumulative_premium_flow` net jumps
  ≥+$500M in the next 5 sessions, phase-9 thesis becomes wrong.
- **Phase-7 call BID > call ASK volume today** — mildly bearish tilt
  signal that COULD intensify into a directional SHORT case if it persists
  3+ sessions. If risk-monitor flags this, switch the iron condor to a
  put-credit-spread-only structure.

## Citation failures

**None.** Three citations from phase-9 thesis were spot-checked:

1. `[STRUCT:front_end_iv_ratio]` ratio 1.41, near-IV 74.0%, far-IV 52.5%
   → verified in phase-4 §Front-end IV ratio: `ratio: 1.41 — BACKWARDATION`
   with `near_iv: 0.7405, far_iv: 0.5254`. ✅
2. `[INSIGHT:price_vs_flow]` DIVERGENCE TRUE, price +26.84% / 30d, net
   flow today -$42.65M → verified in phase-7 §Price vs flow:
   `divergence: true, price_change_pct: 26.84, net_premium_flow: -42,649,954`. ✅
3. `[DP:price_levels]` $219.44 ($2.25B 5d) and $235.74 ($1.36B 5d) →
   verified in phase-2 §Price levels: top two rows are `$219.44 / $2.25B /
   10.27M shares` and `$235.74 / $1.36B / 5.75M shares`. ✅

## Sanity checks

- [x] All `phase-*.md` files present (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
- [x] Phase-9 cites ≥3 distinct upstream datapoints (5 citations listed)
- [x] Conviction bin is one of {0.55, 0.65, 0.75, 0.85, 0.95} (0.55 ✅)
- [x] ≥1 directional + ≥1 defined-risk structure present (235/250 call
       debit + 220/215-240/245 iron condor ✅)
- [x] Sizing math shown explicitly (Kelly walkthrough with raw -0.50 result)
- [x] Disclaimer line present at top of phase-9 ✅

## Final auditor note

The run is internally consistent. The data does not support a directional
bet — it supports a defined-risk RANGE / vol-sell structure that earns
the textbook IV-crush carry around a binary event. Phase-9's down-binning
to 0.55 and 0.5% sizing are honest acknowledgments that even a clean
structural-carry setup does not pass strict Kelly at this conviction
level. **The blueprint is ready for action, with the explicit caveat that
this is a discretionary under-sized carry trade, not a high-conviction
bet.** If the PM wants a high-conviction NVDA bet, they should wait for
post-earnings clarity rather than force one into the IV pricing wall.
