# Phase 2 — Dark Pool & Block Prints

**Ticker:** ADBE
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T20:30:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

ADBE printed **$173.8M of total off-exchange premium** on 2026-05-19 with a
**mega-tier buy_ratio of 1.00** — one single $24.1M block at **$261.86**
hitting **$4.71 ABOVE NBBO mid** (the highest "trade-vs-mid" of the
session) `[DP:block_stratified] [DP:largest]`. The block tier
(≥$1M trades) is **66.8% buy-side** on $21.4M premium, and the large tier
(≥$100k) is **53.5% buy-side** on $128.3M premium — every institutional
tier is net-buying. Five-day price-level clustering pins $255.64 as the
dominant institutional level ($133.4M / 521.8k shares across 34 prints),
~$3 above the 2026-05-19 close near $252. **Read: institutional
accumulation through the May 13-19 dip, with at least one mega ticket
paying up over $4 to get filled.** This is the bullish counterweight to
the front-end put hedging surfaced in phase-1-flow.md.

## Key signals

- **Mega ticket $24.1M @ $261.86, +$4.71 vs mid, 92,057 shares**
  `[DP:largest]` — the most aggressive institutional accumulation footprint
  of the day. Buyer paid 1.8% premium to NBBO mid; this is "size-now"
  desperation buying, not patient algo accumulation.
- **Block tier (≥$1M) buy_ratio 0.668 on $21.4M / 10 trades**
  `[DP:block_stratified]` — well above the 0.55 "accumulation" threshold
  from the phase-2 rubric.
- **Five-day institutional center-of-gravity = $255.64** with $133.4M /
  521.8k shares across **34 separate trades** `[DP:price_levels, days=5]`.
  Multi-day concentration at one level = a desk-defined VWAP target.
- **Secondary clusters $252 ($36.2M / 6 trades) and $253 ($13.5M / 7
  trades)** `[DP:price_levels]` — current spot ≈ $252 sits ON the cluster,
  not below it. Institutions defended the level into the close.
- **Deep support shelves at $236-237 and $233.85** ($15.8M + $14.0M +
  $7.4M) `[DP:price_levels]` — 7-8% below spot, marks the prior demand
  zone established earlier in May.
- **Extended-hours prints all in $257.66-$260.87 zone**, totaling ~$2.1M
  across 11 prints — **all above where ADBE closed** ($252) — pre-market
  buyers got filled higher, which is mild accumulation evidence rather
  than overnight distribution `[DP:extended_hours]`.

## Detailed findings

### Largest blocks (top 12, sorted by premium)

| Time (UTC) | Price | Size | Premium ($) | NBBO mid | Trade vs mid | Read |
|------------|------:|-----:|------------:|---------:|-------------:|------|
| 15:42:58 | **261.861** | **92,057** | **24,106,138** | 257.155 | **+4.706** | **MEGA aggressive buy** |
| 17:23:44 | 252.330 | 14,733 | 3,717,578 | 252.330 | 0.000 | At-mid passive print |
| 13:54:10 | 264.280 | 12,440 | 3,287,643 | 264.495 | −0.215 | Below mid (mildly sell) |
| 14:35:42 | 263.200 | 12,200 | 3,211,040 | 263.055 | +0.145 | At/above mid (buy) |
| 15:28:24 | 257.230 | 9,739 | 2,505,163 | 257.230 | 0.000 | At-mid |
| 14:20:36 | 263.975 | 8,184 | 2,160,371 | 263.975 | 0.000 | At-mid |
| 19:52:37 | 254.543 | 6,760 | 1,720,707 | 254.615 | −0.073 | Slightly below mid |
| 17:40:05 | 255.000 | 6,303 | 1,607,265 | 254.875 | +0.125 | Above mid (buy) |
| 13:42:33 | 260.240 | 4,200 | 1,093,008 | 260.055 | +0.185 | Above mid (buy) |
| 15:01:51 | 259.260 | 4,100 | 1,062,966 | 259.515 | −0.255 | Below mid (sell) |
| 19:57:55 | 254.939 | 4,160 | 1,060,547 | 254.990 | −0.051 | At-mid |
| 15:44:59 | 256.660 | 3,880 | 995,841 | 256.590 | +0.070 | Above mid (buy) |

Block-tier sentiment (top 12): **7 buys, 3 sells, 2 at-mid** by trade-vs-mid
sign. The single MEGA block at +$4.71 over mid is an extreme outlier —
without it, block buy/sell roughly balances, but its $24.1M weight dominates
the tier statistic.

### Tier breakdown (single-day)

| Tier | Buy vol | Sell vol | Buy_ratio | Total premium ($M) | Trades | Read |
|------|--------:|---------:|----------:|-------------------:|-------:|------|
| MEGA (≥$10M)   | 92,057  | 0       | **1.000** | 24.11   | 1   | Single aggressive accumulator |
| BLOCK (≥$1M)   | 55,359  | 27,460  | **0.668** | 21.43   | 10  | Net buy (above 0.55 threshold) |
| LARGE (≥$100k) | 265,952 | 231,106 | 0.535     | 128.31  | 586 | Modest net buy |
| RETAIL (<$100k)| 0       | 0       | 0.500     | 0.00    | 0   | Empty in this snapshot |
| **TOTAL ALL TIERS** | — | — | — | **173.85** | 597 | — |

All institutional tiers are buy-skewed. The **MEGA print is the single
highest-conviction footprint of the entire day**; if the block_stratified
classifier is accurate (NBBO-based), this is a "size-up" institution
forced to pay the offer.

### Price levels (5-day cluster, top 15)

| Price | Total $premium ($M) | Total shares | Trades | Distance to spot $252 |
|------:|--------------------:|-------------:|-------:|----------------------:|
| **255.64** | **133.4** | **521,767** | **34** | +1.4% (resistance turned magnet) |
| 252.00 | 36.2 | 143,818 | 6 | flat (current spot pin) |
| 261.86 | 24.1 | 92,057 | 1 | +3.9% (single mega print) |
| 236.07 | 15.8 | 67,002 | 31 | −6.3% (deep support shelf) |
| 237.01 | 14.0 | 59,040 | 23 | −5.9% (paired w/ 236) |
| 253.00 | 13.5 | 53,215 | 7 | +0.4% |
| 233.85 | 7.4 | 31,835 | 4 | −7.2% (floor) |
| 263.20 | 4.7 | 18,040 | 4 | +4.4% |
| 252.33 | 3.9 | 15,333 | 2 | +0.1% |
| 236.74 | 3.8 | 16,047 | 6 | −6.0% |
| 236.30 | 3.4 | 14,566 | 7 | −6.2% |
| 234.40 | 3.4 | 14,627 | 5 | −6.9% |
| 264.28 | 3.4 | 12,840 | 2 | +4.9% |
| 254.30 | 3.4 | 13,342 | 9 | +0.9% |
| 243.95 | 3.4 | 13,755 | 3 | −3.2% |

Cluster map (3 zones):
- **Resistance / supply zone: $261-264** ($24.1M + $4.7M + $3.4M = $32.2M)
- **Magnet / mid zone: $252-255.64** ($133.4M + $36.2M + $13.5M + $3.9M +
  $3.4M = ~$190M institutional VWAP — by far the densest)
- **Demand floor: $233-237** ($15.8M + $14.0M + $7.4M + $3.8M + $3.4M +
  $3.4M = ~$48M, dispersed across many small prints — looks like a desk
  laddering a position, not a single buyer)

### Extended-hours activity

11 ext-hours prints between 08:33 UTC and 13:18 UTC totaling ~$2.13M.
Price range $257.66 → $260.87, **all above the regular-session close of
~$252.** No post-market activity captured. Pre-market buying ahead of a
regular-session selloff = the pre-market crowd was wrong, but the pattern
is **bullish positioning that got squeezed** rather than overnight
distribution. Not a high-conviction signal on its own; corroborates the
intraday mega-buyer narrative.

### ADBE in market context

ADBE did **not** make the top-50 dark-pool tickers by aggregate premium
on 2026-05-19; the cutoff there is ~$434M (VUG). ADBE's $173.8M still
ranks materially above the long tail. The top of the list is dominated
by ETFs, semis (MU, NVDA, INTC, AMD, AVGO), and mega-caps (AAPL, MSFT,
GOOGL, AMZN, META). **In its sector / market-cap peer set, ADBE's DP
activity is elevated but not extreme.**

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=ADBE, top-n=25, sort-by=premium, date=2026-05-19 | 25 blocks, top = $24.1M @ +$4.71 mid |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=ADBE, top-n=30, min-tier=large, date=2026-05-19 | All-tier total $173.8M; mega 100% buy |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=ADBE, top-n=15, date=2026-05-19 | 11 ext-hr prints, $2.1M, all $257-261 |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=ADBE, top-n=15, days=5, date=2026-05-19 | 5-day clusters; dominant $255.64 |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=50, date=2026-05-19 | ADBE NOT in top-50 (cutoff ~$434M) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION** (mega buy_ratio 1.0, block
  buy_ratio 0.668, price levels above spot, extended-hours buyers).
- **Conviction:** **4/5** — single mega print is the cleanest possible
  accumulation signal; block-tier corroborates; large-tier is only mildly
  positive. The 4 (not 5) reflects that the mega print is concentrated in
  ONE ticket (single-actor risk), so if it was a basket trade or a tracking
  error the signal degrades.
- **Three S/R levels for phase-9:**
  1. **$255.64** — 5-day institutional VWAP; primary magnet. **Entry zone
     pullback target.** First reclaim level on any bounce.
  2. **$236-237** — multi-day floor with 60+ trades stratified across
     prices. **Hard stop / invalidation zone**; a daily close below
     ~$233.85 breaks the demand shelf.
  3. **$261.86 / $263.20** — recent supply / where mega buyer paid up.
     **First profit-take zone**; reclaim and hold = thesis confirmation.
- **Open questions:**
  - Does the $255.64 cluster line up with options OI walls? — phase 3
    `oi_pin_risk` will answer.
  - Is dealer gamma positive or negative at the $252-255 zone? — phase 4.
  - Did $236-237 institutional buying coincide with an IV spike or a
    macro selloff? — phase 5 (historical) and phase 6 (macro).
  - **CONFLICT with phase 1:** front-end puts are being bought
    aggressively as event hedges while institutions accumulate stock.
    This isn't necessarily contradictory (stock-long + put-collar is a
    common structure into earnings) but phase 9 must reconcile and
    phase 10 must score the apparent tension.
