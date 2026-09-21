# Phase 10 — Audit & Confidence Score

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T21:18:00-04:00
**Dominant bias audited:** LONG (lean), conviction 0.55

## Summary

Confluence score **45/100** — a **genuinely mixed** setup, tilted slightly positive by
the darkpool accumulation but fought by an inert price, insider selling, and a held bear
disconfirmation. The score maps to the **0.55–0.65** conviction band; phase-9 chose
**0.55**, which **MATCHES** (correctly at the low end, given the disconfirmation and two
CAUTION gates). **Two contradicting phases** (5 historical, 7b fundamentals). All three
thesis citations resolve. The run is **internally consistent and honest** — it does not
overstate a $644M print that moved price zero; it sizes to a starter and expresses
defined-risk. Ready for action as a starter/toe-in, with tight, falsifiable invalidation.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **0** | Genuinely mixed: net_flow −$167k, largest sweep a $12 LEAP put; call-heavy premium offsets. `[FLOW:insights_deep_dive]` |
| 2 — dark pool | **+** | Mega buy_ratio 1.000, $644M, zero sell `[DP:block_stratified]` — **would be `++`; capped at `+` by BUSY_NAME_NORMAL_DAY context modifier** (see note). |
| 3 — OI | **+** | Chain 43% call-skewed (Jan-27 LEAP calls) `[OI:term_structure]`; near-term capped by $13 covered-call writing. |
| 4 — structure | **0** | Long-gamma **range** (ZGL $5.70), boxed $11–$13 `[STRUCT:gex]`; DEX +34.4M bid is supportive but the regime is directionally neutral. |
| 5 — historical | **−** | Price inert ($11.72→$11.85/30d) `[HIST:trend]`, VRP premium-selling, signal-backtest n=0 — no measurable directional edge. |
| 6 — macro | **+** | Fed easing + Tech persistence INFLOW score 1 `[MACRO:SectorPersistence_2026-07-13]`; tempered by weak breadth. |
| 7 — insights | **+** | conviction-matrix DIRECTIONAL_LONG + ACCUMULATION 1.58 `[INSIGHT:institutional_accumulation]`, low confidence. |
| 7b — fundamentals | **−** | CAUTION: insiders persistent net sellers (−9.6M sh Mar-26, MSPR −100 Jul-26) `[FUND:insider_MSPR]` — contradicts the accumulation thesis. |
| 8 — agents | **0** | 2 LONG (+2 ea) / 2 RANGE (−2 ea) / 0 SHORT `[AGENT:desk]` → net 0; nobody short, nobody presses. |

**Raw score (symmetric):** 0+7+7+0−7+7+7−7 + (agents 0) = **+14**
**Base score:** round((14 + 130) / 260 × 100) = **55/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed = true; bull_residual 0.65 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** **45/100**
**Recommended bin:** 0.55–0.65 → **0.55**
**Phase-9 actual bin:** **0.55** — **MATCH**

> **Context-cap note.** The BUSY_NAME_NORMAL_DAY modifier caps phases 1–2 at `+`. That
> verdict was about the *options* tape being quiet for the name; the *darkpool* is
> genuinely the anomaly (phase-2, ~15× record). The cap is therefore conservative here —
> absent it, phase-2 = `++` and confluence ≈ 48, still in the same 0.55–0.65 band. The
> mechanical cap is applied as written; the bin is unchanged.

## Contradictions

- **phase-5 (historical):** a $644M accumulation event produced **zero price appreciation over 30 days** and the signal has **no measurable historical edge (backtest n=0, VRP premium-selling)** — this is the core tension with a directional long. **Resolution: wait for confirmation** — the block must either re-fire (fresh large-tier buying) or price must clear the $13 gamma wall before pressing; until then, starter-only (already applied).
- **phase-7b (fundamentals):** **insiders are persistent net sellers** (−9.6M sh Mar-2026, MSPR −100 Jul-2026) while the darkpool buyer accumulates — the block may be absorbing insider/offering supply. **Resolution: tighten invalidation** — exit on continued insider selling *plus* a shelf break; the one-step size cut is applied and the strongest-bear-point (supply-absorption) is carried into invalidation.

## Citation failures

None. Spot-checked 3 of phase-9's thesis citations:
1. `[DP:block_stratified]` buy_ratio 1.000 / 54.6M sh / $644.2M / zero sell → **resolves** in phase-2-dark-pool.md §Tier breakdown ✓
2. `[HIST:trend]` price 11.72 → 11.85 over 30d → **resolves** in phase-5-historical.md §Multi-day trend ✓
3. `[SENT:short_float]` ~28–32% of float short, ~5 dtc → **resolves** in phase-7c-sentiment.md §Short interest ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + decision.json + this audit.
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 in the citations summary).
- [✓] Conviction bin ∈ {0.55, …, 0.95} → 0.55.
- [✓] ≥1 directional ($12/$13 call debit spread) + ≥1 defined-risk ($11/$10 put credit spread).
- [✓] Sizing math shown; Kelly p = conviction-bin fallback (win_rate_source=null, n=0) — justified.
- [✓] All five risk gates evaluated: fundamentals CAUTION (fired), sentiment CAUTION (fired), correlation none, rotation aligned, debate disconfirmed (fired). phase-0.5 BUSY_NAME_NORMAL_DAY reflected (no top-of-band; final 1.0% starter).
- [✓] Structures sized to front-expiry expected move (±5.3% / ±$0.63; `expected_move` in JSON); Aug-21 avoids the 09-03 earnings binary.
- [✓] `decision.json` exists and passes `validate_decision.py` (OK, incl. context/expected_move/gates.sentiment; confluence_score 45, recommended_bin 0.55 backfilled).

## Final auditor note

The run is **internally consistent and ready for action as a starter-size, defined-risk
long** — every downside filter (inert price, insider selling, disconfirmation, weak
regime, quiet-for-the-name context) is surfaced and correctly cuts size rather than being
argued away, and the single dominant signal (the $644M unattributed block) is neither
inflated nor dismissed. Phase-9 needs no revision; the one thing that would materially
re-rate this blueprint is **attribution of the 07-09 block** — a strategic-buyer
confirmation upgrades it toward 0.65–0.75, an offering/13D disclosure invalidates it.
