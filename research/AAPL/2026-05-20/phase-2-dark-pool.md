# Phase 2 — Dark Pool & Block Prints

**Ticker:** AAPL
**As-of date:** 2026-05-20
**Generated:** 2026-05-20T22:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark pool tape reads **strongly accumulative** on 2026-05-20. AAPL printed
**$2.49B total DP premium** (ranked ~10th in the market behind NVDA/SPY/MU)
on **8.26M shares** at avg $300.90 [DP:ticker_summary]. The mega-tier
(≥ $10M per print) shows a **buy ratio of 0.794** — i.e. roughly 4-to-1
buy-skewed institutional clearing — across 18 prints totaling $1.049B
[DP:block_stratified]. The signal is concentrated in a **post-close cluster
at $302.25** that includes a true after-hours buy of 762k shares at +$0.635
above NBBO mid. That cluster aligns within minutes of the **$54.1M ask-side
2028 300C LEAP sweep at 16:00:43 UTC** documented in phase-1-flow.md, so
dark pool confirms institutional accumulation on the day — adding weight to
the cash-equity leg of the LEAP buyer's package.

## Key signals

- **Mega-tier buy_ratio 0.794, $1.049B premium** across 18 prints
  [DP:block_stratified] — high-confidence institutional accumulation.
- **Largest single DP print: 816,028 sh @ $302.25 = $246.6M at 20:00:17 UTC**
  (+$0.045 above mid) [DP:largest]. Standard market-on-close auction print —
  size suggests one large institutional buy program.
- **True after-hours buy: 762,382 sh @ $302.25 = $230.4M at 21:30:40 UTC**
  (+$0.635 above mid = +21bp above NBBO) [DP:largest]. This is a genuine
  post-market aggressive buy — strongest directional signal of the day.
- **5-day DP cluster: $298.21 ($1.31B) and $297.84 ($1.13B)** = institutional
  support zone; **$302.25 ($1.18B)** = today's distribution/clearing print
  [DP:price_levels]. Sets up $297.84–$298.21 as primary support, $302.25
  as battleground.
- **Net buy volume across all tiers: large 2.10M vs 1.55M sell, block 691k
  vs 446k, mega 2.76M vs 715k** — every tier net long [DP:block_stratified].

## Detailed findings

### Largest blocks (top 10)

| Time (UTC) | Size | Price | Premium | NBBO mid | Trade vs mid |
|------------|------|-------|---------|----------|--------------|
| 20:00:17 | 816,028 | $302.25 | **$246.6M** | $302.205 | +$0.045 (above) |
| 21:30:40 | 762,382 | $302.25 | **$230.4M** | $301.615 | **+$0.635** (above mid by 21bp) |
| 20:00:06 | 386,500 | $302.25 | $116.8M | $302.275 | −$0.025 (at mid) |
| 20:00:27 | 206,140 | $302.25 | $62.3M | $302.15 | +$0.10 |
| 20:00:18 | 180,455 | $302.25 | $54.5M | $302.205 | +$0.045 |
| 20:00:32 | 179,538 | $302.25 | $54.3M | $302.15 | +$0.10 |
| 20:02:00 | 165,120 | $302.25 | $49.9M | $302.20 | +$0.05 |
| 20:00:33 | 148,650 | $302.25 | $44.9M | $302.15 | +$0.10 |
| 20:00:01 | 119,272 | $302.25 | $36.0M | $302.315 | −$0.065 |
| 20:00:07 | 98,675 | $302.25 | $29.8M | $302.275 | −$0.025 |

**Interpretation.** All 18 mega-tier prints cleared at the same price
**$302.25** within seconds of 20:00:00 UTC (16:00 ET market-on-close
auction) plus the one true after-hours print at 21:30:40 UTC. This is a
classic large institutional buy program: a single aggregated MOC order
plus a post-market top-up at +21bp aggression. Trade vs mid is mostly
positive (+$0.04 to +$0.10) and dominated by the +$0.635 after-hours
print — i.e. the buyer was lifting the offer.

### Tier breakdown (single day)

| Tier | Threshold | Trade count | Total premium | Buy vol | Sell vol | Buy ratio |
|------|-----------|-------------|---------------|---------|----------|-----------|
| **Mega** | ≥ $10M | 18 | **$1,048,864,323** | 2,755,182 | 715,006 | **0.794** |
| Block | ≥ $1M | 140 | $342,429,312 | 691,125 | 446,230 | 0.608 |
| Large | ≥ $100k | 5,027 | $1,099,282,551 | 2,105,614 | 1,548,073 | 0.576 |
| Retail | < $100k | 0 | $0 | 0 | 0 | 0.5 |
| **Total** | — | 5,185 | **$2,490,576,186** | — | — | — |

Mega tier 0.794 = **high-confidence accumulation** (rubric threshold for
"strong" is ≥ 0.55; 0.794 is well above the institutional-buy bar).

### Price levels (5-day aggregation, top 5)

| Price | Total premium (5d) | Total shares | Trades |
|-------|--------------------|--------------|--------|
| $298.21 | $1,305.6M | 4,378,041 | 168 |
| $302.25 | $1,179.4M | 3,902,066 | 157 |
| $297.84 | $1,128.1M | 3,787,487 | 150 |
| $297.00 | $163.5M | 550,601 | 42 |
| $297.14 | $139.3M | 468,794 | 28 |
| $300.23 | $138.3M | 460,574 | 47 |

**Cluster zones:** $297.00–$298.40 is a $2.7B 5-day institutional support
shelf; $302.25 is a $1.18B distribution zone built mostly today;
$300.00–$300.23 is a thinner pivot. **Implication for trade plan:** any
long entry should use $297.84–$298.21 as the primary risk anchor; any
breakout above $302.25 (with DP confirmation) targets a re-rate to the
LEAP-buyer's strike of $300+.

### Extended-hours activity

Of the top 15 DP prints today, **15/15 were tagged
`extended_hours_trade`** [DP:extended_hours]. The 20:00 UTC cluster is the
4 PM ET MOC auction — not strictly "after hours" in the directional sense.
But the **21:30:40 UTC** print (5:30 PM ET, true post-market) of **762,382
sh @ $302.25 at +$0.635 above mid** is the standout: aggressive
post-market accumulation, no news catalyst in the window (per the
top-premium options trade timestamps clustered at 16:00 UTC and the
overall day's flow profile). Treat as **directional**, not index/ETF
rebalance.

### Market context (ticker_summary)

| Rank | Ticker | Total DP premium |
|------|--------|------------------|
| 1 | NVDA | $10.55B |
| 2 | SPY | $9.90B |
| 3 | MU | $9.76B |
| 4 | QQQ | $5.53B |
| 5 | TSLA | $4.48B |
| ... | ... | ... |
| **10** | **AAPL** | **$2.49B** |

AAPL DP volume is normal-large for a mega-cap on a non-event day —
the signal is in the **tier mix and post-close aggression**, not in
the absolute rank.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol: AAPL, top-n: 25, sort-by: premium, date: 2026-05-20}` | Top 25 prints, 18 of them ≥ $10M, all at $302.25 |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol: AAPL, top-n: 30, min-tier: large, date: 2026-05-20}` | Mega buy_ratio 0.794 ($1.049B), block 0.608, large 0.576 |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol: AAPL, top-n: 15, date: 2026-05-20}` | All 15 are ext-hours; standout = 21:30:40 UTC 762k sh @ +$0.635 |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol: AAPL, top-n: 15, days: 5, date: 2026-05-20}` | $297.84/$298.21 support cluster, $302.25 distribution |
| `mcp__uw-pp__dark_pool_ticker_summary` | `{top-n: 30, date: 2026-05-20}` | AAPL rank 10, $2.49B total premium, avg $300.90 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **accumulation** (institutional buying).
- **Conviction:** 4 / 5. Mega-tier buy ratio of 0.794 is unambiguous; the
  $230M after-hours print at +21bp above mid is directional, not benchmark
  flow. Half-point off perfect because all of the mega activity is
  concentrated in one MOC + one AH window — single-window risk.
- **Three things later phases should remember:**
  1. **5-day institutional support cluster: $297.84–$298.21** ($2.4B
     combined DP premium across 5 sessions). Phase 9 should anchor stops
     just below $297.84.
  2. **$302.25 = today's clearing/distribution zone** (~$1.18B printed at
     exactly this price). Phase 9 must treat sustained closes above
     $302.25 as a confirmed accumulation breakout (DP-supported), and
     repeated rejections at $302.25 as the bearish 5-day sweep persistence
     winning.
  3. **DP confirms phase-1's $54M LEAP timestamp.** The largest option
     sweep crossed at 16:00:43 UTC; the biggest DP print cluster crossed
     16:00:01–16:00:36 UTC. Same actor/program is the natural inference.
- **Open questions:**
  - Is the 5-day bearish sweep persistence (phase-1) being driven by put
    buyers or call sellers? If sellers, DP accumulation is even more
    bullish (call sellers + DP buyers = covered-call income, not
    distribution).
  - Does phase-3 OI show a 2026-05-20 jump in AAPL share OI or in
    institutional 13F holdings disclosures that would corroborate the
    $1.05B mega-tier print?
