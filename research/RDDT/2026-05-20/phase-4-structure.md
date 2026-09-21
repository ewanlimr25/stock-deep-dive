# Phase 4 — Dealer Structure & Gamma

**Ticker:** RDDT
**As-of date:** 2026-05-20 (data anchor 2026-05-18)
**Generated:** 2026-05-19T00:45:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

RDDT is in a **POSITIVE GEX regime** with **total dealer gamma
$1.261B**, ZGL $158.39, spot $158.89 — spot sits **just $0.50 above
ZGL**, classic knife-edge between long-gamma pin and short-gamma cliff.
The single largest gamma wall in the chain is **$160 strike at
+$622.7M GEX** (49% of total) — gravitational anchor for any
intraday move. ATM 0DTE flip strike is $157.50, today's ZGL $158.03.
Public DEX is heavily call-long (+$18.0B) → dealers are **short calls,
short gamma above 160 not yet, but already long below 160** because
they hedge by buying underlying on the way up. Term structure is
**BACKWARDATION** (5/22 IV 79.1% vs 7/17 IV 63.5%) — front-end IV is
priced for an event in the next week. 30D term-skew is **COMPLACENT**
(skew_ratio 0.946 = calls more expensive than puts) — confirms the
phase-1 bullish flow. Vanna interpretation: rising IV would force
dealers to BUY underlying (long-gamma feedback), while a vol crush
would force selling. This is a classic **gamma-pin-into-an-event-week
setup**.

## Key signals

- Regime **POSITIVE**, total GEX **+$1.261B**, ZGL **$158.39**, spot
  **$158.89** — long gamma but on the edge [STRUCT:gex].
- **$160 strike GEX = +$622.7M** = 49% of all dealer gamma; same
  strike where phase-1 sweep ladder, phase-2 dark-pool blocks, and
  phase-3 OI buildup converge [STRUCT:gex, today_gamma_flip].
- Net DEX **+$18.01B** (call_dex +$22.03B, put_dex −$4.02B) — public
  is dominantly call-long; dealer hedge is to BUY underlying on
  upticks, supporting any rally [STRUCT:dex].
- Term structure **BACKWARDATION** with 5/22 IV 79.1% printing 1,500
  bps over 7/17 IV 63.5% — market is pricing a **near-term catalyst**
  inside the next 4 days (consistent with the front-end sweep
  concentration) [STRUCT:iv_term_structure].
- 30D skew **COMPLACENT** (put_25d 61.8% < call_25d 65.4%, ratio
  0.946) — almost no tail-hedging demand; risk-on positioning
  [STRUCT:term_skew].

## Detailed findings

### GEX (DTE ≤ 45)

- Underlying price: **$158.89**
- Total GEX: **+$1,261,243,128** (positive)
- Regime: **POSITIVE** — "Dealers net long gamma; expect mean-reversion
  and reduced volatility"
- Zero Gamma Level: **$158.39** (spot sits $0.50 / 0.3% above)

Top positive (long-gamma) walls — dealers must SELL on rallies into,
BUY on dips back to:

| Strike | Net GEX | Position |
|--------|---------|----------|
| 160   | **+$622,690,698** | spot $158.89 → **immediately above** = magnet |
| 170   | +$281,720,653 | resistance above |
| 165   | +$177,792,216 | |
| 167.5 | +$121,002,103 | |
| 175   |  +$41,304,010 | |
| 162.5 |  +$34,442,480 | |
| 172.5 |  +$14,583,642 | |
| 157.5 |     +$527,797 | just below spot |

Top negative (short-gamma) holes — dealers must BUY on rallies into,
SELL on dips below; trend-amplifying if spot enters:

| Strike | Net GEX | Position |
|--------|---------|----------|
| 150 | **−$77,323,127** | -5.7% below spot |
| 140 |  −$62,622,883 | -11.9% below |
| 145 |  −$31,846,805 | -8.7% below |
| 155 |  −$12,766,411 | -2.4% below |
| 152.5 | −$5,175,744 | -4.0% below |
| 135 |   −$5,857,074 | tail |
| 125 |   −$4,208,626 | tail |
| 130 |   −$3,934,555 | tail |
| 120 |   −$9,897,144 | tail |

**Asymmetric structure:** above ZGL = stacked long-gamma walls (pin
behavior); below ZGL = stacked short-gamma holes (trend amplification).
Spot at $158.89 is **literally on the pivot**: a push up takes it
into the 160 magnet (dealers sell rallies, capping); a push down
through 158.39 unlocks the short-gamma zone with 150 as the air
pocket (-5.7% in one swoop).

### DEX

| Metric | Value | Read |
|--------|-------|------|
| call_dex | +$22,032,809,270 | public massively call-long |
| put_dex  | −$4,021,314,417  | put exposure exists but dominated |
| **net_dex** | **+$18,011,494,853** | net call-long |
| spot | $158.93 | |

Read: classic bull-skew DEX. Dealers are short calls (against public's
long calls) and the standard hedge is to **own underlying** in
proportion to call delta. As spot rises, call delta rises, dealers
buy more underlying → reflexive bid. As spot falls, dealers unwind
the hedge → reflexive offer. This is the mechanism by which positive
DEX usually pairs with positive GEX above ZGL.

### Vanna + charm

| Metric | Value |
|--------|-------|
| call_vanna | −101,543 |
| put_vanna  | +24,570  |
| **net_vanna** | **−76,973** |
| net_charm  | +18,487,137 |
| spot | $158.93 |

Tool interpretation: "Public net vanna negative (call-heavy book).
Falling IV → call delta drops → dealers (short calls) cut long-
underlying hedge → SELLING pressure. Rising IV reverses."

Implication: a **vol crush** (e.g., front-end IV 79% collapsing toward
the back-end 63% post-event) would trigger mechanical SELLING by
dealers — important risk if a catalyst passes uneventfully and the
front-end IV mean-reverts. The classic post-earnings IV-crush
dealer-deleveraging dynamic.

Positive net charm = dealer position is decaying in a direction that,
all else equal, requires re-hedging that supports the underlying as
options approach expiry.

### IV term structure (BACKWARDATION)

| Expiry | DTE | Avg IV | Contracts |
|--------|-----|--------|-----------|
| 2026-05-22 | 4   | **79.1%** | 3,786 |
| 2026-05-29 | 11  | 67.8%     | 1,052 |
| 2026-06-05 | 18  | 66.0%     |   271 |
| 2026-06-12 | 25  | 64.6%     |   137 |
| 2026-06-18 | 31  | 66.0%     | 1,330 |
| 2026-06-26 | 39  | 63.2%     |   175 |
| 2026-07-17 | 60  | **63.5%** |   321 |
| 2026-08-21 | 95  | 70.1%     |   239 |
| 2026-09-18 |123  | 69.5%     |   153 |
| 2026-10-16 |151  | 67.8%     |    44 |
| 2026-11-20 |186  | 71.0%     |    47 |
| 2026-12-18 |214  | 69.5%     |    58 |
| 2027-01-15 |242  | 68.7%     |   297 |
| ... | | | |
| 2028-01-21 |613  | 73.3%     |    35 |
| 2028-06-16 |759  | 69.2%     |   131 |

Read: clean **BACKWARDATION** — 5/22 IV (4 DTE) is 79.1% versus
back-month IV in the 63-67% range. The 5/22 front-end is pricing
**~15 vol points of event premium** relative to the August baseline.
The structure also shows a second mini-hump at 8/21 (70.1%) — this
ties exactly to the phase-1 8/21 170C/175P concentration. Two
catalyst pricings: one inside next 4 days, one around mid-August.

Earnings cadence (assumed quarterly): if RDDT reports Q1 in late
April/early May historically, the 8/21 hump is consistent with **Q2
earnings** in mid/late August — the LEAP write activity and the 8/21
positioning then makes sense as straddle-style event positioning.

### Term skew (30D, COMPLACENT)

| Metric | Value |
|--------|-------|
| put_25d_iv  | 61.79% |
| call_25d_iv | **65.35%** |
| skew | −0.0356 |
| skew_ratio | 0.946 |
| **interpretation** | **COMPLACENT** |

Read: skew is INVERTED — 25Δ calls are richer than 25Δ puts at 30D.
That's an unusual configuration and consistent with the phase-1
call-buying frenzy: vol traders are pricing upside more dearly than
downside. **No tail hedging** is being bid — no one is paying up for
crash protection in the 30D window. This is bullish-confirming but
also a contrarian "everyone's on one side" flag (see phase-8 agent
review).

### Front-end IV ratio

| Metric | Value |
|--------|-------|
| near (10 DTE) IV | 67.85% |
| far (30 DTE) IV  | 65.98% |
| ratio | 1.028 |
| regime | **FLAT** |

Read: when measured at 10D/30D the ratio is 1.028 (flat), but the
full term structure showed dramatic backwardation at the 5/22
expiry (4 DTE). The "event" is therefore concentrated in the next
4 days, not generically across the front end. Likely a discrete
catalyst inside this trading week (see phase-6 calendar).

### Today's gamma flip (5/22 0DTE proxy / today's expiry)

| Field | Value |
|-------|-------|
| today_expiry | 2026-05-22 |
| spot | $159.01 |
| today_total_gex | +$1,120,929,902 |
| today_zero_gamma | **$158.03** |
| atm_flip_strike | **$157.50** |
| regime | POSITIVE |

Key walls (5/22 expiry only):

| Strike | GEX | Role |
|--------|-----|------|
| **160** | **+$602,734,564** | support wall (magnet) |
| 170 | +$242,032,484 | support wall (far) |
| 165 | +$165,049,996 | support wall |
| 167.5 | +$118,765,626 | support wall |
| **150** | **−$67,699,758** | resistance wall (short-γ trigger below) |

Read: 5/22 alone holds 89% of total chain GEX, confirming this week
is the gravitational center. The **160 magnet for THIS week** is
60% of today's gamma — pin behavior into Friday 5/22 close is the
highest-probability mechanical outcome. Break below 150 would
trigger short-gamma cascades; the 150 strike acts as a "resistance"
in the structural sense (it stops dealer hedge buying and ignites
hedge selling).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=RDDT, date=2026-05-18, dte_max=45 | POSITIVE, ZGL 158.39, total +$1.26B |
| `mcp__uw-pp__options_structure_dex` | symbol=RDDT, date=2026-05-18, dte_max=45 | net +$18.01B (call-long public) |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=RDDT, date=2026-05-18, dte_max=45 | net_vanna −77k, charm +18.5M |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=RDDT, date=2026-05-18 | BACKWARDATION; 5/22 IV 79.1% |
| `mcp__uw-pp__options_structure_term_skew` | symbol=RDDT, date=2026-05-18, dte_target=30 | COMPLACENT, skew_ratio 0.946 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=RDDT, date=2026-05-18, near_dte=7, far_dte=30 | FLAT 1.028 (10D vs 30D) |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=RDDT, date=2026-05-18 | today expiry 5/22, ZGL 158.03, 160 wall +$603M |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** POSITIVE GEX (long-gamma) with spot $0.50 above ZGL
  — pin-prone above ZGL, cliff-prone below.
- **Conviction:** 5 / 5 — GEX magnitude is unambiguous; the 160 wall
  is one of the cleanest single-strike concentrations seen in any
  single-name read; backwardation + complacent skew + dominant
  call-DEX all confirm the bullish-but-pinning setup.
- **Three structural levels for phase-9:**
  1. **$158.39 (chain ZGL) / $158.03 (today's ZGL) / $157.50 (ATM
     flip strike)** — the gamma pivot zone. Long-gamma pin above this
     band, short-gamma trend-amp below. Effective stop trigger for
     long positions; first-touch entry zone for shorts on confirmed
     break.
  2. **$160 (largest GEX wall, +$622.7M / 49% of chain)** — primary
     magnet. Spot will repeatedly probe this strike. Pin into 5/22
     close very plausible; sustained break above with volume opens
     the 165 → 167.5 → 170 stair of secondary walls.
  3. **$150 (largest negative GEX hole, −$77.3M)** — first short-gamma
     air pocket if 158.39 ZGL fails. Combined with phase-2's dark-pool
     bid at $154.12, the realistic "panic to" range is $154 → $150 in
     a one-day flush.
- **Open questions:**
  - Phase 6 must identify the discrete catalyst priced into the 5/22
    front-end IV (79.1%) and the 8/21 secondary hump (70.1%) — most
    likely earnings, possibly index inclusion/secondary offering.
  - Phase 5 must contextualize whether current IV percentile is rich
    or cheap relative to RDDT's own history before recommending vol
    structures.
  - Phase 8 contrarian-scanner should flag the COMPLACENT skew +
    persistent bullish positioning as a crowded-trade setup.
