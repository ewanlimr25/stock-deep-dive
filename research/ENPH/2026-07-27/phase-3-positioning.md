# Phase 3 — Open Interest & Positioning

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T20:42:00-04:00
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`

## Summary

**Almost nothing was positioned today, and what was positioned was premium
*selling*.** Only **two** contracts in the entire chain moved OI by ≥500, and
`smart-positioning` classifies both as sales: **1,324 new short Nov-20 $70 calls**
(`net_ask_bid = −1,407`, 99.5% of volume on the bid, $205,517 collected) and
**542 new short Oct-16 $30 puts** ($157,419 collected). Someone is **selling both
wings** into a binary event. `position-rolls` returns `rolls_detected = 0`, which
**fails to confirm phase-1's Jun-2027 → Oct-2026 protection-roll hypothesis**.

**This phase also overturns phase-2's headline inference.** Phase-2 concluded the
800-lot Nov-20 $35 put was *bought* by a customer (28,800-share delta hedge, 96%
match). The OI record says the position **did not open**: `last_oi 407 → curr_oi 412`,
a change of **+5**. The print carries `report_flags = {futures_floor}` and
`upstream_condition_detail = "slft"` (single-leg floor trade) — it is a **negotiated,
delta-neutral floor cross**, i.e. an existing position changing hands, not new
downside demand. The stock leg was part of the package, not a dealer hedging in
the market. **Phase-2's directional conclusion must be downgraded; its factual
observations stand.**

Structurally, the tradeable chain is **put-heavy below and stranded above**. The
August OPEX (2026-08-21, 18.64% of OI) carries a **7,888-contract $40 put wall**
and a **3,734-contract $35 put wall**, while the huge $60/$70/$75 call walls are
legacy OI from when ENPH traded twice as high — 58% to 97% out of the money and
economically dead. The earnings expiry itself (2026-07-31) holds only **6.98%** of
total OI and its heaviest strikes are worthless far-OTM calls.

## Key signals

- **Only 2 OI builds ≥500 in the whole chain**, both **sales**: Nov-20 **C70
  +1,324** (`inferred_direction="bearish"`, bid_vol 1,411 vs ask_vol 4, $205,517)
  and Oct-16 **P30 +542** (`inferred_direction="bullish"`, $157,419)
  [OI:smart_positioning].
- **The 800-lot Nov-20 P35 did NOT open**: `407 → 412` (+5), flagged
  `{futures_floor}` / `slft`. **Downgrades phase-2's "customer bought" read to a
  position transfer** [OI:oi_changes DUCKDB].
- **$40 put wall of 7,888 contracts at 2026-08-21** (vs 850 calls, `net_oi = −7,038`),
  only **+5.24%** from spot; **$35 put wall 3,734** at −7.92% [OI:oi_by_strike].
- **OPEX cliff is 2027-01-15 at 24.52% of OI** (59,336) — 172 DTE, outside any
  tradeable horizon. Nearest real cliffs: **2026-09-18 (20.51%)** and
  **2026-08-21 (18.64%)** [OI:term_structure].
- **`rolls_detected = 0`** — phase-1's protection-roll hypothesis **unconfirmed**
  [OI:position_rolls]. **ENPH absent from `pin-risk` and `opex-concentration`**
  [OI:pin_risk], [OI:opex_concentration].

## Detailed findings

### OI walls by strike

`uw oi oi-by-strike --symbol ENPH`, `spot = 38.01`.

**All-expiry aggregate** (the tool's default — note the caveat that this mixes LEAPs
into the wall map):

| Strike | Call OI | Put OI | `net_oi` | Total OI | `role` | `distance_pct` |
|---|---|---|---|---|---|---|
| 50 | 19,699 | 13,539 | +6,160 | **33,238** | call_wall_resistance | +31.54% |
| **40** | 8,550 | **21,170** | **−12,620** | **29,720** | **put_heavy** | **+5.24%** |
| **35** | 4,883 | **23,133** | **−18,250** | **28,016** | **put_wall_support** | **−7.92%** |
| 70 | **25,083** | 11 | +25,072 | 25,094 | call_wall_resistance | +84.16% |
| 30 | 2,349 | 17,134 | −14,785 | 19,483 | put_wall_support | −21.07% |
| 60 | 18,104 | 0 | +18,104 | 18,104 | call_wall_resistance | +57.85% |
| 75 | 15,659 | 0 | +15,659 | 15,659 | call_wall_resistance | +97.32% |
| 45 | 5,824 | 5,150 | +674 | 10,974 | call_wall_resistance | +18.39% |
| 55 | 9,362 | 514 | +8,848 | 9,876 | call_wall_resistance | +44.70% |
| 65 | 9,023 | 444 | +8,579 | 9,467 | call_wall_resistance | +71.01% |

**The call walls are a mirage.** $60, $65, $70 and $75 carry **68,269 call
contracts** with **455 puts between them** — and sit **58% to 97% above spot**.
These are the fossils of ENPH at $60–$74 (52-week high **$73.74**,
`phase-0.5-context.md`). At 58%+ OTM their delta is ~0 and they exert **no dealer
hedging pressure**. Labelling $70 a "call_wall_resistance" is technically correct
and practically meaningless. **Phase-9 must not use them as targets or resistance.**

Note too that `$45` is tagged `call_wall_resistance` on `net_oi = +674` against
`total_oi = 10,974` — a **two-sided battleground** (5,824 calls / 5,150 puts), not
a wall. Exactly the mislabel the phase-3 pitfall warns about; quoted with `net_oi`
so phase-9 does not treat it as clean resistance.

**Tradeable-horizon map (`--dte-max 30`)** — this is what phase-9 should size against:

| Strike | Call OI | Put OI | `net_oi` | Total OI | `role` | `distance_pct` |
|---|---|---|---|---|---|---|
| 50 | 6,829 | 6,055 | **+774** | 12,884 | call_wall_resistance ⚠️ | +31.54% |
| **40** | 1,252 | **8,444** | **−7,192** | 9,696 | **put_heavy** | **+5.24%** |
| 45 | 2,579 | 3,265 | −686 | 5,844 | put_heavy | +18.39% |
| **35** | **10** | **4,217** | **−4,207** | 4,227 | **put_wall_support** | **−7.92%** |
| 60 | 4,173 | 0 | +4,173 | 4,173 | call_wall_resistance | +57.85% |
| **42.5** | **3,735** | **0** | **+3,735** | 3,735 | **call_wall_resistance** | **+11.81%** |
| 30 | 285 | 3,446 | −3,161 | 3,731 | put_wall_support | −21.07% |
| 55 | 3,161 | 0 | +3,161 | 3,161 | call_wall_resistance | +44.70% |
| 75 | 3,148 | 0 | +3,148 | 3,148 | call_wall_resistance | +97.32% |
| 90 | 2,024 | 0 | +2,024 | 2,024 | call_wall_resistance | +136.78% |

Within 30 DTE the picture is clean:

- **$40 (+5.24%) is the dominant near structure** — 8,444 puts vs 1,252 calls.
  These puts are **in the money** with spot at $38.01. That is *existing
  protection*, already working, not a level being defended.
- **$42.50 (+11.81%) is the only genuine near-term call wall** — 3,735 calls,
  **zero puts**. This is the first real overhead gamma level.
- **$35 (−7.92%) is a clean put wall** — 4,217 puts against **10** calls.
- **$50 is tagged `call_wall_resistance` on `net_oi = +774`** out of 12,884 — again
  a battleground, not a wall, and 31.5% away regardless.

### OI term structure

`uw oi term-structure --symbol ENPH` → `total_oi = 241,974` across
`expiry_count = 15`.

| Expiry | DTE | Call OI | Put OI | Total OI | P/C OI | **% of total** | Contracts |
|---|---|---|---|---|---|---|---|
| **2026-07-31** | **4** | 13,502 | 3,395 | 16,897 | **0.251** | **6.98%** | 79 |
| 2026-08-07 | 11 | 1,135 | 907 | 2,042 | 0.799 | 0.84% | 39 |
| 2026-08-14 | 18 | 462 | 620 | 1,082 | 1.342 | 0.45% | 24 |
| **2026-08-21** | **25** | 20,025 | **25,090** | **45,115** | **1.253** | **18.64%** | 42 |
| 2026-08-28 | 32 | 191 | 320 | 511 | 1.675 | 0.21% | 20 |
| 2026-09-04 | 39 | 13 | 26 | 39 | 2.000 | 0.02% | 9 |
| **2026-09-18** | **53** | 25,583 | 24,042 | **49,625** | 0.940 | **20.51%** | 18 |
| 2026-10-16 | 81 | 1,706 | 1,487 | 3,193 | 0.872 | 1.32% | 11 |
| 2026-11-20 | 116 | 7,911 | 4,190 | 12,101 | 0.530 | 5.00% | 19 |
| 2026-12-18 | 144 | 8,202 | 13,389 | 21,591 | 1.632 | 8.92% | 20 |
| **2027-01-15** | **172** | **41,707** | 17,629 | **59,336** | 0.423 | **24.52%** | 18 |
| 2027-02-19 | 207 | 66 | 881 | 947 | 13.348 | 0.39% | 8 |
| 2027-06-17 | 325 | 16,789 | **52** | 16,841 | **0.003** | 6.96% | 10 |
| 2028-01-21 | 543 | 7,653 | 1,613 | 9,266 | 0.211 | 3.83% | 14 |
| 2028-12-15 | 872 | 2,597 | 791 | 3,388 | 0.305 | 1.40% | 13 |

**OPEX cliff = 2027-01-15 at 24.52%** — but at **172 DTE** it is a LEAP anchor, not
a tradeable gravity well. The cliffs that matter inside a swing horizon are
**2026-09-18 (20.51%, 53 DTE)** and **2026-08-21 (18.64%, 25 DTE)**. Together the
two nearest monthlies hold **39.15%** of all OI.

Two structural reads:

1. **The earnings expiry is nearly empty and wrongly skewed.** 2026-07-31 holds
   just **6.98%** of OI with a P/C of **0.251** — heavily call-tilted. But its
   strike map (below) shows that call OI is parked at **$50 (3,864) and $42.50
   (3,591)** — 31.5% and 11.8% OTM with **zero puts**. **55% of the earnings-week
   call OI is lottery tickets.** Combined with phase-1's `call_ask_share = 0.475`,
   these are being *sold*, not bought. The market has **not** built a directional
   book for tomorrow's print.
2. **Real positioning sits in August/September, and it is protective.**
   2026-08-21 is put-heavy (P/C **1.253**, 25,090 puts) and 2026-12-18 more so
   (P/C **1.632**). The name's hedges are placed *past* the event, in the monthlies.

**2026-07-31 (earnings expiry, DTE 4) strike map:**

| Strike | Call OI | Put OI | `net_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|
| 50 | 3,864 | 0 | +3,864 | call_wall_resistance | +31.54% |
| **42.5** | **3,591** | **0** | +3,591 | call_wall_resistance | **+11.81%** |
| 55 | 1,115 | 0 | +1,115 | call_wall_resistance | +44.70% |
| 45 | 759 | 154 | +605 | call_wall_resistance | +18.39% |
| **40** | 356 | 374 | **−18** | put_heavy | **+5.24%** |
| 46 | 488 | 140 | +348 | call_wall_resistance | +21.02% |
| 33 | 0 | 472 | −472 | put_wall_support | −13.18% |
| 43 | 424 | 0 | +424 | call_wall_resistance | +13.13% |
| 35 | 10 | 288 | −278 | put_wall_support | −7.92% |
| **36** | 38 | 223 | −185 | put_wall_support | **−5.29%** |

**Near-the-money OI for the event is trivially thin** — $40 carries 730 total
contracts and $36 just 261. Inside the 12.25% implied move ($33.36–$42.66) the
entire chain holds roughly **2,000 contracts**. **There is no meaningful pin and no
dealer wall to fight tomorrow.** The stock is free to move to wherever the print
sends it. This is the single most important structural fact for phase-9.

**2026-08-21 (monthly OPEX, DTE 25) strike map:**

| Strike | Call OI | Put OI | `net_oi` | `role` | `distance_pct` |
|---|---|---|---|---|---|
| 50 | 2,834 | 6,055 | −3,221 | put_heavy | +31.54% |
| **40** | 850 | **7,888** | **−7,038** | **put_heavy** | **+5.24%** |
| 45 | 1,744 | 3,111 | −1,367 | put_heavy | +18.39% |
| 60 | 3,931 | 0 | +3,931 | call_wall_resistance | +57.85% |
| **35** | **0** | **3,734** | **−3,734** | **put_wall_support** | **−7.92%** |
| 30 | 285 | 2,927 | −2,642 | put_wall_support | −21.07% |
| 75 | 3,031 | 0 | +3,031 | call_wall_resistance | +97.32% |
| 90 | 2,024 | 0 | +2,024 | call_wall_resistance | +136.78% |
| 55 | 2,017 | 0 | +2,017 | call_wall_resistance | +44.70% |
| 25 | 106 | 445 | −339 | put_wall_support | −34.23% |

The August book is **put-dominated at every strike from $30 to $50** — 24,115 puts
vs 5,428 calls across those five strikes. The $40/$45/$50 puts (17,054 contracts)
are all **already in the money**. This is a book that has *been* hedged, and is
currently *paying off*.

### Largest OI increases

`uw oi biggest-increases --symbol ENPH --min-oi-change 500` → **2 rows only.**

| `option_symbol` | Parsed | DTE | `last_oi` | `curr_oi` | **`oi_diff_plain`** | `oi_change` | Volume |
|---|---|---|---|---|---|---|---|
| `ENPH261120C00070000` | 2026-11-20 **C** 70 | 116 | 359 | 1,683 | **+1,324** | 3.688 | 1,418 |
| `ENPH261016P00030000` | 2026-10-16 **P** 30 | 81 | 56 | 598 | **+542** | 9.679 | 624 |

Expiry, side and strike parsed from the OPRA `option_symbol` per the phase-3
composition note (`biggest-increases` carries no `side`/`expiry` column).

**Float normalization** (`Shs Float = 127.77M`, `phase-0-intake.md`): the largest
build is `1,324 × 100 = 132,400` share-equivalents = **0.104% of float**
[OI:oi_pct_float fz]. Essentially identical to the largest dark-pool block
(0.101%, `phase-2-dark-pool.md`). **Advisory and de-rating only: nothing built
today is structural for this name.**

**Broader OI-change detail** (raw `chain-oi-changes-2026-07-27.parquet`, which
carries the ask/bid/mid split the CLI omits; `last_date = 2026-07-24`,
`curr_date = 2026-07-27`, 344 ENPH rows, Σvolume 12,765):

| Contract | DTE | OI Δ | Vol | ask_v | bid_v | avg px | Read |
|---|---|---|---|---|---|---|---|
| 2026-11-20 C70 | 116 | **+1,324** | 1,418 | **4** | **1,411** | 1.45 | **sold to open** |
| 2026-10-16 P30 | 81 | +542 | 624 | 173 | 363 | 2.52 | sold to open |
| 2026-08-21 P35 | 25 | +473 | 655 | 60 | 582 | 2.58 | **sold to open** |
| 2026-09-18 C75 | 53 | +383 | 697 | 207 | 490 | 0.25 | sold to open |
| **2026-11-20 P22.5** | 116 | **+210** | 227 | **227** | **0** | 1.14 | **bought — tail hedge** |
| 2026-07-31 P36 | 4 | +165 | 225 | 47 | 171 | 2.13 | sold |
| 2026-07-31 C45 | 4 | +161 | 320 | 214 | 100 | 0.61 | bought (lottery) |
| 2026-09-18 C60 | 53 | +147 | 516 | 302 | 181 | 0.70 | bought |
| 2026-07-31 P33 | 4 | +125 | 181 | 86 | 87 | 0.95 | balanced |
| 2026-08-07 P31 | 11 | +119 | 236 | 149 | 87 | 0.58 | bought |
| **2026-11-20 P17.5** | 116 | +86 | 86 | **86** | **0** | 0.35 | **bought — tail hedge** |
| 2026-08-21 P40 | 25 | **−97** | 211 | 4 | 193 | 5.02 | closing |

**The dominant behaviour is premium selling into the wings** — C70, C75, P35, P30
all sold to open, collecting roughly **$0.7M** combined. The only unambiguous
*buying* is **deep tail protection**: Nov-20 **P22.50** (+210, **100% on the ask**)
and **P17.50** (+86, **100% on the ask**) — strikes **41% and 54% below spot**.

That combination is a coherent institutional stance: **sell the wings you think are
unreachable, buy cheap insurance against the crash you can't rule out.** It is
neither bullish nor bearish — it is **short volatility with a tail hedge**, and it
implies the seller expects ENPH to stay roughly *range-bound between ~$30 and ~$50*.
Note the tension with phase-1: the front week is bid at **~170% IV** while these
sellers are supplying the **back**. Vol is being sold where it is expensive in
absolute terms but cheap relative to the event.

### Closing / roll activity

`uw oi decrease-with-volume --symbol ENPH --min-volume 100` → 6 rows, all trivial:

| Contract | DTE | `last_oi` | `curr_oi` | OI Δ | Vol |
|---|---|---|---|---|---|
| 2026-08-21 P40 | 25 | 7,985 | 7,888 | −97 | 211 |
| 2026-08-21 C45 | 25 | 1,785 | 1,744 | −41 | 444 |
| 2026-09-18 P40 | 53 | 4,062 | 4,036 | −26 | 175 |
| 2026-09-18 C55 | 53 | 3,904 | 3,886 | −18 | 204 |
| 2026-08-21 C55 | 25 | 2,031 | 2,017 | −14 | 165 |
| 2026-09-18 C65 | 53 | 4,788 | 4,787 | −1 | 113 |

Largest closure is **−97 contracts**. **Nobody is unwinding.** The existing
put-heavy August/September book is being **held**, not liquidated, into the print.
That is a meaningful negative: hedges are staying on.

`uw oi position-rolls --symbol ENPH --threshold 500 --near-dte-max 30` →
**`rolls_detected = 0`, `results: []`**, with the tool's own caveat
*"Single-day detection only — cross-session rolls are not captured."*

**This does not confirm phase-1's roll hypothesis.** Phase-1 inferred a protection
roll from Jun-2027 → Oct-2026 (sold $205,860 + $170,725 of Jun'27 P40/P45; bought
$176,570 of Oct'26 P40). At the 500-contract threshold no roll is detected. Two
readings, and I cannot separate them: (a) the legs are genuinely unrelated prints,
or (b) the roll is real but each leg is under 500 contracts (the Jun'27 legs were
161 and 104 lots — **both below threshold**, so the tool *structurally could not*
see it). **Reading (b) is more likely on the numbers**, but the tool provides no
confirmation. Recorded as **unconfirmed, not refuted** — and see the Jun-2027 data
conflict in `## Tool errors`.

### Smart positioning

`uw oi smart-positioning --symbol ENPH --min-oi-change 500` → 2 rows:

| Contract | Inferred | `net_ask_bid` | `oi_diff_plain` | ask_v | bid_v | `prev_total_premium` |
|---|---|---|---|---|---|---|
| 2026-11-20 **C70** | **bearish** | **−1,407** | +1,324 | 4 | 1,411 | **$205,517** |
| 2026-10-16 **P30** | **bullish** | −190 | +542 | 173 | 363 | **$157,419** |

> **Read the labels carefully.** The tool's convention is directional-equivalent:
> *selling calls* → "bearish", *selling puts* → "bullish". **Both rows are sales.**
> A naive reading ("one bearish, one bullish — mixed") misses that a single desk
> short both wings produces exactly this output. The honest summary is
> **"short strangle / premium supply"**, not "mixed directional opinion".

The C70 row is emphatic: **`net_ask_bid = −1,407` on 1,418 contracts — 99.5% sold
into the bid**, opening 1,324 new contracts for $205,517. At **+84% from spot**
with **116 DTE**, this is a seller expressing that ENPH will not revisit $70 by
November. Given the stock was **$64.03 on 2026-05-22** (`phase-0.5-context.md`),
that is a considered view, not a throwaway.

### Pin risk

`uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5` → **ENPH absent**
(top row is SPY, `spot 739.02`, `dte_to_opex 0`, `pin_score 2,078,720.99`).

**Correct and expected.** ENPH's nearest expiry (2026-07-31) is a **weekly**, not a
monthly OPEX, and — per the strike map above — carries only ~2,000 contracts inside
the implied move. Per the phase-3 instruction, **pin commentary is skipped**: there
is no pin. Tomorrow's move is unconstrained by dealer positioning.

### OPEX concentration

`uw oi opex-concentration --top-n 20 --min-concentration-pct 40` → **ENPH absent.**

**Correctly filtered, not a failure:** ENPH's most concentrated expiry is
2027-01-15 at **24.52%**, well below the 40% threshold. ENPH's OI is **unusually
well distributed across 15 expiries** — no single expiry dominates, which is the
opposite of a cliff. (For contrast the tool's top row is `EQ` at
`concentration_pct = 100` on 1,201 contracts.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` / SQL path | Rows used |
|---|---|---|
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --date 2026-07-27 --json` | `spot=38.01`; K50 `total_oi=33238 role=call_wall_resistance`; K40 `put_oi=21170 net_oi=-12620 role=put_heavy distance_pct=5.24`; K35 `put_oi=23133 net_oi=-18250 role=put_wall_support`; K70 `call_oi=25083 put_oi=11 distance_pct=84.16` ← `.results[]` | 10 |
| `uw oi oi-by-strike --symbol ENPH --top-n 10 --dte-max 30 --date 2026-07-27 --json` | K40 `put_oi=8444 call_oi=1252 net_oi=-7192`; K42.5 `call_oi=3735 put_oi=0`; K35 `put_oi=4217 call_oi=10`; K50 `net_oi=+774` of `total_oi=12884` ← `.results[]` | 10 |
| `uw oi oi-by-strike --symbol ENPH --expiry 2026-07-31 --top-n 12 --date 2026-07-27 --json` | K50 `call_oi=3864 put_oi=0`; K42.5 `call_oi=3591 put_oi=0`; K40 `total_oi=730 net_oi=-18`; K36 `total_oi=261` ← `.results[]` | 12 |
| `uw oi oi-by-strike --symbol ENPH --expiry 2026-08-21 --top-n 12 --date 2026-07-27 --json` | K40 `put_oi=7888 call_oi=850 net_oi=-7038`; K35 `put_oi=3734 call_oi=0`; K50 `put_oi=6055` ← `.results[]` | 12 |
| `uw oi term-structure --symbol ENPH --date 2026-07-27 --json` | `total_oi=241974`, `expiry_count=15`; 2027-01-15 `pct_of_total_oi=24.52 total_oi=59336`; 2026-09-18 `20.51`; 2026-08-21 `18.64 put_call_oi_ratio=1.253`; 2026-07-31 `6.98 put_call_oi_ratio=0.251`; 2027-06-17 `put_oi=52` ← `.term_structure[]` | 15 |
| `uw oi biggest-increases --symbol ENPH --top-n 20 --min-oi-change 500 --date 2026-07-27 --json` | **2 rows**: `ENPH261120C00070000 oi_diff_plain=1324 last_oi=359 curr_oi=1683 volume=1418`; `ENPH261016P00030000 oi_diff_plain=542 volume=624` ← `.results[]` | 2 |
| `uw oi decrease-with-volume --symbol ENPH --top-n 15 --min-volume 100 --date 2026-07-27 --json` | 6 rows, max decrease `ENPH260821P00040000 oi_diff_plain=-97 volume=211` ← `.results[]` | 6 |
| `uw oi smart-positioning --symbol ENPH --top-n 20 --min-oi-change 500 --date 2026-07-27 --json` | C70 `inferred_direction="bearish" net_ask_bid=-1407 prev_ask_volume=4 prev_bid_volume=1411 prev_total_premium=205517`; P30 `inferred_direction="bullish" prev_total_premium=157419` ← `.results[]` | 2 |
| `uw oi position-rolls --symbol ENPH --threshold 500 --near-dte-max 30 --date 2026-07-27 --json` | **`rolls_detected=0`**, `results=[]`, `caveat="Single-day detection only…"` | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-07-27 --json` | ENPH **absent** ← `[.results[]\|select(.ticker=="ENPH")]` → `[]`; top row SPY `pin_score=2078720.99` | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-07-27 --json` | ENPH **absent** ← same path → `[]` (max ENPH concentration 24.52% < 40% filter) | top-20 |
| DuckDB `chain-oi-changes-2026-07-27.parquet` (ENPH) | `n_rows=344`, `last_date=2026-07-24`, `curr_date=2026-07-27`, `Σvolume=12765`; `ENPH261120P00035000 last_oi=407 curr_oi=412 oi_diff_plain=5`; tail hedges `ENPH261120P00022500 +210 ask_v=227 bid_v=0`, `ENPH261120P00017500 +86 ask_v=86 bid_v=0` | 344 |
| DuckDB `bot-eod-report-2026-07-27.parquet` (ENPH Nov-20 P35) | 800-lot print `side=mid premium=464000 canceled=False report_flags={futures_floor} upstream_condition_detail="slft" open_interest=412 executed_at=11:06:45.512711-04:00` | 6 |

## Tool errors

No `uw` command errored; all exited 0 and round-tripped through `jq`. **Two
dataset conflicts** are surfaced here rather than buried, because they bear
directly on phase-1's and phase-2's conclusions:

**1. Nov-20 P35 — `All Options` and `OI changes` disagree on volume by 135×.**

| Source | Reported day volume | OI |
|---|---|---|
| `bot-eod-report-2026-07-27.parquet` (All Options) | **811** (805 mid + 4 ask + 2 bid) | `open_interest = 412` |
| `chain-oi-changes-2026-07-27.parquet` | **6** | `last_oi 407 → curr_oi 412` |

The conflict runs the **other way** on Nov-20 C70: All Options captures only **3**
contracts while OI-changes reports **1,418** with OI +1,324. So neither file is a
complete tape — `bot-eod-report` appears to be a **filtered notable-print feed**
(it caught the floor cross but almost none of the C70 selling), while OI-changes
tracks per-contract volume aligned to the OI delta.

**What is robust:** both sources independently report **OI = 412** on Nov-20 P35,
and OI-changes gives the prior value **407**. **Open interest moved +5, under
either reading.** That fact — the decision-relevant one — does not depend on
resolving the volume conflict, and it is what this phase relies on. Cross-check:
Σ OI-changes volume for ENPH = **12,765** vs the screener's `call_volume + put_volume
= 14,999` (85% coverage), so OI-changes is the closer proxy for true chain volume.

**2. Jun-2027 puts — phase-1's sweeps have no OI footprint.** Phase-1 reported 258
contracts sold on the bid in Jun-2027 P40/P45 ($366,560). Those `option_symbol`s
return **zero rows** in the OI-changes parquet, and `term-structure` shows
**total Jun-2027 put OI = 52** across all strikes. 258 contracts cannot trade
against 52 OI and leave it at 52. **Unresolved.** Most likely the same
floor/negotiated-print class as the P35 cross (not OI-generating), but I cannot
demonstrate it. Flagged for **phase-10** as an open internal inconsistency.

## DATA NOTE / CORRECTION

**CORRECTION TO PHASE 2 — issued here, to be reconciled by phase-10.**

`phase-2-dark-pool.md` concluded: *"The customer was the put buyer… This upgrades
the day's largest option print from unattributable to genuine downside demand."*
**That conclusion is downgraded.**

- **What stands (factual):** exactly one DP print within ±5 min of the option
  print; **28,800 shares**, classified `hit`, at **11:06:45.556 ET** vs the option
  at **11:06:45.512711 ET**; implied put delta **27,608 shares**; **96% match**.
  Phase-2 also correctly flagged that the block printed **$0.48 below the NBBO bid
  at exactly the prior close ($36.70)**, calling it "a negotiated block priced at a
  reference".
- **What is new:** `report_flags = {futures_floor}`, `upstream_condition_detail =
  "slft"` (single-leg floor trade), and **`last_oi 407 → curr_oi 412` (+5)**.
- **Revised interpretation:** the option and stock legs are a **negotiated,
  delta-neutral floor package**, and **the position did not open**. The stock leg
  was part of the cross, not a dealer hedging in the open market — which also
  explains the below-bid reference price phase-2 could not account for. This is an
  **existing position changing hands**, so it adds **no net new downside exposure**
  to the market.
- **Net effect on the thesis:** phase-2's conviction of 2/5 and its
  "MIXED, leaning DISTRIBUTION" bias are **unchanged or slightly softened**; the
  one piece of evidence it treated as a genuine bearish upgrade is withdrawn.
  Phase-2's own caveat — *"Coincidence cannot be fully excluded… Phase-3 can settle
  it — if 2026-07-28 OI on the Nov-20 $35 put rises by ~800, the position opened"*
  — is exactly the test that has now been run, **one day earlier than anticipated
  and against the hypothesis.** Phase-2 asked the right question; the answer is no.

Other notes:

- **`biggest-increases` `oi_change` is a ratio, not a delta** (C70: `oi_change =
  3.688` vs `oi_diff_plain = 1324`). Only `oi_diff_plain` is quoted as a contract count.
- **Expiry/side parsed from OPRA `option_symbol`**, per phase-3 guidance:
  `ENPH261120C00070000` → 2026-11-20 / Call / $70; `ENPH261016P00030000` →
  2026-10-16 / Put / $30. Both spot-checked against `strike` and `dte`
  (116 → 2026-11-20 ✓, 81 → 2026-10-16 ✓).
- **`term-structure` `total_oi = 241,974` vs `insights deep-dive`
  `total_open_interest = 355,935`** — a **32% gap** between two UW surfaces on the
  same date. Not reconciled. All wall/cliff percentages here are computed on the
  `term-structure` denominator and are internally consistent; **do not mix the two
  totals**. Flagged for phase-10.
- No value written in this phase was corrected after first read.

## Verdict for downstream phases

- **Positioning bias:** **PREMIUM SELLING / SHORT VOL, with protective puts held
  and deep tail hedges bought.** Not a directional book. The two OI builds ≥500 are
  both sales (C70 +1,324, P30 +542); the only unambiguous buying is Nov P22.50 /
  P17.50 tail insurance at −41% / −54%. Existing put protection in Aug/Sep is
  **held, not unwound** (largest closure −97).
- **Conviction:** **2 / 5.** Two qualifying builds in an entire chain is close to
  no positioning at all; `rolls_detected = 0`; ENPH absent from both `pin-risk` and
  `opex-concentration`. What conviction exists attaches to the **C70 sale**
  (`net_ask_bid = −1,407`, 99.5% bid-side) — clean and unambiguous, but 84% OTM and
  therefore a statement about the *tails*, not the next move.
- **Largest OI build as % of float:** **0.104%** (1,324 contracts = 132,400
  share-equivalents ÷ 127.77M). **Not structural for this name** — the same order
  as the largest dark-pool block (0.101%). Advisory, de-rating only; raises nothing.
- **Three pin/cliff strikes for phase-9** (sourced from `oi-by-strike` roles and the
  `term-structure` cliff, not hand-picked):
  1. **$35.00 — `put_wall_support`**, −7.92%. 4,217 puts vs **10** calls at ≤30 DTE
     (23,133 puts all-expiry). The cleanest support in the chain and the strongest
     level phase-9 has. Corroborated by `2026-08-21` carrying 3,734 puts / 0 calls
     there, and by phase-2's $36.70 most-transacted DP level just above it.
  2. **$42.50 — `call_wall_resistance`**, +11.81%. 3,735 calls, **zero puts** at
     ≤30 DTE. The **only** genuine near-term overhead wall; everything above ($50,
     $55, $60, $70, $75) is stranded legacy OI 31–97% OTM with no hedging effect.
  3. **$40.00 — `put_heavy`**, +5.24%. 8,444 puts vs 1,252 calls (≤30 DTE); 7,888
     puts at 2026-08-21 alone. ⚠️ **Not support** — spot is *below* it, so this is
     **in-the-money protection**, i.e. a supply overhang of hedged stock, not a
     floor. Phase-9 must not invert its sign.
  **OPEX cliff for reference: 2026-08-21 (18.64%) and 2026-09-18 (20.51%)** —
  2027-01-15's 24.52% is a LEAP anchor at 172 DTE, not tradeable.
- **Three things later phases must remember:**
  1. **There is no dealer structure to constrain tomorrow's move.** The earnings
     expiry holds **6.98%** of OI, ~2,000 contracts inside the ±12.25% implied
     move, and **55% of its call OI is parked at $42.50/$50 with zero puts**.
     ENPH is absent from `pin-risk`. **No pin, no wall, no gamma brake** — the
     print sets the price.
  2. **The 800-lot Nov-20 $35 put did not open a position** (`407 → 412`,
     `{futures_floor}` / `slft`). **Phase-2's "downside demand" upgrade is
     withdrawn.** Do not carry it into phase-8, 8b or 9.
  3. **Today's real positioning is a short strangle with a tail hedge** — C70 and
     C75 and P35 and P30 all **sold** (~$0.7M collected), Nov P22.50/P17.50
     **bought outright**. Someone is being paid to say ENPH stays between roughly
     **$30 and $50** while insuring against a collapse below **$22.50**. That is a
     *range* view, and it sits in direct tension with phase-1's persistent
     directional bearish sweep campaign — **phase-8b must adjudicate**.
- **Open questions:**
  - Does the **$42.50 call wall** (3,735 contracts, zero puts, +11.8%) exert real
    gamma resistance, or is it too small to matter against a 12.25% implied move?
    → **phase-4** (GEX, `zero_gamma_level`)
  - Front-week IV ~170% while back-month wings are being **sold** — is the term
    structure genuinely kinked at 2026-07-31, and by how much? → **phase-4**
    (`iv-term-structure`, `term-skew`)
  - August/September put protection is **held, not unwound** into the print. Is that
    conviction, or simply hedges too far ITM to be worth closing? → **phase-7c**
  - The **Jun-2027 put trades have no OI footprint** and Jun-2027 put OI is **52**
    against 258 contracts reportedly traded. Real trades outside the OI dataset, or
    a phase-1 artifact? → **phase-10** (unresolved contradiction)
