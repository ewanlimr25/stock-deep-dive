# Phase 2 — Dark Pool & Block Prints

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool shows **mild, suggestive accumulation** — not high-conviction.
Block-tier ($1M+) prints lean buy at **buy_ratio 0.653** ($33.8M, 10 trades), but
the broader large tier is balanced (0.523) and there are **no mega ($10M+) prints**
at all. The biggest single block (**50,000 sh @ $138.06, slightly above mid**) and
after-hours prints clustered at **$139.36 with the NBBO ask stretching to
$140.4–141.32** add a faint bullish lean the flat options tape (phase-1) lacked.
Net: institutions are quietly *following price up* into the 5/28 print, with a deep
5-day accumulation shelf at **$119–124** — but the footprint is too balanced to call
accumulation with conviction.

## Key signals

- **Block-tier buy_ratio 0.653** ($33.8M / 10 trades) — suggestive accumulation,
  but large-tier only 0.523 and **mega-tier empty** [DP:block_stratified]
- **Biggest block 50,000 sh @ $138.06 above mid (+$0.075)** at 18:04 — buy-ish [DP:largest]
- **After-hours demand:** $139.36 prints with NBBO ask reaching **$141.32**
  (bid 138.92) → post-close buyers reaching up [DP:extended_hours]
- **5-day institutional shelf $119–124** — biggest clusters by premium *and* trade
  count: $118.97 (16 trades), $123.95 (15 trades), $120.5–120.6 (several) [DP:price_levels]
- **Total DP premium $88.29M** across 278 prints — high *magnitude* (matches the
  31-session-high premium read from phase-0.5 `[CTX:]`), but balanced direction

## Detailed findings

### Largest blocks — `[DP:largest]`

| Time (UTC) | Price | Size | Premium | vs mid | Read |
|-----------|-------|------|---------|--------|------|
| 18:04 | 138.06 | 50,000 | $6.90M | +0.075 | **buy-ish (above mid)** |
| 13:54 | 134.665 | 50,475 | $6.80M | −0.005 | at mid (morning) |
| 14:14 | 134.06 | 41,400 | $5.55M | 0 | at mid (morning) |
| 13:53 | 134.00 | 25,000 | $3.35M | 0 | at mid |
| 18:03 | 138.215 | 18,360 | $2.54M | 0 | at mid (afternoon) |
| 16:10 | 138.91 | 13,000 | $1.81M | 0 | at mid |
| 13:30 | 125.00 | 4,956 | $0.62M | **−0.425** | outlier sell, below mid |

Big prints track the **intraday rally from ~$134 (morning) to ~$139 (close)** —
institutions paid mid-or-above as price rose. One odd $125 sell print at the open
is below-mid noise. No single dominant directional block.

### Tier breakdown — `[DP:block_stratified]`

| Tier (boundary) | Trades | Premium | Buy ratio | Read |
|-----------------|--------|---------|-----------|------|
| mega (≥$10M) | 0 | $0 | — | **no mega prints** |
| block (≥$1M) | 10 | $33.76M | **0.653** | suggestive buy (0.55–0.7 band) |
| large (≥$100K) | 268 | $54.52M | 0.523 | balanced |
| **all tiers** | — | **$88.29M** | — | high magnitude, mild buy lean |

Per the rubric, buy_ratio 0.653 is **suggestive only** (high-confidence needs
≥0.7). With no mega prints and a balanced large tier, this is mild accumulation,
not a conviction footprint.

### Price levels (5-session institutional S/R) — `[DP:price_levels]`

| Price | Premium | Trades | Zone vs spot (~$139) |
|-------|---------|--------|----------------------|
| 123.95 | $7.87M | 15 | **support shelf** (−11%) |
| 119.15 | $7.23M | 1 | deep support (−14%) |
| 118.97 | $6.45M | 16 | **support shelf** (−14%) |
| 120.5–120.6 | $5.9M+$2.97M+$2.82M | 2+5+8 | **support shelf** (−14%) |
| 134.00–134.67 | ~$13.3M | 2+4+1 | recent pivot (−3 to −4%) |
| 138.06 / 138.22 | $7.15M + $3.41M | 3+3 | **at spot** (today's blocks) |
| 139.36 | $3.32M | 11 | **at/above spot** (today's close) |

A heavy **$119–124 accumulation base** (high trade counts, built earlier in the
week at lower prices) underpins the name; **$134** is recent pivot support; today's
size printed **at $138–139.36**. Clusters are *below* and *at* spot — no clear
resistance shelf above, consistent with price discovery higher into the catalyst.

### Extended-hours activity — `[DP:extended_hours]`

All post-close (20:00 UTC = 16:00 ET) prints at **$139.36**, totalling ~$3.3M
across 11 prints, with NBBO **ask widening to $140.4 then $141.32** (bid 138.92).
Reads as **mild post-close buying interest reaching up** — but could be
closing-auction / passive flow; **de-rate to a faint bullish tell, not directional
conviction** (rubric: extended-hours can be rebalancing).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=NTAP, top_n=25, sort=premium | top block 50k @ 138.06 above mid |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=NTAP, top_n=30, min_tier=large | block buy 0.653, large 0.523, no mega |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=NTAP, top_n=15, days=5 | shelf $119–124; today's size $138–139 |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=NTAP, top_n=15 | $139.36 post-close, ask to $141.32 |

## Tool errors

None.

## Verdict for downstream phases

- **Net institutional bias:** **Mild accumulation / balanced.** Block-tier buy
  0.653 + biggest block above mid + AH demand lean bullish; large-tier 0.523 + no
  mega prints keep it suggestive, not conviction.
- **Conviction:** **2.5/5.** Adds a faint bullish lean the flat options tape
  (phase-1) lacked, but nowhere near a "smart money loading up" footprint.
- **Three S/R levels for phase-9 (entry/stop reference):**
  1. **$119–124** — major 5-day DP accumulation shelf → primary downside support /
     stop-reference zone.
  2. **$134** — recent pivot support (today's morning blocks, ~$13M).
  3. **$139–141** — spot / near-term resistance (today's close blocks + AH NBBO ask
     to $141.32). Note the 145C overwrite (phase-1) sits just above at +4%.
- **Open questions:** Is the $119–124 shelf old longs that will defend, or exited
  size? Does dealer positioning (phase-4 GEX) corroborate $140–145 as a supply
  ceiling? Is the mild block buying a hedge leg against the 145C overwrite, or
  standalone accumulation? Spot reference for all downstream phases: **~$139.36**.
