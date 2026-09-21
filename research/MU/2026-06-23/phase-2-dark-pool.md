# Phase 2 — Dark Pool & Block Prints

**Ticker:** MU
**As-of date:** 2026-06-23
**Generated:** 2026-06-23
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

The dark pool reads **net accumulation today** — and it leans *against* the thin
options-bearish tag from phase 1. MU is the **#1 dark-pool name in the market**
($17.49B premium, 80,756 trades), the **mega tier is 85.9% bought** (buy_ratio 0.859 —
above the 0.7 high-confidence threshold), the broad large/block tiers are mildly
accumulative (buy_ratio 0.534), and the **single largest block (522,285 sh / $553M)
printed at $1058.88 — above the $1057.93 NBBO ask** (paying up). The catch: the heavy
5-day price-level shelves sit *above* spot ($1133.99 / +7.8% with $5.14B; $1211 /
+15.2%), so MU has **pulled back ~7–15% into the print** and institutions are buying
that dip. Size-as-%-of-float is tiny (biggest block = **0.047% of the 1.12B float**) —
for a $1.37T name the *buy ratio*, not block size, is the signal.

## Key signals

- MU **#1 dark-pool ticker** today: total_premium **$17.49B**, 80,756 trades, avg_price $1077.18 `[DP:ticker_summary]`
- **Mega-tier buy_ratio 0.859** (9 prints, $704M; sell_ratio 0.141) — high-confidence institutional buying `[DP:block_stratified]`
- Largest block **522,285 sh @ $1058.88 = $553.0M**, printed **above ask** (nbbo_ask 1057.93, trade_vs_mid +1.25) `[DP:largest]`
- Broad large tier ($14.05B, 78,993 trades) buy_ratio **0.534**; block tier ($2.74B) 0.534 — mild net accumulation across the whole book `[DP:block_stratified]`
- Heavy 5-day shelves are **overhead** ($1133.99 +7.8% $5.14B; $1211.38 +15.2% $2.97B) — stock fell into the print from those levels `[DP:price_levels]`

## Detailed findings

### Largest blocks — `[DP:largest]`

| Time (UTC) | Price | Size (sh) | Premium | NBBO context | % float |
|---|---|---|---|---|---|
| 20:08:20 | $1058.88 | 522,285 | $553.0M | **above ask** (bid 1057.33 / ask 1057.93) → aggressive buy | 0.047% |
| 17:53:19 | $1064.00 | 24,449 | $26.0M | midday | 0.002% |
| 21:08:48 | $1051.77 | 20,000 | $21.0M | at close px | 0.002% |
| 14:04:43 | $1102.29 | 17,134 | $18.9M | early, higher | 0.002% |
| 13:59:49 | $1093.79 | 16,741 | $18.3M | early, higher | 0.001% |

The $553M block dwarfs everything else (next is $26M) and is an **extended-hours
print** (`ext_hour_sold_codes=extended_hours_trade`, 20:08 UTC ≈ 4:08pm ET) — a
post-close institutional buy right before tomorrow's catalyst. Above-ask pricing
argues genuine accumulation, but pre-catalyst timing means it could also be a
positioning/hedge leg — de-rate slightly (see verdict).

### Tier breakdown — `[DP:block_stratified]`

| Tier | buy_ratio | derived sell_ratio | total_premium | trades |
|---|---|---|---|---|
| **mega** | **0.859** | 0.141 | $704.4M | 9 |
| block | 0.534 | 0.466 | $2.739B | 1,754 |
| large | 0.534 | 0.466 | $14.048B | 78,993 |
| retail | — | — | $0 | 0 |
| **all tiers** | — | — | **$17.492B** | — |

The signal: the 9 largest (mega) prints are decisively **bought** (85.9%), while the
broad book is only mildly net-buy (53.4%). Concentration of conviction in the biggest
hands = constructive. (`sell_ratio` derived as `1 − buy_ratio`; no such field exists.)

### Price levels (5-day clusters, window 2026-06-16 → 06-23) — `[DP:price_levels]`

| price_level | premium | vs spot $1051.77 | role |
|---|---|---|---|
| 1211.38 | $2.97B | +15.2% | far overhead supply |
| 1190.00 | $0.13B | +13.1% | overhead |
| **1133.99** | **$5.14B** | **+7.8%** | **major overhead shelf** (heaviest cluster) |
| 1110.00 | $0.14B | +5.5% | overhead |
| 1100.00 | $0.09B | +4.6% | overhead |
| 1058.88 | $0.57B | +0.7% | today's block / near-term pivot |
| 1057.56 | $0.28B | +0.6% | pivot |
| **1044.88 / 1043.19** | $0.18B / **$0.85B** | −0.7 / −0.8% | **near support** (strong) |
| **1020.76** | **$0.89B** | −2.9% | **support** (strong) |

Spot sits in a thin pocket between support $1043 and pivot $1058. The dominant volume
shelves ($1134, $1211) are now **overhead resistance** — MU was trading there last week
and has declined into earnings, so today's buying is dip-buying beneath heavy supply.

### Extended-hours activity — `[DP:extended_hours]`

Dominated by the single $553M / 522k-share block at 20:08 UTC (above ask). The 20:00
UTC cluster (16,889 + 9,135 + 7,623 sh at exactly $1051.77) is the **closing cross**;
a small 22:53/23:59 UTC tail ($1067 / $1065) and an 11:01 UTC premarket print at
$1120. Net extended-hours bias = buy, but the marquee block being post-close + pre-
catalyst warrants the hedge caveat above.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `dark-pool ticker-summary --top-n 30` | MU **rank 1**, total_premium $17.49B ← `.results[]\|select(.ticker=="MU")` | top-30 |
| `dark-pool block-stratified --symbol MU --min-tier large` | mega buy_ratio 0.859 ← `.results[0].mega.buy_ratio`; large 0.534 | tiers |
| `dark-pool largest --symbol MU --sort-by premium --top-n 25` | 522,285 sh @ $1058.88 = $553M ← `.results[0].size/.price/.premium`; above ask ← `.price>.nbbo_ask` | top-25 |
| `dark-pool price-levels --symbol MU --days 5 --top-n 15` | $1133.99 $5.14B ← `.results[]\|.price_level,.total_premium`; window `.dates_covered` | 5-day |
| `dark-pool extended-hours --symbol MU --top-n 15` | $553M block flagged `ext_hour_sold_codes` | top-15 |

## Tool errors

(none — all five reads parsed cleanly through `jq`)

## DATA NOTE / CORRECTION

First extraction of price-levels used `jq '.price'` (null — the field is
`price_level`); re-extracted against `.results[].price_level`. No value was
transcribed from the null read; corrected before this MD was written.

## Verdict for downstream phases

- **Bias:** **ACCUMULATION** (mega 85.9% buy, broad 53.4% buy, biggest block above ask) —
  contradicts phase-1's thin bearish options lean and supports phase-1's bullish
  *structural* prints (LEAP call buying, put selling).
- **Conviction:** **3/5** — clear buy ratios, but de-rated because (a) it's a mega-cap
  where blocks print all day (signal is the *ratio* vs baseline, and 53.4% broad is
  only mild), (b) the marquee $553M block is an after-hours/closing print that could be
  hedging into the binary, and (c) buying is occurring beneath heavy overhead supply.
- **Largest block as % of float:** **0.047%** (522,285 / 1.12B) — *not* meaningful as a
  size signal for a $1.37T mega-cap; the 0.859 mega buy_ratio and above-ask print are
  the real tells. `[DP:block_pct_float fz]`
- **Three S/R levels for phase-9:**
  1. **Support $1043.19** (−0.8%, $0.85B) → first downside reference / stop pivot.
  2. **Support $1020.76** (−2.9%, $0.89B) → deeper support if the print disappoints.
  3. **Resistance $1133.99** (+7.8%, $5.14B major shelf) → the level a bullish gap must reclaim; nearer pivot $1058 (today's block).
- **Open questions:** Where is dealer gamma/pin positioned for the post-earnings move
  (phase 3/4)? Does the OI wall structure corroborate the $1043 support / $1134
  resistance the dark pool drew? Is the mega-buy genuine accumulation or a delta hedge
  against the LEAP calls sold to dealers (phase 1's 1500c)?
