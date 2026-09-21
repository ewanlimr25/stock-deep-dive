# Phase 4 — Dealer Structure & Gamma

**Ticker:** MU
**As-of date:** 2026-06-25 (post-close run)
**Generated:** 2026-06-25
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

The dealer structure reads **range-bound with a mild downward tactical lean** — a
meaningful counterweight to phase-1's bullish premium. GEX is **POSITIVE (dealers
net long gamma)**: the tool's own label is *"mean-reversion and reduced
volatility,"* so dealers sell rips / buy dips and damp realized vol — no trend
amplification in either direction. DEX is supportive (dealers net short calls →
structural hedge is to **buy** underlying, +$30.5B). But two structural headwinds
push down: (1) **vanna** — with IV deflating post-earnings (iv_rank 100→77, see
phase-0.5), the net-negative book means dealers *cut* their long hedge as call
deltas fall → mechanical **selling pressure**; and (2) **max-pain** sits far below
spot at every near expiry (6-26 → **1040**, −14.5%; 7-17 → 800), a downward
OI-gravity (soft/static-OI, partly offset by the positive gamma). Skew is
**COMPLACENT** (25Δ put/call ≈ 1.006 — no downside fear priced) and the term
structure is a **mild post-earnings backwardation normalizing** (front-end ratio
1.026 = FLAT). Spot ≈ **$1,207**.

## Key signals

- **GEX POSITIVE — dealers long gamma → mean-reversion / vol suppression** `[STRUCT:gex]`
- **DEX +$30.5B — dealers net short calls → hedge is to BUY underlying** (structural bid) `[STRUCT:dex]`
- **Vanna headwind: falling IV → dealer hedge SELLING** (net_vanna −6,777) `[STRUCT:vanna_charm]`
- **Max-pain far below spot: 6-26 → 1040 (−14.5%), 7-17 → 800 (−34%)** — downward gravity (soft) `[STRUCT:max_pain]`
- **Skew COMPLACENT (ratio 1.006); term structure mild backwardation normalizing post-earnings** `[STRUCT:term_skew / iv_term_structure / front_end_iv_ratio]`

## Detailed findings

### GEX `[STRUCT:gex]`

- `regime`: **POSITIVE** — *"Dealers net long gamma — expect mean-reversion and
  reduced volatility."*
- `zero_gamma_level`: 41.47 — **a coarse artifact** on a $1,207 stock (the
  zero-crossing landed on a worthless deep strike). Per-strike GEX magnitudes near
  spot (1085–1120) all round to ≈0Bn; `total_gex` +$51.5M is small but positive.
  **Read: gamma is positive across the tradeable range — spot is deep in
  long-gamma territory, no flip level near current price.** Treat as a vol-suppressed,
  mean-reverting regime; do not use 41.47 as a literal level.

### DEX `[STRUCT:dex]`

- `net_dex` +$30.46B (call_dex +$33.96B, put_dex −$3.49B).
- `interpretation`: *"Public is net call-long → dealers net short calls → dealer
  hedge is to BUY underlying."* A structural dealer **bid** — mildly supportive,
  and it explains how the +4% rally was partly mechanically chased by short-call
  hedging.

### Vanna + charm `[STRUCT:vanna_charm]`

- net_vanna **−6,777** (call_vanna −8,003, put_vanna +1,227); net_charm +1,042,869.
- `vanna_interpretation`: *"Public net vanna negative (call-heavy book). **Falling
  IV → call delta drops → dealers (short calls) cut long-underlying hedge →
  SELLING pressure.** Rising IV reverses."*
- **This is the key tactical headwind.** IV is actively deflating post-earnings, so
  the vanna flow is currently a **mechanical seller** — it works *against* the
  bullish call premium until IV stabilizes. If IV re-firms (e.g. a new catalyst),
  the mechanic flips to a bid.

### IV term structure `[STRUCT:iv_term_structure]`

- `structure`: **BACKWARDATION** (front IV > back IV) — but earnings passed ~6-23,
  so this is **residual post-earnings front-end elevation normalizing**, not forward
  event stress (next earnings 2026-09-22, far). Per the heuristic, do not trade this
  backwardation as a fresh signal — it's decaying.

### Term skew `[STRUCT:term_skew]`

- put_25Δ_iv 0.966 vs call_25Δ_iv 0.9604; skew 0.0055; **skew_ratio 1.006**;
  `interpretation`: **COMPLACENT**.
- Despite phase-3's heavy put-OI *build*, the **skew is essentially flat** — the
  options market is **not** pricing downside fear. Mechanically: downside protection
  is cheap (favourable for buying hedges). Contrarian-wise: complacency on an
  extended name is a mild yellow flag (no fear cushion if sentiment turns).

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

- near_iv (7DTE) 1.246 vs far_iv (29DTE) 1.2145; **ratio 1.026; regime FLAT.**
- IV levels are very high in absolute terms (~120–125%, normal for MU at $1,200),
  but the near/far ratio is flat — no acute event-stress hump. Consistent with "no
  imminent binary."

### Today's gamma flip

- **Skipped** — 0DTE intraday tool; this is a **post-close run**, so the intraday
  ZGL/flip read is not meaningful (per composition guidance). The standing GEX
  regime (POSITIVE) is the relevant gamma read.

### Max pain (opex-gravity) `[STRUCT:max_pain]` (spot ≈ $1,207)

| Expiry | max_pain | distance % | put_call_oi_ratio |
|--------|----------|------------|-------------------|
| **2026-06-26 (1DTE)** | **1040** | **−14.45%** | 1.76 |
| 2026-07-02 | 1015 | −16.5% | 1.99 |
| 2026-07-10 | 1000 | −17.74% | 4.77 |
| **2026-07-17 (OPEX)** | **800** | **−34.19%** | 1.77 |
| 2026-07-24 | 1020 | −16.09% | 0.93 |

Every near-expiry max-pain magnet sits **well below spot** — the chain's pain-minimizing
point is 14–34% under current price, because the rally pushed spot above OI built at
lower strikes. This is a **downward gravity**, BUT: (a) **static-OI caveat** — the
magnet migrates as OI rebuilds at higher strikes, so it's a *soft* pull, not a
target; and (b) the **positive-gamma regime cushions** the pull (dealers buy dips).
Net: a mild downward bias near-term, not a crash signal. Cross-check: phase-3's
6-26 OPEX cliff (22.55% of OI, put-heavy) and its 1000 put_wall_support roughly
agree with the 1000–1040 max-pain cluster.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|------------------|--------------------------|------|
| `options-structure gex --symbol MU --dte-max 45` | regime POSITIVE, total_gex +$51.5M, ZGL 41.47(artifact) ← `.regime,.total_gex,.zero_gamma_level` | per-strike |
| `options-structure dex --symbol MU --dte-max 45` | net_dex +$30.46B, dealers buy underlying ← `.net_dex,.interpretation` | agg |
| `options-structure vanna-charm --symbol MU --dte-max 45` | net_vanna −6,777, falling-IV → SELLING ← `.net_vanna,.vanna_interpretation` | agg |
| `options-structure iv-term-structure --symbol MU` | BACKWARDATION ← `.structure` | term |
| `options-structure term-skew --symbol MU --dte-target 30` | COMPLACENT, skew_ratio 1.006 ← `.interpretation,.skew_ratio` | 25Δ |
| `options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | ratio 1.026, FLAT ← `.ratio,.regime` | near/far |
| `options-structure max-pain --symbol MU --dte-max 30` | 6-26 → 1040 (−14.45%) ← `.results[].{max_pain_strike,distance_pct}` | per-exp |

## Tool errors

None. (`iv-term-structure` per-row `slope`/`iv` jq multiply hit a null cell — the
regime label `.structure` was read directly, no number transcribed from the null.)

## DATA NOTE / CORRECTION

GEX `zero_gamma_level` 41.47 is flagged as a **coarse artifact**, not a tradeable
level — corroborated by near-spot per-strike GEX ≈ 0 and the POSITIVE regime label,
which is what's carried downstream. No value re-read; this is an interpretation
guard, not a correction.

## Verdict for downstream phases

- **Dealer regime:** **LONG-GAMMA / mean-reverting** (vol suppressed, no trend
  amplification) **with a mild downward tactical lean** from (a) the vanna
  selling-mechanic while IV deflates and (b) max-pain gravity 14–34% below spot.
  DEX (dealers buy underlying) is a partial offsetting bid.
- **Conviction:** **3 / 5** — the structure is a genuine, multi-signal counterweight
  to the bullish flow: it caps explosive upside (long gamma) and adds a near-term
  downward drag (vanna + max-pain), while the complacent skew warns the downside
  isn't priced.
- **Three structural levels for phase-9 (+ max-pain pin):**
  1. **Spot ≈ $1,207** sits deep in **positive-gamma** territory → expect
     mean-reversion / range, not a vol-expansion breakout (no ZGL flip near spot).
  2. **Pin/magnet ~1200** (phase-3 call_heavy net +37k, −1.3%) is the nearest OI
     anchor; **GEX magnitudes are small**, so the pin is OI-driven, not gamma-walled.
  3. **Near-expiry max-pain = 1040 (6-26)** — the opex-gravity magnet, a soft
     downward pull ~14% below spot; 7-17 max-pain 800 deeper but static/soft.
- **Open questions:** Will IV stabilize (turning vanna from seller to bid) or keep
  crushing? Does the complacent skew + extended price set up a mean-reversion fade,
  or does the positive-gamma + dealer-bid simply hold a range? Phase-5 (historical
  win-rate) and phase-6 (macro/sector) should arbitrate whether this digests
  sideways or rolls over.
