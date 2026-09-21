# Phase 4 — Dealer Structure & Gamma

**Ticker:** NVDA
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T02:33:00Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md
**Spot referenced:** $212.55–$212.65 (close $212.60)

## Summary

The 45-DTE dealer book is **long-gamma** (`total_gex +$192.9M`, `ZGL $138.94`,
spot $212.56 — far above) — a vol-suppressed, mean-reverting regime that explains
why the 5-session bearish campaign (phase-1) has *drifted* prices lower rather
than crashed them. But the picture is bifurcated: **K212.5 carries -$85.7M of
negative GEX right at spot** and **today's 0DTE regime is NEGATIVE (short-gamma)**
with K212.5 the "resistance_wall." Above spot the long-gamma walls cluster tightly
at **K215 (+$43.8M), K217.5 (+$27M), K220 (+$75.7M), K225 (+$35.2M), K230
(+$39.9M)** — a dealer-defined ceiling that maps almost 1:1 to the OI builds
phase-3 identified as call writing. Vanna mechanics are net **bearish**: dealers
are net short calls (DEX +$17.08B public; hedge is the inverse) and falling IV
is mechanically *cutting* their long-underlying hedge → selling pressure. Skew is
**COMPLACENT** (calls slightly richer than puts at 30d, skew_ratio 0.987) and
term structure is **CONTANGO with FLAT front-end** — no fear premium, no event
stress priced. The net read: vol-suppressed grind lower into a known long-gamma
ceiling at $215–$220, with K212.5 as the gamma flip pivot for any intraday break.

## Key signals

- **GEX regime POSITIVE / total +$192.9M; ZGL $138.94** [STRUCT:gex] — long-gamma,
  dealers sell rallies & buy dips intraday.
- **K212.5 = -$85.7M negative GEX** [STRUCT:gex] right at spot → 0DTE short-gamma
  pivot; below this, dealer mechanics amplify selling intraday.
- **DEX +$17.08B, dealer hedge interpretation: dealers net-short calls → long
  underlying hedge** [STRUCT:dex]. Falling IV → dealers cut hedge → SELLING.
- **Vanna interp:** "Public net vanna negative (call-heavy book). Falling IV →
  call delta drops → dealers (short calls) cut long-underlying hedge → SELLING
  pressure." [STRUCT:vanna_charm] (net_vanna -60,024; net_charm +2.07M).
- **Skew COMPLACENT (skew_ratio 0.987)** [STRUCT:term_skew] — calls slightly
  richer than puts at 30d ATM; downside hedges are cheap.

## Detailed findings

### GEX — [STRUCT:gex]

- `total_gex`: +$192,911,878 → **regime POSITIVE / long-gamma**
- `zero_gamma_level`: **$138.94** (far below spot $212.56 — structural floor for
  any gamma flip would require a ~35% decline)
- `underlying_price`: $212.56

**Top POSITIVE GEX (long-gamma walls = magnetic/ceiling):**

| Strike | net_gex |
|-------:|--------:|
| $220 | +$75.66M |
| $215 | +$43.79M |
| $230 | +$39.89M |
| $225 | +$35.25M |
| $217.5 | +$26.96M |
| $222.5 | +$19.44M |
| $240 | +$18.36M |
| $235 | +$17.09M |

**Top NEGATIVE GEX (short-gamma / amplification zones):**

| Strike | net_gex |
|-------:|--------:|
| **$212.5** | **−$85.74M** |
| $207.5 | −$21.88M |
| $195 | −$20.46M |
| $205 | −$9.45M |
| $202.5 | −$7.60M |

The structure pins **the dealer ceiling to $215–$230** (matching phase-3's call
writing at $215/$217.5/$220) and **the gamma flip to K212.5** — the most acute
spot-local short-gamma in the chain.

### DEX — [STRUCT:dex]

| Field | Value |
|-------|------:|
| call_dex | +$23.00B |
| put_dex | −$5.92B |
| **net_dex** | **+$17.08B** |
| interp | "Public is net call-long → dealers net short calls → dealer hedge is to BUY underlying." |

Dealers hold a *long-underlying* hedge against a *short-call* public book. The
implication: if IV falls or spot falls, that hedge gets cut — mechanical selling.
This is the engine of the slow grind.

### Vanna + Charm — [STRUCT:vanna_charm]

| Field | Value |
|-------|------:|
| call_vanna | −98,185 |
| put_vanna | +38,161 |
| net_vanna | −60,024 |
| net_charm | +2,070,711 |

**Interpretation (verbatim):** *"Public net vanna negative (call-heavy book).
Falling IV → call delta drops → dealers (short calls) cut long-underlying hedge
→ SELLING pressure. Rising IV reverses."* — Given phase-0.5's IV collapse (76 →
30.5 over two weeks), this mechanism has been *driving* the bearish drift.

### IV term structure — [STRUCT:iv_term_structure]

**Structure: CONTANGO** (normal). Selected rows:

| DTE | Expiry | avg_iv |
|----:|--------|-------:|
| 0 | 2026-05-27 | 4.1% (0DTE close artifact) |
| 2 | 2026-05-29 | 50.1% (weekly lift) |
| 7 | 2026-06-03 | 41.2% |
| 22 | 2026-06-18 | 44.5% |
| 30 | 2026-06-26 | 40.6% |

No backwardation → no event stress beyond the weekly lift.

### Term skew — [STRUCT:term_skew] (30-day, 25Δ)

| Field | Value |
|-------|------:|
| put_25d_iv | 0.3905 |
| call_25d_iv | 0.3958 |
| skew | −0.0053 |
| **skew_ratio** | **0.987** |
| interpretation | **COMPLACENT** — calls slightly richer than puts |

Negative skew (calls > puts) on a megacap is **rare** and a yellow flag — the
market is not paying for downside protection despite the persistent bearish flow.
Downside hedges are cheap; this is the asymmetry phase-9 should exploit.

### Front-end IV ratio — [STRUCT:front_end_iv_ratio]

- near_iv (7d) 41.22% / far_iv (30d) 40.56% / **ratio 1.016 → FLAT** — no event
  stress priced; consistent with no earnings until 2026-08-26 (phase-0.5).

### Today's gamma flip — [STRUCT:today_gamma_flip]

- `regime: NEGATIVE` (today 0DTE short-gamma)
- `atm_flip_strike: $152.5` (0DTE flip far below — 0DTE-specific, not 45D ZGL)
- `key_walls`: K212.5 (gex −$80.0M, "resistance_wall"), K215/K217.5/K220
  (support_walls), K207.5 (resistance_wall, gex −$1.7M)

The 0DTE book is *amplifying* (short-gamma) right at spot; the 45-DTE book is
*suppressing* (long-gamma) just above. Net intraday behaviour: whippy at $212.5,
sticky into the $215–$220 walls.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw options-structure gex --dte-max 45` | total +$192.9M, ZGL $138.94, regime POSITIVE |
| `uw options-structure dex --dte-max 45` | net +$17.08B, dealers net-short calls |
| `uw options-structure vanna-charm --dte-max 45` | net_vanna -60k → falling-IV selling pressure |
| `uw options-structure iv-term-structure` | CONTANGO |
| `uw options-structure term-skew --dte-target 30` | COMPLACENT (skew_ratio 0.987) |
| `uw options-structure front-end-iv-ratio --near 7 --far 30` | FLAT (1.016) |
| `uw options-structure today-gamma-flip` | 0DTE regime NEGATIVE; K212.5 = -$80M wall |

## Tool errors

(none)

## Verdict for downstream

- **Dealer regime:** **LONG-GAMMA structurally (45D)**, **SHORT-GAMMA intraday
  (0DTE)** — vol-suppressed grind into a hard ceiling at K215–K220, with K212.5
  as the gamma flip pivot.
- **Conviction:** **4/5** on structural read (the GEX walls + skew complacency
  + vanna mechanics line up *with* phase-1's bearish flow — confluence high).
- **Three structural levels for phase-9:**
  1. **K215 / K217.5 / K220** — long-gamma resistance cluster (combined +$146M
     GEX). The dealer-defined ceiling and the phase-3 call-writing strikes.
  2. **K212.5** — the gamma flip pivot. Break below cleanly = 0DTE short-gamma
     amplification; close above = grind sticks.
  3. **K207.5 / K195** — short-gamma acceleration zones below (modest size);
     the *next* support shelf with K207.5 a dealer-confirmed phase-2 absence.
- **Open questions:**
  - Why is skew negative (calls > puts)? Sentiment phase-7c must resolve —
    crowded long-call positioning OR genuine lack of perceived downside risk.
  - Vanna-selling persists as long as IV falls; a vol spike reverses dealer flow
    — phase-7c short-interest / put-skew watch is the trigger for a regime flip.
