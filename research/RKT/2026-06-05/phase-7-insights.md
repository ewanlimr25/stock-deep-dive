# Phase 7 — UW Insights Confluence

**Ticker:** RKT
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T17:55:00-04:00
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite layer classifies RKT's day as **COVERED_CALL** ("Dark pool buying
+ call selling — yield enhancement, capping upside", confidence 43.6%) with
**no price-vs-flow divergence** ("Price and flow are aligned": bearish flow,
price −18.91% over 30d) and flow_sentiment **bearish** (net −$209,751). The
`institutional-accumulation` tool prints **ACCUMULATION (buy/sell 5.3)** — but
that ratio counts the 06-05 16:00:28 closing cross (5.82M sh = 87% of the
"buy" volume) at face value, which phase-2's tier-stratified read already
de-rated; ex-cross the DP tape leans distribution. RKT appears on **neither**
the bullish nor bearish market-wide signal-confluence top-20. Net composite:
**neutral-to-bearish with capped upside** — agreeing with phases 1/2/5, and
with phase-3's covered-call open question now answered in the affirmative by
the scenario classifier.

## Key signals

- `scenario: "COVERED_CALL"`, `confidence_pct` 43.6, explanation verbatim:
  *"Dark pool buying + call selling — yield enhancement, capping upside."*
  options_flow block: call_bid_volume 16,969 > call_ask_volume 11,550 (calls
  sold); put_ask_volume 8,141 > put_bid_volume 4,850 (puts bought)
  [INSIGHT:conviction_matrix]
- `divergence: false` — *"Price and flow are aligned"*; flow_direction
  "bearish"; price_start 15.60 → price_end 12.65 (**−18.91%** over the
  30d lookback; period_low 12.38 = the 52w low phase-5 flagged)
  [INSIGHT:price_vs_flow]
- `signal: "ACCUMULATION — dark pool buy volume significantly exceeds sell
  volume"`, buy_sell_ratio **5.3** (6,726,882 vs 1,268,948), vwap 12.68 —
  **artifact-inflated by the 4pm cross** (see cross-check)
  [INSIGHT:institutional_accumulation]
- RKT **absent from both** signal-confluence top-20 boards (bullish and
  bearish, `--min-score 1`) — no high-confluence stack either way
  [INSIGHT:signal_confluence]
- `flow_sentiment: "bearish"`, net_flow −209,751 (derived bullish −
  bearish premium consistent with phase-1); **analyst consensus block absent**
  from analyst-vs-flow output (yfinance returned nothing)
  [INSIGHT:analyst_vs_flow]

## Detailed findings

### Deep dive snapshot

- `yahoo_fundamentals`: **errored** — `{"error":"yahoo quoteSummary RKT: HTTP
  401"}` (rate-limit/auth; fundamentals deferred to phase-7b Finnhub).
- `uw_dark_pool`: total_premium $101,376,628.58, total_shares 7,995,830,
  trade_count 80, avg_price 12.7585 — matches phase-2 exactly.
- `uw_top_oi_changes` top 5: Sep-18 13C +2,971, Jun-12 14C +1,170, 0DTE 14C
  +586, Jun-18 17C +394, Sep-18 12P +351 — matches phase-3.
- `uw_screener` directional aggregates (whole-tape; quoted in phase-0.5/1):
  bullish_premium 1,256,315 vs bearish_premium 1,466,066 → **derived net_flow
  −$209,751** (no `net_flow` key in this block); call_premium 1,912,369 vs
  put_premium 1,332,438; P/C 0.46; iv_rank 29.9622; implied_move 0.1514 /
  implied_move_perc 0.011984 (phase-9 N4 sizes to this). Reconciles with
  phase-1's aggregate and phase-0.5's BUSY_NAME_NORMAL_DAY rank.

### Signal confluence (market-wide, --min-score 1, top-20)

Bullish board: TLRY, VXX, BITX, ZSL, KREF, … (no RKT). Bearish board: MTUM,
IRDM, NASA, BLD, EWY, SMH, … (no RKT). RKT's confluence score is below the
top-20 cut in both directions — consistent with phase-0.5 (outside top-50 on
every leadership screen) and the mixed phase-1 tape.

### Conviction matrix

scenario **COVERED_CALL**, confidence_pct **43.6** (thresholds bear 0.4 / bull
0.6 — i.e. mid-band, weak-bear side). Inputs the tool used: dark_pool buy_ratio
0.841 (80 trades; includes the cross), call selling dominance on the bid, put
buying on the ask. This is the same signature phase-1's DuckDB cut found
(calls net-sold 12,773 bid vs 8,042 ask ex-0DTE) and answers phase-3's open
question: the day's flow signature is **yield-enhancement against stock, not
directional accumulation** — upside capped.

### Price vs flow

`divergence: false` — bearish flow + falling price = trend confirmation, not a
reversal setup. 30d: 15.60 → 12.65 (−18.91%), period range 12.38–15.94. No
contrarian divergence credit available for a long thesis.

### Analyst vs flow

Output contained only the options_flow block (flow_sentiment "bearish",
net_flow −209,751, P/C 0.46) — **no analyst consensus returned** (yfinance
gap, mirrors the Yahoo 401). Wall-Street-vs-flow agreement is unverifiable
from this tool today; phase-7b/7c pull analyst data from Finnhub/fz instead.

### Institutional accumulation

`signal` verbatim: "ACCUMULATION — dark pool buy volume significantly exceeds
sell volume"; buy 6,726,882 / sell 1,268,948 (ratio 5.3), 80 trades, total DP
volume 7,995,830, vwap 12.68, avg_trade_price 12.76, price_30d −18.91%.
top_price_levels[0] = $12.65 / 6,400,475 sh / $80,966,008.75 / 8 trades — i.e.
the closing-cross shelf. **Caveat (decisive):** 5,821,043 of the 6,726,882
buy-classified shares (86.5%) are the single 16:00:28 closing cross phase-2
de-rated as benchmark-flow-like; ex-cross, buy ≈ 906k vs sell ≈ 1.27M →
**ratio ≈ 0.71, distribution-leaning**, matching phase-2's block-tier
sell_ratio 0.883. The composite's headline is mechanically true and
analytically misleading.

### Earnings play

Skipped — next earnings 2026-07-30 (phase-0.5 `.uw_screener`), 55 days out,
beyond the 30d window.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol RKT --date 2026-06-05 --json` | blocks ← `.uw_screener` / `.uw_dark_pool` / `.uw_top_oi_changes[:5]` / `.yahoo_fundamentals` | whole-tape |
| `uw insights signal-confluence --direction bullish/bearish --min-score 1 --top-n 20 --date 2026-06-05 --json` | no RKT ← `.results[].ticker` | top-20 ×2 |
| `uw insights conviction-matrix --symbol RKT --date 2026-06-05 --json` | COVERED_CALL ← `.scenario`; 43.6 ← `.confidence_pct` | 1 |
| `uw insights price-vs-flow --symbol RKT --lookback-days 30 --json` | false ← `.divergence`; −18.91 ← `.price_change_pct` | 30d |
| `uw insights analyst-vs-flow --symbol RKT --json` | bearish ← `.options_flow.flow_sentiment`; analyst block absent | 1 |
| `uw insights institutional-accumulation --symbol RKT --json` | 5.3 ← `.buy_sell_ratio`; `.signal` verbatim | 80 trades |
| `uw insights earnings-play` | skipped — earnings 55d out (>30d window) | — |

## Tool errors

- `uw insights deep-dive` → `yahoo_fundamentals: {"error":"yahoo quoteSummary
  RKT: HTTP 401"}` (Yahoo auth/rate-limit; non-fatal — fundamentals deferred to
  phase-7b).
- `uw insights analyst-vs-flow` returned no analyst-consensus block (yfinance
  gap) — agreement read unavailable, noted in body.

## DATA NOTE / CORRECTION

None — first reads stood (deep-dive block keys discovered via `keys` probe
before extraction; nothing transcribed from a failed path).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent both boards) | **agrees** w/ phase-0.5/1 | BUSY_NAME_NORMAL_DAY; no high-confluence stack |
| conviction_matrix COVERED_CALL | **agrees** w/ phase-1 (calls net-sold ex-0DTE) + phase-3 (call-wall staircase; answers its covered-call question) + phase-4 (capped upside at 14.5) | confidence 43.6% = weak-bear mid-band |
| price_vs_flow aligned (no divergence) | **agrees** w/ phase-5 (19/30 bearish days, downtrend intact) | no reversal credit |
| analyst_vs_flow (flow bearish) | **agrees** w/ phase-1 net −$209,751 | analyst side missing — gap, not conflict |
| institutional_accumulation ACCUMULATION 5.3 | **DISAGREES** w/ phase-2 (mixed-leaning-distribution) | composite counts the 4pm cross as a buy; phase-2's stratified read is the better-instrumented one — ex-cross ratio ≈0.71 sell-leaning. Override the composite here. |

## Verdict for downstream phases

- **UW composite bias:** neutral-to-bearish, **upside structurally capped**
  (COVERED_CALL); no divergence to fade; the lone bullish composite
  (ACCUMULATION) is artifact-driven and overridden by phase-2's stratified read.
- **Conviction:** 3/5
- **Phase 9 baseline:** treat "weak-bear / capped-upside, no high-confluence
  stack" as the baseline; override only with specific contrary evidence from
  phases 1–8 (per phase-7 rule). The ACCUMULATION print must NOT be cited as
  bullish evidence without the ex-cross caveat.
- **Open questions:** Do fundamentals (7b) veto or merely color the weak-bear
  baseline? Is short interest (7c) crowded enough to make squeezes the real
  tail risk for any short expression?
