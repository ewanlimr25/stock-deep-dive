# Phase 7 — UW Insights Confluence

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite instrumentation lands on a **COVERED_CALL scenario (22% confidence):
"Dark pool buying + call selling — yield enhancement, capping upside."** This is the
single cleanest unification of phases 1–4: institutions are **net-buying stock in the
dark pool** (institutional-accumulation buy/sell 2.35) while **selling calls and
writing puts** into IV rank 96.9 (phases 1, 3) — a yield/income posture that is
**mildly constructive on the underlying but hard-caps upside**, NOT a directional
breakout long. Two tensions to flag: (1) **price-vs-flow DIVERGENCE** — price is
−13.5%/30d yet net flow is mildly bullish (+$2.21M) — a potential leading reversal
but, given phase-5's bullish_flow-14% backtest, more likely complacent/late flow than
an imminent turn; (2) the accumulation tool reads 2.35 buy/sell where phase-2 argued
the buy-classification is closing-cross-dominated — reconciled below as **weak-to-mild
net buying, not conviction accumulation.** **NOW is absent from both bullish and
bearish signal-confluence** (score <1 either way) — confirming a mixed, low-conviction
setup. Baseline for phase-9: **neutral-to-mildly-bullish income / defined-risk,
capped upside — not a naked directional long.**

## Key signals

- **Conviction matrix = COVERED_CALL, 22% conf** — "DP buying + call selling, capping
  upside" `[INSIGHT:conviction_matrix]`.
- **price-vs-flow DIVERGENCE=true** — price −13.5% vs bullish flow (+$2.21M), IV rank
  96.9 `[INSIGHT:price_vs_flow]`.
- **institutional-accumulation = ACCUMULATION, buy/sell 2.35** (buy 2.12M vs sell
  0.90M, DP prem $312.7M) — but closing-cross-weighted (see reconciliation)
  `[INSIGHT:institutional_accumulation]`.
- **NOW absent from bullish AND bearish signal-confluence** (min-score 1, 50 found
  each) — no multi-factor confluence either way `[INSIGHT:signal_confluence]`.
- **NOW absent from earnings-play screen** despite earnings in 5 days — cross-check
  the date in 7b/7c `[INSIGHT:earnings_play]`.

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

Whole-tape `uw_screener` aggregates (reconciled vs phase-1): bullish_premium $18.75M,
bearish_premium $16.54M → **net_flow +$2.21M** (derived); call_premium $22.67M vs
put_premium $18.04M; **P/C 0.632**; **iv_rank 96.9**; implied_move_perc 0.49%
(daily); total_open_interest 1,514,177; next_earnings_date **2026-07-22**. Matches
phase-1 exactly (call-heavy, thinly net-bullish). Yahoo fundamentals block returned
null (phase-7b will source fundamentals from Finnhub/`fz`).

### Signal confluence `[INSIGHT:signal_confluence]`

**NOW absent from both directions** at min-score 1 (bullish tickers_found 50, bearish
50). NOW's confluence score is below 1 either way → **no coherent multi-factor
directional stack** exists. Consistent with the mixed phases 1–5.

### Conviction matrix `[INSIGHT:conviction_matrix]`

**Scenario: COVERED_CALL** — confidence **22%**. Explanation: *"Dark pool buying +
call selling — yield enhancement, capping upside."* This is the composite's verdict
and it aligns tightly with:
- phase-2 (net DP buying, even if partly facilitation),
- phase-1/3 (call selling + put writing into high IV),
- phase-4 (delta-neutral, long-gamma, call-heavy dealer book).
Low confidence (22%) reflects the mixed, non-directional nature. **Not
DIRECTIONAL_LONG.**

### Price vs flow `[INSIGHT:price_vs_flow]`

**divergence = true**: "Price is down 13.5% but options flow is bullish (net flow
$2,210,836)." A bullish price/flow divergence — classically a leading reversal cue.
BUT: phase-5's bullish_flow backtest (14.3% win) and the complacent skew (phase-4)
argue this flow is **complacent/late, not predictive**. Treat as a *watch* item that
earnings (7/22) will resolve, not a reversal to front-run.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Tool returned only the options-flow block (flow_sentiment **bullish**, net +$2.21M,
P/C 0.632) — **analyst consensus was not returned** (yfinance leg empty). Wall-Street
vs trader agreement **deferred to phase-7b/7c** (Finnhub/`fz` analyst cross-source).

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

**Signal: ACCUMULATION** — "dark pool buy volume significantly exceeds sell volume."
buy_sell_ratio **2.35** (buy 2,118,936 / sell 902,642), total_dp_premium **$312.7M**,
price_30d −13.51%.

**Reconciliation vs phase-2:** phase-2 de-rated the mega-tier buy_ratio=1.0 as
**closing-cross/auction facilitation** (the 803,594-sh + 271,703-sh 20:09–20:10 prints
at the exact $103.24 close). Those same prints inflate this tool's 2.35 buy/sell.
**Reconciled read: there IS genuine net DP buying, but a large fraction is auction
facilitation → "weak-to-mild accumulation," not conviction.** The COVERED_CALL
scenario is the honest synthesis: mild stock accumulation + call/put writing = capped
yield play. Accumulation against a −13.5% price = the "buying the dip cheaply / income"
interpretation, not aggressive breakout buying.

### Earnings play `[INSIGHT:earnings_play]`

**NOW absent from earnings-play results** despite next_earnings_date 2026-07-22
(5 days out). Either the screen requires an IV/OI-buildup profile NOW doesn't hit, or
the earnings date wasn't ingested by this leaf. **Action:** phase-7b/7c must confirm
the 7/22 date independently (memory flag: UW `next_earnings_date` can be stale). Not
treated as a data failure.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|---|---|---|
| `uw insights conviction-matrix --symbol NOW` | COVERED_CALL, 22% ← `.scenario/.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol NOW --lookback-days 30` | divergence=true, −13.5% vs +$2.21M ← `.divergence/.divergence_signal` | 1 |
| `uw insights analyst-vs-flow --symbol NOW` | flow bullish; analyst leg empty ← `.options_flow` | 1 |
| `uw insights institutional-accumulation --symbol NOW` | ACCUMULATION, 2.35 ← `.signal/.buy_sell_ratio` | 1 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 50` | NOW absent ← `[.results[].ticker]` | 50 |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 50` | NOW absent ← `[.results[].ticker]` | 50 |
| `uw insights earnings-play --days-until-earnings 30` | NOW absent ← filter | results |

## Tool errors

None fatal. `analyst-vs-flow` returned no analyst consensus (yfinance leg empty) —
deferred to 7b/7c. `earnings-play` did not list NOW — flagged for date cross-check.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| conviction_matrix = COVERED_CALL | **agrees** phases 1–4 | unifies DP-buy + call/put-write + delta-neutral + long-gamma |
| price_vs_flow = DIVERGENCE (bullish) | **partial** — conflicts phase-5 | flow bullish vs −13.5% trend + 14% bullish backtest; treat flow as complacent |
| institutional_accumulation = ACCUMULATION 2.35 | **partial** — phase-2 de-rated | reconciled: mild net buy, closing-cross-weighted, not conviction |
| signal_confluence (both empty) | **agrees** phases 1,5 | no directional confluence; mixed/low-conviction confirmed |

## Verdict for downstream

- **UW composite bias:** **COVERED_CALL — neutral-to-mildly-bullish income posture
  with a hard upside cap.** Not directional long; not short.
- **Conviction:** **2 / 5** (low-confidence composite 22%; internally coherent but weak).
- **Phase 9 baseline:** treat this as **the baseline** — a **defined-risk / premium-
  selling / capped-upside** structure fits the composite, the VRP premium-selling
  regime (phase-5), AND the TRANSITIONAL "iron condors in range" macro guidance
  (phase-6). Override toward a directional long ONLY with specific contrary evidence
  (there is little: bullish_flow backtest is 14%). A directional *short* has trend +
  backtest support but conflicts with the mildly-bullish flow/DP — so the honest
  center is **market-neutral / income with a slight bullish lean, everything
  subordinate to the 7/22 earnings binary.**
- **Open questions:** Does phase-7b fundamentals justify the −13.5% de-rate (quality
  veto) or flag it as oversold? Does phase-7c sentiment/short-interest show
  capitulation or complacency into the print? Is the 7/22 earnings date confirmed?
