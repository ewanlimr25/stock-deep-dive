# Phase 3 — Open Interest & Positioning

**Ticker:** NOW
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T12:30:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-0.5-context.md

## Summary

OI builds **temper, not confirm, phase-1's 3.4:1 bullish premium read.** The single
largest new position is clean near-term bullish — **106C 6/05 (+5,436 OI, 15× prior
OI, bought ask-side** 5,126 vs 598 bid) — and 110C builds add an upside-target shelf.
**But the upside is being *sold into*:** the LEAP 150C (+2,451), 140C (+1,771), and a
near-term 110C 9dte (+1,831) are all **written on the bid** (`inferred_direction`
bearish). Net OI tilt is mildly bullish (≈12.5k bullish-side vs ≈9.9k bearish-side
contracts) — far tighter than the premium ratio. With phase-2 showing **no stock
accumulation**, this reads as **speculative near-term call buying + upside call
overwriting**, not a stock-backed conviction build. Every build is <0.06% of float
— all speculative, none structural. `[OI:oi_pct_float fz]`

## Key signals

- **106C 6/05 (9 DTE): +5,436 OI** (last_oi 355 → 5,791, a 15× build), ask-side, $2.36 — the dominant fresh bullish position `[OI:biggest_increases]`
- **150C Jan-28 LEAP: +2,451 OI written** (bid-side 1,942 vs 683) — upside call **sold**, inferred bearish `[OI:smart_positioning]`
- 110C builds across tenors: +2,363 (51d, bought) / +1,831 (9d, **sold**) / +720 (22d, bought) — mixed at the $110 line `[OI:smart_positioning]`
- Closing: **130C 30d −2,179 OI** (vol 3,959) + 140C/125C/150C decreases — upside calls being trimmed `[OI:decrease_with_volume]`
- NOW **absent from pin-risk & opex-concentration** (next monthly OPEX 6/18 > 7d out; no >40% single-strike cliff) `[OI:pin_risk]` `[OI:opex_concentration]`

## Detailed findings

### Largest OI increases (decoded from OCC symbols) `[OI:biggest_increases]`

| contract | type | strike | DTE | OI Δ | curr/last OI | vol | ask/bid prev | read |
|----------|------|--------|-----|------|--------------|-----|--------------|------|
| NOW260605C106 | call | 106 | 9 | **+5,436** | 5,791 / 355 | 5,828 | 5,126 / 598 | **bought — bullish, fresh** |
| NOW280121C150 | call | 150 | 604 | +2,451 | 8,914 / 6,463 | 2,870 | 683 / 1,942 | **sold — upside write** |
| NOW260717C110 | call | 110 | 51 | +2,363 | 7,325 / 4,962 | 4,086 | 2,654 / 974 | bought — bullish |
| NOW260605C110 | call | 110 | 9 | +1,831 | 4,976 / 3,145 | 4,384 | 1,382 / 2,467 | sold — upside write |
| NOW260821C140 | call | 140 | 86 | +1,771 | 4,478 / 2,707 | 1,858 | 545 / 1,292 | sold — upside write |
| NOW260529P97 | put | 97 | 2 | +1,351 | — | 2,065 | — | sold (bullish, 0DTE) |
| NOW260529C105 | call | 105 | 2 | +1,081 | — | 5,479 | — | bought (bullish, 0DTE) |
| NOW260717P100 | put | 100 | 51 | +715 | — | 1,190 | — | **sold — willing to own at $100** |

### Smart positioning (inferred direction) `[OI:smart_positioning]`

- **Bullish-side builds (Σ ≈ 12,456):** 106C(+5,436), 110C 51d(+2,363), 97P sold(+1,351), 105C(+1,081), 98P sold(+790), 110C 22d(+720), 100P sold(+715).
- **Bearish-side builds (Σ ≈ 9,886):** 150C LEAP sold(+2,451), 110C 9d sold(+1,831), 140C sold(+1,771), 93P bought(+1,088), 105C 9d sold(+967), 100P bought(+913), 102C sold(+865).

The 0DTE 5/29 strikes (93–105) are two-way churn — discount. The signal is in
the structural builds: **near-OTM calls bought (106/110), far-OTM calls written
(140/150).** Verdict-level read: a *bounded* bullish posture targeting ~$106–110,
with sellers capping above.

### Closing / roll activity `[OI:decrease_with_volume]`

- 130C 30d **−2,179 OI** (vol 3,959) — largest close; 214C LEAP −712; 140C/130C/150C/125C all decreasing. **Upside-call OI being trimmed/closed** alongside the new writing → consistent with reduced upside conviction overhead.
- `position-rolls`: **0 rows** — no clean near→far roll detected (threshold 500).

### Pin risk / OPEX concentration

- `pin-risk` (dte≤7, ≤5% from spot): **NOW not in top-50.** The 5/29 weekly OI isn't concentrated enough to pin; no gamma-pin commentary warranted.
- `opex-concentration` (≥40%): **NOW not in top-50.** No single-expiry OI cliff. Next monthly OPEX 6/18 is 22 DTE — outside the pin window.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi biggest-increases --symbol NOW --min-oi-change 500` | 17 rows; top 106C +5,436 (bought) |
| `uw oi smart-positioning --symbol NOW --min-oi-change 500` | 17 rows; bullish Σ12.5k vs bearish Σ9.9k |
| `uw oi decrease-with-volume --symbol NOW --min-volume 100` | 130C −2,179 leads; upside calls trimmed |
| `uw oi position-rolls --symbol NOW --threshold 500 --near-dte-max 30` | 0 rows |
| `uw oi pin-risk --dte-max 7 --max-distance-pct 5` | NOW not in top-50 |
| `uw oi opex-concentration --min-concentration-pct 40` | NOW not in top-50 |

## Tool errors

None.

## Verdict for downstream

- **Positioning bias:** **MILDLY BULLISH, BOUNDED** — fresh near-term call buying
  (106C/110C) is the dominant build, but upside calls (140C/150C LEAP) are being
  **written** and 130C OI is being closed. Net OI tilt (≈12.5k vs ≈9.9k) is far
  weaker than phase-1's premium ratio. **Confirms the speculative, non-accumulation
  read of phase-2** — this is options-expressed positioning, not stock-backed.
- **Conviction:** **3/5** — bullish plurality, but heavy two-way call writing caps it.
- **Largest OI build as % of float:** **0.053%** (5,436 × 100 / 1.02B sh-equiv).
  Advisory: tiny — speculative bet, **not** a structural position. `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **$106** — biggest fresh OI build (106C 6/05), the near-term upside **magnet/first target**.
  2. **$110** — repeated call builds (51d/22d bought; 9d written) → upside call **wall / second target & write-zone**.
  3. **$100** — put builds both ways + 100P 51d *sold* (willing to own) + aligns with phase-2 DP support $99.69–$100 → **floor**.
- **Open questions:**
  1. Is the upside call writing (140/150) **covered** (against the AH stock blocks in phase-2) or naked? Phase-2 showed no clear accumulation, so likely overwrite/income — caps the upside thesis.
  2. The 106C 9DTE expires 6/05 — does the near-term thesis have a **hard clock** (phase-9 must respect the 9-day fuse)?
