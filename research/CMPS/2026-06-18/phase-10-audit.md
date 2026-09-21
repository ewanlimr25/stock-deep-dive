# Phase 10 — Audit & Confidence Score

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Inputs audited:** phase-0 … phase-9 + decision.json

## Summary

**Confluence score = 31 / 100** (strong-ish *negative* confluence). Phase-9's bias is
**NEUTRAL**; scored against the latent **bearish flow** thesis that triggered the dive,
the data **fights the bear** — which is exactly why the correct call is *no directional
trade*. The score maps to the **30–49 band → recommended bin 0.55–0.65**; phase-9 chose
**0.55** → **MATCH** (bottom of band, appropriate given 31 sits just above the <30
"strong-negative" line). **4 phases contradict the bear** (3, 4, 5, and a hard 7b VETO);
all 3 spot-checked citations resolve; all sanity checks pass. The run is internally
consistent and the blueprint (watch-only, 0% directional, starter-only defined-risk) is
ready as written.

## Scoring frame

Phase-9 bias is NEUTRAL, which the confluence machinery cannot score directly. Per the
rubric's intent, I score each phase by **whether it confirms the latent bearish-flow
thesis** (the directional signal under test). A low score correctly resolves "the bear
is unconfirmed" → NEUTRAL. Phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` → **no cap**
on phases 1–2.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Bearish IS the signal, but it's ONE non-persistent print: "consistency 0.2, 1 session" [FLOW:sweep_persistence] — mildly agrees, not `++`. |
| 2 — dark pool | **0** | Mixed: large tier 60% sell but the single 100K block was a buy, total only 0.32% of float [DP:block_stratified] — no distribution confirmation. |
| 3 — OI | **−** | Chain call-dominated, `biggest-increases` EMPTY, Jul-17 P/C 0.026 [OI:term_structure] — standing positioning contradicts the bear. |
| 4 — structure | **−** | FULLY_POSITIVE GEX, no ZGL, NORMAL skew (1.047) [STRUCT:gex] — long-gamma pin mechanically resists the downside the put needs. |
| 5 — historical | **−** | +33% 30d trend, OI BUILDING 4d, VRP +5.03 premium-selling, P/C z +3.83 = fade trigger [HIST:pc_ratio_zscore] — backdrop contradicts a fresh bear. |
| 6 — macro | **0** | Two-sided: hawkish FOMC/10y headwind aligns with bear vs Healthcare INFLOW persistence 0.8 adverse [MACRO:sector_flow_persistence] — cancels. |
| 7 — insights | **0** | Conviction-matrix MIXED, CMPS absent both confluence lists; the one pro-bear note is price-vs-flow DIVERGENCE [INSIGHT:price_vs_flow]. |
| 7b — fundamentals | **−−** | **FUNDAMENTAL VETO** — strong-buy (Recom 1.12, target $21.72) + insiders buying (MSPR +100) contradict the short on ≥2 axes [FUND:tier_adjustment]. |
| 8 — agents | **− (0/4 align)** | 0 of 4 active agents bearish (3 NEUTRAL + 1 RANGE/fade) → 4 × −2 = −8. |

**Raw score (symmetric):** (+7 +0 −7 −7 −7 +0 +0 −15) = **−29** (eight phases) **+ (−8)**
(phase-8) = **−37**.
**Base score:** round((−37 + 130) / 260 × 100) = **36 / 100**.
**Gate penalties (one-sided):** phase-8b disconfirmed = false → −0; phase-7c **CAUTION
→ −5**; phase-7c VETO = no → −0.
**Confluence_score:** 36 − 5 = **31 / 100**.
**Recommended bin:** **0.55–0.65** (30–49 band).
**Phase-9 actual bin:** **0.55** → **MATCH.**

## Contradictions

- **phase-3 (OI):** the chain is call-dominated and `biggest-increases` is empty — standing
  positioning is bullish, the opposite of the bear → **wait for confirmation:** only
  re-engage the short if P10/lower put OI actually builds on 6/19+.
- **phase-4 (structure):** FULLY_POSITIVE long-gamma pin resists a downside move → **tighten
  invalidation:** require a negative-GEX flip (not just a price dip) before any short.
- **phase-5 (historical):** +33% trend + premium-selling VRP + a +3.83σ P/C *fade* trigger
  argue the bear is the late/crowded side → **downgrade conviction** (already at 0.55,
  NEUTRAL — satisfied).
- **phase-7b (fundamentals, −−):** hard VETO — improving fundamentals make a fresh short
  smart-money exit-liquidity to fade, not a quality short → **directional watch-only / 0%**
  (already applied in phase-9 sizing).

## Citation failures

None — 3 of 3 spot-checked resolve:
1. [FLOW:top_premium_trades] "ONE Jan-2028 $10 LEAP put ~$647K ask-side" → phase-1 §Largest
   prints (4 ask-side P10 prints sum $252.7K+$157.5K+$131.95K+$104.4K ≈ $646.55K). ✓
2. [HIST:pc_ratio_zscore] "+3.83 BEARISH_EXTREME" → phase-5 §P/C z-score (zscore 3.831,
   extreme BEARISH_EXTREME). ✓
3. [FUND:tier_adjustment] "phase-7b VETO" → phase-7b §Verdict (tier_adjustment: VETO,
   contradiction_count 2). ✓

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + decision.json + this audit.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✓ ≥1 directional (Jan-2028 $10/$7 put debit spread) + ≥1 defined-risk (7/17 iron condor).
- ✓ Sizing math shown; Kelly `p` = phase-5 win-rate 0.857 → N-capped 0.75 (n=7, backtest).
- ✓ All five gates evaluated: fundamentals **VETO**, sentiment **CAUTION**, correlation
  **none**, rotation **adverse**, debate **not-disconfirmed**. Final directional 0% from VETO.
- ✓ Phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` reflected (no top-of-band; final 0% anyway).
- ✓ Structures sized to front-expiry expected move (±4.14% / ±$0.52 in JSON; 7/17 ±27% move
  flagged against the condor's short strikes).
- ✓ `decision.json` exists, backfilled (confluence_score 31, recommended_bin 0.55), and
  passes `validate_decision.py` → **OK** (incl. context / expected_move / gates.sentiment).

## Final auditor note

The run is **internally consistent**: a single, non-persistent, fundamentally-vetoed
bearish LEAP-put print is correctly resolved — by 4 contradicting phases and a 31/100
confluence — into a **NEUTRAL, no-directional-trade** blueprint rather than a forced
short. No revision needed; the only live question the audit endorses carrying forward is
whether that put is informed front-running of the H2-2026 COMP006 durability binary —
monitor the 6/19+ tape for a P10 OI build, which is the single event that would reopen the
bear case.
