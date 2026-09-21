# Phase 7 — UW Insights Confluence

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite tools **agree with the upstream synthesis: a bearish options print
that nothing else confirms.** The conviction matrix lands on **MIXED** (put-ask
volume 2,041 dominates, but the dark pool is balanced at buy_ratio 0.543). Price-vs-
flow flags the central tension explicitly: **DIVERGENCE — price +33.4% while options
flow is bearish (net −$595,149)** — a leading reversal signal, but (per the heuristic)
often early, and here fighting phase-4's long-gamma pin. Institutional accumulation is
**NEUTRAL** (buy/sell 1.19, balanced). And CMPS is **absent from both the bearish and
bullish signal-confluence top-50** (cutoff score ≥4) — i.e. it is a *low-confluence*
name: the bearish read rests on one factor (the LEAP put), not a multi-factor stack.
Treat this as the baseline: **bearish flow, unconfirmed, divergent, low-confluence.**

## Key signals

- Conviction matrix **MIXED** (confidence 4.3%; put_ask 2,041 vs call_ask 891; DP
  buy_ratio 0.543) [INSIGHT:conviction_matrix]
- **Price-vs-flow DIVERGENCE**: "Price up 33.4% but options flow bearish (net
  −$595,149)" — leading reversal flag [INSIGHT:price_vs_flow]
- Institutional accumulation **NEUTRAL** (buy/sell 1.19, balanced DP)
  [INSIGHT:institutional_accumulation]
- **Low confluence**: CMPS absent from bearish (n=50, min score 4) AND bullish
  confluence lists → single-factor bear [INSIGHT:signal_confluence]
- analyst-vs-flow returns flow_sentiment **bearish** (net −$595,149); analyst
  consensus leg empty (deferred to 7b/7c) [INSIGHT:analyst_vs_flow]

## Detailed findings

### Deep-dive snapshot (`[INSIGHT:deep_dive]`)

Whole-tape `uw_screener` aggregates (reconciles with phase-1 / phase-0.5):

| Field | Value |
|-------|-------|
| bullish_premium | $179,048 |
| bearish_premium | $774,197 |
| **net_flow (derived)** | **−$595,149** |
| call_premium / put_premium | $250,780 / $737,595 |
| put_call_ratio | 1.3641 |
| implied_move / implied_move_perc | 0.519 / **4.14%** (phase-9 N4) |
| iv_rank | 20.35 |
| total_open_interest | 122,395 |

**Yahoo fundamentals leg unavailable** — `yahoo_fundamentals` returned `HTTP 401`
(rate-limited). Fundamentals sourced in phase-7b (Finnhub/fz/WebSearch) instead.

### Signal confluence (`[INSIGHT:signal_confluence]`)

- Bearish list: 50 names, all score **≥4**; **CMPS not present** → CMPS bearish
  confluence < 4. Bullish list: 50 names; **CMPS not present**. Low-confluence on
  both sides → the bearish signal is *not* corroborated by a stack of independent
  bearish factors; it is the one LEAP-put print.

### Conviction matrix (`[INSIGHT:conviction_matrix]`)

- `scenario` = **MIXED**, confidence_pct 4.3, thresholds bull 0.6 / bear 0.4.
- options_flow: call_ask 891, call_bid 520, **put_ask 2,041**, put_bid 198 →
  decisively put-ask-heavy (bearish flow), but…
- dark_pool: buy_ratio **0.543** (buy 226,142 / sell 190,696, 13 trades) →
  "Balanced dark pool activity — no clear bias." The balance is what pulls the
  composite off DIRECTIONAL_SHORT to MIXED.

### Price vs flow (`[INSIGHT:price_vs_flow]`)

- `divergence` = **true**; signal = "DIVERGENCE: Price is up 33.4% but options flow
  is bearish (net flow: $−595,149)." period_high 14.76, period_low 9.14, price
  9.39→12.53. This is the bearish-flow-into-rising-price reversal setup — leading but
  early; phase-4 long-gamma suppresses it near-term (per heuristic, pair before sizing).

### Analyst vs flow (`[INSIGHT:analyst_vs_flow]`)

- Returns only the options leg: flow_sentiment **bearish**, net −$595,149, P/C 1.364.
  No analyst consensus payload (yfinance leg empty for CMPS) → defer the Wall-Street
  comparison to phase-7b/7c.

### Institutional accumulation (`[INSIGHT:institutional_accumulation]`)

- `signal` = **NEUTRAL — balanced dark pool activity**; buy_sell_ratio 1.19; buy
  226,142 / sell 190,696; total DP premium $5,095,278. Top levels: $12.10 ($3.025M /
  250K sh), $12.53, $12.20 — confirms phase-2's $12.10 magnet. No accumulation OR
  distribution edge.

### Earnings play

- Earnings 2026-07-30 is **42 days out** (> 30d window) → out of the `earnings-play`
  window; skipped. The pre-earnings IV/OI setup is not yet live; revisit ~7/01.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights conviction-matrix --symbol CMPS` | scenario=MIXED, DP buy_ratio 0.543, put_ask 2,041 ← `.scenario,.dark_pool.buy_ratio` | 1 |
| `uw insights price-vs-flow --lookback-days 30` | divergence=true, +33.4% vs net −$595,149 ← `.divergence,.divergence_signal` | 30d |
| `uw insights institutional-accumulation` | NEUTRAL, buy/sell 1.19 ← `.signal,.buy_sell_ratio` | 13 DP |
| `uw insights analyst-vs-flow` | flow bearish, net −$595,149 ← `.options_flow.flow_sentiment` | — |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 50` | CMPS absent (n=50, min 4) ← `select(.ticker=="CMPS")` empty | 50 |
| `uw insights signal-confluence --direction bullish …` | CMPS absent ← idem | 50 |

## Tool errors

- `uw insights deep-dive` `yahoo_fundamentals` → `HTTP 401` (Yahoo rate-limit). The
  `uw_screener`/`uw_dark_pool`/`uw_top_oi_changes` legs returned fine; only the Yahoo
  fundamentals snapshot is missing. Fundamentals deferred to phase-7b. Not fatal.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (absent both sides) | **agrees** phases 1–3 | bear is single-factor (one LEAP put), not a confluence stack |
| conviction_matrix MIXED | **agrees** phase 2 | put-ask flow bearish, DP balanced → no clean directional edge |
| institutional_accumulation NEUTRAL | **agrees** phase 2 | balanced DP (aggregate 0.543 buy vs large-tier 0.398 sell reconcile to "mixed") |
| price_vs_flow DIVERGENCE | **agrees** phases 1 & 5 | bearish flow vs +33% trend = the core tension; phase-4 long-gamma caps it |

## DATA NOTE / CORRECTION

- DP buy-ratio reconciliation: conviction-matrix/inst-accum report **aggregate** DP
  buy_ratio 0.543 / 1.19 (includes the 100K block buy); phase-2 block-stratified
  reported the **large tier** at 0.398 (sell). Both are correct at their grain — the
  lone block buy lifts the aggregate to mild-buy; net DP = balanced. No re-read needed.

## Verdict for downstream phases

- **UW composite bias:** **MIXED — bearish flow, unconfirmed and divergent, low
  confluence.** The one genuine signal is the price-vs-flow divergence (a *potential*
  early reversal), not a confirmed directional short.
- **Conviction:** **3 / 5** — MIXED is a confident "no clean edge" read; the composite
  declines to validate the bear as directional.
- **Phase 9 baseline:** treat as **MIXED/neutral with a latent bearish-divergence
  tilt**. Only override toward a directional short with specific contrary evidence
  (e.g. the P10 LEAP OI builds on 6/19+, or 7b/7c surface a fundamental crack).
- **Open questions:** Does the divergence resolve down (flow right, fade the rally) or
  up (long-gamma + sector inflow win, flow was a hedge)? Phase-7b (fundamentals/cash
  runway) and 7c (short interest / analyst) must judge whether the bear has a
  fundamental basis or is pure positioning.
