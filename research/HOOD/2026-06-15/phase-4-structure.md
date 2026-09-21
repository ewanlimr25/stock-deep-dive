# Phase 4 — Dealer Structure & Gamma

**Ticker:** HOOD
**As-of date:** 2026-06-15
**Generated:** 2026-06-16T12:12:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md

## Summary

Dealers are **solidly long gamma** — GEX regime **POSITIVE**, zero-gamma level
**~$23–26** (far below the $98.1 spot), total GEX **+$77.6M** — so the structural
default is mean-reversion / suppressed realized vol, with the dominant gamma wall at
**$100 (net_gex +$18.17M)**, reinforced by $95 (+$9.73M) and $105 (+$9.11M). Net
dealer delta (DEX +$2.10B, "public net call-long → dealers short calls → hedge is to
**BUY underlying**") supplies a mechanical bid/floor. Two caveats temper the upside:
net **vanna is negative** (falling IV → dealers cut hedges → selling pressure) and
**skew is COMPLACENT** (25Δ put IV ≈ call IV, ratio 1.001 — no downside fear priced).
Max-pain for the 6/18 OPEX is **$85 (−13.4%)**, a theoretical downward magnet that the
positive-gamma + buy-underlying mechanics actively resist; it would only bite on a
vol-expansion break far below the gamma floor. Net: range-bound, dealer-supported,
**$100 ceiling/pin**, explosive upside capped.

## Key signals

- **POSITIVE GEX** regime ("net long gamma — expect mean-reversion, reduced vol"),
  ZGL $25.91 ≪ spot $98.59, total GEX +$77.6M `[STRUCT:gex]`.
- **$100 = dominant gamma wall** (net_gex +$18.17M), then $95 (+$9.73M), $105
  (+$9.11M); 6/18 today-gamma tags $100/$95/$97/$90/$105 as **support walls**
  `[STRUCT:gex][STRUCT:today_gamma_flip]`.
- **DEX +$2.10B**, dealer hedge = **BUY underlying** (public call-long) → mechanical
  floor `[STRUCT:dex]`.
- **Negative net vanna (−14,004)** → falling IV creates dealer **selling** pressure
  (upside headwind in a low/declining-IV tape) `[STRUCT:vanna_charm]`.
- **Max-pain 6/18 = $85** (−13.4%, pc_oi 0.631) — downward OPEX magnet, offset by
  positive gamma; static-OI caveat `[STRUCT:max_pain]`.

## Detailed findings

### GEX `[STRUCT:gex]`

- regime **POSITIVE** — "Dealers net long gamma — expect mean-reversion and reduced
  volatility." zero_gamma_level **$25.91**, total_gex **+$77,633,690**,
  underlying_price $98.59 (structure tool's reference; close was $98.12 — immaterial
  to regime).
- Largest positive net_gex strikes (gamma walls): **$100 +$18.17M**, $95 +$9.73M,
  $105 +$9.11M, $90 +$6.87M, $110 +$4.89M, $97 +$4.42M. Near-spot map:
  $99 +$2.80M, $98 +$2.34M, $97 +$4.42M, $95 +$9.73M, $100 +$18.17M.
- Small negatives only far below ($75 −$0.55M, $84 −$0.40M). Spot sits well inside
  positive-gamma territory → dealers buy dips / sell rallies around the walls.

### DEX `[STRUCT:dex]`

net_dex **+$2,099,831,725** (call_dex +$2.35B, put_dex −$248M). Interpretation:
*"Public is net call-long → dealers net short calls → dealer hedge is to BUY
underlying."* Mechanical demand for stock = supportive floor, consistent with phase-2
dark-pool accumulation.

### Vanna + charm `[STRUCT:vanna_charm]`

net_vanna **−14,004**, net_charm **+830,665**. Interpretation: *"Public net vanna
negative (call-heavy book). Falling IV → call delta drops → dealers (short calls) cut
long-underlying hedge → SELLING pressure. Rising IV reverses."* With IV mid/low (rank
32.4) and complacent skew, base case is flat/declining IV → mild **upside headwind**.
Positive charm pins hedging toward 6/18 OPEX.

### IV term structure `[STRUCT:iv_term_structure]`

structure **BACKWARDATION**, kink_expiry null. But the slope is driven by the 6/18
OPEX expiry: avg_iv **91.7%** at 2 DTE vs **73.1%** (6/26, 10 DTE), **75.5%** (7/02),
**70.9%** (7/17). The front spike is **OPEX-week pin mechanics**, not an obvious
discrete catalyst — **phase-6 must confirm no HOOD-specific event** before reading it
as event stress.

### Term skew `[STRUCT:term_skew]`

interpretation **COMPLACENT**, skew 0.0005, skew_ratio **1.001** (put_25d_iv 67.09% ≈
call_25d_iv 67.03%, dte_actual 31). Essentially **no put skew** — the market prices
minimal downside tail risk. Contrarian yellow flag (complacency near highs); also
means downside protection is cheap (validates phase-1's $5.54M LEAP-put buyer getting
inexpensive insurance).

### Front-end IV ratio `[STRUCT:front_end_iv_ratio]`

regime **FLAT**, ratio 1.031 (near_iv 73.11% @10d vs far_iv 70.9% @31d). No
event-stress signal — corroborates that the backwardation is OPEX mechanics, not a
catalyst.

### Today's gamma flip (6/18) `[STRUCT:today_gamma_flip]`

regime POSITIVE, atm_flip_strike 23, today_zero_gamma 23.31, today_total_gex +$46.05M,
spot 98.14. key_walls (all **support_wall**): $100 ($10.4M), $95 ($7.27M), $97
($4.22M), $90 ($3.21M), $105 ($2.42M). (EOD as-of run — this is the 6/18 nearest-expiry
gamma map, not a live-intraday 0DTE read; treated as structural, not tradeable-timing.)

### Max pain `[STRUCT:max_pain]` (spot $98.13)

| Expiry | max_pain | dist | put_call_oi_ratio |
|--------|----------|------|-------------------|
| **2026-06-18** | **$85** | −13.38% | 0.631 |
| 2026-06-26 | $85 | −13.38% | 1.001 |
| 2026-07-02 | $82 | −16.44% | 0.353 |
| 2026-07-10 | $84 | −14.40% | 0.318 |

Max pain sits **far below spot** because the chain is so call-heavy that minimizing
total payout pulls the theoretical pin down to ~$85. **But** pc_oi is 0.631 (call-heavy,
*not* a high-put downward setup), the regime is POSITIVE gamma, and the dealer DEX
hedge is to BUY underlying — all three resist a slide toward $85. Per the phase rubric,
a downward max-pain magnet "a short-gamma break can chase toward" requires short
gamma; here ZGL is ~$23, so a break to $85 needs a vol-expansion catalyst through the
gamma floor. **Base case: price stays pinned in the $95–100 gamma range, not $85.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw options-structure gex --symbol HOOD --dte-max 45 --date 2026-06-15` | regime POSITIVE, ZGL 25.91, GEX +77.6M, $100 wall +18.17M ← `.regime/.zero_gamma_level/.per_strike[].net_gex` | per-strike |
| `uw options-structure dex --symbol HOOD --dte-max 45 …` | net_dex +2.10B, hedge=BUY ← `.net_dex/.interpretation` | agg |
| `uw options-structure vanna-charm --symbol HOOD --dte-max 45 …` | net_vanna −14,004, charm +830,665 ← `.net_vanna/.net_charm` | agg |
| `uw options-structure iv-term-structure --symbol HOOD …` | BACKWARDATION; 6/18 iv 91.7% vs 7/17 70.9% ← `.structure/.term_structure[].avg_iv` | 20 exp |
| `uw options-structure term-skew --symbol HOOD --dte-target 30 …` | COMPLACENT, ratio 1.001 ← `.interpretation/.skew_ratio` | 30d |
| `uw options-structure front-end-iv-ratio --symbol HOOD --near-dte 7 --far-dte 30 …` | FLAT, 1.031 ← `.regime/.ratio` | near/far |
| `uw options-structure today-gamma-flip --symbol HOOD …` | POSITIVE, walls $100/$95/$97 support ← `.key_walls[]` | 6/18 |
| `uw options-structure max-pain --symbol HOOD --dte-max 30 …` | 6/18 max_pain $85 −13.38% ← `.results[].max_pain` | 4 exp |

## Tool errors

(none — initial IV-term jq used a non-existent `.iv` key and errored on null×100;
re-read the correct `.avg_iv`. GEX per-strike field is `net_gex` not `gex` — corrected.
No bad value transcribed.)

## DATA NOTE / CORRECTION

- GEX per-strike field is `net_gex` (first jq used `.gex` → null); IV-term row field is
  `avg_iv` (first jq used `.iv` → null×100 error). Both re-read against the correct
  paths before any value was recorded.
- Structure tools reference spot $98.14–98.59 vs the $98.12 close used in phases 0.5–3;
  the ~0.5 difference is a last-vs-close artifact and does not change any regime label.

## Verdict for downstream phases

- **Dealer regime:** **LONG GAMMA (positive)** — mean-reversion, suppressed realized
  vol, dealer-buy-underlying floor (DEX). Range-bound with $100 as the gamma+call-wall
  ceiling; explosive upside structurally capped near-term.
- **Conviction:** **3 / 5** — the long-gamma + buy-hedge floor is clear and supportive,
  but negative vanna (IV-fall selling headwind), complacent skew, and the $85 max-pain
  downward bias are real offsets.
- **Three structural levels for phase-9:**
  1. **$100** — largest GEX strike (+$18.17M) = gamma pin + call wall (phase-3) =
     primary ceiling/breakout trigger. Confluence across phases.
  2. **$95** — secondary gamma support wall (+$9.73M); with the DP base $92–93
     (phase-2) frames the lower edge of the pin range.
  3. **Max-pain $85 (6/18)** — opex-gravity downward magnet; *soft* under positive
     gamma. Treat as a tail target only if a catalyst breaks the $92–95 floor.
  - ZGL ~$23–26 = regime confirmation (long gamma all the way down), not a tradeable level.
- **Open questions:** Does phase-6 find a discrete HOOD catalyst justifying the 6/18
  front-IV backwardation, or is it pure OPEX mechanics? Does the complacent skew + low
  IV argue for owning cheap optionality (debit structure) over premium selling? Will
  declining IV (vanna headwind) cap any $100 breakout attempt?
