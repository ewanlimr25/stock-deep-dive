# Phase 4 — Dealer Structure & Gamma

**Ticker:** MU
**As-of date:** 2026-07-28
**Generated:** 2026-07-28T21:54:00-04:00
**Upstream phases cited:** `phase-0.5-context.md`, `phase-1-flow.md`, `phase-2-dark-pool.md`, `phase-3-positioning.md`

## Summary

**MU is in an unambiguous short-gamma regime with no escape hatch: `regime = "FULLY_NEGATIVE"`,
`regime_description` = "All strikes have negative net GEX — strong gamma amplification",
`total_gex = -45,676,510`, and `zero_gamma_level = null`** — there is **no strike within 45 DTE
at which dealer gamma turns positive.** Dealers amplify every move in both directions, which
explains phase-0.5's violent tape (-8.85%, +12.17%, -8.02%, -6.99% within eight sessions) and is
the single most important structural fact for sizing. Compounding it, **`net_dex` is
-$9,116,110,160** and the tool's own reading is *"Public is net put-long → dealers net short
puts → **dealer hedge is to SELL underlying**"* — a standing mechanical supply. **The largest
negative gamma concentration in the entire chain sits at the $800 strike (-6,527,065)**, the
same strike that is phase-3's dominant put wall (net -32,711 OI, -2.39% from spot), phase-2's
heaviest dark-pool selling zone, and phase-1's written put strike. **Four independent lenses
converge on $800 — a break there is where dealer hedging bites hardest.**

Two genuine counterweights keep this from being a one-way bear read. First, **max pain sits
7.4%–14.7% ABOVE spot on every near expiry** (7/31 → **930**, 8/21 → **940**), a latent upward
pull — though weak at this distance. Second, the vanna configuration is a *bullish* asymmetry:
**`net_vanna` +5,467 (put_vanna +8,328)** with the tool flagging *"Classic vanna-squeeze setup
if VIX collapses"* — falling IV would force dealers short puts to **buy** underlying. And
notably, **skew is `NORMAL` (25Δ put 1.0051 vs call 0.9545, ratio 1.053)** — after an 8.85%
drop, the options market is pricing **no panic**. Term structure is **BACKWARDATION** but mild
(front-end ratio **1.07**).

## Key signals

- **`regime = FULLY_NEGATIVE`, `total_gex = -45,676,510`, `zero_gamma_level = null`** — all 50
  strikes negative; no long-gamma refuge within 45 DTE. [STRUCT:gex]
- **`net_dex = -$9,116,110,160`** (call +$4.81B / put -$13.93B) → **dealers hedge by SELLING**.
  [STRUCT:dex]
- **Largest negative GEX strike = $800 (-6,527,065)**, then 815 (-4,133,679) and 750
  (-3,851,698). [STRUCT:gex]
- **Max pain is above spot everywhere**: 7/29 → 880 (+7.37%), **7/31 → 930 (+13.47%)**,
  8/21 → **940 (+14.69%)**. [STRUCT:max_pain]
- **`vanna_interpretation`: "Classic vanna-squeeze setup if VIX collapses"** — `net_vanna`
  +5,467, `net_charm` -792,093. [STRUCT:vanna_charm]
- **Skew is `NORMAL` — ratio 1.053.** No crash premium despite the drawdown. [STRUCT:term_skew]
- **`regime = BACKWARDATION`, front-end ratio 1.07** (8-DTE IV 1.1003 vs 31-DTE 1.0286).
  [STRUCT:front_end_iv_ratio] [STRUCT:iv_term_structure]

## Detailed findings

### GEX — gamma exposure

`uw options-structure gex --symbol MU --dte-max 45` (underlying_price 820.28):

| field | value |
|---|---|
| `regime` | **`FULLY_NEGATIVE`** |
| `regime_description` | "All strikes have negative net GEX — strong gamma amplification" |
| `total_gex` | **-45,676,510** |
| `zero_gamma_level` | **`null`** |
| strikes returned | 50 |

**Largest |net_gex| strikes** (the `per_strike` array carries only `strike` and `net_gex` —
there are no `call_gex`/`put_gex` fields):

| strike | `net_gex` | distance from spot |
|---:|---:|---:|
| **800** | **-6,527,065** | **-2.5%** |
| 815 | -4,133,679 | -0.7% |
| **750** | -3,851,698 | -8.6% |
| 820 | -3,549,453 | -0.1% |
| 850 | -3,299,191 | +3.6% |
| 810 | -3,157,701 | -1.3% |
| 790 | -2,020,783 | -3.7% |
| 780 | -1,142,183 | -4.9% |
| 830 | -995,316 | +1.2% |
| 900 | -937,938 | +9.7% |
| 870 | -934,128 | +6.1% |
| 860 | -925,520 | +4.7% |

**Reading (quoting the tool's own regime label, per composition guidance):** a `null` zero-gamma
level with a `FULLY_NEGATIVE` regime is materially different from "spot is below the ZGL." It
means there is **no price within the 45-DTE surface at which dealers flip to long gamma** —
MU cannot mean-revert its way into a vol-suppressing regime in the near term. Mechanically:
dealers **buy rallies and sell dips**, so trends extend and realized vol stays elevated.

This is the structural explanation for phase-0.5's observation that MU routinely moves ±5–12%
per session, and it is the reason **any phase-9 stop placed inside ~8% is inside the noise
band** — the implied move is 7.90% and the gamma regime actively amplifies excursions.

**The $800 convergence.** The single largest negative-gamma strike (-6,527,065, ~14% of total
GEX) is $800 — and it is independently:
- phase-3's **dominant put wall** (84,213 OI, net -32,711, `role = put_wall_support`, -2.39%),
- phase-2's **heaviest dark-pool distribution zone** ($790–809 bins, buy_ratio 0.411/0.419),
- phase-1's **written put strike** (the multi-session 750/800 short-put campaign).

Four lenses, one level. **If MU closes below $800, dealer hedging accelerates the move at the
point of maximum gamma** — and the secondary shelf at 750 is itself the third-largest negative
GEX strike (-3,851,698). This is the pivot the whole run has been converging on.

### DEX — dealer delta

`uw options-structure dex --symbol MU --dte-max 45` (spot 820.28):

| field | value |
|---|---:|
| `call_dex` | +$4,813,155,896 |
| `put_dex` | **-$13,929,266,057** |
| **`net_dex`** | **-$9,116,110,160** |
| `interpretation` | *"Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."* |
| `note` | *"DEX = Σ(delta × OI × 100 × spot). Sign reflects public positioning; dealer hedge is the inverse."* |

The public's option book carries **-$9.12B of net delta**, overwhelmingly from long puts
(-$13.93B put DEX against +$4.81B call DEX). Dealers are the other side — **short puts, long
delta — so their hedge is to sell stock.**

**Two cautions on how much to make of this:**
1. This is a **stock-of-positioning** number (Σ over all OI), not today's flow. Phase-1's
   *flow*-based net customer delta was ≈**-$41M ex-0DTE** — i.e. today added essentially
   nothing to this book. The -$9.12B is legacy positioning, largely built when MU was
   $900–1,200.
2. Combined with negative gamma the direction of hedging is **path-dependent**: as spot falls,
   dealers' short puts gain delta and they must sell *more* (amplification down); as spot
   rises, they buy back (amplification up). The DEX sign tells you the current hedge lean, not
   a forecast.

Cross-reference: phase-3's put/call OI ratios (2.592 at 3 DTE, 1.573 at 52 DTE) are the OI-side
expression of this same put-heavy book.

### Vanna + charm

`uw options-structure vanna-charm --symbol MU --dte-max 45` (dte ≥ 1 filter applied by the tool):

| field | value |
|---|---:|
| `put_vanna` | +8,328 |
| `call_vanna` | -2,861 |
| **`net_vanna`** | **+5,467** |
| **`net_charm`** | **-792,093** |
| `vanna_interpretation` | *"Public net vanna positive (put-heavy book). Falling IV → \|put delta\| drops → dealers (short puts) cover by BUYING underlying. Classic vanna-squeeze setup if VIX collapses."* |

**This is the most important bullish asymmetry in the run.** The mechanism: dealers are short a
large put book. If implied vol falls, those puts lose delta, dealers become over-hedged short,
and must **buy stock back**. Three facts make this live rather than theoretical:

- Per `phase-0.5-context.md`, **IV rank 83.48 is only the 43rd percentile of MU's own history**
  and IV *did not spike* on an -8.85% day. Vol is elevated in absolute terms but **already
  mean-reverting-prone relative to MU's recent regime** — there is room for it to fall.
- Front-end IV is **151–152% at the 7/29–7/31 expiries** (see below). A single uneventful
  session collapses that.
- **`net_charm` is -792,093** — negative charm on a put-heavy book means time decay itself
  bleeds delta out of those puts, producing a slow, passive dealer bid as expiry approaches,
  independent of any vol move.

**Caveat per the pitfall:** these are closed-form approximations (the tool says so explicitly:
*"vanna ≈ -vega×delta/(σ×S); charm ≈ -theta×delta/option_price. Coarse for deep ITM/OTM and
near-expiry"*). Direction is trustworthy; magnitude is not. Do not size on the vanna number.

### IV term structure

`uw options-structure iv-term-structure --symbol MU`: **`structure = "BACKWARDATION"`**,
`expiry_count = 24`, **`kink_expiry = null`** (a clean monotone-ish decay, no isolated event
bump the tool could identify).

Per-expiry `avg_iv` (note: this is the **average IV across all strikes in the expiry**, not a
pure ATM read — wing composition affects it):

| expiry | `avg_iv` | | expiry | `avg_iv` |
|---|---:|---|---|---:|
| 2026-07-29 | **1.5099** | | 2026-08-21 | 1.0855 |
| **2026-07-31** | **1.5180** | | 2026-08-28 | 1.0286 |
| 2026-08-03 | 1.0684 | | 2026-09-04 | **0.9893** |
| 2026-08-05 | 1.1003 | | 2026-09-18 | 1.1248 |
| 2026-08-07 | 1.3592 | | 2026-10-16 | **1.2188** |
| 2026-08-10 | 1.0278 | | 2026-11-20 | **0.9203** |
| 2026-08-12 | 1.0146 | | | |
| 2026-08-14 | 1.2554 | | | |

- **Front-end is extreme: 151–152% at 7/29 and 7/31**, collapsing to ~99–103% by early
  September. That is a very steep near-term vol premium — and it decays fast.
- **A distinct hump at 2026-10-16 (121.9%) sitting above 2026-09-04 (98.9%) and 2026-11-20
  (92.0%).** The Oct-16 expiry is the first monthly that **captures the reported 2026-09-22
  earnings date**, which is consistent — the market is pricing an event between 9/18 and 10/16.
  **This is independent corroboration that a September earnings catalyst is real**, and phase-7b/7c
  should weigh it against the possibility that `next_earnings_date` is stale. *(The 8/07 and
  8/14 bumps to 1.359/1.255 are unexplained by any known catalyst — flagged for phase-6.)*
- Practical consequence: **selling front-week vol into this backwardation is where the premium
  is**, and it is precisely what phase-1 observed customers doing (net -$120M premium sold).

### Term skew

`uw options-structure term-skew --symbol MU --dte-target 30` (`dte_actual = 31`):

| field | value |
|---|---:|
| `put_25d_iv` | 1.0051 |
| `call_25d_iv` | 0.9545 |
| `skew` | +0.0506 |
| `skew_ratio` | **1.053** |
| **`interpretation`** | **`NORMAL`** |

**This is the most surprising datapoint in the phase.** MU fell 8.85%, sits -32.4% from its
June peak, and has a documented crash-tail bid (phase-3: 55P +24,412, 500P +11,767) — yet
**25-delta puts are only 5.3% richer than 25-delta calls, and the tool labels the regime
`NORMAL`.** There is **no skew steepening**, hence no broad tail-hedging panic at the
30-day tenor.

Two readings, and phase-8b should debate them:
- **Benign:** the market treats this as an orderly sector repricing, not a solvency or
  demand-shock event. Consistent with phase-0.5's finding that SPY closed **green** and NVDA
  **+0.25%**.
- **Complacent:** in a `FULLY_NEGATIVE` gamma regime with dealers mechanically selling into
  weakness, flat skew means **downside convexity is cheap and under-owned** — the market is not
  paid to be short here, and a gap lower would be poorly hedged. The penny-put buying in
  phase-3 suggests at least someone holds this view.

### Front-end IV ratio

`uw options-structure front-end-iv-ratio --symbol MU --near-dte 7 --far-dte 30`:

| field | value |
|---|---:|
| `near_dte_actual` / `near_iv` | 8 / **1.1003** |
| `far_dte_actual` / `far_iv` | 31 / **1.0286** |
| **`ratio`** | **1.07** |
| **`regime`** | **`BACKWARDATION`** |

Backwardation is confirmed but **mild — a 7% front-end premium.** For context, genuine
event-stress backwardation on a single name typically runs 1.2–1.5×. **The market is pricing
elevated but not acute near-term risk.** Note the tension with the raw `avg_iv` series above
(7/31 at 1.518): the 8-DTE ATM read of 1.1003 is much calmer than the all-strike average,
meaning the 151% figure is inflated by wing/lottery strikes — **the ATM front end is 110%, not
151%.** Cite 1.1003 for structure work.

The pitfall about not trading backwardation within 24h of earnings **does not apply** — the
reported earnings date is 2026-09-22, roughly 8 weeks out.

### Today's gamma flip

`uw options-structure today-gamma-flip --symbol MU` — **this tool is 0DTE-only and intraday;
this run is after-hours, so it is a close-of-session snapshot of the 2026-07-29 expiry and is
reported with reduced weight** per composition guidance.

| field | value |
|---|---:|
| `today_expiry` | 2026-07-29 |
| `regime` | **`NEGATIVE`** |
| `today_total_gex` | -3,954,997 |
| `today_zero_gamma` | **`null`** |
| **`atm_flip_strike`** | **870** |
| `spot` | 820.21 |

`key_walls`:

| strike | `gex` | `role` |
|---:|---:|---|
| 800 | -915,482 | `resistance_wall` |
| **875** | **+872,023** | `support_wall` |
| **880** | +861,967 | `support_wall` |
| 750 | -738,915 | `resistance_wall` |
| 850 | -497,300 | `resistance_wall` |

The **`atm_flip_strike` of 870** says that on the front expiry, gamma only turns positive
**~6.1% above spot** — the two positive-GEX walls (875, 880) sit up there, and everything from
850 down is negative. **MU would have to rally ~6% before dealer hedging began damping rather
than amplifying moves.** Consistent with the 45-DTE `FULLY_NEGATIVE` read. *(The `role` labels
read counter-intuitively — 800 tagged `resistance_wall` while carrying negative GEX — so trust
the `gex` sign and the flip strike over the label string.)*

### Max pain — opex gravity

`uw options-structure max-pain --symbol MU --dte-max 30` (spot 819.60; **`caveat`: "Single-day
OI snapshot. Max pain assumes settlement at each candidate strike with current open interest
unchanged to expiry."**):

| expiry | DTE | **max_pain_strike** | **`distance_pct`** | put/call OI | total OI | holder value at max pain |
|---|---:|---:|---:|---:|---:|---:|
| 2026-07-29 | 1 | **880** | **+7.37%** | 1.172 | 75,353 | $40.9M |
| **2026-07-31** | **3** | **930** | **+13.47%** | **2.592** | **403,258** | **$279.8M** |
| 2026-08-03 | 6 | 930 | +13.47% | 1.195 | 14,111 | $10.5M |
| 2026-08-05 | 8 | 920 | +12.25% | 1.450 | 7,731 | $5.8M |
| 2026-08-07 | 10 | 925 | +12.86% | 2.551 | 116,591 | $60.7M |
| 2026-08-10 | 13 | 900 | +9.81% | 2.082 | 749 | $0.5M |
| 2026-08-14 | 17 | 925 | +12.86% | 1.693 | 41,489 | $28.3M |
| **2026-08-21** | **24** | **940** | **+14.69%** | 1.656 | 305,335 | **$725.6M** |

**Every near expiry's max pain is 7%–15% ABOVE spot** — the inverse of the bearish
configuration the composition guidance warns about ("max pain far below spot with a high
`put_call_oi_ratio` is a downward pull"). Here the put-heavy chain is **deep in the money**, so
the theoretical pin magnet points **up**, toward 930–940.

**How much weight to give it — not much, and here is why:**
1. **Distance destroys the magnet.** Max pain exerts real gravity when spot is *near* it. At
   13–15% away, this is mostly a statement that MU's OI was built when the stock was $900–1,200
   and has not yet repositioned lower.
2. **It will migrate down.** The tool's own caveat pins OI as static; in reality phase-3 already
   shows OI rebuilding at lower strikes (500P +11,767, 55P +24,412, 750/800 writes). Max pain
   should drift toward spot as the chain re-strikes.
3. **It contradicts the gamma read.** A short-gamma regime means dealers *chase* moves rather
   than pinning them. **Negative gamma and max-pain gravity are opposing forces, and in a
   `FULLY_NEGATIVE` regime gamma wins.**

**Cross-check against phase-3 (composition guidance requires it):** phase-3's OPEX cliff was
**2026-07-31 at 18.38% of total OI, put/call 2.592** — max pain names the **same expiry** as the
largest concentration, with the same P/C ratio (2.592) and total OI (403,258). **The two tools
agree exactly.** But phase-3's `oi-by-strike` wall map puts the heavy strikes at **800 (support)
and 900/1000 (resistance)**, whereas max pain says 930 — so **the pin candidate (930) sits above
phase-3's contested 900 battleground**, and MU failed `pin-risk` entirely. **Do not structure a
trade around a 7/31 pin.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --symbol MU --dte-max 45 --date 2026-07-28 --json` | **regime=`FULLY_NEGATIVE`**; total_gex=**-45,676,510**; **zero_gamma_level=`null`**; underlying=820.28 ← `.regime`, `.total_gex`, `.zero_gamma_level` | top-level |
| ″ | strike 800 net_gex=**-6,527,065**; 815=-4,133,679; 750=-3,851,698 ← `.per_strike[]` sorted by `-(.net_gex\|fabs)` | 50 strikes |
| `uw options-structure dex --symbol MU --dte-max 45 --date … --json` | **net_dex=-9,116,110,160**; call_dex=+4,813,155,896; put_dex=-13,929,266,057; interpretation="…dealer hedge is to SELL underlying." ← `.net_dex`, `.interpretation` | top-level |
| `uw options-structure vanna-charm --symbol MU --dte-max 45 --date … --json` | net_vanna=**+5,467**; put_vanna=+8,328; call_vanna=-2,861; net_charm=**-792,093**; vanna_interpretation="Classic vanna-squeeze setup if VIX collapses." | top-level |
| `uw options-structure iv-term-structure --symbol MU --date … --json` | **structure=`BACKWARDATION`**; expiry_count=24; kink_expiry=`null`; 7/31 avg_iv=1.5180 → 11/20 avg_iv=0.9203; **10/16=1.2188** ← `.structure`, `.term_structure[].avg_iv` | 24 expiries |
| `uw options-structure term-skew --symbol MU --dte-target 30 --date … --json` | **interpretation=`NORMAL`**; put_25d_iv=1.0051; call_25d_iv=0.9545; skew=0.0506; **skew_ratio=1.053**; dte_actual=31 | top-level |
| `uw options-structure front-end-iv-ratio --symbol MU --near-dte 7 --far-dte 30 --date … --json` | **regime=`BACKWARDATION`**; near_iv=1.1003 (8d); far_iv=1.0286 (31d); **ratio=1.07** | top-level |
| `uw options-structure today-gamma-flip --symbol MU --date … --json` | regime=`NEGATIVE`; **atm_flip_strike=870**; today_total_gex=-3,954,997; today_zero_gamma=`null`; walls 875/880 positive, 800/750/850 negative | 0DTE (7/29) |
| `uw options-structure max-pain --symbol MU --dte-max 30 --date … --json` | 7/31 → **max_pain_strike=930, distance_pct=13.47, pcoi=2.592, total_oi=403,258**; 8/21 → **940, +14.69%**; 7/29 → 880, +7.37% ← `.results[]` | 8 expiries |

## Tool errors

None — all nine `uw options-structure` commands exited 0 and every payload parsed.

## DATA NOTE / CORRECTION

Two field-path errors were caught and corrected **before** any value was written:

1. **`gex.per_strike` rows contain only `strike` and `net_gex`** — there are no `call_gex` /
   `put_gex` / `gex` fields. The first read used `.gex` and `jq` aborted with
   `null (null) number required`. Re-read against `.net_gex`; the per-strike table traces to
   that path. **No value was transcribed from the failed read.**
2. **`iv-term-structure.term_structure` rows use `avg_iv` / `dte_approx`**, not `iv` / `dte`.
   The first read printed `-` for every row. Re-read against `.avg_iv`. **`avg_iv` is an
   all-strike average, not ATM** — this is disclosed inline, and the ATM front-end figure cited
   for structural conclusions is `front-end-iv-ratio.near_iv = 1.1003`, not the 1.5180
   all-strike average.

Note also a small spot-reference spread across tools — `gex`/`dex`/`vanna-charm` report 820.28,
`today-gamma-flip` 820.21, `max-pain` 819.60, screener close 820.53. Sub-0.12% dispersion from
differing snapshot timestamps; immaterial to every conclusion, recorded for completeness.

## Verdict for downstream phases

- **Dealer regime: SHORT GAMMA — and not marginally.** `FULLY_NEGATIVE` with
  `zero_gamma_level = null` means **no long-gamma regime exists anywhere on the 45-DTE
  surface**; the 0DTE flip strike is 870, ~6.1% above spot. Dealers **buy rallies and sell
  dips**; realized vol stays expanded and trends extend. `net_dex` -$9.12B adds a standing
  mechanical **sell** lean.
- **Conviction: 4 / 5.** The GEX/DEX regime labels are the tool's own (not re-derived), they are
  internally consistent across three separate commands (`gex`, `today-gamma-flip`, `dex`), and
  they independently explain the realized behaviour phase-0.5 measured. Held below 5 because
  GEX sign conventions rest on a dealer-positioning assumption, and the vanna/charm and
  max-pain sub-signals point the other way.
- **Four structural levels for phase 9:**
  1. **$800 — THE pivot.** Largest negative GEX in the chain (**-6,527,065**, ~14% of total),
     and simultaneously phase-3's put wall (net -32,711), phase-2's heaviest distribution zone,
     and phase-1's written strike. **-2.5% from spot.** A sustained break here triggers maximum
     dealer amplification; holding it is the bulls' single requirement.
  2. **$750 — the second gamma shelf** (-3,851,698, third-largest) and phase-3's lower put wall
     (net -20,571), **-8.6% from spot**. The natural downside objective if 800 fails, and the
     level the short-put campaign is underwriting.
  3. **$870 — `atm_flip_strike`.** Where front-expiry gamma turns positive (+6.1%). **Above
     870, dealer hedging switches from amplifying to damping** — the level that would confirm a
     regime change rather than a bounce.
  4. **$930 (7/31) / $940 (8/21) — the max-pain magnets**, +13.5%/+14.7%. **Indicative only**
     — too distant to pin, opposed by negative gamma, and certain to migrate lower as OI
     re-strikes. Do NOT use as a target; note as the reason the chain has an upward tilt.
  *(There is no ZGL to quote — `zero_gamma_level = null` is itself the finding.)*
- **Open questions:**
  - **Which force wins — negative gamma (amplify down) or the vanna squeeze (mechanical bid if
    IV falls)?** They are directly opposed and both are live. The resolution hinges on
    **whether implied vol falls from here**, which hinges on the FOMC (7/28–29) and any
    memory-specific news. **→ phase-6 must date the vol catalysts; phase-8b must debate this
    explicitly — it is the crux of the trade.**
  - **Why is skew `NORMAL` (1.053) after an 8.85% drop?** Complacency (downside cheap and
    under-owned) or correct pricing of an orderly sector rotation? **→ phase-7c positioning
    gate, phase-8b.**
  - **Is the 2026-10-16 IV hump (1.2188 vs 0.9893 at 9/04 and 0.9203 at 11/20) confirming a
    ~2026-09-22 earnings event?** It is consistent, and it is the second independent hint
    (phase-3's Sep-18 OI concentration was the first). **→ phase-7b/7c must verify the
    earnings date.**
  - **What are the unexplained 8/07 (1.3592) and 8/14 (1.2554) IV humps?** No known catalyst.
    **→ phase-6 calendar.**
