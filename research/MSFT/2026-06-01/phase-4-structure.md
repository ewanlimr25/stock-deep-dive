# Phase 4 — Dealer Structure & Gamma

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:07:07Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is a **pinned, vol-suppressed, *complacent* regime that caps
upside and pulls down into OPEX** — structurally at odds with the bullish call
tape. GEX `regime: POSITIVE` ("dealers net long gamma — expect mean-reversion and
reduced volatility"), with the **gamma pin at 460 (+$57.6M), bracketed 450/470/480**;
dealers only flip short-gamma far below (~400–410). DEX says **public is net
call-long → dealers net short calls → hedge is to BUY underlying** (a mechanical
bid). But three flags lean the structure bearish/fragile: (1) **max pain sits
417.5–430 across *every* near-term expiry, 7–9% BELOW spot** — June-OPEX (06-18)
max pain **417.5 (−9.32%)**; (2) **vanna** is negative/call-heavy → **falling IV
mechanically triggers dealer *selling***; (3) term skew is **COMPLACENT** (25Δ
calls richer than puts, skew_ratio 0.902) — zero downside fear priced. The broad
IV curve is CONTANGO but the actionable front (**6d 39.8% vs 30d 35.1% =
BACKWARDATION, ratio 1.134**) prices near-term event stress (no earnings till
07-29 → likely macro, ~06-05; phase-6 to confirm).

## Key signals

- **POSITIVE GEX / long-gamma**, total +$268.7M; **pin at 460** (+$57.6M),
  walls 450/470/480 → mean-reversion, suppressed vol `[STRUCT:gex]`.
- **Max pain 417.5–430 every near-term expiry, ~7–9% below spot**; 06-18 OPEX
  = **417.5 (−9.32%)** → downward OI gravity `[STRUCT:max_pain]`.
- **DEX bid**: dealers net short calls → **buy underlying to hedge** (supportive
  floor near-term), net_dex +$16.75B `[STRUCT:dex]`.
- **Vanna landmine**: net_vanna −47,250 (call-heavy) → **IV down ⇒ dealer
  selling**; IV up ⇒ buying `[STRUCT:vanna_charm]`.
- **Skew COMPLACENT** (call_25Δ_iv 35.66% > put 32.16%, skew_ratio 0.902) +
  **front-end BACKWARDATION** (6d/30d 1.134) → no downside hedging, near-term
  event vol `[STRUCT:term_skew]` `[STRUCT:front_end_iv_ratio]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- `regime`: **POSITIVE** — `regime_description`: *"Dealers net long gamma — expect
  mean-reversion and reduced volatility."*
- `total_gex`: **+268,654,343**; `underlying_price` (tool): 461.14.
- `zero_gamma_level`: **206.8** — far below spot → firmly long-gamma. (Treat the
  206.8 as a coarse aggregate per the ±2% pitfall; the *practical* downside
  gamma-flip is where `net_gex` turns negative ≈ **400–410**.)
- Per-strike GEX:
  - **Most positive (pins):** 460 +$57.6M · 450 +$30.6M · 480 +$27.6M · 470 +$23.3M
  - Most negative (short-γ): 400 −$1.2M · 410 −$0.73M · 390 −$0.51M · 405 −$0.50M
- Read: price is gamma-pinned in **450–480** (epicentre 460 ≈ spot). Below ~410
  dealers flip short-gamma → a break there *amplifies*. The pin range agrees with
  phase-3's 470/480 call walls.

### DEX `[STRUCT:dex]`

`net_dex` +16,754,172,556. `interpretation`: *"Public is net call-long → dealers
net short calls → dealer hedge is to BUY underlying."* → a **mechanical bid** under
spot near-term (supportive). (Coexists with positive GEX: the long-gamma comes
from the put book / structure; the short-call delta is what dealers buy stock
against.)

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna **−47,250** (call_vanna −50,514, put_vanna +3,264), net_charm +966,609.
`vanna_interpretation`: *"Public net vanna negative (call-heavy book). Falling IV →
call delta drops → dealers (short calls) cut long-underlying hedge → SELLING
pressure. Rising IV reverses."* → **Given elevated IV rank (73) + front-end
backwardation likely to normalize after the early-June event, a vol crush is a
mechanical *selling* trigger** — the key downside catalyst in the structure.

### IV term structure `[STRUCT:iv_term_structure]`

`structure`: **CONTANGO**, `kink_expiry`: null, 25 expiries. Front (06-01 0DTE,
degenerate 4.4%) → back (2028-12-15, 36.8%) slopes up normally. No broad-curve
event stress — but see front-end ratio for the actionable near-term.

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

near_dte 6 (06-05 weekly) IV **39.81%** vs far_dte 30 IV **35.11%**, ratio **1.134**,
`regime`: **BACKWARDATION**. The very front is bid over the 30-day → **near-term
event premium**. No earnings until 07-29, so this is most likely a **macro
catalyst in early June (~06-05)** — phase-6 must identify (jobs/CPI/Fed).

### Term skew `[STRUCT:term_skew]`

`interpretation`: **COMPLACENT**. call_25d_iv **0.3566** > put_25d_iv **0.3216**,
skew **−0.0349**, skew_ratio **0.902**. **Calls are richer than puts** — inverted
from the usual put-skew — reflecting the call-buying demand and **zero downside
fear**. Complacent skew is a contrarian yellow flag: cheap puts, crowded calls.

### Max pain (opex-gravity) `[STRUCT:max_pain]`

`caveat`: static single-day OI, unchanged to expiry. Spot ≈ $459.77:

| Expiry | dte | max_pain | dist to spot | P/C OI |
|--------|-----|----------|--------------|--------|
| 2026-06-01 (0DTE) | 0 | 430 | −6.61% | 0.453 |
| 2026-06-03 | 2 | 425 | −7.69% | 0.442 |
| 2026-06-05 | 4 | 422.5 | −8.24% | 0.354 |
| 2026-06-08 | 7 | 425 | −7.69% | 0.685 |
| 2026-06-10 | 9 | 427.5 | −7.15% | 0.359 |
| 2026-06-12 | 11 | 420 | −8.78% | 0.429 |
| **2026-06-18 (OPEX)** | 17 | **417.5** | **−9.32%** | 0.547 |
| 2026-06-26 | 25 | 420 | −8.78% | 0.137 |

**Every near-term max pain is 7–9% below spot.** Driven by the massive OTM *call*
OI above spot (470/480/500) that the pin wants to expire worthless. The active
positive-gamma pin holds price near 460 *now*; max pain is the downward gravity a
break would chase. The 06-18 OPEX magnet **417.5** roughly aligns with the phase-2
DP shelf at $427 and the phase-3 put-wall at 400 — a coherent **417–430 downside
target band**.

### Today's gamma flip

`today-gamma-flip` is 0DTE/intraday-only and the as-of date is an EOD snapshot
(after-hours) → **not meaningful for a reproduced historical run; skipped** per the
phase guidance.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --symbol MSFT --dte-max 45 --date 2026-06-01 --json` | regime POSITIVE, ZGL 206.8, pin 460 ← `.regime,.zero_gamma_level,.per_strike` | per-strike |
| `uw options-structure dex --symbol MSFT --dte-max 45 --date 2026-06-01 --json` | dealers buy underlying ← `.interpretation,.net_dex` | agg |
| `uw options-structure vanna-charm --symbol MSFT --dte-max 45 --date 2026-06-01 --json` | net_vanna −47,250, IV-down⇒sell ← `.net_vanna,.vanna_interpretation` | agg |
| `uw options-structure iv-term-structure --symbol MSFT --date 2026-06-01 --json` | CONTANGO ← `.structure` | 25 exp |
| `uw options-structure front-end-iv-ratio --symbol MSFT --near-dte 7 --far-dte 30 --date 2026-06-01 --json` | ratio 1.134 BACKWARDATION ← `.ratio,.regime` | 2 |
| `uw options-structure term-skew --symbol MSFT --dte-target 30 --date 2026-06-01 --json` | COMPLACENT, skew_ratio 0.902 ← `.interpretation,.skew_ratio` | 1 |
| `uw options-structure max-pain --symbol MSFT --dte-max 30 --date 2026-06-01 --json` | 06-18 max pain 417.5 (−9.32%) ← `.results[].max_pain_strike,.distance_pct` | 8 exp |

## Tool errors

- First *batched* probe of gex/dex/vanna-charm/term-skew/front-end-iv-ratio/max-pain
  through a shell loop returned `jq: parse error: Invalid numeric literal at line 1,
  column 6` — a **truncated/partial buffer under a degraded harness** (JSON-validity
  gate), NOT a tool failure. Each command **re-run individually returned valid JSON**
  that round-tripped through `jq`; all values above come from those clean single runs.
  No number was transcribed from a truncated buffer.

## DATA NOTE / CORRECTION

- **Field:** vanna-charm scalars. **First read:** queried `.squeeze_signal/.total_vanna`
  → null (wrong keys). **Corrected:** actual keys are `.net_vanna` / `.net_charm` /
  `.vanna_interpretation`; re-read cleanly. No wrong value was used.
- Regime labels (`POSITIVE`, `CONTANGO`, `BACKWARDATION`, `COMPLACENT`) are quoted
  verbatim from the tools, not re-derived from `per_strike`.

## Verdict for downstream phases

- **Dealer regime: LONG GAMMA / pinned & vol-suppressed, with a near-term dealer
  bid (DEX) but downward max-pain gravity and a vanna vol-crush landmine.** Net the
  structure is **range-capped with a bearish lean / downside fragility** — it does
  **not** support a bullish breakout and partially *contradicts* the phase-1 call
  tilt (flag for phase-8b debate & phase-10 audit).
- **Conviction: 4/5** — MSFT has deep OI, so GEX/DEX/max-pain are reliable; the
  regime labels are unambiguous.
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **Gamma pin 460** (≈spot) — the mean-reversion magnet; range **450–480**.
  2. **Upside cap 480 → 500** (GEX/call walls); **practical short-gamma trigger
     ~410** (ZGL 206.8 is coarse — use 410, below it moves amplify).
  3. **June-OPEX max pain 417.5** (−9.3%) — the opex-gravity magnet; downside band
     **417–430** (confluent with phase-2 $427 shelf, phase-3 400 put wall).
- **Open questions:** What is the early-June macro catalyst pricing the front-end
  backwardation (phase-6)? If IV crushes post-event, does the negative-vanna
  dealer-selling overwhelm the DEX bid? Is the complacent call skew a fade signal
  (phase-7c sentiment / contrarian)?
