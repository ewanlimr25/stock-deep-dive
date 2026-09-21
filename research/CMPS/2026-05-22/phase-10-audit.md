# Phase 10 — Audit & Confidence Score

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Inputs audited:** phase-0 through phase-9 (incl. 0.5, 7b, 7c, 8b) + decision.json

## Summary

**Confluence score: 60 / 100** (band 50–64 → **recommended bin 0.65**). **Phase-9 actual
bin: 0.65 → MATCH.** The run is **internally consistent** and the central apparent
contradiction (net-selling flow vs a bullish thesis) is *explicitly reconciled* across
phases, not papered over: phase-1's bid-side call selling is the **closing leg of phase-3's
bullish roll-up-and-out**, and phase-2's dark-pool accumulation confirms the underlying is
bought, not distributed. **One formal contradiction** (phase-1 raw flow) and one watch-item
(phase-7 price_vs_flow divergence) are logged. All 3 spot-checked citations resolve. The
score lands mid-band — a *genuinely mixed-to-mildly-constructive* setup — which the blueprint
honestly reflects: RANGE bias, 0.65 conviction, ~0.6% defined-risk size after three gates
fired. Ready for action as a small, defined-risk, optionality-into-Q3 position.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **−** | Net-selling tape: `net_flow −$275.6k`, bid-side calls 2:1 sold `[FLOW:aggressor_ex0dte]` — raw flow does not confirm the bull thesis (reconciled only via phase-3 OI). |
| 2 — dark pool | **+** | ACCUMULATION: large-tier `buy_ratio 0.839`, buy/sell 5.22 `[DP:block_stratified]` — but small N / buying into supply at the high. |
| 3 — OI | **+** | Bullish **roll-up-and-out**, far-call OI **+3,820**, Jul $12 bought `[OI:position_rolls]` — core constructive signal (modest size, $10 hedge tempers). |
| 4 — structure | **+** | POSITIVE gamma pin + DEX +10.8M supportive bid `[STRUCT:dex]`; caps upside but floors the range. |
| 5 — historical | **+** | VRP **−0.7132** (IV 75% vs realized 146%) → premium-buying favours the long-optionality structure `[HIST:vrp]`. |
| 6 — macro | **++** | Two positive Phase 3 TRD trials + WH EO + NDA Q4 + runway 2028, Street $14–22 `[MACRO:CMPS_2026]` — strongest pillar (regime headwind noted). |
| 7 — insights | **0** | Mixed: ACCUMULATION + COVERED_CALL constructive `[INSIGHT:institutional_accumulation]` vs price_vs_flow DIVERGENCE + confluence-absent — net neutral. |
| 7b — fundamentals | **+** | CONFIRM, 0 contradictions: current ratio 3.32, D/E 0.15, funded to 2028 `[FUND:currentRatioQuarterly]`. |
| 8 — agents | **+ (4/4 align, +8)** | 3 RANGE + 1 constrained-LONG, **0 bearish** — all align with the constructive-range bias (earnings-scout skipped). |

**Context modifier (phase-0.5):** `unusual_verdict = GENUINELY_UNUSUAL` → **no cap** on
phases 1–2 (the edge is in the data, not inflated by a busy-name artifact).

**Raw score (symmetric):** (−7 +7 +7 +7 +7 +15 +0 +7) + 8 = **51**
**Base score:** round((51 + 130) / 260 × 100) = **70 / 100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (CAUTION; CROWDED_LONG) · VETO penalty: 0 (not a veto)
**Confluence_score:** 70 − 5 − 5 = **60 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.65** → **MATCH**

> Reconciliation note: phase-9 pre-estimated confluence ≈65 (top of the 0.65 band / bottom
> of 0.75) and reached 0.65 via the debate down-shift; phase-10's exact score (60) lands
> directly in the 0.65 band. **Both paths converge on 0.65 — no conflict.**

## Contradictions

- **phase-1 (flow): the day's aggregate flow is net-bearish (−$275.6k, calls sold 2:1)
  while the blueprint is bullish-biased.** — *Resolution: already reconciled* — phase-3 shows
  the selling is the closing leg of a bullish roll-up-and-out (far-call OI +3,820) and phase-2
  DP is accumulating (0.839), so it is *not* distribution. **Tighten invalidation** (the plan
  already does: exit on cumulative premium net-bearish 3 consecutive sessions / DP flip to
  distribution) and **do not add to the position unless lit flow confirms** with ask-side buying.
- **phase-7 (insights), scored 0 — watch-item, not a hard contradiction:** the
  `price_vs_flow DIVERGENCE` (+114% price vs bearish flow) is a genuine near-term reversal/
  consolidation flag. — *Resolution: wait for confirmation* — the plan correctly responds by
  entering on the $11-wall pullback (not chasing) and keeping size tiny; a sustained close
  >$12.20 on >2× volume is the datapoint that would clear the divergence and flip RANGE→LONG.

## Citation failures

_None._ Spot-checked 3 of phase-9's thesis citations:
1. `[DP:block_stratified]` buy_ratio 0.839 → **resolves** (phase-2 §Tier breakdown: "large-tier buy_ratio 0.839"). ✓
2. `[OI:position_rolls]` far-call OI +3,820 → **resolves** (phase-3 §Closing/roll: "far_oi_change +3,820"). ✓
3. `[HIST:vrp]` VRP −0.7132 → **resolves** (phase-5 §IV regime: "VRP −0.7132 (IV30d 0.7495 − realized 1.4627)"). ✓

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9) + this audit.
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (6: DP, OI, HIST, MACRO, INSIGHT, DEBATE).
- ✓ Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- ✓ ≥1 directional (long Aug $12 call) + ≥1 defined-risk (Aug $12/$16 call debit spread).
- ✓ Sizing math shown; Kelly `p` = phase-5 win-rate (p_raw 0.875 → N-capped 0.85), contamination caveat documented.
- ✓ All five risk gates evaluated: fundamentals CONFIRM (no-op), **sentiment CAUTION (cut)**,
  **correlation cluster CMPS/RDDT 0.746 (cut)**, sector neutral (no-op), **debate disconfirmed
  (down-shift + cut)** → final ≈0.6%.
- ✓ Phase-0.5 `unusual_verdict = GENUINELY_UNUSUAL` reflected (no-op on size; no top-of-band inflation).
- ✓ Structures sized to front-expiry expected move (±13.95% / ±$1.65); `expected_move` in JSON; defined-risk so a catalyst gap ≤ pre-paid debit.
- ✓ `decision.json` exists and **passes `validate_decision.py`** (incl. `context`, `expected_move`, `gates.sentiment` fields); confluence_score 60 + recommended_bin 0.65 backfilled.

## Final auditor note

The run is **internally consistent and ready for action**: the one structural contradiction
(net-selling flow vs a bullish thesis) is explicitly and correctly reconciled as a roll, the
score sits honestly mid-band (60 = mixed-to-mildly-constructive), and phase-9's 0.65 bias /
~0.6% defined-risk sizing faithfully reflects a *de-risked-but-already-priced, crowded,
dealer-pinned* name where the edge is cheap optionality into the Q3 catalyst, not a near-term
chase. No phase requires revision; the chief residual risk the desk must watch is the
**price_vs_flow divergence / 52-week-high crowding** resolving into a pullback before the Q3
binary arrives — which the pullback-entry plan and the $10/$9.02 invalidation already manage.
