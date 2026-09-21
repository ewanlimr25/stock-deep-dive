# Phase 10 — Audit & Confidence Score

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases audited:** phase-0 through phase-9
**Dominant phase-9 bias scored against:** NEUTRAL with mild SHORT tilt, conviction 0.55

## Summary

- **Confluence score: 61 / 100.**
- **Recommended conviction bin: 0.65** (per scoring band 50-64).
- **Phase-9 actual bin: 0.55. → MISMATCH (phase-9 is one bin LOWER than the audit recommends).**
- **Contradictions: 2** (phase-1 flow lean and phase-2 dark-pool lean both
  push softly LONG against the phase-9 SHORT tilt).
- **Citation spot-checks: 3/3 PASS.**
- **Sanity checks: all PASS.**
- **Auditor verdict:** Run is **internally consistent and ready for action**.
  The conviction-bin mismatch is downward (more conservative than the
  score recommends), which is acceptable given the 1-1-1-1 agent split in
  phase 8 — phase-9 deliberately sized down to honor the genuine ambiguity.

## Confluence scorecard

Scored against phase-9's NEUTRAL-with-mild-SHORT-tilt bias.

| Phase | Score | Justification (datapoint quoted) |
|---|---|---|
| 1 — flow | **-** (-7) | "Mixed leaning bullish-multi-month, conviction 3/5"; largest premium = Jan-27 15C $816,270 mid block (delta 0.62) — institutional LEAP accumulation contradicts the SHORT tilt. [FLOW:top_premium_trades] |
| 2 — dark pool | **-** (-7) | Premium-weighted net buy_ratio 0.596 with large-tier $173.97M @ 0.616 — net institutional BUYING, contradicts SHORT tilt. (Block-tier 0.339 partially offsets but only $13.75M of $187.72M total.) [DP:block_stratified] |
| 3 — OI | **0** (0) | SOFI #18 market-wide pin_risk at $15 with 80,486 OI + two-track 15.5/16/16.5C bull-buying + 17/17.5/18/19/20+C institutional-writing — genuinely range-bound (no directional bias). [OI:pin_risk, OI:smart_positioning] |
| 4 — structure | **+** (+7) | "Range-bound mean-reversion within $15-$16" with $15 trapdoor (-$47B GEX) and $16 ceiling (+$25B GEX) — matches phase-9 range thesis; COMPLACENT skew (-5.1%) supports buying cheap downside puts. [STRUCT:gex, STRUCT:term_skew] |
| 5 — historical | **++** (+15) | "Bullish_flow backtest 5d lookback: 7 signals, 0.0% win rate, avg -3.05%" + VRP -9.47% (premium buying favored) + 21:7 bearish:bullish flow days over 28 sessions — strongest single support for the SHORT tilt. [HIST:signal_backtest, HIST:vrp, HIST:trend] |
| 6 — macro | **+** (+7) | Financial Services sector outflow -$48.79M + April CPI YoY +3.8% reaccelerating + Fed projecting only 1 cut for 2026 — sticky-inflation backdrop confirms the headwind for SOFI's NIM thesis. [MACRO:SectorRotation_2026-05-19, MACRO:CPIAUCSL_2026-04, MACRO:FOMC_2026-04-29] |
| 7 — insights | **+** (+7) | Conviction matrix MIXED at 9.57% confidence with SOFI absent from BOTH top-50 confluence tables + call ask/bid 89,595/108,863 (NET BID-HEAVY = call WRITING dominant today) — confirms neutrality with directional tilt away from bulls. [INSIGHT:conviction_matrix, INSIGHT:signal_confluence] |
| 8 — agents (4 returned, 1 MISSING) | **+** (+4 net) | 1 LONG (-2), 1 SHORT (+2), 1 NEUTRAL (+2), 1 RANGE (+2), 1 MISSING (0). Net +4. Contrarian-scanner has the room's highest conviction (4/5 SHORT). [AGENT:contrarian-scanner] |

**Raw score:** -7 -7 +0 +7 +15 +7 +7 +4 = **+26**

**Confluence score:** round((26 + 115) / 230 × 100) = round(141/230 × 100) = **61 / 100**

**Recommended bin (per band 50-64):** **0.65**

**Phase-9 actual bin:** **0.55** → **MISMATCH (-1 bin, conservative)**

## Contradictions

- **phase-1 (flow)**: The single largest premium trade is a Jan-2027 15C
  mid-side $816,270 block (delta 0.62, 2,366 contracts) — institutional ATM
  LEAP call accumulation directly contradicts the SHORT tilt. The
  ask/mid-side bullish call premium aggregate (~$3.46M) outweighs the
  bid-side / call-writing premium aggregate (~$1.52M) on the same session.
  **Suggested resolution:** Tighten invalidation — if the Jan-27 15C OI
  continues to build > 5,000 contracts/day for 2 consecutive sessions
  AND dark pool buy_ratio sustains > 0.65, **exit the put-spread at break-even
  or small loss before the FOMC window**. This is a known
  thesis-killer; phase-9 already cites this risk under the "macro-based
  invalidation" if the macro narrative pivots.

- **phase-2 (dark pool)**: $187.72M total off-exchange premium with
  premium-weighted buy_ratio 0.596 (large-tier 0.616; block-tier 0.339).
  Net dark pool reads as **net institutional buying**, contradicting the
  SHORT tilt. Pre-market prints at $15.56-$15.63 (above eventual close)
  reinforce the BUY interpretation. **Suggested resolution:** Already
  captured in phase-9's signal-based invalidation —
  `dark-pool buy_ratio > 0.65 for 2 consecutive sessions` is the explicit
  trigger to flatten. Auditor recommends additionally watching for the
  block-tier (≥$1M) buy_ratio: if block-tier reverses to ≥ 0.55 (vs today's
  0.339), the institutional distribution-into-strength signal is gone and
  the put thesis is meaningfully weaker.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:

1. **[STRUCT:gex]** — "total GEX -$4.61B on 2026-05-19, peak negative
   -$47.27B at $15 strike, peak positive +$25.18B at $16 strike, ZGL $11.65".
   ✓ Resolves to phase-4 §GEX (multi-week, DTE ≤ 45).
2. **[HIST:signal_backtest]** — "bullish_flow backtest 5d lookback returned
   7 signals with 0.0% win rate / -3.05% avg move".
   ✓ Resolves to phase-5 §Signal backtest.
3. **[MACRO:CPIAUCSL_2026-04 WebSearch:bls.gov]** — "April CPI YoY +3.8%
   (highest since May 2023), core +2.8%, energy +17.9%".
   ✓ Resolves to phase-6 §Inflation.

## Sanity checks

- [x] All `phase-*.md` files present in the dir (phase-0 through phase-9).
- [x] Phase-9 cites ≥3 distinct upstream datapoints (cites 6 in its
      Citations summary).
- [x] Conviction bin is one of {0.55, 0.65, 0.75, 0.85, 0.95}
      → phase-9 chose 0.55. ✓
- [x] At least 1 directional + 1 defined-risk structure present
      (Jun-18 15P/14P put debit spread + Jun-18 14P/15P/16C/17C iron condor). ✓
- [x] Sizing math shown explicitly (Kelly inputs, raw kelly = 43.75%,
      fractional × 0.25 = 10.94%, capped at 5%, final 5.0% for primary;
      iron condor raw_kelly = -0.097 NEGATIVE, manual override to 1.0% with
      explanation). ✓
- [x] Disclaimer line present at top of phase-9. ✓
- [x] Earnings-scout MISSING flagged correctly (next earnings 2026-08-04 ≫
      30d window). ✓

## Final auditor note

**The run is internally consistent and ready for action.** The two
contradictions (phase-1 flow and phase-2 dark pool, both leaning softly
LONG) are explicitly anticipated in phase-9's invalidation triggers and
weighted appropriately in the 5%-cap sizing. The conviction-bin mismatch
is downward — phase-9 sized to 0.55 when the score recommends 0.65 —
which is **acceptable and arguably correct** given the 1-1-1-1 agent
split in phase 8 (the audit score doesn't fully capture how genuinely
unsettled the room is). The PM has chosen the more conservative bin to
honor that uncertainty. The trade blueprint at `phase-9-trade-plan.md`
is the actionable output.

**Final confluence: 61 / 100 — moderate positive confluence for a
mild-SHORT/RANGE thesis. Trade is defensible but does not have
overwhelming edge; size accordingly (the put-debit-spread at 5% book risk
caps loss at 1.25% of book risk given the 0.25 debit / 1.00 max
profit-on-loss math, which is appropriate for a 0.55-conviction bet).**
