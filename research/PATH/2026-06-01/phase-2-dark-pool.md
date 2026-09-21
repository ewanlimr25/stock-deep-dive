# Phase 2 — Dark Pool & Block Prints

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-01
**Generated:** 2026-06-01T20:14:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark-pool tape reads **net accumulation** and, crucially, reframes phase-1's biggest
bearish print. The large tier (the meaty 1,925-trade bucket) is **63.4% buy**
(buy 10.9M sh vs sell 6.29M → **net +4.6M shares bought ≈ 1.1% of the 412.34M float in
one day**), topped by a single **1.6M-share mega block @ $12.72 = $20.35M, buy-classified**
(trade_vs_mid +0.30 → printed above mid). Institutional size clusters **just below
spot** at $12.86–12.91 (>500 trades, ~$60M aggregate) and the $12.72 block, with deeper
shelves at ~$11.70 and $11.28. Net long accumulation under the market while spot holds
$13.10 above it. Read against phase-1, the **$2.31M ATM Sep $13 put now looks like a
protective hedge on this accumulated long**, not a standalone short — i.e. a *cautiously
constructive* institutional posture, not distribution.

## Key signals

- Single **1.6M-share mega block @ $12.72, $20.35M, BUY** (trade_vs_mid +0.30) =
  **0.388% of float** in one print [DP:largest][DP:block_pct_float fz]
- **Large-tier buy_ratio 0.634** → net +4.6M shares accumulated (~1.1% float)
  [DP:block_stratified]
- Heavy institutional **support shelf $12.86–12.91** (147+138+108+98+65+94 trades,
  ~$60M) just below spot [DP:price_levels]
- Deeper accumulation shelves at **$11.69–11.73 (~$11.70)** and **$11.28** (−10.5% /
  −13.9% vs spot) [DP:price_levels]
- Pre-market buying $12.15–12.22 (20K-share prints, 07–08 ET) [DP:extended_hours]
- PATH **outside top-30** dark-pool names absolutely (MU $15.3B, NVDA $12.3B lead) —
  small vs mega-caps, meaningful per-float [DP:ticker_summary]

## Detailed findings

### Largest blocks `[DP:largest]`

| Time (ET) | Price | Size | Premium | vs_mid | % float |
|-----------|-------|------|---------|--------|---------|
| 10:33 | $12.721 | **1,600,000** | **$20,353,600** | +0.30 (buy) | **0.388%** |
| 13:31 | $12.855 | 299,000 | $3,843,645 | 0.00 | 0.073% |
| 10:06 | $12.700 | 252,000 | $3,200,400 | −0.005 | 0.061% |
| 15:57 | $13.130 | 55,135 | $723,923 | −0.005 | 0.013% |
| 10:33 | $12.445 | 47,352 | $589,296 | 0.00 | 0.011% |
| 14:58 | $12.940 | 42,164 | $545,602 | −0.015 | 0.010% |

Top-25 blocks = $35.75M. The 1.6M-share block is the whole story — 57% of the top-25
premium in one trade, buy-classified, at $12.72 (−2.9% below spot — bought the dip).

### Tier breakdown `[DP:block_stratified]`

| Tier (≥) | buy_ratio | derived sell_ratio | buy vol | sell vol | total premium | trades |
|----------|-----------|--------------------|---------|----------|---------------|--------|
| mega (≥$10M) | **1.00** | 0.00 | 1,600,000 | 0 | $20.35M | 1 |
| large (≥$100k) | **0.634** | 0.366 | 10,915,360 | 6,289,022 | $222.1M | 1,925 |
| block (≥$1M) | 0.543 | 0.457 | 299,000 | 252,000 | $7.04M | 2 |
| retail | 0.50 | 0.50 | — | — | $0 | — |
| **all tiers** | — | — | — | — | **$249.5M** | — |

Large-tier buy_ratio 0.634 sits in the **"suggestive accumulation"** band (0.55–0.70),
not the >0.70 high-confidence zone — so accumulation is the read, but probabilistic.
Net large-tier flow = +4.6M shares bought (~1.1% of float). Mega buy is a single block
(n=1) — directionally clear but one transaction.

### Price levels (5-day cluster; dates 2026-05-26→06-01) `[DP:price_levels]`

| Level | Premium | Shares | Trades | vs spot |
|-------|---------|--------|--------|---------|
| $12.90 | $16.36M | 1.27M | 147 | −1.5% |
| $12.91 | $15.59M | 1.21M | 138 | −1.5% |
| $12.89 | $12.20M | 0.95M | 108 | −1.6% |
| $12.88 | $10.93M | 0.85M | 98 | −1.7% |
| $12.72 | $21.02M | 1.65M | 6 | −2.9% (mega-block level) |
| $11.72 | $10.77M | 0.92M | 64 | −10.5% |
| $11.28 | $10.69M | 0.95M | 38 | −13.9% |

**All clusters sit below spot.** Per the strict heuristic (clusters below spot →
distribution) this would caution, BUT the buy_ratio is a *buy* read and spot ($13.10)
is now *above* the accumulation zone — institutions bought $12.7–12.9 and price has
since lifted over them. Reading: accumulation absorbed under the market, now in profit.
The $12.86–12.91 wall is the immediate institutional support; $11.70 / $11.28 are the
deeper shelves.

### Extended-hours activity `[DP:extended_hours]`

Pre-market accumulation $12.15–12.22 (multiple 20K-share prints, 07–08 ET) and an
after-hours 18.5K-share print @ $13.10 (16:20 ET). The 299K @ $12.855 (13:31 ET) and
the marquee 1.6M block are regular-hours. No single overnight catalyst print dominates;
treat as steady accumulation rather than a news gap (cross-check phase-6).

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Rows |
|---------|--------------------------|------|
| `dark-pool largest --symbol PATH --date 2026-06-01` | 1.6M @ $12.72 $20.35M buy ← `.results[0]` | top-25 |
| `dark-pool block-stratified --min-tier large` | large buy_ratio 0.634 ← `.results[0].large.buy_ratio`; sell=1−0.634 | all-day |
| `dark-pool price-levels --days 5` | $12.90 $16.36M ← `.results` sorted; dates ← `.dates_covered` | 5d |
| `dark-pool extended-hours` | pre-mkt $12.15–12.22 ← `.results[]` | top-15 |
| `dark-pool ticker-summary --top-n 30` | PATH outside top-30 ← `.results[]|select(.ticker=="PATH")` | top-30 |

## Tool errors

<none — all reads parsed clean through `jq`>

## Verdict for downstream phases

- **Institutional bias:** **Accumulation (net)** — large-tier 63.4% buy, +4.6M shares
  (~1.1% float), anchored by a 1.6M-share buy block. Cautiously constructive.
- **Conviction:** **3/5** — buy_ratio "suggestive" (0.634, not >0.70); mega is a single
  print; accumulation is below spot (price has since risen over it). Real but not loud.
- **Largest block as % of float:** **0.388%** (1.6M sh / 412.34M) — *meaningful for this
  name* (one print = ~0.4% of float; day's net buy ≈ 1.1% of float). [DP:block_pct_float fz]
- **Three S/R levels for phase-9:**
  1. **$12.86–12.91** — immediate institutional support (heaviest cluster, just below spot)
  2. **$12.72** — mega-block accumulation level
  3. **$11.70 / $11.28** — deeper accumulation shelves (−10% / −14%) = thesis-break zone
- **Open questions:**
  1. Does phase-3 OI corroborate the $13 strike (the Sep put) as a hedge anchor, and
     where are the call walls (resistance) the dark-pool data doesn't show above spot?
  2. Is the accumulator the same party that bought the Sep $13 put (protected long), or
     two different institutions (one long stock, one short via puts)? Phase-3/8 to weigh.
