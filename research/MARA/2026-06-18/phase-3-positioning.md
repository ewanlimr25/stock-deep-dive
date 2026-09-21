# Phase 3 — Open Interest & Positioning

**Ticker:** MARA
**As-of date:** 2026-06-18
**Generated:** 2026-06-19
**Upstream phases cited:** phase-0-intake.md (`Shs Float` 372.36M), phase-1-flow.md, phase-2-dark-pool.md

## Summary

The standing-OI chain is **call-dominated with a ladder of overhead resistance** —
near-term call walls at **$14.5 (+1.8%), $15 (+5.3%), $16 (+12.4%)** and puts only as
support far below ($12/$10/$8) — so the structure **caps upside near $14.5–$15**,
corroborating phase-1's overwrite read. But the key refinement: **phase-1's big
$14.5C 6/26 selling did NOT build a standing short — its OI rose only +514 despite
63,005 volume** (intraday churn, not a structural bear-spread). Today's net-new OI was
**modest** (largest build +2,613 ctr = 0.07% of float) and `smart-positioning` labels
most new call-OI builds **"bearish" = written** (overwriting overhead strikes). Net
positioning = **neutral with a call-writing / capped-upside tilt**; no decisive new
directional bet was established. This **tempers** phase-1's bearish lean.

## Key signals

- **$15 = dominant near-term call wall** (DTE≤30 call_oi 87,485 / net_oi +74,579,
  +5.3%) — primary upside magnet/cap `[OI:oi-by-strike]`.
- **$14.5 is now a call wall too** (DTE≤30 call_oi 39,208 / net_oi +28,836, **+1.8%**)
  — the overwrite strike from phase-1, structurally confirmed `[OI:oi-by-strike]`.
- **6/26 $14.5C OI rose only +514** (curr 2,111) vs 63,005 volume → phase-1's
  call-selling was **churn, not standing short OI** `[OI:biggest-increases]`.
- **6/18 (0DTE) holds 31.1% of all OI**, call-stacked ($15 0DTE call_oi 72,783) →
  pin into today's close ~$14.2–$14.5, then **rolls off** `[OI:term-structure]`.
- New call-OI builds ($16C +2,613, $15.5C +1,473, $15C +863) tagged **bearish/written**
  by `smart-positioning` → overhead resistance being *sold*, not bought `[OI:smart-positioning]`.

## Detailed findings

### OI walls by strike (`oi-by-strike --dte-max 30`, spot $14.24 — tradeable map)

| Strike | call_oi | put_oi | net_oi | total_oi | role | dist |
|--------|---------|--------|--------|----------|------|------|
| **$15** | 87,485 | 12,906 | **+74,579** | 100,391 | **call_wall_resistance** | +5.3% |
| **$16** | 71,988 | 642 | +71,346 | 72,630 | call_wall_resistance | +12.4% |
| **$14.5** | 39,208 | 10,372 | **+28,836** | 49,580 | **call_wall_resistance** | **+1.8%** |
| $14 | 26,602 | 21,500 | +5,102 | 48,102 | call_heavy (battleground) | −1.7% |
| $13 | 23,528 | 20,464 | +3,064 | 43,992 | call_heavy (battleground) | −8.7% |
| $20 | 41,574 | 16 | +41,558 | 41,590 | call_wall_resistance | +40.5% |
| $12 | 10,777 | 22,408 | **−11,631** | 33,185 | **put_wall_support** | −15.7% |
| $17 | 28,394 | 2,058 | +26,336 | 30,452 | call_wall_resistance | +19.4% |

All-expiry adds deeper put support: **$10** (put_oi 79,258, put_wall) and **$8**
(put_oi 46,740, put_wall) — structural downside hedges 30–44% OTM. The chain is
**call-heavy overhead, put-supported far below** — a classic capped-upside lattice.

### OI term structure (`term-structure`, total_oi 1,342,414 across 17 expiries)

| Expiry | DTE | call_oi | put_oi | P/C-OI | % of total OI |
|--------|-----|---------|--------|--------|---------------|
| **2026-06-18** | 0 | 351,558 | 65,421 | 0.19 | **31.1%** (expires today — rolls off) |
| 2026-09-18 | 92 | 113,343 | 117,564 | 1.04 | **17.2%** (largest *forward* cliff) |
| 2027-01-15 | 211 | 126,388 | 71,010 | 0.56 | 14.7% (LEAP) |
| 2026-07-17 | 29 | 63,831 | 26,254 | 0.41 | 6.7% (next monthly) |
| **2026-06-26** | 8 | 37,215 | 45,061 | **1.21** | 6.1% (phase-1 spread expiry; *put*-heavy) |
| 2026-08-21 | 64 | 46,681 | 20,285 | 0.44 | 5.0% |

**OPEX cliffs:** 6/18 0DTE (31%, expiring at this close — near-term pin then gone);
forward gravity is **9/18 (17.2%)**. The tradeable near-term cliff is **6/26 (8 DTE,
6.1%, P/C-OI 1.21 — note it's actually put-heavy)** and **7/17 (29 DTE)**.

### Largest OI increases (today's net-new builds — all modest)

| Contract (OPRA → parsed) | Expiry | Side/Strike | OI Δ | curr OI | % float (sh-equiv) |
|--------------------------|--------|-------------|------|---------|--------------------|
| MARA260626C00016000 | 6/26 | $16 call | +2,613 | 6,214 | 0.07% |
| MARA260618C00014500 | 6/18 | $14.5 call (0DTE) | +2,260 | 35,560 | 0.06% |
| MARA260821C00018000 | 8/21 | $18 call | +1,704 | 2,671 | 0.05% |
| MARA260626C00015500 | 6/26 | $15.5 call | +1,473 | 4,002 | 0.04% |
| MARA260626P00014000 | 6/26 | $14 put | +1,227 | 6,637 | 0.03% |
| **MARA260626C00014500** | 6/26 | **$14.5 call** | **+514** | 2,111 | 0.01% |

Largest build = 0.07% of float — **negligible structural footprint**. The 6/26 builds
skew to **higher-strike calls ($15.5/$16) being written** (smart-positioning: bearish)
= overhead supply, not bullish accumulation.

### Closing / roll activity

- `decrease-with-volume`: closing is **entirely 6/18 0DTE** ($17P −1,705, $16C −1,596,
  $18P −1,516, $15.5C −898…) = ordinary expiry-day unwind. No structural close.
- `position-rolls`: **0 rolls detected** (single-day detection; cross-session rolls
  not captured). No near→far roll signature.

### Smart positioning (inferred)

Mixed but call-write-dominated: $16C/$15.5C/$15C/$18C builds tagged **bearish
(written)**; $14.5C 6/18 + $14P 0DTE tagged bullish. Net = **premium-selling /
overwriting overhead strikes**, consistent with phases 1–2 (buy-write).

### Pin risk / OPEX concentration

- `pin-risk` (dte-max 7): **MARA outside top-25** (leaders AAPL/NVDA/SPY/TSLA…). The
  next monthly OPEX 6/26 is **8 DTE — just beyond the 7-day window**; 6/18 0DTE is
  already expiring. So no forward pin flag for MARA.
- `opex-concentration` (≥40%): **MARA outside top-20** (its peak 6/18 share is 31% <
  40% threshold). Not a concentration-cliff name.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `oi oi-by-strike --symbol MARA --dte-max 30 --date 2026-06-18` | $15 net_oi +74,579 / $14.5 +28,836 ← `.results[].net_oi,.role` | 10 |
| `oi oi-by-strike --symbol MARA --date 2026-06-18` (all-expiry) | $10/$8 put walls ← `.results[]` | 10 |
| `oi term-structure --symbol MARA --date 2026-06-18` | 6/18 31.1% / 9/18 17.2% ← `.term_structure[].pct_of_total_oi` | 17 |
| `oi biggest-increases --symbol MARA --min-oi-change 500` | $14.5C 6/26 Δ+514 vs 63k vol ← `.results[].oi_diff_plain` + OPRA parse | 11 |
| `oi smart-positioning --symbol MARA --min-oi-change 500` | call builds tagged bearish/written ← `.results[].inferred_direction` | 11 |
| `oi decrease-with-volume --symbol MARA --min-volume 100` | all 6/18 0DTE unwind ← `.results[].option_symbol` | 15 |
| `oi position-rolls --symbol MARA --threshold 500 --near-dte-max 30` | rolls_detected 0 ← `.rolls_detected` | 0 |
| `oi pin-risk --dte-max 7 --max-distance-pct 5` | MARA outside top-25 ← ticker scan | 25 |
| `oi opex-concentration --min-concentration-pct 40` | MARA outside top-20 ← ticker scan | 20 |

## Tool errors

(none — all nine reads valid JSON. pin-risk/opex-conc "outside top-N" and rolls=0 are
information, not errors.)

## DATA NOTE / CORRECTION

Refines phase-1: phase-1 read the 6/26 $14.5C as a "sizeable new short-call/credit
spread" from 30× vol/OI. Phase-3 `biggest-increases` shows that contract's **OI rose
only +514** (to 2,111) — the 63,005 volume was overwhelmingly **intraday churn that
did not stick as overnight OI**. The directional *aggressor* lean (net call-selling)
was real, but it did **not** build a standing short position. Phase-9/10 should treat
the bearish-flow conviction as correspondingly lower.

## Verdict for downstream phases

- **Positioning bias:** **NEUTRAL, call-writing / capped-upside tilt.** Overhead call
  walls ($14.5/$15/$16) define the resistance ladder; puts support far below
  ($12/$10/$8). **No large new directional structure** was established today —
  modest builds + intraday churn + overwriting.
- **Conviction:** **2/5** — the wall map is informative and stable, but the *new*
  positioning is small and non-committal; tempers, not amplifies, phase-1.
- **Largest OI build as % of float:** +2,613 ctr ≈ 261k sh = **0.07% of the 372.36M
  float** — negligible. (Largest standing wall, $15 all-expiry 151,159 OI ≈ 4.1% of
  float, but it's dominated by the expiring 0DTE bucket.) `[OI:oi_pct_float fz]`
- **Three pin/cliff strikes for phase-9:**
  1. **$14.5** — `call_wall_resistance` +1.8% (immediate upside cap / overwrite strike).
  2. **$15** — `call_wall_resistance` +5.3%, the dominant near-term magnet (hard cap).
  3. **$12** — `put_wall_support` −15.7% (first structural put-wall floor; $13–$14 is a
     two-sided `call_heavy` battleground above it). Near-term OPEX cliff = **6/26**.
- **Open questions:**
  - The $14.5 short-call writing is structurally confirmed but **small in standing
    OI** — is the overwriting program ongoing (phase-5 should check multi-day OI
    persistence) or was today a one-off churn?
  - 6/26 is **put-heavy** (P/C-OI 1.21) — pre-existing downside hedges sitting under
    the call-spread expiry. Does phase-4 GEX/max-pain place the gravity at $14 or $15?
