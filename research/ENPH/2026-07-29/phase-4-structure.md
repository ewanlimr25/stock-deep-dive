# Phase 4 — Dealer Structure & Gamma

**Ticker:** ENPH
**As-of date:** 2026-07-29
**Generated:** 2026-07-30T02:00:00Z
**Upstream phases cited:** `phase-0-intake.md`, `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

**Short gamma below spot, and the "$35 put wall support" is dead — the tool classifies 35
as a `resistance_wall`.** `today-gamma-flip` returns `key_walls` with **strike 35 at
`gex` −323,628, `role` `resistance_wall`**, alongside 36 (−138,082), 33 (−255,438) and 32
(−136,181) — all negative, all labelled resistance. The `gex` surface confirms it:
**every strike from 25 through 36.5 has negative `net_gex`**, with the mass at
**40 (−1,165,778), 35 (−977,948), 30 (−471,049), 33 (−321,614)** — exactly phase 3's put
walls. `atm_flip_strike` is **36**, and spot (35.07 close) sits **below** it.
**This resolves `phase-3-positioning.md` §H decisively: dealers are short gamma across the
entire 32–36 zone, so the put walls are accelerants, not support.**

**`dex` states the mechanism in its own words.** `interpretation`: *"Public is net put-long
→ dealers net short puts → **dealer hedge is to SELL underlying**."* `net_dex`
**−$65,123,664** = **1.41% of the 127.77M float** in share-equivalents, up from the 0.83%
carried from the 07-27 run — **dealer short-delta grew ~70%**. It also independently
corroborates `phase-1-flow.md`'s whole-tape finding (`put_volume_ask_side`/`bid_side`
= **1.569×**, puts bought): the public *is* net put-long, measured two entirely different
ways.

**And yet the structure is genuinely two-sided — this is the phase's most important
nuance.** Two mechanical forces point *up*:

1. **A live vanna-squeeze setup.** `net_vanna` **+1,327** (up from +913 at the 07-27 run),
   `vanna_interpretation`: *"Public net vanna positive (put-heavy book). Falling IV → |put
   delta| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze
   setup if VIX collapses."* **The IV-falling precondition is already met** — `iv30d`
   0.905 → 0.797 in one session, `iv_rank` 47.05 at ENPH's **15.6th self percentile**
   (`phase-0.5-context.md`). `net_charm` **+24,381** points the same way.
2. **Max pain is above spot at every expiry inside 30 days** — 08-07 → **36** (+2.68%),
   07-31 → **37** (+5.53%), 08-14 → 38, 08-28 → 42, and 08-21 → **45** (+28.35%) carrying
   the largest `holder_value_at_max_pain` ($5,110,800). The chain's gravity pulls **up**,
   not down.

**Gamma/delta amplify spot moves; vanna and charm act on IV and time.** Post-earnings IV
crush is precisely the regime where vanna dominates, so this is a real conflict, not a
rounding error: **if ENPH drifts, the vanna bid and the 36–37 pin win; if it breaks 35,
negative gamma and $65M of dealer selling take over.** 35 is the switch.

**One more asymmetry worth the whole phase: downside is free.** `term-skew` at 30 DTE
returns `put_25d_iv` **0.8445** *below* `call_25d_iv` **0.8498** — `skew` **−0.0053**,
`skew_ratio` **0.994**, `interpretation` **COMPLACENT**. After an 11% two-week decline and
a gap-and-crap, the market charges **no premium** for downside protection. That is the
cleanest structural argument in this run for expressing any bearish view as **long puts**
rather than short stock.

`iv-term-structure` reports **BACKWARDATION**, but the spec's own pitfall voids it:
earnings passed ~28 hours ago, and the label is driven entirely by the 2-DTE expiry at
**140.0%** IV. Beyond 9 days the curve is **flat at 82–87%** (`kink_expiry` null). **Do
not trade this backwardation.**

## Key signals

- **Strike 35 = `resistance_wall`, `gex` −323,628**; 36, 33, 32 likewise negative. Only
  42.5 is a `support_wall` (+427,794) and it expires Friday, 21% away
  [STRUCT:today_gamma_flip]
- **All strikes 25 → 36.5 have negative `net_gex`**; mass at 40 (−1,165,778), 35
  (−977,948), 30 (−471,049), 33 (−321,614). `atm_flip_strike` **36**, spot below it
  [STRUCT:gex]
- **`net_dex` −$65,123,664 = 1.41% of float** (from 0.83% at the 07-27 run);
  `interpretation` = *"dealer hedge is to SELL underlying"* [STRUCT:dex]
- **`today_total_gex` −406,622 — a SIGN FLIP** from the +1,047,168 carried in
  `phase-0-intake.md`; `regime` **NEGATIVE**, `today_zero_gamma` null
  [STRUCT:today_gamma_flip]
- **`net_vanna` +1,327 with IV already collapsing** → *"dealers (short puts) cover by
  BUYING underlying. Classic vanna-squeeze setup"*; `net_charm` +24,381
  [STRUCT:vanna_charm]
- **Max pain above spot at all five expiries ≤30 DTE**: 36 / 37 / 38 / 42 / **45**
  (08-21, `holder_value_at_max_pain` $5,110,800) [STRUCT:max_pain]
- **`skew_ratio` 0.994 — 25Δ puts CHEAPER than 25Δ calls** (0.8445 vs 0.8498),
  `interpretation` COMPLACENT [STRUCT:term_skew]
- **`structure` BACKWARDATION but voided by the 24h-post-earnings pitfall** — 07-31 at
  140.0% vs a flat 82–87% beyond 9 days; `front-end-iv-ratio` 1.14 [STRUCT:iv_term_structure]
- **The 10-16 expiry is the curve's cheapest vol at 82.2%** — exactly where today's
  largest print bought puts (Oct-16 P35, `phase-1-flow.md` §D) [STRUCT:iv_term_structure]
- **`regime` label "FULLY_NEGATIVE / All strikes have negative net GEX" is factually
  wrong** — 25 of 50 strikes are positive. See `## Tool errors` [STRUCT:gex]

## Detailed findings

### A — GEX

`uw options-structure gex --symbol ENPH --dte-max 45`:

| Field | Value |
|---|---|
| `regime` | **FULLY_NEGATIVE** ⚠ (label contradicted by its own data — see below) |
| `regime_description` | "All strikes have negative net GEX — strong gamma amplification" ⚠ |
| `total_gex` | **−2,796,417** |
| `zero_gamma_level` | **null** |
| `underlying_price` | **36.08** ⚠ (≠ verified close 35.07 — see §I) |
| `per_strike` | 50 strikes, 25 → 52 |
| `note` | "GEX most meaningful for index products (SPY, QQQ) and large-cap single stocks with deep OI." |

**The `regime` label is wrong and I am not quoting it as fact.** The spec says to quote the
tool's regime label rather than re-derive it, and to use `per_strike` only to cross-check.
I ran that cross-check and it **fails**: `[.per_strike[] | select(.net_gex > 0)] | length`
= **25 of 50**. `regime_description` claims "All strikes have negative net GEX"; strike
42.5 is **+451,024** and strike 37 is **+108,762**. The label is a mis-derivation.
Reported precisely below and flagged in `## Tool errors`.

**What the surface actually shows — and it matters more than the label:**

| Strike ladder | Sign |
|---|---|
| **25 → 36.5 (every strike)** | **NEGATIVE, without exception** |
| 37 → 52 | mixed, mostly positive — but 40 (**−1,165,778**) and 45 (−84,680) are the exceptions |

Full ladder through the tradeable zone:

| K | `net_gex` | K | `net_gex` |
|---|---|---|---|
| 28 | −11,429 | 36 | −142,844 |
| 29 | −8,159 | 36.5 | −1,033 |
| **30** | **−471,049** | **37** | **+108,762** |
| 31 | −87,486 | 37.5 | −14,919 |
| **32** | **−166,111** | 38 | +73,768 |
| 32.5 | −81,165 | 39 | +25,446 |
| **33** | **−321,614** | **40** | **−1,165,778** |
| 33.5 | −38,607 | 40.5 | +76,404 |
| **34** | **−155,623** | 41 | +17,702 |
| 34.5 | −17,335 | 42 | +28,385 |
| **35** | **−977,948** | **42.5** | **+451,024** |
| 35.5 | −60,576 | 43 | +62,454 |
| | | 44 | +85,955 |
| | | 45 | −84,680 |

Top 10 by absolute magnitude: **40 (−1,165,778) · 35 (−977,948) · 30 (−471,049) ·
42.5 (+451,024) · 33 (−321,614) · 50 (−220,507) · 32 (−166,111) · 34 (−155,623) ·
36 (−142,844) · 37 (+108,762)**.

**Three conclusions:**

1. **The real gamma flip sits between 36.5 (−1,033) and 37 (+108,762)** — the only clean
   sign change in the tradeable zone. `zero_gamma_level` returned `null`, but
   `today-gamma-flip` independently reports `atm_flip_strike` **36** (§G). Per the spec's
   pitfall (ZGL is coarse on low-liquidity names, treat as ±2%), the honest statement is a
   **flip band of roughly 36–37**. **Spot 35.07 is below it → short-gamma regime.**
2. **The negative gamma is concentrated precisely on phase 3's put walls.** Compare
   `oi-by-strike` all-expiry `put_oi`: 40 → 21,073 puts / `net_gex` −1,165,778; 35 →
   25,340 puts / −977,948; 30 → 22,446 puts / −471,049. **The correspondence is exact.**
   This is the mechanical answer to `phase-3-positioning.md` §H: those strikes carry
   *negative* gamma, so dealers there are short gamma and must **sell into declines**.
   **A negative-gamma put wall is an accelerant.**
3. **The one meaningful positive-gamma pocket is 42.5 (+451,024) and it is about to
   vanish.** Phase 3 identified 3,941 contracts of 07-31 C42.5 open interest — junk calls
   21% OTM with 2 days left. That is where this GEX comes from. It expires Friday, it is
   21% above spot, and it is irrelevant to price action at 35.

**Sign/aggregation check:** `[.per_strike[].net_gex] | add` = **−2,994,173** versus the
reported `total_gex` **−2,796,417** — a **$197,756 discrepancy (7.1%)**. Both are negative
and the conclusion is unaffected, but the two figures do not reconcile; the sum is used
only for the sign-split check, and `total_gex` is quoted as the headline. Noted in
`## Tool errors`.

### B — DEX

`uw options-structure dex --symbol ENPH --dte-max 45`:

| Field | Value |
|---|---|
| `call_dex` | +15,532,456 |
| `put_dex` | **−80,656,120** |
| **`net_dex`** | **−65,123,664** |
| `spot` | 36.08 ⚠ |
| **`interpretation`** | **"Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."** |
| `note` | "DEX = Σ(delta × OI × 100 × spot). Sign reflects public positioning; dealer hedge is the inverse." |
| `per_strike` | **absent** — the key is not returned by this leaf |

**Share-equivalent normalization:** −$65,123,664 ÷ 36.08 = **−1,804,979 share-equivalents**
= **1.41% of the 127.77M float**. Against the 07-27 run's carried `net_dex` of −$40.3M
(0.83% of float), **dealer short-delta has grown ~70% in share terms across the event.**

**This is the phase's cleanest cross-lane confirmation.** `dex` infers "public is net
put-long" from OI-weighted deltas. `phase-1-flow.md` reached the same conclusion from a
completely independent measurement — whole-tape side-classified volume, `put_volume_ask_side`
7,236 vs `put_volume_bid_side` 4,613 = **1.569×**, ~90% of the tape classified. Two
methods, two data sources, same answer: **the public is long puts and dealers are short
them.**

> **⚠ This inverts the structural thesis carried from the 07-27 run.** That run's
> `decision.json` reads: *"a structurally armed upside squeeze: net_dex −$40.3M = 0.83% of
> float with net_vanna +913."* The sign of `net_dex` was read there as dealers being short
> *delta* and therefore forced to **buy**. The tool's own `interpretation` field says the
> opposite: dealers short **puts** are **long** delta, so their hedge is to **SELL**. The
> mechanics support the tool — a short put has positive delta, and as spot falls that
> delta rises toward +1, forcing progressively more selling. **The squeeze framing was
> attached to the wrong Greek.** The genuine squeeze mechanism in this book is **vanna**
> (§C), which acts on IV rather than spot — and that one is real. Recorded in
> `## DATA NOTE` and flagged for phase 10.

### C — Vanna and charm

`uw options-structure vanna-charm --symbol ENPH --dte-max 45`:

| Field | Value |
|---|---|
| `call_vanna` | −263 |
| `put_vanna` | +1,590 |
| **`net_vanna`** | **+1,327** (07-27 run: +913 → **+45%**) |
| **`net_charm`** | **+24,381** |
| `spot` | 36.08 ⚠ |
| **`vanna_interpretation`** | **"Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."** |
| `note` | "Closed-form approximations: vanna ≈ −vega×delta/(σ×S); charm ≈ −theta×delta/option_price. Coarse for deep ITM/OTM and near-expiry — filtered to dte ≥ 1 by default." |

**The vanna-squeeze precondition is not hypothetical — it has already fired.** The tool
conditions the setup on falling IV. Measured:

| IV measure | Value | Source |
|---|---|---|
| `iv30d` 07-28 → 07-29 | **0.905 → 0.797** (−10.8pp in one session) | `phase-0.5-context.md` |
| `iv30d` 8-session trend | 1.017 → 0.797 (−22pp, 8 consecutive falls) | `phase-0.5-context.md` |
| `iv_rank` | 69.81 → **47.05** = **15.6th self percentile** | `phase-0.5-context.md` |
| `implied_move_perc` | 12.25% → **5.58%** | `phase-0.5-context.md` |

Falling IV shrinks `|put delta|`; dealers short those puts see their long delta shrink and
**buy back stock**. `net_charm` **+24,381** reinforces it — as time passes, OTM put deltas
decay toward zero and the same dealers cover further.

**This is the strongest bullish mechanical argument in the entire run, and it is
structurally sound.** It must not be dismissed because four other lanes read bearish. Its
limits, stated honestly:

- **Vanna and gamma act on different variables.** Vanna/charm respond to **IV and time**;
  gamma/delta respond to **spot**. They are not contradictory — they are simultaneous, and
  which dominates depends on what moves. A quiet drift with continued IV decay favours
  vanna (dealer buying). A decisive break of 35 favours gamma (dealer selling).
- **The IV crush is largely spent.** Having fallen from 1.017 to 0.797 with `iv_rank` at
  the 15.6th self percentile, there is far less remaining decay to fuel further covering
  than there was pre-event. The vanna engine has already burned most of its fuel.
- **The tool's own note** flags these as coarse closed-form approximations.
- The trigger condition names a **VIX collapse**; phase 6 must establish whether the macro
  tape supports that (today was broadly risk-off — only 2 of 11 sectors green on average
  change, `phase-0.5-context.md`).

### D — IV term structure

`uw options-structure iv-term-structure --symbol ENPH` → `structure` **BACKWARDATION**,
`expiry_count` 15, `kink_expiry` **null**.

| Expiry | `dte_approx` | `avg_iv` | `avg_iv_pct` | contracts |
|---|---|---|---|---|
| **2026-07-31** | **2** | **1.3996** | **140.0%** | 2,537 |
| 2026-08-07 | 9 | 0.9766 | 97.7% | 615 |
| 2026-08-14 | 16 | 0.9039 | 90.4% | 260 |
| **2026-08-21** | 23 | 0.8625 | 86.2% | 885 |
| 2026-08-28 | 30 | 0.8569 | 85.7% | 190 |
| 2026-09-04 | 37 | 0.8502 | 85.0% | 190 |
| 2026-09-18 | 51 | 0.8368 | 83.7% | 893 |
| **2026-10-16** | 79 | **0.8219** | **82.2%** ← curve trough | 89 |
| 2026-11-20 | 114 | 0.8677 | 86.8% | 68 |
| 2026-12-18 | 142 | 0.8498 | 85.0% | 68 |
| 2027-01-15 | 170 | 0.8466 | 84.7% | 191 |
| 2027-02-19 | 205 | 0.8694 | 86.9% | 23 |
| 2027-06-17 | 323 | 0.8561 | 85.6% | 61 |
| 2028-01-21 | 541 | 0.8440 | 84.4% | 40 |
| 2028-12-15 | 870 | 0.8320 | 83.2% | 42 |

**The BACKWARDATION label is real arithmetic but must not be traded, on the spec's own
instruction:** *"A flipped term structure can normalize the day after earnings — don't
trade backwardation if earnings already passed within 24h."* ENPH reported **postmarket
2026-07-28**, roughly **28 hours** before this as-of close. The label is produced **entirely
by the 2-DTE expiry at 140.0%**, which `phase-1-flow.md` §G already established as
mechanical: all 15 `iv-outliers` rows sat in the 07-31 expiry at 128–233% IV, with premium
of $224–$4,893 in 12 of 15 rows. **This is expiry-week IV inflation, not event stress.**

**Beyond the front week the curve is flat — that is the real finding.** From `dte` 9 to
`dte` 870 the range is **82.2% to 97.7%**, and from `dte` 23 outward it is a **flat band of
82–87%** with `kink_expiry` **null**. There is no structural vol stress anywhere past next
week. For a name whose next catalyst is **2026-10-27** (`phase-0.5-context.md`), a flat
83–86% curve is the market pricing *nothing in particular*.

**One actionable observation:** the **10-16 expiry is the cheapest point on the entire
curve at 82.2%** — and that is exactly where today's largest single print bought puts
(Oct-16 P35, ask side, $196,240 + $31,500, plus a $260,820 ask sweep;
`phase-1-flow.md` §D–E). Whoever placed the day's biggest bet **bought the cheapest
volatility on the surface**. Combined with `skew_ratio` 0.994 (§F), that is a well-executed
trade, not a panic hedge — evidence for the "directional bet" reading of the long-dated put
buying in `phase-3-positioning.md` §C.

### E — Front-end IV ratio

`uw options-structure front-end-iv-ratio --symbol ENPH --near-dte 7 --far-dte 30`:

| Field | Value |
|---|---|
| `near_dte_actual` | **9** (2026-08-07) |
| `near_iv` | 0.9766 |
| `far_dte_actual` | **30** (2026-08-28) |
| `far_iv` | 0.8569 |
| **`ratio`** | **1.14** |
| `regime` | **BACKWARDATION** |

**Usefully, this read excludes the 140% front-expiry spike** — `near_dte_actual` resolved
to 9, not 2. So even with the expiry-week artifact removed, there is **mild** front-end
elevation: **1.14×**. That is modest residual event decay 28 hours after a print, not
fresh stress. It is directionally consistent with §D and adds one fact: the crush is
**not quite complete** — roughly 14% of front-end premium remains to bleed out of the
08-07 expiry over the next nine sessions.

That residual matters for §C: it is the remaining fuel for the vanna bid, and it is small.

### F — Term skew

`uw options-structure term-skew --symbol ENPH --dte-target 30`:

| Field | Value |
|---|---|
| `dte_target` / `dte_actual` | 30 / **30** |
| `call_25d_iv` | **0.8498** |
| `put_25d_iv` | **0.8445** |
| `skew` | **−0.0053** |
| **`skew_ratio`** | **0.994** |
| `interpretation` | **COMPLACENT** |

**25-delta puts are trading at a lower implied vol than 25-delta calls.** For an equity
this is unusual — the normal state is a put premium (skew_ratio > 1) reflecting persistent
downside-hedging demand. ENPH has **negative** skew after an 11% two-week decline, a
gap-and-crap session, and a binary event.

| Run | `skew_ratio` | `interpretation` |
|---|---|---|
| 2026-07-27 | 1.001 | COMPLACENT |
| **2026-07-29** | **0.994** | COMPLACENT |

Skew got *flatter* (marginally more call-rich) through the event.

**Three readings, and they layer rather than compete:**

1. **Downside protection is cheap in relative terms.** Anyone wanting short exposure is
   charged **no** skew premium. This is the cleanest structural argument in the run for
   expressing a bearish view as **long puts** rather than short stock — and it explains
   the Oct-16 P35 buyer, who bought the curve's cheapest vol (§D) at zero skew cost.
2. **No tail-hedging panic.** The spec's "skew steepening → tail-hedging demand, often
   precedes broader risk-off" heuristic is **not** firing. Despite the decline, nobody is
   paying up for crash protection. Read with `phase-0.5-context.md`'s finding that ENPH is
   already **−52.4% from its 52-week high**, the plausible interpretation is that ENPH is
   a *de-rated* name rather than a *panicking* one.
3. **It is a modest contrarian caution against the bearish consensus.** COMPLACENT is the
   label the tool assigns, and complacency cuts both ways: it means the market is not
   braced for downside, so a break of 35 would be into thin protection — which is also
   exactly what negative gamma at 32–36 (§A) implies.

Note the tension with `net_vanna` +1,327 (§C): a put-heavy book by *vanna* alongside puts
that are *cheap* by skew. Both are consistent if the put length is concentrated in
**quantity at low IV** rather than in panic bidding — which is what §A–C and phase 3's
$2.84M ask-side Jan-2028 P30 purchase at $8.97 describe.

### G — Today's gamma flip

`uw options-structure today-gamma-flip --symbol ENPH`. The spec notes this leaf is
0DTE-only and intraday, to be skipped after hours. **It returned meaningful data here**
because ENPH has no 07-29 expiry — the leaf resolved `today_expiry` to the nearest
available, **2026-07-31** — so this is effectively a front-expiry gamma read rather than a
true 0DTE snapshot. Reported with that caveat.

| Field | Value |
|---|---|
| `today_expiry` | **2026-07-31** (nearest, not same-day) |
| `spot` | **36** ⚠ |
| `regime` | **NEGATIVE** |
| **`today_total_gex`** | **−406,622** |
| `today_zero_gamma` | **null** |
| **`atm_flip_strike`** | **36** |

`key_walls`:

| Strike | `gex` | `role` |
|---|---|---|
| 42.5 | **+427,794** | `support_wall` |
| **35** | **−323,628** | **`resistance_wall`** |
| 33 | −255,438 | `resistance_wall` |
| 36 | −138,082 | `resistance_wall` |
| 32 | −136,181 | `resistance_wall` |

**Two findings, one of them decisive.**

**(1) The sign flipped versus the carried baseline.** `phase-0-intake.md` carried from the
07-27 run: *"positive-gamma island (`today_total_gex` +1,047,168) expires."* Measured today:
**`today_total_gex` −406,622**, `regime` **NEGATIVE**. **The island did not merely shrink —
it inverted.** `phase-3-positioning.md`'s DATA NOTE required this be re-measured rather than
inherited, and the re-measurement reverses the carried framing. Phase 3 also explained
*why* the residual positive gamma is worthless: the **+427,794 at 42.5** is the 3,941
contracts of 07-31 C42.5 open interest — **21% OTM with 2 days to run**.

**(2) The tool independently labels 35 a `resistance_wall`.** This is the answer to
`phase-3-positioning.md` §H, arrived at by a different leaf than §A.

> **Read the `role` labels carefully — they are GEX-sign labels, not distance-aware
> labels.** 42.5 sits *above* spot yet is called `support_wall`; 32/33/35/36 sit *at or
> below* spot yet are called `resistance_wall`. The mapping is plainly
> positive-GEX → "support", negative-GEX → "resistance", with no reference to where spot
> is. Taken literally the words are confusing. **The economically correct reading is the
> one that matters: the entire 32–36 zone — the zone spot is sitting in — carries negative
> gamma, so there is no dealer dampening anywhere near the money.** Dealers there must
> sell into weakness and buy into strength. The *label* is imprecise; the *sign* is the
> signal, and it agrees exactly with §A.

`atm_flip_strike` **36** supplies the flip level that `gex`'s `zero_gamma_level` returned as
`null`, and it brackets §A's observed 36.5 → 37 sign change. **Flip band: 36–37. Spot
35.07 is below it.**

### H — Max pain

`uw options-structure max-pain --symbol ENPH --dte-max 30`, `spot` **35.06**.
`caveat` (verbatim): *"Single-day OI snapshot. Max pain assumes settlement at each candidate
strike with current open interest unchanged to expiry."*

| Expiry | `dte` | **`max_pain_strike`** | `distance_pct` | `put_call_oi_ratio` | `total_oi` | `holder_value_at_max_pain` |
|---|---|---|---|---|---|---|
| 2026-07-31 | 2 | **37** | **+5.53%** | 0.373 | 26,693 | $643,800 |
| **2026-08-07** | **9** | **36** | **+2.68%** | 0.618 | 3,354 | $220,100 |
| 2026-08-14 | 16 | 38 | +8.39% | 0.636 | 1,402 | $51,350 |
| **2026-08-21** | **23** | **45** | **+28.35%** | 0.891 | **46,288** | **$5,110,800** |
| 2026-08-28 | 30 | 42 | +19.79% | 0.687 | 1,414 | $72,100 |

**Max pain is above spot at every single expiry inside 30 days.** Per the spec's
composition guidance — *"max pain far below spot with a high `put_call_oi_ratio` is a
downward pull"* — the inverse holds: this is an **upward pull**. It is the second genuine
bullish mechanical force in this phase.

**Which figure is tradeable, and which is not:**

- **08-07 max pain 36 (+2.68%, `dte` 9)** is the most usable near-term magnet. Modest,
  plausible, and it **coincides with `atm_flip_strike` 36** (§G) and the 36.5→37 GEX sign
  change (§A). **Three independent leaves converge on 36 as the pivot.** That convergence
  is the single most useful level this phase produces.
- **07-31 max pain 37 (+5.53%, `dte` 2)** carries only $643,800 of holder value and rests
  on the junk-call OI (19,447 calls at 42.5/45/50, `put_call_oi_ratio` 0.373). A +5.5%
  two-day pull is not a realistic magnet; treat as noise.
- **08-21 max pain 45 (+28.35%)** has by far the largest `holder_value_at_max_pain`
  ($5.11M) and the largest `total_oi` (46,288) — but **+28% in 23 days is not a
  forecast**. It is an artifact of the Aug-21 chain's barbell: puts massed at 40 / 35 / 30
  (7,839 / 4,031 / 2,963) against calls at 50 / 60 / 65 / 75 / 90
  (`phase-3-positioning.md` §A), so the total-pain minimum lands in the empty middle. The
  `caveat` bites hardest here: static OI, 23 days out, and phase 3 established that
  **today's flow is not yet in OI**. Directionally informative (the chain would rather be
  higher), quantitatively meaningless.

**Cross-check against phase 3, as the spec requires.** Phase 3's `term-structure` OPEX
cliff is **2026-08-21** (`pct_of_total_oi` 15.69%, the tradeable cliff) and its `oi-by-strike`
walls are 35 / 40 / 30. Max pain's largest holder value is also **08-21** ✔ — the expiries
agree. But max pain's **45** does *not* sit on any phase-3 wall; it sits between them.
**The two reads agree on *which expiry* matters and disagree on *which strike*** — because
max pain minimizes aggregate holder value while `oi-by-strike` ranks raw OI. Phase 9 should
use **phase-3's walls for levels** and **max pain only for directional pull**.

**Read with the GEX surface** (per the spec): max pain here is **not** near a
positive-gamma pin — the pin candidates at 36–37 sit in a **negative**-gamma field (§A: 36
is −142,844; 36.5 is −1,033; 37 is the first positive strike at +108,762). So the
36–37 magnet has **no gamma reinforcement beneath it**. It is a pull without a floor:
mechanically attractive, mechanically unprotected.

### I — Surface reference-price discrepancy (affects every distance in this phase)

The structure leaves do not agree with each other, or with the verified close, on spot:

| Leaf | Reference price |
|---|---|
| `gex` | `underlying_price` **36.08** |
| `dex` | `spot` **36.08** |
| `vanna-charm` | `spot` **36.08** |
| `today-gamma-flip` | `spot` **36** |
| `max-pain` | `spot` **35.06** |
| **Verified close** | **35.07** (`phase-0.5-context.md` DuckDB; `fz` 35.07) |

The 36.08 reference is **+2.88% above** the verified close. It is plausibly a session VWAP
(the day's range was 34.96–39.60 on 8.67M shares, `phase-1-flow.md` §C, so a ~36 VWAP is
consistent) or a mid-session snapshot from the EOD report build. `max-pain` alone uses a
near-close 35.06.

**Handling:** every distance-from-spot statement in this file is computed against the
**verified close 35.07**, and each tool's internal reference is disclosed where quoted.
This matters materially in one place: measured from 36.08, spot would sit **above** the
36–37 flip band and the regime read would invert to long-gamma. **Measured from the true
close of 35.07, spot is below the band and the regime is short-gamma.** Because 35.07 is
independently confirmed by two sources (DuckDB screener parquet and `fz`), the short-gamma
read stands — but downstream phases must know the surface was built at 36.08 and that
GEX/DEX/vanna magnitudes are therefore struck ~2.9% above where price actually closed.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol ENPH --dte-max 45 --date 2026-07-29 --json` | `regime`="FULLY_NEGATIVE", `total_gex`=**−2796417**, `zero_gamma_level`=**null**, `underlying_price`=36.08; K40=−1165778, K35=−977948, K30=−471049, K42.5=**+451024** ← `.per_strike[]`; **positive-strike count=25 of 50** ← `[.per_strike[]\|select(.net_gex>0)]\|length`; Σ`net_gex`=−2994173 | 50 strikes |
| `uw options-structure dex --symbol ENPH --dte-max 45 --date 2026-07-29 --json` | `net_dex`=**−65123664**, `call_dex`=+15532456, `put_dex`=−80656120, `spot`=36.08, `interpretation`="Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying." ← top level; **no `per_strike` key** | 1 |
| `uw options-structure vanna-charm --symbol ENPH --dte-max 45 --date 2026-07-29 --json` | `net_vanna`=**+1327**, `put_vanna`=+1590, `call_vanna`=−263, `net_charm`=**+24381**, `vanna_interpretation`="…Classic vanna-squeeze setup if VIX collapses." | 1 |
| `uw options-structure iv-term-structure --symbol ENPH --date 2026-07-29 --json` | `structure`=**BACKWARDATION**, `kink_expiry`=**null**, `expiry_count`=15; 07-31 `avg_iv`=**1.3996**, 08-07=0.9766, 08-21=0.8625, 10-16=**0.8219** (trough), 12-15-28=0.8320 ← **`.term_structure[]`** (`avg_iv`/`dte_approx`, **not** `iv`/`dte`) | 15 expiries |
| `uw options-structure term-skew --symbol ENPH --dte-target 30 --date 2026-07-29 --json` | `put_25d_iv`=**0.8445**, `call_25d_iv`=**0.8498**, `skew`=−0.0053, `skew_ratio`=**0.994**, `interpretation`=**COMPLACENT**, `dte_actual`=30 | 1 |
| `uw options-structure front-end-iv-ratio --symbol ENPH --near-dte 7 --far-dte 30 --date 2026-07-29 --json` | `ratio`=**1.14**, `near_iv`=0.9766 @ `near_dte_actual`=**9**, `far_iv`=0.8569 @ `far_dte_actual`=30, `regime`=BACKWARDATION | 1 |
| `uw options-structure today-gamma-flip --symbol ENPH --date 2026-07-29 --json` | `today_total_gex`=**−406622**, `regime`=**NEGATIVE**, `atm_flip_strike`=**36**, `today_zero_gamma`=null, `today_expiry`=**2026-07-31**, `spot`=36; `key_walls` K35 `gex`=−323628 `role`=**resistance_wall**, K42.5 +427794 `support_wall` ← `.key_walls[]` | 5 walls |
| `uw options-structure max-pain --symbol ENPH --dte-max 30 --date 2026-07-29 --json` | 08-07 `max_pain_strike`=**36** / `distance_pct`=**+2.68**; 07-31=37/+5.53; **08-21=45/+28.35** / `holder_value_at_max_pain`=**5110800** / `total_oi`=46288; `spot`=**35.06** ← `.results[]` | 5 expiries |
| `phase-0.5-context.md` / `fz` (upstream) | verified `close`=**35.07**; `iv30d` 0.905→0.797; `iv_rank` 47.05 (self 15.6 pctile); `Float`=127.77M → `net_dex` 1.41% of float | — |

All eight `uw` reads were captured to a file before being queried and every value
round-tripped through `jq` on validated JSON. Regime labels are quoted **verbatim** per the
spec; the single exception is `gex`'s `regime`, where the mandated `per_strike` cross-check
**failed** and both the label and the contradicting data are reported (§A,
`## Tool errors`). Derived values, each stated inline: `net_dex` share-equivalents and
%-of-float (§B), the `per_strike` sign split and sum (§A), and distances recomputed against
the verified 35.07 close (§I).

## Tool errors

No invocation failures — all eight `uw options-structure` calls returned exit 0 with
parseable JSON. **Four data-integrity findings**, all silent (exit 0), so none would trip a
graceful-skip guard:

1. **`gex` `regime` / `regime_description` contradict the leaf's own `per_strike` array.**
   Reported: `regime`="FULLY_NEGATIVE", `regime_description`="All strikes have negative net
   GEX — strong gamma amplification". Measured: `[.per_strike[]|select(.net_gex>0)]|length`
   = **25 of 50** positive, including K42.5 **+451,024** and K37 **+108,762**. The claim
   "all strikes" is false. The spec instructs quoting the label and cross-checking with
   `per_strike`; the cross-check failed, so §A reports the label *and* the actual
   distribution (uniformly negative 25→36.5, mixed above). **The near-spot conclusion is
   unaffected** — but a phase that quoted the label alone would have made a false
   statement. Candidate `lib/uw-json-paths.md` / phase-spec note (**propose-only**).
2. **`gex` `total_gex` does not reconcile with `Σ per_strike.net_gex`:** −2,796,417 vs
   **−2,994,173**, a **$197,756 (7.1%)** gap. Same sign, conclusion unaffected;
   `total_gex` is quoted as the headline and the sum used only for the sign check.
3. **`gex` returns `zero_gamma_level`=`null` despite a clean sign change existing** between
   K36.5 (−1,033) and K37 (+108,762). The ZGL is recoverable from `atm_flip_strike`=36 in
   `today-gamma-flip`; §A/§G report a **36–37 flip band** rather than a point estimate,
   per the spec's ±2% coarseness pitfall.
4. **Reference-price inconsistency across leaves** — `gex`/`dex`/`vanna-charm` use 36.08,
   `today-gamma-flip` uses 36, `max-pain` uses 35.06, verified close is **35.07**
   (§I). A **+2.88%** discrepancy that, if left unhandled, would **invert the regime read**
   (spot above vs below the 36–37 flip band). All distances in this file use 35.07.

Two field-path notes (caught before transcription, no values affected):
- **`iv-term-structure` rows use `avg_iv` and `dte_approx`**, not `iv`/`dte` — a first read
  of `.iv`/`.dte` returned `null` for all 15 rows and was **not** transcribed.
- **`dex` returns no `per_strike` key** (unlike `gex`), so per-strike delta attribution is
  unavailable from this leaf.

## DATA NOTE / CORRECTION

No value in this phase was revised after its first validated read. Two **upstream/carried
framings are corrected from validated data here**, and both invert prior conclusions:

**(1) The carried "positive-gamma island" is gone — it inverted.**
`phase-0-intake.md` carried from the 07-27 run: *"2026-07-31 — front-week expiry;
positive-gamma island (`today_total_gex` +1,047,168) expires."*
- **Corrected:** `today_total_gex` = **−406,622**, `regime` = **NEGATIVE**. A sign flip, not
  a decay. Verified against
  `uw options-structure today-gamma-flip --symbol ENPH --date 2026-07-29 --json` →
  `.today_total_gex` / `.regime`, and corroborated by `gex` → `total_gex` −2,796,417 with
  strikes 25→36.5 uniformly negative.
- **Consequence:** Friday's expiry does not retire meaningful positive gamma near the money
  (the only positive pocket, K42.5 **+427,794**, is the 3,941 junk 07-31 C42.5 contracts,
  21% OTM). `phase-3-positioning.md`'s DATA NOTE required this re-measurement; it reverses
  the carried framing.

**(2) The carried "structurally armed upside squeeze" attached the squeeze to the wrong
Greek.** The 07-27 `decision.json` reads: *"a structurally armed upside squeeze: net_dex
−$40.3M = 0.83% of float with net_vanna +913."*
- **Corrected:** `dex`'s own `interpretation` field states *"Public is net put-long →
  dealers net short puts → **dealer hedge is to SELL underlying**."* A short put carries
  **positive** delta; as spot falls that delta rises toward +1, forcing **more** selling.
  A negative `net_dex` of this composition is therefore **downside pressure, not a
  squeeze**. Verified against `.interpretation` and `.note` ("Sign reflects public
  positioning; dealer hedge is the inverse") on
  `uw options-structure dex --symbol ENPH --dte-max 45 --date 2026-07-29 --json`.
- **The squeeze itself is real but it lives in vanna, not delta.** `net_vanna` **+1,327**
  with `vanna_interpretation` naming the *"classic vanna-squeeze setup"*, and the
  falling-IV precondition already satisfied (§C). Vanna acts on **IV**; delta/gamma act on
  **spot**. The mechanism is sound — the prior run's label was on the wrong variable.
- **Consequence:** `net_dex` has grown from 0.83% to **1.41% of float** and now reads as
  ~70% *more* dealer selling pressure, where the carried framing read it as a *stronger*
  squeeze. Phase 8b must debate the vanna-vs-gamma conflict on its merits; phase 10 must
  flag this as a contradiction against the prior run.

## Verdict for downstream phases

- **Dealer regime: SHORT GAMMA below spot — with a genuine, live counterforce.**
  Not "transitional": the sign is unambiguous (25→36.5 uniformly negative `net_gex`;
  `today_total_gex` −406,622; `regime` NEGATIVE; spot 35.07 below the **36–37** flip band).
  But `net_vanna` **+1,327** into an already-collapsing IV, plus max pain **above spot at
  all five expiries ≤30 DTE**, are real mechanical bids. **Gamma/delta act on spot; vanna
  and charm act on IV and time. On a drift, vanna and the 36–37 pin win. On a break of 35,
  negative gamma and $65M of dealer selling win. 35 is the switch.**
- **Conviction: 4 / 5.** The short-gamma read is measured three independent ways
  (`gex` per-strike, `today-gamma-flip` `key_walls` + `atm_flip_strike`, `dex`
  `interpretation`) and it **answers phase 3's central open question**: the put walls at
  35/40/30 carry *negative* gamma, so they are accelerants, not support. It also
  independently reproduces `phase-1-flow.md`'s public-long-puts finding from OI-weighted
  deltas rather than tape classification. Held at 4, not 5, because (a) the surface is
  struck at **36.08 vs the true 35.07 close** — a +2.88% error that would *invert* the
  regime if used naively (§I); (b) `gex`'s own `regime` label is **factually wrong** and
  `zero_gamma_level` is `null`, so the flip level is a band recovered from a second leaf;
  (c) `total_gex` and `Σ per_strike` disagree by 7.1%; and (d) the **vanna counterforce is
  structurally valid, not a rounding error** — this phase is genuinely two-sided and any
  single-direction reading of it is overconfident. Phases 1–2 remain capped at `+` per
  `phase-0.5-context.md`; **this cap does not apply to phase 4**, but the conflict does.
- **Four structural levels for phase-9:**
  1. **ZGL / gamma flip = 36–37 band** (`atm_flip_strike` **36**; observed `net_gex` sign
     change 36.5 → 37; treat as ±2% per the coarseness pitfall). **Spot 35.07 is below it
     → short gamma.** Reclaiming 37 flips the regime to long-gamma and would invalidate
     this phase's read.
  2. **Largest GEX strike = 40 (`net_gex` −1,165,778)**, then **35 (−977,948)** and
     **30 (−471,049)**. These are **amplification zones, not walls** — dealers sell into
     declines through them. 35 is explicitly tagged `resistance_wall` by
     `today-gamma-flip` (`gex` −323,628).
  3. **Vanna pivot = 36** — where `atm_flip_strike`, the 08-07 `max_pain_strike` (+2.68%)
     and the GEX sign change all converge. **The single most useful level this phase
     produces**, and the target the vanna/charm bid pulls toward.
  4. **Near-expiry max-pain magnet = 36 (08-07, `dte` 9, +2.68%)** — the tradeable pin.
     **Do not use 08-21's 45 (+28.35%)** as a level: largest `holder_value` ($5.11M) but a
     barbell artifact, static-OI, and phase 3 established today's flow is not yet in OI.
     Use phase-3's walls for levels and max pain only for directional pull.
- **Open questions:**
  - **Which force resolves first — the vanna bid or the gamma break?** The vanna engine has
    already burned most of its fuel (`iv_rank` at the **15.6th self percentile**,
    `front-end-iv-ratio` only 1.14), and its stated trigger is a **VIX collapse**. Phase 6
    must establish whether the macro tape supports that; today was broadly risk-off. (→ 6, 8b)
  - **Why are 25Δ puts cheaper than 25Δ calls (`skew_ratio` 0.994) when four lanes read
    bearish and the public is net put-long?** Either the market is genuinely complacent —
    in which case a 35 break runs into thin protection *and* negative gamma — or ENPH is
    simply a de-rated name (**−52.4% from its 52-week high**) that has stopped attracting
    hedging demand. The distinction changes the payoff, not the direction. (→ 7c, 8b)
  - **Does the flat 82–87% curve past `dte` 23 mean there is no catalyst until 2026-10-27,
    or is the market under-pricing the 08-21 OPEX?** 46,288 contracts expire there against
    a flat vol surface. (→ 5, 6, 9)
  - **How much does the 36.08-vs-35.07 surface offset distort the GEX/DEX magnitudes?**
    The signs are robust; the magnitudes are struck 2.9% high. (→ 10)
  - **The Oct-16 P35 buyer bought the cheapest vol on the curve (82.2%) at zero skew cost.
    Is that skill, and does it argue the Jan-2028 P30 position is directional rather than
    protective?** (→ 7c, 8b)
