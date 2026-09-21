# Phase 3 — Open Interest & Positioning

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T01:42:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`

## Summary

**One position dominates the entire chain, it is bearish, it is long-dated, and it was
opened hours before the earnings release.** The largest OI change is
**`ENPH280121P00030000` — Jan-2028 $30 puts, +2,000 contracts (`last_oi` 2,361 →
`curr_oi` 4,361, +84.7%)** — built on **`prev_ask_volume` 2,908 vs `prev_bid_volume` 253**
(`net_ask_bid` **+2,655**) for **`prev_total_premium` $2,837,716** at an average $8.97.
`smart-positioning` labels it `inferred_direction` **bearish**. Premium-weighted, the five
qualifying OI builds run **$2,910,482 bearish vs $535,495 bullish — 5.4 : 1**.

**That $2.84M is ~6× the entire day's net option flow** (−$479,813, `phase-1-flow.md`)
and **2.5× the whole top-25 print tape** ($1,149,093). It is the single most economically
meaningful positioning fact in this run, and it is the *only* place in six phases where
ENPH's numbers stop being trivial.

**Timing — established, not assumed.** OI reported for 2026-07-29 reflects **07-28's**
trading (the documented one-session lag). Verified directly: the largest 07-29 print in
`top-premium-trades` is $196,240, so a $2.84M trade cannot be a 07-29 event; querying
`top-premium-trades --date 2026-07-28` returns a **cluster of ask-side Jan-2028 P30
purchases — $438,300 / $231,287 / $111,625 / $99,000 / $85,920 = $966,132 across 1,077
contracts in the top-10 alone, all at $8.93–$9.00.** Since ENPH reported **postmarket on
07-28**, this position was **opened before the release**. It also reconciles
`phase-1-flow.md`'s unexplained 07-28 `net_flow` of **−$3,162,110** — the P30 buying is
~90% of it. Consequence: **today's flow is not yet in OI.** The Oct-16 P35 and Aug-07 C37
buys land in tomorrow's snapshot; every wall below is as of the 07-28 close.

**The near-term structure offers less support than the phase-0 carry implied.** Spot 35.07
sits **−0.17%** from the 35 strike, whose all-expiry profile is `put_wall_support`
(`call_oi` 7,770 / `put_oi` **25,340**, `net_oi` −17,570). But the *tradeable* wall is
thinner than that headline: the Aug-21 monthly holds only **4,031** puts at 35 (up just
**+297** from the 3,734 in `phase-0-intake.md`'s carry, **+8.0%** — a modest build, not a
fortification), and the **07-31 front expiry holds just 721 puts and 24 calls at 35**.
ENPH is **absent from `pin-risk` top-25** (cutoff `pin_score` 157,865) and **absent from
`opex-concentration`** (max concentration 24.95% < the 40% filter). **There is no Friday
pin.** The front expiry's 26,693 OI is 19,447 calls stacked at **42.5 / 45 / 50** — all
21–43% OTM with 2 days left, i.e. **worthless**. The "positive-gamma island" that
`phase-0-intake.md` carried forward is a pile of dead calls, so its expiry removes very
little gamma near spot.

`position-rolls` returned **zero** rows — no near→far rolling. Combined with
`phase-2-dark-pool.md` (distribution, `sell_ratio` 0.610) and `phase-1-flow.md` (whole-tape
puts bought 1.569×, calls flat), positioning is a **fourth independent lane agreeing on
direction** — and the first one with real size behind it.

## Key signals

- **`ENPH280121P00030000` +2,000 OI (+84.7%), `prev_total_premium` $2,837,716,
  `net_ask_bid` +2,655, `inferred_direction` bearish, `dte` 541** — the chain's dominant
  position, opened **pre-print on 07-28** [OI:biggest_increases + OI:smart_positioning]
- **Premium-weighted OI builds: $2,910,482 bearish vs $535,495 bullish (5.4 : 1)**
  [OI:smart_positioning]
- **Spot is on the 35 strike (`distance_pct` −0.17%)**, all-expiry `role`
  `put_wall_support`, `net_oi` **−17,570** (7,770 calls / 25,340 puts)
  [OI:oi_by_strike]
- **But the Aug-21 wall at 35 is only 4,031 puts (+297 / +8.0% vs the prior run) and the
  07-31 wall is 721 puts** — thin where it matters [OI:oi_by_strike --expiry]
- **No Friday pin: ENPH absent from `pin-risk` top-25** (cutoff 157,865); front-expiry OI
  near spot is negligible [OI:pin_risk]
- **Near-term OPEX cliff = 2026-08-21, `pct_of_total_oi` 15.69%** (46,288 OI, `dte` 23,
  `put_call_oi_ratio` 0.891). The *largest* cliff is **2027-01-15 at 24.95%** but it is a
  `dte` 170 LEAP, not tradeable gravity [OI:term_structure]
- **07-31's 19,447 calls are junk** — stacked at 42.5 (3,941) / 45 (2,048) / 50 (4,035),
  21–43% OTM with `dte` 2 [OI:oi_by_strike --expiry 2026-07-31]
- **Legacy call OI far overhead:** 87,033 calls across strikes 50–70 all-expiry, all
  `call_wall_resistance` at `distance_pct` +42.6% to +99.7% — relics of the 73.74 52-week
  high, not live resistance [OI:oi_by_strike]
- **Only one meaningful decrease: `ENPH260821C00065000` −1,111** (3,407 → 2,296) — closing
  dead Aug calls [OI:decrease_with_volume]
- **`position-rolls` = 0 rows** — nobody is rolling exposure forward [OI:position_rolls]
- **Largest build = 0.157% of float** share-equivalent (2,000 × 100 / 127.77M)
  [OI:oi_pct_float fz]

## Detailed findings

### A — OI walls by strike

**All-expiry aggregate** (`uw oi oi-by-strike --symbol ENPH --top-n 10`). Spot 35.07.

| Strike | `call_oi` | `put_oi` | `net_oi` | `total_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|---|
| **35** | 7,770 | **25,340** | **−17,570** | **33,110** | **`put_wall_support`** | **−0.17%** |
| 40 | 10,796 | 21,073 | −10,277 | 31,869 | `put_heavy` | +14.09% |
| 45 | 10,554 | 19,101 | −8,547 | 29,655 | `put_heavy` | +28.35% |
| 70 | 22,918 | 1,844 | +21,074 | 24,762 | `call_wall_resistance` | +99.66% |
| 30 | 1,994 | **22,446** | −20,452 | 24,440 | `put_wall_support` | −14.43% |
| 50 | 20,828 | 1,540 | +19,288 | 22,368 | `call_wall_resistance` | +42.61% |
| 60 | 19,047 | 503 | +18,544 | 19,550 | `call_wall_resistance` | +71.14% |
| 55 | 13,218 | 2,088 | +11,130 | 15,306 | `call_wall_resistance` | +56.87% |
| 65 | 11,022 | 442 | +10,580 | 11,464 | `call_wall_resistance` | +85.40% |
| 25 | 285 | 9,463 | −9,178 | 9,748 | `put_wall_support` | −28.69% |

Two structural facts, and one trap the spec warns about:

1. **The 35 strike is the single heaviest in the chain (33,110) and spot is sitting on it.**
   `net_oi` −17,570 is genuinely put-dominated (3.26 puts per call), so the
   `put_wall_support` tag is not a mislabelled battleground. **Whether it acts as support
   depends on who owns the puts**, which `oi-by-strike` cannot say — see §H.
2. **The 50–70 "resistance walls" are relics, not live levels.** 87,033 calls sit at
   `distance_pct` +42.6% to +99.7%, against a 52-week high of **73.74** and a 52-week low
   of **25.775** (`phase-0.5-context.md`). These were written or bought when ENPH traded
   far higher; at spot 35.07 they are inert. Quoting "call wall at 70" as resistance for a
   1–4 week horizon would be meaningless. Per the spec's pitfall, the `role` tag is a
   call/put-split heuristic and says nothing about distance relevance.

**Tradeable-horizon map** (`--dte-max 30`) — what phase 9 actually sizes against:

| Strike | `call_oi` | `put_oi` | `net_oi` | `total_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|---|
| **40** | 1,955 | **8,124** | −6,169 | **10,079** | `put_heavy` | +14.09% |
| 45 | 4,408 | 3,283 | +1,125 | 7,691 | `call_wall_resistance` | +28.35% |
| 50 | 7,288 | 81 | +7,207 | 7,369 | `call_wall_resistance` | +42.61% |
| **35** | 1,073 | **5,009** | **−3,936** | **6,082** | **`put_wall_support`** | **−0.17%** |
| 55 | 3,193 | 2,029 | +1,164 | 5,222 | `call_wall_resistance` | +56.87% |
| 30 | 362 | 4,238 | −3,876 | 4,600 | `put_wall_support` | −14.43% |
| 60 | 4,238 | 0 | +4,238 | 4,238 | `call_wall_resistance` | +71.14% |
| 42.5 | 4,103 | 1 | +4,102 | 4,104 | `call_wall_resistance` | +21.22% |
| 75 | 3,295 | 13 | +3,282 | 3,308 | `call_wall_resistance` | +113.92% |
| 65 | 2,494 | 442 | +2,052 | 2,936 | `call_wall_resistance` | +85.40% |

**Inside 30 days the 35 wall shrinks from 33,110 to 6,082 total OI (5,009 puts).** The
all-expiry headline overstates near-term support by **5.4×** — precisely the trap flagged
in the spec's pitfall list. And **40 outranks 35** on near-term OI (10,079 vs 6,082), with
8,124 puts: the heaviest tradeable put concentration is **14% above spot**, i.e. puts that
are now deep in the money.

**Per-expiry decomposition of the 35 strike** — the number phase 9 needs:

| Expiry | `dte` | `call_oi` @35 | `put_oi` @35 | Total @35 |
|---|---|---|---|---|
| **2026-07-31** | 2 | **24** | **721** | **745** |
| 2026-08-21 | 23 | 699 | **4,031** | 4,730 |
| 2026-09-18 | 51 | — | **8,970** (from `biggest-increases` `curr_oi`) | — |
| All expiries | — | 7,770 | 25,340 | 33,110 |

- **Aug-21 $35 put OI is 4,031, versus 3,734 in `phase-0-intake.md`'s carry from the
  07-27 run: +297 contracts, +8.0%.** A modest build through a binary event — **not** a
  fortification. Anyone expecting the put wall to have been reinforced into the print will
  not find it here.
- **Aug-21 $40 put OI is 7,839 versus 7,888 carried: −49, flat.** The $40 wall is
  unchanged and is now **14% in the money**.
- **The 07-31 expiry has effectively nothing at 35** (721 puts, 24 calls). Friday's
  expiry cannot pin spot and its roll-off removes almost no gamma near the money.

**Aug-21 monthly, full strike map** (`--expiry 2026-08-21`, the near-term cliff):

| Strike | `call_oi` | `put_oi` | `net_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|
| **40** | 866 | **7,839** | −6,973 | `put_heavy` | +14.09% |
| 45 | 2,226 | 3,146 | −920 | `put_heavy` | +28.35% |
| **35** | 699 | **4,031** | −3,332 | `put_wall_support` | −0.17% |
| 60 | 3,992 | 0 | +3,992 | `call_wall_resistance` | +71.14% |
| 55 | 1,977 | 1,997 | −20 | `put_heavy` | +56.87% |
| **30** | 305 | **2,963** | −2,658 | `put_wall_support` | −14.43% |
| 50 | 3,045 | 0 | +3,045 | `call_wall_resistance` | +42.61% |
| 75 | 3,030 | 13 | +3,017 | `call_wall_resistance` | +113.92% |
| 65 | 2,296 | 442 | +1,854 | `call_wall_resistance` | +85.40% |
| 90 | 2,022 | 0 | +2,022 | `call_wall_resistance` | +156.70% |

The Aug-21 expiry is **put-dominated at every strike within 30% of spot** (40, 35, 30 all
put-heavy; 45 too) while its call OI sits at 50/60/65/75/90 — dead strikes. `phase-3`'s
tradeable structure is therefore **puts near the money, calls in the stratosphere**.

**07-31 front expiry** (`--expiry 2026-07-31`, `dte` 2) — the junk-call finding:

| Strike | `call_oi` | `put_oi` | `role` | `distance_pct` |
|---|---|---|---|---|
| 50 | **4,035** | 81 | `call_wall_resistance` | +42.61% |
| 42.5 | **3,941** | 0 | `call_wall_resistance` | +21.22% |
| 45 | 2,048 | 128 | `call_wall_resistance` | +28.35% |
| 55 | 1,153 | 32 | `call_wall_resistance` | +56.87% |
| 40 | 854 | 0 | `call_wall_resistance` | +14.09% |
| 30 | 56 | 723 | `put_wall_support` | −14.43% |
| 35 | 24 | 721 | `put_wall_support` | −0.17% |
| 33 | 1 | 741 | `put_wall_support` | −5.88% |
| 32 | 0 | 692 | `put_wall_support` | −8.73% |
| 38 | 405 | 169 | `call_wall_resistance` | +8.39% |

**11,177 of the front expiry's 19,447 calls sit at 42.5 / 45 / 50 / 55** — 21% to 57% OTM
with two sessions to run. They will expire worthless. The put side is a thin ladder
(721 + 741 + 692 + 723 = 2,877 across 30/32/33/35). **This materially revises
`phase-0-intake.md`'s carried expectation** that Friday's expiry retires a meaningful
"positive-gamma island (`today_total_gex` +1,047,168)": the gamma being retired is almost
entirely from contracts with ~zero delta and ~zero gamma at spot 35.07. Phase 4 must
verify against live GEX rather than inheriting that framing.

### B — OI term structure

`uw oi term-structure --symbol ENPH` → `expiry_count` **15**, `total_oi` **294,987**.
(Note: the payload key is **`.term_structure`**, not `.results` — see `## Tool errors`.)

| Expiry | `dte` | `call_oi` | `put_oi` | `total_oi` | `put_call_oi_ratio` | `pct_of_total_oi` | contracts |
|---|---|---|---|---|---|---|---|
| 2026-07-31 | 2 | 19,447 | 7,246 | 26,693 | **0.373** | **9.05%** | 82 |
| 2026-08-07 | 9 | 2,073 | 1,281 | 3,354 | 0.618 | 1.14% | 55 |
| 2026-08-14 | 16 | 857 | 545 | 1,402 | 0.636 | 0.48% | 35 |
| **2026-08-21** | **23** | 24,477 | 21,811 | **46,288** | 0.891 | **15.69%** | 52 |
| 2026-08-28 | 30 | 838 | 576 | 1,414 | 0.687 | 0.48% | 32 |
| 2026-09-04 | 37 | 245 | 324 | 569 | 1.322 | 0.19% | 24 |
| **2026-09-18** | **51** | 23,851 | 23,782 | **47,633** | **0.997** | **16.15%** | 19 |
| 2026-10-16 | 79 | 2,774 | 1,985 | 4,759 | 0.716 | 1.61% | 13 |
| 2026-11-20 | 114 | 6,687 | 5,389 | 12,076 | 0.806 | 4.09% | 18 |
| 2026-12-18 | 142 | 8,436 | 12,913 | 21,349 | **1.531** | 7.24% | 19 |
| **2027-01-15** | **170** | **54,964** | 18,631 | **73,595** | **0.339** | **24.95%** | 27 |
| 2027-02-19 | 205 | 616 | 399 | 1,015 | 0.648 | 0.34% | 13 |
| 2027-06-17 | 323 | 17,396 | 15,690 | 33,086 | 0.902 | 11.22% | 19 |
| 2028-01-21 | 541 | 10,489 | 5,799 | 16,288 | 0.553 | 5.52% | 17 |
| 2028-12-15 | 870 | 4,131 | 1,335 | 5,466 | 0.323 | 1.85% | 19 |

**The largest cliff is not the tradeable one.** `2027-01-15` holds **24.95%** of all OI,
but at `dte` **170** with `put_call_oi_ratio` **0.339** (54,964 calls) it is a LEAP
warehouse — the same legacy call inventory as the 50–70 strike walls in §A. It exerts no
near-term gravity.

**The tradeable cliff is `2026-08-21`: 15.69% of total OI, 46,288 contracts, `dte` 23,
`put_call_oi_ratio` 0.891.** It is the first monthly after the event, it holds the heaviest
near-money put OI (7,839 at 40; 4,031 at 35; 2,963 at 30), and it matches the catalyst
calendar carried in `phase-0-intake.md` (monthly OPEX, both structures expiring). **This is
the expiry phase 9 should anchor a 1–4 week horizon to.**

`2026-09-18` is marginally larger (16.15%, 47,633) and is the **most balanced expiry in the
chain** (`put_call_oi_ratio` **0.997** — 23,851 calls vs 23,782 puts). It also holds the
largest single-expiry put position at the 35 strike (**8,970**, §C). At `dte` 51 it is the
natural second anchor and the likely home of the 07-23 put-writing position
(`phase-1-flow.md` open question — see §H).

**Curve shape:** near-dated expiries are **call-skewed** (07-31 at 0.373), the 3–8 week
zone is **balanced-to-put-heavy** (08-21 0.891, 09-18 0.997), and the 4–5 month zone turns
**put-heavy** (12-18 at **1.531**) before reverting to call-dominated LEAPs (01-15 0.339,
12-15-28 0.323). Read against `phase-1-flow.md` §D — where $405,922 of long-dated calls
(Sep C40, Jan-27 C55, Jan-28 C75) were **written** — the picture is coherent: **the
call-heavy long end is inventory being sold, and the put-heavy middle is protection being
bought.**

**Coverage caveat.** `term-structure`'s `total_oi` of **294,987** is **77.4%** of the
`total_open_interest` **381,215** reported by `insights deep-dive`
(`phase-0.5-context.md`; screener `call_open_interest` 221,652 + `put_open_interest`
159,563 = 381,215). Its `source` is `chain-oi-changes-2026-07-29.parquet`, which appears
to carry only contracts with recorded OI activity. `pct_of_total_oi` therefore sums to
100% **of the 294,987 subset**, not of the true chain. Percentages above are internally
consistent and usable for *relative* cliff ranking; they must **not** be quoted as
fractions of total ENPH OI.

### C — Largest OI increases

`uw oi biggest-increases --symbol ENPH --top-n 20 --min-oi-change 500` → **5 rows only**.
Side and expiry parsed from `option_symbol` (OPRA), per the spec — these rows carry no
`side` or `expiry` column. `net_ask_bid` and `inferred_direction` are joined from
`smart-positioning`, which returned the **same 5 contracts**.

| `option_symbol` | Parsed | `dte` | `last_oi` → `curr_oi` | `oi_diff_plain` | `oi_change` | vol | `prev_ask_vol` | `prev_bid_vol` | `net_ask_bid` | `prev_total_premium` | avg px | `inferred_direction` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **`ENPH280121P00030000`** | **2028-01-21 P30** | **541** | 2,361 → **4,361** | **+2,000** | +84.7% | 3,162 | **2,908** | 253 | **+2,655** | **$2,837,716** | $8.97 | **bearish** |
| `ENPH260918C00070000` | 2026-09-18 C70 | 51 | 1,940 → 3,544 | +1,604 | +82.7% | 1,935 | 1,888 | 37 | +1,851 | $55,196 | $0.29 | bullish |
| `ENPH260918P00035000` | 2026-09-18 P35 | 51 | 8,085 → **8,970** | +885 | +10.9% | 1,048 | 348 | **639** | **−291** | $432,888 | $4.13 | **bullish** (sold) |
| `ENPH260731C00045000` | 2026-07-31 C45 | 2 | 1,240 → 2,048 | +808 | +65.2% | 2,130 | 668 | **1,201** | **−533** | $72,766 | $0.34 | **bearish** (sold) |
| `ENPH260731P00032000` | 2026-07-31 P32 | 2 | 94 → 692 | +598 | +636% | 735 | 165 | **491** | −326 | $47,411 | $0.65 | bullish (sold) |

**Premium-weighted direction — the number that matters:**

| Direction | Contracts | Premium |
|---|---|---|
| **Bearish** | 2028 P30 (+2,000) · 07-31 C45 (+808) | **$2,910,482** |
| Bullish | 09-18 P35 (+885) · 09-18 C70 (+1,604) · 07-31 P32 (+598) | **$535,495** |
| **Ratio** | | **5.4 : 1 bearish** |

**Contract counts mislead here; premium does not.** By contract count the split is 2,808
bearish vs 3,087 bullish — *nominally* bullish. By premium it is **5.4:1 bearish**, because
the "bullish" side is three cheap trades (a $0.29 lottery call, and two premium-collection
sales at $0.34 and $0.65) while the bearish side is a single $8.97 institutional put
purchase. Any phase citing the contract split without the premium split inverts the read.

**The Jan-2028 P30 in detail — the run's one non-trivial position:**

- **+2,000 contracts** = 200,000 share-equivalents = **0.157% of the 127.77M float**
- **`prev_ask_volume` 2,908 vs `prev_bid_volume` 253** — 92% ask-side. Unambiguously
  **bought**, not written.
- **$2,837,716 of premium at $8.97 average**, `dte` **541** (18 months), strike 30 =
  **14.4% below spot**
- `smart-positioning` `inferred_direction` **bearish**, `net_ask_bid` **+2,655**
- **Opened on 07-28, before the postmarket print** (§ Summary, verified via
  `top-premium-trades --date 2026-07-28`, which shows the ask-side cluster
  $438,300 / 487 · $231,287 / 259 · $111,625 / 125 · $99,000 / 110 · $85,920 / 96, all at
  $8.93–$9.00, plus a 2027-06-17 P30 mid print of $153,430)

**Two readings, and they are not equally likely.** (a) A directional 18-month bearish bet
entered ahead of a binary event. (b) Portfolio protection struck 14% below spot by a holder
of the underlying. The evidence leans (a) on three grounds: 92% ask-side execution
(protection buyers are usually less price-insensitive), the deliberate pre-print timing,
and the absence of any offsetting long-side accumulation — `phase-2-dark-pool.md` found
**distribution** (`sell_ratio` 0.610), not the stock buying that would accompany a collar.
But strike 30 at 541 DTE is also exactly where a long-term holder would insure, so (b)
cannot be excluded from EOD data. **Either way the position is short-delta and it is the
largest committed capital in the chain.** Phase 8b should test both readings.

**The three "bullish" builds are all premium sales, not bets:**
- **09-18 P35 +885 built on `prev_bid_volume` 639 vs `prev_ask_volume` 348** — the ATM put
  OI at 35 grew by someone **writing** puts (`curr_oi` **8,970**, the largest single-expiry
  put position at the strike). Classified `bullish` because selling puts is short-vol /
  long-delta, but this is **yield harvesting into a −11% two-week decline**, not
  conviction. **It is also the strongest candidate location for the 07-23 put-writing
  position** that `phase-1-flow.md` flagged (+$5,904,530 via `put_ask_bid_x` 0.508) and
  asked whether it survived: **it survived and it grew.**
- **07-31 C45 +808 and P32 +598** are 2-DTE premium sales at $0.34 and $0.65 — expiry-week
  harvesting, consistent with `phase-1-flow.md` §G's 128–233% front-expiry IV.
- **09-18 C70 +1,604 for $55,196** at $0.29 is a far-tail lottery (+99.7% OTM). Cheap
  optionality, not positioning — though it is worth noting *someone* is buying 51-day
  upside tails while others write 40/55/75 calls.

Note the **absence** of any large near-money **call** build. Across a post-earnings session
there is no OI evidence of the speculative call buildup the spec's first heuristic
describes — the only near-dated call build (07-31 C45) was **sold**.

### D — Closing / roll activity

`uw oi decrease-with-volume --symbol ENPH --top-n 15 --min-volume 100` → **6 rows**:

| `option_symbol` | Parsed | `dte` | `last_oi` → `curr_oi` | `oi_diff_plain` | vol |
|---|---|---|---|---|---|
| **`ENPH260821C00065000`** | 2026-08-21 C65 | 23 | 3,407 → **2,296** | **−1,111** | 1,295 |
| `ENPH261120P00045000` | 2026-11-20 P45 | 114 | 656 → 596 | −60 | 106 |
| `ENPH281215C00055000` | 2028-12-15 C55 | 870 | 415 → 357 | −58 | 264 |
| `ENPH260918P00040000` | 2026-09-18 P40 | 51 | 4,046 → 3,992 | −54 | 486 |
| `ENPH270115C00050000` | 2027-01-15 C50 | 170 | 5,977 → 5,954 | −23 | 173 |
| `ENPH261120P00030000` | 2026-11-20 P30 | 114 | 391 → 389 | −2 | 190 |

**Only one decrease is material: Aug-21 C65, −1,111 contracts.** At 85% OTM with 23 days
left these are dead; whoever was short them bought them back for pennies, or a holder gave
up. It cross-checks cleanly against §A (Aug-21 K=65 `call_oi` 2,296 = `curr_oi` exactly),
a useful internal validation of both leaves.

The remaining five decreases total **−197 contracts** — noise.

**`uw oi position-rolls --symbol ENPH --threshold 500 --near-dte-max 30` → 0 rows.**
No near→far rolling at the 500-contract threshold. This matters: the classic
expiry-week behaviour is to roll near-dated exposure forward, and **nobody is doing it**.
Combined with the junk-call composition of 07-31 (§A) — those calls are not worth rolling —
and the absence of near-money call builds (§C), the picture is of positions being **allowed
to expire and not replaced on the upside**, while fresh capital goes into **long-dated
puts**. There is no roll signature to report.

### E — Smart positioning

`uw oi smart-positioning --symbol ENPH --top-n 20 --min-oi-change 500` returned the
**same 5 contracts** as `biggest-increases`, adding `option_type_inferred`,
`inferred_direction` and `net_ask_bid` (tabulated in §C). It contributes no new contracts —
it *classifies* them, and its classifications match the manual `prev_ask_volume` vs
`prev_bid_volume` derivation on all five rows.

Per the spec's pitfall on OPRA parsing for unusual tickers, `option_type_inferred` was
spot-verified against the raw symbols: `ENPH280121P00030000` → `P` at position 10 → put ✓;
`ENPH260918C00070000` → `C` → call ✓. ENPH is a plain 4-character symbol with no dual-class
suffix, so the parser is on safe ground.

**Directional summary:** 2 bearish (premium **$2,910,482**), 3 bullish (premium
**$535,495**). The single bearish position at `dte` 541 carries **5.3× the premium of all
three bullish positions combined.**

### F — Pin risk

`uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5` → **ENPH absent**
(null-safe select → `[]`). Cutoff at #25 is KWEB, `pin_score` **157,864.79**; the leaders
are SPY (2,110,153), HYG (1,689,900) and IWM (1,283,860).

**ENPH has an expiry inside the 7-day window (07-31, `dte` 2) and a high-OI strike within
5% of spot (35, `distance_pct` −0.17%) — so it met the filter criteria and still failed to
rank.** §A explains why: only **745 contracts** (721 puts + 24 calls) sit at the 35 strike
in the 07-31 expiry. The front-expiry OI that exists is 21–57% OTM.

**Conclusion: there is no Friday pin at 35, and no pin commentary is warranted.** This is
a meaningful negative. It removes the mechanical argument for spot being held at 35 into
07-31, and it means phase 9 cannot rely on expiry gravity as support. Any 35-holding thesis
must rest on the Aug-21 wall (4,031 puts, §A) and on dealer hedging behaviour (§H) — both
weaker than a genuine pin.

### G — OPEX concentration

`uw oi opex-concentration --top-n 20 --min-concentration-pct 40` → **ENPH absent**
(null-safe select → `null`). Returned names are all micro-caps with ≥40% single-expiry
concentration: BUR, TONX, LFST, NEWP, GANX, NPWR, IMMX, CWB, FLGT, RNGR, CVGI, WLTH, GSM,
TUSK, SGMOQ, FLD, THRY, DBB, ZURA, KNTK.

**Correctly absent, and informative:** ENPH's maximum single-expiry concentration is
**24.95%** (2027-01-15, §B), below the 40% threshold. ENPH's OI is **diffuse across 15
expiries** — no single-expiry cliff dominates, so there is no concentrated-expiry
mechanical risk to trade around. The nearest thing to a cliff is the Aug-21 monthly at
**15.69%**.

Cross-referencing the spec's request for "cliff strikes within 5% of spot": the only strike
within 5% of 35.07 carrying real OI is **35 itself** (all-expiry 33,110; ≤30-DTE 6,082;
Aug-21 4,730; 07-31 745). The next strikes out — 30 (−14.4%) and 40 (+14.1%) — are both
well beyond 5%. **ENPH's near-money OI is concentrated in exactly one strike, and spot is
sitting on it.**

### H — Who owns the 35 puts? (the question that decides whether the wall is support)

`oi-by-strike` tags 35 `put_wall_support`, but a put wall only produces dealer buying if
**customers are long the puts** (dealers short → short gamma below → they buy stock as it
falls). If customers are **short** the puts, dealers are long them and **sell** into
weakness, making the level an accelerant. The distinction is decisive for phase 9's stop
placement, and this phase can partially resolve it.

**Evidence that customers are long puts at/near 35 (→ genuine dealer support):**
- `phase-1-flow.md` whole-tape: **`put_volume_ask_side` 7,236 vs `put_volume_bid_side`
  4,613 = 1.569×** — today's puts were **bought**, third consecutive session ≥1.38
- Today's largest print: **Oct-16 P35 bought on the ask**, $196,240 + $31,500, 516
  contracts (`phase-1-flow.md` §E)
- Today's largest ask-side sweep: **Oct-16 P35, $260,820 / 591 contracts**
- A fresh Sept-04 put ladder (P25/P30/P35, $153,713) was **bought** (`phase-1-flow.md` §F)

**Evidence that customers are short puts at 35 (→ accelerant):**
- **`ENPH260918P00035000` +885 OI built on `prev_bid_volume` 639 vs `prev_ask_volume` 348
  — written**, and it is the largest single-expiry put position at the strike
  (`curr_oi` **8,970**)
- The 07-23 put-writing session (+$5,904,530, `put_ask_bid_x` 0.508) is unwound nowhere in
  the decrease data — that short-put exposure is still live
- `ENPH260731P00032000` +598 and the Aug-21 P40 bid sweep ($147,337) were also **sold**

**Assessment: genuinely mixed, tilting toward customer-long in the near expiries and
customer-short in September.** The Aug-21 4,031 puts at 35 have no side attribution in the
available data. Today's *flow* is decisively put-buying; the *OI build* at the 35 strike
(which reflects 07-28) was put-selling. **The honest answer is that the 35 wall's
directional character is unresolved, and phase 9 must not assume it produces support.**
Phase 4 can advance this via GEX/gamma sign and dealer positioning, which is the correct
tool for the question.

A structural warning for phase 9: the **short-put position at 09-18 P35 (8,970 contracts)
is now at the money after an 11% two-week decline**. If ENPH breaks 35, those writers face
assignment pressure on ~897,000 share-equivalents (**0.70% of float**) — potential forced
selling, not support.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --date 2026-07-29 --json` | K35 `call_oi`=7770/`put_oi`=25340/`net_oi`=−17570/`total_oi`=33110/`role`=`put_wall_support`/`distance_pct`=−0.17; K70 `net_oi`=+21074 ← `.results[]` | top-10, all expiries |
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --dte-max 30 --date 2026-07-29 --json` | K40 `total_oi`=10079 (`put_oi`=8124); K35 `total_oi`=6082 (`put_oi`=5009) ← `.results[]` | top-10, ≤30 DTE |
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --expiry 2026-08-21 --date 2026-07-29 --json` | K35 `put_oi`=**4031** (vs 3734 carried), K40 `put_oi`=**7839** (vs 7888), K30 `put_oi`=2963 ← `.results[]` | top-10 |
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --expiry 2026-07-31 --date 2026-07-29 --json` | K50 `call_oi`=4035, K42.5 `call_oi`=3941, K45 `call_oi`=2048; K35 `put_oi`=**721**/`call_oi`=24 ← `.results[]` | top-10 |
| `uw oi term-structure --symbol ENPH --date 2026-07-29 --json` | `expiry_count`=15, `total_oi`=294987; 2027-01-15 `pct_of_total_oi`=**24.95**, 2026-09-18 =16.15, **2026-08-21 =15.69** (`total_oi`=46288, `put_call_oi_ratio`=0.891), 2026-07-31 `put_call_oi_ratio`=0.373 ← **`.term_structure[]`** (not `.results`) | 15 expiries |
| `uw oi biggest-increases --symbol ENPH --top-n 20 --min-oi-change 500 --date 2026-07-29 --json` | `ENPH280121P00030000` `oi_diff_plain`=**2000**, `last_oi`=2361→`curr_oi`=4361, `oi_change`=0.847, `prev_ask_volume`=**2908**/`prev_bid_volume`=253, `prev_total_premium`=**2837716**, `avg_price`=8.974, `dte`=541 ← `.results[]` | 5 returned of 20 |
| `uw oi decrease-with-volume --symbol ENPH --top-n 15 --min-volume 100 --date 2026-07-29 --json` | `ENPH260821C00065000` `oi_diff_plain`=**−1111** (3407→2296, vol 1295); other 5 sum −197 ← `.results[]` | 6 returned of 15 |
| `uw oi smart-positioning --symbol ENPH --top-n 20 --min-oi-change 500 --date 2026-07-29 --json` | 2028 P30 `inferred_direction`=**bearish**/`net_ask_bid`=+2655; 09-18 P35 `bullish`/`net_ask_bid`=**−291**; 07-31 C45 `bearish`/−533 ← `.results[]`; bearish prem Σ=2910482, bullish Σ=535495 | 5 returned of 20 |
| `uw oi position-rolls --symbol ENPH --threshold 500 --near-dte-max 30 --date 2026-07-29 --json` | **0 rows** ← `.results\|length` = 0 | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-07-29 --json` | ENPH **absent** ← `[.results[]\|select(.ticker=="ENPH")]` → `[]`; cutoff KWEB `pin_score`=157864.79 ← `.results[24]` | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-07-29 --json` | ENPH **absent** ← null-safe select → `null` | top-20 |
| `uw options-flow top-premium-trades --symbol ENPH --top-n 10 --date 2026-07-28 --json` | **timing proof** — 2028-01-21 P30 ask prints $438300/487, $231287/259, $111625/125, $99000/110, $85920/96 @ $8.93–9.00 ← `.results[]` | top-10 |
| `uw options-flow top-premium-trades --symbol ENPH --top-n 25 --date 2026-07-29 --json` (from phase 1) | max `premium`=**196240** ← `[.results[].premium]\|max` → proves the $2.84M build is not a 07-29 event | top-25 |
| `fz screen --tickers ENPH --view ownership --agent` (from `phase-0-intake.md`) | `Float`=127.77M → 2,000×100/127.77M = **0.157%** | 1 |

All eleven `uw` reads were captured to a file before being queried and every value
round-tripped through `jq` on validated JSON; both market-wide leaves used the null-safe
select form per `memory/batched-stdout-swallow.md`. Derived values, each stated inline:
premium-weighted direction sums (§C, §E), side inference from
`prev_ask_volume`/`prev_bid_volume` (§C), OPRA strike/type/expiry parsing (§C, §D),
float-share-equivalents (§C), and the 294,987 / 381,215 = 77.4% coverage ratio (§B).

## Tool errors

1. **`uw oi term-structure` payload key is `.term_structure`, not `.results`.** The first
   read errored:
   ```
   jq: error (at …/oi_ts.json:158): Cannot iterate over null (null)
   ```
   from `jq '.results[]'`. Exit code was **0** and the JSON was valid — the leaf simply
   returns `{expiry_count, source, symbol, term_structure[], total_oi}`. Diagnosed by
   `jq 'keys[]'` and re-read from `.term_structure[]`. **No value was transcribed from the
   failed read** (the JSON-validity gate caught it). This is a **field-path trap** in the
   same class as the two pinned in `lib/uw-json-paths.md`; candidate addition
   (**propose-only**, per the audit convention) — every other `uw` leaf used in this phase
   returns `.results`.

2. **`uw oi biggest-increases` has no `prev_oi` field** — the prior value is
   **`last_oi`** (with `curr_oi` for current). An initial `.prev_oi` read returned `?`.
   No value transcribed; re-read from `last_oi`, and each row's arithmetic verified
   (`ENPH260731C00045000`: 2,048 / (1 + 0.6516) = 1,240 = `last_oi` ✓;
   `ENPH260731P00032000`: 692 / 7.3617 = 94 = `last_oi` ✓).

No other errors. All eleven `uw` calls returned exit 0 with parseable JSON.
`position-rolls`, `pin-risk` and `opex-concentration` returned **empty results, which is
information, not failure** (recorded in §D, §F, §G respectively).

## DATA NOTE / CORRECTION

**One material correction to an upstream carry, and one timing fact established that all
later phases depend on.**

**(1) The 07-31 "positive-gamma island" framing carried in `phase-0-intake.md` is
misleading.** That file carries from the 07-27 run: *"2026-07-31 — front-week expiry;
positive-gamma island (`today_total_gex` +1,047,168) expires."*

- **Corrected reading:** the 07-31 expiry's 19,447 calls are stacked at **42.5 (3,941) /
  45 (2,048) / 50 (4,035) / 55 (1,153)** — **21% to 57% OTM with `dte` 2** — and only
  **745 contracts** (721 puts, 24 calls) sit at the 35 strike where spot actually is. The
  gamma retiring on Friday belongs almost entirely to contracts with ~zero gamma at spot
  35.07.
- **Verified against:** `uw oi oi-by-strike --symbol ENPH --expiry 2026-07-31 --json`
  → `.results[]` `strike`/`call_oi`/`put_oi`; corroborated by
  `uw oi term-structure` → `.term_structure[] | select(.expiry=="2026-07-31")`
  (`call_oi` 19,447, `put_oi` 7,246, `put_call_oi_ratio` 0.373).
- **Downstream consequence:** phase 4 must **measure** current GEX rather than inherit
  "+1,047,168 expiring," and must not treat Friday's roll-off as a material change in
  dealer gamma near the money. Phase 9 must not use expiry gravity as support — reinforced
  independently by ENPH's absence from `pin-risk` (§F).

**(2) OI reported for 2026-07-29 reflects 07-28's trading — established, not assumed.**
This is the spec's documented pitfall ("OI updates daily after close"), and it is proven
here rather than presumed:
- The largest print in `top-premium-trades --date 2026-07-29` is **$196,240**
  (`[.results[].premium] | max`), so a **$2,837,716** trade cannot be a 07-29 event.
- `top-premium-trades --date 2026-07-28` returns the ask-side Jan-2028 P30 cluster
  ($438,300 / $231,287 / $111,625 / $99,000 / $85,920 at $8.93–$9.00).
- It reconciles `phase-1-flow.md`'s otherwise-unexplained 07-28 `net_flow` of
  **−$3,162,110** — the P30 buying is ~90% of that figure.
- **Therefore every OI figure in this phase is as of the 07-28 close**, and **today's
  flow is not yet in OI**: the Oct-16 P35 purchase and the Aug-07 C37 purchase
  (`phase-1-flow.md` §D–F) will appear in tomorrow's snapshot. Phase 4, 5 and 9 must not
  read this phase's walls as incorporating today's tape.

No value in this phase was revised after its first validated read. The two items in
`## Tool errors` are wrong *field paths* caught by the validity gate before transcription,
not corrected data.

## Verdict for downstream phases

- **Positioning bias: PUTS BEING BOUGHT — long-dated, institutional, and pre-positioned
  ahead of the event.** Not hedging-with-stock (phase 2 found distribution, not
  accumulation), and explicitly *not* speculative call buildup — the only near-dated call
  build was **written**, and `position-rolls` is empty, so upside exposure is being allowed
  to lapse unreplaced.
- **Conviction: 4 / 5** — the highest of any phase so far, and for one reason:
  **this is the only lane in the run where the magnitude is not trivial.** $2,837,716 of
  ask-side long-dated put buying is ~6× the day's entire net option flow and 2.5× the
  whole top-25 print tape, with a 5.4:1 premium-weighted bearish skew and a
  `smart-positioning` `bearish` label. It is a fourth independent lane agreeing with
  phases 0.5/1/2. Held at 4 rather than 5 because (a) the position is **`dte` 541** — an
  18-month expression says little about a 1–4 week horizon; (b) the
  bearish-bet-vs-protection ambiguity is genuinely unresolved (§C); (c) the *other* side
  of the 35 strike is real — 8,970 written September puts (§H); and (d) only **5 rows**
  cleared the 500-contract threshold at all, so the sample is thin and the rest of the
  +17,988 OI build (`phase-0.5-context.md`) is diffuse and unattributed.
- **Largest OI build as % of float:** **0.157%** (2,000 contracts × 100 / 127.77M
  share-equivalents). Combined across all five builds: 5,895 contracts = **0.461% of
  float**. **For a 127.77M-float name this is a real institutional position but not a
  float-dominating one** — it is the *premium committed* ($2.84M at 92% ask-side) and the
  *pre-print timing* that make it structural, not the share-equivalent size. Consistent
  with phase 2's 0.852%-of-float off-exchange volume: genuine institutional participation,
  unremarkable scale.
- **Three pin/cliff strikes for phase-9** (sourced from `oi-by-strike` roles and the
  `term-structure` cliff, not hand-picked):
  1. **35 — `put_wall_support`, `distance_pct` −0.17%, spot is on it.** All-expiry
     `total_oi` 33,110 (`net_oi` −17,570) but only **6,082 inside 30 days** and **4,031
     puts in the Aug-21 monthly** (+297 / +8.0% vs the carried 3,734). **Treat as a
     contested level, not as support** — §H shows today's flow is put-*buying* while the
     OI at the strike was put-*writing*, and **no Friday pin exists** (§F). Downside risk:
     8,970 written Sept-18 puts are now ATM = ~0.70% of float of potential assignment
     pressure if 35 breaks.
  2. **2026-08-21 — the tradeable OPEX cliff, `pct_of_total_oi` 15.69%** (46,288 OI,
     `dte` 23, `put_call_oi_ratio` 0.891). Put-dominated at every strike within 30% of
     spot: **40 → 7,839 puts** (now 14% ITM), **35 → 4,031**, **30 → 2,963**. Anchor a
     1–4 week horizon here, **not** to 2027-01-15 (24.95% but `dte` 170, a LEAP warehouse).
  3. **30 — `put_wall_support`, `distance_pct` −14.43%**, all-expiry `put_oi` **22,446**
     (`net_oi` −20,452), Aug-21 `put_oi` 2,963. **This is where the institutional money
     actually went** — the $2.84M Jan-2028 P30 purchase. It is the structural downside
     objective the largest position in the chain is aiming at.
     Secondary reference: **40 (`put_heavy`, +14.09%)** — heaviest near-term OI (10,079,
     with 8,124 puts) and the first overhead level; it sits just above phase 2's
     36.15–36.30 distribution shelf.
- **Open questions:**
  - **Is the Jan-2028 P30 position a directional bet or protection on an unreported long?**
    §C leans directional (92% ask-side, deliberate pre-print timing, no offsetting
    accumulation in phase 2) but cannot exclude a collar. If it is a hedge, its bearish
    signal weight should be cut substantially. (→ 7c, 8b)
  - **Does dealer gamma at 35 actually produce support, or is the wall an accelerant?**
    §H shows conflicting side evidence (today's flow buys puts; the OI build at 35 wrote
    them). GEX sign and dealer positioning are the right tools. (→ 4)
  - **What is the *current* GEX, given that Friday's expiring "gamma island" is 11,177
    junk calls at 42.5–55?** The carried `today_total_gex` +1,047,168 must be re-measured,
    not inherited. (→ 4)
  - **Why does nobody roll?** Zero `position-rolls` rows plus no near-money call builds
    plus written 07-31 calls = upside exposure being abandoned. Is that capitulation
    (contrarian bullish) or correct positioning for a name with no catalyst until
    **2026-10-27**? (→ 4, 5, 7c)
  - **Tomorrow's OI will absorb today's Oct-16 P35 (516–591 contracts bought) and Aug-07
    C37 (1,157 bought).** Does the Oct-16 P35 build confirm a sustained put-accumulation
    campaign spanning 07-28 → 07-29, or was the P30 purchase a one-off? (→ 5, 9)
