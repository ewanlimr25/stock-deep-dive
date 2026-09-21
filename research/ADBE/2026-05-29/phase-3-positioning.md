# Phase 3 — Open Interest & Positioning

**Ticker:** ADBE
**As-of date:** 2026-05-29
**Generated:** 2026-05-30T19:58:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

ADBE's open-interest map shows spot ($259.21) pinned **right at the 260
call-wall resistance** (`distance_pct` +0.34%, net_oi +8,983) with the next
upside wall at **300** (net_oi +11,264) and **put-wall support stacked below at
240 / 230 / 220** [OI:oi_by_strike]. Fresh OI buildup is **thin and call-led but
ambiguous in intent**: the only ≥500-contract increases are **260C 6/5 (+1,101,
vol 1,783)** and **280C 6/18 (+993)** — and `smart-positioning` infers **both as
*bearish*** (net ask-bid −478 on the 260C), i.e. the new near-money call OI is
being **sold/written**, not bought to open [OI:smart_positioning]. That reconciles
with phase-1's bid-side 250 call selling and phase-2's de-rated accumulation: the
institutional footprint looks more like **covered-call writing against a long /
range-selling into rich IV** than a fresh directional call grab. No position
rolls, and pin-risk/opex-concentration return no ADBE rows (spot is not within a
near-OPEX pin window for ADBE; the only weekly OPEX is the 6/5 expiry).

## Key signals

- Spot sits **at the 260 call wall** (`call_wall_resistance`, net_oi +8,983,
  distance +0.34%) — the immediate overhead cap [OI:oi_by_strike].
- **Put-wall support shelf: 240** (net_oi −4,843, −7.4%), **230** (−8,337,
  −11.2%), **220** (−17,834, −15.1%) — and **245** on the ≤30-DTE map
  (put_wall_support, −5.45%) [OI:oi_by_strike].
- Next upside wall **300** (`call_wall_resistance`, net_oi +11,264, +15.8%) — the
  ceiling the LEAP/upside calls are layered into [OI:oi_by_strike].
- Fresh OI builds are **call-strikes but inferred SOLD**: 260C 6/5 +1,101 and
  280C 6/18 +993 both tag `inferred_direction: bearish` [OI:smart_positioning].
- **No rolls, no ADBE pin-risk/opex-concentration rows** — positioning is
  static-walls + light writing, not an active roll or pin setup
  [OI:position_rolls][OI:pin_risk].

## Detailed findings

### OI walls by strike — `[OI:oi_by_strike]`

**All-expiry aggregate:**

| Strike | call_oi | put_oi | net_oi | role | dist % |
|--------|---------|--------|--------|------|--------|
| 200 | 21,448 | 12,113 | +9,335 | call_heavy | −22.8 |
| 300 | 19,751 | 8,487 | +11,264 | call_wall_resistance | +15.8 |
| 240 | 9,465 | 14,308 | −4,843 | put_wall_support | −7.4 |
| 250 | 13,147 | 9,152 | +3,995 | call_heavy | −3.5 |
| 220 | 295 | 18,129 | −17,834 | put_wall_support | −15.1 |
| **260** | **13,571** | **4,588** | **+8,983** | **call_wall_resistance** | **+0.34** |
| 280 | 9,029 | 6,774 | +2,255 | call_wall_resistance | +8.1 |
| 350 | 12,990 | 1,386 | +11,604 | call_wall_resistance | +35.1 |
| 230 | 2,018 | 10,355 | −8,337 | put_wall_support | −11.2 |
| 500 | 11,782 | 0 | +11,782 | call_wall_resistance | +92.9 |

**Tradeable-horizon (≤30 DTE) wall map** — the one phase-9 sizes against:

| Strike | call_oi | put_oi | net_oi | role | dist % |
|--------|---------|--------|--------|------|--------|
| **260** | 7,824 | 2,156 | +5,668 | call_wall_resistance | +0.34 |
| 250 | 7,166 | 3,911 | +3,255 | call_heavy | −3.5 |
| 255 | 3,415 | 1,188 | +2,227 | call_heavy | −1.6 |
| **245** | 3,231 | 4,063 | −832 | put_wall_support | −5.45 |
| 240 | 5,353 | 8,505 | −3,152 | put_wall_support | −7.4 |
| 230 | 1,240 | 6,403 | −5,163 | put_wall_support | −11.2 |
| 280 | 5,437 | 2,129 | +3,308 | call_wall_resistance | +8.1 |
| 300 | 10,207 | 1,804 | +8,403 | call_wall_resistance | +15.8 |

Near-term structure: **resistance 260 (at spot) → 280 → 300**; **support 245 →
240 → 230**. The 250/255 strikes are two-sided `call_heavy` battlegrounds (both
sides loaded), not clean levels.

### OI term structure — `[OI:term_structure]`

`uw oi term-structure --symbol ADBE` returned **no parseable rows this run**
(empty `results` in the captured output). The OPEX-cliff read therefore falls back
to the expiry-heatmap from phase-1 and the max-pain in phase-4: premium/OI
concentrates in **6/18 monthly** (largest premium expiry $10.3M) with heavy
near-weekly activity in **6/5 and 6/12** (the earnings straddle). Treated as a
data gap, not a structural absence — see Tool errors.

### Largest OI increases — `[OI:biggest_increases]`

| Strike | Expiry (dte) | OI Δ (oi_diff_plain) | Volume | Note |
|--------|--------------|----------------------|--------|------|
| 260 C | 6/5 (7) | +1,101 | 1,783 | curr_oi 1,975 from 874; near-money |
| 280 C | 6/18 (20) | +993 | 1,073 | OTM upside |

Only two strikes cleared the +500 threshold — **builds are small** (consistent
with phase-0.5's "normally-sized" turnover). Both are call strikes, but see
smart-positioning below for intent.

### Closing / roll activity — `[OI:decrease_with_volume]` / `[OI:position_rolls]`

Decreases are tiny (largest −172 at 255). **`position-rolls` returns `[]`** — no
near→far roll signature. Positioning is being *adjusted at the margin*, not rolled.

### Smart positioning (inferred direction) — `[OI:smart_positioning]`

| Strike | Expiry | Type | Inferred dir | net_ask_bid | OI Δ |
|--------|--------|------|--------------|-------------|------|
| 260 C | 6/5 | call | **bearish** | −478 | +1,101 |
| 280 C | 6/18 | call | **bearish** | −993 | +993 |

Both fresh call builds carry **negative net ask-bid → inferred sold-to-open
(call writing)**. This is the key reconciliation: the new near-money/OTM call OI
is **supply, not demand** — covered-call writing or call-spread financing into
IV-rank-100, *not* a directional long add. It aligns with phase-1's bid-side 250C
6/18 selling ($0.96M) and phase-2's de-rated accumulation read.

### Pin risk / OPEX concentration — `[OI:pin_risk]` / `[OI:opex_concentration]`

**No ADBE rows** in either market-wide scan (top rows are HYG, etc.). ADBE is not
within a high-conviction OPEX pin window at the 7-DTE / 40%-concentration
thresholds — its OI is spread across 6/5, 6/12, 6/18 rather than cliffed into one
expiry. Pin commentary therefore deferred to phase-4 max-pain.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw oi oi-by-strike --symbol ADBE --top-n 10 [--dte-max 30] --date 2026-05-29` | 260 call wall at spot; 245/240/230 put support; 300 upside wall |
| `uw oi biggest-increases --symbol ADBE --top-n 20 --min-oi-change 500 --date 2026-05-29` | only 260C 6/5 (+1,101) & 280C 6/18 (+993) cleared 500 |
| `uw oi smart-positioning --symbol ADBE --top-n 20 --min-oi-change 500 --date 2026-05-29` | both builds inferred **bearish (sold)** |
| `uw oi decrease-with-volume --symbol ADBE --top-n 15 --min-volume 100 --date 2026-05-29` | tiny decreases (≤172); no closing wave |
| `uw oi position-rolls --symbol ADBE --threshold 500 --near-dte-max 30 --date 2026-05-29` | `[]` — no rolls |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-05-29` | no ADBE row |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-05-29` | no ADBE row |
| `uw oi term-structure --symbol ADBE --date 2026-05-29` | empty results this run (see Tool errors) |

## Tool errors

- `uw oi term-structure --symbol ADBE --date 2026-05-29` returned no parseable
  `results` rows in this run's captured output (empty). Not surfaced as an engine
  error; treated as a transient/empty return. OPEX-cliff read substituted from
  phase-1 expiry-heatmap (6/18 monthly largest) and phase-4 max-pain.

## Verdict for downstream phases

- **Positioning bias:** **MIXED / mildly distributive at the margin.** Static walls
  are call-heavy above (260/280/300 resistance) with put support 240–245, but the
  *fresh* OI is **call writing (inferred sold)** into IV-100 — supply, not a
  directional long. Net: positioning does **not** confirm phase-1's bullish flow;
  it leans toward **range/covered-call** behavior.
- **Conviction:** **2 / 5** (builds are small and intent is writing, not buying).
- **Largest OI build as % of float (share-equiv):** 1,101 contracts × 100 =
  110,100 sh = **0.027% of the 403.40M float** [OI:oi_pct_float fz] — immaterial;
  the OI builds are not structural for this name.
- **Three pin/cliff strikes for phase-9 (sourced from roles):**
  1. **260 = call_wall_resistance at spot** (net_oi +5,668 ≤30DTE) — immediate cap
     [OI:oi_by_strike].
  2. **245 = put_wall_support** (≤30DTE, −5.45%) — first downside shelf, aligns
     with phase-2 DP cluster 244.76 [OI:oi_by_strike].
  3. **240/230 = deeper put_wall_support** (−7.4% / −11.2%) — stop reference
     [OI:oi_by_strike].
- **Open questions:** Is the inferred call-writing covered (institutions short
  calls vs the dark-pool shares from phase-2) or naked range-selling? Does phase-4
  GEX confirm dealers are long gamma around 260 (pinning spot to the wall) — which
  would corroborate a range read over a breakout? Where is max-pain relative to
  260?
