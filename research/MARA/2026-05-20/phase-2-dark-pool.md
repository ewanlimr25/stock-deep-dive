# Phase 2 — Dark Pool & Block Prints

**Ticker:** MARA
**As-of date:** 2026-05-19
**Generated:** 2026-05-20T00:15:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Single-day dark-pool activity in MARA totals **$53.7M** across 274 trades —
material but not exceptional (MARA does not rank in the market-wide top-50
DP summary; cutoff for top-50 is ~$435M premium). Block-tier (≥$1M)
buy_ratio is **0.512** and large-tier (≥$100K) buy_ratio is **0.497** —
**balanced** flow on the raw split, but the *pattern of execution* is
bullish: the two largest block buys executed at the **lowest** intraday
prices ($11.75 and $12.40), while the two largest block sells happened at
mid-range prices ($12.10, $11.80). Multi-day 5-session price-level cluster
analysis shows institutional volume concentrated **above** today's close —
heaviest cluster at **$13.28** ($15.4M premium) — meaning the recent
institutional VWAP is ~$12.70, $0.30-$0.40 above today's $12.30-$12.44
close.

## Key signals

- Total DP premium today: **$53.7M** / 274 trades — meaningful flow [DP:dark_pool_block_stratified]
- Block tier (≥$1M): 4 prints, buy_ratio **0.512**, $7.25M premium [DP:dark_pool_block_stratified]
- Largest block: **210,000 shares @ $11.75 = $2.47M** at NBBO ASK side
  (trade_vs_mid +0.005) → institutional BUYER paid the offer [DP:dark_pool_largest]
- Top 5-day price cluster: **$13.28** with $15.4M / 1.16M shares across only
  7 trades → big-print "stash" level $1 above spot [DP:dark_pool_price_levels]
- Cluster ladder above spot ($13.28, $13.20, $13.00, $12.80, $12.65, $12.62)
  outweighs clusters at/below spot ($12.40, $12.10, $12.00, $11.91, $11.75) → 5-day
  institutional VWAP ~$12.70
- MARA NOT in market-wide DP top-50 — so 5/5 sweep persistence + $54M DP is
  ticker-specific activity, not market-wide flow

## Detailed findings

### Largest individual blocks (top 10)

| Time (UTC) | Price | Size | Premium | NBBO | trade_vs_mid | Read |
|------------|-------|------|---------|------|--------------|------|
| 13:51 | $11.75 | 210,000 | $2.47M | 11.74/11.75 | +0.005 (ASK) | **BUY** at intraday low |
| 16:43 | $12.10 | 183,293 | $2.22M | 12.10/12.11 | -0.005 (BID) | **SELL** mid-range |
| 13:41 | $11.80 | 112,500 | $1.33M | 11.81/11.82 | -0.015 (BID-) | **SELL** at low |
| 17:19 | $12.40 | 100,000 | $1.24M | 12.39/12.40 | +0.005 (ASK) | **BUY** mid-afternoon |
| 16:41 | $12.10 | 80,356 | $0.97M | 12.10/12.11 | -0.005 (BID) | **SELL** paired w/ 16:43 |
| 13:48 | $11.82 | 69,900 | $0.83M | 11.83/11.84 | -0.015 (BID-) | **SELL** opening |
| 17:40 | $12.33 | 57,394 | $0.71M | 12.33/12.34 | -0.005 (BID) | SELL |
| 14:24 | $11.66 | 58,384 | $0.68M | 11.65/11.66 | +0.005 (ASK) | **BUY** at intraday low |
| 13:54 | $11.90 | 54,200 | $0.64M | 11.89/11.90 | +0.005 (ASK) | **BUY** at low |
| 19:45 | $12.415 | 51,038 | $0.63M | 12.41/12.42 | 0 (MID) | Mid |

**Block-tier (≥$1M) net:** 2 buys (210k + 100k = 310k shares for $3.71M) vs
2 sells (183k + 112k = 295k shares for $3.55M) → +15k share net buy, +$0.16M
net premium. Razor-thin net BUY, but the **path matters**: buyers paid up at
the low-of-day ($11.75) early and at $12.40 later; sellers took bids at
$11.80-$12.10. Reads as **dip-buying with profit-taking on the lift**, not
distribution.

Adding the next tier ($0.5M-$1M, 6 prints in the top-25 list): another
~$3.6M with mix of buy/sell hits — the granular picture is "institutional
desk algo executing both sides, modestly buying the dip."

### Tier breakdown

| Tier | Premium | Trade count | Buy ratio | Read |
|------|---------|-------------|-----------|------|
| mega (≥$10M) | $0 | 0 | n/a | No mega prints today |
| block (≥$1M) | $7.25M | 4 | **0.512** | Marginally buy |
| large (≥$100K) | $46.46M | 270 | **0.497** | Balanced |
| retail (<$100K) | (excluded) | n/a | n/a | n/a |
| **Total** | **$53.71M** | 274 | 0.498 | **Balanced** raw |

No mega-tier (≥$10M) prints — institutional conviction today is sub-block
average. But cumulative $53.7M of large+block activity on a name that
doesn't appear in market-wide top-50 is itself a tell: this is *specific
positioning* in MARA, not index-driven flow.

### Multi-day price levels (5 sessions)

Top 15 institutional price clusters across 2026-05-13 → 2026-05-19:

| Rank | Price level | Total premium | Shares | Trades | Position vs spot ($12.30-$12.44) |
|------|-------------|---------------|--------|--------|------------------------------------|
| 1 | $13.28 | **$15.40M** | 1,159,674 | 7 | Resistance +6% above |
| 2 | $12.62 | $11.50M | 911,173 | 43 | Resistance +2% |
| 3 | $13.29 | $9.23M | 694,278 | 13 | Resistance +6% |
| 4 | $12.80 | $7.05M | 550,412 | 16 | Resistance +3-4% |
| 5 | $12.19 | $6.96M | 571,284 | 3 | Support −1% (low trade-count = single big print) |
| 6 | $13.00 | $6.78M | 521,200 | 6 | Resistance +5% |
| 7 | $11.91 | $6.63M | 556,806 | 10 | Support −3% |
| 8 | $12.65 | $5.38M | 425,175 | 16 | Resistance +2% |
| 9 | $12.59 | $5.22M | 414,711 | 33 | Resistance +2% |
| 10 | $12.10 | $4.92M | 406,387 | 10 | Support 0 to −2% |
| 11 | $13.20 | $4.74M | 359,100 | 12 | Resistance +6% |
| 12 | $12.51 | $4.62M | 369,654 | 16 | Pivot +1% |
| 13 | $12.00 | $4.47M | 372,464 | 14 | Support −2% |
| 14 | $12.60 | $4.47M | 354,727 | 23 | Resistance +2% |
| 15 | $12.40 | $4.41M | 355,790 | 13 | At spot |

**5-day institutional VWAP estimate** (premium-weighted across top 15 levels)
≈ **$12.74**. Today's $12.30-$12.44 close sits roughly **−$0.30 below**
this VWAP. Reads two ways:
- *Bullish:* institutions accumulated higher (at $12.60-$13.30); today's
  retracement is a discount.
- *Bearish:* institutions distributed at peaks and price is rolling lower —
  the $13.28/$13.29 dual-cluster looks like supply being unloaded ($24.6M
  combined across only 20 trades = single counterparty pattern).

**Tactical S/R for phase 9:**
- Hard resistance band: **$13.20-$13.29** (combined $29.4M institutional volume)
- Mid resistance: **$12.60-$12.80** (combined $28.4M)
- Pivot zone: **$12.40-$12.51** (combined $9.0M)
- First support: **$12.00-$12.19** (combined $16.4M, but #5 is single-print
  hedge — discount slightly)
- Lower support: **$11.91** (combined $6.6M) and **$11.75** (today's
  intraday buy block)

### Extended hours

Single print only:

| Time | Price | Size | Premium |
|------|-------|------|---------|
| 13:27 UTC (premarket, ~09:27 ET) | $11.84 | 9,840 | $116,518 |

Trivial. No overnight catalyst signature.

### Market-wide context

`dark_pool_ticker_summary` top-50 ranks MARA below the threshold (#50 is
~$435M; MARA today = $53.7M). For context, peers/leaders today:
- MU $11.6B, QQQ $7.9B, SPY $7.7B, NVDA $6.3B (top 4 are semis + index ETFs)
- No crypto/miner peer (CLSK, RIOT, WULF, IREN) appears in the top-50 either

→ MARA's $53M is not a sector-led move; it's idiosyncratic name flow.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol: MARA, date: 2026-05-19, top_n: 25, sort_by: premium}` | 25 prints, top is $2.47M @ $11.75 |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol: MARA, date: 2026-05-19, min_tier: large}` | block 0.512, large 0.497, total $53.7M |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol: MARA, date: 2026-05-19, top_n: 15}` | 1 print, $117K @ $11.84 |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol: MARA, date: 2026-05-19, days: 5, top_n: 15}` | 15 levels, top $13.28 ($15.4M) |
| `mcp__uw-pp__dark_pool_ticker_summary` | `{date: 2026-05-19, top_n: 50}` | MARA below threshold; sector peers absent |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** mixed-to-mildly bullish (balanced raw split, but
  intraday pattern is dip-buying with profit-taking)
- **Conviction:** 3/5 — flow magnitude is real and persistent but tier
  breakdown is essentially 50/50; no mega prints; below market-wide top-50.
- **Three things later phases must remember:**
  1. **5-day institutional VWAP ≈ $12.74**; today's close $12.30-$12.44 is
     below it. Use this as the "reversion target" in phase 9.
  2. **$13.20-$13.29 is hard resistance** — $29M institutional volume
     parked there over 5 sessions, mostly in low-count high-size prints
     consistent with distribution. Above this band, structure changes.
  3. **First support at $11.91 / $11.75** (today's algo buy point).
     Below $11.75 invalidates the dip-buying read and turns bias bearish.
- **Open questions:**
  - Are the $13.28/$13.29 mega-clusters (only 20 trades, $24.6M combined) a
    *single* institutional liquidation, or a working order? Phase 7
    (insights/accumulation) should help adjudicate.
  - Phase 1 flagged a 6P 2026-06-18 put with 1,503 contracts and 134% IV —
    that's a crash hedge. Does the DP tape show any sign of forced selling
    or a known holder distributing? (No evidence in today's tape; flag for
    phase 7.)
  - Phase 4 (GEX/flip): is the dealer gamma flip at or near $12.60 (the #2
    DP cluster)? A gamma-flip coinciding with $12.60 institutional pin would
    materially raise conviction.
