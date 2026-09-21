# Phase 7 — UW Insights Confluence

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T02:15:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's own composite instrumentation calls DOCN **MIXED / NEUTRAL with ~1%
confidence** — no directional edge. The conviction matrix returns **MIXED**
(balanced DP buy_ratio 0.49, thresholds bull 0.6 / bear 0.4), institutional
accumulation is **NEUTRAL** (buy/sell 0.96), and DOCN scores **below threshold in
BOTH the bullish and bearish signal-confluence lists** (not present in either).
The single non-neutral read is **`price-vs-flow` = DIVERGENCE**: price −34.1% while
net options flow is mildly bullish (+$154K) — an early, low-conviction
dip-buying/reversal tell, not a confirmed turn. This is a clean, internally
consistent baseline: **UW agrees with phases 1–6 that DOCN is a mixed, vol-rich,
fallen name with no directional flow edge** — the only "signal" is the weak
bullish divergence, which the long-gamma regime (phase-4) is expressing as a
$115–128 base, not a rip.

## Key signals

- **conviction-matrix: MIXED, confidence 1%** `[INSIGHT:conviction_matrix]` — no
  clear bias (DP 0.49, call ask/bid 1686/1115, put ask/bid 1439/922).
- **institutional-accumulation: NEUTRAL** (buy_sell 0.96, buy 190,203 / sell
  198,286, VWAP $117.82) `[INSIGHT:institutional_accumulation]` — confirms phase-2.
- **price-vs-flow: DIVERGENCE=true** — "Price down 34.1% but flow bullish (+$154K)"
  `[INSIGHT:price_vs_flow]` — weak early-reversal tell; period low $111.13, now $118.91.
- **signal-confluence: DOCN absent from BOTH bullish & bearish lists** (score <1)
  `[INSIGHT:signal_confluence]` — no confluence in either direction.
- **analyst-vs-flow:** only flow side returned (bullish, +$154K, P/C 0.864); **no
  analyst consensus** in payload `[INSIGHT:analyst_vs_flow]` — no Street cross-check.

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]` (from phase-0.5/1 whole-tape block)

- Whole-tape: bullish_premium $2.886M vs bearish_premium $2.732M → **derived
  net_flow +$154,130** (≈53% bull); call_premium $3.006M vs put_premium $2.998M;
  **P/C 0.864**; **implied_move 2.14 / implied_move_perc 1.80%** (phase-9 N4 sizes to
  this); **iv_rank 99.12**; total_OI 147,920; **next_earnings 2026-08-04**.
- Dark pool $45.77M / 388,489 sh / avg $117.43. Reconciles with phase-1 (balanced
  aggregate) and phase-0.5 `[CTX:]` (outside top-50 net-directional).

### Signal confluence `[INSIGHT:signal_confluence]`

- Bullish list (min-score 1, top-20): **DOCN NOT present**.
- Bearish list (min-score 1, top-20): **DOCN NOT present**.
- → DOCN's directional confluence score is **below 1 in both directions** — the
  instrumentation sees no stacked directional case. Consistent with MIXED.

### Conviction matrix `[INSIGHT:conviction_matrix]`

- **scenario: MIXED**, confidence_pct **1**. DP buy_ratio 0.49 ("balanced — no clear
  bias"). Options flow: call_ask 1,686 / call_bid 1,115 (net call buying), put_ask
  1,439 / put_bid 922 (net put buying too) — **two-sided**, matching phase-1's
  hedging-heavy tape. Not DIRECTIONAL_LONG, not HEDGED_LONG, not COVERED_CALL — MIXED.

### Price vs flow `[INSIGHT:price_vs_flow]`

- **divergence: true** — "Price is down 34.1% but options flow is bullish (net flow
  $154,130)." period_high $187.5, period_low $111.13, price_end $118.91,
  price_change −34.12%, iv_rank 99.1.
- Read: a classic bullish-flow / falling-price divergence = **early reversal
  candidate**, but net flow is tiny ($154K) and the signal "is often early"
  (phase-7 heuristic). Paired with phase-4's **long-gamma** regime, the divergence
  is manifesting as **basing in a $115–128 range**, not an impulsive reversal.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

- Payload returned only the options-flow side (bullish, net +$154K, P/C 0.864); **no
  yfinance analyst consensus** included → no agree/disagree computable here. (Street
  view deferred to phase-7b/7c cross-source analyst pulls.)

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

- **signal: NEUTRAL — balanced dark pool activity.** buy_sell_ratio **0.96**
  (slight sell lean), buy 190,203 / sell 198,286, total DP $45.77M, VWAP $117.82,
  price_30d −34.12%. Top level $118.91 ($13.68M / 115,049 sh). **Confirms phase-2's
  balanced-to-mild-distribution verdict** — no stealth accumulation.

### Earnings play `[INSIGHT:earnings_play]` (earnings 8/4, in-window)

- Market-wide top-10 earnings-vol plays are INTC/AMD/SNDK (all IV rank 100); **DOCN
  is not in the top-10** (IV rank 99.1, smaller name) but is a legitimate
  earnings-vol candidate: **earnings 2026-08-04 (~18 DTE), IV rank 99, rich VRP**
  (phase-5). The setup is a *vol* setup (sell/fade rich IV or straddle-aware), not a
  directional flow setup.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | |
|---------|--------------------------|--|
| `insights conviction-matrix` | MIXED, conf 1% ← `.scenario`,`.confidence_pct` | DP 0.49 |
| `insights price-vs-flow --lookback-days 30` | divergence true, −34.1% ← `.divergence`,`.price_change_pct` | |
| `insights analyst-vs-flow` | flow bullish, no analyst ← `.options_flow.flow_sentiment` | |
| `insights institutional-accumulation` | NEUTRAL, 0.96 ← `.signal`,`.buy_sell_ratio` | |
| `insights earnings-play --days-until-earnings 30` | DOCN not top-10 ← filter `.results[]` | 10 rows |
| `insights signal-confluence --direction bullish` | DOCN absent ← `index("DOCN")` | 20 |
| `insights signal-confluence --direction bearish` | DOCN absent ← `index("DOCN")` | 20 |

## Tool errors

(none — all seven calls returned valid JSON on first read.)

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both) | **agrees** phases 1–3 | No directional edge — matches mixed tape, no fresh OI build |
| conviction_matrix MIXED | **agrees** phase-1 | Two-sided flow (call & put buying), balanced DP |
| institutional_accumulation NEUTRAL | **agrees** phase-2 | 0.96 buy/sell = phase-2's mild-distribution/balanced read |
| price_vs_flow DIVERGENCE | **consistent** phase-4/5 | Bullish divergence expressed as long-gamma base, not reversal rip |
| earnings_play in-window | **agrees** phase-4/5 | Confirms this is a vol/earnings setup, not a flow-momentum setup |

**No contradictions.** The run is internally consistent — UW's composite is the
mixed/neutral baseline the granular phases already built.

## Verdict for downstream phases

- **UW composite bias:** **MIXED / NEUTRAL** with a **weak bullish price-vs-flow
  divergence** (dip-buying into a −34% crash, expressed as a $115–128 base).
- **Conviction:** **2/5.**
- **Phase-9 baseline instruction:** treat DOCN as a **mixed, vol-rich, fallen name
  with NO directional flow edge**; the only positive tell is a low-conviction
  bullish divergence. Override toward a direction ONLY with specific contrary
  evidence from phases 7b/7c/8/8b. The dominant tradeable feature remains **rich IV
  / premium-selling into 8/4 earnings** (phase-5), inside a long-gamma range (phase-4).
- **Open questions:** Does phase-7b fundamentals justify the −34% de-rate (is the
  competitive/SMB/AI-capex fear real, or overdone → supporting the divergence)? Does
  phase-7c (short interest, earnings behavior) show the crash is crowded-short
  (squeeze fuel) or justified? These decide whether the bullish divergence is
  actionable or a value trap.
