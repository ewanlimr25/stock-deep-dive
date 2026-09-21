# Phase 7 — UW Insights Confluence

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T13:12:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md,
phase-3-positioning.md, phase-5-historical.md

## Summary

UW's own composite engines land where phases 1–5 did, which validates the
chain's internal consistency: **bearish flow direction on a neutral
institutional base, with no high-conviction stack**. `conviction-matrix`
classifies HOOD as **MIXED (confidence 8.4%)** — "Balanced dark pool activity
— no clear bias"; `institutional-accumulation` reads **"NEUTRAL — balanced
dark pool activity"**; `price-vs-flow` finds **no divergence** ("Price and
flow are aligned": price −2.64%/30d alongside bearish net flow −$13,575,317);
and HOOD is **absent from both the bullish and bearish `signal-confluence`
top-20 at min-score 1** — there is no 3+-factor setup here, in either
direction. The composite's one unambiguous directional datapoint is the flow
itself: bearish_premium $57.61M > bullish_premium $44.04M (derived net_flow
−$13.58M), with call-side selling confirmed in the matrix's ask/bid split
(call bid 198,276 > call ask 159,136). Yahoo fundamentals errored (HTTP 401)
— deferred to phase-7b/Finnhub.

## Key signals

- `conviction-matrix`: scenario **MIXED**, confidence_pct **8.4**, explanation
  verbatim "Balanced dark pool activity — no clear bias"; options_flow split:
  call_ask 159,136 vs call_bid **198,276** (net −39,140 = call supply ✓
  phase-1), put_ask 70,245 vs put_bid 69,973 (puts dead-even)
  [INSIGHT:conviction_matrix]
- `institutional-accumulation`: signal **"NEUTRAL — balanced dark pool
  activity"**, buy_sell_ratio 1.40, vwap 82.79, top level 82.47 ($44.86M)
  [INSIGHT:institutional_accumulation]
- `price-vs-flow`: **divergence false** — flow bearish AND price falling
  (−2.64% over the window, 84.71→82.47; period range 69.93–94.40) — no
  reversal signal, trend-confirming [INSIGHT:price_vs_flow]
- `signal-confluence`: HOOD **not in bearish top-20** (leaders MTUM 6, IRDM 6)
  **nor bullish top-20** (TLRY/VXX/BITX 6) at `--min-score 1` — no factor
  stack [INSIGHT:signal_confluence]
- `analyst-vs-flow`: analyst block **empty** (yfinance thin — known); options
  side restates flow_sentiment "bearish", net_flow −13,575,317
  [INSIGHT:analyst_vs_flow]

## Detailed findings

### Deep dive snapshot [INSIGHT:deep_dive]

- `uw_screener` directional aggregates (whole-tape; reconciled vs phase-1 ✓
  and phase-0.5 [CTX:] rank #33 bearish ✓): bullish_premium **$44,036,989** vs
  bearish_premium **$57,612,306** → derived net_flow **−$13,575,317** (no
  `net_flow` key in this block); call_premium $81,433,934 vs put_premium
  $32,060,841; P/C ratio 0.40; `implied_move` $0.5998 / `implied_move_perc`
  **0.727%** (phase-9 N4 input — with phase-6's caveat that realized daily
  swings ran ±6%); iv_rank 49.59; total OI 2,139,203.
- `uw_dark_pool`: total_premium $376,412,130 / 4,546,754 sh / 1,584 trades /
  avg 82.96 — matches phase-2 ✓.
- `uw_top_oi_changes`: Jun-05 86C/100C/90C (0DTE artifacts), Jun-12 87C
  +2,597, Sep-18 90C +2,469 — matches phase-3 ✓.
- `yahoo_fundamentals`: **error** "yahoo quoteSummary HOOD: HTTP 401" —
  surfaced verbatim below; phase-7b covers fundamentals via Finnhub.

### Signal confluence [INSIGHT:signal_confluence]

Absent from both direction lists at min-score 1 / top-n 20 (bearish leaders
MTUM 6, IRDM 6, NASA 5; bullish TLRY 6, VXX 6, BITX 6). Read: HOOD's bearish
day is a *single-axis* signal (premium direction), not a multi-factor
confluence — exactly phase-0.5's "GENUINELY_UNUSUAL in direction, not size".

### Conviction matrix [INSIGHT:conviction_matrix]

MIXED @ 8.4% confidence (thresholds bear ≤0.40 / bull ≥0.60; DP buy_ratio
0.584 sits in the dead zone). ⚠ Reconciliation: this 0.584 is the *all-trades
volume* ratio (2,655,779 buy / 1,890,975 sell) **including** the 429k-share
EOD cross phase-2 de-rated; phase-2's tier-level ratios (block 0.543 / large
0.540) are the cleaner institutional read. Both land "balanced".

### Price vs flow [INSIGHT:price_vs_flow]

No divergence — bearish flow with falling price = alignment, a
trend-confirmation (not the early-reversal pattern). Period stats: high 94.40
/ low 69.93 / end 82.47.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

Analyst consensus block empty (yfinance) — no agreement test possible from
this tool. Phase-6 found DB raising PT to $98 on the as-of day (WebSearch);
phase-7b's analyst cross-source will quantify street consensus properly.

### Institutional accumulation [INSIGHT:institutional_accumulation]

NEUTRAL. buy_sell_ratio 1.40 (volume basis, EOD-cross caveat as above), VWAP
82.79 vs close 82.47 (closed 0.4% under institutional VWAP — fractionally
weak). Top levels: 82.47 ($44.9M), 80.60 ($3.9M), 86.24 ($3.6M), 83.50
($3.3M), 80.00 ($3.1M) — consistent with phase-2's at-spot shelf + 80-zone
prints.

### Earnings play

Skipped — next earnings 2026-07-29 (phase-0.5 `uw_screener`), 54 days out,
beyond the 30-day window. (Date itself re-verified in phase-7b/7c — UW field
can be stale.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol HOOD --date 2026-06-05 --json` | DP $376.4M ← `.uw_dark_pool.total_premium`; OI Δs ← `.uw_top_oi_changes[:5]`; Yahoo error ← `.yahoo_fundamentals.error` | blocks |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --date 2026-06-05 --json` | HOOD absent ← `select(.ticker=="HOOD")` (empty); leaders ← `.results[:3]` | top-20 |
| same, `--direction bullish` | HOOD absent ← same | top-20 |
| `uw insights conviction-matrix --symbol HOOD --date 2026-06-05 --json` | MIXED / 8.4 / 0.584 ← `.scenario, .confidence_pct, .dark_pool.buy_ratio`; flow split ← `.options_flow.*` | summary |
| `uw insights price-vs-flow --symbol HOOD --lookback-days 30 --json` | divergence=false ← `.divergence, .divergence_signal`; −2.64% ← `.price_change_pct` | summary |
| `uw insights analyst-vs-flow --symbol HOOD --json` | analyst block empty; flow bearish ← `.options_flow.flow_sentiment` | summary |
| `uw insights institutional-accumulation --symbol HOOD --json` | NEUTRAL / 1.40 / vwap 82.79 ← `.signal, .buy_sell_ratio, .vwap`; levels ← `.top_price_levels[:5]` | summary |
| `uw insights earnings-play` | SKIPPED — earnings 54d out (>30d window) | — |

(`price-vs-flow`, `analyst-vs-flow`, `institutional-accumulation` are
trailing/latest-anchored; latest = as-of = 2026-06-05, point-in-time clean.)

## Tool errors

- `uw insights deep-dive` → `yahoo_fundamentals`: `"yahoo quoteSummary HOOD:
  HTTP 401"` (verbatim). Fundamentals deferred to phase-7b (Finnhub + fz).
- `analyst-vs-flow`: analyst block returned empty (yfinance thin) — recorded
  as no-data, not an error.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (no stack) | **agrees** w/ phase-0.5 | direction-only unusualness; no size/multi-factor confirmation |
| conviction_matrix MIXED | **agrees** w/ phase-2 (balanced DP) + phase-3 (two-way book) | call bid>ask split independently re-confirms phase-1's call supply |
| price_vs_flow (aligned, no divergence) | **agrees** w/ phase-1 | bearish flow + falling price = continuation, not reversal |
| institutional_accumulation NEUTRAL | **agrees** w/ phase-2 | 1.40 ratio inflated by EOD cross; tier ratios are the clean read |
| flow_sentiment bearish, net −$13.58M | **agrees** w/ phase-1 | identical derived figure across 3 tools |

No upstream phase is contradicted by the composite — the run is internally
consistent; the composite simply caps how much conviction the bearish lean
deserves.

## Verdict for downstream phases

- **UW composite bias:** **mildly bearish** — bearish single-axis flow on a
  MIXED/NEUTRAL institutional base; no confluence stack, no divergence.
- **Conviction:** 2.5 (recorded as 2–3: the direction is consistent
  everywhere, but every composite engine independently refuses to call it
  high-conviction)
- **Phase 9 must treat this as the BASELINE** and only exceed it with the
  specific structural/macro evidence of phases 4 & 6 (short gamma + OPEX
  gravity at 80 + macro headwind + FOMC 6/17), which the UW composites do not
  model.
- **Open questions:** Do fundamentals veto or merely not support (7b)? Is
  short interest / sentiment positioning crowded enough to gate sizing (7c)?
  Can the bull case (Sep call accumulation, DB $98 PT, World Cup/SpaceX
  catalysts) survive the 8b debate?
