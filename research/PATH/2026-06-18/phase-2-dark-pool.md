# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:03:06Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool is **balanced with a slight distribution lean — it does NOT confirm phase-1's
bullish call flow.** The single biggest block (262,000 sh, $2.68M @ $10.235) printed
as a BUY, but it is only **0.067% of the 391.72M float** (negligible for this name),
and the dominant **large tier ($11.39M across 67 trades) is buy_ratio 0.48** (i.e.
sell_ratio 0.52 — slight net selling). No mega-tier prints. The heaviest 5-day price
clusters sit **above** current spot ($10.79 = $16.4M, $10.54–10.57) = **overhead
supply** now that price has rolled back to $10.27. PATH is **not in the DP top-30
names**. Net: institutional underlying activity is balanced, not accumulative — a
**yellow-flag divergence** against the bullish options tape.

## Key signals

- **Largest block a buy but tiny:** 262,000 sh @ $10.235, $2,681,570, **0.067% of float**,
  block-tier buy_ratio **1.0** [DP:largest][DP:block_pct_float fz].
- **Dominant tier mildly distributive:** large tier buy_ratio **0.48** (buy_vol 533,128
  vs sell_vol 578,611, $11.39M, 67 trades) [DP:block_stratified].
- **No mega tier:** mega buy_ratio 0.5 with 0 volume — no whale-sized conviction print [DP:block_stratified].
- **5-day clusters overhead:** $10.79 ($16.36M, 1.52M sh), $10.54–10.57, $10.77–10.78 —
  all **above** spot $10.27 = resistance/supply [DP:price_levels].
- **Closing-cross heavy:** extended-hours $3.76M / 366,554 sh, almost all at $10.27 in
  the 20:00–20:16Z (4:00–4:16pm ET) auction window — passive/cross, de-rated [DP:extended_hours].
- **Not a DP leader:** PATH absent from ticker-summary top-30 (led by SPY/MRVL/MU/NVDA/QQQ) [DP:ticker_summary].

## Detailed findings

### Largest blocks (float = 391.72M) — `[DP:largest]`

| time (Z) | px | size | premium | % float | NBBO |
|----------|----|------|---------|---------|------|
| 15:11:36 | $10.235 | 262,000 | $2,681,570 | 0.067% | [10.23–10.24] (BUY, at mid) |
| 20:00:49 | $10.27 | 58,573 | $601,545 | 0.015% | closing cross |
| 20:16:21 | $10.27 | 57,539 | $590,926 | 0.015% | closing cross |
| 20:08:38 | $10.2695 | 55,775 | $572,781 | 0.014% | closing cross |
| 18:37:48 | $10.31 | 29,103 | $300,052 | 0.007% | [10.30–10.31] |
| 13:30:14 | $10.16 | 27,064 | $274,970 | 0.007% | open print |

Even the largest block is 0.067% of float; the largest 5-day cluster (1.52M sh) is
0.39% of float — **no single print is meaningful conviction for this large-float name.**

### Tier breakdown — `[DP:block_stratified]`

| tier | buy_ratio | derived sell_ratio | buy_vol | sell_vol | premium | trades |
|------|-----------|--------------------|---------|----------|---------|--------|
| mega | 0.50 | 0.50 | 0 | 0 | $0 | 0 (none) |
| block | **1.00** | 0.00 | 262,000 | 0 | $2.68M | 1 |
| large | **0.48** | **0.52** | 533,128 | 578,611 | $11.39M | 67 |

The premium-dominant **large** tier is slightly distributive (0.48). The one block-tier
buy is real but a single print. Net: balanced-to-slight-sell.

### Price levels (5-day clusters; spot $10.27) — `[DP:price_levels]`

dates_covered: 2026-06-12, 15, 16, 17, 18.

| price_level | premium | shares | trades | vs spot |
|-------------|---------|--------|--------|---------|
| **$10.79** | $16.36M | 1,516,080 | 34 | **+5.1% overhead** |
| $10.77 | $7.49M | — | 71 | +4.9% overhead |
| $10.78 | $6.03M | — | 55 | +5.0% overhead |
| $10.54–10.57 | ~$19.5M (3 levels) | — | 173 | +2.6–2.9% overhead |
| $10.53 | $6.30M | — | 52 | +2.5% overhead |
| **$10.23** | $8.21M | — | 5 | **−0.4% (support, big blocks)** |

Heavy supply overhead at **$10.53–10.57 and $10.77–10.79**; nearest support is the
**$10.23** block zone (where today's 262k buy printed). Price has retraced from the
$10.5–10.8 transaction zone down to $10.27.

### Extended-hours — `[DP:extended_hours]`

$3.76M / 366,554 sh, concentrated 20:00–20:16Z at $10.27 = **closing-auction cross**,
plus one 21:06Z print ($10.28, 16,600). Treat as passive/index cross, **not directional
accumulation** — de-rated. No pre-market prints flagged.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|---------------------|------|
| `dark-pool largest --symbol PATH --sort-by premium --date 2026-06-18` | 262k @ $10.235 $2.68M ← `.results[0]` | 25 |
| `dark-pool block-stratified --min-tier large --date 2026-06-18` | large buy_ratio 0.48; block 1.0; mega 0/none ← `.results[].{large,block,mega}.buy_ratio` | 1 |
| `dark-pool extended-hours --date 2026-06-18` | $3.76M closing cross @ $10.27 ← `sum(.results[].premium)` | 15 |
| `dark-pool price-levels --days 5` (no --date; anchors latest=2026-06-18) | $10.79 $16.36M overhead ← `.results[].price_level/total_premium` | 15 |
| `dark-pool ticker-summary --date 2026-06-18` | PATH absent top-30 ← `.results[]` | 30 |

## Tool errors

_none_

## DATA NOTE / CORRECTION

`price-levels` price field is `price_level` (not `price`); first jq used `.price` →
null, re-read with `.price_level`. Values above are from the corrected path. All
round-tripped through `jq`.

## Verdict for downstream

- **Institutional bias:** **Mixed / balanced, slight distribution** — NOT clean accumulation.
- **Conviction:** **2/5** (one block-tier buy vs a slightly distributive large tier; no
  mega print; heavy clusters overhead; closing-cross-dominated; not a DP-leader name).
- **Largest block as % of float:** 0.067% (262k / 391.72M) — **negligible**; size is not
  meaningful conviction for PATH's large float. [DP:block_pct_float fz]
- **Three S/R levels for phase-9:**
  1. **Support $10.23** (today's 262k buy + 5-day $8.21M cluster) — nearest floor.
  2. **Resistance $10.53–10.57** (heavy 5-day clusters, ~$19.5M) — first overhead supply.
  3. **Resistance $10.77–10.79** (heaviest 5-day cluster $16.36M) — major supply cap.
- **Open questions:** The bullish call flow (phase 1) is **not** backed by underlying
  accumulation — is the options bid squeeze-positioning into the 31.78% short float rather
  than fundamental institutional buying? Resolve via dealer positioning (phase 3/4) and the
  7c short-interest gate. Why are the heaviest DP clusters overhead — trapped longs or
  defended supply?
