# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`

## Summary

**FSLR reported Q2 earnings on 2026-07-30 (AMC) — today is the day-1 reaction.**
This was not supplied by any single field; it was recovered by tracking
`next_earnings_date` across the 78 local screener snapshots, where it flipped
**2026-07-30 → 2026-10-29 on exactly 2026-07-31**. Every downstream phase must
read today's tape as post-event, not as a clean directional day.

The headline context is a **divergence**: price closed **+2.44% at 211.03** on
**1.68× normal stock volume**, call volume ran **2.58× its 30-day average** —
and yet net-directional option premium is **negative** and sits in the
**bottom 1.2 percentile of 4,499 optionable names** (`net_call_premium`
−$1.01M, `net_put_premium` +$1.28M → net −$2.29M). Calls were net *sold* and
puts net *bought* into a post-earnings pop. FSLR's own sector (Technology) is
simultaneously the **worst** sector on the directional tape at **−$187.7M**
net bullish−bearish premium. Name and sector agree, and they disagree with
price.

Against its own history the day is only *moderately* unusual (net-directional
in the 21st self-percentile of 67 sessions; total premium a middling 60.6th),
so the unusualness lives in the **composition** of the flow, not its size.
Phase 0.5 sets no bias — but it hands phases 1–2 a specific question: is the
negative net premium **call overwriting into strength** or **directional put
buying**?

## Universe ranking

Universe N = **4,499** optionable names with option volume today
(`stock-screener-2026-07-31.parquet`).

| Metric | FSLR value | Universe percentile | Read |
|--------|-----------|--------------------:|------|
| Total option premium | $26.66M (call 19.84M + put 6.83M) | **97.7** | Top 2.3% — a busy name |
| Net-directional prem (`net_call_prem − net_put_prem`) | **−$2.29M** | **1.2** | Bottom 1.2% — extreme bearish |
| Net bullish−bearish prem | **−$2.37M** | **1.1** | Bottom 1.1% |
| IV rank | 81.94 | **92.8** | High-vol name |
| Option vol vs stock avg30 | 0.02 | 96.4 | Options-heavy relative to its float turnover |

**Leaderboard placement:**

- **Net bullish premium:** FSLR is **outside top-60**. Leaders (single names,
  ETFs set aside): AMZN +$89.6M, NVDA +$60.5M, GOOG +$40.8M, MSTR +$37.0M,
  GOOGL +$28.3M, SNDK +$20.9M, SBUX +$11.3M. (Index products NDX +$122.4M,
  QQQ +$31.8M, SPY +$27.5M, SOXX +$19.2M, XSP +$17.4M dominate the raw list.)
- **Net bearish premium:** FSLR ranks **#50** at **−$2.37M**, wedged between
  SPOT (−$2.39M) and IESC (−$2.36M). Leaders: SPX −$886.7M, MU −$158.4M,
  AAPL −$141.1M, SPXW −$138.8M, EWY −$23.8M, RDDT −$22.9M, AMD −$20.9M,
  SOXL −$20.7M, TSLA −$20.4M, MSFT −$12.4M.
- **Volume-vs-average (`--min-volume-ratio 2`):** **outside top-60** — that
  list is monopolised by microcaps with absurd ratios (INBK 2240×, FYC 600×,
  MSFY 300×). FSLR's real read comes from its own averages below.
- **IV rank (high):** **outside top-100**, despite an 81.94 IV rank in the
  92.8th universe percentile — 100+ names carry a higher rank today.

**Volume vs FSLR's own 30-day option averages** (the meaningful cut):

| Series | Today | 30-day avg | Ratio |
|--------|------:|-----------:|------:|
| Call volume | 24,254 | 9,382.8 | **2.58×** |
| Put volume | 6,770 | 7,326.8 | **0.92×** |
| Total option volume | 31,024 | 16,709.6 | **1.86×** |
| Stock volume | 3,014,081 | 1,799,313 | **1.68×** |

The asymmetry is the story: **call volume nearly tripled while put volume was
below average** — yet the *premium* signature is net-bearish. High call
turnover with negative net call premium is the fingerprint of calls being
**sold** (written), not bought.

## Sector read

Net bullish−bearish premium summed by sector, non-index names only:

| Sector | N | Net bull−bear ($M) | Total prem ($M) | % green |
|--------|--:|-------------------:|----------------:|--------:|
| Consumer Cyclical | 341 | **+86.4** | 3,868.5 | 28.7 |
| Communication Services | 161 | +38.0 | 2,142.9 | 49.1 |
| Consumer Defensive | 135 | +3.9 | 128.6 | 29.6 |
| Utilities | 95 | +3.4 | 124.8 | 29.5 |
| Energy | 193 | +1.1 | 148.2 | **81.9** |
| Real Estate | 171 | −0.4 | 36.3 | 27.5 |
| Basic Materials | 204 | −3.7 | 99.0 | 22.1 |
| Healthcare | 618 | −5.9 | 491.9 | 23.5 |
| Financial Services | 422 | −17.9 | 984.3 | 42.7 |
| Industrials | 462 | −20.9 | 1,292.6 | 54.3 |
| **Technology (FSLR)** | 531 | **−187.7** | 13,379.4 | 58.2 |

**Technology is the most-sold sector on the options tape today by a factor of
9× the next-worst**, even though 58.2% of tech names closed green — the same
price-vs-premium divergence FSLR shows, at sector scale. Per the phase-0.5
heuristics this is *not* the yellow-flag case (name strong / sector sold);
it is the **aligned** case: FSLR's bearish premium signature matches its
sector's. Phase-6 inherits a live question — is this tech-wide de-risking
(index hedging bleeding into single names) or genuine single-name
distribution? Note the top bearish leaderboard is itself tech-led (MU, AAPL,
AMD, SOXL, MSFT), which leans toward the former.

Energy at 81.9% green with barely positive net premium is the day's clearest
rotation destination; Consumer Cyclical leads on premium with only 28.7%
green (concentrated, not broad).

## Self-history

Window: **2026-04-27 → 2026-07-31 = 67 sessions**. The pre-gap block
(2026-03-13…03-27) is **excluded** — per `phase-0-intake.md`, local data has a
~1-month hole (2026-03-27 → 2026-04-27) and a percentile spanning it would be
non-contiguous.

| Metric | Self-percentile (N=67) | Read |
|--------|-----------------------:|------|
| Net-directional premium | **21.2** | Bottom quintile — bearish for FSLR, but ~14 of its own sessions were *more* bearish |
| Net bullish−bearish premium | 25.8 | Same picture |
| Total option premium | **60.6** | Middling — today is *not* a size outlier for FSLR |
| IV rank | **39.4** | 81.94 is *below* FSLR's own recent median — it habitually runs high IV |
| Option vol vs stock avg30 | 87.9 | Elevated turnover |

The IV reading is the one most likely to be misread downstream: an 81.94 IV
rank sits in the **92.8th universe** percentile but only the **39.4th
self** percentile. FSLR printed a **100.0** IV rank on 2026-07-23, 07-24 and
07-28 into the print. **Do not treat 81.94 as "elevated vol" for this name** —
it is post-earnings vol *crush*, and phase-4/5 must price it that way.

**Last 12 sessions** (the run-up and the event):

| Date | Close | Chg% | Call vol | Put vol | Net-dir ($M) | Net bull−bear ($M) | IV rank | iv30d |
|------|------:|-----:|---------:|--------:|-------------:|-------------------:|--------:|------:|
| **2026-07-31** | **211.03** | **+2.44** | **24,254** | 6,770 | **−2.29** | **−2.37** | 81.9 | 0.738 |
| 2026-07-30 | 206.01 | +3.40 | 12,339 | 6,953 | +0.02 | +0.02 | 94.6 | 0.795 |
| 2026-07-29 | 199.24 | −1.65 | 5,533 | 1,957 | −0.85 | −0.85 | 91.1 | 0.811 |
| 2026-07-28 | 202.59 | −1.57 | 5,250 | 7,890 | −1.06 | −0.95 | **100.0** | 0.805 |
| 2026-07-27 | 205.83 | +1.48 | 9,265 | 4,938 | −3.64 | −3.67 | 98.3 | 0.775 |
| 2026-07-24 | 202.82 | −1.51 | 6,409 | 3,210 | 0.00 | 0.00 | **100.0** | 0.806 |
| 2026-07-23 | 205.92 | −1.41 | 4,137 | 4,619 | −1.15 | −2.35 | **100.0** | 0.792 |
| 2026-07-22 | 208.86 | +1.36 | 9,115 | 3,767 | −0.24 | −0.24 | 96.4 | 0.759 |
| 2026-07-21 | 206.05 | +0.36 | 10,549 | **12,070** | **+14.17** | **+18.41** | 97.0 | 0.753 |
| 2026-07-20 | 205.31 | −3.15 | 23,422 | 9,795 | −2.09 | −3.80 | 99.1 | 0.764 |
| 2026-07-17 | 211.99 | +0.03 | 11,335 | 7,381 | −1.29 | −1.29 | 92.0 | 0.753 |
| 2026-07-16 | 211.93 | −5.31 | 8,136 | 4,985 | −1.58 | −2.01 | 83.1 | 0.723 |

Three things this table says:

1. **Net-directional premium has been negative on 10 of the last 12 sessions.**
   Today is a continuation of a persistent bearish premium regime, not a new
   signal — which cuts both ways: it is confirmed, but it is also *already
   in the price* (the stock is flat-to-lower over the same span, 211.93 → 211.03).
2. **2026-07-21 is the lone violent outlier** (+$14.17M net-dir, +$18.41M
   net bull−bear) on put volume 12,070 > call volume 10,549 — the signature of
   large **put selling**, not call buying. Phase-3 should check whether that OI
   is still open; if so there is a bullish structural position underneath this
   tape that today's flow does not capture.
3. **IV crush is confirmed and modest**: 94.6 → 81.9 IV rank, iv30d 0.795 →
   0.738. A drop that small after a print means the market is *not* done
   pricing movement — consistent with `implied_move_perc` still at 0.76%/day.

## Source

**CLI + DuckDB.** Rankings and the `uw_screener` block come from the `uw` CLI;
exact percentiles, the sector leaderboard, the earnings-date flip and the
self-history series come from the DuckDB escape hatch (`lib/duckdb-cuts.md`
§C) against `~/Documents/Stocks/Stock Screener/stock-screener-*.parquet`.
All DuckDB-derived numbers are tagged ` DUCKDB` downstream.

**Outside top-N (information, not error):** net-bullish premium (outside
top-60), volume-vs-average ≥2 (outside top-60), IV rank high (outside
top-100).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw screener bullish-bearish --direction bullish --top-n 60 --date 2026-07-31 --json` | FSLR absent ← `[.results[].ticker]\|index("FSLR")` → null; leader AMZN net=89581893 ← `.results[1].net_flow` | top-60 |
| `uw screener bullish-bearish --direction bearish --top-n 60 --date 2026-07-31 --json` | FSLR idx=49 (rank #50) ← `[.results[].ticker]\|index("FSLR")`; net_flow=−2374671, iv_rank=81.9358, put_call_ratio=0.2791 ← `[.results[]\|select(.ticker=="FSLR")]\|.[0]` | top-60 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 60 --date 2026-07-31 --json` | FSLR null ← `[.results[].ticker]\|index("FSLR")`; INBK ratio=2240.4 ← `.results[0].volume_ratio` | top-60 |
| `uw screener iv-rank --mode high --top-n 100 --date 2026-07-31 --json` | FSLR null ← `[.results[].ticker]\|index("FSLR")` | top-100 |
| `uw insights deep-dive --symbol FSLR --date 2026-07-31 --json` | iv_rank=81.9358, iv30d=0.737828, implied_move=1.6113, implied_move_perc=0.0076247, total_open_interest=577414, next_earnings_date=2026-10-29 ← `.uw_screener.*` | 1 |
| DuckDB §C universe `PERCENT_RANK()` over `stock-screener-2026-07-31.parquet` | universe_n=4499; pctile_total_prem=97.7; pctile_net_dir=1.2; pctile_iv_rank=92.8 | 4,499 |
| DuckDB §C self-history over 67 post-gap screener files | self_pctile_net_dir=21.2; self_pctile_total=60.6; self_pctile_iv_rank=39.4; sessions_in_window=67 | 67 |
| DuckDB `GROUP BY sector` on `stock-screener-2026-07-31.parquet` | Technology net_bb=−187.7M / n=531 / 58.2% green | 3,333 non-index |
| DuckDB `GROUP BY next_earnings_date` over all 78 screener files | 2026-07-30 last_seen 2026-07-30 (n=62) → 2026-10-29 first_seen 2026-07-31 (n=1) | 78 |
| `fz screen --tickers FSLR --view technical --json` | RSI=43.00, ATR=10.34, Beta=1.76, Gap=+3.29%, Change from Open=−0.82%, SMA20=−1.49%, SMA50=−13.93%, SMA200=−9.91%, 52W High=−34.25% | 1 |

## Tool errors

None — all commands exited 0 and every payload round-tripped through `jq`
(or pandas `to_string` for the DuckDB cuts).

Two non-fatal notes carried from `phase-0-intake.md`: `fz quote` remains
degraded to 14 fields (unused here — the `fz screen --view technical` path was
used instead), and `fz screen` still emits `"Ticker": "FFSLR"`.

`fz news FSLR --json` returned **general market wire, not ticker-filtered
news** (headlines about Amazon, SpaceX, the Fed). No FSLR-specific headline
was retrievable on that path, so the earnings date was established from the
screener parquet instead. Phase-7c must source FSLR news elsewhere.

## DATA NOTE / CORRECTION

The UW `next_earnings_date` of **2026-10-29** was initially treated as suspect
per the standing "UW earnings dates can be stale" caution. **It is correct and
current** — the parquet history shows it rolled forward on 2026-07-31 itself.
The field was not stale; the *prior* value (2026-07-30) was the event. No
number was changed, but the interpretation was inverted: this is a
**post-earnings day-1** run, not a pre-earnings run.

The phase-0.5 recipe's `vol_x` = option volume ÷ **stock** `avg30_volume`
yields 0.02 for FSLR — a cross-sectionally comparable ratio (hence the valid
96.4 percentile) but **not** "option volume vs its own option average." The
latter was computed separately (1.86× total, 2.58× calls) and is the figure
quoted in the narrative. Both are reported above so the 0.02 is not
mistaken for a collapse in activity.

## Verdict for downstream phases

- **Bias from this phase:** **none** — phase 0.5 sets context only.
- **Conviction:** n/a

```
universe_pctile_total_prem:  97.7
universe_rank_net_dir:       #50 on the bearish leaderboard (outside top-60 bullish); 1.2 universe percentile
sector_leadership:           TECHNOLOGY is LAGGING — worst sector on the tape at -$187.7M net bull-bear
iv_rank:                     81.94   (92.8 universe pctile, but only 39.4 SELF pctile - post-earnings crush)
implied_move_pct:            0.76%   (daily, $1.61 on a 211.03 close - no event premium left)
self_pctile_net_dir:         21.2    (N=67 sessions, post-gap window)
unusual_verdict:             GENUINELY_UNUSUAL
```

**Justification and challenge for the `unusual_verdict`** (phase-10 should
audit this): the strict rubric wants rank ≤~25 on net-directional **and**
vol-vs-avg ≥2 **and** self_pctile ≥80. Read symmetrically for a bearish day
(distance from the median, since the rubric's thresholds are written
bullish-side), FSLR scores: universe **48.8 points** from median (extreme),
total option volume **1.86×** — just under the ≥2 bar, though calls alone run
**2.58×** — and self-history **28.8 points** from median (moderate, not
extreme). That is **one clear pass, two marginal**. The verdict is set to
GENUINELY_UNUSUAL on the strength of the cross-sectional extreme and the
composition (2.58× call volume with *negative* net call premium), **not** on
size — FSLR's absolute dollars are mid-pack and its total-premium
self-percentile is an ordinary 60.6. **If phase-1 finds the negative net call
premium is routine covered-call overwriting rather than aggressive selling,
this verdict should be downgraded to BUSY_NAME_NORMAL_DAY and phase-1/2
confluence capped at `+`.**

- **Three things later phases should remember:**
  1. **Today is day-1 post-earnings (reported 2026-07-30 AMC).** Gap +3.29%,
     faded −0.82% from the open, closed +2.44%. IV rank 94.6 → 81.9. Any
     "unusual flow" read must net out event mechanics, and any options
     structure must respect that the vol crush is *already* partly done —
     with `iv30d` still 0.738 and IV rank only in FSLR's 39th self-percentile,
     there is less premium left to sell than the 81.94 headline implies.
  2. **The core divergence to resolve in phase 1:** call volume **2.58×**
     average and price **+2.44%**, yet `net_call_premium` is **−$1.01M** and
     `net_put_premium` **+$1.28M** — bottom **1.2 percentile** of 4,499 names.
     Someone sold this pop. Determine whether that is overwriting (neutral,
     supply of upside) or directional (bearish).
  3. **Technology is the day's worst sector (−$187.7M)** and the bearish
     leaderboard is tech-led (MU, AAPL, AMD, SOXL, MSFT). FSLR's bearish
     premium may be **sector beta, not stock-specific** — phase-6 must
     separate the two before phase-9 sizes anything.
- **Open questions:**
  - Is 2026-07-21's +$14.17M net-directional (on put volume > call volume, i.e.
    put *selling*) still open in OI? → phase-3.
  - Net-directional premium has been negative 10 of 12 sessions while price
    went nowhere (211.93 → 211.03). Is the bearish premium *predictive* or
    already discounted? → phase-5 must test the persistence, not assume it.
  - Price is **−34.25% from its 52-week high (320.95)** but **+22.70% off the
    low (171.99)**, below SMA20/50/200 with RSI 43 and Beta 1.76. Is the
    post-earnings gap a trend change or a bounce in a downtrend? → phase-4/5.
