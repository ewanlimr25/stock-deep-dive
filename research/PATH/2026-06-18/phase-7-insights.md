# Phase 7 — UW Insights Confluence

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:17:38Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-5-historical.md

## Summary

UW's composite engine reads PATH as **MIXED / low-confidence — no confluence setup in
either direction.** PATH is **absent from both the bullish and bearish signal-confluence
lists** (score < 1), the conviction-matrix returns **MIXED at just 7.9% confidence**, and
institutional-accumulation is **NEUTRAL**. The only directional flag is `price-vs-flow`
**DIVERGENCE** — bullish flow against a −6.0% price move — but the net flow driving it is a
trivial **+$17,799**, so it is a weak, early reversal hint, not a signal. This **agrees**
with the upstream chain: phase-0.5 BUSY_NAME_NORMAL_DAY, phase-1 mild-bullish-but-capped,
phase-2 balanced dark pool, phase-5 edge-weak/counter-trend. Treat MIXED as the baseline.

## Key signals

- **No confluence rank:** PATH absent from signal-confluence bullish AND bearish (min-score
  1, top-20) — composite score < 1 [INSIGHT:signal_confluence].
- **Conviction matrix MIXED, 7.9% confidence:** "Balanced dark pool — no clear bias" [INSIGHT:conviction_matrix].
- **Institutional accumulation NEUTRAL:** buy_sell_ratio 1.37, "balanced" [INSIGHT:institutional_accumulation].
- **Price-vs-flow DIVERGENCE:** price −6.04% vs bullish flow (net +$17,799) — weak/early reversal hint [INSIGHT:price_vs_flow].
- **Whole-tape aggregate (reconciles phase-1):** bullish $1,002,311 vs bearish $984,512
  (net **+$17,799**), call $1.873M / put $0.670M, P/C 0.335, iv_rank 34.55, implied_move 2.06% [INSIGHT:deep_dive].

## Detailed findings

### Deep-dive snapshot — `[INSIGHT:deep_dive]`

- `uw_screener`: bullish_premium $1,002,311 · bearish_premium $984,512 · **derived net_flow
  +$17,799** · call_premium $1,872,959 · put_premium $669,968 · put_call_ratio 0.335 ·
  call_volume 27,552 · put_volume 9,225 · **implied_move_perc 2.06%** · iv_rank 34.55 ·
  total_open_interest 778,391 · next_earnings_date 2026-09-03.
- Reconciles with phase-1's aggregate and phase-0.5's `[CTX:]` (universe pctile 89 total
  prem / 80 net-dir; self-pctile 33 total → busy-name-normal-day). Earnings far out (phase-6).

### Signal confluence — `[INSIGHT:signal_confluence]`

**PATH not in the bullish OR bearish top-20 at min-score 1** → composite confluence score
**< 1** in both directions. (For scale, the top bullish name SWBI scored **6/6**:
bullish_flow + low_pcr + volume_spike + dp_accumulation + oi_building + low_iv_cheap_options
— PATH fires none of these strongly enough to rank.) UW sees no stacked edge here.

### Conviction matrix — `[INSIGHT:conviction_matrix]`

scenario **MIXED**, confidence **7.9%**. dark_pool buy_ratio 0.579 (buy 795,128 / sell
578,611, 68 trades); options_flow call_ask 14,337 > call_bid 9,066 (call buying), put_ask
3,671 < put_bid 4,369 (mild put selling). explanation: "Balanced dark pool activity — no
clear bias." thresholds bull 0.6 / bear 0.4 — buy_ratio 0.579 sits **just below** the bull line.

### Price vs flow — `[INSIGHT:price_vs_flow]`

**divergence: true** — "Price is down 6.0% but options flow is bullish (net flow $17,799)."
period_high 13.2 / period_low 9.2 (30d). Classic bullish-flow-vs-falling-price divergence: a
*leading* reversal signal but often early, and here driven by a tiny net flow. Per the
heuristic, pair with phase-4 (near-spot **short gamma** → a $10 break could go the other way)
before sizing — the divergence is **not** a clean long trigger.

### Analyst vs flow — `[INSIGHT:analyst_vs_flow]`

Returned options_flow only (flow_sentiment bullish, net_flow +17,799); **no analyst-consensus
block populated** (yfinance analyst data absent for PATH at this read). Wall-Street-vs-trader
agreement **cannot be assessed here** — defer to phase-7b (`fz` analyst cross-source).

### Institutional accumulation — `[INSIGHT:institutional_accumulation]`

signal **NEUTRAL — balanced dark pool activity.** buy_sell_ratio 1.37 (buy 795,128 / sell
578,611), vwap $10.24, total_dp_premium $14.07M / volume 1,373,739, price_30d −6.04%.
top_price_levels: $10.27 ($3.9M, closing cross) and $10.24 ($2.68M, the 262k block).

### Earnings play

**Skipped** — next earnings ~2026-09-08 (phase-6), outside the 30-day window.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|---------------------|------|
| `insights deep-dive --symbol PATH --date 2026-06-18` | net_flow +$17,799; iv_rank 34.55; impl_move 2.06% ← `.uw_screener` | 1 |
| `insights signal-confluence --direction bullish --min-score 1 --top-n 20` | PATH absent ← `.results[].ticker` | 20 |
| `insights signal-confluence --direction bearish --min-score 1 --top-n 20` | PATH absent | 20 |
| `insights conviction-matrix --symbol PATH --date 2026-06-18` | MIXED, 7.9% ← `.scenario/.confidence_pct` | 1 |
| `insights price-vs-flow --symbol PATH --lookback-days 30` | divergence true ← `.divergence/.divergence_signal` | 1 |
| `insights analyst-vs-flow --symbol PATH` | flow bullish; no analyst block ← `.options_flow` | 1 |
| `insights institutional-accumulation --symbol PATH` | NEUTRAL, ratio 1.37 ← `.signal/.buy_sell_ratio` | 1 |

## Tool errors

_none._ `analyst-vs-flow` returned no analyst-consensus block (not an error — yfinance data
absent); deferred to phase-7b. Earnings-play intentionally skipped (out of window).

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (PATH unranked) | **agrees** ph-0.5 / ph-1 / ph-5 | No stacked edge — matches BUSY_NAME_NORMAL_DAY + capped flow + edge-weak backtest |
| conviction_matrix MIXED | **agrees** ph-2 | Balanced DP; matches phase-2 balanced-to-slight-distribution |
| institutional_accumulation NEUTRAL | **reconciles** ph-2 | Phase-2 large-tier was 0.48 (ex-block); phase-7 aggregate buy_ratio 0.579 (incl 262k block + closing crosses) → **net NEUTRAL**. Both = no real accumulation |
| price_vs_flow DIVERGENCE | **agrees** ph-5 | Counter-trend bullish flow (price −6%); early/weak reversal hint, tiny net flow |

## Verdict for downstream

- **UW composite bias:** **MIXED / NEUTRAL** (weak bullish-flow tilt fully offset by neutral
  dark pool, no confluence rank, and a price/flow divergence on trivial net flow).
- **Conviction:** **2/5.**
- **Baseline for phase-9:** Start from **MIXED, low-conviction**. Phase-9 should only deviate
  toward a directional long on *specific* contrary strength — and the strongest such item
  (the 5-session bullish sweep persistence + 10-day OI build, phases 1/5) is **slow and
  counter-trend**, not a confluence trigger. The DP buy_ratio 0.579 sits just under the 0.6
  bull threshold — a hair short of even a mild bull call.
- **Open questions:** Does the fundamentals veto (7b) or the short-interest gate (7c) tip the
  MIXED baseline? The price/flow divergence + near-spot short gamma means the asymmetric risk
  is a **break of $10**, not the upside — the debate (8b) must weigh squeeze-fuel (31.78% SI)
  against the hawkish-macro / downtrend bear case.
