# Phase 2 — Dark Pool & Block Prints

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool is **MIXED and leans distribution-at-the-top**, not accumulation.
Today's tier buy_ratios are only *weakly* positive (large 0.573, block 0.526 — both
inside the "suggestive only," sub-0.7 band), and the single mega print ($13.16M) is
tagged buy. But the **5-day price-level map is the real tell: ~$83M of dark-pool
premium printed at $91–92** — right at the parabolic peak (phase-0.5: 05-26 close
$89.83) — and the stock then fell **−9.7% to $81.11**. That is the smart-money
distribution signature: heavy size changes hands at the top, price rolls over. Today
itself opened with **pre-market sell blocks at $82.5–$82.9** (the first printed below
bid) that preceded the decline. Block sizes are modest as a share of the 132.68M
float (largest 0.12%), and GFS sits **outside the top-40 DP names**. Net: the dark
pool does **not** confirm a long; it confirms phase-1's call-writing/profit-taking
read.

## Key signals

- **5-day DP supply wall at $91–92:** $26.5M + $23.7M + $18.5M + $14.0M ≈ **$83M**
  printed 13% above spot, at the parabolic peak `[DP:price_levels]`. Now overhead
  resistance.
- Tier buy_ratios **suggestive-only**: large 0.573 ($105.3M, 496 trades), block
  0.526 ($84.3M, 37 trades), mega 1.0 (1 trade, $13.16M) `[DP:block_stratified]`.
- **Pre-market sell distribution:** 12:05Z block 50,000 sh @ $82.50 **below bid
  (82.60/82.70)** = sell; further $82.75–$82.90 blocks pre-open, all before the
  −9.7% day `[DP:extended_hours]`.
- Largest single block **163,000 sh / $13.16M @ $80.72 = only 0.12% of float**
  `[DP:largest]`, `[DP:block_pct_float fz]`. Whole-day 2.49M sh = **1.88% of float**.
- GFS **outside top-40** DP names (leaders MU/NVDA/SPY/SNDK/QQQ/TSLA)
  `[DP:ticker_summary]` — large absolute $, not a market-leading DP name.

## Detailed findings

### Largest blocks (top-25, classified by price vs NBBO) `[DP:largest]`

| time (UTC) | price | size | $M | % float | aggressor |
|-----------|------:|-----:|---:|--------:|-----------|
| 15:01 | 80.72 | 163,000 | 13.16 | 0.12% | mid (tool: buy) |
| 15:04 | 80.83 | 53,250 | 4.30 | 0.04% | mid |
| 12:05 | 82.50 | 50,000 | 4.12 | 0.04% | **HIT (sell)** |
| 14:05 | 82.45 | 50,000 | 4.12 | 0.04% | mid |
| 14:09 | 82.14 | 50,000 | 4.11 | 0.04% | LIFT (buy) |
| 13:49 | 81.85 | 50,000 | 4.09 | 0.04% | mid |
| 12:09 | 82.75 | 42,500 | 3.52 | 0.03% | **HIT (sell)** |
| 15:51 | 79.10 | 45,087 | 3.57 | 0.03% | **HIT (sell)** |
| 15:53 | 79.40 | 41,127 | 3.27 | 0.03% | **HIT (sell)** |

Strict price-vs-NBBO count of the top-25: **9 hits ($24.6M) vs 5 lifts ($14.0M)**,
11 mid ($41.9M). My manual hit/lift count leans sell; the tool's probabilistic tier
buy_ratio leans weakly buy. Both agree the signal is **not** a high-conviction
accumulation — they disagree only on which side of "mixed."

### Tier breakdown `[DP:block_stratified]`

| tier (≥) | trades | buy_vol | sell_vol | buy_ratio | $ |
|----------|------:|--------:|---------:|----------:|---:|
| mega ($10M) | 1 | 163,000 | 0 | 1.00 | $13.2M |
| block ($1M) | 37 | 542,002 | 488,664 | **0.526** | $84.3M |
| large ($100k) | 496 | 742,359 | 552,960 | **0.573** | $105.3M |
| **all tiers** | | | | | **$202.7M** |

Per the tool's own caveat, 0.55–0.7 is "suggestive only," >0.7 high-confidence.
Large tier (0.573) is the most populated and the cleanest read — a **mild** buy
lean, consistent with dip-liquidity provision into a falling tape rather than
conviction accumulation.

### Price levels (5-day clusters, window anchored to 2026-05-27) `[DP:price_levels]`

| level | $M | shares | trades | vs spot $81.11 |
|------:|---:|-------:|------:|---------------|
| **91.25** | 26.5 | 290,360 | 2 | +12.5% (peak) |
| **91.55** | 23.7 | 258,800 | 6 | +12.9% |
| 85.64 | 18.7 | 217,839 | 8 | +5.6% (05-22) |
| **91.90** | 18.5 | 201,598 | 2 | +13.3% |
| 80.72 | 14.2 | 175,300 | 4 | −0.5% (today value) |
| 92.20 | 14.0 | 151,700 | 1 | +13.7% |
| 82.75 | 11.3 | 137,050 | 8 | +2.0% |
| 81.35 / 81.11 / 81.01 | 18.5 (sum) | ~252k | 34 | ≈spot |
| 78.77 | 5.5 | 69,981 | 1 | −2.9% |
| 70.79 | 4.4 | 62,493 | 10 | −12.7% (pre-breakout base) |

**The dominant clusters are at $91–92 — above spot — where ~$83M printed at the top.
This is the single most important structural level: heavy supply / distribution
zone.** Below spot the meaningful shelves are $78.77 and the $70.79 pre-breakout base.

### Extended-hours `[DP:extended_hours]`

Largest ext-hours prints were **pre-market** (12:05–12:30Z ≈ 8:05–8:30 ET) at
$82.50–$82.90 — including a 50,000-sh sell below bid — totaling ~$15M of size that
*preceded* the regular-session decline. Two post-close prints (20:06Z, 21:06Z) at
$81.11. No benign rebalancing tag; the pre-market blocks read as distribution.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw dark-pool largest --top-n 25 --sort-by premium` | 25 blocks, top $13.16M; 9 hit / 5 lift / 11 mid |
| `uw dark-pool block-stratified --min-tier large` | large 0.573, block 0.526, mega 1.0; $202.7M all-tier |
| `uw dark-pool price-levels --days 5` | **$83M cluster at $91–92** (peak); base $70.79 |
| `uw dark-pool extended-hours --top-n 15` | pre-market sell blocks $82.5–82.9 before decline |
| `uw dark-pool ticker-summary --top-n 40` | **GFS outside top-40** (MU/NVDA/SPY lead) |

## Tool errors

None.

## Verdict for downstream

- **Bias from this phase:** **MIXED → mild distribution.** Weak intraday buy_ratios
  (≤0.573, suggestive only) against a clear 5-day distribution cluster at $91–92 and
  pre-market selling. Does not support a conviction long.
- **Conviction:** **2/5** (size present, tier signal weak, direction conflicted).
- **Largest block as % of float (advisory):** **0.12%** (163k / 132.68M); whole-day
  1.88%. Meaningful turnover, but **no single dominant block** — no whale footprint
  `[DP:block_pct_float fz]`.
- **Three S/R levels for phase-9:**
  1. **Resistance $91–92** — $83M 5-day DP supply wall (the peak distribution zone).
  2. **Pivot/value $80.7–82.75** — today's mega print + intraday value area.
  3. **Support $78.77, then $70.79** — pre-breakout base / structural floor.
- **Open questions:** Does dealer GEX (phase-4) sit short or long gamma around
  $80–82 (would explain the call writing)? Does OI (phase-3) show the $91–92 supply
  mirrored in call OI being distributed? Is the weak buy_ratio genuine dip-buying or
  just MM liquidity into sellers (phase-5 base-rate + phase-8b debate)?
