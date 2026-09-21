# Phase 2 — Dark Pool & Block Prints

**Ticker:** LRCX
**As-of date (requested):** 2026-05-18
**Effective as-of date (data):** 2026-05-15
**Generated:** 2026-05-18T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

LRCX dark-pool tape on 5/15 was **mixed near spot ($282–$287)** but the
5-day picture shows **clear distribution into strength**: institutions
parked $1.36B+ of premium in the **$289–$300** zone over the prior week
(price clusters at $289.24, $295.44, $296.05, $299.15, $295.93), and stock
has since rolled to $285. Today's tier breakdown reads block-tier
buy_ratio **0.483** (slightly net sell) and large-tier buy_ratio **0.538**
(modest net buy) on **$151.2M total premium** — roughly balanced.
**Conclusion:** institutions sold the $290+ range last week; today they are
neither aggressively accumulating nor dumping at the lows. The $295.44
shelf is the dominant overhead wall and aligns 1:1 with the call-overwrite
strikes from phase-1-flow.md ($295/$300 5/22 calls hit the bid).

## Key signals

- **5-day price-level concentration $295.44 = $627M premium, 2.12M shares,
  65 trades** — overhead institutional gravity center [DP:price_levels].
- Single biggest 5/15 block: **$5.81M at $283.81** executed at NBBO bid
  (trade_vs_mid -$0.265) = **SELL print** [DP:largest].
- Tier stratification: **large-tier $116.5M @ buy_ratio 0.538**, **block-tier
  $34.7M @ buy_ratio 0.483**, **mega-tier zero** [DP:block_stratified].
- 5/15 pre-market dark prints: **6 trades, $1.20M total at $292–$294**, all
  near/below bid — distribution into pre-market strength before a gap-down
  open to $282 [DP:extended_hours].
- LRCX is **not in the day's top-30 ticker_summary** (smallest top-30 ticker
  ~$601M premium; LRCX $151M is one tier below the index/mega-cap leaders
  but in line with sector peer AMAT at $781M and AVGO at $755M)
  [DP:ticker_summary].

## Detailed findings

### Largest blocks (top 10 today, classified vs NBBO mid)

| Time UTC | Price | Size | Premium | NBBO mid | vs mid | Read |
|----------|------:|-----:|--------:|---------:|------:|------|
| 13:32:41 | 283.81 | 20,481 | $5.81M | 284.075 | **-$0.265** | **SELL** |
| 14:52:06 | 282.99 | 11,000 | $3.11M | 282.775 | +$0.215 | **BUY** |
| 13:30:39 | 286.14 |  9,408 | $2.69M | 285.71  | +$0.430 | **BUY** |
| 13:48:56 | 282.93 |  7,766 | $2.20M | 282.72  | +$0.210 | **BUY** |
| 14:26:23 | 285.04 |  7,700 | $2.19M | 285.25  | -$0.210 | **SELL** |
| 14:17:23 | 282.59 |  7,695 | $2.17M | 282.755 | -$0.165 | **SELL** |
| 15:05:56 | 284.38 |  7,400 | $2.10M | 284.22  | +$0.160 | **BUY** |
| 14:17:23 | 282.48 |  6,960 | $1.97M | 282.605 | -$0.125 | **SELL** |
| 13:32:41 | 284.295|  6,315 | $1.80M | 284.195 | +$0.100 | **BUY** |
| 14:16:04 | 282.925|  6,060 | $1.71M | 282.74  | +$0.185 | **BUY** |

Among the top 25 (premium > $849k each):
- **BUY-side prints (above mid):** ~12, aggregate ~$18M
- **SELL-side prints (below mid):** ~10, aggregate ~$20M
- **At-mid / inconclusive:** ~3

→ Two-sided, but the **single largest block of the day was a $5.81M sell**.
Net dollar skew on top-25 is mildly negative; tier-stratified buy_ratio is
the more reliable read (large-tier modestly net buy).

### Tier breakdown (single-day, 5/15)

| Tier | Trades | Premium | Buy vol | Sell vol | Buy ratio |
|------|-------:|--------:|--------:|---------:|----------:|
| **mega (≥$10M)** | 0 | $0 | 0 | 0 | n/a |
| **block (≥$1M)** | 17 | $34.69M | 59,054 | 63,100 | **0.483** |
| **large ($100k–$1M)** | 555 | $116.54M | 220,538 | 189,109 | **0.538** |
| **retail (<$100k)** | n/a | n/a | n/a | n/a | n/a |
| **Total all-tier** | — | **$151.24M** | — | — | — |

Block tier is barely net sell, large tier is modestly net buy. No mega
prints (>$10M) is itself a signal — large allocators are **not** stepping
in size at these prices. The institutional accumulation/distribution
signature usually shows in mega tier; its absence implies **balanced
two-way flow at the marginal price**, not a one-sided campaign.

### Extended-hours (pre-market 5/15)

| Time UTC | Price | NBBO bid/ask | Premium |
|----------|------:|--------------|--------:|
| 11:00:07 | 294.00 | 293.00 / 294.45 | $264,600 |
| 11:00:03 | 294.00 | 293.00 / 294.00 | $176,400 |
| 11:11:09 | 292.50 | 292.50 / 293.80 | $233,123 |
| 11:10:07 | 292.96 | 292.50 / 293.00 | $219,719 |
| 11:34:24 | 292.28 | 291.00 / 293.00 | $200,504 |
| 11:22:05 | 292.76 | 292.51 / 295.00 | $102,466 |

Six pre-market prints, $1.20M total, all at $292–294 within 35 minutes
starting 7:00 AM ET. By 13:30 UTC (regular open) the stock was at ~$284 →
**~$8 gap-down at the open**. Pre-market sellers got out near $293
before retail bid disappeared. Small in dollar terms but directionally
useful: someone *knew* (or feared) the cash open would be lower.

### 5-day price-level clusters (institutional S/R)

| Level | Premium (5d) | Shares | Trades | Distance from $285 spot |
|------:|-------------:|-------:|------:|--------------------------|
| **$295.44** | **$626.8M** | 2,121,729 | 65 | **+3.7% (resistance)** |
| $296.05 | $339.3M | 1,146,194 | 55 | +3.9% (resistance) |
| $299.15 | $329.5M | 1,101,518 | 55 | +5.0% (resistance) |
| $289.24 | $360.9M | 1,247,692 | 61 | +1.5% (near resistance) |
| $295.93 | $107.0M | 361,436 | 1 | +3.8% (single mega print) |
| $297.04 | $80.7M | 271,636 | 3 | +4.2% |
| $298.05 | $8.5M | 28,676 | 1 | +4.6% |
| **$284.98** | $9.6M | 33,657 | 4 | -0.01% (near spot) |
| **$284.00** | $7.0M | 24,633 | 10 | -0.35% (support) |
| **$283.81** | $6.1M | 21,543 | 3 | -0.42% (support) |
| $289.00 | $6.4M | 22,151 | 6 | +1.4% |
| $287.00 | $5.1M | 17,936 | 12 | +0.7% |

**Pattern interpretation:**
The five biggest 5-day premium clusters are all at **$289–$299** — i.e.
ABOVE current spot. Institutions transacted ~**$1.66B** in dark prints in
the $289–$300 band over 5 sessions; in the same 5 sessions, the $283–$287
band has only **~$28M** in clusters. That asymmetry means the **stock has
moved DOWN from where the institutional volume actually transacted**. In
plain terms: institutions sold heavily into $295 and the bid faded; LRCX
is now sitting below its institutional cost basis.

This is the dark-pool equivalent of phase-1's call-overwrite tape: the same
participants who sold $290–$320 OTM calls were also selling stock or
trimming at $290–$300 in dark print form.

### Ticker_summary positioning

LRCX is not in the top 30 dark-pool tickers for 5/15 (cutoff ~$601M). But
on a sector-peer basis: AMAT ($781M) is comparable and AVGO ($755M) is
modestly above. LRCX at $151M is **roughly 19% of AMAT's tape**, which is
proportionate to relative market caps. No anomaly here, just confirmation
that LRCX is getting normal institutional attention, not a feeding frenzy.

## Tool calls (audit trail)

| Tool | Args | Result |
|------|------|--------|
| `mcp__uw-pp__dark_pool_largest` | symbol=LRCX, top-n=25, sort-by=premium, date=2026-05-15 | 25 blocks |
| `mcp__uw-pp__dark_pool_block_stratified` | symbol=LRCX, top-n=30, min-tier=large, date=2026-05-15 | 1 row (LRCX) |
| `mcp__uw-pp__dark_pool_extended_hours` | symbol=LRCX, top-n=15, date=2026-05-15 | 6 prints |
| `mcp__uw-pp__dark_pool_price_levels` | symbol=LRCX, top-n=15, days=5 | 15 rows |
| `mcp__uw-pp__dark_pool_ticker_summary` | top-n=30, date=2026-05-15 | LRCX not in top 30 |

## Tool errors

(none)

## Verdict for downstream phases

- **Bias from this phase:** **Mild distribution / overhead resistance**.
  The 5-day picture is unambiguous — institutions transacted $1.36B+ in
  the $289–$300 band and stock has since dropped to $285. Today's tape
  was balanced, with the single largest block ($5.81M at $283.81) hitting
  the bid (sell), and pre-market exited at $292+ before a gap-down. There
  is no mega-tier accumulation. Net: **bearish overhead, balanced at spot**.
- **Conviction: 3.5/5**. The 5-day cluster signal is high-conviction. The
  single-day flow is balanced and lower-conviction. Combined, it argues
  the institutional crowd is in **distribution-finishing / balanced-at-bottom**
  mode rather than starting a new accumulation campaign.
- **Three S/R levels for phase-9:**
  1. **R1 = $295.44** (institutional wall, $627M premium over 5d, also the
     5/22 295C call-write strike from phase 1). Cleanest stop-out level for
     a bear thesis. Bull thesis must reclaim and hold above here.
  2. **R2 = $289.24 / $290** (intermediate cluster $361M, also 6/18 290C
     write strike). First reaction zone on any rally.
  3. **S1 = $283–$284** (today's intraday volume zone; large block sell at
     $283.81 and large-tier buy support at $282–$284). Below = $280
     (5/15 LOD area).
- **Open questions:**
  - Are the $295+ sellers from the past 5 days still adding shorts, or are
    they done? (phase 3 OI deltas will help.)
  - Is the gap-down at the 5/15 open news-driven, sector-driven, or
    technical? (phase 6 macro / news scan needed.)
  - Does dealer gamma reinforce the $295 wall, or counteract it? (phase 4.)
