# Phase 3 — Open Interest & Positioning

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`

## Summary

**Nobody is positioning in SWKS options.** The single largest open-interest change
anywhere on the chain is **+46 contracts** (Sep-18 52.5 put); `biggest-increases`
at the phase-prescribed `--min-oi-change 500` returns **zero rows**,
`position-rolls --threshold 500` returns **zero rows**, and `smart-positioning` at
the same threshold returns **zero rows**. Dropping the threshold to 1 to see
anything at all yields 20 rows whose largest premium is **$11,924** and whose
inferred-direction tally is **11 bullish / 9 bearish** — a coin flip on noise. The
OPEX cliff is unambiguous — **2026-08-21 holds 61.87% of tracked OI (24,201
contracts, 21 DTE, P/C 0.26)** — but **66.6% of that expiry's OI sits in
functionally dead strikes ≥20% out of the money** (the 80-strike call alone carries
**11,927 contracts** at a $0.24 last fill, a stable legacy position unchanged since
at least 2026-07-14). Strip those and the tradeable Aug-21 structure is a tight
box: **put-wall support at $60.00 (1,139 OI) and call-wall resistance at $65.00
(874 OI)** — which brackets spot $62.28 and matches phase 2's $61.36–62.50
congestion band almost exactly. **Critically, phase 1's open question cannot be
answered:** the OI dataset is lagged one session (`last_date 2026-07-30 →
curr_date 2026-07-31`), so the 3,333 Aug-21 52.5 puts sold on the as-of day would
only appear in the 2026-08-03 file, which is beyond the local snapshot.

## Key signals

- **`uw oi biggest-increases --min-oi-change 500` → 0 rows.** At `--min-oi-change 1`
  the largest change on the entire chain is **+46 contracts / $9,302 premium**
  (SWKS260918P00052500). There is no institutional build here. `[OI:biggest_increases]`
- **OPEX cliff = 2026-08-21, `pct_of_total_oi` 61.87%**, 24,201 contracts, call-heavy
  (`put_call_oi_ratio` **0.26**, 19,203C vs 4,998P), **21 DTE**. `[OI:term_structure]`
- **The Aug-21 call OI is a phantom.** 11,927 of 19,203 Aug-21 calls (**62.1%**) sit
  at the **80 strike, 28.5% OTM, last fill $0.24, bid/ask 0.10/0.25**, with OI flat
  at 11,700–11,950 for at least 12 sessions. Add 75C (2,929), 100C (1,263), 87.5C
  (290) and **16,409 of 24,201 Aug-21 contracts (67.8%) are ≥20% OTM calls priced
  at $0.02–$0.43.** `[OI:oi_by_strike DUCKDB]`
- **Tradeable wall map (≤30 DTE):** `put_wall_support` **$60.00** (`net_oi` −625,
  `distance_pct` −3.78) and `call_wall_resistance` **$65.00** (`net_oi` +435,
  `distance_pct` +4.23). Spot sits inside a **$60–65 box**. `[OI:oi_by_strike]`
- **Only one contract closed:** `decrease-with-volume` returns exactly **1 row** —
  Aug-21 **70 call, OI −46 on 135 volume**. That is the whole of the day's closing
  activity. `[OI:decrease_with_volume]`
- **No pin, no concentration flag.** `pin-risk --dte-max 7` excludes SWKS (nearest
  expiry is 21 DTE); `opex-concentration --min-concentration-pct 40` excludes SWKS
  even at `--top-n 500` (cutoff BEG at 79.37% vs SWKS's 61.87%). `[OI:pin_risk]` `[OI:opex_concentration]`

## Detailed findings

### OI walls by strike

`uw oi oi-by-strike --symbol SWKS --top-n 10 --date 2026-07-31` — **all-expiry
aggregate** (the phase's pitfall #4 applies in full here):

| Strike | `call_oi` | `put_oi` | `net_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|
| **80** | **13,164** | 0 | **+13,164** | `call_wall_resistance` | **+28.29%** |
| 60 | 984 | 3,359 | −2,375 | `put_wall_support` | −3.78% |
| 75 | 3,220 | 0 | +3,220 | `call_wall_resistance` | +20.27% |
| 65 | 1,543 | 524 | +1,019 | `call_wall_resistance` | +4.23% |
| 52.5 | 0 | 1,945 | −1,945 | `put_wall_support` | −15.81% |
| 62.5 | 775 | 859 | −84 | `put_heavy` | +0.22% |
| 55 | 0 | 1,317 | −1,317 | `put_wall_support` | −11.80% |
| 57.5 | 166 | 1,130 | −964 | `put_wall_support` | −7.79% |
| 100 | 1,263 | 0 | +1,263 | `call_wall_resistance` | +60.36% |
| 35 | 1,217 | 0 | +1,217 | `call_heavy` | −43.87% |

Narrowed to the tradeable horizon, `--dte-max 30`:

| Strike | `call_oi` | `put_oi` | `net_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|
| **80** | **11,927** | 0 | +11,927 | `call_wall_resistance` | +28.29% |
| 75 | 2,929 | 0 | +2,929 | `call_wall_resistance` | +20.27% |
| **60** | 514 | **1,139** | **−625** | **`put_wall_support`** | **−3.78%** |
| **65** | **874** | 439 | **+435** | **`call_wall_resistance`** | **+4.23%** |
| 100 | 1,263 | 0 | +1,263 | `call_wall_resistance` | +60.36% |
| 52.5 | 0 | 947 | −947 | `put_wall_support` | −15.81% |
| 67.5 | 0 | 887 | −887 | `put_heavy` | +8.24% |
| 70 | 776 | 0 | +776 | `call_wall_resistance` | +12.25% |
| 55 | 0 | 686 | −686 | `put_wall_support` | −11.80% |
| 47.5 | 0 | 564 | −564 | `put_wall_support` | −23.83% |

**The 80 and 75 "walls" must be discarded.** Pulling the full Aug-21 chain shows
why:

| Strike | Type | `curr_oi` | `oi_diff_plain` | `curr_vol` | **`last_fill`** | Dist % |
|---|---|---|---|---|---|---|
| 47.5 | P | 564 | −1 | 119 | $0.20 | −23.7% |
| **52.5** | **P** | **947** | +9 | **3,333** | **$0.70** | **−15.7%** |
| 55 | P | 686 | +7 | 6 | $1.00 | −11.7% |
| 57.5 | P | 336 | +2 | 38 | $1.65 | −7.7% |
| 57.5 | C | 166 | +1 | 0 | $6.18 | −7.7% |
| **60** | **P** | **1,139** | **+15** | 15 | **$2.85** | **−3.7%** |
| 60 | C | 514 | −3 | 44 | $4.42 | −3.7% |
| **65** | **C** | **874** | **+15** | 72 | **$2.50** | **+4.4%** |
| 65 | P | 439 | −1 | 0 | $5.45 | +4.4% |
| 67.5 | P | 887 | −1 | 0 | $7.39 | +8.4% |
| 70 | C | 776 | **−46** | 8 | $0.90 | +12.4% |
| 72.5 | C | 464 | +2 | 4 | $0.65 | +16.4% |
| 75 | C | **2,929** | +1 | 155 | **$0.43** | +20.4% |
| **80** | **C** | **11,927** | −12 | 107 | **$0.24** | **+28.5%** |
| 87.5 | C | 290 | +3 | 0 | **$0.05** | +40.5% |
| 100 | C | 1,263 | +12 | 3 | **$0.02** | +60.6% |

**16,409 of 24,201 Aug-21 contracts (67.8%) are calls ≥20% OTM trading at
$0.02–$0.43.** Those carry essentially no dealer gamma at spot and cannot act as
resistance; the `role` tag is a mechanical call/put-split heuristic and is
misleading here, exactly as the phase's pitfall note warns. The 80-strike position
is *static*, not new — its OI history is flat across every available session:

| `curr_date` | `last_oi` → `curr_oi` | Δ | `last_fill` |
|---|---|---|---|
| 2026-07-14 | 11,740 → 11,734 | −6 | $0.94 |
| 2026-07-17 | 11,702 → 11,700 | −2 | $0.51 |
| 2026-07-21 | 11,703 → 11,734 | +31 | $0.60 |
| 2026-07-22 | 11,734 → 11,857 | +123 | $1.00 |
| 2026-07-24 | 11,856 → 11,855 | −1 | $0.57 |
| 2026-07-28 | 11,855 → 11,869 | +14 | $0.61 |
| 2026-07-29 | 11,869 → 11,692 | −177 | $0.90 |
| 2026-07-30 | 11,692 → 11,939 | +247 | $0.30 |
| **2026-07-31** | **11,939 → 11,927** | **−12** | **$0.24** |

A legacy overwrite or an old upside bet from when SWKS traded near its 52-week
high of **$90.90** (`phase-0.5-context.md`). It is decaying to zero and is not a
signal.

**The real, tradeable wall map is a $60–65 box:**
- **$60.00 put-wall support** — 1,139 puts vs 514 calls, `net_oi` −625, −3.8% from
  spot, and the **largest live near-money contract on the Aug-21 board**. OI grew
  +15 into the as-of file.
- **$65.00 call-wall resistance** — 874 calls vs 439 puts, `net_oi` +435, +4.2%
  from spot, OI +15.
- **$52.50 put-wall support** — 947 puts, −15.8% from spot. This is exactly the
  strike phase 1 found being **sold** in 3,333 contracts.

This box **independently reproduces phase 2's finding** that spot sits inside a
$61.36–62.50 dark-pool congestion band, and it corroborates
`phase-1-flow.md`'s conclusion that upside is capped: the Sep-18 62.5/65 credit
call spread and the sold 110 Jan-27 85 calls line up with a 65 call wall.

### OI term structure — the OPEX cliff

`uw oi term-structure --symbol SWKS --date 2026-07-31` (key is `.term_structure`,
**not** `.results`), 8 expiries:

| Expiry | DTE | `call_oi` | `put_oi` | `total_oi` | `put_call_oi_ratio` | **`pct_of_total_oi`** | `contract_count` |
|---|---|---|---|---|---|---|---|
| **2026-08-21** | **21** | **19,203** | 4,998 | **24,201** | **0.260** | **61.87%** | 16 |
| 2026-09-18 | 49 | 4,315 | 3,099 | 7,414 | 0.718 | 18.95% | 16 |
| 2027-01-15 | 168 | 1,424 | 2,419 | 3,843 | 1.699 | 9.82% | 8 |
| 2028-01-21 | 539 | 1,637 | 0 | 1,637 | 0.000 | 4.18% | 3 |
| 2026-11-20 | 112 | 266 | 1,115 | 1,381 | **4.192** | 3.53% | 9 |
| 2026-12-18 | 140 | 340 | 224 | 564 | 0.659 | 1.44% | 5 |
| 2027-03-19 | 231 | 0 | 67 | 67 | 0.000 | 0.17% | 1 |
| 2027-06-17 | 321 | 11 | 0 | 11 | 0.000 | 0.03% | 2 |

**The OPEX cliff is 2026-08-21 at 61.87% of tracked OI, 21 days out.** Its headline
P/C of 0.26 looks aggressively call-heavy — but as dissected above, that ratio is
manufactured by the dead 75/80/87.5/100 strikes. **Excluding calls ≥20% OTM, the
Aug-21 P/C flips to 4,998 puts vs 2,794 calls = 1.79** — i.e. the *live* Aug-21
book is **put-heavy**, the opposite of the headline. Phase 4 should cross-check
this against max-pain, which will be dragged upward by the same dead call OI.

Secondary structure: **2026-11-20 has a `put_call_oi_ratio` of 4.192** — the only
expiry with a genuinely lopsided put book (1,115 puts vs 266 calls), sitting ~112
days out, i.e. **past the 2026-10-27 earnings date** verified in
`phase-0.5-context.md`. That is the shape of event hedging placed around the next
print, and it is the only forward-looking protection visible on the board.

### Largest OI increases

`uw oi biggest-increases --symbol SWKS --top-n 20 --min-oi-change 500 --date 2026-07-31`
→ **`{"results":[]}`**. Nothing on the chain moved 500 contracts.

Re-run at `--min-oi-change 1` to characterise what little did move (25 rows;
`oi_diff_plain` is the absolute delta — `oi_change` is the *ratio*, per the phase note):

| `option_symbol` | Strike / Type / DTE | `oi_diff_plain` | `oi_change` | `curr_oi` | `curr_vol` |
|---|---|---|---|---|---|
| SWKS260918P00052500 | 52.5 P 49d | **+46** | 0.2009 | 275 | 55 |
| SWKS260918P00057500 | 57.5 P 49d | +29 | 0.1058 | 303 | 34 |
| SWKS261120P00042500 | 42.5 P 112d | +24 | 0.8571 | 52 | 24 |
| SWKS260821C00065000 | 65 C 21d | +15 | 0.0175 | 874 | 31 |
| SWKS260821P00060000 | 60 P 21d | +15 | 0.0133 | 1,139 | 41 |
| SWKS261218P00047500 | 47.5 P 140d | +14 | 0.5833 | 38 | 15 |
| SWKS260918C00062500 | 62.5 C 49d | +12 | 0.0157 | 775 | 19 |
| SWKS260821C00100000 | 100 C 21d | +12 | 0.0096 | 1,263 | 15 |
| SWKS261120P00047500 | 47.5 P 112d | +11 | 0.1089 | 112 | 11 |
| SWKS270115C00110000 | 110 C 168d | +11 | 0.0215 | 523 | 13 |
| *(15 more, all ≤ +10)* | | | | | |

The largest single build is **46 contracts on $9,302 of premium**. For scale, the
day's *options* tape was $877,883 (`phase-1-flow.md`) and the day's *dark pool* was
$16,263,573 (`phase-2-dark-pool.md`). **There is no OI-visible institutional
positioning in SWKS on this date, in either direction.**

Note the tilt of what did build: the three largest increases are **all puts**
(52.5P, 57.5P, 42.5P), and the 42.5P/47.5P builds sit at 112–140 DTE — again
straddling the 2026-10-27 earnings date.

### Closing / roll activity

`uw oi decrease-with-volume --symbol SWKS --top-n 15 --min-volume 100 --date 2026-07-31`
→ **1 row**:

| `option_symbol` | `oi_diff_plain` | `volume` | `curr_oi` |
|---|---|---|---|
| SWKS260821C00070000 (70 C, 21 DTE) | **−46** | 135 | 776 |

One position closing, 46 contracts, in a $0.90 call 12.4% OTM. Immaterial.

`uw oi position-rolls --symbol SWKS --threshold 500 --near-dte-max 30 --date 2026-07-31`
→ **`{"results":[]}`**. **No near→far rolls.** The roll signature the phase
describes (near-DTE strike X decreasing while far-DTE strike X increases) does not
appear anywhere.

### Smart positioning (inferred direction)

`uw oi smart-positioning --symbol SWKS --top-n 20 --min-oi-change 500 --date 2026-07-31`
→ **0 rows**. At `--min-oi-change 1`, 20 rows:

| Symbol | Strike | DTE | Type | `inferred_direction` | `oi_diff_plain` | `net_ask_bid` | `prev_total_premium` |
|---|---|---|---|---|---|---|---|
| SWKS260918P00052500 | 52.5 | 49 | put | bearish | 46 | +45 | $9,302 |
| SWKS260918P00057500 | 57.5 | 49 | put | bearish | 29 | +28 | $10,638 |
| SWKS261120P00042500 | 42.5 | 112 | put | bearish | 24 | +24 | $3,070 |
| SWKS260821C00065000 | 65 | 21 | call | bullish | 15 | +5 | $6,942 |
| SWKS260821P00060000 | 60 | 21 | put | **bullish** | 15 | −3 | $11,924 |
| SWKS261218P00047500 | 47.5 | 140 | put | bullish | 14 | −15 | $4,125 |
| SWKS260918C00062500 | 62.5 | 49 | call | bullish | 12 | +8 | $8,862 |
| SWKS260821C00100000 | 100 | 21 | call | bearish | 12 | −11 | $64 |
| SWKS261120P00047500 | 47.5 | 112 | put | bearish | 11 | +9 | $2,545 |
| SWKS270115C00110000 | 110 | 168 | call | bullish | 11 | +7 | $1,800 |
| *(10 more)* | | | | | | | |

**Tally: 11 bullish / 9 bearish.** Largest premium in the entire set: **$11,924**.
This is a coin flip on noise-level sizes and carries **no information**. Recorded
for completeness, not used in the verdict.

Per the phase's pitfall #2, the OPRA parsing was spot-checked: `SWKS260918P00052500`
→ SWKS, 2026-09-18, **P**ut, strike 52.500 — matches the row's own
`strike: 52.5`, `dte: 49`, `option_type_inferred: "put"`. Parsing is correct;
SWKS is a plain single-class symbol with no dual-class ambiguity.

### Pin risk

`uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-07-31`
returned 25 market-wide rows; **SWKS is absent**. This is expected and correct —
SWKS's nearest expiry is **2026-08-21 at 21 DTE**, well outside the 7-day window.
Per the phase instruction, **pin commentary is skipped**; there is no OPEX-week pin
mechanic in play on this date.

### OPEX concentration

`uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-07-31`:
**SWKS absent.** Re-run at `--top-n 500`: still absent — the 500th-ranked name
(BEG) sits at **79.37%** concentration, above SWKS's 61.87%. So SWKS's Aug-21
cliff, while real and dominant *for this name*, is **not extreme by market
standards** and produces no cross-sectional flag.

### Float normalization (advisory)

`phase-0-intake.md` recorded **`fz_available = yes, DEGRADED`** with **`Shs Float`
unavailable** (14 of 84 fields parse). Falling back to the same derived denominator
used in `phase-2-dark-pool.md` — `marketcap / close = 9,401,539,419 / 62.28 =
150,956,637 shares outstanding` (**shares outstanding, not float**, so these
percentages are *understated*):

| Position | Contracts | Share-equivalent | % of shares out |
|---|---|---|---|
| **Largest OI build (Sep-18 52.5P)** | **+46** | 4,600 | **0.0030%** |
| Largest OI decrease (Aug-21 70C) | −46 | 4,600 | 0.0030% |
| Whole Aug-21 expiry OI | 24,201 | 2,420,100 | 1.60% |
| Legacy Aug-21 80C position | 11,927 | 1,192,700 | 0.79% |
| Aug-21 60P (live put wall) | 1,139 | 113,900 | 0.075% |
| Aug-21 52.5P (phase-1 strike) | 947 | 94,700 | 0.063% |

**Read for this name: the build is not structural — it is not even measurable.**
0.003% of the share count is three orders of magnitude below the 0.380% of shares
outstanding that the dark pool absorbed over 2026-07-29/30
(`phase-2-dark-pool.md §Float normalization`). Where the flow lives in SWKS right
now is the **share tape, not the option chain**. Tagged `[OI:oi_pct_float fz]`,
advisory only, **does not raise conviction**.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw oi oi-by-strike --symbol SWKS --top-n 10 --date 2026-07-31 --json` | 80: call_oi 13164 / put_oi 0 / net_oi 13164 / role `call_wall_resistance` / distance_pct 28.29; 60: 984/3359/−2375/`put_wall_support`/−3.78; 65: 1543/524/+1019/`call_wall_resistance`/4.23; 52.5: 0/1945/−1945/`put_wall_support`/−15.81 ← `.results[]` | top-10 all-expiry |
| `uw oi oi-by-strike --symbol SWKS --top-n 10 --dte-max 30 --date 2026-07-31 --json` | 80: 11927/0/+11927; **60: 514/1139/−625/`put_wall_support`/−3.78**; **65: 874/439/+435/`call_wall_resistance`/+4.23**; 52.5: 0/947/−947 ← `.results[]` | top-10 ≤30 DTE |
| `uw oi term-structure --symbol SWKS --date 2026-07-31 --json` | Aug-21: call_oi 19203, put_oi 4998, total_oi 24201, put_call_oi_ratio 0.26, **pct_of_total_oi 61.87**, dte 21, contract_count 16; Nov-20 put_call_oi_ratio **4.192**; expiry_count 8 ← **`.term_structure[]`** (not `.results`) | all 8 expiries |
| `uw oi biggest-increases --symbol SWKS --top-n 20 --min-oi-change 500 --date 2026-07-31 --json` | **`.results` = []** ← `.results\|length` = 0 | top-20 (empty) |
| `uw oi biggest-increases --symbol SWKS --top-n 25 --min-oi-change 1 --date 2026-07-31 --json` | max `oi_diff_plain` = **46** (SWKS260918P00052500, oi_change 0.20087, curr_oi 275, volume 55, prev_total_premium 9302) ← `.results[0]` | top-25 |
| `uw oi decrease-with-volume --symbol SWKS --top-n 15 --min-volume 100 --date 2026-07-31 --json` | **1 row**: SWKS260821C00070000, oi_diff_plain −46, volume 135, curr_oi 776 ← `.results[0]` | 1 |
| `uw oi smart-positioning --symbol SWKS --top-n 20 --min-oi-change 500 --date 2026-07-31 --json` | **0 rows** ← `.results\|length` | (empty) |
| `uw oi smart-positioning --symbol SWKS --top-n 20 --min-oi-change 1 --date 2026-07-31 --json` | 20 rows; tally bullish 11 / bearish 9 ← `[.results[].inferred_direction]\|group_by(.)`; max prev_total_premium 11924 | top-20 |
| `uw oi position-rolls --symbol SWKS --threshold 500 --near-dte-max 30 --date 2026-07-31 --json` | **`.results` = []** | (empty) |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-07-31 --json` | 25 rows; SWKS **absent** ← `[.results[]\|select(.ticker=="SWKS")]` = `[]` | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-07-31 --json` | 20 rows; SWKS **absent**; all 20 at concentration_pct 100 | top-20 |
| `uw oi opex-concentration --top-n 500 --min-concentration-pct 40 --date 2026-07-31 --json` | 500 rows; SWKS still **absent**; cutoff BEG concentration_pct **79.37**, total_oi 1944 ← `.results[-1]` | top-500 |
| DuckDB `chain-oi-changes-2026-07-31.parquet`, `underlying_symbol='SWKS'` | n=**60** contracts tracked, Σ`curr_oi`=**39,118**, Σ`last_oi`=38,919, call 27,196 / put 11,922; **`last_date`=2026-07-30, `curr_date`=2026-07-31** `[OI:lag DUCKDB]` | 60 |
| DuckDB — Aug-21 chain (`dte=21`) | 16 strikes; 80C curr_oi 11,927 last_fill $0.24; 75C 2,929 @$0.43; 100C 1,263 @$0.02; 87.5C 290 @$0.05 ⇒ **16,409 / 24,201 = 67.8% ≥20% OTM calls**; 60P 1,139 @$2.85; 65C 874 @$2.50 `[OI:chain DUCKDB]` | 16 |
| DuckDB — SWKS260821C00080000 OI history | flat 11,700–11,939 across 2026-07-14 → 2026-07-31; last_fill decayed $0.94 → $0.24 `[OI:legacy_strike DUCKDB]` | 12 sessions |
| DuckDB — SWKS260821P00052500 row | last_oi 938 → curr_oi 947 (+9), `volume` 11, **`curr_vol` 3,333**, `prev_vol` 11, trades 5 ⇒ confirms the one-session lag `[OI:lag DUCKDB]` | 1 |

## Tool errors

No `uw oi` command errored in this phase.

**Valid empties (thresholds, not failures) — recorded per orchestration rule 3:**
- `biggest-increases --min-oi-change 500` → `[]` (max actual change on the chain is
  46).
- `smart-positioning --min-oi-change 500` → `[]` (same reason).
- `position-rolls --threshold 500` → `[]` (no roll approaches 500 contracts).
- `pin-risk --dte-max 7` → SWKS absent (nearest expiry 21 DTE — structurally
  excluded, not missing data).
- `opex-concentration --min-concentration-pct 40` → SWKS absent at both `--top-n 20`
  and `--top-n 500` (SWKS's 61.87% ranks below the 500th name's 79.37%).

## DATA NOTE / CORRECTION

1. **The OI dataset is lagged one session — this is load-bearing.** The
   2026-07-31 file carries **`last_date = 2026-07-30`, `curr_date = 2026-07-31`**,
   so `oi_diff_plain` reports the OI change produced by **2026-07-30's** trading,
   and the row's `volume` field is likewise **2026-07-30's** volume. The *as-of*
   day's volume lives in a separate column, `curr_vol`. Verified on the phase-1
   contract: `SWKS260821P00052500` has `volume = 11`, `prev_vol = 11`, but
   **`curr_vol = 3,333`** — which reconciles **exactly** with
   `uw options-flow unusual-volume`'s `total_volume = 3333` and `open_interest =
   947` in `phase-1-flow.md`. **Consequence: phase 1's open question — "did the
   3,333 short 52.5 puts become open interest?" — is UNANSWERABLE from this
   snapshot.** Those contracts can only appear in the **2026-08-03** OI file, and
   `phase-0-intake.md` establishes 2026-07-31 as the latest available date. Any
   downstream phase asserting that the short-put position did or did not stick is
   asserting beyond the data.
2. **`oi-by-strike`, `term-structure` and `biggest-increases` all read a partial
   chain.** The OI-changes parquet tracks only **60 SWKS contracts totalling 39,118
   OI**, against the screener's `total_open_interest` of **118,470** — i.e.
   **33.0% coverage** (call 27,196 of 75,306; put 11,922 of 43,164). Every OI
   percentage in this phase (`pct_of_total_oi` included) is a share of the
   **tracked** subset, not of the true chain. Stated at each use; the wall
   *ranking* is still usable because the untracked contracts are, by construction,
   the inactive ones — but no absolute OI total from this phase should be treated
   as the full book.
3. **`term-structure` returns `.term_structure`, not `.results`.** A first `jq`
   pass against `.results[]` produced **empty output** and would have been recorded
   as "no term structure available". Re-read against the actual key returned all 8
   expiries. No value from the empty read was carried forward.
4. **The `role` tags at strikes 80/75/100/87.5 are rejected on evidence, not
   overridden by opinion.** The rejection rests on quoted `last_fill` values
   ($0.24 / $0.43 / $0.02 / $0.05), a bid/ask of 0.10/0.25 on the 80C, and a
   12-session flat OI history — all read from validated JSON/parquet, not inferred.

## Verdict for downstream phases

- **Positioning bias:** **NONE — the option chain is inert.** Not "calls being
  built", not "puts being built", not "rolling out". The largest change on the
  entire chain is 46 contracts; three of the phase's five ranked tools return empty
  at their prescribed thresholds. What structure exists is **legacy and decaying**
  (the 11,927-contract Aug-21 80C), and what little is being added tilts **mildly
  toward puts** (the three largest builds are all puts, and the 42.5P/47.5P adds sit
  at 112–140 DTE, straddling the 2026-10-27 earnings date verified in
  `phase-0.5-context.md`).
- **Conviction:** **1 / 5.** This phase contributes essentially no directional
  information. It is nonetheless *useful* — it establishes (a) that the $60–65 box
  is a real structural feature, (b) that the headline Aug-21 call-heaviness is an
  artifact, and (c) that phase 1's short-put position cannot be confirmed. Those
  are constraints on downstream conviction, not additions to it.
- **Largest OI build as % of float:** **0.0030%** (46 contracts = 4,600
  share-equivalents vs 150,956,637 **shares outstanding**; true float % is higher —
  `Shs Float` unavailable per `phase-0-intake.md`). **Not structural — not even
  measurable.** For contrast, phase 2's dark pool absorbed **0.380%** of shares
  outstanding over two sessions, ~127× larger. **The SWKS story is in the share
  tape, not the option chain.**
- **Three pin/cliff strikes for phase-9** (sourced from `oi-by-strike` roles and
  the `term-structure` cliff, not hand-picked):
  1. **$60.00 — `put_wall_support`, ≤30 DTE** (`net_oi` −625; 1,139 puts vs 514
     calls; `distance_pct` −3.78%). The largest *live* near-money contract on the
     Aug-21 board, and it sits inside phase 2's **$60.25–61.22 immediate-support**
     shelf (three blocks, ~277,000 shares). Two independent datasets naming the
     same level is the strongest confluence in this run so far.
  2. **$65.00 — `call_wall_resistance`, ≤30 DTE** (`net_oi` +435; 874 calls vs 439
     puts; `distance_pct` +4.23%). Confirmed from a third angle by
     `phase-1-flow.md`'s Sep-18 62.5/65 credit call spread. Note this sits
     **below** phase 2's $64.68 dark-pool supply wall — so $64.70–65.00 is a
     **stacked resistance zone**, not a single line.
  3. **2026-08-21 — the OPEX cliff, 61.87% of tracked OI, 21 DTE.** The gravity
     date. Phase 4 must reconcile it with max-pain, bearing in mind that max-pain
     will be **dragged artificially high** by the 16,409 dead ≥20%-OTM calls; a
     max-pain print near $75–80 should be treated as an artifact of that legacy OI,
     not as a genuine upward pin.
  - Secondary reference: **$52.50 `put_wall_support`** (947 OI, −15.8%) — the
    phase-1 short-put strike, unconfirmable as OI until 2026-08-03.
- **Open questions:**
  - **Is the call buildup speculative or covered?** Moot as asked — there *is* no
    call buildup. The real question inherited by phase 8 is whether the
    11,927-contract legacy 80C is a **covered overwrite** against a long holder
    (which would mean a large institution has held SWKS stock through the de-rate
    and is still short upside), or an abandoned outright long. The OI data cannot
    distinguish them; only the size and its 12-session stability are observable.
  - **Did phase 1's 3,333 short Aug-21 52.5 puts become open interest?**
    **Unresolvable from this snapshot** (see DATA NOTE 1). Phase 9 must treat the
    "$52.50 flow-anchored floor" as **provisional** and must not size against it as
    if confirmed.
  - **Why does the Nov-20 expiry carry a `put_call_oi_ratio` of 4.192** (1,115
    puts vs 266 calls) when every nearer expiry is call-tilted? It is the only
    forward-looking hedge structure on the board and it sits past the 2026-10-27
    earnings date. Phase 6's catalyst calendar and phase 7c's positioning gate
    should determine whether that is routine event hedging or someone specifically
    positioned for a bad October print.
