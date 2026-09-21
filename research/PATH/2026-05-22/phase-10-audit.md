# Phase 10 — Audit & Confidence Score

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Inputs audited:** phase-0 … phase-9 + decision.json

## Summary

**Confluence score = 59/100** (band 50–64 → recommended bin **0.65**). Phase-9's actual bin
is **0.55** — one notch lower, **intentionally**, because the phase-8b debate disconfirmation
gate down-shifts the bin (this is correct gate behavior, not a mismatch). The run is
**internally consistent**: a genuinely two-sided, BUSY_NAME, binary-event setup where the
dominant tension (phase-1 bearish flow vs phase-2 dark-pool accumulation) is explicitly
resolved in phase-3 (overwriting/buy-write) and phase-7c (short-hedging into a 30%-short
squeeze). **One contradiction** (phase-1) and **one corrected data error** (phase-0's spot
price) logged; all 3 spot-checked citations resolve; decision.json validates. Ready for
action as a defined-risk, starter-size, neutral-to-mildly-long vol-harvest into 05-28.

## Confluence scorecard

Dominant bias scored against = **NEUTRAL with a mild long tilt** (phase-9). Phase-0.5
`unusual_verdict = BUSY_NAME_NORMAL_DAY` → phases 1–2 capped at `+` (cannot `++`).

| Phase | Score | Justification (diagnostic datapoint) |
|-------|-------|--------------------------------------|
| 1 — flow | **−** | Net_flow −$398,934 + 5-session bearish sweep persistence ($6.01M) contradict a long on their face [FLOW:sweep_persistence] (decoded downstream as overwriting/short-hedging) |
| 2 — dark pool | **+** | Block buy_ratio 1.0 ($13.95M, 0 sells) = accumulation; capped at + by BUSY_NAME [DP:block_stratified] |
| 3 — OI | **+** | Two-sided premium writing = buy-write/collar around an accumulated long, neutral-to-mild-long [OI:smart_positioning] |
| 4 — structure | **+** | Call-skew COMPLACENT (call 93.3% > put 86.2%) + DEX +$28.2M = upside tilt; $11 long-gamma pin [STRUCT:term_skew] · [STRUCT:gex] |
| 5 — historical | **0** | PREMIUM_SELLING regime, no directional edge; bearish_flow backtest 28.6%, DP-accum null [HIST:vrp] · [HIST:signal_backtest] |
| 6 — macro | **0** | Tech persistent inflow (aligned) offset by TRANSITIONAL half-size = net neutral [MACRO:MarketRegime_2026-05-22] |
| 7 — insights | **+** | conviction_matrix DIRECTIONAL_LONG (37.8%) + ACCUMULATION 6.11×, tempered by DIVERGENCE [INSIGHT:conviction_matrix] |
| 7b — fundamentals | **+** | CONFIRM: 83% GM, +12.6% growth, 2/2 beats, no debt — quality supports the long, no veto [FUND:earnings_surprise] |
| 8 — agents | **+8** | 2 LONG + 3 NEUTRAL, 0 SHORT/opposed (4 net-aligned units) [AGENT:desk] |

**Raw score (symmetric):** (−7 +7 +7 +7 +0 +0 +7 +7) + 8 = **+36**
**Base score:** round((36 + 130) / 260 × 100) = **64**/100
**Debate penalty (phase-8b):** **−5** (disconfirmed: bull_residual 0.55 < bear_residual 0.65)
**Sentiment penalty (phase-7c):** **0** (tier_adjustment = CONFIRM)
**Confluence_score:** **59**/100
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — one notch below by the **phase-8b debate gate** (down-shift
one bin). **MATCH** with the gate logic (the recommended-band bin is 0.65; the debate gate
legitimately pulls the operative bin to 0.55). Not a discrepancy.

## Contradictions

- **phase-1 (flow): scored `−`.** The whole-tape net_flow is −$398,934 and PATH shows a
  5-session bearish sweep campaign — directly against a long tilt. **Resolution: already
  reconciled, keep tight invalidation.** Phase-3 (OI smart_positioning) and phase-7c
  (short interest ~30%) decode this as call-overwriting + short-seller hedging, not
  directional conviction, and phase-5 shows bearish_flow has a 28.6% historical hit-rate in
  this tape. The trade already (a) sizes to starter, (b) is defined-risk, and (c) invalidates
  on two closes below $10.50 + an accumulation→distribution flip — so the contradiction is
  bounded. No further downgrade required beyond the debate down-shift already applied.

## Data-quality flags

- **phase-0 spot price error (corrected).** Phase-0 intake noted "PATH trades near $17"
  (misreading the 2026-05-29 $17 lottery call as a spot-level signal). Phase-0.5 corrected
  this to **~$10.99** (DP avg $10.95), and every downstream phase uses the correct ~$11 spot.
  The error did not propagate. Flag for the calibration loop: intake should not infer spot
  from an unusual-volume strike.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. **[DP:block_stratified]** "block buy_ratio 1.0, $13.95M, zero sells" → resolves in
   phase-2-dark-pool.md §Tier breakdown (block tier buy_ratio 1.00, $13.95M, 3 trades). ✓
2. **[SENT:short_interest]** "~28–31% of float short, ~5.2 DTC" → resolves in
   phase-7c-sentiment.md §Short interest & borrow (MarketBeat 31.49% / Fintel 28.48%). ✓
3. **[HIST:vrp]** "VRP +0.4367 (IV30d 98.7% vs realized 55%)" → resolves in
   phase-5-historical.md §IV regime (VRP +0.4367, PREMIUM_SELLING). ✓
(Also confirmed [STRUCT:gex] $11 wall +$20.5M and [DEBATE:bear_residual] 0.65 ≥ 0.55 resolve.)

## Sanity checks

- ✓ All phase files present: phase-0, **0.5**, 1, 2, 3, 4, 5, 6, 7, **7b**, **7c**, 8, **8b**, 9, 10, decision.json.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (6 in the citations summary).
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ ≥1 directional (06-18 $11/$12.5 call debit spread) + ≥1 defined-risk (06-18 iron condor).
- ✓ Sizing math shown; Kelly `p` = conviction-bin fallback (justified: `win_rate_source=null`,
  dark_pool_accumulation backtest 0 signals), capped, debate-adjusted to 0.55.
- ✓ All five risk gates evaluated in phase-9: fundamentals (CONFIRM), sentiment/crowd
  (CONFIRM, CROWDED_SHORT), correlation (soft-watch, no cut), rotation (aligned), debate
  (disconfirmed → cut). Phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected (starter size, no top-of-band).
- ✓ Structures sized to the ±11.8% expected move; `expected_move` present in decision.json
  (front_expiry_pct 11.8, abs 1.30) and a single-catalyst gap does not exceed either max loss.
- ✓ decision.json exists and **passes validate_decision.py** (`context`, `expected_move`,
  `gates.sentiment` fields present; re-validated after backfilling confluence_score 59 /
  recommended_bin 0.65 — see below).

## Final auditor note

The run is **internally consistent and ready for action**. The central tension (bearish
options tape vs dark-pool accumulation) is genuinely resolved rather than papered over —
phase-3's buy-write read and phase-7c's ~30% short interest convert the "bearish flow" into
short-hedging/overwriting, and the desk + debate correctly converge on a **small, defined-
risk, neutral-to-mildly-long vol-harvest** into a binary event rather than a directional bet.
The honest residual risk is the one the bear named and phase-9 carries: an unseeable 05-28
guide over a negative-GEX air pocket below $10.50 — appropriately handled by defined-risk
wings and a two-close-below-$10.50 invalidation. No phase-9 revision required.
