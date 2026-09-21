# Phase 1 — Options Flow

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`

## Summary

**The tape is not bearish — and phase-0.5's headline needs correcting.** The
screener's "bottom 1.2 percentile net-directional" reading is an artifact of a
classification gap: UW's `bullish_premium`/`bearish_premium` **exclude every
`mid` and `no_side` print**, which today amounts to **$2,545,750 — 9.5% of
FSLR's $26.66M total premium** — including the single largest new position of
the day. Reconstructed from the raw tape, **net customer delta notional is
+$10.73M (net long)**, not negative.

The day has exactly two stories. First, a **1,900-lot cross of Aug-21 $230
calls, $1.805M, printed at the offer** (`price 9.50 = nbbo_ask 9.50`,
`pos_in_spread = 1.000`) against an open interest of just **255** — a 7.5×-OI
brand-new bullish position worth **+$15.2M in delta**. UW tagged it `no_side`
and dropped it from the directional math entirely. Second, a **LEAP holder
rolling up-and-out for a $1.37M net credit**, trimming roughly **−$3.7M** of
delta but staying long.

Every DTE bucket is call-weighted roughly 2:1, and put ask-side premium is
concentrated in **deep-ITM** strikes (320/280/260/255/252.5) with deltas of
−0.56 to −0.85 — synthetic/structural mechanics, not clean directional
bearishness. Conviction is capped by the fact that the bullish delta rests
overwhelmingly on **one cross print** whose true initiator cannot be proven.

## Key signals

- **1,900 Aug-21 $230 calls bought at the offer for $1.805M**, vol/OI = 7.6×
  (OI 255), delta 0.376 → **+$15.2M delta notional**, a new position
  `[FLOW:unusual_volume]` `[FLOW:top_premium_trades]`
- **UW's directional premium omits $2,545,750 (9.5% of the tape)** as
  `mid`/`no_side`; reconciled exactly — `bullish 10,872,218` and
  `bearish 13,246,889` reproduce UW's figures only when crosses are dropped
  `[FLOW:aggressor_ex0dte DUCKDB]`
- **Net customer delta notional +$10.73M long** (ask = buy, bid = sell,
  cross-at-ask = buy) — the tape's true directional footprint
  `[FLOW:delta_notional DUCKDB]`
- **LEAP roll for $1.37M net credit**: bought 1,000 Jan-28 $460C + 1,000
  Mar-27 $410C ($2.70M debit, 12:48:15 ET) / sold 1,000 Jan-28 $450C + 1,000
  Jun-27 $340C ($4.07M credit, 14:15:31 ET) `[FLOW:top_premium_trades]`
- **Sweep persistence 0.8 — FSLR in the top sweep names 4 of 5 sessions,
  $17.28M 5-day sweep premium, but `dominant_direction = "mixed"`**
  `[FLOW:sweep_persistence]`
- **All 15 IV outliers are 0DTE expiry-day artifacts** (IV 1.36–6.60,
  `max_iv` 18.34) — discarded as noise `[FLOW:iv_outliers]`

## Detailed findings

### Whole-tape aggregate (read the top-N against this)

From `uw insights deep-dive` `.uw_screener` — the whole tape, not the top-N:

| Field | Value |
|-------|------:|
| `call_premium` | $19,838,946 |
| `put_premium` | $6,825,911 |
| **Total premium** | **$26,664,857** |
| `bullish_premium` | $10,872,218 |
| `bearish_premium` | $13,246,889 |
| **Derived `net_flow` = bullish − bearish** | **−$2,374,671** |
| `call_volume` | 24,254 |
| `put_volume` | 6,770 |
| `put_call_ratio` | 0.2791 |
| `iv_rank` | 81.94 |
| `implied_move` / `implied_move_perc` | $1.611 / 0.7625% |
| `total_open_interest` | 577,414 |

Read naively this is bearish: −$2.37M net flow, bottom 1.2 percentile of
4,499 names per `phase-0.5-context.md`. **That read does not survive the raw
tape.**

#### The classification gap (why the aggregate misleads)

Reconstructing UW's own definition from the raw parquet reproduces its numbers
**exactly**:

| Reconstruction | Value | UW field | Match |
|----------------|------:|----------|:-----:|
| call@ask + put@bid | **10,872,218** | `bullish_premium` = 10,872,218 | ✓ exact |
| call@bid + put@ask | **13,246,889** | `bearish_premium` = 13,246,889 | ✓ exact |
| `mid` + `no_side` | **2,545,750** | *(not in any UW directional field)* | — |

So `bullish + bearish + unclassified` = $26,664,857 = total premium. UW's
directional math is computed on **90.5%** of the tape and silently drops the
other **9.5%** — which today contains the day's largest opening position.

Full aggressor split, all DTE:

| Type | Side | Trades | Contracts | Premium ($M) | Delta notional ($M) |
|------|------|-------:|----------:|-------------:|--------------------:|
| call | ask | 1,753 | 11,760 | 8.175 | +60.1 |
| call | bid | 1,771 | 9,646 | 9.268 | +59.3 |
| call | mid | 235 | 948 | 0.591 | +6.4 |
| **call** | **no_side** | **1** | **1,900** | **1.805** | **+15.2** |
| put | ask | 1,213 | 3,612 | 3.978 | −22.9 |
| put | bid | 1,046 | 2,935 | 2.698 | −17.7 |
| put | mid | 121 | 223 | 0.150 | −1.0 |

**Net customer delta notional = +$10.73M** (customer buys at ask, sells at bid,
cross-at-or-above-ask counted as a buy). Calls contribute +$16.0M; puts
−$5.2M. The tape is **modestly net long**, and the sign is opposite to
`net_flow`.

Excluding 0–1DTE (removing pin/expiry noise) the picture is unchanged in
direction: call ask $7.590M vs call bid $8.701M, put ask $3.705M vs put bid
$2.399M, with the $1.805M cross intact.

Premium by DTE bucket — **every bucket is ~2:1 call-weighted**:

| DTE bucket | Call ($M) | Put ($M) | Call:Put | Contracts (C/P) |
|-----------|----------:|---------:|---------:|-----------------|
| 0–1DTE | 1.344 | 0.579 | 2.3× | 4,889 / 2,123 |
| 2–7DTE | 1.317 | 0.696 | 1.9× | 2,478 / 1,229 |
| 8–45DTE | 4.991 | 2.361 | 2.1× | 9,494 / 1,814 |
| 46–180DTE | 4.660 | 2.040 | 2.3× | 3,217 / 1,283 |
| LEAP | 7.527 | 1.151 | **6.5×** | 4,176 / 321 |

0DTE is only **$1.92M = 7.2%** of premium — modest, so the tape is not
0DTE-inflated. **LEAP is the heaviest bucket at $8.68M (32.6% of all
premium)**, driven by the roll below; per the standing pitfall, LEAP flow is
institutional but slow — high conviction, low short-term tradeability.

### The two structural packages

Both resolved from raw-tape timestamps (microsecond-identical execution =
one package):

**Package A — 12:48:15.314407 ET, exchange XISX, BUY (debit $2.700M)**

| Leg | Side | Price | Size | Premium | OI | pos_in_spread | Delta |
|-----|------|------:|-----:|--------:|---:|--------------:|------:|
| Jan-2028 $460 C | ask | 19.10 | 1,000 | $1,910,000 | 4,311 | 0.672 | 0.275 |
| Mar-2027 $410 C | ask | 7.90 | 1,000 | $790,000 | 2,562 | 0.513 | 0.168 |

**Package B — 14:15:31.093066 ET, exchange XPHO, SELL (credit $4.074M)**

| Leg | Side | Price | Size | Premium | OI | pos_in_spread | Delta |
|-----|------|------:|-----:|--------:|---:|--------------:|------:|
| Jan-2028 $450 C | bid | 19.87 | 1,000 | $1,987,000 | **671** | 0.498 | 0.285 |
| Jun-2027 $340 C | bid | 20.87 | 1,000 | $2,087,000 | 1,807 | 0.498 | 0.333 |

**Net effect: +$1.374M cash taken in, ≈−$3.7M delta shed.** Delta notional
sold (450C $6.09M + 340C $7.12M = $13.21M) exceeds delta bought (460C $5.88M +
410C $3.59M = $9.47M).

Three qualifications that matter:

1. **Package B printed at `pos_in_spread` 0.498 — dead mid-market**, despite
   UW labelling both legs `bid`. Calling this "aggressive selling" overstates
   it; these are negotiated package prints. The `bid` tag is what pushes
   $4.07M into `bearish_premium` and drives the bottom-1.2-percentile reading.
2. **Jan-28 $450C OI is only 671 against a 1,000-lot sale** — at least 329
   contracts are a *newly opened short*, not a close. The rest of the package
   is consistent with closing (340C sold 1,000 of 1,807 OI).
3. Direction of travel is **up and out in strike, shorter in tenor**
   (340→410/460, Jun-27→Mar-27/Jan-28): a holder monetising gains and
   retaining cheaper, further-OTM upside. **A trim, not a reversal** — this
   desk is still long ~44,300 delta-shares of calls after the roll.

### New positioning (unusual volume, vol/OI ≥ 3)

11 contracts qualified. Ranked by significance rather than raw ratio:

| Type | Strike | Expiry | Volume | OI | Vol/OI | Premium | IV |
|------|-------:|--------|-------:|---:|-------:|--------:|---:|
| **CALL** | **230** | **2026-08-21** | **1,937** | **255** | **7.60** | **$1,839,371** | 0.775 |
| CALL | 210 | 2026-08-07 | 643 | 104 | 6.18 | $573,601 | 0.742 |
| CALL | 240 | 2026-08-07 | 364 | 28 | 13.00 | $64,566 | 0.736 |
| PUT | 185 | 2026-08-28 | 187 | 19 | 9.84 | $139,325 | 0.761 |
| CALL | 250 | 2026-09-04 | 106 | 10 | 10.60 | $90,555 | 0.754 |
| CALL | 237.5 | 2026-08-07 | 152 | 8 | 19.00 | $24,143 | 0.761 |
| PUT | 195 | 2026-08-07 | 187 | 56 | 3.34 | $40,290 | 0.739 |
| PUT | 190 | 2026-08-07 | 147 | 42 | 3.50 | $20,015 | 0.737 |
| PUT | 212.5 | 2026-07-31 | 286 | 37 | 7.73 | $137,080 | 1.453 † |
| PUT | 207.5 | 2026-07-31 | 148 | 41 | 3.61 | $34,024 | 1.444 † |
| CALL | 220 | 2026-07-31 | 1,050 | 349 | 3.01 | $45,986 | 1.358 † |

† 0DTE — discount entirely.

**New-position premium is overwhelmingly upside**: $2.59M across new call
strikes vs $0.20M across new (non-0DTE) put strikes — **13:1**. The strikes
cluster at **210 / 230 / 237.5 / 240 / 250** in Aug–Sep, i.e. **0% to +18%
above the 211.03 close**.

#### Resolving the $1.805M cross

The single most important print of the day carried `side = no_side`, so it was
adjudicated on the raw tape:

```
executed_at 2026-07-31 12:11:46.663402-04:00   exchange XPHO
price 9.50   nbbo_bid 8.05   nbbo_ask 9.50   pos_in_spread 1.000
size 1900    premium 1,805,000   open_interest 255   delta 0.376
report_flags {cross_trade}   upstream_condition_detail tlct
```

It printed **exactly at the offer**. The rest of that contract's day was
retail-scale (ask 9 trades / 22 contracts; bid 7 trades / 13 contracts), so
the cross *is* the position. **Read: buyer-initiated, opening, +$15.2M
delta.**

**The honest caveat:** a `cross_trade` is pre-negotiated and printed by a
single broker representing both sides. Printing at the offer is the
conventional buyer-initiated signature, but it does **not** prove a customer
buyer — it is also consistent with a dealer facilitating a client at the
offer. **This single print carries the entire bullish delta conclusion**; if
it were reversed, net customer delta would swing from +$10.73M to roughly
−$4.5M. Phase-3 must check whether Aug-21 $230 OI actually rises to confirm
the open, and phase-8b's bear case should attack this print first.

### Sweeps (ask vs bid)

| Side | Calls (n / premium) | Puts (n / premium) |
|------|--------------------:|-------------------:|
| ask | 11 / **$5,129,451** | 9 / $1,198,175 |
| bid | 13 / **$6,524,694** | 3 / $614,604 |
| **net** | **−$1,395,243** | **+$583,571** |

On sweeps alone the read is mildly bearish — but $4.07M of that bid-side call
premium **is Package B, printed at mid**. Strip the roll and ask-side call
sweeps ($5.13M) dominate bid-side ($2.45M) by better than 2:1.

Ask-side sweeps ex-package concentrate in **Oct-16 $230 ($540,985)**, **Aug-07
$210 ($517,994)**, **Aug-21 $300 ($319,860 across 3,817 contracts at $0.82 —
lottery tickets)**, **Sep-18 $250 ($279,177)** and **Sep-04 $245 ($184,886)**.

Ask-side **put** sweeps sit at high strikes — Jun-27 $200 ($193,600), Jun-16-28
$160 ($153,650), Aug-28 $185 ($139,325), Sep-11 $305 ($131,565), Dec-18 $180
($126,950), Jan-27 $320 ($115,750), Jan-27 $260 ($114,120). The deep-ITM ones
(305/320/260, deltas −0.56 to −0.85) behave like **synthetic short stock or
conversion/reversal mechanics**, not directional put buying. The genuinely
directional puts are the OTM Aug-28 $185 and Dec-18 $180 — **$266K total,
immaterial next to $2.59M of new call premium.**

### Multi-day persistence

`uw hot-chains sweep-persistence --days 5 --symbol FSLR`, covering
2026-07-31 / 07-30 / 07-29 / 07-28 / 07-27:

```
consistency_score      0.80
sessions_in_top        4  (of 5)
dominant_direction     "mixed"
total_sweep_premium    $17,278,108
```

FSLR has been a persistent sweep venue into and out of the print, but **there
is no persistent direction** — which agrees with `phase-0.5-context.md`, where
net-directional premium was negative on 10 of 12 sessions while price went
nowhere (211.93 → 211.03). **Persistent activity, no persistent edge.** This
is the single strongest argument against sizing today's read aggressively.

### Largest premium prints (top 12 of 25)

| Type | Strike | Expiry | Premium | Size | Price | Side | Delta | IV | Time (ET) |
|------|-------:|--------|--------:|-----:|------:|------|------:|---:|----------:|
| CALL | 340 | 2027-06-17 | $2,087,000 | 1,000 | 20.87 | bid | 0.333 | 0.630 | 14:15:31 |
| CALL | 450 | 2028-01-21 | $1,987,000 | 1,000 | 19.87 | bid | 0.285 | 0.601 | 14:15:31 |
| CALL | 460 | 2028-01-21 | $1,910,000 | 1,000 | 19.10 | ask | 0.275 | 0.594 | 12:48:15 |
| **CALL** | **230** | **2026-08-21** | **$1,805,000** | **1,900** | **9.50** | **no_side** | **0.376** | **0.794** | **12:11:46** |
| CALL | 410 | 2027-03-19 | $790,000 | 1,000 | 7.90 | ask | 0.168 | 0.635 | 12:48:15 |
| CALL | 230 | 2026-10-16 | $418,895 | 199 | 21.05 | ask | 0.481 | 0.683 | 12:21:46 |
| CALL | 230 | 2026-10-16 | $292,595 | 139 | 21.05 | bid | 0.481 | 0.683 | 12:21:46 |
| CALL | 210 | 2026-08-07 | $270,000 | 300 | 9.00 | ask | 0.534 | 0.744 | 15:44:55 |
| CALL | 135 | 2026-08-21 | $231,750 | 30 | 77.25 | bid | 0.925 | 1.515 | 09:32:11 |
| CALL | 135 | 2026-08-21 | $230,100 | 30 | 76.70 | ask | 0.989 | 0.855 | 09:32:11 |
| CALL | 245 | 2026-09-04 | $180,500 | 190 | 9.50 | ask | 0.328 | 0.748 | 12:22:35 |
| PUT | 320 | 2027-01-15 | $115,750 | 10 | 115.75 | ask | −0.741 | 0.674 | 10:58:07 |

By side within the top-25: ask-calls $3.89M, bid-calls $4.88M, no_side-call
$1.81M, ask-puts $0.56M, bid-puts $0.23M, mid-call $0.09M. **The top 25 alone
account for $11.5M of $26.66M (43%)** — better coverage than the AAPL case
that motivated the whole-tape rule, but still under half the tape.

The paired $135 Aug-21 calls (30 lots each way, deltas 0.925 vs 0.989, IV 1.52
vs 0.86, same second) are a **deep-ITM cross — stock-replacement or an
unwind, delta-neutral in aggregate. Not a signal.**

### IV outliers + Greeks

**All 15 IV outliers expire 2026-07-31 — the same day.** Reported IVs run
1.359 to 6.596 with `max_iv` **18.34** on the $220 call. These are
expiration-day pricing artifacts on near-worthless contracts (e.g. PUT 190 at
$341 total premium, PUT 195 at $660). **Zero signal — excluded from every
downstream inference.**

That the IV-outlier screen surfaced *nothing but 0DTE* is itself informative:
away from expiry, **FSLR's surface is orderly post-print**. `iv30d` = 0.7378
versus 0.795 a week ago and 0.725 a month ago — the earnings crush was
**shallow**, consistent with `implied_move_perc` still at 0.7625%/day.

Greeks on the significant prints: the LEAP legs carry heavy vega (0.73–0.88)
and negligible gamma (0.0021–0.0029) — **a vega position, not a directional
gamma bet**. The Aug-21 $230 block is the mirror image: gamma **0.0094**
(3–4× the LEAPs) on vega 0.193 — **short-dated directional gamma**. The two
big trades of the day are therefore not the same trade expressed twice; they
are different desks with different objectives.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw insights deep-dive --symbol FSLR --date 2026-07-31 --json` | call_premium=19838946, put_premium=6825911, bullish=10872218, bearish=13246889, put_call_ratio=0.2791 ← `.uw_screener.*`; net_flow **derived** = −2374671 | whole tape |
| `uw options-flow sweeps --symbol FSLR --side ask --min-premium 100000 --top-n 25 --date 2026-07-31 --json` | call prem=5129451, put prem=1198175 ← `[.results[]\|{t:.option_type,p:.total_premium}]\|group_by(.t)`; top=460C 2028-01-21 $1,922,850 ← `.results[0].total_premium` | 20 |
| `uw options-flow sweeps --symbol FSLR --side bid … --json` | call prem=6524694, put prem=614604 (same path); top=340C 2027-06-17 $2,087,000 | 16 |
| `uw options-flow unusual-volume --symbol FSLR --min-vol-oi-ratio 3 --top-n 25 --date 2026-07-31 --json` | 230C 2026-08-21 vol=1937, oi=255, vol_oi_ratio=7.6006, total_premium=1839371 ← `.results[]` | 11 |
| `uw options-flow top-premium-trades --symbol FSLR --top-n 25 --date 2026-07-31 --json` | premium=2087000, size=1000, side="bid", delta=0.33347, executed_at=…18:15:31Z ← `.results[0].{premium,size,side,delta,executed_at}` (**fields are `premium`/`size`, not `total_premium`/`total_size`**) | 25 |
| `uw options-flow iv-outliers --symbol FSLR --top-n 15 --date 2026-07-31 --json` | all `.results[].expiry` = 2026-07-31; max_iv=18.3406 ← `.results[0].max_iv` | 15 |
| `uw options-flow greek-screener --symbol FSLR --top-n 15 --sort-by premium --date 2026-07-31 --json` | 230C Aug-21 gamma=0.0093926, vega=0.19318 ← `.results[3].{gamma,vega}`; 340C vega=0.72873 | 15 |
| `uw hot-chains smart-money-flow --direction bullish --top-n 10 --min-volume 500 --date 2026-07-31 --json` | FSLR rows = `[]` ← `[.results[]\|select(.underlying_symbol=="FSLR")]` | 10 (market-wide) |
| `uw hot-chains smart-money-flow --direction bearish … --json` | FSLR rows = `[]` (same path) | 10 (market-wide) |
| `uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol FSLR --json` | consistency_score=0.8, sessions_in_top=4, dominant_direction="mixed", total_sweep_premium=17278108 ← `.results[0]` | 1 |
| `uw hot-chains sweep-ratio --top-n 15 --min-volume 500 --min-sweep-ratio 0.3 --date 2026-07-31 --json` | FSLR rows = `[]` (same path) | 15 (market-wide) |
| DuckDB §A aggressor+delta split on `All Options/bot-eod-report-2026-07-31.parquet` | call ask 8.175M/+60.1 δ$M; call bid 9.268M/+59.3; no_side 1.805M/+15.2; put ask 3.978M/−22.9; put bid 2.698M/−17.7 | 6,140 prints |
| DuckDB §A net customer delta | **+10.73** ($M) ← `SUM(CASE ask→+δ·size·100·px, bid→−…, no_side&price≥ask→+…)` | 6,140 |
| DuckDB §A UW-definition reconciliation | bullish=10872218 ✓, bearish=13246889 ✓, **unclassified=2545750** | 6,140 |
| DuckDB §A cross adjudication | price=9.50, nbbo_ask=9.50, pos_in_spread=1.000, oi=255, report_flags={cross_trade} | 19 prints on that chain |
| DuckDB §A DTE-bucket premium | LEAP call 7.527M / put 1.151M; 0-1DTE call 1.344M / put 0.579M | 6,140 |

## Tool errors

**`uw hot-chains sweep-persistence --days 5 --top-n 20 --symbol FSLR --date 2026-07-31 --json`**

```
Error: unknown flag: --date
error: unknown flag: --date
```

`sweep-persistence` does **not** accept `--date`. Re-run without it (exit 0).
Per the standing note that trailing tools anchor to the latest available date,
this is **safe here only because the latest available date *is* the as-of date
(2026-07-31)** — confirmed in `phase-0-intake.md`, and the returned
`dates_covered` = `["2026-07-31","2026-07-30","2026-07-29","2026-07-28","2026-07-27"]`
verifies the window ends on the as-of date. **On any historical as-of run this
tool would silently return the wrong window.**

Non-errors worth recording:

- `smart-money-flow` returned **no FSLR rows in either direction**. Per the
  phase-1 rule, this is recorded as "no smart-money flow detected on this
  date" and was **not** re-run with looser thresholds. The top-10 is
  market-wide and monopolised by names like SPCX ($11.6M premium); FSLR's
  $26.7M whole-tape premium does not concentrate in any single chain enough to
  rank.
- `sweep-ratio` likewise returned no FSLR rows (top-15 market-wide).

## DATA NOTE / CORRECTION

**Field-path error, caught and corrected before any number was written.** The
first extraction of `top-premium-trades` used `.total_premium` / `.total_size`
(the field names used by `sweeps` and `unusual-volume`) and returned **`null`
for all 25 rows**. The correct paths for this tool are **`.premium`** and
**`.size`**, with `.price`, `.delta`, `.implied_volatility` and `.executed_at`
alongside. No null was transcribed; the table above is built from the
corrected read. This is a new instance of the documented phantom-field
trap — the tools in this family do **not** share a field vocabulary.

**Correction to `phase-0.5-context.md`.** That phase set
`unusual_verdict: GENUINELY_UNUSUAL` on the strength of a bottom-1.2-percentile
net-directional reading, and explicitly wrote: *"If phase-1 finds the negative
net call premium is routine covered-call overwriting rather than aggressive
selling, this verdict should be downgraded."* Phase 1 finds something
different from either branch: **the negative reading is substantially a
measurement artifact.** $2,545,750 (9.5% of premium) is unclassified by UW,
and the largest component printed at the offer. Adjusting for it moves
bullish premium from $10.87M to **$12.68M against $13.25M bearish** — a
**−$0.57M** net, versus the −$2.37M headline. On delta the sign flips outright
to **+$10.73M long**.

**The verdict is therefore revised to `BUSY_NAME_NORMAL_DAY`** for
confluence purposes, and **phases 1–2 confluence is capped at `+` (not `++`)**
per `rubrics/confluence-scoring.md`. Rationale: once the artifact is removed
the tape is close to balanced, FSLR's total-premium self-percentile is an
ordinary **60.6**, and `sweep_persistence.dominant_direction` is **"mixed"**
across 4 of 5 sessions. What remains genuinely notable is *composition* — a
7.6×-OI new call block and a LEAP roll — **not** unusualness of magnitude.
Phase 10 must audit this override.

## Verdict for downstream phases

- **Bias from this phase:** **mildly bullish** — reversing the sign implied by
  the raw screener aggregate, on the strength of the delta reconstruction and
  the 13:1 new-call-vs-new-put premium skew.
- **Conviction: 2 / 5.** Deliberately low despite a clean directional read,
  for four reasons: (1) the entire bullish delta conclusion rests on **one
  cross print** whose initiator is unprovable; (2) `dominant_direction` is
  **"mixed"** over 5 sessions with **$17.28M** of sweep premium producing no
  price progress; (3) the largest premium bucket is **LEAP (32.6%)**, which is
  slow money with poor short-term tradeability; (4) the day is **post-earnings
  day-1**, when flow is contaminated by position adjustment rather than fresh
  directional conviction.
- **Three datapoints later phases must remember:**
  1. **1,900 Aug-21 $230 calls at the offer, $1.805M, vol/OI 7.6× (OI 255),
     +$15.2M delta, gamma 0.0094.** The trade of the day. **Phase 3 must
     verify the OI actually opens** — if Aug-21 $230 OI does not jump toward
     ~2,155, the buy interpretation is wrong and this phase's bias inverts.
  2. **UW directional premium drops `mid`/`no_side` prints — $2,545,750 (9.5%)
     today.** Any phase quoting `bullish_premium`/`bearish_premium`/`net_flow`
     is quoting a 90.5% sample. Phase 7's composite inherits this bias.
  3. **LEAP roll: +$1.374M credit, ≈−$3.7M delta, up-and-out in strike
     (340→410/460), and Jan-28 $450C OI of 671 against a 1,000-lot sale means
     ≥329 newly opened short.** A large holder is taking money off the table
     while staying long — supportive but decaying.
- **Open questions:**
  - **Is the dark pool confirming?** +$10.73M of option delta is small next to
    FSLR's $3.01M-share / ~$636M day. Phase 2 must say whether block prints
    corroborate accumulation or show distribution into the +2.44% pop.
  - **Does Aug-21 $230 open in OI?** → phase 3. This is the single
    highest-value verification in the run.
  - **Who is short the Aug-21 $230 calls, and where does that put dealer
    gamma?** 1,900 contracts of 0.0094 gamma is meaningful into a 3-week
    expiry with the stock 9% below the strike → phase 4.
  - **Is deep-ITM put ask-side buying (320/305/280/260/255) directional or
    conversion/synthetic mechanics?** It is $0.6M of the $3.98M put ask-side
    total; if structural, the residual directional put buying is negligible.
    → phase 3 OI and phase 4 structure.
