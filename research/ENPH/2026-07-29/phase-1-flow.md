# Phase 1 — Options Flow

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T01:14:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`

## Summary

**Bearish, confirmed on the whole tape, and economically trivial — but the price action
is the real story.** The whole-tape aggregate is mildly bearish (`net_flow` = −$479,813)
and the ranked top-N adds nothing to that: the top-25 prints total $1,149,093, only
**21.9% of the day's $5,258,451 premium**, and their initiator-signed delta notional is
**−$1.64M against a $4.80B market cap — 0.034%**. What *does* survive scrutiny is the
whole-tape ask/bid decomposition, which the volume P/C ratio actively hides: **puts were
aggressively bought at 1.569× the rate they were sold while calls printed dead-even at
1.000**, giving net aggressive direction of **−2,622 contracts** and marking the most
put-bid session of the trailing eight [FLOW:ask_bid_split DUCKDB].

**The finding that reframes the entire run:** ENPH **gapped up +9.03% to 39.60** on the
Q2 print, then sold off **−11.44% from that high to close at 35.07 — $0.11 off the
session low of 34.96** — on 1.69× average volume. `phase-0.5-context.md` recorded the
close-to-close move as −3.44% and called the event "a whimper"; at intraday resolution
that is wrong. The realized **range was 13.2% of prior close against a pre-print implied
±12.25%** — the options market priced the movement almost exactly right, and the tape
round-tripped it. A full gap engulfment closing on the low is one of the most bearish
daily structures available, and it happened on the highest-volume session of the window.

Persistence is maximal but directionless: ENPH appears in top sweep activity **5 of 5
sessions** (`consistency_score` 1.0) on $7,400,862 of 5-day sweep premium, yet
`dominant_direction` is **"mixed"** — up from $1,335,255 and *bearish* at the 07-27 run.
ENPH is absent from both smart-money-flow leaderboards and from the sweep-ratio top-15.
Per `phase-0.5-context.md`'s BUSY_NAME_NORMAL_DAY verdict, this phase's confluence is
**capped at `+`**.

## Key signals

- **Whole-tape ask/bid is the clean read:** `put_volume_ask_side` 7,236 vs
  `put_volume_bid_side` 4,613 → **1.569×** puts bought; `call_volume_ask_side` 8,285 vs
  `call_volume_bid_side` 8,284 → **1.000×** calls flat. Net aggressive direction
  **−2,622 contracts** [FLOW:ask_bid_split DUCKDB]
- **Volume P/C 0.7259 is a trap.** Raw volume looks call-heavy (18,150 calls vs 13,176
  puts) yet `net_call_premium` is **−$223,790** (calls net *sold*) and `net_put_premium`
  is **+$256,023** (puts net *bought*) [FLOW:insights_deep_dive]
- **Intraday: high 39.60 (+9.03% vs prev close 36.32), low 34.96, close 35.07 —
  −11.44% from high, closing 0.31% off the low** on 8,670,939 shares (1.69× the 30-day
  average 5,127,858) [FLOW:ohlc DUCKDB]
- **Largest single print of the day is a bought ATM put:** 2026-10-16 P35, **ask side**,
  $196,240, 446 contracts @ $4.40, `delta` −0.368, struck at `underlying_price` 36.69
  (11:15 ET, pre-FOMC) [FLOW:top_premium_trades]
- **Upside is being supplied, not bought:** call-side bid prints total $308,168 across 8
  rows (2026-09-18 C40, 2026-12-18 C50, 2027-01-15 C55, 2028-01-21 C75) vs only $95,048
  of call-side ask prints [FLOW:top_premium_trades]
- **Sweep persistence 5/5 sessions, `consistency_score` 1.0, but `dominant_direction`
  "mixed"** on `total_sweep_premium` $7,400,862 — maximal attention, zero consensus
  [FLOW:sweep_persistence]
- **The one genuine bullish initiation:** 2026-08-07 C37, `vol_oi_ratio` **14.89**
  (1,206 vol on 81 OI), $218,770, 99 trades — of which the ask-side sweep captures
  1,157 contracts / $209,361, i.e. **~96% aggressively bought** [FLOW:unusual_volume +
  FLOW:sweeps]
- ENPH absent from `smart-money-flow` **both** directions and from `sweep-ratio` top-15 —
  no smart-money flow detected on this date [FLOW:smart_money_flow]

## Detailed findings

### A — Whole-tape aggregate (read the top-N against this)

`uw insights deep-dive --symbol ENPH --date 2026-07-29` → `.uw_screener`:

| Field | Value |
|---|---|
| `call_premium` | $2,888,189 |
| `put_premium` | $2,370,262 |
| **Total premium** | **$5,258,451** |
| `bullish_premium` | $2,153,830 |
| `bearish_premium` | $2,633,643 |
| **`net_flow` (derived `bullish − bearish`)** | **−$479,813** |
| `call_volume` | 18,150 |
| `put_volume` | 13,176 |
| `put_call_ratio` | 0.7259 |
| `net_call_premium` | **−$223,790** |
| `net_put_premium` | **+$256,023** |
| `iv_rank` | 47.05 |
| `implied_move` / `implied_move_perc` | 1.962 / **5.58%** |
| `total_open_interest` | 381,215 |

`net_flow` was **derived** — the `uw_screener` block carries no `net_flow` key
(`lib/uw-json-paths.md` phantom-field trap). The derivation was independently reproduced
in DuckDB as `net_call_premium − net_put_premium` = −223,790 − 256,023 = **−$479,813**,
matching `bullish_premium − bearish_premium` exactly.

**Two aggregate reads point the same way and one is deceptive:**

1. **`put_call_ratio` 0.7259 is call-heavy and means nothing here.** Volume counts
   contracts without regard to who initiated. The premium decomposition inverts the read:
   `net_call_premium` is **negative** (−$223,790 — the market was a net *seller* of calls
   in premium terms) while `net_put_premium` is **positive** (+$256,023 — a net *buyer* of
   puts). Any downstream phase quoting P/C 0.726 as bullish evidence is misreading the
   tape; phase 3 should note that ENPH's own P/C sits at the **87.5th self percentile**
   (`phase-0.5-context.md`) — put-heavy *for this name* despite the sub-1.0 absolute level.
2. **Call premium exceeds put premium ($2.89M vs $2.37M, 1.219×) purely on notional
   density**, not on intent — calls are cheaper per contract at these strikes and
   more numerous.

**Magnitude discipline (mandated by `phase-0.5-context.md`).** −$479,813 is **5.8× below**
the day's bearish top-50 cutoff (NEE, −$2,762,256) and ranks ENPH **477th of 538**
Technology names. Total premium sits at the **93.8th universe percentile but the 26.6th
self percentile**. Everything below is directionally informative and economically
negligible. `unusual_verdict` = **BUSY_NAME_NORMAL_DAY** → **this phase is capped at `+`.**

### B — Whole-tape ask/bid decomposition (the phase's most load-bearing evidence)

The `uw_screener` block carries `call_volume`/`put_volume` but not the ask/bid split; the
CLI exposes ask-vs-bid only per-contract in `sweeps`/`smart-money-flow`, which is top-N.
The screener parquet **does** carry whole-tape side-classified volume, so this is a
sanctioned escape-hatch cut (`lib/duckdb-cuts.md`) — the only way to get an ask-vs-bid
read on **100% of the tape** rather than the top 21.9% of it.

| Date | Call ask | Call bid | Call a/b | Put ask | Put bid | **Put a/b** | Net aggr. dir. |
|---|---|---|---|---|---|---|---|
| 2026-07-20 | 3,753 | 6,120 | 0.613 | 4,728 | 1,899 | 2.490 | −5,196 |
| 2026-07-21 | 1,985 | 3,772 | 0.526 | 1,321 | 1,885 | 0.701 | −1,223 |
| 2026-07-22 | 2,875 | 3,917 | 0.734 | 914 | 902 | 1.013 | −1,054 |
| 2026-07-23 | 4,884 | 6,238 | 0.783 | 3,521 | 6,937 | **0.508** | **+2,062** |
| 2026-07-24 | 2,851 | 5,475 | 0.521 | 2,349 | 2,880 | 0.816 | −2,093 |
| 2026-07-27 | 4,196 | 4,635 | 0.905 | 2,410 | 1,719 | 1.402 | −1,130 |
| 2026-07-28 | 10,292 | 10,806 | 0.952 | 8,277 | 5,981 | 1.384 | −2,810 |
| **2026-07-29** | **8,285** | **8,284** | **1.000** | **7,236** | **4,613** | **1.569** | **−2,622** |

`Net aggr. dir.` = `(call_ask − call_bid) − (put_ask − put_bid)`. Classification coverage
today is high — calls 16,569 / 18,150 = **91.3%**, puts 11,849 / 13,176 = **89.9%** — so
this is a genuine whole-tape read, not a fragment.

Three things fall out:

1. **Today is the most put-bid session of the window** (`put_ask_bid_x` 1.569, highest of
   the eight) and the **third consecutive session ≥ 1.38** (1.402 → 1.384 → 1.569). Put
   buying is not a one-day event-day artifact; it is an accelerating three-day trend that
   spans the print.
2. **Call flow has stopped being dumped but has not turned into buying.** `call_ask_bid_x`
   climbed 0.521 → 0.905 → 0.952 → **1.000** across the last four sessions. Dead-even is
   the *absence* of a signal, not a bullish one — and it is why the phase reads bearish
   rather than strongly bearish.
3. **`Net aggr. dir.` is negative in 7 of 8 sessions.** The aggressive-flow tilt has been
   persistently bearish for two weeks, through a −11.1% decline (39.46 → 35.07).

**This resolves an open question from `phase-0.5-context.md`.** That phase flagged the
2026-07-23 `net_flow` of **+$5,904,530** — the largest directional print of the window,
on a −1.74% candle — and asked whether the position was still alive. The ask/bid split
answers it: 07-23 is the *only* session with positive net aggressive direction (+2,062),
and it got there through **put selling** (`put_ask_bid_x` 0.508 — puts sold roughly 2:1,
6,937 bid vs 3,521 ask), not call buying (`call_ask_bid_x` 0.783, calls still net sold).
That +$5.9M was **premium collected by writing puts** into a 38.89 close. ENPH has since
fallen to 35.07 (**−9.8%**), so that position is now underwater and is a *source* of
potential forced hedging, not a bullish vote. Phase 3 must check whether those strikes
still sit in open interest.

### C — Intraday price structure (the dominant fact of the session)

| Date | Prev close | High | Low | Close | High vs prev close | Close vs high | Volume |
|---|---|---|---|---|---|---|---|
| 2026-07-20 | 41.57 | 41.55 | 39.24 | 39.46 | −0.05% | −5.03% | 3,467,516 |
| 2026-07-21 | 39.46 | 40.82 | 39.10 | 39.94 | +3.44% | −2.15% | 2,838,074 |
| 2026-07-22 | 39.94 | 40.82 | 39.40 | 39.58 | +2.20% | −3.04% | 2,360,776 |
| 2026-07-23 | 39.58 | 39.52 | 37.85 | 38.89 | −0.15% | −1.59% | 3,800,484 |
| 2026-07-24 | 38.89 | 38.93 | 36.58 | 36.70 | +0.10% | −5.73% | 3,509,972 |
| 2026-07-27 | 36.70 | 38.25 | 36.21 | 38.01 | +4.22% | −0.63% | 3,114,887 |
| 2026-07-28 | 38.01 | 37.90 | 35.39 | 36.32 | −0.29% | −4.17% | 7,442,672 |
| **2026-07-29** | **36.32** | **39.60** | **34.96** | **35.07** | **+9.03%** | **−11.44%** | **8,670,939** |

**This is a full gap-and-crap / bearish outside day, and it materially corrects the
`phase-0.5-context.md` framing.** That phase saw only the −3.44% close-to-close and
concluded the event "passed with a whimper." At intraday resolution:

- ENPH **gapped up 9.03%** to 39.60 — the initial market verdict on the Q2 print was
  *positive*.
- It then gave back the entire gap and more, closing at 35.07, **$0.11 (0.31%) above the
  session low of 34.96** and **below the prior close**.
- Realized **range = 39.60 − 34.96 = $4.64 = 12.8% of the 36.32 prior close** (13.2%
  measured against the low). The pre-print implied move was **±12.25%**
  (`phase-0-intake.md`). **The options market priced the magnitude almost exactly right
  — it simply had no directional edge, and the tape round-tripped it.**
- Volume 8,670,939 = **1.69×** the 30-day average (5,127,858) and the highest of the
  window.

The independent print-level tape confirms the arc. `underlying_price` on the top-25
prints runs **38.345 at 13:34 UTC (9:34 ET) → 35.035 at 19:59 UTC (15:59 ET)** — a
monotone intraday bleed, not a single air-pocket:

| Time (UTC) | Underlying | Print |
|---|---|---|
| 13:34 | 38.345 | C40 bid $22,140 |
| 14:24 | 36.555 | C50 bid $80,000 |
| 15:15 | **36.69** | **P35 ask $196,240** ← largest print of the day, **pre-FOMC** |
| 16:20 | 36.07 | P35 ask $31,500 |
| 18:38 | 35.76 | P35.5 ask $27,250 |
| 19:53 | 35.16 | P55 bid $113,160 |
| 19:59 | 35.035 | P60 bid $66,355 |

Two timing facts matter downstream: the **largest bet of the day was placed at 11:15 ET,
before the 14:00 ET FOMC statement**, so it is an ENPH/earnings expression rather than a
macro reaction; and the **two deep-ITM put sales landed at 15:53 and 15:59 ET**, in the
closing minutes (see §E for why that changes their interpretation).

> **Attribution caution carried from `phase-0.5-context.md`:** 15 of 16 solar names fell
> today (SHLS −7.03%, FLNC −5.78%, ARRY −5.69% all worse than ENPH's −3.44%). The
> *close-to-close* decline is largely sector beta. But **the +9.03% gap and its full
> intraday engulfment are ENPH-specific** — no peer had an earnings print — and that
> reversal is the idiosyncratic signal. Phases 5 and 7b must keep these two components
> separate.

### D — Sweeps (ask vs bid, ≥ $100,000 premium)

**Ask side — aggressive buying (2 rows, $470,181):**

| Expiry | Contract | Premium | Size | Trades | Avg px |
|---|---|---|---|---|---|
| 2026-10-16 | **P35** | **$260,820** | 591 | 18 | $4.41 |
| 2026-08-07 | **C37** | **$209,361** | 1,157 | 79 | $1.85 |

**Bid side — aggressive selling (5 rows, $666,419):**

| Expiry | Contract | Premium | Size | Trades | Avg px |
|---|---|---|---|---|---|
| 2026-09-18 | C40 | $168,839 | 428 | 75 | $3.58 |
| 2026-08-21 | P40 | $147,337 | 294 | 64 | $5.03 |
| 2027-01-15 | C55 | $123,098 | 353 | 22 | $3.47 |
| 2028-01-21 | C75 | $113,985 | 150 | 6 | $7.52 |
| 2027-06-17 | P55 | $113,160 | 46 | 1 | $24.60 |

**Bid-side sweep premium exceeds ask-side $666,419 vs $470,181 → net −$196,238.**

The composition is more informative than the net:

- **Upside call supply is the dominant sweep theme.** Three of five bid rows are
  long-dated call *writing* — 2026-09-18 C40, 2027-01-15 C55, 2028-01-21 C75 — totalling
  **$405,922**, versus only **$209,361** of call buying (the Aug-07 C37). Someone is
  systematically monetizing ENPH upside from 40 out to 75 across 2 months to 18 months.
  This is the structural counterweight to any squeeze thesis and phase 3/4 must check
  whether it shows up as OI at those strikes.
- **Downside is being bought at the money, not in the tail.** The single largest ask sweep
  is the **Oct-16 P35** — struck at spot, 79 DTE, `delta` −0.368. This is a considered
  directional hedge or bearish position with real vega, not a lottery ticket.
- **Two clean opposing prints.** The Aug-07 C37 (1,157 contracts, 79 trades, +5.5% OTM,
  9 DTE) is genuine short-dated upside speculation. The Aug-21 P40 bid (294 contracts,
  ITM put *sold*) leans bullish. Neither is large.

### E — Largest premium prints (top-25) and the ambiguity that must be flagged

Top-25 total premium **$1,149,093 = 21.9%** of the whole-tape $5,258,451. Per the audit
warning in the phase spec, the top-N is the tip of the iceberg and is read *against* §A/§B.

**Bucketed by option type × initiating side:**

| Bucket | n | Premium | Contracts | Signed delta notional |
|---|---|---|---|---|
| put · **ask** (bought) | 6 | **$370,270** | 1,966 | **−$1,681,017** |
| call · **bid** (sold) | 8 | **$308,168** | 737 | **−$1,090,364** |
| put · **bid** (sold) | 4 | $242,870 | **184** | +$379,988 |
| call · **ask** (bought) | 3 | $95,048 | 538 | +$748,380 |
| call · mid | 3 | $110,080 | 544 | excluded |
| put · mid | 1 | $22,657 | 163 | excluded |
| **Total (ask/bid only)** | **21** | **$1,016,356** | | **−$1,643,012** |

Initiator-signed delta notional = `±delta × size × 100 × underlying_price`, positive for
ask-initiated (buyer) and negative for bid-initiated (seller), mid excluded. Net
**−$1,643,012 = 0.034% of the $4.80B market cap.** Directionally bearish, economically
irrelevant — both must be stated together.

**Bearish-leaning initiations** (buy puts + sell calls) = $678,438 versus
**bullish-leaning** (buy calls + sell puts) = $337,918 — roughly **2:1 bearish** in the
top-25, consistent with §B's whole-tape read.

**The honest caveat on `put · bid`.** That bucket's $242,870 rests on just **184
contracts** and consists of deep-ITM long-dated puts:

| Print | Premium | Size | Avg px | Intrinsic (spot 35.07) | Extrinsic | Time (ET) |
|---|---|---|---|---|---|---|
| 2027-06-17 P55 bid | $113,160 | 46 | $24.60 | $19.93 | $4.67 | **15:53** |
| 2027-06-17 P60 bid | $66,355 | 23 | $28.85 | $24.93 | $3.92 | **15:59** |
| 2026-08-21 P45 bid | $37,480 | 40 | $9.37 | $9.93 | −$0.56 | 11:01 |
| 2026-08-21 P37 bid | $25,875 | 75 | $3.45 | $1.93 | $1.52 | 10:42 |

The two Jun-2027 prints — **69 contracts total, 1 trade each, executed in the final seven
minutes of the session, deep in the money** — read as **position housekeeping: an existing
long-put holder monetizing a profitable bearish position**, not as a fresh synthetic-long
initiation. Both readings are defensible from EOD data alone and I will not pretend
otherwise, but the size, trade count, moneyness and closing-bell timing all favour the
close-out. Under that reading the +$379,988 of "bullish" signed delta in this bucket is
**an exit, not a vote**, and the top-25's true directional tilt is more bearish than the
table's net suggests. Phase 3 can partially adjudicate this via OI change at those strikes.

### F — New positioning (`vol_oi_ratio` ≥ 3)

8 contracts qualify; total premium **$536,710** (calls $305,308 / puts $231,402):

| Expiry | Contract | Vol | OI | vol/OI | Premium | Avg IV | Trades |
|---|---|---|---|---|---|---|---|
| 2026-08-14 | C36 | 111 | 4 | **27.75** | $28,231 | 87% | 14 |
| 2026-08-07 | **C37** | 1,206 | 81 | **14.89** | **$218,770** | 93% | 99 |
| 2026-09-04 | P25 | 1,845 | 160 | 11.53 | $61,546 | 87% | 34 |
| 2026-09-04 | P30 | 298 | 28 | 10.64 | $35,556 | 83% | 17 |
| 2026-09-04 | P35 | 185 | 18 | 10.28 | $56,611 | 85% | 14 |
| 2026-07-31 | C37.5 | 484 | 63 | 7.68 | $58,307 | 131% | 27 |
| 2026-07-31 | P35.5 | 337 | 66 | 5.11 | $34,908 | 127% | 46 |
| 2026-08-21 | P37 | 122 | 39 | 3.13 | $42,781 | 83% | 18 |

- **The Aug-07 C37 is the day's one unambiguous bullish initiation** and the only
  new-position row with real conviction markers: 1,206 contracts on 81 OI, **99 separate
  trades**, and cross-confirmed by the ask-side sweep at 1,157 contracts / $209,361 —
  **~96% of the volume was aggressively bought**. Spot 35.07, strike 37 (+5.5% OTM),
  **9 DTE**. Real, aggressive, and short-dated: this needs a move inside two weeks or it
  is worthless. At $218,770 it is 4.2% of the day's premium.
- **A fresh Sept-04 weekly put ladder was built** — P25 + P30 + P35 = $153,713 on
  vol/OI 10.3–11.5×. The P25 is 1,845 contracts for only $61,546 (**28.7% OTM**, avg
  $0.33) — cheap crash insurance, high contract count, negligible dollars. Phase 3 should
  watch whether the Sept-04 ladder persists in OI.
- **The 07-31 rows are expiry-week mechanics, not intent.** C37.5 at 131% IV and P35.5 at
  127% IV, 2 DTE, straddling spot — gamma scalping into Friday's expiry.
- Total new-position premium $536,710 is **10.2% of the day's tape** — modest even by
  ENPH's own standards, on the day after earnings.

### G — IV outliers and Greeks

`iv-outliers` returns **15 rows, all in the 2026-07-31 front expiry** (2 DTE), IV
**128%–233%**:

| Contract | Avg IV | Vol | Premium |
|---|---|---|---|
| 07-31 P45 | **233%** | 52 | $44,857 |
| 07-31 C49.5 | 208% | 69 | $3,792 |
| 07-31 P29.5 | 168% | 251 | $2,341 |
| 07-31 C48 | 163% | 62 | $276 |
| 07-31 P28 | 157% | 214 | $224 |
| 07-31 C44 | 142% | 53 | $660 |
| 07-31 P29 | 142% | 520 | $709 |
| 07-31 P30.5 | 141% | 151 | $676 |
| 07-31 P31 / P32 | 139% | 206 / 107 | $1,259 / $1,247 |
| 07-31 P37.5 | 138% | 75 | $13,337 |
| 07-31 P30 | 136% | 484 | $1,246 |
| 07-31 C42.5 | 134% | 200 | $2,984 |
| **07-31 C37.5** | **132%** | **482** | **$58,127** |
| 07-31 C38.5 | 130% | 69 | $4,893 |

**Interpretation: this is expiry mechanics, not information.** Every row is the 2-DTE
expiry, where IV inflates by construction. Premium is trivial in 12 of 15 rows ($224 to
$4,893). The wide far-OTM put ladder (P28 → P32: 1,933 contracts for a combined **$7,702**
— avg $0.04/contract) is lottery tickets and dealer hedging noise, and any phase citing
"1,933 contracts of put buying" without the dollar figure would be badly misleading. Only
three rows carry real money: C37.5 $58,127, P45 $44,857, P37.5 $13,337.

Crucially, **the IV outlier list contains nothing beyond 07-31** — there is *no*
elevated-IV cluster in the Aug/Sep/Oct expiries where the actual positioning lives (§D–F).
Consistent with `phase-0.5-context.md`: `iv30d` collapsed 0.905 → **0.797** and `iv_rank`
sits at ENPH's **15.6th self percentile**. The back of the curve is quiet and cheap.

`greek-screener --sort-by premium` returned the **same 15 prints** as
`top-premium-trades`, enriched with greeks — no independent rows, so it adds confirmation
rather than new evidence. Notable greeks: the Oct-16 P35 carries `gamma` 0.0273 /
`vega` 0.0644; the 07-31 C36.5 carries `gamma` **0.1115** (4× the Oct put — near-dated ATM
gamma, relevant to phase 4's expiry-week read); the Jan-2028 C75 carries `vega` **0.1762**,
the highest in the set, so the LEAP call *writing* in §D is a short-vega expression —
someone selling long-dated ENPH volatility at a 15.6th-percentile IV rank.

### H — Market-wide screens: ENPH does not appear

| Screen | Result |
|---|---|
| `smart-money-flow --direction bullish --top-n 10 --min-volume 500` | ENPH **absent**. Leaders: INFY, TLT, GOOGL, MSTR, BTDR, PEP, IWM, SPY, VFC |
| `smart-money-flow --direction bearish --top-n 10 --min-volume 500` | ENPH **absent**. Leaders: GOOGL, MSTR, WOLF, IWM, BTDR, SPY, **PLUG 261218 P2**, AVTR, VIX |
| `sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3` | ENPH **absent**. Leaders: REPL, STUB, SPXW, CMCSA, HYG, IWM, META, KEEL, ITUB, TLT, FRMI, BTAL, EWZ, DLO, **NRG 260821 C165** |

**No smart-money flow detected on this date** — recorded per the phase's composition
guidance; the commands were **not** re-run with looser thresholds. This is corroborating
evidence for the magnitude discipline in §A: ENPH's tape today does not clear any
market-wide aggression filter in either direction.

One adjacent-name observation worth handing to phase 6: **PLUG 2026-12-18 P2 appears on
the bearish smart-money list** and **NRG 2026-08-21 C165 on the sweep-ratio list** — the
clean-energy complex is seeing directional institutional flow, just not in ENPH. This is
consistent with `phase-0.5-context.md`'s finding that capital is rotating to
grid/power-generation (GEV, PWR, NRG) rather than distributed solar.

### I — Sweep persistence (5-day campaign read)

`uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ENPH`:

| Field | Value |
|---|---|
| `ticker` | ENPH |
| `sessions_in_top` | **5** (of 5) |
| `consistency_score` | **1.0** |
| `dominant_direction` | **mixed** |
| `total_sweep_premium` | **$7,400,862** |

Versus the 2026-07-27 run (`research/ENPH/2026-07-27/decision.json`, which recorded a
"5-of-5 **bearish** sweep campaign worth only $1,335,255"):

| | 2026-07-27 | 2026-07-29 | Change |
|---|---|---|---|
| `sessions_in_top` | 5/5 | 5/5 | unchanged |
| `total_sweep_premium` | $1,335,255 | **$7,400,862** | **+454%** |
| `dominant_direction` | bearish | **mixed** | **flipped** |

**Sweep premium rose 5.5× while directional consensus broke down.** ENPH has been in the
top-20 sweep names every session for a week — maximal attention — but the event resolved
the *consensus*, not the *interest*: two-way institutional traffic now, where a week ago
it was one-way bearish. This is the single strongest argument against high conviction in
either direction from flow alone, and phase 8b should weigh it against any one-sided thesis.

> **Reproducibility caveat.** `sweep-persistence` accepts **no `--date` flag** (`Error:
> unknown flag: --date`, exit 1 — see `## Tool errors`) and anchors to the latest
> available sessions, consistent with `memory/uw-cli-mcp-parity.md`. Because the as-of
> date **is** the latest available date (2026-07-29, `phase-0-intake.md`), the 5-session
> window is 2026-07-23 → 2026-07-29 and the read is as-of-correct **for this run only**.
> A future re-run at a later date will not reproduce it.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ENPH --date 2026-07-29 --json` | `call_premium`=2888189, `put_premium`=2370262, `bullish_premium`=2153830, `bearish_premium`=2633643, `net_call_premium`=−223790, `net_put_premium`=+256023, `put_call_ratio`=0.72595 ← `.uw_screener`; `net_flow`=−479813 **derived** | whole tape |
| `uw options-flow sweeps --symbol ENPH --side ask --min-premium 100000 --top-n 25 --date 2026-07-29 --json` | 2 rows; Oct-16 P35 `total_premium`=260820/`total_size`=591; Aug-07 C37 209361/1157 ← `.results[]`; sum $470,181 | top-25 (2 returned) |
| `uw options-flow sweeps --symbol ENPH --side bid --min-premium 100000 --top-n 25 --date 2026-07-29 --json` | 5 rows; Sep-18 C40 168839, Aug-21 P40 147337, Jan-15-27 C55 123098, Jan-21-28 C75 113985, Jun-17-27 P55 113160 ← `.results[]`; sum $666,419 | top-25 (5 returned) |
| `uw options-flow unusual-volume --symbol ENPH --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-29 --json` | 8 rows; Aug-07 C37 `vol_oi_ratio`=14.89 (`total_volume`=1206, `open_interest`=81, `total_premium`=218770, `trade_count`=99) ← `.results[]`; sum $536,710 | top-25 (8 returned) |
| `uw options-flow top-premium-trades --symbol ENPH --top-n 25 --date 2026-07-29 --json` | Σ`premium`=1149093 ← `[.results[].premium]\|add`; by-side ask=465318/bid=551038/mid=132737 ← `group_by(.side)`; signed Δ-notional=−1643012 ← `map((if .side=="ask" then 1 else -1 end)*.delta*.size*100*.underlying_price)\|add` | top-25 |
| `uw options-flow iv-outliers --symbol ENPH --top-n 15 --date 2026-07-29 --json` | all 15 rows `expiry`=2026-07-31; `avg_iv` max 2.33 (P45), `total_premium` 224…58127 ← `.results[]` | top-15 |
| `uw options-flow greek-screener --symbol ENPH --top-n 15 --sort-by premium --date 2026-07-29 --json` | Oct-16 P35 `delta`=−0.3685/`gamma`=0.02727/`vega`=0.06436; 07-31 C36.5 `gamma`=0.11151; Jan-28 C75 `vega`=0.17615 ← `.results[]` — **same 15 prints as top-premium-trades** | top-15 |
| `uw hot-chains smart-money-flow --direction bullish --top-n 10 --min-volume 500 --date 2026-07-29 --json` | ENPH **absent** ← `[.results[]\|select((.option_symbol//"")\|startswith("ENPH"))]` → `[]` | top-10 |
| `uw hot-chains smart-money-flow --direction bearish --top-n 10 --min-volume 500 --date 2026-07-29 --json` | ENPH **absent** ← same null-safe select → `[]`; `PLUG261218P00002000` present | top-10 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-07-29 --json` | ENPH **absent**; `NRG260821C00165000` present ← `.results[]` | top-15 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ENPH --json` | `sessions_in_top`=5, `consistency_score`=1, `dominant_direction`="mixed", `total_sweep_premium`=7400862 ← `.results[0]` | 1 |
| DuckDB `stock-screener-*.parquet` (8 files ≥ 2026-07-20) — whole-tape ask/bid | today `call_volume_ask_side`=8285, `call_volume_bid_side`=8284, `put_volume_ask_side`=7236, `put_volume_bid_side`=4613 → put a/b **1.569**, net aggr **−2622** | 8 sessions |
| DuckDB — OHLC verification | 2026-07-29 `high`=39.60, `low`=34.96, `close`=35.07, `prev_close`=36.32, `total_volume`=8670939 → high +9.03%, close −11.44% from high | 8 sessions |
| DuckDB — classification coverage | calls 16569/18150=91.3%, puts 11849/13176=89.9% ← `(ask_side+bid_side)/volume` | 1 |

All eleven `uw` reads were captured to a file before being queried and every value
round-tripped through `jq` on validated JSON (`memory/batched-stdout-swallow.md`); all
ENPH-row selects used the null-safe `[…]|.[0]//null` / `select(...)` → `[]` form. Two
values are **derived**, not read: `net_flow` (§A, cross-validated two ways) and the
initiator-signed delta notional (§E, formula stated inline).

## Tool errors

1. **`uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ENPH --date 2026-07-29 --json`**
   → exit **1**:
   ```
   Error: unknown flag: --date
   error: unknown flag: --date
   ```
   `--help` confirms the leaf accepts only `--days`, `--symbol`, `--top-n`. **Resolution:**
   re-run without `--date`; the leaf anchors to the latest available sessions, which here
   *is* the as-of date (2026-07-29), so the result is as-of-correct for this run. The
   reproducibility limitation is recorded in §I. No value was transcribed from the failed
   invocation — the first `jq` attempt errored (`parse error: Invalid numeric literal at
   line 1, column 6`, parsing the plaintext `Error:` string) and was correctly treated as
   a tool error per the JSON-validity gate.

No other errors. All remaining ten `uw` calls returned exit 0 with parseable JSON.
`uw hot-chains sweep-ratio` **does** accept `--date` (exit 0 both with and without);
ENPH was absent either way.

## DATA NOTE / CORRECTION

**One material correction to an upstream phase, made from validated data in this phase.**

`phase-0.5-context.md` states in its Summary: *"The earnings event passed with a whimper,
and that is the finding"*, and in its trailing-tape section: *"the realized reaction
**−3.44% ≈ 28% of the priced ±12.25%**"*, concluding *"Vol sellers won the event
decisively."*

- **What was wrong:** the inference, not the number. −3.44% is the correct
  close-to-close change (`close` 35.07 / `prev_close` 36.32) and 28% is arithmetically
  right, but both are computed from closes only and therefore describe the *net* of a
  violent two-sided session as though it were a quiet one.
- **Corrected reading:** `high`=**39.60**, `low`=**34.96** → realized range **$4.64 =
  12.8% of prev close**, against a pre-print implied **±12.25%**. **The implied move
  captured the realized range almost exactly.** Vol sellers did not "win decisively" —
  intraday realized vol roughly *matched* what was priced; what collapsed was the
  *forward* surface (`iv30d` 0.905 → 0.797) once the binary resolved, which is mechanical
  and expected.
- **`jq` / SQL path re-verified against:** `read_parquet('stock-screener-2026-07-29.parquet')`
  → `high`, `low`, `close`, `prev_close`, `total_volume` for `ticker='ENPH'`;
  independently corroborated by `.results[].underlying_price` on
  `top-premium-trades` (38.345 at 13:34 UTC → 35.035 at 19:59 UTC).
- **Downstream consequence:** phase 4 must **not** treat `iv_rank` 47.05 / self-15.6th
  percentile as evidence that realized vol is low or that the market over-priced the
  event. Realized *range* vol was fully consistent with the pre-print mark. The cheapness
  in the surface is a post-catalyst term-structure fact, not a mispricing that the event
  demonstrated.

`phase-0.5-context.md` is **not** edited (immutability rule); this note is the correction
of record and phases 4, 5, 7b and 9 must read it alongside that file.

No other value in this phase was revised after its first validated read.

## Verdict for downstream phases

- **Net bias: BEARISH** — on evidence quality, not on size.
- **Conviction: 3 / 5.** Three independent lanes agree on direction (whole-tape ask/bid
  −2,622 contracts with puts bought 1.569× and calls flat at 1.000; top-25 initiations
  ~2:1 bearish with signed delta −$1.64M; a gap-up fully engulfed to close $0.11 off the
  low on 1.69× volume). Conviction is held at 3 rather than 4–5 because (a) magnitude is
  negligible — `net_flow` −$479,813 is 5.8× below the day's bearish top-50 cutoff and the
  signed delta is 0.034% of market cap; (b) `phase-0.5-context.md` caps phases 1–2 at
  **`+`** on BUSY_NAME_NORMAL_DAY; (c) ENPH clears **no** market-wide aggression screen in
  either direction; and (d) `dominant_direction` on the 5-day sweep campaign is
  explicitly **"mixed"**, having flipped from bearish while premium grew 5.5×. Flow says
  which way, and says so consistently — it does not say *hard*.
- **Three datapoints later phases must remember:**
  1. **`put_volume_ask_side` 7,236 vs `put_volume_bid_side` 4,613 → 1.569×, with
     `call_volume_ask_side` 8,285 vs `call_volume_bid_side` 8,284 → 1.000.** Whole tape,
     ~90% classified, third consecutive session of put a/b ≥ 1.38, net aggressive
     direction negative in 7 of 8 sessions. **This is the phase's load-bearing evidence
     and it overrides the `put_call_ratio` 0.7259, which is a volume artifact** —
     `net_call_premium` is −$223,790 (calls net sold) and `net_put_premium` +$256,023
     (puts net bought).
  2. **High 39.60 (+9.03%) → close 35.07 (−11.44% from high, 0.31% off the low of 34.96),
     volume 1.69× average.** The initial reaction to the Q2 print was *positive* and was
     completely reversed. Realized range 12.8% ≈ the pre-print implied ±12.25%. See
     `## DATA NOTE` — this corrects `phase-0.5-context.md`'s "whimper" framing and
     constrains phase 4's reading of the low IV rank.
  3. **The upside is being sold and the downside bought at the money.** $405,922 of
     long-dated call *writing* (Sep C40, Jan-27 C55, Jan-28 C75 — the C75 carrying the
     set's highest `vega` 0.1762, i.e. short long-dated vol at a 15.6th-percentile IV
     rank) versus a single $196,240–$260,820 bought **Oct-16 P35** at spot, 79 DTE,
     `delta` −0.368. The lone credible bull expression is **2026-08-07 C37** — 1,206
     vol on 81 OI, 99 trades, ~96% ask-side, $218,770 — which is real but needs a move
     within **9 days**.
- **Open questions for downstream:**
  - **Is the dark pool confirming or contradicting this?** A gap-up sold to the low on
    1.69× volume should show distribution in the print tape if the selling was
    institutional. If phase 2 instead shows accumulation at 35, the two lanes conflict and
    phase 10 must flag it. Apply `memory/darkpool-closing-auction-artifact.md` — decompose
    tiers by session before calling anything. (→ 2)
  - **Does OI corroborate the call-writing campaign at 40/55/75 and the Sept-04 put
    ladder (P25/P30/P35), and did the 07-23 put-selling position (+$5,904,530, now ~9.8%
    underwater) survive?** Today's OI build was near-balanced (+9,120 calls / +8,868 puts,
    `oi_pcr` 0.72) — strike placement is what matters. (→ 3)
  - **Can the two Jun-2027 deep-ITM put sales (69 contracts, 15:53/15:59 ET) be resolved
    as closes rather than synthetic longs?** If they are closes, the top-25 is more
    bearish than §E's net shows. (→ 3)
  - **With every IV outlier confined to the 2-DTE 07-31 expiry and nothing elevated in
    Aug/Sep/Oct, what does the term structure look like once the 07-31 gamma island
    expires?** Spot 35.07 sits on the 08-21 $35 put wall. (→ 4)
  - **Does the 17.94% short base explain the +9.03% gap** (a genuine squeeze attempt that
    failed) **or was the gap real buying that got distributed into?** The distinction
    decides whether 35 is support or a waypoint. (→ 7c, 2)
