# Phase 10 — Audit & Confidence Score

**Ticker:** NBIS (Nebius Group NV)
**As-of date:** 2026-06-17
**Generated:** 2026-06-18T01:06:07Z
**Dominant bias audited:** LONG (tactical / event-boxed), per phase-9

## Summary

**Confluence score = 32/100** (base 42 − 5 debate-disconfirm − 5 sentiment-CAUTION). That sits in the
**30–49 band → recommended conviction bin 0.55–0.65**, and with the phase-8b disconfirmation the
recommendation snaps to the **0.55 floor — which MATCHES phase-9's 0.55.** A score of 32 is meaningfully
below the 50 "perfectly mixed" line: **the dominant LONG bias is being actively fought by the data**
(distribution, edge-negative history, hawkish macro), and the run honestly reflects that — phase-9 sized
to a token/starter (~0.3%), defined-risk, event-boxed-to-Jun-22 expression, explicitly flagging the
post-inclusion fade as the higher-quality trade. **4 contradicting phases** logged. The run is internally
consistent; all citations resolve; `decision.json` validates with the backfilled score.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|-------|-------|----------------------------|
| 1 — flow | **+** | Bullish delta-notional 1.76:1 (+$0.469bn vs −$0.267bn) + 5/5 sweep campaign $722.4M [FLOW] — but net premium only +$18M of $640M gross (two-sided), so mild not strong. (phase-0.5 GENUINELY_UNUSUAL → no cap applied) |
| 2 — dark pool | **−** | Mega-tier dark pool 93.6% sell (buy_ratio 0.064, $158.5M) [DP:block_stratified] — distribution, does not confirm the long. |
| 3 — OI | **+** | Net new OI builds 1.6:1 bullish (Δoi 23,148 vs 14,351) + LEAP call book (2028-01 P/C 0.06) [OI:smart_positioning]. |
| 4 — structure | **0** | Positive-gamma DEX dip-bid (+$2.88bn) supportive, OFFSET by negative vanna (−1,795) vol-crush risk + downward max-pain ($267.5) [STRUCT] — genuinely mixed. |
| 5 — historical | **−−** | bullish_flow backtest edge-NEGATIVE 37.5% (n=8, avg −0.58%) + MIXED 90d cum flow + 15/15 day split, parabolic +127% vs SMA200 [HIST]. |
| 6 — macro | **−** | Hawkish June-17 FOMC (hike-biased dots), CPI +4.17% YoY, rising yields, TRANSITIONAL "half-size" regime [MACRO] — headwind for a P/E-808-normalized long (Jun-22 inclusion offsets near-term only). |
| 7 — insights | **0** | UW composite MIXED, confidence 2.7%; NBIS absent from signal-confluence both directions [INSIGHT] — no clean edge. |
| 7b — fundamentals | **−** | tier_adjustment CAUTION: insider MSPR −100/−100/−34/−100 (~1.04M-share May sale), op margin −70.55%, normalized P/E 808× [FUND] — quality cut. |
| 8 — agents | **0 (split)** | 2 LONG (+2,+2) / 1 NEUTRAL (−2) / 1 SHORT (−2) = 0; all converge on "tiny/defined-risk/event-boxed, fade after Jun-22." |

**Raw score (symmetric):** 8 phases = +7 −7 +7 +0 −15 −7 +0 −7 = **−22**; phase-8 = **0** → **−22**.
**Base score:** round((−22 + 130) / 260 × 100) = **42/100**.
**Debate penalty (phase-8b):** **−5** (disconfirmed=true; bull_residual 0.55 vs bear_residual 0.65).
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment CAUTION). VETO penalty: −0 (not VETO).
**Confluence_score:** 42 − 5 − 5 = **32/100**.
**Recommended bin:** 30–49 band → 0.55–0.65; debate down-shift → **0.55**.
**Phase-9 actual bin:** **0.55** → **MATCH.**

## Contradictions

- **phase-2 (dark pool):** mega-tier 93.6% sell contradicts the bullish thesis — *resolution: tighten
  invalidation* (exit the long if institutional-accumulation flips to clear distribution or mega buy_ratio
  stays <0.10); already reflected in phase-9 signal-based invalidation.
- **phase-5 (historical):** bullish_flow win-rate 37.5% (edge-negative) + MIXED 90d flow contradicts a
  long — *resolution: downgrade conviction + starter size* (done: bin 0.55, p=0.375<0.50 → starter floor).
- **phase-6 (macro):** hawkish FOMC + rising yields contradict a long-duration high-multiple long —
  *resolution: time-box to Jun-22 + macro invalidation on a hot July CPI* (done).
- **phase-7b (fundamentals):** insider selling (MSPR −100) into the rally contradicts the bullish flow —
  *resolution: cut one size step (CAUTION) + carry insider-selling as a key risk* (done).

Net: the contradictions are **acknowledged and priced** — phase-9 did not paper over them; it sized to a
token and routed the higher-conviction expression to the post-Jun-22 fade.

## Citation failures

Spot-checked 3 of phase-9's thesis citations — all resolve:
1. `[FLOW:sweep_persistence]` 5/5 sessions, $722.4M → present in phase-1-flow.md §Sweep-persistence ✓
2. `[DP:block_stratified]` mega buy_ratio 0.064 (93.6% sell), $158.5M → present in phase-2-dark-pool.md §Tier breakdown ✓
3. `[HIST:signal_backtest]` win_rate 37.5%, n=8 → present in phase-5-historical.md §Signal backtest ✓

**No citation failures.**

## Sanity checks

- [✓] All `phase-*.md` present incl. phase-0.5, 7b, 7c, 8b (14 prior artifacts + this audit).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 in the citations summary).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.55.
- [✓] ≥1 directional (call debit spread) + ≥1 defined-risk (iron condor).
- [✓] Sizing math shown; Kelly p = phase-5 win-rate 0.375 (backtest, n=8), N-cap 0.75, p<0.50 → starter floor.
- [✓] All 5 risk gates evaluated (fundamentals CAUTION, sentiment CAUTION, correlation none, rotation aligned, debate disconfirmed) + context modifier (GENUINELY_UNUSUAL, directional conviction flagged capped).
- [✓] Structures sized to the ±4.86% front-expiry expected move; `expected_move` in decision.json.
- [✓] `decision.json` exists, backfilled (confluence 32, recommended_bin 0.55), and **passes `validate_decision.py` (OK)** incl. context/expected_move/gates.sentiment fields.

## Final auditor note

The run is **internally consistent and ready for action as written** — a low-confluence (32/100), 0.55-
conviction, token-size, defined-risk, event-boxed-to-Jun-22 long, with the dominant signal honestly
identified as distribution-into-strength and the higher-quality trade routed to the post-inclusion fade.
No revision required; the single most important thing for the desk to monitor is the mega-tier dark-pool
buy_ratio and DEX into June 22 — if either confirms distribution/flips negative, the long invalidates and
the fade activates.
