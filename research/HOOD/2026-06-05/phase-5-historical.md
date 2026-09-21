# Phase 5 — Historical Context & VRP

**Ticker:** HOOD
**As-of date:** 2026-06-05
**Generated:** 2026-06-07T12:50:00-04:00
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md,
phase-2-dark-pool.md, phase-4-structure.md

## Summary

HOOD is in a **high-IV, higher-realized** regime: IV30 71.85% sits at the
97.44th percentile of the available history (**dates_used = 39 sessions**, not
a true 1y — gap-aware N), yet **VRP is −0.0858** (realized 30d vol 80.43% >
implied) → the tool's own regime call is **PREMIUM_BUYING** ("Vol cheap vs
realised"). The tape's recent character explains it: the last five closes ran
90.73 → 88.16 → 82.85 → 88.33 → 82.47 (−6.0%, +6.6%, −6.6% swings), with 4/5
sessions bearish net flow (Σ ≈ −$39.9M) — phase-1's bearish day extends a week-long
distribution streak interrupted by one +6.6% bounce. GEX regime has flipped
**12 times in 30 sessions** (latest flip: the as-of day itself,
POSITIVE→NEGATIVE) — dealer-regime instability that empirically precedes
realized-vol expansion. The market-wide bearish_flow backtest:
**win_rate 87.5% on N=8** (avg 5-day move −2.73%) — edge-positive but
small-sample (<10 → low-confidence per rubric; phase-9 must cap).

## Key signals

- `iv_percentile` **97.44** / `iv_zscore` 1.994 / regime **HIGH_IV** — over
  **39 actual sessions** (gap 2026-03-30→04-24 excluded), not 252 calendar
  days [HIST:iv_percentile_zscore]
- `vrp` **−0.0858** (iv30d 0.7185 − realised 0.8043), regime
  **PREMIUM_BUYING**, interpretation verbatim: "Vol cheap vs realised — favour
  premium buying." [HIST:vrp]
- 90d cumulative flow ≈ flat: bullish $1.5704B vs bearish $1.5847B → net
  **−$14.26M over 40 sessions**, trend "MIXED" — i.e. the as-of day's −$13.58M
  equals the entire 40-session net imbalance; no stealth multi-week build
  either way [HIST:cumulative_premium_flow]
- **12 GEX regime flips in 30 sessions**; latest 2026-06-05 POSITIVE→NEGATIVE
  (spot 81.81 vs ZGL 87.45) — "GEX flip in last 5d" heuristic fires → expect
  larger ranges [HIST:gex_time_series]
- P/C z-score **−0.016** (current 0.40 vs mean 0.402, σ 0.124) — **NORMAL**, no
  sentiment extreme despite the bearish week; HOOD's P/C is *always* ~0.4
  (call-volume culture) [HIST:pc_ratio_zscore]
- OI `overall_trend` **BUILDING**: +1,819,088 net OI over 30 sessions,
  `consecutive_build_days` 30/30 — positions are being added, not abandoned,
  through the chop [HIST:oi_trend]

## Detailed findings

### IV regime [HIST:iv_percentile_zscore, HIST:vrp]

IV30 71.85% = 97.44th %ile (z +1.99) of the 39-session local history → rich
*for its own recent past*; but realized 30d is 80.43%, so VRP −8.6 vol pts →
**options are still cheap vs delivered movement**. Structural caveat: with
N=39 skewed to a high-vol stretch, the percentile overstates 1y richness; the
VRP read is the more robust of the two. Cross-check phase-4: front-end
backwardation (5d 77.7% vs 33d 70.0%) = the market already pays up for
near-term movement.

### Cumulative premium flow — 90d requested, 40 sessions present [HIST:cumulative_premium_flow]

`dates_covered` = 40 (2026-03-13→06-05, hole 03-28→04-24 excluded — matches
phase-0's local-dates list). Net −$14,255,526 on ~$3.16B two-way premium —
**balanced to a rounding error**; no 60d+ persistent institutional build.
The bearishness is concentrated in the *last five sessions* (below), not the
quarter.

### P/C ratio z-score [HIST:pc_ratio_zscore]

current 0.400 / mean 0.402 / z −0.016 → `extreme`="NORMAL". The 0.40 P/C that
looked call-heavy in phase-0.5 is exactly HOOD's 20-day baseline — no
contrarian sentiment extreme to fade.

### GEX time series [HIST:gex_time_series] (30 points, 2026-03-27→06-05, gap inside)

12 `regime_flip_dates` in the window — first 2026-04-27 (POS→NEG, ZGL 89.44),
last **2026-06-05 (POS→NEG, ZGL 87.45, spot 81.81)**. The ZGL has sat in the
high-80s while spot oscillated through it — an unstable hedging equilibrium;
tool note verbatim: "Empirically precedes realised-vol expansion." Trajectory
endpoint total_gex +32.6M vs −65.5M on 2026-03-27.

### OI trend [HIST:oi_trend]

BUILDING — every one of the 30 sessions net-positive OI (+1.82M cumulative).
As-of day: +64,097 net (683 contracts ↑ / 319 ↓); top builds = the Jun-12
87/89/90/91/93C + Sep-18 90/95C set already mapped in phase-3 (0DTE rows are
settlement artifacts). Sustained buildup, not a spike — the chain is getting
*more* loaded into Jun-18 OPEX, consistent with its 21.39% cliff (phase-3).

### Multi-day trend [HIST:trend] (`days_analyzed`=30 actual sessions,
`date_range` 2026-03-27→06-05 — window CROSSES the data hole; treated as 30
sessions, never a calendar trend)

- Window aggregates: bullish_days 14 / bearish_days 16; price 66.02 → 82.47
  (+24.9% over 30 sessions); iv_rank 31.37 → 49.59; `flow_direction_latest`
  "bearish".
- Recent 5 sessions (newest first in `daily_data`; pulled via `[:5]` — see
  DATA NOTE):

| Date | Close | Net flow | Direction | IV rank | P/C |
|---|---|---|---|---|---|
| 2026-06-05 | 82.47 | −$13,575,317 | bearish | 49.59 | 0.40 |
| 2026-06-04 | 88.33 | +$6,264,103 | bullish | 42.37 | 0.14 |
| 2026-06-03 | 82.85 | −$17,571,353 | bearish | 35.83 | 0.46 |
| 2026-06-02 | 88.16 | −$5,683,190 | bearish | 44.18 | 0.26 |
| 2026-06-01 | 90.73 | −$9,369,628 | bearish | 44.40 | 0.31 |

Daily swings −2.8%, −6.0%, +6.6%, −6.6% — realized vol delivering the 80%
print. 4/5 days bearish flow, Σ −$39.94M. **Decodes phase-2's DP price-levels:
90.73 / 88.16 / 82.85 / 88.33 / 82.47 are the five session closes** — the
"clusters" are largely EOD/benchmark prints at each close, softening the
overhead-supply read (it's positioning *throughput*, not a fortress).
06-03's −$17.6M was *more* bearish than the as-of day — the campaign predates it
(phase-1's 5/5 sweep-persistence agrees).

### Price context — `fz` advisory [HIST:rsi fz, HIST:52w_proximity fz]

RSI(14) **51.45** (neutral); price +2.49% vs SMA20, +5.39% vs SMA50,
**−20.16% vs SMA200**; Perf YTD **−27.08%**; 52W high 153.86 (price −46.4%
from it), 52W low 63.51 (+29.8% above). Read: a deep-drawdown name in a
2-month recovery (66→82.5 over the window) that stalled this week at ~90.
Advisory only — does not enter sizing.

### Signal backtest [HIST:signal_backtest] (market-wide, latest-anchored 2026-06-05)

`--signal-type bearish_flow --lookback-days 5`: **win_rate 87.5%,
total_signals 8**, avg_move_pct **−2.73%** (5-day horizon). Sample rows:
NVDA 06-03 −4.49%, SPY 06-03 −2.21% (wins), GOOGL 06-03 +2.66% (loss). This is
the **base rate of the signal class across the tape, not HOOD-specific**
(tool takes no --symbol). N=8 < 10 → low-confidence per pitfall; phase-9
applies the N-conditional cap from the sizing rubric.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol HOOD --lookback-days 252 --json` | 97.44 / 1.994 / N=39 ← `.iv_percentile, .iv_zscore, .dates_used` | 39 sessions |
| `uw historical vrp --symbol HOOD --realised-window-days 30 --json` | −0.0858 PREMIUM_BUYING ← `.vrp, .regime, .interpretation` | summary |
| `uw historical cumulative-premium-flow --symbol HOOD --days 90 --json` | net −$14,255,526, MIXED, N=40 ← `.net_flow, .trend_direction, .dates_covered\|length` | 40 sessions |
| `uw historical pc-ratio-zscore --symbol HOOD --lookback-days 20 --json` | z −0.016 NORMAL ← `.zscore, .extreme` | 20 sessions |
| `uw historical gex-time-series --symbol HOOD --days 30 --dte-max 45 --json` | 12 flips; last 06-05 POS→NEG ← `.regime_flip_dates`, `.trajectory[-1]` | 30 points |
| `uw historical oi-trend --symbol HOOD --days 30 --top-n 10 --json` | BUILDING, +1,819,088, 30/30 ← `.overall_trend, .total_net_oi_change, .consecutive_build_days` | 30 sessions |
| `uw historical trend --symbol HOOD --days 30 --json` | 14/16 days, 66.02→82.47 ← top-level; recent-5 ← `.daily_data[:5]` | 30 sessions |
| `uw historical signal-backtest --signal-type bearish_flow --lookback-days 5 --top-n 20 --json` | 87.5% / N=8 / −2.73% ← top-level `.win_rate, .total_signals, .avg_move_pct` | 8 signals |
| `fz quote HOOD --agent` | RSI 51.45, SMA200 −20.16%, YTD −27.08% ← `.fundamentals.*` | advisory |

All `uw historical` tools are latest-anchored (no `--date`); latest available
date = 2026-06-05 = as-of, so this run is point-in-time clean (a re-run after
new sessions land will shift every trailing value — engine behavior).

## Tool errors

(none. Data-quality caveats: (1) `iv-percentile-zscore` requested 252d but
`dates_used`=39 — percentile is over the local non-contiguous window;
(2) `trend.date_range` 03-27→06-05 crosses the 03-28→04-24 hole —
all reads quoted as session counts, never calendar trends.)

## DATA NOTE / CORRECTION

`daily_data` is ordered newest-first; an initial `[-5:]` slice returned the
five *oldest* rows (04-27…04-30 + 03-27). Re-pulled with `.daily_data[:5]` and
the recent-5 table above was written from that corrected read.

## Verdict for downstream phases

- **Volatility regime:** rich vs own history (97.4th %ile, N=39) but **cheap vs
  realized** (VRP −0.0858) → **premium-BUYING environment; favor debit
  structures** over credit despite the high IV print.
- **Premium-buying vs selling:** BUYING (tool-native regime label).
- **Conviction signal is historically edge-positive:** 3 — backtest 87.5% is
  strong but N=8 and market-wide; the 5-session bearish-flow streak + GEX
  instability + OI build into OPEX corroborate, the flat 90d cum-flow does not.
- **Three specific data points:** IV %ile 97.44 (N=39) · VRP −0.0858 ·
  bearish_flow win-rate 87.5% (N=8, market-wide, avg −2.73%/5d).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bearish_flow
  signal_backtest_win_rate: 0.875
  win_rate_n:       8
  win_rate_source:  backtest
  ```
- **Open questions:** What drove the ±6% daily swings of 06-01→06-05 (phase 6
  news)? Does the macro regime support a downside continuation, or was this
  week idiosyncratic re-pricing? With VRP negative, is the better expression
  long-options (debit put/put-spread) rather than short-stock?
