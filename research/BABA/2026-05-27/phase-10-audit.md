# Phase 10 — Audit & Confidence Score

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T05:10:00Z
**Inputs audited:** phase-0 → phase-9 + decision.json

## Summary

**Confluence score 45/100 — mixed, with a faint bearish tilt that the gates
erase.** A sub-50 score is the correct read for phase-9's **NEUTRAL / no-trade**
verdict: the lone directional lean (bearish) earns +14 raw across the eight signal
phases but is **directly contradicted by phase-2 (dark-pool accumulation at $126.5)
and phase-5 (the bearish signal is edge-negative + cumulative flow is net-bullish)**,
then docked −5 (phase-8b disconfirmed) and −5 (phase-7c CAUTION). **Recommended bin
0.55 = phase-9 actual bin 0.55 → MATCH.** Two contradictions logged (both already
priced into the NEUTRAL call). All 3 spot-checked citations resolve. All structural
sanity checks pass; `decision.json` re-validates after backfill. **The run is
internally consistent and ready as a WATCH blueprint — no revision needed.**

## Confluence scorecard

*Scoring convention:* phase-9's bias is **NEUTRAL**, so the eight phases are scored
against the only directional *lean* the chain produced (mild **bearish**); a net
score near 50 therefore correctly ratifies NEUTRAL. Phase-0.5
`BUSY_NAME_NORMAL_DAY` caps phases 1–2 at `+`.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** (+7) | 5-session bearish sweep persistence, consistency 1.0, $43.1M `[FLOW:sweep_persistence]` (capped at + by BUSY_NAME_NORMAL_DAY) |
| 2 — dark pool | **−** (−7) | block buy_ratio 0.667 at $126.5 + extended-hours buys = mild accumulation, *contradicts* bearish `[DP:block_stratified]` |
| 3 — OI | **+** (+7) | upside calls $145–180 unwinding + P110 Mar-2027 hedge build lean bearish at the margin `[OI:decrease_with_volume]` |
| 4 — structure | **0** (0) | LONG GAMMA = range/vol-suppression (not directional); unstable regime + complacent skew net neutral `[STRUCT:gex]` |
| 5 — historical | **−** (−7) | `bearish_flow` win_rate 37.5% (edge-negative) + cumulative 90d flow net-bullish +$327M *contradict* a conviction short `[HIST:signal_backtest]` |
| 6 — macro | **+** (+7) | China headwind net (earnings miss, ADR-delisting, Section-301) agrees bearish `[MACRO:ADR_delisting_2026-05 WebSearch:man.com]` |
| 7 — insights | **0** (0) | UW composite MIXED, 6% confidence, signal-confluence score 0 both ways `[INSIGHT:conviction_matrix]` |
| 7b — fundamentals | **+** (+7) | 4/4 accelerating EPS misses (−89.5%), EPS −17.8% YoY agrees bearish; tier CONFIRM (sound B/S + cheap value temper from ++) `[FUND:earnings_surprise]` |

**Raw score (8 phases):** +7 −7 +7 +0 −7 +7 +0 +7 = **+14**
**Phase 8 (agents):** 4/4 RANGE/NEUTRAL — none endorsed the bearish lean → **0**
(neither confirm nor oppose a directional bias; earnings-scout MISSING = 0).
**Raw total:** +14
**Base score:** round((14 + 130) / 260 × 100) = **55**/100
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_res 0.55 vs bear_res 0.55)
**Sentiment penalty (phase-7c):** **−5** (CAUTION; VETO penalty N/A)
**Confluence_score:** 55 − 5 − 5 = **45**/100
**Recommended bin:** **0.55** (band 30–49)
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-2 (dark pool):** Block-tier buy_ratio 0.667 at $126.5 + extended-hours
  buys contradict the bearish lean. — **Resolution: already resolved.** phase-8's
  accumulation-hunter showed this is **covered-call overwriting** (paired with the
  C129–135 5/29 call selling), not directional accumulation; phase-9 makes the
  $126 break the bear trigger that voids it. No further action.
- **phase-5 (historical):** The `bearish_flow` signal is **edge-negative (37.5%,
  n=8)** and cumulative 90d flow is **net-bullish +$327M** — both contradict
  shorting the downtrend. — **Resolution: downgrade conviction (done).** This is
  the decisive reason phase-9 is NEUTRAL with final_size 0; it floors Kelly `p`
  below 0.50 and is the bear's strongest unrefuted point in phase-8b.

## Citation failures

*(none — all 3 spot-checked resolve)*
- `[FLOW:sweep_persistence]` → phase-1 §Key signals: "consistency 1.0, 5/5 sessions
  in top, $43.14M total sweep premium, dominant_direction = bearish" ✓
- `[HIST:signal_backtest]` → phase-5 §Signal backtest: "win_rate 37.5%, n=8 …
  10d lookback 33.3%, n=15" ✓
- `[FUND:earnings_surprise]` → phase-7b §Earnings-surprise history: "2026-03-31
  actual 0.62 vs est 5.905 = −89.5%; beat-rate 0/4" ✓

## Sanity checks

- [✓] All phase files present: phase-0, 0.5, 1, 2, 3, 4, 5, 6, 7, 7b, 7c, 8, 8b, 9,
  decision.json, 10.
- [✓] Phase-9 thesis cites ≥3 distinct upstream datapoints (5: FLOW, HIST×2, FUND,
  DEBATE).
- [✓] Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- [✓] ≥1 directional (put debit spread 125/113) + ≥1 defined-risk (long strangle
  125P/135C).
- [✓] Sizing math shown; Kelly `p` = phase-5 win-rate 0.375 (n=8, backtest), not
  the bin.
- [✓] All five risk gates evaluated (fundamentals CONFIRM, sentiment CAUTION,
  correlation none, rotation neutral, debate disconfirmed) + phase-0.5
  `BUSY_NAME_NORMAL_DAY` reflected (no top-of-band sizing; final 0%).
- [✓] Structures sized to front-expiry expected move ±2.16% / $2.76;
  `expected_move` present in decision.json.
- [✓] `decision.json` exists and passes `validate_decision.py` (incl.
  `context` / `expected_move` / `gates.sentiment`), confluence backfilled.

## Final auditor note

The chain is internally consistent: every phase points to "no directional edge,"
the two contradictions (DP accumulation, edge-negative history) are exactly why the
verdict is NEUTRAL rather than a short, and the 45/100 confluence + 0.55 bin + 0%
size all agree. The blueprint is **ready as a WATCH plan** — the actionable content
is the level structure (bear trigger <$126→$110–113, bull trigger >$131 reclaim) and
the cheap-vol observation; no revision required.
