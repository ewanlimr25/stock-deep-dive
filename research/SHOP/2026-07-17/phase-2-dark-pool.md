# Phase 2 — Dark Pool & Block Prints

**Ticker:** SHOP
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) · as-of 2026-07-17
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Institutional dark-pool prints lean **distribution**: the **block tier (≥$1M) is
74% sell** (`buy_ratio 0.257`, 143k sell vs 49k buy shares, $23.8M premium) while
the large tier ($100k–$1M) is balanced (`0.516`). Premium-weighted trade-vs-mid on
the top-25 prints agrees — $23.2M below-mid (sell-lean) vs $12.3M above-mid. **But
two caveats de-rate it:** (1) the two biggest blocks ($9.75M + $4.43M at 123.56)
are **after-hours prints** (21:12–21:14 UTC) on an **NDX-index member** — likely
rebalance/ETF flow, not directional; (2) on a ~**1.30B-share float**, even the
78,884-share top block is **~0.006% of float** — the sizes are immaterial *for this
name*. Net read: mild distribution confirming phase-0.5's persistent bearish tilt,
but low conviction. Key 5-day institutional levels: **125.06 (heavy overhead),
123.55–123.65 (spot pivot), 122.56 support.**

## Key signals

- **Block-tier buy_ratio 0.257 → 74% sell** (institutional distribution). `[DP:block_stratified]`
- **Large-tier buy_ratio 0.516 → balanced** — no institutional accumulation. `[DP:block_stratified]`
- **Top-25 prints premium-weighted: $23.2M below-mid vs $12.3M above-mid** (sell-lean). `[DP:largest]`
- **Two biggest blocks are after-hours** ($14.2M combined at 123.56, 21:12–21:14 UTC)
  on an **NDX member** → index-rebalance suspect, de-rate. `[DP:extended_hours]`
- **5-day price-level clusters:** 125.06 ($125.9M), 124.74 ($26.3M), 123.55/56
  (~$50M combined), 122.56 ($3.0M). `[DP:price_levels]`

## Detailed findings

### Largest blocks (spot ref 123.56, prev 125.06) `[DP:largest]`

| Time (UTC) | Price | Size (sh) | Premium | vs-mid | % float¹ | Note |
|---|---|---|---|---|---|---|
| 21:14 | 123.56 | 78,884 | $9.75M | −0.09 (wide NBBO) | 0.006% | **After-hours** — index/ETF suspect |
| 21:12 | 123.56 | 35,884 | $4.43M | −0.09 (wide NBBO) | 0.003% | **After-hours** — index/ETF suspect |
| 19:45 | 123.39 | 28,515 | $3.52M | −0.005 (at mid) | 0.002% | Intraday, at-mid |
| 20:00 | 123.56 | 20,432 | $2.52M | +0.115 (buy-lean) | 0.002% | Closing-auction, above-mid |
| 20:00 | 123.56 | 16,585 | $2.05M | +0.115 (buy-lean) | 0.001% | Closing-auction, above-mid |
| 14:39 | 122.47 | 12,425 | $1.52M | +0.055 (buy-lean) | 0.001% | Intraday support-ish buy |

¹ float ≈ 1.30B sh (mcap $160.34B ÷ 123.56); `fz Shs Float` was n/a → derived. All
sizes **immaterial vs float** — advisory only, never a conviction add.

Top-25 total dark-pool premium = **$35.5M** (SHOP **not** in the market-wide
dark-pool ticker-summary top-40 → off-exchange activity not a universe leader).

### Tier breakdown (buy/sell) `[DP:block_stratified]`

| Tier (single-day) | buy_ratio | derived sell_ratio | buy_vol | sell_vol | total_premium |
|---|---|---|---|---|---|
| **block (≥$1M)** | **0.257** | **0.743** | 49,442 | 143,283 | $23.79M |
| large ($100k–$1M) | 0.516 | 0.484 | 148,032 | 139,117 | $35.33M |
| mega (≥$10M) | — | — | 0 | 0 | $0 (no single block ≥$10M) |
| retail (<$100k) | — | — | 0 | 0 | $0 |

The **block tier is the clean institutional read: 74% sell = distribution.** The
larger-aggregate large tier is balanced, so this is *mild* distribution, not a
liquidation. Ratios 0.55–0.75 are "suggestive"; 0.743 sits at the high-confidence
edge but is diluted by the balanced large tier.

### Price levels (5-day: 2026-07-13 → 07-17) `[DP:price_levels]`

Dominant institutional clusters (premium): **125.06 ($125.9M — by far the heaviest,
= prev close / major overhead), 124.74 ($26.3M), 123.55 ($25.2M) + 123.56 ($25.1M)
≈ $50M at spot, 125.68/125.82 (~$19M), 122.56 ($3.0M).** Spot (123.56) sits **on** a
large cluster with **heavy overhead supply at 124.7–125.8**. Support thins below
122.5.

### Extended-hours activity `[DP:extended_hours]`

All top extended-hours prints are the closing/after-hours blocks at **123.56** (six
prints 20:00–21:14 UTC, $9.75M/$4.43M the largest). SHOP is an **NDX index member**
→ these are **rebalance/ETF-creation suspect**, not clean directional intent.
De-rate the after-hours sell-lean accordingly.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw dark-pool block-stratified --symbol SHOP --top-n 30 --min-tier large --date 2026-07-17` | block buy_ratio 0.257 ← `.results[0].block.buy_ratio` | 1 tkr |
| `uw dark-pool largest --symbol SHOP --top-n 25 --sort-by premium --date …` | below-mid $23.2M ← `[.results[]\|select(.trade_vs_mid<0).premium]\|add` | 25 |
| `uw dark-pool price-levels --symbol SHOP --days 5 --date …` | 125.06 $125.9M ← `.results[0]{price_level,total_premium}` | 15 |
| `uw dark-pool extended-hours --symbol SHOP --top-n 15 --date …` | 78,884@123.56 21:14 ← `.results[0]{executed_at,size}` | 15 |
| `uw dark-pool ticker-summary --top-n 40 --date …` | SHOP absent ← `index("SHOP")`=null | 40 |

## Tool errors

<none — all green>

## DATA NOTE / CORRECTION

`fz Shs Float` was n/a (phase-0 partial quote); float ≈1.30B derived from mcap
$160.34B ÷ spot 123.56 for the %-of-float column. Advisory only. Premium-weighted
buy/sell sums recomputed with null-safe filters (`select(.trade_vs_mid<0)`); one
row had null premium and was excluded — noted, does not change the sell-lean sign.

## Verdict for downstream phases

- **Bias:** MILD DISTRIBUTION (block-tier 74% sell), de-rated for after-hours/index
  prints and immaterial %-of-float.
- **Conviction:** 2/5 — clean block-tier sell ratio but balanced large tier, tiny
  vs float, biggest prints index-suspect.
- **Largest block as % of float:** ~0.006% (78,884 sh / ~1.30B) — **immaterial for
  a mega-float name**; do not read block size as conviction here.
- **Three S/R levels for phase-9:**
  1. **125.06** — heaviest 5-day institutional cluster = major overhead resistance
     (also prev close, and phase-1 sellers active 124.7–125.8).
  2. **123.55–123.65** — spot pivot (~$50M clustered here, = today's close).
  3. **122.56 / 121.48** — nearest institutional support; thins below 122.5.
- **Open questions:** Do the OI walls (phase-3) reinforce 125 as resistance and
  116/121 as the options battle zone from phase-1? Is dealer positioning (phase-3/4)
  short-gamma below spot, which would let this mild distribution accelerate?
