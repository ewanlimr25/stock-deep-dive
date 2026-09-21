# Phase 3 — Open Interest & Positioning

**Ticker:** PATH · **As-of:** 2026-07-22 · **Underlying:** $10.53 · **Generated:** 2026-07-22
**Upstream:** phase-1-flow.md (open Q: are Dec-$12 calls closed or written?), phase-2-dark-pool.md ($12 overhead supply)

## Summary

Standing positioning is **structurally bullish but slow** — the option chain is
**LEAP-dominated**, with **41.2% of all OI at 2027-01-15** (128,500 calls vs 79,420
puts) and heavy call OI stacked at $12/$13/$14/$15/$17/$20 (all net-long calls). That
is where the 5-day bullish sweep campaign lives. **Today's marginal OI change,
however, is negligible and mixed**: the only two builds above 500 are a small **put
write at $11 (8/21, +898)** and a **cheap $13 call lotto (7/24, +598)**; the biggest
decreases are small Aug-21 $12/$13 call *closes*. Critically, the **$893k Dec-$12
call sweep from phase-1 did NOT register a large OI shift** (no Dec-18 C12 row in the
top increases or decreases), which — pending the T+1 OI lag caveat — argues it was
**closing/matched (profit-take), not a fresh structural short**. No pin risk, no OPEX
concentration flag, no rolls near-term.

## Key signals

- **OPEX cliff = 2027-01-15, 41.2% of total OI** (call 128,500 / put 79,420, P/C 0.62) — the structural bullish LEAP base `[OI:term_structure]`.
- **Near-term cliff = 2026-08-21, 16.2% of OI, call-heavy** (P/C 0.392, call 58,540 / put 22,946) `[OI:term_structure]`.
- **$12 = call-wall resistance** (call_oi 53,129, net_oi +28,468, 12.1% OTM) — coincides with phase-2's $12 dark-pool overhead supply `[OI:oi_by_strike]`.
- **Today's only OI builds are tiny & bullish-leaning** — $11 put +898 (net-sold → put write) and $13 call +598 (net-bought ask), both inferred bullish `[OI:biggest_increases]` `[OI:smart_positioning]`.
- **Small call *closing* in Aug-21 $12/$13** (−561 / −243) — mild de-risking of near-term upside `[OI:decrease_with_volume]`.
- **No pin-risk / no opex-concentration / no rolls for PATH** (all market-wide scans returned PATH-empty) `[OI:pin_risk]` `[OI:opex_concentration]` `[OI:position_rolls]`.

## Detailed findings

### OI walls by strike — tradeable horizon (≤30 DTE) `[OI:oi_by_strike]`

| strike | call_oi | put_oi | net_oi | role | dist% |
|---|---|---|---|---|---|
| $8.5 | 18 | 13,076 | −13,058 | put_wall_support | −20.6% |
| $9 | 0 | 7,539 | −7,539 | put_wall_support | −15.9% |
| $10 | 3,137 | 4,852 | −1,715 | put_wall_support | −6.6% |
| **$11** | 7,539 | 7,242 | **+297** | (two-sided battleground) | +2.8% |
| $12 | 15,028 | 5,413 | +9,615 | call_wall_resistance | +12.1% |
| $12.5 | 5,434 | 543 | +4,891 | call_wall_resistance | +16.8% |
| $13 | 14,136 | 856 | +13,280 | call_wall_resistance | +21.4% |
| $14 | 15,035 | 559 | +14,476 | call_wall_resistance | +30.8% |
| $15 | 12,670 | 1,670 | +11,000 | call_wall_resistance | +40.1% |

$11 is tagged `call_wall_resistance` but net_oi is only **+297** (call 7,539 ≈ put
7,242) — a **true two-sided battleground / pin**, not a clean wall; it sits nearest
spot (+2.8%). Real overhead resistance begins at **$12**. Support ladder: **$10 →
$9 → $8.5** puts (the near-ATM 10.5 puts bought in phase-1 sit just above the $10 wall).

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| expiry | dte | call_oi | put_oi | P/C | % of total OI |
|---|---|---|---|---|---|
| **2027-01-15** | 177 | 128,500 | 79,420 | 0.62 | **41.2%** |
| 2026-08-21 | 30 | 58,540 | 22,946 | 0.39 | 16.2% |
| 2028-01-21 | 548 | 47,729 | 4,279 | 0.09 | 10.3% |
| 2026-09-18 | 58 | 32,290 | 19,648 | 0.61 | 10.3% |
| 2026-07-24 | 2 | 20,809 | 12,475 | 0.60 | 6.6% |
| 2026-12-18 | 149 | 26,499 | 3,252 | 0.12 | 5.9% |
| 2026-07-31 | 9 | 10,595 | 9,523 | 0.90 | 4.0% |

The gravity well is **Jan-2027 (41.2%)** — deep-liquidity LEAP expiry, moderately
call-tilted. Near-term, **8/21 (16.2%) is strongly call-heavy** (P/C 0.39). Note
**7/31 is the only near expiry that is balanced/put-leaning (P/C 0.90)** — where the
fresh put buying is landing. Cross-check the 8/21 call cliff against phase-4 max-pain.

### Largest OI increases `[OI:biggest_increases]` (option_symbol parsed)

| option_symbol | expiry / type / strike | OI Δ | vol | read |
|---|---|---|---|---|
| PATH260821P00011000 | 2026-08-21 PUT $11 | +898 | 1,082 | put WRITE (net_ask_bid −174) |
| PATH260724C00013000 | 2026-07-24 CALL $13 | +598 | 2,607 | event call lotto (net_ask_bid +325) |

Both below any structural threshold. **Largest OI build as % of float:** +898 ct ×100 =
89,800 sh ≈ **0.017% of ~526M shares out** — negligible (exact float n/a, phase-0).
For contrast the standing Jan-2027 call OI (128,500 ct = 12.85M sh ≈ **2.4% of shares
out**) is the only structurally meaningful positioning.

### Closing / roll activity `[OI:decrease_with_volume]` `[OI:position_rolls]`

Top decreases are small near-term **call closes**: Aug-21 C12 −561, Aug-21 C13 −243,
Jul-31 C13.5 −258, plus a Dec-2028 P12 −199. `position-rolls` returned **empty**
(no near→far rolls above the 500 threshold). No large roll signature.

### Smart positioning `[OI:smart_positioning]`

Both marginal builds inferred **bullish**: the $11 put via net-sold (writing) and the
$13 call via net-bought. Directionally these are small bullish tags; the tool's
inference on the dual-class-adjacent PATH symbol was spot-checked against the
option_symbol parse and matches.

### Pin risk / OPEX concentration

`pin-risk` (dte-max 7, ≤5% distance) → **PATH empty** (no near-strike pin candidate).
`opex-concentration` (≥40% single-strike) → **PATH empty**. Nothing to pin the 7/24 or
7/31 tape to a single strike within the tradeable band.

## Tool calls (audit)

| Datapoint | Command | jq path |
|---|---|---|
| walls (all-exp) | `uw oi oi-by-strike --symbol PATH --top-n 10 --json` | `.results[].{strike,call_oi,put_oi,net_oi,role,distance_pct}` |
| walls (≤30 DTE) | `uw oi oi-by-strike --symbol PATH --top-n 10 --dte-max 30 --json` | same |
| term structure | `uw oi term-structure --symbol PATH --json` | `.term_structure[].{expiry,dte,call_oi,put_oi,put_call_oi_ratio,pct_of_total_oi}` |
| increases | `uw oi biggest-increases --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-07-22 --json` | `.results[].{option_symbol,oi_diff_plain,volume}` |
| decreases | `uw oi decrease-with-volume --symbol PATH --top-n 15 --min-volume 100 --date 2026-07-22 --json` | `.results[].{option_symbol,oi_diff_plain,volume}` |
| smart positioning | `uw oi smart-positioning --symbol PATH --top-n 20 --min-oi-change 500 --date 2026-07-22 --json` | `.results[].{option_symbol,inferred_direction,net_ask_bid,oi_diff_plain}` |
| pin / opex / rolls | `uw oi pin-risk`/`opex-concentration`/`position-rolls` (market-wide, filtered PATH) | → all PATH-empty |

## Tool errors

<none>

## Verdict for downstream

- **Positioning bias: standing structure is BULLISH (LEAP call dominance — Jan-2027 41% cliff, call-heavy chain), but the MARGINAL/today build is negligible and mixed** (tiny put write + call lotto; small near-term call closes). The Dec-$12 call sale did **not** create a large bearish OI position — most consistent with profit-taking/closing the campaign, not fresh shorting (T+1 OI lag caveat noted).
- **Conviction: 3/5** on the standing bullish LEAP base being real; **2/5** on any *fresh* directional signal from today's OI (it's structurally trivial).
- **Largest OI build as % of float:** ≈0.017% of shares out (negligible); the structural read is the standing 2.4%-of-shares-out Jan-2027 call OI.
- **Three pin/cliff strikes for phase-9:**
  1. **$12 call wall** (net_oi +9,615, 12% OTM) — resistance, doubly confirmed by phase-2's $12 dark-pool overhead supply. The pivotal reclaim level.
  2. **$11 two-sided battleground** (net_oi +297, +2.8%) — nearest pin; the first hurdle overhead and the likely magnet into 7/24.
  3. **$10 put wall support** (−6.6%) → $9 → $8.5 deeper supports; the standing put floor if the 7/24 event disappoints.
  - **OPEX cliffs to respect:** near-term **8/21 (call-heavy, 16.2%)**; structural **Jan-2027 (41.2%)**.
- **Open questions:**
  - Is the LEAP/near-term call OI dominance *long speculation* or *covered-call/overwrite supply* against institutional stock (phase-2 showed mild accumulation)? → phase-4 dealer GEX will disambiguate (short-gamma vs long-gamma dealers).
  - Does tomorrow's OI file confirm the Dec-$12 calls were closed (campaign unwind) vs written? (T+1 lag).
