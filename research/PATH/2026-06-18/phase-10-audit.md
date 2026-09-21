# Phase 10 — Audit & Confidence Score

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:36:02Z
**Inputs audited:** phases 0–9 + decision.json

## Summary

**Confluence score 33/100** (sub-50 = the data is *fighting* the candidate bullish bias).
Recommended conviction bin **0.55** (band 30–49, floored by the disconfirmed debate) —
**MATCHES** phase-9's actual 0.55. **4 contradiction phases** (2, 4, 5, 6). The run is
**internally consistent**: phase-9's NEUTRAL / WATCH-ONLY call is the correct read of a
low-confluence, counter-trend, gate-cut setup. One genuine internal contradiction (the GEX
regime label) was already flagged and resolved upstream. All 3 spot-checked citations resolve;
all sanity checks pass; `decision.json` validates.

## Confluence scorecard

Dominant bias scored against = the **bullish/long candidate** (the directional thesis phase-9
evaluated and rejected). Phase-0.5 `BUSY_NAME_NORMAL_DAY` caps phases 1–2 at `+`.

| Phase | Score | Justification (datapoint) |
|-------|-------|---------------------------|
| 1 — flow | **+** | Ex-0DTE delta-notional +$1.07M long + sweep persistence 1.0; but flat net_flow +$17.8k, capped by BUSY_NAME_NORMAL_DAY [FLOW:delta_notional][FLOW:sweep_persistence] |
| 2 — dark pool | **−** | Dominant large-tier buy_ratio **0.48** (slight distribution), clusters overhead = supply — does NOT confirm the bullish flow [DP:block_stratified] |
| 3 — OI | **+** | Long-dated bullish base (2027 LEAP 34.5% of OI, call-skewed) + 10-day OI build, but near-term builds tiny/mixed [OI:term_structure] |
| 4 — structure | **−** | Near-spot **short gamma** ($10 gex −8.69M), DEX −4.9M (dealers sell), complacent skew — downside-asymmetric, not bull-supportive [STRUCT:gex][STRUCT:dex] |
| 5 — historical | **−−** | bullish_flow backtest **37.5%** (n=8, avg −0.51%, below floor) + counter-trend (−37% YTD, below all SMAs) [HIST:signal_backtest] |
| 6 — macro | **−** | FOMC **hawkish flip** 6/17 + TRANSITIONAL half-size regime; tech inflow is semis-led, PATH not participating [MACRO:FOMC_2026-06-17] |
| 7 — insights | **0** | MIXED, 7.9% confidence; PATH absent from both bullish AND bearish confluence; price-vs-flow divergence [INSIGHT:conviction_matrix] |
| 7b — fundamentals | **+** | fundamental_signal BULLISH (P/E 16.9 cheapest profitable peer, +19.6% net margin, $129M FCF, $244M buyback) — tier CAUTION on insider selling [FUND:cashflow] |
| 8 — agents | **−4 (1/4 align)** | accumulation NEUTRAL (−2), contrarian RANGE (−2), sweep LONG (+2), risk NEUTRAL (−2); earnings-scout skipped |

**Raw score (symmetric):** phases = (+7 −7 +7 −7 −15 −7 +0 +7) = **−15**; phase-8 = **−4** → **raw −19**
**Base score:** round((−19 + 130) / 260 × 100) = **43/100**
**Gate penalties (one-sided):** debate (phase-8b disconfirmed, bull_res 0.55 vs bear_res 0.65) **−5**; sentiment (phase-7c CAUTION) **−5**; sentiment VETO **0**
**Confluence_score:** 43 − 5 − 5 = **33/100**
**Recommended bin:** **0.55** (band 30–49 → 0.55–0.65; disconfirmed debate floors it at 0.55)
**Phase-9 actual bin:** **0.55** → **MATCH**

## Contradictions

- **phase-2 (dark pool):** balanced-to-slight-distribution (buy_ratio 0.48) contradicts the
  bullish flow lean — *resolution: already reflected — phase-9 is NEUTRAL/watch-only; the DP
  non-confirmation is the trade's primary "wait for confirmation" trigger (buy_ratio >0.60).*
- **phase-4 (structure):** near-spot short gamma + DEX sell-overhang make the asymmetry
  **downside** — *resolution: tighten invalidation — phase-9's $10 two-close stop and the
  "break of $10 → $9.20" risk capture it.*
- **phase-5 (historical):** bullish_flow backtests 37.5% (below 0.45 floor), counter-trend —
  *resolution: downgrade — this is the dominant reason p<0.50 forced starter/skip → 0% size.*
- **phase-6 (macro):** hawkish FOMC + TRANSITIONAL regime headwind — *resolution: wait for
  confirmation — the ~7/15 CPI and ~7/28 FOMC are the named macro invalidation triggers.*

**Internal (intra-phase) contradiction flagged:** phase-4 `gex.regime = POSITIVE` vs
`total_gex −7.3M` vs `today-gamma-flip = NEGATIVE`. **Resolved upstream:** the ZGL (2.34) is a
low-price artifact; the tradeable near-spot gamma is **short**, corroborated by phase-5's
GEX time-series (ZGL collapsed 7.65→2.34, total_gex flipped negative 6/12, 6/17, 6/18). Not a
cross-phase inconsistency — both phases agree once the label is set aside.

**Reconciliations (not contradictions):** phase-1 flat net_flow vs ex-0DTE +$1.07M long (0DTE
delta-one artifact, reconciled in phase-1); phase-2 "slight distribution" (large-tier 0.48) vs
phase-7 "neutral" (aggregate 0.579 incl. block + closing crosses) — both = no real accumulation.

## Citation failures

3 of phase-9's thesis citations spot-checked — **all resolve**:
1. `[HIST:signal_backtest] 37.5% (n=8, avg −0.51%)` → phase-5-historical.md §Signal backtest ✓
2. `[DP:block_stratified] large-tier buy_ratio 0.48` → phase-2-dark-pool.md §Tier breakdown ✓
3. `[FLOW:sweep_persistence] consistency 1.0, 5/5 sessions, $2.27M` → phase-1-flow.md §Sweeps ✓

(Also verified: `[MACRO:FOMC_2026-06-17]` → phase-6 §Rates ✓; `[SENT:short_float fz] 31.78%` → phase-7c §Short interest ✓.) **No citation failures.**

## Sanity checks

- ✓ All `phase-*.md` present (0, 0.5, 1–7, 7b, 7c, 8, 8b, 9, 10) + decision.json (15 files).
- ✓ Phase-9 thesis cites ≥3 distinct upstream datapoints (6 cited).
- ✓ Conviction bin ∈ {0.55,…,0.95} → 0.55.
- ✓ ≥1 directional ($10/$12 call debit spread) + ≥1 defined-risk (long $9.50P/$11C strangle).
- ✓ Sizing math shown; Kelly p = phase-5 win-rate 0.375 (capped, n<10→0.75); not a bin fallback.
- ✓ All five risk gates evaluated (fundamentals CAUTION, sentiment CAUTION, correlation none,
  rotation neutral, debate disconfirmed); `unusual_verdict = BUSY_NAME_NORMAL_DAY` reflected (no top-of-band).
- ✓ Structures sized to front-expiry expected move (±2.06% / $0.21); `expected_move` in JSON.
- ✓ `decision.json` exists and passes `validate_decision.py` (incl. context/expected_move/gates.sentiment); confluence_score 33 + recommended_bin 0.55 backfilled.
- ✓ Disclaimer present at top of phase-9.

## Final auditor note

The run is **internally consistent and ready as a research conclusion**: confluence 33/100 and
the matched 0.55 bin correctly express that PATH is a low-edge, counter-trend, dark-pool-
unconfirmed setup in a hawkish regime — phase-9's **NEUTRAL / WATCH-ONLY (0% directional)** call
is the data-faithful outcome, not a hedge. No phase needs revision; the only "trade" here is a
disciplined pass, with the $10 line and DP buy_ratio >0.60 as the concrete triggers that would
reopen the question.
