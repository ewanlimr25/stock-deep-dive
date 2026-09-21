# Phase 10 — Audit & Confidence Score

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Dominant bias audited:** SHORT (tactical fade toward 117, activated only on a 123 break)

## Summary

**Confluence score: 54/100** — just above "perfectly mixed" (50), which honestly
captures this run: a *slight* net-positive confluence for the near-term fade, heavily
gated. Recommended conviction bin (band 50–64) is **0.65**; phase-9 chose **0.55** — a
**conservative downward deviation** (allowed; phase-9 applied the phase-8b debate
down-shift to the floor). **2 contradicting phases** (macro/sector, fundamentals),
both already reflected in phase-9's gates and tiny 0.5% size. All 15 phase artifacts
present; all 3 spot-checked citations resolve; `decision.json` validates. The run is
**internally consistent and ready for action as specified** — i.e., as a sub-1%,
defined-risk scalp that is *watch-only until 123 breaks* and flat before Aug-5.

## Confluence scorecard

| Phase | Score | Justification (datapoint) |
|---|---|---|
| 1 — flow | **+** | net_flow −$1.08M (bullish $7.28M < bearish $8.36M) mildly bearish `[FLOW:insights_deep_dive]`; capped at `+` by BUSY_NAME_NORMAL_DAY |
| 2 — dark pool | **+** | block-tier buy_ratio 0.257 (74% sell) = distribution `[DP:block_stratified]`; de-rated (after-hours/index, immaterial vs float); capped at `+` |
| 3 — OI | **0** | brackets spot — put walls 117/120 vs call walls 125/130, no structural directional build `[OI:oi_by_strike]` |
| 4 — structure | **+** | short gamma, 123 = −$12.8M GEX, max pain 117–121 below spot `[STRUCT:gex][STRUCT:max_pain]` — strongest pro-short, braked by NORMAL skew |
| 5 — historical | **+** | bearish_flow backtest 100% (n=10, −5.22%) vs bullish_flow 14% `[HIST:signal_backtest]` — near-term pro-short (medium-term base is the countervail) |
| 6 — macro | **−** | Technology #1 durable inflow, persistence 0.8 = ADVERSE to the short `[MACRO:sector_flow]`; medium-term easing tailwind |
| 7 — insights | **+** | confirmed price-vs-flow DIVERGENCE (price +6.5% vs flow −$1.08M) `[INSIGHT:price_vs_flow]` — the one directional composite signal |
| 7b — fundamentals | **−** | CAUTION — rev +32%, fortress balance sheet contradict a short `[FUND:revenueGrowthTTMYoy]` (healthy business, not a VETO) |
| 8 — agents | **+2** | 3 SHORT (+2 ea) − NEUTRAL/RANGE (−2 ea) = net +2; avg conviction 2.2 `[AGENT:desk]` |

**Raw score (symmetric):** 7+7+0+7+7−7+7−7+2 = **23**
**Base score:** round((23 + 130) / 260 × 100) = **59/100**
**Debate penalty (phase-8b):** **−5** (disconfirmed; bull_residual 0.60 vs bear_residual 0.65)
**Sentiment penalty (phase-7c):** **0** (tier_adjustment = CONFIRM — crowded-long + low SI *supports* the fade)
**Confluence_score:** **54/100**
**Recommended bin:** **0.65** (band 50–64)
**Phase-9 actual bin:** **0.55** — **conservative deviation** (phase-9 lowered to the
floor on the debate disconfirmation; a lower-than-recommended bin is always permitted).

## Contradictions

- **phase-6 (macro/sector):** Technology is the #1 *durably-bid* inflow sector
  (persistence 0.8) while the thesis shorts a name inside it — the standing sector lift
  fights the fade. **Resolution: keep size tiny (done, 0.5%) + tighten invalidation
  (done — stand down if 123 hasn't broken in 2–3 sessions; scalp not swing).**
- **phase-7b (fundamentals):** CAUTION — +32% revenue, 48% gross margin, fortress
  balance sheet describe a healthy business, contradicting a directional short.
  **Resolution: downgrade conviction (done via gate + 0.55 bin) + defined-risk
  structures only (done).**

## Citation failures

None — 3 thesis citations spot-checked, all resolve:
1. `[STRUCT:gex]` "123 = −$12.8M GEX" → phase-4 §GEX (`.per_strike` 123 → −12,771,622). ✓
2. `[INSIGHT:price_vs_flow]` "price +6.5% vs flow −$1.08M" → phase-7 §Price vs flow. ✓
3. `[DP:block_stratified]` "buy_ratio 0.257 (74% sell)" → phase-2 §Tier breakdown. ✓

## Sanity checks

- ✓ All `phase-*.md` present incl. 0.5, 7b, 7c, 8b (15 artifacts + decision.json).
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (8 in citations block).
- ✓ Conviction bin 0.55 ∈ {0.55, 0.65, 0.75, 0.85, 0.95}.
- ✓ ≥1 directional (123/117 put debit spread) + ≥1 defined-risk (126/130 bear call spread).
- ✓ Sizing math shown; Kelly p = phase-5 win-rate (p_raw 1.00 → N-capped 0.85), not the bin.
- ✓ All five risk gates evaluated (fundamentals CAUTION, sentiment CONFIRM, correlation
  cluster SHOP/PATH 0.707, sector rotation adverse, debate disconfirmed) + context
  BUSY_NAME_NORMAL_DAY reflected (no top-of-band; 0.5% final).
- ✓ Structures sized to front-expiry expected move (±6% / $7.4 in `expected_move`);
  both expiries (7/24) clear FOMC 7/29 & earnings 8/5.
- ✓ `decision.json` exists, backfilled (confluence 54, recommended_bin 0.65), and
  passes `validate_decision.py` → `OK`.

## Final auditor note

The run is internally consistent: a genuinely mixed setup (confluence 54) that phase-9
translated into an honest, heavily-gated **0.5% scalp** rather than forcing a position —
the two contradictions (adverse sector, healthy fundamentals) are acknowledged and
priced into the size and invalidation, not ignored. No revision required; the only
caution to the desk is operational — this trade is **watch-only until 123 breaks**, and
if the 116–121 stalemate holds into 7/24 it should be stood down, not held for the 8/5
binary.
