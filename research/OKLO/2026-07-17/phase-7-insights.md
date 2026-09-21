# Phase 7 — UW Insights Confluence

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite reads **MIXED / low-confluence** — it does **not** hand us a clean
directional call. `conviction-matrix` = **MIXED at 9% confidence** ("balanced dark pool —
no clear bias"), `institutional-accumulation` = **NEUTRAL** (DP buy/sell 1.44, but labeled
balanced), and OKLO is in **neither** the bearish nor bullish `signal-confluence` top-50.
The single structured composite signal is **price-vs-flow DIVERGENCE = true**: *"price down
37.1% but options flow is bullish (+$397,772)."* On its face that is a "bullish reversal"
tell, **but phase-5 already showed this flow-tag has been wrong all month** (20/30 bullish
flow-days into a −37% move), so it reads as **noise, not an imminent bounce** — while
honestly flagging it as the *squeeze/reversal risk* to any short (it pairs with phase-4's
vanna-squeeze and max-pain-above-spot). Net: the composite baseline is **MIXED**; the
bearish tilt this blueprint carries comes from layers the composite under-weights
(sweep-persistence, positioning, structure, trend, fundamentals).

## Key signals

- **Conviction matrix MIXED, confidence 9%** — "balanced dark pool activity, no clear bias"
  [INSIGHT:conviction_matrix]
- **Ask/bid tape leans bearish**: call_bid_vol 13,939 > call_ask 11,025 (calls sold);
  put_ask 10,964 > put_bid 7,331 (puts bought) [INSIGHT:conviction_matrix.options_flow]
- **Price-vs-flow DIVERGENCE**: −37.1% price vs +$397,772 bullish net-flow — the
  unreliable-flow-tag / squeeze-risk signal [INSIGHT:price_vs_flow]
- **Institutional-accumulation NEUTRAL**: DP buy/sell 1.44, vwap $41.09, dp_prem $29.5M —
  mild dip-buy, not conviction accumulation [INSIGHT:institutional_accumulation]
- **No directional confluence**: OKLO outside both bearish and bullish signal-confluence
  top-50 → low-confluence name [INSIGHT:signal_confluence]

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates) — [INSIGHT:deep_dive]

(From the `uw_screener` block, cross-checked to phase-1/0.5): bullish_premium $8,702,389 vs
bearish_premium $8,304,617 → **net_flow +$397,772** (barely bullish); call_premium
$6,344,472 vs **put_premium $13,408,062** (2.1×); put_call_ratio 0.731; iv_rank 32.7; iv30d
97.5%; total_open_interest 701,517; implied_move_perc 0.00733 (**±0.73% — flagged suspect,
phase-6/phase-9 use IV-derived ~±25% to 08-10 earnings**). Consistent with phase-1.

### Signal confluence — [INSIGHT:signal_confluence]

- **Bearish, min-score 1, top-50:** tickers_found 50, **OKLO absent** → bearish confluence
  score below the top-50 cut.
- **Bullish, min-score 1, top-50:** **OKLO absent** → also below cut.
- Read: UW's factor-scoring finds OKLO **directionally diffuse** — no stacked confluence
  either way. Corroborates the MIXED conviction-matrix.

### Conviction matrix — [INSIGHT:conviction_matrix]

Scenario **MIXED**, confidence **9%**. Explanation: "Balanced dark pool activity — no clear
bias." options_flow ask/bid: **calls net sold** (bid 13,939 > ask 11,025), **puts net
bought** (ask 10,964 > bid 7,331) — an intraday bearish tilt inside a "mixed" label.
dark_pool buy_ratio 0.59 (mild buy). The bearish options tilt matches phase-1/3; the MIXED
label comes from the offsetting mild DP buy.

### Price vs flow — [INSIGHT:price_vs_flow]

**divergence = true.** `divergence_signal`: "Price is down 37.1% but options flow is bullish
(net flow $397,772)." price_start $65.39 → price_end $41.11. Standard heuristic = leading
bullish reversal, **but phase-5 disproves it for this name** (bullish flow-tag failed all
month). Treat as: (a) the flow-tag is unreliable → not a bounce signal; (b) it nonetheless
marks the **squeeze/mean-reversion RISK** to a short (with vanna + max-pain $47–50 + DP dip-buy).

### Analyst vs flow — [INSIGHT:analyst_vs_flow]

Returned **options_flow only** (flow_sentiment "bullish", net +$397,772) — **no analyst
consensus payload** (yfinance analyst side empty this call). Cannot score agreement; the
fundamentals/analyst read is deferred to phase-7b. Incomplete, not an error.

### Institutional accumulation — [INSIGHT:institutional_accumulation]

signal **"NEUTRAL — balanced dark pool activity."** buy_sell_ratio 1.44 (buy 422,892 / sell
293,904), total_dp_premium $29.45M, vwap $41.09, price_30d −37.1%. Mild dip-buying at ~$41
into a collapse — bottom-fishing, tool-labeled neutral. Matches phase-2 large-tier 0.611 buy.

### Earnings play — [INSIGHT:earnings_play]

Earnings 2026-08-10 (~24d, in-window). Tool returned 10 top market-wide setups; **OKLO not
among them** → not flagged as a premier earnings-vol setup despite the in-window date. Note
only; IV rank 32.7 is mid, so no standout pre-earnings IV-rank signal.

## Tool calls (audit trail)

| Command | Key value ← `jq` path | Notes |
|---|---|---|
| `insights conviction-matrix` | MIXED, 9% ← `.scenario/.confidence_pct` | calls sold/puts bought |
| `insights price-vs-flow --lookback 30` | divergence true, −37.1% vs +$398K ← `.divergence_signal` | flow-tag unreliable |
| `insights institutional-accumulation` | NEUTRAL, 1.44 ← `.signal/.buy_sell_ratio` | vwap 41.09 |
| `insights analyst-vs-flow` | options-only (no analyst) ← `.options_flow` | incomplete |
| `insights signal-confluence bearish/bullish --min-score 1 --top-50` | OKLO absent both ← filtered `.results[]` | low-confluence |
| `insights earnings-play --days 30` | OKLO absent (10 rows) ← `.results[]` | not a top setup |

## Tool errors

None fatal. `analyst-vs-flow` returned no analyst consensus block (yfinance) — deferred to
phase-7b. `earnings-play`/`signal-confluence` "OKLO absent" is information (below cut), not error.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| conviction_matrix = MIXED (9%) | partial | DP-balanced label agrees w/ phase-2; but under-weights phase-1 5-day bearish persistence + phase-3 put-building |
| price_vs_flow = divergence (bullish flow / falling price) | agree w/ phase-5 | phase-5 already flagged the flow-tag as unreliable → divergence = noise + squeeze-risk, not a bounce |
| institutional_accumulation = NEUTRAL | agree w/ phase-2 | mild large-tier dip-buy, no mega conviction |
| signal_confluence (OKLO absent both) | agree | matches phase-0.5 "BUSY_NAME_NORMAL_DAY / not unusual" |

## Verdict for downstream

- **UW composite bias:** **MIXED / low-confluence (9% confidence)** — no clean directional
  edge from the composite tools alone.
- **Conviction:** 2 / 5 (the composite itself is low-conviction; the actionable tilt lives
  in the flow-persistence / structure / trend / fundamentals layers, not here).
- **Phase-9 guidance:** treat this MIXED read as the **baseline**. The blueprint's **bearish
  tilt** is a deliberate override justified by *specific* upstream evidence the composite
  under-weights — 5-day bearish sweep persistence ($41M), put-building + confirmed roll,
  FULLY_NEGATIVE GEX + dealer-sell DEX, −37% trend, and the fundamental de-rating (phase-6).
  Size **modestly / defined-risk** and treat the price-vs-flow divergence + vanna-squeeze +
  max-pain $47–50 + DP dip-buy as the **explicit reversal risk**.
- **Open questions:** Does phase-7b fundamentals confirm the de-rating (quality veto that
  hardens the short) or find a floor? Does phase-7c short-interest/positioning show the
  short is crowded (squeeze fuel)? Does the phase-8 desk + phase-8b debate resolve
  bearish-tilt-vs-squeeze-risk?
