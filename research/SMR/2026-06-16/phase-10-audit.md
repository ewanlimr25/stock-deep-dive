# Phase 10 — Audit & Confidence Score

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T12:27:51Z
**Inputs audited:** phases 0–9 + decision.json

## Summary

**Confluence score 55/100** (mildly mixed, slight bearish lean) → confluence-table
bin **0.65**, less the **phase-8b disconfirmation** one-bin down-shift → **effective
recommended bin 0.55**, which **MATCHES** phase-9's actual 0.55. The run is
**internally consistent**: every composite tool and agent corroborates a bearish
tape, and phase-9 honestly converts that into a **RANGE / watch-only** call because
the directional short is negative-edge (p=0.286, raw_kelly −0.099) and was
disconfirmed in debate. **One contradiction** logged (phase-5: the bearish setup's
own backtest is edge-negative) — already resolved by the watch-only sizing. All 3
spot-checked citations resolve. decision.json validates `OK`.

## Confluence scorecard

Scored against the **bearish directional lean** (the thesis the signal phases
express; phase-9's *actionable* bias is RANGE/watch-only because that lean is
negative-edge). Phase-0.5 `BUSY_NAME_NORMAL_DAY` caps phases 1–2 at `+`.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Net-bearish whole-tape `net_flow −$159,229` + persistent 5/5 bearish sweep ($9.18M); capped at `+` (BUSY_NAME) [FLOW:sweep_persistence] |
| 2 — dark pool | **+** | DISTRIBUTION `buy_ratio 0.384`, $4.63M sells vs $1.72M buys; capped at `+` (BUSY_NAME) [DP:block_stratified] |
| 3 — OI | **+** | At-money $10 put-heavy (net_oi −8,116); OI builds 6 bearish/4 bullish [OI:smart_positioning] |
| 4 — structure | **0** | Mixed: $10 gamma resistance + dealers-sell DEX (bearish) vs COMPLACENT skew + broad long-gamma + conditional vanna-squeeze (not bearish) [STRUCT:term_skew] |
| 5 — historical | **−** | Downtrend confirms, BUT `bearish_flow win_rate 28.6%` (n=7) — the setup's own edge is **negative** [HIST:signal_backtest] |
| 6 — macro | **+** | Net headwind for SMR (CPI 4.17%, Industrials options outflow −$318M), tempered by FOMC/Japan two-way risk [MACRO:MarketRegime_2026-06-16 UW] |
| 7 — insights | **+** | DIRECTIONAL_SHORT but only 13.7% confidence [INSIGHT:conviction_matrix] |
| 7b — fundamentals | **+** | CONFIRM (0 contradictions): rev −62% TTM, 0/4 beats, MSPR negative — tempered by ~$1B cash floor [FUND:revenueGrowthTTMYoy] |
| 8 — agents | **+ (net +4)** | 0 LONG; contrarian RANGE (+2) + accumulation SHORT (+2, bearish-aligned); sweep/risk NEUTRAL (0 each) |

**Raw score (symmetric):** +7+7+7+0−7+7+7+7 (= +35) + 4 (agents) = **+39**
**Base score:** round((39 + 130)/260 × 100) = **65/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.55 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **−5** (CAUTION)
**Confluence_score:** **55/100**
**Recommended bin:** confluence-table 55 → 0.65, **−1 bin (debate gate) → 0.55**
**Phase-9 actual bin:** **0.55 — MATCH**

## Contradictions

- **phase-5 (historical):** the bearish setup's own `signal-backtest win_rate` is
  **28.6%** (n=7, avg forward move +1.66%) — the directional short is
  **edge-negative**, contradicting a tradeable bearish thesis. **Resolution
  (applied):** phase-9 correctly **down-graded to watch-only (final_size 0%)** and
  expressed only a defined-risk fade-the-rip — the contradiction is the reason the
  trade is not taken at spot. No further action; tighten via the $10.95 / $10-gamma
  invalidation.
- **phase-4 (structure):** scored `0` (neutral), not a contradiction — but note the
  COMPLACENT skew + conditional vanna-squeeze are *latent bullish* mechanics that
  reinforce the watch-only stance.

## Citation failures

None — 3 spot-checked from phase-9's thesis, all resolve:
1. **[DP:block_stratified]** "buy_ratio 0.384, $4.63M sells vs $1.72M buys" →
   resolves to phase-2 §Tier breakdown + §Largest blocks. ✓
2. **[HIST:signal_backtest]** "bearish_flow win_rate 28.6% (n=7)" → resolves to
   phase-5 §Signal backtest + sizing handoff. ✓
3. **[MACRO:FOMC_2026-06-17]** "FOMC decision one day after as-of, hawkish dot-plot
   risk" → resolves to phase-6 §Catalyst calendar + §Summary. ✓

## Sanity checks

- [✓] All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9) + decision.json (15 files).
- [✓] Phase-9 cites ≥3 distinct upstream datapoints (5 citations).
- [✓] Conviction bin ∈ {0.55,…,0.95} → 0.55.
- [✓] ≥1 directional (long $10 put) + ≥1 defined-risk (bear put debit spread $10/$8).
- [✓] Sizing math shown; Kelly p = phase-5 win-rate **0.286** (n=7, backtest), not the bin.
- [✓] All five gates evaluated: fundamentals CONFIRM, **sentiment CAUTION**,
  correlation none, rotation neutral, **debate disconfirmed** (each shown).
- [✓] Phase-0.5 `unusual_verdict=BUSY_NAME_NORMAL_DAY` reflected → no top-of-band size (floor).
- [✓] Structures sized to the front-expiry expected move (±5.68% / $0.56); `expected_move` in JSON; 07-17 expiry clears the 06-18 FOMC/OPEX; credit/condor explicitly rejected (VRP −2.15).
- [✓] decision.json exists and passes `validate_decision.py` (incl. `context` /
  `expected_move` / `gates.sentiment`); confluence_score=55, recommended_bin=0.55 backfilled.

## Final auditor note

The run is **internally consistent and ready for action** — the action being
**stand aside / watch-only**, which is the correct, well-supported conclusion, not a
failure to find a trade. The bearish tape is real but the directional short is a
negative-edge bet (28.6% historical win-rate) into a crowded short, an FOMC binary
one day out, and a live Japan-pledge squeeze catalyst; phase-9 faithfully translated
that into a defined-risk fade-the-rip with 0% size at spot, and no phase needs
revision.
