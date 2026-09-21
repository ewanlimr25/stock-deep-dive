# Phase 3 — Open Interest & Positioning

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:35:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning **reframes phase-1's "bearish" tape as largely call-*writing*, not
directional bearishness.** The dominant near-term structure is a coiled **$14–15
range**: spot $14.54 sits on the **$14.5 put-support** wall and is capped by a hard
**$15 call wall** (+3.06%, 22.7k call OI ≤30-DTE). Today's OI *builds* are a
signature income/collar footprint — a massive **45,000-lot Mar-2027 $19 call**
(neutral-tagged, structural) plus **call-writing** across $16/$17/$18/$21 (smart-
positioning "bearish") and **put-selling** at $13/$14 (smart-positioning "bullish").
Read against phase-2's continuous stock accumulation, the coherent story is
**institutions long stock, overwriting calls and selling downside puts**, with a
near-term Jul-24 straddle hedging the 07-30 earnings — constructive-but-capped and
range-bound, **not** a bearish directional bet. Term-structure gravity is
**Sept-18 (26.5% of OI, call-heavy)**, post-earnings.

## Key signals

- **$15 call wall = near ceiling** (net_oi +21,514 ≤30-DTE, dist +3.06%) — the pin/cap `[OI:oi-by-strike]`
- **$14.5 put support at spot** (net_oi −5,675, dist −0.38%) + layered $13.5 (−12,540) / $13 (−6,187) put walls below `[OI:oi-by-strike]`
- **45,000-lot Mar-2027 $19 call built today** (+45k OI, vol 45k) — largest build, "neutral" = structural, not directional `[OI:biggest-increases / smart-positioning]`
- **Call-writing footprint:** $18C (+11k Jun-27, +4.7k Sep), $16/$17 (Aug), $21 (Dec) all smart-tagged **bearish** = calls sold `[OI:smart-positioning]`
- **Put-selling footprint:** $14 Sep (+3.1k) & $13 Aug (+2.5k) smart-tagged **bullish** = puts sold (willing to own lower) `[OI:smart-positioning]`

## Detailed findings

### OI walls by strike — tradeable horizon (≤30 DTE) `[OI:oi-by-strike]`

| Strike | call_oi | put_oi | net_oi | role | dist % |
|---|---|---|---|---|---|
| 13.0 | 4,171 | 10,358 | −6,187 | put_wall_support | −10.68 |
| 13.5 | 509 | 13,049 | **−12,540** | put_wall_support | −7.25 |
| **14.5** | 2,684 | 8,359 | −5,675 | **put_wall_support** | **−0.38** (at spot) |
| 14.0 | 11,140 | 7,445 | +3,695 | call_heavy (2-sided) | −3.81 |
| **15.0** | 22,663 | 1,149 | **+21,514** | **call_wall_resistance** | **+3.06** |
| 15.5 | 6,755 | 1,024 | +5,731 | call_wall_resistance | +6.49 |
| 16.0 | 16,041 | 528 | +15,513 | call_wall_resistance | +9.93 |

Near-term cage: **$14.5 put support (spot) → $15 call wall (+3%)**, with a $13.5/$13
put floor and a $16 secondary ceiling. Matches phase-2's dark-pool $14.30–14.90
cluster. The $14 strike is a two-sided `call_heavy` battleground (net only +3,695),
not clean support.

*(All-expiry aggregate adds far walls: $19C 76k OI (+30.5%), $18C 45.6k (+23.7%),
$17C 40k (+16.8%) — these are the LEAP overwrite/structural strikes, not tradeable levels.)*

### OI term structure — OPEX cliffs `[OI:term-structure]`

| Expiry | call_oi | put_oi | % of total OI |
|---|---|---|---|
| **2026-09-18** | 133,698 | 23,934 | **26.49** (gravity well, call-heavy) |
| 2027-01-15 | 69,549 | 47,797 | 19.72 (LEAP, balanced) |
| 2026-07-17 (expiring today) | 54,487 | 35,714 | 15.16 |
| 2026-08-21 | 51,376 | 13,558 | 10.91 (1st post-earnings monthly) |
| 2027-03-19 | 48,495 | 40 | 8.16 (all-call LEAP — the $19 build) |
| 2026-07-24 | 13,919 | 4,315 | 3.06 (the straddle weekly) |

Gravity well **Sept-18 (26.5%)** is post-earnings and heavily call-skewed — dealer
short-gamma into a call-wall regime above spot. Earnings (07-30) fall between the
07-24 weekly (small) and 08-21 monthly.

### Largest OI increases (new builds today) `[OI:biggest-increases]`

| Contract (parsed OPRA) | Exp | Type | Strike | ΔOI | Vol |
|---|---|---|---|---|---|
| RKT270319C00019000 | 2027-03-19 | C | 19 | **+45,000** | 45,000 |
| RKT270617C00018000 | 2027-06-17 | C | 18 | +11,000 | 11,014 |
| RKT260918C00018000 | 2026-09-18 | C | 18 | +4,682 | 5,126 |
| RKT260918P00014000 | 2026-09-18 | P | 14 | +3,127 | 5,160 |
| RKT261218C00021000 | 2026-12-18 | C | 21 | +3,000 | 3,595 |
| RKT260814P00013000 | 2026-08-14 | P | 13 | +2,549 | 2,551 |
| RKT260821C00016000 | 2026-08-21 | C | 16 | +2,327 | 4,207 |

The +45k Mar-2027 $19 call dwarfs everything — a structural far-LEAP position.
Everything else is upside-call and downside-put builds at strikes well OTM.

### Smart positioning (inferred direction) `[OI:smart-positioning]`

| Contract | Inferred dir | Read |
|---|---|---|
| Mar-27 $19C (+45k) | **neutral** | structural (collar/buy-write), not directional |
| Jun-27 $18C (+11k) | bearish | call written (overwrite) |
| Sep $18C (+4.7k) | bearish | call written |
| **Sep $14P (+3.1k)** | **bullish** | put **sold** — willing to own at $14 |
| Dec $21C (+3k) | bearish | call written (matches phase-1 $21.2C bid-sale) |
| **Aug $13P (+2.5k)** | **bullish** | put **sold** |
| Aug $16/$17C | bearish | calls written |

Pattern = **systematic call-writing above + put-selling below** ⇒ income/collar
around a long. This is the reconciling key: phase-1's "calls sold" (net_call_prem
−231k) is overwriting, and some of phase-1's puts are being *sold* here (not all
bought), softening the directional-bearish read to **range-neutral/constructive**.

### Closing / roll activity `[OI:decrease-with-volume]`

Minor: Sep $20C −2,670 (vol 3,085, upside call closing), Dec $12P −648, Aug $15C
−388. No material near→far roll campaign (`position-rolls` returned **0 rows**).

### Pin risk / OPEX concentration

**RKT absent** from market-wide `pin-risk` (≤7 DTE, ≤5% dist, top-25) and
`opex-concentration` (≥40%, top-20). Today (07-17) is an OPEX but RKT is not a pin
candidate at these thresholds — its OI gravity is Sept-18, not the front weekly.
No pin commentary warranted for the front expiry.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw oi oi-by-strike --symbol RKT --dte-max 30` | $15 call wall net_oi +21,514 @+3.06%; $14.5 put support @−0.38% ← `.results[].{net_oi,role,distance_pct}` | 10 |
| `uw oi oi-by-strike --symbol RKT` (all-expiry) | $19C 76k OI @+30.5% ← `.results[]` | 10 |
| `uw oi term-structure --symbol RKT` | Sept-18 26.49% pct_of_total_oi ← `.term_structure[].pct_of_total_oi` | 8 expiries |
| `uw oi biggest-increases --symbol RKT --min-oi-change 500` | Mar-27 $19C +45,000 ← `.results[].oi_diff_plain` + parse `.option_symbol` | 10 |
| `uw oi smart-positioning --symbol RKT --min-oi-change 500` | call-writing (bearish) + put-selling (bullish) ← `.results[].inferred_direction` | 10 |
| `uw oi decrease-with-volume --symbol RKT` | Sep $20C −2,670 ← `.results[]` | 15 |
| `uw oi position-rolls --symbol RKT --threshold 500` | 0 rows (no roll campaign) | 0 |
| `uw oi pin-risk` / `opex-concentration` (market-wide) | RKT absent from both | 0 RKT |

## Tool errors

None. `position-rolls` (0 rows), `pin-risk`/`opex-concentration` (no RKT) are
findings, not errors. All OI figures traced to `jq` paths above.

## DATA NOTE / CORRECTION

`biggest-increases`/`smart-positioning` have **no `side`/`expiry` columns** — parsed
strike/type/expiry from OPRA `option_symbol` (e.g. `RKT270319C00019000` → 2027-03-19
Call $19) per phase-3 rule, not inferred from `net_oi`. **Dual-class caveat:** RKT
is dual-class; spot-checked that the inference is internally consistent (calls-sold
→ "bearish" tag, puts-sold → "bullish" tag), so the direction tags are trustworthy
here, but treated as *suggestive* not definitive.

## Verdict for downstream phases

- **Positioning bias:** **Range-neutral / mildly constructive** — a
  call-writing + put-selling (income/collar) footprint around structural longs,
  coiled inside a **$14.5–15.0** near-term cage. **Reframes phase-1 bearishness as
  overwriting; confirms phase-2 accumulation.**
- **Conviction:** **3 / 5** — the wall map and build pattern are clear and mutually
  consistent across three lanes; docked because "call-selling" could alternatively be
  outright bearish and the smart-positioning inference is heuristic on a dual-class name.
- **Largest OI build as % of float:** **n/a** (`fz` float unavailable) — advisory:
  the +45k Mar-27 $19C ≈ 4.5M share-equiv ≈ ~0.45% of the ~1.0B Class-A count;
  structurally meaningful but not float-dominating. Tag `[OI:oi_pct_float est]`.
- **Three pin/cliff strikes for phase-9 (sourced from roles):**
  1. **$15.0 call_wall_resistance** (+3.06%, net_oi +21,514) — near-term cap / upside pin.
  2. **$14.5 put_wall_support** (−0.38%, at spot) — the pin/mean; break below opens $13.5.
  3. **$13.5 put_wall_support** (−7.25%, net_oi −12,540) — primary downside shelf (aligns w/ dark-pool $14.30 support one tier up).
  - OPEX cliff for the calendar: **Sept-18** (26.5% of OI, call-heavy), post-earnings.
- **Open questions:** is the +45k Mar-27 $19C a buy-write (stock+short-call, confirming
  accumulation) or a standalone bullish LEAP? Does structure/max-pain (phase-4) put
  opex gravity at the $15 wall? Does IV term (phase-4) show the Jul-24/earnings vol
  kink the straddle is paying for?
