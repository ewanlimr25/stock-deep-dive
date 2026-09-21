# Phase 10 — Audit & Confidence Score

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T01:18:43Z
**Dominant bias audited:** LONG (mild) — phase-9

## Summary

**Confluence score: 48 / 100** (base 58 − 5 debate − 5 sentinel-CAUTION). This is a
**mixed-to-slightly-positive** read — the dominant bias is mildly bullish but the data
is fighting it on the structural axis. **Recommended conviction bin: 0.55** (band 30–49,
lower end given the debate disconfirmation) → **phase-9's 0.55 = MATCH.** One phase
scored a contradiction (phase-4 structure, `-`), and two one-sided gate penalties fired
(phase-8b disconfirmed, phase-7c CAUTION). All three phase-9 spot-checked citations
resolve. The run is **internally consistent**: every phase agrees the trade is a *small,
defined-risk dip-buy, not a chase*, and the sizing (~0.6%) honestly reflects the two
fired gates. Ready for action as a token/watch-and-dip-buy blueprint.

## Confluence scorecard

Context (phase-0.5) = **GENUINELY_UNUSUAL** → no cap on phases 1–2.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Net_flow +$1.22M bullish, P/C 0.184, $45 Jan-2028 delta-0.85 LEAP + 5/5-session bullish sweep persistence [FLOW:sweeps/sweep-persistence] — but two-way $75 churn caps below `++`. |
| 2 — dark pool | **+** | Large-tier buy_ratio 0.61 across 115 trades [DP:block-stratified] — mild accumulation; the headline $241M is a de-rated quarter-end rebalance cross, so not `++`. |
| 3 — OI | **0** | Structurally call-heavy chain (walls $75/$80) but today added only +1,466 net OI [OI:biggest-increases] — churn; structural bull offset by zero retention → neutral. |
| 4 — structure | **−** | POSITIVE/long-gamma (ZGL $59.97) with max-pain $59–63 sitting 15–20% below spot [STRUCT:gex/max-pain] — caps upside / mean-reversion, a headwind to a bullish continuation. |
| 5 — historical | **0** | OI BUILDING 25 days (+128k) + bullish_flow backtest 62.5% [HIST] vs 90d cumulative premium net-bearish −$9.5M + PREMIUM_SELLING + extended +34.9%/30d — genuinely mixed. |
| 6 — macro | **0** | Regime TRANSITIONAL + hawkish Fed dots + rich sector (PEG 2.89) [MACRO] roughly offset by persistent Consumer Defensive inflow + idiosyncratic catalyst → neutral for a single-name thesis. |
| 7 — insights | **+** | Borderline DIRECTIONAL_LONG (49.9%) + price-vs-flow no divergence [INSIGHT] — mild agree; composite inflated by the rebalance cross, so not `++`. |
| 7b — fundamentals | **+** | CONFIRM, 0 contradictions: revenue +24.6%, 4/4 earnings beats, insiders buying (June MSPR +44.1) [FUND] — valuation risk (P/E 166x) keeps it below `++`. |
| 8 — agents | **0** (2 align / 2 range) | accumulation-hunter LONG (+2), sweep-tracker LONG (+2), contrarian-scanner RANGE (−2), risk-monitor RANGE (−2); earnings-scout MISSING. Net 0. |

**Raw score (symmetric):** +21 (eight phases: 7+7+0−7+0+0+7+7) + 0 (phase-8) = **+21**
**Base score:** round((21 + 130) / 260 × 100) = **58 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** **48 / 100**
**Recommended bin:** **0.55** (band 30–49; the debate disconfirmation argues the floor)
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-4 (structure):** long-gamma dealer cap at $75 + max-pain $59–63 sitting 15–20%
  *below* spot means the option structure has no upside magnet near $74 and favors
  mean-reversion — it contradicts a bullish continuation. **Resolution: already handled —
  phase-9 caps the directional target at $75–78 (short of the $80 wall), enters on dips
  ($70/$64–65) rather than chasing, and tightens first-invalidation to two closes below
  $70.** Keep the target capped; do not extend beyond $80 on this horizon.

*(One-sided gate penalties, not scored contradictions but recorded:* phase-8b
**disconfirmed** (bear ≥ bull) and phase-7c **CAUTION** — both correctly cut phase-9's
size, not the bias.)*

## Citation failures

_None._ Spot-checked 3 of phase-9's thesis citations:
1. `[HIST:oi-trend]` "OI BUILDING 25 consecutive days, +127,955" → **resolves** —
   phase-5-historical.md §OI trend (`consecutive_build_days 25`, `total_net_oi_change +127,955`). ✓
2. `[STRUCT:gex]` "ZGL $59.97, gamma walls $70 (+1.03M)/$75 (+681k)" → **resolves** —
   phase-4-structure.md §GEX (`zero_gamma_level 59.97`; $70 gex +1,030,467, $75 +681,186). ✓
3. `[HIST:signal-backtest]` "bullish_flow win_rate 0.625 (n=8)" → **resolves** —
   phase-5-historical.md §Signal backtest (`win_rate 62.5%`, `total_signals 8`). ✓

## Sanity checks

- [✓] All phase files present — phase-0, 0.5, 1, 2, 3, 4, 5, 6, 7, **7b, 7c**, 8, **8b**, 9, decision.json (+ this phase-10).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (Jul-31 $72/$78 call debit spread) + ≥1 defined-risk (Jul-31 $65/$60 put credit spread).
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate 0.625 (n=8, capped 0.75 → 0.625), not the bin.
- [✓] All five risk gates evaluated: fundamentals CONFIRM, **sentiment CAUTION (fired)**,
  correlation none, rotation neutral, **debate disconfirmed (fired)**. Phase-0.5
  `unusual_verdict = GENUINELY_UNUSUAL` reflected (no context cap; macro half-size reinforces small).
- [✓] Structures sized to the front-expiry expected move; `expected_move` (±3.52% / $2.61) in decision.json.
- [✓] `decision.json` exists and passes `validate_decision.py` (**OK**), incl. `context`,
  `expected_move`, and `gates.sentiment` fields. Backfilled `confluence_score = 48`,
  `recommended_bin = 0.55`.

## Final auditor note

The run is **internally consistent and honest**: a genuine, insider/OI-confirmed
turnaround (phases 1/2/5/7b) that is structurally capped and extended (phases 4/5/6),
correctly resolved into a *small, defined-risk, dip-buy* rather than a chase — with the
two fired gates (sentiment CAUTION, debate disconfirmed) cutting size to ~0.6% and the
confluence (48) matching the 0.55 floor bin. **No revision required**; the blueprint is
ready to act on as a token starter / dip-buy alert at $70 and $64–65, capped-target
$75–80, invalidated on two closes below the $64–65 shelf (hard stop under ZGL $60).
