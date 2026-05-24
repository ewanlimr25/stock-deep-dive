# stock-deep-dive

A Claude Code skill that runs an end-to-end, multi-phase institutional deep
dive on a single US-listed ticker — synthesizing options flow, dark pool
prints, dealer positioning, historical IV/GEX context, macro regime, deep
fundamentals, a parallel multi-agent analyst desk, and a bull/bear debate into
an actionable trade blueprint with a 0-100 confluence audit and a structured,
calibration-ready `decision.json`.

Designed for users who already have access to the [Unusual Whales MCP server
(`uw-pp`)](https://github.com/) and want repeatable, immutable, file-based
research artifacts for every ticker they study.

## Install

Clone (or symlink) this directory into your Claude Code skills path:

```bash
# user-level install
ln -s ~/Development/stock-deep-dive ~/.claude/skills/stock-deep-dive

# project-level install
ln -s ~/Development/stock-deep-dive .claude/skills/stock-deep-dive
```

Then in any Claude Code session: `/stock-deep-dive NVDA` (or any US ticker).

## Requirements

- Unusual Whales MCP server (`uw-pp`) configured and authenticated.
- WebSearch + WebFetch tools available (used as fallback for macro data).
- `python3` on PATH (stdlib only — used to validate `decision.json`; no pip
  installs required).
- Optional: `FRED_API_KEY` (free) for hard inflation/rate/labor series in
  phase-6 — otherwise WebSearch fallback. Register at
  https://fred.stlouisfed.org/docs/api/api_key.html.
- Optional: `FINNHUB_API_KEY` (free) for phase-7b deep fundamentals — otherwise
  the fundamental veto degrades to `NA` and the run proceeds on flow + UW
  insights. Register at https://finnhub.io/register.
- Optional: the following analyst sub-agents on the user's machine —
  `accumulation-hunter`, `contrarian-scanner`, `sweep-tracker`,
  `earnings-scout`, `risk-monitor`. Phase 8 will degrade gracefully if any
  are missing (writes a `MISSING: <agent>` line and continues).

## What gets produced

For each run:

```
research/<TICKER>/<YYYY-MM-DD>/
  phase-0-intake.md         intake + sanity checks
  phase-1-flow.md           options flow (sweeps, premium, IV outliers)
  phase-2-dark-pool.md      block prints + price levels
  phase-3-positioning.md    OI buildup, pin risk, rolls
  phase-4-structure.md      dealer GEX/DEX, vanna/charm, term skew
  phase-5-historical.md     IV percentile, VRP, GEX time series, signal backtests
  phase-6-macro.md          regime + CPI/NFP/FOMC + sector rotation + correlation
  phase-7-insights.md       UW composite confluence (insights_*)
  phase-7b-fundamentals.md  FINNHUB statements/surprise/peers/MSPR — quality veto
  phase-8-agent-views.md    5 analyst sub-agents in parallel
  phase-8b-debate.md        bull vs bear disconfirmation (1–2 rounds)
  phase-9-trade-plan.md     PM-voice blueprint (thesis, structures, sizing)
  decision.json             machine-resolvable envelope (validated)
  phase-10-audit.md         0-100 confluence + contradiction log
```

The blueprint is sized on the **empirical** signal win-rate that phase-5
backtests (not the narrative conviction), then run through four risk gates —
fundamental veto (7b), cross-name correlation (6/8), sector rotation (6), and
bull/bear disconfirmation (8b) — each of which can only cut size, never add it.

## Design principles

1. **Composite first.** Prefer `insights_deep_dive`, `insights_signal_confluence`,
   and `insights_conviction_matrix` over re-implementing confluence math.
2. **Immutability.** Outputs are never overwritten — re-runs on the same day
   append `-v2.md` and reference the prior version.
3. **No mocks.** Tool errors surface verbatim in the phase MD; the run
   continues with what's available.
4. **Citation discipline.** Every numeric claim in phase-9 must be tagged
   (`[FLOW:]`, `[DP:]`, `[OI:]`, `[STRUCT:]`, `[HIST:]`, `[MACRO:]`,
   `[AGENT:<name>]`) and resolve to an upstream phase file.
5. **Free macro only.** UW `risk_market_regime` first; FRED-free series second;
   WebSearch + WebFetch fallback. Never silently substitute a paid feed.

## Layout

```
SKILL.md            entry point + when-to-invoke + phase graph
phases/             one detailed prompt per phase (12 files: 0–10 + 7b/8b)
templates/          shared MD skeletons (phase + trade plan) + decision.json
rubrics/            confluence, invalidation, sizing, citation conventions
schemas/            decision.schema.json + stdlib validate_decision.py
commands/           /deep-dive-calibration — the outcome/calibration loop
research/           run outputs — gitignored
```

## Calibration loop

The deep dive generates blueprints; `/deep-dive-calibration` measures them.
Once you have a handful of dated `decision.json` files, run:

```
/deep-dive-calibration
```

It resolves each past blueprint to WIN / LOSS / INCONCLUSIVE on a horizon-matched,
**path-aware ±1R** window (using each plan's own invalidation rule), Brier-scores
calls by their phase-10 confluence band, and attributes hit-rate to the phases
and UW tools that fired. Propose-only — it never edits the phase prompts, it tells
you which ones to trust. This is what converts the confluence score from an
assertion into a measured edge.

## Not a substitute for

- `trade-analysis` skill — that one runs the 12-agent buy-side memo flow with
  yfinance/Finnhub data and CFA-style validation. Use it when the user wants a
  hedge-fund memo, not a flow-driven blueprint.

## Disclaimer

For research and educational use only. Not financial advice. Sizing guidance
is illustrative and assumes the reader supplies their own portfolio context
and risk limits.
