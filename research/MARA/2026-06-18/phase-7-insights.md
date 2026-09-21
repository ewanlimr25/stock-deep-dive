# Phase 7 — UW Insights Confluence

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-5-historical.md, phase-6-macro.md

## Summary

UW's composite tools **independently reproduce the upstream synthesis** — a strong
internal-consistency check. MARA appears in **neither** the bullish nor the bearish
`signal-confluence` list (no directional edge), the `conviction-matrix` reads
**MIXED** (confidence 6.8%, "balanced dark pool — no clear bias"), and
`institutional-accumulation` is **NEUTRAL** with buy_sell_ratio 1.32 (56.8% buy —
the same mild accumulation phase-2 found). The one standalone signal is a
**price-vs-flow DIVERGENCE** (price +12% over 30d while net flow is bearish −$1.6M) —
the textbook **call-overwrite-into-strength / buy-write signature**, which, paired
with phase-4's long-gamma regime, resolves as **"capped/range," not an imminent
reversal.** Composite verdict: **MIXED/NEUTRAL with a mild bearish-flow lean over mild
DP accumulation** = the buy-write range thesis. No new contradiction surfaced.

## Key signals

- `signal-confluence`: **MARA in neither bullish≥1 nor bearish≥1 list** → no
  directional confluence `[INSIGHT:signal-confluence]`.
- `conviction-matrix`: **MIXED**, 6.8% confidence, "balanced dark pool"
  `[INSIGHT:conviction-matrix]`.
- `institutional-accumulation`: **NEUTRAL**, buy_sell_ratio 1.32, VWAP $14.09 (= phase-2)
  `[INSIGHT:institutional-accumulation]`.
- `price-vs-flow`: **DIVERGENCE** — "price up 12.0% but flow bearish (net −$1.6M)"
  `[INSIGHT:price-vs-flow]`.
- Whole-tape net_flow **−$1,605,816** reconfirmed across deep-dive / price-vs-flow /
  analyst-vs-flow `[INSIGHT:deep-dive]`.

## Detailed findings

### Deep-dive snapshot (whole-tape `uw_screener` — reconciles phases 0.5/1)

| Field | Value |
|-------|-------|
| call_premium / put_premium | $12,926,879 / $2,231,047 |
| bullish_premium / bearish_premium | $5,715,408 / $7,321,224 |
| **derived net_flow** | **−$1,605,816 (net bearish)** |
| put_call_ratio | 0.1276 |
| iv_rank / iv30d | 30.30 / 0.797 |
| implied_move / implied_move_perc | 0.207 / 0.01456 (**±1.46%** — phase-9 N4) |
| total_open_interest | 1,900,583 |
| next_earnings_date | 2026-08-04 |

Matches phase-1 exactly. (Yahoo fundamentals sub-block null again — price/sector/PE
sourced from `fz`/local parquet upstream: spot $14.22, P/E n/a (loss-making), short
float 26.49%.)

### Signal confluence (market-wide, filtered)

- **MARA absent from both bullish≥1 and bearish≥1 lists** → its directional
  confluence score is below 1 either way. No stacked signal — consistent with
  phase-0.5 (outside top-50) and phase-5 (MIXED 90d flow).

### Conviction matrix (scenario)

- **scenario = MIXED**, `confidence_pct` 6.8, explanation "Balanced dark pool
  activity — no clear bias." Dark-pool buy_ratio 0.568 (between bull 0.6 / bear 0.4
  thresholds).
- **Nuance worth flagging:** the matrix's `options_flow` shows **call_ask_volume
  211,500 > call_bid_volume 108,210** (net call buying *by contract count*) while
  puts are net-sold (put_bid 22,040 > put_ask 16,983). Yet by **premium/dollars** the
  tape is net-bearish (bullish $5.7M < bearish $7.3M). Reconciliation: **lots of cheap
  retail call buying (volume) vs a few large near-ATM call sells (dollars)** — the
  smart-money, dollar-weighted read is bearish; the contract-count read is mildly
  bullish-retail. Phase-9 should weight the **dollar/premium** read.

### Price vs flow (divergence)

- **divergence = true**: "Price is up 12.0% but options flow is bearish (net flow
  −$1,605,816)." flow_direction bearish, period_high $15.32, period_low $11.53,
  price $12.70→$14.22 (+11.97%).
- Read: this is the **overwrite-into-strength / buy-write divergence**, not a fresh
  reversal trigger — holders sold calls as price rallied (phase-2 accumulation +
  phase-1 call-selling). Per the skill, divergence is "early" — paired with phase-4
  **long-gamma**, it resolves as **capped/range**, not an imminent down-leg.

### Analyst vs flow

- `analyst`/`consensus` = **null** (yfinance analyst block empty for MARA — a known
  thin sub-block, `[[data-source-workarounds]]`). `options_flow.flow_sentiment` =
  **bearish** (net −$1.6M). Cross-source analyst view from phase-5 `fz`: **Target
  $17.70 (+24% vs $14.22)** — Street still constructive vs a bearish near-term flow →
  a *disagreement* (Street long-term up, options flow near-term capped).

### Institutional accumulation

- `signal` = **NEUTRAL — balanced dark pool activity**. buy_sell_ratio **1.32**
  (buy 4,293,232 / sell 3,261,706 = 56.8% buy), total_dp_premium **$106.46M**,
  total_dp_volume 7,554,938, **VWAP $14.09**, avg_trade_price $14.03, 30d price
  +11.97%. **Exactly reproduces phase-2** (mild buy lean, not strong enough to label
  ACCUMULATION).

### Earnings play

- **Out of window** — next earnings 2026-08-04 (47 DTE > 30). Skipped (not an error).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `insights deep-dive --symbol MARA --date 2026-06-18` (reused) | net_flow −1.6M, implied_move 1.46% ← `.uw_screener` | 1 |
| `insights signal-confluence --direction bullish\|bearish --min-score 1 --top-n 20` | MARA in neither list ← ticker scan | top-20 ea |
| `insights conviction-matrix --symbol MARA --date 2026-06-18` | MIXED, 6.8% ← `.scenario,.confidence_pct` | 1 |
| `insights price-vs-flow --symbol MARA --lookback-days 30` | divergence true, flow bearish ← `.divergence,.divergence_signal` | 30d |
| `insights analyst-vs-flow --symbol MARA` | analyst null, flow bearish ← `.analyst,.options_flow.flow_sentiment` | 1 |
| `insights institutional-accumulation --symbol MARA` | NEUTRAL, buy_sell 1.32, VWAP 14.09 ← `.signal,.buy_sell_ratio,.vwap` | 1 |

## Tool errors

(none — `analyst-vs-flow` null analyst block and `earnings-play` out-of-window are
expected, not errors.)

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (neither list) | **agrees** 0.5/1/5 | no directional edge — matches BUSY_NAME / MIXED |
| conviction_matrix (MIXED) | **agrees** 1/2 | balanced; matches capped/buy-write |
| institutional_accumulation (NEUTRAL, 1.32) | **agrees** 2 | identical to phase-2 mild-buy (56.8%) |
| price_vs_flow (DIVERGENCE) | **agrees** 1/4 | buy-write-into-strength; long-gamma → capped, not reversal |
| analyst_vs_flow | partial | flow bearish vs `fz` Street target +24% — long-term/near-term split (defer to 7b/7c) |

## Verdict for downstream phases

- **UW composite bias:** **MIXED / NEUTRAL** with a **mild bearish-flow lean over mild
  DP accumulation** — i.e. the **buy-write / range-bound** read. No clean direction.
- **Conviction:** **3/5** — the composite is internally consistent and reproduces
  phases 1–6; its very neutrality (MIXED, no confluence) is itself the signal: **this
  is a range/premium-selling setup, not a directional trade.**
- **Phase-9 baseline:** treat the setup as **capped-upside / range-bound / premium-
  selling**, gravity ~$14 (VWAP $14.09, max-pain $14), cap $14.5–$15. Override only
  with specific contrary evidence from phases 7b/7c/8/8b.
- **Open questions:**
  - The price-vs-flow **divergence** + weak Q1 fundamentals (phase-6) — is the bearish
    flow purely benign overwriting, or is there a fundamental rationale (phase-7b
    quality veto) that makes the capped read lean genuinely bearish?
  - Street target $17.70 vs bearish flow — does phase-7c sentiment/SI (26.5% short
    float!) tilt this toward a squeeze risk or confirm the cap?
