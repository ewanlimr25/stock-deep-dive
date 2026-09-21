# Phase 4 — Dealer Structure & Gamma

**Ticker:** OKLO
**As-of date:** 2026-07-17
**Generated:** 2026-07-18T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

Dealer structure is **short-gamma and mechanically two-sided**. GEX is
**FULLY_NEGATIVE** (total −8.99M, all strikes negative — "strong gamma amplification"),
so any directional move gets *chased*, not dampened. DEX is deeply negative (−167M):
the public is net put-long, dealers are net short puts, and their hedge is to **sell
underlying** — a standing bearish mechanical lean, and the biggest negative-GEX strikes
sit right on the downside put walls ($35 −851K, $33 −475K), so a break toward $35 would
**accelerate**. Cutting the other way: skew is **COMPLACENT** (25Δ puts *cheaper* than
calls — no crash premium), vanna is positive (a **conditional upside squeeze if IV
collapses** post-OPEX), and **max pain sits at $47–$50, above spot $41.11** — the OI
gravity/ceiling coincides with the $50 call wall. Net: a volatile, amplification-prone
regime with a bearish mechanical tilt but a real mean-reversion/squeeze pull toward $47–50.

## Key signals

- **Short-gamma regime, FULLY_NEGATIVE GEX** total −8,985,854, ZGL null (no flip in range)
  — trend amplification [STRUCT:gex]
- **DEX −167.4M**: "dealers net short puts → hedge is to SELL underlying" — bearish
  mechanical bias [STRUCT:dex]
- **Negative GEX concentrated at $35 (−851K) / $33 (−475K)** — a downside break through
  these put walls is dealer-amplified [STRUCT:gex.per_strike]
- **Skew COMPLACENT**: put_25Δ_iv 0.9801 < call_25Δ_iv 0.9871 (skew −0.007, ratio 0.993)
  — no downside premium priced [STRUCT:term_skew]
- **Max pain $47–$50 above spot**: 07-17 $48 (+16.8%), 07-24 $47 (+14.3%), 07-31 $50
  (+21.6%) — OI magnet/ceiling near the $50 call wall [STRUCT:max_pain]
- **Vanna-squeeze primed**: net_vanna +1,942, "falling IV → dealers (short puts) cover by
  BUYING underlying" — conditional upside if vol crushes [STRUCT:vanna_charm]

## Detailed findings

### GEX — [STRUCT:gex]

- **regime: FULLY_NEGATIVE** — "All strikes have negative net GEX — strong gamma
  amplification." total_gex **−8,985,854**, underlying $41.41, **ZGL null** (no zero-gamma
  crossing in the surface → spot is in a wholly short-gamma zone).
- Most-negative strikes: **$35 (−851,138)**, **$33 (−474,586)**, $30 (−164,476), $25
  (−94,120). Negative gamma is stacked on the **downside put walls** (phase-3: $35 wall
  12,227 put OI, fresh $33) → a move down toward $35 is where dealer hedging most amplifies.
- Tool caveat quoted: "GEX most meaningful for index products and large-cap single stocks
  with deep OI" → treat OKLO's ZGL/levels as a **±2% coarse band**, not precise.

### DEX — [STRUCT:dex]

net_dex **−167,411,981** (call_dex +34.2M, put_dex −201.6M). Interpretation verbatim:
*"Public is net put-long → dealers net short puts → dealer hedge is to SELL underlying."*
Standing mechanical **sell pressure** — corroborates the phase-1/3 bearish/protective lean.

### Vanna + charm — [STRUCT:vanna_charm]

net_vanna **+1,942**, net_charm −452. Interpretation verbatim: *"Public net vanna positive
(put-heavy book). Falling IV → |put delta| drops → dealers (short puts) cover by BUYING
underlying. Classic vanna-squeeze setup if VIX collapses."* → **conditional upside**: a
post-OPEX / into-calm IV crush mechanically forces dealer buy-backs. The counterweight to
the negative-DEX sell lean. Watch IV30d (currently ~97%).

### IV term structure — [STRUCT:iv_term_structure / front_end_iv_ratio]

- `iv-term-structure` `structure = BACKWARDATION`, but this is **0DTE-distorted** (today is
  OPEX; the 07-17 front spikes). The cleaner **front-end 7-vs-30 DTE ratio = 0.965 → FLAT**
  (near_iv 0.964 vs far_iv 0.999, near slightly *below* far). No acute event-stress in the
  tradeable window; earnings 2026-08-10 (~24d out) not yet inverting the near curve.

### Term skew — [STRUCT:term_skew]

25Δ: put_iv **0.9801** vs call_iv **0.9871** → skew **−0.007**, ratio 0.993, interpretation
**COMPLACENT**. Puts are *not* bid over calls despite the bearish flow — the market is **not**
pricing crash risk. Read: the phase-1/3 put activity is orderly **hedging/rolling**, not
panic; and downside protection is *cheap* relative to calls for anyone wanting it.

### Max pain — [STRUCT:max_pain], spot $41.11

| Expiry | max_pain | dist% | put_call_oi_ratio |
|---|---|---|---|
| 2026-07-17 (OPEX, today) | $48 | +16.8% | 0.634 |
| 2026-07-24 | $47 | +14.3% | 1.64 |
| 2026-07-31 | $50 | +21.6% | 1.093 |
| 2026-08-07 / 08-14 | $50 | +21.6% | ~0.97 |

Max pain is **consistently above spot at $47–$50**, aligning with the phase-3 **$50 call
wall**. OI gravity therefore points *up* toward $47–50, yet price sits at $41 and today's
OPEX did not pin up — the bearish flow/negative-GEX mechanics are currently overriding the
static-OI magnet. Treat $47–50 as an **upside target/ceiling**, softening with distance
(tool caveat: static-OI estimate).

### Today's gamma flip

Run is **after-hours on OPEX day** — `today-gamma-flip` (0DTE intraday) not meaningfully
actionable EOD; skipped per skill guidance. The full-surface GEX above already reads short-gamma.

## Tool calls (audit trail)

| Command | Key value(s) ← `jq` path | Notes |
|---|---|---|
| `options-structure gex --dte-max 45` | FULLY_NEGATIVE, −8.99M, $35=−851K ← `.regime/.total_gex/.per_strike` | ±2% coarse |
| `options-structure dex --dte-max 45` | net −167.4M, "SELL underlying" ← `.net_dex/.interpretation` | |
| `options-structure vanna-charm` | +1,942, squeeze-if-IV-falls ← `.net_vanna/.vanna_interpretation` | conditional |
| `options-structure iv-term-structure` | BACKWARDATION (0DTE-distorted) ← `.structure` | |
| `options-structure front-end-iv-ratio 7/30` | 0.965 FLAT ← `.ratio/.regime` | cleaner read |
| `options-structure term-skew --dte-target 30` | COMPLACENT, ratio 0.993 ← `.interpretation` | |
| `options-structure max-pain --dte-max 30` | $48/$47/$50 above spot ← `.results[].max_pain` | static-OI |

## Tool errors

`iv-term-structure` per-row `iv` field returns `null` (regime label populated, per-expiry
IV not) — relied on the `structure` label + `front-end-iv-ratio` for the slope; no value
transcribed from a null. Not fatal.

## DATA NOTE / CORRECTION

The `iv-term-structure` "BACKWARDATION" label conflicts with the FLAT 7/30 front-end ratio;
resolved in favor of FLAT (the backwardation is a 0DTE-OPEX artifact). No number changed —
interpretation reconciled, both reads recorded.

## Verdict for downstream

- **Dealer regime:** **SHORT GAMMA (FULLY_NEGATIVE GEX)** — amplification/volatile, with a
  bearish DEX mechanical tilt (dealers selling) offset by a conditional vanna-squeeze-up.
- **Conviction:** 3 / 5 (regime signal is clear; direction is genuinely two-sided — GEX
  amplifies whichever way flow pushes).
- **Structural levels for phase-9:**
  1. **Downside acceleration $35–$33** — most-negative GEX strikes; a break here is dealer-amplified.
  2. **Gamma pivot ≈ spot $41 (ZGL null → whole near-range short-gamma)** — no dampening cushion above.
  3. **Max-pain / upside magnet $47–$50** — OI gravity + $50 call wall = the ceiling a squeeze targets.
- **Open questions:** Does a post-OPEX IV crush actually fire the vanna squeeze up, or does
  the negative-DEX sell lean + bearish flow win the break down? (Phase-5 historical
  post-OPEX behavior + phase-6 vol regime should adjudicate.) Why is skew COMPLACENT while
  positioning is bearish — hedging vs. genuine short conviction?
