# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T20:14:00-04:00
**Upstream phases cited:** `phase-0-intake.md`

## Summary

**ENPH is having a quiet options day on the eve of a binary event.** Today's option
volume sits at the **16.4th percentile of the name's own 74-session history**
(`opt_vol_ratio = 0.57×` its 30-day option average) and total premium at only the
**31.5th self-percentile** — yet cross-sectionally it still ranks in the **94.2nd
universe percentile on total premium** purely because ENPH is a chronically
option-heavy name. That gap is the whole point of this phase: the big absolute
number is the name's baseline, not a signal. Direction is mildly negative and has
been persistently so — net directional premium **−$258,731**, which is the
**5.2nd universe percentile** (bottom 5% = among the day's more net-bearish names)
and the **59th most bearish of 531 Technology names**, but the *magnitude* is
trivial ($0.26M on a $4.76M premium day). Meanwhile `next_earnings_date = 2026-07-28`,
`er_time = postmarket` — **confirmed by web search as Q2'26 results after the close
tomorrow** — with a **12.25% implied move** and `iv30d = 92.2%`. The honest read:
positioning is *not* crowding in ahead of the print, and no one on the tape is
making a large directional statement. Verdict **BUSY_NAME_NORMAL_DAY**, at the
quiet end of its own normal.

## Universe ranking

`uw screener` top-50 lists, as-of 2026-07-27:

| Metric | ENPH result |
|---|---|
| `bullish-bearish --direction bullish --top-n 50` | **outside top-50** |
| `bullish-bearish --direction bearish --top-n 50` | **outside top-50** |
| `volume-vs-average --min-volume-ratio 2 --top-n 50` | **outside top-50** |
| `iv-rank --mode high --top-n 50` | **outside top-50** |
| `iv-rank --mode low --top-n 50` | **outside top-50** |

ENPH appears on **none** of the five day-leader screens. It is not a name the tape
is making a statement about today, in either direction or on volatility.

**Exact universe percentiles** (DuckDB, n=4,579 optionable names with volume):

| Percentile | Value | Read |
|---|---|---|
| `pctile_total_prem` | **94.2** | top 6% by gross premium — a *liquidity* fact, not a signal |
| `pctile_net_dir` | **5.2** | bottom 5% — net-bearish tail, but only −$0.26M |
| `pctile_bullbear_net` | **5.2** | identical (`bullish−bearish` = `net_call−net_put` here) |
| `pctile_iv_rank` | **76.8** | elevated but not extreme cross-sectionally |
| `pctile_vol_vs_avg` (recipe defn: option contracts ÷ `avg30_volume` **shares**) | **90.3** | ⚠️ see note |

> **Definitional caveat on `pctile_vol_vs_avg`.** The `lib/duckdb-cuts.md §C` recipe
> divides option *contracts* by average *share* volume — a measure of option activity
> relative to share liquidity, not of unusual option volume. Recomputed correctly as
> option volume ÷ the name's own 30-day option average:
> **`opt_vol_ratio = 0.57×`, universe percentile 52.3** (n=4,515). ENPH's option
> volume is **below** its own average and dead mid-pack cross-sectionally. The 90.3
> figure must not be cited downstream as evidence of unusual volume.

**Day's directional leaders** (`net_flow`, top-10 each side):

- **Bullish:** SPX +$782.1M · SPXW +$201.2M · **SNDK +$58.1M** · SPY +$45.3M ·
  **PLTR +$31.3M** · **MSFT +$29.4M** · GOOG +$25.0M · GOOGL +$19.6M ·
  **MU +$17.9M** · NBIS +$15.7M
- **Bearish:** TSLA −$71.3M · **WOLF −$69.9M** · **AMD −$65.7M** · GLD −$54.4M ·
  NDX −$52.3M · **NVDA −$41.9M** · AMZN −$31.6M · NDXP −$31.5M · SMH −$27.3M ·
  QQQ −$25.9M

Setting the index/ETF complex (SPX, SPXW, SPY, NDX, NDXP, SMH, QQQ, GLD) aside per
the phase pitfall note, the single-name tape is **memory/AI-led on the bull side**
(SNDK, MU, PLTR, MSFT, NBIS) and **semis-led on the bear side** (WOLF, AMD, NVDA).
ENPH — solar hardware — is adjacent to none of it. **There is no thematic tailwind
or headwind flowing through ENPH today.**

## Sector read

Sector-aggregated net directional premium, single names only (`is_index=false`):

| Sector | n | Net dir ($M) | Total prem ($M) | % names bullish |
|---|---|---|---|---|
| Communication Services | 167 | **+72.6** | 1,373.4 | 49.7 |
| **Technology** | **531** | **+21.0** | **12,518.9** | **53.3** |
| Consumer Defensive | 141 | +12.8 | 142.1 | 59.6 |
| Industrials | 459 | +9.5 | 1,254.1 | 49.7 |
| Healthcare | 631 | +7.2 | 430.3 | 45.3 |
| Real Estate | 177 | −1.1 | 31.8 | 53.7 |
| Energy | 197 | −2.7 | 121.8 | 48.2 |
| Basic Materials | 201 | −6.2 | 90.7 | 41.8 |
| Utilities | 95 | −10.0 | 157.2 | 46.3 |
| Financial Services | 426 | −19.2 | 688.3 | 47.4 |
| Consumer Cyclical | 349 | **−84.6** | 2,278.3 | 54.2 |

- ENPH's sector, **Technology, is mid-pack-to-favoured**: 2nd of 11 on net direction
  (+$21.0M) with 53.3% of names net-bullish. But the magnitude is small against
  $12.5B of gross Technology premium — a rounding-error tilt, not sector conviction.
- **ENPH sits on the bearish tail *within* a mildly-bid sector**: rank **59 of 531**
  Technology names ordered most-bearish-first (~top 11% most net-bearish).
- Per the phase heuristic this is the **yellow-flag configuration** — name soft while
  its sector is mildly bid — which **phase-6 must resolve**. Note the sector tilt is
  driven by AI/memory names ENPH shares no economic driver with; Finviz classifies
  ENPH as Technology / **Solar**, whose real comps sit closer to Utilities/Industrials.
  Treat the "Technology is bid" read as **weak evidence at best** for ENPH.

## Self-history

74 local sessions (`sessions_in_window = 74`), spanning 2026-03-13 → 2026-07-27.
**Gap-aware caveat (phase-0 §Local data):** the window contains the
2026-03-27 → 2026-04-27 hole, so these are 74 *available* sessions, not a
contiguous 74-day calendar window.

| Self-percentile (today vs own 74 sessions) | Value | Read |
|---|---|---|
| `self_pctile_optvol` | **16.4** | **bottom sixth** — a genuinely quiet option day |
| `self_pctile_total_prem` | **31.5** | below-median premium |
| `self_pctile_net_dir` | **37.0** | mildly below median; bearish lean, not extreme |
| `self_pctile_iv_rank` | **57.5** | middling *for this name* |
| `self_pctile_iv30d` | **54.8** | 92.2% IV is **normal** for ENPH, not elevated |

The IV rows matter: an `iv30d` of **0.922 (92.2%)** looks alarming in isolation and
ranks 76.8 cross-sectionally, but is only the **54.8th percentile of ENPH's own**
distribution. ENPH simply lives at ~90–100% implied vol. **Do not let phase-4 read
absolute IV as a signal** — read it against the name's own 54.8th percentile.

**Last 15 sessions** (`close`, day change, share volume, option volume, P/C ratio,
net directional premium in $k, IV rank, `iv30d`):

| Date | Close | Chg% | Share vol | Opt vol | P/C | Net dir ($k) | IVR | iv30d |
|---|---|---|---|---|---|---|---|---|
| **2026-07-27** | **38.01** | **+3.57** | 3,114,887 | **14,999** | 0.547 | **−259** | 69.8 | 0.922 |
| 2026-07-24 | 36.70 | −5.63 | 3,509,972 | 14,957 | 0.622 | −347 | 66.8 | 0.924 |
| 2026-07-23 | 38.89 | −1.74 | 3,800,484 | 22,722 | 0.947 | **+1,887** | 65.2 | 0.927 |
| 2026-07-22 | 39.58 | −0.90 | 2,360,776 | 10,828 | 0.405 | −216 | 75.0 | 0.987 |
| 2026-07-21 | 39.94 | +1.22 | 2,838,074 | 10,148 | 0.546 | +50 | 79.5 | 1.004 |
| 2026-07-20 | 39.46 | −5.08 | 3,467,516 | 18,719 | 0.633 | −518 | 82.1 | 1.017 |
| 2026-07-17 | 41.57 | +1.19 | 3,726,883 | 24,787 | 0.493 | −727 | 80.9 | 1.031 |
| 2026-07-16 | 41.08 | **−6.74** | 3,357,070 | 26,344 | **1.537** | **−4,433** | 76.5 | 1.007 |
| 2026-07-15 | 44.05 | −2.08 | 1,990,046 | 8,641 | 0.618 | −108 | 80.1 | 1.008 |
| 2026-07-14 | 44.99 | +4.47 | 2,951,370 | 20,523 | 1.174 | −1,015 | 76.6 | 0.976 |
| 2026-07-13 | 43.06 | −3.95 | 2,777,383 | 20,146 | 0.528 | −150 | 76.6 | 0.973 |
| 2026-07-10 | 44.84 | −0.11 | 2,608,457 | **42,278** | **0.130** | −85 | 77.4 | 0.980 |
| 2026-07-09 | 44.89 | +4.35 | 3,804,678 | 10,939 | 0.458 | −80 | 77.1 | 1.005 |
| 2026-07-08 | 43.02 | +0.07 | 3,476,545 | 14,841 | 0.594 | −336 | 76.5 | 1.007 |
| 2026-07-07 | 42.99 | −3.50 | 4,574,916 | 22,338 | 0.274 | +620 | 76.9 | 1.039 |

Four facts for downstream phases:

1. **Persistent one-way distribution.** Net directional premium is negative in
   **11 of the last 15 sessions**. The −$259k today is not a new development; it is
   the continuation of a three-week bleed whose single worst day was
   **2026-07-16: −$4.43M with a P/C of 1.537 on a −6.74% close.**
2. **The tape is in a downtrend.** $44.89 (2026-07-09) → $38.01 = **−15.3% in 13
   sessions**, punctuated by −6.74%, −5.08% and −5.63% days. Today's **+3.57%**
   bounce is off the 2026-07-24 low close of $36.70.
3. **Today's bounce is unconfirmed.** +3.57% came on **3.11M shares vs a 5.24M
   30-day average (0.59×)** and on *below-average option volume*. A thin-tape drift
   higher into a binary event is the weakest kind of rally; **phase-1 must not score
   today's green candle as demand.**
4. **IV is falling into the print** (`iv30d` 1.017 → 0.922, IVR 82.1 → 69.8 over
   six sessions). Vol compressing on the eve of earnings is unusual and hands
   **phase-4** a direct question: is the event genuinely underpriced, or is the
   term structure simply rolling as the front expiry decays?

### Self-history vs. prior ENPH deep dives (thesis continuity)

Two prior blueprints exist (`phase-0-intake.md §Prior versions`). Both are stale
(~9 weeks) and — critically — **the prior thesis has already resolved**:

| Run | ENPH close | Short float | IVR | Prior call |
|---|---|---|---|---|
| `research/ENPH/2026-05-19/` | **$46.83** | — | 58.2 | (no `decision.json`) |
| `research/ENPH/2026-05-22/` | **$64.03** | **32.53%** | 92.1 | confluence **35**, conviction **0.55** |
| **this run 2026-07-27** | **$38.01** | **17.94%** | **69.8** | — |

The 2026-05-22 blueprint read: *"Genuinely bullish tape … but a largely-spent short
squeeze (32.53% float short) on a deteriorating core (Q1'26 revenue −18% QoQ, GAAP
loss) … Token, trigger-gated long above $65, defined-risk only, with a symmetric
defined-risk fade below $60,"* invalidating on *"two daily closes below 60.0."*

- **That invalidation triggered, and the fade branch was right.** ENPH went
  $64.03 → $38.01 = **−40.6%**. The prior run's own scepticism (confluence 35,
  the deteriorating-core veto, the "largely-spent squeeze") was the correct read;
  its long branch was never validated.
- **The squeeze has substantially unwound**: short float **32.53% → 17.94%**
  (`phase-0-intake.md §Finviz augments`). Roughly **45% of the short base has
  covered**, and $26 of downside was delivered while they did. The single largest
  bullish mechanic in the prior thesis is now **half spent**.
- **Do not treat this run as independent confirmation of the prior one.** It is the
  third look at the same name; the honest prior is that the last two looks found
  a weak long case and the market resolved *against* the long.
- **Caveat on the prior `decision.json`**: its `as_of`, `symbol`, `direction`,
  `entry`, `stop`, `targets` and `horizon_days` fields are all **`null`** (known
  writer bug, cf. `research/_calibration` notes). Only `thesis`, `conviction`,
  `confluence_score` and `invalidation` are populated. Phase-9 of *this* run must
  make `schemas/validate_decision.py` print `OK` with those fields actually filled.

## Source

**CLI + DuckDB.** The five `uw screener` rankings and `uw insights deep-dive` are
CLI-primary; exact universe percentiles, the corrected option-volume ratio, the
sector aggregate, the 15-session series and the self-history percentiles are
DuckDB escape-hatch cuts (`lib/duckdb-cuts.md §A/§C`) over
`~/Documents/Stocks/Stock Screener/stock-screener-*.parquet`, tagged
`[CTX:… DUCKDB]` downstream.

"Outside top-N" recorded on **all five** screener metrics — informational, not an
error. The earnings date was cross-checked against the web because
`next_earnings_date` is a known-stale field (see Tool errors).

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-27 --json` | ENPH absent ← `[.results[].ticker]\|index("ENPH")` → `outside_top50`; leaders ← `.results[:10]` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-07-27 --json` | ENPH absent ← same path; TSLA `net_flow=-71289458` ← `.results[0].net_flow` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-07-27 --json` | ENPH absent ← same path | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-07-27 --json` | ENPH absent ← same path | top-50 |
| `uw screener iv-rank --mode low --top-n 50 --date 2026-07-27 --json` | ENPH absent ← same path | top-50 |
| `uw insights deep-dive --symbol ENPH --date 2026-07-27 --json` | `iv_rank=69.8119`, `iv30d=0.922018992271469`, `implied_move=4.65215194552611`, `implied_move_perc=0.1224572767972127`, `put_call_ratio=0.5474053440627257`, `total_open_interest=355935`, `bullish_premium=1843847`, `bearish_premium=2102578`, `call_premium=2171125`, `put_premium=2593624`, `call_volume=9693`, `put_volume=5306`, `next_earnings_date=2026-07-28T00:00:00Z` ← `.uw_screener.*`; **`net_flow` derived = 1843847−2102578 = −258731** (field absent by design, `lib/uw-json-paths.md`) | 1 |
| DuckDB `§C` universe percentiles over `stock-screener-2026-07-27.parquet` | `pctile_total_prem=94.2`, `pctile_net_dir=5.2`, `pctile_bullbear_net=5.2`, `pctile_iv_rank=76.8`, `pctile_vol_vs_avg=90.3`, `universe_n=4579` | 4,579 |
| DuckDB corrected option-vol ratio (same parquet) | `opt_vol_ratio=0.57`, `pctile=52.3`, `n=4515` ← `(call_volume+put_volume)/(avg_30_day_call_volume+avg_30_day_put_volume)` | 4,515 |
| DuckDB `§C` self-history over 74 `stock-screener-*.parquet` | `self_pctile_net_dir=37.0`, `self_pctile_total_prem=31.5`, `self_pctile_iv_rank=57.5`, `self_pctile_iv30d=54.8`, `self_pctile_optvol=16.4`, `sessions_in_window=74` | 74 |
| DuckDB `§A` sector aggregate (same parquet) | Technology `net_dir=+$21.0M`, `n=531`, `pct_names_bullish=53.3`; Comm Svcs `+$72.6M`; Cons Cyclical `−$84.6M` | 11 sectors / 3,374 names |
| DuckDB ENPH rank within Technology | `rk_bearish=59` of `n=531` ← `ROW_NUMBER() OVER(ORDER BY bullish_premium−bearish_premium ASC)` | 531 |
| DuckDB raw ENPH row | `close=38.01`, `prev_close=36.70` (**+3.57%**), `total_volume=3114887`, `avg30_volume=5244294.95` (**0.59×**), `week_52_high=73.74`, `week_52_low=25.775`, `marketcap=4836994674`, `er_time=postmarket` | 1 |
| DuckDB 15-session series | table above ← `ORDER BY date DESC LIMIT 15` | 15 |
| DuckDB prior-run closes | 2026-05-19 `close=46.825`, 2026-05-22 `close=64.03` (`iv_rank=92.0614`) | 2 |
| `jq` on `research/ENPH/2026-05-22/decision.json` | `confluence_score=35`, `conviction=0.55`, `invalidation.price="two daily closes below 60.0…"`; `as_of`/`symbol`/`direction`/`entry`/`stop`/`targets`/`horizon_days` all **null** | 1 |
| WebSearch "Enphase Q2 2026 earnings date" | Q2'26 results **2026-07-28, after market close**, call 4:30pm ET — confirms `next_earnings_date` | — |

## Tool errors

No command errored; all exited 0 and round-tripped through `jq` or DuckDB. Two
data-quality items carried forward rather than errors:

1. **`next_earnings_date` verified, not assumed.** Memory flags this UW field as
   sometimes stale. Cross-checked against StockTitan / Nasdaq / TradingView: ENPH
   Q2 2026 results are released **2026-07-28 after the close**, matching
   `er_time=postmarket`. **The field is correct for this run.**
2. **`pctile_vol_vs_avg=90.3` is definitionally misleading** (recipe divides option
   contracts by share volume). Superseded by the corrected `opt_vol_ratio=0.57×`
   / percentile 52.3. Recorded here so no downstream phase cites 90.3 as unusual
   option volume.

## DATA NOTE / CORRECTION

- **`opt_vol_ratio` — recomputation, not a correction of a written value.** The
  `§C` recipe's `vol_x` (90.3rd percentile) was recognised as an option-contracts ÷
  share-volume ratio *before* any verdict was written, and the correct
  option-vs-own-option-average ratio was computed alongside it
  (`0.57×`, 52.3rd pctile). Both are reported above; only the corrected figure
  feeds the `[CTX:]` block and the verdict. No value was published and retracted.
- Every other number stood on first read. The only repeated query was the ENPH raw
  screener row, re-run to surface `er_time` and 52-week levels; the overlapping
  fields returned identical values.

## Verdict for downstream phases

- **Bias from this phase:** **none** — phase 0.5 sets context only, per the phase spec.
- **Conviction:** n/a (context phase)

```
[CTX:]
universe_pctile_total_prem:  94.2
universe_rank_net_dir:       outside top-50 both directions (universe pctile 5.2 = net-bearish tail; 59th of 531 Technology names)
sector_leadership:           Technology mid-pack/mildly-bid (+$21.0M net dir, 2nd of 11, 53.3% names bullish) — but ENPH shares no driver with the AI/memory names carrying it; treat as WEAK
iv_rank:                     69.81
implied_move_pct:            12.25
self_pctile_net_dir:         37.0
unusual_verdict:             BUSY_NAME_NORMAL_DAY
```

**Binding consequence of `BUSY_NAME_NORMAL_DAY`:** per
`rubrics/confluence-scoring.md`, **phases 1–2 confluence is capped at `+`, never
`++`.** Nothing on today's tape earns a double-plus. Phase-10 must enforce this cap.

- **Three things later phases should remember:**
  1. **ENPH's big numbers are its baseline.** 94.2nd universe percentile on premium
     but **16.4th self-percentile on option volume** and **31.5th on premium** — a
     below-average day for the name. Likewise `iv30d=92.2%` is only the **54.8th
     self-percentile**: ENPH always trades ~90–100% vol. Every magnitude downstream
     must be judged against the name's own distribution, not the universe's.
  2. **A confirmed binary lands tomorrow after the close (2026-07-28, postmarket),
     with a 12.25% implied move (±$4.65 → roughly $33.36–$42.66).** This dominates
     every horizon shorter than ~2 weeks. Phase-4 owns the vol-vs-event question
     (note IV is *falling* into the print: `iv30d` 1.017 → 0.922 over six sessions);
     phase-9 must size for a one-day gap that dwarfs any technical stop, and cannot
     write a swing plan that pretends the event is avoidable.
  3. **The distribution is persistent and the prior thesis already resolved against
     the long.** Net directional premium negative in **11 of 15 sessions**; price
     **−15.3% in 13 sessions** to $38.01; today's **+3.57%** bounce came on **0.59×**
     average share volume and below-average option volume — treat it as unconfirmed.
     Against that, ENPH is **−48.5% from its 52-week high ($73.74)** yet still
     **+47.5% off the 52-week low ($25.78)**, and the prior blueprint's fade-below-$60
     branch delivered **−40.6%** while short float fell **32.53% → 17.94%** (about
     45% of the short base covered). Both the squeeze fuel and the easy downside
     are **partly spent** — phases 7c and 8b must resist re-running either stale story.
- **Open questions:**
  - Why is option volume at the **16th self-percentile** on earnings eve? Genuine
    disinterest, or has positioning already been established in prior sessions
    (i.e. sitting in OI rather than today's tape)? → **phase-1 vs phase-3**
  - Is the falling `iv30d` into a confirmed binary a real underpricing of the event,
    or front-expiry roll mechanics? → **phase-4** (`term-structure`, `vrp`)
  - Technology is mildly bid while ENPH sits in its bearish tail — does the solar /
    clean-energy complex explain the divergence, or is this name-specific? → **phase-6**
  - With ~45% of the short base already covered at **17.94%** float short, is the
    remaining short a squeeze risk into a beat or simply a correctly-positioned
    bear? → **phase-7c**
