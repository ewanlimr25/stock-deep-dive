# Phase 10 — Audit & Confidence Score

## Summary

**Confluence score: 62 / 100** (positive-of-mixed) → **recommended conviction bin
0.65**, which **MATCHES** phase-9's actual bin (0.65). The run is **internally
consistent**: the dominant LONG bias is supported by 6 of 8 signal phases plus the
fundamentals CONFIRM, opposed by exactly 2 (dark-pool + the composite engine that
reads off it) — and phase-9 honestly carries that opposition as its #1 key risk, its
invalidation, and the reason for a defined-risk, deviated-down-to-1.5% size. **2
contradictions logged** (phase-2, phase-7), both the same underlying signal
(institutional distribution), both already mitigated in the plan. No citation
failures. The score sits mid-band — this is a *real but thin-edge* long, correctly
sized small, not a high-conviction trade dressed up.

## Confluence scorecard

| Phase | Score | Justification (diagnostic datapoint) |
|-------|-------|--------------------------------------|
| 1 — flow | **+** | 20/20 call sweeps, $26.3M, ~54% ask targeting $200 `[FLOW:sweeps]` — bullish, but tempered to `+` (not `++`) by the 52%-volume-ask / 190C call-writing signature. |
| 2 — dark pool | **−−** | Mega-tier buy ratio **0.017**, $1.05B ~90% sell into the pop `[DP:block-stratified]` — strong contradiction of a long. |
| 3 — OI | **+** | $200 call wall net **+58,153 OI** + call OI > put every tenor `[OI:oi-by-strike]`; thin 191→185 floor keeps it `+` not `++`. |
| 4 — structure | **+** | Positive gamma **+$50.4M** (node $190), DEX +$585.6M dealers buy dips `[STRUCT:gex]`/`[STRUCT:dex]` — stabilizing, supports the long. |
| 5 — historical | **+** | `bullish_flow` **60% (5d) / 72.9% (10d)**, avg +5% `[HIST:signal-backtest]`; held to `+` because the win-rate is universe-pooled & `dark_pool_accumulation`=0 signals. |
| 6 — macro | **+** | Technology **#1 sector inflow, persistence 1.0, 5 sessions** `[MACRO:sector_flow_persistence]`; narrow 36% breadth caveat caps at `+`. |
| 7 — insights | **−** | Composite engine scenario **DISTRIBUTION, 32.9%** `[INSIGHT:conviction-matrix]` — mild contradiction (reads off phase-2). |
| 7b — fundamentals | **++** | **CONFIRM**: +23.9% beat (3rd accelerating), fwd P/E 12.4 `[FUND:earnings_surprise]`/`[FUND:forwardPE fz]` — strong quality support. |
| 8 — agents | **+ (3/5 align)** | 3 LONG (+2 each) / 2 NEUTRAL-lean-long (−2 each) → net **+2**; 0 short. |

**Raw score (symmetric):** +30 (phases +28, desk +2)
**Base score:** round((30+130)/260×100) = **62 / 100**
**Context modifier (phase-0.5):** `GENUINELY_UNUSUAL` → no cap on phases 1–2 (applied; phase-1 held at `+` on its own merits, not the context cap).
**Debate penalty (phase-8b):** −0 (not disconfirmed; bull 0.65 vs bear 0.55)
**Sentiment penalty (phase-7c):** −0 (tier_adjustment NO-CUT/CONFIRM, crowd BALANCED)
**Confluence_score:** **62 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.65** — ✅ **MATCH**

## Contradictions

- **phase-2 (dark pool):** Institutional cash tape is ~90% sell ($1.05B mega+block,
  buy-ratio 0.017) into the +8.5% pop — directly opposes the long. **Resolution:
  already applied** — phase-9 tightened invalidation to a sustained close below $185,
  chose a **defined-risk** structure (debit spread caps gap risk), and deviated size
  **down to 1.5%**. Phase-7b's reframing (no fundamental rot to front-run → mechanical
  profit-taking) keeps it a risk, not a thesis-killer. *Wait-for-confirmation
  datapoint:* whether DP sell pressure persists on 5/30+ or fades.
- **phase-7 (insights):** Composite engine voted DISTRIBUTION (32.9% confidence) —
  but this is a *re-expression* of phase-2 (the matrix reads the same dark-pool
  tape), not an independent contradiction. **Resolution: down-weight as
  non-independent**; the single underlying signal (institutional selling) is already
  the carried #1 risk. No separate action.

(Both contradictions trace to one signal — institutional distribution — so the true
independent-contradiction count is **1**, double-counted by the scorecard's
phase-by-phase mechanic. Noted so the score isn't misread as two separate problems.)

## Citation failures

Spot-checked 3 phase-9 thesis citations:
1. `[FUND:earnings_surprise]` "+23.9% beat" → resolves: phase-7b earnings table,
   period 2026-03-31 actual 3.81 vs est 3.075, surprise +23.9%. ✅
2. `[FLOW:sweeps]` "20/20 call sweeps, $26.3M, targeting $200" → resolves: phase-1
   sweeps table, 20 contracts 100% calls, $26.3M, $200 magnet. ✅
3. `[DP:block-stratified]` "mega buy-ratio 0.017, $1.05B ~90% sell" → resolves:
   phase-2 block-stratification table, mega 0.017 / block 0.098, $1.05B conviction
   tiers. ✅

**No citation failures.**

## Sanity checks

- ✅ All phase files present: 0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9, 10 + decision.json.
- ✅ Phase-9 cites ≥3 distinct upstream datapoints (8 distinct tags in the thesis/citations).
- ✅ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- ✅ ≥1 directional (190/200 call debit spread) + ≥1 defined-risk (180/175 put credit spread) structure present.
- ✅ Sizing math shown; Kelly `p` = phase-5 backtest win-rate (0.60, source=backtest, N=70), not the bin.
- ✅ All five risk gates evaluated in phase-9 sizing block (fundamentals CONFIRM / sentiment NO-CUT / correlation soft-watch / rotation aligned / debate not-disconfirmed) + phase-0.5 `GENUINELY_UNUSUAL` reflected (no-op, edge in p).
- ⚠️ Structures sized to expected move: the **6/18 expected move (~±10.7% from IV30d
  0.458)** comfortably contains the $190→$200 (~5%) spread width — but the
  `expected_move` field in decision.json carries the **daily** implied move (0.52%),
  not the front-*expiry* move. Minor schema-population nuance (the daily figure is
  what the screener exposes as `implied_move_perc`); the *structure* is correctly
  sized to the multi-week move per phase-9 §Expected move. Flagged, non-blocking.
- ✅ decision.json exists and passes `validate_decision.py` (OK), incl. context /
  expected_move / gates.sentiment fields.

## Final auditor note

The run is **internally consistent and ready for action as a small, defined-risk
tactical long**: the confluence score (62) and the recommended bin (0.65) match
phase-9 exactly, the lone real contradiction (institutional distribution) is
explicitly carried as the #1 risk + invalidation rather than buried, and sizing was
correctly deviated *down* (not up) to reflect the thin base-case reward:risk the
debate exposed. No revision required; the only watch-item is the `expected_move`
field convention (daily vs front-expiry), which does not affect the structure
selection or sizing.
