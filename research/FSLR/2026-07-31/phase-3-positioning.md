# Phase 3 — Open Interest & Positioning

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`

## Summary

**Phase 1's headline verification cannot be performed today — the OI dataset
is lagged one full session.** The file carries `last_date = 2026-07-30`,
`curr_date = 2026-07-31`, and the smoking gun is direct: `FSLR260821C00230000`
shows `curr_oi = 255` and **`volume = 28`**, while `phase-1-flow.md` recorded
**1,937 contracts** traded on that exact chain today. Today's tape is simply
not in this file. **Whether the 1,900-lot Aug-21 $230 block opened will only be
answerable from the 2026-08-03 snapshot** (expected OI ≈ 255 + 1,900 ≈
**2,155** if it opened). Fortunately `phase-2-dark-pool.md` already settled the
question by a different route — the 49-second, 101.1%-match QCT delta hedge.

What the lagged data *does* show is **prior-session positioning that is
call-built and well-distributed**. Across the 348 tracked contracts, OI rose
**+6,117 calls vs +3,514 puts**. The single largest build is **Sep-18 $220
calls, +985 contracts (996 → 1,981, a 98.9% doubling)** — landing squarely in
the **2026-09-18 expiry, which alone holds 26.81% of tracked OI at a P/C of
0.382**, the most call-skewed major expiry on the board.

Two structural facts matter more than any single build. **FSLR has no OPEX
cliff** — it fell outside `opex-concentration`'s top-20 because no expiry
reaches the 40% threshold, and outside `pin-risk`'s top-25 because monthly
OPEX (Aug-21) is 21 days out, beyond the 7-day window. And the tradeable wall
map is **thin and put-tilted near spot** while the imposing call walls sit
18–52% away, unreachable inside any realistic horizon.

**A significant coverage caveat governs everything below**: term-structure
sums to **224,381** contracts against the **577,414** `total_open_interest`
reported by `uw insights deep-dive` — the dataset covers only **38.9%** of
FSLR's real open interest.

## Key signals

- **OI data is one session stale** (`last_date` 2026-07-30 → `curr_date`
  2026-07-31); Aug-21 $230 shows `volume = 28` vs today's actual 1,937
  `[OI:oi_lag DUCKDB]`
- **OPEX cliff = 2026-09-18: 60,163 contracts, 26.81% of tracked OI, P/C
  0.382** (43,524 calls vs 16,639 puts) — the gravity well, 49 DTE
  `[OI:term_structure]`
- **Largest build: Sep-18 $220 calls +985 (996 → 1,981, +98.9%)** on 1,082
  volume — a doubling, in the cliff expiry `[OI:biggest_increases]`
- **No pin risk, no OPEX concentration** — FSLR outside top-25 and top-20
  respectively; OI is spread across 15 expiries with no 40%+ cluster
  `[OI:pin_risk]` `[OI:opex_concentration]`
- **Nearest genuine call wall: $217.5 (+3.07%), net_oi +3,139**; nearest
  support **$200 (−5.22%), net_oi −1,811** and **$190 (−9.96%), net_oi
  −3,040** `[OI:oi_by_strike]`
- **Near-term 220 is put-heavy** (call 1,400 / put 2,316, net −916) even though
  the all-expiry aggregate tags it `call_wall_resistance` — a two-sided
  battleground, not a wall `[OI:oi_by_strike]`
- **`position-rolls` detected 0 rolls** despite phase-1 documenting a clear
  $4.07M-credit LEAP roll today — the tool cannot see it through the OI lag
  `[OI:position_rolls]`
- **Largest OI build = 0.0971% of float** (985 × 100 ÷ 101.48M) — not
  structural `[OI:oi_pct_float fz]`

## Detailed findings

### The OI lag (read this before any number below)

| Field | Value |
|-------|-------|
| `last_date` | **2026-07-30** |
| `curr_date` | **2026-07-31** |
| Tracked FSLR contracts | 348 |
| Tracked total OI | **224,381** |
| Actual `total_open_interest` (phase 0.5 / `insights deep-dive`) | **577,414** |
| **Coverage** | **38.9%** |

`curr_oi` is the snapshot at **today's open** — i.e. after 2026-07-30's close.
Three independent confirmations:

1. `FSLR260821C00230000`: `curr_oi = 255`, `volume = 28`. Phase 1 recorded
   **1,937** contracts on that chain today (`vol_oi_ratio = 7.6` against the
   same stale 255).
2. Summed tracked volume — calls **12,167**, puts **6,702** — matches
   `phase-0.5-context.md`'s **2026-07-30** session row (call 12,339 / put
   6,953) to within the untracked-contract residual. It does **not** resemble
   today's 24,254 / 6,770.
3. The Jan-2028 strikes traded today (450, 460) are absent from the file
   entirely; the tracked Jan-2028 strikes are 260/300/320/400.

**Consequence:** every "build" below describes **2026-07-30** positioning.
Today's flow (phase 1) and today's hedge (phase 2) are *not* reflected. The
two phases are complementary, not corroborating — phase 3 cannot confirm
phase 1, and no downstream phase should claim that it does.

### OI walls by strike

**All-expiry aggregate** (`oi-by-strike --top-n 10`, spot 211.02) — dominated
by far-dated LEAP call strikes and **not tradeable**:

| Strike | Call OI | Put OI | Net OI | Total | Role | Dist % |
|-------:|--------:|-------:|-------:|------:|------|-------:|
| 300 | 26,638 | 0 | +26,638 | 26,638 | call_wall_resistance | +42.17 |
| 250 | 14,003 | 3,695 | +10,308 | 17,698 | call_wall_resistance | +18.47 |
| 320 | 16,800 | 0 | +16,800 | 16,800 | call_wall_resistance | +51.64 |
| 260 | 16,503 | 0 | +16,503 | 16,503 | call_wall_resistance | +23.21 |
| **180** | 6 | **16,361** | **−16,355** | 16,367 | **put_wall_support** | **−14.70** |
| 220 | 7,772 | 5,263 | +2,509 | 13,035 | call_wall_resistance | +4.26 |
| 280 | 10,880 | 3 | +10,877 | 10,883 | call_wall_resistance | +32.69 |
| 270 | 10,069 | 670 | +9,399 | 10,739 | call_wall_resistance | +27.95 |
| 160 | 2 | 9,109 | −9,107 | 9,111 | put_wall_support | −24.18 |
| 200 | 2,147 | 5,326 | −3,179 | 7,473 | put_wall_support | −5.22 |

Per the standing pitfall, this aggregate is **structurally misleading**: eight
of ten rows sit 14–52% from spot, and the 300/320/260/280 "walls" with **zero
put OI** are the long-dated LEAP call inventory (cross-reference the 22,142
Jan-2028 calls below), not resistance any 21-day move will meet.

**Tradeable map** (`--dte-max 30`) — this is what phase 9 should size against:

| Strike | Call OI | Put OI | Net OI | Total | Role | Dist % |
|-------:|--------:|-------:|-------:|------:|------|-------:|
| 250 | 2,802 | 3,695 | −893 | 6,497 | put_heavy | +18.47 |
| 280 | 4,250 | 0 | +4,250 | 4,250 | call_wall_resistance | +32.69 |
| **220** | 1,400 | 2,316 | **−916** | 3,716 | **put_heavy** | **+4.26** |
| **200** | 777 | 2,588 | **−1,811** | 3,365 | **put_wall_support** | **−5.22** |
| 300 | 3,354 | 0 | +3,354 | 3,354 | call_wall_resistance | +42.17 |
| **190** | 126 | 3,166 | **−3,040** | 3,292 | **put_wall_support** | **−9.96** |
| **217.5** | 3,172 | 33 | **+3,139** | 3,205 | **call_wall_resistance** | **+3.07** |
| **210** | 1,015 | 1,447 | −432 | 2,462 | put_wall_support | **−0.48** |
| 240 | 1,489 | 695 | +794 | 2,184 | call_wall_resistance | +13.73 |
| 165 | 0 | 2,112 | −2,112 | 2,112 | put_wall_support | −21.81 |

Three readings:

1. **$217.5 is the only clean near-term call wall** — net_oi **+3,139** on
   3,172 calls against just 33 puts, **+3.07%** above spot. It sits between
   the current 211.03 and phase-2's institutional block level at **$214.00**,
   making 214–217.5 the first genuine overhead congestion band.
2. **The 220 role tag flips with tenor.** All-expiry it reads
   `call_wall_resistance` (+2,509); inside 30 days it is `put_heavy`
   (**−916**). Phase 9 must not label 220 as resistance — near-term it is a
   two-sided battleground, exactly the mislabelling the pitfall warns about.
3. **Support is layered and put-backed: 210 (−432, essentially at spot) →
   200 (−1,811) → 190 (−3,040).** Put support *thickens* as price falls,
   which is the normal protective-hedge ladder rather than directional bearish
   positioning. It aligns closely with phase-2's dark-pool shelf at
   205.83–206.01 and 202.59.

### OI term structure — the OPEX-cliff lens

15 expiries, 224,381 tracked contracts:

| Expiry | DTE | Call OI | Put OI | Total | P/C | % of total | Contracts |
|--------|----:|--------:|-------:|------:|----:|-----------:|----------:|
| 2026-07-31 | 0 | 9,678 | 5,698 | 15,376 | 0.589 | 6.85 | 68 |
| 2026-08-07 | 7 | 1,232 | 1,852 | 3,084 | 1.503 | 1.37 | 40 |
| 2026-08-14 | 14 | 1,042 | 390 | 1,432 | 0.374 | 0.64 | 30 |
| **2026-08-21** | **21** | 13,812 | **16,110** | **29,922** | **1.166** | **13.34** | 45 |
| 2026-08-28 | 28 | 502 | 394 | 896 | 0.785 | 0.40 | 16 |
| 2026-09-04 | 35 | 210 | 48 | 258 | 0.229 | 0.11 | 13 |
| 2026-09-11 | 42 | 14 | 3 | 17 | 0.214 | 0.01 | 6 |
| **2026-09-18** | **49** | **43,524** | 16,639 | **60,163** | **0.382** | **26.81** | 31 |
| 2026-10-16 | 77 | 1,775 | 946 | 2,721 | 0.533 | 1.21 | 19 |
| 2026-12-18 | 140 | 16,301 | 8,605 | 24,906 | 0.528 | 11.10 | 22 |
| **2027-01-15** | 168 | 27,604 | 25,334 | **52,938** | 0.918 | **23.59** | 23 |
| 2027-03-19 | 231 | 3,508 | 137 | 3,645 | 0.039 | 1.62 | 13 |
| 2027-06-17 | 321 | 774 | 569 | 1,343 | 0.735 | 0.60 | 15 |
| **2028-01-21** | 539 | **22,142** | **0** | 22,142 | **0.000** | 9.87 | **4** |
| 2028-06-16 | 686 | 5,538 | 0 | 5,538 | 0.000 | 2.47 | 2 |

**The cliff is 2026-09-18** at 26.81% — and it is emphatically **call-side**
(P/C 0.382; 43,524 calls). Combined with 2027-01-15 (23.59%), just two
expiries hold **half of all tracked OI**.

**The near-term picture inverts this.** The tradeable expiries are
put-skewed: **Aug-21 P/C 1.166** (16,110 puts vs 13,812 calls) and **Aug-07
P/C 1.503**. So FSLR carries **near-term protection and far-term upside** — a
classic institutional shape: hedged through the next month, structurally long
beyond it.

**2028-01-21 is remarkable**: 22,142 calls, **zero puts**, across just **4
strikes** (260: 3,457 · 300: 7,018 · 320: 10,996 · 400: 671). That is a pure,
concentrated long-dated call position — and it is a *different* set of strikes
from the 450/460 legs traded today (`phase-1-flow.md`), which the dataset does
not track. The Jan-2028 LEAP franchise is therefore **larger than either
phase can see alone**.

Also note the 2027-03-19 line: P/C **0.039**, 3,508 calls vs 137 puts — the
expiry into which phase-1's $790,000 Mar-27 $410 call purchase landed.

### Largest OI increases (reflecting 2026-07-30)

Only **2** contracts cleared the `--min-oi-change 500` threshold — itself
evidence that 07-30 was not a heavy position-building session. Side and expiry
parsed from the OPRA `option_symbol` (the rows carry neither column):

| `option_symbol` | Parsed | Strike | Type | DTE | last_oi | curr_oi | **OI Δ** | `oi_change` | Volume | Avg px |
|---|---|---:|:--:|---:|--------:|--------:|---------:|------------:|-------:|-------:|
| `FSLR260918C00220000` | 2026-09-18 Call | 220 | C | 49 | 996 | **1,981** | **+985** | 0.9890 | 1,082 | $16.32 |
| `FSLR260731C00250000` | 2026-07-31 Call | 250 | C | 0 | 188 | 751 | +563 | 2.9947 | 634 | $0.13 |

The Jul-31 $250 call is **0DTE at $0.13** — expiring worthless today, pure
lottery noise; discard.

**The one real build is Sep-18 $220 calls: +985 contracts, a 98.9% doubling,
on 1,082 volume** — meaning the position was opened almost entirely fresh
(vol/OI-change ≈ 1.1). At $16.32 average price that is roughly **$1.61M**
committed. It lands in the 26.81% cliff expiry at a strike **+4.26%** from
spot. Note `oi_change` is the **ratio** (0.9890), not the delta — the delta is
`oi_diff_plain` = 985.

**Float normalization:** 985 × 100 = 98,500 shares = **0.0971% of the 101.48M
float**. For comparison, today's untracked Aug-21 $230 block is 1,900 × 100 =
190,000 shares = **0.187% of float**. Both are **tactical, not structural** —
in a 101.48M-float S&P 500 name neither size compels a re-rating.

### Closing / roll activity

`decrease-with-volume` returned **one** row:

| `option_symbol` | Parsed | last_oi | curr_oi | OI Δ | Volume | Avg px |
|---|---|--------:|--------:|-----:|-------:|-------:|
| `FSLR260821C00250000` | 2026-08-21 Call 250 | 2,024 | 1,662 | **−362** | 828 | $3.90 |

828 contracts traded to close 362 — roughly 2.3 volume per unit of OI
reduction, i.e. **two-way trading around a shrinking position**, not a clean
liquidation. Aug-21 $250 is +18.47% from spot; letting it go is consistent
with a holder abandoning a strike that the post-earnings move did not bring
into reach.

`position-rolls --threshold 500 --near-dte-max 30` returned
**`rolls_detected: 0`** with the tool's own caveat: *"Single-day detection
only — cross-session rolls are not captured."*

**This is a false negative, and an instructive one.** `phase-1-flow.md`
documents an unmistakable roll executed **today**: 1,000 Jan-28 $460C + 1,000
Mar-27 $410C bought at 12:48:15 ET against 1,000 Jan-28 $450C + 1,000 Jun-27
$340C sold at 14:15:31 ET, for a **$1.374M net credit**. The tool missed it
for two compounding reasons — the OI lag means today's legs are invisible, and
the roll's near leg (Jun-2027, 321 DTE) is far outside `--near-dte-max 30`.
**`position-rolls` should not be read as evidence that no rolling occurred.**

### Smart positioning (inferred direction)

| `option_symbol` | Strike/Type | DTE | OI Δ | `prev_ask_volume` | `prev_bid_volume` | `net_ask_bid` | Inferred |
|---|---|---:|-----:|------------------:|------------------:|--------------:|----------|
| `FSLR260918C00220000` | 220 C | 49 | +985 | 14 | 66 | **−52** | **bearish** |
| `FSLR260731C00250000` | 250 C | 0 | +563 | 224 | 222 | +2 | bullish |

**The "bearish" tag on the Sep-18 $220 build is very weak evidence and should
not be carried forward at face value.** The inference rests on
`net_ask_bid = −52`, drawn from just **80 classified contracts (14 ask + 66
bid) out of 1,082 total volume — 7.4% of the tape on that chain**. The other
92.6% is unclassified. Reading a $1.6M position's intent from 80 contracts is
not a reliable signal.

If it *were* right, the interpretation would be **call writing against stock**
— which would sit naturally beside phase-2's regular-session accumulation
(institutions buying stock and selling upside), and is exactly the
"covered-call writing" signature in this phase's heuristics. If it is wrong,
it is a straightforward long-call position in the cliff expiry. **Phase 8b
should treat this as genuinely unresolved**; the second row's "bullish" tag is
meaningless (0DTE, `net_ask_bid = +2`).

### Pin risk

**FSLR is outside the top-25** on `pin-risk --dte-max 7 --max-distance-pct 5`
(list headed by SPY: spot 746.81, `dte_to_opex` 0, `pin_score` 2,148,293).

Correct and expected: **2026-08-21 is the next monthly OPEX, 21 days out** —
well beyond the 7-day window. Today's 0DTE weekly carried 15,376 contracts
(6.85% of tracked OI) but expires into the close. **No pin commentary
applies**, and phase 9 should not build a pin thesis. The relevant pin date is
**2026-08-21**, and it should be re-examined nearer the event.

### OPEX concentration

**FSLR is outside the top-20** on
`opex-concentration --min-concentration-pct 40` (list headed by AIOT at 100%
concentration on 1,550 OI).

This is a **positive structural finding, not a null result**: FSLR's most
concentrated expiry is 2026-09-18 at **26.81%**, comfortably below the 40%
threshold, with OI spread across 15 expiries. **There is no OI cliff to
create a mechanical unwind or a gamma air-pocket at any single expiry.** For
phase 9 this means expiry-date selection is relatively unconstrained — no
single date carries destabilising concentration.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|------------------|--------------------------------|-----------|
| `uw oi biggest-increases --symbol FSLR --top-n 20 --min-oi-change 500 --date 2026-07-31 --json` | `FSLR260918C00220000`: oi_diff_plain=985, curr_oi=1981, last_oi=996, oi_change=0.98896, volume=1082, avg_price=16.3178 ← `.results[0]` | 2 |
| `uw oi decrease-with-volume --symbol FSLR --top-n 15 --min-volume 100 --date 2026-07-31 --json` | `FSLR260821C00250000`: oi_diff_plain=−362, curr_oi=1662, volume=828 ← `.results[0]` | 1 |
| `uw oi smart-positioning --symbol FSLR --top-n 20 --min-oi-change 500 --date 2026-07-31 --json` | inferred_direction="bearish", net_ask_bid=−52, prev_ask_volume=14, prev_bid_volume=66 ← `.results[0]` | 2 |
| `uw oi position-rolls --symbol FSLR --threshold 500 --near-dte-max 30 --date 2026-07-31 --json` | `rolls_detected=0`, `results=[]`, caveat="Single-day detection only" ← `.rolls_detected`, `.caveat` | 0 |
| `uw oi oi-by-strike --symbol FSLR --top-n 10 --date 2026-07-31 --json` | strike 300: call_oi=26638, put_oi=0, net_oi=26638, role="call_wall_resistance", distance_pct=42.17 ← `.results[0]` | 10 |
| `uw oi oi-by-strike --symbol FSLR --top-n 10 --dte-max 30 --date 2026-07-31 --json` | 217.5: net_oi=+3139, role="call_wall_resistance", distance_pct=3.07; 220: net_oi=−916, role="put_heavy"; spot=211.02 ← `.results[]`, `.spot` | 10 |
| `uw oi term-structure --symbol FSLR --date 2026-07-31 --json` | 2026-09-18: total_oi=60163, pct_of_total_oi=26.81, put_call_oi_ratio=0.382 ← `.term_structure[7]` (**results live under `.term_structure`, not `.results`**); expiry_count=15 | 15 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-07-31 --json` | FSLR = null ← `[.results[].ticker]\|index("FSLR")`; SPY pin_score=2148292.93 ← `.results[0]` | 25 (market-wide) |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-07-31 --json` | FSLR = null ← same path; AIOT concentration_pct=100 ← `.results[0]` | 20 (market-wide) |
| DuckDB on `OI changes/chain-oi-changes-2026-07-31.parquet` | **`last_date`=2026-07-30, `curr_date`=2026-07-31**, n=348 | 348 |
| DuckDB strike-230 chain scan | `FSLR260821C00230000`: curr_oi=255, last_oi=239, volume=**28** (vs 1,937 today) | 13 |
| DuckDB Jan-2028 scan | strikes 260/300/320/400 → OI 3,457/7,018/10,996/671 = **22,142**, zero puts; **450 & 460 absent** | 4 |
| DuckDB net OI change by type (type parsed from OPRA `substr`) | calls +6,117 on 12,167 vol; puts +3,514 on 6,702 vol | 348 |

## Tool errors

No command errored — all nine exited 0 and every payload parsed.

Four structural findings that downstream phases must not mistake for signal:

1. **`uw oi term-structure` returns its rows under `.term_structure`, not
   `.results`.** A `.results | length` check reports **0 rows** on a fully
   populated response. Caught before any number was written.
2. **The OI changes parquet has no `option_type` column** — a first query
   referencing it raised
   `Binder Error: Referenced column "option_type" not found in FROM clause!`
   Type and expiry must be parsed from the OPRA `option_symbol`, exactly as
   the phase-3 guidance specifies.
3. **The dataset covers 38.9% of FSLR's open interest** (224,381 tracked vs
   577,414 reported). Every wall, cliff and percentage in this phase describes
   the most-active 348 contracts, not the full chain.
4. **`position-rolls` returned a false negative** (0 rolls on a day phase 1
   documented a $4.07M-credit roll) — see §Closing / roll activity.

## DATA NOTE / CORRECTION

**No correction to prior phases; one significant limitation on this one.**

`phase-1-flow.md` closed with: *"Does Aug-21 $230 open in OI? → phase 3. This
is the single highest-value verification in the run."* **Phase 3 cannot
perform it.** The OI snapshot predates the trade by one session. Any claim
that phase 3 corroborated phase 1's block would be fabrication.

The verification instead came from `phase-2-dark-pool.md` — the QCT delta
hedge, 49.0s lag, 101.1% size match, dealer paying **above the ask** — which
is *stronger* evidence than an OI print because it identifies which side the
dealer took. The open item that remains for **2026-08-03** is narrow
confirmation: does `FSLR260821C00230000` OI print near **2,155**?

Note also that `uw insights deep-dive`'s `total_open_interest` of 577,414
(quoted in `phase-0.5-context.md`) and this phase's 224,381 are **not
contradictory** — they measure different universes. Phase 10 should not flag
them as an internal inconsistency.

## Verdict for downstream phases

- **Bias from this phase:** **mildly bullish, structurally — with near-term
  protection.** Far-dated OI is overwhelmingly call-side (Sep-18 P/C 0.382;
  Jan-2028 22,142 calls / zero puts; Mar-2027 P/C 0.039) while the tradeable
  1–3 week window is put-skewed (Aug-21 P/C 1.166, Aug-07 P/C 1.503) and
  support thickens downward (210 → 200 → 190). The market is **hedged into
  August and long into 2027–28.**
- **Conviction: 2 / 5.** Capped hard by the one-session lag — this phase
  describes 07-30, cannot see today's two largest trades, and covers 38.9% of
  the chain. The lone qualifying build (+985) is real but modest, and its
  directional tag rests on 7.4% of that chain's volume.
- **Largest OI build as % of float:** **0.0971%** (985 contracts × 100 ÷
  101.48M shares). Today's untracked Aug-21 $230 block would be **0.187%**.
  **Neither is structural for this name** — both are tactical positions that a
  101.48M-float S&P 500 constituent absorbs without re-rating. Nothing in the
  OI data compels a size increase.
- **Three pin/cliff strikes for phase-9 entry/stop reference** (sourced from
  `oi-by-strike` roles and the `term-structure` cliff, not hand-picked):
  1. **$217.5 — `call_wall_resistance`, net_oi +3,139, +3.07%** (dte ≤ 30).
     The only clean near-term call wall. Stacked with phase-2's $214.00
     institutional block, it defines a **214.00–217.50 overhead band** —
     the first real resistance and a natural first target / partial-exit zone.
  2. **$200 — `put_wall_support`, net_oi −1,811, −5.22%** (dte ≤ 30), backed
     by **$190** (net_oi −3,040, −9.96%). Confirmed independently by phase-2's
     dark-pool shelf at 205.83–206.01 → 202.59. **A stop placed above $200
     sits inside the protective ladder rather than beneath it** — phase 9
     should weigh whether that is intended.
  3. **2026-09-18 — the OPEX cliff, 26.81% of tracked OI, P/C 0.382**, 49 DTE.
     The gravity well for any expiry choice, and the expiry where the sole
     qualifying OI build (Sep-18 $220 +985) sits. Cross-check against phase-4
     max-pain and phase-6's catalyst calendar.
- **Open questions:**
  - **Is the Sep-18 $220 call build speculative or covered?** `smart-positioning`
    infers bearish (call writing) from 80 of 1,082 contracts — too thin to
    trust. If it is covered-call writing against the stock phase 2 shows
    institutions accumulating, the two phases describe **one** integrated
    trade (long stock / short upside), which would meaningfully cap phase-9's
    target. → phase 4 GEX and phase 8b.
  - **Does `FSLR260821C00230000` OI print ≈ 2,155 on 2026-08-03?** The one
    clean falsification test available. Until then the block's opening status
    rests solely on phase-2's hedge inference.
  - **How large is the untracked LEAP position?** The tracked Jan-2028 book is
    22,142 calls across 4 strikes with zero puts; today's 450/460 legs are
    invisible to this dataset. The true long-dated call franchise is larger
    than 9.87% of OI suggests, and phase-4 GEX computed on the tracked subset
    will understate far-dated dealer exposure.
  - **Why is Aug-07 P/C 1.503 with only 3,084 OI?** A small, sharply
    put-skewed one-week expiry immediately after a print is unusual — residual
    earnings hedges left unclosed, or a fresh short-dated bearish view?
    → phase 4.
