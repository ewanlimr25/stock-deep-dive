# Phase 3 — Open Interest & Positioning

**Ticker:** NTAP
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

Positioning is **static — no fresh conviction OI build.** `oi_biggest_increases`
(≥500) and `oi_smart_positioning` both return **empty**, zero rolls detected, and
the day's most-traded contract — **145C 6/18 (6,231 volume)** — actually saw OI
*decrease* (1,642 → 1,597). Huge volume, no net OI growth, is the textbook
signature of **intraday churn / call overwriting**, not position-building — directly
corroborating phase-1's "145C is an overwrite, not a buy" read [FLOW:aggressor_ex0dte DUCKDB].
The largest standing OI walls in the earnings expiry are **125C (2,825) and 145C
(1,597)**; NTAP carries **no near-term pin risk** (OI sits in 6/18, 27 DTE).

## Key signals

- **No OI build ≥500 anywhere** — `oi_biggest_increases` empty; the biggest NTAP OI
  changes (per phase-0.5 `insights_deep_dive`) were +50/+47/+46 ctr — trivial [OI:biggest_increases]
- **Most-traded strike LOST OI:** 145C 6/18 OI 1,642 → 1,597 (−45) on 6,231 volume
  → churn/overwrite, not opening [OI:decrease_with_volume]
- **Zero position rolls** detected (threshold 500, near_dte ≤30) [OI:position_rolls]
- **No smart-positioning signal** — empty even at min_oi_change=500 [OI:smart_positioning]
- **Standing OI walls: 125C (2,825) and 145C (1,597) for 6/18** — the post-earnings
  battleground strikes [OI:decrease_with_volume]
- **No pin risk / no OPEX concentration** — NTAP absent from both lists [OI:pin_risk], [OI:opex_concentration]

## Detailed findings

### Largest OI increases — `[OI:biggest_increases]`

**Empty** at min_oi_change=500. NTAP's largest OI changes today (from phase-0.5
`uw_top_oi_changes`) were +50 (160C 9/18), +47 (120C 6/18), +46 (135C 9/18), +45
(125P 6/18), +42 (130C 6/18) — all trivial. **Despite the day's 31-session-high
option premium (phase-0.5 `[CTX:]`), essentially no net new OI was built.** The
activity was churn, not accumulation. This is the single most important positioning
fact: it tells later phases the "huge flow" did not lay down directional positions.

### Closing / roll activity — `[OI:decrease_with_volume]`, `[OI:position_rolls]`

| Strike/Exp | curr OI | prev OI | OI Δ | Volume | Read |
|-----------|---------|---------|------|--------|------|
| 145C 6/18 | 1,597 | 1,642 | −45 | 212 | overwrite/churn (vs 6,231 total day vol) |
| 125C 6/18 | 2,825 | 2,848 | −23 | 355 | minor trim of large ITM-ish wall |

Rolls detected: **0**. No near→far migration — positions are being held or churned
in place, not rolled out past earnings.

### Smart positioning — `[OI:smart_positioning]`

**Empty** (min_oi_change=500, direction=both). No contract shows a directionally-
inferable OI build of size. Confirms: the chain is not signalling fresh
bullish *or* bearish conviction. Consistent with phase-1 flat aggressor footprint
and phase-2's merely-suggestive DP buy lean.

### Pin risk — `[OI:pin_risk]`

NTAP **absent** from the OPEX-week pin list (dte_max=7). All entries are 0DTE
(today's 5/22 expiry) ETFs/mega-caps (HYG, SPY, TLT, QQQ, NVDA…). NTAP's OI mass is
in the **6/18 monthly (27 DTE, the earnings expiry)** — no near-term pin mechanics
apply. **Pin commentary skipped** per phase spec.

### OPEX concentration — `[OI:opex_concentration]`

NTAP **absent** (min_concentration 40%). The list is tiny illiquid names at 100%
single-expiry concentration. NTAP's OI (total ~29,220, phase-0.5) is **spread across
strikes/expiries** — no single-expiry cliff. The relevant concentration is simply
that 6/18 holds the bulk of near-term OI as the first post-earnings monthly.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__oi_biggest_increases` | symbol=NTAP, top_n=20, min_oi_change=500 | **empty** — no build ≥500 |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=NTAP, top_n=15, min_volume=100 | 145C −45, 125C −23 (churn) |
| `mcp__uw-pp__oi_smart_positioning` | symbol=NTAP, top_n=20, min_oi_change=500 | **empty** |
| `mcp__uw-pp__oi_position_rolls` | symbol=NTAP, threshold=500, near_dte_max=30 | **0 rolls** |
| `mcp__uw-pp__oi_opex_concentration` | top_n=20, min_conc=40 | NTAP absent |
| `mcp__uw-pp__oi_pin_risk` | dte_max=7, max_dist=5, top_n=25 | NTAP absent (0DTE ETFs only) |

## Tool errors

None. (Four tools returned empty result sets — meaningful findings, not errors:
no NTAP OI build, no rolls, no pin, no concentration.)

## Verdict for downstream phases

- **Positioning bias:** **NEUTRAL / static.** No fresh OI conviction in either
  direction. The day's volume was churn (145C overwrite), confirming — not
  contradicting — the flat options tape (phase-1) and the merely-suggestive DP
  accumulation (phase-2).
- **Conviction:** **2/5.** Static positioning *lowers* the case for a clean
  directional swing pre-earnings; it does not support a "positions being loaded"
  narrative.
- **Three pin/cliff strikes for phase-9 (entry/stop reference):**
  1. **145C 6/18** — largest fresh-traded strike + overwrite wall + DP resistance
     proxy (phase-2 noted 145C sits +4% above the ~$139 close) → likely upside
     magnet/cap into 6/18.
  2. **125C 6/18** — biggest standing OI wall (2,825) → ITM-ish support reference.
  3. **No 0DTE/weekly pin** — the only structural strike mass is 6/18 monthly;
     phase-4 (GEX/gamma flip) should resolve whether 145 is a hard dealer ceiling.
- **Open questions:** Will today's churn show up as a real OI build in tomorrow's
  snapshot (i.e. were these opening trades not yet settled)? Is the 145C wall a
  dealer-short-gamma cap or dealer-long-gamma magnet (phase-4)? Does the static OI
  argue for a vol-structure trade over a directional one (phase-4/9)?
