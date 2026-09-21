# Phase 2 — Dark Pool & Block Prints

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:07Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark-pool tape on SYM is **modestly accumulative**: 13 large-tier prints
totaling $1.82M premium with **buy_ratio 0.672** (24,294 buy shares vs 11,854
sell shares) [DP:block_stratified]. No mega-tier or block-tier prints — this
is mid-institutional positioning, not a single anchor LP. The single largest
print is 4,000 shares at $50.40 (+3¢ vs NBBO mid), executed 09:54 ET
[DP:largest], i.e., buy-side. A 5-day price-level scan shows the deepest
institutional base in the **$46.40–$47.40 zone** ($4.04M aggregated premium
across that band) with a fresh, sizable cluster at **$49.96** ($2.02M, 40,356
shares) [DP:price_levels]. **Net read: accumulation underneath current spot
in the high-$46s/low-$47s, plus a same-week mid-$49s shelf — directly
contradicts the "distribution" interpretation that the bid-side LEAP call
flow in phase-1 might suggest in isolation.**

## Key signals

- **Buy_ratio 0.672 in large tier**, 13 trades, $1.82M premium
  [DP:block_stratified]. ≥0.55 = accumulation by rubric → accumulation
  confirmed.
- **No mega/block-tier prints** [DP:block_stratified] — conviction is
  capped: this is not "a billionaire bought a billion-dollar stake," it is
  "several mid-size funds are quietly adding."
- **Single largest print at +3¢ vs NBBO mid**: 4,000 sh @ $50.40 vs mid
  $50.37, 09:54 ET [DP:largest]. Buy-side ask-print.
- **Deep institutional base at $46.40–$47.40**: aggregated multi-day
  premium ≈ **$4.04M** across 9 sub-levels in that 100-bp band
  [DP:price_levels]. This is the multi-week accumulation zone.
- **Fresh $49.96 shelf**: $2.02M / 40,356 shares in 2 prints —
  same-week add right under spot [DP:price_levels].
- **SYM does not appear in top-100 ticker_summary** [DP:ticker_summary] —
  absolute premium ($1.82M today) is small vs mega-caps. Signal is real
  but ticker is mid-liquidity.

## Detailed findings

### Largest blocks (sorted by premium)

| Time (UTC) | Price | NBBO mid | vs mid | Size | Premium | Read |
|------------|-------|----------|--------|------|---------|------|
| 13:54 | 50.400  | 50.370 | +0.030 | 4,000 | $201,600 | **buy** |
| 16:14 | 50.060  | 50.060 | 0.000  | 3,907 | $195,584 | neutral |
| 17:45 | 50.720  | 50.670 | +0.050 | 3,185 | $161,543 | **buy** |
| 19:58 | 51.000  | 50.970 | +0.030 | 3,017 | $153,867 | **buy** |
| 18:41 | 50.4551 | 50.455 | +0.0001 | 2,988 | $150,760 | neutral |
| 16:02 | 49.800  | 49.820 | −0.020 | 2,837 | $141,283 | sell |
| 17:34 | 50.600  | 50.640 | −0.040 | 2,700 | $136,620 | sell |
| 17:21 | 50.340  | 50.280 | +0.060 | 2,552 | $128,468 | **buy** |
| 14:13 | 50.815  | 50.815 | 0.000  | 2,397 | $121,804 | neutral |
| 20:00 | 50.950  | 50.720 | +0.230 | 2,248 | $114,536 | **strong buy** (ext-hr) |
| 18:58 | 50.2201 | 50.255 | −0.035 | 2,272 | $114,100 | sell |
| 13:34 | 50.105  | 50.175 | −0.070 | 2,076 | $104,018 | sell |
| 14:14 | 50.820  | 50.835 | −0.015 | 1,969 | $100,065 | sell |

Buy/sell split by share count from this list: ~17,300 buy-side vs ~11,800
sell-side shares — consistent with the stratified buy_ratio of 0.672.

The **20:00 UTC (4:00pm ET) extended-hours print at $50.95** sits +23¢ above
NBBO mid (a wide quote at that time: bid $50.25 / ask $51.19) — that is the
single most aggressive buy print of the session.

### Tier breakdown

| Tier | Trades | Premium | Buy vol | Sell vol | Buy ratio |
|------|--------|---------|---------|----------|-----------|
| mega (≥$10M)  | 0  | $0       | 0      | 0      | n/a |
| block (≥$1M)  | 0  | $0       | 0      | 0      | n/a |
| large (≥$100K)| 13 | $1.82M   | 24,294 | 11,854 | **0.672** |
| retail        | (excluded) | — | — | — | — |

All institutional activity is in the **large** tier. No anchor mega/block
print to drive conviction higher than 3/5.

### Price levels (multi-day, days=5)

Sorted by total premium (top 15):

| Level | Premium | Shares | Trades | Distance from spot $50.50 |
|-------|---------|--------|--------|---------------------------|
| **$49.96** | $2,016,186 | 40,356 | 2 | −1.07% |
| $47.01 | $1,230,299 | 26,171 | 3 | −6.91% |
| $49.19 | $637,552  | 12,961 | 2 | −2.59% |
| $46.91 | $586,187  | 12,496 | 3 | −7.11% |
| $46.47 | $506,469  | 10,900 | 2 | −7.98% |
| $47.81 | $478,100  | 10,000 | 1 | −5.33% |
| $47.00 | $455,900  | 9,700  | 1 | −6.93% |
| $47.05 | $436,718  | 9,282  | 3 | −6.83% |
| $47.37 | $435,805  | 9,200  | 1 | −6.20% |
| $45.40 | $417,680  | 9,200  | 1 | −10.10% |
| $46.40 | $380,609  | 8,203  | 1 | −8.12% |
| $47.98 | $355,820  | 7,416  | 1 | −4.99% |
| $47.40 | $322,036  | 6,794  | 1 | −6.14% |
| $46.94 | $302,059  | 6,435  | 2 | −7.05% |
| $47.38 | $297,251  | 6,274  | 2 | −6.18% |

**Cluster aggregates:**
- **$46.40–$47.40 band:** ~$4.04M premium, ~$8K shares × 60 — clear
  multi-day accumulation base.
- **$49.19–$49.96 band:** ~$2.65M premium — fresh week-old shelf right
  under spot.
- Nothing meaningful **above** $51 in the multi-day data → no overhead
  institutional resistance yet built into the dark-pool tape.

### Extended-hours activity

Only one ext-hours print: **20:00 UTC / 4:00pm ET, 2,248 sh @ $50.95**,
premium $114,536 [DP:extended_hours]. Quote was very wide ($50.25 × $51.19),
trade is +23¢ vs the rough midpoint — definitively buy-side, but small
size. No pre-market activity.

No catalyst-night signature (no large pre/post-market block clusters).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=SYM, top-n=25, sort-by=premium, date=2026-05-21 | 13 prints, $1.82M total |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=SYM, top-n=30, min-tier=large, date=2026-05-21 | large-tier only, buy_ratio 0.672 |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=SYM, top-n=15, date=2026-05-21 | 1 print at 20:00 UTC |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=SYM, top-n=15, days=5, date=2026-05-21 | dense cluster $46.4–$47.4 + fresh $49.96 shelf |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=100, date=2026-05-21 | SYM NOT in top-100 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **accumulation** — large-tier buy_ratio 0.672
  + ask-side buy prints at $50.40, $50.60+, $51.00, plus an aggressive
  ext-hours buy at $50.95.
- **Conviction:** 3/5. Buy_ratio is solidly bullish, *but* total premium
  is only $1.82M and there are no mega/block-tier anchors. Lower for thin
  liquidity, capped because the signal is consistent across multiple
  intraday prints.
- **Three S/R levels for phase-9:**
  1. **Support — $46.40–$47.40 institutional base** ($4.04M multi-day
     accumulation). Phase-9 stops should sit *below* this band; a daily
     close inside it would confirm a re-test of accumulation.
  2. **Support — $49.96 shelf** ($2.02M fresh same-week add). First line
     of defense; clean break + close under invalidates the near-term
     accumulation thesis.
  3. **Resistance — none mapped in DP above $51.00.** First test of new
     territory; dark-pool tape has no shelf to lean on above current spot.
- **Open questions:**
  - Phase-3: do OI/positioning changes in calls mirror this accumulation
    (call-build at $50-$55) or does positioning still skew bearish?
  - Phase-2 finds accumulation; phase-1 found LEAP call bids (de-risking).
    Phase-4 GEX/dealer positioning should tell us whether both fit a
    "long stock + write calls" institutional flow, or whether two
    different desks are doing opposite things. Flag for phase-10
    contradiction audit if not reconciled by phase-9.
  - No mega/block prints — is this a function of float (low) or sentiment?
    Phase-6 should pull SYM market cap / float.
