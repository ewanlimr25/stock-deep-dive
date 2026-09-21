# Phase 4 — Dealer Structure & Gamma

**Ticker:** RKT
**As-of date:** 2026-07-17
**Generated:** 2026-07-19T19:41:00-04:00
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md

## Summary

Dealer structure is **range-suppressing now, coiled for an earnings break.** The
tool labels the regime **POSITIVE / "dealers net long gamma — expect mean-reversion
and reduced volatility"** with ZGL **$9.66** far below spot $14.57 → structurally
long-gamma. But the single largest GEX pocket is **−$48.5M at the $14.5 ATM strike**
(dealers short the customer-bought straddle from phase-1), which drags headline
`total_gex` to **−$28.5M** — i.e. a local short-gamma pocket at the money inside a
long-gamma book. **DEX is +$51M and dealers must BUY underlying to hedge** (a
supportive mechanical bid, matching phase-2 accumulation). IV is in **backwardation**
with a front-end ratio 0.896 (earnings 07-30 stress just beyond the 7-day window),
while **skew is NORMAL (1.031)** — no tail-hedging panic. **Max-pain magnets cluster
$14–14.5**, at/just below spot. Net: the $14–15 cage holds in ordinary tape, but the
ATM short-gamma pocket + backwardation say the **07-30 earnings is the release valve**.

## Key signals

- **GEX regime POSITIVE / long-gamma**, ZGL **$9.66** ≪ spot $14.57 → mean-reversion / vol-suppression `[STRUCT:gex]`
- **ATM short-gamma pocket −$48.5M at $14.5** (dealers short the long straddle) → headline total_gex −$28.5M; break-accelerant at the money `[STRUCT:gex per_strike]`
- **DEX +$51.1M, "dealers net short calls → hedge is to BUY underlying"** → supportive bid, confirms phase-2 accumulation `[STRUCT:dex]`
- **IV BACKWARDATION**, front-end ratio 0.896 (near 0.613 < far 0.685) → 07-30 earnings event stress `[STRUCT:iv-term-structure / front-end-iv-ratio]`
- **Max-pain $14 (07-24) → $14.5 (07-31, earnings expiry)**, at/below spot → mild downward-to-neutral pin `[STRUCT:max-pain]`

## Detailed findings

### GEX `[STRUCT:gex]`

- **Regime (tool label):** `POSITIVE` — "Dealers net long gamma — expect
  mean-reversion and reduced volatility."
- **Zero Gamma Level:** **$9.66** (spot $14.57 firmly above → long-gamma regime).
- **Headline total_gex:** −$28,483,978 (net slightly negative — see ATM pocket).
- **Largest per-strike GEX (net_gex):**

| Strike | net_gex | Read |
|---|---|---|
| **14.5** | **−48,519,285** | ATM short-gamma pocket (dealers short the customer straddle) — break-accelerant |
| **15.0** | **+13,075,787** | positive-gamma wall = reinforces the $15 cap/pin |
| 16.0 | +4,423,252 | secondary positive-gamma ceiling |
| 13.5 | −2,641,561 | minor short-gamma (put support strike) |
| 15.5 | +1,959,697 | positive |

**Interpretation tension (flagged):** the ZGL-based `regime` reads long-gamma, yet
`total_gex` is negative because the −$48.5M ATM pocket dominates. Reconciliation:
the *structural* book (call OI $15–19) is long-gamma and pins the range, but *at the
money* dealers are short the earnings straddle → local hedging would **amplify** a
move through $14.5. Range-bound in quiet tape; primed to run on the catalyst.

### DEX `[STRUCT:dex]`

- **net_dex +51,091,169.** Interp: *"Public is net call-long → dealers net short
  calls → dealer hedge is to BUY underlying."* → a mechanical **bid under the stock**,
  consistent with phase-2's continuous dark-pool accumulation and phase-3's structural
  +45k Mar-27 $19C. Constructive.

### Vanna + charm `[STRUCT:vanna-charm]`

- Net vanna −3,673, net charm +94,200, **no squeeze signal**. Minor / not a
  vanna-squeeze setup. De-emphasized.

### IV term structure & event stress `[STRUCT:iv-term-structure / front-end-iv-ratio]`

- **Structure: BACKWARDATION** — front IV elevated → event stress.
- **Front-end IV ratio 0.896** (near_iv 0.6133 @7-DTE < far_iv 0.6845 @30-DTE):
  the 30-day captures the **07-30 earnings**; the 7-day (07-24 weekly) does not →
  vol is priced into the post-earnings tenor. Textbook pre-earnings term shape.

### Term skew `[STRUCT:term-skew]`

- **Interpretation: NORMAL**, skew_ratio **1.031** (25Δ puts only ~3% richer than
  calls). No steepening → the phase-1 put buying is hedging/straddle, **not** panic
  tail-demand. Softens any "bearish fear" read.

### Max pain (opex gravity) `[STRUCT:max-pain]`

| Expiry | Max-pain | dist % | put/call OI ratio |
|---|---|---|---|
| 2026-07-17 (today) | $14.0 | −3.81 | 0.655 |
| 2026-07-24 (straddle wk) | $14.0 | −3.81 | 0.31 (call-heavy) |
| **2026-07-31 (post-earnings)** | **$14.5** | **−0.38** | 0.209 (very call-heavy) |
| 2026-08-07 | $15.0 | +3.06 | 0.146 |
| 2026-08-14 | $14.0 | −3.81 | 1.509 (put-heavy) |

Near-expiry magnets sit **$14–14.5**, i.e. at/just below spot — a mild
downward-to-neutral pull. The 07-31 magnet ($14.5, ~at spot) and $15 by 08-07 bracket
the same $14–15 cage phases 2–3 drew. *Caveat (tool):* static-OI snapshot; near-expiry
strikes are the tradeable magnets, far ones indicative only.

### Today's gamma flip

**Skipped** — run is after-hours (as-of 2026-07-17, executed 2026-07-19); 0DTE
intraday flip not meaningful.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows |
|---|---|---|
| `uw options-structure gex --symbol RKT --dte-max 45` | regime POSITIVE, ZGL 9.66, total_gex −28.5M; $14.5 net_gex −48.5M ← `.regime`/`.zero_gamma_level`/`.per_strike[].net_gex` | book+strikes |
| `uw options-structure dex --symbol RKT --dte-max 45` | net_dex +51.1M, "hedge is to BUY underlying" ← `.total_dex`/`.interpretation` | 1 |
| `uw options-structure vanna-charm --symbol RKT --dte-max 45` | vanna −3,673, charm +94,200, no squeeze ← `.net_vanna`/`.net_charm` | 1 |
| `uw options-structure iv-term-structure --symbol RKT` | BACKWARDATION ← `.structure` | term |
| `uw options-structure term-skew --symbol RKT --dte-target 30` | NORMAL, 1.031 ← `.interpretation`/`.skew_ratio` | 1 |
| `uw options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | 0.896 (0.613/0.685) ← `.ratio`/`.near_iv`/`.far_iv` | 1 |
| `uw options-structure max-pain --symbol RKT --dte-max 30` | $14 (07-24) / $14.5 (07-31) ← `.results[].max_pain` | 5 expiries |

## Tool errors

None. GEX `per_strike` headline `gex` alias returned null on first probe; the live
field is `net_gex` — re-read (below). All values traced to `jq` paths above.

## DATA NOTE / CORRECTION

First GEX per-strike jq used `.gex`/`.gamma_exposure` (null); the actual field is
`.per_strike[].net_gex` — re-read, giving the $14.5 −48.5M pocket. Regime/ZGL quoted
**verbatim** from the tool's `regime`/`regime_description`/`zero_gamma_level` (not
re-derived) per phase-4 rule; the total_gex-vs-regime sign tension is reported as a
finding, not silently reconciled.

## Verdict for downstream phases

- **Dealer regime:** **Long-gamma / range-suppressing (transitional at the money).**
  ZGL $9.66 ≪ spot → structurally long-gamma (mean-reversion), but a −$48.5M ATM
  short-gamma pocket + IV backwardation mean the **07-30 earnings is the break
  catalyst**. DEX bid is supportive/constructive.
- **Conviction:** **3 / 5** — regime, DEX, skew, and max-pain all cohere with the
  phases 2–3 range/accumulation read; docked for the total_gex-vs-ZGL sign tension
  and coarse ZGL on a lower-liquidity name (±2% band).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **$14.5** — largest-magnitude GEX strike (ATM short-gamma pivot) **and** the
     07-31 max-pain magnet **and** phase-3 put-support: the mean/pin the market
     defends; the break level for an earnings move.
  2. **$15.0** — positive-gamma wall (+$13.1M GEX) = the cap; coincides with phase-3
     $15 call wall. Upside pin/resistance.
  3. **ZGL $9.66** — regime floor (not a tradeable level; confirms long-gamma). Near
     max-pain magnet **$14.0** (07-17/07-24) is the mild downside pull.
- **Open questions:** does history (phase-5) show RKT earnings moves typically
  exceed the ~$15/$14 cage (validating the straddle) or stay pinned? Does macro
  (phase-6) put a rate/mortgage catalyst before 07-30 that front-runs the earnings
  break?
