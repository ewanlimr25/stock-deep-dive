# Invalidation Rubric (Phase 9)

A thesis is invalidated when ONE of the following fires. Each phase-9 trade
plan MUST list all three categories with concrete, falsifiable conditions.

## Price-based (always include)

Pick the tightest of:
- Two daily closes below/above a level cited from phase-2 (dark pool wall) or
  phase-3 (largest OI strike).
- Intraday break of the gamma flip (phase-4) with no immediate reclaim.
- Move beyond ATR×1.5 against the directional bias within the time horizon.

## Signal-based (always include)

Pick the most diagnostic of:
- **DEX/GEX flip** in the wrong direction on phase-4 daily refresh.
- **Cumulative premium flow** turns net against thesis for 3 consecutive
  sessions (phase-5 `historical_cumulative_premium_flow`).
- **Dark pool accumulation** reverses to distribution (phase-7
  `insights_institutional_accumulation`).
- **Conviction matrix** flips from `DIRECTIONAL_LONG` to `HEDGED_LONG` or vice
  versa (phase-7 `insights_conviction_matrix`).

## Macro-based (always include)

Pick the highest-probability event in the next 30d from phase-6's calendar:
- Hawkish/dovish surprise from FOMC, CPI print, NFP, or PPI relative to
  consensus.
- Regime flip from `RISK-ON` to `RISK-OFF` (or vice versa) per UW
  `risk_market_regime`.
- Sector-specific catalyst (chip-export rules, drug approval, tariff change)
  cited in phase-6.

## What does NOT count as invalidation

- A single down-day on no volume.
- One sub-agent in phase-8 disagreeing while the other four align.
- IV crush after earnings if the directional thesis is structural.
- A single news headline absent a follow-through move.

## Exit on invalidation

Phase-9 must specify ONE of:
- **Hard stop:** close 100% at the price/signal level.
- **Tranche exit:** close 50% at first invalidation, 50% at the secondary.
- **Roll:** restructure to a defined-risk hedge instead of closing.

Choose based on the option structure (debit = hard stop usually; credit = roll
or close).
