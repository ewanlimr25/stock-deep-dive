# Phase 4 — Dealer Structure & Gamma

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-06-18
**Generated:** 2026-06-20T13:08:01Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealer structure is **transitional / near-spot short gamma**, with a mild **upward pin to
$11** and a downside-acceleration risk through $10. The `gex` tool's aggregate `regime`
label reads **POSITIVE** (ZGL 2.34), but that label is unreliable here: `total_gex` is
**negative (−7.31M)**, `today-gamma-flip` returns **NEGATIVE**, and the largest gamma
concentration is a **−8.69M "resistance_wall" at $10** (the put wall). For a $10 stock a
ZGL of **2.34** is a coarse artifact (below any realistic price), so the *tradeable*
gamma is **short around spot**: a break of $10 can accelerate; $12–$13 are positive-gamma
support walls that would dampen. DEX shows dealers net short puts → hedge = **SELL
underlying** (mild overhang). Vanna is positive → a **vanna-squeeze bid if IV collapses**.
IV term is **CONTANGO / front-end FLAT** (no event stress; earnings far out). Skew is
**COMPLACENT** — calls richer than puts (skew_ratio 0.886), i.e. crowd paying up for
upside against the 31.78% short float.

## Key signals

- **Near-spot short gamma:** total_gex −7.31M; today-gamma-flip **NEGATIVE**; $10 strike
  gex **−8,691,218** ("resistance_wall") [STRUCT:gex][STRUCT:today_gamma_flip].
- **Gamma support walls above:** $12 gex +2,412,463 ("support_wall"), $13 +567,939 [STRUCT:today_gamma_flip].
- **Max pain $11 across every expiry** (+7% above spot $10.27); 0DTE holder_value $1.15M —
  mild upward pin magnet [STRUCT:max_pain].
- **DEX overhang:** net_dex −4,908,533 → "dealers net short puts → hedge is to SELL underlying" [STRUCT:dex].
- **Vanna-squeeze setup + complacent skew:** net_vanna +280 (bid if IV falls); term-skew
  **COMPLACENT**, call_25Δ IV 0.658 > put_25Δ IV 0.583 [STRUCT:vanna_charm][STRUCT:term_skew].

## Detailed findings

### GEX — `[STRUCT:gex]`

- `regime`: **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced
  volatility" (**tool's label; see contradiction below**)
- `zero_gamma_level`: **2.34** (coarse/meaningless for a $10 name — treat as N/A)
- `total_gex`: **−7,308,680** (negative — contradicts the POSITIVE label)
- spot: $10.27
- Per-strike: positive gex builds at $5–$7 (low-strike call OI, e.g. $7 = +21,331), but the
  dominant near-spot concentration is the **negative $10 put wall**.

**Contradiction flagged for phase-10:** `regime=POSITIVE` vs `total_gex<0` vs
`today-gamma-flip=NEGATIVE`. Resolution: the ZGL-based label is a low-price artifact; the
tradeable near-spot gamma is **short** (negative), confirmed by today-gamma-flip and the
−8.69M $10 wall.

### DEX — `[STRUCT:dex]`

net_dex **−4,908,533** (call_dex +16.30M, put_dex −21.21M). Interpretation: "Public is net
put-long → dealers net short puts → dealer hedge is to **SELL underlying**." Mild downward
hedging overhang.

### Vanna + charm — `[STRUCT:vanna_charm]`

net_vanna **+280**, net_charm +14,630. Interpretation: "Public net vanna positive
(put-heavy book). Falling IV → |put delta| drops → dealers (short puts) cover by **BUYING
underlying**. Classic vanna-squeeze setup if VIX collapses." → conditionally bullish bid on
IV compression.

### IV term structure — `[STRUCT:iv_term_structure]`

`structure`: **CONTANGO** (normal upward IV slope; front < back). No event-stress
backwardation — consistent with earnings far out (Sep 3, phase-0.5). (Per-row dte/iv fields
returned null — only the headline regime label is reliable.)

### Term skew — `[STRUCT:term_skew]`

`interpretation`: **COMPLACENT**. call_25Δ_iv 0.6576 **>** put_25Δ_iv 0.5827; skew −0.0749,
skew_ratio 0.886 (dte_actual 27). **Negative/call skew** — calls richer than puts: demand is
on the upside (squeeze-positioning vs 31.78% SI), downside hedges are cheap → complacency is
itself a contrarian yellow flag.

### Front-end IV ratio — `[STRUCT:front_end_iv_ratio]`

ratio **1.026**, regime **FLAT** (near_iv 0.7255 @ 6 DTE vs far_iv 0.7071 @ 27 DTE). No
front-end event stress.

### Today's gamma flip (0DTE; informational — run after-hours) — `[STRUCT:today_gamma_flip]`

regime **NEGATIVE**; today_total_gex −7,327,807; today_zero_gamma 2.34; atm_flip_strike 3.
key_walls: **$10 resistance_wall (gex −8,691,218)**, **$12 support_wall (+2,412,463)**, $9.5
& $9 resistance_walls (negative), $13 support_wall (+567,939). Confirms short-gamma near spot.

### Max pain (opex gravity) — `[STRUCT:max_pain]`

| expiry | DTE | max_pain | dist% | P/C OI | holder_value |
|--------|-----|----------|-------|--------|--------------|
| 2026-06-18 | 0 | **$11** | +7% | 0.378 | $1,150,950 |
| 2026-06-26 | 8 | $11 | +7% | 0.911 | $94,400 |
| 2026-07-02 | 14 | $11 | +7% | 0.356 | $50,050 |
| 2026-07-10 | 22 | $11 | +7% | 0.316 | $26,700 |
| 2026-07-17 | 29 | $11 | +7% | 0.272 | $246,600 |

**Max pain is $11 across every expiry** (+7% above spot) → static-OI magnet pulls **up**
toward $11. Agrees with phase-3's $11 call wall and today-gamma-flip's $10→$12 wall band.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← path | Rows |
|------------------|---------------------|------|
| `options-structure gex --symbol PATH --dte-max 45 --date 2026-06-18` | regime POSITIVE; total_gex −7.31M; ZGL 2.34 ← `.regime/.total_gex/.zero_gamma_level` | surface |
| `options-structure dex --dte-max 45` | net_dex −4.91M; hedge=SELL ← `.net_dex/.interpretation` | 1 |
| `options-structure vanna-charm --dte-max 45` | net_vanna +280; squeeze-if-IV-falls ← `.net_vanna/.vanna_interpretation` | 1 |
| `options-structure iv-term-structure` | CONTANGO ← `.structure` | — |
| `options-structure term-skew --dte-target 30` | COMPLACENT; ratio 0.886 ← `.interpretation/.skew_ratio` | 1 |
| `options-structure front-end-iv-ratio --near-dte 7 --far-dte 30` | FLAT; ratio 1.026 ← `.regime/.ratio` | 1 |
| `options-structure today-gamma-flip` | NEGATIVE; $10 wall −8.69M ← `.regime/.key_walls[]` | 5 walls |
| `options-structure max-pain --dte-max 30` | $11 all expiries, +7% ← `.results[].max_pain_strike` | 5 exp |

## Tool errors

_none_ (all commands accepted `--date 2026-06-18`).

## DATA NOTE / CORRECTION

No value corrected. The `gex` `regime` label (POSITIVE) **conflicts** with its own
`total_gex` (−7.31M) and with `today-gamma-flip` (NEGATIVE); resolved in favor of the
tradeable near-spot short-gamma read and flagged for phase-10. `iv-term-structure`
per-row fields were null — only `.structure` (CONTANGO) used. All scalars via `jq`.

## Verdict for downstream

- **Dealer regime:** **Transitional → short gamma near spot** ($10 negative wall;
  today-gamma-flip NEGATIVE). Positive-gamma damping only above at $12–$13. (Aggregate
  ZGL-based POSITIVE label discounted as a low-price artifact.)
- **Conviction:** **2/5** (mixed signals; conflicting GEX labels; magnitudes small).
- **Three structural levels for phase-9 (+ max-pain magnet):**
  1. **$10 — short-gamma battle line / resistance_wall** (gex −8.69M; also phase-3 put-wall,
     phase-2 $10.23 DP support). Break below can accelerate (short gamma).
  2. **$12 — positive-gamma support_wall** (+2.41M; also phase-3 heavy call wall) — upside
     damper/magnet cap.
  3. **Max-pain $11 (+7%)** — opex pin magnet (mild upward pull); $13 secondary support_wall.
- **Open questions:** Does the DEX sell-overhang (dealers selling) win over the max-pain $11
  upward pull and the vanna-squeeze-if-IV-falls bid? With complacent call skew on a 31.78%
  short-float name, is the upside already crowded (contrarian risk — phase 7c/8b)? A break of
  $10 (short gamma) is the asymmetric downside risk the trade plan must respect.
