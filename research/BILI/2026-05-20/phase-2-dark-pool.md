# Phase 2 — Dark Pool & Block Prints

**Ticker:** BILI
**As-of date:** 2026-05-20 (data date 2026-05-19)
**Generated:** 2026-05-20T09:42:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark-pool tape is **accumulation at the block tier** with a slight selling tilt
at the large tier. Three block-class trades (≥$1M each) totaling **$5.91M /
307,752 shares cleared at a perfect 1.00 buy_ratio** — institutions paid at or
above NBBO mid for every block-sized print on the day. Total off-exchange
premium of **$19.73M** is meaningful for a sub-$5B mkt-cap ADR but did not
crack the top-30 market-wide ticker summary (which is dominated by mega-caps
and ETFs). Price-level clustering reveals a **5-day overhead supply zone at
$22.30–$22.45** ($10.5M / 469k shares) which lines up exactly with the 22.5
strike where the bearish put diagonal-roll lives (see phase-1-flow.md §Bearish
bloc).

## Key signals

- Block-tier buy_ratio **1.00** ($5.91M / 307,752 shares all at/above NBBO mid)
  [DP:block_stratified].
- Largest single print: **125,252 shares @ $19.65 = $2.46M at 17:22:58Z**,
  +$0.005 above mid → **buy** [DP:largest].
- 5-day institutional resistance cluster at **$22.34** ($8.23M, 368,615
  shares, 1 trade) — matches the 22.5 put strike from phase-1 [DP:price_levels].
- Today's primary accumulation level: **$19.65** — 189,972 shares across 8
  trades, $3.73M [DP:price_levels].
- Pre-market sold off to **$18.26** then institutional buyers absorbed the
  open at $18.82+ (see ext-hours table below) [DP:extended_hours].

## Detailed findings

### Largest blocks [DP:largest]

| Time (UTC) | Price | Size | Premium | NBBO mid | Trade-vs-mid | Read |
|---|---|---|---|---|---|---|
| 17:22:58 | $19.65 | 125,252 | **$2,461,202** | $19.645 | +$0.005 | **Buy at ask** |
| 13:32:03 | $18.82 | 105,700 | **$1,989,274** | $18.815 | +$0.005 | **Buy at ask** |
| 13:38:24 | $18.975 | 76,800 | **$1,457,280** | $18.975 | 0 | Mid (DP classifier: buy) |
| 16:29:42 | $19.20 | 49,199 | $944,621 | $19.365 | -$0.165 | Below-mid → sell |
| 13:45:50 | $19.75 | 21,100 | $416,725 | $19.760 | -$0.010 | Slight sell |
| 13:36:07 | $18.94 | 20,000 | $378,798 | $18.970 | -$0.030 | Sell |
| 13:32:29 | $18.75 | 19,200 | $360,000 | $18.830 | -$0.080 | Sell |
| 14:18:55 | $19.402 | 16,153 | $313,400 | $19.405 | -$0.003 | Mid |
| 13:33:46 | $19.09 | 16,206 | $309,373 | $19.095 | -$0.005 | Mid |
| 17:05:25 | $19.65 | 15,683 | $308,171 | $19.65 | 0 | Mid |
| 16:23:35 | $19.615 | 13,300 | $260,880 | $19.585 | **+$0.030** | **Buy above ask** |
| 17:00:16 | $19.55 | 12,600 | $246,330 | $19.565 | -$0.015 | Slight sell |

The three at-ask block prints ($2.46M / $1.99M / $1.46M) form the spine of the
day's institutional accumulation case. The biggest print (17:22 = 1:22 PM ET)
landed at $19.65, just below today's high of $19.95, after stock had recovered
from pre-market $18.26 lows — i.e. a chase-the-strength buy.

### Tier breakdown [DP:block_stratified]

| Tier | Total Premium | Trades | Buy Vol | Sell Vol | Buy Ratio |
|---|---|---|---|---|---|
| Mega (≥$10M) | $0 | 0 | 0 | 0 | n/a |
| **Block (≥$1M)** | **$5,907,756** | **3** | **307,752** | **0** | **1.00** |
| Large (≥$100k) | $13,820,275 | 77 | 332,579 | 382,910 | 0.465 |
| Retail (<$100k) | n/a (filtered) | — | — | — | — |
| **TOTAL** | **$19,728,031** | — | — | — | — |

Block-tier buy_ratio of 1.00 is the highest-conviction smart-money signal
available from this dataset. The large-tier 0.465 (slight sell) is noise
relative to the block-tier directional clarity — the size differential matters
(block trades are 4-10x larger per print).

### Price levels (5-day aggregation, 2026-05-13 → 2026-05-19) [DP:price_levels]

| Rank | Price Level | Premium | Shares | Trades | Distance to spot ($19.94) |
|---|---|---|---|---|---|
| 1 | **$22.34** | **$8,234,859** | 368,615 | 1 | **+12.0%** |
| 2 | **$19.65** | **$3,732,950** | 189,972 | 8 | **-1.5%** |
| 3 | $18.82 | $2,343,648 | 124,530 | 3 | -5.6% |
| 4 | **$22.45** | **$2,245,000** | 100,000 | 1 | **+12.6%** |
| 5 | $18.98 | $1,457,280 | 76,800 | 1 | -4.8% |
| 6 | $19.20 | $1,051,383 | 54,761 | 2 | -3.7% |
| 7 | $19.55 | $1,026,355 | 52,500 | 6 | -2.0% |
| 8 | $20.70 | $849,983 | 41,062 | 1 | +3.8% |
| 9 | $20.75 | $831,183 | 40,057 | 2 | +4.1% |
| 10 | $21.74 | $635,895 | 29,250 | 2 | +9.0% |
| 11 | $19.75 | $559,971 | 28,353 | 2 | -0.9% |
| 12 | $19.49 | $513,998 | 26,372 | 4 | -2.3% |
| 13 | $19.19 | $500,859 | 26,100 | 1 | -3.8% |

**Interpretation:**
- Levels with multi-trade signatures ($19.65 / 8, $19.55 / 6, $19.49 / 4)
  represent **iterative accumulation** in the current zone (-2% to spot) —
  classic "build position on a base" pattern.
- The two huge **single-trade** clusters at $22.34 ($8.2M) and $22.45 ($2.25M)
  almost certainly come from the week's prior session(s) when BILI was higher.
  Spot has since fallen ~12% off those prints. Whether those whales are now
  underwater longs (distribution risk on bounce) or shorts (resistance
  defended) cannot be resolved from DP alone; but **a 22.5-strike put roll
  with notional ~14k share-equivalents** (phase-1) sitting at the same level
  suggests at least *one* counter-party there is bearishly hedged.
- **$18.82 / $18.98 / $19.20** form a triple base 4-6% below spot — likely
  pre-market liquidity zone. Any retest into that band should see
  institutional buy interest.

### Extended-hours activity [DP:extended_hours]

| Time (UTC) | Price | Size | Premium | NBBO bid-ask | Direction |
|---|---|---|---|---|---|
| 12:32:37 | $18.811 | 9,900 | $186,229 | $18.79–$18.85 | At-mid |
| 12:34:24 | $18.8065 | 9,900 | $186,184 | $18.82–$18.85 | At-bid (sell) |
| 12:41:03 | $18.4365 | 9,900 | $182,521 | $18.43–$18.60 | At-bid (sell) |
| 12:45:58 | $18.60 | 9,685 | $180,141 | $18.60–$18.62 | At-bid (sell) |
| 13:27:08 | $18.2616 | 6,000 | $109,570 | $18.22–$18.37 | Near-bid (sell) |
| 13:27:05 | $18.26 | 6,000 | $109,560 | $18.22–$18.37 | Near-bid (sell) |

**Pre-market read:** ~$954k of ext-hours premium, all near or at bid =
**institutional selling overnight** that pushed price from $18.81 → $18.26.
Then at the regular-hours open (13:30Z = 9:30 ET) the **$1.99M block buy at
$18.82** absorbed the dip and reversed price action. This is the textbook
"shake out weak hands pre-market, accumulate at the open" institutional
signature.

### Ticker-rank context [DP:ticker_summary]

BILI did not place in the top-30 market-wide dark-pool ticker summary today.
The 30th-ranked SOXS had $608.8M in DP premium; BILI's $19.7M is ~3% of that
floor, consistent with a small-mid cap ADR. Treat conviction as **relative to
BILI's own baseline**, not the absolute market leaderboard.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `dark_pool_largest` | symbol=BILI, date=2026-05-19, top-n=25 | 25 BILI prints, top = $2.46M @ $19.65 |
| `dark_pool_block_stratified` | symbol=BILI, date=2026-05-19, min-tier=large | Block buy_ratio=1.00, Large 0.465 |
| `dark_pool_extended_hours` | symbol=BILI, date=2026-05-19 | 6 ext-hours prints, all near/at bid |
| `dark_pool_price_levels` | symbol=BILI, days=5 | $22.34 (1 print $8.2M) and $19.65 (8 prints $3.7M) lead |
| `dark_pool_ticker_summary` | date=2026-05-19, top-n=30 | BILI not in top-30 (sub $600M threshold) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Accumulation** (block-tier buy_ratio 1.00 is
  unambiguous; large-tier noise does not override).
- **Conviction:** **4 / 5** — three block-class buys totaling $5.9M, intraday
  ascending price absorption ($18.82 → $19.65 → $19.95), with classic
  pre-market shakeout → open-buy signature.
- **Three S/R levels for phase-9 to anchor:**
  1. **Support 1: $19.49–$19.65** (today's primary accumulation cluster,
     $5.3M / 268k shares across 18 trades within that band).
  2. **Support 2: $18.82–$18.98** (gap-fill / lower band, ~$3.8M / 201k
     shares — where the regular-hours opening block absorption occurred).
  3. **Resistance: $22.30–$22.50** (5-day institutional overhead cluster
     ~$10.5M + congruent 22.5-strike put-roll positioning from phase-1).
- **Open questions:**
  - Does the $22.34 single block of $8.2M represent a now-underwater long
    (overhang risk on a bounce) or an unwind/short (resistance defended)?
    → can only be partially resolved by phase-3 OI build and phase-5
    historical price/dark-pool trend.
  - Is the **block-tier accumulation aligned with the Jan-2027 $25 call
    sweep** from phase-1 (same institution buying both legs)? Phase-7
    `insights_institutional_accumulation` should be the arbiter.
  - Pre-market selling — was it discretionary (news-driven) or rebalancing?
    Phase-6 macro/news scan should check China ADR sector for catalyst.
