# Phase 2 — Dark Pool

## Summary

**The institutional cash tape CONTRADICTS the bullish options flow.** On $1.45B of
total dark-pool premium (7.62M shares, ~**0.96% of the 792.9M float** in a single
session — heavy), the prints are overwhelmingly **sell-leaning**:

- **Mega tier (≥$10M): buy ratio 0.017** — $616.7M premium, 21 trades, **3.17M
  sell vs 0.055M buy shares.** Almost pure distribution.
- **Block tier (≥$1M): buy ratio 0.098** — $429.0M, 146 trades, 2.03M sell vs
  0.22M buy.
- **Large tier (≥$100k): buy ratio 0.479** — $407.8M, balanced-to-slightly-sell.
- **19 of the top-20 largest prints executed BELOW NBBO mid** ($596M sell-lean vs
  $11M buy-lean). The single largest print: **1,037,753 shares @ $191.10** with NBBO
  $191.42/$191.77 — **$0.495 below mid**, ~$198M, clearly sold.

**Caveat (don't over-read):** on a **+8.5% up day**, "below-mid" prints are partly
mechanical — late-tape prints stamped at the session VWAP/last ($191.10) while a
fast NBBO sits higher will *look* sell-side. So some of the 19/20 below-mid is
artifact. **But** the mega-tier buy ratio of 1.7% and block 9.8% are tier-level
aggregates that don't depend on the mid comparison, and they say the same thing:
**large institutions were net distributors into the pop.**

**Cash-tape read: DISTRIBUTION / BEARISH-divergent, conviction MODERATE.** This is
the first hard contradiction in the chain — options buyers are positioning long
while the biggest holders are selling shares into their strength.

## Block stratification (`uw dark-pool block-stratified`) `[DP:block-stratified]`

| Tier (boundary) | Buy ratio | Premium | Trades | Buy / Sell shares |
|-----------------|-----------|---------|--------|-------------------|
| **mega** (≥$10M) | **0.017** | $616.7M | 21 | 55.2k / 3,171.7k |
| **block** (≥$1M) | **0.098** | $429.0M | 146 | 220.4k / 2,029.3k |
| large (≥$100k) | 0.479 | $407.8M | 1,724 | 1,027.0k / 1,116.7k |
| retail (<$100k) | — | $0 | 0 | — |
| **all tiers** | | **$1,453.5M** | | |

- The conviction tiers (mega + block) carry **$1.05B of the $1.45B** and are
  **~90% sell**. The retail tier is empty. This is an institutional footprint, and
  it is a selling one.

## Price levels (`uw dark-pool price-levels`) `[DP:price-levels]`

| Price level | Premium | Shares | Trades |
|-------------|---------|--------|--------|
| **$191.10** | $907.8M | 4.75M | 234 |
| $191.09 | $49.4M | 258k | 10 |
| $191.11 | $38.5M | 202k | 28 |
| $192.35 | $16.1M | 84k | 10 |
| $184.27 | $7.5M | 41k | 1 |
| $186.30 | $7.3M | 39k | 2 |

- The institutional tape is **pinned to the close, $191.10** ($908M / 4.75M shares
  there alone) — i.e. the distribution happened *at the closing print*, not on a
  pullback. Secondary interest clusters $191–$192.4. Minor lower nodes at $184–$186
  could act as supports if price gives back the pop. **No accumulation shelf below**.

## Largest prints (`uw dark-pool largest`) `[DP:largest]`

| Time (Z) | Size | Price | NBBO bid/ask | vs mid | Premium |
|----------|------|-------|--------------|--------|---------|
| 20:12 | 1,037,753 | 191.10 | 191.42/191.77 | **−0.50** | $198.3M |
| 20:00 | 285,190 | 191.10 | 190.60/192.49 | −0.45 | $54.5M |
| 20:00 | 226,471 | 191.10 | 190.60/192.49 | −0.45 | $43.3M |
| 20:17 | 219,439 | 191.10 | 191.20/191.50 | −0.25 | $41.9M |
| 20:17 | 211,639 | 191.10 | 191.20/191.50 | −0.25 | $40.4M |

- All five largest prints **below mid**, clustered in the closing 20:00–20:53Z
  window — late-day institutional selling into the strength.

## Float normalization (advisory) `[DP: fz]`

- DP shares 7.62M / float 792.87M = **0.96% of float** changed hands off-exchange in
  one day — a high-participation session. The single 1.04M-share block ≈ **0.13% of
  float** in one print.

## Tool calls

```bash
uw dark-pool block-stratified --symbol CRM --date 2026-05-29 --json
uw dark-pool price-levels     --symbol CRM --date 2026-05-29 --json
uw dark-pool largest          --symbol CRM --date 2026-05-29 --top-n 20 --json
# (ticker-summary takes no --symbol; covered by block-stratified + insights aggregate)
```

## Tool errors

- `uw dark-pool ticker-summary` rejects `--symbol` (it's a market-wide ranking). The
  per-ticker aggregate is fully covered by `block-stratified` + the
  `insights deep-dive` dark-pool block (phase-0.5). Not blocking.

## Read-through

- **This is the pivot of the dive.** Phases 0.5/1 built a clean bullish options
  story; phase-2 introduces a **hard divergence**: the largest holders sold ~$1.05B
  (mega+block, ~90% sell) into the +8.5% rally, concentrated at the closing print.
  Options traders bought calls; institutions handed them stock.
- **Two readings, and phase-8/8b must adjudicate:**
  1. *Bearish/distribution:* smart money is using the pop (and the call-buyers'
     demand) as exit liquidity → the +8.5% is a selling opportunity, fade-risk high.
  2. *Benign/mechanical-plus-rotation:* part of the below-mid skew is up-day tape
     artifact, and large index/portfolio rebalancing prints at the close are not
     always "informed." Under this reading the options flow still leads.
  The **tier aggregates (mega 1.7%, block 9.8% buy)** tilt me toward reading (1) as
  the dominant signal — those are not mid-dependent and they are lopsided.
- **For phase-9 geometry:** no dark-pool accumulation shelf exists *below* spot to
  lean long against; the only institutional level is **$191.10 distribution** right
  at spot. Minor lower nodes $184–$186. This *weakens* the long case materially and
  raises the bar for the bullish-flow thesis to clear.

## Citations

- `[DP:block-stratified]` mega buy-ratio 0.017 ($616.7M), block 0.098 ($429.0M) — `uw dark-pool block-stratified`
- `[DP:largest]` 19/20 top prints below mid ($596M vs $11M); 1.04M-sh block −$0.50 vs mid — `uw dark-pool largest`
- `[DP:price-levels]` $908M / 4.75M shares pinned at $191.10 close; no shelf below — `uw dark-pool price-levels`
- `[DP: fz]` 7.62M DP shares = 0.96% of 792.9M float — `uw insights deep-dive` + `fz` float

## Upstream references

- phase-1-flow.md §Summary — "BULLISH, 20/20 call sweeps"; phase-2 directly
  **contradicts** it on the cash tape: mega-tier dark pool ~98% sell into the pop.
- phase-0.5-context.md §Composite — "$1.45B dark-pool premium, 7.62M shares";
  phase-2 resolves that aggregate as **distribution**, not accumulation.

## Next phase

- phase-3-positioning.md (open interest — is the call buying building genuine new OI
  walls at $200, and is the 160P hedge from the OI-changes block growing? does
  positioning corroborate the flow or the dark-pool selling?)
