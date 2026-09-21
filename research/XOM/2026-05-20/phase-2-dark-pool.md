# Phase 2 — Dark Pool & Block Prints

**Ticker:** XOM
**As-of date (user request):** 2026-05-20
**Effective data date:** 2026-05-18
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

XOM cleared **$492.2M** of dark-pool premium on 2026-05-18 — a heavy day, but
the day's footprint is **mixed-leaning-distribution**: the mega tier (6 trades,
$206.6M) printed `buy_ratio = 0.049` (95% sell-classified), while the block
tier (39 trades, $65.3M) and large tier (941 trades, $220.4M) show only mild
buy skews of 0.586 and 0.545 respectively. Five-day price-level aggregation
reveals a **massive institutional accumulation cluster at $150–152**
(≥$1.1B cumulative premium across $150.63/$150.80/$150.91/$150.93/$151.57/
$152.39/$152.78) — that was the bid-zone of the rally that took spot from
$155.85 → $161.10 intraday on 2026-05-18. Today's prints concentrate at
**$159.30 / $159.44 / $160.49** with most mega prints landing **below NBBO mid**.
*(see phase-1-flow.md §"Detailed findings" — the 5-of-5-session sweep
persistence in options aligns with this multi-day institutional footprint.)*

## Key signals

- **Largest single print of the day: $79.68M at $159.44** (499,749 shares,
  19:52:49Z, NBBO mid $160.21 → trade_vs_mid = **-$0.77 below mid**, sell-side
  classification). Single largest XOM trade across the regular + ext-hours
  session. [DP:dark_pool_largest]
- **Mega-tier sell skew on the day:** 6 mega trades totaling $206.6M with
  buy_ratio **0.049** — i.e. only ~$10M of mega-tier was buy-classified, the
  rest sell-classified. [DP:dark_pool_block_stratified]
- **Five-day institutional accumulation cluster at $150–152**: top price-level
  $151.57 alone shows **$739.5M** premium across 67 trades. Stacking the
  $150.63 / $150.80 / $150.91 / $150.93 / $151.57 / $152.39 / $152.78 prints
  gives ~$1.34B aggregated premium 5–6% below today's spot. [DP:dark_pool_price_levels]
- **Heavy post-close (extended-hours) activity:** $60M+ of XOM printed in the
  20:00–22:00Z window, all at $160.49 (the closing print). Largest ext-hours
  print = $32.86M (205,815 shares, 20:09:29Z) — likely VWAP/closing-cross
  execution but adds to the mega-tier sell skew. [DP:dark_pool_extended_hours]
- **XOM is not in top-30 dark-pool tickers**: the 30th-ranked name (CRWV) has
  $827M; XOM at $492M would rank ~45–55. Heavy by absolute size, but moderate
  vs. index-ETF and mega-cap-tech leaders. [DP:dark_pool_ticker_summary]

## Detailed findings

### Largest blocks

Top 6 individual XOM prints (date 2026-05-18, sorted by premium):

| Time (UTC) | Price | Size | Premium | NBBO mid | Trade vs Mid | Side |
|---|---|---|---|---|---|---|
| 19:52:49 | $159.4425 | 499,749 | $79,681,230 | 160.21 | **-$0.77** | sell |
| 15:13:02 | $159.30 | 300,000 | $47,790,000 | 159.32 | -$0.02 | ~mid |
| 20:09:29 | $159.6412 | 205,815 | $32,856,553 | 160.20 | -$0.56 | sell |
| 21:42:37 | $160.49 | 123,196 | $19,771,726 | 160.59 | -$0.10 | sell |
| 14:03:04 | $156.345 | 104,410 | $16,323,981 | 156.345 | 0.00 | mid |
| 20:49:05 | $160.49 | 63,392 | $10,173,782 | 160.425 | **+$0.065** | buy |

Pattern: 5 of 6 mega prints landed at or below NBBO mid; the one above-mid
print is the smallest mega ($10.2M). The 19:52:49Z and 20:09:29Z prints
together total $112.5M of likely VWAP / institutional unwind during the
20:00Z post-close window.

### Tier breakdown (single-day, 2026-05-18)

| Tier | Premium | Trade count | Buy ratio | Read |
|------|---------|-------------|-----------|------|
| **Mega** (≥$10M) | $206,597,273 | 6 | **0.049** | 95% sell-classified — strong distribution signal at mega tier |
| **Block** (≥$1M) | $65,279,177 | 39 | 0.586 | Mild buy skew |
| **Large** (≥$100k) | $220,357,333 | 941 | 0.545 | Slight buy skew, very high trade count |
| Retail | $0 | 0 | n/a | (no retail-tier prints reported) |
| **Total** | **$492,233,782** | 986 | weighted ~0.40 | Net: institutional distribution + retail-channel accumulation |

Caveat (verbatim from tool): "Conviction in mega/block tiers is the
institutional smart-money signal; retail-tier moves are noise." With only 6
trades at mega tier the ratio is sensitive — the $79.68M single print
dominates. If that print is actually a VWAP cross (not directional sell),
the mega buy_ratio could materially understate true institutional intent.
**Treat mega buy_ratio 0.049 as suggestive, not high-confidence.**

### Price levels (5-day aggregation, 2026-05-14 → 2026-05-18)

Sorted by total_premium:

| Price | Premium | Shares | Trades | Distance from $160.49 |
|-------|---------|--------|--------|------------------------|
| $151.57 | $739,495,479 | 4,878,904 | 67 | -5.6% |
| $150.63 | $181,388,567 | 1,204,199 | 61 | -6.1% |
| $152.78 | $135,030,462 | 883,823 | 62 | -4.8% |
| $150.93 | $123,651,004 | 819,249 | 16 | -6.0% |
| $150.80 | $99,391,327 | 659,079 | 8 | -6.0% |
| $150.91 | $82,460,925 | 546,416 | 17 | -6.0% |
| **$159.44** | $80,424,858 | 504,413 | 2 | -0.65% |
| $152.39 | $80,088,942 | 525,560 | 3 | -5.0% |
| **$160.49** | $75,724,633 | 471,834 | 74 | 0.0% |
| $159.30 | $48,342,771 | 303,470 | 4 | -0.74% |
| $159.64 | $32,968,298 | 206,515 | 2 | -0.53% |
| $150.76 | $19,856,010 | 131,703 | 6 | -6.1% |
| $151.32 | $19,507,872 | 128,921 | 8 | -5.7% |
| $156.35 | $17,553,952 | 112,277 | 7 | -2.6% |
| $157.43 | $15,610,580 | 99,161 | 9 | -1.9% |

**Cluster 1 (institutional accumulation, ~$1.34B aggregated):** $150.63 to
$152.78 — multi-session bid zone. This is where the rally started, likely the
2026-05-12 to 2026-05-15 sessions.

**Cluster 2 (today's churn, ~$237M aggregated):** $159.30 / $159.44 / $159.64
/ $160.49 — today's print zone. The high trade-count (74) at $160.49 vs. low
trade-count (2–4) at $159.30 / $159.44 / $159.64 suggests $160.49 was hit by
many smaller institutional accounts (closing prints, VWAP fills) while the
$159.30 / $159.44 levels were a few large negotiated blocks.

**Cluster 3 (intraday transit, $33M):** $156.35 / $157.43 — modest activity
during the ramp from $156 to $160.

### Extended-hours activity

15 ext-hours prints (all flagged `extended_hours_trade`). All occurred in the
20:00:24Z → 22:00Z window (post-4pm-ET close). Aggregate ext-hours premium
visible in top 15: **$87.7M**. Notable:
- 9 of 15 prints are at exactly $160.49 (the closing-cross reference price)
- The two largest ext-hours prints are also the two largest of the entire day
  (the $32.86M and $19.77M sells listed above)

This is consistent with **institutional unwind into the closing cross** or
ETF rebalance flow — not necessarily directional. XOM is a major component of
XLE, VTV, and S&P 500 funds; closing-cross VWAP executions are routine. But
the *size* ($60M+ in post-close at-mid-or-below prints) is heavy and adds to
the mega-tier sell-side skew.

### Ticker summary cross-check

XOM **does not appear** in the top-30 dark-pool tickers list (cutoff at
CRWV $827M). XOM's $492M ranks below LITE ($1.03B), AMD ($2.6B), TSLA ($5.1B),
etc. — meaningful absolute size but not at the "all-eyes" mega-cap level.
Phase 5 historical should compare today's $492M against XOM's 30-day average
to determine whether this is elevated or normal.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=XOM, top-n=25, sort-by=premium, date=2026-05-18 | 25 rows; top $79.7M @ $159.44 (size 499,749), 5/6 mega prints below mid |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=XOM, min-tier=large, top-n=30, date=2026-05-18 | Total $492.2M; mega buy_ratio 0.049, block 0.586, large 0.545 |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=XOM, top-n=15, date=2026-05-18 | 15 ext-hours prints, all in 20:00-22:00Z, aggregate $87.7M, 9 prints at $160.49 |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=XOM, days=5, top-n=15, date=2026-05-18 | $150-152 cluster aggregates ~$1.34B; today's $159-160 cluster ~$237M |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=30, date=2026-05-18 | XOM absent (30th = CRWV $827M; XOM at $492M ranks ~45-55) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed-leaning-distribution** (mega tier 95% sell
  + 5/6 mega prints below mid + heavy ext-hours selling at $160.49) AGAINST the
  context of a $1.34B 5-day accumulation at $150-152 (i.e. existing longs may
  be **trimming into strength**, not turning short).
- **Conviction:** 3/5 (heavy absolute size + clear mega-tier sell skew, but
  ratio sensitivity at 6 mega trades and possible VWAP-cross attribution caps
  conviction).
- **Three S/R levels for phase-9 to use:**
  1. **Strong institutional support at $150–152** ($1.34B aggregated premium
     across 7 levels in the 5-day window). A break below $150 invalidates the
     bull case — institutional cost basis is *here*, not lower.
  2. **Today's distribution / accumulation zone at $159.44 → $160.49** ($237M
     aggregate). Acts as both today's resistance (above-mid print rare) and
     near-term magnet (very high trade count at $160.49).
  3. **Intraday floor at $156.35–$157.43** ($33M aggregate, 16 trades). Modest
     support — useful as the first pullback level before the $150–152 zone.
- **Open questions:**
  - Is the $79.68M 19:52Z print a VWAP execution or directional sell? Phase 6
    should check for after-hours news on 2026-05-18 that might have caused a
    block. Phase 7's `insights_institutional_accumulation` should give a
    multi-day vector that disambiguates.
  - **The phase-1 Dec'26 160P ($1.1M ask-side, $612k single block) timestamp
    is 15:42:58Z — the same hour as the $47.79M 15:13Z mid-cross print.** Are
    these the same actor hedging a block buy with a tactical put? Cross-check
    via phase-3 OI delta on Dec'26 160P.
  - Is the mega-tier sell concentration consistent with XOM's 30-day baseline
    (institutions chronically sell into rallies in oil stocks) or a regime
    change? Phase 5 must compare today's $492M against rolling baseline.
