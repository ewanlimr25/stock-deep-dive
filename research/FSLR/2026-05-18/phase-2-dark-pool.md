# Phase 2 — Dark Pool & Block Prints

**Ticker:** FSLR
**As-of date:** 2026-05-18 (data anchor: 2026-05-15)
**Generated:** 2026-05-18T00:15:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

FSLR printed **$71.23M total dark-pool premium** on 2026-05-15 — a healthy
but unremarkable day for a ~$25B name. The tape rallied from a pre-market
$223.50 print to a 19:21 UTC $236.55 print — about a **+5.8% intraday move**
— and the dark pool absorbed that move on net: large-tier
(≥$100K) prints ran a **53.5% buy ratio across $61.0M of premium / 377
trades**, while the block tier (≥$1M, 6 trades, $10.24M) was dominated by
one 11,655-share seller at $231.03 (sweeping the bid) and shows only a
**17.5% buy ratio** in aggregate. No mega-tier (≥$10M) prints. Net read:
**moderate accumulation in mid-size lots underneath a one-name distribution
print**, consistent with rotation rather than panic. The biggest
institutional 5-day price clusters sit at **$231.62 ($17.5M premium) and
$219.95 ($16.7M, single block crossing trade)** — these become the phase-9
support anchors.

## Key signals

- **$2.69M sell-side block** at 15:57:43 UTC: 11,655 sh @ $231.03, executed
  AT the NBBO bid (trade_vs_mid = −$0.415) — single largest print of the
  day, distinctly distributive [DP:dark_pool_largest].
- **$1.82M buy-side block** at 17:34:35 UTC: 7,704 sh @ $235.87, executed
  **above** the NBBO ask of $235.57 (trade_vs_mid = +$0.47) — buyer paid up
  on the lift [DP:dark_pool_largest].
- Stratified tier breakdown: **large-tier buy_ratio = 0.535 on $61.0M
  premium across 377 trades** (mild accumulation); **block-tier buy_ratio
  = 0.175 on $10.24M / 6 trades** (sell-skewed) [DP:dark_pool_block_stratified].
- 5-day institutional S/R clusters: **$231.62 ($17.49M, 10 trades, 75.5K sh),
  $219.95 ($16.69M, 1 single block), $233.27 ($11.93M, 12 trades)** —
  high-trade-count clusters around $234 frame the consolidation zone
  [DP:dark_pool_price_levels].
- Pre-market: a single $360.7K block at $223.50 (1,614 sh, 12:06 UTC, between
  $223 bid / $224.47 ask) — modest, not a directional signal
  [DP:dark_pool_extended_hours].
- FSLR is **not** in the market-wide top-30 dark-pool tickers (top boards
  dominated by SPY at $11.76B, MU $8.0B, NVDA $8.0B, QQQ $7.1B) — FSLR's
  $71M is mid-cap-typical [DP:dark_pool_ticker_summary].

## Detailed findings

### Largest blocks (single-trade view)

Top-10 DP prints on 2026-05-15:

| Time (UTC) | Size | Price | NBBO mid | trade_vs_mid | Premium | Read |
|------------|------|-------|----------|--------------|---------|------|
| 15:57:43 | 11,655 | 231.03 | 231.445 | **−0.415** | $2.69M | **SELL** at bid; biggest distribution print |
| 17:34:35 |  7,704 | 235.87 | 235.40  | **+0.47**  | $1.82M | **BUY** above ask; biggest accumulation print |
| 19:21:43 |  7,600 | 236.55 | 236.635 | −0.085 | $1.80M | Near-mid, neutral |
| 19:43:24 |  5,990 | 236.96 | 237.04  | −0.08  | $1.42M | At-bid lean-sell |
| 15:53:52 |  5,702 | 232.01 | 232.43  | −0.42  | $1.32M | Sell, near 15:57 distribution |
| 13:43:20 |  5,280 | 224.50 | 224.755 | −0.255 | $1.19M | Early sell into pre-rally zone |
| 19:04:55 |  3,700 | 235.86 | 235.86  | 0.00   | $0.87M | Crossing, neutral |
| 19:11:09 |  3,100 | 236.79 | 236.73  | +0.06  | $0.73M | Lean-buy near highs |
| 14:44:54 |  3,063 | 232.445| 232.525 | −0.08  | $0.71M | Mid-zone neutral |
| 16:48:13 |  2,998 | 232.75 | 232.775 | −0.025 | $0.70M | Mid, neutral |

The intraday tape (chronologically): 13:43 $224.50 → 15:53 $232 →
15:57 $231 (one big seller) → 17:34 $235.87 (BUYER lifts above ask) →
19:21 $236.55 → 19:44 $236.39. The rally was real and the BUY block at
17:34 sat **above** the NBBO ask — that is paid-up accumulation, not
opportunistic mid-price hits. The 15:57 selling block is the only print
that fights the tape.

### Tier breakdown (single-day)

| Tier | Trades | Total premium | Buy vol | Sell vol | Buy ratio |
|------|--------|---------------|---------|----------|-----------|
| Mega (≥$10M) | 0 | $0 | 0 | 0 | n/a |
| Block (≥$1M) | 6 | **$10.24M** | 7,704 | 36,227 | **0.175** |
| Large (≥$100K) | 377 | **$60.99M** | 140,784 | 122,485 | **0.535** |
| Retail (<$100K) | 0 | $0 | 0 | 0 | n/a |
| **All tiers** | 383 | **$71.23M** | | | |

The block tier number is **almost entirely** explained by the single
11,655-share sell at $231.03 (which contributes 32% of all block-tier
sell volume). Strip that print and block tier flips to roughly balanced.
The persistent signal is the large-tier 0.535 buy ratio — broad,
377-print accumulation by mid-size accounts as price worked higher.

### Price levels (5-day institutional S/R)

Aggregated 2026-05-11 → 2026-05-15. Spot at session close ≈ $236.5.

| Rank | Level | 5d Premium | Shares | Trades | Distance vs $236.5 |
|------|-------|------------|--------|--------|-------------------|
| 1 | **$231.62** | $17.49M | 75,525 | 10 | −2.1% — **major support** |
| 2 | **$219.95** | $16.69M | 75,888 | **1** | −7.0% — single block crossing, lower-bound anchor |
| 3 | $233.27 | $11.93M | 51,148 | 12 | −1.4% — near-spot S |
| 4 | **$234.60** | $10.03M | 42,759 | **17** | −0.8% — **highest-conviction cluster (most trades)** |
| 5 | $234.90 | $8.32M | 35,434 | 12 | −0.7% |
| 6 | $235.29 | $6.52M | 27,731 | 2 | −0.5% |
| 7 | $236.53 | $6.37M | 26,922 | 2 | +0.0% — **at spot** |
| 8 | $234.54 | $6.18M | 26,332 | 3 | −0.8% |
| 9 | $224.92 | $6.11M | 27,146 | 2 | −4.9% |
| 10 | $228.06 | $5.12M | 22,449 | 16 | −3.6% — dense (16 trades) below |
| 11 | $235.78 | $4.97M | 21,097 | 3 | −0.3% |
| 12 | $235.75 | $4.44M | 18,851 | 5 | −0.3% |
| 13 | $227.91 | $4.06M | 17,817 | 2 | −3.6% |
| 14 | $237.00 | $3.42M | 14,446 | 5 | +0.2% — **first resistance shelf** |
| 15 | $231.44 | $3.25M | 14,025 | 4 | −2.1% — confirms $231 support |

**Interpretation:** Levels 3–6 + 8 + 11–12 form a tight institutional
acceptance band between **$233.27 and $235.78** (~$53M of 5-day premium).
Spot at $236.5 has just lifted to the top edge of that band; **$237** is
the highest level on the board with $3.4M premium — first resistance
shelf above is thin. **$231.62** below is the must-hold; lose it and
$224–228 zone is the air-gap landing area.

### Extended-hours activity

| Time (UTC) | Size | Price | NBBO | Premium | Read |
|------------|------|-------|------|---------|------|
| 12:06:02 (pre-market) | 1,614 | $223.50 | bid 223 / ask 224.47 | $360.7K | Modest pre-open print, near mid |

Single ext-hours print, near pre-market mid, not directional. Pre-market
spot was already at $223.50; by US open the stock rallied to $232+ on
regular-session prints. No after-hours blocks reported.

### Market-wide context (ticker summary)

FSLR's $71.23M does not crack the top-30 tickers by DP premium.
Reference points from 2026-05-15:
- SPY $11.76B, MU $8.05B, NVDA $8.01B, QQQ $7.11B dominate.
- Closest mid-cap analogs: NBIS $865M, LITE $829M, AMAT $781M.
- FSLR sits well below these — **the bigger-than-normal flow story is
  RELATIVE (5-day persistence + intraday rally absorption) rather than
  absolute size**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__dark_pool_largest` | `{symbol: FSLR, sort-by: premium, top-n: 25, date: 2026-05-15}` | 25 rows; biggest $2.69M sell at $231.03 |
| `mcp__uw-pp__dark_pool_block_stratified` | `{symbol: FSLR, min-tier: large, top-n: 30, date: 2026-05-15}` | 1 row: $71.23M total, block buy_ratio 0.175, large buy_ratio 0.535 |
| `mcp__uw-pp__dark_pool_extended_hours` | `{symbol: FSLR, top-n: 15, date: 2026-05-15}` | 1 pre-market print $360.7K @ $223.50 |
| `mcp__uw-pp__dark_pool_price_levels` | `{symbol: FSLR, top-n: 15, days: 5, date: 2026-05-15}` | 15 levels; top $231.62 ($17.5M) |
| `mcp__uw-pp__dark_pool_ticker_summary` | `{top-n: 30, date: 2026-05-15}` | FSLR not in top-30 (market dominated by SPY/MU/NVDA) |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mild accumulation** (large-tier buy_ratio 0.535
  on $61M / 377 trades, plus a $1.82M buyer paying **above** ask at $235.87).
  Block-tier 0.175 buy_ratio is bearish-looking but is dominated by one
  11,655-share sell that may be a single fund unwind, not a regime.
- **Conviction:** 3/5. The 53.5% large-tier buy is moderate, not strong
  (heuristic threshold for confident accumulation is 0.55+). What lifts
  conviction is the **intraday tape**: a +5.8% move was *absorbed*, not
  *rejected*, by the dark pool.
- **Three S/R levels for phase-9 to use as entry/stop reference:**
  1. **Support: $231.62** — biggest 5d cluster ($17.5M), aligns with the
     morning sell-zone; loss = end of constructive read.
  2. **Support: $234.50–235.30 acceptance band** — densest trade-count zone
     ($30M+ across $234.54, $234.60, $234.90, $235.29, $235.75); first
     "buy-the-dip" line.
  3. **Hard floor: $219.95** — single $16.7M crossing block; below this
     the institutional bid is unanchored.
  4. **Resistance: $237.00** — thinnest upper shelf ($3.4M); break invites
     air-gap higher with no DP overhead through ~$240+.
- **Open questions for downstream phases:**
  - Does dealer gamma flip below $232 to drive amplification on a pullback
    to $231 support? (→ phase-4 structure)
  - Is the 5-day $35.4M sweep premium [FLOW:hot_chains_sweep_persistence]
    consistent in direction with the DP large-tier 53.5% buy bias? Both
    look "mixed but constructive" — confluence forming.
  - Was the 11,655-share seller a known holder unwind (insider, 13F-tracked
    fund)? Out of scope here; macro phase may catch a corporate event.
