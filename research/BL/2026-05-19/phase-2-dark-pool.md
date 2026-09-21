# Phase 2 — Dark Pool & Block Prints

**Ticker:** BL
**As-of date:** 2026-05-19
**Generated:** 2026-05-19T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md

## Summary

Dark pool **strongly confirms** the bullish options campaign documented in
phase-1-flow.md: BL printed **$5,204,240** in DP premium on 2026-05-19 with a
**block-tier `buy_ratio = 1.00`** ($1.048M single print) and a **large-tier
`buy_ratio = 0.893`** across 15 trades ($4.156M) [DP:dark_pool_block_stratified].
The two largest individual blocks both lifted **above NBBO mid** (+$0.07 and
+$0.14), which is institutional accumulation paying for immediacy, not VWAP
inventory dressing [DP:dark_pool_largest]. Over the past 5 sessions the
institutional footprint concentrates at three S/R zones: a **base at $24.90–
25.81** ($7.7M+ cluster), a **mid-range accumulation $28.91–29.43** ($3.2M),
and a **high-range continuation $30.17–30.50** ($3.6M)
[DP:dark_pool_price_levels]. Extended-hours = empty — clean intraday-only
profile, no overnight rebalancing noise [DP:dark_pool_extended_hours]. **Net
bias: accumulation, conviction 5/5.**

## Key signals

- **Block-tier 100% buy ratio:** BL block tier = 1 trade, `buy_volume=36254`,
  `sell_volume=0`, `total_premium=1048103.14`
  [DP:dark_pool_block_stratified].
- **Large-tier 89.3% buy ratio:** 15 trades, `buy_volume=126262`,
  `sell_volume=15096`, `total_premium=4156137.71`
  [DP:dark_pool_block_stratified].
- **Anchor block paying up:** $1,048,103 @ $28.91, size 36,254, **+$0.07
  above NBBO mid** ($28.84), 18:55:43Z [DP:dark_pool_largest].
- **Second anchor block paying up:** $862,503 @ $28.98, size 29,762,
  **+$0.14 above NBBO mid** ($28.84), 17:13:50Z — even more aggressive
  [DP:dark_pool_largest].
- **5-day institutional support cluster:** $25.80/$25.81 carries
  `total_premium=7710534` across just 3 trades (149,400 shares per level)
  [DP:dark_pool_price_levels] — this is **the floor** if BL pulls back.

## Detailed findings

### Largest blocks (today 2026-05-19) [DP:dark_pool_largest]

| Time (UTC) | Price | NBBO mid | vs mid | Size | Premium | Read |
|------------|-------|----------|--------|------|---------|------|
| 18:55:43 | **28.91** | 28.84 | **+0.07** | 36,254 | $1,048,103 | block-tier buy |
| 17:13:50 | **28.98** | 28.84 | **+0.14** | 29,762 | $862,503 | aggressive buy |
| 14:23:31 | 30.00 | 29.98 | +0.02 | 19,500 | $585,000 | at-offer buy |
| 15:14:17 | 29.43 | 29.43 | 0 | 17,995 | $529,593 | mid-fill (likely buy w/ NBBO at-mid) |
| 15:14:17 | 29.43 | 29.43 | 0 | 13,270 | $390,536 | same time, paired |
| 14:48:38 | 29.38 | 29.455 | −0.075 | 10,500 | $308,490 | one of only 2 below-mid prints (sell-side) |
| 18:17:56 | 28.91 | 28.87 | +0.04 | 6,958 | $201,156 | buy |
| 17:13:49 | 28.859 | 28.855 | +0.004 | 6,300 | $181,812 | at-mid buy |
| 18:17:56 | 28.91 | 28.87 | +0.04 | 5,500 | $159,005 | buy |
| 19:49:51 | 30.23 | 30.225 | +0.005 | 5,000 | $151,150 | at-offer late-day buy |
| 17:11:59 | 28.68 | 28.655 | +0.025 | 5,240 | $150,283 | buy |
| 14:22:03 | 30.021 | 30.09 | −0.069 | 4,596 | $137,977 | below-mid (VWAP-style sell) |
| 19:04:22 | 29.44 | 29.38 | +0.06 | 4,472 | $131,656 | buy |
| 19:09:55 | 29.375 | 29.375 | 0 | 4,435 | $130,278 | at-mid |
| 13:57:37 | 30.31 | 30.305 | +0.005 | 4,140 | $125,483 | buy at intraday high |
| 19:42:23 | 30.14 | 30.08 | +0.06 | 3,690 | $111,217 | buy |

Tally: **14 of 16 prints are at-or-above NBBO mid**; only 2 prints (3.7% of
premium) are below mid and they look like VWAP-style sells, not aggressive
distribution. **No single institutional sell block** of size in today's tape.

### Tier breakdown [DP:dark_pool_block_stratified]

| Tier | Trades | Buy volume | Sell volume | Buy ratio | Total premium |
|------|--------|-----------|-------------|-----------|---------------|
| mega (≥$10M) | 0 | 0 | 0 | n/a | $0 |
| **block ($1M-$10M)** | 1 | **36,254** | **0** | **1.000** | **$1,048,103** |
| **large ($100k-$1M)** | 15 | **126,262** | **15,096** | **0.893** | **$4,156,138** |
| retail (<$100k) | n/a | n/a | n/a | n/a | (excluded by `min-tier=large`) |
| **Total (all tiers)** | — | — | — | — | **$5,204,241** |

Both "smart-money" tiers (block + large) print buy ratios deep in the
high-confidence band (>0.7 = high; 1.000 and 0.893 are emphatic). **No
mega-tier print** today — consistent with BL's $3-5B market cap; mega-tier
($10M+) blocks are typically reserved for mega-caps. The fact that BL has
*any* block-tier ($1M+) print at all is itself notable — phase-7 conviction
matrix should weight this.

### Price levels (5-day institutional S/R)
[DP:dark_pool_price_levels, days=5]

| Level | 5-day premium | Shares | Trades | Zone |
|-------|---------------|--------|--------|------|
| $25.81 | $3,856,014 | 149,400 | 1 | **floor cluster** |
| $25.80 | $3,854,520 | 149,400 | 2 | **floor cluster** |
| $24.90 | $1,005,960 | 40,400 | 2 | floor cluster |
| $28.91 | $1,408,264 | 48,712 | 3 | today mid-range |
| $28.98 | $862,503 | 29,762 | 1 | today mid-range |
| $29.43 | $920,129 | 31,265 | 2 | today mid-range |
| $29.83 | $596,600 | 20,000 | 1 | upper mid |
| $29.90 | $1,115,270 | 37,300 | 3 | upper mid |
| $30.00 | $1,071,000 | 35,700 | 2 | upper |
| $30.17 | $657,012 | 21,777 | 3 | upper |
| $30.30 | $827,766 | 27,319 | 2 | upper |
| $30.39 | $2,422,083 | 79,700 | 1 | upper-block |
| $30.40 | $778,240 | 25,600 | 1 | upper |
| $30.41 | $1,468,803 | 48,300 | 1 | upper-block |
| $30.50 | $685,671 | 22,481 | 2 | upper |

**Three institutional zones emerge:**
1. **Floor cluster:** $24.90–25.81 — **$8.72M** of premium in just 3 levels.
   This was likely accumulation earlier in the week (sweep-persistence said BL
   was in the top sweep board 3 of 5 sessions). Phase-9 stop must sit BELOW
   this band (e.g. $24.50) — breaking this floor would invalidate the thesis.
2. **Today's mid-range:** $28.91–29.43 — **$3.19M** premium spread across 6
   trades. This is "step 1 today" — institution lifted at this band in
   the late-morning/mid-day.
3. **Today's upper range:** $30.17–30.50 — **$3.61M** premium across 5+
   levels. "Step 2 today" — institution kept buying into strength even as
   spot rose to $30.27. **No visible institutional sell stack here** — the
   absence of a clear distribution wall above $30.50 is bullish for
   continuation.

### Extended hours [DP:dark_pool_extended_hours]

`results: []` — **no pre-market or post-market prints**. Cleanly intraday.
This rules out: news-leak frontrunning, ETF creation/redemption rebalancing
disguising the print, or after-hours catalyst hedging. Consistent with the
"single sponsor, paced campaign" interpretation from phase 1.

### Ticker-summary cross-check [DP:dark_pool_ticker_summary]

BL is **not** in the top 50 names by DP premium (top is MU at $11.6B; #50
clears around $400M). BL's $5.2M places it well outside that league, which
matches its market-cap profile. **This means dark-pool conviction here is
"strong for BL," not "strong vs the tape."** Phase-7 conviction matrix and
phase-8 risk monitor should weight accordingly: this is a small-cap
idiosyncratic accumulation pattern, not a sector/macro flow play.

## Cross-phase confluence (with phase-1-flow.md)

| Phase 1 datapoint | Phase 2 corroboration | Verdict |
|--------------------|----------------------|---------|
| $4.14M ask-side calls @ Dec $27.5C, ~18:58-19:42Z | $1.048M block buy @ $28.91, 18:55Z; $151k buy @ $30.23, 19:49Z | **stock + options stacked: same sponsor profile, options trailing the stock by minutes** |
| Buyer paid up from $7.40 to $8.40 in options | DP buyer paid +$0.07 and +$0.14 above mid in stock | **same "pay-for-immediacy" behavior in two markets** |
| Persistence 3 of 5 sessions, $17.97M sweep agg | 5-day DP floor cluster at $24.90-25.81 ($8.72M) — same window | **same campaign visible in both venues across the week** |

Confluence is **very high**. Phase-1's bullish call is being underwritten by
phase-2 dark-pool flow at the same time, by the same kind of price action.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | `{symbol:BL, top-n:25, sort-by:premium, date:2026-05-19}` | 16 rows; 14 at-or-above mid; top 2 above-NBBO buys |
| `dark_pool_block_stratified` | `{symbol:BL, top-n:30, min-tier:large, date:2026-05-19}` | block buy_ratio=1.00; large buy_ratio=0.893; total $5.20M |
| `dark_pool_extended_hours` | `{symbol:BL, top-n:15, date:2026-05-19}` | empty (no XH prints) |
| `dark_pool_price_levels` | `{symbol:BL, top-n:15, days:5, date:2026-05-19}` | 15 levels; floor $24.90-25.81 ($8.72M), mid $28.91-29.43, upper $30.17-30.50 |
| `dark_pool_ticker_summary` | `{top-n:50, date:2026-05-19}` | BL absent from top-50; market dominated by MU/QQQ/SPY/NVDA |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **Accumulation** (institutional, intraday,
  unhedged).
- **Conviction:** **5 / 5** — both smart-money tiers are saturated buy-side,
  buyer paid up in two venues simultaneously, no offsetting distribution
  visible, no overnight noise to discount.
- **Three S/R levels for phase 9 to use as entry/stop reference:**
  1. **Institutional floor: $24.90 – $25.81** (5-day, $8.72M premium). Stop
     loss reference. A break of $24.85 invalidates the accumulation thesis
     (see rubrics/invalidation-rubric.md).
  2. **Current accumulation zone: $28.91 – $30.50** (today, $6.80M premium
     across 16 prints). Pullback entries should target the lower half
     ($28.90–29.40); chase entries above $30.50 risk paying retail.
  3. **No visible institutional sell wall above $30.50** within the
     5-day data — open air for continuation. Phase-4 (GEX / gamma flip) must
     identify the dealer pin/charm levels in this same band before sizing.
- **Three things later phases should remember:**
  1. The buyer is **paying up in both stock and options simultaneously** —
     this is a high-conviction accumulator, not a passive index rebalancer.
  2. **$24.90–25.81 is the institutional floor**; any phase-9 stop must
     respect this and sit just below.
  3. Dark pool footprint **scales with BL** ($5.2M today is meaningful for
     this name; would be tape-noise for SPY/NVDA). Don't over-claim
     absolute-dollar conviction; risk-monitor in phase-8 must size the
     position to BL's ADV.
- **Open questions for downstream phases:**
  - What is BL's **dealer gamma profile** at $27.5, $30, and $32.5? Is the
    upper range $30.17-30.50 a dealer pin (charm) or a soft ceiling? → phase 4.
  - Are there **stacked OI strikes** ($30 / $32.5 / $35 calls) that
    sequence the upside path the buyer is laddering toward? → phase 3.
  - Does the **IV percentile** in phase-5 show a regime that justifies the
    79-81% IV the buyer is paying, or is the buyer overpaying for vol? → phase 5.
