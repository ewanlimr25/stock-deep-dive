# Phase 3 — Open Interest & Positioning

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:35:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

Positioning paints a **capped-upside, hedged-downside front month with quietly
accumulating September upside**. Fresh OI built overnight in OTM calls 87–93
(Jun-12) and 95–125 (Jun-18) — and `smart-positioning` infers the nearby ones
(89/90/93 Jun-12) **bearish** (bid-dominant prints, i.e. written), consistent
with phase-1-flow.md's −$11.23M net call selling. Against that, the September
builds are **ask-dominant (bought)**: Sep-18 90C +2,469, 95C +1,903, 120C +964
— dated past the 2026-07-29 earnings. The all-expiry wall map: call walls 90
(net_oi +74,534) and 100 (+110,879) overhead, put walls 75 (−18,051) and 70
(−32,897) below; spot 82.47 sits in the 80 `call_heavy` battleground. The OPEX
cliff is **Jun-18 with 21.39% of total OI** (391,214 contracts). Puts are being
*closed*, not built: Jun-18 75P −1,154, Jul-17 100P −821 (the latter likely the
near leg of a Jul→Sep 100P roll given phase-1's Sep-18 100P ask buys).

## Key signals

- **Call wall 90** (≤30DTE: call_oi 50,583 / net_oi +43,361, `role`
  call_wall_resistance, +9.13% from spot) and **100** (net +55,248, +21.3%) —
  with 85/86 as the first shelf (+14,521/+16,953 net) [OI:oi_by_strike]
- **Put wall 75** (≤30DTE net_oi −8,975; all-expiry −18,051) and **70**
  (≤30DTE −4,241; all-expiry −32,897) [OI:oi_by_strike]
- **Jun-18 OPEX cliff: 21.39% of total OI** (391,214 of 1,828,738; P/C OI
  0.536), next: Jun-05 14.82% (expired at as-of), Jan-2027 12.56%, Jul-17
  10.86% [OI:term_structure]
- **Front-month call OI written, Sep call OI bought**: Jun-12 89C/90C/93C
  builds inferred bearish (net_ask_bid −1,410/−181/−1,335) vs Sep-18 90C/95C
  builds inferred bullish (+2,549/+2,050 ask-dominant) [OI:smart_positioning]
- **Put de-risking**: Jun-18 75P OI −1,978→15,772 (−1,154), Jul-17 100P −821
  (avg $16.62, ITM) — closing/rolling, not capitulation buying
  [OI:decrease_with_volume]

## Detailed findings

### OI walls by strike — all expiries [OI:oi_by_strike] (spot 82.47)

| Strike | call_oi | put_oi | net_oi | role | distance |
|---|---|---|---|---|---|
| 100 | 140,651 | 29,772 | +110,879 | call_wall_resistance | +21.3% |
| 90 | 108,491 | 33,957 | +74,534 | call_wall_resistance | +9.1% |
| 80 | 56,942 | 44,352 | +12,590 | **call_heavy (two-sided)** | −3.0% |
| 75 | 39,745 | 57,796 | −18,051 | put_wall_support | −9.1% |
| 85 | 53,265 | 37,813 | +15,452 | call_wall_resistance | +3.1% |
| 70 | 28,678 | 61,575 | −32,897 | put_wall_support | −15.1% |
| 95 | 74,123 | 11,754 | +62,369 | call_wall_resistance | +15.2% |
| 120 | 55,968 | 1,808 | +54,160 | call_wall_resistance | +45.5% |
| 50 / 60 | 12,299 / 10,622 | 45,185 / 44,551 | −32,886 / −33,929 | put_wall_support | −39% / −27% |

### OI walls — ≤30 DTE (the tradeable map) [OI:oi_by_strike --dte-max 30]

| Strike | call_oi | put_oi | net_oi | role | distance |
|---|---|---|---|---|---|
| 100 | 63,162 | 7,914 | +55,248 | call_wall_resistance | +21.3% |
| 90 | 50,583 | 7,222 | +43,361 | call_wall_resistance | +9.1% |
| 95 | 43,927 | 3,666 | +40,261 | call_wall_resistance | +15.2% |
| 80 | 23,771 | 16,670 | +7,101 | **call_heavy (two-sided)** | −3.0% |
| 85 / 86 | 26,455 / 19,280 | 11,934 / 2,327 | +14,521 / +16,953 | call_wall_resistance | +3.1% / +4.3% |
| 70 | 16,404 | 20,645 | −4,241 | put_wall_support | −15.1% |
| 75 | 13,131 | 22,106 | −8,975 | put_wall_support | −9.1% |

Note: 80 is a battleground (`call_heavy`, near-even split), NOT clean support —
phase-9 must not lean on it as a stop shelf; true put support is 75.

### OI term structure [OI:term_structure] (total_oi 1,828,738 · 21 expiries)

| Expiry | DTE | call_oi | put_oi | P/C OI | % of total |
|---|---|---|---|---|---|
| **2026-06-18** | 13 | 254,766 | 136,448 | 0.536 | **21.39% ← OPEX cliff** |
| 2026-06-05 | 0 | 193,340 | 77,676 | 0.402 | 14.82% (expired at as-of) |
| 2027-01-15 | 224 | 151,288 | 78,424 | 0.518 | 12.56% |
| 2026-07-17 | 42 | 135,650 | 62,945 | 0.464 | 10.86% |
| 2026-08-21 | 77 | 69,014 | 61,771 | **0.895** | 7.15% (puttiest — hedges parked past earnings 2026-07-29) |
| 2026-09-18 | 105 | 61,290 | 37,341 | 0.609 | 5.39% |

~15% of OI rolled off at today's expiry → Monday's chain re-anchors on Jun-18.

### Largest OI increases [OI:biggest_increases] (Δ = `oi_diff_plain`; side/expiry parsed from OPRA `option_symbol`)

| Contract | Δ OI | curr_oi | Volume | Read |
|---|---|---|---|---|
| Jun-05 86C / 100C / 90C | +10,734 / +8,391 / +4,667 | 16,680 / 28,019 / 20,374 | 42,751 / 24,797 / 48,721 | 0DTE settlement noise — expired at as-of, ignore |
| **Jun-12 87C** | +2,597 | 3,408 | 6,843 | new front-week call OI |
| **Sep-18 90C** | +2,469 | 5,957 | 3,289 | bought (ask-dom +2,549) |
| Jun-12 91C / 89C / 90C / 93C | +2,398 / +1,515 / +1,448 / +1,430 | — | — | written (89/90/93 bid-dom) |
| Sep-18 95C / 120C | +1,903 / +964 | 4,563 / 4,802 | 2,472 / 1,768 | bought (ask-dom) |
| Jun-18 100C / 125C / 95C | +1,125 / +1,017 / +973 | 23,105 / 5,117 / 12,226 | — | adds to OPEX call ceiling |
| Jun-12 87P | +1,209 | 1,819 | 1,595 | small put add |

Largest non-0DTE build (Jun-12 87C, 2,597 contracts ≈ 259,700 sh-equiv) =
**0.034% of float** (761.21M, phase-0) `[OI:oi_pct_float fz]` — advisory: no
single build is structural for this name; the signal is the *pattern*, not size.

### Closing / roll activity [OI:decrease_with_volume, OI:position_rolls]

- Jun-18 170C −1,978 (lottery abandonment); 2028-01 100C −430 (LEAP trim).
- **Jun-18 75P −1,154** (15,772 remain) and **Jul-17 100P −821** (avg price
  $16.62, deep ITM) — put *closing*. Read with phase-1's Sep-18 100P ask buys
  ($440k print, Δ−0.61): consistent with a Jul→Sep 100P roll-out.
- `position-rolls`: `rolls_detected`=0 (single-day detection, near_dte_max 30;
  the Jul-17 leg at 42 DTE is outside its near window — absence here doesn't
  contradict the roll hypothesis).
- Remaining decreases are 0DTE strikes (81P/80P/77P/84C/85C…) — expiry churn.

### Smart positioning [OI:smart_positioning]

Mixed but tenor-split: 9 of 20 rows bearish-inferred, concentrated ≤7 DTE calls
(written); September rows uniformly bullish-inferred (ask-dominant). Spot-check
per pitfall: HOOD260918C00090000 → Sep-18 2026, Call, strike 90 ✓ parses clean.

### Pin risk / OPEX concentration [OI:pin_risk, OI:opex_concentration]

- `pin-risk` (dte≤7, ≤5% from spot, market-wide top-25): **no HOOD rows**.
- `opex-concentration` (≥40%, top-20): no HOOD (small-cap names only). HOOD's
  21.39% Jun-18 concentration is below the 40% cliff threshold — gravity, not
  a cliff.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw oi biggest-increases --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | Δs ← `.results[].oi_diff_plain` (NOT `oi_change` ratio); side/expiry from `option_symbol` | 20 |
| `uw oi decrease-with-volume --symbol HOOD --top-n 15 --min-volume 100 --date 2026-06-05 --json` | 75P −1,154; 100P −821 ← `.results[].oi_diff_plain` | 15 |
| `uw oi smart-positioning --symbol HOOD --top-n 20 --min-oi-change 500 --date 2026-06-05 --json` | inferred_direction + net_ask_bid ← `.results[]` | 20 |
| `uw oi position-rolls --symbol HOOD --threshold 500 --near-dte-max 30 --date 2026-06-05 --json` | rolls_detected=0 ← `.rolls_detected` | 0 |
| `uw oi oi-by-strike --symbol HOOD --top-n 10 [--dte-max 30] --date 2026-06-05 --json` | wall tables ← `.results[] \| {strike, call_oi, put_oi, net_oi, role, distance_pct}` | 10 ×2 |
| `uw oi term-structure --symbol HOOD --date 2026-06-05 --json` | Jun-18 21.39% ← `.term_structure \| sort_by(-.pct_of_total_oi)` | 21 expiries |
| `uw oi pin-risk --top-n 25 --dte-max 7 --max-distance-pct 5 --date 2026-06-05 --json` | no HOOD ← ticker filter (empty) | top-25 |
| `uw oi opex-concentration --top-n 20 --min-concentration-pct 40 --date 2026-06-05 --json` | no HOOD ← ticker filter (empty) | top-20 |

## Tool errors

(none)

## DATA NOTE / CORRECTION

0DTE (Jun-05) rows dominate `biggest-increases` ranks 1–3 — OI is settled
overnight, so these reflect June-4 trades in contracts that expired at the
as-of close; excluded from the positioning read rather than counted as builds.

## Verdict for downstream phases

- **Positioning bias:** **near-term capped / mildly bearish** — front-month
  call supply being written at 87–93 over spot, put protection held at 75/70;
  **medium-term two-way** — September 90/95/120 calls accumulating ask-side
  (post-earnings upside bets). Not a one-way bearish book.
- **Conviction:** 3
- **Largest OI build as % of float:** 0.034% (Jun-12 87C) `[OI:oi_pct_float fz]`
  — not structural; pattern over size.
- **Three pin/cliff strikes for phase-9** (from `oi-by-strike` roles +
  `term-structure`):
  1. **90 = call_wall_resistance** (≤30DTE net_oi +43,361) — first hard ceiling;
     85/86 the near shelf
  2. **75 = put_wall_support** (≤30DTE net_oi −8,975; all-expiry −18,051) — the
     real downside shelf (80 is a two-sided battleground, not support)
  3. **Jun-18 OPEX = 21.39% OI gravity** — position decay/pin dynamics into
     June 18; phase-4 must cross-check max-pain for this expiry
- **Open questions:** Is the 87–93 call writing covered (against the balanced
  dark-pool book of phase-2) or naked speculation? Does max-pain/GEX (phase-4)
  put Jun-18 gravity nearer 80 or 85? Who is buying September upside while
  selling June — same desk rolling, or different cohorts?
