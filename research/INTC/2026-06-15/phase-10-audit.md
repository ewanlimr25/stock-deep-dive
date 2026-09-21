# Phase 10 — Audit & Confidence Score

**Ticker:** INTC
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T01:24:55Z
**Dominant bias audited:** RANGE (phase-9)

## Summary

**Confluence score 68/100 → recommended bin 0.75; phase-9 actual bin 0.55 →
MISMATCH (by design, phase-9 more conservative).** The run is **internally
consistent**: every signal phase coheres around the *same* conclusion — a euphoric,
extended name whose flow has stopped confirming price, capped by positive-gamma
mean-reversion at $130. The high confluence reflects that **coherence**, not a
directional edge: the rubric's directional-bin mapping over-translates a tightly-agreed
*RANGE* read into an inflated 0.75 directional bin, while phase-9 correctly drove
conviction to the **0.55 floor** because three downside gates fired (7b CAUTION, 7c
CAUTION, 8b disconfirmed) on a BUSY_NAME_NORMAL_DAY. **No phase scored negative
against the range bias** (0 contradictions); the residual tensions are *break-risks*,
not contradictions. The blueprint is ready for action **as written** — a minimal
(0.6%) defined-risk, wait-for-FOMC plan.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Two-way, net-flat tape supports range: `net_flow −$1.16M`, ask-call $80.6M ≈ bid-call $79.6M [FLOW:insights_deep_dive] (capped at + by BUSY_NAME_NORMAL_DAY) |
| 2 — dark pool | **+** | Accumulation-leaning but suggestive — mega `buy_ratio 0.583` + ascending shelves build the *dip-bid floor* of the range [DP:block_stratified] (capped at +) |
| 3 — OI | **+** | The walls *define* the range: `$130 call_wall_resistance` (+1.7%) over `$110 put_wall_support` [OI:oi_by_strike] |
| 4 — structure | **++** | Range core: regime POSITIVE, largest gamma pin `$130 (+$15.3M)`, dealer dip-bid, mean-reverting [STRUCT:gex] |
| 5 — historical | **+** | Extension + cap supports mean-reversion: +246.5% YTD, target $99.98 (−22%), VRP −0.085 premium-buying [HIST:vrp][HIST:target fz] |
| 6 — macro | **+** | Regime literally counsels range: "half size, defined-risk, iron condors in range" [MACRO:MarketRegime]; sector tailwind is the break-risk |
| 7 — insights | **++** | Range core: conviction-matrix MIXED 5.7% + explicit price-vs-flow DIVERGENCE [INSIGHT:price_vs_flow] |
| 7b — fundamentals | **0** | NEUTRAL — improving earnings (4/4 beats) offset by stretched valuation (11.9× sales); tier CAUTION (not VETO) [FUND:earnings_surprises] |
| 8 — agents | **+ (4/4 align)** | Unanimous non-directional: 3 RANGE + 1 NEUTRAL, all align with the RANGE bias (+2 each = +8; earnings-scout MISSING) [AGENT:desk] |

**Raw score (symmetric):** 65 (phases) + 8 (desk) = **+73**
**Base score:** round((73 + 130) / 260 × 100) = **78/100**
**Sentiment penalty (phase-7c):** −5 (tier_adjustment = CAUTION)
**Debate penalty (phase-8b):** −5 (disconfirmed = true; bull_residual 0.55 vs bear_residual 0.65)
**Confluence_score:** 78 − 5 − 5 = **68/100**
**Recommended bin:** **0.75** (65–79 band)
**Phase-9 actual bin:** **0.55** — **MISMATCH (phase-9 deliberately more conservative)**

### Why the mismatch is correct, not an error

The confluence rubric is directional; it rewards *agreement-with-the-bias*. A RANGE
bias on which nearly every phase agrees therefore scores high (68) and maps to a high
*directional* bin (0.75) — but a coherent RANGE read is not a license for a large
position. Phase-9 correctly let the **three downside gates** (7b CAUTION → cut, 7c
CAUTION → cut, 8b disconfirmed → bin −1 + cut) and **BUSY_NAME_NORMAL_DAY** drive both
the **0.55 conviction floor** and the **0.6% size**. An upward move to the 0.75
recommended bin is **forbidden** by the sizing rubric here (gates fired + busy-name
context). The auditor **accepts 0.55** and flags the rubric's over-translation of a
range read, not a phase-9 defect. (`decision.json` backfilled: `confluence_score 68`,
`recommended_bin 0.75`.)

## Contradictions

**None** — no phase scored `-` or `--` against the RANGE bias; the chain is
internally consistent. The residual **break-risks** (not contradictions, logged for
completeness) and their resolutions:

- **Upside-break risk** — the 5-day bullish sweep persistence ($1.23B, consistency
  1.0) [FLOW:sweep_persistence] + Tech sector inflow (+$7.78B, persistence 1.0) +
  foundry catalyst (BofA $135) argue for a continuation that would break $130.
  **Resolution: wait for confirmation** — a two-daily-close break >$132 on volume
  converts the range to a momentum long (already phase-9's upside invalidation).
- **Either-way-break risk** — realized vol 94% [HIST:vrp] + FOMC 6/17 inside OPEX +
  negative vanna make a violent range-break in *either* direction plausible.
  **Resolution: tighten via defined risk + minimal size** — phase-9 already caps loss
  at the premium and sizes 0.6%, and recommends trading the FOMC *resolution*, not the
  anticipation.

## Citation failures

**None.** Spot-checked 3 of phase-9's thesis citations:
1. `[FLOW:insights_deep_dive] net_flow −$1.16M` → phase-1 §Whole-tape: bull $229,872,054
   − bear $231,034,898 = −$1,162,844 ✓ **resolves.**
2. `[STRUCT:gex] largest gamma pin $130 (+$15.3M)` → phase-4 §GEX per-strike: $130 =
   +15,325,541 ✓ **resolves.**
3. `[INSIGHT:price_vs_flow] DIVERGENCE` → phase-7 §Price vs flow: `divergence=true`,
   "Price up 33.5% but options flow bearish" ✓ **resolves.**

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + `decision.json`.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (6 listed).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✓ ≥1 directional (call debit spread 125/135) + ≥1 defined-risk (call credit spread 132/140).
- ✓ Sizing math shown; Kelly p = phase-5 win-rate (p_raw 1.00, N=7 → capped 0.75), not the bin.
- ✓ All five gates evaluated: fundamentals CAUTION, sentiment CAUTION (crowd CROWDED_LONG),
  correlation none, rotation aligned, debate disconfirmed; **BUSY_NAME_NORMAL_DAY** reflected in sizing.
- ✓ Structures sized to the front-expiry expected move (`expected_move` 6.17% / $7.87 in JSON);
  the FOMC-gap-exceeds-stop case addressed via defined-risk (max loss = premium).
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. `context`,
  `expected_move`, `gates.sentiment` fields) — re-validated after backfill: **OK**.

## Final auditor note

The run is **internally consistent and ready for action**: 14 phases converge on a
single, well-evidenced conclusion — INTC is a euphoric +246%-YTD foundry re-rate
whose tape has stopped confirming price, structurally capped at $130 in a
positive-gamma range, with two CAUTION gates and a failed disconfirmation forcing
conviction to the 0.55 floor and size to a 0.6% defined-risk toe. **No revision
required** — the only divergence (confluence-recommended 0.75 vs actual 0.55) is the
sizing rubric correctly over-riding a directionally-inflated confluence number downward
via the fired gates; trade it minimal and let FOMC (6/17) decide the $130 break.
