# Phase 3 — Open Interest & Positioning

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T12:05:00Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

The chain is **call-dominated with a hard $100 ceiling**. `oi-by-strike` shows
**$100 as the dominant call wall** (net_oi **+98,818** all-expiry, **+30,220**
near-term, only **+1.91%** above the $98.12 spot), with progressive call resistance
above at $105/$110/$120 and **no near-money put support** — put walls are far OTM
($75 at −23.6%, tail at $55–70). Term structure puts **25.2% of all OI at the 6/18
OPEX** (3 days out) — the gravity well. New builds are call-tilted (11 of 15 call
builds bought) but smart-positioning flags the **near-money $97C 6/18 as written**
(net_ask_bid −4,575) and the $100C as two-sided (−640): layered on phase-2's dark-pool
accumulation, this reads as **accumulate-stock + overwrite-near-money-calls + buy
far-OTM put tail hedges**, not one-way call buying. Bullish-tilted, but upside is
structurally capped at $100 into Friday.

## Key signals

- **$100 call wall** = primary resistance: net_oi +98,818 (all-exp), +30,220 (≤30d),
  +1.91% from spot `[OI:oi_by_strike]`.
- **6/18 OPEX = gravity well**: 25.2% of total OI (1,666,121), call 257,826 / put
  162,683, PC 0.63 `[OI:term_structure]`.
- Largest new build = **$55P 6/26 +16,506** (vol 16,568), bought on ask (net_ask_bid
  +16,504) → far-OTM tail hedge `[OI:biggest_increases][OI:smart_positioning]`.
- **Near-money call writing**: $97C 6/18 net_ask_bid −4,575 (written), $100C 6/18
  −640 (two-sided) → covered-call/overwrite signature with phase-2 accumulation
  `[OI:smart_positioning]`.
- Upside calls **bought**: $95C/$102C/$105C/$110C builds (call builds 11 bullish vs 4
  bearish) `[OI:smart_positioning]`.

## Detailed findings

### OI walls by strike `[OI:oi_by_strike]` (spot $98.12)

**Near-term (DTE ≤ 30, tradeable):**

| Strike | call_oi | put_oi | net_oi | role | dist |
|--------|---------|--------|--------|------|------|
| **$100** | 38,100 | 7,880 | **+30,220** | call_wall_resistance | +1.91% |
| $90 | 27,093 | 8,165 | +18,928 | call_heavy | −8.28% |
| $95 | 22,150 | 3,675 | +18,475 | call_heavy | −3.19% |
| $120 | 17,451 | 870 | +16,581 | call_wall_resistance | +22.29% |
| $110 | 17,427 | 2,488 | +14,939 | call_wall_resistance | +12.10% |
| $85 | 17,104 | 8,407 | +8,697 | call_heavy | −13.38% |
| $80 | 15,842 | 10,457 | +5,385 | call_heavy | −18.48% |
| $55 | 81 | 29,455 | −29,374 | put_wall_support | −43.95% |
| $70 | 4,534 | 18,546 | −14,012 | put_wall_support | −28.67% |
| $75 | 12,054 | 17,213 | −5,159 | put_wall_support | −23.57% |

**All-expiry** confirms $100 the giant wall (net +98,818, call 135k/put 36k), then
$105 (+54,244), $90 (+48,317), $95 (+38,502). Deep tail put walls $50–70.

Read: every strike from $80 to $120 is **call-heavy or a call wall** — even strikes
*below* spot. The only true put support is ≥23% OTM (tail hedges). So in OI terms
there is **no structural downside support near spot**; the near support is the
phase-2 dark-pool base ($92–93), not an OI put wall.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| Expiry | pct_of_total_oi | call_oi | put_oi | PC |
|--------|-----------------|---------|--------|----|
| **2026-06-18** | **25.2%** | 257,826 | 162,683 | 0.63 |
| 2026-07-17 | 13.9% | 163,409 | 69,341 | 0.42 |
| 2027-01-15 | 13.5% | 151,922 | 73,817 | 0.48 |
| 2026-08-21 | 8.9% | 74,323 | 74,242 | 0.99 |
| 2026-09-18 | 6.3% | 61,673 | 44,247 | 0.71 |

OPEX cliff = **6/18 (25.2%)** — cross-check with phase-4 max-pain (expect pin gravity
near $98–100). 7/17 (13.9%, PC 0.42) and the 1/15/27 LEAP (13.5%) are the next nodes;
both call-tilted, matching phase-1's 7/17 sweep concentration ($20M) and LEAP prints.

### Largest OI increases `[OI:biggest_increases]` (OPRA-parsed)

| Contract | Side | Expiry | Strike | OI Δ | Vol | dir (smart-pos) |
|----------|------|--------|--------|------|-----|-----------------|
| HOOD260626P00055000 | put | 6/26 | $55 | +16,506 | 16,568 | bought (tail hedge) |
| HOOD260618C00097000 | call | 6/18 | $97 | +7,040 | 8,254 | **written** (−4,575) |
| HOOD260618P00084000 | put | 6/18 | $84 | +4,556 | 4,939 | ~neutral |
| HOOD260618C00100000 | call | 6/18 | $100 | +3,883 | 32,906 | two-sided (−640) |
| HOOD260618C00095000 | call | 6/18 | $95 | +2,716 | 20,877 | bought (+1,907) |
| HOOD260702C00100000 | call | 7/02 | $100 | +2,695 | 3,631 | written (−2,519) |
| HOOD260618C00102000 | call | 6/18 | $102 | +2,271 | 5,256 | bought (+253) |
| HOOD270115C00140000 | call | 1/15/27 | $140 | +2,227 | 2,546 | LEAP call |
| HOOD260618C00110000 | call | 6/18 | $110 | +2,160 | 5,129 | OTM upside |

The $100C 6/18 build has vol 32,906 vs OI Δ 3,883 → heavy intraday churn (matches
phase-1 two-way $100C). Near-money $97C and 7/02 $100C are net-written.

### Closing / roll activity `[OI:decrease_with_volume][OI:position_rolls]`

Minor decreases only: $90C 6/26 −916, $100C 7/17 −667 (vol 12,572 = churn not unwind),
$80P 7/17 −651, $90C 7/02 −612. `position-rolls` returned **0 rows** — no near→far
rolling detected. No material unwind of the call base.

### Smart positioning `[OI:smart_positioning]`

Call builds **11 bullish / 4 bearish**; put builds **1 bullish / 4 bearish**. Net:
OTM calls bought (specs reach for upside), near-money calls written ($97/$100), puts
bought far-OTM as hedges. Coherent with phase-2 accumulation = covered-call overwrite +
tail protection.

### Pin risk / OPEX concentration `[OI:pin_risk][OI:opex_concentration]`

- HOOD **not** in market-wide pin-risk top-25 (dte-max 7) — no market-flagged extreme
  pin, but local $100-wall + 6/18 (25%) imply own-name gravity toward $98–100 Friday.
- HOOD **not** in opex-concentration top-20 (min 40%) — 6/18 at 25.2% is concentrated
  but below the 40% threshold; OI spread across 20 expiries.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq`/parse | Rows used |
|------------------|---------------------------|-----------|
| `uw oi oi-by-strike --symbol HOOD --top-n 10 --dte-max 30 --date 2026-06-15` | $100 net_oi +30,220 call_wall ← `.results[].net_oi/.role` | top-10 |
| `uw oi oi-by-strike --symbol HOOD --top-n 10 --date 2026-06-15` (all-exp) | $100 net_oi +98,818 | top-10 |
| `uw oi term-structure --symbol HOOD --date 2026-06-15` | 6/18 25.2% of 1,666,121 ← `.term_structure[].pct_of_total_oi` | 20 expiries |
| `uw oi biggest-increases --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-06-15` | $55P6/26 +16,506 ← `.oi_diff_plain`; side/expiry ← OPRA `option_symbol` | top-20 |
| `uw oi smart-positioning --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-06-15` | $97C net_ask_bid −4,575 (written); calls 11 bull/4 bear ← `.inferred_direction/.net_ask_bid` | top-20 |
| `uw oi decrease-with-volume --symbol HOOD --top-n 15 --min-volume 100 --date 2026-06-15` | minor decreases, $90C6/26 −916 | top-15 |
| `uw oi position-rolls --symbol HOOD --threshold 500 --near-dte-max 30 --date 2026-06-15` | 0 rows | 0 |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --json` | HOOD absent ← `select(.ticker=="HOOD")` empty | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --json` | HOOD absent | top-20 |

## Tool errors

(none — `pin-risk`/`opex-concentration` are market-wide; run without `--date`, latest
available oi date = 2026-06-15 = as-of, so as-of correct.)

## DATA NOTE / CORRECTION

- `biggest-increases` carries no `side`/`expiry` column — parsed both from OPRA
  `option_symbol` per the phase guidance (e.g. `HOOD260618C00097000` → 6/18 Call $97).
- `oi_diff_plain` used for the OI delta (not the fractional `oi_change` ratio).

## Verdict for downstream phases

- **Positioning bias:** **bullish-tilted but capped** — call OI dominates the whole
  chain (even sub-spot strikes are call-heavy), OTM upside calls are bought, but
  near-money $97–100 calls are written against accumulated stock (phase-2) and the
  **$100 wall + 6/18 gravity cap upside near-term**. Puts are far-OTM tail hedges,
  not aggressive bearish positioning → confirms phase-1/2 read that the puts are
  protective, not directional shorts.
- **Conviction:** **3 / 5** — clear call dominance and a clean wall map, but the $100
  ceiling and covered-call overwrite temper near-term upside.
- **Largest OI build as % of float:** **0.217%** ($55P 6/26 +16,506 ct ×100 =
  1.65M sh-equiv / 760.74M float) — small for this large-float name; the OI builds are
  not structurally outsized (advisory; do not raise conviction).
- **Three pin/cliff strikes for phase-9:**
  1. **$100 call_wall_resistance** (net_oi +30,220 near-term) — primary ceiling /
     breakout trigger; +1.91% from spot.
  2. **6/18 OPEX cliff** (25.2% of OI) — expect pin gravity $98–100 into Friday;
     resolve against phase-4 max-pain.
  3. **$75 put_wall_support** (nearest OI support, −23.6%) — but downside support near
     spot is structurally thin; lean on the phase-2 DP base **$92–93** as the real
     near support for stops.
- **Open questions:** Does phase-4 max-pain confirm a ~$98–100 pin for 6/18? Is the
  $97/$100 call writing covered (vs phase-2 accumulation) or naked? Does the 7/17
  call-tilt (PC 0.42) signal a post-OPEX upside continuation if $100 breaks?
