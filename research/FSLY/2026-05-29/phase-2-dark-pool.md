# Phase 2 — Dark Pool

## Summary

The institutional cash tape is **small but mildly constructive — net balanced-to-
slightly-accumulative**, a contrast to the thin options flow and a contrast to CRM's
clear distribution. Total dark-pool premium is just **$10.5M (596.5k shares = 0.41%
of the 145.2M float, 32 trades)** — light, fitting the quiet day. The composition:

- **No mega tier.** The conviction is in the **large tier: buy_ratio 0.85, $6.74M,
  31 trades, 326.4k buy vs 57.6k sell shares** — clear mid-tier *accumulation*.
- **One $3.78M block printed as a sell** (212.5k shares @ $17.765, **−$0.055 below
  NBBO mid**, ~0.15% of float) — the single offsetting distribution print.
- Across the top-12 largest prints, **8 were above-mid buys ($3.2M) vs 2 below-mid
  sells ($4.0M)** — buy-skewed by count, sell-skewed by dollars (the one block
  dominates the dollar tally).
- Price levels cluster **at/just below the $17.77 close** ($4.78M / 269k sh at
  $17.77; secondary $17.49–$17.58) — institutions transacting right around the
  close, with a mild **support shelf $17.49–$17.58**.

**Cash-tape read: NEUTRAL-to-mildly-BULLISH, conviction LOW** (small absolute size).
The large-tier 0.85 buy ratio leans accumulation and gives phase-9 a usable support
shelf ~$17.5; the lone $3.78M sell block keeps it from being a clean buy. On $10.5M
total it is a *supportive footnote*, not a thesis driver.

## Block stratification (`uw dark-pool block-stratified`) `[DP:block-stratified]`

| Tier (boundary) | Buy ratio | Premium | Trades | Buy / Sell shares |
|-----------------|-----------|---------|--------|-------------------|
| mega (≥$10M) | — | $0 | 0 | — |
| **block** (≥$1M) | **0.00** | $3.78M | 1 | 0 / 212.5k |
| **large** (≥$100k) | **0.85** | $6.74M | 31 | 326.4k / 57.6k |
| retail (<$100k) | — | $0 | 0 | — |
| **all tiers** | | **$10.51M** | 32 | |

- The two tiers tell opposite small stories: **one block sold ($3.78M)** vs **31
  large-tier buys ($6.74M, 85% buy)**. Net dollars roughly offset; net *trade count*
  and the large-tier ratio lean **accumulation**. No mega/retail tiers active.

## Price levels (`uw dark-pool price-levels`) `[DP:price-levels]`

| Price | Premium | Shares | Trades |
|-------|---------|--------|--------|
| **$17.77** | $4.78M | 269k | 5 |
| $17.58 | $1.08M | 61k | 4 |
| $17.57 | $0.88M | 50k | 1 |
| $17.75 | $0.55M | 31k | 1 |
| $17.49 | $0.45M | 26k | 2 |
| $17.55 | $0.35M | 20k | 2 |

- Activity concentrates **at the $17.77 close** and a cluster **$17.49–$17.58** →
  a mild institutional **support shelf ~$17.5** (≈ −1.5% from close) for phase-9.

## Largest prints (`uw dark-pool largest`) `[DP:largest]`

| Size | Price | NBBO bid/ask | vs mid | Premium | Read |
|------|-------|--------------|--------|---------|------|
| 212,512 | $17.765 | 17.80/17.84 | **−0.055** | $3.78M | the lone sell block |
| 49,900 | $17.57 | 17.50/17.51 | **+0.065** | $0.88M | buy |
| 35,959 | $17.58 | 17.56/17.60 | 0.00 | $0.63M | at-mid |
| 31,100 | $17.75 | 17.71/17.73 | +0.030 | $0.55M | buy |

- 8 of 12 prints above-mid (buys), 2 below (sells); the $3.78M block is the only
  large distribution. **Mildly buy-skewed by count.**

## Float normalization (advisory) `[DP: fz]`

- DP 596.5k shares = **0.41% of the 145.2M float** (light); the $3.78M block =
  **0.15% of float**. On a heavily-shorted (14.6%) small-cap, even modest off-exchange
  accumulation matters more than the dollars imply — but today's size is small.

## Tool calls

```bash
uw dark-pool block-stratified --symbol FSLY --date 2026-05-29 --json
uw dark-pool price-levels     --symbol FSLY --date 2026-05-29 --json
uw dark-pool largest          --symbol FSLY --date 2026-05-29 --top-n 12 --json
```

## Tool errors

none

## Read-through

- Unlike CRM (clear institutional distribution), FSLY's cash tape is **net
  neutral-to-mildly-accumulative**: the large tier bought (0.85 ratio, $6.74M) and
  prints cluster as a support shelf ~$17.5, offset by a single $3.78M sell block.
  On a +4.9% day, mild net buying *with* price is benign-to-supportive — no
  distribution-into-strength red flag.
- But the **magnitudes are small** ($10.5M total, 0.41% of float). This corroborates
  the bullish lean *weakly*; it does not by itself make a trade. Combined with
  phase-1's thin call-tilt, the picture after two phases is **"faint bullish lean on
  a quiet small-cap, supported by mild dark-pool accumulation at ~$17.5."**
- **For phase-9 geometry:** the $17.49–$17.58 dark-pool shelf is the first usable
  support reference (intake/structure will add OI walls + the squeeze context).

## Citations

- `[DP:block-stratified]` large-tier buy_ratio 0.85 ($6.74M, 326k/58k) vs one $3.78M sell block — `uw dark-pool block-stratified`
- `[DP:price-levels]` $4.78M/269k sh at $17.77 close; support shelf $17.49–$17.58 — `uw dark-pool price-levels`
- `[DP:largest]` 8/12 prints above-mid (buys); lone $3.78M block −$0.055 vs mid — `uw dark-pool largest`
- `[DP: fz]` DP 596.5k sh = 0.41% of 145.2M float (light) — `uw insights deep-dive` + `fz` float

## Upstream references

- phase-1-flow.md §Read-through — "faint weak-bullish prior, conviction LOW"; phase-2
  adds a *mild* corroborating accumulation (large-tier 0.85 buy) but at small size —
  the lean stays weak.
- phase-0.5-context.md §Verdict — "BUSY_NAME_NORMAL_DAY leaning QUIET"; the small
  $10.5M DP tape is consistent with the quiet-day context.

## Next phase

- phase-3-positioning.md (OI walls + the squeeze-lottery call builds — does
  positioning around the 14.6% short float give an asymmetric upside structure, or
  is OI as thin as the flow?)
