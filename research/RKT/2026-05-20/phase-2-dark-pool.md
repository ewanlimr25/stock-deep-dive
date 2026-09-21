# Phase 2 — Dark Pool & Block Prints

**Ticker:** RKT
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:15:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

The dark pool tape is **net distribution at $12.52–$12.75**, not accumulation.
RKT printed $132.67M total dark-pool premium on 2026-05-19 stratified as
follows: **mega tier (≥$10M)** = 2 prints / $60.23M / 100% SELL classification;
**block tier (≥$1M)** = 9 prints / $21.90M / 11.1% buy (89% sell); **large
tier (≥$100k)** = 257 prints / $50.53M / 59.3% buy [DP:block_stratified].
That's the classic **distribution-to-smaller-hands** footprint: one or two
large holders unloading, broken up across many medium-sized institutions. The
biggest single print — **2.8M shares at $12.52 at 15:51 UTC for $35.06M** —
landed mid-tape after the morning gap and almost certainly funded a large
holder's exit. Combined with phase-1's observation that the morning options
package (Jul 12C + Dec 10P) executed at 14:10 UTC and the second-mega print
at 14:17 UTC hit at -$0.105 vs mid, the dominant institutional activity
today reads as **stock distribution paired with optional-replacement long
exposure**, not pure accumulation.

## Key signals

- **$60M of mega-tier sells, zero mega-tier buys** [DP:block_stratified].
  This single fact materially weakens the bullish-tilt read from phase-1.
- **2.8M shares @ $12.52 at 15:51 UTC ($35.06M)** — largest single print of
  the day, executed at the bid (trade vs mid = -$0.005) [DP:largest].
- **2.0M shares @ $12.60 at 14:17 UTC ($25.18M)** — executed at -$0.105 vs
  NBBO mid, an unambiguous large-seller print, **7 minutes after** the
  options package (Jul 12C + Dec 10P) hit at 14:10 [DP:largest, FLOW:top_premium_trades].
- **5-day price-level distribution clustered at $12.52 and $12.60 today,
  with multi-day clusters at $14.00, $14.25, $14.45** — institutions have
  been distributing from $14.x DOWN to ~$12.5 over the last 5 sessions
  [DP:price_levels].
- **Large tier (sub-$1M, sub-mega) is 59.3% buy** — the medium-bucket
  institutions ARE accumulating, which is what's powering the 5-session
  bullish-sweep persistence signal from phase-1 [DP:block_stratified,
  FLOW:sweep_persistence].

## Detailed findings

### Largest blocks (`mcp__uw-pp__dark_pool_largest`, top 25)

| # | Time (UTC) | Size | Price | NBBO mid | vs mid | Premium | Read |
|---|------------|------|-------|----------|--------|---------|------|
| 1 | 15:51:32 | 2,800,000 | 12.52 | 12.525 | -0.005 | **$35.06M** | At-bid mega print (sell) |
| 2 | 14:17:15 | 1,998,300 | 12.60 | 12.705 | -0.105 | **$25.18M** | -0.83% from mid — unambiguous large seller |
| 3 | 13:35:15 | 496,784 | 12.55 | 12.585 | -0.035 | $6.23M | Sell-leaning |
| 4 | 13:54:36 | 297,900 | 12.62 | 12.665 | -0.045 | $3.76M | Sell-leaning |
| 5 | 18:47:44 | 249,013 | 12.725 | 12.725 | 0.000 | $3.17M | At-mid (neutral) |
| 6 | 17:27:38 | 195,300 | 12.75 | 12.755 | -0.005 | $2.49M | At-bid |
| 7 | 14:34:15 | 116,531 | 12.705 | 12.715 | -0.010 | $1.48M | Sell-leaning |
| 8 | 16:55:39 | 100,000 | 12.85 | 12.855 | -0.005 | $1.29M | At-bid |
| 9 | 14:30:05 | 97,500 | 12.695 | 12.695 | 0.000 | $1.24M | At-mid |
| 10 | 16:36:32 | 94,200 | 12.80 | 12.795 | **+0.005** | $1.21M | At-ask (buy-leaning) |
| 11 | 16:48:57 | 81,209 | 12.785 | 12.795 | -0.010 | $1.04M | Sell-leaning |
| 12 | 17:00:22 | 75,000 | 12.85 | 12.855 | -0.005 | $0.96M | At-bid |
| 13 | 18:18:47 | 74,901 | 12.815 | 12.805 | **+0.010** | $0.96M | At-ask (buy) |
| 14 | 17:54:27 | 70,700 | 12.76 | 12.755 | **+0.005** | $0.90M | At-ask (buy) |
| 15 | 18:48:10 | 70,700 | 12.73 | 12.725 | **+0.005** | $0.90M | At-ask (buy) |

Tally of largest 25 by sign:
- At-bid / below-mid (sell-leaning): 19 of 25 prints
- At-ask / above-mid (buy-leaning): 4 of 25 prints
- At-mid (neutral): 2 of 25 prints

But the dollar concentration tilts even more heavily sell — the two megas at
the top account for $60.2M of the $132.7M total dark-pool premium.

### Tier breakdown (`mcp__uw-pp__dark_pool_block_stratified`)

| Tier | Trades | Total Premium | Buy Vol | Sell Vol | Buy Ratio | Read |
|------|--------|---------------|---------|----------|-----------|------|
| **MEGA** (≥$10M)  | 2   | **$60.23M** | 0          | 4,798,300 | **0.000** | Pure distribution |
| **BLOCK** (≥$1M)  | 9   | **$21.90M** | 191,700    | 1,536,737 | **0.111** | 89% sell |
| LARGE (≥$100k)    | 257 | $50.53M     | 2,361,387  | 1,619,963 | **0.593** | Modest accumulation |
| Retail (<$100k)   | 0   | $0          | 0          | 0         | n/a       | (no rows) |
| **TOTAL**         | 268 | **$132.67M** |           |           |           | Net distribution by dollars |

Interpretation: a one- or two-handed selling program executed at $12.52–$12.60
across two large mega-tier prints, with the offset absorbed by 257 medium
institutional buyers. Premium-weighted buy ratio across all tiers ≈ 0.302
(roughly two-thirds of dollar volume is sell-leaning by NBBO classification).

### Price levels (5-day, `mcp__uw-pp__dark_pool_price_levels`)

| Price Level | Premium | Shares | Trades | Distance from $12.86 spot |
|-------------|---------|--------|--------|--------------------------|
| **$12.52**  | $35.50M | 2,835,280 | 5 | -2.6% (today's distribution floor) |
| **$12.60**  | $25.28M | 2,006,337 | 2 | -2.0% |
| **$14.25**  | $22.98M | 1,612,585 | 8 | +10.8% (multi-day distribution from higher) |
| **$14.00**  | $14.63M | 1,044,919 | 6 | +8.9% |
| $12.73 | $7.28M | 571,894 | 19 | -1.0% (most-traded by count today) |
| $14.45 | $7.25M | 501,410 | 2 | +12.4% |
| $13.80 | $7.11M | 514,930 | 3 | +7.3% |
| $12.55 | $6.60M | 525,526 | 4 | -2.4% |
| $12.62 | $5.24M | 415,461 | 7 | -1.9% |
| $13.03 | $4.67M | 358,777 | 9 | +1.3% |
| $12.75 | $4.43M | 347,795 | 9 | -0.9% |
| $14.64 | $4.25M | 290,378 | 15 | +13.8% |
| $12.71 | $3.64M | 286,328 | 17 | -1.2% |
| $14.28 | $3.49M | 244,225 | 16 | +10.0% |
| $12.65 | $3.09M | 244,241 | 11 | -1.6% |

Two distribution clusters emerge:
- **Lower cluster: $12.52–$12.75** (today, ~$92M aggregate) = current
  distribution zone, also acts as short-term S/R band.
- **Upper cluster: $13.80–$14.64** (multi-day, ~$59M aggregate) = prior
  distribution from before the recent decline, now overhead resistance.

The 8 trades / $23M at exactly $14.25 across the 5-day window is the
single most-defended overhead level. This is where prior holders have been
trimming and is the first hard target for any bullish thesis to overcome.

### Extended-hours activity (`mcp__uw-pp__dark_pool_extended_hours`)

| Time (UTC) | Size | Price | NBBO bid/ask | Premium | Read |
|------------|------|-------|--------------|---------|------|
| 11:05:59 | 22,100 | $13.00 | 12.96 / 13.08 | $287,300 | Small pre-market lift print (above mid) |

Only one extended-hours block — too small to be a directional signal. A
$287k pre-market lift at $13.00 (top of the NBBO band) suggests a
single retail-priced fill, not institutional positioning. **No conviction
contribution.**

### Cross-reference against options-flow timestamps

| Time (UTC) | Options event | Dark-pool event |
|------------|---------------|-----------------|
| 14:10:09 | Jul 12C bought ask, $132k [FLOW:top_premium_trades] | — |
| 14:10:17 | Dec 10P bought ask, $356k [FLOW:top_premium_trades] | — |
| **14:17:15** | — | **Mega print: 1.998M shares @ $12.60 / -$0.105 vs mid, $25.18M [DP:largest]** |
| 14:30:05 | — | 97,500 @ mid $12.695 |
| 14:34:15 | — | 116,531 @ -$0.010 vs mid |
| 15:51:32 | — | **Mega print: 2.800M shares @ $12.52, $35.06M [DP:largest]** |
| 17:14:23 | Multiple Dec 13P bought ask, ~$420k cumulative [FLOW:top_premium_trades] | — |

Two strong inferences:
1. **The 14:10 options package preceded the 14:17 mega-sell by 7 minutes.**
   That sequencing is consistent with a single desk hedging-then-selling
   pattern: lay on the put protection and call replacement, then execute the
   stock liquidation. This is the classic **monetize-stock-but-keep-upside**
   structure used by family offices and PE positions that need to delever
   but believe in upside.
2. **The 17:14 Dec 13P buys came after the second mega-sell at 15:51.** The
   institution may have ADDED downside hedging after dropping the next 2.8M
   share block — consistent with continuing to lighten and protect.

### Ticker summary context (`mcp__uw-pp__dark_pool_ticker_summary`)

RKT is NOT in the top 30 dark-pool tickers by premium today (top 30 sits
between LITE at $772M and MU at $11.6B). RKT's $132.67M places it well
below mega-cap and ETF baseline — but in the context of a $12 stock with
~2B shares outstanding (Rocket common float), $132M dark-pool premium is
~0.5–1.5% of float traded in one session, which IS elevated. So RKT is a
"high-relative-activity" name even if it doesn't crack the absolute leader
board.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | `{symbol: RKT, top_n: 25, sort_by: premium, date: 2026-05-19}` | 25 prints; top two = $35.06M + $25.18M |
| `dark_pool_block_stratified` | `{symbol: RKT, top_n: 30, min_tier: large, date: 2026-05-19}` | $132.67M / mega 100% sell / block 89% sell / large 59% buy |
| `dark_pool_extended_hours` | `{symbol: RKT, top_n: 15, date: 2026-05-19}` | 1 print only ($287k @ $13.00 pre-market) |
| `dark_pool_price_levels` | `{symbol: RKT, top_n: 15, days: 5, date: 2026-05-19}` | $12.52, $12.60, $14.25 dominant levels |
| `dark_pool_ticker_summary` | `{top_n: 30, date: 2026-05-19}` | RKT not in top 30 (top dominated by MU/QQQ/SPY/NVDA) |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** distribution-leaning (mixed when adjusted for
  large-tier accumulation, but net dollar-weighted SELL)
- **Conviction:** 4/5 — the mega+block 100%/89% sell ratios are an explicit,
  not inferred, signal.
- **Three things later phases must remember:**
  1. **Phase-1 sweep persistence + phase-2 dark-pool distribution are
     contradictory** by surface read. The reconciliation that holds is the
     "stock-to-options conversion" structure: an institution is dropping
     stock at $12.52–$12.60 while replacing exposure with Jan-2027 12.2C
     LEAPS (delta 0.63). Phase-9 must explicitly flag this and decide
     whether to lean with the LEAPS buyer or with the stock seller.
  2. **Key S/R levels for the trade plan:**
     - **$12.52** is today's institutional distribution floor (immediate
       support; if it breaks, the next stop is $12.00 or lower).
     - **$12.73** is the most-traded level today (19 prints) — current pivot.
     - **$14.00–$14.25** is the major overhead distribution cluster — first
       upside target for any rally.
  3. **The two morning mega prints (14:17 and 15:51 UTC) were preceded by
     options structuring 7 minutes earlier.** This is a known smart-money
     sequence; the same desk likely controls both. Phase-3 (OI) should
     verify whether OI grew at the cited strikes (Jul 12C, Dec 10P,
     Jan-27 12.2C) on the 5/19 → 5/20 boundary to confirm the legs are
     opening, not closing.
- **Open questions:**
  - Is the stock seller a known PE / founder block (e.g., post-IPO lockup,
    family-trust quarterly liquidity)? Phase-6 / news check.
  - Does dealer GEX absorb a move toward $12.00 (i.e., are dealers short
    gamma below $12.50 such that further selling becomes self-reinforcing)?
    Phase-4.
  - Does the 5-day flow data show the LEAPS buyer increasing or static?
    Phase-5 historical OI trend.
