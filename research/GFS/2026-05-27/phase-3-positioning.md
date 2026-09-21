# Phase 3 — Open Interest & Positioning

**Ticker:** GFS
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T00:00:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning is **mixed with a clean time-split: near-term defensive, long-term
bullish.** The two near-dated (22 DTE, June OPEX) builds are *bearish* — **$120 June
calls SOLD** (oi +1,053, inferred bearish, call-writing — confirms phase-1's
$120 bid-sweep) and **$85 June puts BOUGHT** (oi +520, inferred bearish, downside
hedge/bet). The two longer-dated builds are *bullish* — **$95 Oct calls BOUGHT**
(oi +550, 142 DTE) and **$120 Jan-2027 LEAP calls BOUGHT** (oi +858, 233 DTE).
Meanwhile **ITM $75–$85 calls are being closed** (decreases of −590/−166/−64/−60) =
profit-taking on the +35% run. So the chain says: *hedge/cap the recent gains
short-term, stay structurally long into 2027.* No near-term pin or OPEX-cliff
mechanics (June OPEX 22 days out; GFS outside both pin-risk and opex-concentration
top-40). All builds are **structurally tiny** — largest is 0.08% of float.

## Key signals

- **$120 Jun call: oi +1,053, inferred BEARISH** (net_ask_bid −49 → sold) — call
  writing, the chain's largest build `[OI:smart_positioning]`, `[OI:biggest_increases]`.
- **$85 Jun put: oi +520, inferred BEARISH** (net_ask_bid +573 → bought on ask) —
  near-term downside hedge/bet `[OI:smart_positioning]`.
- **$120 Jan-2027 LEAP call: oi +858, inferred BULLISH** (net_ask_bid +701 → bought),
  prev premium $1.25M — slow-money long `[OI:smart_positioning]`.
- **$95 Oct call: oi +550, inferred BULLISH** (net_ask_bid +610 → bought) — mid-dated
  long `[OI:smart_positioning]`.
- **ITM $75–$85 calls closing** (−590, −166, −64, −60 with high volume) = run
  profit-taking `[OI:decrease_with_volume]`.
- **No pin / OPEX cliff** near spot `[OI:pin_risk]`, `[OI:opex_concentration]`.

## Detailed findings

### Largest OI increases `[OI:biggest_increases]`, `[OI:smart_positioning]`

| strike | type | expiry/DTE | OI Δ | vol | avg px | inferred dir | read |
|------:|------|-----------|----:|----:|-------:|--------------|------|
| 120 | call | Jun-18 / 22 | **+1,053** | 1,169 | $1.50 | **BEARISH** (sold) | call writing / ceiling |
| 120 | call | Jan-2027 / 233 | +858 | 1,015 | $12.34 | **BULLISH** (bought) | LEAP accumulation |
| 95 | call | Oct-16 / 142 | +550 | 725 | $16.69 | **BULLISH** (bought) | mid-dated long |
| 85 | put | Jun-18 / 22 | +520 | 803 | $5.83 | **BEARISH** (bought) | near hedge/bet |

The June-22DTE pair (sold $120 call + bought $85 put) is a **defensive structure
around the recent gains**; the Oct/Jan call buys are a **separate, longer-horizon
bullish book**. These are different actors / different intents — do not net them into
one direction.

### Closing / roll activity `[OI:decrease_with_volume]`, `[OI:position_rolls]`

| strike | OI Δ | vol | avg px | read |
|------:|----:|----:|-------:|------|
| 80 call | −590 | 796 | $11.50 | closing deep-ITM call (profit-take) |
| 80 call | −166 | 384 | $16.10 | closing ITM call |
| 75 call | −64 | 109 | $16.39 | closing ITM call |
| 85 call | −60 | 593 | $10.21 | closing ITM call |

Position-rolls tool returned **0 rows** — no clean near→far roll flagged (the
$120 sold-Jun / bought-Jan'27 could be a diagonal but was not detected as a roll).
The decreases are unambiguous **ITM-call profit-taking** after the parabola.

### Pin risk / OPEX concentration

- `pin_risk` (dte≤7): **GFS absent** — June OPEX is 22 days out, weeklies thin. No
  near-term pin to trade `[OI:pin_risk]`.
- `opex_concentration` (≥40%): **GFS outside top-40** — no OI cliff within 5% of
  spot `[OI:opex_concentration]`.

### Float normalization (advisory) `[OI:oi_pct_float fz]`

Largest build $120 Jun call 1,053 ct × 100 = 105,300 share-equiv = **0.08% of the
132.68M float**. All four builds combined ≈ 0.23% of float. **Not structural** — no
position here is large enough to move or pin the name.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw oi biggest-increases --min-oi-change 500` | 4 builds: $120c, $120c-LEAP, $95c, $85p |
| `uw oi decrease-with-volume --min-volume 100` | 4 decreases, all ITM $75–85 calls closing |
| `uw oi smart-positioning --min-oi-change 500` | $120 Jun call bearish; LEAP/$95 bullish; $85 put bearish |
| `uw oi position-rolls --threshold 500` | **0 rows** (no roll detected) |
| `uw oi pin-risk --dte-max 7` | **GFS absent** (no near-term pin) |
| `uw oi opex-concentration --min-concentration-pct 40` | **GFS outside top-40** |

## Tool errors

None. (`option_type`/`expiry` returned null in `biggest-increases` /
`decrease_with_volume`; recovered from `smart_positioning`'s `option_symbol` +
phase-0.5 `top_oi_changes`.)

## Verdict for downstream

- **Positioning bias:** **MIXED — near-term defensive (bearish), long-term bullish.**
  For a short-to-medium-horizon trade the near-term read dominates: calls being
  written + puts being bought around June OPEX = the desk is **hedging the
  parabola**, not chasing it.
- **Conviction:** **2.5/5** — the time-split is a genuine, coherent tell, but no
  single dominant build.
- **Largest OI build as % of float (advisory):** **0.08%** (share-equiv) — not
  structural `[OI:oi_pct_float fz]`.
- **Three strikes for phase-9:**
  1. **$120** — soft ceiling (calls written near-term; LEAP-call magnet long-term).
  2. **$85** — near-term hedge strike (puts bought); first overhead pivot.
  3. **$95** — mid-dated bullish call interest; the longer-horizon upside marker.
- **Open questions:** Is the $120-call-writing covered (against stock / the closed
  ITM calls) or naked? Does dealer GEX (phase-4) confirm dealers are long gamma /
  short these written calls, reinforcing a cap near $85–$90? Does the LEAP-call
  accumulation reflect a known catalyst the fundamentals phase (7b) can name?
