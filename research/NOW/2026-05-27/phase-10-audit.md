# Phase 10 — Audit & Confidence Score

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T13:54:00Z
**Dominant bias audited:** LONG (trigger-contingent)

## Summary

**Confluence score 53 / 100 → recommended bin 0.65; phase-9 set 0.55** (the
mandated phase-8b debate down-shift) — internally consistent. The run is a
**coherent, honestly-mixed "real setup, no trigger" blueprint.** Two phases
contradict the long (dark pool, UW insights — both centered on the same
*no-accumulation* fact), one macro phase is neutral, and five lean bullish, while
the desk split 2 conditional-long / 1 range / 1 neutral and the debate was
disconfirmed. The score of 53 (barely above perfectly-mixed 50) faithfully
reflects a quality-backed bullish structure that the institutional tape does not
yet corroborate. All 3 spot-checked citations resolve; `decision.json` validates.
**Verdict: internally consistent and ready for action as a small, defined-risk,
trigger-contingent position — not a conviction long.**

## Confluence scorecard

| Phase | Score | Justification (quoted datapoint) |
|-------|-------|----------------------------------|
| 1 — flow | **+** | "call premium $59.4M vs put $17.2M (3.4:1), net delta-notional +$0.36bn" — bullish, but vol_confirmed=NO (0.9× avg) + two-way calls keep it off `++` `[FLOW]` |
| 2 — dark pool | **−** | "dark pool does NOT corroborate the bullish flow… large tier balanced 0.492; mega 'sell' = AH rebalance" — no accumulation `[DP:block_stratified]` |
| 3 — OI | **+** | "biggest build 106C 6/05 +5,436 bought; net OI ~12.5k vs ~9.9k" — mildly bullish, bounded (upside calls written) `[OI:smart_positioning]` |
| 4 — structure | **+** | "short gamma (spot 102.75 < ZGL 104.62) + dealers short calls → buy-hedge bid; $110 wall +7.4M" — bullish-leaning, tempered by negative vanna `[STRUCT:gex]` |
| 5 — historical | **+** | "VRP −0.165 PREMIUM_BUYING + OI building 30 days" — constructive for a debit long despite counter-trend (below 200-SMA) `[HIST:vrp]` |
| 6 — macro | **0** | "Fed easing 3.62% + diversifier vs Tech outflow −$433.5M + TRANSITIONAL regime" — tailwinds and headwinds offset `[MACRO:sector_rotation]` |
| 7 — insights | **−** | "conviction-matrix DISTRIBUTION (13.5%); NOW absent from bullish confluence (score 0)" — composite does not endorse the long `[INSIGHT:signal_confluence]` |
| 7b — fundamentals | **+** | "CONFIRM: forward PEG ≈1.0, strong-buy recom 1.35, target $140.63 (+37.7%)" — quality confirms (no veto) `[FUND:metric]` |
| 8 — agents | **0 (2/4 align)** | sweep-tracker +2, risk-monitor +2, accumulation-hunter −2, contrarian-scanner −2 (earnings-scout MISSING) |

**Raw score (symmetric):** +21 (8 phases) + 0 (phase-8) = **+21**
**Base score:** round((21 + 130)/260 × 100) = **58 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.65 = bear_residual 0.65)
**Sentiment penalty (phase-7c):** 0 (CONFIRM, neither CAUTION nor VETO)
**Context modifier (phase-0.5):** GENUINELY_UNUSUAL → no cap on phases 1–2 (note: directional-only, vol_confirmed=NO — already reflected in the `+` not `++` on phase-1)
**Confluence_score:** **53 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **MISMATCH by one bin, JUSTIFIED**: the phase-8b debate-disconfirmation gate mandates a one-bin down-shift (documented in phase-9 §Conviction note). 0.65 − 1 bin = 0.55. Consistent with both rubrics.

## Contradictions

- **phase-2 (dark pool):** the 3.4:1 bullish options tape has **no dark-pool
  sponsorship** — the $162M is a single $102.12 closing-cross pin, intraday large
  tier is balanced (0.492), NOW absent from the block-stratified top-30. →
  **Resolution: tighten invalidation** — exit if laddered DP buying never appears
  *and* the flow sign flips (already in phase-9 signal-invalidation); **wait for
  confirmation** of an accumulation footprint below market before upsizing.
- **phase-7 (insights):** UW composite reads **DISTRIBUTION (13.5%)** and scores
  NOW **0 on bullish confluence** — the engine does not endorse the long. →
  **Resolution: downgrade conviction** (already applied — 0.55); the early tell that
  resolves it is `price-vs-flow` flipping from aligned-bullish to a confirmed
  composite bullish-confluence score >0.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[STRUCT:gex]` ZGL $104.62 vs spot $102.75, $110 wall +7.4M → **resolves** (phase-4 §GEX). ✓
2. `[FUND:metric]` forward PEG ≈1.0, strong-buy 1.35, target $140.63 → **resolves** (phase-7b §Valuation / Forward consensus). ✓
3. `[MACRO:sector_rotation]` Tech −$433.5M, persistence 1.0 → **resolves** (phase-6 §Sector rotation). ✓

## Sanity checks

- ✓ All phase files present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10, decision.json).
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- ✓ ≥1 directional (105/110 call debit spread) + ≥1 defined-risk (100/95 put credit spread).
- ✓ Sizing math shown; Kelly p = phase-5 win-rate 0.857, N-capped to 0.75 (n=7), b=1.625, raw_kelly 0.596, cap 5%, gates → 1.9%.
- ✓ All five risk gates evaluated: fundamentals CONFIRM, sentiment CONFIRM/BALANCED, correlation none (diversifier), **sector rotation ADVERSE (−½ step)**, **debate DISCONFIRMED (−1 step + bin down-shift)**. Context modifier (GENUINELY_UNUSUAL, vol_confirmed=NO) reflected.
- ✓ Structures sized to expected move; `expected_move` (4.07% / $4.15) in JSON; target $110 ≈1.45× the 51-DTE move (noted as rich-edge, mitigated by 50% take at $106).
- ✓ `decision.json` exists, backfilled (confluence_score 53, recommended_bin 0.65), and **passes `validate_decision.py` (OK)**; `context`, `expected_move`, `gates.sentiment`/`crowd_state` fields all present.

## Final auditor note

The run is **internally consistent**: every phase's verdict is reflected in the
score, the two contradicting phases (DP, insights) trace to one honest fact —
*no dark-pool accumulation under the bullish call tape* — and phase-9 correctly
translated a 53 confluence + disconfirmed debate + adverse rotation into a small
(1.9%), defined-risk, **trigger-contingent** long rather than a conviction
position. **Ready for action as specified; do not upsize without (a) a $103.30
break on volume and (b) the appearance of dark-pool accumulation — absent both,
the negative-vanna IV-bleed makes range-decay the base case.**
