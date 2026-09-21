# Phase 4 — Dealer Structure & Gamma

**Ticker:** SMR
**As-of date:** 2026-06-16
**Generated:** 2026-06-17T11:58:56Z
**Upstream phases cited:** phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **range-bound-with-a-hard-ceiling-at-$10, leaning mildly
bearish on the hedge.** The blended ≤45-DTE GEX surface is labeled **POSITIVE /
long-gamma** (`zero_gamma_level=4.4`, far below spot $10 → mean-reversion regime),
**but the front 06-18 expiry alone is short-gamma** (`today-gamma-flip` regime
NEGATIVE, flip $7.5) with the **single heaviest gamma node a resistance wall right
at $10** (`gex −3.73M`). Dealer delta hedge is to **SELL underlying** (`net_dex
−$28.2M`, public net put-long). Vol surface shows **no downside fear** —
25Δ skew is **COMPLACENT** (calls *richer* than puts, `skew_ratio 0.957`) — and a
**conditional vanna-squeeze** sits underneath (dealers short puts would *buy* if IV
collapses). Near-expiry **max pain is $12** but that's 21% above spot — not a
realistic 2-day magnet; the call-heavy 06-18 book more likely **decays in the
writers' favour**. Conviction 2.

## Key signals

- **$10 is the dominant gamma wall** (= spot): `today-gamma-flip` key_walls →
  $10 `gex −3,731,168` **resistance_wall**, $9 −1.09M resistance, $12 +1.09M /
  $11.5 +0.52M / $11 +0.48M support [STRUCT:today_gamma_flip].
- **Dealer hedge = sell underlying:** `net_dex −28,153,184`, "Public net put-long →
  dealers net short puts → dealer hedge is to SELL underlying" (put_dex −$52.9M vs
  call_dex +$24.7M) [STRUCT:dex].
- **Complacent skew (no downside bid):** 25Δ call IV 0.9988 > 25Δ put IV 0.9561,
  `skew −0.0427`, `interpretation=COMPLACENT` — calls richer than puts on an
  18%-short name (squeeze-aware, not crash-fearing) [STRUCT:term_skew].
- **Front-expiry short-gamma vs broad long-gamma:** 06-18 `today_total_gex
  −2,566,313` (NEGATIVE, flip $7.5) inside a ≤45-DTE `regime=POSITIVE` (ZGL $4.4) →
  amplification risk *into* 06-18, mean-reversion beyond [STRUCT:gex].
- **Near-expiry max pain $12 (06-18), 21.46% OTM**, P/C OI 0.433 — above spot and
  unreachable in 2 days → 06-18 OTM calls likely expire worthless
  [STRUCT:max_pain].

## Detailed findings

### GEX (≤45 DTE) — [STRUCT:gex]

`regime=POSITIVE` · `regime_description="Dealers net long gamma — expect
mean-reversion and reduced volatility"` · `zero_gamma_level=4.4` · spot $10 ·
`total_gex=-1,170,071`. Per-strike, the large **negative** gamma nodes sit *below*
spot ($8 `−618,173`, $8.5 `−271,294`, $7 `−85,497`) — i.e. a short-gamma air-pocket
under $8.5 that a break could accelerate into, while spot ($10) sits in the
long-gamma zone above ZGL. (See DATA NOTE on the label-vs-total_gex sign tension.)

### DEX (≤45 DTE) — [STRUCT:dex]

`net_dex=-28,153,184` (call_dex +24.7M / put_dex −52.9M). Public is **net
put-long** → dealers net short puts → **dealer hedge is to SELL underlying** — a
standing mechanical supply consistent with phase-1/2's bearish lean. On an
18%-short name this "public put-long" may partly be shorts hedging, not fresh
bears.

### Vanna + charm (≤45 DTE) — [STRUCT:vanna_charm]

`net_vanna +563` (put_vanna +2,093 / call_vanna −1,530), `net_charm +316,041`.
Interpretation: *"Public net vanna positive (put-heavy book). Falling IV → |put
delta| drops → dealers (short puts) cover by BUYING underlying. Classic
vanna-squeeze setup if VIX collapses."* → **a conditional bullish/upside risk to
the bearish thesis** if IV/VIX falls. Flag for phase-8b.

### IV term structure & front-end — [STRUCT:iv_term_structure]

`structure=BACKWARDATION` (whole curve — front 2-DTE 06-18 IV is mechanically
elevated). But `front-end-iv-ratio` (near 9-DTE 1.0369 vs far 30-DTE 1.0636) =
**FLAT** (ratio 0.975, mild contango) → **no genuine 9–30-DTE event stress**
(earnings 08-06 is ~7 weeks out). The backwardation is a 2-DTE artifact, not a
catalyst tell.

### Term skew — [STRUCT:term_skew]

`COMPLACENT`: 25Δ put 0.9561 vs 25Δ call 0.9988 → **calls richer than puts**
(`skew_ratio 0.957`). No tail-hedging bid; if anything an upside-call bid (the
squeeze-aware market). This **tempers the bearish conviction** — the vol surface is
not confirming a breakdown.

### Today's gamma flip (06-18 front expiry; intraday tool, EOD snapshot) — [STRUCT:today_gamma_flip]

`regime=NEGATIVE`, `today_zero_gamma=7.5`, `atm_flip_strike=7.5`, spot $10.04,
`today_total_gex=-2,566,313`.

| Strike | gex | role |
|--------|-----|------|
| **$10** | −3,731,168 | **resistance_wall** (heaviest) |
| $9 | −1,090,539 | resistance_wall |
| $12 | +1,093,550 | support_wall |
| $11.5 | +517,918 | support_wall |
| $11 | +484,874 | support_wall |

Into the 2-DTE OPEX, dealers are **short gamma**, so a move through $10 can be
amplified; $10 is the pivot/ceiling. (Caveat: `today-gamma-flip` is an intraday
0DTE tool — quoted here as the 06-16 EOD snapshot of the front expiry, not a live
read.)

### Max pain (≤30 DTE) — [STRUCT:max_pain]

| Expiry | DTE | max_pain | dist% | P/C OI | total_oi |
|--------|-----|----------|-------|--------|----------|
| **2026-06-18** | 2 | **$12** | +21.46 | 0.433 | 163,940 |
| 2026-06-26 | 10 | $11.5 | +16.4 | 0.782 | 24,518 |
| 2026-07-02 | 16 | $11.5 | +16.4 | 0.893 | 10,179 |
| 2026-07-10 | 24 | $11 | +11.34 | 0.618 | 7,050 |

**All max-pain strikes sit ABOVE spot ($9.88)** because the chain is call-OI-heavy.
The 06-18 magnet at $12 is 21% away and unreachable in 2 days → realistically those
OTM calls decay (favouring writers, per phase-1/3). Cross-check vs phase-3: $12 is
also the `oi-by-strike` call-wall — **structures agree on $12 as the upper bound**,
while the realistic near-term gravity is the $10 gamma wall / put-heavy strike.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --symbol SMR --dte-max 45 --date 2026-06-16` | regime=POSITIVE, ZGL=4.4, total_gex=−1.17M ← top-level | per-strike |
| `uw options-structure dex --symbol SMR --dte-max 45 --date …` | net_dex=−28,153,184 ← `.net_dex`; hedge=SELL | aggregate |
| `uw options-structure vanna-charm --symbol SMR --dte-max 45 --date …` | net_vanna +563, conditional squeeze ← `.vanna_interpretation` | aggregate |
| `uw options-structure iv-term-structure --symbol SMR --date …` | structure=BACKWARDATION ← `.structure` | curve |
| `uw options-structure term-skew --symbol SMR --dte-target 30 --date …` | COMPLACENT, skew=−0.0427 ← `.interpretation`/`.skew` | 25Δ |
| `uw options-structure front-end-iv-ratio --symbol SMR --near-dte 7 --far-dte 30 --date …` | FLAT, ratio 0.975 ← `.regime` | 9v30 dte |
| `uw options-structure today-gamma-flip --symbol SMR --date …` | NEGATIVE, $10 wall gex −3.73M ← `.key_walls` | front exp |
| `uw options-structure max-pain --symbol SMR --dte-max 30 --date …` | 06-18 max_pain=$12 dist 21.46% ← `.results[0]` | 4 expiries |

## Tool errors

(none — all reads jq-validated. `iv-term-structure.term_structure[]` per-row
`dte`/`iv` fields returned null under the names tried; the headline `.structure`
regime label is intact and used.)

## DATA NOTE / CORRECTION

**GEX label vs total_gex sign tension:** `gex` (≤45 DTE) reports `regime=POSITIVE`
(spot $10 above ZGL $4.4 → long-gamma by the spot-vs-ZGL rule) while
`total_gex=−1,170,071` is negative (dominated by the deep-OTM put gamma at $8).
Per the phase rule I **quote the tool's regime label verbatim (POSITIVE)** and do
not re-derive; the negative total is flagged, not used to override. The
front-expiry `today-gamma-flip` (NEGATIVE, flip $7.5) is the spot-relevant
near-term read and is treated as the tradeable gamma picture into 06-18.

## Verdict for downstream phases

- **Bias from this phase:** **Range-bound / transitional, mild bearish hedge** —
  $10 gamma ceiling, dealer delta-hedge sells, but complacent skew + conditional
  vanna-squeeze cap the bearish conviction.
- **Conviction:** **2/5** (structure is range-defining, not strongly directional;
  front short-gamma vs broad long-gamma split).
- **Three structural levels for phase-9 (+ max-pain pin):**
  1. **$10 — dominant gamma resistance wall** (= spot; front-expiry pivot/ceiling).
  2. **ZGL $4.4 broad / $7.5 front** — short-gamma air-pocket only *below* ~$8.5
     (acceleration risk if it breaks; not near-term).
  3. **$12 — upper structural cap** (support_wall in front gamma + 06-18 max-pain +
     phase-3 call-wall — triple-confirmed ceiling).
  - **Near-expiry max-pain pin: $12 (06-18)** — indicative only (21% OTM, static-OI).
- **Open questions:** Does insights/composite (phase-7) corroborate the
  range-bound + mild-bearish read? Does the COMPLACENT skew + conditional
  vanna-squeeze argue against shorting here (phase-8b bull case)? Is the public
  put-long DEX genuine bears or short-base hedging (phase-7c short interest)?
