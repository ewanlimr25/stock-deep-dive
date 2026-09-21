# Phase 4 — Dealer Structure & Gamma

**Ticker:** CMPS
**As-of date:** 2026-06-18
**Generated:** 2026-06-20
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **firmly long-gamma and pinning** — and that actively works
*against* phase-1's bearish LEAP-put thesis near-term. GEX is **FULLY_POSITIVE**
(every strike positive net GEX, no zero-gamma level), so dealers sell rallies and
buy dips → mean-reversion and suppressed realized vol. The largest GEX sits at **$13
(net_gex 1.87M)** with $12 second (1.22M); spot ($12.53 close) is pinned **inside the
heaviest gamma zone $12–13**. DEX is positive (+$30.65M) → public net call-long,
dealers net-short calls, dealer hedge = **buy underlying** (a supportive bid into
dips). Skew is **NORMAL** (25Δ put IV 102.9% vs call 98.25%, ratio 1.047 — no panic
tail-bid). Near-expiry **max pain = $12 (−4.15%)** for the 2026-07-17 cliff, a mild
downward magnet. Net: the chain mechanically pins $12–13 and dampens the very
downside the puts are positioned for; the bear case needs a gamma-flip/vol-expansion
or a fundamental catalyst, not this regime.

## Key signals

- GEX regime **FULLY_POSITIVE**, total_gex 4.85M, **no ZGL** → strong pin /
  long-gamma [STRUCT:gex]
- Largest GEX strike **$13 (1.87M)**, then $12 (1.22M) — spot pinned $12–13
  [STRUCT:gex]
- DEX **+$30.65M**, dealers net-short calls → hedge is to **buy dips** (supportive)
  [STRUCT:dex]
- Near-expiry **max pain $12 (−4.15%)**, 2026-07-17, P/C OI 0.026 [STRUCT:max_pain]
- Skew **NORMAL** (ratio 1.047) — options market pricing **no downside fear**,
  contradicting the bearish put [STRUCT:term_skew]
- Vanna negative (call-heavy book): **falling IV → mechanical dealer selling**
  (mild headwind given low IV rank) [STRUCT:vanna_charm]

## Detailed findings

### GEX (`[STRUCT:gex]`, underlying $12.44 in-tool)

- `regime` = **FULLY_POSITIVE**; `regime_description` = "All strikes have positive
  net GEX — strong gamma pinning effect"; `zero_gamma_level` = **null**; total_gex
  = 4,851,589.
- Top strikes: **$13 = 1,866,570** · $12 = 1,218,553 · $15 = 784,611 · $11 = 698,560.
- Tool `note`: GEX most meaningful for index/large-cap deep-OI names — **CMPS is
  small, treat ZGL/GEX as a coarse ±2% read** (per common-pitfalls).

### DEX (`[STRUCT:dex]`)

- net_dex **+30,650,023** (call_dex +32.2M, put_dex −1.58M).
- `interpretation`: "Public is net call-long → dealers net short calls → dealer hedge
  is to BUY underlying." → supportive dip-buying bid; reinforces the call-heavy book
  from phase-3.

### Vanna + charm (`[STRUCT:vanna_charm]`)

- net_vanna **−1,532** (call-heavy), net_charm +27,487.
- `vanna_interpretation`: "Public net vanna negative … Falling IV → call delta drops
  → dealers cut long-underlying hedge → SELLING pressure. Rising IV reverses." With
  IV rank low (20.35), the asymmetric risk is a further IV slide → mild mechanical
  selling. No vanna-squeeze setup (would need positive vanna + negative dealer delta).

### IV term structure (`[STRUCT:iv_term_structure]`)

- `structure` = **BACKWARDATION** (front IV > back) → nominal event-stress. **Caveat:**
  distorted by 0DTE pin-noise IV (the 6/18 $7C printed ~1586% IV, phase-1) and the
  thin small-name chain — treat as soft. Next earnings 2026-07-30 (phase-0.5) is the
  nearest scheduled catalyst.

### Term skew (`[STRUCT:term_skew]`, 30-DTE target)

- skew_ratio **1.047**, `interpretation` = **NORMAL**. 25Δ put IV 102.9% vs call IV
  98.25% — puts only marginally richer. **No tail-hedging skew** → the market is not
  corroborating a downside scare; the bearish LEAP put is idiosyncratic, not a
  skew-wide event.

### Front-end IV ratio (`[STRUCT:front_end_iv_ratio]`)

- `regime` = **FLAT**, ratio 1.0 — but near/far **both resolved to 27 DTE** (no
  distinct 7-DTE expiry exists; only 6/18-0DTE and 7/17 near-term). **Unreliable
  here** — single-expiry collapse; disregard the event-stress read from this tool and
  defer to iv-term-structure's (soft) backwardation.

### Today's gamma flip

- Skipped — `today-gamma-flip` is 0DTE intraday-only and this is an after-hours as-of
  run (executed 2026-06-20 for 2026-06-18). Not meaningful post-session.

### Max pain (`[STRUCT:max_pain]`, spot $12.52)

| Expiry | DTE | max_pain_strike | distance % | P/C OI | total_oi |
|--------|-----|-----------------|------------|--------|----------|
| 2026-06-18 | 0 | $11 | −12.14% | 0.481 | 22,926 (expired) |
| **2026-07-17** | 29 | **$12** | **−4.15%** | 0.026 | 29,029 |

Near-expiry magnet = **$12** (Jul-17 cliff). Agrees with phase-3: the $12 strike is
call_heavy (net_oi +8,824) and the 7/17 expiry is the 31.21% OPEX cliff. So a mild
gravity toward $12 sits just under the $12.53 close, capped by the $13 GEX/call wall.
Static-OI caveat: as today's flow settles, the magnet can migrate.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --dte-max 45` | regime=FULLY_POSITIVE, ZGL=null, total 4.85M ← `.regime,.zero_gamma_level`; top strike $13=1.87M ← `.per_strike\|sort_by(-.net_gex)` | per-strike |
| `uw options-structure dex --dte-max 45` | net_dex=+30.65M ← `.net_dex`; "hedge is to BUY" ← `.interpretation` | summary |
| `uw options-structure vanna-charm --dte-max 45` | net_vanna=−1,532 ← `.net_vanna`; falling-IV→selling ← `.vanna_interpretation` | summary |
| `uw options-structure iv-term-structure` | structure=BACKWARDATION ← `.structure` | term |
| `uw options-structure term-skew --dte-target 30` | ratio=1.047, NORMAL ← `.skew_ratio,.interpretation` | 25Δ |
| `uw options-structure front-end-iv-ratio --near 7 --far 30` | FLAT ratio=1.0, both 27 DTE (collapsed) ← `.regime,.near_dte_actual` | — |
| `uw options-structure max-pain --dte-max 30` | Jul-17 max_pain=$12 @ −4.15% ← `.results[1].max_pain_strike` | 2 exp |

## Tool errors

<none — all green. `front-end-iv-ratio` returned a degenerate single-expiry result
(documented above), not an error.>

## DATA NOTE / CORRECTION

- In-tool spot differs slightly per command (GEX $12.44, vanna $12.45, max-pain
  $12.52) vs the official close $12.53 — all within rounding/intraday-snapshot
  variance. **Phase-9 uses $12.53 (close).** No value re-read.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (FULLY_POSITIVE GEX, no flip)** — pinning,
  mean-reversion, suppressed vol. Mechanically *resists* the phase-1 bearish move.
- **Conviction:** **3 / 5** — the $12–13 pin and $12 max-pain magnet are clear and
  agree with phase-3 walls, but GEX is coarse on a small name (tool's own caveat).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **ZGL = none** (fully positive GEX) → spot deep in long-gamma; a flip would
     require heavy put-OI build below — watch the P10 LEAP settle.
  2. **Largest GEX strike $13** — overhead pin / resistance cap (= phase-3 call wall).
  3. **Vanna pivot:** falling-IV → dealer selling (mild); no squeeze setup.
  4. **Near-expiry max-pain $12 (−4.15%, Jul-17)** — the opex-gravity magnet just
     below spot.
- **Open questions:** Does the bearish put thesis require a **gamma flip** (negative
  GEX) that only materializes if the P10/lower-strike put OI builds substantially
  (phase-3 follow-through)? Is the BACKWARDATION real event-stress (a catalyst before
  7/30 earnings) or 0DTE-noise artifact (phase-6/7c to resolve)?
