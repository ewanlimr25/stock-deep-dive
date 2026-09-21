# Phase 2 — Dark Pool & Block Prints

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark-pool headline ("mega tier 100% buy, $48M") **does not survive scrutiny** and
should be de-rated to neutral/mild-distribution. Two facts dismantle it: (1) the
"$48M mega" is a **single 314,700-share block ($24M) reported twice** 6 seconds apart
at 16:03 ET — de-duped, there is exactly one mega print; (2) the off-exchange *buying*
is **entirely the 16:00 ET closing auction** (94.8% above mid on $62M of close/AH
prints), while the **regular intraday session leaned to the sell side** (only 40.8%
above mid on $208M). Stripped of closing-cross mechanics, HOOD's dark-pool day was
mildly distributive, not accumulative. HOOD did **not** rank in today's dark-pool
top-50, and the single mega block is **0.041% of float** — routine for a 761M-share
name. **Verdict: MIXED, mild intraday distribution; closing-auction "buy" de-rated.**

## Key signals

- **De-duped mega = ONE 314,700-sh block @ $24.0M** (76.23), not $48M — the tool
  double-counted two identical 16:03 ET prints [DP:largest][DP:dedup DUCKDB].
- **Session split:** close/AH (16:00 ET+) $62.2M @ **94.8% abv mid** vs regular
  intraday $207.6M @ **40.8% abv mid** [DP:session_split DUCKDB] — the "buying" is the
  closing cross; the trading day was net offered.
- Block-tier (≥$1M) buy_ratio 0.67, large-tier (≥$100k) 0.546 — *mild* buy, below the
  ≥0.55 "suggestive" line for large tier [DP:block_stratified].
- 5-day price clusters: **75.76** ($115.8M, top cluster), **76.23** ($62.2M, =spot),
  **73.64** ($23.4M, lower support) [DP:price_levels].
- HOOD **outside dark-pool top-50** today; mega block **0.041% of float**
  [DP:ticker_summary][DP:block_pct_float fz] — not a standout, not meaningful for the name.

## Detailed findings

### Largest blocks (table)

| Time (ET) | Price | Size | Premium | NBBO | Read | % float |
|-----------|-------|------|---------|------|------|---------|
| 16:03:44 | 76.23 | 314,700 | $24.0M | 76.09/76.30 | abv mid — **dup of next** | 0.041% |
| 16:03:50 | 76.23 | 314,700 | $24.0M | 76.09/76.30 | **same block re-reported** | (dup) |
| 09:56 | 73.86 | 37,872 | $2.80M | 73.82/73.87 | early, near bid | 0.005% |
| 16:00:18 | 76.23 | 24,777 | $1.89M | 76.13/76.34 | closing cross | 0.003% |
| 16:00:11 | 76.23 | 20,698 | $1.58M | 76.13/76.20 | closing cross | 0.003% |
| 10:52 | 75.88 | 19,500 | $1.48M | 75.89/75.92 | near bid (sell-lean) | 0.003% |
| 13:22 | 75.385 | 17,900 | $1.35M | 75.37/75.40 | near bid (sell-lean) | 0.002% |

DuckDB de-dup of all prints ≥$10M returns **one distinct row**: 314,700 sh / $23.99M /
76.23 [DP:dedup DUCKDB]. So the block-stratified "mega buy_volume 629,400 / $47.98M /
buy_ratio 1.0" is a **double-count of a single block** — treat mega as one $24M print.

### Tier breakdown (single-day) [DP:block_stratified]

| Tier (boundary) | Trades | Premium | buy_ratio | Note |
|-----------------|--------|---------|-----------|------|
| mega (≥$10M) | 2 | $47.98M | 1.00 | **really 1 block, $24M** (dup) |
| block (≥$1M) | 9 | $13.57M | 0.67 | mild buy |
| large (≥$100k) | 1,040 | $212.12M | 0.546 | barely buy-side |
| retail (<$100k) | 0 | $0 | — | — |
| **all tiers** | 1,051 | **$273.67M** | — | matches insights DP total |

Large tier (the bulk, $212M) is 0.546 buy — below the 0.55 "suggestive" threshold,
i.e. effectively balanced. Only the (de-rated) mega and the small 9-trade block tier
show a buy lean.

### Session split (the decisive cut, DuckDB) [DP:session_split DUCKDB]

| Session (ET) | Trades | Shares | Premium | % above mid |
|--------------|--------|--------|---------|-------------|
| 16:00+ (close/auction) | 32 | 815,521 | $62.17M | **94.8%** |
| regular intraday | 1,004 | 2,752,367 | $207.62M | **40.8%** |
| pre 09:00 | 15 | 52,388 | $3.88M | 28.2% |

The whole-day 52.8%-above-mid average masks a regime: **buying is concentrated in the
closing cross** (MOC/auction/passive mechanics at the official 76.23 close), while the
**actual trading day printed 40.8% above mid → ~59% at/below mid (net offered).** Per
the phase-2 pitfall, closing-auction/extended-hours prints are de-rated for directional
intent. The directional read of the *intraday* dark pool is **mild distribution**.

### Price levels (5-day clusters; window ~2026-05-20→27) [DP:price_levels]

| Level | Premium | Shares | vs spot (76.23) |
|-------|---------|--------|------------------|
| **75.76** | $115.8M | 1,528,458 | −0.6% (just below — support) |
| 76.23 | $62.2M | 815,679 | at spot (closing cluster) |
| 73.64 | $23.4M | 317,133 | −3.4% (lower support) |
| 75.92 | $18.2M | 239,283 | −0.4% |
| 74.51 | $10.0M | 134,805 | −2.3% |
| 75.00 | $9.0M | 120,165 | −1.6% (round-number) |

The dominant 5-day institutional level is **75.76** (1.53M shares) — directly below
spot, the natural support/pivot. **73.64** is the next shelf down. Overhead, 76.23 is
the closing-cluster (more mechanical than conviction).

### Extended-hours activity [DP:extended_hours]

15 of the top extended/AH prints land at **20:00–20:03 UTC = 16:00–16:03 ET** (the
close), all at 76.23 — i.e. the closing auction, not genuine pre/post-market
positioning. One pre-market-ish print (09:56, 73.86) printed near the bid. Nothing
here reads as directional overnight conviction; it is auction plumbing.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol HOOD --top-n 25 --sort-by premium --date 2026-05-27` | top = 2× 314,700 @76.23 (dup), then 37,872 @73.86 |
| `uw dark-pool block-stratified --symbol HOOD --top-n 30 --min-tier large --date 2026-05-27` | mega buy_ratio 1.0 (dup-inflated), large 0.546 |
| `uw dark-pool price-levels --symbol HOOD --top-n 15 --days 5` | top cluster 75.76 $115.8M; 76.23, 73.64 |
| `uw dark-pool extended-hours --symbol HOOD --top-n 15 --date 2026-05-27` | bulk at 16:00–16:03 ET closing auction |
| `uw dark-pool ticker-summary --top-n 50 --date 2026-05-27` | HOOD not in top 50 |
| DuckDB dedup (≥$10M) + session-split by ET hour | 1 distinct mega; close 94.8% vs intraday 40.8% abv mid |

## Tool errors

None (price-levels/ticker-summary initially parsed with wrong jq field names — keys
are `price_level`/`total_premium`/`total_shares` and `ticker`; re-run succeeded).

## Verdict for downstream

- **Institutional bias:** **MIXED → mild intraday DISTRIBUTION.** The accumulation
  signal is an artifact (double-counted mega + closing-auction buying). Regular-session
  dark pool was net offered (40.8% above mid).
- **Conviction:** **2/5** (low; size unremarkable, signal de-rated, name not a DP leader).
- **Largest block as % of float:** **0.041%** (one $24M block) — *not meaningful for a
  761M-share float*; advisory de-rate, never a conviction add [DP:block_pct_float fz].
- **Three S/R levels for phase-9:**
  1. **75.76** — dominant 5-day institutional level, ~0.6% below spot → first support/pivot.
  2. **73.64** — lower institutional shelf, ~3.4% below → deeper support / stop reference.
  3. **76.23 / 75.92** — closing-cluster / overhead; price must reclaim and hold above
     76.2 (with *intraday*, not just auction, prints) to confirm any upside.
- **Open questions:**
  - Does dealer positioning (phase-3/4) put a gamma wall near 75–76 that explains the
    75.76 magnetism, or is it organic support?
  - Phase-1's one clean bullish print (Dec-18 75C $1.82M @15:30 ET / 19:30Z) — no
    corroborating large dark-pool buy near that time intraday (intraday was offered),
    so the call buy is **not** dark-pool-confirmed.
