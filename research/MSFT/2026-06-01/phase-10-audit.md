# Phase 10 — Audit & Confidence Score

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:37:51Z
**Dominant bias audited:** RANGE (phase-9)

## Summary

**Confluence score 59 / 100 → recommended bin 0.65 → MATCHES phase-9's 0.65.**
The run is **internally consistent**. The data confluences mildly *for the range
thesis* (phase-4 long-gamma pin `++`, phase-8 4/4 RANGE, phases 2/5/6/7 all `+`),
sitting just above the 50 "perfectly mixed" midpoint, with **two honest
contradictions** — the bullish flow (phase-1) and bullish fundamentals (phase-7b),
which are exactly the forces that could break the range *up* and are correctly
logged as the upside-invalidation risks. The phase-7c CAUTION (crowded long) costs
5 points. **2 contradictions, 0 citation failures, all sanity checks pass.** The
blueprint — a starter-sized defined-risk fade of the capped upside, directional
long skipped on negative edge — is faithfully supported by the chain and ready as
research.

## Confluence scorecard

| Phase | Score | Justification (quote a datapoint) |
|-------|-------|-----------------------------------|
| 1 — flow | **−7** | Bullish tilt mildly *contradicts* the range bias: net_flow **+$81.2M** on $1.39B gross calls, ask-side call sweeps $274.6M [FLOW:sweeps] — the "breaks-up" risk (two-way/MIXED keeps it from `--`; BUSY_NAME caps at `+`, non-binding here). |
| 2 — dark pool | **+7** | MIXED/rebalance, **institutional-accumulation NEUTRAL (1.13)**, $2.31B AH at single price $460.52 [DP:extended_hours] — no directional accumulation = supports range (BUSY_NAME cap `+`). |
| 3 — OI | **0** | Call-heavy chain but **new builds ~50/50 buy/write** (bull 56,078 vs bear 55,182 OI), walls bracket spot 470/480/500 vs 400 [OI:smart_positioning] — genuinely mixed. |
| 4 — structure | **++ (+15)** | **POSITIVE GEX +$268.7M, pin 460, max pain 417.5 every near-term expiry** [STRUCT:gex][STRUCT:max_pain] — the core, high-conviction range signal. |
| 5 — historical | **+7** | **bullish_flow edge-negative (44.4% win, −1.25% avg, n=9)** + VRP FAIR premium-selling [HIST:signal_backtest] — no directional edge = supports fade/range. |
| 6 — macro | **+7** | Regime **TRANSITIONAL — "iron condors in range, half size"** [MACRO:MarketRegime] — explicitly range-supportive (Tech tailwind keeps it from `++`). |
| 7 — insights | **+7** | **conviction-matrix MIXED 3%, signal-confluence ABSENT (<1)** [INSIGHT:conviction_matrix] — no directional confluence = supports mixed/range. |
| 7b — fundamentals | **−7** | **BULLISH / CONFIRM** (P/E 27.4 cheapest of peers, 4/4 beats, PT $560) [FUND:peer_pe] — a directional-up pull that mildly *contradicts* the neutral/range bias (CONFIRM, so not a veto; floors downside). |
| 8 — agents | **+8** (4/4 align) | All four active agents returned **RANGE** (earnings-scout MISSING) [AGENT:risk-monitor] — +2 each. |

**Raw score (symmetric):** 29 (eight phases) + 8 (phase-8) = **37**
**Base score:** round((37 + 130) / 260 × 100) = **64 / 100**
**Debate penalty (phase-8b):** −0 (NOT disconfirmed — bull_residual 0.65 vs
bear_residual 0.55)
**Sentiment penalty (phase-7c):** **−5** (tier_adjustment = CAUTION)
**Confluence_score:** 64 − 0 − 5 = **59 / 100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.65** → **MATCH**

## Contradictions

- **phase-1 (flow):** The bullish call tilt (+$81.2M net, $274.6M ask-side call
  sweeps) is a directional-up pull against the RANGE bias — the primary "breaks-up"
  risk. **Resolution: tighten invalidation** — phase-9 correctly exits/flips on two
  daily closes >480 and waits for an RTH lift >$462 with buy_ratio >0.7 before
  conceding genuine accumulation. Adequately handled.
- **phase-7b (fundamentals):** BULLISH/CONFIRM (cheapest-of-peers, 4/4 beats, PT
  $560, +22%) is a longer-horizon upward pull contradicting a neutral range.
  **Resolution: wait-for-confirmation / acknowledge as a floor** — this is a slow
  tailwind, not a 1-4w range-breaker; phase-9 correctly uses it to justify the
  **call credit spread over the iron condor** (don't take the downside-tail risk
  when the quality floors the downside). Adequately handled.

*(No phase scored `--`. Both contradictions are the bull case, correctly carried
into phase-9's upside invalidation rather than ignored.)*

## Citation failures

Spot-checked 3 of phase-9's thesis citations — **all resolve:**
1. **[FLOW:insights_deep_dive] net_flow +$81.2M** → phase-1-flow.md §Whole-tape
   aggregate (bull $795.5M − bear $714.3M = +$81.2M). ✓
2. **[STRUCT:gex] POSITIVE GEX +$268.7M, pin 460** → phase-4-structure.md §GEX
   (total_gex 268,654,343; 460 = +$57.6M, the largest positive GEX strike). ✓
3. **[HIST:signal_backtest] bullish_flow 44.4%, −1.25%, n=9** → phase-5-historical.md
   §Signal backtest (win_rate 44.4%, avg_move_pct −1.25%, total_signals 9). ✓

**No citation failures.**

## Sanity checks

- [✓] All `phase-*.md` present incl. phase-0.5, 7b, 7c, 8b (15 artifacts: phase-0
  through phase-10 + decision.json — confirmed via `ls`).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (6 citations, spanning
  phases 1/4/5/8/6).
- [✓] Conviction bin ∈ {0.55, 0.65, 0.75, 0.85, 0.95} → 0.65.
- [✓] ≥1 directional (long call debit spread) + ≥1 defined-risk (bear call credit
  spread + iron condor) structures present.
- [✓] Sizing math shown; Kelly p = **phase-5 win-rate 0.444** (backtest, n=9, N-cap
  0.75), NOT the conviction bin; directional long skipped via the sub-0.50
  win-rate-map floor.
- [✓] All five risk gates evaluated: fundamentals **CONFIRM**, sentiment **CAUTION
  (−1 step)**, correlation **0.637 soft-watch (no cut)**, rotation **aligned (no
  cut)**, debate **not disconfirmed (no cut)**; **context BUSY_NAME_NORMAL_DAY**
  reflected (not top-of-band; final 1.0% starter).
- [✓] Structures sized to expected move; `expected_move` in JSON (±3.33% / $15.36;
  480 short beyond the move).
- [✓] `decision.json` exists and passes `validate_decision.py` (`OK`), incl.
  `context` / `expected_move` / `gates.sentiment` fields; `confluence_score` (59)
  and `recommended_bin` (0.65) backfilled and re-validated.

## Final auditor note

The run is **internally consistent and ready as research** — confluence 59 and the
recommended 0.65 bin match phase-9, the two contradictions are the bull case that
phase-9 correctly converts into upside invalidation (not buried), and the sizing
honestly reflects a negative directional edge into a crowded, pinned, half-size
regime. No revision required; the only judgment call worth flagging to the desk is
that "confluence 59" reads as *moderate confidence in a RANGE*, not in a direction —
the actionable takeaway is patience plus a starter-sized defined-risk fade, exactly
as phase-9 wrote it.
