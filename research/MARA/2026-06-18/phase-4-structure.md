# Phase 4 — Dealer Structure & Gamma

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer structure is **unambiguously long-gamma / range-bound** and every vol
metric is **calm — no event stress.** GEX regime is **POSITIVE** (`zero_gamma_level
$5.26`, spot $14.24 sits *far above* it → dealers buy dips / sell rallies, suppressed
realized vol), and the gamma concentration is a **wall at $14.5 (peak net_gex
+$36.4M) and $15 (+$24.2M)** — the same $14.5 strike that is phase-1's overwrite
strike and phase-3's call wall: **triple confluence pinning/capping price at
$14.5–$15.** Near-term max-pain gravity is **$14** (6/26). Term structure is CONTANGO,
skew NORMAL, front-end IV FLAT → no catalyst stress (earnings 8/4 is far). The
structure **favors premium sellers** and a **mean-reverting $14–$14.5 range**, not a
directional breakout. One mechanical caveat (vanna): if IV drifts *down* from here,
dealers cut their long-underlying hedge → a mild **selling** drift.

## Key signals

- **POSITIVE GEX / long-gamma**, ZGL **$5.26** ≪ spot $14.24, total_gex +$87.2M →
  mean-reversion, vol suppression `[STRUCT:gex]`.
- **Peak gamma wall at $14.5 (+$36.4M net_gex)** then $15 (+$24.2M) — dealer pin/cap
  exactly at the overwrite strike `[STRUCT:gex]`.
- **Max-pain magnet $14** for 6/26 (−1.7%), $14.5 for 7/2 — gravity just below spot,
  under the call wall `[STRUCT:max-pain]`.
- **DEX net +$175.8M, dealers net short calls → buy-to-hedge** = supportive bid
  underneath `[STRUCT:dex]`.
- Term structure **CONTANGO**, skew **NORMAL** (ratio 1.02), front-IV **FLAT** (ratio
  1.032) → **no event stress, no tail-hedge demand** `[STRUCT:iv-term-structure / term-skew / front-end-iv-ratio]`.

## Detailed findings

### GEX (gamma)

- `regime` = **POSITIVE** — "Dealers net long gamma — expect mean-reversion and
  reduced volatility." `zero_gamma_level` **$5.26**; `underlying_price` $14.09;
  `total_gex` **+87,232,983**; `dte_max` 45.
- Spot is ~$9 / ~170% above ZGL → **deeply, stably long-gamma**. A gamma flip would
  require a collapse toward ~$5 (not a near-term risk). Peak strikes:

| Strike | net_gex |
|--------|---------|
| **$14.5** | **+36,449,393** |
| **$15** | **+24,162,934** |
| $16 | +9,383,124 |
| $14 | +7,166,783 |
| $15.5 | +5,202,316 |

The gamma "ceiling" sits at **$14.5/$15** — dealers sell strength into it, reinforcing
the cap. Spot $14.24 rests at the foot of the $14.5 wall.

### DEX (dealer delta)

- `net_dex` **+175,797,088** (call_dex +230.7M, put_dex −54.9M). Interpretation
  (verbatim): *"Public is net call-long → dealers net short calls → dealer hedge is
  to BUY underlying."* → standing book gives dealers a **long-underlying hedge =
  supportive bid** beneath spot. (This is the *standing* book, not today's flow.)

### Vanna + charm

- `net_vanna` **−2,553** (negative — call-heavy public book), `net_charm` +82,124.
- Interpretation (verbatim): *"Falling IV → call delta drops → dealers (short calls)
  cut long-underlying hedge → SELLING pressure. Rising IV reverses."* → With IV rank
  only ~30 and a calm long-gamma tape, a further IV *drift-down* would impose a **mild
  mechanical sell drift** — a headwind to any upside, supportive of the capped/range read.

### IV term structure

- `structure` = **CONTANGO** (front IV < back IV; normal upward slope), `expiry_count`
  17, no kink. **No backwardation → no near-term event stress.** (Per-expiry IV
  values returned null in this build — the regime label is authoritative; recorded
  under Tool errors.)

### Term skew (25Δ)

- `interpretation` = **NORMAL**. put_25d_iv 0.8216 vs call_25d_iv 0.8053,
  `skew_ratio` **1.02**, skew +0.0163 (dte_actual 28). Puts only *marginally* richer
  than calls → **no tail-hedging surge, no risk-off skew steepening.**

### Front-end IV ratio (event stress)

- `regime` = **FLAT**. near_iv 0.9031 (7DTE) / far_iv 0.8749 (28DTE), `ratio` **1.032**
  — front only trivially elevated. **No catalyst priced in the next week.**

### Today's gamma flip (0DTE — historical EOD snapshot, de-rated)

- 6/18 0DTE: `regime` POSITIVE, `today_zero_gamma` $5.25, `atm_flip_strike` $6,
  `today_total_gex` +78.2M, spot $14.12. Confirms the **expiring** 0DTE was a
  positive-gamma pin into the close. **This is an as-of EOD run, not live intraday**
  — the 6/18 0DTE has expired; treat as confirmation of the pin regime, not a
  tradeable forward signal.

### Max pain (opex gravity)

| Expiry | DTE | max_pain | dist from $14.24 | P/C-OI |
|--------|-----|----------|------------------|--------|
| 2026-06-18 | 0 | $12 | −15.7% | 0.19 (static-OI artifact; expiring) |
| **2026-06-26** | 8 | **$14** | **−1.7%** | 1.21 |
| 2026-07-02 | 14 | $14.5 | +1.8% | 0.73 |
| 2026-07-10 | 22 | $14 | −1.7% | 0.93 |
| 2026-07-17 | 29 | $13 | −8.7% | 0.41 |

Near-term gravity clusters at **$14** (6/26, 7/10), i.e. just below spot and **below
the $14.5 cap** — agrees with phase-3's $14.5/$15 walls and $14 `call_heavy`
battleground. The 6/18 $12 reading is the static-OI caveat firing on the expiring
0DTE; discount it.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `options-structure gex --symbol MARA --dte-max 45 --date 2026-06-18` | regime POSITIVE, ZGL 5.26, peak $14.5 +36.4M ← `.regime,.zero_gamma_level,.per_strike[].net_gex` | per-strike |
| `options-structure dex --symbol MARA --dte-max 45` | net_dex +175.8M, dealers buy-to-hedge ← `.net_dex,.interpretation` | 1 |
| `options-structure vanna-charm --symbol MARA --dte-max 45` | net_vanna −2,553; falling-IV→sell ← `.net_vanna,.vanna_interpretation` | 1 |
| `options-structure iv-term-structure --symbol MARA` | CONTANGO ← `.structure` | 17 |
| `options-structure term-skew --symbol MARA --dte-target 30` | NORMAL, ratio 1.02 ← `.interpretation,.skew_ratio` | 1 |
| `options-structure front-end-iv-ratio --symbol MARA --near-dte 7 --far-dte 30` | FLAT, ratio 1.032 ← `.regime,.ratio` | 1 |
| `options-structure today-gamma-flip --symbol MARA` | POSITIVE, ZGL 5.25 (0DTE/historical) ← `.regime` | 1 |
| `options-structure max-pain --symbol MARA --dte-max 30` | 6/26 max_pain $14 ← `.results[].max_pain_strike` | 5 |

## Tool errors

- `iv-term-structure`: `.term_structure[].iv`/`.dte` returned **null** per row (this
  build doesn't populate per-expiry IV in that array), though the top-level
  `structure=CONTANGO` regime label is present and used. No number transcribed from
  the null rows.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA / POSITIVE** (spot ≫ ZGL $5.26). Strong
  mean-reversion, suppressed realized vol → a **range-bound pin environment**, not a
  trend-amplifying short-gamma setup. Calm vol structure (contango / normal skew /
  flat front-end), no catalyst stress.
- **Conviction:** **3/5** — the long-gamma + gamma-wall + max-pain + calm-vol reads
  are mutually consistent and point one direction (range/pin); high internal coherence.
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **$14.5** — peak gamma wall (+$36.4M) = upside cap/pin (triple-confluence with
     phase-1 overwrite strike + phase-3 call wall).
  2. **$15** — secondary gamma wall (+$24.2M) = hard ceiling.
  3. **$14** — **6/26 max-pain magnet** + max-pain gravity (the opex pin to fade toward).
     ZGL $5.26 noted as the (distant) long-gamma flip floor.
- **Open questions:**
  - Structure favors **premium sellers / range-fade**; does phase-5 historical show
    MARA actually mean-reverts in long-gamma regimes, or does its 5.35 beta let it
    break pins on a BTC move? (The gamma pin holds only absent a large BTC catalyst.)
  - Vanna says **falling IV → dealer selling**; with IV rank ~30, is there room for
    IV to keep bleeding (→ mild downward drift) or is it near a floor?
