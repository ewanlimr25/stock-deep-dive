# Phase 4 — Dealer Structure & Gamma

**Ticker:** NOW
**As-of date:** 2026-07-17
**Generated:** 2026-07-19 (run) for as-of 2026-07-17
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

Dealers are **net LONG gamma (POSITIVE regime, ZGL $101.21, spot $103.37 above it)**
— the mechanical read is **range-bound, mean-reverting, vol-suppressed** with the
strongest positive-GEX pins stacked **$100–103** (right at/below spot). A **negative-
gamma pocket at $104–105** sits just above: a push through ~$104 flips dealers short
gamma there and could accelerate toward the phase-3 $110 call wall. **All of this pin
structure is provisional — it evaporates at earnings 7/22.** IV term structure is
**BACKWARDATION** with a steep event ladder (7/24 = 114.2% → 8/21 = 74.0%; front-end
ratio 1.544) pricing a **large earnings move (~±10–12% est.)**, yet 30-day skew is
**COMPLACENT** (put25Δ 71.9% ≈ call25Δ 72.7%) — no downside fear priced into a binary
event (a mild contrarian yellow flag). DEX shows dealers short calls → a small
mechanical hedge-bid now; post-earnings **IV crush turns vanna into selling
pressure**. Conviction **3/5**.

## Key signals

- **POSITIVE gamma, ZGL $101.21 < spot $103.37** → mean-reversion regime, total_gex
  +$17.08M `[STRUCT:gex]`.
- **Positive-GEX pin stack $100–103** (net_gex +$6.10M@102, +$6.08M@100, +$4.10M@103);
  **negative-gamma pocket $104–105** (−$5.11M@105, −$3.66M@104) = breakout accelerant
  `[STRUCT:gex per_strike]`.
- **BACKWARDATION, front IV 114.2% (7/24) vs 74.0% (8/21)**, front-end ratio 1.544 =
  strong earnings-event stress `[STRUCT:iv_term_structure]` `[STRUCT:front_end_iv_ratio]`.
- **Skew COMPLACENT** (skew_ratio 0.989, calls slightly richer than puts) — no
  tail-hedge bid despite the event `[STRUCT:term_skew]`.
- **7/24 (post-earnings) max pain $104, ≈ spot** (dist +0.59%, pc_oi 0.96)
  `[STRUCT:max_pain]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- **Regime: POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced
  volatility." total_gex **+$17,079,210**, **ZGL $101.21**, spot $103.37.
- Top strikes by |net_gex|:

| strike | net_gex | role |
|---|---|---|
| 102 | +$6.10M | positive pin (support magnet) |
| 100 | +$6.08M | positive pin (support magnet) |
| **105** | **−$5.11M** | negative-gamma pocket (accelerant above) |
| 103 | +$4.10M | positive pin (≈ spot) |
| **104** | **−$3.66M** | negative-gamma pocket |
| 120 | +$3.30M | positive (aligns w/ phase-3 $120 call wall) |
| 115 | +$2.12M | positive |
| 85 | −$1.94M | negative (downside accelerant, deep) |

Read: below ~$104 the book is strongly long-gamma → price is magnetized to $100–103
and vol is damped. Cross $104–105 and dealers flip short-gamma → a move can run to
the $110/$120 walls (phase-3). ZGL $101.21 is the regime pivot / mechanical support.

### DEX `[STRUCT:dex]`

net_dex **+$222.5M** (call_dex +$899.1M, put_dex −$676.6M). "Public net call-long →
dealers net short calls → dealer hedge is to BUY underlying." → small **mechanical
bid** at the margin now. (Flips to selling on IV crush — see vanna.)

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna **−232** (call-heavy book), net_charm **+121,401**. Interpretation:
"Falling IV → call delta drops → dealers (short calls) cut long-underlying hedge →
SELLING pressure. Rising IV reverses." **Critical for the event:** pre-earnings IV
rise = supportive; **post-earnings IV crush = mechanical vanna SELLING drag** on top
of whatever the print delivers.

### IV term structure `[STRUCT:iv_term_structure]`

**Structure: BACKWARDATION** (front > back), 16 expiries:

| expiry | dte | avg_iv |
|---|---|---|
| 2026-07-17 | 0 | 155.7% (expiring) |
| **2026-07-24** | 5 | **114.2%** (spans earnings 7/22) |
| 2026-07-31 | 12 | 92.1% |
| 2026-08-07 | 19 | 82.1% |
| 2026-08-14 | 26 | 76.0% |
| 2026-08-21 | 33 | 74.0% |
| 2026-08-28 | 40 | 70.3% |
| 2026-09-18 | 61 | 68.0% |

Steep front-loaded ladder = the market is pricing the earnings event heavily into
7/24. **Rough earnings-implied move ≈ ±10–12%** (7/24 ATM IV 114% × √(5/365); phase-9
to refine off the actual 7/24 ATM straddle mid). IV rank 96.9 (phase-0.5) is this
event premium.

### Term skew (30d) `[STRUCT:term_skew]`

put_25Δ_iv **71.9%**, call_25Δ_iv **72.7%**, skew −0.0079, skew_ratio **0.989** →
**COMPLACENT** (calls marginally richer than puts). No downside tail bid — unusual
into a binary earnings event; reads as upside-speculative/complacent positioning.
Mild contrarian flag for phase-7c/8b.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

near_iv (7d) **114.2%** / far_iv (30d) **73.9%**, ratio **1.544** → **BACKWARDATION /
event stress** — confirms a large catalyst priced into the front.

### Today's gamma flip

Skipped — run is **after-hours / as-of reproduction** (2026-07-17 EOD), not intraday;
`today-gamma-flip` (0DTE intraday) is not meaningful here (rubric: note and skip).

### Max pain (opex gravity) `[STRUCT:max_pain]`

| expiry | max_pain | dist% | put_call_oi_ratio |
|---|---|---|---|
| 2026-07-17 (0DTE) | 100 | −3.28% | 0.427 |
| **2026-07-24 (post-earnings)** | **104** | **+0.59%** | 0.96 |
| 2026-07-31 | 101 | −2.31% | 0.452 |
| 2026-08-07 | 106 | +2.52% | 1.246 |
| 2026-08-14 | 106 | +2.52% | 0.747 |

Near-term magnets cluster **$100–106**, bracketing spot. The immediate post-earnings
7/24 magnet is **$104 ≈ spot** — neutral gravity. Agrees with phase-3's $100/$105
battlegrounds and the positive-GEX pin stack. (Caveat: static-OI estimate; near
expiry only.)

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|---|---|---|
| `uw options-structure gex --symbol NOW --dte-max 45` | regime POSITIVE, ZGL 101.21, total +$17.08M ← `.regime/.zero_gamma_level` | per_strike |
| `uw options-structure dex --symbol NOW --dte-max 45` | net_dex +$222.5M, dealers buy hedge ← `.net_dex/.interpretation` | 1 |
| `uw options-structure vanna-charm --symbol NOW --dte-max 45` | net_vanna −232; IV-crush = selling ← `.vanna_interpretation` | 1 |
| `uw options-structure iv-term-structure --symbol NOW` | BACKWARDATION; 7/24 114.2% ← `.structure/.term_structure[].avg_iv` | 16 |
| `uw options-structure term-skew --symbol NOW --dte-target 30` | COMPLACENT, ratio 0.989 ← `.interpretation/.skew_ratio` | 1 |
| `uw options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | ratio 1.544 BACKWARDATION ← `.ratio/.regime` | 1 |
| `uw options-structure max-pain --symbol NOW --dte-max 30` | 7/24 max pain 104 (+0.59%) ← `.results[].max_pain` | 5 exp |

## Tool errors

None fatal. Two jq field-name corrections (below) — re-read cleanly before any
transcription.

## DATA NOTE / CORRECTION

- GEX per-strike field is **`net_gex`**, not `gex`; first jq (`.gex`) hit a null.
  Corrected → $102 +$6.10M etc. No wrong value written.
- iv-term-structure per-expiry field is **`avg_iv`/`avg_iv_pct`** with **`dte_approx`**
  (not `iv`/`dte`); first jq returned nulls. Corrected → 7/24 114.2%. No wrong value
  written.

## Verdict for downstream

- **Dealer regime:** **POSITIVE / long-gamma** (mean-reversion, vol-suppressed)
  **below ~$104**; **transitional/short-gamma pocket $104–105**. This holds ONLY into
  the 7/22 earnings — the event overrides the pin.
- **Conviction:** **3 / 5** (clean, internally coherent structure; the caveat is the
  binary event).
- **Structural levels for phase-9:**
  - **ZGL $101.21** — regime pivot / mechanical support (below it → short-gamma,
    trend-amplifying down).
  - **Positive-GEX pins $100 / $102** — downside magnets; **negative-gamma trigger
    $104–105** — break above accelerates toward **$110 → $120** call walls (phase-3).
  - **Near-expiry max pain $104 (7/24)** — the post-earnings opex pin ≈ spot.
- **Open questions:** What's the exact 7/24 ATM straddle-implied earnings move
  (phase-9 to price)? Does the COMPLACENT skew + call-heavy book mean the market is
  under-hedged for a downside miss (phase-7c/8b)? Post-event, how much does the vanna
  IV-crush drag matter for a directional hold?
