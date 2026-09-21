# Phase 5 — Historical Context & VRP

**Ticker:** SYM
**As-of date (effective):** 2026-05-21
**Generated:** 2026-05-22T15:13Z
**Upstream phases cited:** phase-1-flow.md, phase-3-positioning.md, phase-4-structure.md

## Summary

SYM is exiting a **3-week negative-gamma drawdown** and snap-back rally:
spot $58.40 → $45.17 (−22.7%) between 2026-04-27 and 2026-05-19, then
$45.17 → $50.95 (+12.8%) in 2 sessions [HIST:gex_time_series + HIST:trend].
**The GEX regime flipped from NEGATIVE → POSITIVE on 2026-05-21 itself**
[HIST:gex_time_series] — phase-4's positive-gamma read is *brand new* and
historically vol-expansion follows regime flips per the tool's own note.
IV30d collapsed from a 2026-05-06 peak of **~100%** (IV rank 60.2) to
today's **63.2%** (IV rank 5.79) — IV is at the **10.34th percentile of the
trailing 1y window** with z-score −1.015 [HIST:iv_percentile_zscore]. VRP
is **FAIR at +2.5 vol pts** (IV 63.2% vs realized 60.7%)
[HIST:vrp] — premium-selling has no statistical edge here; this is NOT a
rich-IV regime. P/C z-score is **NORMAL** (current 0.489 vs 20d mean 0.544,
z −0.178) [HIST:pc_ratio_zscore]. 90d cumulative premium flow is
essentially **balanced** at −$784K net (gross bullish $17.08M vs bearish
$17.86M) — direction is MIXED, not a stealth build [HIST:cumulative_premium_flow].

**This materially refines phase-4:** the "vol-selling" stance from phase-4
needs to be downgraded because IV is at the *bottom* of the 1y window, not
the top. The right read is **post-event reset, mean-reverting under fresh
positive gamma**, not "rich vol to fade."

## Key signals

- **GEX regime just flipped POSITIVE today** (2026-05-21) from NEGATIVE.
  Spot $50.26 vs ZGL $35.19. Single regime flip in the 30-day window
  [HIST:gex_time_series]. Tool note: *"Empirically precedes realised-vol
  expansion."*
- **IV at 10.34th percentile (252d)** — LOW_IV regime, z-score −1.015,
  current IV30d 63.2% [HIST:iv_percentile_zscore]. Down from ~100% just
  15 sessions ago.
- **VRP FAIR (+0.025)** — IV30d 63.2% vs realized 60.7%. *"No clear edge
  from VRP alone"* per tool [HIST:vrp]. Selling vol here is selling cheap
  vol after the event.
- **P/C z-score NORMAL (−0.178)**, no sentiment extreme
  [HIST:pc_ratio_zscore].
- **90d premium flow balanced (net −$784K on $35M gross)**
  [HIST:cumulative_premium_flow]. No directional accumulation in the
  flow tape over the medium term.
- **Latest flow_direction = bearish** on 2026-05-21 (net_flow −$183K)
  [HIST:trend], driven by the bid-side LEAP-call prints from phase-1.
  19 bearish days vs 11 bullish days in the 30-session window.
- **30 consecutive days of net OI builds** [HIST:oi_trend,
  `consecutive_build_days=30`]. Same-day OI Δ +1,703 on 2026-05-21;
  fresh LEAP put add at Jan-27 P42.5 (+93 OI) reinforces the LEAP
  bid-side bearish flow from phase-1.

## Detailed findings

### IV regime

| Metric | Value |
|--------|-------|
| current IV30d | 63.23% |
| IV percentile (252d) | **10.34** |
| IV z-score (252d) | **−1.015** |
| Regime | **LOW_IV** |
| dates_used | 29 (note: 252d window has data gap 2026-03-28 → 2026-04-26 per phase-0) |

Historical IV30d trajectory from `historical_trend` (selected dates):

| Date | Spot | IV30d | IV rank |
|------|------|-------|---------|
| 2026-04-27 | 59.52 | 95.8% | 58.5 |
| 2026-04-30 | 59.11 | 101.7% | 67.5 |
| 2026-05-01 | 58.89 | 100.4% | 65.5 |
| 2026-05-06 | 61.16 | 96.9% | 60.2 |
| 2026-05-08 | 52.27 | 63.0% | 6.5 |
| 2026-05-13 | 49.73 | 68.9% | 17.4 |
| 2026-05-15 | 47.30 | 58.7% | 5.4 |
| 2026-05-19 | 46.62 | 65.4% | 10.0 |
| 2026-05-20 | 49.96 | 64.7% | 9.4 |
| **2026-05-21** | **50.95** | **63.2%** | **5.79** |

**IV collapsed ~38 vol points in 13 trading sessions** (Apr 30 to May 21),
implying a binary event (likely earnings or material news) passed in early
May. Phase-6 must identify what.

### Volatility Risk Premium

| Metric | Value |
|--------|-------|
| IV30d | 63.23% |
| Realized vol (30d) | 60.73% |
| **VRP** | **+0.025 (2.5 vol pts)** |
| Regime | **FAIR** |

Interpretation per tool: *"IV close to realised — no clear edge from VRP
alone."* This is **not a premium-selling regime** by the rubric — the
phase-4 long-gamma read still holds for dealer hedging, but the
*economic* case for selling SYM vol vs realized is neutral, not bullish.

### Cumulative premium flow (90 sessions)

| Metric | Value |
|--------|-------|
| Cumulative bullish premium | $17,080,251 |
| Cumulative bearish premium | $17,864,689 |
| **Net flow** | **−$784,438** |
| Trend direction | **MIXED** |

No stealth institutional build over the medium term. The phase-1 bid-side
LEAP call activity is consistent with this — small bearish skew, not
large enough to dominate.

### P/C ratio z-score

| Metric | Value |
|--------|-------|
| current P/C | 0.4889 |
| 20d mean | 0.5439 |
| 20d std | 0.3083 |
| z-score | −0.178 |
| Extreme flag | **NORMAL** |

Sentiment is unstressed. No contrarian setup from positioning extremes.

### GEX time series (30 days) — **regime flip on 2026-05-21**

| Date | Spot | Regime | total_gex | ZGL |
|------|------|--------|-----------|-----|
| 2026-04-27 | 58.40 | NEGATIVE | 219,863 | 72.27 |
| 2026-04-28 | 56.17 | NEGATIVE | 251,055 | 74.15 |
| 2026-04-29 | 56.92 | NEGATIVE | 37,850 | 69.99 |
| 2026-04-30 | 58.95 | NEGATIVE | 467,437 | 59.28 |
| 2026-05-01 | 58.20 | NEGATIVE | 59,405 | 75.85 |
| 2026-05-04 | 58.26 | NEGATIVE | 492,758 | 72.30 |
| 2026-05-05 | 57.68 | NEGATIVE | 394,500 | 59.62 |
| 2026-05-06 | 60.89 | NEGATIVE | 1,104,340 | 76.05 |
| 2026-05-07 | 57.50 | NEGATIVE | 2,396,293 | 79.07 |
| 2026-05-08 | 52.04 | **FULLY_NEGATIVE** | −1,393,572 | n/a |
| 2026-05-11 | 52.15 | FULLY_NEGATIVE | −629,000 | n/a |
| 2026-05-12 | 50.76 | FULLY_NEGATIVE | −2,423,404 | n/a |
| 2026-05-13 | 49.39 | FULLY_NEGATIVE | −4,209,627 | n/a |
| 2026-05-14 | 49.51 | FULLY_NEGATIVE | −1,526,745 | n/a |
| 2026-05-15 | 47.36 | FULLY_NEGATIVE | **−8,315,373** | n/a |
| 2026-05-18 | 47.05 | POSITIVE† | −5,518,343 | 39.16 |
| 2026-05-19 | 45.17 | FULLY_NEGATIVE | −3,810,591 | n/a |
| 2026-05-20 | 49.42 | NEGATIVE | 15,361,193 | 49.75 |
| **2026-05-21** | **50.26** | **POSITIVE** | **+11,216,424** | **35.19** |

† 2026-05-18 label is "POSITIVE" but total_gex was still −$5.5M — the tool
appears to label by ZGL crossover rather than total sign; the actual
hedging dynamic was still short-gamma.

**Regime flip date:** 2026-05-21, NEGATIVE → POSITIVE.

The drawdown from $58 → $45 happened **inside a negative-gamma regime**
(dealer hedging amplifying down moves). The bounce $45 → $51 in 2 sessions
flipped the regime as customer puts that drove the negative gamma either
expired worthless, were closed, or got delta-disconnected. Phase-3's
finding of put closures (P46, P44.5 closing) on 2026-05-21 corroborates.

### OI trend

| Metric | Value |
|--------|-------|
| consecutive_build_days | **30** |
| net_oi_change (today) | +1,703 |
| contracts_with_increases (today) | 163 |
| contracts_with_decreases (today) | 68 |

Persistent OI accumulation across 30 sessions — the chain has been
*growing* the entire window. Today's top adds:

| Contract | DTE | Strike | OI Δ | Vol |
|----------|-----|--------|------|-----|
| SYM 2026-05-22 C53 | 1 | 53 | +404 | 431 |
| SYM 2026-05-22 C52 | 1 | 52 | +113 | 120 |
| SYM 2027-01-15 C50 | 239 | 50 | +110 | 114 |
| **SYM 2027-01-15 P42.5** | 239 | 42.5 | **+93** | 106 |
| SYM 2026-05-29 C52 | 8 | 52 | +87 | 169 |
| SYM 2026-05-22 C51 | 1 | 51 | +79 | 201 |
| SYM 2026-05-29 C55 | 8 | 55 | +77 | 105 |
| SYM 2026-05-22 C54 | 1 | 54 | +69 | 69 |
| SYM 2026-08-21 C72.5 | 92 | 72.5 | +61 | 61 |

The Jan-27 **P42.5 OI add (+93)** is a new finding not surfaced in
phase-3 (which only saw +100 threshold): it's a **fresh LEAP put hedge**
~16% below spot, consistent with a long-stock institution buying tail
protection at the level just below the negative-GEX air pocket. This
matches the phase-1 LEAP-call bid-side activity — coherent "long stock,
sell upside, hedge downside" footprint.

### Multi-day trend table (30 sessions)

| Date | Close | Net flow | Flow dir | PCR | IV rank |
|------|-------|----------|----------|-----|---------|
| 2026-05-21 | 50.95 | −183K | bearish | 0.49 | 5.79 |
| 2026-05-20 | 49.96 | +17K   | bullish | 0.29 | 9.43 |
| 2026-05-19 | 46.62 | −15K   | bearish | 0.54 | 10.00 |
| 2026-05-18 | 47.05 | −6K    | bearish | 0.45 | 9.47 |
| 2026-05-15 | 47.30 | −552K  | bearish | 0.69 | 5.36 |
| 2026-05-14 | 50.15 | +249K  | bullish | 0.62 | 7.56 |
| 2026-05-13 | 49.73 | −77K   | bearish | 0.29 | 17.38 |
| 2026-05-12 | 51.32 | −70K   | bearish | 0.53 | 16.06 |
| 2026-05-11 | 51.71 | +253K  | bullish | 0.83 | 16.55 |
| 2026-05-08 | 52.27 | −251K  | bearish | 0.54 | 6.53 |
| 2026-05-07 | 56.43 | +109K  | bullish | 0.26 | 12.29 |
| 2026-05-06 | 61.16 | +143K  | bullish | 0.44 | 60.22 |
| 2026-05-05 | 58.03 | +75K   | bullish | 1.32 | 61.11 |
| 2026-05-04 | 57.00 | −470K  | bearish | 1.32 | 62.63 |
| 2026-05-01 | 58.89 | −197K  | bearish | 0.41 | 65.47 |
| 2026-04-30 | 59.11 | −5K    | bearish | 0.53 | 67.52 |
| 2026-04-29 | 57.35 | −4K    | bearish | 0.38 | 67.07 |
| 2026-04-28 | 57.08 | −952K  | bearish | 0.46 | 62.82 |
| 2026-04-27 | 59.52 | −99K   | bearish | 0.33 | 58.54 |

Note the data gap 2026-04 → 2026-03-27 (phase-0 flagged). Sessions before
that show SYM in the ~$50–$53 range with normal-ish IV ranks 19–29.

**The shape of the move:** ~$50 in mid-March, ran up to ~$60 by early
May with IV ranks hitting 60+, then crashed back to $45 with IV
collapsing. Today's $50.95 close puts SYM **almost exactly back where
it started in March**, but with IV at the 1y low — a complete
event-driven round trip.

### Signal backtest

- `signal_type=dark_pool_accumulation`: **zero historical signals
  returned** in this dataset. Either the signal classifier didn't fire
  recently or has a small universe — cannot derive a SYM-specific win
  rate.
- `signal_type=high_iv_rank`: 20 cross-sectional signals, vol
  realisation rate 70%, avg 5d move 4.05%. Not SYM-specific; only
  marginally relevant (and notably, SYM today is LOW_IV not high — so
  this backtest isn't the right comparator anyway).

**No directly-applicable signal backtest fired for SYM.** Phase-9 has
to lean on first-principles structure rather than a quantified historical
win rate.

## Tool calls (audit trail)

| Tool | Args | Result summary |
|------|------|----------------|
| `historical_iv_percentile_zscore` | symbol=SYM, lookback-days=252 | IV %ile 10.34, z −1.015, LOW_IV |
| `historical_vrp` | symbol=SYM, realised-window-days=30 | vrp +0.025, FAIR |
| `historical_cumulative_premium_flow` | symbol=SYM, days=90 | net −$784K on $35M gross, MIXED |
| `historical_pc_ratio_zscore` | symbol=SYM, lookback-days=20 | z −0.178, NORMAL |
| `historical_gex_time_series` | symbol=SYM, days=30, dte-max=45 | 1 regime flip on 2026-05-21 (NEG→POS) |
| `historical_oi_trend` | symbol=SYM, days=30, top-n=10 | 30 consecutive build days, +1,703 today |
| `historical_trend` | symbol=SYM, days=30 | 19 bearish / 11 bullish days |
| `historical_signal_backtest` | signal-type=dark_pool_accumulation | 0 signals |
| `historical_signal_backtest` | signal-type=high_iv_rank | 20 signals (other tickers), 70% vol-realisation |

## Tool errors

None.

## Verdict for downstream phases

- **Bias from this phase:** **post-event mean-reversion long bias** —
  vol-crush has finished, gamma flipped positive today, OI is rebuilding,
  no sentiment extreme either way. Premium tape is mildly bearish but
  not stealth-distributive.
- **Conviction:** 3/5. Strong signals (IV %ile 10, regime flip today) but
  the lack of a SYM-specific backtest and the 30d data gap inside the
  252d window cap conviction.
- **Three specific data points for phase-9:**
  1. **IV %ile 10.34** [HIST:iv_percentile_zscore] — **vol is cheap**.
     Long-vol or long-premium structures are funded; short-premium is
     not edge-positive.
  2. **GEX regime flipped today** [HIST:gex_time_series] — historically
     precedes realized-vol expansion. Don't sell vol just because dealers
     are long gamma; the regime is FRESH and could revert.
  3. **VRP +2.5 vol pts = FAIR** [HIST:vrp] — no statistical case for
     credit-spread/iron-condor structures purely on the carry. Phase-4's
     "vol-rich" lean is invalidated by the historical context.
- **Open questions:**
  - Phase-6: what is the catalyst that drove the IV 100% → 63% collapse
    in early May? Earnings on or around 2026-05-07? Customer / regulatory
    news? Knowing this changes whether the round-trip is "old news, move
    on" or "stage-1 of a larger move."
  - Phase-7: does `insights_signal_confluence` corroborate the long-bias
    despite the bearish phase-1 LEAP flow?
  - Will the fresh GEX regime flip hold for the next 5 sessions, or
    revert toward negative as new LEAP-put OI (P42.5 +93 today) builds
    short-gamma exposure on the downside?
