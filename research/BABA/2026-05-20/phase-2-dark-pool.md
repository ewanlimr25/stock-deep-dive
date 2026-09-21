# Phase 2 — Dark Pool & Block Prints

**Ticker:** BABA
**As-of date:** 2026-05-20 (data: 2026-05-19)
**Generated:** 2026-05-20T00:10:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md
**Spot reference:** $135.5–$135.7 intra-day; close ~$135.56 (see phase-1)

## Summary

Single-day dark-pool activity totals **$122.0M premium** across 477 prints in the
large+block tiers. Block-tier buy_ratio = **0.584** (mild buyer skew); large-tier
buy_ratio = 0.512 (balanced); **no mega-tier prints**. Tape buying on the day is
real but not aggressive. The much louder signal sits in the **5-session price-level
chart**: the dominant institutional clusters are at **$140.87 ($32.9M)**, **$145.81
($32.4M)** and **$144.15 ($23.2M)** — i.e., ABOVE current spot. BABA was distributed
out of that $140–$146 zone into the recent pullback, and a new but lighter
accumulation pocket is forming at **$133.40 / $134.50** ($6.4–$7.0M each, 19–23
trades — i.e. repeated VWAP imprints, not one-offs).

## Key signals

- Block-tier buy_ratio **0.584** on $27.76M / 16 trades (≥$1M each) — suggestive
  but not high-confidence accumulation [DP:block_stratified].
- Five-day institutional VWAP cluster: **$140.87 / $145.81 / $144.15** — $88.5M of
  combined premium **above** spot, defining overhead resistance [DP:price_levels].
- New lower cluster forming at **$133.40 (19 trades)** and **$134.50 (23 trades)**
  — emerging institutional support 1–2% below spot [DP:price_levels].
- Top single block: **21,128 shares @ $135.59** ($2.86M) printed **−5.5¢ vs mid**
  → seller-initiated; second-largest 20,500 @ $135.39 was **+5.5¢ vs mid** →
  buyer-initiated. Tape today is two-sided, not one-way accumulation [DP:largest].
- Pre-market ext-hours saw both buyers (e.g. 13:04Z $432K above NBBO ask) and
  sellers (e.g. 09:34Z $530K at NBBO bid) — confirming the same two-sided
  positioning that the options tape shows [DP:extended_hours].

## Detailed findings

### Block-stratified summary (single day)

| Tier | Trades | Premium | Buy vol | Sell vol | Buy_ratio | Read |
|------|-------:|--------:|--------:|---------:|----------:|------|
| Mega (≥$10M) | 0 | $0 | 0 | 0 | n/a | no super-blocks today |
| Block (≥$1M) | 16 | $27,755,854 | 119,354 | 85,128 | **0.584** | mild buyer skew (suggestive) |
| Large ($100K–$1M) | 461 | $94,266,078 | 355,557 | 339,159 | 0.512 | balanced |
| Retail | 0 | $0 | — | — | n/a | (BABA notional too large for retail tier) |
| **TOTAL** | **477** | **$122,021,932** | | | | |

Per the rubric (≥0.55 = suggestive, ≥0.7 = high-confidence), the block-tier
0.584 is suggestive only. No mega-tier participation today is the more important
fact — sovereign-scale buyers stayed home. [DP:block_stratified]

### Largest single blocks (top 10 of 25 returned)

| Time (UTC) | Price | Size | Premium | NBBO mid | vs Mid | Side |
|-----------|------:|----:|--------:|---------:|------:|------|
| 18:28:07 | $135.59 | 21,128 | $2,864,746 | $135.645 | −5.5¢ | sell |
| 14:17:13 | $135.39 | 20,500 | $2,775,495 | $135.335 | +5.5¢ | buy |
| 13:51:34 | $135.91 | 16,200 | $2,201,742 | $136.085 | −17.5¢ | **sell (heavy)** |
| 16:05:02 | $135.67 | 15,800 | $2,143,586 | $135.675 | −0.5¢ | neutral |
| 16:41:46 | $135.70 | 15,500 | $2,103,350 | $135.700 | 0 | at-mid |
| 15:00:43 | $135.51 | 13,700 | $1,856,419 | $135.505 | 0 | at-mid |
| 13:58:05 | $136.58 | 13,400 | $1,830,172 | $136.640 | −6.0¢ | sell |
| 14:13:40 | $135.39 | 13,200 | $1,787,148 | $135.355 | +3.5¢ | buy |
| 16:46:48 | $135.92 | 11,500 | $1,563,080 | $135.890 | +3.0¢ | buy |
| 14:07:49 | $135.89 | 10,800 | $1,467,612 | $135.830 | +6.0¢ | buy |

Across the top-25: 13 prints buyer-side, 8 prints seller-side, 4 prints at mid.
Buyer-side premium total ≈ **$15.1M**; seller-side premium total ≈ **$11.7M**.
**Net buyer-skew ≈ +$3.4M** of the $25M+ in single-block activity — directionally
positive but modest. [DP:largest]

### Price-level clusters (5 sessions: 2026-05-13 → 2026-05-19)

| Price level | Total premium | Shares | Trades | Position vs spot ($135.5) |
|-----------:|--------------:|-------:|------:|----|
| **$140.87** | **$32,870,957** | 233,337 | 6 | **+3.9% above** |
| **$145.81** | **$32,408,022** | 222,262 | 15 | **+7.6% above** |
| **$144.15** | **$23,212,619** | 161,031 | 5 | **+6.4% above** |
| $140.81 | $17,971,580 | 127,630 | 6 | +3.9% above |
| $145.91 | $8,310,302 | 56,955 | 7 | +7.7% above |
| $145.62 | $8,212,090 | 56,394 | 14 | +7.4% above |
| $143.55 | $7,891,515 | 54,974 | 7 | +5.9% above |
| $144.31 | $7,770,517 | 53,846 | 6 | +6.5% above |
| $143.45 | $7,304,747 | 50,922 | 9 | +5.9% above |
| $143.10 | $7,204,785 | 50,348 | 14 | +5.6% above |
| $144.35 | $7,075,741 | 49,018 | 6 | +6.5% above |
| **$133.40** | **$6,961,472** | 52,185 | **19** | **−1.6% below** |
| $134.85 | $6,718,901 | 49,825 | 5 | −0.5% below |
| $144.00 | $6,547,524 | 45,469 | **25** | +6.3% above |
| **$134.50** | **$6,440,406** | 47,884 | **23** | **−0.7% below** |

Interpretation:
- The two single biggest VWAP nodes ($140.87 and $145.81) hold $65M combined
  premium — these are **distribution / overhead supply** zones where BABA was
  worked off over the last week.
- The lower cluster at **$133.40 (19 trades) / $134.50 (23 trades) / $134.85**
  is the freshly forming **support zone** — multiple smaller prints repeatedly
  hitting the same band suggests active institutional bid-side accumulation
  *now*, even though aggregate notional is still smaller than the overhead.
- Bullish-flow phase-1 strikes $137–$140 and $145C LEAP **map directly** to the
  overhead DP supply — option buyers are betting the supply at $140 / $145 gets
  consumed. Phase 4 (dealer GEX) will determine whether dealer hedging amplifies
  or dampens that move.

[DP:price_levels]

### Extended-hours activity

13 ext-hours prints totaling **$3.12M** premium, all single-day. Mix:

| Time (UTC) | Premium | Price | NBBO bid/ask | Side read |
|-----------|--------:|------:|-------------:|----------|
| 09:34Z | $530,091 | 135.40 | 135.40 / 135.70 | at-bid → sell |
| 13:04Z | $432,800 | 135.25 | 135.08 / 135.20 | **above ask → strong buy** |
| 13:09Z | $337,500 | 135.00 | 135.00 / 135.41 | at-bid → sell |
| 13:22Z | $324,936 | 135.39 | 134.88 / 135.36 | **above ask → strong buy** |
| 09:56Z | $271,478 | 135.74 | 135.50 / 135.65 | **above ask → buy** |
| 13:08Z | $243,180 | 135.10 | 135.00 / 135.21 | near-bid → sell |
| 08:07Z | $217,760 | 136.10 | 136.05 / 136.33 | near-bid → neutral |
| 12:28Z | $148,533 | 135.03 | 135.00 / 135.20 | near-bid → sell |
| 11:50Z | $135,051 | 135.05 | 135.00 / 135.41 | near-bid → sell |
| 08:50Z | $122,346 | 135.94 | 135.70 / 135.95 | near-ask → buy |
| 09:19Z | $122,076 | 135.64 | 135.55 / 136.00 | near-mid → neutral |
| 11:32Z | $121,905 | 135.45 | 135.34 / 135.49 | near-ask → buy |
| 11:00Z | $114,514 | 135.52 | 135.50 / 135.72 | near-bid → neutral |

Ext-hours buyer premium ≈ $1.18M ($432K + $325K + $271K + $122K + $122K), seller
premium ≈ $1.39M ($530K + $338K + $243K + $149K + $135K). **Slight seller-skew in
the pre-market**, with the buyers paying the most aggressive prices (above ask).
Net read: the bid-side seller pressure was getting absorbed by ask-side buyers
willing to chase. Same two-sided dynamic as the regular-session block tape.
[DP:extended_hours]

### Market-context sanity check

BABA does not appear in the day's top-30 dark-pool ticker_summary (top is
MU $11.6B → SOXS $609M). At ~$122M aggregate, BABA is meaningful but not
sector-defining. The top-30 cohort is dominated by mega-cap tech (MU, NVDA,
TSLA, INTC, AMD, MSFT, META, AVGO) and indices (QQQ, SPY, IWM, HYG, SMH, VOO,
TLT, LQD) — the lack of competing China-tech tickers in this list (no PDD, no
JD, no KWEB) suggests **BABA-specific positioning**, not a "China-trade"
sector rotation. [DP:ticker_summary]

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `dark_pool_largest` | symbol=BABA, top_n=25, sort=premium | 25 prints; net buy +$3.4M, two-sided |
| `dark_pool_block_stratified` | symbol=BABA, min_tier=large | block buy_ratio 0.584, large 0.512, no mega |
| `dark_pool_extended_hours` | symbol=BABA, top_n=15 | 13 prints $3.1M; sellers slightly heavier on bid |
| `dark_pool_price_levels` | symbol=BABA, days=5, top_n=15 | overhead $140–$146 cluster $88M+, new $133–$135 support |
| `dark_pool_ticker_summary` | top_n=30 | BABA not in top-30 (avg-cap), no China-tech peers either |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mixed, with mild buyer skew on the day and a
  clearly defined overhead supply zone ($140–$146) from the prior 5 sessions.**
- **Conviction:** **3 / 5** — block buy_ratio is only suggestive (0.584), and
  the 5-day price-level chart actually shows BABA was *distributed* down from
  $145 → $135 before today's two-sided activity.
- **Three S/R levels for phase-9:**
  1. **$133.40** — fresh DP support (19 trades at exact level over 5 sessions)
     and aligns with phase-1 Mar27 $130P short-put pin.
  2. **$140.87 / $140.81 / $144.15 / $145.81** — overhead supply zone where
     institutions distributed; **phase-1 LEAP risk-reversal $145C target sits
     right at the second supply node** — a long thesis must work through
     this resistance.
  3. **$134.50–$135** — current VWAP / accumulation pocket; loss of $133.40
     with size flips the recent micro-trend bearish.
- **Open questions:**
  - Are OI deltas in Jun18 $137–$141 calls actually opening positions (vs
    closing), and do they sit on the dealer-short side? (→ phase 3 + phase 4.)
  - Does GEX flip at $137–$140 to support a magnet move into the overhead DP
    supply, or does dealer positioning fight the rally? (→ phase 4.)
  - Is BABA's recent vol regime quiet enough that a $145 reversion would
    require a catalyst (earnings, headline) rather than flow alone? (→ phase 5.)
