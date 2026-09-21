# Phase 7 — UW Insights Confluence

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:58:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-5-historical.md

## Summary

**UW's composite engine does NOT endorse a bullish setup — it leans cautious,
which is the value of this consolidation pass.** The `conviction-matrix` returns
**DISTRIBUTION** (13.5% confidence), `institutional-accumulation` returns
**DISTRIBUTION**, and **NOW is absent from the bullish `signal-confluence` list
even at min-score 1 (score 0)**. The single constructive composite is
`price-vs-flow`: bullish flow + rising price are **ALIGNED, no divergence**
(+8.42% over 30d). The DISTRIBUTION labels are driven by the dark-pool buy_ratio
0.365 — the **same sell-tilt phase-2 showed is inflated by after-hours
closing-cross/rebalance prints**, so they overstate true intraday distribution. Net
composite read: **a bullish, price-confirmed options tape with NO accumulation
confirmation** — phase-9's baseline is "cautious-bullish, un-corroborated."

## Key signals

- `conviction-matrix` **DISTRIBUTION** (confidence **13.5%** — low) `[INSIGHT:conviction_matrix]`
- `institutional-accumulation` **DISTRIBUTION** (buy/sell 0.57; sell 3.68M > buy 2.11M) `[INSIGHT:institutional_accumulation]`
- **NOW absent from bullish `signal-confluence` (score 0)** — engine does not flag a bullish confluence `[INSIGHT:signal_confluence]`
- `price-vs-flow` **ALIGNED, no divergence** — bullish flow + price +8.42% `[INSIGHT:price_vs_flow]`
- Whole-tape: bullish prem $32.0M > bearish $27.0M, net +$5.0M, P/C 0.284, IV rank 63 `[INSIGHT:deep_dive]`

## Detailed findings

### Deep-dive snapshot `[INSIGHT:deep_dive]`

Directional aggregates (reconciled vs phase-1 & phase-0.5 `[CTX:]`):

| field | value |
|-------|-------|
| bullish_premium / bearish_premium | $31.98M / $26.97M |
| net_flow | +$5.01M |
| call_premium / put_premium | $59.40M / $17.22M (P/C 0.284) |
| implied_move / implied_move_perc | $4.15 / **4.07%** (phase-9 N4) |
| iv_rank / iv30d | 63.07 / 0.582 |
| total_open_interest | 1,404,048 |
| dark pool total premium | $595.6M (avg $103.06, 2,112 trades) |
| next_earnings | 2026-07-22 (51 DTE — outside near-term) |

Yahoo fundamentals: **HTTP 401 (unavailable)** — deferred to phase-7b (Finnhub/fz).

### Signal confluence `[INSIGHT:signal_confluence]`

NOW **not in the bullish list at min-score 1** → confluence score **0**. UW's
6-factor engine (which weighs DP accumulation + OI + price + flow jointly) finds no
bullish stack. Consistent with the DP/OI caution in phases 2–3; contradicts a naïve
read of phase-1's call premium alone.

### Conviction matrix `[INSIGHT:conviction_matrix]`

- `scenario` **DISTRIBUTION**, `confidence_pct` **13.5** (weak), `explanation`
  "Dark pool selling with mixed options activity."
- DP buy_ratio 0.365 (< bear threshold 0.4); options call_ask 59,293 > call_bid
  48,206 (bullish), puts slightly bid-side. → options bullish, DP selling → net
  low-confidence DISTRIBUTION.
- **Caveat (carry phase-2):** the DP buy_ratio 0.365 uses *all tiers incl.
  after-hours* — the mega "sells" are $102.12 closing-cross/rebalance prints.
  Intraday large-tier was balanced (0.492). So this label **overstates** true
  distribution; read it as "no accumulation," not "active distribution."

### Price vs flow `[INSIGHT:price_vs_flow]`

- `divergence` **false** — "Price and flow are aligned." `flow_direction` bullish,
  `price_change_pct` **+8.42%** (period 94.19→102.12, range 83.58–110.83).
- **The cleanest constructive composite:** bullish flow is *confirmed* by rising
  price — no reversal-divergence warning. Pairs with phase-4 short-gamma (moves
  amplify) and phase-5 V-recovery.

### Institutional accumulation `[INSIGHT:institutional_accumulation]`

- `signal` **DISTRIBUTION** — "dark pool sell volume significantly exceeds buy."
  buy_side 2.11M / sell_side 3.68M (ratio 0.57). Top level $102.12 ($162M, 47
  trades) — the rebalance-inflated cluster again. Same AH caveat → "no
  accumulation," de-rate the "distribution" strength.

### Analyst vs flow `[INSIGHT:analyst_vs_flow]`

- Returned **options_flow only (bullish, net +$5.0M)** — **no analyst consensus**
  (yfinance analyst side empty). No Wall-St-vs-flow comparison available here;
  deferred to phase-7b/7c (Finnhub analyst revisions).

### Earnings play

- Skipped — earnings 2026-07-22 is **51 DTE, outside the 30-day window** (not an
  error; out of window per phase-6 calendar).

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw insights conviction-matrix --symbol NOW` | DISTRIBUTION, 13.5% conf |
| `uw insights price-vs-flow --symbol NOW --lookback-days 30` | aligned, no divergence, +8.42% |
| `uw insights institutional-accumulation --symbol NOW` | DISTRIBUTION (sell > buy) |
| `uw insights analyst-vs-flow --symbol NOW` | options bullish; analyst side empty |
| `uw insights signal-confluence --direction bullish --min-score 1` | NOW absent (score 0) |
| `uw insights deep-dive --symbol NOW` | whole-tape bullish; yahoo fundamentals 401 |

## Tool errors

- `uw insights deep-dive` → `yahoo_fundamentals: HTTP 401` (fundamentals unavailable; handled in phase-7b).
- `uw insights analyst-vs-flow` → analyst consensus side empty (yfinance); no error, just no data.

## Cross-check vs phases 1–5

| UW insight | Phase agreement? | Notes |
|------------|------------------|-------|
| signal_confluence (score 0) | **DISAGREES phase-1**, agrees phase-2/3 | No bullish stack despite call premium → DP/OI caution wins |
| conviction_matrix (DISTRIBUTION) | agrees phase-2 (soft DP) | But inflated by AH rebalance (phase-2 de-rated) → "no accumulation" |
| institutional_accumulation (DISTRIBUTION) | agrees phase-2 | Same AH caveat |
| price_vs_flow (aligned bullish) | **agrees phase-1 + phase-5** | Bullish flow confirmed by +8.42% price |

## Verdict for downstream

- **UW composite bias:** **MIXED / cautious-bullish.** Flow is bullish and
  price-confirmed (price-vs-flow aligned), but the accumulation composites say
  DISTRIBUTION (low-confidence, rebalance-inflated) and the bullish confluence
  engine scores NOW **0**. The composite does **not** corroborate a directional long.
- **Conviction:** **2/5** — the consolidation pass actively withholds a bullish
  endorsement; only price-vs-flow alignment is clean.
- **Phase-9 baseline:** treat this as "**bullish, price-aligned options flow that
  the institutional composite does NOT confirm with accumulation.**" Override toward
  more-bullish only with specific contrary evidence (e.g., proving the AH blocks
  were benign rebalance — phase-2 already argued this); otherwise size as an
  un-corroborated tactical bounce, not a high-confluence long.
- **Open questions:**
  1. Does fundamentals (phase-7b) explain the −33% YTD and justify either the bounce or further downside?
  2. Does the complacent skew + crowded calls (phase-4) trip the positioning gate (phase-7c)? The composite's refusal to flag bullish confluence raises the bar.
