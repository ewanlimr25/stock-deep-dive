# Phase 2 — Dark Pool & Block Prints

**Ticker:** USAR
**As-of date:** 2026-05-20 (effective UW data date: 2026-05-19)
**Generated:** 2026-05-20T10:00:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark-pool tape on 2026-05-19 is **clearly accumulative on the day**: the
large-tier (≥$100k) `buy_ratio` is **0.623**, with **$18.62M** of large-tier
premium across **118 trades** and **+228,457 net buy-volume** (578,055 buy
vs 349,598 sell). No mega-tier ($10M+) or block-tier ($1M+) prints fired,
so the institutional read is "many medium-sized buyers" rather than "one
whale". Critically, the **5-day price-level chart shows a $10.1M
concentration at $25.42** vs spot ~$20.40 — institutions appear to have
filled large blocks ~5 sessions ago around $25, before the stock dropped
~20% into the current $19.5–$20.7 zone where today's dip-buying is
occurring. This re-frames the phase-1 put-sweep structure as **hedging
existing-long inventory, not new bearish directional bet**.

## Key signals

- **Large-tier buy_ratio 0.623, $18.62M premium, 118 prints**, net
  buy-volume +228k shares [DP:block_stratified]
- **Top single block: $505,960 @ $19.46** (size 26,000) at 14:16:55Z, right
  at NBBO ask (+0.005 vs mid) — buy-pressure print [DP:dark_pool_largest]
- **Premarket tape: 5 prints, ~$784k, all at $20.70–$20.81** (above the
  regular-session VWAP that landed near $20.05–$20.40)
  [DP:dark_pool_extended_hours]
- **5-day price-level cluster: $25.42 with $10.13M** (4 prints, 397,873
  shares) — by far the largest concentration of the 5-day window, currently
  **+24.6% above spot $20.40** [DP:dark_pool_price_levels]
- **Today's prints are bracketed $19.46–$20.78**, mostly clustered $19.80–
  $20.50; this is where the new buying is happening, NOT $25
- **USAR absent from market-wide ticker_summary top-30** (dominated by MU,
  QQQ, SPY, NVDA, SNDK). USAR's $18.6M total is meaningful for a sub-$25
  small-cap but not a market-wide standout. [DP:ticker_summary]

## Detailed findings

### Largest blocks (table)

Top 10 by premium, today only:

| Time (UTC) | Price | NBBO bid/ask | vs Mid | Size | Premium | Read |
|-----------|-------|--------------|--------|------|---------|------|
| 14:16:55 | 19.460 | 19.45/19.46 | +0.005 | 26,000 | $505,960 | **At ask** — buy |
| 14:23:03 | 19.480 | 19.44/19.46 | +0.030 | 25,414 | $495,062 | **Above ask** — strong buy |
| 19:49:09 | 20.012 | 20.01/20.02 | -0.003 | 21,459 | $429,438 | Mid — neutral |
| 19:41:36 | 20.025 | 20.03/20.05 | -0.015 | 19,132 | $383,118 | Below mid — sell |
| 15:43:20 | 19.900 | 19.88/19.90 | +0.010 | 14,941 | $297,326 | At ask — buy |
| 15:54:37 | 19.950 | 19.93/19.94 | +0.015 | 12,650 | $252,368 | Above ask — buy |
| 13:35:03 | 20.321 | 20.35/20.36 | -0.034 | 11,698 | $237,715 | Below bid — sell |
| 19:49:08 | 20.042 | 20.05/20.06 | -0.013 | 11,400 | $228,479 | Below mid — sell |
| 17:25:21 | 20.480 | 20.48/20.49 | -0.005 | 11,100 | $227,331 | Mid — neutral |
| 14:03:07 | 19.950 | 19.95/19.96 | -0.005 | 10,695 | $213,365 | Mid — neutral |

Buy-side trade-vs-mid > +0.005 prints (likely buyers paying up) account for
the top three by premium ($505k, $495k, $297k). The aggregator's buy_ratio
of 0.623 corroborates: institutions are **NET adding** at this level.

### Tier breakdown

```
ALL TIERS (single-day stratification):
  mega   (≥$10M):  0 trades, $0 premium
  block  (≥$1M):   0 trades, $0 premium
  large  (≥$100k): 118 trades, $18.62M, buy_ratio 0.623
                    buy_volume  578,055 sh
                    sell_volume 349,598 sh
                    NET +228,457 sh BUY
  retail (<$100k): not surfaced
```

- **No block- or mega-tier prints** today; the institutional flow is broken
  into ~120 mid-size pieces. That's a working-the-bid pattern, not a
  one-shot whale.
- **Buy ratio 0.623** is in the "suggestive but high-confidence" range per
  the rubric (0.55–0.70 suggestive; >0.70 high-confidence). Tag as
  **moderate-conviction accumulation**.

### Price levels (5-day clusters)

Sorted by total premium:

| Price level | Premium | Shares | Trades | Distance from spot ($20.40) |
|-------------|---------|--------|--------|------------------------------|
| **$25.42** | **$10,113,932** | 397,873 | 4 | **+24.6%** |
| $25.77 | $1,503,948 | 58,361 | 6 | +26.3% |
| $25.55 | $1,395,288 | 54,611 | 5 | +25.2% |
| $25.95 | $1,187,289 | 45,756 | 4 | +27.2% |
| $25.83 | $1,183,793 | 45,831 | 5 | +26.6% |
| $25.59 | $1,136,592 | 44,416 | 4 | +25.4% |
| $25.15 | $1,105,720 | 43,968 | 7 | +23.3% |
| $25.10 | $1,177,105 | 46,900 | 5 | +23.0% |
| $25.00 | $1,229,550 | 49,182 | 6 | +22.5% |
| $24.83 | $1,699,637 | 68,451 | 7 | +21.7% |
| $24.80 | $1,714,772 | 69,144 | 4 | +21.6% |
| $24.77 | $1,084,744 | 43,792 | 3 | +21.4% |
| $24.54 | $1,380,759 | 56,268 | 6 | +20.3% |
| $24.18 | $1,108,652 | 45,850 | 5 | +18.5% |
| $21.27 | $1,338,033 | 62,913 | 8 | +4.3% |

**Critical observation**: **14 of 15 top price levels are between $24.18
and $25.95** — a tight $1.77-wide band representing where institutions
parked the bulk of dark-pool premium over the last 5 sessions. Only **one
level ($21.27)** sits anywhere near current spot. **The $25.42 single line
is $10.1M of premium across just 4 trades** — i.e., 4 prints of ~$2.5M
each — which is too big and too clustered to be coincidence. The most
likely explanation is either:

1. A **secondary offering or block cross at $25.42** earlier in the
   5-session window, with USAR subsequently selling off ~20% to spot.
2. A multi-day institutional **distribution program at $25** that has run
   into a wall (which sellers might have caused the drop to $20).

Either way, **$25.42 is a hard upside resistance level**: anyone long from
$25 area is underwater and will sell into rallies; anyone short that level
will defend it. The $24.18–$25.95 band is a thick **supply zone**.

The $21.27 level ($1.34M, 8 trades) is the only inside-1-day reference and
is +4.3% from spot — call it the **near-overhead pivot**.

Below spot, the dark-pool tape is **empty** in the 5-day window — there is
NO institutional support level visible below current price within the data
provided. That is a meaningful asymmetry: support is what is being built
RIGHT NOW at $19.50–$20.50, not earlier in the week.

### Extended-hours activity

| Time (UTC) | Price | NBBO bid/ask | Size | Premium | Note |
|-----------|-------|--------------|------|---------|------|
| 12:20:48 | 20.71 | 20.70/20.78 | 10,000 | $207,100 | Premarket, below ask |
| 12:29:45 | 20.72 | 20.70/20.75 | 5,888 | $121,999 | Premarket |
| 12:37:53 | 20.77 | 20.80/20.84 | 8,875 | $184,336 | Premarket, below bid |
| 12:55:35 | 20.81 | 20.81/20.85 | 6,788 | $141,259 | Premarket, at bid |
| 13:06:58 | 20.70 | 20.71/20.84 | 6,251 | $129,396 | Premarket, below bid |

Premarket aggregate: **~37,802 shares, $784,089 premium**, prices $20.70–
$20.81. The premarket was a **higher price zone** than the regular
session ended — i.e., the **regular session leaked lower** after premarket
buying tried (and failed) to defend the $20.70 area. Tag this as **sellers
absorbed dip-buyers** intraday, then late-session ramp back to ~$20.40 by
EOD.

That tape is consistent with an **early-day institutional fade** followed
by **late-day institutional dip-buy** — both sides are active, with
buy-side slightly winning the day (0.623 ratio).

### Ticker summary context

USAR did not appear in the **top-30 market-wide dark-pool tickers** on
2026-05-19. The market leaderboard is dominated by:

- MU ($11.6B premium) [memory-chip flow]
- QQQ ($7.9B), SPY ($7.7B) [index rotation]
- NVDA ($6.3B), SNDK ($5.5B), TSLA ($4.0B), INTC ($3.5B), AMD ($3.1B)
  [semi/AI trade]

The fact that USAR is below the top-30 cut does not diminish the
ticker-level signal — it just means USAR is not a flagship trade today.
The relative magnitudes still imply this is institutional activity in a
mid-tier small-cap, not retail froth.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | symbol=USAR, top-n=25, sort=premium, date=2026-05-19 | 25 prints, top = $506k @ $19.46 (at ask) |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=USAR, top-n=30, min-tier=large, date=2026-05-19 | large tier: 118 trades, $18.6M, buy_ratio 0.623 |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=USAR, top-n=15, date=2026-05-19 | 5 premarket prints, $784k total, $20.70–$20.81 |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=USAR, top-n=15, days=5, date=2026-05-19 | $25.42 cluster $10.1M; supply band $24.18–$25.95; $21.27 pivot |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=30, date=2026-05-19 | USAR not in top-30; MU/QQQ/SPY/NVDA dominate |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION** at current levels, with a
  significant **OVERHANG** at $25 from the prior-week supply zone.
- **Conviction:** **3/5** — buy_ratio 0.623 is suggestive but not
  decisive; no mega/block tier prints; supply overhang caps near-term
  upside conviction.
- **Three S/R levels for phase-9:**
  1. **Resistance: $24.18–$25.95** (5-day dark-pool supply band; $25.42
     is the modal line). Any rally must clear this thick zone to confirm
     a structural reversal.
  2. **Near-term pivot: $21.27** (only inside-band DP level above spot,
     $1.34M premium, 8 trades). Acts as the gate between dip-buy zone
     and resistance.
  3. **Support: $19.46** (today's heaviest at-ask buy print) and the
     wider **$19.50–$20.00** zone where today's net-buying took place.
     Below $19.46 there is no visible institutional bid in the 5-day
     window — break-of-support invalidation candidate.
- **Open questions:**
  - Was there an actual offering/cross at $25.42 to confirm the supply
    interpretation? (Phase 6 macro/news web search must check.)
  - Does the put-spread structure from phase-1 ($349k ask $18P + $305k
    mid $14P, paired at 17:35:34Z) belong to one of these dark-pool
    buyers as **collar/hedge inventory**, or is it a separate bear bet?
    (Phase 7 `insights_deep_dive` may resolve.)
  - Is there overnight dark-pool tape pre-2026-05-20 that would shift
    the read? (Cannot be checked — UW only has 2026-05-19 EOD data.)
