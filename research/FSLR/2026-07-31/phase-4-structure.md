# Phase 4 — Dealer Structure & Gamma

**Ticker:** FSLR
**As-of date:** 2026-07-31
**Generated:** 2026-07-31
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

**Dealers are short gamma below $215.03, and the single most important number
in this run is the gamma wall at $217.50.** `uw options-structure gex` returns
`regime = "NEGATIVE"` — *"Dealers net short gamma — expect trend acceleration
and increased volatility"* — with `zero_gamma_level = 215.03` against a spot
of 212.24 (211.03 official close). Spot sits **below** the ZGL, so hedging
**amplifies** moves in either direction rather than damping them.

The per-strike surface shows why $217.50 matters so much: **net_gex
+2,344,544 at that one strike is 78% of the entire summed gamma across all
strikes**, and it lines up exactly with phase-3's only clean near-term call
wall (net_oi +3,139, +3.07%) and sits just above phase-2's institutional block
level at $214.00. **The 214–217.5 band is now triple-confirmed from three
independent datasets.** Between the 215.03 flip and that wall, a move through
$215 should accelerate — then stall hard.

Two tool labels contradict their own underlying data and must not be traded:
**`iv-term-structure` reports `BACKWARDATION` purely on a 224.2% 0DTE
artifact** (ex-0DTE the curve is a normal downward slope from 79.6% at 21 days
to 61.4% at 539), and **`total_gex` is reported positive (+2,993,842) while
the regime label says dealers are net short gamma.** The clean read is
`front-end-iv-ratio`: near 0.7595 / far 0.7588, **ratio 1.001, regime FLAT** —
earnings vol has already normalized, exactly one day after the print.

Skew is **COMPLACENT** (25Δ puts 0.7613 *cheaper* than 25Δ calls 0.7652,
`skew_ratio` 0.995) and near-dated max pain clusters at **205–210, just below
spot**. Vanna is the one genuinely constructive mechanism: a put-heavy public
book means falling IV forces dealers to **buy** stock — and IV is falling.

## Key signals

- **`regime = NEGATIVE`, `zero_gamma_level = 215.03`, spot 212.24 → short
  gamma; dealer hedging amplifies moves** `[STRUCT:gex]`
- **$217.50 gamma wall: net_gex +2,344,544 — 78% of total summed per-strike
  gamma**, and the 0DTE book independently tagged it `support_wall` at
  +2,339,132 `[STRUCT:gex]` `[STRUCT:today_gamma_flip]`
- **Term skew COMPLACENT: 25Δ put IV 0.7613 < 25Δ call IV 0.7652,
  `skew_ratio` 0.995, skew −0.0039** — puts cheaper than calls, no tail-hedge
  bid `[STRUCT:term_skew]`
- **`front-end-iv-ratio` FLAT at 1.001** (7d 0.7595 vs 28d 0.7588) — event
  stress fully discharged one day after earnings `[STRUCT:front_end_iv_ratio]`
- **Vanna-squeeze setup live**: `net_vanna +347` (put-heavy book), falling IV →
  dealers short puts **buy** underlying `[STRUCT:vanna_charm]`
- **DEX −56,310,922** (call +143.5M / put −199.9M): public net put-long →
  dealer static hedge is to **sell** underlying `[STRUCT:dex]`
- **Near max pain sits *below* spot: 205–210** across 0/7/14/28 DTE — mild
  downward gravity `[STRUCT:max_pain]`
- **Aug-21 max pain of $250 (+18.47%) is not tradeable** — roughly a 5σ move
  in 21 days at the current 0.76%/day implied `[STRUCT:max_pain]`

## Detailed findings

### GEX

| Field | Value |
|-------|------:|
| `regime` | **NEGATIVE** |
| `regime_description` | *"Dealers net short gamma — expect trend acceleration and increased volatility"* |
| `zero_gamma_level` | **215.03** |
| `underlying_price` | 212.24 |
| `total_gex` | +2,993,842 ⚠ |
| Σ `per_strike[].net_gex` (cross-check) | **+2,345,141** ⚠ |
| `dte_max` | 45 |

Per-strike net GEX around spot:

| Strike | net_gex | Read |
|-------:|--------:|------|
| 190 | −583,415 | Negative pocket — downside accelerant |
| 195 | −96,366 | |
| 197.5 | −47,191 | |
| **200** | **−465,782** | Negative pocket at phase-3's put wall |
| 202.5 | +53,052 | |
| 205 | +83,834 | |
| 207.5 | +113,491 | |
| **210** | **+685,342** | Second-largest positive |
| **212.5** | **+476,419** | Positive, just above spot |
| 215 | +243,616 | ZGL vicinity |
| **217.5** | **+2,344,544** | **The wall — 78% of summed gamma** |
| **220** | **−620,582** | Negative immediately above the wall |
| 222.5 | +29,893 | |
| 225 | +95,222 | |
| 230 | +39,892 | |
| 250 | −262,268 | |
| 280 | +361,157 | |

The structure is a **positive-gamma shelf from 202.5 to 217.5, walled by
negative pockets at 200 below and 220 above**. Practical consequences:

- **Below 200 and above 220, dealer hedging accelerates the move.** These are
  the break-out/break-down thresholds.
- **Between roughly 202.5 and 217.5, hedging is stabilising** — chop, mean
  reversion, suppressed realized vol.
- **The ZGL at 215.03 sits inside that shelf, 1.9% above the close.** Because
  spot is below it, the tool's regime is NEGATIVE, but the strike-level detail
  says the *immediate* neighbourhood (210–212.5, both firmly positive) is
  stabilising. Per the pitfall that ZGL on a single name is coarse, treat
  **215.03 ± 2% (≈ 210.7–219.4)** as a transition band rather than a line.

**$217.50 deserves separate emphasis.** Three independent datasets now
converge on it:

| Source | Evidence |
|--------|----------|
| Phase 4 GEX (≤45 DTE) | net_gex **+2,344,544** — the dominant strike |
| Phase 4 `today-gamma-flip` (0DTE) | `support_wall`, gex **+2,339,132** — its largest wall |
| Phase 3 `oi-by-strike` (≤30 DTE) | `call_wall_resistance`, **net_oi +3,139** (3,172 calls vs 33 puts), +3.07% |

Combined with phase-2's dark-pool institutional level at **$214.00** (28,000
shares, $5.99M, bought above the offer), **214.00–217.50 is the most
strongly-evidenced price zone in this entire deep dive.**

### DEX

| Field | Value |
|-------|------:|
| `call_dex` | +143,549,154 |
| `put_dex` | −199,860,076 |
| **`net_dex`** | **−56,310,922** |
| `spot` | 212.24 |
| `interpretation` | *"Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."* |

Public carries **net short delta of −$56.3M**, driven by a put book almost
$200M in delta-notional. Dealers hold the inverse (+$56.3M long delta) and
statically hedge by **selling stock** — a persistent, mechanical supply
overhang.

Two caveats materially limit this reading:

1. **DEX assumes the entire public side is long every contract.** That is a
   crude convention. Phase 3 showed the near-term book is genuinely put-skewed
   (Aug-21 P/C 1.166, Aug-07 P/C 1.503), so the *direction* is credible even
   if the magnitude is not.
2. **It contradicts a position we have actually observed.** Phase 2 proved a
   dealer is **short 1,900 Aug-21 $230 calls and long 72,200 shares** via the
   QCT hedge. That is a dealer *buying* stock. DEX's blanket assumption cannot
   see specific hedges of this kind. **Net dealer flow is therefore the
   difference between a general short-delta hedge and a specific long-stock
   hedge**, and DEX alone overstates the selling pressure.

### Vanna + charm

| Field | Value |
|-------|------:|
| `net_vanna` | **+347** |
| `call_vanna` | −411 |
| `put_vanna` | +759 |
| `net_charm` | +6,631 |
| `spot` | 212.19 |
| `vanna_interpretation` | *"Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."* |

**This is the phase's most constructive finding, and unlike a "if VIX
collapses" hypothetical, the trigger is already firing.** Phase 0.5 documented
the crush in progress: IV rank **94.6 → 81.9** and `iv30d` **0.795 → 0.738**
in one session. Continued normalization mechanically obliges dealers short
puts to **buy** stock.

It also partially offsets DEX: the static hedge sells, the vanna dynamic buys.

**Discount the magnitude heavily.** The tool's own note flags these as
*"Closed-form approximations… Coarse for deep ITM/OTM and near-expiry."* A
`net_vanna` of +347 against a `net_dex` of −56,310,922 are not comparable
units, and no relative sizing should be inferred. Treat vanna as a
**directional mechanism that is real but unquantified here**.

`net_charm` +6,631 is likewise directionally supportive (time decay on a
put-heavy book bleeds delta toward dealer buying) and equally coarse.

### IV term structure

`structure = "BACKWARDATION"`, `kink_expiry = null`, `expiry_count = 15`.

| Expiry | DTE | `avg_iv` | | Contracts |
|--------|----:|---------:|--|----------:|
| 2026-07-31 | 0 | **2.2423** | **224.2%** ⚠ artifact | 1,797 |
| 2026-08-07 | 7 | 0.7595 | 75.9% | 1,000 |
| 2026-08-14 | 14 | 0.7828 | 78.3% | 341 |
| **2026-08-21** | 21 | **0.7963** | **79.6%** ← hump | 842 |
| 2026-08-28 | 28 | 0.7588 | 75.9% | 178 |
| 2026-09-04 | 35 | 0.7566 | 75.7% | 126 |
| 2026-09-11 | 42 | 0.7473 | 74.7% | 85 |
| 2026-09-18 | 49 | 0.7181 | 71.8% | 954 |
| 2026-10-16 | 77 | 0.6783 | 67.8% | 327 |
| 2026-12-18 | 140 | 0.6684 | 66.8% | 93 |
| 2027-01-15 | 168 | 0.6519 | 65.2% | 229 |
| 2027-03-19 | 231 | 0.6379 | 63.8% | 43 |
| 2027-06-17 | 321 | 0.6371 | 63.7% | 55 |
| 2028-01-21 | 539 | 0.6139 | 61.4% | 47 |
| 2028-06-16 | 686 | 0.6156 | 61.6% | 23 |

**The `BACKWARDATION` label is an artifact and must not be traded.** It is
produced entirely by the 0DTE row at **224.2%** — an expiration-day pricing
distortion across 1,797 contracts, the same artifact phase 1 documented when
*all fifteen* IV outliers turned out to be 0DTE with `max_iv` 18.34.

**Ex-0DTE the curve is normal**: a mild hump at the Aug-21 monthly OPEX
(79.6%) then a clean monotonic decline to 61.4% at 539 days. That is
textbook downward-sloping long-end, not backwardation.

The independent, 0DTE-free tool agrees — see below. And the standing pitfall
applies directly: *"don't trade backwardation if earnings already passed
within 24h."* FSLR reported **2026-07-30 AMC**, well inside 24 hours.

The **Aug-21 hump (79.6%, the local maximum ex-0DTE)** is the one real feature:
it is the monthly OPEX, it carries 13.34% of tracked OI at P/C 1.166
(phase 3), and it is where the 1,900-lot $230 call block (phase 1) expires.
**Aug-21 options are the richest on the board — an argument for selling, not
buying, that expiry's premium.**

### Term skew

| Field | Value |
|-------|------:|
| `put_25d_iv` | **0.7613** |
| `call_25d_iv` | **0.7652** |
| `skew` | **−0.0039** |
| `skew_ratio` | **0.995** |
| `interpretation` | **COMPLACENT** |
| `dte_actual` / `dte_target` | 28 / 30 |

**25-delta puts are cheaper than 25-delta calls** — a genuine inversion of the
normal equity skew, where downside protection almost always commands a
premium. There is **no tail-hedging bid** in FSLR at the 28-day tenor.

Read against phase 3, this sharpens rather than contradicts: the near-term
book is put-*heavy* by open interest (Aug-21 P/C 1.166) yet put-*cheap* by
implied vol. Those puts are **legacy positions, not fresh demand** — consistent
with phase 3's reading of a protective ladder left over from the earnings
event rather than new bearish conviction. It also fits phase 1's finding that
genuinely directional OTM put buying totalled just **$266K** against $2.59M of
new call premium.

Two-sided implication: complacency means **cheap protection for a long
position**, and it means **the market is not braced for a downside shock**.
The standing heuristic (skew *steepening* precedes risk-off) is not firing —
but the absence of a hedge bid is itself a fragility.

### Front-end IV ratio

| Field | Value |
|-------|------:|
| `near_iv` (7 DTE actual) | 0.7595 |
| `far_iv` (28 DTE actual) | 0.7588 |
| `ratio` | **1.001** |
| `regime` | **FLAT** |

**This is the trustworthy term-structure read** — it samples 7 vs 28 DTE and
therefore excludes the 0DTE artifact that corrupted `iv-term-structure`. A
ratio of 1.001 is as flat as this measure gets: **no event stress remains**.

Where the two tools disagree, **`front-end-iv-ratio` FLAT is correct and
`iv-term-structure` BACKWARDATION is contaminated.** Phase 10 should treat
this as a resolved conflict, not an open contradiction.

Practical consequence: **there is no cheap-vol trade and no expensive-vol
trade at the front end.** Post-earnings IV-crush selling is largely done —
consistent with phase 0.5's finding that IV rank 81.94 is only the **39.4th
self-percentile** for a name that habitually runs high vol.

### Today's gamma flip (0DTE)

| Field | Value |
|-------|------:|
| `today_expiry` | 2026-07-31 |
| `regime` | **POSITIVE** |
| `today_total_gex` | 3,444,464 |
| `today_zero_gamma` | 187.99 |
| `atm_flip_strike` | 172.5 |
| `spot` | 212.40 |

`key_walls`:

| Strike | gex | role |
|-------:|----:|------|
| **217.5** | **+2,339,132** | support_wall |
| 210 | +754,684 | support_wall |
| **220** | **−601,867** | **resistance_wall** |
| 212.5 | +360,884 | support_wall |
| 215 | +202,736 | support_wall |

**This describes a session that has now closed** — 2026-07-31 was the 0DTE
expiry and these contracts have expired. Per the phase-4 guidance that this
tool is intraday-only, **it carries no forward tradeable signal** and is
recorded for corroboration only.

Its corroborative value is nonetheless high: computed on a completely separate
(0DTE) book, it independently reproduces the ≤45-DTE surface almost
strike-for-strike — **217.5 largest positive, 220 negative, 210/212.5/215
positive**. Two different expiry books agreeing this closely is meaningful
confirmation that the 217.5 wall and 220 negative pocket are structural
features of FSLR's chain, not a one-expiry accident.

Note the 0DTE book was **POSITIVE gamma with ZGL 187.99** (spot far above),
which is why today's session mean-reverted — phase 0.5 recorded a **+3.29%
gap that faded −0.82% from the open** to close +2.44%. Dealer long-gamma
hedging into today's expiry is a clean mechanical explanation for that fade.

### Max pain

`spot = 211.02`, `dte_max = 30`. Source is the **OI-changes parquet**, so per
`phase-3-positioning.md` it inherits the **one-session lag** and the
**38.9% chain coverage**. Tool caveat: *"Max pain assumes settlement at each
candidate strike with current open interest unchanged to expiry."*

| Expiry | DTE | **Max pain** | Distance % | P/C OI | Total OI |
|--------|----:|-------------:|-----------:|-------:|---------:|
| 2026-07-31 | 0 | **210** | −0.48 | 0.589 | 15,376 |
| 2026-08-07 | 7 | **205** | −2.85 | 1.503 | 3,084 |
| 2026-08-14 | 14 | **210** | −0.48 | 0.374 | 1,432 |
| **2026-08-21** | **21** | **250** | **+18.47** | 1.166 | **29,922** |
| 2026-08-28 | 28 | **205** | −2.85 | 0.785 | 896 |

**The tradeable magnet is 205–210 — below spot.** Four of five expiries pin
there, and it aligns tightly with phase-2's dark-pool support shelf at
**205.83–206.01** and phase-3's **$200** put wall. Mild but consistent
downward gravity in the next month.

**The Aug-21 reading of $250 must be discarded as a tradeable target.** At
+18.47% with the implied move at **0.76%/day** (phase 0.5), a 21-day 1σ move
is roughly **√21 × 0.76% ≈ 3.5%** — so $250 is about a **5σ** event. It is an
artifact of a lopsided put book: phase 3 showed Aug-21 $250 puts carry **3,695
OI**, the largest put position in that expiry, so the pain function is
minimised where those puts die. **Max pain at an unreachable strike is
arithmetic, not gravity.** Per the pitfall on static-OI estimates, and given
that Aug-21 is the highest-OI near expiry (29,922) actively being traded, this
level will migrate substantially.

Cross-check against phase 3 as the guidance requires: the near-expiry max pain
(205–210) **agrees** with phase-3's put walls at 200/210 and the
`oi-by-strike` support ladder. The Aug-21 250 **disagrees** with everything —
correctly, since phase 3 independently tagged 250 as `put_heavy` (net_oi
−893).

### Note on spot price across tools

Five different spot values appear in this phase: `gex` 212.24, `dex` 212.24,
`vanna-charm` 212.19, `today-gamma-flip` 212.40, `max-pain` 211.02 — against
the official close of **211.03** (`phase-0.5-context.md`). The
options-structure tools read a last-trade/underlying print from the options
tape (which extends past the equity close), while max-pain reads `stock_price`
from the OI file.

The spread is ~0.65%. **All price levels quoted downstream should reference
the official close of 211.03**, and GEX/DEX distances re-based accordingly —
e.g. the ZGL at 215.03 is **+1.90% above the close**, not +1.31% above 212.24.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --symbol FSLR --dte-max 45 --date 2026-07-31 --json` | regime="NEGATIVE", zero_gamma_level=215.03, total_gex=2993842, underlying_price=212.24 ← `.{regime,zero_gamma_level,total_gex,underlying_price}`; 217.5 net_gex=2344544.18 ← `.per_strike[]\|select(.strike==217.5).net_gex`; Σ per_strike=2345140.73 ← `[.per_strike[].net_gex]\|add` | 45 strikes |
| `uw options-structure dex --symbol FSLR --dte-max 45 --date 2026-07-31 --json` | net_dex=−56310922, call_dex=143549154, put_dex=−199860076 ← `.{net_dex,call_dex,put_dex}`; interpretation ← `.interpretation` | 1 |
| `uw options-structure vanna-charm --symbol FSLR --dte-max 45 --date 2026-07-31 --json` | net_vanna=347, put_vanna=759, call_vanna=−411, net_charm=6631 ← `.{net_vanna,put_vanna,call_vanna,net_charm}` | 1 |
| `uw options-structure iv-term-structure --symbol FSLR --date 2026-07-31 --json` | structure="BACKWARDATION", kink_expiry=null ← `.{structure,kink_expiry}`; 0DTE avg_iv=2.2423 / contract_count=1797 ← `.term_structure[0]` (**rows under `.term_structure`; key is `avg_iv`, and `dte_approx` not `dte`**) | 15 |
| `uw options-structure term-skew --symbol FSLR --dte-target 30 --date 2026-07-31 --json` | put_25d_iv=0.7613, call_25d_iv=0.7652, skew=−0.0039, skew_ratio=0.995, interpretation="COMPLACENT", dte_actual=28 ← `.` | 1 |
| `uw options-structure front-end-iv-ratio --symbol FSLR --near-dte 7 --far-dte 30 --date 2026-07-31 --json` | near_iv=0.7595, far_iv=0.7588, ratio=1.001, regime="FLAT", far_dte_actual=28 ← `.` | 1 |
| `uw options-structure today-gamma-flip --symbol FSLR --date 2026-07-31 --json` | regime="POSITIVE", today_total_gex=3444464, today_zero_gamma=187.99, atm_flip_strike=172.5 ← `.`; 217.5 gex=2339132 role="support_wall" ← `.key_walls[0]` | 5 walls |
| `uw options-structure max-pain --symbol FSLR --dte-max 30 --date 2026-07-31 --json` | 2026-08-21 max_pain=250, distance_pct=18.47, put_call_oi_ratio=1.166, total_oi=29922 ← `.results[3]`; spot=211.02 ← `.spot`; caveat ← `.caveat` | 5 expiries |

## Tool errors

No command errored — all eight exited 0 and every payload parsed.

**Three internal inconsistencies inside successful output**, all material:

1. **`gex`: `total_gex` = +2,993,842 (positive) while `regime` = "NEGATIVE"
   ("dealers net short gamma").** These disagree on their face. The regime
   label is evidently derived from **spot (212.24) vs `zero_gamma_level`
   (215.03)** — spot below ZGL — not from the sign of `total_gex`. Per the
   guidance to quote the tool's own regime label rather than re-derive it,
   **`regime = NEGATIVE` is carried forward**, with the caveat that
   `total_gex`'s sign does not corroborate it.
2. **`gex`: Σ `per_strike[].net_gex` = 2,345,141 vs `total_gex` = 2,993,842 —
   a gap of 648,701 (21.7%).** The per-strike array does not sum to the
   reported total, so `per_strike` is either truncated or filtered differently.
   Per-strike values are used only for **relative** ranking (which strike
   dominates), never as absolute magnitudes.
3. **`iv-term-structure` returns `BACKWARDATION` on a 0DTE artifact.** The
   0DTE row carries `avg_iv` **2.2423 (224.2%)** across 1,797 contracts;
   ex-0DTE the curve slopes normally downward. `front-end-iv-ratio` (7 vs 28
   DTE, no 0DTE) returns **FLAT at 1.001** and is the correct read.

Also noted: `iv-term-structure` rows live under **`.term_structure`** (as in
phase 3's `oi term-structure`), the IV field is **`avg_iv`**, and the DTE
field is **`dte_approx`** — a first extraction keyed on `.dte` and `.iv`
returned `null` for all 15 rows. Caught and corrected before writing; no null
was transcribed.

## DATA NOTE / CORRECTION

No correction to prior phases. Three first-pass readings were overturned here
before writing:

1. **"Term structure is in backwardation → event stress ahead"** → the label
   is a 0DTE artifact; the clean measure says FLAT and the event is behind us.
2. **"Aug-21 max pain 250 implies an 18% upside magnet"** → ~5σ in 21 days;
   an artifact of 3,695 puts sitting at that strike. Discarded.
3. **"total_gex positive → dealers long gamma"** → contradicted by the tool's
   own `regime` label and by spot sitting below the ZGL. The tool's label is
   authoritative per the phase guidance.

`max-pain` reads the **OI-changes parquet**, so it inherits phase 3's
one-session lag and 38.9% coverage. Its numbers describe 2026-07-30
positioning — today's 1,900-lot Aug-21 $230 call block is **not** in the
Aug-21 pain calculation. Adding 1,900 calls at $230 would pull the Aug-21 max
pain **down** from $250 toward spot, reinforcing that the $250 figure is stale
as well as unreachable.

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA / TRANSITIONAL.** `regime = NEGATIVE` with
  spot 1.90% below the 215.03 ZGL — hedging amplifies moves. But the immediate
  neighbourhood (210 +685K, 212.5 +476K) is positive-gamma and stabilising, so
  the honest label is **transitional within a 210.7–219.4 band**, turning
  decisively short-gamma only below **200** (net_gex −465,782) or above
  **220** (−620,582).
- **Conviction: 3 / 5.** Supported by unusually strong cross-dataset agreement
  on the 217.5 wall (three independent sources) and by two clean, uncontested
  reads (`front-end-iv-ratio` FLAT, `term-skew` COMPLACENT). Held below 4
  because three of eight tools returned internally inconsistent or artifact-
  driven output, `max-pain` is built on lagged 38.9%-coverage OI, and the
  tool's own note warns *"GEX most meaningful for index products… and
  large-cap single stocks with deep OI"* — FSLR at $22.7B market cap is at
  the lower edge of that qualification.
- **Three structural levels for phase-9, plus the pin magnet:**
  1. **ZGL $215.03** (+1.90% vs the 211.03 close) — the gamma flip. Above it
     dealer hedging turns stabilising; below it, amplifying. Treat as a
     **±2% band (210.7–219.4)** per the low-liquidity pitfall.
  2. **$217.50 — the largest GEX strike (net_gex +2,344,544, 78% of summed
     gamma).** Triple-confirmed by phase-3's call wall (net_oi +3,139) and
     the 0DTE `support_wall` (+2,339,132). With phase-2's $214.00 block level
     this defines a **214.00–217.50 resistance/target band** — the natural
     first-target and partial-exit zone for any long.
  3. **Vanna pivot — the IV path, not a price.** `net_vanna` +347 on a
     put-heavy book means **continued IV decline mechanically forces dealer
     buying**; an IV *spike* reverses it into selling. Phase 9 should treat
     **rising IV as an invalidation input**, not merely falling price. Watch
     `iv30d` against today's 0.738.
  4. **Max-pain magnet: $205–210** (0/7/14/28 DTE all pin 205 or 210, −0.48%
     to −2.85% from spot). Confirmed by phase-2's 205.83–206.01 dark-pool
     shelf and phase-3's $200 put wall. **The Aug-21 $250 is explicitly
     excluded as unreachable and stale.**
- **Open questions:**
  - **Does the 220 negative-gamma pocket (−620,582) gate or accelerate a
    breakout?** Price must clear the +2.34M gamma wall at 217.5 — where
    dealers sell into strength — before reaching air above 220. **The
    214–217.5 band should therefore be sticky, and 220+ fast.** Phase 9 must
    decide whether to target inside the wall or through it.
  - **Which dominates — DEX's static sell hedge (−$56.3M public delta) or the
    vanna buy from falling IV?** The tools give no common units. Unresolved,
    and phase 8b should not let either side claim it.
  - **Who is short the 1,900 Aug-21 $230 calls, and is that dealer's 72,200
    long shares (phase 2) reflected in DEX?** Almost certainly not — DEX
    assumes public-long-everything. That known position means dealers must
    **buy more** stock as price approaches 230, partially offsetting the DEX
    supply overhang precisely on a rally.
  - **Is the Aug-21 IV hump (79.6%, the ex-0DTE maximum) a premium-selling
    opportunity?** It is the richest expiry, it holds 13.34% of tracked OI,
    and it is where the phase-1 block expires. Phase 9 should weigh
    **selling** Aug-21 premium against **buying** the Sep-18 cliff expiry
    (71.8% IV, 26.81% of OI).
