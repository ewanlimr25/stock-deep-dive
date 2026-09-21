# Phase 2 — Dark Pool & Block Prints

**Ticker:** FSLY
**As-of date:** 2026-05-19  (Effective data date: 2026-05-18)
**Generated:** 2026-05-19T00:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark pool tape on 2026-05-18 shows **clear institutional accumulation at
$16.48 – $16.55**: $15.04M total FSLY DP premium, with a 5-of-6
above-mid pattern in the largest blocks and a **block-tier buy_ratio of
0.847** ($7.24M in 3 prints, only one ($1.11M) was a sell)
[DP:dark_pool_block_stratified]. The accumulation is partially
counterbalanced by **post-market distribution** — the single largest
extended-hours print ($1.11M @ $16.60) executed **25¢ below NBBO mid**
[DP:dark_pool_extended_hours]. The 5-day price-level map reveals a much
larger **$22M overhead supply zone at $18.41 – $19.03** that the stock
must work through if the bullish flow campaign from phase-1 plays out
[DP:dark_pool_price_levels]. This **partially confirms** the bullish
options flow read from phase-1-flow.md §"Net interpretation" but adds an
overhead-supply ceiling the trade plan has to respect.

## Key signals

- **Two paired ~$3M block buys at 15:12:17Z and 15:12:51Z** (185,500
  shares each, prices $16.48 and $16.53, both above NBBO mid) →
  **371,000-share accumulation in 34 seconds** at the open of the cash
  session [DP:dark_pool_largest]. This is the headline institutional
  print of the day.
- **Block tier buy_ratio = 0.847** (3 trades, $7.24M, 371K shares bought
  vs 67K sold) [DP:dark_pool_block_stratified] — strong but trade-count is
  thin, so the read is "one institution accumulated" not "many".
- **Post-market sell signature:** the largest 4PM+ print was 67,062 shares
  @ $16.6021 vs NBBO mid $16.855 → executed **25.3¢ below mid**
  [DP:dark_pool_extended_hours]. Followed by a second post-market print
  at $16.71 vs mid $16.795 (−8.5¢). After-hours net = distribution.
- **5-day overhead supply at $18.41–$19.03: $22.0M of cumulative DP
  premium** across 7 price levels [DP:dark_pool_price_levels]. That is
  the wall the long thesis from phase-1 has to break.
- **5-day at-spot support cluster: $16.48–$16.55 ≈ $8.9M** — meaningful
  but smaller than the overhead supply. Tactical floor, not a fortress.

## Detailed findings

### Largest blocks (today, sorted by premium)

`dark_pool_largest`, top 10, date=2026-05-18:

| # | Time (Z) | Price | NBBO mid | Δ vs mid | Size | Premium | Read |
|---|---|---|---|---|---|---|---|
| 1 | 15:12:51 | 16.53 | 16.515 | **+1.5¢** | 185,500 | $3,066,315 | BUY |
| 2 | 15:12:17 | 16.48 | 16.475 | **+0.5¢** | 185,500 | $3,057,040 | BUY |
| 3 | 20:10:59 | 16.6021 | 16.855 | **−25.3¢** | 67,062 | $1,113,370 | SELL (post-mkt) |
| 4 | 18:18:12 | 16.55 | 16.545 | +0.5¢ | 34,100 | $564,355 | mid/buy |
| 5 | 21:03:53 | 16.71 | 16.795 | **−8.5¢** | 32,443 | $542,123 | SELL (post-mkt) |
| 6 | 15:12:21 | 16.465 | 16.465 | 0.0¢ | 31,740 | $522,599 | mid |
| 7 | 18:16:24 | 16.525 | 16.495 | +3.0¢ | 30,100 | $497,402 | BUY |
| 8 | 16:41:38 | 16.51 | 16.495 | +1.5¢ | 28,100 | $463,931 | BUY |
| 9 | 13:51:49 | 16.83 | 16.870 | −4.0¢ | 22,227 | $374,080 | sell-leaning |
| 10 | 14:55:13 | 16.52 | 16.525 | −0.5¢ | 20,783 | $343,335 | mid |

**The 15:12 pair (rows 1 and 2) executed 34 seconds apart, same size
(185,500), same buyer profile** — almost certainly one institutional
order broken into two prints. Combined: $6.12M, 371,000 shares, both
above mid → unambiguous BUY.

### Block-stratified tier breakdown

`dark_pool_block_stratified`, symbol=FSLY, min_tier=large, date=2026-05-18:

| Tier | Trades | Premium | Buy vol | Sell vol | Buy ratio |
|---|---|---|---|---|---|
| **mega** (≥$10M) | 0 | $0 | 0 | 0 | n/a |
| **block** (≥$1M) | 3 | $7,236,725 | 371,000 | 67,062 | **0.847** |
| **large** (≥$100K) | 34 | $7,805,474 | 257,463 | 212,377 | 0.548 |
| Total all tiers | | **$15,042,199** | | | |

The block tier carries the bullish signal. The large tier (still
institutional but smaller orders) is barely off neutral at 0.548 buy —
plenty of two-way flow. No mega prints today.

### Extended-hours activity

`dark_pool_extended_hours`, top 5, date=2026-05-18:

| Time (Z) | Price | NBBO mid (wide) | Δ vs mid | Size | Premium |
|---|---|---|---|---|---|
| 20:10:59 | 16.6021 | 16.855 | **−25.3¢** | 67,062 | $1,113,370 |
| 21:03:53 | 16.71 | 16.795 | **−8.5¢** | 32,443 | $542,123 |
| 20:00:10 | 16.71 | 16.575 | +13.5¢ | 14,546 | $243,064 |
| 12:54:39 | 17.00 | 17.475 (wide) | n/a | 10,832 | $184,144 |
| 20:00:10 | 16.71 | 16.575 | +13.5¢ | 6,152 | $102,800 |

**Net after-hours read = distribution-leaning.** The biggest two prints
both executed materially below NBBO mid — that's a seller hitting bids,
not a buyer. The two prints AT $16.71 above the day's narrower-spread
mid look like a different participant *buying* into the offer, but they
are <30% of the after-hours notional.

This is the principal **discordant note** vs the intraday block
accumulation: someone took $1.66M of shares off the offer in cash
session, then someone (potentially the same or different desk) sold
$1.66M post-close into a wide market. Net dollar-impact is ~zero, but
the *behavioural* read shifts from "pure accumulation" to "active
two-sided rotation".

### 5-day institutional price levels

`dark_pool_price_levels`, days=5 (2026-05-12 → 2026-05-18):

| Price | $ Premium | Shares | Trades | Distance from $16.50 |
|---|---|---|---|---|
| **$18.84** | $5,652,000 | 300,000 | 3 | +14.2% (overhead) |
| $16.48 | $3,490,464 | 211,800 | 3 | −0.1% (at spot) |
| $16.53 | $3,066,315 | 185,500 | 1 | +0.2% (at spot) |
| $18.82 | $2,939,691 | 156,202 | 3 | +14.1% (overhead) |
| $19.03 | $2,890,238 | 151,878 | 3 | +15.3% (overhead) |
| $18.91 | $2,834,144 | 149,858 | 1 | +14.6% (overhead) |
| $18.88 | $2,765,920 | 146,500 | 2 | +14.4% (overhead) |
| $18.80 | $2,763,548 | 147,000 | 3 | +13.9% (overhead) |
| $17.68 | $2,133,357 | 120,665 | 3 | +7.2% (overhead) |
| $18.41 | $1,977,961 | 107,452 | 2 | +11.6% (overhead) |
| $16.52 | $1,486,619 | 89,982 | 6 | +0.1% (at spot) |
| $17.45 | $1,444,219 | 82,787 | 1 | +5.8% (overhead) |
| $17.25 | $1,442,963 | 83,659 | 5 | +4.5% (overhead) |
| $16.55 | $1,405,095 | 84,900 | 6 | +0.3% (at spot) |
| $17.62 | $1,161,140 | 65,899 | 3 | +6.8% (overhead) |

**Aggregated by zone:**

| Zone | $ Premium | Total shares | Read |
|---|---|---|---|
| At-spot ($16.48–$16.55) | $8,948,493 | 567,182 | Working accumulation base |
| Mid ($17.25–$17.68) | $6,181,680 | 353,010 | Gap fill / supply absorbed |
| **Overhead ($18.41–$19.03)** | **$21,823,505** | 1,159,890 | **Heavy supply wall** |

The fact that $22M of dark-pool activity sits at $18.41–$19.03 over the
last 5 sessions tells us **the stock traded up there recently** and
either (a) institutions distributed at those levels, or (b) institutions
bought there and are now under water. Either way, that zone will absorb
upside flow when the stock attempts to retest. **First major upside
target = $17.45–$17.68 (gap-fill).** **Real resistance = $18.84.**

### Ticker-summary cross-check

FSLY does **not** appear in the market-wide DP top-30 (lowest entrant
CRWV at $827M premium). FSLY's $15M day-total is large relative to its
own historical baseline but small in absolute terms — phase 5 will need
to confirm whether $15M is unusually high for FSLY itself.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__dark_pool_largest` | symbol=FSLY, top_n=25, sort_by=premium, date=2026-05-18 | 25 prints; top 2 are paired $3M block buys at 15:12 |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=FSLY, top_n=30, min_tier=large, date=2026-05-18 | $15.04M total; block-tier buy_ratio 0.847; no mega trades |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=FSLY, top_n=15, date=2026-05-18 | 5 prints; largest two below NBBO mid (distribution) |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=FSLY, top_n=15, days=5, date=2026-05-18 | $18.84 = largest 5d cluster; $22M overhead supply at $18.41-$19.03 |
| `mcp__uw-pp__dark_pool_ticker_summary` | top_n=30, date=2026-05-18 | FSLY below top-30 cut; market-wide leader is MU |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** mixed-bullish (intraday accumulation
  confirmed; post-market and overhead supply temper conviction)
- **Conviction:** 3 / 5 — the block-tier buy_ratio is high but supported
  by only 3 trades; the overhead supply at $18.84 is the real ceiling.
- **Three S/R levels for phase-9 to use:**
  1. **$16.48 — primary support** (largest at-spot DP cluster, $3.49M /
     5d; aligns with intraday block buy print). A break below = thesis
     under pressure.
  2. **$17.45 – $17.68 — first upside target / pivot** (gap-fill zone,
     $3.6M of 5d DP across 4 levels). Bullish flow campaign should
     punch through this on the way up.
  3. **$18.84 — primary resistance / supply wall** (largest 5d cluster
     overhead, $5.65M; total $22M zone $18.41-$19.03). Trade plan must
     respect this as the realistic upside target before a major shelf.
- **Open questions:**
  - Was the 5/12-5/18 trading above $18 driven by a known catalyst
    (earnings, news), or technical squeeze? → phase 5 (historical),
    phase 6 (macro/catalyst calendar).
  - Is the $20 Jan'27 call write from phase-1 the same institution
    that distributed at $18.84? They would be naturally short ~$18-20
    upside if so. → phase 3 OI buildup at $20 strike will tell.
  - Has FSLY's 5-day DP premium of $15M today been a *step-up* vs the
    prior 30-session base, or normal? → phase 5 historical trend.
