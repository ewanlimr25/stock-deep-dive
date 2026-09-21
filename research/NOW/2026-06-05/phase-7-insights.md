# Phase 7 — UW Insights Confluence

**Ticker:** NOW
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T12:58:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's own composite instruments unanimously read the as-of day as
**no-edge**: conviction-matrix scenario **MIXED** (confidence 2.1%,
"Balanced dark pool activity — no clear bias"), institutional-accumulation
**NEUTRAL** (buy/sell 0.92), **no price-vs-flow divergence**, and NOW absent
from BOTH bullish and bearish signal-confluence top-20 even at
`--min-score 1`. This agrees with phases 0.5/1/2 (busy, two-way,
seller-dominated tape). The bearish lean elsewhere in this run lives in
exactly the dimensions these single-day composites don't measure: 5-session
sweep persistence (phase-1), the +6.09σ P/C extreme (phase-5), eroding GEX
(phases 4/5), and macro (phase-6). The Yahoo fundamentals leg errored
(HTTP 401) and the analyst block came back empty — fundamentals/analyst
coverage falls entirely to phase-7b.

## Key signals

- **Conviction matrix: MIXED, confidence 2.1%** — thresholds bull ≥0.60 /
  bear ≤0.40 vs DP buy_ratio 0.479; options block: call ask 43,721 vs call
  bid 62,286, put ask 31,574 vs put bid 55,191 [INSIGHT:conviction_matrix]
  — both wings net-bid (sold), corroborating phase-1
  [FLOW:aggressor_ex0dte DUCKDB].
- **Institutional accumulation: "NEUTRAL — balanced dark pool activity"**,
  buy_sell_ratio 0.92 (1,980,015 buy vs 2,153,609 sell), VWAP 114.47, total
  DP premium $473,177,699 [INSIGHT:institutional_accumulation] — matches
  phase-2 to the dollar.
- **No divergence**: "Price and flow are aligned", flow_direction bullish,
  net_premium_flow +$1,783,036, price +24.71% over the 30d window (90.17 →
  112.45; period high 139.20 / low 84.93) [INSIGHT:price_vs_flow] — no
  leading reversal signal from this lens.
- **Signal confluence: NOW absent both directions at min-score 1** (bullish
  top: TLRY/VXX/BITX score 6; bearish top: MTUM/IRDM/NASA)
  [INSIGHT:signal_confluence] — the day's factor stack simply isn't firing
  on NOW.
- **Analyst leg empty + Yahoo 401** [INSIGHT:analyst_vs_flow,
  INSIGHT:deep_dive] — no analyst-consensus cross-check available from UW;
  phase-7b must source it (fz/Finnhub/WebSearch).

## Detailed findings

### Deep dive snapshot

[INSIGHT:deep_dive] `uw_screener` directional aggregates (whole tape —
identical to the phase-0.5/phase-1 reads, reconciliation ✓):
bullish_premium **$62,496,824** vs bearish_premium **$60,713,788** → derived
**net_flow +$1,783,036** (no `net_flow` key in this block); call_premium
$74,064,700 vs put_premium $77,595,932; call_volume 126,878 / put_volume
101,468; P/C **0.80**; iv_rank **79.23**; iv30d 0.6693; total OI 1,603,623;
`implied_move` 0.4264 / `implied_move_perc` 0.38% (unit suspect — phase-0.5
DATA NOTE; `volatility` 4.39 is the plausible daily %); next_earnings_date
2026-07-22. `uw_dark_pool`: $473,177,699 premium / 4,133,624 shares / 2,014
trades / avg 114.39 (= phase-2 ✓). `uw_top_oi_changes` head: 125C 6/5
+1,853, 119P 6/5 +1,372, 135C 6/18 +1,248, 175C 6/12 +1,157, 123C 6/5
+1,128 (= phase-3 ✓). `yahoo_fundamentals`: **error** (see Tool errors) —
no P/E, market cap, or short % from this tool.

### Signal confluence

[INSIGHT:signal_confluence --min-score 1 --top-n 20, both directions] NOW
in neither list → score < 1 or outside top-20 on both stacks. Day leaders
for context: bullish TLRY/VXX/BITX (6), bearish MTUM/IRDM (6). Confluence
≥5 is the "rare, high-conviction" bar — NOW is nowhere near it on either
side.

### Conviction matrix

[INSIGHT:conviction_matrix] scenario **MIXED**, confidence_pct **2.1**,
explanation verbatim: "Balanced dark pool activity — no clear bias."
dark_pool.buy_ratio 0.479 (buy 1,980,015 / sell 2,153,609 / 2,014 trades).
options_flow: call_ask 43,721 < call_bid 62,286; put_ask 31,574 < put_bid
55,191 — net premium *supply* on both wings (the put-write/overwrite
signature phases 1/3 documented).

### Price vs flow

[INSIGHT:price_vs_flow --lookback-days 30] divergence **false** —
"Price and flow are aligned"; flow_direction "bullish"; net_premium_flow
+1,783,036; price_start 90.17 → price_end 112.45 (+24.71%); period_high
139.20, period_low 84.93. Nuance for phase-9: the 30d lens nets the +33%
melt-up and the −17% fade into "aligned" — phase-5's daily table shows flow
chased *both* legs (−$17M bearish on 6/2 and 6/3); this tool's alignment is
real but coarse.

### Analyst vs flow

[INSIGHT:analyst_vs_flow] Returned options_flow block only
(flow_sentiment "bullish", net_flow +1,783,036, pcr 0.8) — **analyst
consensus block absent** (yfinance source; consistent with the Yahoo 401).
No Wall-Street-vs-flow agreement check possible from UW today.

### Institutional accumulation

[INSIGHT:institutional_accumulation] signal **"NEUTRAL — balanced dark pool
activity"**; buy_sell_ratio **0.92**; total_dp_premium $473,177,699; vwap
114.47; price_30d_change_pct +24.71. Top price levels: 112.45 ($32.73M),
118.24 ($16.14M), 113.69 ($7.74M), 115.67 ($4.84M), 114.86 ($4.55M) —
the as-of-day ladder from phase-2, all between close and the morning high.

### Earnings play

Skipped — next_earnings_date 2026-07-22 is 47 days out, beyond the 30-day
window (phase-6 calendar).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol NOW --date 2026-06-05 --json` | DP $473,177,699 ← `.uw_dark_pool.total_premium`; OI head ← `.uw_top_oi_changes[0:5]`; yf error ← `.yahoo_fundamentals.error` | full object |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 20 --date 2026-06-05 --json` | NOW absent ← `select(.ticker=="NOW")` → [] | top-20 ×2 |
| `uw insights conviction-matrix --symbol NOW --date 2026-06-05 --json` | MIXED / 2.1% / buy_ratio 0.479 ← `.scenario, .confidence_pct, .dark_pool.buy_ratio` | 1 |
| `uw insights price-vs-flow --symbol NOW --lookback-days 30 --json` | divergence false / +24.71% ← `.divergence, .price_change_pct` | 30d window |
| `uw insights analyst-vs-flow --symbol NOW --json` | analyst block absent ← top-level keys | 1 |
| `uw insights institutional-accumulation --symbol NOW --json` | NEUTRAL / 0.92 ← `.signal, .buy_sell_ratio` | 1 |

## Tool errors

- `uw insights deep-dive --symbol NOW --date 2026-06-05 --json` →
  `.yahoo_fundamentals = {"error": "yahoo quoteSummary NOW: HTTP 401"}`
  (verbatim). Fundamentals snapshot unavailable from this tool; phase-7b
  covers via Finnhub/fz.
- `uw insights analyst-vs-flow` returned no analyst block (yfinance-sourced;
  empty/thin per `lib/uw-json-paths.md`) — recorded as data gap, not
  retried beyond the documented behavior.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent, both sides) | **agrees** with 0.5/1/2 | two-way tape, no factor stack firing |
| conviction_matrix MIXED 2.1% | **agrees** with 1/2/3 | both wings net-sold; DP 0.479 ≈ phase-2 tiers 0.461–0.477 |
| institutional_accumulation NEUTRAL 0.92 | **agrees** with 2 | same prints, same $473.2M |
| price_vs_flow no divergence | **agrees-with-nuance** vs 5 | 30d lens nets melt-up+fade; daily flow chased both legs |
| analyst_vs_flow (empty) | n/a | gap → phase-7b |
| (not measured by composites) | — | the run's bearish lean — sweep persistence 5/5 [FLOW:sweep_persistence], P/C z +6.09σ [HIST:pc_ratio_zscore], GEX erosion 47.8M→6.9M [HIST:gex_time_series], macro headwind [MACRO] — sits outside these tools' single-day scope |

## Verdict for downstream phases

- **UW composite bias:** NEUTRAL / MIXED (no-edge on single-day composite
  instrumentation)
- **Conviction:** 2 / 5
- **Phase-9 baseline:** treat **MIXED** as the baseline; any directional
  tilt must be justified by the specific contrary evidence the composites
  don't capture (persistence, positioning extremes, dealer structure decay,
  macro regime) — and sized accordingly small given phase-0.5's cap and
  phase-6's half-size guidance.
- **Open questions:** Does the fundamentals/quality picture (7b) or the
  short-interest/sentiment gate (7c) break the tie? Is the analyst street
  still anchored above the stock after the buyback (gap from the missing
  analyst block)?
