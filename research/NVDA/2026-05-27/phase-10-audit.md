# Phase 10 — Audit & Confidence Score

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:28:00Z
**Dominant bias audited:** RANGE (capped-upside with bearish tilt)

## Summary

Confluence score **64/100** → recommended conviction bin **0.65**, which
**MATCHES** phase-9's actual bin (0.65). The run is **internally consistent**:
the flow / OI / structure stack (phases 1, 3, 4) all point to a dealer-defined
capped-upside ceiling at $215–$220, and the UW composite independently labels it
`COVERED_CALL` (phase-7) — strong agreement on *geometry*. The score is held
below 70 by **two honest contradictions** against any *directional* read: the
`bearish_flow` signal's 37.5% historical win-rate (phase-5) and the pristine,
analyst-loved fundamentals (phase-7b CAUTION). Both are correctly reflected in
phase-9's *starter* sizing and defined-risk structures. No gate-penalty applied
(phase-7c CONFIRM, phase-8b not disconfirmed). All three spot-checked citations
resolve. `decision.json` validates. **Ready for action as a small, defined-risk
fade — not as an outright short.**

## Confluence scorecard

Context modifier applied: phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` →
phases 1 & 2 capped at `+` (cannot score `++`).

| Phase | Score | Justification (datapoint) |
|-------|:-----:|---------------------------|
| 1 — flow | **+** | Net bearish: `net_flow -$66.25M`, bid-sweep $215.9M > ask $155.9M, 5/5 bearish sweep persistence $4.55B [FLOW:sweep_persistence]. (Would be `++`; capped at `+` by BUSY_NAME.) |
| 2 — dark pool | **0** | Mega buy_ratio 0.964 but all after-hours $212.60 MOC prints; intraday tiers balanced (0.537/0.515) [DP:block_stratified] — mechanical, neither confirms nor refutes. |
| 3 — positioning | **+** | 3:1 bearish OI build; 0DTE $215C +20,954 written on the bid; put hedges at $200 [OI:smart_positioning]. |
| 4 — structure | **++** | Long-gamma walls $215/$217.5/$220 = +$146M ceiling, K212.5 = −$85.7M flip, vanna-selling in falling IV [STRUCT:gex][STRUCT:vanna_charm]. |
| 5 — historical | **−** | `bearish_flow` win_rate **0.375** (n=8) — below the 0.45 edge threshold; the directional signal historically loses [HIST:signal_backtest]. |
| 6 — macro | **+** | Technology −$433.5M largest sector outflow + breadth 37.1% bullish align with the bearish tilt [MACRO:sector_rotation_2026-05-27]. |
| 7 — insights | **+** | `conviction_matrix = COVERED_CALL` "yield enhancement, capping upside"; absent from signal-confluence both directions [INSIGHT:conviction_matrix]. |
| 7b — fundamentals | **−** | `CAUTION`, fundamental_signal BULLISH (PEG 0.39, op margin 64%, +43.8% target) — contradicts a directional bearish thesis on the underlying [FUND:peg fz]. |
| 8 — agents | **+ (4/4 align, +8)** | 3 RANGE (accumulation-hunter, contrarian-scanner, risk-monitor) + 1 SHORT (sweep-tracker), all on the bearish-tilt/capped side; earnings-scout skipped (earnings > 30d). |

**Raw score (symmetric):** +7 + 0 + 7 + 15 − 7 + 7 + 7 − 7 (eight phases = +29) + 8 (phase-8) = **+37**
**Base score:** round((37 + 130) / 260 × 100) = **64/100**
**Debate penalty (phase-8b):** 0 — *not* disconfirmed (bull_residual 0.75 > bear_residual 0.65)
**Sentiment penalty (phase-7c):** 0 — `CONFIRM` (no CAUTION/VETO)
**Confluence_score:** **64/100**
**Recommended bin:** **0.65** (50–64 band)
**Phase-9 actual bin:** **0.65** → **MATCH**

## Contradictions

- **phase-5 (historical):** the `bearish_flow` signal's empirical win-rate is
  0.375 (n=8) — *below a coin flip* — so the directional bear edge is
  negative-expectancy [HIST:signal_backtest]. **Resolution: already applied** —
  phase-9 used 0.375 as Kelly `p`, hit the SHORT-side floor, and sized to
  *starter* (0.75%); the trade leans on structure/range, not on the signal's
  directional payoff. No further action needed.
- **phase-7b (fundamentals):** business quality is exceptional and the Street is
  strong-buy (+43.8% target) — this contradicts any outright short
  [FUND:peg fz][SENT:recom fz]. **Resolution: already applied** — phase-7b
  CAUTION cut one size step, and phase-9 chose a *capped-upside / range* framing
  with defined-risk structures rather than a naked short. The `fade` (plan-B)
  entry explicitly flips long above $220.50 to respect the upside.

Both contradictions are *constructive* — they shaped the trade into the
defined-risk, starter-size form it took, rather than being ignored.

## Citation failures

Spot-checked 3 of phase-9's thesis citations — **all resolve**:

1. `[INSIGHT:conviction_matrix]` "COVERED_CALL — yield enhancement, capping
   upside" → resolves to phase-7-insights.md §Conviction matrix (confidence
   19.9%, explanation verbatim). ✓
2. `[FLOW:sweep_persistence]` "dominant_direction bearish, consistency 1, 5/5,
   $4.55B" → resolves to phase-1-flow.md §Key signals + §Tool calls. ✓
3. `[STRUCT:gex]` "long-gamma walls 215/217.5/220 = +$146M; K212.5 = −$85.7M;
   ZGL $138.94" → resolves to phase-4-structure.md §GEX (sum 43.79+26.96+75.66
   = $146.4M; K212.5 −$85.74M; ZGL $138.94). ✓

No citation failures.

## Sanity checks

- [✓] All phase files present: phase-0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- [✓] ≥1 directional (put debit spread 210/200) + ≥1 defined-risk (iron condor) structure.
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate 0.375 (n=8, backtest), not a bin fallback.
- [✓] All five risk gates evaluated: fundamentals CAUTION (fired), sentiment CONFIRM, correlation none, sector_rotation aligned, debate not disconfirmed.
- [✓] Phase-0.5 `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected — final size sits below the Kelly suggestion, off top-of-band.
- [✓] Structures sized to front-expiry expected move (±1.94% / $4.12); `expected_move` block present in JSON.
- [✓] `decision.json` exists and passes `validate_decision.py` (incl. `context`/`expected_move`/`gates.sentiment`).
- [✓] Disclaimer present at top of phase-9.

## Final auditor note

The run is internally consistent and ready for action: every directional signal
(flow, OI, structure, agents) agrees the upside is capped at $215–$220 while the
two dissenting phases (5 historical edge, 7b fundamentals) were correctly
absorbed into a *starter-size, defined-risk* expression rather than ignored. The
single most important thing to watch is the phase-8b `strongest_bear_point` — a
CPI/FOMC vol re-pricing could flip the cheap-IV complacent-skew book and gap NVDA
*up* through the short-call zone; the $220.50 invalidation and the long plan-B
fade exist precisely for that tail.
