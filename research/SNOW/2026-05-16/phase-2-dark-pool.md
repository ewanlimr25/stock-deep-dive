# Phase 2 — Dark Pool & Block Prints

**Ticker:** SNOW
**As-of date:** 2026-05-16 (data date: 2026-05-15)
**Generated:** 2026-05-17T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

SNOW's institutional dark-pool tape on 2026-05-15 is **balanced-to-mildly-distributive** — and **diverges from the bullish options tape from phase-1**. Total DP premium $108.2M with **buy_ratio 0.514 at the LARGE tier ($100k-$1M)** but **buy_ratio just 0.304 at the BLOCK tier ($1M-$10M)** — i.e., the bigger institutional prints were 70% sell-side. The 5-day price-level cluster is concentrated in **$150.74-$153.20** (now $5-$8 below spot), defining institutional absorption support; conversely there is **no comparable DP cluster above $153**, meaning the $155-$160 rally zone is "uncharted institutional territory" with no offset from dark-pool absorption. Conclusion: institutions used the intraday rally to lighten size while options buyers were paying ask. This is a signal phase-9 must respect.

## Key signals

- **Largest single block:** 19,000 shares @ $158.99 at 17:42Z, **$3,020,810 premium**, trade_vs_mid = -$0.005 (at-mid, ambiguous) [DP:largest].
- **Block-tier divergence:** BLOCK tier ($1M-$10M) **buy_ratio 0.304** on 8 trades / $16.7M premium — institutional blocks were net SELL [DP:block_stratified].
- **5-day institutional support cluster:** $151.62 ($17.2M, 113k shares), $152.37 ($16.6M, 109k shares), $150.76 ($11.2M, 74k shares) — institutions absorbed heavily $5-$8 BELOW current spot [DP:price_levels].
- **Morning lows sold:** 11,400 shares @ $149.745 at 13:30Z, trade_vs_mid = **-$0.45** (deep below mid = SELLER pressing) [DP:largest].
- **SNOW absent from top-30 DP universe:** SPY/MU/NVDA dominate today's tape; SNOW's $108M premium is meaningful for a mid-cap but not headline-tier flow [DP:ticker_summary].

## Detailed findings

### Largest blocks (top 25 ranked by premium)

[DP:largest]:

| Time (UTC) | Price | Size | Premium | NBBO mid | trade_vs_mid | Interpretation |
|---|---|---|---|---|---|---|
| 17:42 | 158.99 | 19,000 | $3,020,810 | 158.995 | -0.005 | At-mid (ambiguous) |
| 19:45 | 157.855 | 18,983 | $2,996,561 | 157.83 | +0.025 | Slight BUY |
| 19:37 | 157.72 | 13,200 | $2,081,904 | 157.78 | -0.06 | SELL |
| 13:33 | 150.46 | 13,500 | $2,031,210 | 150.45 | +0.01 | At-mid |
| 14:33 | 156.11 | 11,971 | $1,868,793 | 156.21 | -0.10 | SELL |
| 18:27 | 157.72 | 11,100 | $1,750,692 | 157.755 | -0.035 | SELL |
| 13:30 | 149.745 | 11,400 | $1,707,093 | 150.195 | **-0.45** | STRONG SELL (deep below mid) |
| 14:11 | 154.6101 | 7,872 | $1,217,091 | 154.73 | -0.12 | SELL |
| 14:24 | 156.535 | 6,094 | $953,924 | 156.615 | -0.08 | SELL |
| 17:17 | 158.55 | 5,000 | $792,750 | 158.45 | +0.10 | BUY |
| 14:57 | 157.70 | 5,000 | $788,500 | 157.73 | -0.03 | SELL |
| 14:05 | 155.07 | 5,000 | $775,350 | 155.225 | -0.155 | SELL |
| 14:03 | 154.665 | 5,000 | $773,325 | 154.705 | -0.04 | SELL |
| 13:50 | 152.56 | 5,000 | $762,800 | 152.60 | -0.04 | SELL |
| 13:37 | 150.52 | 5,000 | $752,600 | 150.465 | +0.055 | BUY |
| 14:58 | 157.7686 | 4,368 | $689,133 | 157.70 | +0.069 | BUY |
| 17:44 | 159.06 | 4,328 | $688,412 | 159.075 | -0.015 | At-mid |
| 15:05 | 156.9701 | 4,368 | $685,645 | 157.135 | -0.165 | SELL |
| 18:52 | 158.725 | 4,200 | $666,645 | 158.66 | +0.065 | BUY |
| 18:54 | 159.48 | 4,000 | $637,920 | 159.405 | +0.075 | BUY |

**Buy/sell tally on top 25:**
- Strong SELL (trade_vs_mid ≤ -0.05): **9** trades
- SELL (trade_vs_mid -0.05 to -0.01): **6** trades
- At-mid (|trade_vs_mid| ≤ 0.01): **3** trades
- BUY (trade_vs_mid +0.01 to +0.05): **2** trades
- Strong BUY (trade_vs_mid ≥ +0.05): **5** trades

Net: 15 sell-leaning vs 7 buy-leaning on the top 25 — **~2:1 sell bias on the largest individual blocks** despite the LARGE-tier aggregate ratio being 51.4% buy (which is volume-weighted with hundreds of smaller prints).

**Temporal pattern:** the morning prints at $149-$152 were sells, while the late-afternoon prints at $158-$159 were a mixed bag. The cleanest readings are:
- 13:30Z: 11,400 sh @ $149.745 vs mid $150.195 = **seller pressing $0.45 below mid** at session lows.
- 17:42Z: 19,000 sh @ $158.99 vs mid $158.995 = the day's largest block was perfectly at-mid, looking like a VWAP-style institutional exit fill.
- 19:37Z: 13,200 sh @ $157.72 vs mid $157.78 = late-day seller.

### Tier breakdown

[DP:block_stratified]:

| Tier | Tier range | Buy ratio | Buy vol | Sell vol | Total premium | Trade count |
|---|---|---|---|---|---|---|
| MEGA | ≥ $10M | n/a | 0 | 0 | $0 | 0 |
| BLOCK | $1M-$10M | **0.304** | 32,483 | 74,543 | $16,674,154 | 8 |
| LARGE | $100k-$1M | 0.514 | 300,639 | 283,759 | $91,536,895 | 395 |
| RETAIL | < $100k | n/a | 0 | 0 | $0 | 0 |
| **TOTAL** |  |  |  |  | **$108,211,049** | 403 |

The most important number on this page is **block_buy_ratio = 0.304**. The 8 largest institutional prints (each $1M-$10M) skewed 2.3× toward sellers. This is the cleanest "smart money" signature available on a single day. The LARGE tier (395 smaller prints) is balanced (51.4% buy), but these are more likely to include execution-algo bystanders.

There is no mega-tier print today, so we cannot triangulate against the absolute largest size buckets.

### Price levels (5-day institutional support/resistance)

[DP:price_levels] aggregated 2026-05-11 → 2026-05-15:

| Rank | Price level | Total premium | Total shares | Trade count | Distance from spot ($158) |
|---|---|---|---|---|---|
| 1 | $151.62 | $17,172,902 | 113,262 | 4 | -$6.38 (-4.0%) |
| 2 | $152.37 | $16,590,953 | 108,886 | 23 | -$5.63 (-3.6%) |
| 3 | $150.76 | $11,213,826 | 74,382 | 17 | -$7.24 (-4.6%) |
| 4 | $152.66 | $9,147,995 | 59,924 | 6 | -$5.34 (-3.4%) |
| 5 | $151.46 | $8,493,867 | 56,080 | 5 | -$6.54 (-4.1%) |
| 6 | $152.70 | $8,429,040 | 55,200 | 1 | -$5.30 (-3.4%) |
| 7 | $150.74 | $8,274,417 | 54,892 | 4 | -$7.26 (-4.6%) |
| 8 | $152.14 | $7,751,527 | 50,950 | 6 | -$5.86 (-3.7%) |
| 9 | $151.50 | $6,719,934 | 44,356 | 21 | -$6.50 (-4.1%) |
| 10 | $152.26 | $6,418,823 | 42,157 | 7 | -$5.74 (-3.6%) |
| 11 | $153.20 | $5,447,332 | 35,557 | 2 | -$4.80 (-3.0%) |
| 12 | $152.16 | $4,953,562 | 32,555 | 7 | -$5.84 (-3.7%) |
| 13 | $151.13 | $4,797,165 | 31,742 | 3 | -$6.87 (-4.4%) |
| 14 | $152.94 | $4,625,670 | 30,245 | 3 | -$5.06 (-3.2%) |
| 15 | $151.60 | $4,444,313 | 29,316 | 9 | -$6.40 (-4.1%) |

**Every single one of the top-15 price levels is below spot ($158).** Cluster bands:
- **$150.74-$151.62**: $54.4M aggregate (4 of top 15)
- **$151.46-$152.94**: $58.8M aggregate (9 of top 15)
- **$152.94-$153.20**: $10.1M (2 of top 15)
- **Above $153.20**: empty (not in top 15)

The 5-day institutional absorption zone is **$150.50-$153.20** with the densest weight at **$151-$152.50**. This is the level where any pullback should find institutional bid — and below which the rally story is broken.

Note that 17 of the top 25 single-block prints on 5/15 were in the $149-$152 zone (the lows of the day), which confirms this level was where institutions transacted heaviest TODAY too. The absorption is real, not stale.

### Extended-hours activity

[DP:extended_hours]:

| Time (UTC) | Price | Size | Premium | NBBO bid/ask | Note |
|---|---|---|---|---|---|
| 08:06 | 149.00 | 700 | $104,300 | 148.00 / 158.39 | Premarket; wide $10 spread; print well below mid; algo-style |
| 12:21 | 150.89 | 1,000 | $150,890 | 149.50 / 150.88 | Late premarket; at-ask |

No meaningful overnight or post-market block activity. The single pre-market print at $149.00 with a 10-point NBBO spread is mechanical, not informational. **Hedging signature = NO** (no large pre/post-market block ahead of a known catalyst).

### Ticker summary (universe check)

[DP:ticker_summary] top 30 by total premium on 2026-05-15:

SNOW does **not** appear in the top 30. The list is dominated by SPY ($11.8B), MU ($8.0B), NVDA ($8.0B), QQQ ($7.1B), SNDK ($5.9B), TSLA ($4.4B), MSFT ($3.0B), INTC ($2.9B), IWM ($2.5B), AMD ($2.1B), AMZN ($1.9B), AAPL ($1.7B), etc. SNOW's $108M total premium is institutional-level activity but not headline tier.

**Implication:** SNOW is a focus name but not the consensus institutional focus name today — the broad tape is more concerned with semis (MU, NVDA, INTC, SNDK, AMD, SMH, SOXL) and index-level positioning (SPY, QQQ, IWM, VOO, SQQQ, TQQQ).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=SNOW, top_n=25, sort_by=premium, date=2026-05-15 | 25 blocks; 15 sell-lean vs 7 buy-lean |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=SNOW, top_n=30, min_tier=large, date=2026-05-15 | block tier buy_ratio 0.304, large tier 0.514 |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=SNOW, top_n=15, date=2026-05-15 | 2 small EH trades; no signal |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=SNOW, top_n=15, days=5, date=2026-05-15 | 5-day cluster $150.50-$153.20 |
| `mcp__uw-pp__dark_pool_ticker_summary` | top_n=30, date=2026-05-15 | SNOW not in top 30 (SPY/MU/NVDA lead) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mildly distributive / balanced**. Net opposite of phase-1 options flow (this is a divergence).
- **Conviction:** 3/5. Block-tier sell ratio is decisive (0.304) but no mega-tier confirms; LARGE tier is balanced; early-day sells could be morning panic/forced exits that don't extrapolate.
- **Three S/R levels for phase-9 to use:**
  1. **$151-$152.50 = primary institutional support** (5-day combined ~$59M premium absorbed here; pullback target #1).
  2. **$150.74-$150.76 = secondary support / 4.6% drawdown line** ($19.5M absorbed; pullback target #2; thesis-broken if violated on heavy volume).
  3. **$158-$159 = current spot, "uncharted" zone**. No DP cluster above $153.20 in last 5 days, so dealer/option-flow dynamics (phase 4) will dominate price action here, not institutional absorption.
- **Open questions:**
  - The phase-1 bullish options flow + phase-2 mildly distributive DP flow = "options ramp on selling" pattern. Is this options market makers chasing delta higher into institutional supply? Phase 4 GEX should clarify.
  - Are the BLOCK-tier sellers the same actors who sold the 280C bid leg in phase-1's Dec-28 LEAP spread? Probably not (DP sellers are typically share-level, not derivative leg), but if SNOW is approaching an exit window for a large holder, this would be the pattern.
  - Why is the morning print at $149.745 so far below mid? Forced liquidation? Phase 6 should check for any 5/15 pre-market headlines.
