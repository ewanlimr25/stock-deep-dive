# Phase 5 — Historical Context & VRP

**Ticker:** HOOD
**As-of date:** 2026-05-27
**Generated:** 2026-05-28T14:03:50Z
**Upstream phases cited:** phase-0-intake.md, phase-0.5-context.md, phase-3-positioning.md, phase-4-structure.md

## Summary

Today's flow sits inside a **cheap-IV, range-bound, longer-term-downtrend** context.
1-year IV percentile is **15.6 (LOW_IV)** and VRP is **−0.024 (FAIR**, realized 61.2%
slightly above IV 58.8%) — optionality is cheap-to-fair, which *favors buying* premium
if one takes a directional view, even though phase-3/4 show participants *selling* it.
Over the available 30-session window HOOD went essentially **nowhere (74.9 → 76.23,
+1.8%) on 14 bullish vs 16 bearish days**, and dealer GEX has been **persistently
short-gamma with spot stuck below the ZGL** (the 78–80 zone is a recurring ceiling —
spot only printed POSITIVE-gamma regime on the 5/11 and 5/14 local highs of ~81 before
falling back). The bullish_flow signal backtested **90.9%/N=11**, but that is a
**market-wide, in-sample, semis-led-rally** sample (MU, SNDK, NVDA…) — **HOOD is not in
the signal set**, so treat it as a generic class edge, not HOOD's. fz cross-check: HOOD
is **−31% YTD, −49% from its 52-wk high, 25% below its 200-DMA**, RSI neutral 52 — a
beaten-down name bouncing into resistance, not a momentum leader. **Verdict: cheap IV,
choppy/range, edge only weakly positive for HOOD specifically.**

## Key signals

- **IV percentile 15.6 → LOW_IV**, z-score −0.86, IV30d 0.588 (only 32 sessions used)
  [HIST:iv_percentile_zscore] — optionality is cheap.
- **VRP −0.024 → FAIR** (IV 58.8% vs realized 61.2%) [HIST:vrp] — slightly premium-
  *buying* friendly; IV is not overpriced.
- **GEX persistently NEGATIVE/short-γ**, spot below ZGL most of 2 weeks; 78–80 a
  recurring ceiling; FULLY_NEGATIVE on 5/22 (spot 73.63) [HIST:gex_time_series].
- **Cumulative 90d flow MIXED, net −$42.5M** (bullish $1.036B vs bearish $1.078B) over
  the ~33 sessions present [HIST:cumulative_premium_flow] — no stealth accumulation.
- **bullish_flow backtest 90.9% / N=11 / avg +4.09%** — *market-wide, in-sample,
  HOOD absent* [HIST:signal_backtest]; P/C z-score −1.05 NORMAL (no extreme)
  [HIST:pc_ratio_zscore].

## Detailed findings

### IV regime (percentile + z-score + VRP)

- iv-percentile-zscore: current_iv30d **0.588**, **iv_percentile 15.63 (LOW_IV)**,
  z-score −0.862, dates_used **32** (gap-shrunk, *not* 252) [HIST:iv_percentile_zscore].
- VRP: iv30d 0.588 vs realised_vol **0.612** → **vrp −0.0236, regime FAIR** ("IV close
  to realised — no clear edge from VRP alone") [HIST:vrp]. IV is *not* rich; realized is
  marginally higher → debit structures are not being overpaid for.

### Cumulative premium flow (90d / ~33 sessions across the gap)

net_flow **−$42.47M**, trend_direction **MIXED** (cum bullish $1,035.9M vs bearish
$1,078.3M) [HIST:cumulative_premium_flow]. dates_covered confirms the hole (jumps
2026-03-27 → 2026-04-27). No persistent directional accretion — consistent with the
near-balanced single-day tape (phase-1) and choppy day-count.

### P/C ratio z-score (sentiment)

current_pc 0.3625 vs mean 0.4748 (std 0.107) → **z −1.05, NORMAL** (not |z|>2)
[HIST:pc_ratio_zscore]. PC is call-heavier than its 20d mean but **not** at a
contrarian extreme. No fade trigger.

### GEX time series (30d, regime stability) [HIST:gex_time_series]

Highly unstable — **10 regime flips** in the window. Recent trajectory: 5/19 NEG
(zgl 90.5, spot 74.3), 5/20 NEG, 5/21 NEG, **5/22 FULLY_NEGATIVE (gex −$32.9M, spot
73.63)**, 5/26 NEG (zgl 79.85, spot 74.0), **5/27 NEG (zgl 77.85, spot 76.2)**. Spot
has sat **below the ZGL** for nearly the whole window; the only POSITIVE-gamma days
coincided with the 5/11 (80.5) and 5/14 (81.0) local highs — i.e. **price only escapes
short-gamma when it tags ~80–81, then falls back.** This reinforces phase-4: 78–80 is a
structural ceiling, and the regime is amplification-prone (larger ranges), not a calm pin.

### OI trend (buildup) [HIST:oi_trend]

**consecutive_build_days = 30** — total OI grew every session (net_oi_change positive
daily). But the builds are **two-sided** (calls 75–82 *and* puts 69–74 — see phase-3),
so this is rising *engagement/open interest*, not directional accumulation.

### Multi-day trend table [HIST:trend]

date_range 2026-03-18→05-27, **days_analyzed 30**, **bullish_days 14 / bearish_days 16**,
**price_change 74.9 → 76.23 (+1.8%)**, iv_rank_change 22.0 → 23.2 (flat-low),
flow_direction_latest "bullish". IV rank by session: 29.7 (5/14) → 17.6 (5/22) → 23.2
(5/27); PCR 0.30–0.55 (today 0.36). A flat, choppy, low-and-falling-IV grind.

### Price context (fz, advisory — EOD/live cross-check) [HIST:rsi fz][HIST:52w_proximity fz]

> Note: fz `Price` = **78.42**, *above* the UW 5/27 close of 76.23 — fz returns a live
> (next-session, ~2026-05-28) quote. The as-of analysis anchors to **76.23**; the 78.42
> live print means HOOD is **now testing the 78 gamma-flip/ceiling** (phase-4) — an
> advisory heads-up for execution, not part of the as-of read.

- RSI(14) **52.2** — neutral (no oversold-bounce or overbought-exhaustion edge).
- SMA20 **+2.4%**, SMA50 **+2.8%** — price just above short-term MAs (recent stabilization).
- SMA200 **−24.6%** — deep below the 200-DMA → **longer-term downtrend intact**.
- Perf YTD **−30.7%**, Perf Month **−4.5%** — beaten down, still bleeding monthly.
- 52W High 153.86 → **−49.0% from high**; 52W Low 62.92 → **+24.6% above low**.

Read: a fallen fintech (-49% from highs) bouncing within a downtrend, **into** dealer
resistance at 78–80, RSI neutral. This *tempers* any fresh-breakout bullish thesis.

### Signal backtest (current signal's edge) [HIST:signal_backtest]

`bullish_flow`, lookback 5 trading days: **win_rate 90.9%, total_signals 11, avg_move
+4.09%**. **Critical caveats:** (1) signal set = AAPL, AMD, AMZN, AVGO, GOOGL, IWM,
MCHP, META, MSFT, MU, NVDA, PANW, QQQ, RCL, SMH, SNDK, SPY, TSLA, UPS, Z — **HOOD is
absent**; (2) methodology = "in-sample backtest — not a robust live edge"; (3) the
window was a **semis-led rally** (MU +21.5%, SNDK +7.2%); (4) N=11 is small. So this is
the *generic* bullish_flow edge in a strong tape, **not** HOOD's — phase-9 must apply
the N-conditional cap and lean toward the conviction-bin fallback.

## Tool calls (audit trail)

| Command | Result summary |
|---------|----------------|
| `uw historical iv-percentile-zscore --symbol HOOD --lookback-days 252` | IV %ile 15.6 LOW_IV, z −0.86, 32 sessions |
| `uw historical vrp --symbol HOOD --realised-window-days 30` | vrp −0.024 FAIR (IV 0.588 < realized 0.612) |
| `uw historical pc-ratio-zscore --symbol HOOD --lookback-days 20` | z −1.05 NORMAL |
| `uw historical cumulative-premium-flow --symbol HOOD --days 90` | net −$42.5M MIXED, gap-spanning |
| `uw historical gex-time-series --symbol HOOD --days 30 --dte-max 45` | 10 flips; persistently NEG, spot < ZGL |
| `uw historical oi-trend --symbol HOOD --days 30 --top-n 10` | 30 consecutive build days (two-sided) |
| `uw historical trend --symbol HOOD --days 30` | +1.8% px, 14 bull / 16 bear days, IV flat-low |
| `uw historical signal-backtest --signal-type bullish_flow --lookback-days 5 --top-n 50` | 90.9% / N=11, HOOD absent, in-sample |
| `fz quote HOOD --agent` | RSI 52, −25% vs 200DMA, −49% from 52wH, live px 78.42 |

## Tool errors

- `gex-time-series` series is under key `trajectory` (+ `regime_flip_dates`), not
  `series` (first jq cut returned empty). Re-parsed cleanly.
- `trend` daily_data has null `total_volume`/`total_premium` in this build; IV rank +
  PCR populate, and the summary keys (bull/bear days, price_change) resolve the trend.
- **Gap caveat (MANDATORY):** every "30d/90d/252d" window above spans the
  **21-session hole 2026-03-28→04-24**. True N: IV %ile uses **32** sessions, trend
  **30**, cumulative-flow **33**. None annualized across the hole.
- **Latest-anchor caveat:** trailing tools (iv-%ile, pc-z, oi-trend, cum-flow,
  signal-backtest, vrp realized leg) anchor to latest available = 2026-05-27 (= as-of,
  so reproducible *today*; a future session would shift them).

## Verdict for downstream

- **Volatility regime:** **CHEAP** (IV %ile 15.6) / **FAIR VRP** (−0.024) — optionality
  is cheap-to-fair; *if directional, buy premium* rather than sell.
- **Premium environment:** slightly **premium-BUYING** friendly (IV ≤ realized) — though
  note phase-3/4 participants are net *sellers* (range bet on a still-volatile name).
- **Conviction that today's signal is HISTORICALLY EDGE-POSITIVE:** **2/5.** The generic
  bullish_flow class is edge-positive but HOOD didn't fire it; HOOD's own context (mixed
  cum-flow, 16 bear days, persistent short-γ below ceiling, downtrend) is range-bound,
  not edge-rich.
- **Three specific datapoints:** IV %ile **15.6**; VRP **−0.024**; signal win-rate
  **90.9% (N=11, market-wide, HOOD absent — discount heavily)**.
- **Sizing handoff block (phase-9 reads verbatim):**
  ```
  signal_class:              bullish_flow
  signal_backtest_win_rate:  0.909
  win_rate_n:                11
  win_rate_source:           backtest
  win_rate_caveat:           market-wide + in-sample + semis-rally; HOOD NOT in signal set → apply N-conditional cap, prefer conviction-bin fallback
  ```
- **Open questions:**
  - Will the cheap IV + persistent short-gamma resolve into a vol *expansion* (break of
    78 ceiling either way) — what catalyst? (phase-6/7c)
  - With the live print already at 78.42 (testing the flip), is the as-of 76.23 thesis
    about to be overtaken by a regime flip to long-gamma above 78? (phase-9 execution note)
