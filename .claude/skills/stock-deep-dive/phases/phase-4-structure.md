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
| `uw options-structure max-pain --symbol <S> --dte-max 30 --json` | **Per-expiry max-pain strike** (the OI-pin magnet) + `distance_pct` from spot + `put_call_oi_ratio`. The opex-gravity read — where the chain pulls price into each expiry. Add `--expiry <D>` for the full per-strike `pain_curve`; `--dte-max 0` to include LEAPs. |

## Composition guidance

- Default `--dte-max 45` keeps the read on near-term dealer hedging (which
  drives intraday moves). For LEAPs, pass `--dte-max 365` and call out
  separately.
- `uw options-structure today-gamma-flip` is 0DTE-only and intraday — only meaningful if running
  the skill during the trading session. If after-hours, note and skip.
- **`uw options-structure max-pain` is the opex-gravity read** — compute max pain
  natively here, never assert a max-pain level by eye (the invented-command
  fabrication of 2026-05-30, `docs/audit/2026-05-30`, asserted "max-pain 195" when
  the real magnet was 207.5–210). Read it *with* the GEX surface: max pain near a
  positive-gamma pin reinforces the range; max pain far below spot with a high
  `put_call_oi_ratio` is a downward pull that a short-gamma break can chase toward.
  Cross-check the near-expiry max-pain strike against phase-3's `oi-by-strike`
  walls and `term-structure` OPEX cliff — they should roughly agree.

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
   - ### Max pain (per-expiry pin strike, distance from spot, P/C OI ratio —
     the opex-gravity magnet for phase-9's levels/calendar)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Dealer regime (long γ / short γ / transitional)
   - Conviction 1–5
   - Three structural levels for phase-9 (ZGL, largest GEX strike, vanna
     pivot) — **plus the near-expiry max-pain strike** as the opex pin magnet
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
- Max pain is a **static-OI** estimate ("OI unchanged to expiry," per the tool's
  own `caveat`) — it migrates as OI builds, so the further the expiry, the softer
  the magnet. Quote the near-expiry strike for tradeable gravity; treat far-dated
  max pain as indicative only.
