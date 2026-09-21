# Phase 7 — UW Insights Confluence

**Ticker:** PATH
**As-of date:** 2026-07-13
**Generated:** 2026-07-13T20:42:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-6-macro.md

## Summary

UW's composite instrumentation independently lands where the workup did: a
**DIRECTIONAL_LONG** conviction-matrix scenario ("Dark pool buying + aggressive call
purchases — institutional directional bet") and an explicit **ACCUMULATION** signal
(buy/sell ratio **1.58**), but at **low composite confidence (25.4%)** — and, crucially,
the composite reads only the **as-of 07-13** darkpool (buy_ratio 0.612, $337M), so it
is **blind to the 07-09 $644M mega block**; the true accumulation is materially
stronger than 25% implies. The one caution the composite surfaces is a **price-vs-flow
DIVERGENCE** — price up 1.1% over 30d while *options* net flow is mildly bearish
(−$167k), the phase-1 LEAP-put hedging. PATH is **not in the market-wide
signal-confluence list** (below score 1 either direction), confirming phase-0.5's
"quiet, not a confluence leader" read. Net: composite baseline is **mildly bullish
(accumulation-driven), low-confidence, options-hedged.** Conviction 3/5.

## Key signals

- **Conviction-matrix: DIRECTIONAL_LONG**, confidence **25.4%** — "institutional directional bet" `[INSIGHT:conviction_matrix]`.
- **Institutional-accumulation: ACCUMULATION**, buy/sell ratio **1.58**, $337M DP premium, VWAP **$11.93** `[INSIGHT:institutional_accumulation]`.
- **Price-vs-flow: DIVERGENCE** — "price up 1.1% but options flow bearish (net −$166,751)" `[INSIGHT:price_vs_flow]` — the LEAP-put hedge, an early caution.
- **Composite is blind to the 07-09 mega block** — it scores only the 07-13 tape; the real accumulation (phase-2, $644M) is understated by the 25.4% confidence.
- **PATH absent from signal-confluence** (bullish & bearish, min-score 1, top-50) `[INSIGHT:signal_confluence]` — not a market confluence leader; quiet name.

## Detailed findings

### Deep-dive snapshot (`uw_screener` whole-tape, reconciled with phase-1/0.5)
- bullish_premium **$771,148** vs bearish_premium **$937,899** → **net_flow −$166,751** (mild bearish).
- call_premium **$1,278,744** vs put_premium **$636,088**; put_call_ratio **0.265**.
- iv_rank **40.4**; implied_move_perc **5.3%** (front-expiry ±$0.63); next_earnings **2026-09-03**.
- Reconciles exactly with phase-1 and phase-0.5 `[CTX:]` — call-heavy by premium, net-bearish by aggressor, quiet for the name.

### Signal confluence `[INSIGHT:signal_confluence]`
- PATH not returned in either bullish or bearish list at `--min-score 1 --top-n 50`. Market-wide confluence score < 1 → not a multi-factor confluence leader. Consistent with the quiet-options read; the *idiosyncratic* darkpool event is not what this cross-sectional factor-count captures.

### Conviction matrix `[INSIGHT:conviction_matrix]`
- scenario **DIRECTIONAL_LONG**, confidence_pct **25.4** (low). explanation: "Dark pool buying + aggressive call purchases — institutional directional bet."
- Inputs: dark_pool buy_ratio **0.612** (07-13 only), options_flow call_ask 13,700 vs call_bid 7,655 (net call buying), put_ask 3,644 vs put_bid 1,688. thresholds bull 0.6 / bear 0.4 → just clears bull.
- **Caveat:** this uses the as-of 07-13 darkpool, not 07-09. The scenario would be far higher-confidence if the mega block were in-window.

### Price vs flow `[INSIGHT:price_vs_flow]`
- **divergence = true**: "Price is up 1.1% but options flow is bearish (net flow −$166,751)." flow_direction bearish; price 11.72 → 11.85 (+1.11%).
- Read carefully: the divergence is **price vs OPTIONS flow** (the LEAP-put hedge), NOT price vs darkpool. Darkpool + price are aligned (both up/accumulating). So this is a minor early-caution flag from the hedging leg, not a darkpool contradiction.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`
- Only options_flow returned (flow_sentiment **bearish**, net −$166,751, P/C 0.265); **analyst consensus empty** (yfinance returned no rating block). No Wall-Street-vs-flow agreement read available — cross-source analyst view deferred to phase-7b/7c.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`
- signal **ACCUMULATION** — "dark pool buy volume significantly exceeds sell volume." buy_sell_ratio **1.58**, buy_side 17,304,526 vs sell_side 10,965,546 (07-13), total_dp_premium **$337.3M**, dark_pool_trades 2,964, VWAP **$11.93**, price_30d +1.11%.
- top_price_levels cluster $11.87–$11.92 (167/152/152 trades) — the current-range shelf just above the $11.80 mega-block level.

### Earnings play
- Skipped — earnings 2026-09-03 is >30d out (phase-6). Not an in-window IV/OI setup.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path |
|---------|--------------------------|
| `insights conviction-matrix --date 2026-07-13` | DIRECTIONAL_LONG 25.4% ← `.scenario`,`.confidence_pct` |
| `insights institutional-accumulation` | ACCUMULATION 1.58 ← `.signal`,`.buy_sell_ratio` |
| `insights price-vs-flow --lookback-days 30` | DIVERGENCE, flow bearish ← `.divergence`,`.divergence_signal` |
| `insights analyst-vs-flow` | flow bearish, no consensus ← `.options_flow.flow_sentiment` |
| `insights signal-confluence --min-score 1` (bull+bear) | PATH absent ← `select(.ticker=="PATH")` |

## Tool errors

- `analyst-vs-flow` returns only `{options_flow, symbol}` — no analyst consensus block (yfinance empty for PATH). Not fatal; analyst view is covered cross-source in phase-7b/7c.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent) | **agrees** phase-0.5/1 | quiet options, not a cross-sectional leader |
| conviction_matrix DIRECTIONAL_LONG | **agrees (understates)** phase-2 | blind to 07-09 mega; real accumulation stronger |
| institutional_accumulation ACCUMULATION 1.58 | **agrees strongly** phase-2 | independent confirmation on the 07-13 tape alone |
| price_vs_flow DIVERGENCE (bearish options) | **agrees** phase-1 | the LEAP-put hedge; early caution, not a DP contradiction |

## Verdict for downstream

- **UW composite bias:** **mildly BULLISH** — DIRECTIONAL_LONG + ACCUMULATION on the darkpool/call axis, but **low confidence (25.4%)** and flagged by a mild options-flow divergence.
- **Conviction:** 3/5.
- **Phase-9 baseline instruction:** treat the composite as **"accumulation-driven directional long, low-confidence, options-hedged."** The deep-dive's own knowledge of the **07-09 $644M mega block RAISES** this above the composite's blind 25.4%; the price-vs-flow divergence and quiet confluence LOWER any urgency. Override only with specific phase-7b/7c/8b evidence.
- **Open questions:** Does the fundamental veto (7b) support a genuine long, or is PATH a value trap absorbing a block? Does short interest / positioning (7c) explain the LEAP-put hedge? Is the 07-09 buyer strategic or a mechanical cross (still the pivotal unknown)?
