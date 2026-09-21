# Phase 2 — Dark Pool & Block Prints

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T01:26:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`

## Summary

**Distribution, and it independently corroborates phase 1's gap-and-crap read.** The
large tier — 188 trades, $32,667,158, immune to the closing-auction artifact — prints
`buy_ratio` **0.390**, i.e. derived `sell_ratio` **0.610**, clearing the ≤0.45
distribution threshold. An auction-stripped recount of the top-25 individual blocks agrees
independently: RTH-only, **204,542 shares printed below the NBBO mid versus 88,887 above**
(buy proxy **30.3%**). Two methods, one built from tier aggregates and one from individual
prints, bracket today's institutional side at **0.30–0.39 buy**. ENPH was sold off-exchange.

**The temporal shape is the finding.** Three of the four above-mid blocks landed in the
**first eleven minutes** of the session — 8,800 @ 38.25, 14,200 @ 38.08, 53,300 @ 37.48,
a volume-weighted **$37.56** — and then every meaningful print for the rest of the day was
below mid, at monotonically lower prices, down to 35.01. Institutions **bought the +9.03%
earnings gap and then distributed into it all session**. Those early buyers are **−6.6%
underwater** against the 35.07 close. This is the same event phase 1 saw in the options
tape (`high` 39.60 → `close` 35.07, $0.11 off the low) and in the whole-tape put/call
ask-bid split, now visible in a third, independent lane.

**Two artifacts had to be stripped and one field is structurally empty — all three would
have inverted or fabricated the read.** (1) The single largest print, 137,666 shares /
$4,827,947 at 20:00:06 UTC, is the **closing auction**, confirmed by
`ext_hour_sold_codes` = `extended_hours_trade`. It is *the entire* `sell_volume` of the
block tier, whose `buy_ratio` 0.279 therefore rests on **two trades** and is meaningless.
(2) The `price-levels --days 5` leaderboard is topped by five values — 35.07, 38.01,
36.32, 38.89, 36.70 — that are simply the **daily closing prices** of the last five
sessions, i.e. the same auction artifact repeated; the genuine institutional shelf is the
**36.15–36.30** band ($9,246,618 across 38 trades), which sits **above** spot and is now
overhead supply. (3) The **mega tier is empty** (`buy_volume` 0, `sell_volume` 0,
`trade_count` 0) and its `buy_ratio` 0.5 is a **default, not a neutral reading** — the
accumulation/distribution heuristic keyed to `mega.buy_ratio` is **n/a** this run and the
verdict rests on the large tier.

Magnitude, as everywhere in this run, is small: **$39,492,789** across all tiers,
**1,088,795 shares = 12.6% of the day's 8,670,939 share volume and 0.852% of the 127.77M
float**. ENPH is **absent from the dark-pool `ticker-summary` top-30**, whose #30 cutoff
(SPCX) is **$1,043,127,918 — 26× ENPH's entire off-exchange tape**. Phases 1–2 remain
**capped at `+`** per `phase-0.5-context.md`.

## Key signals

- **Large tier `buy_ratio` 0.390 → derived `sell_ratio` 0.610** on 188 trades,
  `buy_volume` 350,361 vs `sell_volume` 547,468, `total_premium` $32,667,158
  [DP:block_stratified]
- **Auction-stripped top-25 blocks: 204,542 shares below mid vs 88,887 above** (RTH only,
  20 blocks) → buy proxy **30.3%**; including the auction it is 20.2%
  [DP:largest]
- **The gap was bought and then distributed.** Above-mid blocks are 3-of-4 concentrated in
  the first 11 minutes at a volume-weighted **$37.56**; every print from 13:43 UTC onward
  is below mid, laddering 37.17 → 35.01 [DP:largest]
- **Closing-auction artifact isolated:** 137,666 sh / $4,827,947 @ 35.07 at 20:00:06 UTC,
  `ext_hour_sold_codes` = `extended_hours_trade`; it is 100% of the block tier's
  `sell_volume` and 72.5% of that tier's premium [DP:extended_hours]
- **Genuine institutional shelf is 36.15–36.30, ABOVE spot** — $9,246,618 across 38 trades
  — not the closing-price levels that top the raw leaderboard [DP:price_levels]
- **Mega tier structurally empty** — `trade_count` 0, `buy_ratio` 0.5 is a default →
  the mega-keyed heuristic is **n/a**, not neutral [DP:block_stratified]
- **Largest single block = 0.108% of float**; all off-exchange volume = **0.852% of
  float** — real institutional participation, unremarkable size [DP:block_pct_float fz]
- **ENPH absent from `ticker-summary` top-30** ($39.5M vs a $1.043B cutoff); **BE ranks
  #26** — the clean-energy institutional bid is in Bloom, not Enphase [DP:ticker_summary]
- **After-hours did not continue lower:** post-close prints ladder 35.07 → 34.90 by
  20:32 UTC, then recover to 35.24–35.34 by 22:34 and settle 15,089 sh @ 35.00 at 23:32 —
  net flat, mildly stabilizing [DP:extended_hours]

## Detailed findings

### A — Largest blocks (top-25, with session and NBBO-mid classification)

`float` = 127.77M (`phase-0-intake.md`, `fz screen --view ownership`). `vs mid` =
`trade_vs_mid`; positive = printed above the NBBO midpoint (buy-side lean), negative =
below (sell-side lean).

| Time (UTC) | Session | Price | Size | Premium | vs mid | NBBO bid/ask | % float |
|---|---|---|---|---|---|---|---|
| 13:30:49 | RTH | 38.715 | 6,249 | $241,930 | −0.040 | 38.57/38.94 | 0.005% |
| 13:33:39 | RTH | 37.5007 | 8,000 | $300,006 | −0.184 | 37.60/37.77 | 0.006% |
| **13:34:44** | RTH | **38.25** | **8,800** | $336,600 | **+0.150** | 38.00/38.20 | 0.007% |
| **13:35:14** | RTH | **38.08** | **14,200** | $540,736 | **+0.075** | 37.93/38.08 | 0.011% |
| **13:40:08** | RTH | **37.48** | **53,300** | **$1,997,684** | **+0.080** | 37.30/37.50 | 0.042% |
| 13:43:23 | RTH | 36.695 | 27,100 | $994,435 | −0.005 | 36.60/36.80 | 0.021% |
| 13:51:57 | RTH | 37.17 | 26,242 | $975,415 | −0.105 | 37.17/37.38 | 0.021% |
| 14:05:17 | RTH | 37.39 | 10,000 | $373,900 | −0.040 | 37.37/37.49 | 0.008% |
| 15:23:24 | RTH | 36.61 | 10,589 | $387,663 | −0.090 | 36.67/36.73 | 0.008% |
| 17:21:50 | RTH | 36.9003 | 7,000 | $258,302 | −0.025 | 36.86/36.99 | 0.005% |
| 17:51:04 | RTH | 36.265 | 12,888 | $467,383 | **0.000** | 36.24/36.29 | 0.010% |
| 18:01:12 | RTH | 36.6801 | 9,000 | $330,121 | −0.095 | 36.68/36.87 | 0.007% |
| 18:06:19 | RTH | 36.57 | 13,032 | $476,580 | −0.055 | 36.55/36.70 | 0.010% |
| 18:17:00 | RTH | 36.07 | 26,835 | $967,938 | −0.100 | 36.09/36.25 | 0.021% |
| 18:45:10 | RTH | 36.06 | 8,877 | $320,105 | −0.030 | 36.05/36.13 | 0.007% |
| **18:59:09** | RTH | **36.84** | **12,587** | $463,705 | **+0.040** | 36.77/36.83 | 0.010% |
| 19:19:40 | RTH | 36.00 | 19,300 | $694,800 | −0.055 | 36.04/36.07 | 0.015% |
| 19:19:40 | RTH | 35.96 | 11,800 | $424,328 | −0.095 | 36.04/36.07 | 0.009% |
| 19:28:34 | RTH | 35.60 | 13,473 | $479,639 | −0.020 | 35.60/35.64 | 0.011% |
| 19:50:03 | RTH | 35.01 | 7,045 | $246,645 | −0.010 | 35.01/35.03 | 0.006% |
| **20:00:06** | **AUCTION** | **35.07** | **137,666** | **$4,827,947** | −0.150 | 35.05/35.39 | **0.108%** |
| **20:00:15** | **AUCTION** | 35.07 | 9,763 | $342,388 | −0.150 | 35.05/35.39 | 0.008% |
| 20:07:19 | POST | 35.07 | 11,030 | $386,822 | −0.150 | 35.05/35.39 | 0.009% |
| 22:34:05 | POST | 35.34 | 6,920 | $244,553 | **+0.050** | 35.20/35.38 | 0.005% |
| 23:32:02 | POST | 35.00 | 15,089 | $528,115 | −0.240 | 34.88/35.60 | 0.012% |

**Session decomposition** (RTH = 13:30:00–19:59:00 UTC = 09:30–15:59 ET):

| Session | Blocks | Shares | Premium | Price range |
|---|---|---|---|---|
| **RTH** | 20 | **306,317** | **$11,277,916** | 35.01 – 38.715 |
| **Closing auction** (20:00–20:01) | 2 | 147,429 | $5,170,335 | 35.07 flat |
| **Post-close** (> 20:01) | 3 | 33,039 | $1,159,490 | 35.00 – 35.34 |
| **Total top-25** | 25 | 486,785 | $17,607,740 | |

**Side classification, with and without the auction** — the decomposition
`memory/darkpool-closing-auction-artifact.md` mandates:

| Scope | Above mid | At mid | Below mid | Buy proxy |
|---|---|---|---|---|
| **RTH only (auction-free)** | 4 blocks / **88,887 sh** | 1 / 12,888 | 15 / **204,542 sh** | **30.3%** |
| All 25 incl. auction + post | 5 / 95,807 | 1 / 12,888 | 19 / 378,090 | 20.2% |

Stripping the auction moves the read from 20.2% to **30.3% buy** — a 10pp swing that
**does not flip the sign**. That is the important outcome: unlike the HOOD case in
`memory/darkpool-closing-auction-artifact.md` (0.803 → 0.227, sign inverted), here the
artifact **exaggerates** an already-real distribution rather than manufacturing it.
Distribution survives the strip, which is what makes this phase's verdict trustworthy.

**The intraday arc — the most informative structure in this phase:**

| | Time window | Blocks | Shares | VWAP | vs 35.07 close |
|---|---|---|---|---|---|
| **Gap bought** | 13:34:44 – 13:40:08 | 3 above mid | **76,300** | **$37.66** | **−6.9%** |
| All above-mid (RTH) | 13:34 – 18:59 | 4 | 88,887 | **$37.56** | **−6.6%** |
| Below-mid ladder | 13:43 – 19:50 | 15 | 204,542 | 35.01 → 37.17 range | — |

Read against `phase-1-flow.md` §C, the two lanes describe one event. Institutions paid
**above the midpoint** for 76,300 shares in the first six minutes of trading, at
37.48–38.25, while the stock printed its 39.60 high. From 13:43 UTC onward the print tape
is **uninterruptedly below mid** — 15 consecutive size blocks stepping 37.17 → 36.70 →
36.61 → 36.57 → 36.27 → 36.07 → 36.06 → 36.00 → 35.96 → 35.60 → 35.01. Supply met the
gap and won. The 18:59:09 above-mid print at 36.84 (12,587 sh) is the only counter-tick
after the open, and it did not hold.

**Float normalization** (advisory, `[DP:block_pct_float fz]`): the largest block is
**0.108% of float**; the entire top-25 is **0.381%**; all off-exchange volume across
tiers is **0.852%**. For a 127.77M-float name these are **real institutional prints but
unremarkable in size** — no single actor moved a position-defining stake. Consistent with
`ticker-summary` excluding ENPH from the top-30 (§E). Size does not add conviction here;
the *pattern* does.

### B — Tier breakdown

`uw dark-pool block-stratified --symbol ENPH --top-n 30 --min-tier large` → 1 row.
`highest_tier` = **`block`** (no mega prints). `total_premium_all_tiers` = **$39,492,789.05**.

| Tier | `buy_ratio` | derived `sell_ratio` | `buy_volume` | `sell_volume` | `total_premium` | `trade_count` |
|---|---|---|---|---|---|---|
| **large** | **0.390** | **0.610** | 350,361 | 547,468 | **$32,667,158** | **188** |
| block | 0.279 | 0.721 | 53,300 | 137,666 | $6,825,631 | **2** |
| mega | *0.5 (default)* | *n/a* | **0** | **0** | **$0** | **0** |
| retail | *0.5 (default)* | *n/a* | **0** | **0** | **$0** | **0** |

`sell_ratio` is **derived as `1 − buy_ratio`** — there is no `sell_ratio` field
(`lib/uw-json-paths.md` phantom-field trap, confirmed against the returned key set:
`block, highest_tier, large, mega, retail, ticker, total_premium_all_tiers`, with
buy/sell nested per tier).

**The large tier is the verdict and it is robust.** `buy_ratio` **0.390** on **188
trades** and $32.7M clears the distribution threshold (`buy_ratio` ≤ 0.45). No single
print can dominate 188 trades. Its independent agreement with the auction-stripped
top-25 count (30.3% buy) is the strongest evidence in this phase.

**The block tier must be discarded, not reported.** Its `buy_ratio` 0.279 rests on
**exactly two trades**: `buy_volume` 53,300 — the 13:40:08 gap purchase at 37.48 — and
`sell_volume` 137,666 — **the closing auction at 35.07** (§C). Remove the auction and the
block tier reads 53,300 buy / 0 sell = `buy_ratio` **1.000**. Both numbers are artifacts of
a 2-observation sample. **Any downstream citation of "block tier 72% selling" would be
false.**

**The mega tier is empty, and 0.5 is a default rather than a neutral reading.** With
`buy_volume` 0, `sell_volume` 0, `trade_count` 0 and `total_premium` $0, the
accumulation/distribution heuristics in the phase spec — both keyed to
`.results[].mega.buy_ratio` — are **inapplicable this run**. This is the same class of
trap as the structurally-empty MSPR field in `memory/data-source-workarounds.md`: an
empty aggregate that renders as a plausible mid-range number. Recorded as **n/a**; the
verdict rests on the large tier, which the heuristic's spirit supports (`sell_ratio`
0.610 ≥ 0.55 with clusters not above spot — see §D).

**Confidence calibration.** Per the phase's own pitfall note, dark-pool buy/sell is
probabilistic (NBBO-based): ratios > 0.7 are high-confidence, **0.55–0.7 suggestive
only**. Large-tier `sell_ratio` **0.610 sits in the suggestive band**, and the
auction-stripped print count (69.7% below mid) is also inside it. This is why conviction
below is **3, not 4** despite three lanes agreeing — the *direction* is well-corroborated;
the *classification method* is inherently probabilistic.

**Participation context:** total off-exchange volume = 350,361 + 547,468 + 53,300 +
137,666 = **1,088,795 shares** = **12.6%** of the day's 8,670,939 share volume
(`phase-1-flow.md` §C) and **0.852% of float**. Normal-to-healthy off-exchange
participation; no evidence of an unusual institutional footprint by size.

### C — Extended-hours activity

`uw dark-pool extended-hours --symbol ENPH --top-n 15` → 15 rows, every one carrying
`ext_hour_sold_codes` = **`extended_hours_trade`** (the only value present in the set).

| Window | Prints | Shares | Premium | Price range |
|---|---|---|---|---|
| **Pre-market** (< 13:30 UTC) | 2 | **6,000** | $222,464 | 36.89 – 37.2648 |
| **Post-close** (≥ 20:00 UTC) | 13 | **211,390** | $7,414,087 | 34.90 – 35.34 |

**Pre-market was tiny and already marked the gap.** Only 6,000 shares printed, at
**36.89 and 37.2648** (12:21:18 and 12:24:02 UTC = 08:21 / 08:24 ET) — both **above** the
36.32 prior close. The market knew the print was being taken well before the open; there
was simply no institutional size behind it. 6,000 shares is 0.005% of float.

**This call is what confirms the auction artifact.** The 20:00:06 UTC print of 137,666
shares — the largest single block of the day and the entire `sell_volume` of the block
tier — is returned by the **extended-hours** endpoint and tagged
`extended_hours_trade`. It is a closing cross, not intraday institutional intent.
Together with 20:00:15 (9,763 sh) and 20:00:01 (4,166 sh), the 35.07 auction cluster is
**151,595 shares**. Its `trade_vs_mid` of −0.150 is an artifact of a stale, 34-cent-wide
NBBO (35.05/35.39) at the bell, not evidence of selling.

**Post-close price action does not extend the decline** — a genuinely useful, mildly
constructive datapoint:

| Time (UTC) | Price | Size |
|---|---|---|
| 20:00:01 – 20:00:15 | 35.07 (auction cluster) | 151,595 |
| 20:07:19 | 35.07 | 11,030 |
| 20:12:18 | 35.0301 | 4,000 |
| 20:16:58 / 20:17:05 | 35.061 / 35.0725 | 3,000 / 3,000 |
| 20:22:47 | 34.99 | 3,756 |
| **20:32:24** | **34.90** ← post-close low | 5,700 |
| 22:33:26 | 35.24 / 35.25 | 3,800 / 3,500 |
| **22:34:05** | **35.34** (+0.05 vs mid) | 6,920 |
| 23:32:02 | 35.00 | 15,089 |

ENPH probed **34.90** by 20:32 UTC, then **recovered to 35.24–35.34** by 22:33–22:34
(the 6,920-share print at 35.34 being the only above-mid print of the after-hours
session), and settled with 15,089 shares at **35.00** at 23:32. Net: **flat around
35.00–35.34, no continuation lower.** For a stock that closed $0.11 off its session low
after engulfing a +9% gap, the absence of after-hours follow-through is a mild
stabilization signal and the clearest counterweight in this phase to the bearish read.

Per the phase's pitfall guidance, these are **not** flagged as index rebalancing or ETF
creation/redemption: the prints ladder continuously with price rather than crossing in one
size at one level, and the pre-market total is a trivial 6,000 shares. Phase 6 should
confirm no overnight ENPH-specific headline explains the 22:33–22:34 recovery.

### D — Price levels (5-day institutional clusters)

`uw dark-pool price-levels --symbol ENPH --top-n 15 --days 5`. `total_shares` returned
**`null` for all 15 rows** — a phantom field this run; ranking and interpretation use
`total_premium` and `trade_count` only.

| Rank | Level | Premium | Trades | Reading |
|---|---|---|---|---|
| 1 | **35.07** | $5,909,197 | 6 | **today's close — auction artifact** |
| 2 | **38.01** | $5,354,568 | 5 | **07-27 close — artifact** |
| 3 | **36.32** | $4,281,438 | 9 | **07-28 close — artifact** |
| 4 | **38.89** | $4,188,807 | 5 | **07-23 close — artifact** |
| 5 | **36.70** | $3,581,087 | 11 | **07-24 close — artifact** |
| 6 | 37.48 | $2,166,344 | 2 | the gap-buy block |
| 7 | 36.20 | $1,991,000 | 5 | genuine |
| 8 | **36.27** | $1,857,235 | **11** | **genuine — densest** |
| 9 | **36.30** | $1,541,413 | **10** | **genuine** |
| 10 | 36.24 | $1,333,886 | 1 | genuine |
| 11 | 36.15 | $1,330,305 | 3 | genuine |
| 12 | **36.28** | $1,192,779 | **8** | **genuine** |
| 13 | 36.84 | $1,157,008 | 6 | genuine |
| 14 | 37.20 | $1,124,364 | 4 | genuine |
| 15 | 36.00 | $1,098,036 | 2 | genuine |

**The raw leaderboard must not be used as-is.** Its top five levels are precisely the
**closing prices of the last five sessions** — 35.07 (07-29), 38.01 (07-27), 36.32
(07-28), 38.89 (07-23), 36.70 (07-24), all cross-checked against the OHLC table in
`phase-1-flow.md` §C. These are closing-auction crosses aggregated across the window: the
§A artifact, repeated five times. Reporting 35.07 and 38.01 as "institutional support and
resistance" would be reporting the closing print as though it were a decision.

**The genuine institutional shelf is 36.15 – 36.30**, which no single row makes obvious:

| Level | Premium | Trades |
|---|---|---|
| 36.15 | $1,330,305 | 3 |
| 36.20 | $1,991,000 | 5 |
| 36.24 | $1,333,886 | 1 |
| 36.27 | $1,857,235 | 11 |
| 36.28 | $1,192,779 | 8 |
| 36.30 | $1,541,413 | 10 |
| **Band total** | **$9,246,618** | **38** |

**$9.25M across 38 trades in a 15-cent band** is 2.3× the premium and 3.8× the trade count
of the largest non-artifact single level. It is where institutions actually transacted
repeatedly.

**Its position relative to spot is the interpretation.** The shelf sits at **36.15–36.30,
which is 3.1%–3.5% ABOVE the 35.07 close**. Read with §A — the below-mid ladder passed
straight through 36.27 (12,888 sh at mid, 17:51), 36.07 and 36.06 without pausing — this
band is **distribution inventory, now overhead supply**, not accumulation support.
Institutions did not defend it. Per the phase heuristic, distribution requires clusters
*below* spot; here the clusters are *above* spot **because price has already fallen
through them**, which is the same evidence viewed later in the sequence. **Phase 9 should
treat 36.15–36.30 as the first genuine resistance band, not as support.**

**No cluster sits within 1% of spot (34.72–35.42).** The nearest genuine (non-close) level
is **36.00** ($1,098,036, 2 trades), **2.7% above**. There is **no institutional price
shelf beneath the current price in the 5-day window** — nothing in this lane supports 35
as a defended level. Phase 3 must supply that from the $35 put wall
(`phase-0-intake.md`: 3,734 contracts at the 08-21 expiry) if it exists at all.

> **Window caveat.** `--days 5` anchors to the **latest available date**, not to `--date`.
> Latest available = **2026-07-29** = the as-of date (`phase-0-intake.md`), so the window
> is 2026-07-23 → 2026-07-29 and is as-of-correct **for this run only**; a re-run after a
> new session lands will slide it. The five artifact levels independently confirm the
> window's contents (they are exactly the five session closes 07-23, 07-24, 07-27, 07-28,
> 07-29), which is a useful accidental validation of the boundary.

### E — Universe context: ENPH is not a top dark-pool name

`uw dark-pool ticker-summary --top-n 30 --date 2026-07-29`: **ENPH absent**
(null-safe select → `null`).

Top-30: SPY, MU, QQQ, SNDK, NVDA, AAPL, MSFT, INTC, META, AMD, TSLA, LQD, AMZN, SOXL,
VOO, STX, GOOGL, IWM, HYG, TQQQ, NBIS, AVGO, SMH, GOOG, SKHY, **BE**, TSM, CAT, SOXX,
SPCX.

The #30 cutoff (SPCX) is `total_premium` **$1,043,127,918** against ENPH's
`total_premium_all_tiers` of **$39,492,789** — ENPH's *entire* off-exchange tape is
**26× below** the threshold. In absolute institutional terms ENPH is a small name and
today was not an exception, reinforcing the magnitude discipline from
`phase-0.5-context.md` (universe 93.8th percentile on option premium, but 26.6th on its
*own* history).

**BE at #26 is the notable adjacency**, and it now recurs across three independent lanes:
BE was the **#9 most bearish** name on net option premium (−$28,202,872,
`phase-0.5-context.md`), carries the clean-energy complex's largest option volume
(253,397 contracts), and is the only solar/clean-energy name in the dark-pool top-30.
Combined with `phase-1-flow.md` §H (PLUG on the bearish smart-money list, NRG on
sweep-ratio), the pattern is consistent: **institutions are expressing clean-energy views
with real size — in BE, PLUG and NRG. Not in ENPH.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw dark-pool largest --symbol ENPH --top-n 25 --sort-by premium --date 2026-07-29 --json` | Σ`size`=486785, Σ`premium`=17607740 ← `[.results[].size]\|add`; RTH split above/at/below mid = 88887 / 12888 / 204542 ← `select(.executed_at[11:19]>="13:30:00" and <"19:59:00")\|group_by(.trade_vs_mid>0)`; largest `size`=137666 @ `price`=35.07, `executed_at`=…T20:00:06Z | top-25 |
| `uw dark-pool block-stratified --symbol ENPH --top-n 30 --min-tier large --date 2026-07-29 --json` | `large.buy_ratio`=0.390, `large.buy_volume`=350361, `large.sell_volume`=547468, `large.total_premium`=32667158.43, `large.trade_count`=188; `block.buy_ratio`=0.279 / `trade_count`=2; `mega.trade_count`=**0** / `mega.buy_ratio`=0.5 (default); `highest_tier`="block"; `total_premium_all_tiers`=39492789.05 | 1 |
| `uw dark-pool extended-hours --symbol ENPH --top-n 15 --date 2026-07-29 --json` | `ext_hour_sold_codes` unique = `["extended_hours_trade"]`; PRE 2 prints / 6000 sh / $222464 @ 36.89–37.2648; POST 13 prints / 211390 sh / $7414087 @ 34.90–35.34 ← `group_by(.executed_at[11:19]<"13:30:00")`; **20:00:06 137666 @ 35.07 present here** | top-15 |
| `uw dark-pool price-levels --symbol ENPH --top-n 15 --days 5 --json` | `price_level` 35.07 $5909197/6tr, 38.01 $5354568/5tr, 36.32 $4281438/9tr, 38.89 $4188807/5tr, 36.70 $3581087/11tr; genuine band 36.15–36.30 Σ$9246618 / 38 tr ← `.results[]`; **`total_shares`=null for all 15** | top-15, 5 sessions |
| `uw dark-pool ticker-summary --top-n 30 --date 2026-07-29 --json` | ENPH **absent** ← `[.results[]\|select(.ticker=="ENPH")]\|.[0]//null` → `null`; cutoff SPCX `total_premium`=1043127917.97 ← `.results[29]`; BE at index 25 (#26) | top-30 |
| `fz screen --tickers ENPH --view ownership --agent` (from `phase-0-intake.md`) | `Float`=127.77M → % -of-float column | 1 |
| DuckDB (via `phase-1-flow.md` §C) | `total_volume`=8670939 → off-exchange share 1088795/8670939 = 12.6% | 1 |

All five `uw` reads were captured to a file before being queried and every value
round-tripped through `jq` on validated JSON; the ENPH-row select on `ticker-summary` used
the null-safe `[…]|.[0]//null` form per `memory/batched-stdout-swallow.md`. Derived
values, each stated inline: `sell_ratio = 1 − buy_ratio` (§B), session buckets from
`executed_at[11:19]` (§A, §C), above/below-mid counts from `trade_vs_mid` sign (§A),
above-mid VWAP (§A), the 36.15–36.30 band aggregate (§D), and total off-exchange volume
as the sum of the four tiers' buy+sell volumes (§B).

## Tool errors

None. All five `uw dark-pool` calls returned exit 0 with parseable JSON.

Two **data-quality** findings (not invocation errors — both returned exit 0, which is why
they are dangerous):

1. **`price-levels` returns `total_shares` = `null` for all 15 rows** while
   `total_premium` and `trade_count` populate correctly. Any share-count normalization off
   this leaf would silently produce nulls. Interpretation in §D uses premium and trade
   count only. Candidate addition to the `lib/uw-json-paths.md` phantom-field list
   (**propose-only**, per the audit convention).
2. **`block-stratified` returns `mega.buy_ratio` = 0.5 on `trade_count` = 0.** The
   documented accumulation/distribution heuristic keys on exactly this field, so a naive
   read would report "mega tier neutral at 0.50" when the correct answer is **no mega
   prints exist**. Same failure class as the structurally-empty MSPR field in
   `memory/data-source-workarounds.md`. Recommend the phase spec require a
   `trade_count > 0` guard before citing any tier ratio (**propose-only**).

## DATA NOTE / CORRECTION

No value in this phase was revised after its first validated read.

Three readings were **rejected before use** rather than corrected after — recorded here
because each would have produced a materially wrong verdict:

1. **Block-tier `buy_ratio` 0.279 → discarded.** Traced to `trade_count` = 2, whose
   `sell_volume` (137,666) is exactly the 20:00:06 UTC closing-auction print confirmed via
   `extended-hours`. Auction-free, the tier reads `buy_ratio` 1.000. Neither number is
   reportable. Verified against `.results[0].block.{buy_ratio,buy_volume,sell_volume,trade_count}`
   cross-referenced to `.results[]|select(.size==137666)` in `largest` and to the
   `extended-hours` row set.
2. **Top-25 aggregate side split 20.2% buy → superseded by 30.3% (RTH-only).** Verified
   against `select(.executed_at[11:19]>="13:30:00" and .executed_at[11:19]<"19:59:00")`.
   Per `memory/darkpool-closing-auction-artifact.md`, both are reported (§A) so the size of
   the artifact is on the record. The sign is unchanged — distribution either way.
3. **`price-levels` top-5 → excluded as S/R.** 35.07 / 38.01 / 36.32 / 38.89 / 36.70 are
   the five session closes 07-29 / 07-27 / 07-28 / 07-23 / 07-24, cross-checked against
   the OHLC table in `phase-1-flow.md` §C. The genuine shelf is the 36.15–36.30 band.
4. **`mega.buy_ratio` 0.5 → recorded as n/a, not neutral** (`trade_count` = 0), so the
   mega-keyed heuristic is inapplicable and the verdict rests on the 188-trade large tier.

This phase **confirms** rather than corrects `phase-1-flow.md`'s DATA NOTE: the
intraday gap-and-crap that phase established from OHLC and print-level `underlying_price`
is independently visible in the block tape (gap bought above mid at a VWAP of $37.56 in
the first 11 minutes, then 15 consecutive below-mid blocks laddering to 35.01).

## Verdict for downstream phases

- **Bias from this phase: DISTRIBUTION.**
- **Conviction: 3 / 5.** Direction is corroborated by two independent, artifact-free
  measures (large tier `sell_ratio` 0.610 on 188 trades; auction-stripped top-25 at 69.7%
  below mid) and by a third lane in `phase-1-flow.md`. Held at 3 rather than 4 because
  (a) **0.610 sits in the 0.55–0.70 "suggestive only" band** of a probabilistic NBBO
  classifier, not the >0.70 high-confidence band; (b) the **mega tier is empty**, so the
  spec's primary accumulation/distribution key is unavailable; (c) magnitude is small —
  0.852% of float, $39.5M total, **absent from the `ticker-summary` top-30** against a
  $1.043B cutoff; (d) `phase-0.5-context.md`'s BUSY_NAME_NORMAL_DAY **caps phases 1–2 at
  `+`**; and (e) after-hours **did not** extend the decline (34.90 → 35.34 → 35.00), the
  one genuine counterweight.
- **Largest block as % of float:** **0.108%** (137,666 sh vs 127.77M float) — and that
  print is the **closing auction**, so it carries no directional information. The largest
  *intraday* block is 53,300 sh = **0.042% of float**, and it was a **buy** at 37.48.
  Total off-exchange volume is **0.852% of float** / 12.6% of share volume. **For a
  127.77M-float name this is genuine institutional participation at unremarkable size —
  the pattern carries the signal, not the magnitude, and size adds no conviction here.**
- **Three S/R levels for phase-9:**
  1. **36.15 – 36.30 → first genuine RESISTANCE** ($9,246,618 / 38 trades, the densest
     non-artifact cluster; **3.1–3.5% above spot**). Institutions distributed here and did
     not defend it on the way down — treat as overhead supply. Extend to **36.00**
     ($1,098,036) as the band's lower lip.
  2. **34.90 → nearest tested SUPPORT** (post-close low, 5,700 sh; session low **34.96**).
     Note this is a *price* level, not a dark-pool cluster — **no institutional shelf
     exists below spot in the 5-day window**, the nearest genuine level being 36.00,
     **2.7% above**. Phase 3 must source any real 35 defence from the $35 put wall.
  3. **37.48 – 38.25 → the trapped-buyer zone** (76,300 sh bought above mid at a VWAP of
     **$37.66**, now −6.9%). Expect supply on any retest; a reclaim of 38.25 on volume
     would invalidate this phase's distribution read.
- **Open questions:**
  - **Does the $35 put wall (3,734 contracts, 08-21) actually create dealer support at
    35?** Phase 2 finds **no institutional cluster below spot** — if phase 3 also finds no
    real wall, then 34.96/34.90 is an untested edge, not support, and phase 9 cannot place
    a stop just beneath it. (→ 3, 4)
  - **Do the 40 / 55 / 75 call-writing strikes from `phase-1-flow.md` §D ($405,922 of
    long-dated call supply) show up as OI builds?** If the same institutions distributing
    stock in the 36.15–36.30 band are writing those calls, it is one coherent
    monetization programme rather than two unrelated signals. (→ 3)
  - **Who bought 76,300 shares above mid at a VWAP of $37.66 in the first six minutes, and
    are they still long?** If that position is liquidated, it is 0.06% of float of
    additional supply into any bounce. Watch 07-30 for continuation blocks below 35.
    (→ 5, 9)
  - **Does the 22:33–22:34 after-hours recovery to 35.24–35.34 correspond to an overnight
    headline, or is it mechanical?** The one above-mid after-hours print (6,920 sh @
    35.34) sits there. (→ 6)
  - **Why is institutional clean-energy conviction landing in BE (#26 dark pool, #9 most
    bearish on options), PLUG and NRG but not ENPH?** Three lanes now show the same
    absence. Is ENPH un-owned, un-hedgeable, or simply already de-rated? (→ 6, 7b, 7c)
