# Phase 10 — Audit & Confidence Score

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Dominant bias (phase-9):** RANGE @ conviction 0.55

## Summary

**Confluence score: 51 / 100** — perfectly-mixed, leaning *slightly* toward the RANGE read.
The structural lane (long-gamma pin + $6 max-pain) strongly supports the range thesis, but the
bullish flow (phase-1), the DIRECTIONAL_LONG/divergence insight (phase-7), and the adverse
risk-off macro (phase-6) each pull against a clean range — and the bull/bear debate was
**disconfirmed (bear 0.75 ≥ bull 0.55)**, costing −5. The raw band (51 → 0.65) is correctly
**down-shifted one bin to 0.55** by the disconfirmed-debate gate, **matching phase-9's chosen
bin.** Three contradictions logged (phases 1, 6, 7); all three are the *expected* tension of a
counter-trend bullish signal pinned inside a range, and phase-9 already neutralised them by
taking directional size to **0%** (watch-only) with carry-only defined-risk structures. The run
is **internally consistent and self-aware** — the audit endorses it.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|----------------------------|
| 1 — flow | **−** | Bullish but a single small campaign — net_flow only **+$441,792**, one strike, counter-trend `[FLOW:insights_deep_dive]`; a directional signal that mildly *contradicts* the range thesis. |
| 2 — dark pool | **+** | Mild accumulation **buy_ratio 0.629, no mega blocks**, clustered AT spot $5.95 `[DP:block_stratified]` — a value-area battleground = range-supportive. |
| 3 — OI | **0** | Call-heavy but **far-dated** (Jan-27 LEAP 33%, July 27%) with **no fresh OI build ≥500 today** `[OI:term_structure, biggest_increases]` — positioned, not moving; neutral to a 1-4w range. |
| 4 — structure | **++** | **GEX POSITIVE/long-gamma (ZGL $3.50) + July max-pain $6.00** `[STRUCT:gex, max_pain]` — textbook pin; the strongest agreement with RANGE. |
| 5 — historical | **+** | **Long-gamma 30/30 sessions, no flip** + dead **20% backtest** `[HIST:gex_time_series, signal_backtest]` — kills the directional edge and confirms range-suppression. |
| 6 — macro | **−** | **TRANSITIONAL risk-off, Industrials −$61.6M out persistence 1.0, β2.31** `[MACRO:MarketRegime, sector_flow]` — tilts the risk *down/breakdown*, against a balanced range. |
| 7 — insights | **−** | **DIRECTIONAL_LONG (34.8%) + price-vs-flow DIVERGENCE** `[INSIGHT:conviction_matrix, price_vs_flow]` — a directional-up read (low-conf) that contradicts range. |
| 7b — fundamentals | **0** | **CONFIRM** (rev +50%, 4/4 beats, target +133%) `[FUND:earnings, recom fz]` — bullish long-horizon but a no-op for the 1-4w range timeframe. |
| 8 — agents | **+ (4/4 non-MISSING align, +8)** | **3 RANGE + 1 NEUTRAL, 0 directional** `[AGENT:phase-8]` — the desk endorses the non-directional read. |

Context modifier (phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL`): **no cap** applied to phases
1–2 (the direction is genuinely top-percentile; the small *scale* is already in `p` and the size).

**Raw score (symmetric):** +16  (phases 1–7b = +8, phase-8 = +8)
**Base score:** round((16 + 130) / 260 × 100) = **56 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed — bull_residual 0.55 vs bear_residual 0.75)
**Sentiment penalty (phase-7c):** −0 (tier_adjustment CONFIRM, not CAUTION/VETO)
**Confluence_score:** **51 / 100**
**Recommended bin:** band(51) = 50–64 → **0.65**, then **−1 bin for the disconfirmed-debate gate → 0.55**
**Phase-9 actual bin:** **0.55** → **MATCH** (the gate down-shift is correctly applied, not double-counted)

## Contradictions

- **phase-1 (flow):** bullish single-strike sweep argues mild upside against the RANGE thesis —
  *resolution: tighten invalidation* (phase-9 already does — "tomorrow's OI doesn't confirm the
  $6-Oct build" voids the bull premise) and **wait for confirmation** (a 3-session net-bullish
  cumulative-flow flip) before any long.
- **phase-6 (macro):** adverse risk-off rotation tilts the high-beta name down, not range —
  *resolution: downgrade conviction* (already at the floor 0.55) and keep the **put-debit hedge** as
  the trend-continuation expression; the gate already cut half a step.
- **phase-7 (insights):** DIRECTIONAL_LONG + bullish divergence is a directional-up read —
  *resolution: wait for confirmation*; the divergence is "often early," and phase-4's long-gamma +
  phase-5's 20% backtest say it's premature. Phase-9 takes directional size to 0% pending the
  Aug-12 catalyst.

## Citation failures

Spot-checked 3 of phase-9's thesis citations — **all resolve:**
1. `[FLOW:sweeps]` $871,964 / 6,738 ct / 84.2% ask → **present** in phase-1-flow.md §Sweeps. ✓
2. `[HIST:signal_backtest]` win_rate 0.20 (n=5), avg −0.05% → **present** in phase-5-historical.md §Signal backtest. ✓
3. `[STRUCT:max_pain]` July-OPEX max-pain $6.00 → **present** in phase-4-structure.md §Max pain. ✓

(None failed.)

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10) + `decision.json`.
- ✓ Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → **0.55**.
- ✓ ≥1 directional ($6/$8 call debit spread) + ≥1 defined-risk ($5.5/$4.5 put debit spread).
- ✓ Sizing math shown; Kelly **p = phase-5 win-rate 0.20** (n=5, capped 0.75 → 0.20), raw_kelly −0.143 (negative).
- ✓ All **five** risk gates evaluated in phase-9: fundamentals CONFIRM, sentiment/crowd CONFIRM
  (CROWDED_SHORT), correlation none (0.521 < 0.60), rotation ADVERSE (cut), debate DISCONFIRMED (down-shift+cut).
- ✓ Phase-0.5 `unusual_verdict` reflected (GENUINELY_UNUSUAL = no-op; small scale carried into size).
- ✓ Structures sized to expected move; `expected_move` (2.42% / $0.14) in `decision.json`; debit
  max-loss = debit, so a single Aug-12 earnings gap cannot exceed it.
- ✓ `decision.json` exists and **passes `validate_decision.py` → OK** (incl. `context`,
  `expected_move`, `gates.sentiment`/`crowd_state`).

## Final auditor note

The run is **internally consistent, well-cited, and appropriately self-skeptical**: every
bullish lane (flow, squeeze fuel, analyst targets, cheap vol) is honestly logged, and every one
is correctly overridden by the negative empirical edge (20% backtest), the long-gamma pin, the
adverse macro, and the disconfirmed debate — landing on a defensible **0% directional / watch +
token-carry** call with a 0.55 conviction that matches the confluence band after the debate
gate. **No revision required;** the single actionable watch-item is tomorrow's OI confirmation of
the $6-Oct build and the ~Aug-12 earnings catalyst that would be needed to convert the latent
squeeze into a real trade.
