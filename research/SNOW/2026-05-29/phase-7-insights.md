# Phase 7 — UW Insights Confluence

**Ticker:** SNOW · **As-of:** 2026-05-29 · **Generated:** 2026-05-29
**Upstream:** phases 1–6. Reconciles composites against the bottom-up read
(post-earnings distribution + parabolic/overbought + $255 gamma pin).

## Summary

The UW composites lean **cautious-to-bearish**, and one fires an outright
reversal warning: **`price-vs-flow` flags a DIVERGENCE — "price is up 77.5% but
options flow is bearish (net −$4.39M)"** `[INSIGHT:price-vs-flow]`. That is a
textbook leading-exhaustion signal — price at new highs, flow not confirming —
and it lines up exactly with phase-2 (mega-tier distribution), phase-1 (call
selling / put hedging), and phase-5 (RSI-87 parabolic). `conviction-matrix` is
**MIXED at just 0.6% confidence** (calls net sold: ask 63,744 vs bid 66,922; puts
net sold: ask 18,270 vs bid 31,666; DP balanced 0.494) `[INSIGHT:conviction-matrix]`,
`institutional-accumulation` is **NEUTRAL**, and SNOW is **absent from the bullish
signal-confluence board** (unlike a clean continuation name)
`[INSIGHT:signal-confluence]`. So the composite baseline is **not bullish** — it's
a mixed tape with an active bearish divergence on a massively-extended chart.

## Key signals

- **`price-vs-flow` DIVERGENCE (bearish)** — "price +77.5% but flow bearish, net
  −$4.39M," flow_direction bearish, period $133→$256 `[INSIGHT:price-vs-flow]`.
  Leading reversal/exhaustion signal — the standout finding.
- **`conviction-matrix` MIXED, 0.6% confidence** — calls net sold + puts net sold,
  DP balanced 0.494 `[INSIGHT:conviction-matrix]`. Essentially zero directional edge.
- **`institutional-accumulation` NEUTRAL** — balanced DP `[INSIGHT:institutional-accumulation]`
  (the *mega-tier* selling from phase-2 nets out against large-tier buying here).
- **Absent from bullish signal-confluence** `[INSIGHT:signal-confluence]` — SNOW
  does not present a bullish factor stack (contrast: a clean continuation name
  would score ≥3).

## Detailed findings

### Deep dive snapshot
- Whole-tape `uw_screener`: call premium $232.6M (ITM-0DTE-inflated, phase-1) vs
  put $28.3M; bullish $113.8M vs bearish $118.2M → **net slightly bearish**; P/C
  0.40; IV rank 51.5; implied move 0.55%/day (post-earnings crush); next earnings
  2026-08-26. DP $1.10B (phase-2). Short float 5.81% (phase-0).

### Signal confluence
SNOW **not present** on the bullish board (score < threshold even at min-score 1)
and not surfaced on the bearish board either — no clean factor stack in either
direction. Read against phase-1: the gross call activity is closing/ITM noise, so
the "bullish_flow" factor doesn't register as net-directional.

### Conviction matrix
**MIXED**, **0.6%** confidence. Both calls and puts net sold; DP 0.494. No bias.

### Price vs flow
**DIVERGENCE = true** — the only composite with a strong signal, and it is
**bearish/reversal**: price up 77.5% (period $133.02 → $256.18) while net options
flow is bearish (−$4.39M). Pair with phase-4 long-gamma mean-reversion → a fade /
consolidation setup, not continuation. *Caveat:* divergence signals are often
early; phase-4 says the immediate mechanic is a $255 pin, not a crash.

### Analyst vs flow / Institutional accumulation
Institutional accumulation NEUTRAL. (Analyst view deferred to 7b/7c — HSBC
upgrade noted in phase-0 news.)

### Earnings play
Out of window (earnings 2026-05-27 passed; next 2026-08-26). Skipped.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| `insights conviction-matrix` | `--symbol SNOW` | MIXED, 0.6% |
| `insights price-vs-flow` | `--lookback-days 30` | **DIVERGENCE bearish** |
| `insights institutional-accumulation` | `--symbol SNOW` | NEUTRAL |
| `insights signal-confluence` | bull/bear `--min-score 1 --top-n 100` | SNOW absent both |

## Tool errors
(none)

## Cross-check vs phases 1–6
| UW insight | Phase agreement? | Notes |
|---|---|---|
| price-vs-flow DIVERGENCE | **agrees** phases 1,2,5 | Confirms distribution + overbought exhaustion |
| conviction-matrix MIXED 0.6% | **agrees** phase-1 | Net-balanced/cautious tape |
| institutional-accumulation NEUTRAL | **agrees** phase-2 | Mega-tier sell nets vs large-tier buy |
| absent from bullish confluence | **agrees** phase-1/5 | No clean continuation stack |

## Verdict for downstream

- **UW composite bias: MIXED with an active BEARISH DIVERGENCE** — not bullish.
  The weight of the composites (divergence + MIXED 0.6% + NEUTRAL accumulation +
  no bullish confluence) says **fade/consolidate the parabolic move**, not chase it.
- **Conviction: 2 / 5** (and the directional sign tilts mildly *bearish/range*,
  not long).
- **Baseline for phase-9:** treat SNOW as a **low-conviction range-to-fade** at
  the $250–$255 pin (phase-4) — the post-earnings pop is being distributed
  (phase-2) into an overbought chart (phase-5) with flow not confirming the highs
  (this phase). A long is only defensible as a *defined-risk pullback* entry, not
  a chase. Override toward outright fade only if 7b shows valuation stretched /
  7c shows crowded-long.
- **Open questions:**
  - Is the +52–77% run fundamentally justified (phase-7b) or is valuation now the
    binding constraint (adds to fade case)?
  - Is the crowd / retail euphoric and long into the mega-tier distribution
    (phase-7c)? If so, the divergence sharpens toward a fade.
