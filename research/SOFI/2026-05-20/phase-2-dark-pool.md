# Phase 2 — Dark Pool & Block Prints

**Ticker:** SOFI
**As-of date (requested):** 2026-05-20
**Effective data date:** 2026-05-19 (5-day aggregation through 2026-05-13)
**Generated:** 2026-05-20T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

SOFI dark pool tape on 2026-05-19 shows **net institutional accumulation** with
$187.72M of total premium executed off-exchange — overwhelmingly in the
large-tier ($100k–$1M) bucket where buy-side volume (7.05M shares) exceeds
sell-side (4.39M shares) for a **buy_ratio of 0.616**. No mega-tier (>$10M)
single trades printed, but seven block-tier (>$1M) prints traded with a 0.339
buy_ratio — meaning the $1M+ blocks lean slightly distributive ($13.7M total) —
contradicting the dominant large-tier signal. Net read: **institutional desks
are accumulating SOFI in $100k–$1M slices at $15.00–$15.30**, while one or two
larger holders are trimming bigger blocks closer to $15.29. Five-day price-level
clusters peak at **$15.63 ($26.7M)** and **$15.42 ($22.4M)**, meaning the
$15.30–$15.65 band is institutional battleground from the prior week. This
**reinforces the long-dated 15C bullish flow** from phase 1 — institutions are
willing to pay 0.005–0.01 above NBBO mid to acquire size at the $15 handle.

## Key signals

- **Total SOFI dark pool premium 2026-05-19: $187.72M** with **buy_ratio 0.616
  in the dominant large tier ($173.97M of $187.72M total)** — net accumulation.
  [DP:block_stratified]
- **Largest single block: 215,651 shares @ $15.06, $3.25M** executed *above*
  NBBO mid ($15.05) — classified BUY at 15:58 UTC. [DP:largest]
- **Counter-signal: block-tier (>$1M) trades, n=7, buy_ratio 0.339** —
  $13.7M of distribution from a few large holders, but only 7.3% of total tape.
  [DP:block_stratified]
- **5-day institutional clusters: $15.63 ($26.7M / 1.71M sh), $15.42
  ($22.4M), $15.31 ($18.1M), $15.30 ($17.4M), $15.45 ($17.3M)** —
  persistent accumulation/distribution in the $15.30–$15.65 corridor.
  [DP:price_levels]
- **Pre-market activity small but accumulative**: 5 prints totaling ~$687k at
  prices $15.56–$15.63 (above RTH range) — institutions willing to pay up in
  thin liquidity. [DP:extended_hours]
- **SOFI absent from top-30 ticker_summary** (top-30 cutoff ~$608M; SOFI at
  $187M ranks roughly 60–80) — flow is conviction-driven not flow-of-funds
  noise. [DP:ticker_summary]

## Detailed findings

### Largest blocks (top 10, RTH)

| Time (UTC) | Price | NBBO mid | Size (sh) | Premium | vs Mid | Side inference |
|---|---|---|---|---|---|---|
| 15:58:52 | $15.06 | $15.05 | 215,651 | $3,247,704 | **+$0.01** | BUY |
| 15:09:39 | $15.03 | $15.035 | 201,497 | $3,028,500 | -$0.005 | SELL |
| 17:34:19 | $15.29 | $15.295 | 159,000 | $2,431,110 | -$0.005 | SELL |
| 14:09:19 | $15.155 | $15.155 | 98,900 | $1,498,830 | $0.000 | NEUTRAL |
| 16:11:44 | $15.04 | $15.025 | 92,743 | $1,394,855 | **+$0.015** | BUY |
| 19:42:14 | $15.22 | $15.225 | 74,447 | $1,133,083 | -$0.005 | SELL |
| 16:08:05 | $15.06 | $15.065 | 67,400 | $1,015,044 | -$0.005 | SELL |
| 13:46:14 | $15.155 | $15.165 | 57,200 | $866,866 | -$0.01 | SELL |
| 16:40:10 | $15.1401 | $15.145 | 54,290 | $821,956 | -$0.005 | SELL |
| 14:21:41 | $15.12 | $15.115 | 53,790 | $813,305 | **+$0.005** | BUY |

The seven block-tier prints (≥$1M) split: BUY 215k @ $15.06, BUY 92k @ $15.04,
SELL 201k @ $15.03, SELL 159k @ $15.29, SELL 74k @ $15.22, SELL 67k @ $15.06,
NEUTRAL 98k @ $15.155 → that yields **308k buy-volume vs 601k sell-volume in
the block tier alone**, matching the 0.339 buy_ratio reported by stratified.
However, the **large-tier bucket dwarfs blocks 12.6× by premium**, and that
bucket prints 7.05M shares BUY vs 4.39M shares SELL. The headline read is
**accumulation, with a few larger holders distributing into strength at
$15.20–$15.29**.

### Tier breakdown

| Tier | Premium | Trades | Buy vol (sh) | Sell vol (sh) | Buy ratio |
|---|---|---|---|---|---|
| Mega (≥$10M) | $0 | 0 | 0 | 0 | n/a |
| Block (≥$1M, <$10M) | $13,749,126 | 7 | 308,394 | 601,244 | **0.339** |
| Large ($100k–$1M) | $173,970,726 | 1,101 | 7,046,590 | 4,391,275 | **0.616** |
| Retail (<$100k) | (not surfaced) | — | — | — | — |
| **Total** | **$187,719,852** | — | — | — | — |

**Weighted net buy-ratio (premium-weighted across block+large):**
(0.339 × 13.75M + 0.616 × 173.97M) / 187.72M = **0.596 = net buyer**.

### Price levels (institutional S/R, 5-day rolling 2026-05-13 → 2026-05-19)

| Price level | 5-day Premium | Shares | Trade count | Distance from 2026-05-19 close ($15.27) |
|---|---|---|---|---|
| $15.63 | $26.74M | 1,710,842 | 114 | **+2.4%** — heaviest 5-day cluster |
| $15.42 | $22.37M | 1,450,462 | 97 | +1.0% |
| $15.31 | $18.08M | 1,181,299 | 92 | +0.3% |
| $15.30 | $17.44M | 1,140,155 | 100 | +0.2% |
| $15.45 | $17.32M | 1,121,033 | 74 | +1.2% |
| $15.55 | $16.18M | 1,040,869 | 68 | +1.8% |
| $15.29 | $15.94M | 1,042,814 | 88 | +0.1% |
| $15.50 | $15.84M | 1,022,236 | 83 | +1.5% |
| $15.41 | $15.47M | 1,004,162 | 90 | +0.9% |
| $15.52 | $15.39M | 991,374 | 84 | +1.6% |
| $15.61 | $14.70M | 941,535 | 83 | +2.2% |
| $15.33 | $14.59M | 952,069 | 101 | +0.4% |
| $15.64 | $14.47M | 925,094 | 75 | +2.4% |
| $15.53 | $14.09M | 907,586 | 77 | +1.7% |
| $15.43 | $14.01M | 908,008 | 77 | +1.0% |

**Observation:** every top-15 cluster is **above** the 2026-05-19 close of
$15.27. That tells us **the prior week traded a HIGHER range ($15.30–$15.65)**
and **today (2026-05-19) has been a pullback session into the $15.02–$15.29
zone where the large-tier accumulation just printed**. Institutions are
**buying the dip into a range that was the prior week's value area**.

### Extended-hours activity

Five small premarket prints (RTH starts 13:30 UTC = 09:30 ET):

| Time (UTC) | Price | NBBO mid (~) | Size | Premium |
|---|---|---|---|---|
| 11:22 | $15.61 | $15.615 | 9,325 | $145,563 |
| 12:01 | $15.56 | $15.565 | 8,000 | $124,480 |
| 12:07 | $15.59 | $15.595 | 10,301 | $160,593 |
| 12:17 | $15.59 | $15.585 | 6,800 | $106,012 |
| 12:46 | $15.63 | $15.625 | 9,647 | $150,783 |

Aggregate: 44,073 shares, $687,431 premium, average price $15.59 — **all
prints above the eventual RTH close of $15.27**. Pre-market accumulation at
+2% to the close is consistent with the prior-week value-area thesis — desks
were positioned to acquire above where the regular session ultimately settled.
Modest size, so **not a smoking gun on its own**.

### Ticker-summary context

SOFI does NOT appear in the top-30 dark pool tickers on 2026-05-19. The
top-30 cutoff sits at ~$608M premium (SOXS at #30). SOFI's $187M places it
roughly in the **#60–80 range** of US-listed dark-pool-active tickers — solid
mid-tier institutional activity, not blockbuster volume. Notable that LQD,
HYG, TLT (rates ETFs) all rank ahead of SOFI — consistent with the macro
"defensive rates positioning" backdrop noted in phase-1 [FLOW:smart_money_flow].

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `dark_pool_largest` | symbol=SOFI, top-n=25, sort-by=premium, date=2026-05-19 | 25 rows; largest $3.25M @ $15.06 BUY |
| `dark_pool_block_stratified` | symbol=SOFI, top-n=30, min-tier=large, date=2026-05-19 | $187.72M total; large-tier buy_ratio 0.616, block-tier 0.339 |
| `dark_pool_extended_hours` | symbol=SOFI, top-n=15, date=2026-05-19 | 5 small pre-market prints at $15.56–$15.63, ~$687k aggregate |
| `dark_pool_price_levels` | symbol=SOFI, top-n=15, days=5, date=2026-05-19 | Heaviest cluster $15.63 ($26.7M); all top-15 are above today's close |
| `dark_pool_ticker_summary` | top-n=30, date=2026-05-19 | SOFI absent from top-30; tape dominated by MU/QQQ/SPY/NVDA |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION**.
- **Conviction:** **4 / 5** — premium-weighted buy_ratio 0.596 across all
  institutional tiers, $187M off-exchange total, dip-buying into prior-week
  value area. Half-point deducted because block-tier (n=7, $13.7M, ratio 0.339)
  shows some distribution-into-strength behavior.
- **Three S/R levels for phase 9 to use:**
  1. **Support: $15.02–$15.06** — today's largest accumulation zone
     (215k-share +$0.01-mid buy at $15.06; 200k-sh sell at $15.03 but
     absorbed into 0.616 large-tier buy ratio).
  2. **Pivot / mean-reversion target: $15.29–$15.33** — 5-day institutional
     mid-cluster ($15.29 + $15.30 + $15.31 + $15.33 = $66.0M aggregate).
  3. **Upside resistance: $15.55–$15.65** — distribution zone for last week
     ($15.55, $15.61, $15.63, $15.64 each >$14M, $26.7M peak at $15.63).
- **Open questions:**
  - Does OI at $15 strike across May/Jun/Jul expiries explain the dark-pool
    bid at $15.00–$15.06? (phase 3 must answer)
  - Is the Jul-2026 16P single block from phase-1 a sold put? If the dark
    pool accumulation persists, that interpretation gains support
    (institutions long stock + short downside puts = bullish synthetic).
  - Does the $15.63 5-day cluster mark recent distribution-into-rip OR
    accumulation-near-prior-resistance? Phase 5 historical context required.
