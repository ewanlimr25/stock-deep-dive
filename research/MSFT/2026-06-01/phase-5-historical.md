# Phase 5 — Historical Context & VRP

**Ticker:** MSFT
**As-of date:** 2026-06-01
**Generated:** 2026-06-02T11:10:47Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-1-flow.md, phase-4-structure.md

## Summary

History argues for **caution, not chase.** MSFT has rallied **+20% (≈$383→$460)**
over the 30-session window while **IV rank doubled (29.9→73.1)** — a *nervous,
vol-bid* rally, not a calm trend — and **`fz` RSI is 72.9 (overbought)**, price
extended +9.7%/+13.9% above its 20/50-day MAs, +12.9% on the month yet still
**−17% below the 52-week high and −4.8% YTD**. The decisive number: the
**`bullish_flow` signal class win-rate is 44.4% (N=9) with an average forward move
of −1.25%** — i.e. **edge-negative right now**. Vol is elevated in *level*
(HIGH_IV, IV30 33.4%, 91st pctile of available history) but only **FAIR** vs
realized (VRP +1.84 pts), so this is a mild premium-*selling* tape — consistent
with the heavy call writing seen in phases 1/3/4. OI has built **30/30
consecutive sessions (+3.13M)**, the one cleanly constructive signal, but 90-day
cumulative flow is **net +$955M yet MIXED** (no stealth accumulation). Dealer GEX
has been **stably POSITIVE since ~05-07** (no recent flip).

## Key signals

- **`bullish_flow` backtest: win_rate 44.4%, avg_move −1.25%, N=9** → **edge-
  negative** signal class; downgrade conviction `[HIST:signal_backtest]`.
- **Price +20% (383→460.52) with IV rank 29.9→73.1** — vol-bid rally, IV expanding
  *into* the move (unusual; hedged/chasing) `[HIST:trend]`.
- **VRP +0.0184 = FAIR** (IV30 33.4% vs RV30 31.5%); regime HIGH_IV, IV %ile 91.4
  over **35 sessions** (gap-limited, not a true year) `[HIST:vrp]` `[HIST:iv_percentile_zscore]`.
- **OI BUILDING 30/30 sessions, +3.13M net** — sustained engagement (but ~half
  written, per phase-3) `[HIST:oi_trend]`.
- **`fz` RSI 72.9 overbought, +12.9% on month, −17% below 52w high, −4.8% YTD** —
  chasing an extended mean-reversion bounce off the lows `[HIST:rsi fz]` `[HIST:52w_proximity fz]`.

## Detailed findings

### IV regime (percentile + z-score + VRP) `[HIST:iv_percentile_zscore]` `[HIST:vrp]`

- `regime`: **HIGH_IV**; `current_iv30d` **0.3339 (33.4%)**; `iv_percentile`
  **91.43**, `iv_zscore` **+1.215** — but `dates_used` = **35**, so this "252-day"
  percentile is computed over only **35 available sessions** (snapshot + gap
  limited): **directionally elevated, low-confidence as a true 1-year extreme.**
- VRP **+0.0184** (+1.84 vol pts), `realised_vol` 31.54%, `regime` **FAIR**. IV is
  high in level but only marginally rich vs realized → **mild premium-selling
  lean**, not a screaming sell and not cheap.

### Cumulative premium flow (90d) `[HIST:cumulative_premium_flow]`

`net_flow` **+$955.4M** (cumulative_bullish $14.21B vs bearish $13.25B = +7.2%),
`trend_direction` **MIXED**, over **36 sessions (2026-03-13 → 06-01, crosses the
21-session gap)**. Net bullish but mixed → **not** a persistent stealth build (the
≥60d-persistent-accumulation heuristic does **not** fire). Echoes the two-way theme
from phases 1–4.

### P/C ratio z-score (20d) `[HIST:pc_ratio_zscore]`

`current_pc_ratio` 0.2563, `mean_pc_ratio` 0.3221, `zscore` **−0.819**, `extreme`
**NORMAL**. Today is more call-heavy than the 20-day mean but **not an extreme
(|z|<2)** → no contrarian sentiment trigger from P/C alone.

### GEX time series (30 sessions) `[HIST:gex_time_series]`

`regime_flip_dates`: clustered **04-29 → ~05-07** (POS↔NEG several times at spot
$413–424, right after the gap). **No flip in the last ~17 sessions** → regime has
been **stably POSITIVE (long-gamma) since ~05-07** as price climbed to $460.
Confirms phase-4's current POSITIVE GEX is stable, not freshly flipped.

### OI trend (30 sessions) `[HIST:oi_trend]`

`overall_trend` **BUILDING**, `consecutive_build_days` **30** (every session),
`total_net_oi_change` **+3,134,661**. Relentless OI accretion through the rally —
sustained positioning growth. Constructive, but cross-read with phase-3: ~half the
*new* builds are inferred call writing, so this is "engagement building," not
unambiguous bullish accumulation.

### Multi-day trend (30 sessions, **spans gap**) `[HIST:trend]`

`days_analyzed` **30**, `date_range` **2026-03-23 → 2026-06-01** (includes the
03-28→04-24 hole — 30 *sessions*, not calendar days). `bullish_days` **14** /
`bearish_days` **16** (slightly more bearish sessions), `price_change` **383 →
460.52 (+20.2%)**, `iv_rank_change` **29.86 → 73.07**, `flow_direction_latest`
**bullish**. Read: a strong price advance on **balanced-to-slightly-bearish daily
flow with IV expanding** — the rally is not flow-propelled and is increasingly
hedged/nervous.

### Price context (`fz`, advisory) `[HIST:rsi fz]` `[HIST:52w_proximity fz]`

RSI(14) **72.86 (overbought)** · price vs SMA20 **+9.67%**, SMA50 **+13.92%**,
SMA200 **+0.51%** · Perf Month **+12.93%**, Perf YTD **−4.78%** · 52W High
**$555.45 (−17.09%)**, 52W Low **$356.28 (+29.26%)**. The move is a sharp
mean-reversion bounce off the lows; price is overbought and extended above
short-term MAs but has large overhead room to the highs. **Tempers a fresh-breakout
thesis** — chasing calls into RSI 73 after +29% off the low.

### Signal backtest `[HIST:signal_backtest]`

`signal_type` bullish_flow, `lookback_days` 5: **`win_rate` 44.4%, `total_signals`
9, `avg_move_pct` −1.25%**. Re-run once to confirm (not the empty stub). **Below
the 0.45 edge line AND negative average move** → the current signal class is
**historically edge-negative**. Market-wide base rate (tool is not symbol-scoped),
small N → low confidence but clearly cautionary.

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|------------------|--------------------------|-----------|
| `uw historical iv-percentile-zscore --symbol MSFT --lookback-days 252 --json` | %ile 91.43, z 1.215, HIGH_IV, dates_used 35 ← `.iv_percentile,.iv_zscore,.regime,.dates_used` | 35 sess |
| `uw historical vrp --symbol MSFT --realised-window-days 30 --json` | VRP +0.0184 FAIR, RV 31.54% ← `.vrp,.regime,.realised_vol` | 30 |
| `uw historical cumulative-premium-flow --symbol MSFT --days 90 --json` | net +$955.4M MIXED, 36 sess ← `.net_flow,.trend_direction,.dates_covered` | 36 |
| `uw historical pc-ratio-zscore --symbol MSFT --lookback-days 20 --json` | z −0.819 NORMAL ← `.zscore,.extreme` | 20 |
| `uw historical gex-time-series --symbol MSFT --days 30 --dte-max 45 --json` | last flip ~05-07, stable POS ← `.regime_flip_dates` | 30 |
| `uw historical oi-trend --symbol MSFT --days 30 --top-n 10 --json` | BUILDING 30/30, +3.13M ← `.overall_trend,.consecutive_build_days,.total_net_oi_change` | 30 |
| `uw historical trend --symbol MSFT --days 30 --json` | +20.2% px, IV 29.9→73.1, 14/16 days ← `.price_change,.iv_rank_change,.bullish_days` | 30 |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20 --json` | win 44.4%, avg −1.25%, N=9 ← `.win_rate,.avg_move_pct,.total_signals` | 9 (mkt-wide) |
| `fz quote MSFT --agent` | RSI 72.86, −17.09% vs 52wH, Perf YTD −4.78% ← `.fundamentals.*` | 1 |

## Tool errors

None. (Several first-pass `jq` extractions used wrong key names — `current_iv`,
`cumulative_premium`, `series` — returning null; corrected against the actual
`keys_unsorted` and re-read. No null/wrong value was carried into the findings.)

## DATA NOTE / CORRECTION

- **Gap-aware N:** the 252-day IV percentile uses only **35 sessions** and 90-day
  cumulative flow only **36 sessions** (the snapshot spans 03-13→06-01 across the
  21-session 03-28→04-24 hole). Percentiles/sums are over *available* sessions, not
  the calendar window — treat absolute percentiles as directional, not precise.
- **Latest-anchor:** all `uw historical` reads here (no `--date` support) anchor to
  the latest available date = **2026-06-01** (= as-of), so this run is reproducible
  *as of this snapshot*; a later session landing would shift every trailing value.

## Verdict for downstream phases

- **Volatility regime: RICH in level, FAIR vs realized** (HIGH_IV, IV30 33.4%, 91st
  pctile-of-35; VRP +1.84 pts) → **mild premium-SELLING environment** (favor credit
  / defined-risk over naked long premium).
- **Premium environment:** seller-leaning, not a clean debit setup — buying calls
  here pays elevated IV into an overbought, mean-reverting tape.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE: 2/5 (LOW).** The
  bullish_flow backtest is sub-0.45 with a negative avg move; flow is mixed; price
  overbought/extended. Only OI-building (30/30) is constructive, and it is half-written.
- **Three specific datapoints:** IV %ile **91.43** (35 sess); VRP **+0.0184 (FAIR)**;
  signal win rate **44.4%** (avg move −1.25%, N=9).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:     bullish_flow
  signal_backtest_win_rate: 0.444
  win_rate_n:       9
  win_rate_source:  backtest        # market-wide base rate, NOT MSFT-specific; small N
  ```
  Kelly `p` = 0.444 (below break-even for most debit structures); phase-9 applies
  the N-conditional cap (N=9 is small → lean toward the conviction-bin floor).
- **Open questions:** Does the macro phase (6) explain the IV-up-into-rally
  (front-end backwardation = event premium)? Given premium-selling regime + edge-
  negative bullish backtest + overbought price, should phase-9 favor a *credit/fade*
  or *defined-risk* structure over long calls? Does fundamentals (7b) justify the
  +20% re-rate or is it sentiment?
