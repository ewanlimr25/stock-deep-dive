# Phase 4 — Dealer Structure & Gamma

**Ticker:** SWKS
**As-of date:** 2026-07-31
**Generated:** 2026-08-02
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

Dealers are **net short gamma with spot pinned at the single most negative-gamma
strike on the board**. `uw options-structure gex` returns
`regime: "NEGATIVE"` — *"Dealers net short gamma — expect trend acceleration and
increased volatility"* — with `zero_gamma_level` **77.61** against an underlying of
**62.45**, and the per-strike surface is negative continuously from **45 through
62.5**, bottoming at **62.5 (−448,437 GEX)**, which is where price closed. The
mechanical read is that **any decisive move off $62.50 gets amplified rather than
damped**, in either direction. Both delta and vanna lean the same way: `dex`
returns *"Public is net call-long → dealers net short calls → dealer hedge is to
BUY underlying"* (`net_dex` **+$3,674,783** ≈ 58,844 share-equivalents), and
`vanna-charm` returns *"Classic vanna-squeeze setup if VIX collapses"* — but both
are **mechanically trivial in size** (the dealer buy-to-hedge is ~1.2% of a day's
share volume). Vol structure is quiet and confirms the event is behind us:
`iv-term-structure` = **FLAT** (`kink_expiry: null`, avg IV 57.2%–60.7% across all
eight expiries) and `term-skew` = **NORMAL** (`skew_ratio` 1.042, 25Δ put 61.58%
vs 25Δ call 59.10%). **Max pain for the 2026-08-21 OPEX cliff is $65.00
(+4.23%)** — which lands exactly on phase 3's `call_wall_resistance`. Two caveats
dominate everything here: the ZGL is **contaminated by the same dead legacy
80-strike call OI** phase 3 exposed, and `gex` and `today-gamma-flip` return
**opposite regime labels off identical numbers**.

## Key signals

- **`gex.regime = "NEGATIVE"`**, `regime_description` = *"Dealers net short gamma —
  expect trend acceleration and increased volatility"*; `zero_gamma_level` **77.61**
  vs `underlying_price` **62.45** ⇒ spot is **19.5% below ZGL**, deep in short-gamma
  territory. `[STRUCT:gex]`
- **Spot sits on the most negative-gamma strike:** per-strike GEX at **62.5 =
  −448,437**, the minimum of the entire surface; `today-gamma-flip` independently
  names `atm_flip_strike` **62.5**. `[STRUCT:gex]` `[STRUCT:today_gamma_flip]`
- **Max pain (2026-08-21, 21 DTE) = $65.00**, `distance_pct` **+4.23%**,
  `holder_value_at_max_pain` **$603,250**, `put_call_oi_ratio` 0.26. Identical to
  phase 3's `call_wall_resistance` strike. `[STRUCT:max_pain]`
- **Dealer hedge flow is a bid, but a small one:** `net_dex` **+$3,674,783**
  (`call_dex` +$16,283,328, `put_dex` −$12,608,545) = **58,844 share-equivalents**
  ≈ **1.2% of the as-of day's 4,991,143 share volume**. `[STRUCT:dex]`
- **Vol is flat and calm, not stressed:** `iv-term-structure.structure` = **FLAT**,
  `kink_expiry` **null**; `term-skew.interpretation` = **NORMAL**, `skew` +0.0249,
  `skew_ratio` **1.042**. No backwardation, no tail-hedging bid. `[STRUCT:iv_term_structure]` `[STRUCT:term_skew]`
- **Two tool-level contradictions must be carried to phase 10:** (a) `gex` says
  `NEGATIVE` while `today-gamma-flip` says `POSITIVE` off the **same**
  `total_gex = 1,191,030` and **same** ZGL 77.61; (b) `front-end-iv-ratio` resolved
  **both** legs to the same expiry (`near_dte_actual = far_dte_actual = 19`), so its
  `ratio: 1` / `regime: "FLAT"` is a **degenerate non-measurement**. `[STRUCT:gex]` `[STRUCT:front_end_iv_ratio]`

## Detailed findings

### GEX — gamma exposure and the zero-gamma level

`uw options-structure gex --symbol SWKS --dte-max 45 --date 2026-07-31`:

| Field | Value |
|---|---|
| `regime` | **`NEGATIVE`** |
| `regime_description` | *"Dealers net short gamma — expect trend acceleration and increased volatility"* |
| `total_gex` | 1,191,030 |
| **`zero_gamma_level`** | **77.61** |
| `underlying_price` | 62.45 |
| `dte_max` | 45 |
| `note` (tool's own) | *"GEX most meaningful for index products (SPY, QQQ) and large-cap single stocks with deep OI."* |

Per-strike surface (all 18 strikes returned):

| Strike | GEX | | Strike | GEX |
|---|---|---|---|---|
| 45 | −16,795 | | 70 | +80,555 |
| 47.5 | −26,960 | | 72.5 | +81,467 |
| 50 | −105,965 | | **75** | **+395,116** |
| 52.5 | −112,087 | | 77.5 | +67,157 |
| 55 | −86,861 | | **80** | **+807,007** |
| 57.5 | −74,693 | | 82.5 | +5,112 |
| 60 | −173,504 | | 95 | +394,902 |
| **62.5** | **−448,437** | | 100 | +18,999 |
| 65 | +247,603 | | | |
| 67.5 | +138,413 | | | |

**The surface flips sign at 65.** Everything from 45 to 62.5 is negative gamma;
everything from 65 up is positive. Spot **62.45 sits on the negative-gamma
minimum**.

**The ZGL of 77.61 is not tradeable and should not be quoted as a level.** It is
manufactured by exactly the OI phase 3 disqualified: **+807,007 GEX at strike 80**
and **+395,116 at 75** are produced by the **11,927-contract legacy Aug-21 80 call
(last fill $0.24, bid/ask 0.10/0.25, OI flat since 2026-07-14)** and the
2,929-contract 75 call (last fill $0.43) — see
`phase-3-positioning.md §OI walls by strike`. Those contracts carry negligible
dollar gamma in any economic sense; they inflate a static Σ(gamma × OI)
computation and drag the zero-crossing 24% above spot. The **+394,902 at strike 95**
is the same artifact one step further out.

**The tradeable statement is the sign of gamma where price actually is, and that is
unambiguous: short gamma from 45 to 62.5, most negative at spot.** The phase's own
pitfall — *"ZGL on low-liquidity tickers is coarse; treat as ±2% band"* —
understates the problem here; on this name the ZGL is not merely coarse, it is
**driven by dead OI**, and phase 9 must not use 77.61 as a level.

Read against phase 2, this is coherent: dealers short gamma below 65 means the
**−5.40% earnings break on 2026-07-29 would have been amplified by dealer selling
into it**, which is precisely the mechanical backdrop against which the dark pool
absorbed **+341,637 net shares** that session
(`phase-2-dark-pool.md §The two sessions that matter`). Someone was buying what
the hedging machine had to sell.

### DEX — net dealer delta

`uw options-structure dex --symbol SWKS --dte-max 45 --date 2026-07-31`:

| Field | Value |
|---|---|
| `call_dex` | **+$16,283,328** |
| `put_dex` | **−$12,608,545** |
| **`net_dex`** | **+$3,674,783** |
| `spot` | 62.45 |
| `interpretation` | *"Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying."* |
| `note` (tool's own) | *"DEX = Σ(delta × OI × 100 × spot). Sign reflects public positioning; dealer hedge is the inverse."* |

`per_strike` returned **empty** for this leaf on this ticker (the key exists but
carries no rows) — noted, not an error, and the aggregate is sufficient.

**Sizing the hedge honestly:** `net_dex / spot = 3,674,783 / 62.45 =` **58,844
share-equivalents** of dealer buying. Against the as-of session's **4,991,143**
share volume that is **1.18%**; against the **150,956,637** derived shares
outstanding (`phase-2-dark-pool.md`) it is **0.039%**. The *direction* is a bid;
the *magnitude* is noise. Compare: phase 2's two-session dark-pool absorption was
**+573,766 shares — 9.8× larger than the entire standing dealer delta hedge.**

Note also that `call_dex` is itself inflated by the legacy 80/75-strike OI, so the
true public call-length is smaller than $16.28M suggests. The **sign** survives
that correction (put_dex is large and negative on live near-money strikes); the
**size** does not.

### Vanna + charm

`uw options-structure vanna-charm --symbol SWKS --dte-max 45 --date 2026-07-31`:

| Field | Value |
|---|---|
| `call_vanna` | −257 |
| `put_vanna` | +282 |
| **`net_vanna`** | **+25** |
| `net_charm` | **+14,264** |
| `vanna_interpretation` | *"Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."* |
| `note` (tool's own) | *"Closed-form approximations: vanna ≈ −vega×delta/(σ×S); charm ≈ −theta×delta/option_price. Coarse for deep ITM/OTM and near-expiry — filtered to dte ≥ 1 by default."* |

The tool's squeeze label is quoted verbatim per the composition guidance, but it
must be read with three constraints:

1. **`net_vanna` is +25** — the residual of −257 and +282. That is not a squeeze
   engine; it is two nearly-cancelling books. The phase's vanna-squeeze setup
   ("positive vanna + negative dealer delta + IV declining") is only **partially**
   satisfied: vanna is positive and IV *is* declining (iv30d 0.741 → 0.559 across
   the event, `phase-0.5-context.md`), but dealer delta is **positive** (dealers
   need to *buy*, per DEX), and the magnitude is negligible.
2. The IV decline that would drive the squeeze **has already happened** — IV rank
   fell 91.2 → 52.9 over three sessions and now sits at the **29.9th percentile of
   SWKS's own 78-session history**. There is far less vol left to collapse.
3. `net_charm` **+14,264** is likewise directionally supportive (time decay pushes
   dealers to buy) and likewise immaterial next to a 5M-share daily tape.

**Verdict on the squeeze: label acknowledged, effect not material.** It is a
tailwind of the correct sign, not a mechanism to trade.

### IV term structure

`uw options-structure iv-term-structure --symbol SWKS --date 2026-07-31`:
`structure` = **`FLAT`**, `kink_expiry` = **null**, `expiry_count` = 8.

| Expiry | `dte_approx` | `avg_iv` | `avg_iv_pct` | `contract_count` |
|---|---|---|---|---|
| 2026-08-21 | 19 | 0.6042 | 60.4% | 208 |
| 2026-09-18 | 47 | **0.5721** | **57.2%** | 172 |
| 2026-11-20 | 110 | 0.6030 | 60.3% | 35 |
| 2026-12-18 | 138 | 0.5867 | 58.7% | 3 |
| 2027-01-15 | 166 | 0.5842 | 58.4% | 35 |
| 2027-02-19 | 201 | 0.5797 | 58.0% | 1 |
| 2027-03-19 | 229 | **0.6068** | **60.7%** | 14 |
| 2028-01-21 | 537 | 0.5780 | 57.8% | 4 |

Total range across 537 days: **57.2% to 60.7% — a 3.5-point band.** There is no
front-end stress, no backwardation, and no kink. This is exactly what a curve looks
like **after** an event has cleared, and it corroborates
`phase-0.5-context.md`'s verified finding that earnings were **2026-07-28
postmarket** and the next print is **2026-10-27**. The phase's pitfall *"don't
trade backwardation if earnings already passed within 24h"* is moot — there is no
backwardation to mis-trade.

One mild feature worth carrying: the **Sep-18 expiry is the cheapest point on the
curve at 57.2%**, ~2.8 points below Nov-20 (60.3%) and 3.2 below Mar-19 (60.7%).
The 2026-11-20 elevation is consistent with the 2026-10-27 earnings date sitting
inside it — the same expiry phase 3 flagged for its anomalous `put_call_oi_ratio`
of **4.192**. **Sep-18 is the local vol trough and Nov-20 carries the event
premium.**

### Term skew

`uw options-structure term-skew --symbol SWKS --dte-target 30 --date 2026-07-31`:

| Field | Value |
|---|---|
| `put_25d_iv` | 0.6158 (61.58%) |
| `call_25d_iv` | 0.5910 (59.10%) |
| `skew` | **+0.0249** |
| `skew_ratio` | **1.042** |
| **`interpretation`** | **`NORMAL`** |
| `dte_target` / `dte_actual` | 30 / **19** |

25Δ puts carry a **4.2% relative premium** over 25Δ calls. The tool labels this
**NORMAL** and that label is taken as authoritative per the composition guidance.
There is **no skew steepening**, so the phase's "tail-hedging demand precedes
risk-off" heuristic does **not** fire.

This is a genuinely notable *negative* result. On the day **Apple fell −7.35% with
−$141.1M of net bearish premium** (`phase-0.5-context.md §Sector read`), SWKS's put
skew stayed normal. Combined with `phase-1-flow.md`'s finding that the SWKS put
ask-share **collapsed to 0.088** on that same day, the options market showed **no
demand for downside protection into its largest customer's blow-up**. Phase 8 must
adjudicate whether that is informed calm or unpriced complacency — it is the
sharpest open question in this run.

Note `dte_actual = 19` against a 30-day target: SWKS has **no expiry between
Aug-21 and Sep-18**, so the "30-day" skew is measured on the 19-day tenor. Minor,
but it means this is a front-tenor skew reading, not a true 30-day one.

### Front-end IV ratio — **degenerate, no signal**

`uw options-structure front-end-iv-ratio --symbol SWKS --near-dte 7 --far-dte 30 --date 2026-07-31`:

```
near_dte_actual = 19    near_iv = 0.6042
far_dte_actual  = 19    far_iv  = 0.6042
ratio = 1               regime  = "FLAT"
```

**Both legs resolved to the same expiry (2026-08-21).** SWKS has no listed expiry
between 7 and 30 DTE other than Aug-21, so the tool compared Aug-21 with itself and
returned a mechanically guaranteed `ratio: 1`. **The `FLAT` regime here is an
artifact of the resolution, not a measurement of event stress.** It is recorded for
audit completeness and **contributes nothing** to the verdict. Any downstream phase
that cites "front-end IV ratio = 1, no event stress" would be citing a tautology.

(The genuine event-stress read comes from `iv-term-structure` above, which compares
eight distinct expiries and independently returns FLAT.)

### Today's gamma flip

`uw options-structure today-gamma-flip --symbol SWKS --date 2026-07-31`:

| Field | Value |
|---|---|
| `regime` | **`POSITIVE`** ⚠ |
| `today_total_gex` | 1,191,030 |
| `today_zero_gamma` | 77.61 |
| **`atm_flip_strike`** | **62.5** |
| `today_expiry` | **2026-08-21** |
| `spot` | 62.45 |

`key_walls`:

| Strike | GEX | `role` | Distance from spot |
|---|---|---|---|
| 80 | +807,007 | `support_wall` ⚠ | +28.1% |
| **62.5** | **−448,437** | `resistance_wall` ⚠ | **+0.1%** |
| 75 | +395,116 | `support_wall` ⚠ | +20.1% |
| 95 | +394,902 | `support_wall` ⚠ | +52.1% |
| 65 | +247,603 | `support_wall` | +4.1% |

**This leaf is de-rated on three independent grounds and its labels are not used:**

1. **It is designed as a 0DTE/intraday read.** `phase-1-flow.md` established
   `share_0dte = 0` and `share_weeklies = 0` for SWKS — there is **no 0DTE book at
   all**, so the tool fell back to `today_expiry = 2026-08-21`, **21 days out**.
   This is not "today's" gamma flip in any meaningful sense.
2. **The run is not intraday.** Per the phase instruction ("*if after-hours, note
   and skip*"), this is an as-of/after-hours run against a completed session.
   Noted and skipped as a live signal.
3. **The `role` tags are mechanically inverted for out-of-range strikes.** A
   positive-GEX strike **28% above spot** is labelled `support_wall`, and the
   negative-GEX strike **at spot** is labelled `resistance_wall`. The tags appear to
   key purely on the sign of GEX with no reference to `distance_pct`. A
   positive-gamma strike far above spot is a pin/resistance if price ever reaches
   it — it is not support beneath current price.

**What *is* usable from this leaf** is `atm_flip_strike` = **62.5**, which
independently corroborates the `gex` per-strike minimum. Two leaves agreeing that
**62.5 is the pivot** is the one solid structural fact here.

**⚠ Regime contradiction (carried to phase 10).** `gex` returns
`regime: "NEGATIVE"` and `today-gamma-flip` returns `regime: "POSITIVE"` from
**identical inputs** — same `total_gex` 1,191,030, same ZGL 77.61, same spot 62.45.
The most likely mechanism is that `gex` labels by **spot vs ZGL** (62.45 < 77.61 ⇒
short gamma) while `today-gamma-flip` labels by the **sign of Σ GEX** (1,191,030 >
0 ⇒ positive). Both cannot be quoted as-is. **This phase adopts `NEGATIVE`**, on
the grounds that (a) the phase's own interpretation heuristics define the regime by
spot-versus-ZGL, and (b) the positive Σ is produced entirely by the dead 75/80/95
strikes, whereas every strike price can actually reach in the near term is
negative. This adoption is a **reasoned choice between contradictory tool outputs,
not a derived value**, and is flagged as such.

### Max pain — the opex-gravity magnet

`uw options-structure max-pain --symbol SWKS --dte-max 30 --date 2026-07-31`:

| Field | Value |
|---|---|
| `expiry` | **2026-08-21** |
| `dte` | 21 |
| **`max_pain_strike`** | **65** |
| **`distance_pct`** | **+4.23%** |
| `holder_value_at_max_pain` | $603,250 |
| `call_oi` / `put_oi` / `total_oi` | 19,203 / 4,998 / 24,201 |
| `put_call_oi_ratio` | 0.26 |
| `caveat` (tool's own) | *"Single-day OI snapshot. Max pain assumes settlement at each candidate strike with current open interest unchanged to expiry."* |

Full `pain_curve` for 2026-08-21 (total holder value at each candidate settlement):

| Strike | Call value | Put value | **Total value** |
|---|---|---|---|
| 47.5 | $0 | $5,290,000 | $5,290,000 |
| 52.5 | $0 | $3,073,000 | $3,073,000 |
| 55 | $0 | $2,201,250 | $2,201,250 |
| 57.5 | $0 | $1,501,000 | $1,501,000 |
| 60 | $41,500 | $884,750 | $926,250 |
| **65** | $381,500 | $221,750 | **$603,250 ← minimum** |
| 67.5 | $770,000 | $0 | $770,000 |
| 70 | $1,158,500 | $0 | $1,158,500 |
| 72.5 | $1,741,000 | $0 | $1,741,000 |
| 75 | $2,439,500 | $0 | $2,439,500 |
| 80 | $5,301,000 | $0 | $5,301,000 |
| 87.5 | $18,538,500 | $0 | $18,538,500 |
| 100 | $40,963,500 | $0 | $40,963,500 |

The curve is **shallow and asymmetric**: $603,250 at 65 versus $926,250 at 60 — a
gravity differential of only ~$323k, and 60 is the second-best strike. The pull
toward 65 is real but weak, and the curve rises far more steeply *above* 65 than
below it. Note there is **no 62.5 strike listed for Aug-21** — consistent with
phase 3's full Aug-21 chain, which has no 62.5 contract.

Max pain across all expiries (`--dte-max 0`):

| Expiry | DTE | Max pain | `distance_pct` | `put_call_oi_ratio` |
|---|---|---|---|---|
| **2026-08-21** | **21** | **65** | **+4.23%** | 0.26 |
| 2026-09-18 | 49 | **62.5** | **+0.22%** | 0.718 |
| 2026-11-20 | 112 | 72.5 | +16.26% | **4.192** |
| 2026-12-18 | 140 | 50 | −19.82% | 0.659 |
| 2027-01-15 | 168 | 65 | +4.23% | 1.699 |
| 2027-03-19 | 231 | 55 | −11.80% | 0.000 |
| 2027-06-17 | 321 | 60 | −3.78% | 0.000 |
| 2028-01-21 | 539 | 35 | −43.87% | 0.000 |

**Two near-dated magnets bracket spot: Sep-18 at 62.5 (+0.22%, essentially spot)
and Aug-21 at 65 (+4.23%).** Read with the GEX surface per the composition
guidance: max pain sits **just above** a short-gamma zone, so this is *not* the
"max pain near a positive-gamma pin reinforces the range" case, nor the "max pain
far below spot pulls a short-gamma break downward" case. It is the mild upward-pull
case — a weak magnet toward 65 into 2026-08-21, in a regime where dealers will
**amplify** rather than resist whichever way price actually goes.

**A phase-3 caution, checked and cleared.** `phase-3-positioning.md §OI term
structure` warned that max pain "will be dragged artificially high by the 16,409
dead ≥20%-OTM calls" and that "a max-pain print near $75–80 should be treated as an
artifact." **That did not happen** — the pain curve shows those very strikes
produce *enormous* holder value ($5.3M at 80, $41.0M at 100), which pushes the
minimum **down**, not up. Max pain landed at **65**, and the phase-3 caution is
therefore **withdrawn**: the $65 magnet is genuine, not an artifact. It is also
**the same strike phase 3 independently identified as `call_wall_resistance`**
(`net_oi` +435, `distance_pct` +4.23%) — the two agree to the cent.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw options-structure gex --symbol SWKS --dte-max 45 --date 2026-07-31 --json` | `regime`=**NEGATIVE**, `regime_description`="Dealers net short gamma…", `total_gex`=1191030, **`zero_gamma_level`=77.61**, `underlying_price`=62.45 ← `.regime`, `.zero_gamma_level`; per-strike min **62.5 = −448437**, max **80 = +807007**, sign flip between 62.5 and 65 ← `.per_strike[]` | 18 strikes |
| `uw options-structure dex --symbol SWKS --dte-max 45 --date 2026-07-31 --json` | `call_dex`=16283328, `put_dex`=−12608545, **`net_dex`=3674783**, `spot`=62.45, `interpretation`="Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying." ← `.net_dex`, `.interpretation`; derived 3674783/62.45 = **58,844 share-equiv** | aggregate (`per_strike` empty) |
| `uw options-structure vanna-charm --symbol SWKS --dte-max 45 --date 2026-07-31 --json` | `call_vanna`=−257, `put_vanna`=+282, **`net_vanna`=+25**, `net_charm`=+14264, `vanna_interpretation`="…Classic vanna-squeeze setup if VIX collapses." ← `.net_vanna`, `.vanna_interpretation` | aggregate |
| `uw options-structure iv-term-structure --symbol SWKS --date 2026-07-31 --json` | **`structure`=FLAT**, `kink_expiry`=**null**, `expiry_count`=8; avg_iv Aug-21 0.6042 (208 contracts), Sep-18 **0.5721** (172), Nov-20 0.6030, Mar-19 **0.6068** ← `.structure`, **`.term_structure[]`** (not `.results`) | 8 expiries |
| `uw options-structure term-skew --symbol SWKS --dte-target 30 --date 2026-07-31 --json` | `put_25d_iv`=0.6158, `call_25d_iv`=0.5910, `skew`=0.0249, **`skew_ratio`=1.042**, **`interpretation`=NORMAL**, `dte_actual`=**19** (target 30) ← `.interpretation`, `.skew_ratio` | aggregate |
| `uw options-structure front-end-iv-ratio --symbol SWKS --near-dte 7 --far-dte 30 --date 2026-07-31 --json` | `near_dte_actual`=**19**, `far_dte_actual`=**19**, near_iv=far_iv=0.6042, `ratio`=1, `regime`=FLAT ← `.ratio`, `.regime` — **degenerate: both legs = same expiry** | 1 (self-compare) |
| `uw options-structure today-gamma-flip --symbol SWKS --date 2026-07-31 --json` | `regime`=**POSITIVE** ⚠ (contradicts `gex`), `today_total_gex`=1191030, `today_zero_gamma`=77.61, **`atm_flip_strike`=62.5**, `today_expiry`=2026-08-21, key_walls roles ← `.atm_flip_strike`, `.key_walls[]` | 5 walls |
| `uw options-structure max-pain --symbol SWKS --dte-max 30 --date 2026-07-31 --json` | **`max_pain_strike`=65**, `distance_pct`=**4.23**, `dte`=21, `holder_value_at_max_pain`=603250, `call_oi`=19203, `put_oi`=4998, `put_call_oi_ratio`=0.26 ← `.results[0]`; 13-point `pain_curve` min at 65 ($603,250) vs 60 ($926,250) ← `.pain_curve[]` | 1 expiry + 13 strikes |
| `uw options-structure max-pain --symbol SWKS --dte-max 0 --date 2026-07-31 --json` | Sep-18 max_pain **62.5** (+0.22%, pcr 0.718); Nov-20 **72.5** (+16.26%, pcr **4.192**); Jan-27 65; Jan-28 35 ← `.results[]` | 8 expiries |

## Tool errors

No `uw options-structure` command errored. All eight leaves returned parseable JSON.

**Non-error anomalies recorded per orchestration rule 3:**
- `dex` → `.per_strike` present but **empty** for this ticker. Aggregate fields
  returned normally; no value was invented for the missing rows.
- `front-end-iv-ratio` → **degenerate self-comparison** (`near_dte_actual` =
  `far_dte_actual` = 19). Not a failure of the tool; a consequence of SWKS having
  no listed expiry between 7 and 30 DTE besides 2026-08-21. Output discarded as
  uninformative.
- `today-gamma-flip` → ran successfully but is **structurally inapplicable**
  (SWKS has no 0DTE book: `share_0dte = 0` per `phase-1-flow.md`; and this is an
  after-hours as-of run). Only `atm_flip_strike` retained.

## DATA NOTE / CORRECTION

1. **Regime label contradiction — adopted `NEGATIVE`, flagged for phase 10.**
   `gex.regime = "NEGATIVE"` vs `today-gamma-flip.regime = "POSITIVE"`, from
   identical `total_gex` (1,191,030), ZGL (77.61) and spot (62.45). Neither value
   was altered. This phase **adopts NEGATIVE** because the phase's own heuristics
   define the regime by spot-versus-ZGL, and because every strike within reach of
   spot carries negative GEX. Recorded as a **reasoned adjudication between
   conflicting tool outputs**, not a re-derivation — the composition guidance
   forbids recomputing a regime by hand, and no recomputation was performed.
2. **`zero_gamma_level = 77.61` is reported but explicitly disqualified as a
   tradeable level.** It is not a wrong read — it is the tool's correct output on
   a chain whose positive-gamma mass is the dead 75/80/95 legacy call OI documented
   in `phase-3-positioning.md`. Downstream phases must use the **62.5 sign-flip**,
   not 77.61.
3. **`iv-term-structure` returns `.term_structure`, not `.results`.** A first `jq`
   pass against `.results[]` yielded empty rows (the same trap
   `phase-3-positioning.md` hit on `oi term-structure`). Re-read against the actual
   key returned all 8 expiries. No value from the empty read was carried forward.
4. **A phase-3 caution is withdrawn on evidence.** Phase 3 predicted max pain would
   be dragged toward $75–80 by dead call OI. The returned `pain_curve` shows the
   opposite mechanism — those strikes generate the *largest* holder value
   ($5,301,000 at 80; $40,963,500 at 100), pushing the minimum down to **65**. The
   $65 magnet is genuine. Correction recorded because phase 10 would otherwise flag
   phase 3 and phase 4 as contradictory.
5. `net_dex` share-equivalents (58,844) and the %-of-volume figures are **derived**
   (`net_dex / spot`, then ÷ the screener's `total_volume` 4,991,143). Both inputs
   are validated values already quoted in this run; the arithmetic is shown inline.

## Verdict for downstream phases

- **Dealer regime:** **SHORT GAMMA (transitional at the margin).** Spot 62.45 sits
  **19.5% below** the reported ZGL of 77.61 and **directly on the most negative
  per-strike GEX on the board (62.5, −448,437)**. Practical consequence for phase 9:
  **moves off $62.50 are amplified, not damped** — dealers sell into weakness and
  buy into strength. Realized vol should exceed what the flat 57–60% IV surface
  implies, which argues (with `phase-1-flow.md`'s finding that the tape is net
  short premium into 29.9th-percentile-cheap vol) for **owning gamma rather than
  selling it**. "Transitional at the margin" because the sign flips just 4% above
  spot at strike 65.
- **Conviction:** **3 / 5.** Up-weighted by the unusually clean cross-phase
  agreement on levels — **62.5 named independently by `gex` per-strike minimum and
  by `atm_flip_strike`; 65 named independently by max pain, by phase-3's
  `call_wall_resistance`, and by phase-1's Sep-18 62.5/65 credit call spread.**
  Held below 4 by: (a) the **regime-label contradiction** between two leaves of the
  same tool family; (b) the ZGL being **structurally unusable**; (c) one leaf
  (`front-end-iv-ratio`) returning a **degenerate non-measurement** and another
  (`today-gamma-flip`) being **inapplicable**; (d) the tool's own note that GEX is
  *"most meaningful for index products and large-cap single stocks with deep OI"* —
  SWKS's chain is neither deep nor active (`phase-3-positioning.md`: largest OI
  change on the entire chain = 46 contracts); (e) every dealer-flow magnitude here
  (58,844 delta-shares, net_vanna +25) is **an order of magnitude below** the
  573,766 shares the dark pool moved.
- **Structural levels for phase-9:**
  1. **$62.50 — the gamma pivot / ZGL proxy.** Per-strike GEX minimum (−448,437)
     and `atm_flip_strike`. Spot closed at $62.28, i.e. **0.35% below the pivot**.
     Above it dealers are progressively less short gamma; below it they are
     maximally short. **This — not 77.61 — is the level to trade around.**
  2. **$80.00 — the largest GEX strike (+807,007).** Reported for completeness and
     **explicitly disqualified**: it is the dead legacy Aug-21 80 call (11,927 OI,
     $0.24 last fill). **Do not use as a level.** The largest *live* positive-GEX
     strike is **$65.00 (+247,603)**.
  3. **Vanna pivot — none identifiable.** `net_vanna` is +25 (−257 calls vs +282
     puts); there is no strike at which vanna meaningfully turns. Recorded as
     **n/a** rather than manufactured.
  4. **★ Max-pain opex magnet: $65.00 for 2026-08-21 (21 DTE, +4.23%)**, with
     **$62.50 for 2026-09-18 (49 DTE, +0.22%)** behind it. The Aug-21 pull is
     **weak** ($603,250 vs $926,250 at strike 60 — a ~$323k differential) and rests
     on a **static-OI snapshot** per the tool's own caveat, on a chain with **33%
     tracking coverage** (`phase-3-positioning.md §DATA NOTE 2`). Treat $65 as a
     soft upward magnet, not a target.
  - **Composite near-term structure: a $60–65 box with a $62.50 pivot** — GEX
    sign-flip at 65, max pain at 65, phase-3 `call_wall_resistance` at 65,
    phase-3 `put_wall_support` at 60, phase-2 dark-pool support shelf at
    $60.25–61.22. **Five independent reads, three data sources, one box.**
- **Open questions:**
  - **Why is skew NORMAL (1.042) on the day Apple fell −7.35%?** Combined with the
    SWKS put ask-share collapsing to 0.088 (`phase-1-flow.md`), the options market
    priced **no** incremental downside risk from its largest customer's earnings
    miss. Phases 6, 7c and 8b must decide whether that is informed calm (SWKS
    already de-rated on its own 2026-07-28 print) or unpriced complacency. **This
    is the highest-value unresolved question in the run.**
  - **Does short gamma at spot favour the accumulator or the seller?** Phase 2's
    buyers absorbed a dealer-amplified break at $58–59; the same mechanics will
    amplify the *next* break. Phase 9 must size for a wider realized-vol
    distribution than the 9.10% `implied_move_perc` implies, and must not place a
    stop just below $60 where dealer selling accelerates.
  - **Is Sep-18 the right tenor?** It is the cheapest point on the IV curve
    (57.2%), its max pain sits at spot (62.5, +0.22%), and it carries the
    62.5/65 credit spread phase 1 observed — while Aug-21 (21 DTE) is where 61.87%
    of tracked OI expires. Phase 9 should weigh Sep-18 for structure against
    Aug-21 for gravity.
