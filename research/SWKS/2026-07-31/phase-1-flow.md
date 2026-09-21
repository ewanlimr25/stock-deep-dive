# Phase 1 — Options Flow

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`

## Summary

SWKS's 2026-07-31 tape is a **premium-selling tape, not a directional one**. On the
whole tape both sides were hit on the bid — the call ask-share was **0.175** (172
ask vs 811 bid contracts) and the put ask-share was **0.088** (312 ask vs 3,245
bid) — and both net-premium fields are negative (`net_call_premium` **−$170,899**,
`net_put_premium` **−$214,781**), which is the signature of net option *supply*,
not demand. The headline "net bullish +$43,882" is almost entirely an artifact of
UW classifying **sold puts as bullish premium**: a single opening block of **3,333
Aug-21 52.5-strike puts (vol/OI 3.52×, $219,979 premium, sold on the bid)** is 25%
of the day's $877,883 and 90% of all Aug-21 put volume. Direction is therefore
**mixed/neutral with a soft downside marker at 52.5**, and conviction is **low** —
the phase-0.5 `unusual_verdict: QUIET` cap applies, the day's largest print is only
$173,030, and `hot-chains sweep-persistence` reports SWKS's **dominant 5-session
sweep direction as bearish** (consistency 0.4, 2 of 5 sessions, $9.72M — dominated
by the 2026-07-29 earnings reaction).

## Key signals

- **Whole-tape net premium is negative on BOTH legs** — `net_call_premium`
  **−$170,899**, `net_put_premium` **−$214,781**. Net option seller's tape.
  `[FLOW:screener DUCKDB]`
- **Put ask-share 0.088 / call ask-share 0.175** — 88.9% of the day's put contracts
  and 82.5% of call contracts traded on the **bid**. `[FLOW:screener DUCKDB]`
- **One trade is the day:** Aug-21 **52.5 put**, volume **3,333** vs open interest
  **947** = **3.52× vol/OI (opening)**, **$219,979** premium, avg IV 0.633 — of
  which **$173,159 / 2,664 contracts / 3 trades executed as a bid-side sweep**.
  Someone **sold** ~3,300 puts 15.7% below spot. `[FLOW:unusual_volume]` `[FLOW:sweeps]`
- **Calls were sold too** — a Sep-18 **62.5/65 bear call spread** (68 lots: 62.5C
  sold on the bid @5.55, 65C bought on the ask @4.49, net credit ~$1.06 × 68 =
  **$7,208**), **110 Jan-2027 85 calls sold on the bid** (~$39,250), and deep-ITM
  55 calls sold (delta 0.76–0.84). Upside is being monetized, not bought.
  `[FLOW:top_premium_trades]`
- **Zero 0DTE, zero weeklies** — `share_0dte = 0`, `share_weeklies = 0`,
  `share_monthlies = 0.759`, `share_leaps = 0.015`, `regime_hint = INSTITUTIONAL`.
  None of this premium is pin-noise; the top-25 covers **60.5%** of the whole
  tape. `[FLOW:dte_volume_share]`
- **Ask-side sweeps: zero.** `sweeps --side ask --min-premium 100000` returned
  **0 rows**; the bid side returned exactly **1**. No aggressive buyer anywhere on
  the tape. `[FLOW:sweeps]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

From `uw insights deep-dive --symbol SWKS --date 2026-07-31` → `.uw_screener`:

| Field | Value |
|---|---|
| `call_premium` | **$380,703** |
| `put_premium` | **$497,180** |
| `bullish_premium` | **$376,945** |
| `bearish_premium` | **$333,063** |
| **derived `net_flow` = bullish − bearish** | **+$43,882** |
| `call_volume` | **1,080** |
| `put_volume` | **4,384** |
| `put_call_ratio` | **4.0593** |
| `iv_rank` | **52.8977** |
| `iv30d` | **0.559032** |
| `implied_move` / `implied_move_perc` | **$5.6749 / 9.098%** |
| `total_open_interest` | **118,470** |

**Total tape = $877,883.** The top-25 premium prints sum to **$531,547 = 60.5%**,
so unlike the pathological case the phase prompt warns about, the top-N here *is*
broadly representative — but it is representative of **selling**, not buying:

| Top-25 split | Count | Premium |
|---|---|---|
| **bid** (seller-initiated) | 15 | **$339,295 (63.8%)** |
| mid | 6 | $133,800 (25.2%) |
| **ask** (buyer-initiated) | 4 | **$58,452 (11.0%)** |
| calls | 13 | $199,172 (339 contracts) |
| puts | 12 | $332,375 (3,637 contracts) |

**Whole-tape ask/bid split** (screener parquet, the fields the `uw_screener` block
does not carry) — last 5 sessions, so the as-of day is read in context:

| Date | Call vol | ask / bid | **call ask-share** | Put vol | ask / bid | **put ask-share** | `net_call_premium` | `net_put_premium` |
|---|---|---|---|---|---|---|---|---|
| 2026-07-27 | 788 | 405 / 267 | 0.603 | 322 | 213 / 96 | 0.689 | +$48,664 | +$77,973 |
| 2026-07-28 *(earnings PM)* | 2,235 | 740 / 1,250 | 0.372 | 1,402 | 463 / 828 | 0.359 | −$135,380 | −$170,894 |
| **2026-07-29 *(−5.40% reaction)*** | 8,387 | 3,086 / 4,816 | 0.391 | 5,513 | 2,786 / 1,491 | **0.651** | **−$3,338,495** | **+$1,471,139** |
| 2026-07-30 | 427 | 155 / 241 | 0.391 | 466 | 254 / 152 | 0.626 | −$33,434 | +$34,029 |
| **2026-07-31 (as-of)** | 1,080 | 172 / 811 | **0.175** | 4,384 | 312 / 3,245 | **0.088** | **−$170,899** | **−$214,781** |

The regime **flipped** between the reaction day and the as-of day. On 2026-07-29
the tape was textbook bearish — puts *bought* (ask-share 0.651, `net_put_premium`
**+$1.47M**) and calls *sold* (`net_call_premium` **−$3.34M**), producing the
window's only large net-bearish print (**−$4.81M**, see
`phase-0.5-context.md §Event context`). By 2026-07-31 the puts that were bought
into the event are being **supplied back**: put ask-share collapsed 0.651 → 0.088
and `net_put_premium` flipped +$1.47M → −$214,781. That is the shape of
**post-event de-hedging plus fresh premium selling into crushed vol** (`iv30d`
0.574 → 0.559, IV rank 62.6 → 52.9; only the **29.9th percentile of SWKS's own
78-session history**, `phase-0.5-context.md §Self-history`).

### Sweeps (ask vs bid, persistence)

| Side | Rows (≥$100k) | Detail |
|---|---|---|
| **ask** | **0** | No aggressive buying anywhere on the tape at the $100k threshold. |
| **bid** | **1** | put · strike **52.5** · expiry **2026-08-21** · `total_premium` **$173,159** · `total_size` **2,664** · `trade_count` **3** · `avg_price` **0.6467** |

`uw hot-chains sweep-persistence --days 5 --symbol SWKS`:

```
ticker=SWKS  sessions_in_top=2  consistency_score=0.4
dominant_direction=bearish  total_sweep_premium=9,716,085
```

SWKS appears in top sweep activity on only **2 of the last 5 sessions**, and the
**dominant direction over the window is bearish** — but note that the $9.72M
five-day sweep premium is overwhelmingly the 2026-07-29 earnings reaction, when
$14.92M of total premium printed against $877,883 on the as-of day. **The
persistence signal is describing the event, not the current tape.** With
`consistency_score = 0.4` there is no multi-day campaign here.

`uw hot-chains smart-money-flow` (market-wide, `--min-volume 500`): SWKS is
**absent from both the bullish and the bearish top-10**. No smart-money flow
detected on this date — per the phase prompt, not re-run with looser thresholds.
For scale, the #1 bullish row (SPCX Aug-07 330C) carried **$11,566,480** of
premium — 13× SWKS's entire day.

`uw hot-chains sweep-ratio --min-volume 500 --min-sweep-ratio 0.3`: **no SWKS
rows** in the top-15.

### New positioning (unusual volume, vol/OI)

`uw options-flow unusual-volume --symbol SWKS --min-vol-oi-ratio 3` — **1 row**:

| Field | Value |
|---|---|
| `option_type` / `strike` / `expiry` | **put / 52.5 / 2026-08-21** |
| `total_volume` | **3,333** |
| `open_interest` | **947** |
| **`vol_oi_ratio`** | **3.5195** |
| `total_premium` | **$219,979** |
| `trade_count` | **7** |
| `avg_iv` | **0.6327** |

This is the **only** contract on the SWKS board opening in size, and it accounts
for **90.0%** of all Aug-21 put volume (3,333 of 3,702) and **76.0%** of the day's
entire put volume (3,333 of 4,384).

> **Correction to phase 0.** `phase-0-intake.md §Ticker sanity` recorded
> `unusual-volume` as **empty** and inferred "thin *new-position* activity". That
> empty result came from the command's **default** `--min-vol-oi-ratio`, not from
> an absence of new positioning. At the phase-prescribed threshold of 3 the screen
> **does** return a row. The phase-0 open question *"is SWKS flow closing/rolling
> rather than opening?"* is answered: **there is exactly one genuinely opening
> position, and it is short puts.** See `## DATA NOTE / CORRECTION`.

**Direction of the opening position.** The block traded on the **bid**
(`sweeps --side bid`, `side: "bid"` on the largest print), i.e. **seller-initiated
— the aggressor sold**. Opening + sold ⇒ **short puts opened**, not long puts. At
strike 52.5 against a $61.48 underlying at execution, that is **15.7% below spot**
and **1.1% above the 52-week low of $51.93** (`phase-0.5-context.md`). Read
plainly: someone took in ~$220k to be a buyer of SWKS at $52.50 through Aug-21,
right on top of the annual low.

### Largest premium prints

`uw options-flow top-premium-trades --symbol SWKS --top-n 25` (all 25 rows; times UTC):

| Time (UTC) | Type | Strike | Expiry | Premium | Size | Price | Side | IV | Delta | Underlying |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:06:26 | put | 52.5 | 2026-08-21 | **$173,030** | 2,662 | 0.65 | **bid** | 0.634 | −0.130 | 61.48 |
| 14:06:26 | put | 52.5 | 2026-08-21 | $46,620 | 666 | 0.70 | mid | 0.650 | −0.135 | 61.48 |
| 13:34:26 | call | 77.5 | **2028-01-21** | $38,280 | 29 | 13.20 | mid | 0.560 | 0.544 | 62.32 |
| 13:30:19 | call | 62.5 | 2026-09-18 | $37,740 | 68 | 5.55 | **bid** | 0.580 | 0.557 | 62.655 |
| 13:30:19 | call | 65 | 2026-09-18 | $30,532 | 68 | 4.49 | **ask** | 0.590 | 0.484 | 62.655 |
| 15:10:38 | put | 47.5 | 2027-01-15 | $16,250 | 50 | 3.25 | mid | 0.610 | −0.188 | 61.71 |
| 15:10:38 | put | 47.5 | 2027-01-15 | $16,250 | 50 | 3.25 | mid | 0.610 | −0.188 | 61.71 |
| 15:10:38 | put | 45 | 2027-01-15 | $13,850 | 50 | 2.77 | bid | 0.630 | −0.161 | 61.71 |
| 15:10:38 | put | 45 | 2027-01-15 | $13,850 | 50 | 2.77 | bid | 0.630 | −0.161 | 61.71 |
| 16:30:53 | call | 55 | 2026-09-18 | $13,160 | 14 | 9.40 | bid | 0.570 | 0.760 | 62.06 |
| 19:57:24 | call | 85 | 2027-01-15 | $12,250 | 35 | 3.50 | bid | 0.560 | 0.284 | 62.46 |
| 19:57:08 | call | 85 | 2027-01-15 | $11,520 | 32 | 3.60 | bid | 0.570 | 0.288 | 62.495 |
| 16:29:06 | call | 55 | 2026-09-18 | $10,340 | 11 | 9.40 | bid | 0.580 | 0.758 | 62.025 |
| 14:03:30 | put | 55 | 2026-09-18 | $10,080 | 42 | 2.40 | bid | 0.580 | −0.272 | 60.805 |
| 16:28:31 | put | 65 | 2027-03-19 | $9,960 | 8 | 12.45 | ask | 0.600 | −0.424 | 61.985 |
| 16:28:31 | put | 65 | 2027-03-19 | $9,960 | 8 | 12.45 | ask | 0.600 | −0.424 | 61.985 |
| 19:57:08 | call | 85 | 2027-01-15 | $8,280 | 23 | 3.60 | bid | 0.570 | 0.288 | 62.51 |
| 16:28:31 | put | 70 | 2026-09-18 | $8,200 | 8 | 10.25 | mid | 0.590 | −0.669 | 61.985 |
| 16:28:31 | put | 70 | 2026-09-18 | $8,200 | 8 | 10.25 | mid | 0.590 | −0.669 | 61.985 |
| 17:53:40 | call | 55 | 2026-08-21 | $8,100 | 10 | 8.10 | bid | 0.580 | 0.832 | 62.1501 |
| 17:58:15 | call | 55 | 2026-08-21 | $8,100 | 10 | 8.10 | bid | 0.570 | 0.839 | 62.215 |
| 17:50:42 | call | 55 | 2026-08-21 | $8,000 | 10 | 8.00 | ask | 0.570 | 0.836 | 62.10 |
| 19:57:09 | call | 85 | 2027-01-15 | $7,200 | 20 | 3.60 | bid | 0.570 | 0.288 | 62.48 |
| 14:07:12 | put | 52.5 | 2026-09-18 | $6,125 | 35 | 1.75 | bid | 0.630 | −0.198 | 61.835 |
| 16:40:51 | call | 60 | 2026-09-18 | $5,670 | 9 | 6.30 | bid | 0.560 | 0.618 | 62.16 |

Four structures are legible inside this list:

1. **The 52.5P Aug block (14:06:26)** — $173,030 bid + $46,620 mid = **$219,650**
   across 3,328 contracts in one second. Sold. This is the trade of the day.
2. **A Sep-18 62.5/65 bear call spread (13:30:19)** — identical 68-lot size, same
   timestamp, 62.5C hit the **bid** and 65C lifted the **ask**. Selling the lower
   strike and buying the higher is a **credit call spread** (or a long call rolled
   *up* into lower delta). Either reading caps upside; neither is fresh call buying.
3. **Jan-2027 85 calls sold on the bid (19:57:08–19:57:24)** — 35 + 32 + 23 + 20 =
   **110 contracts, ~$39,250**, all bid-side, delta 0.284–0.288. Overwriting the
   36%-OTM upside into year-end 2027.
4. **Deep-ITM 55 calls sold (delta 0.76–0.84)** across Aug-21 and Sep-18 —
   ~$39,700 across 45 contracts, 4 of 5 on the bid. Monetizing existing long delta.

The only unambiguous **buying** in the whole top-25 is the 65C Sep leg ($30,532,
part of the spread above), the 2027-03-19 65 puts (2 × $9,960 on the **ask** —
in-the-money protective puts, 16 contracts, small), and one 10-lot 55C. Total
ask-side premium across all 25 prints: **$58,452**.

### IV outliers + Greeks

`uw options-flow iv-outliers --symbol SWKS --top-n 15` → **0 rows**. This is a
correct empty, not a failure: the command's default `--min-iv` is **1.0 (100% IV)**
and SWKS's richest contract on the day printed at **IV 0.650**. The whole surface
sits in a 0.56–0.65 band; there is **no vol outlier on the board**, consistent with
`iv30d = 0.559` and a post-event IV rank at the 29.9th self-percentile.

`uw options-flow greek-screener --symbol SWKS --top-n 15 --sort-by premium`
(15 rows, same prints as above). Aggregate **contract**-Greeks across those 15
(Σ greek × size × 100, unsigned by side):

| Aggregate | Value |
|---|---|
| Σ delta-notional | **−35,993 share-equivalents** |
| Σ vega | **+16,287** per vol-point |
| Σ gamma | **+8,416** |

The −36.0k delta is **the delta of the contracts traded, not of anyone's
position** — and it is 96% just the 52.5P block (−0.1297 × 2,662 × 100 = −34,526).
Because the aggressor **sold** that block, the **aggressor is long ≈ +34.5k
deltas** and the counterparty (likely a market maker) is short them. Read
directionally, the initiating side of the day's dominant trade took the **long**
side of SWKS delta while simultaneously being **short ~16.3k of vega** — long
underlying, short volatility. That is a "range-bound-to-higher, vol stays crushed"
expression, and it is the single most informative thing on this tape.

### Tenor composition

`uw options-flow dte-volume-share --symbol SWKS`:

```
share_0dte      = 0
share_weeklies  = 0
share_monthlies = 0.759
share_leaps     = 0.015
regime_hint     = INSTITUTIONAL
```

`uw options-flow expiry-heatmap --symbol SWKS` (sums to $877,883 = the whole tape,
so this is complete, not top-N):

| Expiry | Total premium | Call prem | Put prem | Call vol | Put vol |
|---|---|---|---|---|---|
| **2026-08-21** | **$343,247** | $74,441 | **$268,806** | 446 | **3,702** |
| **2026-09-18** | **$289,310** | **$188,532** | $100,778 | 435 | 386 |
| 2027-01-15 | $117,443 | $48,273 | $69,170 | 134 | 214 |
| 2026-11-20 | $43,492 | $27,618 | $15,874 | 32 | 32 |
| 2028-01-21 | $41,520 | $40,810 | $710 | 31 | 1 |
| 2027-03-19 | $40,437 | $0 | $40,437 | 0 | 47 |
| 2026-12-18 | $1,379 | $1,029 | $350 | 2 | 1 |
| 2027-02-19 | $1,055 | $0 | $1,055 | 0 | 1 |

**No 0DTE and no weeklies at all** — the phase's standard "discount for 0DTE
inflation" pitfall does not apply here; nothing needs to be discounted for pin
noise. The tape is a clean two-expiry story: **Aug-21 is the put story** (78.3% of
its premium is puts, and 90% of that is the one sold 52.5 strike) and **Sep-18 is
the call story** (65.2% calls, dominated by the bear call spread and ITM call
sales). 1.5% LEAPs.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw insights deep-dive --symbol SWKS --date 2026-07-31 --json` | call_premium=380703, put_premium=497180, bullish_premium=376945, bearish_premium=333063, call_volume=1080, put_volume=4384, put_call_ratio=4.059259, iv_rank=52.8977, iv30d=0.559032, implied_move=5.674921, total_open_interest=118470 ← `.uw_screener.*`; **derived net_flow = 376945 − 333063 = +43882** (no `net_flow` key in this block) | whole tape |
| `uw options-flow sweeps --symbol SWKS --side ask --min-premium 100000 --top-n 25 --date 2026-07-31 --json` | **0** ← `.results\|length` | top-25 (empty) |
| `uw options-flow sweeps --symbol SWKS --side bid --min-premium 100000 --top-n 25 --date 2026-07-31 --json` | 1 row ← `.results\|length`; total_premium=173159, total_size=2664, trade_count=3, strike=52.5, expiry=2026-08-21, avg_price=0.6466667, side=`bid` ← `.results[0]` | top-25 |
| `uw options-flow unusual-volume --symbol SWKS --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-31 --json` | 1 row; total_volume=3333, open_interest=947, **vol_oi_ratio=3.519535**, total_premium=219979, trade_count=7, avg_iv=0.6326847 ← `.results[0]` | top-25 |
| `uw options-flow top-premium-trades --symbol SWKS --top-n 25 --date 2026-07-31 --json` | Σpremium=531547 ← `[.results[].premium]\|add`; bid n=15/$339295, ask n=4/$58452, mid n=6/$133800 ← `group_by(.side)`; call n=13/$199172/339ct, put n=12/$332375/3637ct ← `group_by(.option_type)` | top-25 |
| `uw options-flow iv-outliers --symbol SWKS --top-n 15 --date 2026-07-31 --json` | **0** ← `.results\|length` (default `--min-iv 1.0`; max observed IV 0.650) | top-15 (empty) |
| `uw options-flow greek-screener --symbol SWKS --top-n 15 --sort-by premium --date 2026-07-31 --json` | Σ(delta×size×100)=−35993, Σ(vega×size×100)=+16287, Σ(gamma×size×100)=+8416 ← `[.results[]\|.delta*.size*100]\|add` etc. | top-15 |
| `uw options-flow dte-volume-share --symbol SWKS --date 2026-07-31 --json` | share_0dte=0, share_weeklies=0, share_monthlies=0.759, share_leaps=0.015, regime_hint=`INSTITUTIONAL` ← `.share_*`, `.regime_hint` | whole tape |
| `uw options-flow expiry-heatmap --symbol SWKS --date 2026-07-31 --json` | Aug-21 total=343247 (put 268806 / call 74441, put vol 3702); Sep-18 total=289310 (call 188532 / put 100778) ← `.results[].total`, `.total_premium_put`, `.total_volume_put`; Σ totals = 877883 = whole tape | all 8 expiries |
| `uw hot-chains smart-money-flow --direction bullish --top-n 10 --min-volume 500 --date 2026-07-31 --json` | SWKS **absent** ← `[.results[]\|select(.underlying_symbol=="SWKS" or .ticker=="SWKS")]` = `[]`; #1 row premium=11566480 (SPCX260807C00330000) ← `.results[0].premium` | top-10 |
| `uw hot-chains smart-money-flow --direction bearish --top-n 10 --min-volume 500 --date 2026-07-31 --json` | SWKS **absent** ← same filter = `[]` | top-10 |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol SWKS --json` *(no `--date` flag on this leaf)* | ticker=SWKS, sessions_in_top=2, consistency_score=0.4, dominant_direction=`bearish`, total_sweep_premium=9716085 ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-07-31 --json` | SWKS **absent** ← `[.results[]\|select((.option_symbol//"")\|startswith("SWKS"))]` = `[]`; 15 rows total | top-15 |
| DuckDB `stock-screener-*.parquet`, ticker=SWKS, date≥2026-07-23 | 2026-07-31: call_volume_ask_side=172, call_volume_bid_side=811 ⇒ call_ask_share=**0.175**; put_volume_ask_side=312, put_volume_bid_side=3245 ⇒ put_ask_share=**0.088**; net_call_premium=−170899, net_put_premium=−214781. 2026-07-29: put_ask_share=0.651, net_call_premium=−3338495, net_put_premium=+1471139 `[FLOW:ask_bid_split DUCKDB]` | 5 sessions |

## Tool errors

- `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol SWKS --date 2026-07-31 --json`
  → **`Error: unknown flag: --date`** (verbatim; `jq` consequently failed with
  `parse error: Invalid numeric literal at line 1, column 6`). This leaf exposes
  **no `--date` flag** — confirmed against `--help`, whose only flags are `--days`,
  `--symbol`, `--top-n`. Re-run without `--date` succeeded. **As-of safety:** the
  leaf anchors to the latest available date, which `phase-0-intake.md §UW
  availability` established **is** 2026-07-31 across all five datasets, so the
  5-session window it scanned is 2026-07-27 → 2026-07-31 and is as-of-consistent
  on this run. No value was transcribed from the failed call.

No other tool errors. The two empty results (`sweeps --side ask`, `iv-outliers`)
are **valid empties** attributable to explicit thresholds ($100k premium floor and
the default 100% IV floor respectively), not failures.

## DATA NOTE / CORRECTION

1. **Correcting `phase-0-intake.md`.** Phase 0 ran
   `uw options-flow unusual-volume --symbol SWKS --top-n 1` at the command's
   **default** vol/OI threshold, got `[]`, and recorded "thin *new-position*
   options activity", carrying an open question about whether SWKS flow was
   closing/rolling rather than opening. Re-read at the phase-1-prescribed
   `--min-vol-oi-ratio 3`, the screen returns **one row: Aug-21 52.5P,
   vol_oi_ratio 3.5195**. **Corrected value: there IS an opening position, and it
   is short puts.** Verified against `jq '.results[0]'` on validated JSON. The
   phase-0 inference is superseded; the phase-0 *observation* (empty at default
   threshold) stands and is itself informative — nothing else on the board opens
   in size.
2. **`net_flow` derived, not read.** The `insights deep-dive` `uw_screener` block
   has **no `net_flow` field** (`lib/uw-json-paths.md` phantom-field trap #1).
   Value **+$43,882** was derived as `bullish_premium − bearish_premium` and
   independently cross-checked against the parquet's
   `net_call_premium − net_put_premium` = −170899 − (−214781) = **+43,882** —
   exact agreement.
3. **Ask/bid split is not in the `uw_screener` block.** As the phase prompt warns,
   that block carries `call_volume`/`put_volume` only. The whole-tape ask-vs-bid
   figures quoted above come from the screener parquet's
   `call_volume_ask_side` / `call_volume_bid_side` / `put_volume_ask_side` /
   `put_volume_bid_side` columns via DuckDB and are tagged
   `[FLOW:ask_bid_split DUCKDB]`. They are *not* inferred from the top-25.
4. The Σ delta/vega/gamma figures are **unsigned contract Greeks** (greek × size ×
   100), summed without applying trade side. They are labelled as such in the text
   and the directional interpretation applies the side explicitly rather than
   reading a sign off the sum.

## Verdict for downstream phases

- **Net bias from this phase:** **MIXED, tilted neutral-constructive with a defined
  downside marker — NOT bullish.** The nominal `+$43,882` net-bullish print is real
  but is produced by *put selling* being classified as bullish premium; calls were
  sold on the same tape (call ask-share 0.175, bear call spread, 110 sold Jan-27
  85Cs, ITM call sales). The honest summary is: **the initiating flow is long delta
  and short vol, with upside capped and a floor sold at 52.5.**
- **Conviction:** **2 / 5.** Justification: (a) `phase-0.5-context.md` returned
  `unusual_verdict: QUIET` — total premium $877,883, option volume **1.00×** the
  name's own 30-day average, rank 565/4,499 on net direction; (b) the entire
  directional read rests on **one $219,979 trade**; (c) `sweep-persistence`
  `consistency_score = 0.4` with `dominant_direction = bearish` gives **no**
  multi-session confirmation; (d) SWKS is absent from every market-wide
  smart-money and sweep-ratio screen. The phases-1–2 confluence cap from a
  non-`GENUINELY_UNUSUAL` context verdict applies.
- **Three datapoints later phases must remember:**
  1. **Short 3,333 Aug-21 52.5 puts, opened (vol/OI 3.52×), sold on the bid,
     $219,979.** Strike 52.5 sits **1.1% above the 52-week low of $51.93**. This is
     the tape's only real position and it marks a **defended level at $52.50 into
     2026-08-21**. Phase 3 must check whether OI confirms it survives, and phase 9
     should treat 52.5 as a flow-anchored floor rather than an arbitrary stop.
  2. **The whole tape is net short premium on both legs** (`net_call_premium`
     **−$170,899**, `net_put_premium` **−$214,781**; call ask-share 0.175, put
     ask-share 0.088) into an IV rank of 52.9 that is only the **29.9th percentile
     of SWKS's own history**. Sellers are supplying already-cheap vol. For phase 9
     that argues **structurally for owning optionality rather than selling it** —
     the crowd is on the other side of that trade.
  3. **Upside is being monetized, not bought.** Sep-18 62.5/65 credit call spread
     (68 lots), 110 Jan-27 85Cs sold on the bid, deep-ITM 55Cs sold. Combined with
     `expiry-heatmap` showing Sep-18 at 65.2% calls, the flow says **capped**, and
     any phase-9 upside target above ~$65 lacks flow support from this tape.
- **Open questions:**
  - **Is the dark pool confirming or contradicting?** The as-of tape is a single
    seller's footprint on $878k of premium. Phase 2 must say whether real shares
    were being accumulated on 2026-07-30/31 (which would corroborate the long-delta
    read) or distributed (which would make the put sale pure premium harvesting).
    Mind the closing-auction artifact when tiering the prints.
  - **Did the 52.5P short survive to become open interest?** Put OI moved only
    42,612 → 43,164 (+552) between 2026-07-30 and 2026-07-31 while 3,333 contracts
    printed at one strike — a **large discrepancy**. Phase 3 owns this: either much
    of the block was intraday-offset, or the OI print lags. Until resolved, the
    "defended $52.50" read is provisional.
  - **Does the AAPL −7.35% shock (`phase-0.5-context.md`) get expressed in SWKS
    options at all?** This tape shows **no** hedge demand on the day AAPL broke —
    put ask-share fell to 0.088. That is either genuine confidence or dangerous
    complacency, and phases 6 and 8 must adjudicate it.
