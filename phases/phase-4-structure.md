# Phase 4 — Dealer Structure & Gamma

## Goal

Map dealer positioning and second-order Greeks. Identify gamma flip, vanna /
charm flows, term structure regime. Emit `phase-4-structure.md`.

## Tools

All require `symbol=<SYMBOL>`.

| Tool | Args | What it answers |
|------|------|-----------------|
| `mcp__uw-pp__options_structure_gex` | symbol, dte_max=45 | GEX per strike + Zero Gamma Level |
| `mcp__uw-pp__options_structure_dex` | symbol, dte_max=45 | Net dealer delta hedge |
| `mcp__uw-pp__options_structure_vanna_charm` | symbol, dte_max=45 | Vanna + charm + squeeze signal |
| `mcp__uw-pp__options_structure_iv_term_structure` | symbol | Backwardation / contango / kinked |
| `mcp__uw-pp__options_structure_term_skew` | symbol, dte_target=30 | 25Δ put vs call IV |
| `mcp__uw-pp__options_structure_front_end_iv_ratio` | symbol, near_dte=7, far_dte=30 | Event-stress signal |
| `mcp__uw-pp__options_structure_today_gamma_flip` | symbol | 0DTE ZGL + ATM flip + walls |

## Composition guidance

- Default `dte_max=45` keeps the read on near-term dealer hedging (which
  drives intraday moves). For LEAPs, pass `dte_max=365` and call out
  separately.
- `today_gamma_flip` is 0DTE-only and intraday — only meaningful if running
  the skill during the trading session. If after-hours, note and skip.

## Output sections

1. **Summary** — dealer regime: long-gamma / short-gamma + ZGL relative to
   spot, term structure shape.
2. **Key signals** — top-5 with `[STRUCT:<tool>]` citations.
3. **Detailed findings**
   - ### GEX (total, per-strike top 10, zero gamma level)
   - ### DEX (net dealer delta, hedging direction)
   - ### Vanna + charm (squeeze regime if any)
   - ### IV term structure (regime + slope)
   - ### Term skew (put vs call IV, regime)
   - ### Front-end IV ratio (event stress)
   - ### Today's gamma flip (if intraday)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Dealer regime (long γ / short γ / transitional)
   - Conviction 1–5
   - Three structural levels for phase-9 (ZGL, largest GEX strike, vanna
     pivot)
   - Open questions

## Interpretation heuristics

- **Long-gamma regime** (spot ABOVE ZGL, GEX positive): dealers sell rallies
  and buy dips → intraday mean-reversion, suppressed realized vol.
- **Short-gamma regime** (spot BELOW ZGL, GEX negative): dealers buy rallies
  and sell dips → trend amplification, expanded realized vol.
- **Vanna squeeze setup**: positive vanna + negative dealer delta + IV
  declining → mechanical bid from dealer hedging.
- **Backwardation**: front-month IV > back-month → event stress (earnings,
  catalyst, macro).
- **Skew steepening** (puts much richer than calls): tail-hedging demand,
  often precedes broader risk-off.

## Common pitfalls

- ZGL on low-liquidity tickers is coarse; treat as ±2% band.
- Vanna/charm closed-form estimates are noisy at 0DTE and deep ITM/OTM —
  filter DTE ≥ 1.
- A flipped term structure can normalize the day after earnings — don't
  trade backwardation if earnings already passed within 24h.
