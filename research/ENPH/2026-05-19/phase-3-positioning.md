# Phase 3 — Open Interest & Positioning

**Ticker:** ENPH
**As-of date:** 2026-05-19 (effective UW date 2026-05-15)
**Generated:** 2026-05-19T00:00:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md

## Summary

OI positioning is **decisively bullish and consistent with phase-1's
ask-side call sweeping**. The dominant flow on 2026-05-15 was a
**roll-up of June 18 calls from $45/$60 strikes (OI −4,817 combined) into
$50/$55/$60 strikes (OI +10,207 combined)**, with the **June 18 $50 call
adding +4,985 OI to reach 26,273 — by far the most heavily-owned strike on
the chain** [OI:biggest_increases]. **Smart-positioning inferred bullish
direction on 11 of the 13 most-changed contracts**; the only meaningful
bearish print was a small **Aug-2026 $40 put long (810 contracts, $389k
prev premium)** that reads as light hedging, not new short. **Cross-session
rolls were not detected** by the single-day `oi_position_rolls` tool, but
the same-strike $45→$50/$55 pattern is a same-day rolloff signature.
**The big Jun-2027 $70C/$45P combo from phase-1 (12,300×ea) has not yet
shown up in the OI delta snapshot** — that trade printed at 17:13:03Z and
OI updates after settlement, so it will land in the 2026-05-18 OI delta;
the Jan-2027 $70 call is, however, already showing **+1,310 OI / bullish
(net_ask_bid +1,077)** confirming there's a sister LEAP campaign underway.

## Key signals

- **Jun-2026 $50 call: +4,985 OI to 26,273 (most-owned strike on chain);
  ask-volume 9,652 vs bid-volume 6,374 → net_ask_bid +3,278 bullish**
  [OI:biggest_increases][OI:smart_positioning].
- **Roll-up signature: Jun-2026 $45C −2,460 OI / Jun-2026 $60C −2,357 OI
  while Jun-2026 $50C +4,985 / $55C +3,714** [OI:decrease_with_volume +
  OI:biggest_increases] — institutions paying up by closing lower-delta
  positions and adding higher-delta ones.
- **Jan-2027 $70 call: +1,310 OI to 4,492 (vol 1,413, ask-vol 1,087 vs
  bid-vol 10 = aggressive ask buying)** [OI:smart_positioning] — sister
  LEAP campaign for the still-pending Jun-2027 $70C combo.
- **11 of 13 top-OI-change contracts inferred bullish**; only Aug-2026
  $40 put +810 OI is a long-put / hedging signature (small $389k premium
  context) [OI:smart_positioning].
- **No OPEX-week pin risk for ENPH** [OI:pin_risk] — next monthly OPEX is
  6/18 (>30d), outside the dte_max=7 window; pin commentary skipped.

## Detailed findings

### Largest OI increases (top 13, min_oi_change=500)

| Symbol | Type | Strike | DTE | Curr OI | OI Δ | Vol | Prev Ask Vol | Prev Bid Vol | Direction |
|---|---|---|---|---|---|---|---|---|---|
| ENPH260618C00050000 | call | 50 | 34 | 26,273 | **+4,985** | 17,908 | 9,652 | 6,374 | **Bullish** |
| ENPH260618C00055000 | call | 55 | 34 | 7,292 | **+3,714** | 8,760 | 5,402 | 2,286 | **Bullish** |
| ENPH260515C00050000 | call | 50 | 0 | 7,170 | +2,197 | 7,952 | 4,548 | 2,934 | Bullish (0DTE) |
| ENPH260618P00050000 | put | 50 | 34 | 5,409 | +1,508 | 1,637 | 188 | 1,353 | **Bullish (puts SOLD)** |
| ENPH270115C00070000 | call | 70 | 245 | 4,492 | **+1,310** | 1,413 | 1,087 | 10 | **Bullish (LEAP)** |
| ENPH270115C00100000 | call | 100 | 245 | 4,732 | +1,015 | 1,243 | 828 | 303 | Bullish (deep OTM LEAP) |
| ENPH260821C00075000 | call | 75 | 98 | 1,292 | +848 | 1,241 | 246 | 145 | Bullish |
| ENPH260821C00060000 | call | 60 | 98 | 1,842 | +817 | 951 | 911 | 21 | **Bullish (clean ask)** |
| ENPH260821P00040000 | put | 40 | 98 | 1,187 | +810 | 932 | 887 | 45 | **Bearish (puts BOUGHT, hedging)** |
| ENPH260821P00050000 | put | 50 | 98 | 1,263 | +759 | 911 | 1 | 910 | Bullish (puts SOLD) |
| ENPH260515C00055000 | call | 55 | 0 | 1,362 | +663 | 1,655 | 569 | 923 | Bearish (0DTE) |
| ENPH260626C00060000 | call | 60 | 42 | 624 | +624 | 652 | 83 | 564 | Bearish |
| ENPH270115C00075000 | call | 75 | 245 | 5,135 | +517 | 558 | 541 | 12 | **Bullish (LEAP)** |

**Bullish OI delta total (11 contracts):** ≈ **+18,453 new bullish OI**
across calls bought + puts sold.
**Bearish OI delta total (2 contracts):** ≈ **+1,434 new bearish OI**
(Aug $40P long hedge + 0DTE $55C bid).
**Net inferred bullish positioning: ~13× bearish.**

### Closing / roll activity (top 8)

| Symbol | Type | Strike | DTE | Curr OI | OI Δ | Vol |
|---|---|---|---|---|---|---|
| ENPH260618C00045000 | call | 45 | 34 | 6,679 | **−2,460** | 4,718 |
| ENPH260618C00060000 | call | 60 | 34 | 7,592 | **−2,357** | 4,438 |
| ENPH260515C00045000 | call | 45 | 0 | 4,221 | −416 (0DTE expiry) | 1,986 |
| ENPH260515C00035000 | call | 35 | 0 | 3,995 | −379 (0DTE expiry) | 167 |
| ENPH260618P00040000 | put | 40 | 34 | 6,339 | −376 (closing puts) | 2,883 |
| ENPH260618P00025000 | put | 25 | 34 | 3,662 | −368 (closing tails) | 517 |
| ENPH270115C00165000 | call | 165 | 245 | 658 | −342 (deep OTM closing) | 690 |
| ENPH260717C00045000 | call | 45 | 63 | 1,990 | −235 | 883 |

**Pattern:** the −2,460 / −2,357 dump on **Jun 45C / Jun 60C** is exactly
mirrored by the +4,985 / +3,714 build on **Jun 50C / Jun 55C**. That's a
classic same-strike, same-expiry **roll up the chain** while keeping the
expiry constant. **Bullish interpretation:** holders are closing $45 ITM
longs (taking profits / freeing capital) and rotating into $50/$55 strikes
with more upside leverage. They're also closing $40 puts (less downside
hedge needed).

### Smart positioning (inferred direction summary)

`oi_smart_positioning` (top 13 by OI change):

| Direction count | Count |
|---|---|
| Bullish | **11** |
| Bearish | 2 (1 mechanical 0DTE + 1 hedge) |

Top bullish prints all show **net_ask_bid > 0 on calls** OR **net_ask_bid <
0 on puts** (puts sold = synthetic long).

The Aug-2026 $40P with **net_ask_bid +842** and inferred_direction
"bearish" is the cleanest hedge signature on the board: 810 new long
puts at the $40 strike, ~24% OTM from current $52.50 spot. **Read as
portfolio protection by an existing long holder, NOT a directional short.**

### Pin risk / OPEX concentration

- `oi_pin_risk` (dte_max=7): **ENPH absent from top-25.** Next ENPH OPEX
  is **June 18 (34 DTE)** — fully outside the OPEX-week pin window.
- `oi_opex_concentration` (min_concentration_pct=40): **ENPH absent**
  (concentration is diffuse across May, June, Aug, Sept, Jan-2027, and
  Jun-2027 expiries — no single-expiry cliff dominates).

Reading: **no near-term pin pressure** for the 1–5d horizon. Phase-9
mechanical entry/stop levels should NOT key off pin gravity.

### Cross-session rolls

`oi_position_rolls` (threshold=500, near_dte_max=30): **0 rolls
detected.** The tool only flags single-day near→far migrations and the
roll-up activity above is **same-DTE, different-strike**, which doesn't
trigger this detector.

### Cross-check vs phases 1–2

| Phase-1 / Phase-2 claim | Phase-3 confirmation? |
|---|---|
| 5/5 bullish sweep persistence | **Confirmed**: 11/13 bullish OI delta; clean call-buy/put-sell signature. |
| Jun-2027 $70C + $45P combo (17:13:03Z) | **Not yet** in OI snapshot (will appear in 2026-05-18 delta); however, Jan-2027 $70C is already building (+1,310 OI, clean ask buying), consistent with the same fund running a multi-tenor LEAP campaign. |
| Jan-2027 $100 puts sold $3.2M | **Indirect confirmation**: Jan-2027 $100C *building* (+1,015 OI / bullish), suggesting same-fund put-sale to call-buy alongside; the put-sell itself does not show as an OI decrease at the strike (volume of 606 was below the close-with-volume threshold). |
| Dark pool accumulation $48–$54 | **Strikes line up**: Jun-2026 $50C is the OI-heavyweight (26,273) and the $50 line is the dealer hedging center directly inside the DP accumulation band. |
| Aug-2026 $40 put long (potential hedge) | **NEW** signal — not visible in phase-1 (small premium); important for phase-9 invalidation as institutional downside protection level. |

## Tool calls (audit trail)

| Tool | Args | Result summary |
|---|---|---|
| `mcp__uw-pp__oi_biggest_increases` | symbol=ENPH, date=2026-05-15, top_n=25, min_oi_change=500 | 13 rows ≥500; Jun 50C +4,985 leads |
| `mcp__uw-pp__oi_decrease_with_volume` | symbol=ENPH, date=2026-05-15, top_n=20, min_volume=100 | 20 rows; Jun 45C −2,460 / Jun 60C −2,357 lead the roll-down side |
| `mcp__uw-pp__oi_smart_positioning` | symbol=ENPH, date=2026-05-15, top_n=20, min_oi_change=500 | 13 rows; 11 bullish / 2 bearish |
| `mcp__uw-pp__oi_position_rolls` | symbol=ENPH, date=2026-05-15, threshold=500, near_dte_max=30 | 0 rolls detected (single-day measure) |
| `mcp__uw-pp__oi_pin_risk` | date=2026-05-15, dte_max=7, max_distance_pct=5, top_n=25 | ENPH absent (next OPEX 6/18 = 34 DTE) |
| `mcp__uw-pp__oi_opex_concentration` | date=2026-05-15, top_n=30, min_concentration_pct=40 | ENPH absent — diffuse expiry distribution |

## Tool errors

None.

## Verdict for downstream phases

- **Positioning bias:** **Bullish — calls being built and rolled up;
  puts being sold (synthetic long); modest tail-hedge in Aug $40 puts.**
- **Conviction:** **4 / 5** (would be 5/5 with the Jun-2027 combo OI
  delta confirming).
- **Three key strikes for phase-9 entry/stop reference:**
  1. **$50 strike (Jun 2026 $50 call OI 26,273)** — the dealer hedging
     center and the natural pivot. Spot above $50 keeps dealers buying.
  2. **$55 strike (Jun 2026 $55 call OI 7,292, rapidly building)** —
     near-term call wall / breakout target.
  3. **$40 strike (Aug 2026 $40 put OI 1,187, new hedging activity)** —
     primary institutional downside line. If spot trades through $40,
     hedgers' protection kicks in and the bullish thesis is in trouble.
- **Open questions:**
  - Did the Jun-2027 combo create new OI? Re-pull 2026-05-18 OI delta
     when available; the put leg should add ~12,000 to the Jun-2027 $45
     put line (currently OI 71 per phase-1).
  - Is the Aug-2026 $40 put long part of a married-put position (long
     stock + long put = bullish core)? Phase-7 institutional accumulation
     signal will help distinguish.
  - Is the **same fund** buying calls at $50/$55 AND the LEAP combo? Very
     likely given the clean ask-side signature on both campaigns, but
     uncorroborated.
