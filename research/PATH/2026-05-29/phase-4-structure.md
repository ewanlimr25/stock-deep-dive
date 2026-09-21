# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phase-3-positioning.md ("is the June $12–$15 call OI dealer-short
/ squeeze fuel?") · phase-2-dark-pool.md ($12 supply, $11.2–$11.8 support) ·
phase-1-flow.md (LEAP call lean)

## Summary

Dealers are **net long gamma (positive GEX +$28.6M)** with the **Zero Gamma
Level at $7.90**, far below spot $11.71 — a **long-gamma, mean-reverting regime**
that *suppresses* volatility and caps directional follow-through near term. The
gamma profile is decisive: a **massive positive gamma wall at $12 (+$11.4M, the
single largest strike)**, reinforced at $11.5 (+$9.4M) and $13 (+$5.6M), but
**negative gamma below $11** (−$3.6M at $11, turning more negative toward $9–$10).
So **$11 is the pivot**: above it dealers sell rallies into a $12 magnet
(boxed/mean-reverting); below it the regime flips short-gamma and moves
*amplify* downward toward the $9–$10 put shelf. DEX is **+$58.9M — dealers are
net short calls and must BUY underlying to hedge** (a standing supportive bid),
which directly answers phase-3: the June call OI *is* dealer-short, i.e. genuine
**squeeze fuel** — but the positive-gamma wall means that fuel only ignites on a
decisive break through $12–$13. Term structure is benign: **contango**,
**complacent** skew (0.865), no event stress (no earnings until Sep).

## Key signals

- **Positive GEX / long-gamma regime** — total +$28.6M, ZGL $7.90 vs spot $11.71;
  "dealers net long gamma → mean-reversion, reduced vol" `[STRUCT:gex]`. Caps the
  near-term range.
- **$12 = largest positive gamma wall** (+$11.4M), with $11.5 (+$9.4M) and $13
  (+$5.6M) `[STRUCT:gex]` — a strong upside magnet/cap; dealers sell rallies into
  it. Matches phase-2 $12 DP supply and phase-3 $12 call OI.
- **$11 = gamma pivot** — GEX flips negative below $11 (−$3.6M at $11, −$1.0M at
  $10.5) `[STRUCT:gex]`. A break under $11 → short-gamma acceleration toward the
  $9–$10 put strikes.
- **Dealers net short calls, hedge = BUY underlying** — DEX +$58.9M
  `[STRUCT:dex]`. Standing dealer bid *and* the squeeze-fuel phase-3 asked about:
  a push through $13 forces dealer call-hedge buying on top of 31% short cover.
- **No event stress** — IV term structure **CONTANGO**, skew **COMPLACENT**
  (0.865, puts *not* bid for protection), front-end ratio 1.16
  `[STRUCT:iv-term-structure][STRUCT:term-skew]`. Vol is not pricing a catalyst.

## Detailed findings

### GEX (per-strike, dte≤45)
| Strike | GEX ($) | Read |
|---|---|---|
| 13 | +5,626,685 | upper positive wall |
| **12** | **+11,354,085** | **largest wall — upside cap / magnet** |
| 12.5 | +3,265,475 | wall |
| 11.5 | +9,397,781 | wall (just below spot) |
| 11 | −3,559,037 | **flip to negative — pivot** |
| 10.5 | −1,040,457 | short-gamma |
| 10 | −588,356 | short-gamma |
| 9 / 9.5 | −425K / −396K | short-gamma (toward put shelf) |
- Total GEX +$28.6M, regime **POSITIVE**, ZGL **$7.90**, spot **$11.71**.
- Read: boxed $11–$12.5 by long gamma; downside air below $11.

### DEX
Net DEX **+$58.9M**. Interpretation (verbatim): *"Public is net call-long →
dealers net short calls → dealer hedge is to BUY underlying."* Supportive bid at
spot; convex squeeze risk above $13.

### Vanna + charm
Vanna −2,188 (negligible), charm **+103,645** (positive — mild time-decay tailwind
to spot as OTM calls bleed). **No squeeze signal flagged** by the tool — the
convexity is latent, not active.

### IV term structure
**CONTANGO** — 0DTE 23.1% (expiring, ignore), 7DTE 86.3%, then settling
74–79% out to 2028. Normal upward/flat curve; no backwardation → no priced
catalyst (consistent with Sep earnings).

### Term skew / front-end
- Term skew ratio **0.865 → COMPLACENT** (25Δ puts cheaper than the
  call-richness baseline; little tail-hedging demand priced).
- Front-end IV ratio **1.16** (7d vs 30d) — front mildly elevated, not a stress
  reading.

### Today's gamma flip
Skipped — EOD/after-hours as-of run; `today-gamma-flip` is intraday-0DTE only.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `options-structure gex` | `--symbol PATH --dte-max 45` | +$28.6M, ZGL $7.90, $12 wall |
| `options-structure dex` | `--symbol PATH --dte-max 45` | +$58.9M, dealers short calls |
| `options-structure vanna-charm` | `--symbol PATH --dte-max 45` | vanna −2188, charm +103645 |
| `options-structure iv-term-structure` | `--symbol PATH` | CONTANGO |
| `options-structure term-skew` | `--dte-target 30` | 0.865 COMPLACENT |
| `options-structure front-end-iv-ratio` | `--near-dte 7 --far-dte 30` | 1.16 |

## Tool errors
(none — `today-gamma-flip` intentionally skipped, after-hours.)

## Verdict for downstream

- **Dealer regime: LONG GAMMA above $11 (mean-reverting, vol-suppressed),
  flipping SHORT GAMMA below $11 (trend-amplifying down).** Near-term the stock
  is structurally **boxed $11–$12.5** with a hard cap at the $12 wall.
- **Conviction: 4 / 5** — clean, deep-OI GEX/DEX read (despite the small-cap
  caveat in the tool note). The structure is the clearest signal in the chain so
  far and it argues **range, not breakout — unless $13 gives way.**
- **Three structural levels for phase-9:**
  1. **ZGL $7.90** — regime floor (well below; not a near-term level but the
     short-gamma cascade target if $11 breaks is the $9–$10 shelf, not ZGL).
  2. **$12 — largest gamma wall / upside cap & magnet.** Primary resistance;
     a *close* above $13 is the squeeze trigger (dealer call-hedge buying + 31%
     short cover).
  3. **$11 — gamma pivot / regime flip.** The line between mean-reversion (above)
     and downside acceleration (below). Aligns with phase-2's $11.2 support.
- **Open questions:**
  - The setup is *convex*: capped near term, explosive if $13 breaks given 31%
    short float + dealers short calls. Phase-7c short-interest trend decides
    whether the squeeze is loading or unwinding.
  - Complacent skew + 31% short float = cheap downside optionality; does phase-8b
    bear case favour owning puts over shorting stock?
