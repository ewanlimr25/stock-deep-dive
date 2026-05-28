# Phase 4 — Dealer Structure & Gamma

## Goal

Map dealer positioning and second-order Greeks. Identify gamma flip, vanna /
charm flows, term structure regime. Emit `phase-4-structure.md`.

## Tools

All require `--symbol <SYMBOL>` and take `--json`; pass `--date <AS-OF>` if not
today. `term-skew` reports the regime in `interpretation` and the ratio in
`skew_ratio`; `iv-term-structure` returns the regime in `structure` and the rows
in `term_structure`.

| Command | What it answers |
|---------|-----------------|
| `uw options-structure gex --symbol <S> --dte-max 45 --json` | GEX per strike + Zero Gamma Level |
| `uw options-structure dex --symbol <S> --dte-max 45 --json` | Net dealer delta hedge |
| `uw options-structure vanna-charm --symbol <S> --dte-max 45 --json` | Vanna + charm + squeeze signal |
| `uw options-structure iv-term-structure --symbol <S> --json` | Backwardation / contango / kinked |
| `uw options-structure term-skew --symbol <S> --dte-target 30 --json` | 25Δ put vs call IV |
| `uw options-structure front-end-iv-ratio --symbol <S> --near-dte 7 --far-dte 30 --json` | Event-stress signal |
| `uw options-structure today-gamma-flip --symbol <S> --json` | 0DTE ZGL + ATM flip + walls |

## Composition guidance

- Default `--dte-max 45` keeps the read on near-term dealer hedging (which
  drives intraday moves). For LEAPs, pass `--dte-max 365` and call out
  separately.
- `uw options-structure today-gamma-flip` is 0DTE-only and intraday — only meaningful if running
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
