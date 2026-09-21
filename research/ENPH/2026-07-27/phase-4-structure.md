# Phase 4 — Dealer Structure & Gamma

**Ticker:** ENPH
**As-of date:** 2026-07-27
**Generated:** 2026-07-27T20:55:00-04:00
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

**Short gamma everywhere, dealers hedging by selling — but with a loaded
vanna spring that fires *upward* the moment the event passes.** `gex` returns
`regime = "FULLY_NEGATIVE"` (`regime_description`: *"All strikes have negative net
GEX — strong gamma amplification"*) with `zero_gamma_level = null` — there is no
flip point because **no strike is positive**. `dex` gives `net_dex = −$40,323,765`
with the tool's own reading: *"Public is net put-long → dealers net short puts →
dealer hedge is to SELL underlying."* Both mechanics amplify a downside move.

Against that sits the single most important structural fact for the next two
weeks. `vanna-charm` reports `net_vanna = +913` and states: *"Public net vanna
positive (put-heavy book). Falling IV → |put delta| drops → dealers (short puts)
cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."*
And IV **is** about to collapse — `front-end-iv-ratio` = **1.727**
(`near_iv 1.7009` @ 4 DTE vs `far_iv 0.9846` @ 32 DTE), `iv-term-structure` =
**BACKWARDATION**, with the 2026-07-31 expiry at **170.1%** against ~86% in the
back months. Once the print clears, that 170% front week collapses toward ~90%,
and the mechanical consequence is **dealer buying**.

The third leg is the anomaly: `term-skew` at 32 DTE returns
`interpretation = "COMPLACENT"`, `skew_ratio = 1.001`
(`put_25d_iv 0.9558` vs `call_25d_iv 0.9548`). **Downside protection costs the
same as upside** on a stock down 40% in nine weeks with 17.94% of float short.
That is not a normal price for this risk.

Finally, `max-pain` is **above spot at every near expiry** — **$41 (+7.87%)** for
the earnings week, and **$40 is the max-pain strike for 8 of 15 expiries**,
including the two heaviest (2026-09-18, 49,625 OI; 2027-01-15, 59,336 OI).

## Key signals

- **`regime = "FULLY_NEGATIVE"`, `zero_gamma_level = null`, `total_gex = −566,158`**
  — every one of 50 strikes negative; no long-gamma zone exists [STRUCT:gex].
- **`net_dex = −$40,323,765`** (`put_dex −61,664,586` vs `call_dex +21,340,821`) →
  *"dealer hedge is to SELL underlying"* [STRUCT:dex].
- **`net_vanna = +913` → vanna-squeeze setup on IV collapse** — the post-earnings
  crush from 170% mechanically forces dealers to **buy** [STRUCT:vanna_charm].
- **`front-end-iv-ratio = 1.727`, BACKWARDATION** — 2026-07-31 at **170.1%** vs
  2026-08-21 at 100.7% and 2026-10-16 at **86.3%** [STRUCT:front_end_iv_ratio],
  [STRUCT:iv_term_structure].
- **`skew_ratio = 1.001`, `interpretation = "COMPLACENT"`** — puts and calls priced
  identically at 25Δ. Downside is **cheap** [STRUCT:term_skew].
- **Max pain $41 (+7.87%) for the earnings expiry; $40 for 8 of 15 expiries**
  [STRUCT:max_pain].

## Detailed findings

### GEX

`uw options-structure gex --symbol ENPH --dte-max 45` (`underlying_price = 37.52`):

| Field | Value |
|---|---|
| `regime` | **FULLY_NEGATIVE** |
| `regime_description` | *"All strikes have negative net GEX — strong gamma amplification"* |
| `zero_gamma_level` | **null** |
| `total_gex` | **−566,158** |
| strikes returned | 50 |
| `note` | *"GEX most meaningful for index products (SPY, QQQ) and large-cap single stocks with deep OI."* |

Most-negative strikes (`net_gex`):

| Strike | `net_gex` | vs spot |
|---|---|---|
| **40** | **−1,112,908** | +5.24% |
| **35** | **−502,635** | −7.92% |
| 30 | −303,706 | −21.07% |
| 33 | −109,545 | −13.18% |
| 45 | −95,748 | +18.39% |
| 36 | −55,707 | −5.29% |
| 38 | −42,148 | +0.03% |
| 31 | −34,505 | −18.44% |
| 34 | −30,864 | −10.55% |
| 25 | −15,975 | −34.23% |

**Quoting the tool's label rather than re-deriving it** (per composition guidance):
the regime is **FULLY_NEGATIVE**. `zero_gamma_level = null` is not a missing value —
it is the correct output when the surface never crosses zero. Per the phase-4
heuristic, short gamma means **dealers buy rallies and sell dips → trend
amplification and expanded realized vol.** There is no mean-reverting zone
anywhere in the 45-day surface.

The gamma concentration mirrors phase-3's OI map exactly: the two most negative
strikes, **$40 and $35**, are precisely the `put_heavy` (8,444 puts) and
`put_wall_support` (4,217 puts) strikes from `oi-by-strike --dte-max 30`. The
gamma is negative *because* of the public's long-put book — the same book `dex`
and `vanna-charm` are reading.

⚠️ **Internal inconsistency:** `total_gex = −566,158` but
`[.per_strike[].net_gex] | add = −916,496` — a **62% gap**. The two figures come
from the same payload and disagree. The *sign and regime are unaffected* (both
strongly negative), and no directional conclusion here depends on the magnitude,
but **neither number should be quoted as a precise GEX level**. Flagged for
phase-10; see `## Tool errors`.

**Honest caveat on applicability.** The tool's own `note` warns GEX is most
meaningful for index products and large-caps with deep OI. ENPH is a **$4.84B**
name (`phase-0.5-context.md`) with 241,974 total OI. The FULLY_NEGATIVE label is
robust — it takes no precision to observe that all 50 strikes are negative — but
the magnitudes are coarse. Treat GEX here as **directional regime, not a
calibrated hedging-flow estimate**, and per the pitfall note treat any implied
level as a **±2% band**.

### DEX

`uw options-structure dex --symbol ENPH --dte-max 45` (`spot = 37.52`):

| Field | Value |
|---|---|
| `call_dex` | +$21,340,821 |
| `put_dex` | **−$61,664,586** |
| **`net_dex`** | **−$40,323,765** |
| `interpretation` | *"Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."* |
| `note` | *"DEX = Σ(delta × OI × 100 × spot). Sign reflects public positioning; dealer hedge is the inverse."* |

Put DEX is **2.9× call DEX** in magnitude. The public's book is decisively
long puts, and the mechanical consequence is dealer **supply** of stock.

Scaled for context: −$40.3M of net dealer delta ÷ $38.01 ≈ **1.06M
share-equivalents = 0.83% of the 127.77M float** (`phase-0-intake.md`), or ~0.20×
the 5.24M-share 30-day average volume. **This is the largest positioning number
found anywhere in the run so far** — an order of magnitude beyond the largest OI
build (0.104% of float) or dark-pool block (0.101%). Dealer hedging, not today's
tape, is the dominant flow in this name.

This is the structural explanation for phase-0.5's observation that price fell
15.3% in 13 sessions on unremarkable volume: **a persistent, mechanical seller
sits underneath the stock.**

### Vanna + charm

`uw options-structure vanna-charm --symbol ENPH --dte-max 45` (`spot = 37.52`):

| Field | Value |
|---|---|
| `put_vanna` | +1,208 |
| `call_vanna` | −294 |
| **`net_vanna`** | **+913** |
| `net_charm` | +57,572 |
| `vanna_interpretation` | *"Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."* |
| `note` | *"Closed-form approximations… Coarse for deep ITM/OTM and near-expiry — filtered to dte ≥ 1 by default."* |

**This is the most important finding in phase 4, and it inverts the sign of the
other two.** GEX and DEX both say *sell*. Vanna says that as soon as **IV falls**,
the same short-put dealer book must **buy**.

And IV is not merely likely to fall — it is nearly *certain* to, mechanically:
the 2026-07-31 expiry prices **170.1%** into a binary that resolves tomorrow after
the close. Whatever the outcome, on 2026-07-29 that contract will no longer carry
event premium. `term-skew` shows the 32-DTE surface at ~95.5% and the back months
at ~86%. **A 70-point IV collapse in the front week is the base case, not a
scenario.**

The phase-4 heuristic for a vanna squeeze requires *positive vanna + negative
dealer delta + IV declining*. **All three conditions are met** —
`net_vanna = +913` ✓, `net_dex = −$40.3M` (dealers short delta via short puts) ✓,
IV collapse imminent ✓. This is a textbook setup.

**Two disciplined qualifications:**

1. **It is conditional on price, not just vol.** Vanna operates through
   `∂delta/∂σ`. If ENPH *gaps down* on the print, the **spot** move dominates:
   put deltas rise on the move far faster than they fall on the IV crush, and
   dealers sell into it (the FULLY_NEGATIVE gamma). The vanna bid is real **if the
   stock holds or rallies**, and is overwhelmed if it breaks. It is therefore an
   **asymmetry amplifier on the upside**, not a floor.
2. **`net_vanna = +913` is a small absolute number** and the tool flags its own
   closed-form approximation as coarse. The *direction* is trustworthy; the
   magnitude is not. Do not size on it.

`net_charm = +57,572` (positive) adds a mild same-direction drift as the front
week decays into 2026-07-31.

### IV term structure

`uw options-structure iv-term-structure --symbol ENPH` →
`structure = "BACKWARDATION"`, `kink_expiry = null`, `expiry_count = 15`:

| Expiry | ~DTE | `avg_iv` | vs back-month (~86%) |
|---|---|---|---|
| **2026-07-31** | 4 | **1.7009 (170.1%)** | **1.97×** |
| 2026-08-07 | 11 | 1.2147 | 1.41× |
| 2026-08-14 | 18 | 1.0837 | 1.26× |
| 2026-08-21 | 25 | 1.0074 | 1.17× |
| 2026-08-28 | 32 | 0.9846 | 1.14× |
| 2026-09-04 | 39 | 0.9311 | 1.08× |
| 2026-09-18 | 53 | 0.8957 | 1.04× |
| **2026-10-16** | 81 | **0.8626** | **1.00× (trough)** |
| 2026-11-20 | 116 | 0.8923 | 1.03× |
| 2026-12-18 | 144 | 0.8702 | 1.01× |
| 2027-01-15 | 172 | 0.8581 | 0.99× |
| 2027-02-19 | 207 | 0.8736 | 1.01× |
| 2027-06-17 | 325 | 0.8736 | 1.01× |
| 2028-01-21 | 543 | 0.8689 | 1.01× |
| 2028-12-15 | 872 | 0.8537 | 0.99× |

The curve decays **monotonically** from 170.1% to a trough of 86.3% at 81 DTE,
then sits flat at ~85–89% out to 2028. `kink_expiry = null` is correct: this is
a clean, smooth backwardation, **not** a kinked surface.

**This resolves phase-0.5's open question definitively.** Phase-0.5 flagged that
`iv30d` was *falling* into the print (1.017 → 0.922 over six sessions) and asked
whether the event was underpriced or the curve was simply rolling.
**Answer: neither — the event premium is real but concentrated in one expiry.**
`iv30d` is a 30-day construct; as the earnings date approached, the 170% weekly
became a smaller weight in a 30-day window increasingly dominated by ~100%
August vol. The 30-day number fell *because* the event compressed into the front
week. **The event is priced, and priced richly.** Phase-1 reached the same
conclusion from the IV-outlier concentration; the two agree.

Note also the flat ~86% back end confirms phase-0.5's self-history read: ENPH's
*structural* vol level is ~86–92%, and `iv30d = 0.922` at the **54.8th
self-percentile** is simply normal for this name.

### Term skew

`uw options-structure term-skew --symbol ENPH --dte-target 30`
(`dte_actual = 32`):

| Field | Value |
|---|---|
| `put_25d_iv` | 0.9558 |
| `call_25d_iv` | 0.9548 |
| `skew` | **0.001** |
| `skew_ratio` | **1.001** |
| `interpretation` | **COMPLACENT** |

**25-delta puts are priced 0.1 vol points above 25-delta calls.** For practical
purposes the skew is **zero**.

This is genuinely anomalous and it matters more than any single flow print in
this run:

- Equity skew is normally *persistently* positive — puts trade above calls because
  downside gaps are the risk that must be insured.
- ENPH is **−40.6% in nine weeks** (`phase-0.5-context.md`), **−48.5% from its
  52-week high**, carries **17.94% short float** (`phase-0-intake.md`), sits in a
  **FULLY_NEGATIVE gamma** regime with dealers mechanically selling, and reports
  a binary tomorrow.
- Every one of those facts argues puts should be *bid*. They are not.

Phase-1 independently observed the same thing at the front: the 2026-07-31 ATM
strikes price P36.5 at 1.721 vs C36.5 at 1.716 — flat. **The flatness holds
across the near curve.**

Two readings, and phase-8b should argue them:

- **Complacency (the tool's own label):** the market is under-pricing left-tail
  risk in a name with every structural reason to gap down. Cheap puts = the
  efficient way to express bearishness.
- **Genuine two-sidedness:** with the stock already halved and 17.94% short,
  the market prices a real *upside* gap (short covering on a beat) as symmetric
  to the downside. Flat skew is then correct, not complacent.

**Either way, one conclusion is unambiguous and directly actionable for phase-9:
downside convexity is unusually cheap relative to upside.** Any bearish
expression should be **long puts outright**, not put spreads — spreads give away
the cheap convexity for nothing. And any bullish expression should *not* fund
itself by selling puts, since it would be selling the underpriced wing.

### Front-end IV ratio

`uw options-structure front-end-iv-ratio --symbol ENPH --near-dte 7 --far-dte 30`:

| Field | Value |
|---|---|
| `near_iv` (`near_dte_actual = 4`) | **1.7009** |
| `far_iv` (`far_dte_actual = 32`) | 0.9846 |
| **`ratio`** | **1.727** |
| `regime` | **BACKWARDATION** |

A **72.7% front-end premium** — unambiguous event stress, exactly as expected one
day before a confirmed post-close print. Cross-checks cleanly against
`iv-term-structure` (170.1% / 98.46% = 1.727 ✓) and against phase-1's finding that
**all 15 IV outliers** sat in 2026-07-31.

**Implied vs realized cross-check.** The `implied_move_perc = 12.25%`
(`phase-0.5-context.md`) is the market's price for the event. ENPH's realized
daily moves over the last 15 sessions include **−6.74%, −5.63%, −5.08%, +4.47%,
+4.35%, +3.95%, +3.57%** — a stock that routinely moves 4–7% on *no* catalyst.
A 12.25% one-day expectation is roughly **2× its ordinary daily range**, which for
a name with ENPH's earnings history is **not obviously rich**. Phase-5 (`vrp`)
owns the formal verdict; the preliminary read is **fairly priced, not a giveaway
in either direction.**

### Today's gamma flip

`uw options-structure today-gamma-flip --symbol ENPH`:

| Field | Value |
|---|---|
| `today_expiry` | **2026-07-31** |
| `spot` | 37.74 |
| `today_total_gex` | **+1,047,168** |
| `regime` | **POSITIVE** |
| `today_zero_gamma` | 42.21 |
| `atm_flip_strike` | 38 |

`key_walls`:

| Strike | `gex` | `role` |
|---|---|---|
| **42.5** | **+703,006** | support_wall |
| 50 | +288,055 | support_wall |
| 45 | +97,048 | support_wall |
| **33** | **−71,465** | **resistance_wall** |
| 43 | +61,996 | support_wall |

⚠️ **De-rated per the phase-4 instruction.** This tool is specified as *"0DTE-only
and intraday — only meaningful if running the skill during the trading session.
If after-hours, note and skip."* This run is **after-hours on an as-of date**, and
the tool anchored to **2026-07-31 (4 DTE)**, not a 0DTE expiry. **Reported for
completeness; not load-bearing.**

Two observations that survive the de-rating:

1. **The single-expiry read contradicts the 45-day surface** — `POSITIVE` /
   `+1,047,168` here vs `FULLY_NEGATIVE` / `−566,158` at `--dte-max 45`. Both can
   be true and the reconciliation is informative: the 2026-07-31 expiry is
   **call-heavy** (13,502 calls vs 3,395 puts, `phase-3-positioning.md`) and
   phase-1 showed those calls being **sold** by the public (`call_ask_share = 0.475`),
   so dealers are **long calls = long gamma** in that one week. The negative
   aggregate comes from the **put-heavy August/September book**. **The earnings
   week is a small island of positive gamma inside a short-gamma sea** — and it
   expires four days from now, after which only the negative surface remains.
2. **The `role` labels are counter-intuitive and should not be taken at face
   value**: $42.50 and $50 sit **above** spot yet are tagged `support_wall`, while
   $33 sits **below** spot and is tagged `resistance_wall`. The labels appear to
   track the sign of `gex` rather than position relative to spot. Note also
   `today_zero_gamma = 42.21` with `spot = 37.74` — spot is **below** the stated
   zero-gamma line while `regime` reads `POSITIVE`, which is internally
   inconsistent under the usual convention. **Quoted verbatim, not interpreted.**

The one cross-confirmed number: **$42.50 carries by far the largest positive
gamma (+703,006)**, and phase-3 independently identified $42.50 as the **only
genuine near-term call wall** (3,735 calls, zero puts, +11.81%). Two tools agree
on that level.

### Max pain

`uw options-structure max-pain --symbol ENPH` (`spot = 38.01`).
`caveat`: *"Single-day OI snapshot. Max pain assumes settlement at each candidate
strike with current open interest unchanged to expiry."*

**Near expiries (`--dte-max 30`):**

| Expiry | DTE | **Max pain** | `distance_pct` | P/C OI | Call OI | Put OI | Total OI |
|---|---|---|---|---|---|---|---|
| **2026-07-31** | 4 | **$41** | **+7.87%** | 0.251 | 13,502 | 3,395 | 16,897 |
| 2026-08-07 | 11 | $40 | +5.24% | 0.799 | 1,135 | 907 | 2,042 |
| 2026-08-14 | 18 | $42 | +10.50% | 1.342 | 462 | 620 | 1,082 |
| 2026-08-21 | 25 | $50 | +31.54% | 1.253 | 20,025 | 25,090 | 45,115 |

For the earnings expiry, `holder_value_at_max_pain = 399,650`.

**Full curve (`--dte-max 0`, includes LEAPs):**

| Expiry | DTE | Max pain | `distance_pct` | Total OI |
|---|---|---|---|---|
| 2026-07-31 | 4 | $41 | +7.87% | 16,897 |
| 2026-08-07 | 11 | **$40** | +5.24% | 2,042 |
| 2026-08-14 | 18 | $42 | +10.50% | 1,082 |
| 2026-08-21 | 25 | $50 | +31.54% | 45,115 |
| 2026-08-28 | 32 | **$40** | +5.24% | 511 |
| 2026-09-04 | 39 | $36 | −5.29% | 39 |
| **2026-09-18** | 53 | **$40** | +5.24% | **49,625** |
| 2026-10-16 | 81 | **$40** | +5.24% | 3,193 |
| 2026-11-20 | 116 | **$40** | +5.24% | 12,101 |
| 2026-12-18 | 144 | $50 | +31.54% | 21,591 |
| **2027-01-15** | 172 | **$40** | +5.24% | **59,336** |
| 2027-02-19 | 207 | **$40** | +5.24% | 947 |
| 2027-06-17 | 325 | $25 | −34.23% | 16,841 |
| 2028-01-21 | 543 | $35 | −7.92% | 9,266 |
| 2028-12-15 | 872 | **$40** | +5.24% | 3,388 |

**$40 is the max-pain strike in 8 of 15 expiries**, including the two heaviest
(2026-09-18 at 49,625 OI and 2027-01-15 at 59,336 OI — together **45%** of all OI).
**Every near-dated max pain sits above spot.** The chain's static gravity points
**up**, toward $40–41.

**Cross-checks required by the composition guidance:**

- **vs phase-3 `oi-by-strike`:** $40 is the `put_heavy` strike (8,444 puts ≤30 DTE,
  21,170 all-expiry). ✅ **Agree** — max pain is pulled to $40 precisely because
  that put block is ITM and would expire worthless at $40.
- **vs phase-3 `term-structure` OPEX cliff:** cliffs at 2026-09-18 (20.51%) and
  2026-08-21 (18.64%). The 09-18 cliff max-pains at **$40** ✅; the 08-21 cliff
  max-pains at **$50** ⚠️ — a **+31.54%** outlier driven by its 6,055 deep-ITM $50
  puts. Per the pitfall (*"the further the expiry, the softer the magnet"*), and
  because $50 is implausible within 25 days, **the $50 reading is discarded as an
  ITM-put artifact.**
- **vs GEX:** max pain $40–41 sits directly on the **most negative gamma strike
  ($40, −1,112,908)**. Per the composition guidance this is the *unfavourable*
  combination: max pain near a **positive**-gamma pin reinforces a range, but here
  the magnet coincides with the point of **maximum instability**. There is pull
  toward $40 and **no gamma brake** once price gets there.

**Weight this appropriately.** The earnings expiry holds 6.98% of OI with roughly
2,000 contracts inside the implied move (`phase-3-positioning.md`), and ENPH is
absent from `pin-risk`. A $41 magnet backed by 16,897 contracts will **not**
withstand a 12.25% event move. Max pain is a **drift** here, not a pin — relevant
if the print is a non-event, irrelevant if it is not.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol ENPH --dte-max 45 --date 2026-07-27 --json` | `regime="FULLY_NEGATIVE"`, `zero_gamma_level=null`, `total_gex=-566158`, `underlying_price=37.52`; K40 `net_gex=-1112908.28`, K35 `-502634.49`, K30 `-303706.29` ← `.regime` / `.zero_gamma_level` / `.total_gex` / `.per_strike[]`; Σ`per_strike` **=−916,496** ← `[.per_strike[].net_gex]\|add` | 50 strikes |
| `uw options-structure dex --symbol ENPH --dte-max 45 --date 2026-07-27 --json` | `net_dex=-40323765`, `call_dex=21340821`, `put_dex=-61664586`, `spot=37.52`, `interpretation="Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."` | 1 |
| `uw options-structure vanna-charm --symbol ENPH --dte-max 45 --date 2026-07-27 --json` | `net_vanna=913`, `put_vanna=1208`, `call_vanna=-294`, `net_charm=57572`, `vanna_interpretation="…Classic vanna-squeeze setup if VIX collapses."` | 1 |
| `uw options-structure iv-term-structure --symbol ENPH --date 2026-07-27 --json` | `structure="BACKWARDATION"`, `kink_expiry=null`, `expiry_count=15`; 2026-07-31 `avg_iv=1.7009 contract_count=1385 dte_approx=4`; 2026-10-16 `avg_iv=0.8626` (trough) ← `.term_structure[]` | 15 |
| `uw options-structure term-skew --symbol ENPH --dte-target 30 --date 2026-07-27 --json` | `interpretation="COMPLACENT"`, `skew_ratio=1.001`, `skew=0.001`, `put_25d_iv=0.9558`, `call_25d_iv=0.9548`, `dte_actual=32` | 1 |
| `uw options-structure front-end-iv-ratio --symbol ENPH --near-dte 7 --far-dte 30 --date 2026-07-27 --json` | `ratio=1.727`, `regime="BACKWARDATION"`, `near_iv=1.7009` (`near_dte_actual=4`), `far_iv=0.9846` (`far_dte_actual=32`) | 1 |
| `uw options-structure today-gamma-flip --symbol ENPH --date 2026-07-27 --json` | `today_expiry="2026-07-31"`, `today_total_gex=1047168`, `regime="POSITIVE"`, `today_zero_gamma=42.21`, `atm_flip_strike=38`, `spot=37.74`; `key_walls[0]={strike:42.5, gex:703006, role:"support_wall"}` | 5 walls |
| `uw options-structure max-pain --symbol ENPH --dte-max 30 --date 2026-07-27 --json` | `spot=38.01`; 2026-07-31 `max_pain_strike=41 distance_pct=7.87 put_call_oi_ratio=0.251`; 2026-08-21 `max_pain_strike=50 distance_pct=31.54` ← `.results[]` | 4 |
| `uw options-structure max-pain --symbol ENPH --expiry 2026-07-31 --date 2026-07-27 --json` | `holder_value_at_max_pain=399650`, `max_pain_strike=41`; **`pain_curve` absent** ← `.results[0].pain_curve` → `null` | 1 |
| `uw options-structure max-pain --symbol ENPH --dte-max 0 --date 2026-07-27 --json` | `max_pain_strike=40` in **8 of 15** expiries incl. 2026-09-18 (`total_oi=49625`) and 2027-01-15 (`total_oi=59336`) ← `.results[]` | 15 |

## Tool errors

No command errored; all exited 0 and round-tripped through `jq`. **Four data
inconsistencies** are surfaced verbatim rather than smoothed over:

1. **`gex`: `total_gex` ≠ Σ`per_strike`.** Reported `total_gex = −566,158`;
   `[.per_strike[].net_gex] | add = −916,496`. **62% discrepancy within a single
   payload.** Sign and `regime` are unaffected (both strongly negative, all 50
   strikes negative), so no conclusion in this phase depends on it — but **neither
   figure is quotable as a calibrated GEX level.** Flagged for phase-10.
2. **`max-pain --expiry 2026-07-31` returns no `pain_curve`.** The phase-4 tool
   table documents *"Add `--expiry <D>` for the full per-strike `pain_curve`"*, and
   `lib/uw-json-paths.md` records `pain_curve only with --expiry`. The keys
   returned are `[call_oi, distance_pct, dte, expiry, holder_value_at_max_pain,
   max_pain_strike, put_call_oi_ratio, put_oi, total_oi]` — **no `pain_curve`**.
   Consequence: the *shape* of the pain function (how sharp the $41 magnet is)
   could not be assessed, only its argmax. *Propose-only note for the skill:*
   `lib/uw-json-paths.md §options-structure` should drop the `pain_curve` claim or
   the CLI should restore the field.
3. **`today-gamma-flip` regime is internally inconsistent** — `regime = "POSITIVE"`
   with `today_zero_gamma = 42.21` above `spot = 37.74`, and `role` labels that
   track `gex` sign rather than position vs spot ($42.50 above spot tagged
   `support_wall`; $33 below spot tagged `resistance_wall`). Quoted verbatim,
   explicitly not interpreted, and already de-rated as an after-hours call on a
   4-DTE (not 0DTE) expiry.
4. **Spot price disagrees across tools on the same date:** `gex`/`dex`/`vanna-charm`
   use **37.52**; `today-gamma-flip` uses **37.74**; `max-pain` and `oi-by-strike`
   use **38.01** (the true close, matching `stock-screener` `close = 38.01`). The
   structure tools sourcing `bot-eod-report-*.parquet` appear to use a VWAP-like or
   last-print reference rather than the official close. **All `distance_pct` figures
   in this phase are taken from the `max-pain`/`oi-by-strike` family (spot 38.01)**
   for consistency with phases 2 and 3. The ~1.3% spot spread is immaterial to a
   12.25% implied move but must not be compounded into level arithmetic.

## DATA NOTE / CORRECTION

- **All regime labels are quoted from the tools, not re-derived** (per composition
  guidance): `regime="FULLY_NEGATIVE"` + `regime_description`, `structure="BACKWARDATION"`,
  `interpretation="COMPLACENT"`, `vanna_interpretation`, `dex.interpretation`.
  `per_strike` was used only to *cross-check* the GEX label (confirming all 50
  strikes negative) and to rank strikes — never to recompute the regime.
- **`zero_gamma_level = null` is a genuine value, not a failed read.** With
  `regime = "FULLY_NEGATIVE"` there is no zero crossing. Phase-9 must not
  substitute a hand-picked ZGL; the correct statement is *"no long-gamma zone
  exists within 45 DTE."*
- **The −$40.3M DEX → 0.83%-of-float conversion is mine, not the tool's**:
  `40,323,765 ÷ 38.01 ÷ 127,770,000`. Derived context, flagged as such.
- **The 2026-08-21 max pain of $50 (+31.54%) is deliberately discarded** as a
  deep-ITM-put artifact, per the phase-4 pitfall on static-OI drift. Recorded here
  so phase-10 sees the exclusion was reasoned, not an omission.
- No value written in this phase was corrected after first read.

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA (FULLY_NEGATIVE), dealers hedging by SELLING,
  with a positive-vanna spring that reverses the sign on IV collapse.** Not
  "transitional" — there is no long-gamma zone at all within 45 DTE
  (`zero_gamma_level = null`). The regime is unambiguous; its *consequence* is
  path-dependent, and that is the honest finding: **the same book that amplifies
  a breakdown also mechanically buys a relief rally.**
- **Conviction:** **4 / 5** — the highest of any phase so far, and the only phase
  whose signals are large relative to the name. Four independent tools agree on a
  put-heavy public book (`gex` negative at every strike, `dex` −$40.3M with put
  DEX 2.9× call DEX, `vanna` positive, max pain pulled above spot by ITM puts).
  `net_dex` alone is **0.83% of float** — 8× any positioning number in phases 1–3.
  Docked one point for the four data inconsistencies above and the tool's own
  small-cap applicability warning. **Note this phase is *not* subject to the
  phase-0.5 `BUSY_NAME_NORMAL_DAY` cap**, which binds phases 1–2 only; structure
  is a stock-of-positioning read, not a flow-of-the-day read.
- **Three structural levels for phase-9, plus the pin magnet:**
  1. **ZGL: none — `zero_gamma_level = null`.** Phase-9 must treat the *entire*
     45-DTE surface as short-gamma. The only positive-gamma pocket is the
     2026-07-31 expiry (`today_total_gex = +1,047,168`), and it **expires in 4
     days**. Practical translation: **expect trend continuation and expanded
     realized vol, in whichever direction the print resolves.**
  2. **Largest GEX strike: $40.00** (`net_gex = −1,112,908`), +5.24%. Also the
     `put_heavy` strike (phase-3) *and* the modal max-pain strike (8 of 15
     expiries). **The single most important level in the chain** — and, being the
     most negative gamma, the point of maximum instability rather than support.
  3. **Vanna pivot / upside wall: $42.50.** Largest positive gamma in the earnings
     expiry (`+703,006`) and phase-3's **only** genuine near-term call wall (3,735
     calls, zero puts, +11.81%). Two tools independently agree. This is the level a
     post-earnings vanna squeeze would run into.
  4. **Max-pain magnet: $41 (+7.87%) for 2026-07-31; $40 (+5.24%) is the modal
     strike across the whole curve.** Gravity points **up**, but it is a drift, not
     a pin — 16,897 contracts cannot hold against a 12.25% move.
  (Secondary downside reference: **$35**, `net_gex = −502,635`, phase-3's
  `put_wall_support` with 4,217 puts vs 10 calls.)
- **Three things later phases must remember:**
  1. **`net_dex = −$40,323,765` ≈ 0.83% of float — dealers are a persistent
     mechanical *seller*.** This is the structural explanation for a 15.3% slide on
     unremarkable volume (`phase-0.5-context.md`) and it is the largest positioning
     number in the entire run. It does not switch off tomorrow.
  2. **The vanna squeeze is armed and its trigger is near-certain.** All three
     conditions are met, and the front week *must* de-vol from 170.1% after the
     print. **If ENPH does not break down on the number, the mechanical bid is the
     dominant flow for the following week** — and it runs into $42.50. This is the
     strongest *bullish* mechanic anywhere in phases 1–4, and it exists in a name
     where every flow read has been bearish.
  3. **`skew_ratio = 1.001` / "COMPLACENT" — downside convexity is priced flat to
     upside** on a name down 40.6% with 17.94% short float in a short-gamma regime.
     **Direct structuring consequence for phase-9: express bearish views as
     outright long puts, never put spreads** (spreads sell the cheap wing), and do
     **not** fund bullish views by selling puts.
  - *(Carried correction from phase-3: phase-2's "customer bought the 800-lot Nov
    $35 puts" is withdrawn — OI moved 407→412. Nothing in phase-4 reinstates it.)*
- **Open questions:**
  - Is a **12.25% implied move** rich or cheap against ENPH's realized earnings-day
    history and current `vrp`? The whole risk/reward of buying vs selling the event
    turns on this. → **phase-5** (`vrp`, `iv-percentile-zscore`)
  - **How large were ENPH's last four earnings-day moves?** If historical earnings
    gaps exceed 12.25%, the front week is *cheap* despite 170% IV. → **phase-5 / 7b**
  - Is flat skew **complacency** or a correctly-priced two-sided distribution given
    17.94% short float? → **phase-7c / phase-8b**
  - `total_gex` vs Σ`per_strike` differ by 62%. Does the same discrepancy appear on
    other tickers (tool bug) or is it ENPH-specific? → **phase-10** (unresolved)
