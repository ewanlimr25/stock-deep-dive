# Phase 2 — Dark Pool & Block Prints

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T01:20:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

DOCN's off-exchange tape is **balanced-to-mildly-distributive**, not accumulation.
Total dark-pool premium is **$45.77M** (388,489 shares, avg $117.43) — but the
block tier is **50/50** (buy_ratio 0.501) and the large tier is **mildly
sell-side** (buy_ratio 0.468 → sell 0.532), with **no mega-tier prints at all**.
Executions cluster **at/just-below spot** (~$117–119) with avg price ($117.43)
below the ~$119 close. DOCN is **not in the dark-pool top-30** (dominated by
SPY/MU/QQQ/SNDK/NVDA), and even the two largest blocks (~38.6K shares, ~$4.6M
each) are **0.037% of shares** — modest size for a ~104M-share name. This does not
confirm the mild bullish tilt phase-1 flagged; if anything it leans neutral-to-soft.

## Key signals

- Total DP premium **$45.77M** / 388,489 sh / avg **$117.43** `[DP:block_stratified]`
  — but `[DP:ticker_summary]` says DOCN is **NOT in top-30** (busy-name baseline).
- **Block tier buy_ratio 0.501** ($30.6M, 13 trades) — dead balanced `[DP:block_stratified]`.
- **Large tier buy_ratio 0.468** (sell 0.532; $15.1M, 68 trades) — mild
  distribution `[DP:block_stratified]`. **No mega tier** (0 trades).
- Biggest 5-day price cluster is **$117.02 ($38.1M)** — support just below spot;
  upside supply at **$123.3 ($17.3M)** and **$126.3 ($20.6M)** `[DP:price_levels]`.
- Two ~38.6K-share blocks (~$4.6M each) printed **post-market at $118.91**
  (20:48 & 21:09 UTC) `[DP:extended_hours]` — a late paired cross, below-mid vs a
  wide/stale NBBO, not a clean aggressive lift.

## Detailed findings

### Largest blocks (today) `[DP:largest]`

| Time (UTC) | Price | Size | Premium | NBBO | Aggressor* |
|-----------|-------|------|---------|------|-----------|
| 21:09:57 | 118.91 | 38,666 | $4.60M | 118.2/125 | blw_mid (wide NBBO) |
| 20:48:39 | 118.91 | 38,523 | $4.58M | 118.2/125 | blw_mid (wide NBBO) |
| 16:29:46 | 119.20 | 32,400 | $3.86M | 118.62/119 | **LIFT** (buy) |
| 15:21:48 | 118.09 | 31,093 | $3.67M | 117.47/118.09 | **LIFT** (buy) |
| 20:00:24 | 118.91 | 17,700 | $2.10M | 118.2/125 | blw_mid |
| 16:30:12 | 119.17 | 17,400 | $2.07M | 118.93/119.36 | abv_mid |
| 16:29:57 | 119.02 | 15,000 | $1.79M | 118.82/119.31 | blw_mid |
| 15:00:04 | 116.75 | 13,400 | $1.56M | 116.42/117.03 | abv_mid |

*NBBO-probabilistic. The 118.91 post-market prints show a wide 118.2/125 quote
(the 125 ask is stale) so "blw_mid" there is unreliable — treat as neutral crosses.
The two intraday **LIFTs** at 15:21 and 16:29 (~$7.5M combined) are the cleanest
buy-side signal; offset by abv/blw-mid crosses.

### Tier breakdown `[DP:block_stratified]`

| Tier | buy_ratio | derived sell | buy_vol | sell_vol | premium | trades |
|------|-----------|--------------|---------|----------|---------|--------|
| block | 0.501 | 0.499 | 129,693 | 129,389 | $30.62M | 13 |
| large | **0.468** | **0.532** | 60,510 | 68,897 | $15.15M | 68 |
| mega | — | — | 0 | 0 | $0 | 0 |
| retail | — | — | 0 | 0 | $0 | 0 |

Highest active tier = **block** (no mega conviction prints). Net read: balanced
block flow, mildly sell-leaning large flow → **not accumulation.**

### Price levels (5-day clusters, anchored to 2026-07-17) `[DP:price_levels]`

| Level | Premium | Trades | vs spot (~$119) |
|-------|---------|--------|-----------------|
| **$117.02** | $38.07M | 4 | support (−1.8%) |
| $119.65 | $35.20M | 7 | at spot |
| **$126.30** | $20.56M | 8 | resistance (+6.0%) |
| $115.00 | $15.76M | 1 | support (−3.5%) |
| $118.91 | $13.68M | 9 | at spot (post-mkt cross) |
| **$123.32/123.31** | $17.26M | 10 | resistance (+3.5%) |
| $132.20 | $3.44M | 2 | far resistance |

Window covers 5 sessions (7/13–7/17); cross-checked against phase-0 available-dates
(contiguous, no gap in this window). Clusters frame a **$115–$117 floor and
$123–$126 ceiling** around a ~$119 pivot.

### Extended-hours activity `[DP:extended_hours]`

Heavy post-market concentration **at exactly $118.91** (20:00–21:09 UTC): the two
38.6K blocks plus a stack of smaller prints, ≈$13.7M in the top rows. Single-price
clustering at 118.91 = a **closing/post-close cross**, likely portfolio-level, not
directional intent — de-rate as a signal.

### Float normalization (advisory) `[DP:block_pct_float fz]`

`fz` returned a **null Shs Float** for DOCN (phase-0), so this is derived:
market cap $12.41B / spot $119.17 ≈ **104M shares**. Largest block 38,666 =
**0.037%** of shares; entire day's DP 388,489 sh = **0.373%**. Interpretation:
these block sizes are **not meaningful conviction for a name this size** — reinforces
`BUSY_NAME_NORMAL_DAY`. (Advisory only; does not raise conviction.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `dark-pool largest --sort-by premium --top-n 25` | 38,666@118.91 $4.60M ← `.results[0]` | top-8 |
| `dark-pool block-stratified --min-tier large` | block buy 0.501, large buy 0.468 ← `.results[0].{block,large}.buy_ratio` | all tiers |
| `dark-pool price-levels --days 5` | $117.02 $38.07M ← `.results[0].{price_level,total_premium}` | 12 |
| `dark-pool extended-hours --top-n 15` | EH top prem $13.68M ← `[.results[].premium]\|add` | top-8 |
| `dark-pool ticker-summary --top-n 30` | DOCN NOT in top-30 ← `[.results[].ticker]\|index("DOCN")` | — |

## Tool errors

(none — all five calls returned valid JSON on first read)

## DATA NOTE / CORRECTION

- `price-levels` price field is `.price_level` (not `.price`); re-read before
  transcription (first jq path returned null).
- Block sizes given as %-of-shares are **derived** (fz float null) — flagged advisory.

## Verdict for downstream phases

- **Institutional bias:** **Mixed / balanced, mild distribution lean** (large-tier
  buy 0.468, avg exec $117.43 below spot, no mega conviction).
- **Conviction:** **2/5** (balanced tiers, modest %-of-float, not a DP leader).
- **Largest block as % of float:** ≈**0.037%** (derived) — *not* meaningful size
  for a ~104M-share name; do not read the $4.6M blocks as institutional conviction.
- **Three S/R levels for phase-9:**
  1. **Support $117.0** (biggest 5d cluster $38M) → below it, $115 ($15.8M).
  2. **Pivot $118.9–119.7** (spot zone, $49M combined + post-mkt cross).
  3. **Resistance $123.3 → $126.3** ($17M / $20.6M supply overhead).
- **Open questions:** Do the $123–126 DP supply clusters line up with call OI walls
  (phase-3)? Does the mild large-tier selling reconcile with phase-1's put-writing
  at 115 (both consistent with a $115–120 range)? (phase-3/phase-4.)
