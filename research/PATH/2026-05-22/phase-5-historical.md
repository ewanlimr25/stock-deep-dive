# Phase 5 — Historical Context & VRP

**Ticker:** PATH (UiPath Inc.)
**As-of date:** 2026-05-22
**Generated:** 2026-05-26T00:00:00Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md, phase-0-intake.md

## Summary

PATH is a **beaten-down small-cap recovering into earnings inside a rich-vol /
premium-selling regime**. Over the **31 sessions actually present** (gap 2026-03-28→04-24
excluded — never annualized), price fell from ~$12.45 (03-18) to a **$9.47 trough (05-13)**
then bounced ~15% to $10.93 (05-22). IV30d is **98.7% — 100th percentile of the available
window** with **VRP +43.7 vol points (PREMIUM_SELLING)**: options price far more vol than
the 55% realized. The dealer-gamma regime is stably **POSITIVE** (one transient flip
05-05), and the negative-GEX pockets on 05-12→05-14 coincided with the price low —
confirming the phase-4 downside-acceleration warning empirically. **On edge:** the
phase-2 `dark_pool_accumulation` signal returns **no backtest sample (null)**, and
`bearish_flow` (phase-1's tilt) **won only 28.6% (N=7)** in this rallying window — so the
bearish sweeps are **not** historically edge-positive. The genuine, repeatable edge here is
**structural (sell the expensive vol), not directional.**

## Key signals

- **VRP +0.4367** (IV30d 98.7% − realized 55.0%) → `PREMIUM_SELLING` [HIST:vrp]
- **IV percentile 100**, z-score 1.599, regime HIGH_IV — but `dates_used=30`, so this is a 30-session percentile, not a true 1y [HIST:iv_percentile_zscore]
- **Price arc:** $12.45 (03-18) → **$9.47 (05-13 low)** → $10.93 (05-22), −12% over window, +15% off the low [HIST:trend]
- **Cumulative premium flow balanced:** bullish $44.97M vs bearish $46.32M, net **−$1.35M** (≈flat), `trend MIXED` — no stealth directional build [HIST:cumulative_premium_flow]
- **bearish_flow backtest win_rate 28.6% (N=7)**; `dark_pool_accumulation` **0 signals (null)**; `high_iv_rank` vol_realisation 60% (N=10) [HIST:signal_backtest]
- **P/C z-score −0.40 (NORMAL)** — today's call-heavy P/C 0.31 is not a sentiment extreme [HIST:pc_ratio_zscore]

## Detailed findings

### IV regime (percentile + z-score + VRP)

IV30d 98.7%, **100th-percentile** over 30 available sessions, z 1.599 → `HIGH_IV`. VRP
**+43.7 vol points** (`PREMIUM_SELLING`): "options pricing more vol than realised." This is
the dominant, reliable read of the phase — combined with phase-4's IV bubble (5/29 140%)
and phase-3's two-sided writing, the environment **strongly favors credit/premium-selling
structures over debit**. Caveat: IV is event-elevated; the "100th percentile" is mostly
the earnings ramp, and it **will crush after 05-28**.

### Cumulative premium flow (window net direction)

Over the 31 sessions: bullish $44.97M vs bearish $46.32M → net **−$1.35M (−1.5% of
~$91M)** = effectively **balanced**, `trend MIXED`. There is **no persistent directional
institutional options build** in either direction — the opposite of a stealth accumulation
campaign. This reinforces that the directional edge is weak and the structural (vol) edge
is the real one.

### P/C ratio z-score (sentiment extreme?)

current 0.31 vs 20-day mean 0.399 (std 0.223) → z **−0.40**, `NORMAL`. Despite today's
call-heavy volume, it is well within the name's normal range — **no contrarian extreme**.

### GEX time series (regime stability)

`regime` POSITIVE on 28 of 30 sessions. Two flips: **05-05 → NEGATIVE** (ZGL spiked to
$11.55 above spot $10.70), **05-06 → back POSITIVE**. total_gex went negative on 04-30
(−$2.6M), 05-12 (−$1.5M), **05-13 (−$9.2M, spot $9.47 — the trough)**, 05-14 (−$6.4M) — i.e.
**the short-gamma pockets aligned with the price low**, empirically validating phase-4's
"below ~$10 the downside accelerates." It then rebuilt to +$29.5M by 05-22. ZGL has hovered
$7–$8 most days (today $7.26), so the long-gamma cushion is stable while spot > ~$10.

### OI trend (buildup vs decay)

`consecutive_build_days 30`, net_oi_change **+10,500** on 05-22 (187 contracts up / 55
down) — OI is **building broadly into earnings**, concentrated in 5/29 puts ($8.5/$9/$9.5)
and calls ($10.5/$13.5) per phase-3. Note total_open_interest is **lower** than March
(~690K now vs ~900K in March) — net positions rolled off over the window, but the *recent*
trend is a fresh pre-earnings build. Consistent with event-positioning, not a long campaign.

### Multi-day trend table (selected)

| Date | Close | iv30d | IV rank | net_flow | dir |
|------|-------|-------|---------|----------|-----|
| 03-18 | 12.45 | 67.0% | 45.0 | +1.31M | bull (window high) |
| 05-13 | **9.47** | 91.2% | 78.1 | −0.57M | bear (**window low**) |
| 05-15 | 10.29 | 95.7% | 85.4 | +1.13M | bull (bounce) |
| 05-21 | 10.57 | 92.4% | 77.8 | −0.18M | bear |
| 05-22 | 10.93 | 98.7% | 84.0 | −0.40M | bear |

17 bearish days vs 13 bullish over the window — a slight bearish daily tilt, but the price
*net recovered* off the low. IV rank climbed steadily (40s → 80s) = the earnings ramp.

### Signal backtest (current signal's historical edge)

| Signal | N | Result | Read |
|--------|---|--------|------|
| `dark_pool_accumulation` (phase-2 dominant) | **0** | no results | **null** — no historical sample; phase-9 falls back to conviction bin |
| `bearish_flow` (phase-1 tilt) | 7 | **win_rate 28.6%** | Below 0.45 → **historically losing**; 5 of 7 (QQQM/IWM/TSLA/AMD/QQQ) rose after the signal. Downgrade any bearish framing |
| `high_iv_rank` (phase-4/5 regime) | 10 | vol_realisation **60%** | High-IV names *did* move 60% of the time → the event will likely realize vol; selling naked vol is not free |

The market-wide context: signals dated 05-19/05-20 were followed by a **broad rally** into
05-22 (AMD +12.9%, TSLA +5.4%, RDW +18–26%), which is why bearish_flow "lost." N is tiny and
not PATH-specific — treat as **directional-edge caution**, not a precise probability.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | `{symbol: PATH, lookback_days: 252}` | IV %ile 100 (dates_used 30), z 1.599, HIGH_IV |
| `mcp__uw-pp__historical_vrp` | `{symbol: PATH, realised_window: 30}` | VRP +0.4367, PREMIUM_SELLING (IV 98.7 vs rv 55.0) |
| `mcp__uw-pp__historical_cumulative_premium_flow` | `{symbol: PATH, days: 90}` | net −$1.35M, MIXED (31 sessions present) |
| `mcp__uw-pp__historical_pc_ratio_zscore` | `{symbol: PATH, lookback: 20}` | z −0.40, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | `{symbol: PATH, days: 30, dte_max: 45}` | POSITIVE 28/30; neg pockets at 05-13 low ($9.47) |
| `mcp__uw-pp__historical_trend` | `{symbol: PATH, days: 30}` | $12.45→$9.47→$10.93; 17 bear/13 bull; IV ramp |
| `mcp__uw-pp__historical_oi_trend` | `{symbol: PATH, days: 30, top_n: 10}` | build_days 30, +10,500 OI today, 187↑/55↓ |
| `mcp__uw-pp__historical_signal_backtest` | `{dark_pool_accumulation / bearish_flow / high_iv_rank, lookback: 10}` | 0 / 28.6% / 60% |

## Tool errors

None. Data-quality note: all `historical_*` windows span the **non-contiguous 31-session
snapshot** (gap 2026-03-28→04-24). Series did **not** silently interpolate across the hole —
`dates_covered` / `dates_used` confirm 30–31 actual sessions, and the gap is reflected as a
date jump, not a smoothed line. The "1y" IV percentile is therefore really a 30-session
percentile (lower confidence on the long-horizon framing).

## Verdict for downstream

- **Volatility regime:** **RICH** — sell premium, not buy it. The 5/29 140% IV will crush
  post-event; favor defined-risk credit structures over long premium.
- **Premium environment:** balanced/mixed flow, no directional build → **the edge is
  structural (VRP), not directional**.
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5 directional**
  (bearish_flow has *negative* historical edge here; DP-accumulation has no sample),
  **3–4/5 structural** (the premium-selling regime is a genuine, repeatable edge).
- **Three specific datapoints:** IV %ile **100** (30-session), VRP **+0.4367**, bearish_flow
  win_rate **28.6%** (N=7).
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              dark_pool_accumulation   (phase-2 dominant; phase-1 bearish_flow noted as caution)
  signal_backtest_win_rate:  null                     (dark_pool_accumulation → 0 signals)
  win_rate_n:                0
  win_rate_source:           null
  ```
  → Phase-9 sizes off the **conviction bin**, not an empirical win-rate (`rubrics/sizing-rubric.md`).
  Cautionary cross-refs: `bearish_flow` win_rate 0.286 (N=7) — argues against a bearish
  directional bet; `high_iv_rank` vol_realisation 0.60 (N=10) — the event will likely move it.
- **Open questions:**
  - In a premium-selling regime with a 6-day-out binary event, is the right expression a
    **defined-risk vol-seller** (iron condor / short strangle inside the implied move) rather
    than a directional bet? → phase-9 structure selection.
  - Does the recovery off $9.47 + DP accumulation + call-skew (phase-4) justify a
    **mildly long** lean through the event, or does the rich VRP cap it to a neutral
    vol-harvest? → phase-7/8 synthesis.
