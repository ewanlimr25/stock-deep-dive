# Phase A0 — Intake & Reuse Detection — PATH

- **Ticker:** PATH (UiPath Inc., NYSE)
- **As-of:** 2026-06-21 (Sat→Sun; last session Fri 2026-06-19). All look-backs `<= as_of`.
- **Version:** v1 (no prior `trade-plan.md` in `trade-plans/PATH/2026-06-21/`)
- **Output dir:** `trade-plans/PATH/2026-06-21/`

## Reuse detection

Dated deep-dive runs found (newest with `decision.json` wins):

| Run | decision.json | Note |
|-----|---------------|------|
| 2026-05-18 | ✗ | older, no decision.json |
| 2026-05-22 | ✓ | |
| 2026-05-29 | ✓ | |
| 2026-06-01 | ✓ | |
| 2026-06-05 | ✓ | |
| **2026-06-18** | ✓ | **REUSED** |

- **Reused deep dive:** `research/PATH/2026-06-18/` (generated 2026-06-20T13:33Z)
- **Age:** ~1 trading day (Thu 6/18 → as-of Sun 6/21; only Fri 6/19 elapsed). **NOT STALE** (< 10 trading days) → no staleness conviction cut.
- **Full phase set present:** phase-0 … phase-10 (flow, dark-pool, positioning, structure, historical, macro, insights, fundamentals, sentiment, agent-views, debate, trade-plan, audit). Complete substrate — do NOT re-pull flow/DP/OI/structure/macro/fundamentals/sentiment.
- **`flow_source` = `deep_dive`**

### Deep-dive read (the substrate to fuse in A3)
- **bias NEUTRAL, conviction 0.55, horizon 1-4w, spot $10.27, final size 0% (watch-only pass).**
- Thesis: *no-edge, counter-trend setup*. Lone bull pillar = 5-session sweep persistence (consistency 1.0, $2.27M) [FLOW] + 31.78% short float [SENT]; but bullish_flow backtests **37.5% (n=8, avg −0.51%)** [HIST] and dark-pool large-tier buy_ratio **0.48** refuses to confirm [DP]. Macro = headwind (hawkish FOMC 6/17, TRANSITIONAL regime, half-size).
- Levels: support **10.23**, resistance **10.79**, gamma_flip **10.00**, largest_pin **11.00**.
- Invalidation: two daily closes < **10.00** → breakdown toward 9.20 52w low.
- Gates: fundamentals CAUTION, sentiment CAUTION, crowd_state **CROWDED_SHORT**, debate_disconfirmed true.
- Catalysts: June CPI ~2026-07-15, FOMC ~2026-07-28 (hike risk), UiPath Q2 FY2027 earnings ~2026-09-08 (outside 30d).
- IV rank 34.55; front-expiry implied move 2.06% (~$0.21).

## Reasoning ledger

`trade-plans/_eval/reasoning-ledger.md` loaded. Lessons matched to this setup:

- **L-0002 (ACTIVE, setup:divergent)** — flow↔chart divergence is not a directional trade → default NEUTRAL/RANGE or defined-risk fade; log divergence as top reason_against. **APPLIES** (flow's lone bull pillar vs bearish chart/MA stack).
- **L-0004 (CANDIDATE, setup:divergent + short-gamma + fundamentals-veto)** — persistent sweep campaign in a short-gamma book with a live catalyst can squeeze on a *reclaim*; respect the veto. **PARTIALLY APPLIES** — PATH is near-spot short gamma ($10 strike gex −8.69M) with a 5-session bull sweep + 31.78% SI; but here the "catalyst" is undated (~Sept earnings), and fundamentals are CAUTION not VETO. Note as two-sided risk.
- **L-0003 (ACTIVE, setup:reused-deep-dive)** — stale flow decays. **NOT triggered** (deep dive ~1 trading day old).
- **L-0001 (ACTIVE, pattern:triangle/flag)** — confirm breaks before sizing. Hold pending A2 pattern read.

`ledger_lessons_applied` (provisional): L-0002, L-0004; (conditional on A2): L-0001.

## Chart source probe

- `python3 lib/chart_engine.py --ticker PATH --date 2026-06-21` → `available: true`, **source = yfinance** (371 daily sessions).
- Spot $10.27, sma20 11.13 / sma50 10.69 / sma200 13.01 (price below all → ma_stack mixed/bearish), RSI14 41.7 (neutral), ATR14 0.68 (7.07%), MACD hist −0.148 (bearish), BB 9.72–12.53.
- No tool errors. B1 (chart) is **not** a gap.

## Verdict for downstream

- `deep_dive_reused` = `research/PATH/2026-06-18/`
- `deep_dive_age_days` ≈ 1 trading day (NOT stale)
- `flow_source` = `deep_dive`
- `chart_source` = `yfinance`
- `ledger_lessons` = [L-0002, L-0004, (L-0001 pending A2)]
