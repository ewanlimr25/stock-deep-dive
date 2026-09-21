# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool reads **ACCUMULATION — and directly contradicts the bearish options tape**.
Block-tier (≥$1M) prints are **100% buy-classified** ($13.95M, buy_ratio 1.0, zero sells)
and the large tier ($100K–$1M) is 70% buy. Over the last 5 sessions institutions have
repeatedly worked the **$10.50–$10.65 shelf** and the **$11.00** line. The single biggest
print is a **$9.84M, 900,000-share block @ $10.93** struck at the **4:00 PM close**, with a
second **$3.01M / 275K @ $10.94** at 4:12 PM — both above mid (lean-buy). **Caveat:** those
two dominant blocks are closing-auction / after-close prints, which *can* be benchmark
(MOC/VWAP) or index-rebalance flow rather than directional intent — so the accumulation
read is real but **de-rated for closing-print ambiguity**. Net: stock is being absorbed
near $11 while the options market hedges into the 05-28 earnings — the key tension of this
dive (flagged for phase-10).

## Key signals

- **Block tier 100% buy:** buy_ratio **1.0**, buy_volume 1,275,347 sh, sell 0, $13.95M, 3 trades [DP:block_stratified]
- **Large tier buy-lean:** buy_ratio **0.696**, $12.04M across 66 trades [DP:block_stratified]
- **Dominant block:** $9,837,000 = **900,000 sh @ $10.93** at 16:00:32 ET, trade_vs_mid **+0.02** (NBBO 10.83/10.99) — lean buy, closing cross [DP:largest]
- **5-day accumulation shelf $10.50–$10.65:** $10.52 ($4.60M/16 trades), $10.55 ($2.69M/18), $10.53 ($2.46M/14), $10.50 ($2.15M/13), $10.64 ($2.12M/14) — repeated institutional buying ~4–5% below spot [DP:price_levels]
- Today's total DP premium **$25.99M / 2,375,113 sh / 69 trades**, avg $10.95 (top-decile premium per phase-0.5) [DP:ticker_summary via insights_deep_dive]

## Detailed findings

### Largest blocks (NBBO context)

| Time (ET) | Price | Size | Premium | vs Mid | NBBO | Read |
|-----------|-------|------|---------|--------|------|------|
| 16:00:32 | 10.93 | 900,000 | $9.84M | +0.02 | 10.83/10.99 | **Closing cross**, lean-buy — possible benchmark/rebalance |
| 16:12:42 | 10.938 | 275,347 | $3.01M | +0.038 | 10.87/10.93 | After-close, above ask — buy |
| 12:51:52 | 10.9999 | 100,000 | $1.10M | +0.005 | at ask | Intraday buy at $11 |
| 09:37:09 | 11.00 | 56,025 | $0.62M | +0.005 | at ask | Buy at $11 |
| 13:00:13 | 10.9999 | 50,000 | $0.55M | +0.005 | at ask | Buy at $11 |

The intraday $11.00 prints (100K, 56K, 50K, 33.6K) are at-ask buys — genuine session
accumulation, not just the close. So the buy-lean is **not solely** a closing-auction
artifact: there is real intraday absorption at $11 too. That partially answers the
rebalance caveat — at least ~$2.3M of the block/large buying is intraday at-ask.

### Tier breakdown + buy/sell ratio

| Tier (boundary) | Premium | Trades | Buy ratio | Read |
|---|---|---|---|---|
| mega (≥$10M) | $0 | 0 | — | (the $9.84M block lands in *block*, just under $10M) |
| block (≥$1M) | $13.95M | 3 | **1.00** | High-confidence buy (>0.7) |
| large ($100K–$1M) | $12.04M | 66 | **0.696** | Suggestive buy (0.55–0.7 band edge) |
| retail (<$100K) | — | — | — | n/a |

Per the heuristic, block buy_ratio 1.0 is high-confidence accumulation; large 0.70 is at
the top of the "suggestive" band. Combined, **~$26M of off-exchange flow is buy-skewed**.

### Price levels (5-day institutional S/R)

Two regimes:
- **Spot battleground $10.89–$11.00** — $10.93 ($10.96M, inflated by today's 900K block),
  $11.00 ($3.54M/11 trades), $10.94 ($3.35M), $10.96 ($2.14M), $10.89 ($2.39M). Spot
  ($10.99) sits at the top of the DP range → **$11 is the near-term ceiling/battleground**.
- **Support shelf $10.38–$10.65** — a dense, high-trade-count cluster ($10.52/16,
  $10.55/18, $10.53/14, $10.50/13, $10.64/14, $10.59/5, $10.38/12). Repeated buying here
  over 5 sessions makes **$10.50–$10.65 the institutional support floor**; $10.38 the lower
  edge.

### Extended-hours activity

Six extended-hours prints, dominated by the two close blocks ($9.84M @ 900K, $3.01M @
275K) — both `extended_hours_trade`, both above NBBO mid. A pre-market $265K @ $10.62
(07:22 ET) and a $213K @ $10.69 (08:50 ET) round it out. The concentration of $12.8M+ at
the **4:00–4:12 PM close** is the flag: this *timing* is consistent with MOC/benchmark or a
late-May index-rebalance window, so treat the close blocks as **lower-conviction** than the
intraday at-ask buys. Cross-reference phase-6 for any 05-22 PATH news / rebalance event.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol: PATH, top_n: 25, sort_by: premium}` | #1 = 900K sh @ $10.93 $9.84M (close); intraday $11 buys |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol: PATH, min_tier: large, top_n: 30}` | block buy_ratio 1.0 ($13.95M); large 0.696 ($12.04M) |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol: PATH, top_n: 15}` | $12.8M concentrated at 4:00–4:12 PM close, above mid |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol: PATH, days: 5, top_n: 15}` | Support shelf $10.50–$10.65; ceiling $11.00 |

## Tool errors

None.

## Verdict for downstream

- **Institutional bias:** **ACCUMULATION** (buy-skewed, block tier 1.0 / large 0.70),
  de-rated for the closing-auction concentration of the two largest blocks.
- **Conviction:** **3/5** — strong buy ratio and a genuine intraday-at-ask component, but
  the dominant $12.8M is close/after-hours flow that may be benchmark/rebalance, not a
  thesis. The 5-day support shelf is the more reliable structural read.
- **Three S/R levels for phase-9:**
  1. **$10.50–$10.65** — primary institutional support shelf (5-day, high trade count) →
     natural stop reference / dip-buy zone.
  2. **$10.38** — secondary support / lower accumulation edge.
  3. **$11.00** — near-term ceiling & current battleground (heavy prints, spot capped here).
- **Open questions:**
  - **The core contradiction:** DP accumulating vs options tape 5-day bearish + put-heavy
    (phase-1). Is the put flow a *hedge on a growing long* (consistent with DP buying) or
    a genuine bearish bet (contradicts it)? → phase-3 OI must show whether puts are new
    longs or covered/spread, and whether call OI is building.
  - Were the 4:00 PM blocks index-rebalance / MOC? → phase-6 news check.
  - Does DP support at $10.50 align with an OI put wall / gamma level? → phase-3/4.
