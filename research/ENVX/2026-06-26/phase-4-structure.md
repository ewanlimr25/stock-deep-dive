# Phase 4 — Dealer Structure & Gamma

**Ticker:** ENVX
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T14:47:39Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

Dealer structure says **"$6 pin, not breakout."** At the tradeable 45-DTE horizon GEX is
**POSITIVE / long-gamma** (`zero_gamma_level $3.50` vs spot $5.88, total_gex +2.24M) —
dealers sell rallies and buy dips, **suppressing realized vol and capping the explosive
upside** the phase-1 $6-call thesis would need. Reinforcing the range, **July-OPEX
(2026-07-17) max pain is exactly $6** (0.59% from spot, P/C-OI 0.135) — the OI-gravity
magnet sits at the phase-1 sweep strike and phase-3 battleground (the three agree). The
bullish mechanical kicker: **DEX is net-short-call** (`call_dex +6.14M`, dealers short
calls → hedge is to BUY underlying, a structural bid). The offsetting risks: a **steep
front-end IV backwardation** (5d IV 164% vs 27d 93%, ratio 1.758 = near-term stress),
**complacent call skew** (25Δ call IV 98.9% > put IV 91.6% — no downside hedging priced,
a crowded-bull yellow flag), and a **negative vanna** setup where *falling* IV would force
dealers to sell their hedge. Net: structure **supports drift to/around $6 but resists a
clean break to $7** unless IV rises or spot forces dealers short-gamma below ~$5.5.

## Key signals

- **GEX POSITIVE / long-gamma**, ZGL **$3.50** vs spot $5.88, total_gex +2,243,902
  `[STRUCT:gex]` — "mean-reversion and reduced volatility" (tool's own regime). Caps the
  bull breakout. (Caveat: per-strike GEX mostly null — low liquidity, ZGL coarse ±2%.)
- **July-OPEX max pain = $6.00** (0.59% from spot, P/C-OI 0.135); July-10 also $6;
  06-26/07-02/07-24 pin $7 `[STRUCT:max_pain]` — gravity magnet at the $6 sweep strike.
- **DEX net-short-call**: `net_dex +181,902`, `call_dex +6,144,457` → "dealers net short
  calls → hedge is to BUY underlying" `[STRUCT:dex]` — a mechanical bid (mildly bullish).
- **Backwardation, steep front end**: near 5d IV 1.6413 vs far 27d IV 0.9334, ratio
  **1.758** `[STRUCT:front_end_iv_ratio, iv_term_structure]` — near-term vol stress (squeeze
  watch given 26% SI; no earnings until ~07-30).
- **Call skew, "COMPLACENT"**: 25Δ put IV 0.9158 < call IV 0.9894, skew_ratio 0.926
  `[STRUCT:term_skew]` — calls richer than puts, zero downside fear priced (contrarian flag).

## Detailed findings

### GEX — `[STRUCT:gex]`

`regime = POSITIVE` — "Dealers net long gamma — expect mean-reversion and reduced
volatility." `zero_gamma_level = 3.50`, `underlying_price 5.88`, `total_gex +2,243,902`.
Spot is **well above ZGL → long-gamma**. Per-strike GEX returns null at most strikes
(the tool's `note`: GEX is most meaningful for index/large-cap with deep OI), so the ZGL
is a coarse ±2% estimate — but the *sign/regime* (long-gamma, range-suppressing) is the
takeaway and it works against a fast directional move.

### DEX — `[STRUCT:dex]`

`net_dex +181,902` (small net), `call_dex +6,144,457`, `put_dex −5,962,556`. Interp:
"Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying."
Mechanically supportive — dealer short-call hedging is a standing bid under spot. Consistent
with phase-1 call buying and phase-3 call-owned chain.

### Vanna + charm — `[STRUCT:vanna_charm]`

`net_vanna −69` (~flat, slightly negative), `net_charm +47,033`. Interp: "call-heavy book…
**Falling IV → call delta drops → dealers cut long-underlying hedge → SELLING pressure.**
Rising IV reverses." **Key risk:** IV30d is elevated (87.9%) with no catalyst until ~07-30,
so an IV drift-down would trigger mechanical dealer selling — a headwind for the bull thesis.
Conversely an IV bid (squeeze/event) flips it to mechanical buying.

### IV term structure & front-end ratio — `[STRUCT:iv_term_structure, front_end_iv_ratio]`

`structure = BACKWARDATION` (11 expiries; per-expiry IV null = low liquidity). Front-end
ratio: **near 5d IV 164.1% vs far 27d IV 93.3%, ratio 1.758, regime BACKWARDATION.** Very
steep front — near-term vol stress. No earnings in 5 days (07-30), so this is either
small-cap/0DTE noise or **near-term move-risk pricing (squeeze potential, 26% SI)**. Flag for
phase-6/7c.

### Term skew (25Δ, ~27 DTE) — `[STRUCT:term_skew]`

`put_25d_iv 0.9158`, `call_25d_iv 0.9894`, `skew −0.0735`, `skew_ratio 0.926`,
`interpretation COMPLACENT`. **Calls are richer than puts** (reverse/call skew) — upside
demand, no tail-hedge bid. Confirms bullish positioning but "complacent" = **no fear priced
= crowded-long yellow flag** (phase-8b should weigh this against the bull case).

### Today's gamma flip (0DTE — after-hours, INDICATIVE only) — `[STRUCT:today_gamma_flip]`

`regime NEGATIVE`, `atm_flip 5.5`, `today_zero_gamma 5.07`, `today_total_gex −273,101`,
spot 5.88, expiry 2026-06-26 (now expired). Key 0DTE walls: **$6 resistance (gex −334,777)**,
$7.5 support (+153,347), $6.5/$7 resistance, $8 support. The expired 0DTE flagged $6 as a
short-gamma resistance — indicative of where intraday hedging fought, but **not tradeable
(0DTE expired)**. Useful nearer-flip reference: a break below **~$5.07–5.50 flips dealers
short-gamma → downside acceleration.**

### Max pain (opex gravity) — `[STRUCT:max_pain]`

| Expiry | Max pain | Dist from spot | P/C-OI | Note |
|--------|----------|----------------|--------|------|
| 2026-06-26 (0DTE) | $7 | +17.35% | 0.475 | expired |
| 2026-07-02 | $7 | +17.35% | 1.396 | |
| 2026-07-10 | $6 | +0.59% | 0.202 | |
| **2026-07-17 (OPEX cliff)** | **$6** | **+0.59%** | **0.135** | near-term magnet |
| 2026-07-24 | $7 | +17.35% | 0.158 | |

July-OPEX (the phase-3 cliff) max pain **$6** = pins at the sweep strike. Caveat (tool):
static-OI estimate; tomorrow's $6-Oct sweep OI will only *strengthen* the $6 magnet.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `uw options-structure gex --symbol ENVX --dte-max 45 --date 2026-06-26` | POSITIVE; ZGL 3.5 ← `.regime,.zero_gamma_level` | obj |
| `uw options-structure dex --symbol ENVX --dte-max 45 …` | net_dex +181,902; "BUY underlying" ← `.net_dex,.interpretation` | obj |
| `uw options-structure vanna-charm --symbol ENVX --dte-max 45 …` | net_vanna −69; falling-IV→sell ← `.vanna_interpretation` | obj |
| `uw options-structure iv-term-structure --symbol ENVX …` | BACKWARDATION ← `.structure` | 11 |
| `uw options-structure term-skew --symbol ENVX --dte-target 30 …` | COMPLACENT; ratio 0.926 ← `.interpretation,.skew_ratio` | obj |
| `uw options-structure front-end-iv-ratio --symbol ENVX --near-dte 7 --far-dte 30 …` | ratio 1.758 ← `.ratio,.regime` | obj |
| `uw options-structure today-gamma-flip --symbol ENVX …` | 0DTE NEGATIVE, $6 resist wall ← `.regime,.key_walls` | obj (indicative) |
| `uw options-structure max-pain --symbol ENVX --dte-max 30 …` | Jul-17 max pain $6 ← `.results[]|select(.expiry[:10]=="2026-07-17")` | 5 |

## Tool errors

<none — all reads round-tripped through jq>

## DATA NOTE / CORRECTION

- `gex.per_strike` and `iv_term_structure.term_structure[].iv` are mostly null (low
  single-name OI liquidity, per the tool's own note). Regime *labels* (`POSITIVE`,
  `BACKWARDATION`) are read verbatim from the tool's summary fields, not re-derived from
  the null per-strike arrays. ZGL treated as a coarse ±2% band.

## Verdict for downstream phases

- **Dealer regime:** **Long-gamma (range/pin-suppressing) at the tradeable horizon**, with
  a $6 max-pain magnet and a net-short-call DEX bid. Mechanically this **supports drift to/
  around $6 but resists a clean break to $7.** **Conviction 3/5** — structure is range-
  constructive around the sweep strike, not breakout-friendly.
- **Three structural levels for phase-9 (+ opex magnet):**
  1. **Max-pain $6.00 (July OPEX) = the opex-gravity magnet** — aligns with phase-1 sweep,
     phase-3 battleground; the price the chain pulls toward into 07-17.
  2. **$7 = overhead gravity/resistance** (later-expiry max pain $7 + phase-3 call wall) —
     the cap on the bull move; phase-2 DP supply $6.28–6.33 sits just under it.
  3. **Downside flip ~$5.07–5.50** (0DTE ZGL/atm_flip) — break below flips dealers
     short-gamma → downside acceleration; pair with phase-3 $5.5 put support / phase-2 $5.85.
- **Open questions:** Will an IV drift-down (no catalyst to 07-30) trigger the vanna
  selling headwind before the $6-Oct calls can work? Is the steep front-end backwardation
  squeeze-pricing (26% SI, phase-7c) or noise? Does "complacent" call skew mean the bull
  trade is already crowded (phase-8b)?
