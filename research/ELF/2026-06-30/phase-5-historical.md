# Phase 5 — Historical Context & VRP

**Ticker:** ELF
**As-of date:** 2026-06-30
**Generated:** 2026-07-01T00:32:25Z
**Upstream phases cited:** phase-0-intake.md, phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's bullish flow sits on top of a **major recovery rally that is now
short-term extended and structurally rich, not cheap.** Over the last 30 sessions
ELF ran **+34.9% ($54.86 → $74.00)** while IV rank **collapsed 92.6 → 46.8** — a
classic post-fear-peak recovery with vol crush (IV rank was ~98 on 2026-05-20).
Volatility is a **PREMIUM-SELLING regime** (IV30 0.67 > realized 0.589, VRP +0.081)
— favor credit/defined-risk structures over buying naked premium. OI has been
**BUILDING for 25 consecutive days (+128k net)** — genuine month-long position
accumulation behind the move — yet the **90-day cumulative premium flow is net
BEARISH −$9.5M (trend MIXED)**, so today's bullish spike is a *recent reversal*, not
a persistent ≥60-day stealth build. The bullish_flow signal class backtests at
**62.5% (n=8, market-wide)** — edge-positive but small-N. Net: the momentum is real
and OI-confirmed, but the entry is late (extended), vol is rich, and the dealer
structure (phase-4) votes mean-reversion — a "don't chase / defined-risk" historical
posture.

## Key signals

- **+34.9% in 30 sessions ($54.86→$74.00), IV rank 92.6→46.8** — extended recovery + vol crush [HIST:trend]
- **VRP +0.0806 → PREMIUM_SELLING** (IV30 0.67 vs RV30 0.589) — favor credit structures [HIST:vrp]
- **OI BUILDING 25 consecutive days, +127,955 net** — month-long accumulation behind the rally [HIST:oi-trend]
- **90d cumulative premium NET BEARISH −$9.5M, MIXED** — today's bullish flow is a reversal, not a 60d+ build [HIST:cumulative-premium-flow]
- **bullish_flow backtest win_rate 62.5%, n=8** — edge-positive base rate, small N, market-wide [HIST:signal-backtest]

## Detailed findings

### IV regime `[HIST:iv-percentile-zscore][HIST:vrp]`

- **IV percentile: 61.82** over `dates_used = 55` sessions (gap-affected window; z-score
  returned null this build). Mid-elevated — not a vol extreme.
- **IV rank now 46.83**, down from **92.56 → 46.83** over 30d (`trend` `iv_rank_change`)
  — vol has been crushed as price recovered.
- **VRP = +0.0806** (`iv30d` 0.67 − `realised_vol` 0.5894, 30d window). `regime =
  PREMIUM_SELLING` — "Options pricing more vol than realised — favour premium selling."
  → For phase-9: **debit/naked-long premium is disadvantaged; credit spreads / covered
  structures are favored.**

### Cumulative premium flow — 90d `[HIST:cumulative-premium-flow]`

- `cumulative_bullish` $106.06M vs `cumulative_bearish` $115.56M → **net_flow −$9.51M**,
  `trend_direction = MIXED`. Window = 90 calendar days but **only 56 sessions present**
  (`dates_covered` length 56; spans 2026-03-13→06-30 with the ~31-day April hole).
- Read: **no persistent ≥60d bullish build.** The stealth-accumulation heuristic
  (cumulative + and persistent) does **not** fire — today's +$1.22M is a spike against a
  net-bearish 90d backdrop (heavy put/bearish premium during the earlier decline).

### P/C ratio z-score `[HIST:pc-ratio-zscore]`

- `current_pc_ratio` 0.1841, **z = −1.009**, `NORMAL`. Today is more call-heavy than the
  20-day norm (~1σ) but **not an extreme (|z|<2)** → no contrarian-fade trigger yet;
  hand to phase-8b/contrarian to watch if it stretches.

### GEX time series — 30d `[HIST:gex-time-series]`

- `regime_flip_dates`: 2026-05-26 (POS→NEG), 05-27 (NEG→POS), 06-09 (POS→NEG), 06-10
  (NEG→POS). All flips occurred when **spot was ~$53–59, near the then-ZGL (~$54–58)**.
- **No flip in the last ~20 sessions** (since 06-10). With spot now $74 vs ZGL ~$60
  (phase-4), the regime is **decisively and stably long-gamma** — dealer hedging is not
  in transition; the phase-4 mean-reversion read is stable, not a fresh flip.

### OI trend — 30d `[HIST:oi-trend]`

- `overall_trend = BUILDING`, `consecutive_build_days = 25`, `total_net_oi_change =
  +127,955`. **Positions have accumulated for a full month** behind the +35% move — the
  structural build phase-3 couldn't see in a single-day snapshot. (Both true: month-long
  BUILD, but *today* specifically was churn — the rate of new positioning has cooled.)

### Multi-day trend `[HIST:trend]` (30d, 2026-05-18 → 06-30, days_analyzed 30)

- `price_change`: **$54.86 → $74.00 (+34.9%)**; `iv_rank_change`: **92.56 → 46.83**.
- `bullish_days` 15 / `bearish_days` 15 (balanced daily flow even as price rose +35% —
  the gains came on a handful of strong sessions, incl. 06-30 +5.9%).
- `flow_direction_latest = bullish`.
- Trajectory: fear-peak ~05-18/20 (IV rank 92–98, close ~$51–55) → steady recovery →
  acceleration into $74. **Short-term extended:** +17% in the last 6 sessions (phase-2),
  +5.9% on the as-of day, closing at the highs.

### Price context (`fz` D8 cross-check)

- **n/a this run** — the `fz` fundamentals grid is degraded to 14 fields (phase-0), with
  no `RSI (14)` / `SMA50` / `SMA200` / `52W High/Low`. UW-derived proxy stands in: the
  +34.9%/30d move with IV rank crushed to 46.8 and price at local highs is the
  functional equivalent of an **overbought, extended** read — tempering a
  fresh-breakout thesis. (Advisory only; not in the Kelly `p`.)

### Signal backtest `[HIST:signal-backtest]`

- `--signal-type bullish_flow --lookback-days 5`: **win_rate = 62.5%**, `total_signals =
  8`, no empty-stub note. Populated on first read (no re-run needed).
- >0.45 → **historically edge-positive**, but **n=8 is small (<10 = low-confidence)** and
  the rate is a **market-wide base rate for the bullish_flow class, not ELF-specific.**

## Tool calls (audit trail)

| Command (+ args) | Key value(s) ← `jq` path | Rows used |
|---|---|---|
| `uw historical iv-percentile-zscore --symbol ELF --lookback-days 252` | iv_percentile 61.82, dates_used 55 ← `.iv_percentile`,`.dates_used` | 55 sess |
| `uw historical vrp --symbol ELF --realised-window-days 30` | VRP +0.0806 PREMIUM_SELLING ← `.vrp`,`.regime` | 30d |
| `uw historical cumulative-premium-flow --symbol ELF --days 90` | net −$9.51M MIXED ← `.net_flow`,`.trend_direction`; 56 dates ← `.dates_covered\|length` | 56 sess |
| `uw historical pc-ratio-zscore --symbol ELF --lookback-days 20` | z −1.009 NORMAL ← `.zscore` | 20d |
| `uw historical gex-time-series --symbol ELF --days 30 --dte-max 45` | last flip 06-10 ← `.regime_flip_dates` | 30d |
| `uw historical oi-trend --symbol ELF --days 30 --top-n 10` | BUILDING, 25 consec, +127,955 ← `.overall_trend`,`.consecutive_build_days`,`.total_net_oi_change` | 30d |
| `uw historical trend --symbol ELF --days 30` | +34.9%, IV rank 92.6→46.8 ← `.price_change`,`.iv_rank_change` | 30 sess |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 20` | win_rate 62.5%, n 8 ← `.win_rate`,`.total_signals` (market-wide) | 8 signals |

## Tool errors

_None — all eight reads returned exit 0 and valid JSON._

## DATA NOTE / CORRECTION

- **Gap-aware N:** the 90d cumulative-flow window spans 90 calendar days but only **56
  actual sessions** (`dates_covered` length; ~31-day April hole 2026-03-27→04-27, per
  phase-0). IV percentile uses `dates_used = 55`. Percentiles/sums are over sessions
  *present*, not the calendar span — not annualized across the hole.
- **Latest-anchor caveat:** all trailing reads (iv-percentile, vrp RV leg, cum-flow,
  pc-z, gex-series, oi-trend, trend, backtest) anchor to the **latest available date =
  2026-06-30** (= our as-of). A re-run after a new session lands would shift them.

## Verdict for downstream phases

- **Volatility regime:** **FAIR-to-RICH** — IV percentile 61.8, IV rank 46.8 (crushed
  from 92.6), **VRP +0.081 = PREMIUM_SELLING.** Not cheap; **favor credit / defined-risk
  structures**, avoid buying rich naked premium (phase-9 structure selection).
- **Premium environment:** **premium-SELLING** (IV > realized). Debit-long-vol is
  disadvantaged.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **3 / 5.** For it:
  62.5% bullish_flow backtest, 25-day OI build, stable long-gamma. Against it: extremely
  **extended** (+34.9%/30d, +17%/6d), 90d cumulative net-**bearish**, premium-selling
  vol, phase-4 mean-reversion structure. Positive edge, but a *late/rich* entry.
- **Three specific datapoints:** IV percentile **61.8**; VRP **+0.0806 (PREMIUM_SELLING)**;
  bullish_flow signal win-rate **62.5% (n=8)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.625
  win_rate_n:                8
  win_rate_source:           backtest
  # NOTE: market-wide base rate, NOT ELF-specific; n=8 (<10) → low-confidence,
  #       apply the N-conditional Kelly cap (rubrics/sizing-rubric.md).
  ```
- **Open questions:**
  - What drove the mid-May **fear peak (IV rank ~98) and the −? decline** before this
    recovery — earnings, guidance, a sector event? (phase-6/7b/7c must establish the
    fundamental base the rally is recovering from.)
  - Does 90d net-bearish + premium-selling vol mean the recovery is **short-covering /
    mean-reversion of an oversold**, rather than fresh bullish conviction? (phase-7c
    short interest, phase-8 contrarian.)
  - Is the +35%/30d run **too extended to chase** at $74 into the $75 gamma wall
    (phase-4)? Sizing/structure must respect the late entry.
