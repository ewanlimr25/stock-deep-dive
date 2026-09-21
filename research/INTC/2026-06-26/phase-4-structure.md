# Phase 4 — Dealer Structure & Gamma

**Ticker:** INTC
**As-of date:** 2026-06-26
**Generated:** 2026-06-27T10:05:50-0400
**Upstream phases cited:** phase-0.5-context.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

The dealer book is **net LONG GAMMA (regime POSITIVE, total_gex +30.4M, ZGL $27.26 —
spot $128.35 is far above it)**, so the regime-level expectation is **mean-reversion and
suppressed realized vol — dealers sell rallies, buy dips.** That is a structural
*headwind to any fast directional move*, including the bearish thesis from phases 1/3.
But three things tilt the structure *mildly bearish within the range*: (1) **max-pain
sits BELOW spot at every expiry** (0DTE $125, Jul-02 $120, Jul-17 a soft $100) — a
downward OI gravity; (2) a **local negative-gamma notch at $127–129 (exactly at spot)**
sits between strong positive-gamma pins at **$130 (lid)** and **$125/$120 (downside
magnets)**; (3) **vanna is negative on a call-heavy book** — if the elevated IV
compresses, dealers cut their long hedge and **sell**. IV is genuinely high (ATM ~94%,
iv_rank 94, term **BACKWARDATION**) but **skew is COMPLACENT** (25Δ put ≈ call, no
downside fear premium) — which both flags that the bearish positioning is *measured, not
panic*, and means outright puts are absolutely expensive (high IV) though not richly
skewed. Net structural read: **a vol-suppressed $120–130 range biased toward the $120–125
pins**, not a crash — unless $120 fails.

## Key signals

- **Long-gamma regime**: GEX POSITIVE, ZGL **$27.26** ≪ spot $128.35 — "dealers net long
  gamma, expect mean-reversion and reduced volatility" [STRUCT:gex].
- **Max-pain pulls DOWN every expiry**: $125 / $120 / $100 (0DTE / Jul-02 / Jul-17), all
  below spot — downward opex gravity [STRUCT:max_pain].
- **Pin map near spot**: $130 (+4.16M GEX, lid) · $127–129 (negative-gamma notch) · $125
  (+2.91M) · $120 (+5.34M, major magnet) · $150 (+9.65M, hard cap) [STRUCT:gex].
- **Negative vanna on a call-heavy book**: falling IV → dealers SELL underlying — a
  bearish channel given IV is at iv_rank 94 (more room to fall) [STRUCT:vanna_charm].
- **Skew COMPLACENT** (skew_ratio 1.002, put_25d 0.9423 ≈ call_25d 0.9406) — no crash
  premium priced despite bearish flow; absolute IV high (~94%) [STRUCT:term_skew].

## Detailed findings

### GEX (gamma exposure)

`regime = POSITIVE`, `regime_description = "Dealers net long gamma — expect mean-reversion
and reduced volatility"`, `total_gex = +30,449,365`, `zero_gamma_level = $27.26`,
`underlying_price = $128.35`. Spot is **~$101 above the ZGL** — deeply long-gamma; no
near-term flip risk. Per-strike (top |net_gex|):

| Strike | net_gex | Role |
|---|---|---|
| 150 | +9,653,436 | Largest positive — **hard overhead cap** (= phase-3 call wall, phase-2 $140.94 supply) |
| 140 | +5,513,199 | Positive pin (resistance) |
| 120 | +5,339,219 | Positive pin — **major downside magnet/support** |
| 130 | +4,163,587 | Positive pin — **immediate lid** (= phase-3 $130 call wall) |
| 145 | +3,551,742 | Positive pin |
| 125 | +2,908,344 | Positive pin — **first downside magnet** (= 0DTE max-pain) |
| **129** | **−2,163,556** | Most negative — local accel notch **at spot** |
| 128 | −921,593 | Negative (spot notch) |
| 110 | −917,686 | Negative (toward put wall) |

**Spot sits in a shallow negative-gamma notch ($127–129)** between sticky positive pins
above ($130) and below ($125/$120). Small moves at spot can wobble, but get caught by
the pins → price gravitates to $130, $125, or $120. With max-pain + flow/OI bearish, the
path of least resistance is **down toward $125 → $120**.

### DEX (dealer delta)

`net_dex = +2,185,087,874`, `call_dex = +3.17B`, `put_dex = −0.99B`. Interpretation
(verbatim): *"Public is net call-long → dealers net short calls → dealer hedge is to BUY
underlying."* A mechanical bid — **but it is inflated by the deep-ITM financing calls**
(phase-1: delta ≈0.99), so it overstates genuine bullish demand. Supportive at the
margin, not a directional signal.

### Vanna + charm

`net_vanna = −7,007` (call_vanna −11,213, put_vanna +4,206), `net_charm = +272,842`.
Interpretation (verbatim): *"Public net vanna negative (call-heavy book). Falling IV →
call delta drops → dealers (short calls) cut long-underlying hedge → SELLING pressure.
Rising IV reverses."* With IV at **iv_rank 94** (asymmetric room to fall), the vanna
channel is a **mild bearish tailwind on any IV compression** (e.g. post-rebalance calm).

### IV term structure + skew + front-end (the phase-0.5 tension, resolved)

- `iv-term-structure.structure = BACKWARDATION` (front IV > back across 18 expiries) —
  consistent with event/vol stress and high absolute IV.
- `term-skew.interpretation = COMPLACENT`, skew_ratio **1.002**, put_25d_iv 0.9423 vs
  call_25d_iv 0.9406 (27d) — **flat skew, no downside fear premium**.
- `front-end-iv-ratio.regime = FLAT` (0.964; near_iv 0.9484 @5d, far_iv 0.9843 @27d) — no
  acute front-end event stress; earnings (Jul-23, 28d) sits just past the 27d leg.
- **Resolution of phase-0.5 flag:** INTC ATM IV is genuinely **~92–98%** (iv_rank 94) —
  a high-vol regime. The phase-0.5 `implied_move_perc = 0.65%` was the **0DTE EOD
  residual** (today's expiry, ~no time left), **not** a multi-day move. The real 21-day
  (Jul-17) 1σ expected move at ~94% IV is **≈ ±22% (≈ ±$29 → ~$99–$157)**. Phase-9 must
  use the IV-derived move, NOT 0.65%, and note outright puts are **absolutely expensive**
  (though not richly skewed).

### Today's gamma flip (0DTE 2026-06-26)

`regime = POSITIVE`, `today_zero_gamma = 55.06`, `atm_flip_strike = 60`, spot $128.52 —
the 0DTE book was also positive-gamma with the flip far below. (As-of-day snapshot; the
intraday read is historical now but valid for 2026-06-26.)

### Max pain (opex gravity)

| Expiry | DTE | max_pain | dist | P/C OI |
|---|---|---|---|---|
| 2026-06-26 | 0 | **$125** | −2.09% | 0.84 |
| 2026-07-02 | 6 | **$120** | −6.01% | 0.71 |
| 2026-07-10 | 14 | $124 | −2.87% | 1.05 |
| 2026-07-17 | 21 | **$100** | −21.67% | 0.90 |
| 2026-07-24 | 28 | $118 | −7.57% | 0.77 |

Every near-term magnet is **below spot**. The tradeable gravity is **$120–125** (Jul-02
$120 aligns with the $120 positive-gamma pin and the phase-3 $120 call_heavy floor). The
Jul-17 $100 is a *soft, static-OI* figure (21.7% away; tool caveat: far max-pain
migrates) — directionally-down but not a literal target. **Max-pain agrees with phase-3
(walls/cliff) and phase-2 ($128.32 magnet, overhead supply): the chain leans down.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `options-structure gex --symbol INTC --dte-max 45` | regime POSITIVE, ZGL 27.26, total +30.4M; $150 +9.65M, $129 −2.16M ← `.regime,.zero_gamma_level,.per_strike[].net_gex` | full surface |
| `options-structure dex --symbol INTC --dte-max 45` | net_dex +2.19B, dealers buy hedge ← `.net_dex,.interpretation` | aggregate |
| `options-structure vanna-charm --symbol INTC --dte-max 45` | net_vanna −7,007; IV-down→sell ← `.net_vanna,.vanna_interpretation` | aggregate |
| `options-structure iv-term-structure --symbol INTC` | BACKWARDATION ← `.structure` | 18 expiries |
| `options-structure term-skew --symbol INTC --dte-target 30` | COMPLACENT, skew_ratio 1.002 ← `.interpretation,.skew_ratio` | 27d |
| `options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | FLAT 0.964 ← `.regime,.ratio` | 5d/27d |
| `options-structure today-gamma-flip --symbol INTC` | POSITIVE, ZGL 55.06 ← `.regime,.today_zero_gamma` | 0DTE |
| `options-structure max-pain --symbol INTC --dte-max 30` | 0DTE $125 / Jul-02 $120 / Jul-17 $100 ← `.results[].max_pain_strike` | 5 expiries |

## Tool errors

None — all eight reads returned valid JSON on first call.

## DATA NOTE / CORRECTION

Phase-0.5 carried `implied_move_pct = 0.65%` with a flag. **Corrected here:** that field
is the 0DTE end-of-day residual implied move, not a multi-day figure. INTC's real ATM IV
is ~92–98% (iv_rank 94), implying a ±~22% 21-day move. Downstream phases should use the
IV-derived expected move. Spot references across tools: GEX/DEX $128.35, vanna $128.33,
max-pain/OI $127.67 — all ≈ $128.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA / POSITIVE** (mean-reverting, vol-suppressing) at the
  aggregate, with a **local negative-gamma notch at spot ($127–129)** and a **downward
  max-pain gravity ($120–125 near-term)**. Net structural bias: **mildly bearish but
  range-suppressed** — drift toward the $120–125 pins, NOT a violent break, unless $120
  gives way (then air to the $110 put wall).
- **Conviction:** **3 / 5** — regime is unambiguous (long gamma) but the directional
  edge is nuanced (supportive dealer hedging vs downward max-pain/vanna).
- **Three structural levels for phase-9** (+ max-pain magnet):
  1. **$130** — positive-gamma pin + call wall = immediate lid/resistance.
  2. **$120** — major positive-gamma pin (+5.34M) + Jul-02 max-pain + call_heavy floor =
     primary downside magnet/support; the line that defines the range.
  3. **$150** — largest positive GEX (+9.65M) = hard overhead cap (far).
  - **Near-expiry max-pain magnet: $125 → $120** (the opex pull for the next 1–3 weeks).
- **Open questions:**
  - Does the bearish flow/OI have enough force to drag price through the $125/$120
    positive-gamma pins, given dealers buy dips there? (i.e. is this a grind-to-$120 or a
    failed-breakdown range?)
  - Will IV compress post-rebalance and trigger the negative-vanna dealer selling? Macro
    (phase-6) and the Jul-23 earnings vol path matter here.
  - Skew is complacent — is the bearish positioning a hedge (no fear) rather than a
    conviction short? Phase-7c short-interest/sentiment should help adjudicate.
