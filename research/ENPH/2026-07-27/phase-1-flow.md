# Phase 1 — Options Flow

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T20:22:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`

## Summary

**The tape is bearish, persistently so, and tiny.** Whole-tape net flow is
**−$258,731** (`bullish_premium 1,843,847 − bearish_premium 2,102,578`) on
$4.76M of total premium — a directional statement worth about a quarter of one
percent of ENPH's $4.84B market cap. What redeems the signal is **persistence,
not size**: `hot-chains sweep-persistence` returns ENPH with
**`consistency_score = 1`, `dominant_direction = "bearish"`, `sessions_in_top = 5`
of 5** covering 2026-07-21→2026-07-27, on `total_sweep_premium = $1,335,255`. The
whole-tape ask/bid split corroborates it independently — puts are being **bought**
(`put_ask_share = 0.584`) while calls are being **sold** (`call_ask_share = 0.475`),
a configuration repeated in **5 of the last 6 sessions**. Set against that, today's
+3.57% price bounce has no flow behind it. The single most important non-directional
fact: **all 15 IV outliers sit in one expiry — 2026-07-31 — at 160–186% IV** against
a 92% `iv30d`, which is the market pricing Wednesday's post-close print, not a view.

**Conviction is capped at `+` (not `++`)** per `[CTX:] unusual_verdict =
BUSY_NAME_NORMAL_DAY` (`phase-0.5-context.md`), and the cap is deserved: today's
option volume is the **16.4th percentile of ENPH's own history**.

## Key signals

- **5-of-5 session bearish sweep campaign, perfect consistency.**
  `consistency_score=1`, `sessions_in_top=5`, `dominant_direction="bearish"`,
  `total_sweep_premium=$1,335,255` over 2026-07-21→27 [FLOW:sweep_persistence].
  This is the phase's load-bearing signal.
- **Aggressors buy puts and sell calls, whole-tape.** `put_ask_share=0.584` vs
  `call_ask_share=0.475`; net aggressive direction **−1,130 contracts** today and
  negative in 5 of 6 sessions [FLOW:screener_ask_bid DUCKDB].
- **Ask-side top prints favour puts ~4:1.** Of the top-25 premium trades,
  aggressive (ask) puts total **$273,284** vs aggressive calls **$67,819**
  [FLOW:top_premium_trades].
- **All 15 IV outliers are the 2026-07-31 weekly at 160–186% IV** vs `iv30d=0.922`
  — a pure earnings-event premium, not directional conviction [FLOW:iv_outliers].
- **No smart-money-flow rows and no sweep-ratio rows for ENPH** on this date; the
  name is absent from both market-wide top-10/top-15 lists [FLOW:smart_money_flow],
  [FLOW:sweep_ratio]. Consistent with phase-0.5's "outside top-50 on all five
  screener metrics".

## Detailed findings

### Whole-tape aggregate — read the top-N against this

`uw insights deep-dive --symbol ENPH --date 2026-07-27` → `.uw_screener`:

| Field | Value |
|---|---|
| `call_premium` | $2,171,125 |
| `put_premium` | **$2,593,624** |
| `bullish_premium` | $1,843,847 |
| `bearish_premium` | **$2,102,578** |
| **derived `net_flow`** (`bullish − bearish`) | **−$258,731** |
| `call_volume` | 9,693 |
| `put_volume` | 5,306 |
| `put_call_ratio` | 0.5474 |
| `total_open_interest` | 355,935 |
| `iv_rank` | 69.81 |
| `iv30d` | 0.9220 |
| `implied_move` / `implied_move_perc` | **$4.65 / 12.25%** |
| `next_earnings_date` / `er_time` | **2026-07-28 / postmarket** |

**Total tape premium = $4,764,749.** The top-25 premium prints sum to
**$1,468,329 = 30.8% of the tape** — almost exactly the ~30% tip-of-the-iceberg
ratio the audit warns about. Everything in the sections below describes less than
a third of the day; the aggregate above is the day.

**The volume/premium contradiction, resolved.** `put_call_ratio = 0.547` says
calls outnumber puts nearly 2:1 by *volume* (9,693 vs 5,306) — superficially
bullish. But put *premium* exceeds call premium ($2.59M vs $2.17M), and the
ask/bid split shows the calls are being **sold** while the puts are **bought**.
High call volume here is supply, not demand. **Any downstream phase that cites
`put_call_ratio = 0.547` as bullish without the ask/bid overlay is misreading it.**

Whole-tape aggressive split (screener parquet, `[FLOW:… DUCKDB]`):

| Date | call ask/bid | put ask/bid | `call_ask_share` | `put_ask_share` | Net aggressive (contracts) |
|---|---|---|---|---|---|
| **2026-07-27** | 4,196 / 4,635 | 2,410 / 1,719 | **0.475** | **0.584** | **−1,130** |
| 2026-07-24 | 2,851 / 5,475 | 2,349 / 2,880 | 0.342 | 0.449 | −2,093 |
| 2026-07-23 | 4,884 / 6,238 | 3,521 / 6,937 | 0.439 | 0.337 | **+2,062** |
| 2026-07-22 | 2,875 / 3,917 | 914 / 902 | 0.423 | 0.503 | −1,054 |
| 2026-07-21 | 1,985 / 3,772 | 1,321 / 1,885 | 0.345 | 0.412 | −1,223 |
| 2026-07-20 | 3,753 / 6,120 | 4,728 / 1,899 | 0.380 | **0.713** | **−5,196** |

`call_ask_share` has been **below 0.50 in all six sessions** — calls are net sold
every single day. The one green day (2026-07-23, +2,062) came from put *selling*
(`put_ask_share` 0.337), not call buying, and it matches the single +$1,887k
`net_dir` day in phase-0.5's series. **There is no session in the last six where
aggressive call demand led.**

### Sweeps (ask vs bid)

`uw options-flow sweeps --symbol ENPH --min-premium 100000` returned only
**5 lines total** — 2 ask, 3 bid. At a $100k floor this is a barren tape.

**Ask side (aggressive buyers) — $282,305:**

| Expiry | Contract | Premium | Size | Trades | Avg px | Read |
|---|---|---|---|---|---|---|
| 2026-10-16 | **P40** | **$176,570** | 232 | 43 | 7.63 | Buying ITM-ish downside past earnings |
| 2026-11-20 | C35 | $105,735 | 133 | 16 | 7.95 | Buying ITM calls (Δ~0.6) |

**Bid side (aggressive sellers) — $481,666:**

| Expiry | Contract | Premium | Size | Trades | Avg px | Read |
|---|---|---|---|---|---|---|
| 2027-06-17 | P40 | $205,860 | 161 | 8 | 12.77 | **Selling** long-dated puts |
| 2027-06-17 | P45 | $170,725 | 104 | 6 | 16.42 | **Selling** long-dated puts |
| 2026-12-18 | C50 | $105,081 | 243 | 20 | 4.36 | Selling upside calls |

**The structural read — a protection roll, not a directional bet.** The pairing of
*buying* Oct-16 $40 puts on the ask while *selling* Jun-2027 $40/$45 puts on the
bid is a **put calendar/diagonal rolled shorter** — someone is pulling protection
in from June 2027 to October 2026, i.e. concentrating hedge coverage around the
next two quarters rather than the next two years. That is a bearish *timing*
statement (near-term risk up) but is **not** the same as an outright new short,
and phase-8/8b should not double-count it as fresh directional conviction. The
Dec-18 C50 sale is consistent — capping upside at $50 for yield.

### New positioning (unusual volume, vol/OI ≥ 3)

Seven contracts cleared the `--min-vol-oi-ratio 3` filter. Note how small these
are — the largest is $130k:

| Expiry | Contract | Vol | OI | vol/OI | Premium | Trades | avg IV |
|---|---|---|---|---|---|---|---|
| 2026-08-07 | **P35.5** | 216 | 2 | **108.0** | $50,753 | 97 | 1.196 |
| 2026-10-16 | C60 | 541 | 18 | **30.1** | $68,552 | 45 | 0.871 |
| 2026-08-28 | C37 | 111 | 7 | 15.9 | $46,448 | 5 | 1.016 |
| 2026-07-31 | C38 | 128 | 26 | 4.9 | $28,678 | 39 | **1.687** |
| 2026-08-28 | C54 | 128 | 26 | 4.9 | $8,524 | 128 | 1.012 |
| 2026-11-20 | C35 | 163 | 36 | 4.5 | $130,335 | 17 | 0.880 |
| 2026-07-31 | C47 | 345 | 80 | 4.3 | $12,095 | 42 | **1.667** |

- The **Aug-07 $35.5 put at 108× OI on 97 separate trades** is the day's most
  extreme new position by ratio, but on $50,753 of premium and an average trade
  size of ~2 contracts it is **retail-scale**, not institutional. Phase-0 flagged
  it; it does not survive contact with the aggregate.
- The **Oct-16 $60 call, 541 lots on 18 OI ($68,552)**, is the only sizeable new
  *upside* position — but $60 is **+58% from $38.01** and only ~$127/contract. This
  is lottery-ticket structure, exactly what gets bought into a binary. Do not read
  it as a bullish institution.
- Five of seven new-position lines are calls, which reads bullish until it is set
  against `call_ask_share = 0.475` — most call volume today was sold, not bought.

### Largest premium prints

Top-25, $1,468,329 total (30.8% of tape). Side aggregation:

| Side × type | n | Premium |
|---|---|---|
| **ask** put | 6 | **$273,284** |
| ask call | 2 | $67,819 |
| bid put | 8 | $394,430 |
| bid call | 6 | $198,346 |
| mid put | 2 | $507,000 |
| mid call | 1 | $27,450 |

**Aggressive buyers favoured puts over calls 4.03 : 1** ($273,284 vs $67,819).

Notable individual prints:

| Time (Z) | Contract | Size | Premium | Px | Side | Δ | Underlying |
|---|---|---|---|---|---|---|---|
| 15:06 | **2026-11-20 P35** | **800** | **$464,000** | 5.80 | **mid** | −0.345 | 37.225 |
| 15:53 | 2027-06-17 P45 | 68 | $111,520 | 16.40 | bid | −0.419 | 36.60 |
| 15:00 | **2026-10-16 P60** | 34 | $81,192 | 23.88 | **ask** | **−0.789** | 37.25 |
| 14:47 | 2027-06-17 P40 | 58 | $74,530 | 12.85 | bid | −0.363 | 36.75 |
| 15:00 | **2026-12-18 P55** | 34 | $70,312 | 20.68 | **ask** | **−0.646** | 37.25 |
| 14:43 | 2028-12-15 C75 | 43 | $50,740 | 11.80 | bid | +0.566 | 36.415 |
| 17:12 | 2026-10-16 C40 | 85 | $42,925 | 5.05 | ask | +0.513 | 36.79 |
| 17:11 | 2026-10-16 P35 | 74 | $35,890 | 4.85 | ask | −0.365 | 36.74 |
| 17:11 | 2026-10-16 P55 ×2 | 15+15 | $58,500 | 19.50 | **ask** | −0.769 | 36.72 |
| 18:10 | 2026-08-14 P45 | 30 | $27,870 | 9.29 | bid | −0.725 | 37.08 |

Three things to note:

1. **The day's biggest print — 800× Nov-20 $35 puts for $464,000 — traded at
   `side = "mid"`.** Mid-market execution on an 800-lot is an unattributable
   print: it is consistent with a negotiated/blocked trade and gives **no
   buyer-vs-seller information**. It is 9.7% of the day's total premium and it is
   directionally *unreadable*. Phase-8 and phase-8b must not cite it as bearish
   conviction; the honest label is "large, unattributed, downside-strike".
2. **Deep-ITM puts bought on the ask** — Oct-16 P60 (Δ −0.789, $81,192), Dec-18 P55
   (Δ −0.646, $70,312), Oct-16 P55 ×2 (Δ −0.769, $58,500) — total **$210,004** at
   deltas of −0.65 to −0.79. Buying deep ITM puts is a **synthetic short stock**
   expression: high delta, low time-value bleed. This is the most genuinely
   directional bearish structure on the tape, though at ~$210k it is small.
   *Caveat:* deep-ITM put buys can also be the long leg of a conversion/reversal
   or a box against stock; without the paired stock print this is suggestive, not
   conclusive — **phase-2 should look for an offsetting dark-pool buy**.
3. **Far-dated LEAP calls are being sold** — Dec-2028 C75 on the bid ($50,740),
   Jan-2028 C100 at mid ($27,450), Jan-2027 C55 ×2 bid ($59,432), Jan-2027 C40 bid
   ($37,350). Nobody is paying up for multi-year ENPH upside; the LEAP call side is
   supply.

Net delta-notional of the greek-screener top-15, computed **unsigned** (raw
`Σ delta × size × 100`) = **−30,249 share-equivalents**. This is a *magnitude*
sanity check only — it does not net buyer against seller, since bid-side rows
represent the counterparty's exposure. At ~30k share-equivalents against a
**127.77M float** (`phase-0-intake.md`), the largest fifteen option prints of the
day carry delta worth **0.024% of float**. In dealer-hedging terms this is noise.

### IV outliers + Greeks

**All 15 IV-outlier contracts are the 2026-07-31 expiry** — the first weekly after
Wednesday's post-close print. Nothing else in the chain qualifies:

| Contract (all 2026-07-31) | avg IV | max IV | Vol | Premium |
|---|---|---|---|---|
| P35 | **1.724** | 1.788 | 50 | $8,227 |
| P36.5 | **1.721** | 1.791 | 70 | $16,009 |
| C36.5 | 1.716 | 1.830 | 70 | $19,694 |
| P36 | 1.711 | 1.786 | 71 | $15,759 |
| P37.5 | 1.709 | 1.740 | 67 | $17,309 |
| C37 | 1.706 | **1.862** | 84 | $21,845 |
| C39 | 1.691 | 1.769 | 144 | $25,874 |
| C38 | 1.687 | 1.791 | 128 | $28,678 |
| P34 | 1.686 | 1.781 | 89 | $10,323 |
| C40 | 1.679 | 1.748 | 214 | $32,941 |
| C52 | 1.660 | 1.745 | 128 | $1,010 |
| P32 | 1.654 | 1.797 | 53 | $3,450 |
| P30 | 1.643 | 1.773 | 259 | $7,663 |
| C51 | 1.634 | 1.825 | 167 | $2,134 |
| P28 | 1.617 | 1.759 | 71 | $888 |

- **Front-week IV is ~1.70 against `iv30d = 0.922` — a 1.85× event kink.** Phase-4
  owns whether that is rich or cheap, but note it resolves phase-0.5's open
  question about *falling* `iv30d`: 30-day IV is drifting down because the event
  premium is concentrating into one weekly expiry rather than lifting the whole
  surface. The event is **not** underpriced at the front; the 30-day number was
  simply the wrong place to look.
- **The ATM skew is flat-to-put-favoured**: P36.5 at 1.721 vs C36.5 at 1.716,
  P37.5 at 1.709 vs C37 at 1.706. Symmetric — the front week prices a **two-sided**
  event, not a directional one. This partially offsets the bearish tape read.
- Greeks confirm scale: top-15 by premium show `gamma` 0.008–0.026 and `vega`
  0.051–0.221 per contract. The largest vega line (Dec-2028 C75, v=0.221) is a
  **sold** LEAP — short vol at the very back of the curve while the front week
  trades 170%.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol ENPH --date 2026-07-27 --json` | `bullish_premium=1843847`, `bearish_premium=2102578`, **derived `net_flow`=−258731**, `call_premium=2171125`, `put_premium=2593624`, `call_volume=9693`, `put_volume=5306`, `put_call_ratio=0.5474053440627257`, `iv30d=0.922018992271469` ← `.uw_screener.*` | 1 (whole tape) |
| `uw options-flow sweeps --symbol ENPH --side ask --min-premium 100000 --top-n 25 --date 2026-07-27 --json` | 2 rows; `P40 2026-10-16 total_premium=176570 total_size=232`, `C35 2026-11-20 total_premium=105735` ← `.results[]` | 2 |
| `uw options-flow sweeps --symbol ENPH --side bid --min-premium 100000 --top-n 25 --date 2026-07-27 --json` | 3 rows; `P40 2027-06-17 =205860`, `P45 2027-06-17 =170725`, `C50 2026-12-18 =105081` ← `.results[]` | 3 |
| `uw options-flow unusual-volume --symbol ENPH --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-27 --json` | 7 rows; `P35.5 2026-08-07 vol_oi_ratio=108 total_premium=50753 trade_count=97`; `C60 2026-10-16 vol_oi_ratio=30.06 total_premium=68552` ← `.results[]` | 7 |
| `uw options-flow top-premium-trades --symbol ENPH --top-n 25 --date 2026-07-27 --json` | Σ premium **=1468329** ← `[.results[].premium]\|add`; side×type split ← `group_by(.side+"\|"+.option_type)`; top print `2026-11-20 P35 size=800 premium=464000 side="mid" delta=-0.3451` ← `.results[0]` | 25 |
| `uw options-flow iv-outliers --symbol ENPH --top-n 15 --date 2026-07-27 --json` | all 15 `expiry=2026-07-31`; `avg_iv` range 1.617–1.724, `max_iv` to 1.8617 ← `.results[]` | 15 |
| `uw options-flow greek-screener --symbol ENPH --top-n 15 --sort-by premium --date 2026-07-27 --json` | Σ`delta×size×100` **=−30,249** ← `[.results[]\|.delta*.size*100]\|add`; `gamma` 0.008–0.026, `vega` 0.051–0.221 | 15 |
| `uw hot-chains smart-money-flow --direction bullish --top-n 10 --min-volume 500 --date 2026-07-27 --json` | ENPH **absent** ← `[.results[]\|select(.underlying_symbol=="ENPH")]` → `[]` | top-10 |
| `uw hot-chains smart-money-flow --direction bearish --top-n 10 --min-volume 500 --date 2026-07-27 --json` | ENPH **absent** ← same path → `[]` | top-10 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol ENPH --json` | **`consistency_score=1`, `dominant_direction="bearish"`, `sessions_in_top=5`, `total_sweep_premium=1335255`**, `dates_covered=[2026-07-27,07-24,07-23,07-22,07-21]` ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-07-27 --json` | ENPH **absent** ← `[.results[]\|select(.underlying_symbol=="ENPH")]` → `[]` | top-15 |
| DuckDB `§A` ask/bid split over `stock-screener-*.parquet` (6 sessions) | `call_ask_share=0.475`, `put_ask_share=0.584`, `net_aggr_dir=−1130` (2026-07-27); `call_ask_share<0.50` in **6 of 6** sessions ← `call_volume_ask_side` / `call_volume_bid_side` / `put_volume_ask_side` / `put_volume_bid_side` | 6 |

## Tool errors

None. Every command exited 0 and every value round-tripped through `jq` or DuckDB.

Two **empty-result** outcomes recorded as findings, not errors, per the phase's
composition guidance:

- `hot-chains smart-money-flow` (both directions): **no smart-money flow detected
  for ENPH on this date.** Per instruction, *not* re-called with looser thresholds.
- `hot-chains sweep-ratio`: ENPH outside the market-wide top-15.

Both are consistent with `phase-0.5-context.md`, where ENPH was outside the top-50
on all five screener metrics.

## DATA NOTE / CORRECTION

- **`net_flow` was derived, not read.** `insights deep-dive .uw_screener` has no
  `net_flow` key (`lib/uw-json-paths.md` phantom-field trap #1). Written value
  −$258,731 = `bullish_premium − bearish_premium`. Independently confirmed against
  the screener parquet's `net_call_premium − net_put_premium` = −$258,731 in
  `phase-0.5-context.md` — **exact match**, so the derivation is sound for this row.
- **`sweep-persistence` takes no `--date`.** It is a trailing, latest-anchored tool
  (memory: `uw-cli-mcp-parity`). Its `dates_covered` array was read explicitly and
  confirmed to end on **2026-07-27**, so the 5-session window is correctly anchored
  to the as-of date and no stale-window substitution occurred.
- **The −30,249 delta figure is unsigned.** It sums `delta × size × 100` across the
  top-15 without netting buyer against seller (bid-side rows are the counterparty's
  exposure). It is reported as a magnitude bound only and must not be cited as
  "net dealer delta". Phase-3/4 own real positioning.
- No value written here was corrected after first read.

## Verdict for downstream phases

- **Bias from this phase:** **bearish**
- **Conviction:** **3 / 5** — and the split matters. Direction is well-corroborated
  across four independent reads (sweep persistence 5/5 sessions, whole-tape ask/bid
  in 5 of 6 sessions, ask-side top prints 4:1 puts, deep-ITM put buying).
  **Magnitude is negligible** (−$258,731 net on a $4.84B cap; top-15 delta = 0.024%
  of float). High-confidence direction, near-zero force.
  **Hard cap applied:** `[CTX:] BUSY_NAME_NORMAL_DAY` ⇒ this phase contributes at
  most **`+`**, never `++`, to phase-10 confluence (`rubrics/confluence-scoring.md`).
- **Three datapoints later phases must remember:**
  1. **`consistency_score = 1` / `dominant_direction = "bearish"` / `sessions_in_top = 5`
     of 5 / `total_sweep_premium = $1,335,255`** [FLOW:sweep_persistence] — the only
     signal here strong enough to carry into phase 9. It says the bearish tape is a
     *campaign*, not a one-day print.
  2. **`put_call_ratio = 0.547` is a bull trap.** Calls outnumber puts 9,693 : 5,306
     by volume, but `call_ask_share = 0.475` — the calls are being **sold**. Put
     premium ($2.59M) exceeds call premium ($2.17M) and `put_ask_share = 0.584`.
     Never cite the P/C ratio downstream without this overlay.
  3. **All event risk is priced in one expiry: 2026-07-31 at ~1.70 IV vs
     `iv30d = 0.922`, and the front-week skew is flat** (P36.5 1.721 vs C36.5 1.716).
     The market prices a large **two-sided** move, not a directional one — which
     directly contradicts the tape's one-way bearish lean and is the central
     tension phase-8b must adjudicate.
- **Open questions:**
  - Is the dark pool confirming the bearish option tape, or absorbing supply?
    Specifically: is there an **offsetting block buy** behind the $210k of deep-ITM
    put purchases (which would reclassify them as conversion/hedge rather than
    synthetic short)? → **phase-2**
  - The 800-lot Nov-20 $35 put at **mid** ($464,000, 9.7% of the day's premium) is
    directionally unattributable. Does OI change on 2026-07-28 reveal it as opening
    or closing? → **phase-3** (`oi biggest-increases`)
  - Protection is being **rolled from Jun-2027 into Oct-2026** (sold $205,860 +
    $170,725 in Jun'27 puts, bought $176,570 of Oct'26 P40). Does phase-3's
    `term-structure` show OI actually migrating to the Oct expiry, confirming a
    genuine hedge-tenor shift rather than two unrelated prints? → **phase-3**
  - Front-week IV ~170% with a flat skew, against a persistently bearish tape —
    does `vrp` / `iv-percentile-zscore` say the event is fairly priced? → **phase-4/5**
