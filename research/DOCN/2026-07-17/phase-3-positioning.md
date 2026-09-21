# Phase 3 — Open Interest & Positioning

**Ticker:** DOCN
**As-of date:** 2026-07-17
**Generated:** 2026-07-20T01:30:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

No structural positioning happened on 2026-07-17 — the **largest OI build was just
+206 contracts** (Aug-21 $145C); `biggest-increases`/`smart-positioning` returned
**empty** at the standard ≥500 threshold. The day's real OI action was **expiry
roll-off** (7/17 puts) and, critically, a **−430 OI reduction in the 180C Nov-20**
strike — the same contract phase-1 flagged as an $985K ask-side "bullish" print.
**That print did NOT open a bullish position; OI fell, so it was buy-to-close /
roll, not fresh upside conviction** — de-rating phase-1's one bullish standout.
Standing forward OI is call-heavy (10/16 20.7%, 8/21 16.4%, 11/20 8.9% — all
call-dominant), but with today's tape showing call-*writing* (phase-1), that skew
is not cleanly bullish. Net positioning: **mixed / no fresh conviction.**

## Key signals

- **Largest OI build +206** (Aug-21 $145C, vol 279); next +59 (7/24 $100C). Nothing
  ≥500 → normal day, no structural bet `[OI:biggest_increases]`.
- **180C Nov OI Δ = −430** (vol 475) `[OI:decrease_with_volume]` — phase-1's $985K
  ask print was **OI-reducing (closing/roll), not new bullish opening.** ⚠️ correction.
- Tradeable-horizon walls (dte≤30): **call resistance $128** (2,156 OI, +7.6%),
  then $140/$145; **put support $115** (918 OI, −3.3%), then $110 `[OI:oi_by_strike]`.
- OPEX gravity: today **7/17 = 41.6% of OI** (expiring); forward cliffs **10/16
  (20.7%)** and **8/21 (16.4%, post-earnings)** `[OI:term_structure]`.
- DOCN **not** in market-wide pin-risk (7DTE/5%) or opex-concentration (>40%)
  lists `[OI:pin_risk][OI:opex_concentration]`.

## Detailed findings

### OI walls by strike (dte ≤ 30 — tradeable horizon) `[OI:oi_by_strike]`

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| 140 | 3,383 | 66 | +3,317 | call_wall_resistance | +17.7 |
| 145 | 3,274 | 49 | +3,225 | call_wall_resistance | +21.9 |
| **128** | 2,156 | 11 | +2,145 | call_wall_resistance | **+7.6** |
| 135 | 54 | 1,695 | −1,641 | put_heavy | +13.5 |
| 125 | 213 | 745 | −532 | put_heavy | +5.1 |
| **115** | 1 | 918 | −917 | put_wall_support | **−3.3** |
| 110 | 17 | 736 | −719 | put_wall_support | −7.5 |
| 120 | 121 | 601 | −480 | put_heavy | +0.9 |
| 147 | 676 | 0 | +676 | call_wall_resistance | +23.6 |
| 150 | 385 | 40 | +345 | call_wall_resistance | +26.1 |

**Nearest actionable levels around ~$119 spot: call resistance $128, put support
$115.** The 135 put_heavy (1,695 OI) is ITM-put standing OI, not a support level.
All-expiry aggregate adds a far LEAP wall at $180 (7,487 call OI, +51%) — the Nov
print's strike — plus $160/$260 LEAP calls; ignore for the tradeable horizon.

### OI term structure (OPEX cliffs) `[OI:term_structure]` (total_oi 36,112)

| Expiry | call_oi | put_oi | % of total OI |
|--------|---------|--------|---------------|
| **2026-07-17** (today) | 10,594 | 4,416 | **41.6%** (expiring) |
| **2026-10-16** | 5,792 | 1,691 | **20.7%** (call-heavy) |
| **2026-08-21** | 3,721 | 2,206 | **16.4%** (post-earnings) |
| 2026-11-20 | 3,181 | 15 | 8.9% (180C LEAP) |
| 2026-12-18 | 402 | 44 | 1.2% |
| 2026-07-24 | 406 | 803 | 3.4% (put-lean) |
| 2026-07-31 | 65 | 653 | 2.0% (put-lean) |
| 2028-12-15 | 685 | 4 | 1.9% (LEAP) |

After today's 41.6% rolls off, the forward gravity wells are **10/16 (20.7%)** and
**8/21 (16.4%)** — the latter is the first monthly *after* the 8/4 earnings, the
expiry phase-4/9 must size against. Both call-dominant in standing OI.

### Largest OI increases `[OI:biggest_increases]` (threshold lowered to 50 — nothing ≥500)

| Contract | side | OI Δ | vol |
|----------|------|------|-----|
| DOCN 2026-08-21 $145 C | call | **+206** | 279 |
| DOCN 2026-07-24 $100 C | call | +59 | 59 |

`smart-positioning` returned the same two rows (no directional tag). Both small,
upside calls — mild speculative interest, **not structural.**

### Closing / roll activity `[OI:decrease_with_volume]`

| Contract | OI Δ | vol | Read |
|----------|------|-----|------|
| 2026-07-17 $145 P | −604 | 2,433 | expiry roll-off (0DTE) |
| **2026-11-20 $180 C** | **−430** | 475 | **phase-1 $985K ask was closing/roll** |
| 2026-07-17 $150 P | −194 | 940 | expiry roll-off |
| 2026-07-17 $152.5 P | −112 | 488 | expiry roll-off |
| 2026-07-17 $114 P | −95 | 596 | expiry roll-off |
| 2026-07-17 $120 P | −91 | 907 | expiry roll-off |

`position-rolls` (single-day): **0 detected** (cross-session rolls not captured).

### Pin risk & OPEX concentration

- `pin-risk --dte-max 7 --max-distance-pct 5`: **DOCN absent** — not a top pin
  candidate even on 0DTE 7/17.
- `opex-concentration --min-concentration-pct 40`: **DOCN absent** (its 41.6%
  7/17 concentration is expiring-day and DOCN isn't in the market-wide top-20).

### OI build as % of float (advisory) `[OI:oi_pct_float fz]`

fz float null → derived ~104M shares (phase-2). Largest build 206 contracts ×100 =
20,600 share-equiv = **0.02% of shares** — negligible; confirms no structural bet.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `oi oi-by-strike --dte-max 30` | 128C wall 2,156 / 115P wall 918 ← `.results[].{call_oi,put_oi,role}` | 10 |
| `oi term-structure` | 10/16 20.7%, 8/21 16.4% ← `.term_structure[].pct_of_total_oi` | 16 exp |
| `oi biggest-increases --min-oi-change 50` | max +206 145C Aug ← `.results[0].oi_diff_plain` | 2 |
| `oi decrease-with-volume --min-volume 100` | 180C Nov −430 ← `.results[].oi_diff_plain` (select 180C) | 6 |
| `oi smart-positioning --min-oi-change 50` | same 2 rows, no dir | 2 |
| `oi position-rolls --threshold 500` | 0 rolls ← `.rolls_detected` | 0 |
| `oi pin-risk / opex-concentration` (mkt-wide) | DOCN absent both | — |

## Tool errors

(none — all calls returned valid JSON. `biggest-increases`/`smart-positioning`
were empty at the default ≥500 threshold; re-run at ≥50 to surface the real,
small builds — recorded as a threshold choice, not an error.)

## DATA NOTE / CORRECTION

- **Cross-phase correction:** phase-1 read the 180C Nov-20 $985K ask sweep as a
  bullish opening. Phase-3 `decrease-with-volume` shows **OI Δ −430** for that exact
  contract → the aggressive buying **reduced** open interest (buy-to-close / roll),
  so it is **not** fresh bullish conviction. Phase-9/10 must weight the bullish
  tilt down accordingly. (vol 475 here vs size 795 in phase-1's top-premium view —
  different aggregations; the OI delta is the authoritative "opened vs closed" read.)

## Verdict for downstream phases

- **Positioning bias:** **Mixed / no fresh conviction.** Standing forward OI is
  call-heavy (10/16, 8/21, 11/20), but today's marginal flow was call-*writing*
  (phase-1) and the biggest call print was OI-reducing — the skew is not cleanly
  bullish. No structural new build (max +206).
- **Conviction:** **2/5.**
- **Largest OI build as % of float:** ≈**0.02%** (derived) — not structural.
- **Three pin/cliff strikes for phase-9** (from `oi_by_strike` roles + term cliff):
  1. **Call resistance $128** (nearest, 2,156 OI) → then $140/$145 wall band.
  2. **Put support $115** (put_wall, 918 OI) → then $110.
  3. **OPEX gravity 8/21** (16.4%, first post-earnings monthly) & **10/16** (20.7%).
- **Open questions:** Is the call-heavy 8/21 OI (3,721 calls) speculative upside or
  covered/written against stock (phase-1 showed 140C/150C sold at bid)? Does phase-4
  max-pain confirm a pin near $119–120? (phase-4.)
