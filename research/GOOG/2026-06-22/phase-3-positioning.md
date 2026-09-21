# Phase 3 — Open Interest & Positioning

**Ticker:** GOOG
**As-of date:** 2026-06-22
**Generated:** 2026-06-22
**Upstream phases cited:** phase-0-intake.md (Shs Float 5.07B), phase-1-flow.md, phase-2-dark-pool.md

## Summary

Fresh open interest is being built **almost entirely in upside calls, $370–410**,
across the 6/26, 7/2, 7/17 and 8/21 expiries — and it concentrates at the **7/17 OPEX
cliff, which holds 19.94% of all GOOG OI (the gravity well) and is call-heavy (P/C
0.559)**. The biggest single build is **7/2 $370C +5,216 contracts** (vol 6,866), with
7/17 385C (+3,777), 6/26 375C (+3,515), 7/17 370C (+2,375) and 7/17 410C (+2,197)
right behind. The only meaningful **put** build is a **7/17 $350C ATM put +2,006**
(hedge/short), and a **7/17 $320P is being *closed* (−2,245)** — i.e. a downside hedge
coming *off*. `smart-positioning` tags the builds **mixed** (some 370/385 calls
bullish-bought, some 375/8-21 370 calls bearish-written), which reads as **speculative
near-dated call buying layered with covered-call writing** against phase-2's mega-tier
accumulation. Net: **constructive, upside-leaning positioning toward $370+** (right into
the dark-pool overhead supply at $362–371), but two-sided and modest in size — **no
acute pin** (outside pin-risk top-25), **no ≥40% single-expiry cliff** (outside
opex-concentration), and **no near→far rolls**. Conviction 3.

## Key signals

- **7/17 is the OPEX gravity well — 19.94% of total OI** (call 141,814 / put 79,300,
  P/C 0.559), and fresh call OI is building right into it `[OI:term_structure]`
- Largest fresh build **7/2 $370C +5,216** (vol 6,866); upside calls $370–410 dominate
  the top-15 increases `[OI:biggest_increases]`
- Only notable put build **7/17 $350C-ATM-put +2,006**; **7/17 $320P closed −2,245**
  (downside hedge removed → mild bullish) `[OI:biggest_increases]` `[OI:decrease_with_volume]`
- Near-term (DTE≤30) **$350 wall is put-heavy at spot (net −5,400)** = battleground;
  call resistance stacked **$370/375/380/385/400/410** `[OI:oi_by_strike]`
- All-expiry **put-wall support $330 (net −30,223)** and **$340 (net −13,215)**;
  `smart-positioning` direction **mixed** (buying + writing) `[OI:oi_by_strike]` `[OI:smart_positioning]`

## Detailed findings

### OI walls by strike (`oi-by-strike`) — resistance/support map

**All-expiry aggregate:**

| Strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| 400 | 56,473 | 5,560 | **+50,913** | call_wall_resistance | +14.7 (LEAP) |
| 380 | 28,245 | 19,608 | +8,637 | call_wall_resistance | +8.96 |
| 375 | 25,767 | 14,827 | +10,940 | call_wall_resistance | +7.53 |
| **370** | 29,605 | 11,814 | **+17,791** | call_wall_resistance | +6.09 |
| **350** | 36,794 | 34,936 | **+1,858** | call_wall_resistance | **+0.36 (at spot — 2-sided battleground)** |
| **340** | 13,882 | 27,097 | **−13,215** | put_wall_support | −2.51 |
| **330** | 11,191 | 41,414 | **−30,223** | put_wall_support | −5.37 |
| 300 | 18,355 | 29,677 | −11,322 | put_wall_support | −13.98 |

**DTE≤30 (tradeable horizon):** the at-spot **$350 flips to `put_heavy` (call 7,688 /
put 13,088, net −5,400)** in the near term, with the call wall reasserting at
**$370 (+6,117) / 380 / 385 / 400 / 410**. So for the next month, $350 is a
**pivot/battleground**, supply begins at **$370**, and downside structural support is
**$340 → $330**.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

Total OI 1,108,861 across 18 expiries.

| Expiry | DTE | call_oi | put_oi | P/C | **% of total OI** |
|--------|-----|---------|--------|-----|-------------------|
| **2026-07-17** | 25 | 141,814 | 79,300 | 0.559 | **19.94 ← gravity well** |
| 2026-09-18 | 88 | 96,940 | 80,527 | 0.831 | 16.00 |
| 2027-01-15 | 207 | 108,301 | 62,515 | 0.577 | 15.40 (LEAP) |
| 2026-08-21 | 60 | 57,191 | 59,011 | 1.032 | 10.48 (only put-heavy major) |
| 2026-12-18 | 179 | 52,680 | 39,595 | 0.752 | 8.32 |
| 2026-06-26 | 4 | 58,774 | 28,906 | 0.492 | 7.91 (this week, very call-heavy) |

The **7/17 cliff (19.94%) is the dominant OPEX magnet** for the tradeable horizon —
call-heavy and accumulating fresh upside calls. Cross-check vs phase-4 max-pain and
phase-6 catalyst calendar (earnings 7/22 is *after* 7/17 opex). 8/21 is the one
put-heavy major expiry (P/C 1.03).

### Largest OI increases (fresh positioning) `[OI:biggest_increases]`

| Contract | OI Δ | vol | read |
|----------|------|-----|------|
| 7/2 370C | **+5,216** | 6,866 | upside call build |
| 8/21 370C | +4,417 | 5,246 | (smart-pos: written/bearish) |
| 7/17 385C | +3,777 | 6,609 | upside call build |
| 6/26 375C | +3,515 | 5,829 | (smart-pos: written/bearish) |
| 7/17 370C | +2,375 | 3,159 | upside call build |
| 7/17 410C | +2,197 | 5,217 | far-OTM call build |
| **7/17 350P** | **+2,006** | 3,698 | ATM put (hedge/short) |
| 6/26 372.5C / 377.5C / 385C / 370C | +1,169 / +1,040 / +998 / +986 | — | this-week upside calls |

Overwhelmingly calls $370–410. The single put build of size is the 7/17 350P.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

- **7/17 $320P −2,245** (vol 4,090) — a downside put hedge being *removed* (mild
  bullish). Other decreases are tiny (7/2 360P −210, 9/18 340C −204, LEAP puts −100s).
- `position-rolls` (threshold 500, near-dte≤30): **0 rolls**. (Phase-1's 2027 deep-ITM
  call adjustment was *intra-expiry* strike-to-strike, so it isn't flagged as a
  near→far roll.)

### Smart positioning (inferred direction) `[OI:smart_positioning]`

Direction tags are **mixed**: 7/2 370C / 7/17 385C·370C·410C inferred **bullish**
(bought); 8/21 370C / 6/26 375C / 7/17 350P inferred **bearish** (call-writing /
put-build). Read together with phase-2: institutions are **accumulating stock (mega DP
buy 0.764) while writing some upside calls and buying near-dated calls** — a
covered-call-overlay-plus-speculative-call-buying signature, net constructive but with
written upside capping conviction. (Dual-class parse verified: `GOOG260702C00370000` →
2026-07-02 / Call / 370 — `option_type_inferred` correct for Class C.)

### Pin risk / OPEX concentration

- `pin-risk` (dte≤7, ≤5% from spot): **GOOG outside top-25** — 4 days from 6/26 but no
  acute single-strike pin. Skip pin commentary.
- `opex-concentration` (≥40%): **GOOG outside top-20** — OI is spread across 18
  expiries (max 19.94% at 7/17), no extreme cliff.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|--------------------|------|
| `uw oi term-structure --symbol GOOG --date 2026-06-22 --json` | 7/17 pct_of_total_oi=19.94, P/C 0.559 ← `.term_structure[]` | 18 exp |
| `uw oi oi-by-strike --symbol GOOG --top-n 10 --date 2026-06-22 --json` | 350 net_oi +1,858 (at spot); 330 net −30,223 ← `.results[].net_oi` | 10 |
| `uw oi oi-by-strike --symbol GOOG --top-n 10 --dte-max 30 --json` | 350 net_oi −5,400 (put_heavy near-term) | 10 |
| `uw oi biggest-increases --symbol GOOG --top-n 20 --min-oi-change 500 --date 2026-06-22 --json` | 7/2 370C oi_diff_plain +5,216 ← `.results[].oi_diff_plain` | 20 |
| `uw oi decrease-with-volume --symbol GOOG --top-n 15 --min-volume 100 --date 2026-06-22 --json` | 7/17 320P −2,245 | 15 |
| `uw oi smart-positioning --symbol GOOG --top-n 20 --min-oi-change 500 --date 2026-06-22 --json` | mixed dir tags ← `.results[].inferred_direction` | 20 |
| `uw oi position-rolls --symbol GOOG --threshold 500 --near-dte-max 30 --date 2026-06-22 --json` | 0 rolls | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-22 --json` | GOOG outside top-25 | 25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-22 --json` | GOOG outside top-20 | 20 |
| (float) phase-0 Shs Float 5.07B | 5,216 ctr ×100 = 521,600 sh = 0.0103% float | — |

## Tool errors

None. All nine reads round-tripped through `jq`.

## DATA NOTE / CORRECTION

First-read term-structure jq used wrong field names (`.expiry`/`.pct_of_total_oi` at top
level) and returned empty; re-queried the correct path `.term_structure[]` — values
(7/17 = 19.94%) verified against the validated JSON. No number was transcribed from the
empty first attempt.

## Verdict for downstream phases

- **Bias from this phase:** **Calls being built (upside, $370–410), constructive** —
  fresh call OI concentrated at the call-heavy 7/17 OPEX cliff; downside hedge (320P)
  coming off. Tempered by visible **call writing** (covered overlay) and an ATM
  7/17 350P build, so it is upside-leaning, not one-way.
- **Conviction:** **3 / 5.** Genuine fresh call accumulation toward $370+, aligned with
  phases 1–2, but two-sided (writing present), modest size, and the target ($370) sits
  +6% away into overhead DP supply.
- **Largest OI build as % of float:** 5,216 contracts = 521,600 sh = **0.0103% of the
  5.07B float** — *not* structural as size; the signal is the **direction and the 7/17
  concentration**, not magnitude. (advisory `[OI:oi_pct_float fz]`)
- **Three pin/cliff strikes for phase-9** (sourced from roles, not hand-picked):
  1. **$350 — pivot/battleground** (`call_wall_resistance` all-expiry net +1,858 but
     `put_heavy` net −5,400 near-term; at spot +0.36%). The line in the sand.
  2. **$370 — first call-wall resistance / OPEX magnet** (net +17,791; fresh 7/2+7/17
     370C builds; coincides with the 7/17 19.94% cliff AND phase-2 DP supply $362–371).
  3. **$330–340 — put-wall support / stop reference** (340 net −13,215; **330 net
     −30,223**, the strongest put wall). 
- **Open questions:** Is the $370–410 call build speculative upside or covered-call
  writing against the phase-2 accumulation (smart-positioning says *both*)? Does
  phase-4 max-pain sit near $350 (pinning to spot) or pull toward the 7/17 call-heavy
  370 zone? Resolve dealer gamma sign at $350 in phase-4.
