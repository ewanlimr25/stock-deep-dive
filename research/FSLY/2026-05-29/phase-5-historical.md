# Phase 5 — Historical Backtest & Win-Rate

## Summary

The empirical layer is **mixed-constructive with one genuinely interesting edge**:

- **Matched signal `bullish_flow`**: universe in-sample win-rate **60.0% (5d) /
  72.9% (10d), avg move +5.18%/+5.61%, N=70** `[HIST:signal-backtest]`. Same caveat as
  always — universe-pooled, in-sample, not FSLY-specific — so a *prior on the setup*,
  not a measured FSLY edge.
- **VRP is the standout**: **VRP −0.566, regime PREMIUM_BUYING** — realized vol
  (**144%**) is far *above* IV30d (**88%**), so despite high nominal IV, **options are
  cheap relative to how much FSLY actually moves** `[HIST:vrp]`. For a squeeze-ladder
  long-premium expression (phase-3/4), this is the friendliest possible vol backdrop:
  you're not overpaying for the optionality.
- **OI is building steadily**: **4 consecutive OI-build days**, and on 5/29 **138
  contracts increased vs 37 decreased (net +6,062)**, led by the 20C/30C 7/17 calls
  `[HIST:oi-trend]` — quiet, persistent call accumulation even as price chops.
- **But price action is choppy, not trending**: flow direction is **4 bullish / 4
  bearish over 8 sessions** `[HIST:trend]`; the last 3 (5/27→5/29) flipped bullish
  (P/C 0.37→0.10→0.27) but this is a volatile name that reverses fast (+7.8% 5/26 →
  −4.7% 5/27).

**Sizing implication:** use base **p ≈ 0.60** (the 5d `bullish_flow` rate, haircut
for in-sample + the quiet-day context), avg win ~+5%. The **PREMIUM_BUYING VRP**
genuinely supports a long-premium / defined-risk structure over shares. But the
choppy 4/4 flow split and the quiet tape (phase-0.5) cap this at **small / fractional
Kelly** — a tactical squeeze-optionality bet, not a conviction position.

## Signal backtest (`uw historical signal-backtest`) `[HIST:signal-backtest]`

| Signal | Horizon | Win-rate | Avg move | N |
|--------|---------|----------|----------|---|
| **bullish_flow** | 5d | **60.0%** | +5.18% | 70 |
| **bullish_flow** | 10d | **72.9%** | +5.61% | 70 |
| volume_spike | 5d/10d | n/a (undirected) | +1.2% / +2.3% | 82 |
| high_iv_rank | 5d/10d | n/a | +4.3% / +8.2% | 89 |
| dark_pool_accumulation | — | — | — | **0 signals** |

- `bullish_flow` is the matched class (FSLY's net-call lean) → **60% (5d) / 73%
  (10d)**, +5% avg. `dark_pool_accumulation` = 0 signals (FSLY's $10.5M mild-buy DP
  was below the detector's bar — consistent with phase-2's "small accumulation").
- **Caveat:** these are universe-pooled, in-sample — an optimistic ceiling, not a
  FSLY edge.

## FSLY time-series context `[HIST:]`

| Metric (`uw historical`) | Value | Read |
|--------------------------|-------|------|
| P/C-ratio z-score (20d) | **−0.76** | mild call-lean, NOT extreme (0.27 vs 0.41 mean) |
| IV percentile (252d) | 44.1 | mid; IV z −0.40 |
| **VRP** | **−0.566 (PREMIUM_BUYING)** | RV 144% >> IV 88% → **options cheap vs realized** |
| Flow direction (8d) | **4 bull / 4 bear** | choppy, not trending; last 3 bullish |
| OI build | **4 consecutive build days**, +6,062 on 5/29 (138 up / 37 down) | persistent call accumulation |

## Kelly inputs handed to phase-9

- p ≈ **0.60** (5d `bullish_flow`; 10d = 0.73), avg win ~+5%.
- **VRP −0.566 (PREMIUM_BUYING)** → long premium / defined-risk is *favored* by vol
  (rare green light for buying options on a high-IV name).
- **Caveat tag:** win-rate universe-pooled/in-sample; phase-0.5 context is
  BUSY_NAME_NORMAL_DAY/QUIET → keep size small, let the gates cut.

## Tool calls

```bash
uw historical signal-backtest --signal-type bullish_flow --lookback-days 5  --top-n 100 --json
uw historical signal-backtest --signal-type bullish_flow --lookback-days 10 --top-n 100 --json
uw historical pc-ratio-zscore      --symbol FSLY --json
uw historical iv-percentile-zscore --symbol FSLY --json
uw historical vrp                  --symbol FSLY --json
uw historical trend                --symbol FSLY --days 8 --json
uw historical oi-trend             --symbol FSLY --json
```

## Tool errors

none (signal-backtest is universe-level/in-sample by design — noted, not an error).

## Read-through

- The empirical layer is **genuinely supportive on two specific axes** the rest of
  the dive needed: (1) **VRP says options are cheap vs realized** — so the squeeze-
  ladder long-premium thesis (phase-3/4) isn't fighting overpriced vol; (2) **OI is
  building 4 days straight** on the call side — quiet, persistent positioning under a
  choppy price.
- It is **un-supportive on conviction**: the matched win-rate is universe-pooled
  (not FSLY), and price flow is a 4/4 coin-flip over 8 sessions in a name that
  whipsaws ±5–8% — so the *timing* edge is weak even if the *structure* is bullish.
- **Reconciliation:** this is the classic *armed-but-not-triggered squeeze* — bullish
  OI build + cheap vol + short base (phase-3) but quiet flow + choppy price + dampening
  gamma (phase-1/4). The empirical read says: **express it as cheap, defined-risk
  upside optionality (VRP favors it), sized small (choppy/quiet caps p)** — wait for
  the volume ignition rather than paying up for immediacy.

## Citations

- `[HIST:signal-backtest]` bullish_flow 60% (5d) / 72.9% (10d), avg +5%, N=70 — `uw historical signal-backtest`
- `[HIST:vrp]` VRP −0.566 PREMIUM_BUYING (RV 144% >> IV 88%) — options cheap vs realized — `uw historical vrp`
- `[HIST:oi-trend]` 4 consecutive OI-build days, +6,062 on 5/29 (138 up/37 down), call-led — `uw historical oi-trend`
- `[HIST:trend]` flow 4 bull / 4 bear over 8 sessions — choppy, not trending — `uw historical trend`

## Upstream references

- phase-3-positioning.md §Summary — "$20/$22.5 squeeze ladder, armed not triggered";
  phase-5's 4-day OI build + cheap VRP say the arming is *persistent* and the
  optionality is *cheap* — but the 4/4 choppy flow says the trigger hasn't fired.
- phase-4-structure.md §Read-through — "high IV is the cost of admission"; phase-5's
  VRP (−0.566) *refines* that: IV is high nominally but **cheap vs realized**, so
  long premium is actually favored here.

## Next phase

- phase-6-macro.md (is the tape — risk regime, tech-sector flow, correlation — a
  tailwind for a small-cap squeeze-optionality long?)
