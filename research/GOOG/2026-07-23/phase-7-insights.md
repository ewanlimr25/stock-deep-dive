# Phase 7 — UW Insights Confluence

**Ticker:** GOOG · **As-of:** 2026-07-23 · **Spot:** $318.34
**Generated:** 2026-07-24T01:18:35Z
**Upstream:** phases 1–6. This phase consolidates; it should AGREE with them.

## Summary

UW's own composite instrumentation returns **MIXED / no-directional-edge**, which
matches the phase-by-phase read exactly. The **conviction matrix is MIXED at just
2.9% confidence** ("Balanced dark pool activity — no clear bias"); **institutional
accumulation is NEUTRAL** (dark-pool buy/sell 1.12); and GOOG scores **below 1 on
*both* bullish and bearish signal-confluence** — there is no clean directional
stack in either direction. The one clearly-signed input is options flow: **bearish**
(net −$49.4M; calls net *sold* on the bid, puts net *bought* on the ask), and the
`price-vs-flow` tool reads this as **ALIGNED** with the −9.9% price move — i.e. the
tool sees momentum-confirmation, **not** a reversal divergence. That is the central
tension of this dive: the simple flow-vs-price tool says "bearish momentum
continues," while the structural layer (phase-4: long-gamma, complacent IV,
max-pain above, earnings cleared) says "mean-reversion bounce setup." UW's baseline
is a genuinely two-sided, low-conviction tape with a bearish flow tilt.

## Key signals

- **Conviction matrix MIXED, confidence 2.9%** — no clear bias. `[INSIGHT:conviction_matrix]`
- **Institutional accumulation NEUTRAL** — buy/sell 1.12, DP premium $3.07B, 30d
  price −9.9%. `[INSIGHT:institutional_accumulation]`
- **Signal-confluence: GOOG absent both directions** (score <1 bull AND bear) — no
  confluence stack. `[INSIGHT:signal_confluence]`
- **Price-vs-flow ALIGNED** (flow bearish, price −9.9%) — momentum-confirmation, no
  reversal divergence flagged. `[INSIGHT:price_vs_flow]`
- **Options flow internals bearish:** call_bid 159,292 > call_ask 129,569 (calls
  sold); put_ask 112,843 > put_bid 96,017 (puts bought). `[INSIGHT:conviction_matrix]`

## Detailed findings

### Deep dive snapshot (`uw_screener` whole-tape, from phase-0.5/1 feed) — `[INSIGHT:deep_dive]`
- bullish_premium $258.66M · bearish_premium $308.05M · **derived net_flow −$49.38M**
- call_premium $215.91M · put_premium $406.60M · P/C 0.7126
- **implied_move 1.57% / $4.99** (phase-9 N4 sizes to this — post-earnings, deflating)
- iv30d 0.324 · iv_rank 38.3 · total_open_interest 1,679,706 · next_earnings 2026-11-04
- Reconciles with phase-1 aggregate and phase-0.5 `[CTX:]` (GOOG #6 net-bearish
  universe, net-dir pctile 0.0).

### Signal confluence — `[INSIGHT:signal_confluence]`
GOOG **not present** in either the bearish (`--direction bearish --min-score 1`) or
bullish (`--min-score 1`) top-40 → score < 1 both ways. No 5+/6 high-conviction
confluence; consistent with MIXED.

### Conviction matrix — `[INSIGHT:conviction_matrix]`
scenario **MIXED**, confidence **2.9%**. explanation: "Balanced dark pool activity —
no clear bias." options_flow: call_ask 129,569 / call_bid 159,292 (net call
selling), put_ask 112,843 / put_bid 96,017 (net put buying) → bearish options tilt.
dark_pool buy_ratio 0.529 (balanced). Net = MIXED (bearish options + balanced DP).

### Price vs flow — `[INSIGHT:price_vs_flow]`
divergence_signal: **"Price and flow are aligned"**; flow_direction bearish;
price_change −9.9%; net_premium_flow −$49.4M; 30d range 374.35 → 314.89 (spot 318.34
near the low). **No reversal divergence.** (Caveat: the tool's divergence logic only
fires on flow-vs-price disagreement; it does not incorporate the phase-4 structural
mean-reversion factors — so "aligned/bearish" here is momentum-read, not a verdict
against a bounce.)

### Analyst vs flow — `[INSIGHT:analyst_vs_flow]`
Only `options_flow` returned (flow_sentiment **bearish**, net −$49.4M); **no analyst
consensus** came back from the yfinance side this run. Wall-Street-vs-flow
comparison deferred to phase-7b/7c (Finnhub/`fz` analyst data).

### Institutional accumulation — `[INSIGHT:institutional_accumulation]`
signal **NEUTRAL — balanced dark pool activity**; buy_sell_ratio 1.12 (buy vol
5,047,357 / sell vol 4,498,126); total_dp_premium $3.07B; 30d price −9.9%. Confirms
phase-2 (no accumulation/distribution).

### Earnings play
**Out of window** — next earnings 2026-11-04 (>30d); tool not run (phase-6 confirms
Q2 already reported 07-22).

## Tool calls
| Tool | Args | jq path |
|---|---|---|
| insights deep-dive | --symbol GOOG --date 2026-07-23 (from phase-0.5) | `.uw_screener.*` |
| insights conviction-matrix | --symbol GOOG --date 2026-07-23 | `.{scenario,confidence_pct,explanation,options_flow,dark_pool}` |
| insights price-vs-flow | --symbol GOOG --lookback-days 30 | `.{divergence_signal,flow_direction,price_change_pct,net_premium_flow,period_high,period_low}` |
| insights analyst-vs-flow | --symbol GOOG | `.options_flow.{flow_sentiment,net_flow}` |
| insights institutional-accumulation | --symbol GOOG | `.{signal,buy_sell_ratio,buy_side_volume,sell_side_volume,total_dp_premium}` |
| insights signal-confluence | --direction bearish/bullish --min-score 1 --top-n 40 | GOOG absent both |

## Tool errors
- `insights analyst-vs-flow` returned only the options-flow block (no analyst
  consensus from yfinance) — not fatal; analyst data sourced in phase-7b/7c.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent both) | **agrees** phase-3/5/7 | two-sided book, no clean stack |
| conviction_matrix (MIXED 2.9%) | **agrees** phase-1/2/3 | bearish options + balanced DP |
| institutional_accumulation (NEUTRAL) | **agrees** phase-2 | mega/large buy_ratio ~0.52-0.54 |
| price_vs_flow (ALIGNED bearish) | **tensions with** phase-4/5 | momentum-read vs mean-reversion structure; the dive's core question |

## Verdict for downstream

- **UW composite bias: MIXED / low-edge, with a bearish options-flow tilt.**
  Explicitly no directional confluence (score <1 both ways), neutral institutions,
  balanced dark pool. The only signed vector is bearish flow, read by UW as
  momentum-aligned with the −9.9% drop.
- **Conviction: 2 / 5.** UW's own confidence is 2.9% — this is a no-clear-edge tape.
- **Phase-9 baseline:** treat this as **MIXED / no-directional-conviction**. Do NOT
  size a high-conviction directional bet on the UW composite alone. Any directional
  lean must come from the specific structural/contrarian evidence (phase-4
  mean-reversion + phase-6 earnings-cleared/IV-crush) OR the momentum-continuation
  case (phase-5 bearish_flow backtest + price-vs-flow aligned) — phases 8/8b arbitrate.
- **Open questions:**
  - Reversal vs continuation: does the earnings-cleared, long-gamma, complacent-IV
    structure win (bounce), or does the aligned bearish momentum + sector risk-off
    win (grind to 300 put wall)? → phase-8 desk views, phase-8b debate.
  - Is the capex/FCF de-rate a permanent multiple reset (bearish floor lower) or an
    overshoot on a +24% rev / +82% Cloud quarter (bullish snapback)? → phase-7b.
