# Phase A0 — Intake & Reuse Detection

- **Ticker:** PATH (UiPath Inc., NYSE) — passes `^[A-Z][A-Z0-9.]{0,5}$`
- **As-of:** 2026-07-13 (default = today, US/Eastern)
- **Version:** v1 (`trade-plans/PATH/2026-07-13/` was empty at intake — no overwrite)
- **Risk parameters:** defaults (fraction 0.25, cap 5%) — no user overrides

## Deep-dive reuse (flow substrate)

- **Reused run:** `research/PATH/2026-07-13/` — **same-day, age 0 trading days**. NOT stale.
- `decision.json` present and complete; all phase MDs present (phase-0 … phase-10).
- Runs available: 2026-05-18, 05-22, 05-29, 06-01, 06-05, 06-18, **07-13** (newest ≤ as_of picked).
- **flow_source = `deep_dive`** — no live `uw` re-pull needed at intake.

### decision.json headline (reused, not re-derived)

- bias **LONG**, conviction **0.55**, horizon **1–4w**, spot_reference **11.87**
- Thesis anchor: 2026-07-09 unattributed mega darkpool buy — 54.6M sh / $644M at the ask,
  buy_ratio 1.000 (~15x PATH's darkpool record) [DP:block_stratified]; $678.8M shelf at
  **$11.80** [DP:price_levels]; **28–32% of float short** [SENT:short_float].
- Levels: support 11.80 / resistance 13.00 (gamma wall) / gamma_flip 5.70 / largest pin 11.00
- Gates: fundamentals CAUTION, sentiment CAUTION, crowd_state **CROWDED_SHORT**,
  sector_rotation aligned, **debate_disconfirmed: true**
- Sizing (upstream): p 0.55, payoff_b 3.29, final_size_pct **1.0%** (quarter-Kelly, starter)
- Invalidation: daily close < 11.60; DP large-tier buy_ratio < 0.45; 07-09 block attributes
  as supply; hawkish macro (10y > ~4.8%) / breadth < 33.8%
- Context: BUSY_NAME_NORMAL_DAY, IV rank 40.4, expected front-expiry move ±5.3% ($0.63)
- Catalysts: CPI ~07-15, FOMC ~07-29, earnings 2026-09-03 (outside horizon)

## Prior trade plan (reference)

- `trade-plans/PATH/2026-06-21/` — bias **NEUTRAL**, conviction 0.55, spot 10.27,
  verdict SUFFICIENT. **Never marked to market** (no `/trade-plan-eval` run; ledger has no
  PATH-scoped lesson). Spot has since moved 10.27 → 11.85 (+15.4%).

## Reasoning ledger

Loaded `trade-plans/_eval/reasoning-ledger.md`. Lessons and applicability:

| id | status | scope match for PATH today | thread into |
|----|--------|---------------------------|-------------|
| L-0001 | ACTIVE | conditional — applies **if** A2/A3 land on chart-leads breakout (triangle/flag) | A3 entry style, A4 sizing |
| L-0002 | ACTIVE | conditional — applies **if** A3 finds flow↔chart DIVERGENT | A3 bias + conviction |
| L-0003 | ACTIVE | **not triggered** — reused deep dive is 0 days old | — |
| L-0004 | CANDIDATE | not matched — PATH book is long-gamma, bias LONG, no bearish-sweep-short setup | noted only |

## Chart source probe

```
python3 .claude/skills/trade-plan/lib/chart_engine.py --ticker PATH --date 2026-07-13
→ exit 0, "available": true, "source": "yfinance", "source_note": "373 daily sessions via yfinance"
→ spot 11.85, sma20 10.92, sma50 10.91, sma200 12.95, ma_stack "mixed"
```

- **chart_source = `yfinance`** — B1 available, no critical chart gap at intake.
- No tool errors.

## Verdict for downstream

- `deep_dive_reused`: `research/PATH/2026-07-13/` (decision.json + phase MDs)
- `deep_dive_age_days`: 0 (same-day — no staleness cut)
- `flow_source`: `deep_dive`
- `chart_source`: `yfinance`
- `ledger_lessons`: L-0001 (breakout sizing, conditional), L-0002 (divergent → no directional, conditional), L-0003 (not triggered), L-0004 (candidate, not matched)
