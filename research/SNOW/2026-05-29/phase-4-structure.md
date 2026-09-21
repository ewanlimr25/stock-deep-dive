# Phase 4 — Dealer Structure & Gamma

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-3-positioning.md ("pin near $255 or push to $280 call wall?")
· phase-2-dark-pool.md ($255–$256 distribution zone) · phase-1 (cautious)

## Summary

Dealers are **firmly long gamma (positive GEX +$35.2M)** with the Zero Gamma
Level at **$149.78**, ~$104 below spot $253.39 — a deep **long-gamma,
mean-reverting, vol-suppressed regime**. The decisive feature: the two largest
gamma walls **straddle spot — $255 (+$9.1M) and $250 (+$7.2M)** `[STRUCT:gex]` —
so SNOW is **pinned in a $250–$255 band**, with dealers selling rallies and
buying dips. Crucially, the **$255 wall coincides exactly with phase-2's
mega-tier distribution zone** (the $255.55 closing blocks): both dealer gamma and
institutional supply cap the post-earnings pop right here. Above $255 gamma thins
fast ($260 +$3.3M, then negligible), so a push toward phase-3's $280–$300 call OI
would have to *overcome* the $255–$260 pin first. DEX is enormous (**+$3.63B**,
dealers net short calls → standing buy-to-hedge bid), but in a positive-gamma
regime that bid sells strength rather than chasing it. Term structure is in
**BACKWARDATION** with front-end IV ratio 1.24 — residual post-earnings vol (the
print was 2 days ago, 5/27) still rich at the front and decaying; skew is
**COMPLACENT** (0.972).

## Key signals

- **Long-gamma regime, positive GEX +$35.2M, ZGL $149.78 << spot** `[STRUCT:gex]`
  — mean-reversion, suppressed realized vol; structurally caps the move.
- **$255 + $250 gamma walls straddle spot** — $255 +$9.1M (largest), $250 +$7.2M
  `[STRUCT:gex]`: SNOW is **pinned $250–$255**. $255 = phase-2 distribution zone.
- **Above $255 gamma thins** — $260 +$3.3M, $270/$280 ~+$1.1M `[STRUCT:gex]`: no
  strong wall to magnet price up; the $280–$300 OI (phase-3) is far and unbacked
  by near-term gamma.
- **DEX +$3.63B, dealers short calls → buy-to-hedge bid** `[STRUCT:dex]`: a large
  standing bid that *sells rallies* in this positive-gamma regime (supportive on
  dips, capping on pops).
- **Backwardation + complacent skew** — front IV elevated (ratio 1.24), residual
  post-earnings; puts not bid `[STRUCT:iv-term-structure][STRUCT:term-skew]`.
  Favours **selling rich front premium**.

## Detailed findings

### GEX (per-strike near spot, dte≤45)
| Strike | net GEX ($) | Read |
|---|---|---|
| 280 | +1,088,544 | thin upper |
| 270 | +1,072,112 | thin |
| 260 | +3,267,220 | minor wall |
| 257.5 | +1,402,782 | — |
| **255** | **+9,105,741** | **largest wall — cap/pin** |
| 252.5 | +1,135,650 | — |
| **250** | **+7,168,083** | **2nd wall — floor of the pin** |
| 247.5 | +490,304 | — |
- Total GEX +$35.2M, regime **POSITIVE**, ZGL **$149.78**, spot **$253.39**.
- Read: **boxed $250–$255**; upside above $255 is un-walled (would need to clear
  the pin to reach the $280–$300 OI).

### DEX
Net DEX **+$3.63B**; "public net call-long → dealers net short calls → hedge is
to BUY underlying." Large supportive bid, but positive-gamma → sells rallies.

### Vanna + charm
Vanna −3,842 (negligible at scale), charm **+69,389** (positive, mild time-decay
drift support). **No squeeze signal** — convexity is latent.

### IV term structure / skew
**BACKWARDATION** (front > back), front-end IV ratio **1.24** — residual
post-earnings (5/27) front vol, decaying; *not* a fresh event signal (>24h past
earnings, per rubric). Skew **0.972 COMPLACENT** — no tail-hedging bid. Net:
**front premium is rich → favour selling it** (aligns with phase-5 VRP).

### Today's gamma flip
Skipped — EOD/after-hours as-of run.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `options-structure gex` | `--dte-max 45` | +$35.2M, ZGL $149.78, $255/$250 walls |
| `options-structure dex` | `--dte-max 45` | +$3.63B, dealers short calls |
| `options-structure vanna-charm` | `--dte-max 45` | vanna −3842, charm +69389 |
| `options-structure iv-term-structure` | — | BACKWARDATION |
| `options-structure term-skew` | `--dte-target 30` | 0.972 COMPLACENT |
| `options-structure front-end-iv-ratio` | `--near-dte 7 --far-dte 30` | 1.24 |

## Tool errors
(none — `gex` per-strike `call_gex`/`put_gex` null; used `net_gex`. After-hours,
`today-gamma-flip` skipped.)

## Verdict for downstream

- **Dealer regime: LONG GAMMA, pinned $250–$255 (mean-reverting, vol-suppressed).**
  The $255 wall + phase-2 distribution + the post-earnings IV crush all say the
  move **consolidates/caps near $255** near term, not breaks out.
- **Conviction: 4 / 5** — clean, deep-OI mega-cap GEX read; the pin is the most
  reliable signal in the chain.
- **Three structural levels for phase-9:**
  1. **$255 — largest gamma wall / cap (= phase-2 distribution).** Resistance/pin.
  2. **$250 — second wall / floor of the pin.** Support.
  3. **$260 then air to $280** — a *sustained* break >$255–$260 un-pins toward the
     $280–$300 OI (phase-3), but there's no near-term gamma to pull it there.
  - ZGL $149.78 is far below — no realistic downside-cascade level near term.
- **Open questions:**
  - The structure says *range/pin $250–$255*; phases 1–2 say *distribution*;
    phase-3 says *some bet on $280+*. Net: consolidation with a slight fade risk
    unless $260 clears. Phase-8b debate to settle continuation-vs-fade.
  - Backwardation + complacent skew + VRP → premium-selling structures favored.
