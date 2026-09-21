# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-1-flow.md (LEAP call accumulation, net flow flat, "is the DP
confirming accumulation under $11.72?") · phase-0-intake.md (Shs Float 412.34M)

## Summary

The dark-pool tape shows **mild, real accumulation** — supportive of phase-1's
LEAP-call read but not aggressive. Total off-exchange premium **$74.5M** across
**433 prints** (6.46M shares ≈ **1.57% of the 412M float**). The **block tier
(≥$1M) is 100% buy** (buy_ratio **1.00**, 5 trades, 769K shares, $8.96M) — a
clean institutional accumulation footprint — but the much larger **large tier
(≥$100K) is balanced** (buy_ratio **0.508**, $65.6M, 428 trades) and there were
**no mega-tier (≥$10M) prints**. Prints cluster **at and just above spot**: the
single biggest block was **219,390 sh @ $11.72** (right at the close/ask) and a
**150,000 sh @ $11.78** print sat above mid — institutions were willing to *pay
up*, the accumulation signature. Net: constructive, institutions buying the
$11.65–$11.80 shelf, but the conviction is moderate (block-tier-only, no
mega-tier, balanced large tier).

## Key signals

- **Block tier 100% buy** — buy_ratio 1.00, 769K sh / $8.96M, 0 sells
  `[DP:block-stratified]`. Cleanest accumulation read in the data.
- **Pay-up prints at/above spot** — 219,390 sh @ $11.72 (NBBO ask 11.72),
  150,000 sh @ $11.78 (above mid), 83,300 sh @ $12.00 `[DP:largest]`.
- **Large tier balanced** — buy_ratio 0.508 across $65.6M / 428 trades →
  the *bulk* of the dark-pool dollars are two-sided, not one-way accumulation.
- **Post-close buying at the close price** — multiple after-hours prints pinned
  at **$11.72** (16:00–17:48 ET: 41K, 30K, 19K, 18K sh) `[DP:extended-hours]`,
  consistent with a closing-auction / VWAP-completion buy program.
- **PATH not in DP top-40 by premium** `[DP:ticker-summary]` — institutional
  activity is real but not a market-leading block day (matches phase-0.5's
  BUSY_NAME_NORMAL_DAY).

## Detailed findings

### Largest blocks
| Time (ET) | Price | Size | Premium | NBBO | % float | Read |
|---|---|---|---|---|---|---|
| 12:39 | $11.72 | 219,390 | $2.57M | bid 11.71 / ask 11.72 | 0.053% | at ask — buy |
| 15:46 | $11.69 | 182,066 | $2.13M | 11.68 / 11.69 | 0.044% | at ask — buy |
| 11:36 | $11.78 | 150,000 | $1.77M | 11.75 / 11.76 | 0.036% | **above ask — pay-up** |
| 10:02 | $11.21 | 120,045 | $1.35M | 11.20 / 11.22 | 0.029% | midpoint |
| 13:32 | $12.00 | 83,300 | $1.00M | 11.99 / 12.00 | 0.020% | at ask @ $12 |
| 09:32 | $10.47 | 79,331 | $0.83M | 10.51 / 10.53 | 0.019% | below bid (early, low) |

Largest single block = **0.053% of float** — modest for a 412M-float name
`[DP:block_pct_float fz]`; no single print is a float-moving event. The signal
is the *consistency* of buying the $11.65–$11.80 shelf, not any one block's size.

### Tier breakdown
| Tier | Buy ratio | Premium | Trades | Read |
|---|---|---|---|---|
| Mega (≥$10M) | — | $0 | 0 | none |
| Block (≥$1M) | **1.00** | $8.96M | 5 | clean accumulation |
| Large (≥$100K) | 0.508 | $65.6M | 428 | balanced / two-sided |
| Total | — | $74.5M | 433 | mild net buy |

### Price levels (S/R)
`price-levels --days 5` returned null price bins (CLI field not populated in this
cut), so S/R derived from today's block distribution:
- **Supply / resistance: ~$12.00** (83K @ $12.00; matches phase-1 12C/2028 strike
  interest and phase-3 OI to confirm).
- **Value / support shelf: $11.65–$11.80** (the bulk of large blocks incl. the
  219K @ $11.72 and 150K @ $11.78; also the close & post-close pin) — primary
  reference support.
- **Lower support: $11.20–$11.30** (120K @ $11.21, 45K @ $11.27) and a deeper
  $10.50–$10.90 shelf (the morning lows the stock rallied from).

### Extended-hours activity
Pre-market prints ~$11.29–$11.35 (08:06 ET) and a cluster of post-close prints
pinned at **$11.72** (16:00–17:48 ET). No overnight news identified (confirm in
phase-6); reads as closing-program completion, not a news-driven block.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `dark-pool largest` | `--symbol PATH --sort-by premium --top-n 25` | blocks at/above spot |
| `dark-pool block-stratified` | `--min-tier large --top-n 30` | block buy_ratio 1.0, large 0.508 |
| `dark-pool price-levels` | `--days 5 --top-n 15` | null price bins (unusable) |
| `dark-pool ticker-summary` | `--top-n 40` | PATH not in top-40 |
| `dark-pool extended-hours` | `--top-n 10` | post-close pin @ $11.72 |

## Tool errors
(none — `price-levels` returned rows with null `price`/`size`; not an error but
unusable for S/R, noted above.)

## Verdict for downstream

- **Bias: MILD ACCUMULATION** — block tier 100% buy + pay-up prints at/above
  spot, but no mega tier and balanced large tier. Confirms phase-1's LEAP-call
  lean *modestly*; does not upgrade it to high conviction.
- **Conviction: 3 / 5** — clean signal in the block tier, diluted by the much
  larger balanced large tier. Phase-0.5 cap (`+`, BUSY_NAME_NORMAL_DAY) holds.
- **Largest block as % of float: 0.053%** (advisory) — not meaningful in
  isolation for a 412M-float name; the *cluster* of buying matters more than any
  single print.
- **Three S/R levels for phase-9:**
  1. **Support $11.65–$11.80** (value shelf / close / post-close pin) — primary.
  2. **Lower support $11.20–$11.30** (then $10.50–$10.90 deep shelf).
  3. **Resistance $12.00** (block + option-strike cluster).
- **Open questions:**
  - Does phase-3 OI confirm a $12 supply wall (call OI / dealer short gamma)?
  - With 31% short float, is the block buying *short covering* (mechanical) vs
    *new long accumulation* (directional)? DP buy classification can't tell —
    phase-7c short-interest trend must adjudicate.
