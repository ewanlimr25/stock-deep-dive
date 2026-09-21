# Phase 5 — Historical Context & VRP

**Ticker:** PDD
**As-of date:** 2026-05-26
**Generated:** 2026-05-26T20:40:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-4-structure.md, phase-0-intake.md

## Summary

The multi-week context is **mildly bearish drift into a rich-but-likely-to-be-realized
event, with no historical directional edge for the accumulation signal.** PDD has slid
from ~$102 (5/06) to **$96.58** (5/26) — 17 of the last 30 flow-days were net bearish.
It lives in a **persistent short-gamma regime** (FULLY_NEGATIVE on ~12 of the last 14
sessions) so realized vol is structurally amplified. At the term level vol is *not* rich:
IV30d 44% sits in the **12.9th percentile** (LOW_IV) with VRP **+7.2** (PREMIUM_SELLING)
— it is only the **3-day event weekly that is juiced to 98%** (phase-4). The
`dark_pool_accumulation` backtest returns **0 signals → no edge data** (win_rate_source
= null), so phase-9 cannot size on a measured directional rate. The `high_iv_rank`
backtest shows **77.8% vol-realization** (n=9, avg 5d move 4.84%) — the move usually
comes — but the two China peers in that sample, **FUTU −13.0% and TIGR −14.2%**, both
resolved *down*, a pointed cautionary read for a China ADR into earnings.

## Key signals

- **Mild downtrend:** close $102.31 (5/06) → $96.58 (5/26); 17 bearish vs 13 bullish
  flow-days over the window [HIST:trend]. Enters earnings near the low end of the range.
- **Persistent short gamma:** FULLY_NEGATIVE regime on 5/14, 5/18, 5/19, 5/21, 5/22, 5/26;
  total_gex −$12.8M to −$46M; ZGL (when present) far below spot at 50–70 [HIST:gex_time_series].
  Structurally high realized vol, dealer-amplified.
- **Term vol is LOW, not rich:** IV30d 44% = **12.9th pctile**, z −0.6, LOW_IV [HIST:iv_percentile_zscore];
  VRP **+0.0716** PREMIUM_SELLING [HIST:vrp]. Only the 5/29 event weekly is expensive.
- **No directional backtest edge:** `dark_pool_accumulation` → **total_signals 0**,
  win_rate_source **null** [HIST:signal_backtest]. Phase-9 falls back to the conviction bin.
- **Vol usually realizes, China peers fell:** `high_iv_rank` vol_realisation **77.8%**,
  n=9, but FUTU −13.0% / TIGR −14.2% in-sample [HIST:signal_backtest] — China-name
  high-IV events recently broke *down*.

## Detailed findings

### IV regime — `[HIST:iv_percentile_zscore]` / `[HIST:vrp]`

- IV30d **0.44**, percentile **12.9**, z **−0.6**, regime **LOW_IV** (dates_used 31).
- Realized σ(30) **0.3683**; VRP **+0.0716** → **PREMIUM_SELLING** (IV > RV by ~7 vol pts).
- **Reconciliation with the 76.5 iv_rank / 98% front-week:** the screener iv_rank and the
  5/29 weekly's 98% IV reflect the *event* vol bid; the constant-maturity IV30d is
  moderate-to-low and points to selling, not buying, vol — beyond the immediate print
  vol is fairly-to-cheaply priced (6/18 49%, 6/26 45%, back ~42% per phase-4).

### Cumulative premium flow (90d) — `[HIST:cumulative_premium_flow]`

- cumulative_bullish $788M vs bearish $320M, net **+$467.7M**, trend BULLISH **— but
  distorted.** ~$542M of that bullish premium is the single **2026-03-19** print (P/C 3.9,
  put_premium $617M, net_flow +$454M — an anomalous one-day institutional put event), and
  the window crosses the data gap. **Strip 3/19 and the recent (May) flow is choppy/
  slightly bearish**, matching the 17/30 bearish-day count. Treat the "BULLISH" 90d label
  as outlier-driven, low-confidence.

### P/C ratio z-score — `[HIST:pc_ratio_zscore]`

- current 0.44 vs 20d mean 0.6398, std 0.299, z **−0.668**, extreme **NORMAL**. Today's
  call-tilt is mildly below the recent mean but **not a sentiment extreme** — no contrarian
  signal either way.

### GEX time series (30d) — `[HIST:gex_time_series]`

- Regime is **unstable day-to-day but recently locked short**: flips logged 4/30, 5/01,
  5/07; the last two weeks are dominated by FULLY_NEGATIVE prints (−$22M to −$46M).
- ZGL, when computed, sits far below spot (50–70) → spot has been deep in negative-gamma
  territory. **This name realizes large, amplified moves** — corroborates the 5.69%
  implied and phase-4's move-amplification read.

### OI trend — `[HIST:oi_trend]`

- **consecutive_build_days 28** — OI built for 28 straight sessions into earnings
  (total_open_interest ~1.0–1.2M); net_oi_change +11,066 today, 350 contracts up vs 97
  down. Steady pre-earnings positioning ramp (not a one-day spike). Today's top builds match
  phase-3 (110C, 94P, 99C, 130C, 150C, plus 5/29 90/92/94P weeklies).

### Multi-day trend table — `[HIST:trend]` (gap-aware: 30 sessions, **hole 03-28→04-24 excluded**)

| Date | Close | Net flow $M | IV rank | P/C | Dir |
|------|-------|-------------|---------|-----|-----|
| 05-26 | 96.58 | +1.12 | 76.5 | 0.44 | bull |
| 05-22 | 94.52 | −1.55 | 65.1 | 0.57 | bear |
| 05-20 | 98.15 | +1.89 | 70.2 | 0.27 | bull |
| 05-15 | 95.88 | −4.59 | 74.8 | 1.15 | bear |
| 05-13 | 99.60 | +0.43 | 90.7 | 0.22 | bull |
| 05-06 | 102.31 | +2.81 | 75.4 | 0.36 | bull |
| 04-27 | 98.47 | +0.02 | 64.6 | 0.81 | bull |
| 03-27 | 99.81 | −0.47 | 28.6 | 1.01 | bear |

Net: choppy, lower highs, drifting from ~102 to ~96.6. IV rank peaked 90.7 (5/13) and has
eased to 76.5. **The pre-earnings ramp has not lifted price — it has bled lower.**

### Signal backtest — `[HIST:signal_backtest]`

- **dark_pool_accumulation** (the phase-2 dominant signal): `{"note":"no backtest results",
  "total_signals":0}` → **win_rate_source = null**.
- **high_iv_rank** (vol regime): **vol_realisation_rate 77.8%**, n=9, avg 5d move **4.84%**.
  In-sample: RDW +49%, SMTC +12%, COLO +7%, plus **FUTU −13.0%, TIGR −14.2%** (China
  brokers down hard), WDAY −2%. The vol almost always realized; **direction skewed down for
  the China names**.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=PDD, lb252 | IV30d 12.9 pctile, LOW_IV, z −0.6 |
| `historical_vrp` | symbol=PDD, rw30 | VRP +0.0716, PREMIUM_SELLING |
| `historical_trend` | symbol=PDD, days30 | 17 bear/13 bull; 102→96.58 drift (gap-crossed) |
| `historical_oi_trend` | symbol=PDD, days30 | 28 consecutive build days; +11,066 today |
| `historical_pc_ratio_zscore` | symbol=PDD, lb20 | z −0.668, NORMAL (no extreme) |
| `historical_gex_time_series` | symbol=PDD, days30 | persistent FULLY_NEGATIVE; ZGL far below spot |
| `historical_cumulative_premium_flow` | symbol=PDD, days90 | net +$467.7M BULLISH — outlier-distorted (3/19) |
| `historical_signal_backtest` | dark_pool_accumulation, 5d | total_signals 0 → null |
| `historical_signal_backtest` | high_iv_rank, 5d | vol_realisation 77.8%, n=9, China peers down |

## Tool errors

None. **Data-quality caveat:** `historical_trend` (days=30) and `cumulative_premium_flow`
(days=90) both span the non-contiguous gap (2026-03-28→04-24 absent). Reported reads use
the **actual sessions present**; the 90d cumulative is additionally distorted by the
2026-03-19 outlier print and is treated as low-confidence.

## Verdict for downstream phases

- **Volatility regime:** **Term vol cheap-to-fair (sell-lean, VRP +7, IV30d 12.9 pctile);
  event-weekly vol RICH and crush-prone (98%).** Net: this is a **premium-selling /
  defined-risk environment**, not a buy-naked-premium one — the event vol must be *sold*
  or harvested, and any long premium must clear the implied 5.69% to win.
- **Premium environment:** PREMIUM-SELLING (VRP > 0) at the term; event vol extremely rich.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5.** The directional
  (accumulation) signal has **no backtest support** (n=0); the multi-week tape is a mild
  *down*-drift; the only in-sample China high-IV analogues (FUTU, TIGR) resolved **down**.
  The vol *magnitude* edge is real (77.8% realization), the *direction* edge is not.
- **Three specific datapoints:** IV30d percentile **12.9** (LOW); VRP **+0.0716**
  (premium-selling); high_iv_rank vol-realisation **77.8%** (n=9).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:               dark_pool_accumulation   # phase-2 dominant directional signal
  signal_backtest_win_rate:   null                     # total_signals 0 — no edge data
  win_rate_n:                 0
  win_rate_source:            null                     # → phase-9 falls back to conviction bin
  # secondary (vol, not directional): high_iv_rank vol_realisation_rate 0.778, n=9
  ```
- **Open questions:** With no directional backtest edge and a mild down-drift, does the
  fundamental/sentiment picture (phase-7b/7c) justify a directional lean at all, or is this
  purely a vol-event to be traded with defined-risk premium-selling? How has PDD *itself*
  reacted to its own past earnings (phase-7b should pull surprise history) — the cross-
  sectional high_iv_rank analogue is not PDD-specific.
