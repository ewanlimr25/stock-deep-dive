# Phase 4 — Dealer Structure & Gamma

**Ticker:** ENPH
**As-of date:** 2026-05-22
**Generated:** 2026-05-25T22:43:20Z
**Upstream phases cited:** phase-0.5-context.md, phase-1-flow.md, phase-3-positioning.md

## Summary

The structure is **asymmetric and coiled**: dealers are **net long gamma (GEX
POSITIVE, total +11.5M)** with the heaviest gamma walls at **$65 (3.5M, just above
spot $63.93) and $60 (2.5M)** → near-term ENPH is **pinned / mean-reverting in a
~$60–65 band**, with $65 the ceiling. But **DEX is strongly positive (+$508M) —
public is net call-long, dealers are short calls and must BUY underlying to hedge** —
and phase-3's freshly-bought 70/85/95C sit just above the $65 wall. So a decisive break
of $65 flips local gamma and turns dealer hedging into a **chase higher (squeeze fuel
toward $70+).** The catch: **net vanna is negative with IV-rank at 92** → if IV mean-reverts
DOWN (its likely path), dealer hedging mechanically **SELLS underlying** — a real headwind
that punishes naked long premium. Term structure is **contango overall but front-end
backwardated (near-week IV 118.9% vs 30D 102.7%, ratio 1.157)** with **no earnings until
7/28** → near-term vol is flow/rumor-driven. **30D skew is COMPLACENT (25Δ calls 108% >
puts 95%)** — the crowd is reaching for upside. Net structural read: favors a
**defined-risk / vol-selling bullish expression (call spread or put-financed), NOT naked
long calls.** Conviction 4/5.

## Key signals

- **GEX POSITIVE, ZGL $17.59 (far below spot) → long-gamma, pin 60–65** [STRUCT:gex]
- Gamma walls: **$65 = 3.50M (ceiling), $60 = 2.51M (floor), $70 = 1.32M (magnet)** [STRUCT:gex]
- **DEX +$508M — dealers short calls, hedge = BUY underlying → upside-squeeze fuel above $65** [STRUCT:dex]
- **Net vanna −3,504 + IV-rank 92 → falling-IV = dealer SELLING pressure** (long-premium headwind) [STRUCT:vanna_charm]
- **Front-end backwardation (near IV 119% vs far 103%) with NO earnings till 7/28 → flow-driven near-term vol** [STRUCT:front_end_iv_ratio]
- **30D skew COMPLACENT — calls (108%) richer than puts (95%)** → bullish crowd, thin downside cushion [STRUCT:term_skew]

## Detailed findings

### GEX — dealers net long gamma, walls bracket spot

`regime: POSITIVE`, `total_gex 11,505,725`, `zero_gamma_level 17.59`, spot $63.93.
Top per-strike net GEX:

| Strike | Net GEX | Role |
|--------|---------|------|
| **65** | **3,499,123** | **upper gamma wall / immediate resistance** (just above spot) |
| **60** | **2,505,885** | **gamma floor / support** |
| 50 | 1,883,810 | deep-ITM OI block (phase-3's 25,713-OI strike) |
| **70** | **1,323,534** | the freshly-bought bull-magnet strike (phase-3) |
| 80 | 525,606 | OTM call OI |
| 55 | 366,942 | support |
| 85 | 312,244 | OTM lottery |

ZGL $17.59 is **far below spot and not a usable flip level** — it's dragged down by the
massive deep-ITM 50/60 OI; treat it as "spot is deeply in long-gamma territory," nothing
more (the note warns GEX is coarse outside indices/large-caps). Practically: **dealers
dampen moves inside $60–65**, selling toward the $65 wall and supporting toward $60.

### DEX — the coiled upside accelerant

`net_dex +508,403,529` (call_dex +532.5M, put_dex −24.1M). **Public net call-long →
dealers net short calls → dealer hedge is to BUY underlying.** Inside the long-gamma
band this is contained, but it means the **fresh OTM call wall at 70/85/95 is dealer-short**:
if spot clears the $65 gamma wall toward $70, those calls gain delta fast, dealers must
buy underlying to stay hedged → **mechanical chase higher.** Structure is *pinned now,
explosive if $65 breaks.*

### Vanna / charm — the IV-direction risk (key caution)

`net_vanna −3,504` (call-heavy book), `net_charm +49,519`. Interpretation: **falling IV →
call delta drops → dealers (short calls) cut their long-underlying hedge → SELLING
pressure.** With **IV-rank 92** the path of least resistance for IV is *down*, so vanna is
a **structural headwind to spot and a double-killer for naked long calls** (lose on vega
*and* on vanna-driven spot drift). Rising IV reverses it into a tailwind — but betting on
IV rising from the 92nd percentile is poor odds. **→ This is the single strongest argument
for selling vol (spreads) rather than buying it outright.**

### IV term structure — contango with a front-end event bump

`structure: CONTANGO`, `kink_expiry: null`, 16 expiries. Avg IV by expiry:
5/29 **118.9%** → 6/05 115.4% → 6/12 105.5% → **6/18 103.6%** → 7/17 97.5% → 2027-01 91.4%
→ 2028 83.1%. The curve declines with tenor (contango), **but the near weeks (5/29, 6/05)
are bumped up** — confirmed by the front-end ratio below. **No earnings until 2026-07-28**,
so the near-term bid is **flow / rumor / policy-headline driven**, not a scheduled event
(→ phase 6/7c hunt the catalyst).

**Corrected expected move** (phase-0.5's screener 0.46% was garbage):
- 1 week (→5/29): 1.189 × √(7/365) × $63.93 ≈ **±$10.5 (±16.5%)**
- to 6/18 (27D): 1.036 × √(27/365) × $63.93 ≈ **±$18 (±28%)**

ENPH is priced for very large swings. Phase-9 targets/stops must use these, not 0.46%.

### Term skew (30D, dte_actual 32) — COMPLACENT

`call_25d_iv 1.0825`, `put_25d_iv 0.9484`, `skew −0.1341`, `skew_ratio 0.876`,
`interpretation COMPLACENT`. **25Δ calls are richer than 25Δ puts** (reverse skew) — the
options market is bidding *upside* over downside. Read two ways: (1) confirms a bullish
positioning crowd (everyone reaching for calls), (2) **complacency / crowding flag** —
little downside protection is bid, so a reversal has no put cushion and unwinds fast.
Silver lining for structuring: **puts are relatively cheap → defining downside risk with
a long put is inexpensive.**

### Front-end IV ratio — BACKWARDATION

`near_iv 118.9% (4D)` / `far_iv 102.7% (32D)` = **ratio 1.157 → BACKWARDATION**. Near-term
event stress with no scheduled earnings → flow/rumor. Don't fade it as pure earnings
backwardation (none within 24h); it's live.

### Today's gamma flip (0DTE)

**Skipped intentionally** — `today_gamma_flip` is 0DTE-only and intraday; this is an
after-hours EOD snapshot on a historical as-of date and the 5/22 0DTE strikes expired
today. Not meaningful for this run (per phase guidance).

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__options_structure_gex` | `{symbol: ENPH, dte_max: 45, date: 2026-05-22}` | POSITIVE, total +11.5M, ZGL 17.59; walls 65/60/50/70 |
| `mcp__uw-pp__options_structure_dex` | `{symbol: ENPH, dte_max: 45, date: 2026-05-22}` | net_dex +508M; dealers short calls → buy underlying |
| `mcp__uw-pp__options_structure_vanna_charm` | `{symbol: ENPH, dte_max: 45, date: 2026-05-22}` | net_vanna −3,504; falling IV → dealer selling |
| `mcp__uw-pp__options_structure_iv_term_structure` | `{symbol: ENPH, date: 2026-05-22}` | CONTANGO; near weeks 119%/115% bumped |
| `mcp__uw-pp__options_structure_term_skew` | `{symbol: ENPH, dte_target: 30, date: 2026-05-22}` | COMPLACENT, calls 108% > puts 95% |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | `{symbol: ENPH, near_dte: 7, far_dte: 30, date: 2026-05-22}` | ratio 1.157 → BACKWARDATION |
| `mcp__uw-pp__options_structure_today_gamma_flip` | — | skipped (0DTE intraday; historical EOD snapshot) |

## Tool errors

None.

## Verdict for downstream phases

- **Dealer regime:** **Long-gamma near-term (pin $60–65), with a coiled upside-squeeze
  setup above $65** (positive DEX, dealers short the fresh 70/85/95C). Transitional, not
  one-directional.
- **Conviction:** **4/5** on the structural map.
- **Three structural levels for phase-9:**
  1. **$65 — upper gamma wall / immediate resistance** (3.5M GEX). Break = squeeze trigger.
  2. **$60 — gamma floor / support** (2.5M GEX; aligns with phase-2 $61–62 & phase-3 $60 floor).
  3. **ZGL $17.59 — not usable** (deep-ITM artifact); the real "pivot" is the **IV direction**
     (vanna): falling IV from rank 92 = downside drift.
- **Open questions:**
  - What's bidding near-week IV to 119% with no earnings? Solar-policy headline risk? (→ phase 6/7c)
  - Given long-gamma pin + negative vanna + IV-rank 92, is the right expression a
    **call spread / put-financed structure** (sell the rich vol) rather than long calls?
    (→ phase 9 structuring — strong prior: YES.)
