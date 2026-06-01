# Phase 5 — Historical Context & VRP

## Goal

Place today's signals in their multi-day, multi-week context. Identify
volatility regime, premium-flow trends, GEX regime stability, and historical
win rate of the signals that are currently firing. Emit `phase-5-historical.md`.

## Tools

All take `--symbol <S>` (except `signal-backtest`, which is market-wide) and
`--json`.

| Command | What it answers |
|---------|-----------------|
| `uw historical iv-percentile-zscore --symbol <S> --lookback-days 252 --json` | 1y IV percentile + z-score |
| `uw historical vrp --symbol <S> --realised-window-days 30 --json` | IV30 minus realized vol30 |
| `uw historical cumulative-premium-flow --symbol <S> --days 90 --json` | LEAP-grade premium accretion |
| `uw historical pc-ratio-zscore --symbol <S> --lookback-days 20 --json` | Sentiment extreme detector |
| `uw historical gex-time-series --symbol <S> --days 30 --dte-max 45 --json` | Multi-day ZGL + regime flips |
| `uw historical oi-trend --symbol <S> --days 30 --top-n 10 --json` | OI buildup over time |
| `uw historical trend --symbol <S> --days 30 --json` | Multi-day vol/premium/IV/PCR |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | Historical win rate of current signal (set `--signal-type` to match the phase-1/2 verdict) |

## Composition guidance

- Run `uw historical signal-backtest` with the signal type that matches phase-1's
  verdict (e.g., `bullish_flow` if phase-1 was bullish, `bearish_flow` if
  bearish, `dark_pool_accumulation` if phase-2 was the dominant signal).
  Record signal-specific win_rate or vol_realisation_rate.
- **This win-rate is the Kelly `p` for phase-9 sizing — surface it explicitly.**
  The backtest result returns a `win_rate` (or `vol_realisation_rate`) and a
  sample size `n` (`total_signals`). Phase 9 sizes on this empirical rate, not
  the conviction bin (`rubrics/sizing-rubric.md` §"Choosing the Kelly `p`").
  If the tool returns `{"note":"no backtest results","total_signals":0}`,
  record `win_rate_source=null` so phase-9 falls back to the conviction bin.
  `win_rate` and `total_signals` are **top-level** fields (not per-row), and the
  tool is **market-wide** (no `--symbol`) — so `p` is the base rate of that signal
  class across the tape, not a `<SYMBOL>`-specific rate; say so in the handoff
  block. The empty stub occasionally appears even when a populated result is
  expected — re-run once before recording `win_rate_source=null`.
- `uw historical trend` and `uw historical oi-trend` are the workhorses — run both.
- **`fz` price-context cross-check (D8, advisory).** If `fz_available=yes`
  (phase-0), pull a non-UW read of where price sits in its own range:
  `fz quote <SYMBOL> --agent | jq -c '{rsi:.fundamentals."RSI (14)", sma50:.fundamentals.SMA50, sma200:.fundamentals.SMA200, perf_ytd:.fundamentals."Perf YTD", high52:.fundamentals."52W High", low52:.fundamentals."52W Low"}'`
  (`lib/fz-recipes.md §1`; `52W High/Low` come as a combined `"<level> <pct>%"`
  string). This is an **independent, EOD cross-check** on the UW IV/trend read —
  e.g. an overbought RSI at the 52-week high tempers a fresh-breakout thesis. Tag
  `[HIST:rsi fz]`, `[HIST:52w_proximity fz]`. Advisory; it never enters the Kelly
  `p` or the sizing handoff block. Skip silently if `fz` is absent.

### Gap-aware lookbacks (MANDATORY — the snapshot window is non-contiguous)

The data behind these tools is **not contiguous**: there is a **21-session hole
(2026-03-28 → 2026-04-24)** between two clusters (2026-03-13…03-27 and
2026-04-27…<latest>) — see phase-0's available-local-dates list. The late cluster's
end advances as new sessions land (05-22 at the 2026-05-25 audit, 05-29 as of
2026-06-01); read the exact bounds from phase-0's list, never hardcode them. The `uw historical`
commands read the same `~/Documents/Stocks` files the escape hatch does, so:
- When a `--days` / `--lookback-days` window **crosses the hole**, report the
  **actual number of sessions present**, not the calendar span, and never annualize
  or fit a "30-day trend" across the gap. Quote N explicitly (e.g. "30d trend over
  the **19 sessions actually present**, gap 03-28→04-24 excluded"). Prefer the
  tool's **own** session count over the calendar span: `iv-percentile-zscore.dates_used`,
  `trend.days_analyzed` + `trend.date_range`, and the length of `oi-trend` /
  `gex-time-series` series give the actual N — quote THAT.
- If a `uw historical` series looks suspiciously smooth across late-Mar/Apr,
  **suspect the gap** — cross-check against phase-0's date list (or `lib/duckdb-cuts.md
  § gap`). If the CLI silently interpolates across the hole, surface that as a
  data-quality caveat in the `## Tool errors` section rather than trusting the line.
- This caveat shrinks confidence; a small *true* N (< 10 sessions) is low-confidence
  regardless of the calendar window requested.
- **Latest-anchor caveat (not as-of reproducible).** The trailing commands that
  take no `--date` (`iv-percentile-zscore`, `pc-ratio-zscore`, `oi-trend`,
  `cumulative-premium-flow`, `gex-time-series`, `trend`, `signal-backtest`) and
  `vrp`'s realised-vol leg
  anchor their window to the **latest available date**, not to the run's as-of
  date. A re-run after a new session lands (e.g. an earnings day) shifts every
  trailing read — IV30d, z-scores, build-day counts, win-rates all move. This is
  engine behavior, not a data error; note the latest available date alongside any
  trailing datapoint so a later re-read is interpretable.

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
   - ### Price context (`fz` RSI / SMA20-50-200 / Perf / 52W proximity — advisory
     cross-check on the UW IV/trend read; omit if `fz` absent)
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
