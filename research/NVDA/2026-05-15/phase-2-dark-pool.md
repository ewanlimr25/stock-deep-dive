# Phase 2 — Dark Pool & Block Prints

**Ticker:** NVDA
**As-of date:** 2026-05-15
**Spot reference:** ~$228 (DP volume-weighted avg price $227.87)
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md
**Generated:** 2026-05-17T17:05Z

## Summary

NVDA was the **3rd-largest dark-pool name today** at **$8.01B premium across
33,318 trades**, behind only SPY and MU `[DP:ticker_summary]`. The picture
is **MIXED with a mild distribution lean in the mega tier**: the 5 mega-sized
trades printed buy_ratio = 0.421 (sell-heavy), while the larger and more
diversified "block" and "large" tiers were balanced-to-mildly-buying (0.507
and 0.548). Two clean **5-day institutional levels** stand out — strong
support at **$219–220** and stiff resistance at **$235–236** — both ~3.5–4%
from spot. Phase-1's bullish LEAP signature does NOT have a same-day DP
accumulation confirmation; mega-tier selling slightly conflicts.

## Key signals

- **Mega-tier sell skew:** 5 mega-tier trades, buy_ratio 0.421, $142M total
  premium `[DP:block_stratified]`. Sell volume 360k vs buy volume 263k.
- **Two 200k-share prints at the day's high tick:** $45.86M at $229.30
  (+$0.245 vs NBBO mid → **buy**) and $45.57M at $227.87 (-$0.18 vs mid →
  **sell**) `[DP:largest]`. Net: large institutions netted out near flat in
  the mega tier.
- **Major 5-day support cluster:** **$219.44** with $2.25B premium across
  10.27M shares, 262 trades `[DP:price_levels]`. Single largest institutional
  level in the recent window.
- **Major 5-day resistance cluster:** **$235.74** with $1.36B premium across
  5.75M shares `[DP:price_levels]`. Smaller than the support cluster but
  meaningfully sized.
- **Extended-hours pre-market selling:** $32M+ printed between 11:00–13:30
  UTC, walking the tape from $232 down to $225 `[DP:extended_hours]`.
  Suggests morning weakness setup that was bid through during the regular
  session.

## Detailed findings

### Largest blocks (top 10)

| Time (UTC) | Price | NBBO mid | vs mid | Size | Premium | Read |
|------------|-------|----------|--------|------|---------|------|
| 18:40 | $229.30 | $229.05 | +$0.245 | 200,000 | $45.86M | BUY |
| 17:06 | $227.87 | $228.05 | -$0.18 | 200,000 | $45.57M | SELL |
| 17:26 | $228.60 | $229.04 | -$0.44 | 100,000 | $22.86M | SELL |
| 13:45 | $226.20 | $226.13 | +$0.075 | 62,500 | $14.14M | BUY |
| 13:36 | $227.25 | $227.27 | -$0.02 | 60,624 | $13.78M | flat |
| 13:31 | $227.88 | $227.91 | -$0.025 | 41,880 | $9.54M | flat |
| 14:57 | $226.70 | $226.75 | -$0.045 | 35,831 | $8.12M | SELL-lean |
| 14:18 | $228.16 | $228.17 | -$0.005 | 35,000 | $7.99M | flat |
| 13:36 | $227.25 | $227.27 | -$0.02 | 28,368 | $6.45M | flat |
| 14:19 | $228.25 | $228.26 | -$0.01 | 26,928 | $6.15M | flat |

Mega-tier headline trades are net mildly distributive. Most of the rest is
within tight NBBO spreads — institutional VWAP-style execution, not
directional accumulation.

### Tier breakdown

| Tier | Trades | Premium | Buy vol | Sell vol | Buy ratio | Read |
|------|--------|---------|---------|----------|-----------|------|
| Mega (≥$10M) | 5 | $142.2M | 262.5k | 360.6k | **0.421** | SELL-leaning, small N |
| Block (≥$1M) | 673 | $1.05B | 2.33M | 2.27M | 0.507 | Balanced |
| Large (≥$100k) | 32,640 | $6.82B | 16.39M | 13.54M | **0.548** | Mildly BUYING |
| Retail | 0 | $0 | 0 | 0 | — | — |
| **Total** | 33,318 | **$8.01B** | — | — | — | — |

Note the divergence: mega is selling but the much larger "large" tier is
buying. Possible reads:
- Distribution from a single fund (mega) while many smaller institutions
  accumulate (large). Net mildly bullish ON BALANCE.
- Or, mega-tier sells are programmatic VWAP / rebalancing flows.

### Price levels (5-day aggregation)

| Level | Premium | Shares | Distance from spot ($228) | Role |
|-------|---------|--------|--------------------------|------|
| **$219.44** | $2.25B | 10.27M | -3.8% | **Major support** |
| **$235.74** | $1.36B | 5.75M | +3.4% | **Major resistance** |
| $225.83 | $1.27B | 5.62M | -1.0% | Near support |
| $220.78 | $858M | 3.89M | -3.2% | Secondary support |
| $227.03 | $160M | 706k | -0.4% | At-spot |
| $227.00 | $149M | 655k | -0.4% | At-spot |
| $235.00 | $96M | 408k | +3.1% | Resistance shelf |
| $226.00 | $91M | 401k | -0.9% | Near support |
| $219.29 | $86M | 393k | -3.8% | Support reinforcement |

**Three S/R levels for phase-9:**
1. **$219.44** — primary support (-3.8%, $2.25B in 5d)
2. **$235.74** — primary resistance (+3.4%, $1.36B in 5d)
3. **$225.83** — short stop area (-1.0%, $1.27B in 5d) — first place
   sellers would defend on a pullback

### Extended-hours activity (pre/post-market only)

15 extended-hours blocks, all printed between **08:00–13:45 UTC**
(pre-market). Prices walked from $233 (early) down to $225 (right before
open). Sizes 5k–16k. Total ~$32M. Most prints at slight discount to NBBO,
suggesting opportunistic selling into the morning bid.

No post-market activity (run is on a Friday after close — none expected).

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__dark_pool_largest` | `symbol=NVDA, date=2026-05-15, top-n=25` | 25 rows, top $45.86M |
| `mcp__uw-pp__dark_pool_block_stratified` | `symbol=NVDA, date=2026-05-15, top-n=30, min-tier=large` | 1 row (NVDA) with tier breakdown |
| `mcp__uw-pp__dark_pool_extended_hours` | `symbol=NVDA, date=2026-05-15, top-n=15` | 15 rows pre-market |
| `mcp__uw-pp__dark_pool_price_levels` | `symbol=NVDA, date=2026-05-15, top-n=15, days=5` | 15 levels aggregated 2026-05-11 → 05-15 |
| `mcp__uw-pp__dark_pool_ticker_summary` | `date=2026-05-15, top-n=30` | NVDA ranked #3 by premium |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** MIXED (mild distribution in mega; mild
  accumulation in large) — slight lean to neutral/distributive
- **Conviction:** 3/5 (large data, mixed signals)
- **Three S/R levels for phase-9:**
  1. $219.44 — major support (phase-9 stop reference)
  2. $235.74 — major resistance (phase-9 first profit target)
  3. $225.83 — short-term defense / tighter stop
- **Open questions for downstream:**
  - Phase-7 `insights_institutional_accumulation` and `conviction_matrix`
    should resolve whether this nets to ACCUMULATION, DISTRIBUTION, or
    NEUTRAL. Today the split is genuinely ambiguous.
  - Does phase-3 OI show pin formation at the at-spot $227 level, matching
    the small DP concentration at $227.00 / $227.03?
  - Does the large-tier buy bias persist over the 5-day window in phase-5
    `cumulative_premium_flow`? If yes, that's the structural bullish
    signature.
