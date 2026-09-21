# Phase 2 — Dark Pool & Block Prints

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T19:56:00Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

ADBE printed **$657.8M of dark-pool premium across 815 trades** (2,550,984 shares,
avg $255.14) on 2026-05-29, and the tier classification is **strongly buy-skewed**:
**mega-tier buy_ratio 0.953** ($369.4M, 10 prints), **block-tier 0.87** ($114.9M,
52 prints), **large-tier 0.639** ($173.5M, 753 prints) [DP:block_stratified]. On
its face that is textbook **accumulation**. **The critical caveat:** the two
dominant prints — **498,166 sh and 430,554 sh ($129.1M + $111.6M = $240M)** —
executed at **20:12–20:17 UTC (16:12–16:17 ET), i.e. in the closing-auction window
at the $259.21 close, on a month-end Friday** [DP:largest][DP:extended_hours]. A
large share of the buy-skewed mega premium is therefore **closing-cross /
month-end-rebalance mechanical flow, not discretionary intraday accumulation**.
Net read: **accumulation-leaning but de-rated** — the genuine multi-session
institutional support shelf sits *below* spot at **238–245** [DP:price_levels],
while today's headline blocks are pinned to the close. Total prints = **0.63% of
float** (modest for a 403M-float name).

## Key signals

- **$657.8M DP premium / 815 trades**, mega buy_ratio **0.953**, block **0.87** —
  buy-skewed across institutional tiers [DP:block_stratified].
- Largest block **498,166 sh @ $259.21 = $129.1M** at 16:12 ET — a
  **closing-auction cross** (price = the official close), **0.124% of float**
  [DP:largest fz].
- #2 block **430,554 sh @ $259.19 = $111.6M** at 16:17 ET — also closing-window
  [DP:largest]. Together the top-2 = ~$240M, **~37% of the day's DP premium**,
  both at the close.
- **Multi-session (5-day) support clusters BELOW spot:** $16.6M @ **244.76**,
  $16.0M @ **238.24**, $12.2M @ **241.44** — the real institutional S/R, not
  today's MOC prints [DP:price_levels].
- **No genuine pre/post-market block activity** — `extended-hours` returns the
  same 16:00–16:17 ET closing-window prints, i.e. auction, not overnight
  conviction [DP:extended_hours].

## Detailed findings

### Largest blocks — `[DP:largest]`

| Time (ET) | Size (sh) | Price | Premium | NBBO (bid/ask) | % float | Read |
|-----------|-----------|-------|---------|----------------|---------|------|
| 16:12:47 | 498,166 | 259.21 | $129.1M | 258.53 / 258.96 | 0.124% | closing cross @ close |
| 16:17:59 | 430,554 | 259.19 | $111.6M | 258.10 / 259.00 | 0.107% | closing window |
| 16:15:41 | 127,802 | 259.20 | $33.1M | 258.57 / 258.85 | 0.032% | closing window |
| 16:53:38 | 66,805 | 259.21 | $17.3M | 258.70 / 259.72 | 0.017% | post-close |
| 16:03:13 | 64,945 | 259.21 | $16.8M | 257.63 / 259.06 | 0.016% | post-close |
| 13:09:09 | 16,102 | 254.85 | $4.1M | 254.79 / 254.91 | 0.004% | **intraday** (genuine) |
| 11:50:00 | 15,000 | 256.06 | $3.8M | 256.06 / 256.18 | 0.004% | **intraday** (genuine) |

Most prints execute **at/above the NBBO mid** (price 259.21 vs NBBO mid ~258.7),
which is why the tier classifier reads them buy-side. But the timing — bunched at
16:00–16:17 ET on the close — marks them as **auction/MOC**, where "buy vs sell"
classification is least informative. The only clearly *discretionary intraday*
blocks are the 11:50 ($3.8M @ 256.06) and 13:09 ($4.1M @ 254.85) prints, both
small and below the close.

### Tier breakdown — `[DP:block_stratified]`

| Tier | Premium | Buy vol | Sell vol | Buy ratio | Trades |
|------|---------|---------|----------|-----------|--------|
| mega (≥$10M) | $369.4M | 1,358,446 | 66,805 | **0.953** | 10 |
| block (≥$1M) | $114.9M | 387,394 | 57,951 | **0.870** | 52 |
| large (≥$100k) | $173.5M | 434,486 | 245,902 | **0.639** | 753 |
| retail (<$100k) | $0 | 0 | 0 | 0.50 | 0 |
| **all tiers** | **$657.8M** | | | | **815** |

The buy-skew weakens as you move from mega (0.95, but auction-contaminated) to
large (0.64, the broad discretionary tape). The large-tier 0.64 is the most
trustworthy directional read here — **mildly buy-skewed discretionary flow**,
consistent with phase-1's net-bullish options tape but not a screaming bid.

### Price levels (institutional S/R) — `[DP:price_levels]`

**Today (days=1):** premium concentrates at the close — 259.21 ($300.4M),
259.19 ($117.0M), 259.20 ($57.5M) — i.e. the closing cross dominates. Below that,
today's genuine intraday levels: 252.34, 254.85–254.98, 246.99.

**5-day clusters (multi-session S/R):** the durable institutional levels are
**244.76** ($16.6M), **238.24** ($16.0M), **241.44** ($12.2M), **240.70**
($3.9M), **239.30** ($2.9M), **238.75** ($2.8M) — a clear **238–245 accumulation
shelf below spot**. This is the level phase-9 should treat as institutional
support, not the 259.21 MOC print.

### Extended-hours activity — `[DP:extended_hours]`

Returns the **same 16:00–16:17 ET closing-window prints** (498k/430k/128k blocks).
There is **no true overnight/pre-market conviction print** — the "extended" rows
are the closing auction, reinforcing the mechanical read rather than a news-driven
overnight move.

### Cross-name context — `[DP:ticker_summary]`

ADBE does **not** rank in today's DP top-5 (NVDA $18.2B, MU $17.3B, SPY $13.4B,
MSFT $8.2B, QQQ $7.3B). $657.8M is a meaningful but not extraordinary DP day for a
mega-cap — consistent with phase-0.5's "directionally unusual, normally-sized."

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw dark-pool largest --symbol ADBE --top-n 25 --sort-by premium --date 2026-05-29` | top = 498k sh $129.1M @259.21 closing cross |
| `uw dark-pool block-stratified --symbol ADBE --top-n 30 --min-tier large --date 2026-05-29` | mega 0.953 / block 0.87 / large 0.639; all-tier $657.8M |
| `uw dark-pool extended-hours --symbol ADBE --top-n 15 --date 2026-05-29` | same closing-window prints; no true overnight block |
| `uw dark-pool price-levels --symbol ADBE --top-n 15 --days 5` (+ `--days 1`) | close-pinned today; 238–245 multi-day support shelf |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-05-29` | ADBE outside top-5 (NVDA/MU/SPY/MSFT/QQQ lead) |

## Tool errors

- `uw dark-pool price-levels` does not accept `--date`; `--days` anchors to the
  latest available session (2026-05-29 = latest local), so the read is as-of-correct
  this run but **not as-of-reproducible** after a new session lands (window slides).

## Verdict for downstream phases

- **Net institutional bias:** **ACCUMULATION (de-rated)** — tier classification is
  buy-skewed (mega 0.95 / block 0.87 / large 0.64), but ~37% of premium is
  closing-auction/month-end mechanical flow at the 259.21 close, so the
  discretionary signal is the large-tier 0.64, not the headline mega 0.95.
- **Conviction:** **3 / 5.** Real buy-lean, materially discounted for
  auction/month-end contamination and the absence of genuine overnight conviction.
- **Largest block as % of float:** 498,166 sh = **0.124% of the 403.40M float**
  [DP:block_pct_float fz]; full-day 2.55M sh = **0.63% of float** — modest for this
  name; size alone does not signal high conviction here.
- **Three S/R levels for phase-9:**
  1. **Support 244–245** (DP cluster $16.6M @ 244.76; aligns with phase-3
     put_wall_support 245) [DP:price_levels].
  2. **Deeper support 238–241** (DP clusters $16.0M @ 238.24, $12.2M @ 241.44)
     [DP:price_levels].
  3. **Spot/pivot 259.21** = closing-cross magnet today; treat as near-term
     reference, not a conviction level [DP:largest].
- **Open questions:** Is the 238–245 shelf old accumulation (stale) or being
  refreshed? Does phase-4 GEX place the gamma flip near the 244–245 shelf
  (mechanical support) or above spot? Are institutions *writing calls* against
  these shares (phase-3 smart-positioning infers call selling) rather than adding
  a directional long?
