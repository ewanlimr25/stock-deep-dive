# Phase 2 — Dark Pool & Block Prints

**Ticker:** CMPS
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool tells the **opposite-but-reconciling** story to the options tape:
institutions are **net BUYING** the stock today — large-tier `buy_ratio 0.839`
(120,058 buy vol vs 23,000 sell vol, $1.71M across 11 prints), with most blocks
executing **at or above NBBO mid** around $11.9–$12.1. Read against phase-1's net
call selling, the cleanest interpretation is a **buy-write / covered-call overwrite**:
accumulate shares off-exchange *and* sell the $11–$13 calls against the long for
premium — not distribution. The 5-day institutional footprint is concentrated
**below** today's $11.81 spot ($9.89–$11.45), i.e. the base built during the +26%
run; the only cluster at/above spot is today's $12.07 block ($413k) and a $12.20
sell. Net: **mild accumulation / range-build, capped at ~$12–13**, conviction tempered
by small absolute size (all "large" tier, no mega/block prints).

## Key signals

- Large-tier **buy_ratio 0.839** today (120,058 buy vs 23,000 sell vol), $1.71M / 11 prints `[DP:block_stratified]`.
- Largest block: **34,234 sh @ $12.07 ABOVE the $12.06 ask** (14:50), $413k — a paying-up buy `[DP:largest]`.
- Only 2 sells: 13,000 @ $12.20 (below $12.22 bid) and 10,000 @ $11.90 (below mid) — selling appears at/above $12.2 `[DP:largest]`.
- 5-day DP support shelves **below spot**: $10.86 ($1.19M), $10.56 ($1.16M), $11.45 ($1.03M) `[DP:price_levels]`.
- Extended-hours: one post-market buy, 9,706 sh @ $11.81 at 20:00Z (+$0.03 vs mid), $115k — modest after-hours accumulation, not a catalyst gap `[DP:extended_hours]`.

## Detailed findings

### Largest blocks (today) `[DP:largest]`

| time (Z) | size | price | NBBO (bid/ask) | vs mid | classify |
|----------|------|-------|----------------|--------|----------|
| 14:50 | 34,234 | $12.07 | 12.05 / 12.06 | +0.015 (above ask) | **BUY** |
| 19:02 | 17,700 | $11.76 | 11.74 / 11.76 | +0.01 (at ask) | **BUY** |
| 14:40 | 13,000 | $12.20 | 12.22 / 12.25 | −0.035 (below bid) | **SELL** |
| 17:08 | 11,805 | $11.94 | 11.92 / 11.94 | +0.0099 | **BUY** |
| 13:36 | 11,100 | $11.99 | 11.95 / 12.00 | +0.0149 | **BUY** |
| 14:31 | 10,000 | $12.005 | 12.00 / 12.01 | ~0 | neutral |
| 15:08 | 10,000 | $11.90 | 11.91 / 11.94 | −0.024 | **SELL** |
| 20:00 | 9,706 | $11.81 | 11.70 / 11.86 | +0.03 | BUY (ext-hrs) |
| 13:43 | 8,784 | $11.91 | 11.90 / 11.91 | +0.005 | BUY |
| 13:39 | 8,340 | $12.10 | 12.07 / 12.12 | +0.0051 | BUY |
| 14:15 | 8,389 | $11.996 | 11.96 / 12.00 | +0.016 | BUY |

**9 of 11 prints buy-classified.** The two sells are the highest-priced prints of the
day ($12.20, $11.90) — modest supply emerging into the $12.2 area, but overwhelmed by
buying at $11.8–$12.1.

### Tier breakdown `[DP:block_stratified]`

| Tier (boundary) | trade_count | total_premium | buy_ratio |
|-----------------|-------------|---------------|-----------|
| mega (≥$10M) | 0 | $0 | — |
| block (≥$1M) | 0 | $0 | — |
| large (≥$100k) | 11 | $1,713,847 | **0.839** |
| retail (<$100k) | 0 | — | — |

All institutional activity sits in the **large** tier — meaningful but not
mega-conviction. `buy_ratio 0.839` is in the high-confidence band (>0.7), but on only
11 prints, so treat as *suggestive accumulation*, not a high-N certainty. No mega/block
print means no single whale is driving this; it's distributed institutional buying.

### Price levels — institutional S/R (5-day, 2026-05-18→22) `[DP:price_levels]`

| price | 5-day premium | shares | vs spot ($11.81) |
|-------|--------------|--------|------------------|
| $10.86 | $1.19M | 109,217 | support (−8%) |
| $10.56 | $1.16M | 109,925 | support (−11%) |
| $11.45 | $1.03M | 90,115 | **nearest support (−3%)** |
| $10.15 | $0.93M | 92,074 | support |
| $10.07 / $10.10 | $0.77M / $0.61M | — | support cluster |
| $9.89 / $9.98 | $0.60M / $0.50M | — | deep support |
| **$12.07** | $0.41M | 34,234 | today's buy (+2%) |
| $11.78 / $11.71 | $0.39M / $0.29M | — | at-spot shelf |
| $11.50 | $0.33M | 28,806 | support |

The institutional footprint is **almost entirely below today's $11.81** — the shelves
at $10.56–$10.86 (~$1.2M each) are the heaviest, marking where the bulk of the run-up
accumulation occurred. $11.45 is the nearest support. The lone above-spot cluster is
today's $12.07 buy, which together with the $12.20 sell brackets the **$12.0–$12.2
supply zone**.

### Extended-hours `[DP:extended_hours]`

One post-market print: 9,706 sh @ $11.81, 20:00Z, +$0.03 vs mid, $115k, flagged
`extended_hours_trade`. Modest continuation buy, not an overnight catalyst block — no
gap signature. Nothing to attribute to news (defer to phase-6).

### Ticker-summary cross-check

`insights_deep_dive` (phase-0.5) corroborates: DP total_premium $1.71M / 143,058
shares / 11 trades / avg_price $11.97 — same dataset, consistent.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=CMPS, top_n=25, sort_by=premium | 11 prints; 9 buy / 2 sell; top = 34,234 @ $12.07 above ask |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=CMPS, min_tier=large | large-tier buy_ratio 0.839, $1.71M, no mega/block |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=CMPS, top_n=15 | 1 post-market buy, $115k @ $11.81 |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=CMPS, days=5, top_n=15 | Support $10.56–$11.45; supply $12.07–$12.20 |

## Tool errors

_None._

## Verdict for downstream phases

- **Institutional bias:** **mild ACCUMULATION** (buy_ratio 0.839 today). Critically,
  this **reconciles phase-1's call selling as a buy-write/overwrite**, not distribution:
  the stock is being bought while upside calls are sold against it. Net underlying read
  is constructive-but-capped, *not* bearish.
- **Conviction:** **3/5.** High buy_ratio but small N (11 prints, $1.71M, large-tier
  only). DP buy/sell is probabilistic; 0.839 > 0.7 is high-confidence on direction, but
  the dollar size is modest for a $1.56B-cap name — institutions are nibbling, not
  loading.
- **Three S/R levels for phase-9:**
  1. **Nearest support $11.45** (5-day DP shelf, $1.03M, −3% from spot).
  2. **Major support $10.56–$10.86** (heaviest base, ~$1.2M each, −8% to −11%) — the
     run-up accumulation zone; a logical stop-reference / invalidation floor.
  3. **Supply/resistance $12.0–$12.2** (today's $12.07 buy + $12.20 sell + the $13-call
     overwrite ceiling from phase-1) — the cap the buy-write defines.
- **Open questions for phases 3–4:**
  - Does **OI** confirm the $13/$11 calls are **sold-to-OPEN** (overwrite against this
    DP long, OI rises) vs longs closing (OI falls)? Decisive for the buy-write thesis. (phase 3)
  - Does **dealer gamma/GEX** pin price in the $11–12 zone (dealers long gamma from the
    sold calls → mean-reversion)? (phase 4)
  - Is the $12.2 supply a hard ceiling or just today's overwrite strike rolling up? (phase 3/4)
