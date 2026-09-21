# Phase 2 — Dark Pool & Block Prints

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T11:53:32Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md

## Summary

Dark pool reads **net distribution** and **confirms phase-1's bearish lean.**
The large-tier `buy_ratio` is **0.384** (→ derived sell_ratio **0.616**;
sell_volume 857,492 vs buy_volume 535,114), and across the top-25 blocks sell
premium is **$4.63M vs $1.72M buy (2.7×)**. The two largest prints
($946k + $832k, both at **$9.89, at/below bid**) were **late-session/after-hours
liquidation** as the stock closed weak at $9.89 — down from a pre-market $10.50–
10.70. **But this is distribution without a whale:** there were **no mega- or
block-tier prints** (everything sits in the "large" $100k–$1M tier), and even the
biggest single block is only **0.029% of the 335.44M float** — modest for this
name. Conviction de-rated accordingly.

## Key signals

- **Large-tier net selling:** `large.buy_ratio = 0.384` → **sell_ratio 0.616**;
  $14.1M / 80 trades, all in the large tier (no mega/block) [DP:block_stratified].
- **Top blocks skew sell:** of top-25, **13 sells ($4.63M) vs 8 buys ($1.72M)** by
  NBBO; both largest ($946k, $832k) are at/below bid at $9.89 [DP:largest].
- **Weak close / after-hours dump:** the at-close $9.89 cluster (20:03–21:43Z) is
  the day's heaviest, printing **below** the $9.94 bid as the stock closed down
  from pre-market $10.50–10.70 [DP:extended_hours].
- **Heavy overhead supply $10.64–$10.95:** 5-day clusters at $10.95 ($2.18M),
  $10.64 ($1.83M), $10.88 ($1.57M) sit above spot — institutional supply
  [DP:price_levels].
- **Not a cross-sectional DP leader:** SMR is **outside the top-30** DP tickers
  (SPY/IVV/MU/SPCX/QQQ lead) → distribution is real but not unusual in size
  [DP:ticker_summary].

## Detailed findings

### Largest blocks (top, by premium) — [DP:largest]

| Time (UTC) | Price | Size | Premium | NBBO bid/ask | Class | % float |
|------------|-------|------|---------|--------------|-------|---------|
| 21:43:20 | 9.89 | 95,693 | $946,404 | 9.94/9.95 | **SELL** (below bid) | 0.0285% |
| 20:03:12 | 9.89 | 84,159 | $832,333 | 9.89/9.90 | **SELL** (at bid) | 0.0251% |
| 14:19:23 | 10.20 | 44,215 | $450,993 | 10.21/10.22 | **SELL** | 0.0132% |
| 13:35:48 | 10.61 | 29,971 | $317,992 | 10.61/10.62 | **SELL** | 0.0089% |
| 14:24:22 | 10.02 | 29,279 | $293,376 | 10.02/10.03 | **SELL** | 0.0087% |
| 16:02:51 | 10.08 | 25,980 | $261,878 | 10.07/10.08 | BUY | 0.0077% |

Top-25 total premium $7.16M (≈half the $14.1M DP day). Tally by NBBO: **sell n=13
$4,628,680 · buy n=8 $1,720,003 · mid n=4 $814,597.**

### Tier breakdown — [DP:block_stratified]

| Tier | buy_ratio | sell_ratio (1−) | buy_vol | sell_vol | premium | trades |
|------|-----------|-----------------|---------|----------|---------|--------|
| mega (≥$10M) | — | — | 0 | 0 | $0 | 0 |
| block (≥$1M) | — | — | 0 | 0 | $0 | 0 |
| **large (≥$100k)** | **0.384** | **0.616** | 535,114 | 857,492 | $14,119,282 | 80 |
| retail | — | — | 0 | 0 | $0 | 0 |

`sell_ratio 0.616` is **suggestive of distribution** (0.55–0.7 band = suggestive,
not high-confidence per the rubric). No `sell_ratio` field — derived as
`1 − buy_ratio`. All activity in the "large" tier → no single institutional whale.

### Price levels (5-day S/R clusters; window 06-10→06-16, spot ≈ $9.9) — [DP:price_levels]

| Level | Premium | Shares | Trades | vs spot |
|-------|---------|--------|--------|---------|
| **$10.95** | $2,184,843 | 199,533 | 7 | overhead supply |
| **$10.88** | $1,573,045 | 144,580 | 9 | overhead supply |
| **$10.64** | $1,825,558 | 171,575 | 5 | overhead supply |
| $10.07 | $1,129,544 | 112,181 | 6 | just above |
| **$9.89** | **$2,613,660** | 264,273 | 7 | **biggest — at spot (battleground)** |
| $9.79 | $1,407,649 | 143,787 | 9 | support |
| $9.57 | $1,157,826 | 120,985 | 7 | support |
| $9.48 | $1,124,454 | 118,613 | 4 | support |

Two bands: a lower demand/battleground band **$9.48–$10.07** (heaviest at $9.89)
and an upper **supply band $10.64–$10.95**. With distribution active, the upper
band reads as resistance where institutions distributed.

### Extended-hours — [DP:extended_hours]

14 prints, $3.62M total. The dominant cluster is the **20:03Z (4:03pm ET) +
21:43Z close batch at $9.89** (84k, 95.7k, 27k, 18.8k, 15.6k… all $9.89, at/below
bid) — late-day liquidation into the close. Pre-market prints (11:03–12:54Z ≈
7–8am ET) at **$10.50–$10.70** were higher, before the stock faded to a $9.89
close → an intraday distribution/weakness pattern, not overnight news-block
accumulation.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool largest --symbol SMR --top-n 25 --sort-by premium --date 2026-06-16` | sell $4.63M vs buy $1.72M ← NBBO classify; top block 95,693@9.89 | top-25 |
| `uw dark-pool block-stratified --symbol SMR --top-n 30 --min-tier large --date …` | `large.buy_ratio=0.384` → sell 0.616 ← `.results[0].large` | 1 ticker |
| `uw dark-pool extended-hours --symbol SMR --top-n 15 --date …` | close batch @9.89 below bid ← `.results[].price/executed_at` | 14 |
| `uw dark-pool price-levels --symbol SMR --top-n 15 --days 5 --date …` | $9.89 cluster $2.61M ← `.results[].price_level/total_premium`; window 06-10→16 | 15 levels |
| `uw dark-pool ticker-summary --top-n 30 --date …` | SMR outside top-30 ← `index([.results[].ticker])` null | top-30 |

## Tool errors

(none — all reads jq-validated. The initial buy/sell tally hit one row with a
`null` premium → re-run with `select(.premium!=null …)`; recorded for audit.)

## DATA NOTE / CORRECTION

- `block-stratified` has **no `sell_ratio`** — derived `1 − buy_ratio = 0.616`
  per the field-path trap.
- `price-levels` field is **`price_level`** (not `price`) and **`total_shares`**
  (not `size`); first parse used wrong keys → re-read with correct paths.

## Verdict for downstream phases

- **Bias from this phase:** **Distribution / net selling** (confirms phase-1)
- **Conviction:** **2/5** — sell_ratio 0.616 is only suggestive; sizes are small
  vs the 335M float and there is **no mega/block-tier whale**. Real but not heavy.
- **Largest block as % of float:** **0.0285%** (95,693 sh / 335.44M); full DP day
  ≈ **0.42%** of float [DP:block_pct_float fz]. **Not meaningful size for this
  name** — distribution is broad/retail-institutional, not a concentrated dump.
- **Three S/R levels for phase-9:**
  1. **Resistance/supply: $10.64–$10.95** (heavy overhead DP clusters, ~$5.6M).
  2. **Battleground/pivot: $9.89** (biggest single cluster $2.61M, = the close).
  3. **Support: $9.79 / $9.57 / $9.48** (lower demand band).
- **Open questions:** Does positioning (phase-3 OI walls / pin) corroborate the
  $9.89 pin and the $10.64–10.95 supply? Is the distribution institutions trimming
  into the short base, or short-side hedging? Any catalyst behind the weak close
  (phase-6/7c)?
