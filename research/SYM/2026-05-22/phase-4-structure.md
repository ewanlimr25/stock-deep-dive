# Phase 4 — Dealer Structure & Gamma

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:11Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

SYM is in a **POSITIVE-gamma regime** with dealers net long gamma
[STRUCT:gex]. 45-DTE total GEX = **+$11.22M**, Zero Gamma Level = **$35.19**
(spot $50.26 → ~30% above ZGL). This produces a strong **mean-reversion
/ vol-suppression regime above ~$50**. The five biggest positive-GEX
walls form a **call-wall ladder** at $51 (+$5.67M), $52 (+$4.64M), $55
(+$1.19M), $50 (+$1.14M), $53 (+$1.08M) — these are mechanical
resistances where dealer hedging sells rallies. **Below ~$49.5 the
chain flips into a negative-GEX air pocket** (P49 −$356K, P47.5
−$989K, P45 −$677K, P42.5 −$1.17M) — if spot loses $49.50, dealer
hedging becomes pro-trend and would amplify any downside. Term skew
is **NORMAL** (25Δ put/call ratio 1.032 at 27 DTE) and the front-end
IV ratio is **0.95 (CONTANGO)** when 0DTE pin pricing is excluded —
no event-stress signal. Net dealer delta is +$33.6M (public is net
call-long → dealers short calls → **dealer hedge is to BUY
underlying** [STRUCT:dex]) — that's the mechanical bid that meets
every dip.

## Key signals

- **POSITIVE GEX regime, ZGL $35.19, spot $50.26**: total_gex
  +$11.22M [STRUCT:gex]. ~30% buffer above the flip — long-gamma is
  durable as long as spot stays above ~$49.
- **Massive $51 + $52 gamma wall ($10.31M combined GEX)**
  [STRUCT:gex]. The single most likely intraday magnet/cap. Phase-1
  bid-side LEAP calls and Phase-3 0DTE C52/C53 ask-side opens both
  build this wall.
- **Vanna-squeeze setup live**: net_vanna ≈ +5 (call -765, put +769),
  net_charm +8,647 [STRUCT:vanna_charm]. Tool's own
  interpretation: *"Falling IV → |put delta| drops → dealers (short
  puts) cover by BUYING underlying."* SYM IV is structurally elevated
  (~67-70% in 7-30 DTE) so any IV decay = mechanical bid.
- **Negative-gamma air pocket below $49.5**: P49.5 +$340K, then P49
  −$356K, P48 −$230K, P47.5 −$989K, P45 −$677K, P42.5 −$1.17M
  [STRUCT:gex]. **$49.5 is the dealer-hedge boundary; a daily close
  below would change regime.**
- **Term structure is "BACKWARDATION" label-only**: the
  front-month IV of 134.4% is driven entirely by 2026-05-22 0DTE pin
  pricing (delta-1 puts at IV 380-530%, mark in phase-1). Strip 0DTE
  and the curve is **upward-sloping normal**: 29-May 66.9% → Jun
  65-71% → Aug 76.6% → Jan-27 79.4% → Jan-28 80.9% [STRUCT:iv_term_structure].
- **Term skew NORMAL** (25Δ ratio 1.032), front-end IV ratio 0.95
  (CONTANGO) [STRUCT:term_skew, STRUCT:front_end_iv_ratio]. No
  tail-hedging panic and no event-stress crash bid.

## Detailed findings

### GEX (45-DTE, near-term hedging window)

**Spot $50.26 / ZGL $35.19 / total_gex +$11,216,424 → POSITIVE regime.**

Top 10 strikes by absolute GEX:

| Strike | net_gex | Role |
|--------|---------|------|
| 51 | +$5,674,954 | **support/call wall #1 (largest positive)** |
| 52 | +$4,636,331 | **support/call wall #2** |
| 55 | +$1,193,501 | call wall further OTM |
| 50 | +$1,140,917 | ATM wall — support |
| 53 | +$1,084,085 | call wall |
| 42.5 | −$1,168,765 | **put wall — biggest negative GEX, far OTM** |
| 47.5 | −$989,226 | put wall — closest large negative |
| 45 | −$677,161 | put wall |
| 60 | +$381,947 | upside ceiling |
| 49 | −$356,367 | first negative-GEX strike below spot |

The asymmetry is striking: **call-side GEX is concentrated in a
$50–$55 ladder; put-side GEX sits 5%+ below at $42.5–$47.5**. The
chain wants to keep SYM in the $50–$52 corridor.

### LEAP-inclusive GEX (365-DTE for context)

Including LEAPs, total_gex rises to **+$14.48M** and ZGL to **$37.46**.
Same shape, slightly more positive — the LEAP book is largely a
function of customers being long calls (which dealers hedge by being
short calls + long stock).

### DEX (dealer delta hedge)

| Metric | Value |
|--------|-------|
| call_dex | +$71,334,328 |
| put_dex  | −$37,704,958 |
| **net_dex** | **+$33,629,370** |
| spot | $50.33 |

Interpretation per tool: *"Public is net call-long → dealers net
short calls → dealer hedge is to BUY underlying."*
[STRUCT:dex]. This is a structural mechanical bid worth ~$33.6M of
delta-equivalent buying pressure as the chain re-hedges.

### Vanna + Charm

| Metric | Value |
|--------|-------|
| call_vanna | −765 |
| put_vanna | +769 |
| net_vanna | +5 (≈ neutral) |
| net_charm | +8,647 |
| spot | $50.30 |

Net vanna is ~0 (put_vanna almost exactly offsets call_vanna), but
the *put-vanna positive* leg means **any IV decline mechanically
forces dealers (short puts) to buy stock to re-hedge**
[STRUCT:vanna_charm]. With realized vol low and IV elevated, the
volatility-risk premium is high → if IV mean-reverts, expect a
vanna bid.

Net_charm +8,647 is a *positive time-decay tailwind*: as time passes
without a move, dealer hedge unwinds slightly favor the upside.

### IV Term Structure

| Expiry | Avg IV | Contract count |
|--------|--------|----------------|
| 2026-05-22 (0DTE) | **134.4%** | 164 |
| 2026-05-29 (7 DTE) | 66.9% | 179 |
| 2026-06-05 (14 DTE) | 66.5% | 73 |
| 2026-06-12 (21 DTE) | 65.1% | 23 |
| 2026-06-18 (OPEX) | 70.4% | 126 |
| 2026-06-26 (35 DTE) | 66.6% | 35 |
| 2026-07-02 | 71.6% | 4 |
| 2026-07-17 | 66.8% | 46 |
| 2026-08-21 | 76.6% | 78 |
| 2026-11-20 | 76.2% | 25 |
| 2027-01-15 | 79.4% | 113 |
| 2027-02-19 | 79.9% | 21 |
| 2028-01-21 | 80.9% | 16 |

Label is "BACKWARDATION" — but that is **entirely an artifact of
0DTE pin pricing** (today's expiry IV is 134% because near-zero
optionality is being marked synthetically). Once 0DTE drops off,
the curve is cleanly upward-sloping with **a small kink at the
2026-06-18 OPEX (70.4% vs 65–67% around it)** — modest June OPEX
event premium. Beyond that, the LEAP-out shape is healthy: term
structure rewards longer-dated vol.

**Phase-9 implication:** selling 2026-05-29 vol (66.9% IV) and
holding through pin decay captures the "fake backwardation" → normal
curve transition, with limited downside if the LEAP-curve is
intact.

### Term Skew (25Δ at 27-DTE)

| Metric | Value |
|--------|-------|
| put_25d_iv | 67.0% |
| call_25d_iv | 65.0% |
| skew (put-call) | +0.0206 (≈ 2.1 vol pts) |
| skew_ratio | 1.032 |
| interpretation | **NORMAL** |

No tail-hedging premium, no complacency. SYM is priced for symmetric
risk at the wing. This is rare in a high-IV name and supports a
non-directional vol-selling stance.

### Front-end IV Ratio (7 DTE / 27 DTE)

| Metric | Value |
|--------|-------|
| near_iv (7d) | 66.9% |
| far_iv (27d) | 70.4% |
| ratio | 0.95 |
| regime | **CONTANGO** |

When you remove the pin-pricing artifact, front IV is *lower* than
back IV — no event stress. Reinforces "fake backwardation" reading.

### Today's gamma flip (intraday for 2026-05-21)

| Metric | Value |
|--------|-------|
| spot | $50.36 |
| today_total_gex | +$10,974,185 |
| today_zero_gamma | **$44.53** |
| atm_flip_strike | 43 |
| regime | **POSITIVE** |

Today's key intraday walls (all 2026-05-22 expiry):
- **$51 — support wall ($5.55M GEX)**
- **$52 — support wall ($3.70M GEX)**
- $53 — support wall ($879K)
- $50 — support wall ($614K)
- $49.5 — support wall ($347K)

Reading: spot was pinned in the $50–$51 band for the session by
dealer long-gamma hedging. The $44.53 today-ZGL is so far below
spot it is operationally irrelevant; the practical decision boundary
is the $49.5 wall.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | symbol=SYM, dte-max=45, date=2026-05-21 | regime POSITIVE, total_gex +$11.22M, ZGL $35.19 |
| `mcp__uw-pp__options_structure_gex` | symbol=SYM, dte-max=365, date=2026-05-21 | LEAP-inclusive: total_gex +$14.48M, ZGL $37.46 |
| `mcp__uw-pp__options_structure_dex` | symbol=SYM, dte-max=45, date=2026-05-21 | net_dex +$33.6M; dealers buying underlying |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol=SYM, dte-max=45, date=2026-05-21 | net_vanna ~0, classic squeeze setup if IV falls |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol=SYM, date=2026-05-21 | "BACKWARDATION" (artifact); strip 0DTE = normal upslope |
| `mcp__uw-pp__options_structure_term_skew` | symbol=SYM, dte-target=30, date=2026-05-21 | NORMAL, skew ratio 1.032 |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol=SYM, near-dte=7, far-dte=30, date=2026-05-21 | CONTANGO 0.95 |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol=SYM, date=2026-05-21 | today_ZGL $44.53, walls $50/51/52/53 |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **mean-reversion long-gamma regime with a
  mechanical upside drift toward the $51–$52 wall**. Vol is
  structurally rich; skew is fair. Net dealer hedge is a steady
  buy-flow of underlying.
- **Conviction:** 4/5. Multiple independent signals agree
  (positive GEX, positive DEX, vanna-squeeze setup, normal skew,
  contango when 0DTE is stripped). Capped at 4 because SYM is a
  mid-liquidity name and per-strike GEX numbers ($1–5M) are small
  vs index products — coarse ±2% band around levels.
- **Three structural levels for phase-9:**
  1. **$51–$52 — call/support wall ($10.31M combined GEX).**
     Magnetic intraday target while in long-gamma regime; rallies
     above $52 face cumulative GEX resistance up to $55.
     **Tactical use:** sell short-dated calls at/above $52; cover
     longs if a sustained close above $52 fails to attract
     follow-through.
  2. **$49.5 — first dealer-hedge boundary.** Below this is the
     negative-GEX air pocket ($47.5/$45/$42.5). **Tactical use:**
     daily close < $49.50 = regime change → flip from long-gamma
     thesis to negative-gamma / pro-trend down.
  3. **$35.19 — 45-DTE ZGL (regime invalidation).** Spot needs to
     drop ~30% to genuinely flip. **Tactical use:** structural
     stop / catastrophic exit for any long thesis. Below $35,
     dealer hedging becomes destabilizing.
- **Open questions:**
  - Phase-5 historical: is the current GEX regime in line with the
    multi-month average, or unusually positive (squeeze-fade
    setup)? Look at `historical_gex_time_series`.
  - Phase-6 macro: what catalysts (earnings, sector news) could
    flip IV from current 67-70% sharply enough to fire the
    vanna squeeze? Earnings calendar check needed.
  - Phase-7 insights: does the `playbook_suggest_strategy` tool
    recommend the same vol-selling / call-wall-fade structure?
