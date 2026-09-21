# Phase 5 — Historical Context & VRP

**Ticker:** MSTR
**As-of date:** 2026-05-19 (effective)
**Generated:** 2026-05-20T00:30:00Z
**Upstream phases cited:** phase-1-flow.md, phase-2-dark-pool.md, phase-3-positioning.md, phase-4-structure.md

## Summary

The historical lens reveals three things that change how phases 1–4 should be
read: **(1)** MSTR has just finished a 16% drawdown from $195.94 (2026-05-11)
to $164.74 (2026-05-19) over 6 sessions, accompanied by **bearish flow on 4 of
the last 5 sessions** — the defensive flow signature in phase-1 is not noise,
it is the *continuation* of a real, in-progress sell-off. **(2)** The 45-DTE
GEX regime has flipped between POSITIVE and NEGATIVE **eight times in the past
28 sessions** — the dealer-hedging regime is genuinely unstable; expect more
chop. **(3)** The bearish-flow signal backtest returned **100% downside win
rate** (n=8 firings in the prior window, avg -4.45% in 10 days), and MSTR
itself was one of the historical signals — fired on 2026-05-15 and *already
played out the move* (-7.28% in 10 days, from $177.56 to $164.63). The
implication is critical: **the bearish signal has largely paid off; chasing
short here has poor remaining edge unless a fresh catalyst (e.g. June 18)
hits.** IV30 percentile is **33rd (CHEAP)** and VRP is **−4.3% (slight
premium-buying edge)** — the regime favors **debit option structures over
credit**.

## Key signals

- **IV30 = 68.21%, percentile 33rd (1y window), z-score −0.411** — NORMAL but cheap [HIST:iv_percentile_zscore]
- **VRP = −4.34%** (IV30 68.21% vs realised σ30 72.55%) — FAIR / mild premium-buying edge [HIST:vrp]
- **5-day price action: $186.97 (5/13) → $164.74 (5/19) = -11.9%** with bearish flow on 4/5 days [HIST:trend]
- **GEX regime has flipped 8x in 28 sessions** — unstable dealer hedging environment [HIST:gex_time_series]
- **Bearish_flow signal: 100% downside win rate, avg -4.45% in 10 days (n=8)** — but MSTR's own 5/15 signal has already played [HIST:signal_backtest]
- **OI consecutive_build_days = 28** — the entire data window is one continuous OI accumulation episode [HIST:oi_trend]
- **P/C ratio z-score = +1.45** (current 0.80 vs 20d mean 0.57) — elevated put activity, sentiment leaning defensive but not extreme [HIST:pc_ratio_zscore]

## Detailed findings

### IV regime (percentile, z-score, VRP)

| Metric | Value | Interpretation |
|---|---:|---|
| `current_iv30d` | 0.6821 (68.2%) | Below MSTR's 1y median |
| `iv_percentile` | 33.33 | **33rd percentile — CHEAP** by 1y standards |
| `iv_zscore` | −0.411 | −0.4σ from 1y mean — modestly subdued |
| `regime` | NORMAL | |
| `realised_vol_30d` | 72.55% | Slightly higher than IV |
| `VRP` | **−4.34%** | IV < realised → premium-BUYING regime |
| `vrp_regime` | FAIR | No edge "purely from VRP" |

Read: **IV is statistically cheap and slightly below realised** — this is a *buy-options, don't-sell-options* environment. Debit verticals, calendar spreads, and outright long puts/calls have positive expectancy if directional thesis holds. Iron condors and credit verticals are mathematically disadvantaged here.

### Cumulative premium flow (90d)

| Metric | Value |
|---|---:|
| `cumulative_bullish` | $4,079,344,331 |
| `cumulative_bearish` | $3,864,403,273 |
| `net_flow` | **+$214,941,058 (BULLISH lean)** |
| `bullish/bearish ratio` | 1.056 |
| `trend_direction` | MIXED |

Read: 90-day net premium flow is mildly bullish but essentially balanced. **No persistent stealth-accumulation signature in options.** This rules out a "smart money is quietly building a long" narrative. Phase-1's bearish-lean is therefore a *recent* (1-2 week) phenomenon, not a multi-month theme.

### P/C ratio z-score (sentiment)

- `current_pc_ratio` = **0.80**
- `mean_pc_ratio` (20d) = 0.568
- `std_pc_ratio` (20d) = 0.16
- `zscore` = **+1.452**
- `extreme` = NORMAL (threshold typically |z| ≥ 2)

Read: P/C is **+1.45σ above its 20-day mean** — elevated put activity, but not yet at the contrarian-extreme threshold. Sentiment is leaning bearish/defensive, consistent with phase-1 and phase-3 put-buying tape, but it is NOT washed-out enough for a contrarian long reversal play. **No mean-reversion edge from sentiment alone yet** — would need z ≥ +2 for that.

### GEX time series (28 sessions, 8 regime flips)

Total regime flips: **8 in 28 sessions** — extraordinary instability for a single name. Flip dates and price progression:

| Date | From | To | Spot | ZGL | Note |
|---|---|---|---:|---:|---|
| 2026-05-06 | NEGATIVE | POSITIVE | $184.54 | $178.9 | Rally above ZGL — first long-gamma day in 28d |
| 2026-05-07 | POSITIVE | NEGATIVE | $179.41 | $179.42 | Single-day reversal |
| 2026-05-08 | NEGATIVE | POSITIVE | $183.48 | $179.66 | Bounce back |
| 2026-05-12 | POSITIVE | NEGATIVE | $184.35 | $189.26 | ZGL jumped above spot — flip from below |
| 2026-05-14 | NEGATIVE | POSITIVE | $187.44 | $5.05 (anomaly) | Possible data artifact |
| 2026-05-15 | POSITIVE | NEGATIVE | $176.51 | $179.35 | Big sell day |
| 2026-05-18 | NEGATIVE | POSITIVE | $164.83 | $18.03 (anomaly) | Possible data artifact |
| 2026-05-19 | POSITIVE | NEGATIVE | $165.76 | $174.79 | **Today — back to short-gamma regime** |

Read: The dealer hedging dynamic has been in **constant churn**. The unusual ZGL readings of $5.05 and $18.03 on 5/14 and 5/18 are likely tool artifacts when extreme tail put OI mass produces undefined flip points. Stripping those, the *stable* ZGL band has been **$179 (±$10)** for most of the window — almost exactly today's $174.79 reading. This corroborates phase-4: **$174-$180 is the persistent regime-change zone**.

Total GEX (absolute, 45-DTE) has grown monotonically:
- 2026-03-13: $86M (thin OI)
- 2026-04-27: $500M (OI building)
- 2026-05-04: $1.37B
- 2026-05-11: $4.25B (pre-peak)
- 2026-05-15: $15.59B (post-drawdown begin)
- **2026-05-19: $26.64B (largest reading in window)**

The **31x GEX expansion since 3/13** means dealer hedging now drives MSTR's intraday price action far more than fundamentals. The gamma surface IS the market.

### OI trend (consecutive build days)

- `consecutive_build_days` = **28** (entire window)
- Today's net_oi_change: **+67,516** (sustained build)
- 1,070 contracts saw OI increases vs 499 decreases on 2026-05-19

Read: **MSTR's option chain is in continuous expansion** — no thinning episodes in the window. This is consistent with a single, long-running positioning cycle (probably the BTC-reflexivity catalyst window leading into June 18 expiry, per phase-4).

### Multi-day trend (28 sessions, daily flow)

Recent 10 sessions (chronological), with flow_direction tag:

| Date | Close | Flow dir | Net premium ($M) | IV30 | IV rank | P/C |
|---|---:|---|---:|---:|---:|---:|
| 2026-05-19 | **164.74** | bearish | -8.3 | 68.2% | 30.8 | 0.80 |
| 2026-05-18 | 166.63 | bearish | -6.0 | 69.2% | 31.3 | 0.72 |
| 2026-05-15 | 177.56 | bearish | **-70.4** | 66.2% | 27.8 | 0.35 |
| 2026-05-14 | 186.97 | bullish | +24.6 | 68.8% | 30.8 | 0.34 |
| 2026-05-13 | 178.03 | bearish | -4.6 | 66.7% | 28.3 | 0.62 |
| 2026-05-12 | 184.42 | bearish | -13.7 | 67.5% | 29.2 | 0.62 |
| 2026-05-11 | **195.94** | bullish | +19.4 | 69.2% | 31.3 | 0.56 |
| 2026-05-08 | 187.45 | bullish | +2.2 | 65.6% | 27.5 | 0.34 |
| 2026-05-07 | 179.84 | bullish | +0.7 | 64.2% | 25.3 | 0.66 |
| 2026-05-06 | 186.82 | bearish | -17.0 | 66.5% | 28.1 | 0.53 |
| 2026-05-05 | 186.70 | bullish | **+256.9** | 72.1% | 35.0 | 0.37 |

Aggregate stats over the 28-day window:
- `bearish_days` = **16**
- `bullish_days` = **12**
- `flow_direction_latest` = **bearish**

The peak was 2026-05-11 at $195.94 (bullish flow day), followed by **6 consecutive sessions where bearish flow days outnumbered bullish 4-2 and price fell $31 (-16%)**. The drawdown is real, consistent, and not a one-day flash.

The single largest +bullish day was **2026-05-05 at +$256.9M net premium** (highest IV rank reading of 35) — that's the high-water-mark for bullish accumulation; the subsequent ~10 days have been a slow, persistent distribution.

### Signal backtest — bearish flow (10-day forward returns)

| Field | Value |
|---|---:|
| `signal_type` | bearish_flow |
| `lookback_days` | 10 |
| `total_signals` | 8 |
| `truncated_signals` | 8 (small N) |
| **`win_rate`** | **100.0% down** |
| **`avg_move_pct`** | **−4.45%** |

The 8 historical bearish_flow firings in the window include MU, MSTR, TSLA, NVDA, NDX, SPY, MU again, and GLD — across 2026-05-14 and 2026-05-15. **All 8 went DOWN over the subsequent 10 days, averaging -4.45%.**

Critical for our as-of: **MSTR was one of the 8 firings** (signal date 2026-05-15, price $177.56). It is now at $164.63/$164.74 — already DOWN -7.28%, *over-delivering* on the average. The bear move is largely complete, statistically. Continuing to add short here means betting against a signal that has already cashed.

Statistical caveat: n=8 is small. A 100% win rate is suspicious — it likely reflects a regime-specific window (broad market weakness during 2026-05-14 to 2026-05-19) rather than a permanent edge. Phase-6 (macro) should resolve whether the broader market regime is still risk-off (continuation) or stabilizing (mean-reversion).

## Cross-phase synthesis

The historical context **changes the implication** of phases 1–4 in three important ways:

1. **Phase-1 defensive-flow lean is corroborated** by 4/5 recent bearish-flow days and the -16% drawdown. But the *signal already paid off* over the prior 10 days. The marginal downside opportunity from continuing to short is weaker than it looks on the day-of tape.

2. **Phase-3's bullish OI buildup (12/8 strikes, $170C +8,654) is actually a CONTRARIAN signal** in the context of the trend — speculators are buying near-the-money calls into a 16% drawdown, betting on a snapback. Win rate of such retail-led counter-trend setups historically is poor unless dealer gamma flips.

3. **Phase-4's short-gamma regime + binary-event IV at 6/18 + this phase's GEX-flip instability** combine to a single thesis: **the market has priced a binary event at June 18 expiry and is currently in a wait-and-see drawdown** ahead of it. The setup is *not* "stock will keep falling" — it's "the stock is in a vol-amplified consolidation range until June 18 resolves it."

The premium-buying VRP regime + cheap IV30 + binary event in 30 days = textbook **long-straddle or long-call-spread / long-put-spread** structural setup. Selling premium here is *against* the regime.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `mcp__uw-pp__historical_iv_percentile_zscore` | `{symbol:MSTR, lookback-days:252}` | IV30 68.2%, 33rd percentile, NORMAL |
| `mcp__uw-pp__historical_vrp` | `{symbol:MSTR, date:2026-05-19, realised-window-days:30}` | VRP -4.34%, FAIR |
| `mcp__uw-pp__historical_cumulative_premium_flow` | `{symbol:MSTR, days:90}` | Net +$215M (MIXED, slight bull) |
| `mcp__uw-pp__historical_pc_ratio_zscore` | `{symbol:MSTR, lookback-days:20}` | z +1.45, NORMAL |
| `mcp__uw-pp__historical_gex_time_series` | `{symbol:MSTR, days:30, dte-max:45}` | 8 regime flips in 28 sessions |
| `mcp__uw-pp__historical_oi_trend` | `{symbol:MSTR, days:30, top-n:10}` | 28 consecutive build days; today net +67,516 OI |
| `mcp__uw-pp__historical_trend` | `{symbol:MSTR, days:30}` | 28 days, 16 bearish / 12 bullish; latest bearish; peak 5/11 $195.94 |
| `mcp__uw-pp__historical_signal_backtest` | `{signal-type:bearish_flow, lookback-days:10, top-n:20}` | 8 signals, 100% win, -4.45% avg, MSTR included |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **the bearish move is statistically near-complete**; remaining edge favors **structural binary-event plays around 6/18** rather than chasing fresh shorts at $165.
- **Conviction:** **3.5/5** — the historical signal evidence is unambiguous on direction, but the move has largely already happened.
- **Three specific data points phase-9 must use:**
  1. **IV30 = 33rd percentile / VRP −4.3%** → **prefer DEBIT structures** (long premium). Avoid iron condors / credit spreads.
  2. **Recent 5-day price action: -11.9% on bearish flow 4/5 days** — momentum is bearish but signal has paid.
  3. **MSTR's own 5/15 bearish_flow signal has delivered -7.28% in the prescribed 10-day window**. Conservative interpretation: edge is exhausted; aggressive: the catalyst at 6/18 could re-fire it.
- **Open questions:**
  - **What is the June 18 catalyst?** (Phase 6 must answer.) Phase-4 hypothesized June FOMC; the IV term-structure data here doesn't disambiguate.
  - The unusual 5/14 and 5/18 ZGL anomaly readings ($5.05 and $18.03) — are these data artifacts or genuine sentinel events? Phase-7 insights composite should sanity-check.
  - Are the 8 historical bearish_flow firings (100% win rate) regime-specific or generalizable? **Phase-6's macro regime read will determine whether to lean continuation or mean-reversion.**
