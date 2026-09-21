# Phase 7 — UW Insights Confluence

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md

## Summary

UW's composite tooling reaches the **same verdict the manual phases did: MIXED, no
clean directional edge, low conviction.** Conviction-matrix returns **MIXED at 8.8%
confidence**; SHOP appears in **neither** the bullish nor bearish signal-confluence
list (score < 1 both ways); institutional-accumulation is **NEUTRAL** (mild sell-lean,
buy/sell 0.70); analyst-vs-flow is unavailable; and SHOP is **not** flagged as an
earnings-play setup despite earnings in 19 days. **The single directional flag is
`price-vs-flow`: a confirmed DIVERGENCE** — price rose **+6.5%** over 30 days while
options flow is **bearish** (net −$1.08M). In the phase-4 short-gamma regime with
max-pain below spot, that divergence is the internal-consistency case for a **tactical
near-term fade lower** — but it is low-confidence and, per its own heuristic, "often
early." Phase-9 baseline: **no directional confluence; a small, defined-risk fade is
the only edge the instrumentation supports.**

## Key signals

- **Conviction matrix = MIXED, confidence 8.8%** — "Balanced dark pool activity — no
  clear bias." `[INSIGHT:conviction_matrix]`
- **Signal-confluence: SHOP absent both directions** (min-score 1, top-60) → score <1. `[INSIGHT:signal_confluence]`
- **price-vs-flow DIVERGENCE**: "Price up 6.5% but options flow bearish (−$1.08M)". `[INSIGHT:price_vs_flow]`
- **institutional-accumulation NEUTRAL**, buy/sell 0.70 (mild sell-lean), DP prem $59.1M,
  vwap 123.21. `[INSIGHT:institutional_accumulation]`
- **Not an earnings-play setup** (no IV+OI-buildup ramp) despite Aug-5 earnings. `[INSIGHT:earnings_play]`

## Detailed findings

### Deep-dive snapshot (whole-tape aggregates) `[INSIGHT:deep_dive]`

From the `uw_screener` block (reconciled with phase-1): call_premium **$11.09M** vs
put_premium **$6.35M**; bullish_premium **$7.28M** vs bearish_premium **$8.36M** →
**net_flow −$1.08M** (derived); P/C **0.9185**; iv_rank **85.6**; total_open_interest
**844,569**; next_earnings **2026-08-05**. Yahoo fundamentals returned **null** (mcap /
PE / 52w unavailable from this endpoint) — valuation sourced from fz in phase-6 (mcap
$160.3B, ~13× sales). The `implied_move_perc` (0.49%) remains **unreliable** (phase-4).

### Signal confluence `[INSIGHT:signal_confluence]`

SHOP is **not** in the bearish list nor the bullish list at min-score 1 (top-60 each) →
composite factor score **< 1 in both directions**. No multi-factor directional stack.

### Conviction matrix `[INSIGHT:conviction_matrix]`

`scenario = MIXED`, `confidence_pct = 8.8`. options_flow: call_ask 13,155 / call_bid
12,008 (calls ~balanced); **put_ask 7,773 / put_bid 19,561 → puts net SOLD** (bid
volume 2.5× ask). dark_pool buy_ratio 0.412 (sell-lean). explanation: "Balanced dark
pool activity — no clear bias." Note the **put-selling** aggregate tempers the bearish
read — it corroborates phase-1's $116 put-write / support-defining behaviour.

### Price vs flow `[INSIGHT:price_vs_flow]`

`divergence = true`: *"Price is up 6.5% but options flow is bearish (net flow
−$1,080,438)."* price_start 116.04 → price_end 123.56 (+6.48%), flow_direction
**bearish**, iv_rank 85.6. **Leading reversal signal, lower** — the phase-9 directional
tie-breaker, but early; only actionable because phase-4 (short gamma, max-pain below)
provides the mechanism.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

Returned only `{options_flow, symbol}` — **no analyst consensus / target** (yfinance
analyst data unavailable for SHOP on this call). Cannot assess Street-vs-flow
agreement; phase-7c/7b will source analyst view from Finnhub/fz instead.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

`signal = NEUTRAL — balanced dark pool activity`, buy_sell_ratio 0.70, buy_side 197,474
/ sell_side 282,400, total_dp_premium $59.1M, vwap 123.21, price_30d +6.48%. Mild
sell-lean, tool labels NEUTRAL → **agrees with phase-2** (mild distribution, de-rated).

### Earnings play `[INSIGHT:earnings_play]`

SHOP **not** flagged in the ≤30-day earnings-play scan → no distinctive pre-earnings
IV/OI-buildup signature yet (19 days out; IV elevated broadly, not earnings-specific).

## Tool calls (audit trail)

| Command | Key value ← `jq` path | Rows |
|---|---|---|
| `uw insights conviction-matrix --symbol SHOP --date 2026-07-17` | MIXED, 8.8% ← `.scenario,.confidence_pct` | 1 |
| `uw insights signal-confluence --direction bearish\|bullish --min-score 1 --top-n 60` | SHOP absent ← `select(.ticker=="SHOP")`=∅ | 60 ea |
| `uw insights price-vs-flow --symbol SHOP --lookback-days 30` | divergence true, bearish ← `.divergence,.divergence_signal` | 1 |
| `uw insights institutional-accumulation --symbol SHOP` | NEUTRAL, 0.70 ← `.signal,.buy_sell_ratio` | 1 |
| `uw insights analyst-vs-flow --symbol SHOP` | no consensus ← keys={options_flow,symbol} | 1 |
| `uw insights earnings-play --days-until-earnings 30` | SHOP absent | scan |

## Tool errors

<none as hard errors> — `analyst-vs-flow` returned without analyst fields (yfinance
gap), treated as "unavailable," not an error.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|---|---|---|
| signal_confluence (absent both) | **agrees** phases 1–3 | Mixed/low — no directional stack, matches two-sided flow |
| conviction_matrix (MIXED 8.8%) | **agrees** phase 1 | Put-selling aggregate corroborates phase-1 $116 write |
| institutional_accumulation (NEUTRAL, 0.70) | **agrees** phase 2 | Mild distribution, de-rated — same read |
| price_vs_flow (DIVERGENCE bearish) | **agrees** phases 4–5 | Short-gamma + max-pain-below + bearish_flow backtest = fade-lower thesis |

No contradictions — the composite is internally consistent with the manual phases.

## Verdict for downstream phases

- **UW composite bias:** MIXED with a **mild near-term bearish/reversal lean** (sole
  directional signal = price-vs-flow divergence).
- **Conviction:** 2/5.
- **Phase-9 baseline:** treat as **no clean directional edge**. The only actionable
  thesis the instrumentation supports is a **small, defined-risk tactical fade lower**
  (price-vs-flow divergence + short gamma + max-pain 117–121), explicitly *not* a
  high-conviction position. Override only with specific contrary evidence from 7b/7c/8.
- **Open questions:** Does fundamentals (7b) veto or support the medium-term bullish
  base? Does sentiment/positioning (7c) show crowding a fade could squeeze, or short
  interest that caps downside? Does the desk debate (8/8b) find the divergence is
  distribution or just hedged-long protection?
