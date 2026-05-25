# Phase 5 — Historical Context & VRP

## Goal

Place today's signals in their multi-day, multi-week context. Identify
volatility regime, premium-flow trends, GEX regime stability, and historical
win rate of the signals that are currently firing. Emit `phase-5-historical.md`.

## Tools

| Tool | Args | What it answers |
|------|------|-----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | symbol, lookback_days=252 | 1y IV percentile + z-score |
| `mcp__uw-pp__historical_vrp` | symbol | IV30 minus realized vol30 |
| `mcp__uw-pp__historical_cumulative_premium_flow` | symbol, days=90 | LEAP-grade premium accretion |
| `mcp__uw-pp__historical_pc_ratio_zscore` | symbol, lookback_days=20 | Sentiment extreme detector |
| `mcp__uw-pp__historical_gex_time_series` | symbol, days=30, dte_max=45 | Multi-day ZGL + regime flips |
| `mcp__uw-pp__historical_oi_trend` | symbol, days=30, top_n=10 | OI buildup over time |
| `mcp__uw-pp__historical_trend` | symbol, days=30 | Multi-day vol/premium/IV/PCR |
| `mcp__uw-pp__historical_signal_backtest` | signal_type=bullish_flow (or aligned with phase-1 verdict), lookback_days=20, top_n=20 | Historical win rate of current signal |

## Composition guidance

- Run `historical_signal_backtest` with the signal type that matches phase-1's
  verdict (e.g., `bullish_flow` if phase-1 was bullish, `bearish_flow` if
  bearish, `dark_pool_accumulation` if phase-2 was the dominant signal).
  Record signal-specific win_rate or vol_realisation_rate.
- **This win-rate is the Kelly `p` for phase-9 sizing — surface it explicitly.**
  The backtest result returns a `win_rate` (or `vol_realisation_rate`) and a
  sample size `n` (`total_signals`). Phase 9 sizes on this empirical rate, not
  the conviction bin (`rubrics/sizing-rubric.md` §"Choosing the Kelly `p`").
  If the tool returns `{"note":"no backtest results","total_signals":0}`,
  record `win_rate_source=null` so phase-9 falls back to the conviction bin.
- `historical_trend` and `historical_oi_trend` are the workhorses — run both.

### Gap-aware lookbacks (MANDATORY — the snapshot window is non-contiguous)

The data behind these tools is **not contiguous**: there is a **21-session hole
(2026-03-28 → 2026-04-24)** between two clusters (2026-03-13…03-27 and
2026-04-27…05-22) — see phase-0's available-local-dates list. The `historical_*`
tools read the same `~/Documents/Stocks` files the escape hatch does, so:
- When a `days=` / `lookback_days=` window **crosses the hole**, report the
  **actual number of sessions present**, not the calendar span, and never annualize
  or fit a "30-day trend" across the gap. Quote N explicitly (e.g. "30d trend over
  the **19 sessions actually present**, gap 03-28→04-24 excluded").
- If an MCP historical series looks suspiciously smooth across late-Mar/Apr,
  **suspect the gap** — cross-check against phase-0's date list (or `lib/duckdb-cuts.md
  § gap`). If the MCP silently interpolates across the hole, surface that as a
  data-quality caveat in the `## Tool errors` section rather than trusting the line.
- This caveat shrinks confidence; a small *true* N (< 10 sessions) is low-confidence
  regardless of the calendar window requested.

## Output sections

1. **Summary** — IV percentile, VRP regime, premium-flow direction, GEX
   regime stability over 30d.
2. **Key signals** — top-5 with `[HIST:<tool>]` citations.
3. **Detailed findings**
   - ### IV regime (percentile + z-score + VRP)
   - ### Cumulative premium flow (90d net direction)
   - ### P/C ratio z-score (sentiment extreme y/n)
   - ### GEX time series (regime flip dates if any)
   - ### OI trend (sustained buildup vs spike vs decay)
   - ### Multi-day trend table (date / vol / premium / IV rank / PCR)
   - ### Signal backtest (current signal's historical edge)
4. **Tool calls** — audit.
5. **Tool errors** — verbatim.
6. **Verdict for downstream**
   - Volatility regime (cheap / fair / rich)
   - Premium-buying vs premium-selling environment
   - Conviction 1–5 on whether today's signal is HISTORICALLY EDGE-POSITIVE
   - Three specific data points (IV %ile, VRP value, signal win rate)
   - **Sizing handoff block (phase-9 reads these verbatim):**
     ```
     signal_class:     <e.g. bullish_flow>
     signal_backtest_win_rate: <0.00–1.00 or null>
     win_rate_n:       <integer total_signals, or 0>
     win_rate_source:  backtest | null
     ```
     This is the Kelly `p` input — see `rubrics/sizing-rubric.md`
     §"Choosing the Kelly `p`". Quote the raw win-rate; phase-9 applies the
     N-conditional cap.
   - Open questions

## Interpretation heuristics

- **IV cheap + VRP < 0**: premium-BUYING regime → favor debit structures.
- **IV rich + VRP > 0**: premium-SELLING regime → favor credit structures.
- **Cumulative premium flow + and persistent ≥ 60d**: stealth institutional
  build → high confidence directional.
- **P/C z-score |z| > 2**: sentiment extreme → contrarian setup possible.
- **GEX regime flip in last 5d**: dealer hedging dynamics in transition →
  larger intraday ranges expected.
- **Signal backtest win_rate < 0.45**: today's setup has historically lost →
  downgrade conviction even if today's signals look strong.

## Common pitfalls

- IV percentile is a 1y metric; in a structurally-low-vol year, 80th
  percentile may still be cheap by long-term standards.
- VRP can flip on a single catalyst day — read the trailing-5d trend, not
  just today.
- Signal backtests have small N for sparse tickers; treat <10 historical
  firings as low-confidence.
- Historical tools return empty on tickers that listed recently or had
  trading halts during the lookback window.
