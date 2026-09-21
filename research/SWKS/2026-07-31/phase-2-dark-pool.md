# Phase 2 — Dark Pool & Block Prints

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`

## Summary

The as-of session itself is **balanced-to-flat** — but the two sessions before it
show **decisive institutional accumulation into the earnings gap**, and that is
the finding that matters. Stripping the closing auction and the structurally
non-directional prints (VWAP `average_price_trade` and late `prior_reference_price`
reports — **39.4% of the day's dark-pool shares**), the regular-session directional
buy ratio on 2026-07-31 is **0.461** on just **95,631 shares / $5.91M**, i.e. a net
**−6,697 shares**: a non-event. By contrast **2026-07-29 — the −5.40% earnings
reaction — printed a net +341,637 shares bought ($21.16M) on 1,489,909 directional
shares at buy ratio 0.634**, and **2026-07-30 followed with +232,129 net
($14.21M) at buy ratio 0.751**. Combined, **+573,766 shares ≈ 0.38% of shares
outstanding absorbed in two sessions**, versus a +12k–+24k daily baseline on the
five sessions before the print — a **15–25× step-change**. The buying was
concentrated in a hard shelf at **$58.44–59.34** (≈176,500 shares, ≈$10.4M, all on
2026-07-29 pre-market and in the first ten minutes, against that day's $57.50 low).
This **corroborates the phase-1 read** that the initiating options flow was long
delta (3,333 Aug-21 52.5 puts *sold*, `phase-1-flow.md §New positioning`): real
shares were bought on the break, and the as-of day's put sale monetizes the
resulting comfort. **Verdict: ACCUMULATION (2026-07-29/30), paused on the as-of
day.**

## Key signals

- **Regular-session directional net, last 3 sessions:** 2026-07-29 **+341,637 sh /
  +$21,160,930** · 2026-07-30 **+232,129 sh / +$14,211,575** · 2026-07-31 (as-of)
  **−6,697 sh / −$397,208**. Prior five sessions ran +12,614 to +24,390.
  `[DP:net_imbalance DUCKDB]`
- **Clean buy-ratio trend:** 0.425 → 0.531 → 0.722 → 0.625 → 0.676 → **0.634
  (earnings day, 1.49M shares)** → **0.751** → **0.461 (as-of)**.
  `[DP:buy_ratio DUCKDB]`
- **The accumulation shelf is $58.44–59.34** — ~176,500 shares / ~$10.4M in 12
  blocks ≥5,000 shares, all on 2026-07-29, including **43,200 sh @ $58.4896 at
  08:37:46 ET (pre-market)** and 27,010 @ $58.60 at 09:31:30. The day's low was
  **$57.50**; the close was **$61.19**. `[DP:largest DUCKDB]`
- **Raw UW tier ratios understate this badly.** `block-stratified` reports
  `block.buy_ratio = 0.478` and `large.buy_ratio = 0.395` for the as-of day —
  both look like distribution. They are contaminated: the entire `block`-tier
  "sell" volume (54,485 sh) is **two VWAP `average_price_trade` /
  `derivative_priced` prints**, which carry no directional information.
  `[DP:block_stratified]`
- **Overhead supply sits at $64.68** — the 2026-07-28 pre-earnings close, and by
  far the largest 5-day dark-pool level at **$39,290,060 / 607,453 shares**. That
  is where the pre-print holders are underwater. `[DP:price_levels]`
- **SWKS is absent from `dark-pool ticker-summary --top-n 30`** (cutoff LITE
  **$895,983,820** vs SWKS's **$16,263,573**) — consistent with
  `phase-0.5-context.md`'s `unusual_verdict: QUIET`. `[DP:ticker_summary]`

## Detailed findings

### Largest blocks — as-of session

`uw dark-pool largest --symbol SWKS --top-n 200 --sort-by premium --date 2026-07-31`
returned **56 prints, 263,187 shares, $16,263,573** — which exactly equals
`block-stratified`'s `total_premium_all_tiers` and the `insights deep-dive`
`uw_dark_pool` block (`total_premium = 16263573.1003`, `total_shares = 263187`,
`trade_count = 56`, `avg_price = 61.9005`). So this is the **complete** ≥$100k
universe for the day, not a top-N sample. Top 25 by premium (times UTC; ET = −4):

| Exec (UTC) | ET | Price | Size | Premium | NBBO bid/ask | vs mid | Class |
|---|---|---|---|---|---|---|---|
| 20:00:02 | 16:00:02 | 62.28 | **49,824** | **$3,103,039** | 62.00 / 62.28 | +0.140 | closing auction |
| 13:45:19 | 09:45:19 | 60.7431 | **29,222** | $1,775,035 | 61.05 / 61.14 | −0.352 | **VWAP** |
| 13:45:20 | 09:45:20 | 60.7422 | **25,263** | $1,534,530 | 61.05 / 61.24 | −0.403 | **VWAP** |
| 20:00:20 | 16:00:20 | 62.28 | 8,160 | $508,205 | 61.93 / 62.96 | −0.165 | auction/late |
| 15:48:47 | 11:48:47 | 61.60 | 6,282 | $386,971 | 61.60 / 61.61 | −0.005 | directional |
| 16:50:36 | 12:50:36 | 62.085 | 6,212 | $385,672 | 62.08 / 62.10 | −0.005 | directional |
| 20:00:28 | 16:00:28 | 62.28 | 5,800 | $361,224 | 61.93 / 62.96 | −0.165 | auction/late |
| 19:59:59 | 15:59:59 | 62.30 | 5,700 | $355,110 | 62.28 / 62.29 | +0.015 | directional |
| 18:46:25 | 14:46:25 | 62.50 | 5,000 | $312,500 | 62.49 / 62.50 | +0.005 | directional |
| 16:05:57 | 12:05:57 | 61.93 | 5,000 | $309,650 | 61.87 / 61.89 | +0.050 | directional |
| 19:43:15 | 15:43:15 | 62.545 | 4,897 | $306,283 | 62.54 / 62.55 | 0.000 | flat |
| 20:00:18 | 16:00:18 | 62.28 | 4,409 | $274,593 | 61.93 / 62.96 | −0.165 | auction/late |
| 20:00:18 | 16:00:18 | 62.28 | 4,219 | $262,759 | 61.93 / 62.96 | −0.165 | auction/late |
| 20:54:05 | 16:54:05 | 62.28 | 3,795 | $236,353 | 61.20 / 62.80 | +0.280 | post-close |
| 20:00:00 | 16:00:00 | 62.28 | 3,700 | $230,436 | 62.01 / 62.28 | +0.135 | closing auction |
| 20:00:36 | 16:00:36 | 62.28 | 3,700 | $230,436 | 61.93 / 62.96 | −0.165 | auction/late |
| 17:19:58 | 13:19:58 | 62.2361 | 3,594 | $223,677 | 62.22 / 62.23 | +0.011 | directional |
| 20:00:07 | 16:00:07 | 62.28 | 3,411 | $212,437 | 61.93 / 62.96 | −0.165 | auction/late |
| 13:53:16 | 09:53:16 | 60.645 | 3,400 | $206,193 | 60.66 / 60.74 | −0.055 | directional |
| 20:00:18 | 16:00:18 | 62.28 | 3,190 | $198,673 | 61.93 / 62.96 | −0.165 | auction/late |
| 11:04:08 | 07:04:08 | 63.00 | 3,100 | $195,300 | 62.51 / 64.06 | −0.285 | pre-market |
| 13:40:58 | 09:40:58 | 60.90 | 2,880 | $175,392 | 60.76 / 61.02 | +0.010 | directional |
| 20:00:18 | 16:00:18 | 62.28 | 2,767 | $172,329 | 61.93 / 62.96 | −0.165 | auction/late |
| 20:09:37 | 16:09:37 | 62.28 | 2,754 | $171,519 | 61.93 / 62.80 | −0.085 | post-close |
| 15:52:42 | 11:52:42 | 61.66 | 2,750 | $169,565 | 61.67 / 61.69 | −0.020 | directional |

**Two structural contaminants are visible and must be removed before any
buy/sell read** (this is the discipline the project's closing-auction note
prescribes, extended here to trade-condition codes):

1. **The closing-auction / late-report cluster at 16:00:00–16:00:36 ET.** Every
   one prints at exactly **$62.28**, the official close. Ten of them classify as
   "sell" purely because the reference NBBO after the bell is a **61.93 / 62.96
   spread** whose mid ($62.445) sits above the close — a quoting artifact, not
   selling. The same wide quote makes the 49,824-share cross classify as a "buy".
   The auction is directionally uninformative in **both** directions.
2. **VWAP and late-reference prints.** The trade-condition inventory for the day:

| `sale_cond_codes` | `trade_code` | `ext_hour_sold_codes` | n | Shares | Premium |
|---|---|---|---|---|---|
| *(none)* | *(none)* | *(none)* | 34 | 95,631 | $5,909,379 |
| *(none)* | *(none)* | `extended_hours_trade` | 6 | 63,944 | $3,984,664 |
| **`average_price_trade`** | **`derivative_priced`** | *(none)* | **4** | **58,698** | **$3,572,286** |
| **`prior_reference_price`** | *(none)* | `extended_hours_trade` | **12** | **44,914** | **$2,797,244** |

**103,612 of 263,187 shares (39.4%)** carry `average_price_trade` or
`prior_reference_price` — an average-price fill of a worked order, or a late
report referencing an earlier price. Comparing either to the *current* NBBO mid
produces noise. The two 60.74 prints (29,222 + 25,263 = **54,485 shares**) are
exactly this: they are the entire `block`-tier "sell" volume, and they are VWAP
prints, **not** a distribution signal.

### Tier breakdown

`uw dark-pool block-stratified --symbol SWKS --top-n 30 --min-tier large --date 2026-07-31`
(tier boundaries per the tool's own caveat: mega ≥$10M, block ≥$1M, large ≥$100k,
retail <$100k; `sell_ratio` derived as `1 − buy_ratio` — **there is no
`sell_ratio` field**):

| Tier | `buy_ratio` | derived `sell_ratio` | `buy_volume` | `sell_volume` | `total_premium` | `trade_count` |
|---|---|---|---|---|---|---|
| **mega** (≥$10M) | 0.500 | 0.500 | 0 | 0 | $0 | **0** |
| **block** (≥$1M) | **0.478** | 0.522 | 49,824 | 54,485 | $6,412,604 | 3 |
| **large** (≥$100k) | **0.395** | **0.605** | 62,770 | 96,108 | $9,850,969 | 53 |
| retail | 0.500 | 0.500 | 0 | 0 | $0 | 0 |
| **all tiers** | — | — | — | — | **$16,263,573** | 56 |

`highest_tier = "block"` — **no mega-tier print at all**, so the phase's
accumulation/distribution heuristic (which keys on `mega.buy_ratio`) has **no
mega input to read** and cannot be applied as written on this date.

Taken at face value the `large` tier's 0.395 (⇒ sell_ratio 0.605) clears the
prompt's distribution threshold. **It should not be taken at face value.** All
three `block`-tier trades are the auction cross plus the two VWAP prints; and of
the 53 `large`-tier trades, the auction/late/VWAP contamination above accounts for
the bulk of the "sell" side. Decomposed properly:

| Session | Class | Side | n | Shares | Premium |
|---|---|---|---|---|---|
| Pre-market | directional | sell | 1 | 3,100 | $195,300 |
| **Regular (09:30–16:00)** | **directional** | **buy** | **14** | **40,081** | **$2,482,937** |
| **Regular** | **directional** | **sell** | **17** | **46,778** | **$2,880,145** |
| Regular | directional | flat | 3 | 8,772 | $546,298 |
| Regular | NON-DIRECTIONAL | buy | 1 | 2,513 | $156,794 |
| Regular | NON-DIRECTIONAL | sell | 3 | 56,185 | $3,415,492 |
| Closing auction (16:00–16:01) | directional | buy | 4 | 57,433 | $3,576,927 |
| Closing auction | directional | sell | 1 | 3,411 | $212,437 |
| Closing auction | NON-DIRECTIONAL | sell | 9 | 36,504 | $2,273,469 |
| Post-close | NON-DIRECTIONAL | buy | 1 | 3,795 | $236,353 |
| Post-close | NON-DIRECTIONAL | sell | 2 | 4,615 | $287,422 |

**Headline, regular-session directional prints only:**
**buy 40,081 sh / $2,482,937 (avg $61.868) vs sell 46,778 sh / $2,880,145 (avg
$61.525) ⇒ buy_ratio 0.461, net −6,697 shares.** Balanced, marginally sell-tilted,
and — at $5.9M of directional premium — **too small to be a signal either way**.

For reference, the naive all-session share-weighted buy ratio is **0.408**, and the
naive intraday-including-VWAP figure is **0.287**. Both are wrong; the sequence
0.287 → 0.408 → **0.461** shows exactly how much the answer moves with the
cleaning, which is why the raw tier ratios are not quoted as the verdict.

### The two sessions that matter — regular-session directional history

Same cleaning applied across the available dark-pool window:

| Date | Day % | Directional shares | Premium | **Clean buy_ratio** | **Net shares** | **Net premium** |
|---|---|---|---|---|---|---|
| 2026-07-22 | +0.33% | 177,676 | $11.16M | 0.425 | −25,358 | −$1,604,158 |
| 2026-07-23 | −4.26% | 428,354 | $26.07M | 0.531 | +24,390 | +$1,522,135 |
| 2026-07-24 | −0.43% | 41,002 | $2.48M | 0.722 | +13,094 | +$795,451 |
| 2026-07-27 | +5.36% | 81,309 | $5.08M | 0.625 | +19,001 | +$1,157,810 |
| 2026-07-28 *(earnings PM)* | +1.95% | 49,819 | $3.19M | 0.676 | +12,614 | +$807,006 |
| **2026-07-29** *(−5.40%)* | **−5.40%** | **1,489,909** | **$91.79M** | **0.634** | **+341,637** | **+$21,160,930** |
| **2026-07-30** | **+2.11%** | **513,666** | **$31.48M** | **0.751** | **+232,129** | **+$14,211,575** |
| **2026-07-31 (as-of)** | −0.32% | 95,631 | $5.91M | **0.461** | **−6,697** | **−$397,208** |

This is the phase's central finding. On the earnings break, directional dark-pool
volume went **30× the prior day's** (49,819 → 1,489,909 shares) and the buy ratio
*held at 0.634* — institutions were **net takers of the gap**, not sellers of it.
The follow-through session pushed the buy ratio to **0.751**, its highest in the
window. Cumulative **+573,766 net shares over the two sessions**, versus a
+12,614/+19,001/+13,094 baseline immediately prior.

Scale check: 2026-07-29 dark-pool volume of 1,570,650 total shares was **10.2% of
the day's 15,333,028 consolidated share volume**; on the as-of day, 263,187 shares
was **5.3% of 4,991,143**.

### Price levels — institutional S/R (5-day)

`uw dark-pool price-levels --symbol SWKS --top-n 15 --days 5`. Per the phase
caveat, `--days` anchors to the **latest available date**; `phase-0-intake.md`
confirms that is **2026-07-31**, so the window is **2026-07-27 → 2026-07-31** and
is as-of-consistent. Spot = **$62.28**.

| Level | Premium | Shares | Trades | vs spot | Reading |
|---|---|---|---|---|---|
| **64.68** | **$39,290,060** | **607,453** | 15 | **+3.9%** | 2026-07-28 pre-earnings close — **the overhead supply wall** |
| 62.48 | $17,557,797 | 281,015 | 12 | +0.3% | 2026-07-30 close |
| 63.44 | $15,168,377 | 239,098 | 20 | +1.9% | 2026-07-27 close |
| **62.28** | $7,309,804 | 117,370 | 19 | **spot** | as-of close |
| **61.22** | $6,389,400 | 104,368 | 3 | −1.7% | single 99,400-sh block on 2026-07-30 |
| **60.25** | $6,173,034 | 102,457 | 1 | −3.3% | **single 102,457-sh block on 2026-07-29** |
| 63.43 | $5,965,269 | 94,042 | 2 | +1.8% | |
| **60.83** | $4,690,471 | 77,108 | 2 | −2.3% | 75,308-sh block on 2026-07-29 |
| 63.19 | $3,791,100 | 60,000 | 1 | +1.5% | |
| **58.49** | $3,567,869 | 61,000 | 3 | **−6.1%** | **the gap-day shelf** |
| 60.74 | $3,309,565 | 54,485 | 2 | −2.5% | the two VWAP prints — **not** a real level |
| 61.36 | $3,188,691 | 51,971 | 2 | −1.5% | |
| 62.95 | $3,130,399 | 49,732 | 4 | +1.1% | |
| 61.41 | $2,792,631 | 45,476 | 2 | −1.4% | |
| 62.50 | $2,637,490 | 42,200 | 8 | +0.4% | |

**Clusters within 1% of spot:** 62.28 ($7.31M), 62.48 ($17.56M), 62.50 ($2.64M)
above; 61.41 ($2.79M) and 61.36 ($3.19M) just below. Spot is sitting inside a
**$61.36–62.50 congestion band worth ~$33.5M** — a coiled, two-sided level, not a
trend.

Zooming into the accumulation shelf, all blocks ≥5,000 shares printed below
$59.50 in the window (every one on **2026-07-29**, against that session's
**$57.50 low / $64.08 high / $61.19 close**):

| ET | Price | Size | Premium |
|---|---|---|---|
| 07:33:48 | 58.4896 | 9,600 | $561,500 |
| 07:34:31 | 58.5938 | 14,400 | $843,751 |
| **08:37:46** | **58.4896** | **43,200** | **$2,526,751** |
| 09:30:29 | 59.34 | 6,100 | $361,974 |
| 09:30:30 | 59.335 | 14,750 | $875,191 |
| 09:31:10 | 59.09 | 11,458 | $677,053 |
| 09:31:12 | 59.12 | 7,369 | $435,655 |
| 09:31:30 | 58.60 | 27,010 | $1,582,786 |
| 09:31:55 | 58.49 | 8,200 | $479,618 |
| 09:32:59 | 58.435 | 10,000 | $584,350 |
| 09:38:31 | 59.34 | 17,800 | $1,056,252 |
| 09:40:17 | 58.89 | 6,600 | $388,674 |
| **Total** | **58.44–59.34** | **176,487** | **$10,373,555** |

Three of these — 67,200 shares, $3.93M — printed **pre-market, before 08:38 ET**,
i.e. institutions were positioning on the gap **before the regular session even
opened**, and the price never traded back below $59.86 afterwards.

### Extended-hours activity

`uw dark-pool extended-hours --symbol SWKS --top-n 15` returned **15 rows**, but
they are almost entirely the **16:00 auction/late cluster at $62.28** already
dissected above, plus:

- **2026-07-31 07:04:08 ET — 3,100 sh @ $63.00, $195,300**, against a very wide
  pre-market NBBO of **62.51 / 64.06** (mid 63.285). The only genuine pre-market
  print of the as-of day, and it is a **single small lot** — $195k on a name that
  traded $16.3M of dark pool. No overnight institutional move to attribute.
- **16:09:37 and 16:54:05 ET** — 2,754 sh and 3,795 sh, both at $62.28. Post-close
  cleanup; the 16:54 print classifies "buy" only because the post-close NBBO had
  widened to 61.20 / 62.80.

**Per the phase-prompt's hedging heuristic:** there is **no** concentration of
block premium in pre/post-market ahead of a catalyst. There is no catalyst ahead —
`phase-0.5-context.md` verified the next earnings date is **2026-10-27** and the
print is already behind us. The extended-hours tape here is mechanical, not
directional, and the 2026-07-29 pre-market blocks (67,200 sh at $58.44–58.59) were
a **reaction to** the event, not positioning ahead of it.

### Float normalization (advisory)

`phase-0-intake.md` recorded **`fz_available = yes, DEGRADED`** — `fz quote`
returns only 14 of 84 fields and **`Shs Float` is unavailable**, so the prescribed
`block_shares / Shs Float × 100` cannot be computed from the sanctioned source.

Falling back to an explicit derivation from data already validated in this run:
`marketcap / close = 9,401,539,419 / 62.28 = **150,956,637 shares outstanding**`
(screener parquet). Against that denominator — **shares outstanding, not float, so
this is an under-estimate of the float-relative size**:

| Print | Shares | % of shares out |
|---|---|---|
| Largest as-of block (16:00 auction cross) | 49,824 | **0.033%** |
| Largest as-of VWAP print | 29,222 | 0.019% |
| Largest single 2026-07-29 block (08:37 ET @ 58.49) | 43,200 | **0.029%** |
| 2026-07-29 accumulation shelf, total | 176,487 | **0.117%** |
| **2026-07-29 + 07-30 net directional absorption** | **573,766** | **0.380%** |

**Read for this name:** no *individual* print is meaningful — 0.03% of the share
count is routine for a $9.4B S&P 500 constituent. What is meaningful is the
**aggregate**: 0.38% of the company changing hands net-long through the dark pool
in two sessions, at a 15–25× step-up from baseline. Tagged
`[DP:block_pct_float fz]` with the explicit caveat that the denominator is
**shares outstanding, not `Shs Float`**, because `fz` could not supply float —
which makes the true percentages **higher** than shown. **Advisory only; this does
not raise conviction.**

### Cross-sectional check

`uw dark-pool ticker-summary --top-n 30 --date 2026-07-31`: **SWKS is absent**.
The top-30 cutoff was **LITE at $895,983,820** against SWKS's **$16,263,573** —
55× smaller. Consistent with `phase-0.5-context.md §Verdict`
(`unusual_verdict: QUIET`, rank 565/4,499 on options net-direction). SWKS is not a
name the tape was focused on; the accumulation described here is **real but
small in absolute dollars**, and conviction must be scaled accordingly.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol SWKS --top-n 25 --sort-by premium --date 2026-07-31 --json` | top print: premium=3103038.72, size=49824, price=62.28, nbbo_bid=62.00, nbbo_ask=62.28, trade_vs_mid=0.14, executed_at=2026-07-31T20:00:02Z ← `.results[0]` | top-25 |
| `uw dark-pool largest --symbol SWKS --top-n 200 --sort-by premium --date 2026-07-31 --json` | n=**56** ← `.results\|length`; Σpremium=**16263573** ← `[.results[].premium]\|add`; Σsize=**263187**; min premium=100733.75 ← `.results[-1].premium` ⇒ complete ≥$100k universe | all 56 |
| `uw dark-pool block-stratified --symbol SWKS --top-n 30 --min-tier large --date 2026-07-31 --json` | `mega.trade_count`=0, `block.buy_ratio`=**0.478** (buy_volume 49824 / sell_volume 54485, 3 trades, $6,412,603.79), `large.buy_ratio`=**0.395** (62770 / 96108, 53 trades, $9,850,969.31), `highest_tier`="block", `total_premium_all_tiers`=16263573.1 ← `.results[0].<tier>.buy_ratio`; sell_ratio **derived** as `1 − buy_ratio` | 1 |
| `uw dark-pool extended-hours --symbol SWKS --top-n 15 --date 2026-07-31 --json` | 15 rows ← `.results\|length`; sole pre-market print 3100 sh @ 63.00 = $195,300 @ 11:04:08Z ← `.results[]` | top-15 |
| `uw dark-pool price-levels --symbol SWKS --top-n 15 --days 5 --json` | 64.68 → total_premium=39290060.04 / total_shares=607453 / trade_count=15; 62.48 → 17557797/281015/12; 62.28 → 7309804/117370/19; 58.49 → 3567869/61000/3 ← `.results[].price_level` etc. | top-15 |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-07-31 --json` | SWKS **absent** ← `[.results[]\|select(.ticker=="SWKS")]\|.[0]//null` = null; cutoff LITE 895983819.91 ← `.results[-1]` | top-30 |
| `uw insights deep-dive --symbol SWKS --date 2026-07-31 --json` | `uw_dark_pool` = {avg_price 61.90052, total_premium 16263573.1003, total_shares 263187, trade_count 56} ← `.uw_dark_pool` — cross-checks `largest` exactly | 1 |
| DuckDB `dp-eod-report-2026-07-31.parquet` — trade-code inventory | 4 prints/58,698 sh `average_price_trade`+`derivative_priced`; 12 prints/44,914 sh `prior_reference_price`; ⇒ **103,612 / 263,187 = 39.4% non-directional** `[DP:trade_codes DUCKDB]` | 56 |
| DuckDB — session × class × side (ET via `AT TIME ZONE 'America/New_York'`) | regular-session directional: buy 14/40,081/$2,482,937 · sell 17/46,778/$2,880,145 · flat 3/8,772 ⇒ **buy_ratio 0.461** `[DP:buy_ratio DUCKDB]` | 56 |
| DuckDB — 8-session clean buy_ratio + net imbalance | 07-29 **0.634 / +341,637 sh / +$21,160,930** on 1,489,909 dir. shares; 07-30 **0.751 / +232,129 / +$14,211,575**; 07-31 **0.461 / −6,697 / −$397,208**; baseline 07-22…07-28 −25,358…+24,390 `[DP:net_imbalance DUCKDB]` | 8 days |
| DuckDB — sub-$59.50 blocks ≥5,000 sh, 5-day window | 12 blocks, **176,487 sh / $10,373,555**, all 2026-07-29, range 58.435–59.34; largest 43,200 @ 58.4896 @ 08:37:46 ET `[DP:accumulation_shelf DUCKDB]` | 12 |
| DuckDB `stock-screener-*.parquet` OHLC | 2026-07-29 high 64.08 / **low 57.50** / close 61.19; 2026-07-31 high 63.34 / low 60.42 / close 62.28; marketcap 9,401,539,419 ⇒ derived shares out **150,956,637** | 8 days |

## Tool errors

- `uw insights deep-dive --symbol SWKS --date 2026-07-31 --json` →
  `.yahoo_fundamentals` = **`{"error":"yahoo quoteSummary SWKS: HTTP 401"}`**
  (verbatim). The Yahoo sub-block of the composite is unauthorized. This did **not**
  affect phase 2 — the `uw_dark_pool` and `uw_screener` sub-blocks returned
  normally. **Flagged forward to phase 7b**, whose fundamentals lane may depend on
  this block; it will need Finnhub / `fz` / WebSearch instead.
- DuckDB: `… END session,` → `Parser Error: syntax error at or near "session"`
  (`session` is reserved in DuckDB). Re-run with alias `sess`. No data impact.
- No `uw dark-pool` command errored. No empty results in this phase.

## DATA NOTE / CORRECTION

1. **A first-pass intraday buy-ratio of 0.287 was computed and discarded.** The
   initial decomposition split only on session (pre / regular / auction /
   post-close) using the CLI's UTC `executed_at`, giving regular-session buy
   40,081+2,513 vs sell 46,778+56,185 ⇒ **buy_ratio 0.287**, which reads as heavy
   distribution. Inspecting `sale_cond_codes` / `trade_code` on the parquet showed
   **56,185 of those 105,476 "sell" shares are `average_price_trade` /
   `prior_reference_price`** — VWAP fills and late reports whose print price
   carries no information about aggressor side. **Corrected value: buy_ratio
   0.461**, re-verified against
   `SELECT sd, SUM(size) … WHERE cls='directional' AND et BETWEEN '09:30' AND '16:00'`.
   The discarded 0.287 is recorded here because the size of the correction
   (0.287 → 0.461) is itself the reason the raw `block-stratified` ratios are not
   quoted as this phase's verdict.
2. **A DuckDB session filter silently failed and was caught.** An early cut used
   `CAST(executed_at AS VARCHAR) < '2026-07-31 20:00:00'` intending to exclude the
   auction — but the parquet stores timestamps **in ET with a `-04:00` offset**
   (`2026-07-31 16:00:02.140000-04:00`), so the string comparison matched
   everything and returned the all-session totals unchanged. Detected because the
   "intraday" output was byte-identical to the all-session output. All session
   splits reported here use
   `strftime(executed_at AT TIME ZONE 'America/New_York','%H:%M:%S')` instead.
   **No number from the failed filter was carried forward.**
3. **`sell_ratio` is derived, never read.** `block-stratified` has no `sell_ratio`
   field (`lib/uw-json-paths.md` phantom-field trap #2). All sell ratios above are
   `1 − buy_ratio`, cross-checked against `sell_volume/(buy_volume+sell_volume)`:
   block 54,485/(49,824+54,485) = 0.522 ✓; large 96,108/(62,770+96,108) = 0.605 ✓.
4. **`Shs Float` unavailable**, so the % -of-float column uses **shares
   outstanding derived from `marketcap / close`**. Stated inline at every use. True
   float-relative percentages are **larger** than quoted.

## Verdict for downstream phases

- **Bias from this phase:** **ACCUMULATION** — but *dated*: the accumulation is
  **2026-07-29 and 2026-07-30**, and the **as-of session is neutral/paused**
  (buy_ratio 0.461, net −6,697 shares). Any downstream phase must not read the
  as-of day as accumulation in its own right.
- **Conviction:** **3 / 5.** Up-weighted by the size and consistency of the
  step-change (+573,766 net shares over two sessions vs a +12k–+24k baseline; buy
  ratio held at 0.634 through a −5.40% break and rose to 0.751 the next day) and
  by the fact that it **independently corroborates phase 1's long-delta read from a
  different data source**. Held below 4 by: (a) **no mega-tier print at all**, so
  the prompt's primary accumulation test has no input; (b) the absolute dollars are
  small — $16.3M for the day, SWKS absent from the top-30 dark-pool tickers, and
  `phase-0.5-context.md`'s `QUIET` verdict caps phases 1–2 confluence; (c) the
  as-of session itself shows nothing; (d) dark-pool buy/sell classification is
  probabilistic, and **0.461 / 0.634 / 0.751 all sit in the 0.45–0.75 "suggestive
  only" band** — none reaches the >0.7 high-confidence bar except 07-30's 0.751,
  which barely clears it.
- **Largest block as % of float:** **0.033%** (49,824 sh vs 150,956,637 **shares
  outstanding**; true float % is higher — `Shs Float` unavailable, see
  `phase-0-intake.md`). **Not meaningful for this name in isolation** — a single
  0.03% print is routine for a $9.4B mega-liquid constituent. The meaningful figure
  is the **two-session aggregate at 0.380% of shares outstanding**.
- **Three S/R levels for phase-9:**
  1. **$58.44–59.34 — primary support / the accumulation shelf.** ~176,500 shares,
     ~$10.4M, 12 blocks, all 2026-07-29, of which 67,200 sh printed **pre-market**.
     Price has not revisited it (post-gap low $59.86 on 2026-07-30). This is where
     institutions demonstrably stepped in, and it **brackets the 3,333 short
     Aug-21 52.5 puts from `phase-1-flow.md`** — different instrument, same
     directional message, with the option strike a further 10% below the shelf.
  2. **$60.25–61.22 — immediate support.** Three single blocks: 102,457 sh @
     $60.25 (2026-07-29), 75,308 @ $60.83 (2026-07-29), 99,400 @ $61.22
     (2026-07-30) = ~277,000 shares / ~$17.2M. The natural first stop-reference; a
     close below $60.25 says the 07-29/30 buyers are being run over.
  3. **$64.68 — the overhead supply wall.** The single largest 5-day level at
     **$39,290,060 / 607,453 shares / 15 trades**: the 2026-07-28 pre-earnings
     close, where every pre-print holder is now underwater. This is a **hard
     resistance**, and it independently confirms `phase-1-flow.md`'s conclusion
     that upside is capped (Sep-18 62.5/65 credit call spread, 110 Jan-27 85Cs
     sold). Any phase-9 target above ~$64.70 must clear 607k shares of trapped
     supply.
  - Secondary: spot is inside a **$61.36–62.50 congestion band (~$33.5M)** —
    two-sided, no edge from level alone.
- **Open questions:**
  - **Was the 2026-07-29/30 buying accumulation or dip-hedged flow?** 573,766 net
    shares is real, but the dark pool cannot distinguish a long-only building a
    position from a market maker absorbing the gap and hedging elsewhere. Phase 3
    should check whether OI grew on the call side over the same two sessions (call
    OI 70,778 → 75,306 over 07-28 → 07-31 per `phase-0.5-context.md` — suggestive,
    needs the strike-level cut).
  - **Why did the buying stop on the as-of day (0.751 → 0.461)?** Either the
    program is complete, or the AAPL −7.35% print
    (`phase-0.5-context.md §Sector read`) made the bid step back. Phases 6 and 8
    must resolve which — it is the difference between "accumulation finished, now
    trend" and "accumulation aborted".
  - **Does the $64.68 wall or the $58.44 shelf break first?** Phase 3's gamma /
    OI-wall map and phase 4's max-pain gravity should say whether dealer
    positioning reinforces or fights the $61.36–62.50 congestion band that spot
    currently sits in.
