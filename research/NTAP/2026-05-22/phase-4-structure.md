# Phase 4 — Dealer Structure & Gamma

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **net long gamma** (GEX +1.57M, regime POSITIVE) with spot **$139.37
far above the Zero Gamma Level $115.41** — a mean-reverting, vol-suppressing,
**pinning** regime into the print, with the heaviest gamma walls at **125 (+488K)
and 145 (+392K)**. The 145 wall is the same strike phase-1 flagged as a call
overwrite and phase-3 as the largest fresh-traded strike → a genuine dealer **cap**.
DEX is **+84.4M** (public call-long, dealers short calls, hedge = buy underlying) —
a mild mechanical bid that likely explains part of phase-2's suggestive DP buying
rather than pure conviction. The term structure is in **BACKWARDATION** (6/18 IV
60.2% vs 48.3% next) confirming earnings stress, and skew is **COMPLACENT** (calls
richer than puts). The decisive structural fact for phase-9: **negative vanna +
IV rank 100 means the post-5/28 vol crush will force dealer de-hedge SELLING** — a
headwind for any long-delta position carried through the event.

## Key signals

- **Long-gamma regime:** GEX +1,574,300 POSITIVE, spot $139.37 ≫ ZGL **$115.41**
  → mean-reversion + pinning pre-earnings [STRUCT:gex]
- **Gamma walls 125 (+488K) & 145 (+392K)** bracket spot — 145 = upside cap (the
  overwrite strike), 125 = lower magnet [STRUCT:gex]
- **DEX +84.4M:** dealers short calls → hedge BUYS underlying = mild mechanical
  bid (de-rates phase-2 "accumulation" toward "dealer hedging") [STRUCT:dex]
- **BACKWARDATION:** front 6/18 60.2% IV vs 7/17 48.3% — earnings priced in the
  near month [STRUCT:iv_term_structure]
- **COMPLACENT skew:** 25Δ call IV 61.5% > put IV 55.6% (skew_ratio 0.904) —
  upside-positioned, downside under-hedged (cheap puts) [STRUCT:term_skew]
- **Negative vanna (−817) into IV rank 100** → post-earnings IV crush forces dealer
  SELLING; long delta held through the print fights this [STRUCT:vanna_charm]

## Detailed findings

### GEX (per-strike, ZGL) — `[STRUCT:gex]`

- **regime: POSITIVE** — dealers net long gamma; mean-reversion, suppressed
  realized vol *until the event*.
- **total_gex +1,574,300**, underlying $139.37, **ZGL $115.41** (spot +20.8% above).
- Top positive walls: **125 (+488,460), 145 (+392,113), 135 (+245,217), 130
  (+200,566), 120 (+154,351)**. Negative GEX is down at 95–100 (put-driven), far
  below spot.

Read: between 5/22 and the 5/28 print, dealer long gamma should **dampen moves and
pin price within the 125–145 wall band**. *This regime resets at earnings* — the
implied 10.6% move (phase-0.5 `[CTX:implied_move_pct]`) will overwhelm the gamma
pin on the print. Long-gamma mean-reversion is a *pre-event* statement only.

### DEX (dealer delta hedge) — `[STRUCT:dex]`

- net_dex **+84,443,233** (call_dex +86.3M, put_dex −1.86M). Public net call-long
  → dealers net **short calls** → hedge is to **BUY** underlying.
- Implication: a standing mild mechanical bid. **Caveat for phase-2:** some of the
  dark-pool buy lean (block buy_ratio 0.653) may be *dealer delta hedging of the
  call-heavy book*, not directional institutional accumulation. De-rate the DP
  "accumulation" read accordingly.

### Vanna + charm — `[STRUCT:vanna_charm]`

- net_vanna **−817** (call-heavy book), net_charm +5,201, call_vanna −828.
- Interpretation (verbatim): "Falling IV → call delta drops → dealers (short calls)
  cut long-underlying hedge → SELLING pressure. Rising IV reverses."
- **This is the key risk for a directional long:** NTAP enters 5/28 at **IV rank
  100**. Earnings will crush IV regardless of direction. With negative vanna, that
  crush mechanically unwinds dealer long-hedge → **SELLING pressure post-print**.
  Even a mild beat can fade as vol collapses. Long delta *through* the event fights
  both the vol crush and dealer de-hedging.

### IV term structure — `[STRUCT:iv_term_structure]`

**BACKWARDATION** (kink_expiry null — smooth, not a single binary kink):

| Expiry | Avg IV | Note |
|--------|--------|------|
| 2026-06-18 | **60.2%** | front month — holds the 5/28 earnings |
| 2026-07-17 | 48.3% | — |
| 2026-08-21 | 45.1% | — |
| 2026-09-18 | 47.1% | — |
| 2027-01-15 | 45.8% | LEAP (the bull-tell tenor from phase-1) |

Front-month richness (60.2% vs ~45–48% back) = textbook **earnings stress** in the
6/18 expiry. Confirms the 5/28 print is the dominant driver.

### Term skew (23 DTE actual, target 30) — `[STRUCT:term_skew]`

- call_25d_iv **0.6147** > put_25d_iv **0.556**, skew −0.0587, skew_ratio 0.904 →
  **COMPLACENT** (calls richer than puts).
- Read: market is **positioned for upside / under-hedged on downside**. Cheap puts
  = cheap protection for a long. Contrarian caution: complacency means a downside
  surprise is *not* priced — gaps can be violent.

### Front-end IV ratio — `[STRUCT:front_end_iv_ratio]`

**Degenerate / uninformative here:** near_dte and far_dte both resolved to 23 (no
expiry near 7 DTE exists — next expiry is 6/18 at ~23–27 days), so ratio = 1.0
"FLAT" is an artifact, not a signal. The real event-stress read is the
**BACKWARDATION** above. Flag and disregard the FLAT label.

### Today's gamma flip — `[STRUCT:today_gamma_flip]`

**Skipped.** 0DTE-only, intraday-meaningful tool; this is a retrospective EOD run on
2026-05-22 (after-hours), so the 0DTE flip map is stale and not relevant. Per phase
spec: note and skip.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=NTAP, dte_max=45 | POSITIVE, ZGL 115.41, walls 125/145 |
| `mcp__uw-pp__options_structure_dex` | symbol=NTAP, dte_max=45 | net_dex +84.4M, dealers buy hedge |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=NTAP, dte_max=45 | net_vanna −817 → crush = sell pressure |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=NTAP | BACKWARDATION, 6/18 60.2% |
| `mcp__uw-pp__options_structure_term_skew` | symbol=NTAP, dte_target=30 | COMPLACENT, skew_ratio 0.904 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=NTAP, near=7, far=30 | degenerate (both 23 DTE) |
| `mcp__uw-pp__options_structure_today_gamma_flip` | — | skipped (0DTE intraday, stale EOD) |

## Tool errors

None. (`front_end_iv_ratio` returned a degenerate FLAT due to no ~7-DTE expiry —
noted, not an error.)

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (positive), spot far above ZGL** — pre-earnings
  pin/mean-reversion regime within the 125–145 wall band. Regime *resets at the
  5/28 print*.
- **Conviction:** **4/5** (large-cap, deep-enough OI; GEX/DEX/term structure are
  clean and mutually consistent).
- **Three structural levels for phase-9:**
  1. **145** — top gamma wall (+392K) + overwrite strike (phase-1) + DP resistance
     (phase-2) → strong upside cap/magnet pre-event.
  2. **125** — bottom gamma wall (+488K, the largest) → downside magnet/support;
     aligns above the $119–124 DP shelf (phase-2).
  3. **ZGL $115.41** — regime flip to short-gamma (trend amplification) only on a
     deep post-earnings break; treat as ±2% band.
- **Open questions:** Does NTAP's history (phase-5) show post-earnings IV-crush
  fades despite beats (the negative-vanna risk)? Is the COMPLACENT call skew a
  squeeze setup or just overwriting suppressing put demand? Should phase-9 prefer a
  **defined-risk / vol-aware structure** over naked long delta given the crush +
  de-hedge headwind?
