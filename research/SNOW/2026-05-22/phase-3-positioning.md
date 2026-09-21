# Phase 3 — Open Interest & Positioning

**Ticker:** SNOW
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T15:42:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI resolves phase-1's puzzle: the fresh positioning is a **capped bullish
earnings bet, structured as a bull call spread**, not outright bearishness. The
single largest new position is **5/29 185C, OI +5,046 (366→5,412, 13.8×), bought on
the ask** (prev ask-vol 5,118 vs bid 83), $2.17M, `inferred_direction = bullish`
[OI:smart_positioning]. It is paired with **5/29 200C, OI +3,413, sold on the bid**
(ask 367 vs bid 4,197), `inferred_direction = bearish` [OI:smart_positioning] — i.e.
**call-writing that caps the upside at $200**. Long-185 / short-200 for the
post-earnings 5/29 expiry is a defined-risk move-up bet targeting $185–200, and the
short-200 leg is exactly why phase-1's signed delta-notional in the 2–7DTE week
looked net-bearish (−$15M) — that's the cap, not a bearish thesis. Beyond this
spread, activity is 0DTE churn and minor closing. **No OPEX pin** (SNOW absent from
`pin_risk` and `opex_concentration`); the binary is earnings 5/27, not a gamma pin.

## Key signals

- **Fresh bullish conviction — 5/29 185C +5,046 OI (13.8×), ask-bought, $2.17M**,
  net_ask_bid +5,035 [OI:biggest_increases][OI:smart_positioning]. The dominant new
  position; ~7.5% OTM, expiry captures 5/27 earnings.
- **Upside cap — 5/29 200C +3,413 OI, bid-SOLD** (ask 367 / bid 4,197), inferred
  bearish [OI:smart_positioning] → call-writing at $200 ≈ 16% OTM. Pairs with the
  185C as a **bull call spread**.
- **No genuine downside build:** the only put OI move of size is 0DTE 162.5P
  (+929, expiring) and a *closing* 2027-03 150P (−223) [OI:biggest_increases]
  [OI:decrease_with_volume] — downside hedges being trimmed, not added.
- **No position rolls** detected (single-day) [OI:position_rolls].
- **No OPEX pin / cliff for SNOW** — absent from both `pin_risk` (top-25 is
  HYG/SPY/TLT/NVDA index & mega names) and `opex_concentration` (micro-caps)
  [OI:pin_risk][OI:opex_concentration]. SNOW's OI is spread across expiries.

## Detailed findings

### Largest OI increases [OI:biggest_increases]

| expiry/strike | DTE | OI Δ | curr OI | prev ask/bid vol | $prem | read |
|---------------|-----|------|---------|------------------|-------|------|
| **5/29 185C** | 7 | **+5,046** | 5,412 | 5,118 / 83 | $2.17M | **bought — bullish** (spread long leg) |
| **5/29 200C** | 7 | +3,413 | 6,334 | 367 / 4,197 | $0.87M | **sold — call write** (spread short leg / cap) |
| 5/22 162.5P | 0 | +929 | 1,022 | 327 / 738 | $0.16M | 0DTE, expiring |
| 5/22 170C | 0 | +746 | 3,091 | 825 / 1,173 | $0.18M | 0DTE bid |
| 5/22 167.5C | 0 | +505 | 1,671 | 522 / 403 | $0.14M | 0DTE ask |

Only two builds matter past today's expiry, and they are the two legs of the 5/29
185/200 call spread. Everything else is 0DTE pin churn.

### Closing / roll activity [OI:decrease_with_volume][OI:position_rolls]

Decreases are dominated by **0DTE 5/22 contracts expiring** (160C −964, 165C −110,
175C −103, etc.). The one structurally interesting close: **2027-03 150P −223**
($2.74M prior premium) — a long-dated downside hedge being *reduced*, mildly
constructive. 6/18 190C −197 and 6/18 220P −92 are minor. `position_rolls`: **0
detected** — no near→far rolling on the day.

### Smart positioning (inferred direction) [OI:smart_positioning]

Net of the five flagged builds: **bullish** on the 185C (+5,035 net ask) and 167.5C;
**bearish** on the 200C (−3,830 net ask, = writing) and 0DTE 170C. The signal is the
185/200 structure — directional up, **capped at $200**. This is more constructive
than phase-1's flat delta-notional implied, because the "bearish" 200C leg is a
short-call cap inside a bull spread, not a standalone bearish bet. *Reconciliation
note for phase-10: phase-1 `delta_notional` 2–7DTE = −$15M and phase-3 "capped
bullish" are consistent, not contradictory — the short 200C explains the negative
signed delta.*

### Pin risk & OPEX concentration

**Not applicable to SNOW.** `oi_pin_risk` (dte_max=7) top-25 is entirely index/mega
names with 5/22 monthly-style OI mass (HYG, SPY, TLT, QQQ, NVDA, …); SNOW does not
rank — its near-dated OI is not gamma-concentrated near spot. `oi_opex_concentration`
(≥40%) returns only micro-caps at 100%. SNOW's OI is distributed across 5/22, 5/29,
6/18, 6/26, 7/17, LEAPs — **no single-expiry cliff**. The market mechanic that
matters here is the **earnings binary (5/27)**, not an OPEX pin.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `oi_biggest_increases` | symbol=SNOW, min_oi_change=500 | 5/29 185C +5,046 (bull); 5/29 200C +3,413 (write); rest 0DTE |
| `oi_decrease_with_volume` | symbol=SNOW, min_volume=100 | 0DTE expiry closes; 2027-03 150P −223 (hedge trim) |
| `oi_smart_positioning` | symbol=SNOW, min_oi_change=500 | 185C bullish / 200C bearish (= bull call spread) |
| `oi_position_rolls` | symbol=SNOW, near_dte_max=30 | 0 rolls detected |
| `oi_pin_risk` | dte_max=7, max_distance=5% | SNOW absent (index/mega names only) |
| `oi_opex_concentration` | min_concentration=40% | SNOW absent (micro-caps only) |

## Tool errors

(none)

## Verdict for downstream phases

- **Positioning bias:** **MILD BULLISH, CAPPED** — a 5/29 185/200 bull call spread
  is the dominant fresh structure; directional up into earnings but capped at $200,
  with downside hedges being trimmed (no fresh put builds). Conviction tempered by
  the cap and the earnings-binary nature.
- **Conviction:** **3/5** on the existence of a directional-up structure (the 185C
  +5,046 is real, ask-bought, $2.17M), de-rated by the $200 cap and phase-0.5's
  `BUSY_NAME` flag → net carry as `+`, not `++`.
- **Three strikes for phase-9 entry/stop reference:**
  1. **$185 — upside magnet / spread long-leg & first target** (5/29 185C +5,046 OI;
     ~7.5% above spot; the level the smart-money structure is paying for) [OI:biggest_increases].
  2. **$200 — upside cap / resistance** (5/29 200C call-writing wall, +3,413 sold;
     ~16% OTM — where dealers/writers expect the move to stall) [OI:smart_positioning].
  3. **$150–162.5 — thin downside OI**; the only fresh put is 0DTE 162.5P and a
     *closing* 2027 150P → little options-based downside support; phase-2's dark-pool
     $163.5–$167 shelf is the more reliable floor.
- **Open questions:**
  - Is the 185C buyer a directional fund or a dealer-hedged spread desk? Either way
    it implies an expected earnings move to ~$185 (≈ +7.5%).
  - Does dealer GEX reinforce $185/$200 as gamma walls, and where's the gamma flip
    into the event? → phase-4.
  - Does the historical earnings-move distribution support a $185 target? → phase-5
    + phase-7b/earnings history.
