# Phase A2 — Chart, Technicals & Patterns — NBIS 2026-06-17

**Source:** chart.json (yfinance, 372 daily sessions, look-ahead safe to 2026-06-17)

## Summary

NBIS is in a confirmed parabolic uptrend at new 52-week highs (0.0% off the
high, +534% above the 52-week low). Trend and momentum are bullish; the only
chart caution is the degree of extension above the moving averages, which sets up
mean-reversion risk if the event bid fails.

## Key signals

- Bullish MA stack: 280.91 > 20d 233.76 > 50d 193.96 > 200d 123.94 [CHART:ma_stack]; +127% vs the 200d [CHART:dist_to_sma200_pct].
- Market structure uptrend HH-HL, 60d regression slope +2.68/day [CHART:market_structure]; spot has cleared the 2026-06-02 swing high 278.84 [CHART:swing_high].
- RSI 68.6 (high-neutral, not yet >70) [CHART:rsi14]; MACD histogram positive [CHART:macd]; volume 1.42× the 20d average [CHART:vol_vs_avg].
- ATR 24.29 (~8.6% of price) [CHART:atr14] — wide; stops must respect it.

## Detailed findings

- **Support/resistance:** recent pivots 183 (5/19) → 226.81 (5/21) → 198.31 (5/27) → 278.84 (6/02) → 200.30 (6/09). Above spot, the structural ceiling is the round/OI $300; below, the nearest real shelf is the 200–198 base (the 6/09 low 200.30 and the 5/27 low 198.31), well beneath the deep-dive 267.5 OI pin.
- **Fibonacci (up-swing):** retracements 0.382 → 212.21, 0.5 → 185.72; extensions 1.272 → 358.97, 1.618 → 436.62. No fib level sits near spot — price is in discovery above the swing high.
- **Patterns:** `double_bottom` (low confidence) describes the 198–200 base that *launched* the parabola — already played out, not a fresh entry. `elliott_wave` count is internally inconsistent (impulse-up label but a wave-5 projection of 244, below spot; 2/3 rules, wave-4 overlap) → **discarded**; it yields to flow + structure.

## Tool calls

| Command | Key values |
|---------|-----------|
| `chart_engine.py --ticker NBIS --date 2026-06-17` | available true; source yfinance; spot 280.91; ma_stack bullish; trend uptrend_HH_HL; patterns_detected [double_bottom, elliott_wave]; ATR 24.29 |

## Verdict for downstream

- **Chart bias:** bullish (4/5); conviction 4/5 on trend, but extension is a real mean-reversion risk.
- **Three levels:** trigger 278.84 (breakout) · target/resistance 300 · stop zone 256–267 (1 ATR / pin).
- **Most credible pattern:** none fresh — the move is a continuation, not a new setup; treat the chart as confirming momentum, with the trade thesis carried by the 6/22 mechanical bid (A3).
