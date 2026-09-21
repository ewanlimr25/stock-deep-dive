# Phase 3 — Open Interest & Positioning

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:05:38Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

PATH's positioning is **structurally bullish on a long horizon but near-term balanced**.
The OI gravity well is the **2027-01-15 LEAP, holding 34.5% of all 632,207 OI**, heavily
call-skewed (call 152,629 vs put 65,597, P/C 0.43); the 2028-01-21 LEAP is even more
call-heavy (P/C 0.15). That long-dated call base confirms phase-1's LEAP call buying. But
**today's OI changes are tiny and mixed** — the largest single build is +704 contracts
(**0.018% of float**, not structural) and `smart-positioning` splits bullish/bearish across
the top builds. Near-term structure: **$10 is a put-wall support** (−2.72%), first call
resistance is **$11 (+7%)**, then a heavy **$12 call wall (+16.7%)**. PATH is **not a pin
candidate** for OPEX and absent from opex-concentration — the OI cliff is the far LEAP, not
a near-term level.

## Key signals

- **2027-01-15 LEAP = OI gravity well:** 34.52% of total OI (call 152,629 / put 65,597,
  P/C 0.43) — long-dated bullish call base [OI:term_structure].
- **$10 put-wall support:** net_oi −14,161 (DTE≤30), role `put_wall_support`, −2.72% from
  spot [OI:oi_by_strike].
- **$12 heavy call wall:** net_oi +32,644 (DTE≤30), role `call_wall_resistance`, +16.7%;
  $11 first resistance (+7%, net +2,791, two-sided) [OI:oi_by_strike].
- **Builds tiny & mixed:** top OI Δ +704 (July $10 puts, sold→bullish per smart-pos);
  +674 ($12.50 6/26 calls); +620 ($20 LEAP calls, bought→bullish) [OI:biggest_increases][OI:smart_positioning].
- **No rolls, not a pin name:** rolls_detected 0; PATH absent from pin-risk and
  opex-concentration despite 1 day to monthly OPEX [OI:position_rolls][OI:pin_risk][OI:opex_concentration].

## Detailed findings

### OI walls by strike (DTE≤30, tradeable horizon; spot $10.27) — `[OI:oi_by_strike]`

| strike | call_oi | put_oi | net_oi | role | dist% |
|--------|---------|--------|--------|------|-------|
| $9 | 400 | 11,443 | −11,043 | put_wall_support | −12.45% |
| **$10** | 4,816 | 18,977 | **−14,161** | **put_wall_support** | **−2.72%** |
| $10.5 | 2,183 | 3,947 | −1,764 | put_heavy | +2.14% |
| **$11** | 14,150 | 11,359 | +2,791 | call_wall_resistance (two-sided) | +7% |
| $11.5 | 5,197 | 1,142 | +4,055 | call_wall_resistance | +11.87% |
| **$12** | 34,829 | 2,185 | **+32,644** | **call_wall_resistance** | +16.73% |
| $12.5 | 8,819 | 278 | +8,541 | call_wall_resistance | +21.6% |
| $13 | 27,149 | 257 | +26,892 | call_wall_resistance | +26.46% |
| $14 | 13,838 | 0 | +13,838 | call_wall_resistance | +36.19% |
| $15 | 21,623 | 3 | +21,620 | call_wall_resistance | +45.91% |

Spot sits just above the **$10 put-wall support**; first overhead is **$11** (two-sided),
the real call-OI mass is at **$12+** (well out of reach near-term). All-expiry view adds a
huge **$15 call wall** (call_oi 80,650) — a LEAP strike, not a tradeable near-term level.

### OI term structure (OPEX cliffs; total OI 632,207) — `[OI:term_structure]`

| expiry | DTE | call_oi | put_oi | P/C | % of total OI |
|--------|-----|---------|--------|-----|---------------|
| 2026-06-18 | 0 | 87,607 | 33,129 | 0.378 | 19.1% (expires today) |
| 2026-06-26 | 8 | 9,920 | 9,041 | 0.911 | 3.0% |
| 2026-07-17 | 29 | 37,650 | 10,254 | 0.272 | 7.58% |
| 2026-08-21 | 64 | 64,616 | 18,209 | 0.282 | 13.1% |
| 2026-09-18 | 92 | 29,028 | 9,346 | 0.322 | 6.07% |
| **2027-01-15** | 211 | **152,629** | 65,597 | 0.43 | **34.52% (gravity well)** |
| 2028-01-21 | 582 | 65,031 | 9,746 | 0.15 | 11.83% (very call-heavy) |

After today's 0DTE rolls off, the structure is dominated by the **2027-01-15 LEAP (34.5%)**
and the 2028 LEAP — both heavily call-skewed. Near-term tradeable cliffs: **8/21 (13.1%)**
and **7/17 (7.6%)**, both call-heavy (P/C 0.27–0.28).

### Largest OI increases (OPRA-parsed) — `[OI:biggest_increases]`

| contract | side/strike/expiry | OI Δ | vol | smart-pos read |
|----------|--------------------|------|-----|----------------|
| PATH260717P00010000 | $10 put, 7/17 | +704 | 759 | **bullish** (sold puts, net_ask_bid −305) |
| PATH260626C00012500 | $12.50 call, 6/26 | +674 | 748 | bearish (sold calls) |
| PATH260618P00010000 | $10 put, 0DTE | +640 | 2,182 | bearish (bought puts) |
| PATH270115C00020000 | $20 call, 2027 LEAP | +620 | 842 | bullish (bought calls) |
| PATH260618C00011000 | $11 call, 0DTE | +541 | 1,833 | bearish (sold calls) |

All builds ≤ 704 contracts — **not structural**. Mixed direction. Notably, the new July
$10 puts are **sold** (put-writing at the put wall = mildly bullish/support reinforcement).

### Closing / roll activity — `[OI:decrease_with_volume][OI:position_rolls]`

Decreases are small, led by 0DTE ITM $12 puts (−715, closing into expiry). `position-rolls`:
**0 detected** (single-day detection only — cross-session rolls not captured).

### Pin risk / OPEX concentration — `[OI:pin_risk][OI:opex_concentration]`

PATH **absent** from both lists. Despite 1 day to monthly OPEX, PATH is not a concentrated
pin candidate (its near-spot OI is split between the $10 put wall and dispersed call walls).
No pin commentary warranted.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|---------------------|------|
| `oi oi-by-strike --symbol PATH --dte-max 30 --date 2026-06-18` | $10 put-wall net −14,161; $12 call-wall +32,644 ← `.results[].{net_oi,role}` | 10 |
| `oi oi-by-strike --symbol PATH (all-expiry)` | $15 LEAP call wall 80,650 ← `.results[]` | 10 |
| `oi term-structure --symbol PATH --date 2026-06-18` | 2027-01-15 = 34.52% of 632,207 OI ← `.term_structure[]` | 14 exp |
| `oi biggest-increases --min-oi-change 500 --date 2026-06-18` | top +704 (7/17 $10P) ← `.results[].oi_diff_plain` + OPRA | 5 |
| `oi decrease-with-volume --date 2026-06-18` | $12P 0DTE −715 ← `.results[]` | rows |
| `oi smart-positioning --date 2026-06-18` | mixed dir ← `.results[].inferred_direction` | 5 |
| `oi position-rolls --threshold 500 --near-dte-max 30` | 0 rolls ← `.rolls_detected` | 0 |
| `oi pin-risk --dte-max 7 --max-distance-pct 5` | PATH absent | top-25 |
| `oi opex-concentration --min-concentration-pct 40` | PATH absent | top-20 |

## Tool errors

_none_

## DATA NOTE / CORRECTION

`term-structure` array is under `.term_structure` (not `.results`); first jq returned
empty, re-read with `.term_structure[]`. The chain lists a **2026-06-18 (0DTE)** expiry but
**no 2026-06-19** monthly — reported as the data returns it; the near-term gravity is the
0DTE rolling off today, the structural gravity is the 2027 LEAP. All values via `jq`.

## Verdict for downstream

- **Positioning bias:** **Long-term bullish (LEAP call base), near-term balanced.** Calls
  dominate every meaningful expiry (P/C 0.15–0.43); $10 put wall supports, $11–$12 call
  walls cap. Today's flow added no structural position.
- **Conviction:** **3/5** (durable long-dated call skew is real but slow; near-term builds
  tiny and mixed; not a pin name).
- **Largest OI build as % of float:** 704 contracts ≈ 70,400 sh = **0.018% of 391.72M float**
  — negligible, **not structural** for this name. [OI:oi_pct_float fz]
- **Three pin/cliff strikes for phase-9:**
  1. **$10 put-wall support** (net put OI −14,161, −2.72%) — primary near-term floor (aligns
     with phase-2 $10.23 DP support).
  2. **$11 call-wall resistance** (+7%, two-sided net +2,791) — first overhead cap.
  3. **$12 call-wall resistance** (net +32,644, +16.7%) — heavy call OI; upside magnet/cap if
     a move develops. OPEX cliff for the longer view: **2027-01-15 LEAP (34.5% of OI)**.
- **Open questions:** The long-dated call base is bullish but slow — is there a near-term
  catalyst to pull price toward the $11–$12 call walls (phase-6 calendar)? Is the persistent
  call buying (phase-1) speculative squeeze-positioning against 31.78% short float, or covered
  writing? The $10 put-selling + put-wall suggests support is being defended — resolve vs the
  balanced/distributive dark pool (phase-2) in the structure (phase-4) and gates (7b/7c).
