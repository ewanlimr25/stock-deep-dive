# Phase 5 — Historical Backtest & Win-Rate

## Summary

The empirical record is **constructive for the bull case, with caveats on
specificity.** The signal that matches CRM's setup best — `bullish_flow` — backtests
to a **60.0% win-rate at 5 trading days (avg move +5.18%, N=70)** and **72.9% at 10
days (avg +5.61%)** across the universe. These are *cross-sectional* in-sample
backtests (the CLI doesn't isolate CRM-only signals), so treat them as a **prior on
the setup, not a CRM-specific edge** — the methodology note explicitly says
"in-sample backtest — not a robust live edge."

CRM-specific time-series context sharpens it:
- **P/C-ratio z-score −1.92** (today 0.235 vs 20-day mean 0.697, σ 0.241) — today is
  ~2σ more call-heavy than CRM's own recent norm. Labeled "NORMAL" by the extreme
  detector (just inside the −2 band), but it is a strong directional tilt.
- **IV percentile 35.3 / z −0.61, regime NORMAL** — IV is *below* its 252-day norm
  (crushed into the move). Options are not expensive; **buying premium is viable**,
  and there's no rich-vol headwind to a long.
- **Flow regime just flipped**: flow_direction was **bearish 5/27 & 5/28** (5/28 had
  $84.2M *put* premium, P/C 0.66 — pre-event hedging) → **bullish 5/29** (P/C 0.235).
  This is a **day-1 directional regime flip**, not a mature trend — historically the
  highest-information, but also highest-variance, point.

**Sizing implication (for phase-9 Kelly):** use a **base win-rate p ≈ 0.60–0.65**
(the 5–10d `bullish_flow` band, haircut for in-sample optimism and the phase-2
dark-pool divergence), avg win ≈ +5%, with the understanding that **N is universe-
pooled, not CRM-specific** → keep Kelly fractional. This is a *positive-expectancy
but not high-conviction* empirical anchor.

## Signal backtest (`uw historical signal-backtest`) `[HIST:signal-backtest]`

| Signal | Horizon | Win-rate | Avg move | N |
|--------|---------|----------|----------|---|
| **bullish_flow** | 5d | **60.0%** | +5.18% | 70 |
| **bullish_flow** | 10d | **72.9%** | +5.61% | 70 |
| volume_spike | 5d | n/a (undirected) | +1.21% | 82 |
| volume_spike | 10d | n/a | +2.26% | 89 |
| high_iv_rank | 5d | n/a (undirected) | +4.34% | 89 |
| high_iv_rank | 10d | n/a | +8.17% | 89 |
| dark_pool_accumulation | — | — | — | **0 signals** |

- `bullish_flow` is the matched signal (CRM is a top-net-bullish-flow name today) →
  **60% (5d) / 73% (10d)** with a +5% average move is the primary read.
- **`dark_pool_accumulation` returned 0 signals** — fully consistent with phase-2:
  there is **no** dark-pool *accumulation* footprint to backtest; the DP tape was
  distribution. (A useful cross-check that phase-2's read isn't noise.)
- `volume_spike` / `high_iv_rank` are undirected (no win-rate) but show positive
  average drift after such days (+2–8%), a mild tailwind.

## CRM time-series context `[HIST:]`

| Metric (`uw historical`) | Value | Read |
|--------------------------|-------|------|
| P/C-ratio z-score (20d) | **−1.92** | today ~2σ more call-heavy than norm — strong tilt |
| current vs mean P/C | 0.235 vs 0.697 | flow regime shifted call-side |
| IV percentile (252d) | 35.3 | IV below norm — crushed |
| IV z-score | −0.61 | NORMAL/cheap-side |
| Flow direction 5/27→5/29 | bearish → bearish → **bullish** | **day-1 regime flip** |
| 5/28 put premium | $84.2M (P/C 0.66) | pre-event hedging the day before |

## Kelly inputs handed to phase-9

- p ≈ **0.60** (conservative; the 5d matched-signal rate, haircut not applied yet —
  phase-9 applies the downside gates), up to 0.65 if the 10d horizon is used.
- avg win b ≈ **+5.2%**, and given complacent skew (phase-4) a defined-risk long can
  cap the loss leg.
- **Caveat tag:** win-rate is **universe-pooled / in-sample**, not CRM-specific →
  phase-9 must keep size fractional and let the phase-2 (dark-pool) and phase-7c
  (sentiment) gates cut it.

## Tool calls

```bash
uw historical signal-backtest --signal-type bullish_flow           --lookback-days 5  --top-n 100 --json
uw historical signal-backtest --signal-type bullish_flow           --lookback-days 10 --top-n 100 --json
uw historical signal-backtest --signal-type dark_pool_accumulation --lookback-days 10 --top-n 100 --json   # 0 signals
uw historical iv-percentile-zscore --symbol CRM --json
uw historical pc-ratio-zscore      --symbol CRM --json
uw historical trend                --symbol CRM --days 10 --json
```

## Tool errors

- `signal-backtest` takes no `--date` (anchors to latest available; in-sample by
  design — noted as a limitation, not an error).
- `trend` uses `--days` not `--lookback-days` (corrected).

## Read-through

- The historical layer **supports the bull thesis on balance**: the matched
  `bullish_flow` signal wins 60–73% with a +5% average move, IV is cheap (no vol
  headwind), and CRM's P/C is a ~2σ call-tilt. The +8.5% pop with a flow regime flip
  is statistically the kind of day that *tends* to see follow-through over 5–10
  sessions.
- **But two honest discounts:** (1) the win-rates are **universe-pooled in-sample**,
  not a CRM-specific live edge — optimism bias is real; (2) the **`dark_pool_
  accumulation` backtest found 0 signals**, a clean empirical echo of phase-2 — the
  one tape that historically precedes durable up-moves (institutional accumulation)
  is **absent** here; instead we have distribution. So the empirical tailwind is
  **flow-driven, not accumulation-backed.**
- **Reconciliation with phases 2 & 4:** history says bullish-flow days follow
  through more often than not (phase-4's positive gamma is the mechanism); but the
  missing accumulation signal (phase-2) is exactly why this should be sized as a
  **tactical momentum/continuation trade with a hard stop, not a conviction
  position.** p≈0.60, fractional Kelly.

## Citations

- `[HIST:signal-backtest]` bullish_flow 60.0% (5d) / 72.9% (10d), avg +5.2%, N=70 — `uw historical signal-backtest`
- `[HIST:signal-backtest]` dark_pool_accumulation = 0 signals (no accumulation footprint) — `uw historical signal-backtest`
- `[HIST:pc-ratio-zscore]` P/C z −1.92 (0.235 vs 0.697 mean) — `uw historical pc-ratio-zscore`
- `[HIST:iv-percentile-zscore]` IV pctile 35.3, z −0.61, regime NORMAL (cheap) — `uw historical iv-percentile-zscore`

## Upstream references

- phase-1-flow.md §Summary — "BULLISH, 20/20 call sweeps"; phase-5 gives that flow a
  **60–73% historical follow-through** and a +5% average move.
- phase-2-dark-pool.md §Summary — "distribution, not accumulation"; phase-5's
  `dark_pool_accumulation` backtest independently returns **0 signals**, confirming
  no accumulation tailwind — the edge here is flow-momentum, not smart-money buying.
- phase-4-structure.md §GEX — "positive gamma, mean-reversion"; the mechanism behind
  the 60–73% follow-through is dealer dip-buying into the call-long public.

## Next phase

- phase-6-macro.md (is the tape — risk regime, tech-sector flow, correlation — a
  tailwind or headwind for a tactical CRM long?)
