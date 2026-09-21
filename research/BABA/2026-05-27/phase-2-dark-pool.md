# Phase 2 — Dark Pool & Block Prints

**Ticker:** BABA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:12:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool activity is **mixed with a mild block-tier accumulation lean at
support, beneath a heavy overhead supply shelf**. $131.2M total printed across
506 trades (avg $127.67), but there were **no mega-tier (≥$10M) blocks** — the
smart-money tier present today is the **block tier (≥$1M): buy_ratio 0.667**
(177,911 buy vs 88,914 sell, $34.0M) `[DP:block_stratified]`, while the bulk
**large tier is balanced (buy_ratio 0.522)**. The two biggest prints were
**extended-hours buys** (49,700 @ $126.59 pre-market lift, 40,600 @ $127.88
post-close) `[DP:extended_hours]`. Crucially, the **5-day price-level node sits at
$129–131 — above spot ($127.66)** — i.e. recent institutional VWAP is now
**overhead supply** that price has fallen through `[DP:price_levels]`. BABA is
**outside the top-50 dark-pool names today**, confirming phase-0.5's
`BUSY_NAME_NORMAL_DAY`. Reconciled with phase-1's two-sided premium selling, the
coherent read is **long-stock accumulation at support + covered-call overwriting**
— range-bound/income behavior, not aggressive directional conviction.

## Key signals

- **Block-tier buy_ratio 0.667** ($34.0M, 12 trades) — suggestive accumulation
  (0.55–0.70 band) `[DP:block_stratified]`.
- **No mega-tier blocks**; large tier balanced (0.522, $97.3M, 494 trades) — bulk
  flow is two-sided `[DP:block_stratified]`.
- **5-day supply node $129–131** (sum >$45M across 129.0–131.5 clusters) sits
  **above** spot $127.66 = overhead resistance `[DP:price_levels]`.
- **Extended-hours buys**: 49,700 @ $126.59 (pre-market, at/above ask), 40,600 @
  $127.88 (post-close, near ask) — accumulation-leaning `[DP:extended_hours]`.
- **BABA outside top-50 dark-pool names** today — light/normal session
  `[DP:ticker_summary]`.

## Detailed findings

### Largest blocks (NBBO-classified) `[DP:largest]`

| time(ET) | price | size | $M | NBBO | read |
|----------|------:|-----:|---:|------|------|
| 09:20 (pre) | 126.59 | 49,700 | 6.29 | 126.40/126.70 | buy (>mid) |
| 09:31 | 126.59 | 45,000 | 5.70 | 126.40/126.59 | **buy (at ask)** |
| 16:03 (post) | 127.88 | 40,600 | 5.19 | 127.49/127.92 | buy (near ask) |
| 14:40 | 127.59 | 40,100 | 5.12 | 127.62/127.66 | **sell (<bid)** |
| 10:53 | 128.75 | 24,000 | 3.09 | 128.72/128.84 | neutral |

Top blocks lean buy (3 buys / 1 sell / 1 neutral), consistent with block-tier
0.667. All cluster $126.5–128.75 — right at spot, not above it.

### Tier breakdown `[DP:block_stratified]`

| tier | trades | $M | buy_ratio |
|------|-------:|---:|----------:|
| mega (≥$10M) | 0 | 0 | — |
| **block (≥$1M)** | 12 | 34.0 | **0.667** (suggestive accumulation) |
| large (≥$100k) | 494 | 97.3 | 0.522 (balanced) |
| all tiers | 506 | 131.2 | — |

Smart-money signal lives in the block tier today (no mega prints); its 0.667 buy
tilt is suggestive, not high-confidence (would need ≥0.70).

### Price levels — 5-day S/R clusters `[DP:price_levels]`

Window: 2026-05-27, -26, -22, -21, -20 (cross-checked vs phase-0 dates ✓).

| level | $M | shares | read vs spot $127.66 |
|------:|---:|-------:|------|
| **135.64** | 17.44 | 128,575 | overhead supply (single block, prior level) |
| 131.47 | 10.53 | 80,070 | **resistance (top of node)** |
| 130.00 | 10.39 | 79,906 | resistance |
| 130.03 | 7.89 | 60,670 | resistance |
| 129.90 | 7.54 | 58,072 | resistance |
| 129.5–129.0 | ~27 (sum) | — | **heaviest node = overhead supply** |
| **126.59** | 12.11 | 95,700 | **immediate support (today's buying)** |
| 127.59 / 127.88 | ~12 (sum) | — | at-spot churn |

Net: a thick institutional volume shelf at **$129–131** sits above price — this
is the level a long must reclaim and the level a short fades into. **$126.5** is
the immediate support where today's block buying landed.

### Extended-hours activity `[DP:extended_hours]`

The two largest prints of the day were extended-hours: a **49,700-share
pre-market lift @ $126.59** and a **40,600-share post-close buy @ $127.88**.
No overnight BABA catalyst is yet identified (phase-6 to confirm); absent news
these read as deliberate institutional positioning rather than reaction, and
lean accumulation.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol BABA --sort-by premium` | top blocks $126.5–128.75, buy-leaning |
| `uw dark-pool block-stratified --symbol BABA --min-tier large` | block 0.667 / large 0.522 / no mega |
| `uw dark-pool price-levels --symbol BABA --days 5` | supply node $129–131, support $126.5 |
| `uw dark-pool extended-hours --symbol BABA` | pre-market + post-close buys (2 largest prints) |
| `uw dark-pool ticker-summary` | BABA outside top-50 |
| `fz quote` (phase-0 float 2.40B) | block %-of-float = 0.002% (negligible) |

## Tool errors

(none — all green)

## Verdict for downstream

- **Bias:** **mixed, mild accumulation at support.** Block tier buying (0.667) at
  $126.5 + extended-hours buys, but no mega conviction and a heavy $129–131 supply
  shelf overhead. Reconciles with phase-1 as **long stock + covered-call
  overwriting** (range/income), not aggressive directional positioning.
- **Conviction:** **2 / 5.** No mega blocks, block tier only "suggestive,"
  BABA outside top-50 dark-pool names (light day), large tier balanced.
- **Largest block as % of float:** 49,700 / 2.40B = **0.002%** — negligible.
  For a 2.40B-float mega-cap, dark-pool block *size* is never the signal; the
  buy/sell ratio and price clustering are `[DP:block_pct_float fz]`.
- **Three S/R levels for phase-9:**
  1. **Support: $126.5** (immediate dark-pool cluster + today's block buying).
  2. **Resistance: $129–131** (heaviest 5-day node — overhead supply; reclaim
     level for any long).
  3. **Higher resistance: $135.6** (prior institutional block; aligns with the
     05-13 high $145.8 → $135 retrace).
- **Open questions:** Is the block buying at $126.5 genuine dip accumulation or
  the long leg of covered overwriting (phase-1 call selling)? Does OI/dealer
  positioning (phase-3/4) confirm a pin in the $126–131 range? Were the
  extended-hours prints news-driven (phase-6)?
