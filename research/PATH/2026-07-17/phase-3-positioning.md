# Phase 3 — Open Interest & Positioning

**Ticker:** PATH · **As-of:** 2026-07-17 (July monthly OPEX) · **Version:** v1
Cites: phase-1-flow.md (Nov-16C build open question; LEAP-call directional read);
phase-2-dark-pool.md (accumulation; does OI wall cap it?); phase-0.5-context.md
(Nov-16C +4,255 flagged).

## Summary

PATH is **structurally bullish-positioned but call-walled overhead**. Open
interest is call-dominated at essentially every tenor: put/call OI ratios run
**0.05–0.57** across the ladder, and the single largest expiry — **2027-01-15,
holding 40.8% of all 605k OI** (156,711 calls vs 89,951 puts) — is the structural
gravity well, backed by Aug'26 (15.4%, P/C 0.285), Jan'28 LEAP (12.6%, P/C 0.21)
and Sep'26 (7.8%). Today's *new* positioning is net bullish: the standout is
**Nov'26 $16C +4,255 contracts** (vol 5,367 — confirms the phase-0.5 flag and
phase-1's patient-call read), with `smart-positioning` tagging both it and the
Jan'27 $9P build bullish; there were **no position-rolls and only trivial
closing**. The catch for phase-9: the same call ownership builds **dense
resistance walls just overhead** — a $12.5 wall (+3%) then a heavy **$13 call wall
(19,681 near-term call OI, +7%)** — while put support is *far* below (nearest real
put wall $10, −17.6%). So the positioning confirms the bullish lean of phases 1–2
but caps near-term upside into $13.

## Key signals

- **Jan'27 expiry = 40.8% of total OI** — 156,711 call / 89,951 put OI, the
  structural anchor of the whole chain `[OI:term_structure]`. Everything trades
  around this LEAP mass.
- **Nov'26 $16C +4,255** (vol 5,367) — the day's largest OI build, bullish, OTM
  (+32%), long-dated `[OI:biggest_increases, smart_positioning]`. The patient call
  buyer from phase-1 laddering up.
- **$13 near-term call wall: 19,681 call OI vs 375 put** (net +19,306,
  role=call_wall_resistance, +7.08%) `[OI:oi_by_strike]` — the dominant overhead
  magnet/cap for the tradeable horizon.
- **$12.5 call wall +2.97%** (8,376 call OI, net +8,135) `[OI:oi_by_strike]` — the
  first overhead resistance the accumulation must clear.
- **No rolls, minimal closing** — `position-rolls` 0 rows; decreases are all
  <450 contracts (Sep $20C −433, Aug $11C −303) `[OI:position_rolls,
  decrease_with_volume]`. Positioning is being *built*, not unwound.

## Detailed findings

### OI walls by strike (DTE ≤ 30 — tradeable horizon) `[OI:oi_by_strike]`
| Strike | call OI | put OI | net_oi | role | dist% |
|---|---|---|---|---|---|
| 12 | 9,613 | 2,007 | +7,606 | call_heavy | −1.15 (≈spot) |
| **12.5** | 8,376 | 241 | +8,135 | **call_wall_resistance** | +2.97 |
| **13** | **19,681** | 375 | **+19,306** | **call_wall_resistance** | +7.08 |
| 13.5 | 3,391 | 4 | +3,387 | call_wall_resistance | +11.2 |
| 14 | 15,350 | 28 | +15,322 | call_wall_resistance | +15.3 |
| 15 | 6,938 | 4 | +6,934 | call_wall_resistance | +23.6 |
| 11.5 | 1,748 | 2,001 | −253 | put_wall_support | −5.27 |
| 11 | 6,132 | 2,837 | +3,295 | call_heavy | −9.39 |
| 10 | 996 | 5,433 | −4,437 | put_wall_support | −17.6 |
| 9 | 585 | 4,232 | −3,647 | put_wall_support | −25.9 |
Near-term map: spot ($12) is a call-heavy two-sided pivot; overhead is **all call
resistance** ($12.5 → $13 → $14); the nearest real downside wall is the thin
$11.5 (net −253) then nothing structural until $10 (−17.6%). Upside is capped,
downside is un-cushioned near-term — a "grind or get walled" chart.

### OI term structure (OPEX cliffs) `[OI:term_structure]`
| Expiry | DTE | call OI | put OI | P/C | % of total OI |
|---|---|---|---|---|---|
| **2027-01-15** | 182 | 156,711 | 89,951 | 0.574 | **40.77** |
| 2026-08-21 | 35 | 72,441 | 20,673 | 0.285 | 15.39 |
| 2028-01-21 | 553 | 63,007 | 13,243 | 0.210 | 12.60 |
| 2026-07-17 | 0 | 56,178 | 14,820 | 0.264 | 11.73 (expires today) |
| 2026-09-18 | 63 | 34,095 | 12,998 | 0.381 | 7.78 |
| 2026-12-18 | 154 | 26,570 | 1,451 | 0.055 | 4.63 |
Total OI 605,029 across 16 expiries. **The OPEX cliff is Jan'27** (41% of OI) —
not a near-term pin, a structural anchor. Today's 0DTE (11.7%) evaporates at the
close. Every material expiry is call-heavy (P/C ≤ 0.57), and Dec'18 is almost
pure calls (P/C 0.055) — this is a call-owned name, top to bottom.

### Largest OI increases `[OI:biggest_increases]` (side/expiry parsed from OPRA)
| Contract | Expiry | Side | Strike | OI Δ | vol |
|---|---|---|---|---|---|
| PATH261120C00016000 | 2026-11-20 | Call | $16 | **+4,255** | 5,367 |
| PATH270115P00009000 | 2027-01-15 | Put | $9 | +1,280 | 1,379 |
| PATH260918C00013000 | 2026-09-18 | Call | $13 | +500 | 571 |
Only 3 rows cleared min-oi-change 500. The Nov $16C dominates; the Jan'27 $9P is a
deep-OTM long-dated line (smart-positioning tags it **bullish** → read as put
*writing*/financing, not hedging); the Sep $13C (+500) is small post-earnings call.

### Closing / roll activity `[OI:decrease_with_volume, position_rolls]`
`position-rolls`: **0 rows** (no near→far rolls detected). Decreases all trivial:
Sep'26 $20C −433, Aug'26 $11C −303, Jan'28 $15C −250, Sep'26 $9P −142. No
meaningful unwind — the two-sided Sep $13P from phase-1 does **not** show as a
roll here, consistent with it being intraday two-way MM/spread flow rather than a
position migration.

### Smart positioning `[OI:smart_positioning]`
Net **bullish**: Nov'26 $16C +4,255 (bullish), Jan'27 $9P +1,280 (bullish — put
supply), Sep'26 $13C +500 (bearish — near-money call supply/cap). Two of three,
and the far larger two, read bullish.

### Pin risk / OPEX concentration `[OI:pin_risk, opex_concentration]`
PATH is **not** in the market-wide `pin-risk` top-40 (dte≤7, within 5%) despite
today being July OPEX — its 0DTE mass is call-skewed and below spot, not a tight
two-sided pin. PATH is **not** in `opex-concentration` (no single expiry ≥40%
by that tool's cut at the ticker level within the returned set; the Jan'27 41%
is a far-dated structural bucket, not a near-term cliff). No near-term pin
commentary warranted.

## Tool calls
| Tool | Args | Result |
|---|---|---|
| oi oi-by-strike | --symbol PATH --dte-max 30 / all --date 2026-07-17 | $13 wall dominant; put support far below |
| oi term-structure | --symbol PATH --date 2026-07-17 | Jan'27 = 40.8% of OI |
| oi biggest-increases | --symbol PATH --min-oi-change 500 --date 2026-07-17 | Nov $16C +4,255 lead |
| oi decrease-with-volume | --symbol PATH --min-volume 100 --date 2026-07-17 | all <450, trivial |
| oi smart-positioning | --symbol PATH --min-oi-change 500 --date 2026-07-17 | net bullish |
| oi position-rolls | --symbol PATH --threshold 500 --near-dte-max 30 --date 2026-07-17 | 0 rows |
| oi pin-risk | --dte-max 7 --max-distance-pct 5 --date 2026-07-17 | PATH not in top-40 |
| oi opex-concentration | --min-concentration-pct 40 --date 2026-07-17 | PATH not returned |

## Tool errors
- None (initial `term-structure` jq used the wrong root key; corrected to
  `.term_structure[]` — data validated, not a tool error).

## Verdict for downstream

- **Positioning bias: structurally bullish, near-term call-walled.** Calls own the
  chain at every tenor (P/C 0.05–0.57); new builds are net bullish (Nov $16C
  +4,255); no unwinding. But dense overhead call walls ($12.5, $13) cap the
  immediate upside, and put support is remote (−17%+), so the near-term shape is a
  grind toward $13 resistance rather than open air.
- **Conviction: 3 / 5** — the structural call ownership and clean build/no-unwind
  pattern are a real bullish tell that agrees with phases 1–2; docked because the
  same OI is the overhead resistance and today's new size is modest.
- **Largest OI build as % of float: n/a** — `fz` float unresolved (phase-0/2). The
  Nov $16C +4,255 ≈ 425,500 share-equiv, immaterial against a large software float;
  it's the *direction and persistence*, not the size, that carries — do not treat
  it as a structural float bet.
- **Three pin/cliff strikes for phase-9:**
  1. **$13 call wall** (+7.08%, 19,681 near-term call OI) — primary overhead
     magnet/cap; a close above $13 on volume would flip resistance→support.
  2. **$12.5 call wall** (+2.97%) — the first gate the accumulation must clear;
     the near-term breakout trigger.
  3. **$11.5 → $10 put support** (thin $11.5 net −253, real wall $10 −17.6%) plus
     the **Jan'27 40.8%-OI structural anchor** — the downside is un-cushioned until
     ~$11, so a $11.5 loss opens air to $10/$11 support.
- **Open questions:** Are the dense $12.5/$13 call walls dealer-SHORT (customer-
  bought calls → dealers buy dips, could fuel a squeeze through $13) or dealer-LONG
  covered writes (a hard cap)? **Phase-4 GEX/max-pain must resolve this — it flips
  the entire near-term thesis.** Is Jan'27's 90k put OI (P/C 0.57, the most
  balanced expiry) genuine hedging that offsets the bullish call ownership?
