# Trade Plan — NBIS

**As-of date:** 2026-06-17
**Spot reference:** 280.91 (chart.json, yfinance)
**Voice:** desk PM running an institutional book
**Built from:** research/NBIS/2026-06-17/ (deep dive, age 0d) + chart engine (yfinance, 372 sessions)

> *For research and educational use only. Not financial advice. Sizing,
> structures, targets and dates are illustrative.*

## 0. Information completeness (gap audit)

- **Verdict:** SUFFICIENT — completeness 92%
- **Have:** flow (sweeps 5/5), dark pool (block-stratified), OI/positioning, dealer GEX/DEX/vanna, historical signal-backtest, macro + sector rotation, fundamentals (MSPR), sentiment/crowd, bull/bear debate, OHLCV chart + patterns, event calendar, expected move + IV rank.
- **Missing / how to source:**
  | Item | Severity | How to source |
  |------|----------|---------------|
  | Reused `gamma_flip` = 34.64 is implausible for a $280 name (scale/data artifact) | important | re-run `uw options-structure gex --symbol NBIS --dte-max 45 --json` for the real ZGL before trusting any gamma trigger |
  | Live intraday tape for the 6/22 event | nice_to_have | `uw options-flow sweeps --symbol NBIS` + intraday yfinance on the day |
  | Live borrow/HTB for squeeze sizing | nice_to_have | `fz quote NBIS --agent` (semi-monthly SI) + broker borrow fee |

## 1. Direction & conviction

- **Bias:** LONG (event-gated, defined-risk)
- **Conviction (M-01 bin):** 0.55 (slight)
- **Horizon:** 1-5d (the inclusion window)
- **Flow↔chart agreement:** CHART-LEADS / event-driven. The chart is cleanly bullish; the flow is bullish on the surface but distribution underneath, and the only durable edge is the mechanical 6/22 bid. High reversal risk after the event.

### Thesis

The only clean long is mechanical: Nasdaq-100 forced inclusion effective
2026-06-22 [MACRO:NDX_inclusion_2026-06-22] on a 5/5-session $722.4M bullish
sweep campaign [FLOW:sweep_persistence] into a chart printing new 52-week highs
with a bullish MA stack [CHART:ma_stack] — but the underlying is being
distributed into that strength (mega-tier dark pool 93.6% sell
[DP:block_stratified], insider MSPR -100 [FUND:MSPR]) and the firing signal is
edge-negative [HIST:signal_backtest], so this is a defined-risk, event-gated
starter only.

### Why it should work

- Mechanical forced bid: Nasdaq-100 inclusion 2026-06-22 is valuation-agnostic buying [MACRO:NDX_inclusion_2026-06-22], riding a 5/5-session $722.4M sweep campaign [FLOW:sweep_persistence] with a dealer dip-bid DEX +$2.88bn [STRUCT:dex].
- Price structure intact-bullish: stack 280.91 > 50d 193.96 > 200d 123.94 [CHART:ma_stack], uptrend HH-HL [CHART:market_structure], cleared the 6/02 swing high 278.84 into new highs [CHART:swing_high].
- Technology sector 5-day net inflow, persistence 0.8 [MACRO:sector_flow_persistence].

### Why it may fail (the honest other side)

- **Distribution into strength** — the lit bullish flow is partly exit liquidity: mega-tier DP 93.6% sell [DP:block_stratified], insider MSPR -100, ~1.04M-share May sale [FUND:MSPR].
- **Edge-negative signal** — bullish_flow backtests 37.5% (n=8, avg -0.58%) [HIST:signal_backtest]; history is against the long.
- **Sell-the-news + vanna crush** — 6/22 is the LAST identifiable forced bid; IV rank 91 [CTX:iv_rank] → negative-vanna crush post-OPEX can flip the dealer dip-bid to selling [STRUCT:vanna]; parabolic +127% vs the 200d.
- **Crowded long** and the bull/bear debate was disconfirmed [DEBATE:bear_residual].

## 2. Levels to watch

| Level | Role | Source | Note |
|-------|------|--------|------|
| 278.84 | trigger | [CHART:swing_high] | hold above = breakout intact |
| 300.00 | resistance / T1 | [OI:oi_by_strike] | $300 call wall |
| 267.50 | support / pin | [STRUCT:max_pain] | close below = thesis broken |
| 256.62 | stop (1 ATR) | [CHART:atr14] | ATR(24.29) |
| 200.30 | major support | [CHART:swing_low] | 6/09 swing low; HTF invalidation |

MAs: 20d 233.76 · 50d 193.96 · 200d 123.94 (all well below spot — parabolic). Fib (up-swing) retraces: 0.382 → 212.21, 0.5 → 185.72.

## 3. Patterns forming (chart)

| Pattern | Direction | Confidence | Measured target | Invalidation | Note |
|---------|-----------|-----------|-----------------|--------------|------|
| double bottom | bullish | low | — | 198.31 | the 198–200 base that launched the parabola — already played out, NOT a fresh entry |
| Elliott working count | neutral | none | — | — | engine count internally inconsistent (impulse-up label, projection 244 below spot); discarded, yields to flow+structure |

## 4. Upcoming events that move the tape

| Date | Event | Impact | Source |
|------|-------|--------|--------|
| 2026-06-18 | June OPEX (26.7% of OI); +gamma pin + vanna unwind | ? | [OI:opex_concentration] |
| 2026-06-22 | Nasdaq-100 inclusion effective (forced buying, then sell-the-news) | + | [MACRO:NDX_inclusion_2026-06-22] |
| 2026-07-15 | June CPI | - | [MACRO:CPI] |
| 2026-08-06 | NBIS earnings (beyond horizon) | ? | [FUND:next_earnings] |

## 5. Invalidation

- **Price-based:** two daily closes below the 267.5 pin; a close below 256.62 (1 ATR) negates the event long.
- **Signal-based:** the 5/5 sweep campaign drops out of top sweeps, or DEX dip-bid flips negative as mega-DP selling accelerates post-inclusion.
- **Macro-based:** hot June CPI (7/15) / hawkish re-assertion, or sell-the-news after 6/22.

## 6. Sizing (% of risk, NOT dollars)

- **Kelly p (empirical):** p_raw = 0.375 (bullish_flow, n=8, src=backtest) → capped p = 0.375 [HIST:signal_backtest]
- **Inputs:** b = 1.73, fraction = 0.25, cap_pct = 5
- **Raw Kelly:** 0.014 → fractional ceiling 0.35%. **Win-rate map:** p < 0.50 → starter/skip.
- **Risk gates (each cut):** fundamentals CAUTION · sentiment CAUTION · crowd CROWDED_LONG · rotation aligned (no cut) · debate disconfirmed · context GENUINELY_UNUSUAL (no cut).
- **Final size:** **0.3% of book risk** (starter; the gates + negative edge keep this tiny). No upward deviation.

## 7. Plan A — pure stock (long)

- **Direction:** long (event-gated)
- **Entry:** 281 — trigger: hold above the 278.84 breakout into 6/22; do NOT chase if it loses 267.5.
- **Stop:** 267.4 (under the pin)
- **Targets:** T1 300.0 ($300 call wall, take 70%) · T2 310.0 (overshoot, take 30%)
- **Reward:risk to T1:** ~1.4
- **Size:** 0.3% book
- **One-liner:** Tiny, event-gated long for the 6/22 forced-inclusion bid; stop under the 267.5 pin; take most off at the 300 wall before the sell-the-news/vanna-crush risk.

## 8. Plan B — options (target date + target price)

### B1 — directional

- **Structure:** 290/300 call debit spread
- **Strikes / expiry:** 290/300 / 2026-06-26
- **Target date / target price:** 2026-06-22 / 300.0
- **Debit · breakeven · max loss:** 3.5 · 293.5 · 3.5 · est. payoff at target ~6.5
- **Why:** tiny event-box on the inclusion; the $300 short strike caps the rich IV (rank 91); width 10 ≈ ~0.7× the $13.66 expected move.

### B2 — defined-risk alternative (the higher-EV expression)

- **Structure:** iron condor 255/265 put + 300/310 call
- **Strikes / expiry:** as above / 2026-06-26
- **Target date / target price:** 2026-06-26 / 280.0 (mean-reversion / pin)
- **Credit · breakevens · max loss:** 3.3 · 261.70 / 303.30 · 6.7
- **Why:** harvest IV rank 91 in the positive-gamma mean-reversion zone; wings beyond the ±4.86% ($13.66) expected move.

## 9. Post-entry monitoring checklist

- [ ] Confirm the 278.84 breakout holds on a closing basis before/at 6/22.
- [ ] Watch mega-DP sell-ratio + DEX after 6/18 OPEX — distribution accelerating = exit.
- [ ] Take 70% at the 300 wall; do not hold the directional through the 6/22 sell-the-news / vanna-crush window.
- [ ] Re-source the real gamma flip (`uw options-structure gex`) — do not act on the bogus 34.64.

## 10. Reasoning-ledger lessons applied

- **L-0001** — event/momentum long sized starter; defined-risk preferred until the inclusion bid confirms and holds the 278.84 breakout.

## Citations (≥3, what the eval will spot-check)

1. [FLOW:sweep_persistence] NBIS top sweeps 5/5 sessions, $722.4M — research/NBIS/2026-06-17/phase-1-flow.md
2. [DP:block_stratified] mega-tier DP buy_ratio 0.064 (93.6% sell), $158.5M — research/NBIS/2026-06-17/phase-2-dark-pool.md
3. [CHART:ma_stack] 280.91 > 50d 193.96 > 200d 123.94, 0.0% off the 52-week high — chart.json
4. [HIST:signal_backtest] bullish_flow win_rate 0.375 (n=8), avg -0.58% — research/NBIS/2026-06-17/phase-5-historical.md
