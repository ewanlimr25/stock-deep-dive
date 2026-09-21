# Phase 2 — Dark Pool & Block Prints

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T21:32:00-04:00
**Upstream phases cited:** `phase-0-intake.md` (float 1.12B), `phase-0.5-context.md`, `phase-1-flow.md`

## Summary

**MU was the single largest dark-pool name in the entire market today — $12.93B across
15,787,788 shares (1.41% of the 1.12B float), ahead of SPY ($11.40B) and QQQ ($9.74B)** — and
the headline tier read looks like massive accumulation: **`mega.buy_ratio = 0.803`**. **That
signal is an artifact and it inverts on inspection.** 88% of mega-tier premium is post-close
prints struck at exactly the $820.53 closing price against a stale NBBO of 818.18/819.03, which
the NBBO-based classifier necessarily marks "buy." **Restricted to regular hours, the mega-tier
buy ratio collapses from 0.803 to 0.227 — 77.3% SELLING** (3 buys / 57,902 sh vs 9 sells /
196,620 sh). Every tier is a net seller in regular hours (mega 0.227, block 0.423, large 0.481;
share-weighted ≈ **0.464**), and the buy ratio is *lowest at the lowest prices* (790s 0.411,
800s 0.419) — institutions **sold into weakness rather than absorbing it**. The verdict is
**DISTRIBUTION**, and it directly contradicts the naive read of `block-stratified`. The
after-hours tape confirms: excluding auction prints, post-close trades VWAP'd at **$809.02
(-1.4% vs close)** and the last prints of the evening (18:51–19:02 ET) were at **$780.00–789.00,
roughly -5% below the close**.

## Key signals

- **MU ranks #1 of all tickers in dark-pool premium: $12,931,901,814 on 15,787,788 shares**
  (avg $817.22) — above SPY and QQQ. [DP:ticker_summary]
- **`mega.buy_ratio = 0.803` is a closing-auction artifact.** Regular-hours-only mega buy ratio
  = **0.227**. [DP:block_stratified] + [DP:session_split DUCKDB]
- **Every tier distributes in regular hours:** mega 0.227, block 0.423 (derived sell 0.577),
  large 0.481. [DP:block_stratified]
- **Selling was heaviest at the lows:** $790 bin buy_ratio 0.411, $800 bin 0.419, vs $820 bin
  0.497. No absorption on the dip. [DP:price_bins DUCKDB]
- **Largest print: 2,759,188 shares @ $820.53 = $2.264B at 16:10:12 ET** — **0.246% of float**
  in one cross, post-close, at the closing price. [DP:largest] [DP:block_pct_float fz]
- **After-hours slid to $780–789 by 19:00 ET** (~-5% vs close) on $0.478B of non-auction
  post-close prints VWAP $809.02. [DP:extended_hours]

## Detailed findings

### Largest blocks

`uw dark-pool largest --top-n 25 --sort-by premium` (times converted to ET; float = 1.12B):

| time (ET) | price | size | premium | NBBO bid/ask | % of float | note |
|---|---:|---:|---:|---|---:|---|
| 16:10:12 | 820.53 | **2,759,188** | **$2,263,996,530** | 818.18 / 819.03 | **0.246%** | post-close, px > ask |
| 16:08:14 | 820.53 | 526,583 | $432,077,149 | 814.35 / 815.99 | 0.047% | post-close, px > ask |
| 16:08:55 | 820.53 | 444,393 | $364,637,788 | 820.28 / 821.00 | 0.040% | post-close, at mid |
| **09:21:49** | **900.20** | 216,955 | $195,302,891 | 848.00 / 848.36 | 0.019% | **pre-market at PRIOR close px** |
| 16:08:55 | 820.53 | 204,869 | $168,101,161 | 820.28 / 821.00 | 0.018% | post-close |
| 09:35:02 | 834.00 | 66,000 | $55,044,000 | 834.07 / 834.55 | 0.006% | intraday, px < bid → sell |
| 16:37:37 | 827.41 | 56,660 | $46,881,056 | 823.76 / 825.00 | 0.005% | after-hours |
| 16:00:00 | 820.53 | 45,725 | $37,518,734 | 820.53 / 820.72 | 0.004% | the close itself |
| 10:19:54 | 791.22 | 25,230 | $19,962,481 | 791.11 / 791.54 | 0.002% | at the intraday low |
| 11:48:41 | 830.00 | 23,902 | $19,838,660 | 829.48 / 829.72 | 0.002% | px > ask → buy |
| 11:53:46 | 831.62 | 20,000 | $16,632,400 | 827.02 / 827.44 | 0.002% | px > ask → buy |
| 09:47:54 | 807.48 | 18,276 | $14,757,504 | 807.48 / 808.09 | 0.002% | at bid → sell |
| 10:20:18 | 790.32 | 18,118 | $14,319,018 | 790.27 / 790.73 | 0.002% | near low |
| 10:38:13 | 808.79 | 15,113 | $12,223,243 | 809.17 / 809.55 | 0.001% | px < bid → sell |
| 09:30:07 | 840.56 | 13,620 | $11,448,427 | 842.71 / 843.50 | 0.001% | px < bid → sell |

**Read this table by session, not by size.** The four largest prints are all **post-close
crosses at exactly $820.53**, and two of them (2.76M sh and 526k sh) print *above the prevailing
NBBO ask* — mechanically classified "buy" by any NBBO rule, but economically they are
closing-auction/late-reported crosses where the quote snapshot is meaningless. The fourth-largest
is a **pre-market print at $900.20 — the previous session's close — while the live NBBO was
848.00/848.36**, i.e. 6% above the market. That is a late-report or specially-priced cross, not
an aggressive buyer paying up.

### Tier breakdown — and the artifact

`uw dark-pool block-stratified --min-tier large` (`total_premium_all_tiers` = $12,931,901,814,
reconciling exactly to `insights_deep_dive.uw_dark_pool.total_premium`):

| tier | trades | buy_volume | sell_volume | **`buy_ratio`** | derived sell_ratio | total_premium |
|---|---:|---:|---:|---:|---:|---:|
| **mega** (≥$10M) | **20** | 3,633,841 | 891,607 | **0.803** | 0.197 | $3,731,149,180 |
| **block** (≥$1M) | 898 | 966,537 | 1,222,393 | **0.442** | **0.558** | $1,788,526,973 |
| **large** (≥$100k) | 30,680 | 4,592,949 | 4,480,461 | 0.506 | 0.494 | $7,412,225,661 |
| retail (<$100k) | 0 | 0 | 0 | 0.500 | — | $0 |

*(There is no `sell_ratio` field — derived as 1 − `buy_ratio` per the known field trap.)*

Taken at face value this reads: 20 mega blocks 80% bought (accumulation) while the $1–10M tier
distributes (0.442). **That framing is wrong.** Decomposing the 20 mega trades by session — my
DuckDB replication of the NBBO classifier **reproduces UW's 0.803 exactly**, validating the
method — gives:

| session | class | trades | shares | premium |
|---|---|---:|---:|---:|
| **post-close** | buy | 4 | 3,358,984 | $2.757B |
| **post-close** | sell | 3 | 694,987 | $0.570B |
| pre-market | buy | 1 | 216,955 | $0.195B |
| **regular** | **buy** | **3** | **57,902** | **$0.048B** |
| **regular** | **sell** | **9** | **196,620** | **$0.161B** |

**During the actual trading session, mega blocks ran 9 sells to 3 buys — 196,620 shares sold vs
57,902 bought.** The 0.803 is manufactured by four post-close crosses totalling 3.36M shares.

**Buy ratio, all-session vs regular-hours-only:**

| tier | `buy_ratio` (all) | **`buy_ratio` (regular hours)** | shares (all) | shares (reg) |
|---|---:|---:|---:|---:|
| **mega** | 0.803 | **0.227** | 4,525,448 | 254,522 |
| block | 0.420 | 0.423 | 2,188,930 | 1,983,749 |
| large | 0.482 | 0.481 | 9,072,410 | 8,296,100 |

*(My all-session block/large ratios — 0.420 / 0.482 — differ trivially from UW's 0.442 / 0.506
because of `mid`-print handling; the mega figure matches to three decimals and the direction of
every tier agrees. Cited UW values are the source of truth; the regular-hours column is the
escape-hatch addition.)*

**Share-weighted regular-hours buy ratio across all tiers ≈ 0.464 → 53.6% selling.** Per the
rubric (`Distribution: mega buy_ratio ≤ 0.45 AND clusters below spot`), MU's regular-hours mega
ratio of **0.227** clears the threshold by a wide margin. Per the pitfall note, a ratio this far
from 0.5 (0.227 → 77.3% sell) sits in the **high-confidence** band.

### Price levels

**(a) Regular-hours $10 bins, today only** — the honest intraday distribution:

| bin | trades | shares | premium | **buy_ratio** |
|---|---:|---:|---:|---:|
| $810–820 | 11,036 | 3,914,319 | $3.192B | 0.471 |
| $820–830 | 10,027 | 3,462,384 | $2.852B | 0.497 |
| $800–810 | 3,588 | 1,367,094 | $1.102B | **0.419** |
| $790–800 | 2,373 | 932,109 | $0.741B | **0.411** |
| $830–840 | 1,605 | 703,530 | $0.586B | 0.429 |

**70% of regular-hours volume (7.38M of 10.53M shares) transacted in the $810–830 band**, and
**every bin is below 0.5**. The gradient is the tell: **the lower the price, the heavier the
selling** (790s = 0.411, 800s = 0.419) — the opposite of absorption. Institutions were not
defending $790–810; they were feeding stock into it.

**(b) Hourly VWAP + buy ratio** — the intraday path:

| hour (ET) | shares | VWAP | buy_ratio |
|---|---:|---:|---:|
| 09 | 2,481,323 | 820.93 | **0.412** |
| 10 | 3,158,336 | **805.93** | 0.461 |
| 11 | 1,431,865 | 820.40 | 0.508 |
| 12 | 867,802 | 823.56 | 0.473 |
| 13 | 747,366 | 817.94 | 0.482 |
| 14 | 650,197 | 818.48 | 0.502 |
| 15 | 1,197,482 | 823.95 | 0.487 |

Gap down, trough in the 10:00 hour (VWAP $805.93, prints as low as $790.32), then a grind back
to close at $820.53. Selling pressure was heaviest at the open (0.412) and never turned into
genuine accumulation (peak hourly buy ratio 0.508).

**(c) 5-day clusters** (`price-levels --days 5`, `dates_covered` = 07-22…07-28 — window
terminates on our as-of date, so point-in-time correct):

| price level | premium | shares | trades |
|---:|---:|---:|---:|
| **820.53** | $3.331B | 4,059,410 | 74 |
| 900.20 | $1.568B | 1,742,082 | 98 |
| 920.95 | $1.311B | 1,423,427 | 73 |
| 990.21 | $0.729B | 736,309 | 118 |
| 959.48 | $0.593B | 617,958 | 121 |
| 892.86 | $0.180B | 201,893 | **4** |
| 966.00 | $0.100B | 103,412 | 72 |
| 970.00 | $0.073B | 75,590 | 172 |
| 990.14 | $0.071B | 71,290 | 14 |
| 990.00 | $0.070B | 70,719 | 188 |
| 974.00 | $0.062B | 63,956 | 146 |
| **834.00** | $0.060B | 72,028 | 23 |

**Methodological caveat (important):** the top five "levels" are **exactly the five daily
closing prices** of the five covered sessions (820.53, 900.20, 920.95, 990.21, 959.48). These
buckets are dominated by closing-auction prints, so they measure *where each day closed*, not
independent institutional support/resistance. Do not read "$3.33B defended 820.53" — 4,055,726
of those 4,059,410 shares printed **after 16:00 ET at the closing price**.

The genuinely informative non-close levels are **$892.86** ($180M in only **4 trades** — ~50k
shares each, real block activity) and **$834.00** ($60M / 23 trades). Above spot, the
**$966–992 shelf** (aggregating ~$0.32B across 990.21/990.14/990/992/991/974/975/966/970) is
**overhead supply from the 7/22–7/23 sessions** that MU must now climb back through.

### Extended-hours activity

Session decomposition of the full day (ET):

| session | trades | shares | premium | avg price |
|---|---:|---:|---:|---:|
| pre-market (<09:30) | 1,071 | 605,346 | $0.523B | $843.20 |
| regular (09:30–16:00) | 28,987 | 10,534,371 | $8.602B | $816.70 |
| **post-close (≥16:00)** | 1,539 | **4,647,071** | **$3.806B** | **$809.00** |

Post-close is **29.4% of the day's dark-pool shares** — abnormally large, and the reason the
tier ratios are distorted. Splitting it:

| group | trades | shares | premium | VWAP |
|---|---:|---:|---:|---:|
| **at closing price ($820.53)** | 61 | 4,055,726 | $3.328B | 820.53 |
| **true after-hours (other px)** | 1,478 | 591,345 | $0.478B | **$809.02** |

**The 61 prints at exactly $820.53 are the closing cross and associated late-reported crosses —
87.3% of post-close shares.** Strip them and real after-hours trading VWAP'd at **$809.02, 1.4%
below the close.**

Largest true after-hours prints, in time order:

| time (ET) | price | size | premium | vs close |
|---|---:|---:|---:|---:|
| 16:24:59 | 832.20 | 4,107 | $3.42M | +1.4% |
| 16:37:37 | **827.41** | **56,660** | **$46.88M** | +0.8% |
| 16:43:34 | 825.50 | 4,329 | $3.57M | +0.6% |
| 17:39:11 | 832.00 | 5,000 | $4.16M | +1.4% |
| 18:51:34 | 788.87 | 3,960 | $3.12M | **-3.9%** |
| 18:53:05 | 789.00 | 4,551 | $3.59M | **-3.9%** |
| **19:00:52** | **780.00** | 5,913 | $4.61M | **-4.9%** |
| **19:02:01** | **781.51** | 5,000 | $3.91M | **-4.7%** |

**A clear after-hours downtrend: MU held $825–832 until ~17:40 ET, then broke to $788–789 by
18:51 and $780–781 by 19:00.** That is a further ~5–6% decline from the post-close highs, on
modest but consistent size. Whatever repriced MU during the day **continued to reprice it after
hours**, which is not the footprint of a completed capitulation.

Pre-market for completeness: the $195.3M / 216,955-share print at 09:21:49 struck at $900.20
(the prior close) against an NBBO of 848.00/848.36 — flagged as a late-report/special cross, not
a directional pre-market buy. Genuine pre-market prints were at $837.80–841.36, already ~7%
below the prior close, confirming MU gapped down before the bell.

### Float normalization (advisory — `fz`, `Shs Float` = 1.12B)

| measure | shares | **% of float** |
|---|---:|---:|
| Total dark pool today | 15,787,788 | **1.410%** |
| Regular-hours only | 10,534,371 | 0.940% |
| Closing-auction cluster @820.53 | 4,055,726 | 0.362% |
| Mega tier (all sessions) | 4,525,448 | 0.404% |
| **Single largest block** | **2,759,188** | **0.246%** |
| Mega tier, **regular hours only** | 254,522 | 0.023% |
| True after-hours | 591,345 | 0.053% |

`[DP:block_pct_float fz]` — **Is this size meaningful for MU?** 1.41% of float in one session is
genuinely large in absolute terms, and the 2.76M-share single block (0.246% of float) would be a
headline event in most names. **But MU is a $926.7B mega-cap that prints dark-pool blocks every
session** (per the mega-cap pitfall, the signal is *change vs baseline*), and — decisively —
**the mega-tier footprint that actually occurred during trading hours is only 0.023% of float
and was 77% sold**. The impressive percentages belong to the closing auction, not to a
discretionary accumulator. **This is advisory context only and does not raise conviction.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw dark-pool ticker-summary --top-n 30 --date 2026-07-28 --json` | **MU rank #1** (index 0): premium=12,931,901,814, shares=15,787,788; SPY #2 $11.398B; QQQ #3 $9.736B ← `[.results[].ticker]\|index("MU")`, `.results[0]` | top-30 |
| `uw dark-pool block-stratified --symbol MU --top-n 30 --min-tier large --date … --json` | **mega.buy_ratio=0.803** (buy 3,633,841 / sell 891,607, 20 trades, $3.731B); block.buy_ratio=0.442; large.buy_ratio=0.506; total_all_tiers=12,931,901,814 ← `.results[0].mega.buy_ratio` etc. | 1 row |
| `uw dark-pool largest --symbol MU --top-n 25 --sort-by premium --date … --json` | top print: price=820.53, size=2,759,188, premium=2,263,996,530, nbbo 818.18/819.03, executed_at 20:10:12Z ← `.results[]` | top-25 |
| `uw dark-pool price-levels --symbol MU --top-n 15 --days 5 --date … --json` | 820.53 → $3.331B/4,059,410sh/74 trades; 892.86 → $180.3M/4 trades; `dates_covered`=07-22…07-28 ← `.results[]` | top-15 |
| `uw dark-pool extended-hours --symbol MU --top-n 15 --date … --json` | 23:00:52Z px=780.00 sz=5,913 $4.61M; 20:37:37Z px=827.41 sz=56,660 $46.88M ← `.results[]` | top-15 |
| DuckDB session split (`dp-eod-report-2026-07-28.parquet`) | pre 605,346sh/$0.523B; **reg 10,534,371sh/$8.602B**; **post 4,647,071sh/$3.806B** | 31,597 MU rows |
| DuckDB mega-tier classifier replication | **all=0.803 (matches UW), regular-only=0.227**; reg 3 buys/57,902 vs 9 sells/196,620 | mega rows |
| DuckDB buy_ratio by tier × session | block reg 0.423; large reg 0.481; weighted reg ≈0.464 | all tiers |
| DuckDB regular-hours $10 price bins | 810s 0.471 / 820s 0.497 / **800s 0.419** / **790s 0.411** / 830s 0.429 | reg rows |
| DuckDB hourly VWAP | 09h $820.93 (0.412) → 10h **$805.93** → 15h $823.95 (0.487) | reg rows |
| DuckDB post-close auction split | at-820.53: 61 prints/4,055,726sh/$3.328B · **other: 1,478/591,345sh/VWAP $809.02** | post rows |
| `fz screen --view ownership` (phase-0 carry) | `Float` = 1.12B → % -of-float column | 1 row |

## Tool errors

None. All five `uw dark-pool` commands exited 0 and every payload round-tripped through `jq`.

## DATA NOTE / CORRECTION

No value was re-read or corrected — every figure above stood on first read. Three
**interpretive** corrections are recorded instead, because the raw fields are misleading as
returned:

1. **`mega.buy_ratio = 0.803` is reported faithfully but must not be read as accumulation.** The
   escape-hatch decomposition (which reproduces UW's own number to three decimals, confirming
   the classifier) shows it is produced by 4 post-close crosses; the regular-hours value is
   **0.227**. Both numbers appear above; downstream phases must use the regular-hours figure for
   the directional read and cite 0.803 only as the raw field.
2. **`price-levels` top-5 are the five sessions' closing prices**, not discovered S/R. Flagged
   inline so phase-9 does not treat "$3.33B at 820.53" as institutional defense of that level.
3. **`extended-hours` mixes the closing cross with true after-hours.** Separated above; the
   directional content is in the 1,478 non-auction prints (VWAP $809.02), not the 61 auction
   prints (VWAP $820.53).

My all-session `block`/`large` buy ratios (0.420 / 0.482) differ from UW's (0.442 / 0.506) by
≈0.02 due to `mid`-print treatment; **UW's values are cited as authoritative** in the tier table
and the discrepancy is disclosed rather than silently reconciled.

## Verdict for downstream phases

- **Institutional bias: DISTRIBUTION.** Regular-hours mega buy_ratio **0.227** (rubric threshold
  for distribution is ≤0.45), block 0.423, large 0.481 — every tier a net seller — with the
  heaviest selling at the *lowest* prices (790s 0.411) and a continued slide to $780 after hours.
- **Conviction: 4 / 5.** High, and higher than phase-1's, for three reasons: (a) the size is
  real and enormous — MU was the #1 dark-pool name in the market at 1.41% of float; (b) the
  regular-hours ratio of 0.227 is deep in the high-confidence band (>0.7 sell-side); (c) it is
  **corroborated independently** by the after-hours VWAP ($809.02) and the 19:00 ET prints at
  $780. Held below 5 because the classification is NBBO-probabilistic and one session is not a
  campaign.
- **Largest block as % of float: 0.246%** (2,759,188 sh, $2.264B). *Advisory:* impressive in the
  abstract, but it is a **post-close cross at the closing price** — for a $926.7B mega-cap that
  prints blocks daily, this is auction mechanics, not conviction. The discretionary
  regular-hours mega footprint was **0.023% of float and 77% sold**. **Does not raise conviction.**
- **Three S/R levels for phase 9:**
  1. **$790–806 — the live support shelf.** Today's intraday trough (hour-10 VWAP $805.93, prints
     to $790.32); ~2–3.7% below spot. **Weak, not defended** — it carries the day's *lowest* buy
     ratios (0.411/0.419) and after-hours already traded beneath it to $780.
  2. **$820.53 — the closing-auction anchor**, 4.06M shares. Treat as a *reference/pin* level,
     not as demand. It is where 70% of regular volume clustered ($810–830 band) and where the
     phase-1 1DTE call ladder (815/820/825/830) is struck.
  3. **$900.20 / $920.95 overhead, then the $966–992 shelf.** Prior-session closes carrying
     $1.57B and $1.31B, plus ~$0.32B of 7/22–7/23 supply at $966–992. Any bounce faces
     **9.7%, 12.2% and 18–21%** of overhead respectively.
  *(Cross-reference: phase-1 identified **$750–800** as where a large options participant sold
  the put strip — immediately beneath the $790–806 shelf. If $790 fails, $750 is the next
  structural reference.)*
- **Open questions:**
  - **Who was the 2.76M-share ($2.264B) counterparty at 16:10 ET?** Index/ETF rebalancing,
    an ETF creation/redemption, or a genuine block cross? If it is a real buyer, the
    distribution read weakens materially; if it is rebalancing, it is noise. Phase-6/7c news
    may resolve it. **Flagged and conviction de-rated accordingly per the extended-hours pitfall.**
  - **Does the dark-pool distribution reconcile with phase-1's ITM call selling (-$25.1M,
    46–180DTE)?** Overwriting implies a *retained* long; outright distribution implies an
    exiting one. Both cannot be the same holder. → phase 3 OI.
  - **Does phase-3 OI show the 750/800 put strip OPENING or CLOSING?** Phase-1's decisive
    question is unchanged and is now sharper: dark-pool distribution makes the "closing
    protective puts" reading *less* coherent (why sell protection while selling stock?) and the
    "opening short puts" reading harder to square with the same desks distributing.
  - Was the after-hours break to $780 news-driven (a late headline, or FOMC-eve positioning)?
    → phase-6 / 7c.
