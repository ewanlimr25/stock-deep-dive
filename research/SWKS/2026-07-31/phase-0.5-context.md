# Phase 0.5 — Cross-Sectional & Self-History Context

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`

## Summary

SWKS's 2026-07-31 options tape is **not unusual** — not cross-sectionally, and not
for the name. Total option premium was **$877,883** on **5,464 contracts**, which
is **1.00×** SWKS's own 30-day average option volume and sits at only the **44.2nd
percentile of the name's own 78-session history**. It ranks **565th of 4,499**
optionable names on net-directional premium and **673rd of 4,499** on total
premium — far outside the `uw screener` top-50, whose net-bullish cutoff was
**$1,774,639** (TIGO) versus SWKS's **+$43,882**. The one genuinely extreme
reading is the **put/call volume ratio of 4.06**, which is the **97.4th percentile
of SWKS's own history** and by far the highest in its semiconductor peer group.
The dominant context, however, is event-driven, not flow-driven: **SWKS reported
earnings 2026-07-28 postmarket and fell −5.40% on 2026-07-29** (64.68 → 61.19 on
15.3M shares, 2.96× its 30-day average share volume), and **Apple — its largest
customer — reported 2026-07-30 postmarket and fell −7.35% on the as-of date
itself** (333.43 → 308.91). This is a **post-earnings, post-customer-shock**
read, with IV already crushed from an IV-rank of 91.2 pre-print to 52.9. This
phase sets **context only, no directional bias**.

## Key signals

- Net-directional premium **+$43,882** — rank **565/4,499**, outside `uw screener`
  top-50 both directions (bullish cutoff $1.77M, bearish cutoff −$12.4M) `[CTX:universe_rank]`
- Option volume **5,464 vs 30d avg 5,478 = 1.00×** — the flat definition of a
  normal day; `uw screener volume-vs-average --min-volume-ratio 2` top-50 cutoff
  was **17.7×** (CLGN), so SWKS is nowhere near it `[CTX:vol_vs_avg]`
- **Put/call volume ratio 4.06** (put_volume 4,384 vs call_volume 1,080) —
  **97.4th self-percentile**, highest of 13 semis screened `[CTX:pcr DUCKDB]`
- **Earnings already happened: 2026-07-28 postmarket**, −5.40% next-day reaction.
  `uw insights deep-dive` reports `next_earnings_date = 2026-10-27` — this is
  **correct, not stale** (verified against the field's own history) `[CTX:earnings]`
- **AAPL −7.35% on the as-of date** after its 2026-07-30 postmarket print, with
  **−$141.1M net bearish premium** on $1.57B total — the single largest bearish
  name on the tape `[CTX:customer_shock]`
- IV rank **52.9** (mid-pack, outside both iv-rank top-50s) but only the **29.9th
  percentile of SWKS's own history** — vol is *cheap for this name* post-crush `[CTX:iv]`

## Detailed findings

### Universe ranking (`uw screener` + DuckDB exact percentiles)

| Metric | SWKS value | Universe rank / percentile | Top-50 cutoff |
|---|---|---|---|
| Net bullish−bearish premium | **+$43,882** | **565 / 4,499** · 87.5th pctile | $1,774,639 (TIGO) — **outside top-50** |
| Net call−put premium (`net_call_premium − net_put_premium`) | **+$43,882** | 87.5th pctile | — |
| Total option premium | **$877,883** | **673 / 4,499** · 85.1th pctile | — |
| Option volume ÷ own 30d option avg | **1.00×** (5,464 / 5,478) | 78.8th pctile of 5,864 | 17.70× (CLGN) — **outside top-50** |
| IV rank | **52.9** | 61.6th pctile | high-list floor 97.98 (ARDT); low-list ceiling 0 (HTT) — **outside both** |

> **Percentile-vs-rank caveat.** The 85–88th universe percentiles look strong but
> are a long-tail artifact: 4,499 names carry option volume and the vast majority
> trade a few hundred dollars of premium. The *rank* (565th / 673rd) and the
> top-50 cutoffs are the honest cross-sectional read. **SWKS is not a leader on
> any flow metric today.**

**Day's directional leaders** (`uw screener bullish-bearish`, `.results[].net_flow`):

- Bullish: NDX +$122.4M · AMZN +$89.6M · NVDA +$60.5M · GOOG +$40.8M · MSTR
  +$37.0M · QQQ +$31.8M · GOOGL +$28.3M · SPY +$27.5M · SNDK +$20.9M · SOXX +$19.2M
- Bearish: SPX −$886.7M · **MU −$158.4M** · **AAPL −$141.1M** · SPXW −$138.8M ·
  EWY −$23.8M · RDDT −$22.9M · **AMD −$20.9M** · **SOXL −$20.7M** · TSLA −$20.4M ·
  MSFT −$12.4M

### Sector read (`uw options-flow sector-flow`)

Technology **leads the tape outright**: net call−put premium **+$2,781,021,293**
(call $8.11B vs put $5.33B), #1 of 11 sectors. Ranking:

| Sector | Net (call−put) premium |
|---|---|
| **Technology** | **+$2,781,021,293** |
| Consumer Cyclical | +$1,841,619,593 |
| Communication Services | +$656,316,523 |
| Financial Services | +$499,594,693 |
| Energy | +$78,135,697 |
| Healthcare | +$72,300,875 |
| Consumer Defensive | +$39,406,223 |
| Basic Materials | +$5,019,500 |
| Real Estate | −$1,016,954 |
| Utilities | −$5,546,758 |
| Industrials | −$171,008,916 |

**But the sector headline is misleading for SWKS.** Inside semis the tape is
sharply **bifurcated** — AI/compute bid, handset/analog/RF sold:

| Ticker | Close | Day % | Net bull−bear prem | Total prem | P/C | IV rank |
|---|---|---|---|---|---|---|
| SOXX | 504.89 | +0.07% | +$19,196,805 | $78.1M | 2.20 | 79.5 |
| SMH | 540.53 | +0.30% | +$8,346,121 | $309.3M | 2.91 | 78.1 |
| MPWR | 1426.03 | **+8.35%** | +$3,987,431 | $27.6M | 0.91 | 69.7 |
| AVGO | 389.28 | +0.37% | +$2,667,103 | $121.3M | 0.91 | 51.5 |
| ON | 81.61 | −2.54% | +$1,757,176 | $5.4M | 1.69 | 79.0 |
| TXN | 275.74 | −1.08% | +$891,314 | $9.8M | 0.45 | 57.8 |
| ADI | 367.41 | +0.20% | +$217,987 | $10.9M | 0.94 | 87.4 |
| NXPI | 229.16 | **−6.53%** | +$143,381 | $4.7M | 1.10 | 62.4 |
| **SWKS** | **62.28** | **−0.32%** | **+$43,882** | **$0.88M** | **4.06** | **52.9** |
| QRVO | 90.57 | −0.19% | −$2,598 | $0.02M | 0.34 | 61.1 |
| MCHP | 74.29 | −0.96% | −$3,194,601 | $32.0M | 0.13 | 84.9 |
| QCOM | 147.61 | **−2.63%** | −$4,243,280 | $47.4M | 0.92 | 45.7 |
| **AAPL** | **308.91** | **−7.35%** | **−$141,081,266** | **$1,571.8M** | **0.67** | **52.7** |

**Read:** SWKS's *sector* (Technology) is leading, but SWKS's *industry cohort*
(handset RF / analog: QCOM, NXPI, MCHP, QRVO, SWKS) is the part being sold, and
its single largest end-customer took a −7.35% earnings hit on the as-of date.
Per the phase-0.5 heuristics this is the **yellow-flag configuration** — sector
in favour, sub-industry and customer out of favour — and **phase 6 must resolve
it**. Note also that SWKS's absolute premium ($0.88M) is an order of magnitude
below every liquid peer except QRVO; this is a **thinly-traded options name**.

### Event context — this is a post-earnings read (critical)

`next_earnings_date` in the screener parquet **rolled from `2026-07-28
postmarket` to `2026-10-27 unknown` between the 2026-07-28 and 2026-07-29
snapshots**, which independently confirms the print landed on the evening of
2026-07-28. The `uw insights deep-dive` value of `2026-10-27` is therefore
**accurate, not the known-stale-field trap** — but only because the event is
behind us, not ahead.

SWKS tape, last 10 sessions (screener parquet, DuckDB):

| Date | Close | Day % | Stock vol | Call vol | Put vol | P/C | Total prem | Net bull−bear | IV rank | iv30d |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | 59.80 | +0.76% | 3.15M | 883 | 893 | 1.01 | $0.94M | −$505,597 | 100.0 | 0.728 |
| 2026-07-21 | 62.95 | +5.27% | 3.96M | 1,309 | 716 | 0.55 | $0.67M | −$96,068 | 100.0 | 0.756 |
| 2026-07-22 | 63.16 | +0.33% | 2.53M | 873 | 461 | 0.53 | $0.48M | +$129,930 | 99.1 | 0.742 |
| 2026-07-23 | 60.47 | −4.26% | 4.62M | **21,515** | 244 | **0.01** | $0.83M | −$33,902 | 100.0 | 0.751 |
| 2026-07-24 | 60.21 | −0.43% | 3.26M | 2,078 | 1,456 | 0.70 | $1.61M | +$493,813 | 96.5 | 0.748 |
| 2026-07-27 | 63.44 | +5.36% | 4.25M | 788 | 322 | 0.41 | $0.42M | −$29,309 | 88.7 | 0.733 |
| **2026-07-28** | **64.68** | +1.95% | 6.17M | 2,235 | 1,402 | 0.63 | $1.15M | +$35,514 | **91.2** | 0.741 |
| **2026-07-29** | **61.19** | **−5.40%** | **15.33M** | 8,387 | 5,513 | 0.66 | **$14.92M** | **−$4,809,634** | 62.6 | 0.574 |
| 2026-07-30 | 62.48 | +2.11% | 6.76M | 427 | 466 | 1.09 | $0.27M | −$67,463 | 56.8 | 0.585 |
| **2026-07-31** | **62.28** | **−0.32%** | 4.99M | 1,080 | **4,384** | **4.06** | $0.88M | **+$43,882** | **52.9** | 0.559 |

Three structural facts fall out:

1. **Vol crush is done and then some.** `iv30d` fell 0.741 → 0.559 (−24.6%) and
   IV rank 91.2 → 52.9 across the event. Against SWKS's *own* history the current
   IV rank sits at the **29.9th percentile** — SWKS options are cheaper than they
   have been on ~70% of the available sessions.
2. **The earnings day itself was decisively bearish** (2026-07-29: net bull−bear
   **−$4.81M** on $14.92M premium, the only session in the window above $2M) — and
   that bearish premium was ~110× the +$43,882 recorded on the as-of date. The
   as-of day's marginal positive is **noise inside a bearish event print**.
3. **The as-of day's put skew is a genuine outlier for the name** (P/C 4.06 vs a
   window that otherwise runs 0.01–1.09), even though the dollars behind it are
   small. Phase 1 must determine whether those 4,384 puts are opening hedges,
   closing longs, or sold premium — the phase-0 finding that
   `uw options-flow unusual-volume` returned **empty** argues these are **not**
   fresh vol-far-exceeds-OI positions.

Price location: close **62.28** against a 52-week range of **51.93 – 90.90** —
**31.5% below the 52w high, 19.9% above the 52w low**, i.e. lower-middle of the
annual range. Market cap **$9.40B**, issue type Common Stock, sector Technology.

### Self-history (DuckDB, `lib/duckdb-cuts.md §C`)

`sessions_in_window = 78` (**not** 78 contiguous calendar sessions — see the gap
below).

| Self-history metric | Percentile (of 78 sessions) |
|---|---|
| Net-directional premium (`net_call_premium − net_put_premium`) | **66.2** |
| Net bullish−bearish premium | **68.8** |
| **Total option premium** | **44.2** |
| Option volume (call+put contracts) | **74.0** |
| **Put/call ratio** | **97.4** |
| **IV rank** | **29.9** |

The shape is unambiguous: **ordinary dollars, ordinary-to-slightly-heavy contract
count, extreme put skew, cheap vol.**

> **Gap caveat (`lib/duckdb-cuts.md § gap`).** The 78 sessions span 2026-03-13 →
> 2026-07-31 but are **non-contiguous** — a ~4-week hole runs 2026-03-30 →
> 2026-04-24 (see `phase-0-intake.md §Local data`). These percentiles are over 78
> *available* sessions, not a 78-session calendar window, and no return path may
> be computed across the hole. Phase 5 must scope continuous work to the
> 2026-04-27 → 2026-07-31 block (67 sessions).

## Source

**CLI + DuckDB.** `uw screener bullish-bearish` (both directions),
`uw screener volume-vs-average`, `uw screener iv-rank` (high and low),
`uw insights deep-dive`, and `uw options-flow sector-flow` supplied the
cross-sectional ranks; the local parquet
`~/Documents/Stocks/Stock Screener/stock-screener-2026-07-31.parquet` (present)
supplied the exact universe percentiles, the exact ranks, the peer cross-section,
the 10-session tape, and the 78-session self-history.

**Metrics on which SWKS is "outside top-N":** net bullish premium (outside
top-50), net bearish premium (outside top-50), volume-vs-average ≥2× (outside
top-50), iv-rank high (outside top-50), iv-rank low (outside top-50). Recorded as
information, not error.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol SWKS --date 2026-07-31 --json` | iv_rank=52.8977, put_call_ratio=4.059259, implied_move=5.674921, implied_move_perc=0.0909807, iv30d=0.559032, next_earnings_date=2026-10-27, total_open_interest=118470, bullish_premium=376945, bearish_premium=333063, call_premium=380703, put_premium=497180 ← `.uw_screener.*`; net derived = `bullish_premium − bearish_premium` = **43882** (no `net_flow` field in this block) | whole |
| `uw screener bullish-bearish --direction bullish --top-n 50 --date 2026-07-31 --json` | SWKS **absent** ← `[.results[]\|select(.ticker=="SWKS")]\|.[0]//null`; cutoff TIGO 1774639 ← `.results[-1]`; leaders ← `.results[:10][].net_flow` | top-50 |
| `uw screener bullish-bearish --direction bearish --top-n 50 --date 2026-07-31 --json` | SWKS **absent**; MU −158417849, AAPL −141081266 ← `.results[].net_flow` | top-50 |
| `uw screener volume-vs-average --min-volume-ratio 2 --top-n 50 --date 2026-07-31 --json` | SWKS **absent**; cutoff CLGN 17.7018 ← `.results[-1].volume_ratio` | top-50 |
| `uw screener iv-rank --mode high --top-n 50 --date 2026-07-31 --json` | SWKS **absent**; floor ARDT 97.9779 ← `.results[-1].iv_rank` | top-50 |
| `uw screener iv-rank --mode low --top-n 50 --date 2026-07-31 --json` | SWKS **absent**; ceiling HTT 0 ← `.results[-1].iv_rank` | top-50 |
| `uw options-flow sector-flow --date 2026-07-31 --json` | Technology net_flow=2781021293 (rank 1/11) ← `.[].net_flow`; Industrials −171008916 | all 11 |
| DuckDB `stock-screener-2026-07-31.parquet` — `PERCENT_RANK()` over universe | pctile_total_prem=85.1, pctile_net_dir=87.5, pctile_net_bb=87.5, pctile_iv_rank=61.6, pctile_vol_vs_avg=76.6, universe_n=4499 `[CTX:universe_pctile DUCKDB]` | 4,499 |
| DuckDB `RANK() OVER(ORDER BY … DESC)` | rank_net_bb=565, rank_total_prem=673 of 4,499 `[CTX:universe_rank DUCKDB]` | 4,499 |
| DuckDB option-volume-vs-own-30d-option-avg | ov=5464, ov_avg30=5478, opt_vol_x=**1.00**, pctile=78.8 of 5,864 `[CTX:vol_vs_avg DUCKDB]` | 5,864 |
| DuckDB self-history over 78 screener parquets | self_pctile_net_dir=66.2, net_bb=68.8, total=44.2, optvol=74.0, pcr=**97.4**, ivrank=**29.9**, sessions_in_window=78 `[CTX:self_pctile DUCKDB]` | 78 |
| DuckDB SWKS raw row + 10-session tape | close=62.28, prev_close=62.48, total_volume=4991143, avg30_volume=5957508, week_52_high=90.90, week_52_low=51.93, marketcap=9401539419; 2026-07-29 close=61.19 (−5.40%), vol=15333028, tot_prem=$14.92M | 10 |
| DuckDB peer cross-section (13 semis + AAPL) | AAPL −7.35% / net −141081266; QCOM −2.63%; NXPI −6.53%; MPWR +8.35%; SOXX +19196805 | 14 |
| DuckDB `next_earnings_date` drift, last 12 SWKS snapshots | rolls `2026-07-28 postmarket` → `2026-10-27 unknown` between 07-28 and 07-29 snapshots ⇒ **print was 2026-07-28 PM** | 12 |
| DuckDB AAPL/QRVO earnings drift | AAPL `2026-07-30 postmarket` → `2026-10-29` after 07-30; QRVO `2026-07-28 postmarket` → `2026-10-27` after 07-28 | 10 |

## Tool errors

- `uw options-flow sector-flow` — first `jq` template used `.call_premium` /
  `.put_premium`, which are **not** fields on this response (they returned `null`
  and the derived net collapsed to `0` for every sector). Re-read with the actual
  field names `.total_premium_call` / `.total_premium_put` / `.net_flow`, which
  parse correctly. Recorded per the phantom-field discipline; no value from the
  null read was carried forward.
- DuckDB: `ROUND(close,2) close` → `Parser Error: syntax error at or near "close"`
  (`close` is reserved). Re-run with alias `px`. No data impact.

## DATA NOTE / CORRECTION

1. **`fz` timing caveat from phase-0 is RESOLVED and downgraded.** Phase-0
   recorded `fz` prices as "live 2026-08-02, advisory only". In fact **2026-08-02
   is a Sunday**, so the last close is Friday **2026-07-31** — and `fz screen`'s
   Price **62.28** / Change **−0.32%** reconcile **exactly** with the screener
   parquet's `close=62.28` / `prev_close=62.48` for the as-of date. The `fz`
   price data is therefore as-of-consistent on this run. The *other* phase-0 `fz`
   findings stand unchanged: `Shs Float` and `Short Float` are still unavailable
   (14/84 fields), so phase-2/3 float normalization and the phase-7c SI gate
   still need a fallback source.
2. **`next_earnings_date` verified, not assumed.** The stale-field risk flagged in
   the project's data-source notes was checked directly by reading the field's own
   12-snapshot history rather than trusting the single as-of value. It rolled on
   the correct date, so `2026-10-27` is a real forward date and there is **no
   earnings event inside a normal 1–8 week trade horizon**.
3. `net_flow` was **derived** (`bullish_premium − bearish_premium`) for the
   `insights deep-dive` block, which has no `net_flow` field. Cross-checked
   against the independent parquet derivation `net_call_premium − net_put_premium`
   — both give **+$43,882** exactly.

## Verdict for downstream phases

```
universe_pctile_total_prem:  85.1        # rank 673/4499 — long-tail inflated; treat rank as truth
universe_rank_net_dir:       565 of 4499 (outside top-50 both directions)
sector_leadership:           Technology is LEADING the tape (+$2.78B net, 1st of 11),
                             BUT SWKS's handset-RF/analog sub-cohort is LAGGING
                             (QCOM −2.63%, NXPI −6.53%, MCHP net −$3.19M) and its
                             largest customer AAPL fell −7.35% on the as-of date
                             with −$141.1M net bearish premium — YELLOW FLAG for phase 6
iv_rank:                     52.9        # 61.6th universe pctile, but only 29.9th SELF pctile
implied_move_pct:            9.10%       # implied_move = $5.67 on a $62.28 close
self_pctile_net_dir:         66.2        # (net bull−bear: 68.8; total premium: 44.2)
unusual_verdict:             QUIET
```

**Why QUIET and not BUSY_NAME_NORMAL_DAY:** the rubric's
`BUSY_NAME_NORMAL_DAY` describes *high absolute premium with mid-pack rank*. SWKS
has neither — **$877,883** of total premium and a **$43,882** net is small in
absolute terms for an S&P 500 constituent, its option volume is exactly **1.00×**
its own average, and total premium sits **below its own median** (44.2nd
percentile). Tradeability of any options-flow signal here is **low**: the largest
single print on the day was **$173,030** (`phase-0-intake.md §Ticker sanity`).
Downstream conviction should stay low regardless of how clean an individual print
looks, and the phases-1–2 confluence cap that `BUSY_NAME_NORMAL_DAY` would impose
applies *a fortiori*.

- **Bias from this phase:** **none** — phase 0.5 sets context only, by design.
- **Conviction:** n/a
- **Three things later phases should remember:**
  1. **The flow is not the story; the event is.** 2026-07-31 is **T+2 after a
     −5.40% earnings reaction** (print 2026-07-28 PM) and **T+1 after Apple's own
     −7.35% earnings drop**. The as-of session's +$43,882 net is ~1/110th of the
     −$4.81M net bearish premium printed on the reaction day itself. Any phase
     that reads the as-of day in isolation will over-read it.
  2. **Vol is cheap for this name (29.9th self-percentile, iv30d 0.559, IV rank
     52.9) and the next earnings catalyst is 2026-10-27 — verified, not stale.**
     That combination favours *owning* optionality over selling it, and means a
     1–8 week horizon carries **no scheduled earnings risk**. The 9.10% implied
     move feeds the phase-9 expected-move band.
  3. **P/C 4.06 is the one real outlier (97.4th self-percentile)** but rests on
     small dollars, and `unusual-volume` was **empty** — so these puts are most
     likely **not** new positions. Phase 1 must classify them (opening hedge vs
     closing vs sold premium) before anyone treats the skew as bearish.
- **Open questions:**
  - Does the AAPL −7.35% shock transmit to SWKS, or has SWKS already discounted it
    via its own −5.40% print two days earlier? Its −0.32% on the day AAPL fell
    −7.35% is either **relative strength** or **complacency** — phases 2, 6 and 8
    must adjudicate.
  - With `unusual-volume` empty and OI barely moving (call OI 75,298 → 75,306;
    put OI 42,612 → 43,164), is there **any** new institutional positioning at
    all, or is the as-of tape entirely residual post-event churn? Phase 3 owns this.
  - Is the post-event de-rate (−31.5% from the 52w high of 90.90) a broken story
    or a washed-out one? Phase 7b's quality veto is the arbiter.
