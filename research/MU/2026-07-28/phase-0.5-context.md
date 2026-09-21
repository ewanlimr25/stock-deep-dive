# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T21:14:00-04:00
**Upstream phases cited:** `phase-0-intake.md` (float 1.12B, close -8.85% @ $820.53, gap 2026-03-27→04-27)

## Summary

MU's flow is **big in dollars and utterly ordinary in unusualness**. Total option premium of
**$3.025B ranks in the 99.96th percentile** of the 4,632-name optionable universe — effectively
#2 on the tape — yet MU's own option volume is **0.84× its 30-day average** (61.65th universe
percentile) and today sits at only the **45.9th percentile of MU's own 75-session history**.
Net directional premium is **+$28.6M on $2.83B gross — a 1.0% tilt**, i.e. statistically
balanced. This is the textbook **BUSY_NAME_NORMAL_DAY** signature: the numbers are enormous
because MU is an $820 stock with a $926.7B cap, not because anything unusual happened in
options. The genuinely unusual event today was in **price, not flow** — and it was
**sector-specific**: SPY closed **+0.24%** and NVDA **+0.25%**, while the memory/storage/semicap
complex was destroyed (SNDK **-14.25%**, MU **-8.85%**, STX **-8.53%**, AMD **-8.15%**,
AMAT **-7.82%**, LRCX **-7.54%**). This is a memory-cycle repricing, not risk-off.

**Self-history carries the loudest warning:** this skill's prior MU run on **2026-06-25** marked
the **exact closing peak — 1213.56** — and correctly refused the entry. MU is now **-32.4%**
from that print, and that run's stated invalidation ("two daily closes below 1052") triggered on
**2026-07-01/07-02**. Both prior MU theses are dead. Phase 9 must treat "buy the memory dip"
with extreme prejudice: the last two attempts to define a shelf (**$1,134**, then **$1,052**)
were both sliced through.

## Universe ranking

MU's rank on **net directional premium** (`net_flow` = bullish − bearish), full top-12:

| # | Ticker | net_flow | bullish_prem | bearish_prem |
|---|--------|---------:|-------------:|-------------:|
| 1 | SNDK | +$146.42M | $1.230B | $1.084B |
| 2 | QQQ *(ETF)* | +$123.46M | $1.303B | $1.179B |
| 3 | SPXW *(index)* | +$63.00M | $1.710B | $1.647B |
| 4 | NBIS | +$51.69M | $232.6M | $180.9M |
| 5 | NDX *(index)* | +$49.17M | $241.5M | $192.3M |
| 6 | GLD *(ETF)* | +$41.33M | $129.9M | $88.6M |
| 7 | AAPL | +$31.23M | $249.5M | $218.3M |
| **8** | **MU** | **+$28.56M** | **$1.4294B** | **$1.4008B** |
| 9 | AMAT | +$28.02M | $84.4M | $56.4M |
| 10 | NOW | +$26.55M | $58.8M | $32.3M |

- **Rank 8 overall; rank 4 among single names** (setting aside QQQ/SPXW/NDX/GLD per the
  index-ETF pitfall) — behind SNDK, NBIS, AAPL.
- **The rank flatters MU.** Its $1.429B of *bullish* premium is the largest single-name figure
  on the tape (bigger than QQQ's), but its *bearish* premium is $1.401B — nearly identical.
  MU is #1 in gross two-way premium and merely #8 in net. **A 1.0% net tilt on $2.83B is
  noise, not a directional signal.** [CTX:net_flow]
- **Exact universe percentiles (n=4,632 optionable names):**

  | Metric | Value | Universe %ile |
  |---|---:|---:|
  | Total option premium | **$3.025B** | **99.96** |
  | Net directional premium | +$28.56M | **99.85** |
  | IV rank | 83.48 | 90.00 |
  | **Option volume ÷ 30-day avg option volume** | **0.84×** | **61.65** |
  | Stock volume ÷ 30-day avg | 1.13× | 73.53 |

  `[CTX:universe_pctile DUCKDB]`
- **The 0.84× option-volume ratio is the whole story.** MU is **outside the top-50** on
  `screener volume-vs-average` (that list is dominated by illiquid microcaps — SNN 2885×,
  ZUMZ 675× — whose denominators are near zero). MU is not merely un-elevated; it traded
  **less** option volume than its own norm on a -8.85% day. **Nobody rushed in.**
- MU is also **outside the top-50 on IV rank** — that list is saturated with names pinned at
  IVR 100 (REPL, GLAS, EOSE, FSLR, AMGN…). MU's 83.48 is high in absolute terms but only the
  90th universe percentile.

## Sector read

Net-directional premium and price breadth by sector (single names, `is_index=false`):

| Sector | n | net_dir | total prem | avg chg | % green |
|---|---:|---:|---:|---:|---:|
| **Technology** | 536 | **+$143.6M** | **$14.09B** | **-0.70%** | **47.4%** |
| Communication Services | 167 | +$59.6M | $1.45B | +1.89% | 75.4% |
| Healthcare | 624 | +$13.5M | $0.50B | +0.33% | 52.6% |
| Financial Services | 447 | +$10.4M | $0.72B | +1.05% | 75.8% |
| Consumer Defensive | 141 | +$5.6M | $0.23B | +1.92% | 85.8% |
| Utilities | 91 | +$2.7M | $0.20B | -0.66% | 50.5% |
| Real Estate | 168 | +$0.9M | $0.04B | +0.36% | 61.3% |
| Energy | 196 | -$1.5M | $0.13B | -1.96% | 23.5% |
| Basic Materials | 207 | -$11.9M | $0.12B | -0.99% | 35.7% |
| Industrials | 478 | -$28.5M | $1.53B | -0.50% | 50.2% |
| Consumer Cyclical | 357 | -$30.8M | $2.21B | +1.61% | 77.3% |

**Technology is the day's paradox: #1 in flow dollars (+$143.6M net, $14.09B gross) and the
worst large sector on price (-0.70% avg, only 47.4% green).** Every other major sector was
broadly green — Consumer Defensive 85.8% green, Financial Services 75.8%, Comm Services 75.4%,
Consumer Cyclical 77.3%. **This is a rotation OUT of semis into the rest of the market**, not a
market-wide de-risking.

Zooming to MU's actual peer group makes the epicenter unmistakable:

| Ticker | close | chg% | net_dir | tot prem | IVR |
|---|---:|---:|---:|---:|---:|
| SNDK | 1096.10 | **-14.25%** | +$146.4M | $2.66B | 82.3 |
| **MU** | **820.53** | **-8.85%** | **+$28.6M** | **$3.03B** | **83.5** |
| STX | 747.30 | -8.53% | +$3.1M | $0.20B | 91.9 |
| AMD | 454.62 | -8.15% | +$6.2M | $0.98B | 85.4 |
| AMAT | 476.46 | -7.82% | +$28.0M | $0.16B | 94.2 |
| LRCX | 269.61 | -7.54% | +$1.0M | $0.17B | 86.9 |
| WDC | 463.51 | -6.91% | **-$19.0M** | $0.17B | 90.3 |
| KLAC | 190.80 | -6.18% | -$0.2M | $0.07B | 91.0 |
| INTC | 86.30 | -5.86% | -$18.8M | $0.59B | 73.6 |
| SMCI | 28.45 | -4.56% | -$0.7M | $0.02B | 87.7 |
| SMH | 529.60 | -3.45% | -$16.0M | $0.49B | 92.6 |
| TSM | 392.31 | -1.70% | -$35.8M | $0.29B | 74.2 |
| QQQ | 675.49 | -0.97% | +$123.5M | $2.96B | 76.8 |
| AVGO | 380.91 | -0.60% | +$6.9M | $0.12B | 52.2 |
| **SPY** | **740.86** | **+0.24%** | +$13.3M | $1.90B | 27.2 |
| **NVDA** | **197.01** | **+0.25%** | +$0.1M | $0.94B | 64.0 |

- **The selloff is a clean gradient by memory/storage/semicap exposure.** Pure memory & storage
  (SNDK, MU, STX, WDC) and wafer-fab-equipment (AMAT, LRCX, KLAC) took -6% to -14%. Logic/AI
  compute was untouched: **NVDA +0.25%, AVGO -0.60%, TSM -1.70%**. SPY was **green**.
- **NVDA green while MU -8.85% kills the "AI demand is cracking" reading.** Whatever repriced
  today is specific to the *memory/DRAM/HBM supply-demand or pricing* narrative, or to
  semicap orders — not to AI end-demand. **Phase 6 and phase 7c must identify the catalyst;
  this phase can only bound it.**
- **Yellow flag per the phase heuristic (name strong on flow while its group is sold):** the
  three largest net-*bullish* single names on the entire tape — SNDK (+$146.4M, -14.25%), MU
  (+$28.6M, -8.85%), AMAT (+$28.0M, -7.82%) — are precisely the three worst performers.
  Bullish premium is pouring into names being violently marked down. That is either
  **dip-buying / falling-knife catching**, or **put-selling and call-overwriting into crushed
  prices**, which the premium sign cannot distinguish. **Phase 1 must classify aggressor side
  and moneyness before any of this counts as bullish.** [CTX:flow_vs_price_divergence]

## Self-history

**Today vs MU's own 75-session local window** (2026-03-13 → 2026-07-28; **N=75 available
sessions, not contiguous** — one 31-day hole 2026-03-27→04-27 per `phase-0-intake.md`):

| Metric | Self %ile |
|---|---:|
| Net directional premium | **64.9** |
| Total premium | **58.1** |
| IV rank | **43.2** |
| Option volume | **45.9** |

`[CTX:self_pctile DUCKDB]` — **every metric is mid-pack for MU.** IVR 83.48 sits at only the
**43rd percentile of MU's own recent range**: MU has been living at IVR 80–95 for a month, so
today's "high" IV rank is, for this name, *below normal*. Note the implication for structure —
**a -8.85% day that did not lift MU's IV rank above its own median means the move was largely
already priced by the vol surface.**

**Recent tape (last 12 sessions):**

| date | close | chg% | net_dir | tot prem | P/C | IVR |
|---|---:|---:|---:|---:|---:|---:|
| 2026-07-28 | **820.53** | **-8.85** | +$28.6M | $3.03B | 0.867 | 83.5 |
| 2026-07-27 | 900.20 | -2.25 | +$17.9M | $2.63B | 0.991 | 79.9 |
| 2026-07-24 | 920.95 | -6.99 | **-$139.2M** | $2.00B | 1.234 | 82.5 |
| 2026-07-23 | 990.21 | +3.20 | +$103.8M | $2.15B | 1.110 | 85.6 |
| 2026-07-22 | 959.48 | -1.17 | +$16.8M | $1.64B | 1.028 | 89.5 |
| 2026-07-21 | 970.82 | **+12.17** | **+$289.9M** | $3.90B | 1.207 | 90.3 |
| 2026-07-20 | 865.46 | +1.94 | -$5.8M | $1.99B | 1.076 | 94.7 |
| 2026-07-17 | 848.95 | -0.50 | -$29.4M | $3.09B | 0.912 | 91.9 |
| 2026-07-16 | 853.20 | -5.65 | +$193.7M | $3.29B | 0.999 | 87.3 |
| 2026-07-15 | 904.28 | -8.02 | -$44.5M | $3.16B | 0.807 | 85.3 |
| 2026-07-14 | 983.12 | +4.92 | +$31.4M | $1.86B | 1.049 | 83.2 |
| 2026-07-13 | 937.00 | -4.32 | +$2.1M | $1.92B | 1.011 | 80.8 |

**This is a violent, trendless, high-amplitude chop with a downward drift.** Daily moves of
-8.85%, +12.17%, -6.99%, -8.02%, +4.92%, -5.65% are routine. Two observations phase-5 and
phase-9 must carry:
1. **Net directional premium has near-zero predictive sign here.** +$289.9M on 7/21 preceded
   a lower close 4 of the next 5 sessions; -$139.2M on 7/24 preceded a *bounce*-then-break.
   Flow sign has been a coincident, not leading, indicator for MU this month.
2. **A -8.85% day is roughly a 1.1× "normal" daily move for MU right now** (implied move
   7.90%). Any stop placed inside ~8% is noise-width. This directly constrains phase-9 sizing.

**Prior-run self-history (this skill's own record on MU):**

| Run | spot ref | conviction | confluence | Call | Status today |
|---|---:|---:|---:|---|---|
| `research/MU/2026-06-23` | $1,051.77 | 0.55 | **38** | 1–5d, no direction set | superseded |
| `research/MU/2026-06-25` | **$1,213.56** | 0.55 | **44** | "Structural long, **but only on a pullback to the $1,134 absorbed shelf** — token size at spot" | **INVALIDATED** |

- **2026-06-25 was the exact closing peak of the entire local window** (max close = 1213.56 on
  2026-06-25). The skill correctly refused to buy it: *"the entry is wrong: spot sits at the
  1211-1213 double-top after a +15.8% earnings gap on a +325%-YTD parabola."* That was right.
- **But its proposed alternative entry was also wrong.** The "$1,134 absorbed shelf" was
  breached on 2026-07-01 (close 1032.28) and never reclaimed. Its formal invalidation — *"two
  daily closes below 1052"* — triggered **2026-07-01 (1032.28) and 2026-07-02 (975.56)**.
- **Drawdown from the 06-25 peak: 1213.56 → 820.53 = -32.4%** in 23 sessions.
- Its macro invalidation named *"hawkish FOMC ~July 28-29 flips regime risk-off."* **That FOMC
  is today and tomorrow.** Phase 6 must treat this as a live, dated catalyst — not history.
- **Lesson to carry into phase 9:** on this name, in this regime, *"wait for the pullback to
  the shelf"* has now failed twice. Support levels defined by absorbed volume have not held.
  Any phase-9 long premised on a horizontal shelf must carry an explicit penalty.

Local-window extremes for reference: peak close **1213.56** (2026-06-25), trough close
**355.46** (2026-03-26), `week_52_high` **1255.00**, `week_52_low` **61.54`.

## Source

**CLI + DuckDB.** Rankings from `uw screener bullish-bearish` / `volume-vs-average` /
`iv-rank` and `uw insights deep-dive`. Exact universe percentiles, self-history percentiles,
sector aggregation, peer cut and the price path came from the DuckDB escape hatch
(`lib/duckdb-cuts.md §C`) against `Stock Screener/stock-screener-*.parquet` — tagged
`[… DUCKDB]`. Local snapshot present for the as-of date, so no fallback was needed.

**"Outside top-N" recorded:** MU is outside top-50 on `volume-vs-average` and outside top-50
on `iv-rank` — both are *information* (its 0.84× volume ratio genuinely does not qualify; its
83.48 IVR is below the ~100-IVR crowd), not tool failures.

**Self-history N caveat:** 75 available sessions spanning a non-contiguous window with a
31-day hole (2026-03-27 → 2026-04-27). Percentiles are over available sessions.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw insights deep-dive --symbol MU --date 2026-07-28 --json` | bullish=1,429,357,672; bearish=1,400,800,551; iv_rank=83.4835; implied_move=64.794 / 7.904%; iv30d=0.9604; pcr=0.8671; total_oi=3,326,277; next_earnings=2026-09-22 ← `.uw_screener.*` | whole-tape |
| ″ | DP: premium=$12.932B, shares=15,787,788, trades=31,598, avg_px=817.22 ← `.uw_dark_pool.*` | whole-tape |
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-28 --json` | MU index=7 (rank **8**); net_flow=28,557,121; close=820.53; sector=Technology ← `[.results[].ticker]\|index("MU")`, `.results[]\|select(.ticker=="MU")` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 …` | fetched, MU read via bullish list | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 …` | MU = **outside-top50** ← `index("MU") // "outside-top50"` | top-50 |
| `uw screener iv-rank --mode high --top-n 50 …` | MU = **outside-top50**; top-10 all IVR=100 | top-50 |
| DuckDB §C universe percentiles (`stock-screener-2026-07-28.parquet`) | pctile_total_prem=99.96; pctile_net_dir=99.85; pctile_iv_rank=90.00; **optvol_x=0.84 (61.65)**; stockvol_x=1.13 (73.53); n=4,632 | full universe |
| DuckDB §C self-history (75 screener files) | self_pctile_net_dir=**64.9**; total=58.1; ivr=**43.2**; optvol=**45.9**; sessions=75 | MU rows |
| DuckDB sector aggregate | Technology net=+$143.6M, avg_chg=-0.70%, 47.4% green (worst large sector) | 536 names |
| DuckDB peer cut | SNDK -14.25%, MU -8.85%, AMAT -7.82%, **NVDA +0.25%, SPY +0.24%** | 16 tickers |
| DuckDB price path | peak close 1213.56 @ 2026-06-25; first sub-1052 close 2026-07-01 (1032.28); DD -32.4% | MU rows |
| `jq` on `research/MU/2026-06-2{3,5}/decision.json` | 06-25: spot_ref=1213.56, conviction=0.55, confluence=44, invalidation "two daily closes below 1052"; 06-23: spot_ref=1051.77, confluence=38 | 2 files |

## Tool errors

- `uw insights deep-dive --symbol MU` returned
  `"yahoo_fundamentals":{"error":"yahoo quoteSummary MU: HTTP 401"}`. The Yahoo fundamentals
  leg of the composite is unauthorized. **Non-blocking** — no phase-0.5 value depends on it;
  phase-7b sources fundamentals from Finnhub/`fz` per skill rule 4. Recorded verbatim.

## DATA NOTE / CORRECTION

The §C recipe as written computes `vol_x` as option volume ÷ **`avg30_volume`**, but
`avg30_volume` in this parquet is the **stock** 30-day average volume — mixing units. Both were
computed and reported separately: **`optvol_x` = (call_volume+put_volume) ÷
(avg_30_day_call_volume + avg_30_day_put_volume) = 0.84×** (the correct
option-volume-vs-average, used for the `unusual_verdict`), and `stockvol_x` = total_volume ÷
avg30_volume = 1.13×. The `[CTX:]` block below uses the option-based ratio. No other value was
re-read; all first reads stood.

## Verdict for downstream phases

```
universe_pctile_total_prem:  99.96
universe_rank_net_dir:       8   (rank 4 among single names, ex-index/ETF)
sector_leadership:           TECHNOLOGY is CONFLICTED — #1 in net flow dollars (+$143.6M)
                             but the WORST large sector on price (-0.70% avg, 47.4% green)
                             while SPY +0.24%; MU's memory/storage/semicap sub-complex is
                             the single worst-performing group on the tape (SNDK -14.25%)
iv_rank:                     83.4835   (90th universe pctile, but only 43rd self pctile)
implied_move_pct:            7.90%     (implied_move = 64.79 pts)
self_pctile_net_dir:         64.9
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Why `BUSY_NAME_NORMAL_DAY` and not `GENUINELY_UNUSUAL`:** the rubric requires rank ≤~25 on
net-directional premium **AND** volume-vs-average ≥ 2 **AND** self_pctile_net_dir ≥ 80. MU
satisfies only the first (rank 8). Its option volume ratio is **0.84× (needs ≥2.0)** and its
self percentile is **64.9 (needs ≥80)**. Two of three fail.

→ **Per `rubrics/confluence-scoring.md`, phase-1 and phase-2 confluence is CAPPED at `+`
(not `++`) for this run.** Big dollars on MU are the base rate, not evidence.

- **Bias from this phase:** none (context only, by design)
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **$3.025B of premium is MU's normal.** 99.96th universe percentile but 45.9th self
     percentile on volume and **0.84× its own 30-day option volume**. Never cite MU's absolute
     premium as evidence of unusual interest — cite the ratio, which says the opposite.
     Net tilt is **+1.0% of gross** — directionally balanced.
  2. **The -8.85% is a memory/semicap-specific repricing, not risk-off.** SPY +0.24%,
     NVDA +0.25%, AVGO -0.60% vs SNDK -14.25%, MU -8.85%, AMAT -7.82%. Phase 6 must find the
     memory/DRAM/HBM-specific catalyst and must NOT attribute this to broad market regime.
     A live **FOMC on 2026-07-28/29** is a separate, dated overlay.
  3. **This skill's own 2026-06-25 MU run marked the exact top (1213.56) and its "buy the
     $1,134 shelf" alternative was breached within 4 sessions; formal invalidation triggered
     2026-07-01.** MU is -32.4% from that peak. Shelf-based dip-buying has failed twice on
     this name. Phase 9 must apply an explicit penalty to any long thesis resting on
     horizontal support, and must not re-use $1,052 or $1,134 as live levels.
- **Open questions:**
  - **What repriced memory today?** DRAM/HBM contract pricing, a supplier guide-down, a
    hyperscaler order cut, or an analyst capitulation? The flow data cannot say. → phase-6 / 7c.
  - **Is the +$1.429B of bullish premium dip-buying or short-vol/put-selling into crushed
    prices?** Premium sign alone cannot distinguish them, and the answer inverts the read.
    → phase-1 (aggressor side + moneyness), phase-4 (structure).
  - **Why did IV rank *fall* to only the 43rd self percentile on an -8.85% day?** If the vol
    surface refused to bid on a large down move, the market may regard this as in-distribution
    — or vol is already so elevated there is no headroom. → phase-4.
  - Earnings are dated **2026-09-22** by `uw` (≈8 weeks out, outside most horizons) — but the
    known staleness trap on `next_earnings_date` means phase-7b/7c must cross-check it.
