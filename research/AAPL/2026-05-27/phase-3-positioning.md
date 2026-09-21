# Phase 3 — Open Interest & Positioning

**Ticker:** AAPL
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T03:04:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning **corroborates the mixed, low-conviction read from phases 1–2**. New
OI builds are dominated by **0–2 DTE near-the-money calls** (315C/312.5C/310C) —
short-dated gamma/lottery activity, not structural conviction — and
smart-positioning's inferred direction across those builds is **genuinely
two-way** (315C tagged bearish, 312.5C bullish, 310C 0DTE bearish). The single
**largest OI change of the entire day is a *decrease*: 300C 6/18 −12,646
contracts** (an ITM-call unwind/profit-take). The only structural longer-dated
build is a **290P 8/21 (+3,688, protective put)** alongside scattered modest
upside calls (350C 9/18, 330C 8/21). No position rolls. Largest build is 0.0048%
of float. **Net: mixed/short-dated positioning, no directional structure.**

## Key signals

- OI builds concentrated in **0–2 DTE 310–315 calls** (315C 2DTE +7,112; 312.5C
  0DTE +6,786; 310C 2DTE +3,601) — gamma/pin, not structural `[OI:biggest_increases]`
- Smart-positioning inferred direction is **mixed** (315C 2DTE→bearish, 312.5C→
  bullish, 310C 0DTE→bearish, 320C→bullish) — no consensus `[OI:smart_positioning]`
- **Largest single OI change = a decrease**: 300C 6/18 **−12,646** (ITM unwind) `[OI:decrease_with_volume]`
- Only structural builds: **290P 8/21 +3,688 (protective)**, 350C 9/18 +2,541,
  330C 8/21 +2,471, 325C 7/17 +2,262 — small and mixed call/put `[OI:biggest_increases]`
- Minor upside pin/magnet at **320** (0DTE today, 2.92% above spot, top_strike_OI
  72,147); **no OPEX-concentration cliff** (AAPL absent from ≥40% list) `[OI:pin_risk]`

## Detailed findings

### Largest OI increases

| Strike/Type | Expiry (DTE) | OI Δ | Volume | Inferred dir |
|-------------|--------------|------|--------|--------------|
| 315 C | 5/29 (2) | +7,112 | 24,783 | bearish |
| 312.5 C | 5/27 (0) | +6,786 | 34,454 | bullish |
| **290 P** | **8/21 (86)** | **+3,688** | 4,099 | bullish (put sold?) |
| 310 C | 5/29 (2) | +3,601 | 21,028 | bullish |
| 310 C | 5/27 (0) | +3,473 | 28,868 | bearish |
| 315 C | 5/27 (0) | +3,155 | 12,905 | bearish |
| 260 P | 6/05 (9) | +3,028 | 3,414 | bullish |
| 350 C | 9/18 (114) | +2,541 | 3,110 | bullish |
| 330 C | 8/21 (86) | +2,471 | 3,120 | bearish |
| 325 C | 7/17 (51) | +2,262 | 6,043 | bullish |

**~70% of the build OI is in 0–2 DTE strikes.** This is expiry-week gamma
positioning (matches phase-1's 0DTE-heavy unusual-volume), not a directional
campaign. The longer-dated rows are small (2–3.7k) and split call/put.

**Float context (advisory, `fz` float 14.67B):** largest build 7,112 × 100 =
711,200 sh = **0.0048% of float** `[OI:oi_pct_float fz]`. Even the structural 290P
build (368,800 sh) is 0.0025% — none of these are structural bets *for this name*.

### Closing / roll activity

| Strike/Type | Expiry (DTE) | OI Δ | Volume |
|-------------|--------------|------|--------|
| **300 C** | **6/18 (22)** | **−12,646** | 15,107 |
| 290 P | 5/29 (2) | −944 | 1,982 |
| 305 C | 6/05 (9) | −817 | 1,433 |

The day's **largest OI move is the 300C 6/18 unwind (−12,646)** — an in-the-money
call (spot $311) being closed/reduced for $10M+ of trading (phase-1 showed a 300C
6/18 $10.2M ask-side print, so the line is being *traded heavily while net OI
falls* = profit-taking/distribution at that strike, not fresh buying).
**`uw oi position-rolls` returned 0** — no clean near→far roll signature; this is a
close, not a roll.

### Pin risk (OPEX week)

| Field | Value |
|-------|-------|
| nearest_high_oi_strike | **320** |
| spot | 310.91 |
| pin_distance_pct | 2.92% |
| top_strike_oi | 72,147 |
| total_oi_in_window | 1,238,692 |
| pin_score | 458,977 |

A modest upside magnet at **320** for near-dated expiry, but 2.92% away — weak
pull. The real near-term battleground is the **310–315** stack (heaviest fresh OI).

### OPEX concentration

AAPL is **absent** from the ≥40%-concentration list — OI is spread across strikes,
no single-expiry cliff dominates (normal for a deeply liquid mega-cap). No cliff
risk to flag.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --min-oi-change 500` | 0–2 DTE 310–315 calls dominate; 290P 8/21 structural |
| `uw oi smart-positioning --min-oi-change 500` | inferred direction mixed (both bull & bear tags) |
| `uw oi decrease-with-volume --min-volume 100` | 300C 6/18 −12,646 (largest move = a close) |
| `uw oi position-rolls --threshold 500 --near-dte-max 30` | **0 rolls** |
| `uw oi pin-risk --dte-max 7 --max-distance-pct 5` | pin 320 @ 2.92%, top_strike_OI 72k |
| `uw oi opex-concentration --min-concentration-pct 40` | AAPL absent (no cliff) |

## Tool errors

None.

## Verdict for downstream

- **Positioning bias:** **mixed / short-dated** — fresh OI is 0–2 DTE call gamma
  (no consensus direction), the largest move is a 300C profit-take unwind, and the
  only structural build is a small protective 290P. Not a directional structure.
- **Conviction:** **2/5** — corroborates phases 1–2; nothing here adds directional
  conviction (capped at `+` per phase-0.5 in any case).
- **Largest OI build as % of float:** 0.0048% (711,200 sh / 14.67B) — **not
  structural** for this name. `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **320** — near-term upside pin/magnet & resistance (top_strike_OI 72k).
  2. **310–312.5** — current battleground / heaviest fresh OI (= spot zone).
  3. **300** — strike being unwound; aligns with the **$302–305 DP support**
     (phase-2) just below = confluent downside reference.
- **Open questions:**
  - Is the 290P 8/21 build the hedge against phase-1's deep-ITM 9/18 stock-
    replacement calls (a collar)? Phase-4 GEX/structure to resolve dealer side.
  - With the largest move being a 300C *close*, is net dealer gamma long or short
    around spot? → phase-4.
