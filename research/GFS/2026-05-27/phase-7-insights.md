# Phase 7 — UW Insights Confluence

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite tools **independently converge on MIXED/NEUTRAL with a bearish flow
divergence** — exactly what phases 1–6 found from the raw cuts, so the run is
internally consistent. The **conviction matrix is MIXED** (confidence 8.2%),
**institutional-accumulation is NEUTRAL** (dark-pool buy/sell 1.39, "balanced"), and
GFS is **absent from both the bullish and bearish signal-confluence lists** (no
directional factor score either way). The one directional composite is the standout:
**price-vs-flow flags DIVERGENCE = TRUE — "price up 60.6% but options flow is
bearish"** — a recognized leading reversal signal that corroborates the
distribution-at-the-top (phase-2), call-writing (phase-1/3), short-gamma (phase-4),
and tech-rotation-out (phase-6) stack. The baseline UW read is therefore **not a
long**: it is "extended name, churny/slightly-bearish flow, reversal risk flagged."
Note Wall Street (Susquehanna PT $125, phase-6) is bullish while flow is bearish —
**analyst-vs-flow itself diverges**.

## Key signals

- **Conviction matrix: MIXED**, confidence 8.2% (DP buy_ratio 0.582 vs bull-threshold
  0.60; call_bid 5,885 > call_ask 4,171) `[INSIGHT:conviction_matrix]`.
- **Price-vs-flow: DIVERGENCE TRUE** — "price +60.6% but flow bearish, net
  −$297,698", period high $92.55 / low $48.50 `[INSIGHT:price_vs_flow]`.
- **Institutional-accumulation: NEUTRAL** — buy/sell 1.39, "balanced dark pool"
  `[INSIGHT:institutional_accumulation]`.
- **Signal-confluence: GFS in neither list** (score < min even at min-score 1) — no
  directional confluence `[INSIGHT:signal_confluence]`.
- **Analyst-vs-flow:** flow_sentiment **bearish** (net −$297,698); analyst side
  missing from tool, but phase-6 WebSearch has Susquehanna **Positive / PT $125** →
  **Street bullish vs flow bearish** `[INSIGHT:analyst_vs_flow]`.

## Detailed findings

### Deep-dive snapshot (whole-tape `uw_screener` block) `[INSIGHT:deep_dive]`

| field | value |
|-------|------:|
| bullish_premium | $4,500,876 |
| bearish_premium | $4,798,574 |
| **net_flow** | **−$297,698 (bearish)** |
| call_premium / put_premium | $8.37M / $1.93M |
| put_call_ratio | 0.33 |
| implied_move / perc | **11.03 / 13.6%** `[CTX:implied_move_pct]` |
| iv30d / iv_rank | 82.3% / 79.1 |
| total_open_interest | 92,437 |
| dark-pool total premium | $202.7M (2.49M sh, 534 trades, avg $81.35) |
| next_earnings | 2026-08-04 (outside 30d) |

Reconciles to the dollar with phase-1's aggregate and phase-0.5's `[CTX:]` rank
(net-dir 5.6 universe pctile). Whole-tape is slightly net-bearish on a top-5%
premium day.

### Signal confluence `[INSIGHT:signal_confluence]`

GFS appears in **neither** the bullish nor the bearish top-50 even at `--min-score 1`.
No multi-factor confluence has formed in either direction — the textbook signature of
a genuinely **mixed** name (vs phase-7 heuristic "≥5 is rare/high-conviction").

### Conviction matrix `[INSIGHT:conviction_matrix]`

scenario **MIXED**, confidence **8.2%**. DP buy_ratio 0.582 (just under the 0.60 bull
threshold). Options flow call_ask 4,171 vs call_bid **5,885** (call selling
dominates), put_ask 1,433 vs put_bid 1,795. "Balanced dark pool — no clear bias."
**Matches phases 1–4 exactly.**

### Price vs flow `[INSIGHT:price_vs_flow]`

**divergence: TRUE.** "Price is up 60.6% but options flow is bearish (net flow
−$297,698)." period_high $92.55, period_low $48.50, price_start $50.39 → end $80.93,
flow_direction bearish, iv_rank 79.1. This is the **leading reversal signal** — pair
with phase-4's short-gamma regime (which says a reversal, once underway, accelerates).
The signal is "often early," but here it is **confirmed by an actual −9.7% as-of day**.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Tool returned only the options side: flow_sentiment **bearish**, net −$297,698, P/C
0.33. Analyst/consensus side **absent** (yfinance unavailable — phase-0.5 yahoo
HTTP 401). From phase-6 WebSearch the Street is **bullish** (Susquehanna PT $125,
Positive; tickeron earnings-driven upgrades). → **Street bullish, flow bearish** — a
disagreement the debate (phase-8b) should adjudicate.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

signal **NEUTRAL — balanced dark pool**; buy_sell_ratio 1.39 (buy 1.45M / sell 1.04M),
price_30d +60.49%. top_price_levels today: $80.72 ($14.2M), $82.75 ($11.3M), $81.11.
**Caveat:** this tool's levels are *today's*; phase-2's 5-day `price-levels` surfaced
the more important **$91–92 distribution cluster** — use phase-2 for structure.

### Earnings play

**Skipped** — next earnings 2026-08-04 is outside the 30-day window (phase-6
calendar). Not an error.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw insights conviction-matrix --symbol GFS` | **MIXED**, 8.2% conf |
| `uw insights price-vs-flow --lookback-days 30` | **DIVERGENCE TRUE** (price +60.6%, flow bearish) |
| `uw insights institutional-accumulation` | **NEUTRAL**, buy/sell 1.39 |
| `uw insights analyst-vs-flow` | flow bearish; analyst side missing |
| `uw insights signal-confluence --direction bullish/bearish` | **GFS in neither list** |
| `uw insights deep-dive --symbol GFS --date 2026-05-27` | screener block (above) |

## Tool errors

- `uw insights analyst-vs-flow` returned no analyst/consensus block (yfinance
  unavailable — same root as phase-0.5 yahoo HTTP 401). Street view sourced from
  phase-6 WebSearch instead.

## Cross-check vs phases 1–6

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (neither list) | **agrees** phases 1,7 | no directional edge — matches MIXED |
| conviction_matrix MIXED | **agrees** phases 1–4 | call-selling + balanced DP |
| price_vs_flow DIVERGENCE | **agrees** phases 0.5,2,4,5 | confirms post-parabolic reversal risk |
| institutional_accumulation NEUTRAL | **agrees** phase-2 | weak buy_ratio, no whale |
| analyst_vs_flow (Street bull vs flow bear) | tension w/ phase-6 | Street PT $125 vs bearish tape → phase-8b |

No contradictions — every composite tool corroborates the raw-cut read.

## Verdict for downstream

- **UW composite bias:** **MIXED / NEUTRAL, with an active bearish reversal-divergence
  overlay.** Not a directional long; leans "fade the extension / respect downside."
- **Conviction:** **3.5/5** — the composite is decisively *mixed* (high confidence
  that there is no clean long), and the price-vs-flow divergence adds a genuine
  reversal tell.
- **Phase-9 baseline:** treat this as **MIXED-with-downside-skew**. Override toward
  bullish only with specific contrary evidence (e.g., fundamentals phase-7b finding
  the re-rate cheap, or debate phase-8b breaking the bear case). The default
  structure is range/credit/defined-risk, not a naked directional long.
- **Open questions:** Does the fundamental re-rate (phase-7b) justify holding through
  the extension, making this a *buy-the-dip* rather than a *fade*? Does short interest
  / positioning (phase-7c) say the final leg was a squeeze (→ more downside on
  unwind) or real demand? (phase-8b resolves Street-bull-vs-flow-bear.)
