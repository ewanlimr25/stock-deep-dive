# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH · **As-of:** 2026-07-22 · **Spot:** $10.57 (structure engine) · **Generated:** 2026-07-22
**Upstream:** phase-3-positioning.md (LEAP call-dominant chain, $12 wall, 8/21 cliff), phase-1-flow.md (7/24 event, IV kink)

## Summary

Dealers are **net LONG gamma (POSITIVE regime)** with the Zero-Gamma Level at **$6.92**,
far below spot $10.57 — a **mean-reversion / suppressed-vol, range-bound** regime
(dealers sell rallies, buy dips). DEX is **+1.72M with dealers net SHORT calls, so
their hedge is to BUY the underlying** — a mechanical bid. Max-pain gravity sits
**above spot at $11–$11.5**, giving a mild upward pull. **But the bid is
event-contingent:** the book is call-heavy with slightly negative net vanna, and the
tool's own read is that **falling IV → dealers cut their long-underlying hedge →
selling pressure** — so the **post-7/24 IV crush (term structure is in BACKWARDATION,
near 9d IV 82.8% > far 30d 74.0%) risks flipping the dealer bid into mechanical
selling.** Skew is **COMPLACENT** (25Δ calls richer than puts, ratio 0.919) — little
downside tail is priced despite today's net-bearish flow.

## Key signals

- **POSITIVE gamma regime, ZGL $6.92 vs spot $10.57** — long-gamma, mean-reverting, range-bound; only a ~35% crash flips the regime `[STRUCT:gex]`.
- **DEX +1.72M, dealers net short calls → mechanical BUY-underlying hedge** — structural bid `[STRUCT:dex]`.
- **Max-pain magnet $11–$11.5 (above spot)** — $11.5 for 7/24–8/14, **$11 for the heavy 8/21 cliff** (2.76% above) `[STRUCT:max_pain]`.
- **IV term structure BACKWARDATION** (front 9d 82.8% > 30d 74.0%, ratio 1.119) — event stress confirming the 7/24 catalyst `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`.
- **Vanna warning: post-event IV crush → dealer de-hedge → SELLING pressure** (net_vanna −225, call-heavy book) `[STRUCT:vanna_charm]`.
- **Skew COMPLACENT** — put_25Δ 67.6% < call_25Δ 73.5% (ratio 0.919); minimal downside hedging demand `[STRUCT:term_skew]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- regime **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced volatility" (tool's own label, quoted verbatim).
- zero_gamma_level **$6.92**; total_gex **+3,823,249**; underlying $10.57.
- Spot sits ~53% above ZGL → firmly long-gamma. Implication: intraday moves get faded, realized vol suppressed, price gravitates to the OI pin — **unless the 7/24 event overwhelms the pin.**

### DEX `[STRUCT:dex]`

- net_dex **+1,716,345**; call_dex/put_dex split with public net call-long.
- Interpretation (verbatim): *"Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying."* A mechanical bid — consistent with the standing LEAP call dominance (phase-3) and the persistent bullish sweep campaign (phase-1).

### Vanna + charm `[STRUCT:vanna_charm]`

- net_vanna **−225** (call-heavy book), net_charm **+131,238**, no explicit squeeze signal.
- Interpretation (verbatim): *"Public net vanna negative (call-heavy book). Falling IV → call delta drops → dealers (short calls) cut long-underlying hedge → SELLING pressure. Rising IV reverses."*
- **Trade-relevant:** the front IV is elevated for 7/24; once that event passes, IV mean-reverts/crushes → the DEX bid mechanically **unwinds into selling**. The dealer support is therefore *pre-event*, and a **post-event air-pocket is the structural risk.**

### IV term structure `[STRUCT:iv_term_structure]`

- structure **BACKWARDATION** — front-month IV above back-month = event stress. Corroborates phase-1's 7/24 IV kink. Do not treat backwardation as a durable short-vol signal; it normalizes once 7/24 clears.

### Term skew `[STRUCT:term_skew]` (30d)

- put_25Δ_iv 67.6% vs call_25Δ_iv 73.5%; skew −0.059; skew_ratio **0.919**; interpretation **COMPLACENT**.
- Calls are *richer* than puts — the surface prices upside over downside, minimal tail-hedge bid. A mild **contrarian yellow flag** (complacency into an event) but also confirms the structural call bias. Phase-7c/8b should weigh whether complacency is warranted.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

- near (9d) 82.8% / far (30d) 74.0% → **ratio 1.119**, regime BACKWARDATION. Event stress present but **modest** (not a >1.3 blow-off) — market prices a real but not extreme 7/24 move (implied ~4.7%, phase-0.5).

### Today's gamma flip

Skipped — `today-gamma-flip` is 0DTE/intraday-only and this is an after-hours as-of
run; not meaningful. (Regime read from the `gex` surface above.)

### Max pain `[STRUCT:max_pain]` (dte-max 30, static-OI)

| expiry | max-pain strike | dist from spot |
|---|---|---|
| 2026-07-24 | $11.5 | +7.43% |
| 2026-07-31 | $11.5 | +7.43% |
| 2026-08-07 | $11.5 | +7.43% |
| 2026-08-14 | $11.5 | +7.43% |
| **2026-08-21** | **$11** | **+2.76%** |

All magnets are **above spot** — mild upward opex-gravity. The most reliable is the
**8/21 $11** (the 16.2%-of-OI cliff from phase-3, nearest to spot). Caveat (tool's
own): static-OI snapshot, assumes OI unchanged to expiry — softer the further out.
Cross-checks phase-3: $11 pin agrees with the $11 two-sided battleground; $12 remains
the wall above.

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| GEX regime/ZGL | `uw options-structure gex --symbol PATH --dte-max 45 --date 2026-07-22 --json` | `.{regime,regime_description,zero_gamma_level,total_gex,underlying_price}` |
| DEX | `uw options-structure dex --symbol PATH --dte-max 45 --date 2026-07-22 --json` | `.{net_dex,interpretation}` |
| vanna/charm | `uw options-structure vanna-charm --symbol PATH --dte-max 45 --date 2026-07-22 --json` | `.{net_vanna,net_charm,vanna_interpretation}` |
| IV term | `uw options-structure iv-term-structure --symbol PATH --date 2026-07-22 --json` | `.structure` |
| skew | `uw options-structure term-skew --symbol PATH --dte-target 30 --date 2026-07-22 --json` | `.{put_25d_iv,call_25d_iv,skew_ratio,interpretation}` |
| front-end | `uw options-structure front-end-iv-ratio --symbol PATH --near-dte 7 --far-dte 30 --date 2026-07-22 --json` | `.{ratio,near_iv,far_iv,regime}` |
| max pain | `uw options-structure max-pain --symbol PATH --dte-max 30 --date 2026-07-22 --json` | `.results[].{expiry,max_pain_strike,distance_pct}` |

## Tool errors

<none>

## Verdict for downstream

- **Dealer regime: LONG GAMMA (positive), range-bound / mean-reverting, with an event-contingent mechanical BID (DEX) that risks flipping to SELLING on the post-7/24 IV crush (vanna).**
- **Conviction: 3/5.** GEX + DEX + max-pain agree on a mild upward pin toward $11–$11.5 pre-event; the vanna/IV-crush air-pocket is the key caveat, and complacent skew tempers conviction.
- **Structural levels for phase-9:**
  1. **ZGL $6.92** — regime-flip level; only a catastrophic break turns dealers short-gamma. Effectively a distant floor for "vol expansion" risk.
  2. **Max-pain / pin $11 (8/21 cliff) → $11.5 (7/24)** — the near opex magnet and upside gravity, capped by the **$12 call wall** (phase-3) and **$11.90–12.00 dark-pool supply** (phase-2). This $11.5–$12 zone is the ceiling.
  3. **Vanna pivot: post-7/24 IV crush** — expect mechanical dealer de-hedging/selling once the event clears; a rally into 7/24 that fails to reclaim $12 is structurally vulnerable to a fade.
- **Open questions:**
  - Does the 7/24 event resolve up (through $11.5→$12) or down (toward the $10 put wall), and is the DEX bid strong enough to hold $10.5 into it? → phase-5 base rates, phase-6 catalyst.
  - Is complacent skew justified, or is the market under-pricing a 7/24 downside gap? → phase-7c positioning, phase-8b debate.
