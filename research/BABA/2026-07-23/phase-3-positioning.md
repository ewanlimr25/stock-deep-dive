# Phase 3 — Open Interest & Positioning

**Ticker:** BABA · **As-of:** 2026-07-23 · **Spot:** $114.99 (≈$114.05 in OI snapshot)
**Generated:** 2026-07-24
**Upstream:** phase-2-dark-pool.md (overhead supply $116.85–118.22, support shelf $114.97,
open Q: "does OI put a call wall in the overhead zone?"); phase-1 net_flow −$1.68M.

## Summary

Today's OI **build is overwhelmingly call-side** — 14 call strikes added +27,433 contracts
vs just 2 put strikes +1,379 — but it is concentrated in **far-OTM Aug calls (145/155/165,
26–43% OTM)** plus a 0DTE 120 pin build and a Sep-150. Read against phase-1 (call premium
that was *not* aggressive directional buying, net_flow bearish) and phase-2 (block-tier
distribution), the coherent interpretation is that much of this call build is **premium
selling / overwriting / lottery-ticket speculation, not conviction upside** — smart-positioning
tags the far-OTM Aug strikes **mixed** (155 bullish, 165 & 145 bearish). The **structural wall
map** puts nearest overhead resistance at the **$120 call wall (+5.2%)** — confirming phase-2's
$116–118 overhead supply — with **$110 put-wall support (−3.6%)** below and a roughly balanced
**$115 ATM battleground** (net_oi +1,460). The OI gravity well is **2026-09-18 (27.6% of total
OI, 57 DTE)** — the monthly right after the **2026-09-04 earnings**.

## Key signals

- **Call-tilted OI build:** +27,433 call vs +1,379 put contracts (14 vs 2 strikes)
  `[OI:biggest_increases]`
- **…but far-OTM & ambiguous:** builds at Aug 145/155/165 + 0DTE 120; smart-positioning
  splits bull/bear on them → likely overwriting/spec, not conviction longs `[OI:smart_positioning]`
- **Nearest overhead call wall $120** (net_oi +26,803 near-term, +5.2%) — confirms phase-2
  overhead supply `[OI:oi_by_strike]`
- **Put-wall support $110** (−3.6%) → $105 → **$100 (biggest all-expiry put wall, net −30,075)**
  `[OI:oi_by_strike]`
- **OPEX gravity well 2026-09-18** (27.6% of total OI, post-earnings monthly); near-term
  cliff **2026-08-21** (13.1%, call-heavy PCR 0.42) `[OI:term_structure]`

## Detailed findings

### OI walls by strike `[OI:oi_by_strike]`

**Tradeable horizon (DTE ≤ 30):**

| Strike | call_oi | put_oi | net_oi | role | dist |
|--------|---------|--------|--------|------|------|
| **120** | 32,257 | 5,454 | **+26,803** | call_wall_resistance | +5.2% |
| 130 | 30,614 | 94 | +30,520 | call_wall_resistance | +14% |
| 125 | 23,851 | 2,945 | +20,906 | call_wall_resistance | +9.6% |
| **110** | 10,729 | 14,481 | **−3,752** | put_wall_support | −3.6% |
| **115** | 12,242 | 10,782 | **+1,460** | call_wall (≈balanced) | +0.8% (ATM battleground) |
| 105 | 8,509 | 5,135 | +3,374 | call_heavy | −7.9% |

**All-expiry** adds the structural picture: **$100 is the biggest put wall** (put_oi 130,584,
net −30,075, −12.3%); big far call walls at $150 (net +98,645), $140, $130. Near-term overhead
resistance = **$120**, then $125/$130.

### OI term structure (OPEX cliffs) `[OI:term_structure]`

| Expiry | DTE | % of total OI | call_oi | put_oi | PCR |
|--------|-----|---------------|---------|--------|-----|
| **2026-09-18** | 57 | **27.63%** | 240,572 | 152,284 | 0.63 |
| 2027-01-15 | 176 | 15.74% | 152,750 | 71,025 | 0.46 |
| 2026-12-18 | 148 | 13.20% | 101,883 | 85,806 | 0.84 |
| 2026-08-21 | 29 | 13.09% | 131,425 | 54,631 | 0.42 |
| 2026-07-24 | 1 | 8.02% | 88,479 | 25,554 | 0.29 |

**Gravity well = 2026-09-18** (the post-earnings monthly). Near-term the tradeable cliff is
**2026-08-21** (call-heavy, PCR 0.42). Cross-check against phase-4 max-pain and phase-6's
2026-09-04 earnings.

### Largest OI increases `[OI:biggest_increases]` (side/expiry parsed from OPRA symbol)

| Contract | Expiry | Side | Strike | OI Δ | Vol |
|----------|--------|------|--------|------|-----|
| BABA…C120 | 2026-07-24 | Call | 120 | +4,483 | 9,478 (0DTE pin) |
| BABA…C155 | 2026-08-21 | Call | 155 | +4,138 | 4,870 |
| BABA…C165 | 2026-08-21 | Call | 165 | +3,473 | 3,587 |
| BABA…C119 | 2026-07-24 | Call | 119 | +3,448 | 4,457 (0DTE) |
| BABA…C145 | 2026-08-21 | Call | 145 | +2,632 | 8,952 |
| BABA…C150 | 2026-09-18 | Call | 150 | +1,770 | 2,774 |

All-call build; the Aug 145–165 strikes are 26–43% OTM. High vol/OI on the 0DTE 119/120 =
speculative pin play (discount). The far-OTM Aug builds are the ambiguous ones (see Verdict).

### Closing / roll activity `[OI:decrease_with_volume]` / `[OI:position_rolls]`

Small call closes: 260807 C130 (−575), 270115 C150 (−520), 260731 C135 (−359). **No clean
near→far roll signature** (`position-rolls` returned 0 rows). Nothing structural.

### Smart positioning `[OI:smart_positioning]`

0DTE 120 call inferred **bullish** (net_ask_bid +1,123 — net bought, pin speculation). Aug
far-OTM tags **split**: 155 bullish, but **165 & 145 bearish** — inconsistent, so the "bullish"
label on the aggregate call build is **not reliable directional conviction**.

### Pin risk / OPEX concentration

`pin-risk` (DTE ≤ 7): **no BABA row** — nearest OPEX (07-31 weekly = 8 DTE, 08-21 = 29 DTE)
is outside the pin window; **skip pin commentary**. `opex-concentration`: BABA **outside** the
≥40%-concentration top list.

## Tool calls (audit)

| Datapoint | Command | jq path |
|-----------|---------|---------|
| walls | `uw oi oi-by-strike --symbol BABA --top-n 10 [--dte-max 30] --date 2026-07-23` | `.results[].{strike,call_oi,put_oi,net_oi,role,distance_pct}` |
| OPEX cliff | `uw oi term-structure --symbol BABA --date 2026-07-23` | `.term_structure[].{expiry,dte,pct_of_total_oi,call_oi,put_oi}` |
| OI builds | `uw oi biggest-increases --symbol BABA --top-n 20 --min-oi-change 500 --date 2026-07-23` | `.results[].{option_symbol,oi_diff_plain,volume}` |
| direction | `uw oi smart-positioning --symbol BABA --top-n 20 --min-oi-change 500 --date 2026-07-23` | `.results[].{option_symbol,inferred_direction,net_ask_bid}` |
| rolls/decreases | `uw oi decrease-with-volume` / `position-rolls --symbol BABA --date 2026-07-23` | `.results[]` |
| pin/opex | `uw oi pin-risk --dte-max 7` / `opex-concentration` (market-wide, filtered) | `select(.ticker=="BABA")` → none |

## Tool errors

None. `term-structure` array is under `.term_structure` (not `.results`); `biggest-increases`
has no `side`/`expiry` column — parsed from `option_symbol` per `[[deep-dive-json-field-traps]]`.

## Verdict for downstream

- **Positioning bias: call-tilted OI build, but directionally AMBIGUOUS.** Raw builds are
  14:2 call:put, yet concentrated far-OTM (Aug 145–165) with split smart-positioning tags →
  reads as **overwriting / speculative lottery, not conviction upside**. Combined with phase-1
  (non-aggressive call premium, net bearish) and phase-2 (block distribution), the honest call
  is **range-capped, not bullish**. The $120 call wall is a **ceiling**, not a launchpad.
- **Conviction: 3/5** that positioning is call-tilted; only **2/5** that it's directionally
  bullish (overwriting ambiguity is the reason).
- **Largest OI build as % of float: n/a** (no `fz` `Shs Float` for this ADR). Qualitatively a
  +4k-contract build (0.4M share-equiv) is immaterial vs BABA's multi-billion ADS float — **not
  structural on size**.
- **Three pin/cliff strikes for phase-9** (sourced from roles, not hand-picked):
  1. **Resistance $120** (call_wall, +5.2%, near-term net +26.8k) — coincides with phase-2
     overhead supply $116.85–118.22 → strong ceiling zone $118–120.
  2. **Support $110** (put_wall, −3.6%) → $105 → **$100** (biggest all-expiry put wall).
  3. **OPEX gravity well 2026-09-18** (27.6% OI, post-earnings); **$115 ATM battleground**
     (net_oi +1,460, essentially pinned).
- **Open questions:** Is the far-OTM Aug call build covered-call overwriting (range thesis) or
  genuine speculative upside? Does phase-4 max-pain sit near $115 (pin) — and does dealer GEX
  make $120 a hard cap? Phase-4 to resolve.
