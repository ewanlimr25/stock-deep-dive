# Phase 4 — Dealer Structure & Gamma

**Ticker:** BBAI
**As-of date:** 2026-05-29
**Generated:** 2026-05-31 (re-verified against validated JSON — supersedes an earlier draft that mis-read the GEX sign)
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

> **## DATA NOTE.** Figures are from JSON-validated `uw options-structure` output
> (`gex`/`dex`/`vanna-charm`/`iv-term-structure`/`term-skew`/`front-end-iv-ratio`/
> `max-pain`). The `gex` leaf returns **clean, real per-strike values** (an earlier
> draft wrongly called them synthetic and inverted the regime to "short gamma" — that
> was a field-name error on my side, now corrected).

## Summary

BBAI is in a **positive-gamma (long-gamma) regime with a powerful dealer pin at
$5.00.** `total_gex` is **+$100.2M** with the **Zero Gamma Level at $2.64**, far
below spot $5.04 → dealers are **net long gamma → they sell rallies and buy dips =
vol-suppressing, mean-reverting, pinning**. The pin is overwhelmingly at **$5.00:
+$82.0M of GEX** (vs $7.4M at $5.5, $4.3M at $6) — the single dominant stabilizer,
right at spot. Net DEX is **+$57.5M** (dealers net-short the public's calls → their
delta hedge **buys** the underlying = a supportive bid into dips). Skew is
**COMPLACENT** (25Δ call IV 1.238 > put IV 1.009, ratio 0.815 — the crowd pays up
for calls, not protection) and near-week IV is **front-loaded** (front-end ratio
1.104 backwardation) while max pain sits **below market at $4.00**. Net structural
read: **the +6% pop is into a long-gamma $5 pin — upside is dampened (dealers sell
strength), downside is cushioned (dealers buy weakness), bias is mean-reversion
toward $5.**

## Key signals

- **Long-gamma / POSITIVE regime**: `total_gex +$100.2M`, `ZGL $2.64` ≪ spot $5.04
  → dealers dampen moves (sell rallies / buy dips) [STRUCT:gex]
- **$5.00 = dominant positive-GEX pin: +$82.0M** (next: $5.5 +$7.4M, $6 +$4.3M,
  $4.5 +$3.8M) — a strong stabilizer at spot [STRUCT:gex]
- **DEX +$57.5M** — "public net call-long → dealers net short calls → hedge BUYS
  underlying" = supportive dip-bid [STRUCT:dex]
- **Skew COMPLACENT**: 25Δ call IV 1.238 > put IV 1.009 (ratio 0.815) — call
  chasing, no downside hedge demand [STRUCT:term-skew]
- **Front-loaded near-week IV** (front-end ratio 1.104, near 1.21 / far 1.09);
  overall term `CONTANGO`; **max pain $4.00 (−21%)** for 5/29–6/26 [STRUCT:front-end-iv-ratio][STRUCT:max-pain]

## Detailed findings

### GEX / dealer gamma (`uw options-structure gex`)

| field | value |
|-------|-------|
| `regime` | **POSITIVE (long gamma)** |
| `total_gex` | **+$100,156,760** |
| `zero_gamma_level` | **$2.64** (≪ spot $5.04) |
| top GEX strikes | **$5 +$82.0M**, $5.5 +$7.4M, $6 +$4.3M, $4.5 +$3.8M, $7 +$1.2M |
| only negative strike | $3.5 −$0.33M (negligible) |

→ Spot sits **far above** the ZGL, deep in **long-gamma** territory. Dealers
**sell rallies / buy dips**, suppressing realized vol and **pinning price to $5**
(where +$82M of stabilizing gamma is concentrated). This **caps** an upside
squeeze and **cushions** downside — the structural opposite of a short-gamma
trend-amplifier. (Convention note: DEX shows dealers short the public's calls; the
net GEX including the full book is still positive — the regime label is the tool's.)

### DEX / dealer delta (`uw options-structure dex`)

- `net_dex +$57.5M` (call_dex +$67.3M, put_dex −$9.8M). Interpretation: **public
  net call-long → dealers net short calls → hedge BUYS underlying** — a mechanical
  supportive bid, consistent with phase-2's large-tier dark-pool buying.

### Vanna / charm (`uw options-structure vanna-charm`)

- `net_vanna −4,727` (small/negative), `net_charm +292,944`. No vanna-squeeze
  tailwind (IV is not collapsing; skew complacent). Treat as neutral.

### IV term structure & skew

| read | value | meaning |
|------|-------|---------|
| term structure | **CONTANGO** overall; near-week front-loaded | front weeks ~110–121% IV |
| front-end ratio | **1.104** (near 1.207 / far 1.093) | mild backwardation in the front |
| 25Δ skew | **COMPLACENT** (call 1.238 > put 1.009, ratio 0.815) | calls bid, no put hedge demand |

→ The crowd is **paying up for calls, not protection** — a contrarian caution that
aligns with phase-1 call-writing/distribution, phase-0.5's blow-off read, and a
long-gamma pin that punishes the call chase.

### Max pain (`uw options-structure max-pain`)

| expiry | max-pain | dist% |
|--------|----------|-------|
| 2026-05-29 → 06-26 | **$4.00** | −21.1 |
| 2026-07-02 / 07-10 | $4.50 | −11.2 |
| 2026-07-17 | $5.00 | −1.4 |

→ Static-OI max pain sits **below market at $4** into the 6/18 cliff — a soft
downward magnet beneath the $5 gamma pin. Treat as indicative (static-OI caveat),
but it reinforces that the chain's payoff-gravity is **not above** spot.

## Tool calls (audit trail)

| Command | Result |
|---------|--------|
| `uw options-structure gex --symbol BBAI --dte-max 45 --date 2026-05-29` | POSITIVE, total_gex +$100.2M, ZGL $2.64, $5 +$82M |
| `uw options-structure dex --symbol BBAI --dte-max 45 --date 2026-05-29` | net_dex +$57.5M, hedge buys underlying |
| `uw options-structure vanna-charm --symbol BBAI --dte-max 45 --date 2026-05-29` | net_vanna −4,727; no squeeze |
| `uw options-structure iv-term-structure --symbol BBAI --date 2026-05-29` | CONTANGO; near-week front-loaded |
| `uw options-structure term-skew --symbol BBAI --dte-target 30 --date 2026-05-29` | COMPLACENT, ratio 0.815 |
| `uw options-structure front-end-iv-ratio --symbol BBAI --near-dte 7 --far-dte 30 --date 2026-05-29` | 1.104 BACKWARDATION |
| `uw options-structure max-pain --symbol BBAI --date 2026-05-29` | $4.00 near-term, rising to $5 by 7/17 |

## Tool errors

- First attempt used non-existent leaves `gamma-exposure`/`gamma-flip`/`skew`
  (corrected to `gex`/`today-gamma-flip`/`term-skew`). An intermediate draft
  mis-extracted GEX (wrong field names → nulls) and wrongly inferred "short gamma";
  the validated `gex` output (POSITIVE, ZGL $2.64) is used here.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA / POSITIVE** (spot $5.04 ≫ ZGL $2.64) → vol
  suppression, **$5 pin**, rallies dampened / dips cushioned (mean-reverting).
- **Conviction:** 3/5 — GEX/skew/max-pain are clean and mutually consistent (long
  gamma + complacent skew + sub-spot max pain all point to a capped, pinned $5).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **$5.00** — dominant +GEX pin (+$82M) / spot / phase-3 call_heavy / DP shelf:
     the gravity center & mean-reversion target.
  2. **$5.50** — next GEX strike / call wall = dampened upside resistance.
  3. **$4.00** — near-term **max-pain** magnet ($4.50 first step); ZGL flip only at
     $2.64 (far away — long gamma is secure unless price collapses).
- **Open questions:** Does the long-gamma pin + complacent skew + negative net call
  premium (phase-1) override the 26% short float (phase-7c) — i.e. is the squeeze
  capped? Phase-8b must weigh "dealer pin caps the bounce" vs "short squeeze /
  contract-news momentum (phase-6)".
