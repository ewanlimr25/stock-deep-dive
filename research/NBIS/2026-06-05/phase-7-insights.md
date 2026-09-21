# Phase 7 — UW Insights Confluence

**Ticker:** NBIS
**As-of date:** 2026-06-05
**Generated:** 2026-06-06T21:20:00-0400
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

UW's composite engines return the same verdict the granular phases assembled:
**no clean confluence either way**. NBIS is absent from both the bearish and
bullish `signal-confluence` top-20 even at `--min-score 1`; the
`conviction-matrix` scenario is **MIXED** (DP buy_ratio 0.503 inside the
0.4/0.6 thresholds; "Balanced dark pool activity — no clear bias");
`institutional-accumulation` is **NEUTRAL** (buy/sell 1.01). The one sharp
composite signal is `price-vs-flow`: **DIVERGENCE — "Price is up 54.8% but
options flow is bearish (net flow: $-9,602,713)"** over the 30-session
lookback — a reversal warning that, as of Friday's −12.27% session (phase-6),
is no longer "early": it is actively resolving downward. Analyst consensus
leg of `analyst-vs-flow` returned no data (yfinance degraded; fundamentals
deferred to phase-7b), flow leg = bearish.

## Key signals

- `signal-confluence` (market-wide, min-score 1, top-20): **NBIS absent in
  BOTH directions** (bearish leaders MTUM/IRDM 6; bullish TLRY/VXX 6) — no
  factor stack ≥ cutoff `[INSIGHT:signal_confluence]`
- `conviction-matrix`: scenario **MIXED**, confidence_pct 0.3, DP buy_ratio
  0.503 (thresholds bear 0.4 / bull 0.6); options flow: call ask 56,981 vs call
  bid 70,702, put ask 57,348 vs put bid 61,208 — both net bid-side (selling)
  `[INSIGHT:conviction_matrix]`
- `price-vs-flow`: **divergence: true** — verbatim "DIVERGENCE: Price is up
  54.8% but options flow is bearish (net flow: $-9602713)"; price_start 147.16 →
  price_end 227.81; period_high 278.84 / low 132.70 `[INSIGHT:price_vs_flow]`
- `institutional-accumulation`: **"NEUTRAL — balanced dark pool activity"**,
  buy 1,780,340 vs sell 1,762,405 (ratio 1.01), VWAP 229.89, total DP premium
  $814,456,252 `[INSIGHT:institutional_accumulation]`
- Deep-dive `uw_top_oi_changes` = phase-3's exact put stack (205P +6,871 @ avg
  $3.30; 200P/202.5P/200P-Jun18 next) — cheap-OTM put accumulation, ~$2.3M on
  the lead line `[INSIGHT:deep_dive]`

## Detailed findings

### Deep dive snapshot `[INSIGHT:deep_dive]`

- `yahoo_fundamentals`: **all fields null** (market_cap, PE, short %, beta,
  sector — Yahoo leg returned nothing; see Tool errors). Fundamentals deferred
  to phase-7b (Finnhub/fz); fz phase-0 snapshot stands in: float 201.04M,
  short float 22.43%.
- `uw_screener` directional aggregates (whole-tape; reconciles with phase-1):
  bullish_premium **$195,086,472** vs bearish_premium **$204,689,185** →
  **derived net_flow = −$9,602,713** (no `net_flow` key in this block);
  call_premium $223,213,183 vs put_premium $236,887,376; P/C 0.97;
  call_volume 138,427 / put_volume 134,702; iv_rank 89.97;
  implied_move 0.927 / implied_move_perc 0.004068 (**suspect** — phase-0.5 DATA
  NOTE; phase-9 must size to IV-derived ranges instead); total OI 1,117,357;
  next earnings 2026-08-06. Matches phase-1's aggregate exactly; consistent
  with `[CTX:]` (99.6 pctile gross, 0.8 pctile net-direction).
- `uw_dark_pool`: $814.46M premium, 3,542,745 shares, 3,095 trades, avg price
  230.10 — identical to phase-2's all-tier read.

### Signal confluence `[INSIGHT:signal_confluence]`

Absent from bearish top-20 (leaders: MTUM 6, IRDM 6, NASA 5) and bullish
top-20 (TLRY 6, VXX 6, BITX 6) at min-score 1. The composite factor engine
does not see a stacked setup on NBIS today — consistent with the two-way
$460M tape phases 0.5/1 documented.

### Conviction matrix `[INSIGHT:conviction_matrix]`

Scenario **MIXED**; explanation verbatim: "Balanced dark pool activity — no
clear bias." DP buy_ratio 0.503 (1,780,340 buy / 1,762,405 sell, 3,095
trades). Options legs both net bid-side: calls 56,981 ask vs 70,702 bid; puts
57,348 ask vs 61,208 bid — premium-selling tape from both sides, mirroring
phase-1's DuckDB aggressor split (calls −$29.4M, puts −$38.5M net at-bid).

### Price vs flow `[INSIGHT:price_vs_flow]`

divergence **true**, flow_direction **bearish**, net_premium_flow −$9,602,713,
price_change_pct +54.8 (147.16 → 227.81 over the 30-session window),
period_high 278.84, period_low 132.70, iv_rank 89.97. Heuristic: bearish flow +
rising price = leading reversal signal, "often early — pair with phase-4 dealer
regime." Phase-4's regime is FULLY_NEGATIVE gamma — amplification — and the
reversal has begun (−12.27% Friday, −14% from the 06-01 high). The divergence
is *resolving*, not pending.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Returned only the flow leg: flow_sentiment **bearish**, net_flow −$9,602,713,
P/C 0.97. **No analyst consensus fields** (yfinance leg empty — same Yahoo
degradation as deep-dive). Agreement question deferred to phase-7b's
cross-source analyst pull.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

signal **"NEUTRAL — balanced dark pool activity"**; buy_sell_ratio 1.01;
price_30d_change_pct +54.8; VWAP 229.89 (spot closed 227.81 — fractionally
below institutional VWAP); top price levels 227.81 ($41.1M), 230 ($30.1M),
235 ($12.5M), 223.5/223.75 (~$10M each) — today's repricing shelf, matching
phase-2.

### Earnings play

Skipped — next earnings 2026-08-06 (61 days out; >30d window per phase-6
calendar).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol NBIS --date 2026-06-05 --json` | screener aggregates ← `.uw_screener.*`; DP ← `.uw_dark_pool.*`; OI ← `.uw_top_oi_changes[0:5]`; fundamentals null ← `.yahoo_fundamentals` | whole-tape |
| `uw insights signal-confluence --direction bearish --min-score 1 --top-n 20 --date 2026-06-05 --json` | NBIS absent ← ticker filter | top-20 |
| `uw insights signal-confluence --direction bullish --min-score 1 --top-n 20 --date 2026-06-05 --json` | NBIS absent ← ticker filter | top-20 |
| `uw insights conviction-matrix --symbol NBIS --date 2026-06-05 --json` | MIXED, 0.503, ask/bid splits ← `.scenario/.dark_pool.buy_ratio/.options_flow.*` | 1 |
| `uw insights price-vs-flow --symbol NBIS --lookback-days 30 --json` | divergence true; +54.8% vs −$9.6M ← `.divergence/.divergence_signal/.price_change_pct/.net_premium_flow` | 30-sess window |
| `uw insights analyst-vs-flow --symbol NBIS --json` | flow bearish; analyst leg empty ← `.options_flow.*` | 1 |
| `uw insights institutional-accumulation --symbol NBIS --json` | NEUTRAL 1.01 ← `.signal/.buy_sell_ratio` | 1 |

(`price-vs-flow`, `analyst-vs-flow`, `institutional-accumulation` take no
`--date`; they anchor to latest available = 2026-06-05 = as-of — correct for
this run, per the phase-5 latest-anchor caveat.)

## Tool errors

- `uw insights deep-dive` → `.yahoo_fundamentals` returned all-null fields
  (market_cap, PE, short %, beta, sector, name). Not a command failure — the
  Yahoo leg returned an empty object. Fundamentals deferred to phase-7b.
- `uw insights analyst-vs-flow` → returned `options_flow` block only; no
  analyst/consensus fields present in output. Same degradation; deferred to
  phase-7b/7c.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent both sides) | **agrees** w/ phases 0.5+1 | two-way tape, net only −$9.6M on $460M gross |
| conviction_matrix MIXED | **agrees** w/ phase 2 (all tiers 0.497–0.523) + phase 1 (delta-flat ex-0DTE) | both option legs net bid-side = premium selling |
| price_vs_flow DIVERGENCE (bearish) | **agrees** w/ phase 1 (5-session bearish sweep persistence) + phase 5 (16 bearish vs 14 bullish days while price doubled) | divergence now resolving via −12.27% Friday (phase-6) |
| institutional_accumulation NEUTRAL | **agrees** w/ phase 2 Mixed/balanced verdict | identical underlying numbers |
| deep_dive OI stack | **agrees** w/ phase 3 | same 205P/200P build rows |

No insight disagrees with any upstream phase — the run is internally
consistent.

## Verdict for downstream phases

- **UW composite bias:** **MIXED with a bearish tilt** — no confluence stack,
  balanced institutions, but the only directional composite signal
  (price-vs-flow divergence, bearish) points down and is actively resolving.
- **Conviction:** 2/5
- **Phase 9 baseline:** treat MIXED/bearish-tilt as the baseline; override only
  with specific contrary evidence from phases 1–8 (none of phases 1–5 is
  contrary — they all built this same picture independently).
- **Open questions:** Does the fundamental picture (phase-7b) justify the
  +54.8%/30d price that flow never confirmed? Is the 22.43% short float +
  inverted skew (phase-4) enough squeeze fuel to invalidate a short on any
  AI-capex good news (phase-7c gate)?
