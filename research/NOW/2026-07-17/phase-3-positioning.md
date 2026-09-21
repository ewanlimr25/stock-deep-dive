# Phase 3 — Open Interest & Positioning

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **distributed and mixed with a faint neutral-to-bullish income
tilt — no structural directional bet.** OI spreads across 16 expiries with **no
single cliff** (largest is today's expiring 0DTE at 18%; NOW is absent from both
`pin-risk` and `opex-concentration` top lists). After 0DTE rolls off, the
tradeable-horizon gravity well is the **2026-08-21 monthly (17.4% of OI, P/C 0.74)**
— the first monthly after **earnings 7/22**. Today's single biggest new position is
a **7/24 $60-put, +15,010 contracts** (deep-OTM, −42% from spot), which
`smart-positioning` infers as **bullish (i.e. put-writing / premium collection)** —
directly corroborating phase-1's Jan-2027 bid-side put selling and phase-2's balanced
dark pool. Near-term walls: **$120 heaviest call resistance** (net +27,235 dte≤30),
**$110** call resistance, **$105/$100** two-sided battlegrounds bracketing spot, thin
**$95** put support. Net: mixed, conviction **2/5**.

## Key signals

- **Biggest build = 7/24 60-put +15,010c, inferred bullish (put-write)**
  `[OI:smart_positioning]` `[OI:biggest_increases NOW260724P00060000]`.
- **No OPEX cliff:** max single-expiry concentration 18% (0DTE, expiring); NOW not
  in `opex-concentration` (≥40%) or `pin-risk` top lists `[OI:opex_concentration]` `[OI:pin_risk]`.
- **Tradeable gravity well = 2026-08-21 monthly, 17.4% of OI, P/C 0.74**
  `[OI:term_structure]`.
- **Near-term call wall $120** (net_oi +27,235, dte≤30) = upside cap; **$110** next
  resistance `[OI:oi_by_strike dte<=30]`.
- **$105/$100 are two-sided battlegrounds, not clean walls** ($105 net −93 put_heavy;
  $100 net +8,958 call_heavy) bracketing spot `[OI:oi_by_strike]`.

## Detailed findings

### OI walls by strike (all-expiry) `[OI:oi_by_strike]`

Spot $103.24. (net_oi = call_oi − put_oi)

| strike | call_oi | put_oi | net_oi | role | dist% |
|---|---|---|---|---|---|
| 85 | 4,302 | 42,200 | −37,898 | put_wall_support | −17.8% |
| 90 | 15,019 | 41,341 | −26,322 | put_wall_support | −13.0% |
| 95 | 11,300 | 28,791 | −17,491 | put_wall_support | −8.1% |
| **100** | 53,267 | 57,146 | −3,879 | put_wall_support | **−3.3%** |
| **105** | 31,768 | 21,693 | +10,075 | call_wall_resistance | **+1.6%** |
| **110** | 54,313 | 35,834 | +18,479 | call_wall_resistance | **+6.4%** |
| **120** | 68,257 | 15,326 | +52,931 | call_wall_resistance | +16.1% |
| 130 | 51,191 | 1,043 | +50,148 | call_wall_resistance | +25.7% |
| 140 | 40,506 | 4,901 | +35,605 | call_wall_resistance | +35.4% |
| 150 | 61,264 | 0 | +61,264 | call_wall_resistance | +45.1% |

### OI walls — tradeable horizon (dte ≤ 30) `[OI:oi_by_strike dte<=30]`

| strike | net_oi | role | dist% |
|---|---|---|---|
| **120** | **+27,235** | call_wall_resistance | +16.1% (heaviest near-term) |
| 130 | +23,040 | call_wall_resistance | +25.7% |
| 125 | +12,785 | call_wall_resistance | +20.9% |
| **110** | +12,587 | call_wall_resistance | +6.4% |
| 115 | +14,516 | call_wall_resistance | +11.2% |
| **100** | +8,958 | call_heavy (two-sided) | −3.3% |
| **105** | −93 | put_heavy (two-sided, ~spot) | +1.6% |
| 95 | −2,326 | put_wall_support | −8.1% |
| 60 | −15,021 | put_wall_support | −42.0% (the +15,010 build) |

Near-term structure is **call-resistance-heavy above spot** ($110→$120 wall stack),
**thin genuine put support** ($95 only −2,326 near-term), and two-sided churn at
$100/$105 around spot.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

total_oi 1,174,405 across 16 expiries. Top by pct_of_total_oi:

| expiry | dte | total_oi | P/C | % of total |
|---|---|---|---|---|
| 2026-07-17 | 0 | 212,101 | 0.42 | **18.0%** (expiring today — rolling off) |
| **2026-08-21** | 35 | 205,382 | 0.74 | **17.4%** ← tradeable gravity well |
| 2027-01-15 | 182 | 154,694 | 0.60 | 13.1% (LEAP — phase-1 bid-side puts live here) |
| 2026-09-18 | 63 | 102,251 | 0.78 | 8.7% |
| 2028-01-21 | 553 | 100,902 | 0.41 | 8.5% (LEAP) |
| 2026-07-24 | 7 | 87,315 | 0.96 | 7.4% (first post-earnings weekly) |

No dominant cliff — OI is spread. The **8/21 monthly** is the standing anchor;
**7/24** is the immediate post-earnings weekly to watch. Cross-check 8/21 vs phase-4
max-pain.

### Largest OI increases (parsed from option_symbol) `[OI:biggest_increases]`

| contract | expiry | side | strike | OI Δ | vol |
|---|---|---|---|---|---|
| NOW260724P00060000 | 7/24 | Put | 60 | **+15,010** | 15,010 |
| NOW260731C00140000 | 7/31 | Call | 140 | +2,829 | 3,240 |
| NOW260821C00105000 | 8/21 | Call | 105 | +2,212 | 2,874 |
| NOW260821C00130000 | 8/21 | Call | 130 | +1,993 | 2,573 |
| NOW260724P00075000 | 7/24 | Put | 75 | +1,732 | 1,908 |
| (rest: 0DTE 7/17 C108/C101/P104/C103/C106 — expiry-day churn, discount) | | | | | |

Standout: **7/24 60-put +15,010** — deep-OTM (−42%), 2 days post-earnings. Inferred
bullish (put-write / premium harvest) — but so far OTM it is equally a **cheap
crash-tail hedge through earnings** (~$0.05–0.15 → ~$75k–225k). Secondary builds are
OTM calls (8/21 105/130, 7/31 140) and a small 7/24 75-put.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

Decreases are almost entirely **0DTE 7/17** expiring (120P −4,912, 125C −1,631,
106P −1,229, 130C −1,065) plus a real **7/24 92-put −1,084** close. `position-rolls`
returned **0 rows** — no material near→far rolling detected.

### Smart positioning (inferred) `[OI:smart_positioning]`

MIXED. Biggest (60-put +15,010) = **bullish** (put-write). Remainder split:
105C 8/21 bullish, 130C 8/21 bearish (call-write), 140C 7/31 bearish, 101C 0DTE
bearish, 104P 0DTE bullish. No coherent one-sided campaign — consistent with the
delta-neutral phase-1 tape.

### Pin risk / OPEX concentration

**NOT in pin-risk top-25** (dte≤7, ≤5% distance) and **NOT in opex-concentration
top-20** (≥40%). Despite 0DTE today, spot $103.24 sits between the $100/$105
battlegrounds with no heavy single-strike pin. No pin commentary warranted.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|---|---|---|
| `uw oi oi-by-strike --symbol NOW --top-n 10` | $120 call wall net +52,931; $100 put support ← `.results[].net_oi/.role` | 10 |
| `uw oi oi-by-strike --symbol NOW --dte-max 30` | $120 near-term net +27,235; $105 two-sided ← `.results[]` | 10 |
| `uw oi term-structure --symbol NOW` | 8/21=17.4%, 7/24=7.4%, total_oi 1,174,405 ← `.term_structure[].pct_of_total_oi` | 16 exp |
| `uw oi biggest-increases --symbol NOW --min-oi-change 500` | 7/24 60P +15,010 ← `.results[].oi_diff_plain` + `option_symbol` parse | 13 |
| `uw oi decrease-with-volume --symbol NOW --min-volume 100` | 0DTE churn + 7/24 92P −1,084 ← `.results[]` | 15 |
| `uw oi smart-positioning --symbol NOW --min-oi-change 500` | 60P build inferred bullish; mixed ← `.results[].inferred_direction` | 13 |
| `uw oi position-rolls --symbol NOW --threshold 500 --near-dte-max 30` | 0 rows ← `.results` | 0 |
| `uw oi pin-risk --dte-max 7 --max-distance-pct 5` | NOW absent ← filter `.ticker=="NOW"` | top-25 |
| `uw oi opex-concentration --min-concentration-pct 40` | NOW absent ← filter | top-20 |

## Tool errors

- Initial term-structure jq multiplied a null `pct_of_total_oi` in a mis-sorted path;
  the field is present and valid per-entry (`.term_structure[].pct_of_total_oi`).
  Re-read cleanly — no bad number persisted (see DATA NOTE).

## DATA NOTE / CORRECTION

First term-structure pass computed pct via a null-prone expression and hit a jq
`null*number` error; corrected to the native `.pct_of_total_oi` field
(8/21 = 17.4%, 0DTE = 18.0%) before transcribing. No wrong value written.

## Verdict for downstream

- **Positioning bias:** **Mixed, faint neutral-to-bullish income tilt.** Dominant
  new position is put-writing (7/24 60P +15,010, inferred bullish); OTM call builds
  are modest; no directional structural bet; OI distributed.
- **Conviction:** **2 / 5.**
- **Largest OI build as % of float (advisory, ESTIMATE):** 15,010c × 100 =
  1,501,000 share-equiv ÷ ~2.07B est. float ≈ **~0.07%** — **immaterial for this
  name.** `[OI:oi_pct_float fz]` (`fz` float unavailable; est. only — verify 7b/7c).
- **Three pin/cliff strikes for phase-9 (from roles + term-structure):**
  1. **$110 call_wall_resistance** (+6.4%, net +12,587 near-term) — first hard cap.
  2. **$120 call_wall_resistance** (+16.1%, net +27,235 — heaviest near-term) —
     upside ceiling / target-zone cap.
  3. **$100 put_wall_support** (−3.3%, net −3,879 all-expiry) — downside pin/stop
     reference; **OPEX cliff = 2026-08-21 monthly (17.4%)** is the horizon anchor.
- **Open questions:** Is the 60-put +15,010 a put-write (bullish) or a tail hedge
  (bearish-defensive)? Its far-OTM strike argues cheap-hedge; delta-neutral phase-1
  argues income. Does phase-4 max-pain sit at/near the $105 battleground or the 8/21
  anchor? Does phase-4 GEX show dealers long/short gamma around $103–105?
