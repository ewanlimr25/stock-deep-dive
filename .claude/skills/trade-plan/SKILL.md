---
name: trade-plan
description: Builds an actionable, falsifiable trade plan (a clear direction with reasons it should work AND reasons it may fail, chart levels to watch, upcoming market-moving events, and forming chart patterns like flags / head-and-shoulders / triangles / Elliott waves) for one US-listed ticker. Reuses any existing stock-deep-dive research for the flow/positioning/structure layer and adds a price-structure/pattern layer from OHLCV. Emits at least one pure stock long/short plan and at least one options plan with a target date and target price, saved to trade-plans/<SYMBOL>/<DATE>/. Use when the user asks to "build a trade plan / strategy / setup for <TICKER>", "what's the play on <TICKER>", "give me a long/short and an options trade for <TICKER>", or "recommend a trade for <TICKER>".
model: fable
effort: xhigh
---

# Trade Plan

Turns evidence into a tradeable, two-sided plan for a single US-listed ticker. It
is the action layer that sits **on top of** `stock-deep-dive`: where the deep
dive reads the options-flow tape, this skill reuses that read, adds the price
chart the flow substrate lacks, and converts the whole picture into concrete
stock and options plans with explicit reasons-for, reasons-against, levels,
events, patterns, and sizing.

The complementary `/trade-plan-eval` skill marks each plan to market after a
trade is taken and writes lessons back to a reasoning ledger this skill reads —
so the recommendations improve with use.

## When to invoke

- "trade plan / trade strategy / setup / the play for <TICKER>"
- "recommend a trade (long/short or options) for <TICKER>"
- "give me a stock plan and an options plan for <TICKER>"

Do NOT invoke for: a pure research read with no recommendation (use
`/stock-deep-dive`), market-wide scans (use `uw-daily-analysis`), or marking a
past plan to market (use `/trade-plan-eval`).

## Inputs

- **Required:** one US-listed ticker (equity or ETF).
- **Optional:** as-of date (default = today). All look-backs are look-ahead safe.
- **Optional:** book risk %/cap overrides (defaults: fraction 0.25, cap 5%).

## What it satisfies (the 8 goals)

1. **Is anything critical missing?** Phase A1 grades evidence against
   `rubrics/gap-rubric.md` and emits a `gap_audit` with a verdict.
2. **How to source the gaps?** Every gap carries a concrete `how_to_source`.
3. **Direction with reasons for AND against.** Phase A3 → `reasons_for[]` +
   `reasons_against[]` (steelmanned), every line tagged.
4. **Levels + events + missing info.** A3 builds the level ladder and the
   market-moving event calendar; A1 surfaces what's missing.
5. **Forming patterns.** A2's `chart_engine.py` detects flags, H&S, double
   top/bottom, triangles, cup-&-handle, and an Elliott-wave working count.
6. **A learning loop.** `/trade-plan-eval` marks plans to market and updates the
   reasoning ledger (see that skill).
7. **Saved as `trade-plans/<SYMBOL>/<DATE>/`** — same convention as the deep dive.
8. **≥1 pure stock long/short plan AND ≥1 options plan with target date + price.**

## Output convention (MANDATORY)

```
trade-plans/<SYMBOL>/<YYYY-MM-DD>/
  phaseA0-intake.md       reuse detection + ledger load
  phaseA1-gap-audit.md    critical-info gap audit + sourcing plan (goal #1/#2)
  phaseA2-chart.md        chart / technicals / patterns (goal #4/#5)
  chart.json              raw deterministic chart-engine output
  phaseA3-confluence.md   direction + reasons + levels + events (goal #3/#4)
  trade-plan.md           the deliverable (stock plan + options plans) (goal #8)
  trade-plan.json         structured, validated envelope (eval consumes it)
```

**Immutability:** never overwrite an existing file in the same `<SYMBOL>/<DATE>`.
Re-run on the same day → append `-v2` and reference the prior version.

## Phase graph

| # | File | Purpose | Detailed prompt |
|---|------|---------|-----------------|
| A0 | `phaseA0-intake.md` | validate, set up dir, reuse latest deep dive, load ledger | `phases/phase-A0-intake.md` |
| A1 | `phaseA1-gap-audit.md` | grade evidence vs the required-input checklist; verdict | `phases/phase-A1-gap-audit.md` |
| A2 | `phaseA2-chart.md` + `chart.json` | OHLCV → indicators, levels, fib, patterns, Elliott | `phases/phase-A2-chart.md` |
| A3 | `phaseA3-confluence.md` | fuse flow + chart → direction, reasons, levels, events | `phases/phase-A3-confluence.md` |
| A4 | `trade-plan.md` + `trade-plan.json` | stock plan + options plans; validate | `phases/phase-A4-plans.md` |

## Tooling & data

- **Reuse first.** The flow / dark-pool / OI / dealer-structure / historical /
  macro / fundamentals / sentiment / debate layers come from the most recent
  `research/<SYMBOL>/<DATE>/` deep dive (its `decision.json` + phase MDs). Do not
  re-pull what it already has. If none exists, A0 either recommends a deep dive
  or pulls a compact live `uw` snapshot.
- **Chart engine** (`lib/chart_engine.py`, `lib/ohlc.py`): OHLCV via yfinance
  (primary) with the UW Stock-Screener parquet as the offline fallback. Pure
  pandas/numpy + stdlib. Always exits 0 with an `available` flag.
- **Supporting CLIs** (only to fill gaps A1 names): `uw` (Unusual Whales),
  `fz` (Finviz), and the `uw-daily-analysis/scripts/` enrichers
  (`fred_macro.py`, `finnhub_enrich.py`, `fz_enrich.py`).

## Rubrics (load before A3/A4)

- `rubrics/gap-rubric.md` — the required-input checklist + verdict table.
- `rubrics/direction-rubric.md` — fusing flow+chart → bias, conviction, reasons.
- `rubrics/pattern-rubric.md` — calling patterns honestly (confidence/target/invalidation).
- The canonical stock-deep-dive rubrics for sizing, confluence, invalidation,
  and citation tags — reused, not reinvented (`../stock-deep-dive/rubrics/…`).

## Schema & structured output

- `templates/trade-plan.json` — the envelope A4 fills.
- `schemas/trade_plan.schema.json` — its JSON Schema.
- `schemas/validate_trade_plan.py` — stdlib validator; A4 must make it print `OK`.

## Orchestration rules (mirror stock-deep-dive's discipline)

0. **One phase at a time, run → read → write.** Finish a phase's commands AND its
   MD before the next. Never batch a phase's `Write` with the command whose
   output it quotes. A number written before its source returned is fabrication.
1. **Reuse over re-pull.** Prefer the deep dive's numbers; only call live tools
   to fill a gap A1 explicitly flagged.
2. **No fabrication of levels or patterns.** Every level/pattern traces to
   `chart.json` or a deep-dive phase MD. The engine caps pattern confidence at
   `medium`; promotion to `high` needs a written, cited manual read.
3. **Honesty about gaps.** If a `critical` input is missing, the plan is
   watch-only / 0% — do not manufacture conviction.
4. **Two-sided always.** reasons_against is mandatory and must steelman the other
   side; the strongest opposing argument cannot be omitted.
5. **Cite upstream by path + tag.** Use `[CHART:…]` for chart-engine datapoints
   and the standard `[FLOW:]/[DP:]/[OI:]/[STRUCT:]/[HIST:]/[MACRO:]/[FUND:]/[SENT:]`
   tags for reused deep-dive datapoints.

## Execution

Read each `phases/phase-A*.md` in order (A0→A1→A2→A3→A4) and follow the embedded
instructions exactly, one phase fully before the next. After A4, surface the
plan path, direction + conviction, the one-line stock plan, the headline options
plan (target_price by target_date), the gap-audit verdict, and the reminder to
run `/trade-plan-eval <SYMBOL> <DATE>` after taking the trade.

Disclaimer to include at the top of every `trade-plan.md`: *"For research and
educational use only. Not financial advice. Sizing, structures, targets and
dates are illustrative."*
