# Phase A2 — Chart, Technicals & Patterns (the new layer; goal #4 / #5)

## Goal

Produce the price-structure layer the flow substrate lacks: trend, levels,
indicators, Fibonacci, and chart patterns (flags, head-&-shoulders, double
top/bottom, triangles, cup-&-handle, and an Elliott-wave working count). This is
the deterministic source for "levels to watch on the charts" (goal #4) and
"potential patterns forming" (goal #5).

## Steps

1. **Run the chart engine** (foreground; read the actual JSON before writing):
   ```bash
   python3 .claude/skills/trade-plan/lib/chart_engine.py \
       --ticker <SYMBOL> --date <as_of> --lookback 540 \
       > trade-plans/<SYMBOL>/<DATE>/chart.json
   python3 -c "import json;d=json.load(open('trade-plans/<SYMBOL>/<DATE>/chart.json'));print(d['available'],d['source'])"
   ```
   If `available: false`, record the remedy from the JSON and tell A3/A4 the
   chart layer is absent (B1 critical gap). Do not invent levels.

2. **Interpret, don't just transcribe.** Read `chart.json` and write the
   narrative read using `rubrics/pattern-rubric.md`:
   - **Trend / structure:** `trend.market_structure` + the MA stack
     (`indicators.ma_stack`, dist to 50/200). Note divergences (e.g. 60-day
     regression up but last two swings lower-high/lower-low).
   - **Momentum / volatility:** RSI state, MACD state, ATR (for stops), volume
     vs 20-day average, 52-week proximity.
   - **Support / resistance:** the top clustered levels (`support_resistance`,
     ranked by touches) and the recent swing pivots. Flag any level that lines
     up with a dealer/OI level from the deep dive — that confluence is the
     tradeable one.
   - **Fibonacci:** the dominant-swing retracement cluster + extensions; call
     out coincidences with pivots or dealer levels.
   - **Patterns:** for every entry in `patterns` with `detected: true`, report
     type · direction · confidence · measured target · invalidation ·
     confirmation trigger, per the pattern rubric. Cap engine output at
     `medium`; promote to `high` only with a written, cited manual read.
   - **Elliott wave:** report the working count, `rules_passed: x/3`, the
     wave-5/next-leg projection as a *zone*, and its invalidation. Label it a
     hypothesis; it shapes targets, it does not set the bias.

3. **Tag everything** with the new `[CHART:<detector>]` tag (e.g.
   `[CHART:sma50]`, `[CHART:swing_low]`, `[CHART:triangle]`,
   `[CHART:elliott_wave]`, `[CHART:fib_0.618]`). These resolve to `chart.json`.

## Write `trade-plans/<SYMBOL>/<DATE>/phaseA2-chart.md`

Summary (2–4 sentences), key signals (tagged), detailed findings (trend /
momentum / S-R / fib / patterns / elliott), the tool-call line, and a verdict:
chart bias (bullish/bearish/neutral), the 3 most important levels, and the
single most credible pattern (with its confirmation trigger).

## Verdict for downstream

- chart bias + conviction (1–5)
- ranked levels (with sources) for A3's level ladder
- the patterns to carry into the plan, each with target + invalidation
