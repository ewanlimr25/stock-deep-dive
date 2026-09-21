# Phase 7 — UW Insights Confluence

**Ticker:** IREN
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T01:36Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite engine reads IREN as **MIXED with a bearish-flow tilt and very
low machine confidence**: conviction-matrix scenario "MIXED" at
**confidence_pct 4.4** (DP balanced at buy_ratio 0.544; options tape bearish
on both legs — calls hit at bid 137,134 vs 90,733 ask, puts lifted at ask
139,432 vs 84,737 bid) [INSIGHT:conviction_matrix]. IREN does **not** make the
market-wide signal-confluence list in EITHER direction at score ≥3 (lists
exhausted to n=300) [INSIGHT:signal_confluence], and institutional
accumulation is "NEUTRAL — balanced dark pool activity" (buy/sell 1.19)
[INSIGHT:institutional_accumulation]. The one directional flag is
**price-vs-flow divergence: TRUE** — verbatim "Price is up 7.3% but options
flow is bearish (net flow: $-18832787)" over the 30d lookback
[INSIGHT:price_vs_flow] — a bearish-reversal-class signal, though the −18.4%
crash from the 70.71 period high means much of that "reversal" has already
printed. This is consistent with phases 1–3: a real bearish tape today, but
two-sided structure underneath — not a clean directional stack.

## Key signals

- **Conviction matrix: MIXED, confidence 4.4%** — thresholds bull 0.6 / bear
  0.4 vs DP buy_ratio 0.544; explanation verbatim: "Balanced dark pool
  activity — no clear bias." [INSIGHT:conviction_matrix]
- **Signal confluence: IREN absent both directions** at min-score 1, top-n 300
  (min score appearing in lists = 3 → IREN scores ≤2 each way). Day's top
  confluence names: TLRY/VXX/BITX (bullish, 6), MTUM/IRDM (bearish, 6) —
  note VXX and BITX (2× BTC ETF) scoring 6 bullish echoes the
  vol-up/crypto-bounce tape [INSIGHT:signal_confluence].
- **Price-vs-flow divergence TRUE (bearish)**: 30d price +7.33% (50.64 →
  54.35; period high 70.71 / low 42.21) vs net flow −$18.83M
  [INSIGHT:price_vs_flow].
- **Institutional accumulation NEUTRAL**: buy 4,862,398 vs sell 4,082,228
  (ratio 1.19), VWAP 54.59, total DP $488.27M / 8.94M sh — matches phase-2's
  stratified totals exactly [INSIGHT:institutional_accumulation].
- **Options-flow leg detail (conviction matrix)**: call_bid > call_ask by
  46,401 contracts (selling) AND put_ask > put_bid by 54,695 (buying) — the
  same two-legged bearish signature phase-1's §A cut found ex-0DTE
  [INSIGHT:conviction_matrix].

## Detailed findings

### Deep dive snapshot [INSIGHT:deep_dive]

- `uw_screener` directional aggregates (re-stated; jq `.uw_screener`):
  bullish_premium **$72,372,345** vs bearish_premium **$91,205,132** →
  **derived net_flow = −$18,832,787** (deep-dive has no `net_flow` key);
  call_premium $124,223,791 vs put_premium $70,031,179; P/C 0.91;
  implied_move 0.5229 / implied_move_perc 0.963% (flagged in phase-6 as
  inconsistent with 130% front IV — phase-9 N4 must size off IV instead);
  iv_rank 48.17; total OI 2,459,547; next earnings 2026-08-27.
  Reconciles 1:1 with phase-1's whole-tape block and phase-0.5's #28-bearish
  rank.
- `uw_dark_pool`: $488,273,934.72 premium / 8,944,626 shares / 2,097 trades /
  avg 54.447 — identical to phase-2 stratified totals.
- `uw_top_oi_changes`: 50P 06/12 +29,735; 71C 0DTE +14,537; 55P +8,285; 30P
  +7,505; 64C +7,051 — identical to phase-3's table.
- `yahoo_fundamentals`: **ERROR** (see Tool errors) — no PE/cap/short% from
  this tool; phase-7b covers fundamentals via Finnhub/fz.

### Signal confluence [INSIGHT:signal_confluence]

Absent from bullish AND bearish lists (n=300 each, all listed names score
≥3). Verdict: UW's factor-stack sees **≤2 of 6 factors** aligned for IREN in
either direction — no confluence trade per the engine.

### Conviction matrix [INSIGHT:conviction_matrix]

scenario **MIXED**, confidence_pct **4.4**. Components: dark_pool buy_ratio
0.544 (buy 4,862,398 / sell 4,082,228, 2,097 trades — between bear 0.4 and
bull 0.6 thresholds); options_flow: call ask/bid 90,733/137,134, put ask/bid
139,432/84,737.

### Price vs flow [INSIGHT:price_vs_flow]

divergence **true**; signal verbatim: "DIVERGENCE: Price is up 7.3% but
options flow is bearish (net flow: $-18832787)". price_start 50.64 →
price_end 54.35 (+7.33%), period_high 70.71, period_low 42.21, flow_direction
"bearish". Nuance: the 30d endpoints mask the path — the stock is −23% off
the period high; the "divergence" partially resolved itself this week.
Heuristic check (pair with phase-4 dealer regime): short-gamma regime +
bearish divergence = downside follow-through risk remains live.

### Analyst vs flow [INSIGHT:analyst_vs_flow]

Returned **options_flow only** (sentiment "bearish", net_flow −18,832,787,
P/C 0.91) — **no analyst consensus block** in the payload (yfinance leg
failed alongside the Yahoo 401). Partial result; Wall-Street-vs-flow
comparison deferred to phase-7b/7c (Finnhub/WebSearch analyst data).

### Institutional accumulation [INSIGHT:institutional_accumulation]

signal verbatim: **"NEUTRAL — balanced dark pool activity"**; buy_sell_ratio
1.19; VWAP 54.59 vs avg_trade_price 54.45; today's top DP levels: 54.35
($9.58M/176,204sh), 56.25 ($6.20M), 54.25 ($5.94M), 54.00 ($5.20M), 54.21
($4.87M) — a dense 54.0–54.35 shelf formed TODAY (complements phase-2's
5-day map where sub-60 was previously uncharted).

### Earnings play

Skipped — next earnings 2026-08-27 (83 days; outside the 30d window per
phase-6 calendar).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol IREN --date 2026-06-05 --json` | net_flow derived −18,832,787 ← `.uw_screener.bullish_premium − .bearish_premium`; DP $488,273,934.72 ← `.uw_dark_pool.total_premium` | whole-tape |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 300 --date 2026-06-05 --json` | IREN absent; list-min score=3 ← `[.results[].score]\|min` | 300 ×2 |
| `uw insights conviction-matrix --symbol IREN --date 2026-06-05 --json` | scenario="MIXED", confidence_pct=4.4 ← top-level | 1 |
| `uw insights price-vs-flow --symbol IREN --lookback-days 30 --json` | divergence=true, price_change_pct=7.33 ← top-level | 30d |
| `uw insights analyst-vs-flow --symbol IREN --json` | options_flow only; no analyst block ← payload keys | partial |
| `uw insights institutional-accumulation --symbol IREN --json` | signal="NEUTRAL…", buy_sell_ratio=1.19 ← top-level | today |

## Tool errors

- `uw insights deep-dive --symbol IREN --date 2026-06-05 --json` →
  `yahoo_fundamentals: {"error":"yahoo quoteSummary IREN: HTTP 401"}` —
  fundamentals leg failed (Yahoo auth); options/DP/OI legs returned clean.
  Phase-7b supplies fundamentals via Finnhub/fz instead.
- `uw insights analyst-vs-flow` returned no analyst consensus block (same
  Yahoo dependency) — recorded as partial, not fabricated.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence ≤2/6 both ways | **Agrees** with phases 1–3 | Real bearish tape but two-sided structure → no clean stack; matches phase-1 conviction 3/5, phase-2's 2/5 |
| conviction_matrix MIXED (4.4%) | **Agrees** with phase-2 | DP 0.544 ≈ phase-2's block 0.588/large 0.535; bearish options legs ≈ phase-1 §A |
| institutional_accumulation NEUTRAL | **Agrees** with phase-2 | Identical volumes (4.86M/4.08M); phase-2's "mild buy lean" = ratio 1.19, below conviction bar |
| price_vs_flow DIVERGENCE (bearish) | **Agrees-with-nuance** with phases 0.5/1 | Flow extreme bearish (self-pctile 0.0) while 30d price +7.3%; but −23% off high means partial resolution already |
| (no analyst leg) | n/a | Deferred to 7b/7c |

No upstream phase is contradicted by the composite — the run is internally
consistent: **today was a genuinely bearish, macro-driven tape (phase-6) on a
structurally two-sided name (phases 1–3) in a short-gamma pocket (phase-4).**

## Verdict for downstream phases

- **UW composite bias:** MIXED / bearish-tilt, machine confidence 4.4% —
  treat as **no-edge baseline from the composite engine**.
- **Conviction:** 2/5.
- **Phase-9 instruction:** treat MIXED-low-confidence as the BASELINE; any
  directional trade must be justified by specific upstream evidence (the
  short-gamma map, the put-ladder mechanics, the macro catalysts) and priced
  as a tactical, defined-risk structure — NOT as a high-conviction
  directional. Override bar: phases 8/8b would need a unanimous, specific
  case.
- **Open questions:** Does the fundamentals gate (7b) veto or pass? Is the
  15.71% short float (phase-0) a squeeze accelerant on any bounce (7c)? Do
  the analyst desks (8) find an angle the composite can't see?
