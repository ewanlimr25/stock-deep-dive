# Phase 2 — Dark Pool & Block Prints

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **clean institutional accumulation**. The block tier (≥$1M, the
smart-money tier) is **95.3% buy** ($27.2M, 9 trades, 405,697 buy vs 20,000 sell
shares); whole-day aggressor split is **~64% buy by premium** ($47.5M above-mid/lifted
vs $27.2M below-mid/hit). The largest prints are **end-of-day / post-market blocks at
$64.03 (the close), printing ABOVE mid** — institutions paying up into the close,
including a **$9.6M post-market block** (149,967 sh, 17:36 ET). This DP accumulation
**confirms** phase-1's net-bullish call premium. Crucially, the §B cross-dataset join
finds **no underlying block within ±5 min** of phase-1's $2.5M 2027-06 $60 put
(16:26 ET) → that put is **not a married-put/collar** executed against a stock block;
treat it as standalone hedge/tail-protection, not a thesis-breaker. Bias:
**accumulation, conviction 4/5.**

## Key signals

- **Block tier 95.3% buy** — $27.2M, buy 405,697 sh vs sell 20,000 sh [DP:block_stratified]
- Whole-day DP **~64% buy by premium** ($47.5M vs $27.2M) [DP:aggressor_split DUCKDB]
- **$9.6M post-market block** @ $64.03, above mid (149,967 sh, 17:36 ET) [DP:largest]
- Big EOD blocks cluster at **$64.03** (close), all at/above mid — paying up [DP:largest]
- **No stock block within ±5 min of the $2.5M put** → not a married put [DP:ts_confirm DUCKDB]

## Detailed findings

### Largest blocks (today)

| Time (ET) | Price | Size | Premium | NBBO context |
|-----------|-------|------|---------|--------------|
| 17:36 (post) | $64.03 | 149,967 | **$9.60M** | +0.125 vs mid (buy-lean) |
| 16:00 (close) | $64.03 | 78,691 | $5.04M | +0.145 vs mid |
| 16:00 (close) | $64.03 | 50,309 | $3.22M | +0.145 vs mid |
| 16:41 (post) | $64.03 | 40,486 | $2.59M | +0.075 vs mid |
| 16:00 (close) | $64.03 | 25,200 | $1.61M | +0.145 vs mid |
| 09:47 | $62.81 | 25,125 | $1.58M | +0.075 vs mid |
| 10:03 | $63.585 | 20,000 | $1.27M | −0.035 (sell-lean) |

The institutional footprint is concentrated **at the close and post-market at $64.03**,
consistently above mid. Earlier pre-market prints were small ($0.1–0.17M) at ~$62 →
**institutions paid UP through the session** (pre-market $62 → close/post $64.03).

### Tier breakdown ([DP:block_stratified], single-day)

| Tier (boundary) | Premium | Trades | buy_ratio |
|-----------------|---------|--------|-----------|
| mega (≥$10M) | $0 | 0 | — (the $9.6M block lands in "block") |
| **block (≥$1M)** | **$27.21M** | 9 | **0.953** ← strong accumulation |
| large ($100K–$1M) | $47.49M | 267 | 0.552 (mild buy) |
| retail (<$100K) | — | — | — |
| **all tiers** | **$74.70M** | — | net buy-tilted |

Block-tier 0.953 is in the **high-confidence** band (>0.7). The large tier (0.552) is
only "suggestive," but the DuckDB whole-day aggressor split confirms the net: **64% buy
by premium, 63% by shares.**

### Price levels (5-session DP clusters, [DP:price_levels days=5])

| Level | Premium (5d) | Position vs spot ($64.03) |
|-------|--------------|---------------------------|
| **$64.03** | $22.7M | **at spot — today's close prints (pivot/resistance battle line)** |
| $62.34 | $35.7M | **support** (just below) |
| $61.11 / $61.10 | $17.4M | support |
| $60.62 | $2.8M | support |
| $56.03 | $2.6M | lower support |
| **$53.15** | **$48.4M (largest cluster)** | **major lower shelf** (well below) |
| $49.69 / $49.82 | $30.3M | deep support |
| $46.76 / $47.03 | $21.9M | deep support |

The heaviest historical shelf is **$53.15** ($48.4M) — a major accumulation floor from
when ENPH traded lower. Nearest actionable institutional support is **$62.34** then
**$61.11**; the spot battle line is **$64.03**.

### Extended-hours activity

The five largest blocks are flagged `extended_hours_trade` — but they print at **16:00
(closing cross) and 16:41/17:36 (post-market) at $64.03**, the day's settle. This is
**closing-auction + post-market institutional accumulation**, not an overnight
news-gap print (next earnings 2026-07-28, well away). One caveat: the $9.6M post-market
single block *could* be a portfolio/rebalance trade rather than directional intent —
de-rate slightly — but the 9-trade, 95% block buy ratio is robust to any single print.

### Cross-check of phase-1's $2.5M put ([DP:ts_confirm DUCKDB], §B)

Phase-1 flagged the day's largest options print — a **$2.5M 2027-06 $60 PUT** at
16:26:26 ET, `no_side`. The §B join returns **zero dark-pool prints within ±5 minutes**
of that timestamp. → It was **not** executed alongside a stock block, so it is **not a
married put / collar leg**. Most likely standalone long-dated downside protection (or
an options-structure leg). On a tape that is 3:1 call premium with 95%-buy block DP,
read it as **tail-hedge, not a distribution signal** — but phase 8b should still steelman
it as a possible institutional downside view.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol: ENPH, top_n: 25, sort_by: premium, date: 2026-05-22}` | EOD/post blocks at 64.03 above mid; $9.6M top |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol: ENPH, top_n: 30, min_tier: large, date: 2026-05-22}` | block tier 95.3% buy; total $74.7M |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol: ENPH, top_n: 15, date: 2026-05-22}` | big blocks at close/post @ 64.03; pre-market small @ ~62 |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol: ENPH, top_n: 15, days: 5, date: 2026-05-22}` | clusters 64.03 / 62.34 / 53.15 (major shelf) |
| DuckDB §B + aggressor | `dp-eod-report-2026-05-22.parquet` | no print ±5min of put; day 64% buy by premium |

*(`dark_pool_ticker_summary` not separately called — `insights_deep_dive` already
returned ENPH's DP summary: $74.7M / 1.18M sh / 276 trades @ avg $63.38, confirming
the same totals.)*

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Accumulation** (block tier 95% buy; day 64% buy; paying
  up into the close at $64.03).
- **Conviction:** **4/5** (block buy ratio is high-confidence; de-rated from 5 because
  the single biggest print is a post-market block that could be a portfolio trade, and
  accumulation is happening at elevated IV/price).
- **Three S/R levels for phase-9:**
  1. **Spot pivot / resistance: $64.03** (today's close, heavy DP prints — the battle line).
  2. **Support: $62.34** (recent DP cluster), then **$61.11** (stop-reference zone).
  3. **Major lower shelf: $53.15** ($48.4M cluster) — disaster-stop / re-accumulation floor.
- **Open questions:**
  - Does the EOD/post accumulation reflect a single buyer or broad demand? (size pattern
    suggests one program working the close — phase 3 OI build will corroborate intent.)
  - Is the $2.5M LEAP put a hedge on these very stock longs, or an independent bearish
    view? (→ phase 8b steelman.)
