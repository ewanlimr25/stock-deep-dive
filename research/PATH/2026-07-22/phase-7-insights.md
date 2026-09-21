# Phase 7 — UW Insights Confluence

**Ticker:** PATH · **As-of:** 2026-07-22 · **Spot:** $10.53 · **Generated:** 2026-07-22
**Upstream:** phases 1–6 (mixed flow, balanced DP, long-gamma pin, OpenAI headwind)

## Summary

UW's composite tools **agree with the upstream read: MIXED, low-conviction, no clear
directional edge.** The conviction-matrix returns **MIXED (3.7% confidence)** —
"balanced dark pool, no clear bias"; institutional-accumulation is **NEUTRAL**
(buy/sell ratio 1.16); and price-vs-flow reports the flow is **bearish but "aligned"
with price** (no reversal divergence). PATH appears in **neither** the bullish nor the
bearish signal-confluence list even at `min-score 1`, i.e. its multi-factor score is
**below 1 in both directions** — this is a genuinely two-sided name today, not a
high-confluence setup. The options-flow micro-structure confirms phase-1: **calls net
SOLD (bid 33,934 > ask 27,737), puts net BOUGHT (ask 16,391 > bid 9,419)** = bearish
aggressor, while dark pool is a balanced 0.537 buy. Nothing here overrides phases 1–6;
it ratifies a **no-edge / defined-risk** baseline into the OpenAI-driven impairment.

## Key signals

- **Conviction matrix = MIXED, 3.7% confidence** — "balanced dark pool activity, no clear bias" `[INSIGHT:conviction_matrix]`.
- **PATH absent from bullish AND bearish signal-confluence (min-score 1)** — score <1 both ways; no factor stack `[INSIGHT:signal_confluence]`.
- **Institutional accumulation NEUTRAL** — buy/sell 1.16, balanced `[INSIGHT:institutional_accumulation]`.
- **Price-vs-flow ALIGNED (bearish flow, weak price)** — no reversal divergence; net_premium_flow −$1.60M over 30d `[INSIGHT:price_vs_flow]`.
- **Options micro-structure bearish** — calls net-sold, puts net-bought `[INSIGHT:conviction_matrix]`.

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

- **Whole-tape aggregates (reconciled vs phase-1):** call_premium $4.16M / put_premium $1.29M; bullish_premium $1.66M / bearish_premium $3.26M → **derived net_flow −$1.60M** (net bearish); put_call_ratio 0.419; implied_move_perc **4.70%**; iv_rank 45.6. Consistent with phase-0.5 `[CTX:]` and phase-1.
- **Fundamentals via deep-dive UNAVAILABLE** — `yahoo_fundamentals` returned **HTTP 401** (Yahoo blocked). Substitute (phase-0 `fz` + WebSearch, pending phase-7b Finnhub): market cap **$5.54B**, EV **$4.32B**, sales (TTM) **$1.67B**, income $327M, book/sh $3.66, cash/sh $2.53; most-recent quarterly revenue **$418.4M, +17.3% YoY** (WebSearch). Full fundamentals + quality veto → phase-7b.
- top OI changes (deep-dive): P11 8/21 +898, C13 7/24 +598 — the same trivial builds as phase-3.

### Signal confluence `[INSIGHT:signal_confluence]`

Market-wide, min-score 1, both directions: **PATH not returned in either list.** Its
confluence score is below 1 bullish and below 1 bearish → **no coherent multi-factor
signal** in UW's scoring. Corroborates the phase-1→4 conviction of 2–3/5.

### Conviction matrix `[INSIGHT:conviction_matrix]`

- Scenario **MIXED**, confidence **3.7%**, explanation "Balanced dark pool activity — no clear bias."
- options_flow: call_ask 27,737 / call_bid **33,934** (calls net sold); put_ask **16,391** / put_bid 9,419 (puts net bought) → **bearish aggressor micro-structure.**
- dark_pool: buy_ratio 0.537 (mild buy), buy_vol 6.87M / sell_vol 5.92M, 963 trades → balanced. Matches phase-2.

### Price vs flow `[INSIGHT:price_vs_flow]`

- 30d: price_start 10.75 → price_end 10.70 (**−0.47%**), period_high **12.55**, period_low **9.87**; flow_direction **bearish**, net_premium_flow **−$1.60M**.
- **divergence_signal: "Price and flow are aligned."** No contrarian reversal signal — bearish flow matches weak price. This **tempers** phase-5's mean-reversion-bounce lean: there is no positive divergence arguing for a snap-back; the flow confirms the weakness. (The −0.47% is the 30d net; the crash is today, so "aligned" here means the quarter's flow already leaned bearish.)
- Current $10.53 sits mid-lower in the 9.87–12.55 30d range, above the low.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

- UW tool returned **empty** (yfinance consensus not populated; only `options_flow`/`symbol` keys). Recorded as unavailable.
- **Substitute (WebSearch, phase-6):** UBS **Neutral, PT $12** (cut from $13), Truist **Hold, PT $12**. Options flow bearish. → analysts Neutral/Hold + bearish flow = **roughly aligned, cautious**; PTs cap upside at **$12**.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

- Signal **"NEUTRAL — balanced dark pool activity."** buy_sell_ratio 1.16, total DP premium $136.9M, **VWAP $10.70**, avg_trade_price $10.68, price_30d −0.47%.
- Note: close (~$10.53) is **below** the day's DP VWAP $10.70 — late sellers pressed under the institutional average. Consistent with phase-2's balanced-to-mildly-distributive verdict.

### Earnings play

**Out of window** — next earnings ~Sep 3–8, 2026 (>30d; phase-6). `earnings-play` not
run. The 7/24 IV kink is shock-residual, not an earnings event (phase-6).

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| conviction matrix | `uw insights conviction-matrix --symbol PATH --date 2026-07-22 --json` | `.{scenario,confidence_pct,explanation,options_flow,dark_pool}` |
| price vs flow | `uw insights price-vs-flow --symbol PATH --lookback-days 30 --json` | `.{price_change_pct,period_high,period_low,flow_direction,net_premium_flow,divergence_signal}` |
| analyst vs flow | `uw insights analyst-vs-flow --symbol PATH --json` | empty → WebSearch substitute |
| inst accumulation | `uw insights institutional-accumulation --symbol PATH --json` | `.{signal,buy_sell_ratio,vwap,total_dp_premium}` |
| signal confluence | `uw insights signal-confluence --direction bullish\|bearish --min-score 1 --top-n 50 --json` | filter PATH → absent both |
| deep dive | `uw insights deep-dive --symbol PATH --date 2026-07-22 --json` | `.uw_screener.*`; `.yahoo_fundamentals` = HTTP 401 |

## Tool errors

- `uw insights deep-dive` `.yahoo_fundamentals` → **HTTP 401** (Yahoo quoteSummary blocked). Fundamentals sourced from `fz`/WebSearch/Finnhub instead (phase-7b).
- `uw insights analyst-vs-flow` → empty (no yfinance consensus). WebSearch analyst substitute used.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (PATH absent both) | **agrees** phases 1–4 (conviction 2–3) | no factor stack either way |
| conviction_matrix (MIXED) | **agrees** phase-1 (mixed), phase-2 (mixed) | bearish aggressor micro-structure confirms phase-1 |
| institutional_accumulation (NEUTRAL) | **agrees** phase-2 (balanced/mild-distributive) | VWAP 10.70 > close = late selling |
| price_vs_flow ("aligned", bearish) | **agrees** phase-6 (name headwind); **tempers** phase-5 bounce | no reversal divergence to lean long on |

## Verdict for downstream

- **UW composite bias: MIXED / mildly bearish-neutral, LOW conviction.** No multi-factor edge; balanced institutional flow; bearish options aggressor aligned with weak price; upside analyst-capped at $12.
- **Conviction: 2/5** (the composite's own confidence is 3.7%).
- **Phase-9 baseline:** treat as **no directional edge → defined-risk, half-size** (consistent with the phase-6 regime guidance). Override only with specific contrary evidence from phases 7b/7c/8/8b. The absence of a reversal divergence means a pure mean-reversion long is **not** endorsed by the composite — any long must lean on the long-gamma pin + DEX bid, not on a flow reversal.
- **Open questions:**
  - Does the fundamental layer (7b) reveal quality strong enough to defend $10 despite the OpenAI overhang, or a deteriorating story that validates the de-rate?
  - Does positioning/short-interest (7c) show a crowded short that could squeeze, or complacent longs (phase-4 skew) vulnerable to more downside?
