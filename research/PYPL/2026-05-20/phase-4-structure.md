# Phase 4 — Dealer Structure & Gamma

**Ticker:** PYPL
**As-of date:** 2026-05-19 (UW field `underlying_price` = $44.22; spot from
phase 2 late-session = $43.88; **use $44.22 for GEX/DEX-anchored math**)
**Generated:** 2026-05-20T00:35:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md,
phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure has a **bifurcated gamma profile** that materially shapes
trade design. Aggregate regime is **POSITIVE gamma ($2.187B total GEX,
ZGL = $37.06)** — far below spot, so headline regime is "dealers mean-
revert." However, **per-strike GEX is NEGATIVE in the $40–$45 zone (spot
sits in a short-gamma trough) and flips strongly positive at $45.5–$50** —
so locally, dealers will amplify moves until price escapes the trough.
The $44 strike has the single largest negative-gamma position (−$755M
short-gamma) while the $50 strike has the single largest positive-gamma
wall (+$1.6B long-gamma). DEX is +$3.7B positive (public net call-long →
dealers structurally bid on rallies). Term structure is technically
backwardated only because of the **3DTE 5/22 weekly IV spike to 47.0%**;
the rest of the curve is flat → contangoed. 30-DTE 25Δ skew is
**INVERTED (call IV > put IV by 0.83 vol pt) → COMPLACENT** — unusual,
hints at speculative call demand (squeeze / takeout speculation lens).

## Key signals

- **GEX regime: POSITIVE; total GEX = +$2.187B; ZGL = $37.06; spot $44.22
  → $7.16 above ZGL** [STRUCT:options_structure_gex:2026-05-19].
- **Largest call wall: $50 strike, net_gex = +$1,600,907,124 (~$1.6B
  positive gamma)** [STRUCT:options_structure_gex] — dominant resistance,
  consistent with phase-3 $50 Jun-18 call overwriting (23,713 OI).
- **Largest short-gamma strike: $44, net_gex = −$755,329,825** — spot
  ($44.22) sits 22¢ above the biggest short-gamma magnet
  [STRUCT:options_structure_gex / options_structure_today_gamma_flip].
- **DEX: +$3.71B net (call_dex $10.96B, put_dex −$7.25B)** — public is
  call-heavy → dealers short calls → dealer hedge buys underlying into
  rallies [STRUCT:options_structure_dex:2026-05-19].
- **5/22 weekly IV = 47.0%, vs 5/29 = 34.4%, 6/18 = 36.5%** —
  BACKWARDATION only at the 3-DTE weekly, the rest of the curve normalizes
  [STRUCT:options_structure_iv_term_structure:2026-05-19].
- **30-DTE 25Δ skew = −0.0083 (call IV 34.02% > put IV 33.18%) →
  COMPLACENT (inverted)** [STRUCT:options_structure_term_skew:2026-05-19] —
  takeout / squeeze speculation tell, not normal hedging demand.
- **Today gamma flip (5/22 expiry): ATM flip $40, today_zero_gamma $40.04,
  key walls $44 resistance (−$738M), $46 support (+$640M), $50 ultra-wall
  (positive)** [STRUCT:options_structure_today_gamma_flip].

## Detailed findings

### GEX — per-strike map (top 12 by |net_gex|)

| Strike | Net GEX | Sign | Role |
|--------|---------|------|------|
| **50**   | **+$1,600,907,124** | + | **Mega call wall — dominant cap & reflexive ceiling** |
| 47.5 | +$742,156,556 | + | Major positive-gamma support above spot |
| 46   | +$680,244,956 | + | Positive-gamma support |
| 45.5 | +$227,226,652 | + | Local positive flip |
| 46.5 | +$104,607,877 | + | |
| 47   | +$93,696,985 | + | |
| 55   | +$31,990,862 | + | Secondary call wall |
| 52.5 | +$36,928,399 | + | |
| **44**   | **−$755,329,825** | − | **Largest short-gamma strike — sits 22¢ below spot** |
| 43.5 | −$143,987,216 | − | Short-gamma magnet below spot |
| 44.5 | −$137,832,574 | − | Short-gamma magnet above spot |
| 40   | −$103,997,069 | − | Lower short-gamma support |
| 42.5 | −$95,240,804 | − | |
| 42   | −$62,423,671 | − | |
| 45   | −$58,863,030 | − | |
| 43   | −$46,889,338 | − | |

[STRUCT:options_structure_gex:2026-05-19, dte_max=45].

**Cumulative ZGL = $37.06** but the LOCAL profile is:
- Above $45.5: **strongly positive** gamma → dealers sell rallies → cap.
- $40–$45: **negative gamma trough** containing spot → dealers chase
  direction → trends extend, intraday whipsaws.
- Below $40: small negative GEX, then sparse.

The dominant cumulative-positive comes from the $50 strike alone. Strip
the $50 wall and the local picture is short-gamma between $40 and $50.
**Spot at $44.22 = inside the short-gamma trough.**

### DEX — directional hedge bias

```
call_dex:  +$10,962,118,291
put_dex:    -$7,253,272,547
net_dex:   +$3,708,845,744 → public NET CALL LONG → dealers short calls →
                              dealer hedge BUYS underlying.
```

[STRUCT:options_structure_dex]. Net structural bias is **dealer-as-buyer
on rallies and dealer-as-seller on declines** — i.e. positive-feedback
into rallies (reinforcing) but cushion-removing on selloffs. Net: a slow
upward pressure as long as spot is not falling.

### Vanna + charm

```
call_vanna:  -470,630
put_vanna:   +302,385
net_vanna:   -168,245   (public call-heavy → negative aggregate vanna)
net_charm:   +14,726,493
```

[STRUCT:options_structure_vanna_charm].

- **Vanna interpretation:** falling IV → dealers (short calls) cut their
  long-underlying hedge → MILD SELLING pressure. Rising IV → BUYING.
  Vol direction matters: if 5/22 IV crush (today is 5/19, weekly expires
  Friday) sucks 47% → ~35% by Friday close, vanna will be a structural
  headwind into the weekly close.
- **Charm interpretation:** strongly positive (+$14.7M) — as time passes,
  dealer long-underlying hedges decay → slow background SELLING from
  dealers as Friday approaches. Combined with vanna, **mild downward
  pressure baked in for the next 3 sessions absent a directional catalyst.**

### IV term structure (avg IV per expiry)

| Expiry | DTE | Avg IV | Contract count | Note |
|--------|-----|--------|----------------|------|
| 2026-05-22 | 3 | **47.0%** | 2,130 | **Weekly spike** — 5/22 OPEX vol |
| 2026-05-29 | 10 | 34.4% | 631 | Normalized |
| 2026-06-05 | 17 | 35.5% | 276 | |
| 2026-06-12 | 24 | 34.8% | 266 | |
| 2026-06-18 | 30 | 36.5% | 1,315 | Monthly OPEX |
| 2026-06-26 | 38 | 33.9% | 159 | |
| 2026-07-17 | 59 | 35.3% | 604 | |
| 2026-09-18 | 122 | 39.2% | 444 | Q3 OPEX rise |
| 2026-10-16 | 152 | 39.0% | 91 | |
| 2026-11-20 | 185 | 41.2% | 217 | |
| 2026-12-18 | 213 | 41.1% | 216 | |
| 2027-01-15 | 241 | 41.1% | 349 | |
| 2027-03-19 | 304 | 40.9% | 129 | |
| 2027-12-17 | 577 | 42.0% | 61 | |
| 2028-01-21 | 612 | 41.7% | 170 | |
| 2028-12-15 | 942 | 40.8% | 173 | |

[STRUCT:options_structure_iv_term_structure]. Classified as
"BACKWARDATION" because front (5/22) > back, but the real picture is:
- **5/22 weekly is event-stressed (47% IV vs 34.4% next week)** —
  someone is paying up for 3DTE optionality. Cross-reference: phase 3
  showed $44.5P and $47C / $45C OI builds on 5/22 — short-dated hedging
  + 3DTE call lotto.
- Mid-term (5/29 → 7/17) flat at ~34–36%.
- Back-end (Sep onward) gentle contango up to 41–42%.

No major kink → no binary event in 6–8 weeks per the IV surface alone.

### Term skew (30-DTE 25Δ)

```
call_25d_iv:  34.02%
put_25d_iv:   33.18%
skew:         -0.0083   (call IV > put IV — INVERTED)
skew_ratio:   0.975
interpretation: COMPLACENT
```

[STRUCT:options_structure_term_skew:2026-05-19, dte_target=30].

**This is the most interesting structural signal.** Normal equity skew has
puts more expensive than calls (vol smile up the strike-axis to the left).
PYPL's 30-DTE skew is inverted — 25Δ calls trade above 25Δ puts by 84 bp
of IV. Reasons this happens:
1. Genuine speculative call demand (M&A / buyout / squeeze speculation).
2. Persistent call overwriters absent → put-sellers dominate → put IV
   crushed.
3. Skew flattening as crash hedge demand evaporates → "complacency."

Given phase 2 mega-tier dark-pool accumulation, phase 3 dominant call
overwriting (which SHOULD push call IV down, not up), the most likely
driver is **speculative call demand on top of overwriter supply — i.e.
buyers are paying through the overwriter offer**. This is consistent with
the unusual call buildup at $45–$50 May/Jun strikes.

### Front-end IV ratio (7DTE/30DTE)

```
near_iv (9 DTE):  34.43%
far_iv (29 DTE):  36.48%
ratio:            0.944  → CONTANGO
```

[STRUCT:options_structure_front_end_iv_ratio]. **Contradicts** the term-
structure tool's "BACKWARDATION" label because front-end ratio uses
near-DTE = 9 (skipping the 5/22 weekly). Once the 5/22 weekly spike is
filtered, **the curve is in normal CONTANGO**. No persistent event stress.

### Today gamma flip (5/22 expiry only)

```
spot:              $44.27
today_zero_gamma:  $40.04
atm_flip_strike:   $40
today_total_gex:   +$48,245,767 (mildly positive)
today_expiry:      2026-05-22
key_walls:
  +$639,869,936  $46   support_wall
  +$225,513,129  $45.5 support_wall
  -$737,901,461  $44   resistance_wall
  -$137,470,905  $44.5 resistance_wall
  -$129,949,354  $43.5 resistance_wall
```

[STRUCT:options_structure_today_gamma_flip:2026-05-19].

For the 5/22 weekly expiry alone: dealers are short-gamma at $43.5, $44,
$44.5 (the trough containing spot), and long-gamma at $45.5 and $46. The
**$46 support_wall is a magnet — once spot trades above $45.5, dealer
positive-gamma kicks in and price will be held into Friday**. Below $44,
trend amplifies down toward $40 (today_zero_gamma).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=PYPL, dte-max=45, include-zero-gamma=true, date=2026-05-19 | POSITIVE regime, ZGL $37.06, $50 wall +$1.6B |
| `mcp__uw-pp__options_structure_dex` | symbol=PYPL, dte-max=45, date=2026-05-19 | net_dex +$3.71B → dealer buys rallies |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=PYPL, dte-max=45, date=2026-05-19 | net_vanna −168K, net_charm +14.7M |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=PYPL, date=2026-05-19 | BACKWARDATION (driven by 5/22 47% spike) |
| `mcp__uw-pp__options_structure_term_skew` | symbol=PYPL, dte-target=30, date=2026-05-19 | INVERTED / COMPLACENT (calls > puts) |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=PYPL, near-dte=7, far-dte=30, date=2026-05-19 | CONTANGO ratio 0.944 (filters out 5/22) |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=PYPL, date=2026-05-19 | 5/22 atm_flip $40, $46 support_wall, $44 resistance_wall |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **structurally constructive but locally
  trendy.** Net DEX +$3.71B and inverted call-rich skew lean bullish.
  The aggregate positive-gamma regime ($50 wall) caps near-term upside
  at ~$50. The local short-gamma trough at $40–$45 means PYPL's intraday
  realized vol will be ABOVE its IV-implied vol until spot escapes the
  trough in either direction.
- **Conviction:** **4 / 5**. GEX/DEX numbers are unambiguous and the
  inverted skew is a rare, high-signal tell. Knock 1 point for the
  conflicting term-structure labels (kink at 5/22 only).
- **Three structural levels for phase-9:**
  1. **$50.00 — mega call wall (+$1.6B GEX)**. Price magnet ceiling for
     Jun-18 OPEX. Sustained close above forces gamma unwind.
  2. **$45.50–$46.00 — positive-gamma support band**. First resistance
     becomes support if traded; intraday rallies that reach $46 will
     STALL (positive gamma → dealer sell), but pullbacks INTO $46 from
     above will be bought.
  3. **$44.00 — short-gamma magnet (−$755M GEX)**. Local pull toward
     this strike. Spot oscillating around $44 will be sticky into 5/22
     OPEX absent a directional catalyst.
  4. (Bonus) **$40 — atm_flip / today_zero_gamma boundary**. Loss of $40
     flips daily gamma negative → dealer-driven acceleration toward $35
     put bid (phase-3 floor).
- **Open questions:**
  - The inverted 30-DTE skew — is this a recurring PYPL feature or new?
    Phase 5 historical IV percentile and historical P/C will answer.
  - Is the 5/22 47% IV pop driven by a specific catalyst (analyst day,
    macro event) or just OPEX positioning? Phase 6 macro/news needed.
  - Vanna structure suggests a mild dealer-sell pressure as IV decays
    into the weekly — does the call-wall structure absorb that or
    amplify it on a break?
