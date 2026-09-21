# Phase 2 — Dark Pool & Block Prints

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-1-flow.md (cautious — call selling + put hedging; "is the DP
accumulating or distributing the post-earnings level?") · phase-0 (float 334.88M)

## Summary

The dark pool **answers phase-1's question in favour of distribution**: on a
$1.10B day (4.39M sh ≈ 1.31% of float), the **mega tier (≥$10M) is a net SELLER —
buy_ratio 0.401** (345K bought vs 516K sold, $216.8M, 13 trades) — i.e. the
*largest* institutional blocks are **distributing into the +6.84% post-earnings
pop**, while the smaller large tier nibbles (buy_ratio 0.529) and the block tier
is balanced (0.494). The biggest individual prints are a cluster of
closing-auction / post-close blocks at the **$255.55 close** (125.6K, 111.7K,
97.5K, 64K sh at 16:00–16:11 ET) — size changing hands right at the top of the
day. This is a **distribution-into-strength signature** that lines up cleanly with
phase-1 (the $14M bid-side call sale + near-the-money put hedging): big money is
trimming the post-earnings rally, not chasing it.

## Key signals

- **Mega tier NET SELLER — buy_ratio 0.401** (516K sold vs 345K bought, $216.8M,
  13 trades) `[DP:block-stratified]`. The cleanest distribution read in the data.
- **Smaller tiers diverge from the whales** — large tier 0.529 (slight buy),
  block tier 0.494 `[DP:block-stratified]`: retail/mid-size buying *from* the
  mega-tier sellers = classic distribution-into-strength.
- **Closing-auction blocks at the high** — 125.6K @ $255.55, 111.7K @ $255.54,
  97.5K @ $255.55 (16:00–16:11 ET) `[DP:largest]` `[DP:extended-hours]`: heavy
  size printed at the day's top, consistent with MOC distribution.
- **Largest block 0.0375% of float** (125.6K / 334.88M) `[DP:block_pct_float fz]`
  — individually modest for a $88B mega-cap; the *net mega-tier selling* is the
  signal, not any one print.
- **SNOW absent from DP top-30** `[DP:ticker-summary]` — $1.1B is large in
  absolute terms but the board is dominated by ETFs/larger mega-caps.

## Detailed findings

### Largest blocks
| Time (ET) | Price | Size | Premium | NBBO | Read |
|---|---|---|---|---|---|
| 16:04 | $255.55 | 125,600 | $32.1M | 255.5 / 256.0 | closing-auction, at/below ask |
| 16:04 | $255.54 | 111,709 | $28.5M | 255.5 / 255.98 | closing block |
| 16:05 | $255.55 | 97,500 | $24.9M | 255.1 / 255.5 | **at ask** |
| 16:00 | $255.55 | 64,338 | $16.4M | 255.0 / 256.3 | close |
| 10:37 | $250.47 | 63,167 | $15.8M | 250.52 / 251.96 | **below bid — sell** |
| 12:06 | $248.83 | 63,500 | $15.8M | 248.6 / 248.83 | at ask |
| 09:08 | $239.20 | 50,800 | $12.2M | 238.25 / 240.0 | midpoint (early, low) |

### Tier breakdown
| Tier | Buy ratio | Premium | Trades | Read |
|---|---|---|---|---|
| **Mega (≥$10M)** | **0.401** | $216.8M | 13 | **net distribution** |
| Block (≥$1M) | 0.494 | $324.8M | 132 | balanced |
| Large (≥$100K) | 0.529 | $558.4M | 2,687 | slight buy (smaller players) |
| Total | — | $1,099.9M | — | net seller at the top |

### Price levels (S/R)
- **Resistance / battle zone: $255–$256** (the close; massive MOC size printed
  here — supply is being absorbed/distributed at the top).
- **Support shelf: $248–$251** (intraday blocks).
- **Lower support: $239–$244** (early-session blocks the stock rallied from).

### Extended-hours activity
The biggest prints are the 16:00–16:11 ET closing-auction blocks at $255.55 —
post-earnings MOC distribution, not a fresh overnight directional block.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `dark-pool largest` | `--sort-by premium --top-n 18` | closing blocks at $255.55 |
| `dark-pool block-stratified` | `--min-tier large` | **mega 0.401 (sell)**, large 0.529 |
| `dark-pool ticker-summary` | `--top-n 30` | SNOW absent (ETF-dominated board) |
| `dark-pool extended-hours` | `--top-n 6` | MOC blocks at the close |

## Tool errors
(none)

## Verdict for downstream

- **Bias: MILD-TO-MODERATE DISTRIBUTION** — mega-tier net seller (0.401) into the
  +6.84% rally, with closing-auction size at the $255.55 top. Confirms phase-1's
  cautious read; institutions are trimming, smaller players are buying.
- **Conviction: 3 / 5** — clean tier divergence (whales sell, retail buys), the
  textbook distribution-into-strength tell, though no single print is float-moving.
- **Largest block 0.0375% of float** (advisory) — the *net mega-tier flow*
  matters, not size.
- **Three S/R levels for phase-9:**
  1. **Resistance $255–$256** (close / MOC distribution zone) — the cap to clear.
  2. **Support $248–$251** (intraday shelf).
  3. **Lower support $239–$244** (the gap-up base).
- **Open questions:**
  - Does dealer structure (phase-4) confirm a pin / cap near $255, or is there
    room above if the distribution is absorbed?
  - Is the mega-tier selling outright distribution or hedging of long stock
    (covered-call writing seen in phase-1)? Either way it caps upside near term.
