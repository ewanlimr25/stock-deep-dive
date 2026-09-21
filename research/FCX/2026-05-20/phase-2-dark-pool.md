# Phase 2 — Dark Pool & Block Prints

**Ticker:** FCX
**As-of date:** 2026-05-20 (effective data 2026-05-19)
**Generated:** 2026-05-20T19:40:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-1-flow.md`

## Summary

Dark pool today shows **mild net accumulation** — $48.85M total premium
across 222 prints, with **block-tier buy_ratio 0.69** ($6.55M) and large-tier
buy_ratio 0.601 ($42.3M) [DP:block_stratified]. Inferred net institutional
buy-pressure ≈ **$10–11M of equity** in one session (rough = (buy − sell) ×
tier premium summed across block + large). **No mega-tier prints** (nothing
≥ $10M single trade), so this is real-money positioning, not balance-sheet
hedging.

The day's narrative was **buyers paying up early, sellers showing late**:
the first two block prints of the day (14:13Z $1.54M @ mid and 14:43Z $1.01M
@ mid) executed alongside the bullish 65C July call sweep
[FLOW:options_flow_sweeps@phase-1] — suggesting the same institution may
have been pairing equity accumulation with leveraged upside. By the after-
session (18:27Z), the largest single print of the day printed BELOW NBBO mid
($2.03M @ $59.27 vs mid $59.275, trade_vs_mid = −$0.005) — likely a
distribution slice into market-on-close demand [DP:largest].

The **most important phase-2 datapoint is not today's flow at all** — it's
the 5-day dark-pool price-level map: cumulative institutional activity is
overwhelmingly concentrated at **$65.94–$68.50 ($170M+ across 6 levels)
versus only ~$26M at $60.50–$62.63** [DP:price_levels]. Spot at $59 is
**below the entire institutional positioning band**. This implies FCX has
**recently traded down from the $65–68 area into a value zone** — and the
Jul 65C call buyer in phase-1 may be betting on a return to the prior range
(not chasing a breakout, but anticipating mean-reversion to where
institutions were already established).

## Key signals

- **Block buy_ratio 0.69** ($6.55M, 4 prints) AND large buy_ratio 0.601
  ($42.3M, 218 prints) [DP:block_stratified] — coordinated mild accumulation
  across tiers.
- **Top 3 dark-pool prints by premium:** $2.03M @ $59.27 (sell, 18:27Z),
  $1.97M @ $59.69 ($0.05 above mid = BUY, 17:13Z), $1.54M @ $59.13 (mid,
  14:13Z) [DP:largest]. Net of the top-3 alone: ~$1.5M net buy.
- **Aggressive intraday bid:** the 13:31:56Z print at **$58.98** lifted NBBO
  bid by $0.28 above mid ($58.70 mid) — a $616k block print taken
  significantly through the mid, the most aggressive trade_vs_mid of the day
  [DP:largest].
- **5-day institutional concentration at $65.94/$65.97/$66.14/$67.16/$67.70/
  $68.50 = $256M+ total premium** [DP:price_levels] — every one of these is
  10–17% ABOVE current spot $59.13. This is the upside fair-value map.
- **Extended-hours: 1 print only**, $114k @ $59.95 pre-market
  [DP:extended_hours] — no overnight news-driven institutional reaction.

## Detailed findings

### Largest blocks — top-10 by premium [DP:largest]

| Time (UTC) | Price | NBBO mid | Δ vs mid | Size | Premium | Read |
|-----------|-------|----------|----------|------|---------|------|
| 18:27:40 | 59.27 | 59.275 | **−$0.005** | 34,200 | $2,027,034 | Late-day SELL slice |
| 17:13:03 | 59.69 | 59.645 | **+$0.047** | 33,000 | $1,969,839 | **Aggressive BUY** — paying $0.05 above mid |
| 14:13:33 | 59.13 | 59.130 | $0.000 | 26,100 | $1,543,293 | At-mid (paired w/ options sweep ~14:26Z) |
| 14:43:51 | 58.69 | 58.690 | $0.000 | 17,194 | $1,009,116 | At-mid |
| 17:51:52 | 59.41 | 59.375 | +$0.035 | 16,000 | $950,560 | BUY |
| 17:31:08 | 59.80 | 59.795 | +$0.005 | 11,400 | $681,720 | BUY |
| 15:45:17 | 58.91 | 58.930 | −$0.020 | 10,761 | $633,931 | SELL |
| 13:31:56 | 58.98 | 58.700 | **+$0.280** | 10,440 | $615,751 | **Most aggressive BUY of day** (28¢ through mid) |
| 14:13:33 | 59.205 | 59.130 | +$0.075 | 10,400 | $615,732 | BUY |
| 17:52:42 | 59.33 | 59.335 | −$0.005 | 10,095 | $598,936 | Marginal sell |

**Aggressive-buy total (above-mid prints in top-10):** $1.97M + $0.95M +
$0.68M + $0.62M + $0.62M ≈ **$4.84M of paying-up institutional buying**
across 5 prints. **Aggressive-sell total (below-mid):** $2.03M + $0.63M +
$0.60M ≈ **$3.26M of selling pressure**. **Top-10 net ≈ +$1.6M buy.**

Important nuance: the BIGGEST single trade (34,200 shares @ $59.27 at 18:27Z)
was a sell-side print, executed during the after-hours session window.

### Tier breakdown [DP:block_stratified]

| Tier | Threshold | Premium | Trades | Buy vol | Sell vol | **Buy ratio** |
|------|-----------|---------|--------|---------|----------|--------------|
| mega | ≥$10M | $0 | 0 | 0 | 0 | n/a |
| **block** | ≥$1M | **$6.55M** | **4** | 76,294 | 34,200 | **0.69** |
| **large** | ≥$100k | **$42.30M** | **218** | 430,022 | 285,448 | **0.601** |
| retail | <$100k | (excluded) | – | – | – | – |
| **TOTAL** | – | **$48.85M** | **222** | – | – | – |

- Block tier net = 76,294 − 34,200 = **+42,094 shares net buy** ≈ +$2.5M
- Large tier net = 430,022 − 285,448 = **+144,574 shares net buy** ≈ +$8.6M
  at avg ~$59.4
- **Combined inferred net dark-pool accumulation ≈ +$11M** on the day.

Heuristic threshold check: rubric says "Accumulation: mega buy_ratio ≥ 0.55
AND clusters ABOVE spot." There are **no mega-tier prints** today, so we
de-rate to "block tier 0.69 + large tier 0.60" — meets the **mild
accumulation** bar but not "high-confidence" (would need ≥ 0.70 sustained
across days, plus mega-tier).

### Price levels — 5-day institutional S/R map [DP:price_levels]

Dates covered: 2026-05-13 → 2026-05-19. **Sorted by cumulative premium:**

| Price | Premium | Shares | Trades | Position vs spot $59.13 |
|-------|---------|--------|--------|------------------------|
| **$65.97** | **$85.5M** | 1,295,598 | 6 | +11.6% — major resistance |
| **$65.94** | **$83.4M** | 1,264,959 | 3 | +11.5% — pairs with $65.97 |
| $67.16 | $25.2M | 374,818 | 21 | +13.6% |
| $68.50 | $23.4M | 341,748 | 2 | +15.8% |
| $66.14 | $22.1M | 333,538 | 25 | +11.9% |
| $67.70 | $17.1M | 251,924 | 3 | +14.5% |
| **$60.50** | **$11.3M** | 187,486 | 25 | +2.3% — near-term ceiling |
| $62.30 | $7.7M | 124,083 | 1 | +5.4% |
| $60.56 | $6.5M | 108,214 | 5 | +2.4% |
| $65.89 | $4.4M | 67,020 | 4 | +11.4% |
| $62.59 | $4.4M | 70,300 | 4 | +5.9% |
| $68.15 | $4.4M | 64,347 | 10 | +15.3% |
| $62.63 | $4.3M | 69,397 | 8 | +5.9% |
| $68.25 | $3.9M | 56,431 | 9 | +15.4% |
| $67.47 | $3.7M | 54,768 | 4 | +14.1% |

**Critical observation:** the price-level map shows ~$256M of cumulative
institutional activity stacked **between $65.89–$68.50** (12–16% above
current spot) and only ~$27M in the $60.50–$62.63 band closest to spot.
**Zero meaningful prints below $60.50** in this 5-day window.

This map is **not symmetric** around current price — it's heavily skewed up.
Two readings are possible:

1. **Recent decline from $65–68 → $59:** prior weeks saw heavy two-way action
   at $65–68 (when spot was up there); price has since slid, leaving residual
   institutional inventory marks above. **Phase 5 historical_trend must
   confirm.**
2. **Forward institutional target:** dark pool has been building "destination"
   positions at strikes 11–16% above current — consistent with the LEAP call
   buyers in phase-1 (100C Jan-28 print, 55C Jan-28 ITM call buy).

Either interpretation is **constructive for upside** — but reading #1 sets a
realistic 6–12-month target of $66, not a moonshot.

### Extended-hours [DP:extended_hours]

Single print: **2026-05-19 12:51:20Z, 1,900 shares @ $59.95, $113,905**.
NBBO ask $60.00 / bid $59.75; trade @ $59.95 is near-ask = a small buy. Not
material; no overnight institutional repositioning.

### FCX vs market-wide DP ranking [DP:ticker_summary]

FCX does **not** crack the top-50 dark-pool tickers by premium today (top-50
all > $400M; FCX at $48.85M). This is expected — FCX is a mid-cap ($90B
market cap, vs the ranking dominated by MU/QQQ/SPY/NVDA mega-cap names). The
**absence of FCX from the top-50 is not bearish**; it's structural. The
signal is the within-FCX tier ratios, not the market-cap-normalized rank.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | symbol=FCX, top_n=25, sort=premium, date=2026-05-19 | 25 prints; top = $2.03M sell @ $59.27 |
| `dark_pool_block_stratified` | symbol=FCX, top_n=30, min_tier=large, date=2026-05-19 | block buy_ratio 0.69 / large 0.601 / mega empty |
| `dark_pool_extended_hours` | symbol=FCX, top_n=15, date=2026-05-19 | 1 print, $114k pre-market — trivial |
| `dark_pool_price_levels` | symbol=FCX, days=5, top_n=15 | $256M stacked at $65.89–$68.50 |
| `dark_pool_ticker_summary` | top_n=50, date=2026-05-19 | FCX not in market-wide top-50 (mid-cap) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mild accumulation** (~$11M net buy today + 5-
  day map skews upside)
- **Conviction:** **3/5** — ratios are constructive but not extreme (block
  0.69 is good, not great; no mega-tier; biggest single print was a sell)
- **Three S/R levels for phase-9 to anchor entries/stops:**
  1. **Immediate ceiling: $60.50** — $11.3M / 25 trades, the first
     institutional shelf above spot (also the strike of the July 60C Jul-17
     block-buy in phase-1).
  2. **Intermediate: $62.30–$62.63** — $16.5M aggregate; if price breaks
     $60.50 this is the next stall zone.
  3. **Upside target: $65.94–$66.14** — $191M aggregate, the dominant
     institutional concentration cluster. **This is the gravity well the
     stock is mean-reverting toward** if the bull case plays out, AND it is
     exactly the strike chosen by the July 65C call buyer (no coincidence).
- **Downside floor:** no dark-pool prints below $58.65 in today's data. The
  absence of a clear lower shelf means phase-3 (pin risk) and phase-4 (gamma
  flip) must define the downside; dark-pool alone can't.
- **Open questions:**
  - What was FCX's recent high before the slide to $59? (phase 5
    `historical_trend`)
  - Was the $2.03M late-session sell @ $59.27 a one-off or part of a
    multi-day distribution pattern? (would require day-over-day DP
    comparison)
  - Does the 50% IV environment in phase-1 line up with the volatility regime
    FCX experienced during the $66 → $59 slide? (phase 5
    `historical_iv_percentile_zscore`)
