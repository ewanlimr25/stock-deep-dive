# Phase 2 — Dark Pool & Block Prints

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:00:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The mega-tier (≥$10M) dark-pool blocks are **86.7% buy-side** — on its face a
high-confidence accumulation signal. **But the read is heavily diluted by timing
and rank:** nearly every large block printed at **20:00Z (the 16:00 ET closing
auction)** at exactly $310.85, the signature of benchmark/MOC/rebalance execution
rather than intraday directional conviction; AAPL ranks only **14th** in
universe dark-pool premium today ($2.146B), dwarfed by semis (MU $17.2B, NVDA
$10.8B, SNDK); and the largest block (191k sh) is just **0.0013% of float**.
**Net: a mild accumulation lean, low conviction** — capped at `+` per phase-0.5's
`BUSY_NAME_NORMAL_DAY`. The constructive structural fact is the 5-day premium
clusters at **$302–305 (support, ~2–3% below spot)**, with today's close at the
top of that band.

## Key signals

- **Mega-tier (≥$10M) buy_ratio 0.867** (20 trades, $493.8M, buy 1.377M sh vs sell
  211k) — high-confidence buy skew per heuristic `[DP:block_stratified]`
- …but **concentrated in the 16:00 ET closing cross** (top 8 blocks all 20:00Z @
  $310.85) → benchmark/rebalance execution, de-rate directional meaning `[DP:extended_hours]`
- Block tier (≥$1M) buy_ratio **0.634**, large tier **0.551** — buy-leaning but
  only suggestive (0.55–0.7 band) `[DP:block_stratified]`
- 5-day institutional clusters: **$304.99 ($3.02B), $302.25 ($1.55B)** below spot;
  **$310.85 ($651M)** at spot — support stack 2–3% under price `[DP:price_levels]`
- AAPL **rank 14** in universe DP premium ($2.146B); semis lead (MU/NVDA/SNDK) —
  not a standout, consistent with phase-0.5 sector read `[DP:ticker_summary]`

## Detailed findings

### Largest blocks (top prints)

| Time (UTC) | Price | Size (sh) | Premium | NBBO | % of float |
|------------|-------|-----------|---------|------|-----------|
| 20:00:17 | 310.85 | 191,407 | $59.5M | 310.67/310.79 | 0.0013% |
| 20:00:22 | 310.85 | 143,319 | $44.6M | 310.75/310.79 | 0.0010% |
| 20:00:06 | 310.85 | 132,000 | $41.0M | 310.81/310.88 | 0.0009% |
| 20:00:23 | 310.85 | 128,830 | $40.0M | 310.75/310.79 | 0.0009% |
| 20:00:10 | 310.85 | 109,669 | $34.1M | 310.67/310.83 | 0.0007% |
| 15:46:58 | 310.85 | 61,747 | $19.2M | 310.80/310.84 | 0.0004% |

**Float context (advisory, `fz` float 14.67B):** the single largest block is
**0.0013% of float**; the entire mega-tier buy volume (1.377M sh) is **0.0094% of
float** `[DP:block_pct_float fz]`. For a 14.67B-float name, $2.1B/day of dark pool
and $59M blocks are **routine** — the size is not "conviction" the way it would be
in a thin name. This caps how much weight the buy skew can carry.

### Tier breakdown (buy/sell)

| Tier (boundary) | buy_ratio | buy_vol | sell_vol | premium | trades |
|-----------------|-----------|---------|----------|---------|--------|
| mega (≥$10M) | **0.867** | 1,376,900 | 211,474 | $493.8M | 20 |
| block (≥$1M) | 0.634 | 811,946 | 468,422 | $398.3M | 183 |
| large (≥$100k) | 0.551 | 2,219,957 | 1,808,298 | $1,253.6M | 5,377 |
| **all tiers** | — | — | — | **$2,145.7M** | — |

The buy skew **strengthens with tier size** (0.55 → 0.63 → 0.87), which normally
reads as institutions accumulating. **The caveat:** the mega tier is only 20
trades and is dominated by the closing cross (see below), so the 0.867 rests on a
handful of benchmark-execution prints, not a day-long accumulation pattern.

### Price levels (5-day clusters)

| Level | 5d premium | trades | vs spot ($310.85) |
|-------|-----------|--------|-------------------|
| 304.99 | $3.02B | 142 | −1.9% (support) |
| 302.25 | $1.55B | 148 | −2.8% (support) |
| **310.85** | $651M | 185 | at spot (today) |
| 308.82 | $508M | 126 | −0.7% |

Heaviest institutional volume over the window is **$302–305, 2–3% below spot**.
Today's prints pushing to $310.85 (top of the band) is consistent with a *mild*
"paying up from support" accumulation read — but spot is now stretched to the
upper edge of where size actually traded. (Caveat: `--days 5` anchors to latest
available date, not `--date`; window = 2026-05-20→27 per phase-0 dates.)

### Extended-hours activity

The "extended-hours" tool returns the **closing-auction cluster** (20:00:00–
20:03:51Z @ $310.85). These are not pre-market accumulation — they are 16:00 ET
closing-cross prints. On a mega-cap, a closing-cross block cluster is frequently
**index/ETF rebalance or MOC imbalance execution**, not directional intent. This
is the single most important de-rate on this phase's signal. No genuine
pre-market (12:00–13:30Z) directional block stands out.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol AAPL --sort-by premium` | top blocks all 20:00Z @ $310.85 (closing cross) |
| `uw dark-pool block-stratified --min-tier large` | mega buy 0.867 / block 0.634 / large 0.551 |
| `uw dark-pool price-levels --days 5` | clusters $302–305 (support); $310.85 at spot |
| `uw dark-pool extended-hours` | = closing-cross prints, not pre-market |
| `uw dark-pool ticker-summary --top-n 30` | AAPL rank 14 ($2.146B); semis lead |

## Tool errors

None.

## Verdict for downstream

- **Net institutional bias:** **mild accumulation** (mega buy 0.867, tier skew
  rising with size) — but **low conviction**, materially de-rated by (a) closing-
  cross concentration, (b) rank 14 / mid-pack, (c) trivial % of float.
- **Conviction:** **2/5** (capped at `+` per phase-0.5; the 0.867 alone would be
  `++` but the timing + rank caveats pull it back).
- **Largest block as % of float:** 0.0013% (191k sh / 14.67B) — *not* meaningful
  for this name; routine mega-cap block. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **$304.99** — heaviest 5d cluster ($3.02B), primary support / stop reference.
  2. **$302.25** — secondary support ($1.55B), ~2.8% below spot.
  3. **$310.85** — today's close / at-spot cluster, the pivot; break-and-hold
     above = continuation, fade back into $305 = range.
- **Open questions:**
  - Does OI (phase-3) corroborate accumulation, or is the closing-cross buy skew
    just rebalance flow with no options-OI footprint?
  - Are the phase-1 protective 12/2027 LEAP puts hedging these block longs (collar)?
  - Confirms phase-1: the *underlying* tape is also mid-pack/two-way — no
    standout single-name positioning. Phases 1–2 jointly: mild bullish, low conviction.
